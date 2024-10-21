# pylint: disable=line-too-long
"""The dpojet commands module.

These commands are used in the following models:
DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7KC, DSA70KC, DSA70KD, MSO5KB, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DPOJET:ACTIVATE
    - DPOJET:ADDMeas {PERIod | CCPeriod | FREQuency | NPERiod | PWIdth | NWIdth | PDUTy | NDUTy | PCCDuty | NCCDuty | DATARATE | TIE | RJ | RJDirac | TJber | DJ | DJDirac | PHASENoise | DCD | DDJ | PJ | J2 | J9 | SRJ | PJrms | SJFREQ | PKPKCLKTJ | PKPKCLKRJ | PKPKCLKDJ | PJRMS | FN | RJH | RJV | PJH | PJV | RN | RNV| RNH | DN | DDN | DDN_1 | DDN_0 | PN | PNV | PNH | NPN | TNBER | NOISESUMMARY | UNITAMPLITUDE | RISEtime | SETup | HIGHTime | FALLtime | HOLD | LOWTime | SKEW | GATEDSKEW | HEIght | WIDth | MASKHits | WIDTHBer | HEIGHTBer |CYCLEMIN | CYCLEMAX | ACRMS | ACCOMmonmode | COMmonmode | HIGH | TNTratio | HIGHLOW | LOW | VDIFFxovr | RISESLEWrate | FALLSLEWrate | OVERShoot | UNDERShoot | CYCLEPktopk | JITTERSummary | PCIETTXDiffpp | PCIEDEemph | PCIETTx | PCIETTXRise | PCIETTXFall | PCIEUI | PCIETMinpulse | PCIEMEdmxjitter | PCIETRfmismch | PCIESSCFReqdev | PCIEMAXMINratio | PCIESSCPROFile | PCIEVEye | PCIETTXUTJ | PCIETTXUDJDD | PCIETTXUPWTJ | PCIETTXUPWDJDD | PCIETTXDDJ | PCIEVTXBOOST | PCIEVTXNOEQ | PCIEVTXEIEOS | PCIEPS21TX | PCIEACCommonmode | VTXDiffpp | TMINPULSETJ | TCDRslewmax | USBUI | USBACCommonmode | TMINPULSEDJ | QFACTOR | EYELOW | EYEHIGH | TCMDTOCMD | TIMEOUTSIDELEVEL | SSCFREQDEVMAX | SSCFREQDEVMIN | SSCFREQDEV |SSCMODrate | SSCPROfile | USBSSCFREQDEVMAX | USBSSCFREQDEVMIN | USBSSCMODrate | USBSSCPROFile | AUTOFITMaskhits | AOP | EXRATIO | OMA | OPTHIGH | OPTLOW| EYECROSSLEVEL | EYECROSSTIME | EYECROSSPERCENT | DFEEW | DFEEH | DFEEYEDIAGRAM | VWOE | MASKMARGIN | MASKHITRATIO | RIN | RINXOMA | TDEC }
    - DPOJET:ADDPlot {TIMEtrend | DATAarray | HISTOgram | SPECtrum | TRANSfer | PHASEnoise | EYE | WAVEform | BATHtub | QBathtub | QPulsewidth | COMPOSITEJitterhist | NOISEBAthtub | BERContour | CORRELATEDEye |PDFEye | BEREye | COMPOSITENoisehist}, MEAS<x>
    - DPOJET:ANALYSISMETHOD { JITTEROnly | JITTERNoise }
    - DPOJET:ANALYSISMETHOD?
    - DPOJET:APPLYAll {FILTers | CLOCKRecovery| RJDJ}, MEAS<x>
    - DPOJET:BITRatestate {0|1}
    - DPOJET:BITRatestate?
    - DPOJET:CLEARALLMeas
    - DPOJET:CLEARALLPlots
    - DPOJET:DATAratelimits  <NR3>
    - DPOJET:DATAratelimits?
    - DPOJET:DESKEW {EXEcute}
    - DPOJET:DESKEW:DESKEWHysteresis  <NR3>
    - DPOJET:DESKEW:DESKEWHysteresis?
    - DPOJET:DESKEW:DESKEWMidlevel  <NR3>
    - DPOJET:DESKEW:DESKEWMidlevel?
    - DPOJET:DESKEW:DESKEWchannel {CH<x>}
    - DPOJET:DESKEW:DESKEWchannel?
    - DPOJET:DESKEW:EDGE {RISE | FALL | BOTH}
    - DPOJET:DESKEW:EDGE?
    - DPOJET:DESKEW:MAXimum  <NR3>
    - DPOJET:DESKEW:MAXimum?
    - DPOJET:DESKEW:MINimum  <NR3>
    - DPOJET:DESKEW:MINimum?
    - DPOJET:DESKEW:REFChannel {CH1 - CH4}
    - DPOJET:DESKEW:REFChannel?
    - DPOJET:DESKEW:REFHysteresis  <NR3>
    - DPOJET:DESKEW:REFHysteresis?
    - DPOJET:DESKEW:REFMidlevel  <NR3>
    - DPOJET:DESKEW:REFMidlevel?
    - DPOJET:DESKEW?
    - DPOJET:DIRacmodel {FIBREchannel | PCIExpress}
    - DPOJET:DIRacmodel?
    - DPOJET:EXPORT {PLOT<x>, <file string>}
    - DPOJET:EXPORTRaw {PLOT<x>, <file string>}
    - DPOJET:GATING {OFF | ZOOM | CURSOR | MARKS}
    - DPOJET:GATING?
    - DPOJET:HALTFreerunonlimfail {1 | 0}
    - DPOJET:HALTFreerunonlimfail?
    - DPOJET:HIGHPerfrendering  <NR1>
    - DPOJET:HIGHPerfrendering?
    - DPOJET:INTERp {LINear | SINX}
    - DPOJET:INTERp?
    - DPOJET:JITtermode?
    - DPOJET:JITtermodel {BUJ | Legacy}
    - DPOJET:JITtermodel?
    - DPOJET:LASTError?
    - DPOJET:LIMITRise {1 | 0}
    - DPOJET:LIMITRise?
    - DPOJET:LIMits:FILEName  <string>
    - DPOJET:LIMits:FILEName?
    - DPOJET:LIMits:STATE {1 | 0}
    - DPOJET:LIMits:STATE?
    - DPOJET:LOCKRJ {1 | 0 }
    - DPOJET:LOCKRJ?
    - DPOJET:LOCKRJValue  <NR3>
    - DPOJET:LOCKRJValue?
    - DPOJET:LOGging:MEASurements:FOLDer  <string>
    - DPOJET:LOGging:MEASurements:FOLDer?
    - DPOJET:LOGging:MEASurements:STATE {1 | 0}
    - DPOJET:LOGging:MEASurements:STATE?
    - DPOJET:LOGging:SNAPshot {STATistics | MEASurements}
    - DPOJET:LOGging:STATistics:FILEName  <string>
    - DPOJET:LOGging:STATistics:FILEName?
    - DPOJET:LOGging:STATistics:STATE {1 | 0}
    - DPOJET:LOGging:STATistics:STATE?
    - DPOJET:LOGging:WORSTcase:FOLDer  <string>
    - DPOJET:LOGging:WORSTcase:FOLDer?
    - DPOJET:LOGging:WORSTcase:STATE {1 | 0}
    - DPOJET:LOGging:WORSTcase:STATE?
    - DPOJET:MEAS<x>:BER:TARGETBER  <NR3>
    - DPOJET:MEAS<x>:BER:TARGETBER?
    - DPOJET:MEAS<x>:BITCfgmethod {MEAN | MODE}
    - DPOJET:MEAS<x>:BITCfgmethod?
    - DPOJET:MEAS<x>:BITConfig:ABSRELstate {0|1}
    - DPOJET:MEAS<x>:BITConfig:ABSRELstate?
    - DPOJET:MEAS<x>:BITConfig:ENDPercent  <NR3>
    - DPOJET:MEAS<x>:BITConfig:ENDPercent?
    - DPOJET:MEAS<x>:BITConfig:NUMBins  <NR3>
    - DPOJET:MEAS<x>:BITConfig:NUMBins?
    - DPOJET:MEAS<x>:BITConfig:STARTPercent  <NR3>
    - DPOJET:MEAS<x>:BITConfig:STARTPercent?
    - DPOJET:MEAS<x>:BITPcnt  <NR3>
    - DPOJET:MEAS<x>:BITPcnt?
    - DPOJET:MEAS<x>:BITType {ALLBits | NONTRANsition | TRANsition}
    - DPOJET:MEAS<x>:BITType?
    - DPOJET:MEAS<x>:BUSState:CLOCKPolarity {RISING | FALLING}
    - DPOJET:MEAS<x>:BUSState:CLOCKPolarity?
    - DPOJET:MEAS<x>:BUSState:FROMPattern  <string>
    - DPOJET:MEAS<x>:BUSState:FROMPattern?
    - DPOJET:MEAS<x>:BUSState:FROMSymbol  <string>
    - DPOJET:MEAS<x>:BUSState:FROMSymbol?
    - DPOJET:MEAS<x>:BUSState:MEASUREFrom {CLOCKEdge | START | STOP}
    - DPOJET:MEAS<x>:BUSState:MEASUREFrom?
    - DPOJET:MEAS<x>:BUSState:MEASURETO {START | STOP | CLOCKEdge}
    - DPOJET:MEAS<x>:BUSState:MEASURETO?
    - DPOJET:MEAS<x>:BUSState:MEASUREType {SYMbol | PATTern}
    - DPOJET:MEAS<x>:BUSState:MEASUREType?
    - DPOJET:MEAS<x>:BUSState:TOPattern  <string>
    - DPOJET:MEAS<x>:BUSState:TOPattern?
    - DPOJET:MEAS<x>:BUSState:TOSymbol  <string>
    - DPOJET:MEAS<x>:BUSState:TOSymbol?
    - DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard  <string>
    - DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard?
    - DPOJET:MEAS<x>:CLOCKRecovery:BWType {LOOPBW | JTFBW}
    - DPOJET:MEAS<x>:CLOCKRecovery:BWType?
    - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate  <NR3>
    - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate?
    - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency  <NR3>
    - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency?
    - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier  <NR3>
    - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier?
    - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath  <string>
    - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath?
    - DPOJET:MEAS<x>:CLOCKRecovery:DAMPing  <NR3>
    - DPOJET:MEAS<x>:CLOCKRecovery:DAMPing?
    - DPOJET:MEAS<x>:CLOCKRecovery:DATARate {1 | 0}
    - DPOJET:MEAS<x>:CLOCKRecovery:DATARate?
    - DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth  <NR3>
    - DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth?
    - DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate {FIRST | EVERY}
    - DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate?
    - DPOJET:MEAS<x>:CLOCKRecovery:METHod {STANDARD | CUSTOM | CONSTMEAN | CONSTFIXED | EXPEDGE | EXPPLL | CONSTMEDIAN | BEHAVIORAL}
    - DPOJET:MEAS<x>:CLOCKRecovery:METHod?
    - DPOJET:MEAS<x>:CLOCKRecovery:MODel {ONE | TWO}
    - DPOJET:MEAS<x>:CLOCKRecovery:MODel?
    - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset  <NR3>
    - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:AUTO?
    - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual  <NR3>
    - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual?
    - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype {FIRST | EVERY}
    - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype?
    - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype {AUTO | MANUAL}
    - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype?
    - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset?
    - DPOJET:MEAS<x>:CLOCKRecovery:PATTern {1 | 0}
    - DPOJET:MEAS<x>:CLOCKRecovery:PATTern?
    - DPOJET:MEAS<x>:CLOCKRecovery:STAndard  <string>
    - DPOJET:MEAS<x>:CLOCKRecovery:STAndard?
    - DPOJET:MEAS<x>:COMMONMode:FILTers:STATE {ON | OFF}
    - DPOJET:MEAS<x>:COMMONMode:FILTers:STATE?
    - DPOJET:MEAS<x>:CUSTOMGATING:FROMedge {RISe | FALL | BOTH}
    - DPOJET:MEAS<x>:CUSTOMGATING:FROMedge?
    - DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge {FIRST | ALL}
    - DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge?
    - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE {GATE1 | GATE2 | GATE3 GATE4 | GATE5 | GATE6 | GATE7 | GATE8 | GATE9 | GATE10 | GATE11 | GATE12 | GATE13 | GATE14 | GATE15 | GATE16 | NONE}
    - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE?
    - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE {GATE1 | GATE2 | GATE3 GATE4 | GATE5 | GATE6 | GATE7 | GATE8 | GATE9 | GATE10 | GATE11 | GATE12 | GATE13 | GATE14 | GATE15 | GATE16 | NONE }
    - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE?
    - DPOJET:MEAS<x>:CUSTOMGATING:TOedge {RISe | FALL | BOTH}
    - DPOJET:MEAS<x>:CUSTOMGATING:TOedge?
    - DPOJET:MEAS<x>:CUSTomname  <string>
    - DPOJET:MEAS<x>:CUSTomname?
    - DPOJET:MEAS<x>:DATA?
    - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState {0 | 1 | ON | OFF}
    - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState?
    - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue  <NR3>
    - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue?
    - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState {0 | 1 | ON | OFF}
    - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState?
    - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue  <NR3>
    - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue?
    - DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION {MANUAL,AUTO}
    - DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION?
    - DPOJET:MEAS<x>:DFE:MANUALDELAY  <NR3>
    - DPOJET:MEAS<x>:DFE:MANUALDELAY?
    - DPOJET:MEAS<x>:DFE:MEASatpercent  <NR3>
    - DPOJET:MEAS<x>:DFE:MEASatpercent?
    - DPOJET:MEAS<x>:DFE:RESOlution  <NR3>
    - DPOJET:MEAS<x>:DFE:RESOlution?
    - DPOJET:MEAS<x>:DFE:TAPState {0|1}
    - DPOJET:MEAS<x>:DFE:TAPState?
    - DPOJET:MEAS<x>:DFE:TAPValue  <NR3>
    - DPOJET:MEAS<x>:DFE:TAPValue?
    - DPOJET:MEAS<x>:DISPLAYNAME?
    - DPOJET:MEAS<x>:EDGE1 {RISe | FALL | BOTH}
    - DPOJET:MEAS<x>:EDGE1?
    - DPOJET:MEAS<x>:EDGE2 {RISe | FALL | BOTH}
    - DPOJET:MEAS<x>:EDGE2?
    - DPOJET:MEAS<x>:EDGEIncre  <NR3>
    - DPOJET:MEAS<x>:EDGEIncre?
    - DPOJET:MEAS<x>:EDGES:EYEHeightstate {1 | 0}
    - DPOJET:MEAS<x>:EDGES:EYEHeightstate?
    - DPOJET:MEAS<x>:EDGES:FROMLevel {HIGH | MID | LOW}
    - DPOJET:MEAS<x>:EDGES:FROMLevel?
    - DPOJET:MEAS<x>:EDGES:LEVel {HIGH | MID | LOW}
    - DPOJET:MEAS<x>:EDGES:LEVel?
    - DPOJET:MEAS<x>:EDGES:SLEWRATETechnique {NOMinalmethod | DDRmethod}
    - DPOJET:MEAS<x>:EDGES:SLEWRATETechnique?
    - DPOJET:MEAS<x>:EDGES:SUBRATEDivisor {TWO | FOUR | EIGHT}
    - DPOJET:MEAS<x>:EDGES:SUBRATEDivisor?
    - DPOJET:MEAS<x>:EDGES:TOLevel {HIGH | MID | LOW}
    - DPOJET:MEAS<x>:EDGES:TOLevel?
    - DPOJET:MEAS<x>:EDGES:USERDefinedvoltage  <NR3>
    - DPOJET:MEAS<x>:EDGES:USERDefinedvoltage?
    - DPOJET:MEAS<x>:EDGES:VOLTAGEState {1 | 0}
    - DPOJET:MEAS<x>:EDGES:VOLTAGEState?
    - DPOJET:MEAS<x>:FILTers:BLANKingtime  <NR3>
    - DPOJET:MEAS<x>:FILTers:BLANKingtime?
    - DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ  <NR3>
    - DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ?
    - DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC {NONE | FIRST | SECOND | THIRD}
    - DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC?
    - DPOJET:MEAS<x>:FILTers:LOWPass:FREQ  <NR3>
    - DPOJET:MEAS<x>:FILTers:LOWPass:FREQ?
    - DPOJET:MEAS<x>:FILTers:LOWPass:SPEC {NONE | FIRST | SECOND | THIRD}
    - DPOJET:MEAS<x>:FILTers:LOWPass:SPEC?
    - DPOJET:MEAS<x>:FILTers:RAMPtime  <NR3>
    - DPOJET:MEAS<x>:FILTers:RAMPtime?
    - DPOJET:MEAS<x>:FILTers:SJBAndwidth  <NR3>
    - DPOJET:MEAS<x>:FILTers:SJBAndwidth?
    - DPOJET:MEAS<x>:FILTers:SJFRequency  <NR3>
    - DPOJET:MEAS<x>:FILTers:SJFRequency?
    - DPOJET:MEAS<x>:FROMedge {RISe | FALL | BOTH}
    - DPOJET:MEAS<x>:FROMedge?
    - DPOJET:MEAS<x>:HIGHREFVoltage  <NR3>
    - DPOJET:MEAS<x>:HIGHREFVoltage?
    - DPOJET:MEAS<x>:LOGging:MEASurements:FILEname?
    - DPOJET:MEAS<x>:LOGging:MEASurements:SELect {1 | 0}
    - DPOJET:MEAS<x>:LOGging:MEASurements:SELect?
    - DPOJET:MEAS<x>:LOGging:STATistics:SELect {1 | 0}
    - DPOJET:MEAS<x>:LOGging:STATistics:SELect?
    - DPOJET:MEAS<x>:LOGging:WORSTcase:SELect {1 | 0}
    - DPOJET:MEAS<x>:LOGging:WORSTcase:SELect?
    - DPOJET:MEAS<x>:LOWREFVoltage  <NR3>
    - DPOJET:MEAS<x>:LOWREFVoltage?
    - DPOJET:MEAS<x>:MARGIN:HITCOUNTValue  <NR3>
    - DPOJET:MEAS<x>:MARGIN:HITCOUNTValue?
    - DPOJET:MEAS<x>:MARGIN:HITRATIOState {1 | 0}
    - DPOJET:MEAS<x>:MARGIN:HITRATIOState?
    - DPOJET:MEAS<x>:MARGIN:HITRATIOValue  <NR3>
    - DPOJET:MEAS<x>:MARGIN:HITRATIOValue?
    - DPOJET:MEAS<x>:MARGIN:RESOlution  <NR3>
    - DPOJET:MEAS<x>:MARGIN:RESOlution?
    - DPOJET:MEAS<x>:MASKOffset:HORizontal:AUTOfit?
    - DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual  <NR3>
    - DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual?
    - DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype { AUTOFIT | MANUAL}
    - DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype?
    - DPOJET:MEAS<x>:MASKfile  <string>
    - DPOJET:MEAS<x>:MASKfile?
    - DPOJET:MEAS<x>:MEASRange:MAX  <NR3>
    - DPOJET:MEAS<x>:MEASRange:MAX?
    - DPOJET:MEAS<x>:MEASRange:MIN  <NR3>
    - DPOJET:MEAS<x>:MEASRange:MIN?
    - DPOJET:MEAS<x>:MEASRange:STATE {1 | 0}
    - DPOJET:MEAS<x>:MEASRange:STATE?
    - DPOJET:MEAS<x>:MEASStart  <NR3>
    - DPOJET:MEAS<x>:MEASStart?
    - DPOJET:MEAS<x>:N  <NR3>
    - DPOJET:MEAS<x>:N?
    - DPOJET:MEAS<x>:NAME?
    - DPOJET:MEAS<x>:OPTIcal:BANDWIDth  <NR3>
    - DPOJET:MEAS<x>:OPTIcal:BANDWIDth?
    - DPOJET:MEAS<x>:OPTIcal:BTFILTEr  <string>
    - DPOJET:MEAS<x>:OPTIcal:BTFILTEr?
    - DPOJET:MEAS<x>:OPTIcal:FFETAPS  <string>
    - DPOJET:MEAS<x>:OPTIcal:FFETAPS?
    - DPOJET:MEAS<x>:OPTIcal:SCOPERN  <NR3>
    - DPOJET:MEAS<x>:OPTIcal:SCOPERN?
    - DPOJET:MEAS<x>:OPTIcal:TARGETBer  <NR3>
    - DPOJET:MEAS<x>:OPTIcal:TARGETBer?
    - DPOJET:MEAS<x>:OPTIcal:WFMTYpe {CONTINUOUS | MODULATED}
    - DPOJET:MEAS<x>:OPTIcal:WFMTYpe?
    - DPOJET:MEAS<x>:PHASENoise:HIGHLimit  <NR3>
    - DPOJET:MEAS<x>:PHASENoise:HIGHLimit?
    - DPOJET:MEAS<x>:PHASENoise:LOWLimit  <NR3>
    - DPOJET:MEAS<x>:PHASENoise:LOWLimit?
    - DPOJET:MEAS<x>:PLOTFILES?
    - DPOJET:MEAS<x>:REFVoltage {100 | —100}
    - DPOJET:MEAS<x>:REFVoltage?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:HITPopulation?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:HITS?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh:STATus?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw:STATus?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:STATus?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHLimit?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHMArgin?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:STATus?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC:STATus?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXHits?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:HIGHLimit?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:STATus?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWLimit?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWMArgin?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:STATus?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC:STATus?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:MINHits?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK:STATus?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation:STATus?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:Hits?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MAXHits?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MINHits?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev:STATus?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev?
    - DPOJET:MEAS<x>:RESULts:ALLAcqs?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:MAX:STATus?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:MAX?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC:STATus?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN:STATus?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:MIN:STATus?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:MIN?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC:STATus?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK:STATus?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation:STATus?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev:STATus?
    - DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev?
    - DPOJET:MEAS<x>:RESULts:GETAll?
    - DPOJET:MEAS<x>:RESULts:STATus?
    - DPOJET:MEAS<x>:RESULts:VIew?
    - DPOJET:MEAS<x>:RESULts?
    - DPOJET:MEAS<x>:RJDJ:BER  <NR3>
    - DPOJET:MEAS<x>:RJDJ:BER?
    - DPOJET:MEAS<x>:RJDJ:DETECTPLEN {0 | 1 | ON | OFF}
    - DPOJET:MEAS<x>:RJDJ:DETECTPLEN?
    - DPOJET:MEAS<x>:RJDJ:NCMODe {1 | 0}
    - DPOJET:MEAS<x>:RJDJ:NCMODe?
    - DPOJET:MEAS<x>:RJDJ:PATLen  <NR3>
    - DPOJET:MEAS<x>:RJDJ:PATLen?
    - DPOJET:MEAS<x>:RJDJ:SCOPERN  <NR3>
    - DPOJET:MEAS<x>:RJDJ:SCOPERN?
    - DPOJET:MEAS<x>:RJDJ:SNCREFID  <string>
    - DPOJET:MEAS<x>:RJDJ:SNCREFID?
    - DPOJET:MEAS<x>:RJDJ:TYPe {ARBITrary | REPEating}
    - DPOJET:MEAS<x>:RJDJ:TYPe?
    - DPOJET:MEAS<x>:RJDJ:WINDOwlength  <NR3>
    - DPOJET:MEAS<x>:RJDJ:WINDOwlength?
    - DPOJET:MEAS<x>:RNDN:AUTODETECTpattern {1 | 0 | ON | OFF}
    - DPOJET:MEAS<x>:RNDN:AUTODETECTpattern?
    - DPOJET:MEAS<x>:RNDN:BER  <NR3>
    - DPOJET:MEAS<x>:RNDN:BER?
    - DPOJET:MEAS<x>:RNDN:NCMODe {1 | 0}
    - DPOJET:MEAS<x>:RNDN:NCMODe?
    - DPOJET:MEAS<x>:RNDN:PATLen  <NR3>
    - DPOJET:MEAS<x>:RNDN:PATLen?
    - DPOJET:MEAS<x>:RNDN:SCOPERN  <NR3>
    - DPOJET:MEAS<x>:RNDN:SCOPERN?
    - DPOJET:MEAS<x>:RNDN:SNCREFID  <string>
    - DPOJET:MEAS<x>:RNDN:SNCREFID?
    - DPOJET:MEAS<x>:RNDN:TYPe {ARBITrary | REPEating}
    - DPOJET:MEAS<x>:RNDN:TYPe?
    - DPOJET:MEAS<x>:RNDN:WINDOwlength  <NR3>
    - DPOJET:MEAS<x>:RNDN:WINDOwlength?
    - DPOJET:MEAS<x>:SIGNALType {CLOCK | DATA | AUTO}
    - DPOJET:MEAS<x>:SIGNALType?
    - DPOJET:MEAS<x>:SOUrce1 {CH1 - CH4 | MATH1 - MATH4 | REF1 - REF4 | D0 — D15}
    - DPOJET:MEAS<x>:SOUrce1?
    - DPOJET:MEAS<x>:SOUrce2 {CH1 - CH4 | MATH1 - MATH4 | REF1 - REF4 | D0 — D15}
    - DPOJET:MEAS<x>:SOUrce2?
    - DPOJET:MEAS<x>:SSC:NOMinalfreq:AUTO?
    - DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual  <NR3>
    - DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual?
    - DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype {AUTO | MANUAL}
    - DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype?
    - DPOJET:MEAS<x>:TIMEDATa?
    - DPOJET:MEAS<x>:TOEdge {SAMEas | OPPositeas}
    - DPOJET:MEAS<x>:TOEdge?
    - DPOJET:MEAS<x>:ZOOMEVENT {MAX | MIN}
    - DPOJET:MINBUJUI  <NR3>
    - DPOJET:MINBUJUI?
    - DPOJET:NOISEENABLED {1 | 0 | ON | OFF}
    - DPOJET:NUMMeas?
    - DPOJET:NUMPlot?
    - DPOJET:OPTICALUNITType {WATT | DBM}
    - DPOJET:OPTICALUNITType?
    - DPOJET:PLOT<x>:BATHtub:BER  <NR3>
    - DPOJET:PLOT<x>:BATHtub:BER?
    - DPOJET:PLOT<x>:BATHtub:VERTical:SCALE {LINEAR | LOG}
    - DPOJET:PLOT<x>:BATHtub:VERTical:SCALE?
    - DPOJET:PLOT<x>:BATHtub:XAXISUnits { UNITIntervals | SECOnds }
    - DPOJET:PLOT<x>:BATHtub:XAXISUnits?
    - DPOJET:PLOT<x>:BERContour:ALIGNment {AUTO | LEFT | CENter}
    - DPOJET:PLOT<x>:BERContour:ALIGNment?
    - DPOJET:PLOT<x>:BERContour:BER1E12V {1 | 0}
    - DPOJET:PLOT<x>:BERContour:BER1E12V?
    - DPOJET:PLOT<x>:BERContour:BER1E15V {1 | 0}
    - DPOJET:PLOT<x>:BERContour:BER1E15V?
    - DPOJET:PLOT<x>:BERContour:BER1E18V {1 | 0}
    - DPOJET:PLOT<x>:BERContour:BER1E18V?
    - DPOJET:PLOT<x>:BERContour:BER1E6V {1 | 0}
    - DPOJET:PLOT<x>:BERContour:BER1E6V?
    - DPOJET:PLOT<x>:BERContour:BER1E9V {1 | 0}
    - DPOJET:PLOT<x>:BERContour:BER1E9V?
    - DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale {1 | 0}
    - DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale?
    - DPOJET:PLOT<x>:BERContour:HORizontal:RESolution  <NR3>
    - DPOJET:PLOT<x>:BERContour:HORizontal:RESolution?
    - DPOJET:PLOT<x>:BERContour:MASK {1 | 0}
    - DPOJET:PLOT<x>:BERContour:MASK?
    - DPOJET:PLOT<x>:BERContour:MASKFile  <string>
    - DPOJET:PLOT<x>:BERContour:MASKFile?
    - DPOJET:PLOT<x>:BERContour:SUPERImpose {1 | 0}
    - DPOJET:PLOT<x>:BERContour:SUPERImpose?
    - DPOJET:PLOT<x>:BERContour:TARGETBER {1 | 0}
    - DPOJET:PLOT<x>:BERContour:TARGETBER?
    - DPOJET:PLOT<x>:BEREye:BER1E12V {1 | 0}
    - DPOJET:PLOT<x>:BEREye:BER1E12V?
    - DPOJET:PLOT<x>:BEREye:BER1E15V {1 | 0}
    - DPOJET:PLOT<x>:BEREye:BER1E15V?
    - DPOJET:PLOT<x>:BEREye:BER1E18V {1 | 0}
    - DPOJET:PLOT<x>:BEREye:BER1E18V?
    - DPOJET:PLOT<x>:BEREye:BER1E6V {1 | 0}
    - DPOJET:PLOT<x>:BEREye:BER1E6V?
    - DPOJET:PLOT<x>:BEREye:BER1E9V {1 | 0}
    - DPOJET:PLOT<x>:BEREye:BER1E9V?
    - DPOJET:PLOT<x>:BEREye:TARGETBER {1 | 0}
    - DPOJET:PLOT<x>:BEREye:TARGETBER?
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD {1 | 0}
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD?
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins {TWENtyfive | FIFTY | HUNdred | TWOFifty | FIVEHundred | TWOThousand | MAXimum}
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins?
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ {1 | 0}
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ?
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ {1 | 0}
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ?
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ {1 | 0}
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ?
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE {LINEAR | LOG}
    - DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE?
    - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE {1 | 0}
    - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE?
    - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO {1 | 0}
    - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO?
    - DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE {LINEAR | LOG}
    - DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE?
    - DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins { TWENtyfive | FIFTY | HUNdred | TWOFifty | FIVEHundred | TWOThousand | MAXimum}
    - DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins?
    - DPOJET:PLOT<x>:COMPOSITENoisehist:PN {1 | 0}
    - DPOJET:PLOT<x>:COMPOSITENoisehist:PN?
    - DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN {1 | 0}
    - DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN?
    - DPOJET:PLOT<x>:COMPOSITENoisehist:TN {1 | 0}
    - DPOJET:PLOT<x>:COMPOSITENoisehist:TN?
    - DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V {1 | 0}
    - DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V?
    - DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V {1 | 0}
    - DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V?
    - DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V {1 | 0}
    - DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V?
    - DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V {1 | 0}
    - DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V?
    - DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V {1 | 0}
    - DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V?
    - DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT  <NR2>
    - DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT?
    - DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH  <NR2>
    - DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH?
    - DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER {1 | 0}
    - DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER?
    - DPOJET:PLOT<x>:CURRENTUISACquired?
    - DPOJET:PLOT<x>:CURRENTUISANalyzed?
    - DPOJET:PLOT<x>:DATA:XDATa:DDJDCD?
    - DPOJET:PLOT<x>:DATA:XDATa:DDNONE?
    - DPOJET:PLOT<x>:DATA:XDATa:DDNZERO?
    - DPOJET:PLOT<x>:DATA:XDATa:PJ?
    - DPOJET:PLOT<x>:DATA:XDATa:PN?
    - DPOJET:PLOT<x>:DATA:XDATa:RJBUJ?
    - DPOJET:PLOT<x>:DATA:XDATa:RNNPN?
    - DPOJET:PLOT<x>:DATA:XDATa:TJ?
    - DPOJET:PLOT<x>:DATA:XDATa:TN?
    - DPOJET:PLOT<x>:DATA:XDATa?
    - DPOJET:PLOT<x>:DATA:YDATa:DDJDCD?
    - DPOJET:PLOT<x>:DATA:YDATa:DDNONE?
    - DPOJET:PLOT<x>:DATA:YDATa:DDNZERO?
    - DPOJET:PLOT<x>:DATA:YDATa:PJ?
    - DPOJET:PLOT<x>:DATA:YDATa:PN?
    - DPOJET:PLOT<x>:DATA:YDATa:RJBUJ?
    - DPOJET:PLOT<x>:DATA:YDATa:RNNPN?
    - DPOJET:PLOT<x>:DATA:YDATa:TJ?
    - DPOJET:PLOT<x>:DATA:YDATa:TN?
    - DPOJET:PLOT<x>:DATA:YDATa?
    - DPOJET:PLOT<x>:EXPORTRaw?
    - DPOJET:PLOT<x>:EYE:ALIGNment {AUTO | LEFT | CENter}
    - DPOJET:PLOT<x>:EYE:ALIGNment?
    - DPOJET:PLOT<x>:EYE:EYEVerticalscale {SCALETOData, SCALETORefclk}
    - DPOJET:PLOT<x>:EYE:EYEVerticalscale?
    - DPOJET:PLOT<x>:EYE:HORIZScale {1 | 0}
    - DPOJET:PLOT<x>:EYE:HORIZScale?
    - DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale {1 | 0}
    - DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale?
    - DPOJET:PLOT<x>:EYE:HORizontal:RESolution  <NR3>
    - DPOJET:PLOT<x>:EYE:HORizontal:RESolution?
    - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx  <NR3>
    - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx?
    - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn  <NR3>
    - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn?
    - DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor {AUTO, TWELVEPOINTEIGHT, SIXTEEN}
    - DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor?
    - DPOJET:PLOT<x>:EYE:INTERPolationtype { INTERPOLATION | NONINTERPOLATION }
    - DPOJET:PLOT<x>:EYE:INTERPolationtype?
    - DPOJET:PLOT<x>:EYE:MASKfile  <string>
    - DPOJET:PLOT<x>:EYE:MASKfile?
    - DPOJET:PLOT<x>:EYE:STATE {1 | 0}
    - DPOJET:PLOT<x>:EYE:STATE?
    - DPOJET:PLOT<x>:EYE:SUPERImpose {1 | 0}
    - DPOJET:PLOT<x>:EYE:SUPERImpose?
    - DPOJET:PLOT<x>:EYE:VERTICALAlignment {1 | 0}
    - DPOJET:PLOT<x>:EYE:VERTICALAlignment?
    - DPOJET:PLOT<x>:EYE:VERTScale {1 | 0}
    - DPOJET:PLOT<x>:EYE:VERTScale?
    - DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx  <NR3>
    - DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx?
    - DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn  <NR3>
    - DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn?
    - DPOJET:PLOT<x>:HISTOgram:AUTOset {EXECute}
    - DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale {1 | 0}
    - DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale?
    - DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter  <NR3>
    - DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter?
    - DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN  <NR3>
    - DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN?
    - DPOJET:PLOT<x>:HISTOgram:NUMBins {TWENtyfive | FIFTY | HUNdred | TWOFifty | FIVEHundred | TWOThousand | MAXimum}
    - DPOJET:PLOT<x>:HISTOgram:NUMBins?
    - DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE {LINEAR | LOG}
    - DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE?
    - DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits { UNITAmplitudes | VOLTs }
    - DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits?
    - DPOJET:PLOT<x>:PDFEye:BER1E12V {1 | 0}
    - DPOJET:PLOT<x>:PDFEye:BER1E12V?
    - DPOJET:PLOT<x>:PDFEye:BER1E15V {1 | 0}
    - DPOJET:PLOT<x>:PDFEye:BER1E15V?
    - DPOJET:PLOT<x>:PDFEye:BER1E18V {1 | 0}
    - DPOJET:PLOT<x>:PDFEye:BER1E18V?
    - DPOJET:PLOT<x>:PDFEye:BER1E6V {1 | 0}
    - DPOJET:PLOT<x>:PDFEye:BER1E6V?
    - DPOJET:PLOT<x>:PDFEye:BER1E9V {1 | 0}
    - DPOJET:PLOT<x>:PDFEye:BER1E9V?
    - DPOJET:PLOT<x>:PDFEye:TARGETBER {1 | 0}
    - DPOJET:PLOT<x>:PDFEye:TARGETBER?
    - DPOJET:PLOT<x>:PHASEnoise:BASEline  <NR3>
    - DPOJET:PLOT<x>:PHASEnoise:BASEline?
    - DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter {ONEBYHUNDREDTHdecade | ONEBYTENTHDECADE | ONEDECADE}
    - DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter?
    - DPOJET:PLOT<x>:SOUrce?
    - DPOJET:PLOT<x>:SPECtrum:BASE  <NR3>
    - DPOJET:PLOT<x>:SPECtrum:BASE?
    - DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE {LINEAR | LOG}
    - DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE?
    - DPOJET:PLOT<x>:SPECtrum:MODE {NORMal | AVErage | PEAKhold}
    - DPOJET:PLOT<x>:SPECtrum:MODE?
    - DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE {LINEAR | LOG}
    - DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE?
    - DPOJET:PLOT<x>:TOTALUISAcquired?
    - DPOJET:PLOT<x>:TOTALUISAnalyzed?
    - DPOJET:PLOT<x>:TRANSfer:DENominator {MEAS1 - MEAS99}
    - DPOJET:PLOT<x>:TRANSfer:DENominator?
    - DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE {LINEAR | LOG}
    - DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE?
    - DPOJET:PLOT<x>:TRANSfer:MODE {NORMal | AVErage}
    - DPOJET:PLOT<x>:TRANSfer:MODE?
    - DPOJET:PLOT<x>:TRANSfer:NUMerator {MEAS1 - MEAS99}
    - DPOJET:PLOT<x>:TRANSfer:NUMerator?
    - DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE {LINEAR | LOG}
    - DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE?
    - DPOJET:PLOT<x>:TREND:TYPe {VECTOR | BAR}
    - DPOJET:PLOT<x>:TREND:TYPe?
    - DPOJET:PLOT<x>:TYPe?
    - DPOJET:PLOT<x>:VERTBATHtub:BER   <NR3>
    - DPOJET:PLOT<x>:VERTBATHtub:BER?
    - DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE {LINEAR | LOG}
    - DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE?
    - DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits {VOLTs | UNITAMPLITUDES}
    - DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits?
    - DPOJET:PLOT<x>:XUnits?
    - DPOJET:PLOT<x>:YUnits?
    - DPOJET:POPULATION:CONDition {EACHmeas | LASTmeas}
    - DPOJET:POPULATION:CONDition?
    - DPOJET:POPULATION:LIMIT  <NR3>
    - DPOJET:POPULATION:LIMIT?
    - DPOJET:POPULATION:LIMITBY {ACQuisitions | POPUlation}
    - DPOJET:POPULATION:LIMITBY?
    - DPOJET:POPULATION:STATE {1 | 0}
    - DPOJET:POPULATION:STATE?
    - DPOJET:QUALify:ACTIVE {HIGH | LOW}
    - DPOJET:QUALify:ACTIVE?
    - DPOJET:QUALify:SOUrce {CH1 - CH4 | MATH1 - MATH4 | REF1 - REF4 | SEARCH0 - SEARCH8}
    - DPOJET:QUALify:SOUrce?
    - DPOJET:QUALify:STATE {1 | 0}
    - DPOJET:QUALify:STATE?
    - DPOJET:REFLevel:CH<x>:MIDZero {1 | 0}
    - DPOJET:REFLevel:CH<x>:MIDZero?
    - DPOJET:REFLevels:AUTOset {EXECute}
    - DPOJET:REFLevels:AUTOset:STATE?
    - DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh  <NR3>
    - DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh?
    - DPOJET:REFLevels:CH<x>:ABSolute:FALLLow  <NR3>
    - DPOJET:REFLevels:CH<x>:ABSolute:FALLLow?
    - DPOJET:REFLevels:CH<x>:ABSolute:FALLMid  <NR3>
    - DPOJET:REFLevels:CH<x>:ABSolute:FALLMid?
    - DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis  <NR3>
    - DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis?
    - DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh  <NR3>
    - DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh?
    - DPOJET:REFLevels:CH<x>:ABSolute:RISELow  <NR3>
    - DPOJET:REFLevels:CH<x>:ABSolute:RISELow?
    - DPOJET:REFLevels:CH<x>:ABSolute:RISEMid  <NR3>
    - DPOJET:REFLevels:CH<x>:ABSolute:RISEMid?
    - DPOJET:REFLevels:CH<x>:ABSolute?
    - DPOJET:REFLevels:CH<x>:AUTOSet {1 | 0}
    - DPOJET:REFLevels:CH<x>:BASETop {MINMax | FULLhistogram | EYEhistogram | AUTO}
    - DPOJET:REFLevels:CH<x>:BASETop?
    - DPOJET:REFLevels:CH<x>:PERcent:FALLHigh  <NR3>
    - DPOJET:REFLevels:CH<x>:PERcent:FALLHigh?
    - DPOJET:REFLevels:CH<x>:PERcent:FALLLow  <NR3>
    - DPOJET:REFLevels:CH<x>:PERcent:FALLLow?
    - DPOJET:REFLevels:CH<x>:PERcent:FALLMid  <NR3>
    - DPOJET:REFLevels:CH<x>:PERcent:FALLMid?
    - DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis  <NR3>
    - DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis?
    - DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel { 1 | 0 }
    - DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel?
    - DPOJET:REFLevels:CH<x>:PERcent:RISEHigh  <NR3>
    - DPOJET:REFLevels:CH<x>:PERcent:RISEHigh?
    - DPOJET:REFLevels:CH<x>:PERcent:RISELow  <NR3>
    - DPOJET:REFLevels:CH<x>:PERcent:RISELow?
    - DPOJET:REFLevels:CH<x>:PERcent:RISEMid  <NR3>
    - DPOJET:REFLevels:CH<x>:PERcent:RISEMid?
    - DPOJET:REFLevels:CH<x>:PERcent?
    - DPOJET:REPORT {EXECute | APPEnd}
    - DPOJET:REPORT:APPlicationconfig {1 | 0}
    - DPOJET:REPORT:APPlicationconfig?
    - DPOJET:REPORT:AUTOincrement {1 | 0}
    - DPOJET:REPORT:AUTOincrement?
    - DPOJET:REPORT:COMments  <string>
    - DPOJET:REPORT:COMments?
    - DPOJET:REPORT:DETailedresults {1 | 0}
    - DPOJET:REPORT:DETailedresults?
    - DPOJET:REPORT:ENABlecomments {1 | 0}
    - DPOJET:REPORT:ENABlecomments?
    - DPOJET:REPORT:GETIMAGE?
    - DPOJET:REPORT:GETIMAGEName?
    - DPOJET:REPORT:GETXMLReport?
    - DPOJET:REPORT:PASSFailresults {1 | 0}
    - DPOJET:REPORT:PASSFailresults?
    - DPOJET:REPORT:PLOTimages {1 | 0}
    - DPOJET:REPORT:PLOTimages?
    - DPOJET:REPORT:REPORTName  <string>
    - DPOJET:REPORT:REPORTName?
    - DPOJET:REPORT:SAVEWaveforms {1 | 0}
    - DPOJET:REPORT:SAVEWaveforms?
    - DPOJET:REPORT:SETIMAGEPath  <file string>
    - DPOJET:REPORT:SETupconfig {1 | 0}
    - DPOJET:REPORT:SETupconfig?
    - DPOJET:REPORT:STATE?
    - DPOJET:REPORT:TYPe {MHT|PDF}
    - DPOJET:REPORT:TYPe?
    - DPOJET:REPORT:VIEWreport {1 | 0}
    - DPOJET:REPORT:VIEWreport?
    - DPOJET:RESULts:GETALLResults?
    - DPOJET:RESULts:STATus?
    - DPOJET:RESULts:VIew {SUMmary | DETails}
    - DPOJET:RESULts:VIew?
    - DPOJET:SAVE {MEAS<x> | REF<x>}
    - DPOJET:SAVEALLPLOTS
    - DPOJET:SETIMAGETPath  <file string>
    - DPOJET:SETIMAGETPath?
    - DPOJET:SETLOGGINGPath  <file string>
    - DPOJET:SETLOGGINGPath?
    - DPOJET:SETREPORTPath  <file string>
    - DPOJET:SETREPORTPath?
    - DPOJET:SHOWMEASWARNing {1|0}
    - DPOJET:SHOWMEASWARNing?
    - DPOJET:SNC:ACTIvate
    - DPOJET:SNC:CLOse
    - DPOJET:SOURCEAutoset {HORizontal | VERTical | BOTH}
    - DPOJET:SOURCEAutoset:HORizontal:UICount  <NR3>
    - DPOJET:SOURCEAutoset:HORizontal:UICount?
    - DPOJET:SOURCEAutoset:HORizontal:UIValue  <NR3>
    - DPOJET:SOURCEAutoset:HORizontal:UIValue?
    - DPOJET:SOURCEAutoset:STATE?
    - DPOJET:STATE {RUN | SINGLE | RECALC | CLEAR | STOP}
    - DPOJET:STATE?
    - DPOJET:TDCOMPensation {1 | 0 | ON | OFF}
    - DPOJET:TDCOMPensation?
    - DPOJET:UNITType {UNITinterval | SEConds}
    - DPOJET:UNITType?
    - DPOJET:VERTUNITType {UNITamplitude | VOLts}
    - DPOJET:VERTUNITType?
    - DPOJET:VERsion?
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


class DpojetVersion(SCPICmdRead):
    """The ``DPOJET:VERsion`` command.

    Description:
        - This query-only command returns the current DPOJET version string.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:VERsion?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:VERsion?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:VERsion?
        ```
    """


class DpojetVertunittype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:VERTUNITType`` command.

    Description:
        - This command sets or queries the vertical Unit.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:VERTUNITType?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:VERTUNITType?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:VERTUNITType value`` command.

    SCPI Syntax:
        ```
        - DPOJET:VERTUNITType {UNITamplitude | VOLts}
        - DPOJET:VERTUNITType?
        ```
    """


class DpojetUnittype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:UNITType`` command.

    Description:
        - This command sets or queries the current unit-type setting for DPOJET, either Unit
          Interval, or seconds.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:UNITType?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:UNITType?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:UNITType value`` command.

    SCPI Syntax:
        ```
        - DPOJET:UNITType {UNITinterval | SEConds}
        - DPOJET:UNITType?
        ```
    """


class DpojetTdcompensation(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:TDCOMPensation`` command.

    Description:
        - This command sets or queries the TD compensation state.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:TDCOMPensation?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:TDCOMPensation?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:TDCOMPensation value`` command.

    SCPI Syntax:
        ```
        - DPOJET:TDCOMPensation {1 | 0 | ON | OFF}
        - DPOJET:TDCOMPensation?
        ```
    """


class DpojetState(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:STATE`` command.

    Description:
        - This command sets or queries the current measurement state of DPOJET.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:STATE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:STATE {RUN | SINGLE | RECALC | CLEAR | STOP}
        - DPOJET:STATE?
        ```
    """


class DpojetSourceautosetState(SCPICmdRead):
    """The ``DPOJET:SOURCEAutoset:STATE`` command.

    Description:
        - This query-only command provides the Source Autoset status.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:SOURCEAutoset:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:SOURCEAutoset:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:SOURCEAutoset:STATE?
        ```
    """


class DpojetSourceautosetHorizontalUivalue(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:SOURCEAutoset:HORizontal:UIValue`` command.

    Description:
        - This command sets or queries the UI value for horizontal autoset.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:SOURCEAutoset:HORizontal:UIValue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:SOURCEAutoset:HORizontal:UIValue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:SOURCEAutoset:HORizontal:UIValue value`` command.

    SCPI Syntax:
        ```
        - DPOJET:SOURCEAutoset:HORizontal:UIValue  <NR3>
        - DPOJET:SOURCEAutoset:HORizontal:UIValue?
        ```
    """


class DpojetSourceautosetHorizontalUicount(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:SOURCEAutoset:HORizontal:UICount`` command.

    Description:
        - This command sets or queries the UICount for horizontal autoset.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:SOURCEAutoset:HORizontal:UICount?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:SOURCEAutoset:HORizontal:UICount?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:SOURCEAutoset:HORizontal:UICount value`` command.

    SCPI Syntax:
        ```
        - DPOJET:SOURCEAutoset:HORizontal:UICount  <NR3>
        - DPOJET:SOURCEAutoset:HORizontal:UICount?
        ```
    """


class DpojetSourceautosetHorizontal(SCPICmdRead):
    """The ``DPOJET:SOURCEAutoset:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:SOURCEAutoset:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:SOURCEAutoset:HORizontal?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.uicount``: The ``DPOJET:SOURCEAutoset:HORizontal:UICount`` command.
        - ``.uivalue``: The ``DPOJET:SOURCEAutoset:HORizontal:UIValue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._uicount = DpojetSourceautosetHorizontalUicount(device, f"{self._cmd_syntax}:UICount")
        self._uivalue = DpojetSourceautosetHorizontalUivalue(device, f"{self._cmd_syntax}:UIValue")

    @property
    def uicount(self) -> DpojetSourceautosetHorizontalUicount:
        """Return the ``DPOJET:SOURCEAutoset:HORizontal:UICount`` command.

        Description:
            - This command sets or queries the UICount for horizontal autoset.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:SOURCEAutoset:HORizontal:UICount?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:SOURCEAutoset:HORizontal:UICount?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:SOURCEAutoset:HORizontal:UICount value`` command.

        SCPI Syntax:
            ```
            - DPOJET:SOURCEAutoset:HORizontal:UICount  <NR3>
            - DPOJET:SOURCEAutoset:HORizontal:UICount?
            ```
        """
        return self._uicount

    @property
    def uivalue(self) -> DpojetSourceautosetHorizontalUivalue:
        """Return the ``DPOJET:SOURCEAutoset:HORizontal:UIValue`` command.

        Description:
            - This command sets or queries the UI value for horizontal autoset.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:SOURCEAutoset:HORizontal:UIValue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:SOURCEAutoset:HORizontal:UIValue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:SOURCEAutoset:HORizontal:UIValue value`` command.

        SCPI Syntax:
            ```
            - DPOJET:SOURCEAutoset:HORizontal:UIValue  <NR3>
            - DPOJET:SOURCEAutoset:HORizontal:UIValue?
            ```
        """
        return self._uivalue


class DpojetSourceautoset(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:SOURCEAutoset`` command.

    Description:
        - This command performs a DPOJET horizontal, vertical, or autoset on both horizontal and
          vertical for any sources used in current measurements.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:SOURCEAutoset value`` command.

    SCPI Syntax:
        ```
        - DPOJET:SOURCEAutoset {HORizontal | VERTical | BOTH}
        ```

    Properties:
        - ``.horizontal``: The ``DPOJET:SOURCEAutoset:HORizontal`` command tree.
        - ``.state``: The ``DPOJET:SOURCEAutoset:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = DpojetSourceautosetHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._state = DpojetSourceautosetState(device, f"{self._cmd_syntax}:STATE")

    @property
    def horizontal(self) -> DpojetSourceautosetHorizontal:
        """Return the ``DPOJET:SOURCEAutoset:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:SOURCEAutoset:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:SOURCEAutoset:HORizontal?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.uicount``: The ``DPOJET:SOURCEAutoset:HORizontal:UICount`` command.
            - ``.uivalue``: The ``DPOJET:SOURCEAutoset:HORizontal:UIValue`` command.
        """
        return self._horizontal

    @property
    def state(self) -> DpojetSourceautosetState:
        """Return the ``DPOJET:SOURCEAutoset:STATE`` command.

        Description:
            - This query-only command provides the Source Autoset status.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:SOURCEAutoset:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:SOURCEAutoset:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:SOURCEAutoset:STATE?
            ```
        """
        return self._state


class DpojetSncClose(SCPICmdWriteNoArguments):
    """The ``DPOJET:SNC:CLOse`` command.

    Description:
        - This set only command closes Scope Noise Characterization application.When the Scope Noise
          Characterization application is launched using the

    Usage:
        - Using the ``.write()`` method will send the ``DPOJET:SNC:CLOse`` command.

    SCPI Syntax:
        ```
        - DPOJET:SNC:CLOse
        ```
    """


class DpojetSncActivate(SCPICmdWriteNoArguments):
    """The ``DPOJET:SNC:ACTIvate`` command.

    Description:
        - This set only command activates Scope Noise Characterization application.

    Usage:
        - Using the ``.write()`` method will send the ``DPOJET:SNC:ACTIvate`` command.

    SCPI Syntax:
        ```
        - DPOJET:SNC:ACTIvate
        ```
    """


class DpojetSnc(SCPICmdRead):
    """The ``DPOJET:SNC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:SNC?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:SNC?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.activate``: The ``DPOJET:SNC:ACTIvate`` command.
        - ``.close``: The ``DPOJET:SNC:CLOse`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._activate = DpojetSncActivate(device, f"{self._cmd_syntax}:ACTIvate")
        self._close = DpojetSncClose(device, f"{self._cmd_syntax}:CLOse")

    @property
    def activate(self) -> DpojetSncActivate:
        """Return the ``DPOJET:SNC:ACTIvate`` command.

        Description:
            - This set only command activates Scope Noise Characterization application.

        Usage:
            - Using the ``.write()`` method will send the ``DPOJET:SNC:ACTIvate`` command.

        SCPI Syntax:
            ```
            - DPOJET:SNC:ACTIvate
            ```
        """
        return self._activate

    @property
    def close(self) -> DpojetSncClose:
        """Return the ``DPOJET:SNC:CLOse`` command.

        Description:
            - This set only command closes Scope Noise Characterization application.When the Scope
              Noise Characterization application is launched using the

        Usage:
            - Using the ``.write()`` method will send the ``DPOJET:SNC:CLOse`` command.

        SCPI Syntax:
            ```
            - DPOJET:SNC:CLOse
            ```
        """
        return self._close


class DpojetShowmeaswarning(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:SHOWMEASWARNing`` command.

    Description:
        - This sets or queries the visibility of Reference Level Autoset warnings, either on or off.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:SHOWMEASWARNing?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:SHOWMEASWARNing?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:SHOWMEASWARNing value`` command.

    SCPI Syntax:
        ```
        - DPOJET:SHOWMEASWARNing {1|0}
        - DPOJET:SHOWMEASWARNing?
        ```
    """


class DpojetSetreportpath(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:SETREPORTPath`` command.

    Description:
        - This command sets or queries the Report path of the DPOJET application.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:SETREPORTPath?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:SETREPORTPath?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:SETREPORTPath value`` command.

    SCPI Syntax:
        ```
        - DPOJET:SETREPORTPath  <file string>
        - DPOJET:SETREPORTPath?
        ```
    """


class DpojetSetloggingpath(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:SETLOGGINGPath`` command.

    Description:
        - This command sets or queries the Logging path of the DPOJET application.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:SETLOGGINGPath?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:SETLOGGINGPath?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:SETLOGGINGPath value`` command.

    SCPI Syntax:
        ```
        - DPOJET:SETLOGGINGPath  <file string>
        - DPOJET:SETLOGGINGPath?
        ```
    """


class DpojetSetimagetpath(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:SETIMAGETPath`` command.

    Description:
        - This command sets or queries the image path of the DPOJET application.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:SETIMAGETPath?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:SETIMAGETPath?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:SETIMAGETPath value`` command.

    SCPI Syntax:
        ```
        - DPOJET:SETIMAGETPath  <file string>
        - DPOJET:SETIMAGETPath?
        ```
    """


class DpojetSaveallplots(SCPICmdWriteNoArguments):
    """The ``DPOJET:SAVEALLPLOTS`` command.

    Description:
        - Saves all the plots to Reports/Resource folder.

    Usage:
        - Using the ``.write()`` method will send the ``DPOJET:SAVEALLPLOTS`` command.

    SCPI Syntax:
        ```
        - DPOJET:SAVEALLPLOTS
        ```
    """


class DpojetSave(SCPICmdWrite):
    """The ``DPOJET:SAVE`` command.

    Description:
        - This set-only command saves the specified DPOJET measurement result to the specified ref.
          For Example: ``DPOJET:SAVE`` MEAS4, REF2.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:SAVE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:SAVE {MEAS<x> | REF<x>}
        ```
    """


class DpojetResultsView(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:RESULts:VIew`` command.

    Description:
        - This command sets or queries the results view type.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:RESULts:VIew?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:RESULts:VIew?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:RESULts:VIew value`` command.

    SCPI Syntax:
        ```
        - DPOJET:RESULts:VIew {SUMmary | DETails}
        - DPOJET:RESULts:VIew?
        ```
    """


class DpojetResultsStatus(SCPICmdRead):
    """The ``DPOJET:RESULts:STATus`` command.

    Description:
        - This query-only command returns the overall pass/fail status.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:RESULts:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:RESULts:STATus?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:RESULts:STATus?
        ```
    """


class DpojetResultsGetallresults(SCPICmdRead):
    """The ``DPOJET:RESULts:GETALLResults`` command.

    Description:
        - The query only command returns all the measurement results in binary format. This command
          is similar to curve query.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:RESULts:GETALLResults?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:RESULts:GETALLResults?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:RESULts:GETALLResults?
        ```
    """


class DpojetResults(SCPICmdRead):
    """The ``DPOJET:RESULts`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:RESULts?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:RESULts?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.getallresults``: The ``DPOJET:RESULts:GETALLResults`` command.
        - ``.status``: The ``DPOJET:RESULts:STATus`` command.
        - ``.view``: The ``DPOJET:RESULts:VIew`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._getallresults = DpojetResultsGetallresults(
            device, f"{self._cmd_syntax}:GETALLResults"
        )
        self._status = DpojetResultsStatus(device, f"{self._cmd_syntax}:STATus")
        self._view = DpojetResultsView(device, f"{self._cmd_syntax}:VIew")

    @property
    def getallresults(self) -> DpojetResultsGetallresults:
        """Return the ``DPOJET:RESULts:GETALLResults`` command.

        Description:
            - The query only command returns all the measurement results in binary format. This
              command is similar to curve query.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:RESULts:GETALLResults?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:RESULts:GETALLResults?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:RESULts:GETALLResults?
            ```
        """
        return self._getallresults

    @property
    def status(self) -> DpojetResultsStatus:
        """Return the ``DPOJET:RESULts:STATus`` command.

        Description:
            - This query-only command returns the overall pass/fail status.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:RESULts:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:RESULts:STATus?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:RESULts:STATus?
            ```
        """
        return self._status

    @property
    def view(self) -> DpojetResultsView:
        """Return the ``DPOJET:RESULts:VIew`` command.

        Description:
            - This command sets or queries the results view type.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:RESULts:VIew?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:RESULts:VIew?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:RESULts:VIew value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:RESULts:VIew {SUMmary | DETails}
            - DPOJET:RESULts:VIew?
            ```
        """
        return self._view


class DpojetReportViewreport(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:VIEWreport`` command.

    Description:
        - This command turns on or off viewing report after generation.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:VIEWreport?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:VIEWreport?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:VIEWreport value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:VIEWreport {1 | 0}
        - DPOJET:REPORT:VIEWreport?
        ```
    """


class DpojetReportType(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:TYPe`` command.

    Description:
        - This command sets or queries the report type.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:TYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:TYPe value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:TYPe {MHT|PDF}
        - DPOJET:REPORT:TYPe?
        ```
    """


class DpojetReportState(SCPICmdRead):
    """The ``DPOJET:REPORT:STATE`` command.

    Description:
        - This query-only command provides the report status.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:STATE?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:STATE?
        ```
    """


class DpojetReportSetupconfig(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:SETupconfig`` command.

    Description:
        - This command turns on or off including setup configuration in reports.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:SETupconfig?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:SETupconfig?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:SETupconfig value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:SETupconfig {1 | 0}
        - DPOJET:REPORT:SETupconfig?
        ```
    """


class DpojetReportSetimagepath(SCPICmdWrite):
    """The ``DPOJET:REPORT:SETIMAGEPath`` command.

    Description:
        - This command sets the path of the image which you want to retreive using
          ``DPOJET:REPORT:GETIMAGE`` command.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:SETIMAGEPath value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:SETIMAGEPath  <file string>
        ```
    """


class DpojetReportSavewaveforms(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:SAVEWaveforms`` command.

    Description:
        - This command turns on or off saving waveforms when a report save/append is invoked.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:SAVEWaveforms?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:SAVEWaveforms?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:SAVEWaveforms value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:SAVEWaveforms {1 | 0}
        - DPOJET:REPORT:SAVEWaveforms?
        ```
    """


class DpojetReportReportname(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:REPORTName`` command.

    Description:
        - This command sets the current report file name.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:REPORTName?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:REPORTName?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:REPORTName value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:REPORTName  <string>
        - DPOJET:REPORT:REPORTName?
        ```
    """


class DpojetReportPlotimages(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:PLOTimages`` command.

    Description:
        - This command turns on or off including detailed plot images in reports.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:PLOTimages?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:PLOTimages?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:PLOTimages value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:PLOTimages {1 | 0}
        - DPOJET:REPORT:PLOTimages?
        ```
    """


class DpojetReportPassfailresults(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:PASSFailresults`` command.

    Description:
        - This command turns on or off including pass/fail results in reports.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:PASSFailresults?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:PASSFailresults?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:PASSFailresults value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:PASSFailresults {1 | 0}
        - DPOJET:REPORT:PASSFailresults?
        ```
    """


class DpojetReportGetxmlreport(SCPICmdRead):
    """The ``DPOJET:REPORT:GETXMLReport`` command.

    Description:
        - This query only command retrieve the report in binary format

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:GETXMLReport?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:GETXMLReport?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:GETXMLReport?
        ```
    """


class DpojetReportGetimagename(SCPICmdRead):
    """The ``DPOJET:REPORT:GETIMAGEName`` command.

    Description:
        - This query only commands gets all the PNG format image names from this
          directoryC:Users<userName>TektronixTekApplicationsDPOJETReportsResources

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:GETIMAGEName?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:GETIMAGEName?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:GETIMAGEName?
        ```
    """


class DpojetReportGetimage(SCPICmdRead):
    """The ``DPOJET:REPORT:GETIMAGE`` command.

    Description:
        - This command returns the image which is set using ``DPOJET:REPORT:SETIMAGEPath`` command
          in binary format.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:GETIMAGE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:GETIMAGE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:GETIMAGE?
        ```
    """


class DpojetReportEnablecomments(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:ENABlecomments`` command.

    Description:
        - This command sets or queries the comments enable or disable settings.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:ENABlecomments?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:ENABlecomments?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:ENABlecomments value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:ENABlecomments {1 | 0}
        - DPOJET:REPORT:ENABlecomments?
        ```
    """


class DpojetReportDetailedresults(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:DETailedresults`` command.

    Description:
        - This command turns on or off including detailed results in reports.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:DETailedresults?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:DETailedresults?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:DETailedresults value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:DETailedresults {1 | 0}
        - DPOJET:REPORT:DETailedresults?
        ```
    """


class DpojetReportComments(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:COMments`` command.

    Description:
        - This command sets or queries the comments.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:COMments?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:COMments?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:COMments value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:COMments  <string>
        - DPOJET:REPORT:COMments?
        ```
    """


class DpojetReportAutoincrement(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:AUTOincrement`` command.

    Description:
        - This command turns on or off auto increment of report file names.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:AUTOincrement?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:AUTOincrement?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:AUTOincrement value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:AUTOincrement {1 | 0}
        - DPOJET:REPORT:AUTOincrement?
        ```
    """


class DpojetReportApplicationconfig(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT:APPlicationconfig`` command.

    Description:
        - This command turns on or off including complete application configuration in reports.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REPORT:APPlicationconfig?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:APPlicationconfig?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:APPlicationconfig value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT:APPlicationconfig {1 | 0}
        - DPOJET:REPORT:APPlicationconfig?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetReport(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REPORT`` command.

    Description:
        - These are set-only commands. EXECute executes a DPOJET report save operation for the
          currently defined report configuration. APPEnd appends new data to the selected
          report.Ensure to close the PDF report before append.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:REPORT value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REPORT {EXECute | APPEnd}
        ```

    Properties:
        - ``.applicationconfig``: The ``DPOJET:REPORT:APPlicationconfig`` command.
        - ``.autoincrement``: The ``DPOJET:REPORT:AUTOincrement`` command.
        - ``.comments``: The ``DPOJET:REPORT:COMments`` command.
        - ``.detailedresults``: The ``DPOJET:REPORT:DETailedresults`` command.
        - ``.enablecomments``: The ``DPOJET:REPORT:ENABlecomments`` command.
        - ``.getimage``: The ``DPOJET:REPORT:GETIMAGE`` command.
        - ``.getimagename``: The ``DPOJET:REPORT:GETIMAGEName`` command.
        - ``.getxmlreport``: The ``DPOJET:REPORT:GETXMLReport`` command.
        - ``.passfailresults``: The ``DPOJET:REPORT:PASSFailresults`` command.
        - ``.plotimages``: The ``DPOJET:REPORT:PLOTimages`` command.
        - ``.reportname``: The ``DPOJET:REPORT:REPORTName`` command.
        - ``.savewaveforms``: The ``DPOJET:REPORT:SAVEWaveforms`` command.
        - ``.setimagepath``: The ``DPOJET:REPORT:SETIMAGEPath`` command.
        - ``.setupconfig``: The ``DPOJET:REPORT:SETupconfig`` command.
        - ``.state``: The ``DPOJET:REPORT:STATE`` command.
        - ``.type``: The ``DPOJET:REPORT:TYPe`` command.
        - ``.viewreport``: The ``DPOJET:REPORT:VIEWreport`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._applicationconfig = DpojetReportApplicationconfig(
            device, f"{self._cmd_syntax}:APPlicationconfig"
        )
        self._autoincrement = DpojetReportAutoincrement(device, f"{self._cmd_syntax}:AUTOincrement")
        self._comments = DpojetReportComments(device, f"{self._cmd_syntax}:COMments")
        self._detailedresults = DpojetReportDetailedresults(
            device, f"{self._cmd_syntax}:DETailedresults"
        )
        self._enablecomments = DpojetReportEnablecomments(
            device, f"{self._cmd_syntax}:ENABlecomments"
        )
        self._getimage = DpojetReportGetimage(device, f"{self._cmd_syntax}:GETIMAGE")
        self._getimagename = DpojetReportGetimagename(device, f"{self._cmd_syntax}:GETIMAGEName")
        self._getxmlreport = DpojetReportGetxmlreport(device, f"{self._cmd_syntax}:GETXMLReport")
        self._passfailresults = DpojetReportPassfailresults(
            device, f"{self._cmd_syntax}:PASSFailresults"
        )
        self._plotimages = DpojetReportPlotimages(device, f"{self._cmd_syntax}:PLOTimages")
        self._reportname = DpojetReportReportname(device, f"{self._cmd_syntax}:REPORTName")
        self._savewaveforms = DpojetReportSavewaveforms(device, f"{self._cmd_syntax}:SAVEWaveforms")
        self._setimagepath = DpojetReportSetimagepath(device, f"{self._cmd_syntax}:SETIMAGEPath")
        self._setupconfig = DpojetReportSetupconfig(device, f"{self._cmd_syntax}:SETupconfig")
        self._state = DpojetReportState(device, f"{self._cmd_syntax}:STATE")
        self._type = DpojetReportType(device, f"{self._cmd_syntax}:TYPe")
        self._viewreport = DpojetReportViewreport(device, f"{self._cmd_syntax}:VIEWreport")

    @property
    def applicationconfig(self) -> DpojetReportApplicationconfig:
        """Return the ``DPOJET:REPORT:APPlicationconfig`` command.

        Description:
            - This command turns on or off including complete application configuration in reports.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:APPlicationconfig?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:APPlicationconfig?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REPORT:APPlicationconfig value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:APPlicationconfig {1 | 0}
            - DPOJET:REPORT:APPlicationconfig?
            ```
        """
        return self._applicationconfig

    @property
    def autoincrement(self) -> DpojetReportAutoincrement:
        """Return the ``DPOJET:REPORT:AUTOincrement`` command.

        Description:
            - This command turns on or off auto increment of report file names.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:AUTOincrement?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:AUTOincrement?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:AUTOincrement value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:AUTOincrement {1 | 0}
            - DPOJET:REPORT:AUTOincrement?
            ```
        """
        return self._autoincrement

    @property
    def comments(self) -> DpojetReportComments:
        """Return the ``DPOJET:REPORT:COMments`` command.

        Description:
            - This command sets or queries the comments.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:COMments?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:COMments?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:COMments value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:COMments  <string>
            - DPOJET:REPORT:COMments?
            ```
        """
        return self._comments

    @property
    def detailedresults(self) -> DpojetReportDetailedresults:
        """Return the ``DPOJET:REPORT:DETailedresults`` command.

        Description:
            - This command turns on or off including detailed results in reports.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:DETailedresults?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:DETailedresults?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REPORT:DETailedresults value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:DETailedresults {1 | 0}
            - DPOJET:REPORT:DETailedresults?
            ```
        """
        return self._detailedresults

    @property
    def enablecomments(self) -> DpojetReportEnablecomments:
        """Return the ``DPOJET:REPORT:ENABlecomments`` command.

        Description:
            - This command sets or queries the comments enable or disable settings.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:ENABlecomments?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:ENABlecomments?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REPORT:ENABlecomments value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:ENABlecomments {1 | 0}
            - DPOJET:REPORT:ENABlecomments?
            ```
        """
        return self._enablecomments

    @property
    def getimage(self) -> DpojetReportGetimage:
        """Return the ``DPOJET:REPORT:GETIMAGE`` command.

        Description:
            - This command returns the image which is set using ``DPOJET:REPORT:SETIMAGEPath``
              command in binary format.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:GETIMAGE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:GETIMAGE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:GETIMAGE?
            ```
        """
        return self._getimage

    @property
    def getimagename(self) -> DpojetReportGetimagename:
        """Return the ``DPOJET:REPORT:GETIMAGEName`` command.

        Description:
            - This query only commands gets all the PNG format image names from this
              directoryC:Users<userName>TektronixTekApplicationsDPOJETReportsResources

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:GETIMAGEName?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:GETIMAGEName?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:GETIMAGEName?
            ```
        """
        return self._getimagename

    @property
    def getxmlreport(self) -> DpojetReportGetxmlreport:
        """Return the ``DPOJET:REPORT:GETXMLReport`` command.

        Description:
            - This query only command retrieve the report in binary format

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:GETXMLReport?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:GETXMLReport?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:GETXMLReport?
            ```
        """
        return self._getxmlreport

    @property
    def passfailresults(self) -> DpojetReportPassfailresults:
        """Return the ``DPOJET:REPORT:PASSFailresults`` command.

        Description:
            - This command turns on or off including pass/fail results in reports.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:PASSFailresults?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:PASSFailresults?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REPORT:PASSFailresults value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:PASSFailresults {1 | 0}
            - DPOJET:REPORT:PASSFailresults?
            ```
        """
        return self._passfailresults

    @property
    def plotimages(self) -> DpojetReportPlotimages:
        """Return the ``DPOJET:REPORT:PLOTimages`` command.

        Description:
            - This command turns on or off including detailed plot images in reports.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:PLOTimages?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:PLOTimages?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:PLOTimages value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:PLOTimages {1 | 0}
            - DPOJET:REPORT:PLOTimages?
            ```
        """
        return self._plotimages

    @property
    def reportname(self) -> DpojetReportReportname:
        """Return the ``DPOJET:REPORT:REPORTName`` command.

        Description:
            - This command sets the current report file name.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:REPORTName?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:REPORTName?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:REPORTName value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:REPORTName  <string>
            - DPOJET:REPORT:REPORTName?
            ```
        """
        return self._reportname

    @property
    def savewaveforms(self) -> DpojetReportSavewaveforms:
        """Return the ``DPOJET:REPORT:SAVEWaveforms`` command.

        Description:
            - This command turns on or off saving waveforms when a report save/append is invoked.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:SAVEWaveforms?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:SAVEWaveforms?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:SAVEWaveforms value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:SAVEWaveforms {1 | 0}
            - DPOJET:REPORT:SAVEWaveforms?
            ```
        """
        return self._savewaveforms

    @property
    def setimagepath(self) -> DpojetReportSetimagepath:
        """Return the ``DPOJET:REPORT:SETIMAGEPath`` command.

        Description:
            - This command sets the path of the image which you want to retreive using
              ``DPOJET:REPORT:GETIMAGE`` command.

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:SETIMAGEPath value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:SETIMAGEPath  <file string>
            ```
        """
        return self._setimagepath

    @property
    def setupconfig(self) -> DpojetReportSetupconfig:
        """Return the ``DPOJET:REPORT:SETupconfig`` command.

        Description:
            - This command turns on or off including setup configuration in reports.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:SETupconfig?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:SETupconfig?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:SETupconfig value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:SETupconfig {1 | 0}
            - DPOJET:REPORT:SETupconfig?
            ```
        """
        return self._setupconfig

    @property
    def state(self) -> DpojetReportState:
        """Return the ``DPOJET:REPORT:STATE`` command.

        Description:
            - This query-only command provides the report status.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:STATE?
            ```
        """
        return self._state

    @property
    def type(self) -> DpojetReportType:
        """Return the ``DPOJET:REPORT:TYPe`` command.

        Description:
            - This command sets or queries the report type.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:TYPe value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:TYPe {MHT|PDF}
            - DPOJET:REPORT:TYPe?
            ```
        """
        return self._type

    @property
    def viewreport(self) -> DpojetReportViewreport:
        """Return the ``DPOJET:REPORT:VIEWreport`` command.

        Description:
            - This command turns on or off viewing report after generation.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REPORT:VIEWreport?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REPORT:VIEWreport?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:REPORT:VIEWreport value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT:VIEWreport {1 | 0}
            - DPOJET:REPORT:VIEWreport?
            ```
        """
        return self._viewreport


class DpojetReflevelsChannelPercentRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:PERcent:RISEMid`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:PERcent:RISEMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:RISEMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:RISEMid value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:PERcent:RISEMid  <NR3>
        - DPOJET:REFLevels:CH<x>:PERcent:RISEMid?
        ```
    """


class DpojetReflevelsChannelPercentRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:PERcent:RISELow`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:PERcent:RISELow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:RISELow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:RISELow value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:PERcent:RISELow  <NR3>
        - DPOJET:REFLevels:CH<x>:PERcent:RISELow?
        ```
    """


class DpojetReflevelsChannelPercentRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:PERcent:RISEHigh`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:PERcent:RISEHigh?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:RISEHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:PERcent:RISEHigh  <NR3>
        - DPOJET:REFLevels:CH<x>:PERcent:RISEHigh?
        ```
    """


class DpojetReflevelsChannelPercentPercentreflevel(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel`` command.

    Description:
        - This command sets or gets the Reference Levels to Percentage or Absolute.The reflevel
          commands can be used to set ref levels for CH1-CH4, MATH1-MATH4, and REF1-REF4. The
          command syntax in OLH is shown only for CH<x>. Use MATH<x> and REF<x> for MATH1-MATH4, and
          REF1-REF4 (``DPOJET:REFLevels:MATH<x>`` and REF (``DPOJET:REFLevels:REF<x>``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel { 1 | 0 }
        - DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel?
        ```
    """


class DpojetReflevelsChannelPercentHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis`` command.

    Description:
        - This command sets the hysteresis value used for autoset.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis  <NR3>
        - DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis?
        ```
    """


class DpojetReflevelsChannelPercentFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:PERcent:FALLMid`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:PERcent:FALLMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:FALLMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:FALLMid value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:PERcent:FALLMid  <NR3>
        - DPOJET:REFLevels:CH<x>:PERcent:FALLMid?
        ```
    """


class DpojetReflevelsChannelPercentFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:PERcent:FALLLow`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:PERcent:FALLLow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:FALLLow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:FALLLow value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:PERcent:FALLLow  <NR3>
        - DPOJET:REFLevels:CH<x>:PERcent:FALLLow?
        ```
    """


class DpojetReflevelsChannelPercentFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:PERcent:FALLHigh`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:PERcent:FALLHigh?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:FALLHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:PERcent:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:PERcent:FALLHigh  <NR3>
        - DPOJET:REFLevels:CH<x>:PERcent:FALLHigh?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetReflevelsChannelPercent(SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:PERcent`` command.

    Description:
        - This query only command provide the reference level parameters in percentage such as set
          hysteresis values, Rise High Level, Rise Mid-Level, Rise Low Level, Fall High Level, Fall
          Mid-Level, Fall Low Level values each separated by comma in NR3 values. It also indicates
          the values are in percentage or absolute.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:PERcent?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels:CH<x>:PERcent?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:PERcent?
        ```

    Properties:
        - ``.fallhigh``: The ``DPOJET:REFLevels:CH<x>:PERcent:FALLHigh`` command.
        - ``.falllow``: The ``DPOJET:REFLevels:CH<x>:PERcent:FALLLow`` command.
        - ``.fallmid``: The ``DPOJET:REFLevels:CH<x>:PERcent:FALLMid`` command.
        - ``.hysteresis``: The ``DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis`` command.
        - ``.percentreflevel``: The ``DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel`` command.
        - ``.risehigh``: The ``DPOJET:REFLevels:CH<x>:PERcent:RISEHigh`` command.
        - ``.riselow``: The ``DPOJET:REFLevels:CH<x>:PERcent:RISELow`` command.
        - ``.risemid``: The ``DPOJET:REFLevels:CH<x>:PERcent:RISEMid`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = DpojetReflevelsChannelPercentFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = DpojetReflevelsChannelPercentFalllow(device, f"{self._cmd_syntax}:FALLLow")
        self._fallmid = DpojetReflevelsChannelPercentFallmid(device, f"{self._cmd_syntax}:FALLMid")
        self._hysteresis = DpojetReflevelsChannelPercentHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._percentreflevel = DpojetReflevelsChannelPercentPercentreflevel(
            device, f"{self._cmd_syntax}:PERCENTReflevel"
        )
        self._risehigh = DpojetReflevelsChannelPercentRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = DpojetReflevelsChannelPercentRiselow(device, f"{self._cmd_syntax}:RISELow")
        self._risemid = DpojetReflevelsChannelPercentRisemid(device, f"{self._cmd_syntax}:RISEMid")

    @property
    def fallhigh(self) -> DpojetReflevelsChannelPercentFallhigh:
        """Return the ``DPOJET:REFLevels:CH<x>:PERcent:FALLHigh`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:FALLHigh?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:PERcent:FALLHigh  <NR3>
            - DPOJET:REFLevels:CH<x>:PERcent:FALLHigh?
            ```
        """
        return self._fallhigh

    @property
    def falllow(self) -> DpojetReflevelsChannelPercentFalllow:
        """Return the ``DPOJET:REFLevels:CH<x>:PERcent:FALLLow`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:FALLLow?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:FALLLow value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:PERcent:FALLLow  <NR3>
            - DPOJET:REFLevels:CH<x>:PERcent:FALLLow?
            ```
        """
        return self._falllow

    @property
    def fallmid(self) -> DpojetReflevelsChannelPercentFallmid:
        """Return the ``DPOJET:REFLevels:CH<x>:PERcent:FALLMid`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:FALLMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:FALLMid value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:PERcent:FALLMid  <NR3>
            - DPOJET:REFLevels:CH<x>:PERcent:FALLMid?
            ```
        """
        return self._fallmid

    @property
    def hysteresis(self) -> DpojetReflevelsChannelPercentHysteresis:
        """Return the ``DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis`` command.

        Description:
            - This command sets the hysteresis value used for autoset.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis  <NR3>
            - DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis?
            ```
        """
        return self._hysteresis

    @property
    def percentreflevel(self) -> DpojetReflevelsChannelPercentPercentreflevel:
        """Return the ``DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel`` command.

        Description:
            - This command sets or gets the Reference Levels to Percentage or Absolute.The reflevel
              commands can be used to set ref levels for CH1-CH4, MATH1-MATH4, and REF1-REF4. The
              command syntax in OLH is shown only for CH<x>. Use MATH<x> and REF<x> for MATH1-MATH4,
              and REF1-REF4 (``DPOJET:REFLevels:MATH<x>`` and REF (``DPOJET:REFLevels:REF<x>``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel { 1 | 0 }
            - DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel?
            ```
        """
        return self._percentreflevel

    @property
    def risehigh(self) -> DpojetReflevelsChannelPercentRisehigh:
        """Return the ``DPOJET:REFLevels:CH<x>:PERcent:RISEHigh`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:RISEHigh?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:PERcent:RISEHigh  <NR3>
            - DPOJET:REFLevels:CH<x>:PERcent:RISEHigh?
            ```
        """
        return self._risehigh

    @property
    def riselow(self) -> DpojetReflevelsChannelPercentRiselow:
        """Return the ``DPOJET:REFLevels:CH<x>:PERcent:RISELow`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:RISELow?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:RISELow value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:PERcent:RISELow  <NR3>
            - DPOJET:REFLevels:CH<x>:PERcent:RISELow?
            ```
        """
        return self._riselow

    @property
    def risemid(self) -> DpojetReflevelsChannelPercentRisemid:
        """Return the ``DPOJET:REFLevels:CH<x>:PERcent:RISEMid`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:RISEMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:PERcent:RISEMid value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:PERcent:RISEMid  <NR3>
            - DPOJET:REFLevels:CH<x>:PERcent:RISEMid?
            ```
        """
        return self._risemid


class DpojetReflevelsChannelBasetop(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:BASETop`` command.

    Description:
        - This command sets the base-top method for autoset.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:BASETop?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels:CH<x>:BASETop?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REFLevels:CH<x>:BASETop value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:BASETop {MINMax | FULLhistogram | EYEhistogram | AUTO}
        - DPOJET:REFLevels:CH<x>:BASETop?
        ```
    """


class DpojetReflevelsChannelAutoset(SCPICmdWrite):
    """The ``DPOJET:REFLevels:CH<x>:AUTOSet`` command.

    Description:
        - This command sets or clears the reflevel autoset state of the given source. When set to 1,
          the given source will have a ref level autoset acted on it during the next acquisition.The
          Ref Level Autoset state is shown only for Ch1-Ch4 sources. It is the same for MATH and Ref
          waveforms. For example: ``DPOJET:REFLevels``: MATH<x>, ``DPOJET:REFLevels:REF<x>``.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:REFLevels:CH<x>:AUTOSet value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:AUTOSet {1 | 0}
        ```
    """


class DpojetReflevelsChannelAbsoluteRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:ABSolute:RISEMid`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset. The default is
          0.0.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:ABSolute:RISEMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:RISEMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:RISEMid value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:ABSolute:RISEMid  <NR3>
        - DPOJET:REFLevels:CH<x>:ABSolute:RISEMid?
        ```
    """


class DpojetReflevelsChannelAbsoluteRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:ABSolute:RISELow`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset. The default is
          -1.0.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:ABSolute:RISELow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:RISELow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:RISELow value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:ABSolute:RISELow  <NR3>
        - DPOJET:REFLevels:CH<x>:ABSolute:RISELow?
        ```
    """


class DpojetReflevelsChannelAbsoluteRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset. The default is
          1.0.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh  <NR3>
        - DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh?
        ```
    """


class DpojetReflevelsChannelAbsoluteHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis`` command.

    Description:
        - This command sets the hysteresis value used for autoset. The default is 0.03.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis  <NR3>
        - DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis?
        ```
    """


class DpojetReflevelsChannelAbsoluteFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:ABSolute:FALLMid`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset. The default is
          0.0.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:ABSolute:FALLMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:FALLMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:FALLMid value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:ABSolute:FALLMid  <NR3>
        - DPOJET:REFLevels:CH<x>:ABSolute:FALLMid?
        ```
    """


class DpojetReflevelsChannelAbsoluteFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:ABSolute:FALLLow`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset. The default is
          -1.1.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:ABSolute:FALLLow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:FALLLow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:FALLLow value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:ABSolute:FALLLow  <NR3>
        - DPOJET:REFLevels:CH<x>:ABSolute:FALLLow?
        ```
    """


class DpojetReflevelsChannelAbsoluteFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh`` command.

    Description:
        - This command sets the ref level voltage relative to base top for autoset. The default is
          1.0.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh  <NR3>
        - DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh?
        ```
    """


class DpojetReflevelsChannelAbsolute(SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>:ABSolute`` command.

    Description:
        - This query only command provide the reference level parameters in absolute voltage values
          such as set hysteresis , Rise High Level, Rise Mid-Level, Rise Low Level, Fall High Level,
          Fall Mid-Level, Fall Low Level, each separated by comma in NR3 values.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:ABSolute?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels:CH<x>:ABSolute?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:CH<x>:ABSolute?
        ```

    Properties:
        - ``.fallhigh``: The ``DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh`` command.
        - ``.falllow``: The ``DPOJET:REFLevels:CH<x>:ABSolute:FALLLow`` command.
        - ``.fallmid``: The ``DPOJET:REFLevels:CH<x>:ABSolute:FALLMid`` command.
        - ``.hysteresis``: The ``DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis`` command.
        - ``.risehigh``: The ``DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh`` command.
        - ``.riselow``: The ``DPOJET:REFLevels:CH<x>:ABSolute:RISELow`` command.
        - ``.risemid``: The ``DPOJET:REFLevels:CH<x>:ABSolute:RISEMid`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = DpojetReflevelsChannelAbsoluteFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = DpojetReflevelsChannelAbsoluteFalllow(device, f"{self._cmd_syntax}:FALLLow")
        self._fallmid = DpojetReflevelsChannelAbsoluteFallmid(device, f"{self._cmd_syntax}:FALLMid")
        self._hysteresis = DpojetReflevelsChannelAbsoluteHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = DpojetReflevelsChannelAbsoluteRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = DpojetReflevelsChannelAbsoluteRiselow(device, f"{self._cmd_syntax}:RISELow")
        self._risemid = DpojetReflevelsChannelAbsoluteRisemid(device, f"{self._cmd_syntax}:RISEMid")

    @property
    def fallhigh(self) -> DpojetReflevelsChannelAbsoluteFallhigh:
        """Return the ``DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset. The default
              is 1.0.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh  <NR3>
            - DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh?
            ```
        """
        return self._fallhigh

    @property
    def falllow(self) -> DpojetReflevelsChannelAbsoluteFalllow:
        """Return the ``DPOJET:REFLevels:CH<x>:ABSolute:FALLLow`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset. The default
              is -1.1.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:FALLLow?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:FALLLow value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:ABSolute:FALLLow  <NR3>
            - DPOJET:REFLevels:CH<x>:ABSolute:FALLLow?
            ```
        """
        return self._falllow

    @property
    def fallmid(self) -> DpojetReflevelsChannelAbsoluteFallmid:
        """Return the ``DPOJET:REFLevels:CH<x>:ABSolute:FALLMid`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset. The default
              is 0.0.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:FALLMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:FALLMid value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:ABSolute:FALLMid  <NR3>
            - DPOJET:REFLevels:CH<x>:ABSolute:FALLMid?
            ```
        """
        return self._fallmid

    @property
    def hysteresis(self) -> DpojetReflevelsChannelAbsoluteHysteresis:
        """Return the ``DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis`` command.

        Description:
            - This command sets the hysteresis value used for autoset. The default is 0.03.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis  <NR3>
            - DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis?
            ```
        """
        return self._hysteresis

    @property
    def risehigh(self) -> DpojetReflevelsChannelAbsoluteRisehigh:
        """Return the ``DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset. The default
              is 1.0.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh  <NR3>
            - DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh?
            ```
        """
        return self._risehigh

    @property
    def riselow(self) -> DpojetReflevelsChannelAbsoluteRiselow:
        """Return the ``DPOJET:REFLevels:CH<x>:ABSolute:RISELow`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset. The default
              is -1.0.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:RISELow?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:RISELow value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:ABSolute:RISELow  <NR3>
            - DPOJET:REFLevels:CH<x>:ABSolute:RISELow?
            ```
        """
        return self._riselow

    @property
    def risemid(self) -> DpojetReflevelsChannelAbsoluteRisemid:
        """Return the ``DPOJET:REFLevels:CH<x>:ABSolute:RISEMid`` command.

        Description:
            - This command sets the ref level voltage relative to base top for autoset. The default
              is 0.0.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:RISEMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:ABSolute:RISEMid value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:ABSolute:RISEMid  <NR3>
            - DPOJET:REFLevels:CH<x>:ABSolute:RISEMid?
            ```
        """
        return self._risemid


class DpojetReflevelsChannel(ValidatedChannel, SCPICmdRead):
    """The ``DPOJET:REFLevels:CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absolute``: The ``DPOJET:REFLevels:CH<x>:ABSolute`` command.
        - ``.autoset``: The ``DPOJET:REFLevels:CH<x>:AUTOSet`` command.
        - ``.basetop``: The ``DPOJET:REFLevels:CH<x>:BASETop`` command.
        - ``.percent``: The ``DPOJET:REFLevels:CH<x>:PERcent`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = DpojetReflevelsChannelAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._autoset = DpojetReflevelsChannelAutoset(device, f"{self._cmd_syntax}:AUTOSet")
        self._basetop = DpojetReflevelsChannelBasetop(device, f"{self._cmd_syntax}:BASETop")
        self._percent = DpojetReflevelsChannelPercent(device, f"{self._cmd_syntax}:PERcent")

    @property
    def absolute(self) -> DpojetReflevelsChannelAbsolute:
        """Return the ``DPOJET:REFLevels:CH<x>:ABSolute`` command.

        Description:
            - This query only command provide the reference level parameters in absolute voltage
              values such as set hysteresis , Rise High Level, Rise Mid-Level, Rise Low Level, Fall
              High Level, Fall Mid-Level, Fall Low Level, each separated by comma in NR3 values.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:ABSolute?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels:CH<x>:ABSolute?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:ABSolute?
            ```

        Sub-properties:
            - ``.fallhigh``: The ``DPOJET:REFLevels:CH<x>:ABSolute:FALLHigh`` command.
            - ``.falllow``: The ``DPOJET:REFLevels:CH<x>:ABSolute:FALLLow`` command.
            - ``.fallmid``: The ``DPOJET:REFLevels:CH<x>:ABSolute:FALLMid`` command.
            - ``.hysteresis``: The ``DPOJET:REFLevels:CH<x>:ABSolute:HYSTeresis`` command.
            - ``.risehigh``: The ``DPOJET:REFLevels:CH<x>:ABSolute:RISEHigh`` command.
            - ``.riselow``: The ``DPOJET:REFLevels:CH<x>:ABSolute:RISELow`` command.
            - ``.risemid``: The ``DPOJET:REFLevels:CH<x>:ABSolute:RISEMid`` command.
        """
        return self._absolute

    @property
    def autoset(self) -> DpojetReflevelsChannelAutoset:
        """Return the ``DPOJET:REFLevels:CH<x>:AUTOSet`` command.

        Description:
            - This command sets or clears the reflevel autoset state of the given source. When set
              to 1, the given source will have a ref level autoset acted on it during the next
              acquisition.The Ref Level Autoset state is shown only for Ch1-Ch4 sources. It is the
              same for MATH and Ref waveforms. For example: ``DPOJET:REFLevels``: MATH<x>,
              ``DPOJET:REFLevels:REF<x>``.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:AUTOSet value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:AUTOSet {1 | 0}
            ```
        """
        return self._autoset

    @property
    def basetop(self) -> DpojetReflevelsChannelBasetop:
        """Return the ``DPOJET:REFLevels:CH<x>:BASETop`` command.

        Description:
            - This command sets the base-top method for autoset.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:BASETop?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels:CH<x>:BASETop?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevels:CH<x>:BASETop value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:BASETop {MINMax | FULLhistogram | EYEhistogram | AUTO}
            - DPOJET:REFLevels:CH<x>:BASETop?
            ```
        """
        return self._basetop

    @property
    def percent(self) -> DpojetReflevelsChannelPercent:
        """Return the ``DPOJET:REFLevels:CH<x>:PERcent`` command.

        Description:
            - This query only command provide the reference level parameters in percentage such as
              set hysteresis values, Rise High Level, Rise Mid-Level, Rise Low Level, Fall High
              Level, Fall Mid-Level, Fall Low Level values each separated by comma in NR3 values. It
              also indicates the values are in percentage or absolute.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>:PERcent?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels:CH<x>:PERcent?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:CH<x>:PERcent?
            ```

        Sub-properties:
            - ``.fallhigh``: The ``DPOJET:REFLevels:CH<x>:PERcent:FALLHigh`` command.
            - ``.falllow``: The ``DPOJET:REFLevels:CH<x>:PERcent:FALLLow`` command.
            - ``.fallmid``: The ``DPOJET:REFLevels:CH<x>:PERcent:FALLMid`` command.
            - ``.hysteresis``: The ``DPOJET:REFLevels:CH<x>:PERcent:HYSTeresis`` command.
            - ``.percentreflevel``: The ``DPOJET:REFLevels:CH<x>:PERcent:PERCENTReflevel`` command.
            - ``.risehigh``: The ``DPOJET:REFLevels:CH<x>:PERcent:RISEHigh`` command.
            - ``.riselow``: The ``DPOJET:REFLevels:CH<x>:PERcent:RISELow`` command.
            - ``.risemid``: The ``DPOJET:REFLevels:CH<x>:PERcent:RISEMid`` command.
        """
        return self._percent


class DpojetReflevelsAutosetState(SCPICmdRead):
    """The ``DPOJET:REFLevels:AUTOset:STATE`` command.

    Description:
        - This query-only command provides the Ref Level Autoset status.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels:AUTOset:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels:AUTOset:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:AUTOset:STATE?
        ```
    """


class DpojetReflevelsAutoset(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevels:AUTOset`` command.

    Description:
        - This command performs a DPOJET ref level autoset on any sources selected using
          ``DPOJET:REFLevels:CH<x>:AUTOSet``.All pieces of the reflevel branch have the ability to
          set ref levels for CH1-CH4, MATH1-MATH4, and REF1-Ref4. Only the CH<x> portion is shown in
          this OLH, but it exists and matches exactly for MATH (``DPOJET:REFLevels:MATH<x>`` and REF
          (``DPOJET:REFLevels:REF<x>``).

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:REFLevels:AUTOset value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevels:AUTOset {EXECute}
        ```

    Properties:
        - ``.state``: The ``DPOJET:REFLevels:AUTOset:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DpojetReflevelsAutosetState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> DpojetReflevelsAutosetState:
        """Return the ``DPOJET:REFLevels:AUTOset:STATE`` command.

        Description:
            - This query-only command provides the Ref Level Autoset status.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REFLevels:AUTOset:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels:AUTOset:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:AUTOset:STATE?
            ```
        """
        return self._state


class DpojetReflevels(SCPICmdRead):
    """The ``DPOJET:REFLevels`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevels?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autoset``: The ``DPOJET:REFLevels:AUTOset`` command.
        - ``.ch``: The ``DPOJET:REFLevels:CH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoset = DpojetReflevelsAutoset(device, f"{self._cmd_syntax}:AUTOset")
        self._ch: Dict[int, DpojetReflevelsChannel] = DefaultDictPassKeyToFactory(
            lambda x: DpojetReflevelsChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def autoset(self) -> DpojetReflevelsAutoset:
        """Return the ``DPOJET:REFLevels:AUTOset`` command.

        Description:
            - This command performs a DPOJET ref level autoset on any sources selected using
              ``DPOJET:REFLevels:CH<x>:AUTOSet``.All pieces of the reflevel branch have the ability
              to set ref levels for CH1-CH4, MATH1-MATH4, and REF1-Ref4. Only the CH<x> portion is
              shown in this OLH, but it exists and matches exactly for MATH
              (``DPOJET:REFLevels:MATH<x>`` and REF (``DPOJET:REFLevels:REF<x>``).

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:REFLevels:AUTOset value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevels:AUTOset {EXECute}
            ```

        Sub-properties:
            - ``.state``: The ``DPOJET:REFLevels:AUTOset:STATE`` command.
        """
        return self._autoset

    @property
    def ch(self) -> Dict[int, DpojetReflevelsChannel]:
        """Return the ``DPOJET:REFLevels:CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REFLevels:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels:CH<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.absolute``: The ``DPOJET:REFLevels:CH<x>:ABSolute`` command.
            - ``.autoset``: The ``DPOJET:REFLevels:CH<x>:AUTOSet`` command.
            - ``.basetop``: The ``DPOJET:REFLevels:CH<x>:BASETop`` command.
            - ``.percent``: The ``DPOJET:REFLevels:CH<x>:PERcent`` command.
        """
        return self._ch


class DpojetReflevelChannelMidzero(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:REFLevel:CH<x>:MIDZero`` command.

    Description:
        - This command turns on or off the mid reference level voltage setting.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevel:CH<x>:MIDZero?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevel:CH<x>:MIDZero?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:REFLevel:CH<x>:MIDZero value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:REFLevel:CH<x>:MIDZero {1 | 0}
        - DPOJET:REFLevel:CH<x>:MIDZero?
        ```
    """


class DpojetReflevelChannel(ValidatedChannel, SCPICmdRead):
    """The ``DPOJET:REFLevel:CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevel:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevel:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.midzero``: The ``DPOJET:REFLevel:CH<x>:MIDZero`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._midzero = DpojetReflevelChannelMidzero(device, f"{self._cmd_syntax}:MIDZero")

    @property
    def midzero(self) -> DpojetReflevelChannelMidzero:
        """Return the ``DPOJET:REFLevel:CH<x>:MIDZero`` command.

        Description:
            - This command turns on or off the mid reference level voltage setting.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REFLevel:CH<x>:MIDZero?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevel:CH<x>:MIDZero?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:REFLevel:CH<x>:MIDZero value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REFLevel:CH<x>:MIDZero {1 | 0}
            - DPOJET:REFLevel:CH<x>:MIDZero?
            ```
        """
        return self._midzero


class DpojetReflevel(SCPICmdRead):
    """The ``DPOJET:REFLevel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:REFLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``DPOJET:REFLevel:CH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, DpojetReflevelChannel] = DefaultDictPassKeyToFactory(
            lambda x: DpojetReflevelChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, DpojetReflevelChannel]:
        """Return the ``DPOJET:REFLevel:CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REFLevel:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevel:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.midzero``: The ``DPOJET:REFLevel:CH<x>:MIDZero`` command.
        """
        return self._ch


class DpojetQualifyState(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:QUALify:STATE`` command.

    Description:
        - This command turns on or off measurement qualification.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:QUALify:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:QUALify:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:QUALify:STATE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:QUALify:STATE {1 | 0}
        - DPOJET:QUALify:STATE?
        ```
    """


class DpojetQualifySource(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:QUALify:SOUrce`` command.

    Description:
        - This command sets the qualifier source.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:QUALify:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:QUALify:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:QUALify:SOUrce value`` command.

    SCPI Syntax:
        ```
        - DPOJET:QUALify:SOUrce {CH1 - CH4 | MATH1 - MATH4 | REF1 - REF4 | SEARCH0 - SEARCH8}
        - DPOJET:QUALify:SOUrce?
        ```
    """


class DpojetQualifyActive(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:QUALify:ACTIVE`` command.

    Description:
        - This command sets the active state for the qualifier source, either HIGH or LOW.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:QUALify:ACTIVE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:QUALify:ACTIVE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:QUALify:ACTIVE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:QUALify:ACTIVE {HIGH | LOW}
        - DPOJET:QUALify:ACTIVE?
        ```
    """


class DpojetQualify(SCPICmdRead):
    """The ``DPOJET:QUALify`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:QUALify?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:QUALify?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.active``: The ``DPOJET:QUALify:ACTIVE`` command.
        - ``.source``: The ``DPOJET:QUALify:SOUrce`` command.
        - ``.state``: The ``DPOJET:QUALify:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._active = DpojetQualifyActive(device, f"{self._cmd_syntax}:ACTIVE")
        self._source = DpojetQualifySource(device, f"{self._cmd_syntax}:SOUrce")
        self._state = DpojetQualifyState(device, f"{self._cmd_syntax}:STATE")

    @property
    def active(self) -> DpojetQualifyActive:
        """Return the ``DPOJET:QUALify:ACTIVE`` command.

        Description:
            - This command sets the active state for the qualifier source, either HIGH or LOW.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:QUALify:ACTIVE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:QUALify:ACTIVE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:QUALify:ACTIVE value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:QUALify:ACTIVE {HIGH | LOW}
            - DPOJET:QUALify:ACTIVE?
            ```
        """
        return self._active

    @property
    def source(self) -> DpojetQualifySource:
        """Return the ``DPOJET:QUALify:SOUrce`` command.

        Description:
            - This command sets the qualifier source.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:QUALify:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:QUALify:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:QUALify:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:QUALify:SOUrce {CH1 - CH4 | MATH1 - MATH4 | REF1 - REF4 | SEARCH0 - SEARCH8}
            - DPOJET:QUALify:SOUrce?
            ```
        """
        return self._source

    @property
    def state(self) -> DpojetQualifyState:
        """Return the ``DPOJET:QUALify:STATE`` command.

        Description:
            - This command turns on or off measurement qualification.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:QUALify:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:QUALify:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:QUALify:STATE value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:QUALify:STATE {1 | 0}
            - DPOJET:QUALify:STATE?
            ```
        """
        return self._state


class DpojetPopulationState(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:POPULATION:STATE`` command.

    Description:
        - This command turns on or off population limits.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:POPULATION:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:POPULATION:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:POPULATION:STATE value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:POPULATION:STATE {1 | 0}
        - DPOJET:POPULATION:STATE?
        ```
    """


class DpojetPopulationLimitby(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:POPULATION:LIMITBY`` command.

    Description:
        - This command sets or queries the mechanism by limits, either acquisition or population.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:POPULATION:LIMITBY?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:POPULATION:LIMITBY?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:POPULATION:LIMITBY value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:POPULATION:LIMITBY {ACQuisitions | POPUlation}
        - DPOJET:POPULATION:LIMITBY?
        ```
    """


class DpojetPopulationLimit(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:POPULATION:LIMIT`` command.

    Description:
        - This command sets or queries the current limit value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:POPULATION:LIMIT?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:POPULATION:LIMIT?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:POPULATION:LIMIT value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:POPULATION:LIMIT  <NR3>
        - DPOJET:POPULATION:LIMIT?
        ```
    """


class DpojetPopulationCondition(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:POPULATION:CONDition`` command.

    Description:
        - This command sets or queries the current population limit condition.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:POPULATION:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:POPULATION:CONDition?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:POPULATION:CONDition value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:POPULATION:CONDition {EACHmeas | LASTmeas}
        - DPOJET:POPULATION:CONDition?
        ```
    """


class DpojetPopulation(SCPICmdRead):
    """The ``DPOJET:POPULATION`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:POPULATION?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:POPULATION?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``DPOJET:POPULATION:CONDition`` command.
        - ``.limit``: The ``DPOJET:POPULATION:LIMIT`` command.
        - ``.limitby``: The ``DPOJET:POPULATION:LIMITBY`` command.
        - ``.state``: The ``DPOJET:POPULATION:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = DpojetPopulationCondition(device, f"{self._cmd_syntax}:CONDition")
        self._limit = DpojetPopulationLimit(device, f"{self._cmd_syntax}:LIMIT")
        self._limitby = DpojetPopulationLimitby(device, f"{self._cmd_syntax}:LIMITBY")
        self._state = DpojetPopulationState(device, f"{self._cmd_syntax}:STATE")

    @property
    def condition(self) -> DpojetPopulationCondition:
        """Return the ``DPOJET:POPULATION:CONDition`` command.

        Description:
            - This command sets or queries the current population limit condition.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:POPULATION:CONDition?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:POPULATION:CONDition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:POPULATION:CONDition value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:POPULATION:CONDition {EACHmeas | LASTmeas}
            - DPOJET:POPULATION:CONDition?
            ```
        """
        return self._condition

    @property
    def limit(self) -> DpojetPopulationLimit:
        """Return the ``DPOJET:POPULATION:LIMIT`` command.

        Description:
            - This command sets or queries the current limit value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:POPULATION:LIMIT?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:POPULATION:LIMIT?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:POPULATION:LIMIT value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:POPULATION:LIMIT  <NR3>
            - DPOJET:POPULATION:LIMIT?
            ```
        """
        return self._limit

    @property
    def limitby(self) -> DpojetPopulationLimitby:
        """Return the ``DPOJET:POPULATION:LIMITBY`` command.

        Description:
            - This command sets or queries the mechanism by limits, either acquisition or
              population.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:POPULATION:LIMITBY?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:POPULATION:LIMITBY?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:POPULATION:LIMITBY value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:POPULATION:LIMITBY {ACQuisitions | POPUlation}
            - DPOJET:POPULATION:LIMITBY?
            ```
        """
        return self._limitby

    @property
    def state(self) -> DpojetPopulationState:
        """Return the ``DPOJET:POPULATION:STATE`` command.

        Description:
            - This command turns on or off population limits.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:POPULATION:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:POPULATION:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:POPULATION:STATE value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:POPULATION:STATE {1 | 0}
            - DPOJET:POPULATION:STATE?
            ```
        """
        return self._state


class DpojetPlotItemYunits(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:YUnits`` command.

    Description:
        - This query-only command returns Y units of the plot as a string.Plot units depends on the
          measurement type.Click here to see the possible

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:YUnits?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:YUnits?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:YUnits?
        ```
    """


class DpojetPlotItemXunits(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:XUnits`` command.

    Description:
        - This query-only command returns X units of the plot as a string.Plot units depends on the
          measurement type.Click here to see the possible

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:XUnits?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:XUnits?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:XUnits?
        ```
    """


class DpojetPlotItemVertbathtubYaxisunits(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits`` command.

    Description:
        - This command sets or queries the Y-axis unit for noise bathtube.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits {VOLTs | UNITAMPLITUDES}
        - DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits?
        ```
    """


class DpojetPlotItemVertbathtubHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE`` command.

    Description:
        - This command sets or queries the horizontal scale setting for applicable plots, either
          Linear or Log.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE {LINEAR | LOG}
        - DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE?
        ```
    """


class DpojetPlotItemVertbathtubHorizontal(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DpojetPlotItemVertbathtubHorizontalScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DpojetPlotItemVertbathtubHorizontalScale:
        """Return the ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE`` command.

        Description:
            - This command sets or queries the horizontal scale setting for applicable plots, either
              Linear or Log.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE {LINEAR | LOG}
            - DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE?
            ```
        """
        return self._scale


class DpojetPlotItemVertbathtubBer(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:VERTBATHtub:BER`` command.

    Description:
        - This command sets or queries the noise bathtub BER value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub:BER?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub:BER?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub:BER value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:VERTBATHtub:BER   <NR3>
        - DPOJET:PLOT<x>:VERTBATHtub:BER?
        ```
    """


class DpojetPlotItemVertbathtub(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:VERTBATHtub`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ber``: The ``DPOJET:PLOT<x>:VERTBATHtub:BER`` command.
        - ``.horizontal``: The ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal`` command tree.
        - ``.yaxisunits``: The ``DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ber = DpojetPlotItemVertbathtubBer(device, f"{self._cmd_syntax}:BER")
        self._horizontal = DpojetPlotItemVertbathtubHorizontal(
            device, f"{self._cmd_syntax}:HORizontal"
        )
        self._yaxisunits = DpojetPlotItemVertbathtubYaxisunits(
            device, f"{self._cmd_syntax}:YAXISUnits"
        )

    @property
    def ber(self) -> DpojetPlotItemVertbathtubBer:
        """Return the ``DPOJET:PLOT<x>:VERTBATHtub:BER`` command.

        Description:
            - This command sets or queries the noise bathtub BER value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub:BER?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub:BER?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:VERTBATHtub:BER value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:VERTBATHtub:BER   <NR3>
            - DPOJET:PLOT<x>:VERTBATHtub:BER?
            ```
        """
        return self._ber

    @property
    def horizontal(self) -> DpojetPlotItemVertbathtubHorizontal:
        """Return the ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal:SCALE`` command.
        """
        return self._horizontal

    @property
    def yaxisunits(self) -> DpojetPlotItemVertbathtubYaxisunits:
        """Return the ``DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits`` command.

        Description:
            - This command sets or queries the Y-axis unit for noise bathtube.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits {VOLTs | UNITAMPLITUDES}
            - DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits?
            ```
        """
        return self._yaxisunits


class DpojetPlotItemType(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TYPe`` command.

    Description:
        - This query-only command returns the current plot type for the selected plot.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:TYPe?
        ```
    """


class DpojetPlotItemTrendType(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TREND:TYPe`` command.

    Description:
        - This command sets or queries the trend type setting for Trend plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TREND:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TREND:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:TREND:TYPe value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:TREND:TYPe {VECTOR | BAR}
        - DPOJET:PLOT<x>:TREND:TYPe?
        ```
    """


class DpojetPlotItemTrend(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TREND`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TREND?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TREND?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.type``: The ``DPOJET:PLOT<x>:TREND:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._type = DpojetPlotItemTrendType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def type(self) -> DpojetPlotItemTrendType:
        """Return the ``DPOJET:PLOT<x>:TREND:TYPe`` command.

        Description:
            - This command sets or queries the trend type setting for Trend plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TREND:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TREND:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:TREND:TYPe value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:TREND:TYPe {VECTOR | BAR}
            - DPOJET:PLOT<x>:TREND:TYPe?
            ```
        """
        return self._type


class DpojetPlotItemTransferVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE`` command.

    Description:
        - This command sets or queries the vertical scale setting for applicable plots, either
          Linear or Log. Undefined for non-transfer plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE {LINEAR | LOG}
        - DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE?
        ```
    """


class DpojetPlotItemTransferVertical(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TRANSfer:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TRANSfer:VERTical?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DpojetPlotItemTransferVerticalScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DpojetPlotItemTransferVerticalScale:
        """Return the ``DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE`` command.

        Description:
            - This command sets or queries the vertical scale setting for applicable plots, either
              Linear or Log. Undefined for non-transfer plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE {LINEAR | LOG}
            - DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE?
            ```
        """
        return self._scale


class DpojetPlotItemTransferNumerator(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TRANSfer:NUMerator`` command.

    Description:
        - This command sets or queries the transfer plot numerator.Undefined for nontransfer plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:NUMerator?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TRANSfer:NUMerator?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:TRANSfer:NUMerator value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:TRANSfer:NUMerator {MEAS1 - MEAS99}
        - DPOJET:PLOT<x>:TRANSfer:NUMerator?
        ```
    """


class DpojetPlotItemTransferMode(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TRANSfer:MODE`` command.

    Description:
        - This command sets or queries the transfer plot mode.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TRANSfer:MODE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:TRANSfer:MODE value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:TRANSfer:MODE {NORMal | AVErage}
        - DPOJET:PLOT<x>:TRANSfer:MODE?
        ```
    """


class DpojetPlotItemTransferHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE`` command.

    Description:
        - This command sets or queries the horizontal scale setting for applicable plots, either
          Linear or Log. Undefined for nontransfer plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE {LINEAR | LOG}
        - DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE?
        ```
    """


class DpojetPlotItemTransferHorizontal(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TRANSfer:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TRANSfer:HORizontal?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DpojetPlotItemTransferHorizontalScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DpojetPlotItemTransferHorizontalScale:
        """Return the ``DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE`` command.

        Description:
            - This command sets or queries the horizontal scale setting for applicable plots, either
              Linear or Log. Undefined for nontransfer plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE {LINEAR | LOG}
            - DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE?
            ```
        """
        return self._scale


class DpojetPlotItemTransferDenominator(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TRANSfer:DENominator`` command.

    Description:
        - This command sets or queries the transfer plot denominator.Undefined for non-transfer
          plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:DENominator?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TRANSfer:DENominator?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:TRANSfer:DENominator value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:TRANSfer:DENominator {MEAS1 - MEAS99}
        - DPOJET:PLOT<x>:TRANSfer:DENominator?
        ```
    """


class DpojetPlotItemTransfer(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TRANSfer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TRANSfer?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.denominator``: The ``DPOJET:PLOT<x>:TRANSfer:DENominator`` command.
        - ``.horizontal``: The ``DPOJET:PLOT<x>:TRANSfer:HORizontal`` command tree.
        - ``.mode``: The ``DPOJET:PLOT<x>:TRANSfer:MODE`` command.
        - ``.numerator``: The ``DPOJET:PLOT<x>:TRANSfer:NUMerator`` command.
        - ``.vertical``: The ``DPOJET:PLOT<x>:TRANSfer:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._denominator = DpojetPlotItemTransferDenominator(
            device, f"{self._cmd_syntax}:DENominator"
        )
        self._horizontal = DpojetPlotItemTransferHorizontal(
            device, f"{self._cmd_syntax}:HORizontal"
        )
        self._mode = DpojetPlotItemTransferMode(device, f"{self._cmd_syntax}:MODE")
        self._numerator = DpojetPlotItemTransferNumerator(device, f"{self._cmd_syntax}:NUMerator")
        self._vertical = DpojetPlotItemTransferVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def denominator(self) -> DpojetPlotItemTransferDenominator:
        """Return the ``DPOJET:PLOT<x>:TRANSfer:DENominator`` command.

        Description:
            - This command sets or queries the transfer plot denominator.Undefined for non-transfer
              plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:DENominator?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:DENominator?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:DENominator value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:TRANSfer:DENominator {MEAS1 - MEAS99}
            - DPOJET:PLOT<x>:TRANSfer:DENominator?
            ```
        """
        return self._denominator

    @property
    def horizontal(self) -> DpojetPlotItemTransferHorizontal:
        """Return the ``DPOJET:PLOT<x>:TRANSfer:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DPOJET:PLOT<x>:TRANSfer:HORizontal:SCALE`` command.
        """
        return self._horizontal

    @property
    def mode(self) -> DpojetPlotItemTransferMode:
        """Return the ``DPOJET:PLOT<x>:TRANSfer:MODE`` command.

        Description:
            - This command sets or queries the transfer plot mode.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TRANSfer:MODE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:MODE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:TRANSfer:MODE {NORMal | AVErage}
            - DPOJET:PLOT<x>:TRANSfer:MODE?
            ```
        """
        return self._mode

    @property
    def numerator(self) -> DpojetPlotItemTransferNumerator:
        """Return the ``DPOJET:PLOT<x>:TRANSfer:NUMerator`` command.

        Description:
            - This command sets or queries the transfer plot numerator.Undefined for nontransfer
              plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:NUMerator?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:NUMerator?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:NUMerator value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:TRANSfer:NUMerator {MEAS1 - MEAS99}
            - DPOJET:PLOT<x>:TRANSfer:NUMerator?
            ```
        """
        return self._numerator

    @property
    def vertical(self) -> DpojetPlotItemTransferVertical:
        """Return the ``DPOJET:PLOT<x>:TRANSfer:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer:VERTical?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:TRANSfer:VERTical?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DPOJET:PLOT<x>:TRANSfer:VERTical:SCALE`` command.
        """
        return self._vertical


class DpojetPlotItemTotaluisanalyzed(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TOTALUISAnalyzed`` command.

    Description:
        - This command queries the total UIs analysed for Eye Diagram plot.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TOTALUISAnalyzed?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TOTALUISAnalyzed?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:TOTALUISAnalyzed?
        ```
    """


class DpojetPlotItemTotaluisacquired(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:TOTALUISAcquired`` command.

    Description:
        - This command queries the total UIs acquired for Eye Diagram plot

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TOTALUISAcquired?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TOTALUISAcquired?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:TOTALUISAcquired?
        ```
    """


class DpojetPlotItemSpectrumVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE`` command.

    Description:
        - This command sets or queries the vertical scale setting for applicable plots, either
          Linear or Log.Undefined for nonspectrum plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE {LINEAR | LOG}
        - DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE?
        ```
    """


class DpojetPlotItemSpectrumVertical(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:SPECtrum:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:SPECtrum:VERTical?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DpojetPlotItemSpectrumVerticalScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DpojetPlotItemSpectrumVerticalScale:
        """Return the ``DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE`` command.

        Description:
            - This command sets or queries the vertical scale setting for applicable plots, either
              Linear or Log.Undefined for nonspectrum plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE {LINEAR | LOG}
            - DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE?
            ```
        """
        return self._scale


class DpojetPlotItemSpectrumMode(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:SPECtrum:MODE`` command.

    Description:
        - This command sets or queries the spectrum mode.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:SPECtrum:MODE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:SPECtrum:MODE value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:SPECtrum:MODE {NORMal | AVErage | PEAKhold}
        - DPOJET:PLOT<x>:SPECtrum:MODE?
        ```
    """


class DpojetPlotItemSpectrumHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE`` command.

    Description:
        - This command sets or queries the horizontal scale setting for applicable plots, either
          Linear or Log.Undefined for nonspectrum plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE {LINEAR | LOG}
        - DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE?
        ```
    """


class DpojetPlotItemSpectrumHorizontal(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:SPECtrum:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:SPECtrum:HORizontal?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DpojetPlotItemSpectrumHorizontalScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DpojetPlotItemSpectrumHorizontalScale:
        """Return the ``DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE`` command.

        Description:
            - This command sets or queries the horizontal scale setting for applicable plots, either
              Linear or Log.Undefined for nonspectrum plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE {LINEAR | LOG}
            - DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE?
            ```
        """
        return self._scale


class DpojetPlotItemSpectrumBase(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:SPECtrum:BASE`` command.

    Description:
        - This command sets or queries the spectrum base. Undefined for non-spectrum plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum:BASE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:SPECtrum:BASE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:SPECtrum:BASE value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:SPECtrum:BASE  <NR3>
        - DPOJET:PLOT<x>:SPECtrum:BASE?
        ```
    """


class DpojetPlotItemSpectrum(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:SPECtrum`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:SPECtrum?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.base``: The ``DPOJET:PLOT<x>:SPECtrum:BASE`` command.
        - ``.horizontal``: The ``DPOJET:PLOT<x>:SPECtrum:HORizontal`` command tree.
        - ``.mode``: The ``DPOJET:PLOT<x>:SPECtrum:MODE`` command.
        - ``.vertical``: The ``DPOJET:PLOT<x>:SPECtrum:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._base = DpojetPlotItemSpectrumBase(device, f"{self._cmd_syntax}:BASE")
        self._horizontal = DpojetPlotItemSpectrumHorizontal(
            device, f"{self._cmd_syntax}:HORizontal"
        )
        self._mode = DpojetPlotItemSpectrumMode(device, f"{self._cmd_syntax}:MODE")
        self._vertical = DpojetPlotItemSpectrumVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def base(self) -> DpojetPlotItemSpectrumBase:
        """Return the ``DPOJET:PLOT<x>:SPECtrum:BASE`` command.

        Description:
            - This command sets or queries the spectrum base. Undefined for non-spectrum plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum:BASE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:SPECtrum:BASE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:SPECtrum:BASE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:SPECtrum:BASE  <NR3>
            - DPOJET:PLOT<x>:SPECtrum:BASE?
            ```
        """
        return self._base

    @property
    def horizontal(self) -> DpojetPlotItemSpectrumHorizontal:
        """Return the ``DPOJET:PLOT<x>:SPECtrum:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:SPECtrum:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DPOJET:PLOT<x>:SPECtrum:HORizontal:SCALE`` command.
        """
        return self._horizontal

    @property
    def mode(self) -> DpojetPlotItemSpectrumMode:
        """Return the ``DPOJET:PLOT<x>:SPECtrum:MODE`` command.

        Description:
            - This command sets or queries the spectrum mode.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:SPECtrum:MODE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:SPECtrum:MODE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:SPECtrum:MODE {NORMal | AVErage | PEAKhold}
            - DPOJET:PLOT<x>:SPECtrum:MODE?
            ```
        """
        return self._mode

    @property
    def vertical(self) -> DpojetPlotItemSpectrumVertical:
        """Return the ``DPOJET:PLOT<x>:SPECtrum:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum:VERTical?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:SPECtrum:VERTical?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DPOJET:PLOT<x>:SPECtrum:VERTical:SCALE`` command.
        """
        return self._vertical


class DpojetPlotItemSource(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:SOUrce`` command.

    Description:
        - This query-only command returns the source measurement for the selected plot.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:SOUrce?
        ```
    """


class DpojetPlotItemPhasenoiseSmootheningfilter(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter`` command.

    Description:
        - This command sets or queries the phase noise plot smoothing filter.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter {ONEBYHUNDREDTHdecade | ONEBYTENTHDECADE | ONEDECADE}
        - DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter?
        ```
    """  # noqa: E501


class DpojetPlotItemPhasenoiseBaseline(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:PHASEnoise:BASEline`` command.

    Description:
        - This command sets or queries the phase noise baseline.Undefined for nonphase-noise plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PHASEnoise:BASEline?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PHASEnoise:BASEline?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:PHASEnoise:BASEline value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:PHASEnoise:BASEline  <NR3>
        - DPOJET:PLOT<x>:PHASEnoise:BASEline?
        ```
    """


class DpojetPlotItemPhasenoise(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:PHASEnoise`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PHASEnoise?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PHASEnoise?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.baseline``: The ``DPOJET:PLOT<x>:PHASEnoise:BASEline`` command.
        - ``.smootheningfilter``: The ``DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._baseline = DpojetPlotItemPhasenoiseBaseline(device, f"{self._cmd_syntax}:BASEline")
        self._smootheningfilter = DpojetPlotItemPhasenoiseSmootheningfilter(
            device, f"{self._cmd_syntax}:SMOOTHENINGFilter"
        )

    @property
    def baseline(self) -> DpojetPlotItemPhasenoiseBaseline:
        """Return the ``DPOJET:PLOT<x>:PHASEnoise:BASEline`` command.

        Description:
            - This command sets or queries the phase noise baseline.Undefined for nonphase-noise
              plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PHASEnoise:BASEline?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:PHASEnoise:BASEline?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:PHASEnoise:BASEline value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:PHASEnoise:BASEline  <NR3>
            - DPOJET:PLOT<x>:PHASEnoise:BASEline?
            ```
        """
        return self._baseline

    @property
    def smootheningfilter(self) -> DpojetPlotItemPhasenoiseSmootheningfilter:
        """Return the ``DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter`` command.

        Description:
            - This command sets or queries the phase noise plot smoothing filter.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter {ONEBYHUNDREDTHdecade | ONEBYTENTHDECADE | ONEDECADE}
            - DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter?
            ```
        """  # noqa: E501
        return self._smootheningfilter


class DpojetPlotItemPdfeyeTargetber(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:PDFEye:TARGETBER`` command.

    Description:
        - This command sets or queries the TARGETBER Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:TARGETBER?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:TARGETBER?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:TARGETBER value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:PDFEye:TARGETBER {1 | 0}
        - DPOJET:PLOT<x>:PDFEye:TARGETBER?
        ```
    """


class DpojetPlotItemPdfeyeBer1e9v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:PDFEye:BER1E9V`` command.

    Description:
        - This command sets or queries the BER1E9 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E9V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E9V?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E9V value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:PDFEye:BER1E9V {1 | 0}
        - DPOJET:PLOT<x>:PDFEye:BER1E9V?
        ```
    """


class DpojetPlotItemPdfeyeBer1e6v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:PDFEye:BER1E6V`` command.

    Description:
        - This command sets or queries the BER1E6 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E6V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E6V?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E6V value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:PDFEye:BER1E6V {1 | 0}
        - DPOJET:PLOT<x>:PDFEye:BER1E6V?
        ```
    """


class DpojetPlotItemPdfeyeBer1e18v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:PDFEye:BER1E18V`` command.

    Description:
        - This command sets or queries the BER1E18 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E18V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E18V?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E18V value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:PDFEye:BER1E18V {1 | 0}
        - DPOJET:PLOT<x>:PDFEye:BER1E18V?
        ```
    """


class DpojetPlotItemPdfeyeBer1e15v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:PDFEye:BER1E15V`` command.

    Description:
        - This command sets or queries the BER1E15 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E15V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E15V?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E15V value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:PDFEye:BER1E15V {1 | 0}
        - DPOJET:PLOT<x>:PDFEye:BER1E15V?
        ```
    """


class DpojetPlotItemPdfeyeBer1e12v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:PDFEye:BER1E12V`` command.

    Description:
        - This command sets or queries the BER1E12 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E12V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E12V?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E12V value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:PDFEye:BER1E12V {1 | 0}
        - DPOJET:PLOT<x>:PDFEye:BER1E12V?
        ```
    """


class DpojetPlotItemPdfeye(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:PDFEye`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ber1e12v``: The ``DPOJET:PLOT<x>:PDFEye:BER1E12V`` command.
        - ``.ber1e15v``: The ``DPOJET:PLOT<x>:PDFEye:BER1E15V`` command.
        - ``.ber1e18v``: The ``DPOJET:PLOT<x>:PDFEye:BER1E18V`` command.
        - ``.ber1e6v``: The ``DPOJET:PLOT<x>:PDFEye:BER1E6V`` command.
        - ``.ber1e9v``: The ``DPOJET:PLOT<x>:PDFEye:BER1E9V`` command.
        - ``.targetber``: The ``DPOJET:PLOT<x>:PDFEye:TARGETBER`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ber1e12v = DpojetPlotItemPdfeyeBer1e12v(device, f"{self._cmd_syntax}:BER1E12V")
        self._ber1e15v = DpojetPlotItemPdfeyeBer1e15v(device, f"{self._cmd_syntax}:BER1E15V")
        self._ber1e18v = DpojetPlotItemPdfeyeBer1e18v(device, f"{self._cmd_syntax}:BER1E18V")
        self._ber1e6v = DpojetPlotItemPdfeyeBer1e6v(device, f"{self._cmd_syntax}:BER1E6V")
        self._ber1e9v = DpojetPlotItemPdfeyeBer1e9v(device, f"{self._cmd_syntax}:BER1E9V")
        self._targetber = DpojetPlotItemPdfeyeTargetber(device, f"{self._cmd_syntax}:TARGETBER")

    @property
    def ber1e12v(self) -> DpojetPlotItemPdfeyeBer1e12v:
        """Return the ``DPOJET:PLOT<x>:PDFEye:BER1E12V`` command.

        Description:
            - This command sets or queries the BER1E12 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E12V?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E12V?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:PDFEye:BER1E12V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:PDFEye:BER1E12V {1 | 0}
            - DPOJET:PLOT<x>:PDFEye:BER1E12V?
            ```
        """
        return self._ber1e12v

    @property
    def ber1e15v(self) -> DpojetPlotItemPdfeyeBer1e15v:
        """Return the ``DPOJET:PLOT<x>:PDFEye:BER1E15V`` command.

        Description:
            - This command sets or queries the BER1E15 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E15V?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E15V?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:PDFEye:BER1E15V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:PDFEye:BER1E15V {1 | 0}
            - DPOJET:PLOT<x>:PDFEye:BER1E15V?
            ```
        """
        return self._ber1e15v

    @property
    def ber1e18v(self) -> DpojetPlotItemPdfeyeBer1e18v:
        """Return the ``DPOJET:PLOT<x>:PDFEye:BER1E18V`` command.

        Description:
            - This command sets or queries the BER1E18 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E18V?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E18V?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:PDFEye:BER1E18V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:PDFEye:BER1E18V {1 | 0}
            - DPOJET:PLOT<x>:PDFEye:BER1E18V?
            ```
        """
        return self._ber1e18v

    @property
    def ber1e6v(self) -> DpojetPlotItemPdfeyeBer1e6v:
        """Return the ``DPOJET:PLOT<x>:PDFEye:BER1E6V`` command.

        Description:
            - This command sets or queries the BER1E6 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E6V?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E6V?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:PDFEye:BER1E6V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:PDFEye:BER1E6V {1 | 0}
            - DPOJET:PLOT<x>:PDFEye:BER1E6V?
            ```
        """
        return self._ber1e6v

    @property
    def ber1e9v(self) -> DpojetPlotItemPdfeyeBer1e9v:
        """Return the ``DPOJET:PLOT<x>:PDFEye:BER1E9V`` command.

        Description:
            - This command sets or queries the BER1E9 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E9V?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:BER1E9V?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:PDFEye:BER1E9V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:PDFEye:BER1E9V {1 | 0}
            - DPOJET:PLOT<x>:PDFEye:BER1E9V?
            ```
        """
        return self._ber1e9v

    @property
    def targetber(self) -> DpojetPlotItemPdfeyeTargetber:
        """Return the ``DPOJET:PLOT<x>:PDFEye:TARGETBER`` command.

        Description:
            - This command sets or queries the TARGETBER Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye:TARGETBER?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye:TARGETBER?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:PDFEye:TARGETBER value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:PDFEye:TARGETBER {1 | 0}
            - DPOJET:PLOT<x>:PDFEye:TARGETBER?
            ```
        """
        return self._targetber


class DpojetPlotItemNoisebathtubYaxisunits(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits`` command.

    Description:
        - This command sets or queries the Y-Axis Units of Noise Bathtub.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits { UNITAmplitudes | VOLTs }
        - DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits?
        ```
    """


class DpojetPlotItemNoisebathtub(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:NOISEBATHtub`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:NOISEBATHtub?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:NOISEBATHtub?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.yaxisunits``: The ``DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._yaxisunits = DpojetPlotItemNoisebathtubYaxisunits(
            device, f"{self._cmd_syntax}:YAXISUnits"
        )

    @property
    def yaxisunits(self) -> DpojetPlotItemNoisebathtubYaxisunits:
        """Return the ``DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits`` command.

        Description:
            - This command sets or queries the Y-Axis Units of Noise Bathtub.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits { UNITAmplitudes | VOLTs }
            - DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits?
            ```
        """
        return self._yaxisunits


class DpojetPlotItemHistogramVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE`` command.

    Description:
        - This command sets or queries the vertical scale setting for applicable plots, either
          Linear or Log.Undefined for nonhistogram plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE {LINEAR | LOG}
        - DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE?
        ```
    """


class DpojetPlotItemHistogramVertical(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:HISTOgram:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:HISTOgram:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:HISTOgram:VERTical?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DpojetPlotItemHistogramVerticalScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DpojetPlotItemHistogramVerticalScale:
        """Return the ``DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE`` command.

        Description:
            - This command sets or queries the vertical scale setting for applicable plots, either
              Linear or Log.Undefined for nonhistogram plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE {LINEAR | LOG}
            - DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE?
            ```
        """
        return self._scale


class DpojetPlotItemHistogramNumbins(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:HISTOgram:NUMBins`` command.

    Description:
        - This command sets or queries the current histogram resolution.Undefined for nonhistogram
          plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:HISTOgram:NUMBins?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:HISTOgram:NUMBins?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:NUMBins value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:HISTOgram:NUMBins {TWENtyfive | FIFTY | HUNdred | TWOFifty | FIVEHundred | TWOThousand | MAXimum}
        - DPOJET:PLOT<x>:HISTOgram:NUMBins?
        ```
    """  # noqa: E501


class DpojetPlotItemHistogramHorizontalSpan(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN`` command.

    Description:
        - This command sets or queries the histogram span.Undefined for nonhistogram plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN  <NR3>
        - DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN?
        ```
    """


class DpojetPlotItemHistogramHorizontalCenter(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter`` command.

    Description:
        - This command sets or queries the histogram center.Undefined for nonhistogram plots.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter  <NR3>
        - DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter?
        ```
    """


class DpojetPlotItemHistogramHorizontalAutoscale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale`` command.

    Description:
        - This command sets or queries the horizontal auto scale settings.Undefined for nonhistogram
          plots.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale {1 | 0}
        - DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale?
        ```
    """


class DpojetPlotItemHistogramHorizontal(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:HISTOgram:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:HISTOgram:HORizontal?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:HISTOgram:HORizontal?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autoscale``: The ``DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale`` command.
        - ``.center``: The ``DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter`` command.
        - ``.span``: The ``DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoscale = DpojetPlotItemHistogramHorizontalAutoscale(
            device, f"{self._cmd_syntax}:AUTOscale"
        )
        self._center = DpojetPlotItemHistogramHorizontalCenter(device, f"{self._cmd_syntax}:CENter")
        self._span = DpojetPlotItemHistogramHorizontalSpan(device, f"{self._cmd_syntax}:SPAN")

    @property
    def autoscale(self) -> DpojetPlotItemHistogramHorizontalAutoscale:
        """Return the ``DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale`` command.

        Description:
            - This command sets or queries the horizontal auto scale settings.Undefined for
              nonhistogram plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale {1 | 0}
            - DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale?
            ```
        """
        return self._autoscale

    @property
    def center(self) -> DpojetPlotItemHistogramHorizontalCenter:
        """Return the ``DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter`` command.

        Description:
            - This command sets or queries the histogram center.Undefined for nonhistogram plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter  <NR3>
            - DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter?
            ```
        """
        return self._center

    @property
    def span(self) -> DpojetPlotItemHistogramHorizontalSpan:
        """Return the ``DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN`` command.

        Description:
            - This command sets or queries the histogram span.Undefined for nonhistogram plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN  <NR3>
            - DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN?
            ```
        """
        return self._span


class DpojetPlotItemHistogramAutoset(SCPICmdWrite):
    """The ``DPOJET:PLOT<x>:HISTOgram:AUTOset`` command.

    Description:
        - This command runs a histogram autoset for the specified slot.Undefined for nonhistogram
          plots.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:HISTOgram:AUTOset value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:HISTOgram:AUTOset {EXECute}
        ```
    """


class DpojetPlotItemHistogram(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:HISTOgram`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:HISTOgram?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:HISTOgram?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autoset``: The ``DPOJET:PLOT<x>:HISTOgram:AUTOset`` command.
        - ``.horizontal``: The ``DPOJET:PLOT<x>:HISTOgram:HORizontal`` command tree.
        - ``.numbins``: The ``DPOJET:PLOT<x>:HISTOgram:NUMBins`` command.
        - ``.vertical``: The ``DPOJET:PLOT<x>:HISTOgram:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoset = DpojetPlotItemHistogramAutoset(device, f"{self._cmd_syntax}:AUTOset")
        self._horizontal = DpojetPlotItemHistogramHorizontal(
            device, f"{self._cmd_syntax}:HORizontal"
        )
        self._numbins = DpojetPlotItemHistogramNumbins(device, f"{self._cmd_syntax}:NUMBins")
        self._vertical = DpojetPlotItemHistogramVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def autoset(self) -> DpojetPlotItemHistogramAutoset:
        """Return the ``DPOJET:PLOT<x>:HISTOgram:AUTOset`` command.

        Description:
            - This command runs a histogram autoset for the specified slot.Undefined for
              nonhistogram plots.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:AUTOset value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:HISTOgram:AUTOset {EXECute}
            ```
        """
        return self._autoset

    @property
    def horizontal(self) -> DpojetPlotItemHistogramHorizontal:
        """Return the ``DPOJET:PLOT<x>:HISTOgram:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:HISTOgram:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.autoscale``: The ``DPOJET:PLOT<x>:HISTOgram:HORizontal:AUTOscale`` command.
            - ``.center``: The ``DPOJET:PLOT<x>:HISTOgram:HORizontal:CENter`` command.
            - ``.span``: The ``DPOJET:PLOT<x>:HISTOgram:HORizontal:SPAN`` command.
        """
        return self._horizontal

    @property
    def numbins(self) -> DpojetPlotItemHistogramNumbins:
        """Return the ``DPOJET:PLOT<x>:HISTOgram:NUMBins`` command.

        Description:
            - This command sets or queries the current histogram resolution.Undefined for
              nonhistogram plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:HISTOgram:NUMBins?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:NUMBins?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:NUMBins value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:HISTOgram:NUMBins {TWENtyfive | FIFTY | HUNdred | TWOFifty | FIVEHundred | TWOThousand | MAXimum}
            - DPOJET:PLOT<x>:HISTOgram:NUMBins?
            ```
        """  # noqa: E501
        return self._numbins

    @property
    def vertical(self) -> DpojetPlotItemHistogramVertical:
        """Return the ``DPOJET:PLOT<x>:HISTOgram:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:HISTOgram:VERTical?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:HISTOgram:VERTical?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DPOJET:PLOT<x>:HISTOgram:VERTical:SCALE`` command.
        """
        return self._vertical


class DpojetPlotItemEyeVerticalYaxismin(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn`` command.

    Description:
        - This command sets or queries the Y-Axis minimum value

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn  <NR3>
        - DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn?
        ```
    """


class DpojetPlotItemEyeVerticalYaxismax(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx`` command.

    Description:
        - This command sets or queries the Y-Axis maximum value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx  <NR3>
        - DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx?
        ```
    """


class DpojetPlotItemEyeVertical(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:VERTical?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.yaxismax``: The ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx`` command.
        - ``.yaxismin``: The ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._yaxismax = DpojetPlotItemEyeVerticalYaxismax(device, f"{self._cmd_syntax}:YAXISMAx")
        self._yaxismin = DpojetPlotItemEyeVerticalYaxismin(device, f"{self._cmd_syntax}:YAXISMIn")

    @property
    def yaxismax(self) -> DpojetPlotItemEyeVerticalYaxismax:
        """Return the ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx`` command.

        Description:
            - This command sets or queries the Y-Axis maximum value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx  <NR3>
            - DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx?
            ```
        """
        return self._yaxismax

    @property
    def yaxismin(self) -> DpojetPlotItemEyeVerticalYaxismin:
        """Return the ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn`` command.

        Description:
            - This command sets or queries the Y-Axis minimum value

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn  <NR3>
            - DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn?
            ```
        """
        return self._yaxismin


class DpojetPlotItemEyeVertscale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:VERTScale`` command.

    Description:
        - This command sets or queries the vertical scale state, either on or off.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:VERTScale?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:VERTScale?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:EYE:VERTScale value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:VERTScale {1 | 0}
        - DPOJET:PLOT<x>:EYE:VERTScale?
        ```
    """


class DpojetPlotItemEyeVerticalalignment(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:VERTICALAlignment`` command.

    Description:
        - This command sets or queries the vertical alignment state, either on or off.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:VERTICALAlignment?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:VERTICALAlignment?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:VERTICALAlignment value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:VERTICALAlignment {1 | 0}
        - DPOJET:PLOT<x>:EYE:VERTICALAlignment?
        ```
    """


class DpojetPlotItemEyeSuperimpose(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:SUPERImpose`` command.

    Description:
        - This command sets or queries whether superimposed eyes are generated in eye
          diagrams.Undefined for noneye plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:SUPERImpose?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:SUPERImpose?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:EYE:SUPERImpose value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:SUPERImpose {1 | 0}
        - DPOJET:PLOT<x>:EYE:SUPERImpose?
        ```
    """


class DpojetPlotItemEyeState(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:STATE`` command.

    Description:
        - This command sets or queries the eye state, either on or off.Undefined for noneye plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:EYE:STATE value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:STATE {1 | 0}
        - DPOJET:PLOT<x>:EYE:STATE?
        ```
    """


class DpojetPlotItemEyeMaskfile(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:MASKfile`` command.

    Description:
        - This command sets or queries the mask file.Undefined for noneye plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:MASKfile?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:MASKfile?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:EYE:MASKfile value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:MASKfile  <string>
        - DPOJET:PLOT<x>:EYE:MASKfile?
        ```
    """


class DpojetPlotItemEyeInterpolationtype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:INTERPolationtype`` command.

    Description:
        - This command sets or queries the interpolation type.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:INTERPolationtype?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:INTERPolationtype?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:INTERPolationtype value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:INTERPolationtype { INTERPOLATION | NONINTERPOLATION }
        - DPOJET:PLOT<x>:EYE:INTERPolationtype?
        ```
    """


class DpojetPlotItemEyeInterpolationfactor(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor`` command.

    Description:
        - This command sets or queries eye diagram interpolation factor.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor {AUTO, TWELVEPOINTEIGHT, SIXTEEN}
        - DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor?
        ```
    """


class DpojetPlotItemEyeHorizontalXaxismin(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn`` command.

    Description:
        - This command sets or queries the X-Axis minimum value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn  <NR3>
        - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn?
        ```
    """


class DpojetPlotItemEyeHorizontalXaxismax(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx`` command.

    Description:
        - This command sets or queries the X-Axis maximum value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx  <NR3>
        - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx?
        ```
    """


class DpojetPlotItemEyeHorizontalResolution(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:HORizontal:RESolution`` command.

    Description:
        - This command sets or queries the Horizontal Eye resolution.Undefined for noneye plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:HORizontal:RESolution?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:HORizontal:RESolution?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:HORizontal:RESolution value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:HORizontal:RESolution  <NR3>
        - DPOJET:PLOT<x>:EYE:HORizontal:RESolution?
        ```
    """


class DpojetPlotItemEyeHorizontalAutoscale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale`` command.

    Description:
        - This command sets or queries the horizontal auto scale setting.Undefined for noneye plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale {1 | 0}
        - DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale?
        ```
    """


class DpojetPlotItemEyeHorizontal(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:HORizontal?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autoscale``: The ``DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale`` command.
        - ``.resolution``: The ``DPOJET:PLOT<x>:EYE:HORizontal:RESolution`` command.
        - ``.xaxismax``: The ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx`` command.
        - ``.xaxismin``: The ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoscale = DpojetPlotItemEyeHorizontalAutoscale(
            device, f"{self._cmd_syntax}:AUTOscale"
        )
        self._resolution = DpojetPlotItemEyeHorizontalResolution(
            device, f"{self._cmd_syntax}:RESolution"
        )
        self._xaxismax = DpojetPlotItemEyeHorizontalXaxismax(device, f"{self._cmd_syntax}:XAXISMAx")
        self._xaxismin = DpojetPlotItemEyeHorizontalXaxismin(device, f"{self._cmd_syntax}:XAXISMIn")

    @property
    def autoscale(self) -> DpojetPlotItemEyeHorizontalAutoscale:
        """Return the ``DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale`` command.

        Description:
            - This command sets or queries the horizontal auto scale setting.Undefined for noneye
              plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale {1 | 0}
            - DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale?
            ```
        """
        return self._autoscale

    @property
    def resolution(self) -> DpojetPlotItemEyeHorizontalResolution:
        """Return the ``DPOJET:PLOT<x>:EYE:HORizontal:RESolution`` command.

        Description:
            - This command sets or queries the Horizontal Eye resolution.Undefined for noneye plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:RESolution?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:RESolution?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:RESolution value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:HORizontal:RESolution  <NR3>
            - DPOJET:PLOT<x>:EYE:HORizontal:RESolution?
            ```
        """
        return self._resolution

    @property
    def xaxismax(self) -> DpojetPlotItemEyeHorizontalXaxismax:
        """Return the ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx`` command.

        Description:
            - This command sets or queries the X-Axis maximum value.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx  <NR3>
            - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx?
            ```
        """
        return self._xaxismax

    @property
    def xaxismin(self) -> DpojetPlotItemEyeHorizontalXaxismin:
        """Return the ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn`` command.

        Description:
            - This command sets or queries the X-Axis minimum value.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn  <NR3>
            - DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn?
            ```
        """
        return self._xaxismin


class DpojetPlotItemEyeHorizscale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:HORIZScale`` command.

    Description:
        - This command sets or queries the horizontal scale state, either on or off.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:HORIZScale?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:HORIZScale?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:EYE:HORIZScale value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:HORIZScale {1 | 0}
        - DPOJET:PLOT<x>:EYE:HORIZScale?
        ```
    """


class DpojetPlotItemEyeEyeverticalscale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:EYEVerticalscale`` command.

    Description:
        - This command sets or queries eye diagram vertical scale when superimpose reference clock
          eye is checked.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:EYEVerticalscale?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:EYEVerticalscale?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:EYE:EYEVerticalscale value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:EYEVerticalscale {SCALETOData, SCALETORefclk}
        - DPOJET:PLOT<x>:EYE:EYEVerticalscale?
        ```
    """


class DpojetPlotItemEyeAlignment(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE:ALIGNment`` command.

    Description:
        - This command sets or queries eye alignment state for eye plots.Undefined for noneye plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:ALIGNment?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:ALIGNment?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:EYE:ALIGNment value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EYE:ALIGNment {AUTO | LEFT | CENter}
        - DPOJET:PLOT<x>:EYE:ALIGNment?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetPlotItemEye(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EYE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.alignment``: The ``DPOJET:PLOT<x>:EYE:ALIGNment`` command.
        - ``.eyeverticalscale``: The ``DPOJET:PLOT<x>:EYE:EYEVerticalscale`` command.
        - ``.horizscale``: The ``DPOJET:PLOT<x>:EYE:HORIZScale`` command.
        - ``.horizontal``: The ``DPOJET:PLOT<x>:EYE:HORizontal`` command tree.
        - ``.interpolationfactor``: The ``DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor`` command.
        - ``.interpolationtype``: The ``DPOJET:PLOT<x>:EYE:INTERPolationtype`` command.
        - ``.maskfile``: The ``DPOJET:PLOT<x>:EYE:MASKfile`` command.
        - ``.state``: The ``DPOJET:PLOT<x>:EYE:STATE`` command.
        - ``.superimpose``: The ``DPOJET:PLOT<x>:EYE:SUPERImpose`` command.
        - ``.verticalalignment``: The ``DPOJET:PLOT<x>:EYE:VERTICALAlignment`` command.
        - ``.vertscale``: The ``DPOJET:PLOT<x>:EYE:VERTScale`` command.
        - ``.vertical``: The ``DPOJET:PLOT<x>:EYE:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._alignment = DpojetPlotItemEyeAlignment(device, f"{self._cmd_syntax}:ALIGNment")
        self._eyeverticalscale = DpojetPlotItemEyeEyeverticalscale(
            device, f"{self._cmd_syntax}:EYEVerticalscale"
        )
        self._horizscale = DpojetPlotItemEyeHorizscale(device, f"{self._cmd_syntax}:HORIZScale")
        self._horizontal = DpojetPlotItemEyeHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._interpolationfactor = DpojetPlotItemEyeInterpolationfactor(
            device, f"{self._cmd_syntax}:INTERPOLATIONFactor"
        )
        self._interpolationtype = DpojetPlotItemEyeInterpolationtype(
            device, f"{self._cmd_syntax}:INTERPolationtype"
        )
        self._maskfile = DpojetPlotItemEyeMaskfile(device, f"{self._cmd_syntax}:MASKfile")
        self._state = DpojetPlotItemEyeState(device, f"{self._cmd_syntax}:STATE")
        self._superimpose = DpojetPlotItemEyeSuperimpose(device, f"{self._cmd_syntax}:SUPERImpose")
        self._verticalalignment = DpojetPlotItemEyeVerticalalignment(
            device, f"{self._cmd_syntax}:VERTICALAlignment"
        )
        self._vertscale = DpojetPlotItemEyeVertscale(device, f"{self._cmd_syntax}:VERTScale")
        self._vertical = DpojetPlotItemEyeVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def alignment(self) -> DpojetPlotItemEyeAlignment:
        """Return the ``DPOJET:PLOT<x>:EYE:ALIGNment`` command.

        Description:
            - This command sets or queries eye alignment state for eye plots.Undefined for noneye
              plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:ALIGNment?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:ALIGNment?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:ALIGNment value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:ALIGNment {AUTO | LEFT | CENter}
            - DPOJET:PLOT<x>:EYE:ALIGNment?
            ```
        """
        return self._alignment

    @property
    def eyeverticalscale(self) -> DpojetPlotItemEyeEyeverticalscale:
        """Return the ``DPOJET:PLOT<x>:EYE:EYEVerticalscale`` command.

        Description:
            - This command sets or queries eye diagram vertical scale when superimpose reference
              clock eye is checked.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:EYEVerticalscale?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:EYEVerticalscale?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:EYEVerticalscale value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:EYEVerticalscale {SCALETOData, SCALETORefclk}
            - DPOJET:PLOT<x>:EYE:EYEVerticalscale?
            ```
        """
        return self._eyeverticalscale

    @property
    def horizscale(self) -> DpojetPlotItemEyeHorizscale:
        """Return the ``DPOJET:PLOT<x>:EYE:HORIZScale`` command.

        Description:
            - This command sets or queries the horizontal scale state, either on or off.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:HORIZScale?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:HORIZScale?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:HORIZScale value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:HORIZScale {1 | 0}
            - DPOJET:PLOT<x>:EYE:HORIZScale?
            ```
        """
        return self._horizscale

    @property
    def horizontal(self) -> DpojetPlotItemEyeHorizontal:
        """Return the ``DPOJET:PLOT<x>:EYE:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:HORizontal?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autoscale``: The ``DPOJET:PLOT<x>:EYE:HORizontal:AUTOscale`` command.
            - ``.resolution``: The ``DPOJET:PLOT<x>:EYE:HORizontal:RESolution`` command.
            - ``.xaxismax``: The ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMAx`` command.
            - ``.xaxismin``: The ``DPOJET:PLOT<x>:EYE:HORizontal:XAXISMIn`` command.
        """
        return self._horizontal

    @property
    def interpolationfactor(self) -> DpojetPlotItemEyeInterpolationfactor:
        """Return the ``DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor`` command.

        Description:
            - This command sets or queries eye diagram interpolation factor.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor {AUTO, TWELVEPOINTEIGHT, SIXTEEN}
            - DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor?
            ```
        """
        return self._interpolationfactor

    @property
    def interpolationtype(self) -> DpojetPlotItemEyeInterpolationtype:
        """Return the ``DPOJET:PLOT<x>:EYE:INTERPolationtype`` command.

        Description:
            - This command sets or queries the interpolation type.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:INTERPolationtype?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:INTERPolationtype?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:INTERPolationtype value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:INTERPolationtype { INTERPOLATION | NONINTERPOLATION }
            - DPOJET:PLOT<x>:EYE:INTERPolationtype?
            ```
        """
        return self._interpolationtype

    @property
    def maskfile(self) -> DpojetPlotItemEyeMaskfile:
        """Return the ``DPOJET:PLOT<x>:EYE:MASKfile`` command.

        Description:
            - This command sets or queries the mask file.Undefined for noneye plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:MASKfile?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:MASKfile?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:EYE:MASKfile value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:MASKfile  <string>
            - DPOJET:PLOT<x>:EYE:MASKfile?
            ```
        """
        return self._maskfile

    @property
    def state(self) -> DpojetPlotItemEyeState:
        """Return the ``DPOJET:PLOT<x>:EYE:STATE`` command.

        Description:
            - This command sets or queries the eye state, either on or off.Undefined for noneye
              plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:EYE:STATE value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:STATE {1 | 0}
            - DPOJET:PLOT<x>:EYE:STATE?
            ```
        """
        return self._state

    @property
    def superimpose(self) -> DpojetPlotItemEyeSuperimpose:
        """Return the ``DPOJET:PLOT<x>:EYE:SUPERImpose`` command.

        Description:
            - This command sets or queries whether superimposed eyes are generated in eye
              diagrams.Undefined for noneye plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:SUPERImpose?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:SUPERImpose?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:SUPERImpose value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:SUPERImpose {1 | 0}
            - DPOJET:PLOT<x>:EYE:SUPERImpose?
            ```
        """
        return self._superimpose

    @property
    def verticalalignment(self) -> DpojetPlotItemEyeVerticalalignment:
        """Return the ``DPOJET:PLOT<x>:EYE:VERTICALAlignment`` command.

        Description:
            - This command sets or queries the vertical alignment state, either on or off.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:VERTICALAlignment?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:VERTICALAlignment?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:VERTICALAlignment value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:VERTICALAlignment {1 | 0}
            - DPOJET:PLOT<x>:EYE:VERTICALAlignment?
            ```
        """
        return self._verticalalignment

    @property
    def vertscale(self) -> DpojetPlotItemEyeVertscale:
        """Return the ``DPOJET:PLOT<x>:EYE:VERTScale`` command.

        Description:
            - This command sets or queries the vertical scale state, either on or off.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:VERTScale?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:VERTScale?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:EYE:VERTScale value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EYE:VERTScale {1 | 0}
            - DPOJET:PLOT<x>:EYE:VERTScale?
            ```
        """
        return self._vertscale

    @property
    def vertical(self) -> DpojetPlotItemEyeVertical:
        """Return the ``DPOJET:PLOT<x>:EYE:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE:VERTical?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.yaxismax``: The ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMAx`` command.
            - ``.yaxismin``: The ``DPOJET:PLOT<x>:EYE:VERTical:YAXISMIn`` command.
        """
        return self._vertical


class DpojetPlotItemExportraw(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:EXPORTRaw`` command.

    Description:
        - This query command returns the raw Eye diagram 2d histogram data in binary format. This
          command is similar to curve query

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EXPORTRaw?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EXPORTRaw?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:EXPORTRaw?
        ```
    """


class DpojetPlotItemDataYdataTn(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:YDATa:TN`` command.

    Description:
        - This command returns the TN plot Y data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:TN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:TN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:YDATa:TN?
        ```
    """


class DpojetPlotItemDataYdataTj(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:YDATa:TJ`` command.

    Description:
        - This command returns the TJ plot Y data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:TJ?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:TJ?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:YDATa:TJ?
        ```
    """


class DpojetPlotItemDataYdataRnnpn(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:YDATa:RNNPN`` command.

    Description:
        - This command returns the RNNPN plot Y data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:RNNPN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:RNNPN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:YDATa:RNNPN?
        ```
    """


class DpojetPlotItemDataYdataRjbuj(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:YDATa:RJBUJ`` command.

    Description:
        - This command returns the RJ+BUJ plot Y data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of <y> bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:RJBUJ?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:RJBUJ?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:YDATa:RJBUJ?
        ```
    """


class DpojetPlotItemDataYdataPn(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:YDATa:PN`` command.

    Description:
        - This command returns the PN plot Y data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:PN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:PN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:YDATa:PN?
        ```
    """


class DpojetPlotItemDataYdataPj(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:YDATa:PJ`` command.

    Description:
        - This command returns the PJ plot Y data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of <y> bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:PJ?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:PJ?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:YDATa:PJ?
        ```
    """


class DpojetPlotItemDataYdataDdnzero(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:YDATa:DDNZERO`` command.

    Description:
        - This command returns the DDNZERO plot Y data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:DDNZERO?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:DDNZERO?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:YDATa:DDNZERO?
        ```
    """


class DpojetPlotItemDataYdataDdnone(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:YDATa:DDNONE`` command.

    Description:
        - This command returns the DDNONE plot Y data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:DDNONE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:DDNONE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:YDATa:DDNONE?
        ```
    """


class DpojetPlotItemDataYdataDdjdcd(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:YDATa:DDJDCD`` command.

    Description:
        - This command returns the DDJ+DCD plot Y data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of <y> bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:DDJDCD?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:DDJDCD?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:YDATa:DDJDCD?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetPlotItemDataYdata(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:YDATa`` command.

    Description:
        - This command returns the plot Y data values. This command is similar to the curve query,
          where the output is in the format #<x><yyy><data><newline>, where <x> is the number of <y>
          bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F denote
          the number of y bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.This command does not support plots such as the Eye Diagram Height plot, Waveform
          Plot and Eye diagram with mask hits.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:YDATa?
        ```

    Properties:
        - ``.ddjdcd``: The ``DPOJET:PLOT<x>:DATA:YDATa:DDJDCD`` command.
        - ``.ddnone``: The ``DPOJET:PLOT<x>:DATA:YDATa:DDNONE`` command.
        - ``.ddnzero``: The ``DPOJET:PLOT<x>:DATA:YDATa:DDNZERO`` command.
        - ``.pj``: The ``DPOJET:PLOT<x>:DATA:YDATa:PJ`` command.
        - ``.pn``: The ``DPOJET:PLOT<x>:DATA:YDATa:PN`` command.
        - ``.rjbuj``: The ``DPOJET:PLOT<x>:DATA:YDATa:RJBUJ`` command.
        - ``.rnnpn``: The ``DPOJET:PLOT<x>:DATA:YDATa:RNNPN`` command.
        - ``.tj``: The ``DPOJET:PLOT<x>:DATA:YDATa:TJ`` command.
        - ``.tn``: The ``DPOJET:PLOT<x>:DATA:YDATa:TN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ddjdcd = DpojetPlotItemDataYdataDdjdcd(device, f"{self._cmd_syntax}:DDJDCD")
        self._ddnone = DpojetPlotItemDataYdataDdnone(device, f"{self._cmd_syntax}:DDNONE")
        self._ddnzero = DpojetPlotItemDataYdataDdnzero(device, f"{self._cmd_syntax}:DDNZERO")
        self._pj = DpojetPlotItemDataYdataPj(device, f"{self._cmd_syntax}:PJ")
        self._pn = DpojetPlotItemDataYdataPn(device, f"{self._cmd_syntax}:PN")
        self._rjbuj = DpojetPlotItemDataYdataRjbuj(device, f"{self._cmd_syntax}:RJBUJ")
        self._rnnpn = DpojetPlotItemDataYdataRnnpn(device, f"{self._cmd_syntax}:RNNPN")
        self._tj = DpojetPlotItemDataYdataTj(device, f"{self._cmd_syntax}:TJ")
        self._tn = DpojetPlotItemDataYdataTn(device, f"{self._cmd_syntax}:TN")

    @property
    def ddjdcd(self) -> DpojetPlotItemDataYdataDdjdcd:
        """Return the ``DPOJET:PLOT<x>:DATA:YDATa:DDJDCD`` command.

        Description:
            - This command returns the DDJ+DCD plot Y data values. This command is similar to the
              curve query, where the output is in the format #<x><yyy><data><newline>, where <x> is
              the number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of <y> bytes between 10 and 15 digits.<yyy> is the
              number of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:DDJDCD?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:DATA:YDATa:DDJDCD?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:YDATa:DDJDCD?
            ```
        """
        return self._ddjdcd

    @property
    def ddnone(self) -> DpojetPlotItemDataYdataDdnone:
        """Return the ``DPOJET:PLOT<x>:DATA:YDATa:DDNONE`` command.

        Description:
            - This command returns the DDNONE plot Y data values. This command is similar to the
              curve query, where the output is in the format #<x><yyy><data><newline>, where <x> is
              the number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<yyy> is the number
              of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:DDNONE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:DATA:YDATa:DDNONE?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:YDATa:DDNONE?
            ```
        """
        return self._ddnone

    @property
    def ddnzero(self) -> DpojetPlotItemDataYdataDdnzero:
        """Return the ``DPOJET:PLOT<x>:DATA:YDATa:DDNZERO`` command.

        Description:
            - This command returns the DDNZERO plot Y data values. This command is similar to the
              curve query, where the output is in the format #<x><yyy><data><newline>, where <x> is
              the number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<yyy> is the number
              of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:DDNZERO?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:DATA:YDATa:DDNZERO?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:YDATa:DDNZERO?
            ```
        """
        return self._ddnzero

    @property
    def pj(self) -> DpojetPlotItemDataYdataPj:
        """Return the ``DPOJET:PLOT<x>:DATA:YDATa:PJ`` command.

        Description:
            - This command returns the PJ plot Y data values. This command is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of <y> bytes between 10 and 15 digits.<yyy> is the
              number of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:PJ?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:PJ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:YDATa:PJ?
            ```
        """
        return self._pj

    @property
    def pn(self) -> DpojetPlotItemDataYdataPn:
        """Return the ``DPOJET:PLOT<x>:DATA:YDATa:PN`` command.

        Description:
            - This command returns the PN plot Y data values. This command is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<yyy> is the number
              of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:PN?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:PN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:YDATa:PN?
            ```
        """
        return self._pn

    @property
    def rjbuj(self) -> DpojetPlotItemDataYdataRjbuj:
        """Return the ``DPOJET:PLOT<x>:DATA:YDATa:RJBUJ`` command.

        Description:
            - This command returns the RJ+BUJ plot Y data values. This command is similar to the
              curve query, where the output is in the format #<x><yyy><data><newline>, where <x> is
              the number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of <y> bytes between 10 and 15 digits.<yyy> is the
              number of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:RJBUJ?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:RJBUJ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:YDATa:RJBUJ?
            ```
        """
        return self._rjbuj

    @property
    def rnnpn(self) -> DpojetPlotItemDataYdataRnnpn:
        """Return the ``DPOJET:PLOT<x>:DATA:YDATa:RNNPN`` command.

        Description:
            - This command returns the RNNPN plot Y data values. This command is similar to the
              curve query, where the output is in the format #<x><yyy><data><newline>, where <x> is
              the number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<yyy> is the number
              of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:RNNPN?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:RNNPN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:YDATa:RNNPN?
            ```
        """
        return self._rnnpn

    @property
    def tj(self) -> DpojetPlotItemDataYdataTj:
        """Return the ``DPOJET:PLOT<x>:DATA:YDATa:TJ`` command.

        Description:
            - This command returns the TJ plot Y data values. This command is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<yyy> is the number
              of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:TJ?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:TJ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:YDATa:TJ?
            ```
        """
        return self._tj

    @property
    def tn(self) -> DpojetPlotItemDataYdataTn:
        """Return the ``DPOJET:PLOT<x>:DATA:YDATa:TN`` command.

        Description:
            - This command returns the TN plot Y data values. This command is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<yyy> is the number
              of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:TN?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa:TN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:YDATa:TN?
            ```
        """
        return self._tn


class DpojetPlotItemDataXdataTn(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:XDATa:TN`` command.

    Description:
        - This command returns the TN plot X data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<data> is curve data.<newline> is a
          single-byte new line character at the end of the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:TN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:TN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:XDATa:TN?
        ```
    """


class DpojetPlotItemDataXdataTj(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:XDATa:TJ`` command.

    Description:
        - This command returns the TJ plot X data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<data> is curve data.<newline> is a
          single-byte new line character at the end of the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:TJ?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:TJ?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:XDATa:TJ?
        ```
    """


class DpojetPlotItemDataXdataRnnpn(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:XDATa:RNNPN`` command.

    Description:
        - This command returns the RNNPN plot X data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<data> is curve data.<newline> is a
          single-byte new line character at the end of the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:RNNPN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:RNNPN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:XDATa:RNNPN?
        ```
    """


class DpojetPlotItemDataXdataRjbuj(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:XDATa:RJBUJ`` command.

    Description:
        - This command returns the RJ+BUJ plot X data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of <y> bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:RJBUJ?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:RJBUJ?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:XDATa:RJBUJ?
        ```
    """


class DpojetPlotItemDataXdataPn(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:XDATa:PN`` command.

    Description:
        - This command returns the PN plot X data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<data> is curve data.<newline> is a
          single-byte new line character at the end of the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:PN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:PN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:XDATa:PN?
        ```
    """


class DpojetPlotItemDataXdataPj(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:XDATa:PJ`` command.

    Description:
        - This command returns the PJ plot X data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of <y> bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:PJ?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:PJ?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:XDATa:PJ?
        ```
    """


class DpojetPlotItemDataXdataDdnzero(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:XDATa:DDNZERO`` command.

    Description:
        - This command returns the DDNZERO plot X data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<data> is curve data.<newline> is a
          single-byte new line character at the end of the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:DDNZERO?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:DDNZERO?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:XDATa:DDNZERO?
        ```
    """


class DpojetPlotItemDataXdataDdnone(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:XDATa:DDNONE`` command.

    Description:
        - This command returns the DDNONE plot X data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<data> is curve data.<newline> is a
          single-byte new line character at the end of the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:DDNONE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:DDNONE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:XDATa:DDNONE?
        ```
    """


class DpojetPlotItemDataXdataDdjdcd(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:XDATa:DDJDCD`` command.

    Description:
        - This command returns the DDJ+DCD plot X data values. This command is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of <y> bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:DDJDCD?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:DDJDCD?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:XDATa:DDJDCD?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetPlotItemDataXdata(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA:XDATa`` command.

    Description:
        - This command returns the plot X data values. This command is similar to the curve query,
          where the output is in the format #<x><yyy><data><newline>, where <x> is the number of <y>
          bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F denote
          the number of y bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.This command does not support plots such as the Eye Diagram Height plot, Waveform
          Plot and Eye diagram with mask hits.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:DATA:XDATa?
        ```

    Properties:
        - ``.ddjdcd``: The ``DPOJET:PLOT<x>:DATA:XDATa:DDJDCD`` command.
        - ``.ddnone``: The ``DPOJET:PLOT<x>:DATA:XDATa:DDNONE`` command.
        - ``.ddnzero``: The ``DPOJET:PLOT<x>:DATA:XDATa:DDNZERO`` command.
        - ``.pj``: The ``DPOJET:PLOT<x>:DATA:XDATa:PJ`` command.
        - ``.pn``: The ``DPOJET:PLOT<x>:DATA:XDATa:PN`` command.
        - ``.rjbuj``: The ``DPOJET:PLOT<x>:DATA:XDATa:RJBUJ`` command.
        - ``.rnnpn``: The ``DPOJET:PLOT<x>:DATA:XDATa:RNNPN`` command.
        - ``.tj``: The ``DPOJET:PLOT<x>:DATA:XDATa:TJ`` command.
        - ``.tn``: The ``DPOJET:PLOT<x>:DATA:XDATa:TN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ddjdcd = DpojetPlotItemDataXdataDdjdcd(device, f"{self._cmd_syntax}:DDJDCD")
        self._ddnone = DpojetPlotItemDataXdataDdnone(device, f"{self._cmd_syntax}:DDNONE")
        self._ddnzero = DpojetPlotItemDataXdataDdnzero(device, f"{self._cmd_syntax}:DDNZERO")
        self._pj = DpojetPlotItemDataXdataPj(device, f"{self._cmd_syntax}:PJ")
        self._pn = DpojetPlotItemDataXdataPn(device, f"{self._cmd_syntax}:PN")
        self._rjbuj = DpojetPlotItemDataXdataRjbuj(device, f"{self._cmd_syntax}:RJBUJ")
        self._rnnpn = DpojetPlotItemDataXdataRnnpn(device, f"{self._cmd_syntax}:RNNPN")
        self._tj = DpojetPlotItemDataXdataTj(device, f"{self._cmd_syntax}:TJ")
        self._tn = DpojetPlotItemDataXdataTn(device, f"{self._cmd_syntax}:TN")

    @property
    def ddjdcd(self) -> DpojetPlotItemDataXdataDdjdcd:
        """Return the ``DPOJET:PLOT<x>:DATA:XDATa:DDJDCD`` command.

        Description:
            - This command returns the DDJ+DCD plot X data values. This command is similar to the
              curve query, where the output is in the format #<x><yyy><data><newline>, where <x> is
              the number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of <y> bytes between 10 and 15 digits.<yyy> is the
              number of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:DDJDCD?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:DATA:XDATa:DDJDCD?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:XDATa:DDJDCD?
            ```
        """
        return self._ddjdcd

    @property
    def ddnone(self) -> DpojetPlotItemDataXdataDdnone:
        """Return the ``DPOJET:PLOT<x>:DATA:XDATa:DDNONE`` command.

        Description:
            - This command returns the DDNONE plot X data values. This command is similar to the
              curve query, where the output is in the format #<x><yyy><data><newline>, where <x> is
              the number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<data> is curve
              data.<newline> is a single-byte new line character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:DDNONE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:DATA:XDATa:DDNONE?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:XDATa:DDNONE?
            ```
        """
        return self._ddnone

    @property
    def ddnzero(self) -> DpojetPlotItemDataXdataDdnzero:
        """Return the ``DPOJET:PLOT<x>:DATA:XDATa:DDNZERO`` command.

        Description:
            - This command returns the DDNZERO plot X data values. This command is similar to the
              curve query, where the output is in the format #<x><yyy><data><newline>, where <x> is
              the number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<data> is curve
              data.<newline> is a single-byte new line character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:DDNZERO?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:DATA:XDATa:DDNZERO?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:XDATa:DDNZERO?
            ```
        """
        return self._ddnzero

    @property
    def pj(self) -> DpojetPlotItemDataXdataPj:
        """Return the ``DPOJET:PLOT<x>:DATA:XDATa:PJ`` command.

        Description:
            - This command returns the PJ plot X data values. This command is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of <y> bytes between 10 and 15 digits.<yyy> is the
              number of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:PJ?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:PJ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:XDATa:PJ?
            ```
        """
        return self._pj

    @property
    def pn(self) -> DpojetPlotItemDataXdataPn:
        """Return the ``DPOJET:PLOT<x>:DATA:XDATa:PN`` command.

        Description:
            - This command returns the PN plot X data values. This command is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<data> is curve
              data.<newline> is a single-byte new line character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:PN?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:PN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:XDATa:PN?
            ```
        """
        return self._pn

    @property
    def rjbuj(self) -> DpojetPlotItemDataXdataRjbuj:
        """Return the ``DPOJET:PLOT<x>:DATA:XDATa:RJBUJ`` command.

        Description:
            - This command returns the RJ+BUJ plot X data values. This command is similar to the
              curve query, where the output is in the format #<x><yyy><data><newline>, where <x> is
              the number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of <y> bytes between 10 and 15 digits.<yyy> is the
              number of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:RJBUJ?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:RJBUJ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:XDATa:RJBUJ?
            ```
        """
        return self._rjbuj

    @property
    def rnnpn(self) -> DpojetPlotItemDataXdataRnnpn:
        """Return the ``DPOJET:PLOT<x>:DATA:XDATa:RNNPN`` command.

        Description:
            - This command returns the RNNPN plot X data values. This command is similar to the
              curve query, where the output is in the format #<x><yyy><data><newline>, where <x> is
              the number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<data> is curve
              data.<newline> is a single-byte new line character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:RNNPN?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:RNNPN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:XDATa:RNNPN?
            ```
        """
        return self._rnnpn

    @property
    def tj(self) -> DpojetPlotItemDataXdataTj:
        """Return the ``DPOJET:PLOT<x>:DATA:XDATa:TJ`` command.

        Description:
            - This command returns the TJ plot X data values. This command is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<data> is curve
              data.<newline> is a single-byte new line character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:TJ?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:TJ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:XDATa:TJ?
            ```
        """
        return self._tj

    @property
    def tn(self) -> DpojetPlotItemDataXdataTn:
        """Return the ``DPOJET:PLOT<x>:DATA:XDATa:TN`` command.

        Description:
            - This command returns the TN plot X data values. This command is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<data> is curve
              data.<newline> is a single-byte new line character at the end of the data.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:TN?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa:TN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:XDATa:TN?
            ```
        """
        return self._tn


class DpojetPlotItemData(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.xdata``: The ``DPOJET:PLOT<x>:DATA:XDATa`` command.
        - ``.ydata``: The ``DPOJET:PLOT<x>:DATA:YDATa`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._xdata = DpojetPlotItemDataXdata(device, f"{self._cmd_syntax}:XDATa")
        self._ydata = DpojetPlotItemDataYdata(device, f"{self._cmd_syntax}:YDATa")

    @property
    def xdata(self) -> DpojetPlotItemDataXdata:
        """Return the ``DPOJET:PLOT<x>:DATA:XDATa`` command.

        Description:
            - This command returns the plot X data values. This command is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<yyy> is the number
              of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.This command does not support plots such as the Eye
              Diagram Height plot, Waveform Plot and Eye diagram with mask hits.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:XDATa?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:XDATa?
            ```

        Sub-properties:
            - ``.ddjdcd``: The ``DPOJET:PLOT<x>:DATA:XDATa:DDJDCD`` command.
            - ``.ddnone``: The ``DPOJET:PLOT<x>:DATA:XDATa:DDNONE`` command.
            - ``.ddnzero``: The ``DPOJET:PLOT<x>:DATA:XDATa:DDNZERO`` command.
            - ``.pj``: The ``DPOJET:PLOT<x>:DATA:XDATa:PJ`` command.
            - ``.pn``: The ``DPOJET:PLOT<x>:DATA:XDATa:PN`` command.
            - ``.rjbuj``: The ``DPOJET:PLOT<x>:DATA:XDATa:RJBUJ`` command.
            - ``.rnnpn``: The ``DPOJET:PLOT<x>:DATA:XDATa:RNNPN`` command.
            - ``.tj``: The ``DPOJET:PLOT<x>:DATA:XDATa:TJ`` command.
            - ``.tn``: The ``DPOJET:PLOT<x>:DATA:XDATa:TN`` command.
        """
        return self._xdata

    @property
    def ydata(self) -> DpojetPlotItemDataYdata:
        """Return the ``DPOJET:PLOT<x>:DATA:YDATa`` command.

        Description:
            - This command returns the plot Y data values. This command is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<yyy> is the number
              of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.This command does not support plots such as the Eye
              Diagram Height plot, Waveform Plot and Eye diagram with mask hits.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA:YDATa?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:DATA:YDATa?
            ```

        Sub-properties:
            - ``.ddjdcd``: The ``DPOJET:PLOT<x>:DATA:YDATa:DDJDCD`` command.
            - ``.ddnone``: The ``DPOJET:PLOT<x>:DATA:YDATa:DDNONE`` command.
            - ``.ddnzero``: The ``DPOJET:PLOT<x>:DATA:YDATa:DDNZERO`` command.
            - ``.pj``: The ``DPOJET:PLOT<x>:DATA:YDATa:PJ`` command.
            - ``.pn``: The ``DPOJET:PLOT<x>:DATA:YDATa:PN`` command.
            - ``.rjbuj``: The ``DPOJET:PLOT<x>:DATA:YDATa:RJBUJ`` command.
            - ``.rnnpn``: The ``DPOJET:PLOT<x>:DATA:YDATa:RNNPN`` command.
            - ``.tj``: The ``DPOJET:PLOT<x>:DATA:YDATa:TJ`` command.
            - ``.tn``: The ``DPOJET:PLOT<x>:DATA:YDATa:TN`` command.
        """
        return self._ydata


class DpojetPlotItemCurrentuisanalyzed(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:CURRENTUISANalyzed`` command.

    Description:
        - This command queries the current UIs analyzed for Eye Diagram plot.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CURRENTUISANalyzed?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:CURRENTUISANalyzed?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:CURRENTUISANalyzed?
        ```
    """


class DpojetPlotItemCurrentuisacquired(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:CURRENTUISACquired`` command.

    Description:
        - This command queries the current UIs acquired for eye diagram plot.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CURRENTUISACquired?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:CURRENTUISACquired?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:CURRENTUISACquired?
        ```
    """


class DpojetPlotItemCorrelatedeyeTargetber(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER`` command.

    Description:
        - This command sets or queries the TARGETBER Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER {1 | 0}
        - DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER?
        ```
    """


class DpojetPlotItemCorrelatedeyeEyewidth(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH`` command.

    Description:
        - This command sets or queries the eye width of correlated eye diagram.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH  <NR2>
        - DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH?
        ```
    """


class DpojetPlotItemCorrelatedeyeEyeheight(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT`` command.

    Description:
        - This command sets or queries the eye height of correlated eye diagram.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT  <NR2>
        - DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT?
        ```
    """


class DpojetPlotItemCorrelatedeyeBer1e9v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V`` command.

    Description:
        - This command sets or queries the BER1E9 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V {1 | 0}
        - DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V?
        ```
    """


class DpojetPlotItemCorrelatedeyeBer1e6v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V`` command.

    Description:
        - This command sets or queries the BER1E6 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V {1 | 0}
        - DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V?
        ```
    """


class DpojetPlotItemCorrelatedeyeBer1e18v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V`` command.

    Description:
        - This command sets or queries the BER1E18 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V {1 | 0}
        - DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V?
        ```
    """


class DpojetPlotItemCorrelatedeyeBer1e15v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V`` command.

    Description:
        - This command sets or queries the BER1E15 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V {1 | 0}
        - DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V?
        ```
    """


class DpojetPlotItemCorrelatedeyeBer1e12v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V`` command.

    Description:
        - This command sets or queries the BER1E12 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V {1 | 0}
        - DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetPlotItemCorrelatedeye(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:CORRELATEDEye`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ber1e12v``: The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V`` command.
        - ``.ber1e15v``: The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V`` command.
        - ``.ber1e18v``: The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V`` command.
        - ``.ber1e6v``: The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V`` command.
        - ``.ber1e9v``: The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V`` command.
        - ``.eyeheight``: The ``DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT`` command.
        - ``.eyewidth``: The ``DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH`` command.
        - ``.targetber``: The ``DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ber1e12v = DpojetPlotItemCorrelatedeyeBer1e12v(device, f"{self._cmd_syntax}:BER1E12V")
        self._ber1e15v = DpojetPlotItemCorrelatedeyeBer1e15v(device, f"{self._cmd_syntax}:BER1E15V")
        self._ber1e18v = DpojetPlotItemCorrelatedeyeBer1e18v(device, f"{self._cmd_syntax}:BER1E18V")
        self._ber1e6v = DpojetPlotItemCorrelatedeyeBer1e6v(device, f"{self._cmd_syntax}:BER1E6V")
        self._ber1e9v = DpojetPlotItemCorrelatedeyeBer1e9v(device, f"{self._cmd_syntax}:BER1E9V")
        self._eyeheight = DpojetPlotItemCorrelatedeyeEyeheight(
            device, f"{self._cmd_syntax}:EYEHEIGHT"
        )
        self._eyewidth = DpojetPlotItemCorrelatedeyeEyewidth(device, f"{self._cmd_syntax}:EYEWIDTH")
        self._targetber = DpojetPlotItemCorrelatedeyeTargetber(
            device, f"{self._cmd_syntax}:TARGETBER"
        )

    @property
    def ber1e12v(self) -> DpojetPlotItemCorrelatedeyeBer1e12v:
        """Return the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V`` command.

        Description:
            - This command sets or queries the BER1E12 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V {1 | 0}
            - DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V?
            ```
        """
        return self._ber1e12v

    @property
    def ber1e15v(self) -> DpojetPlotItemCorrelatedeyeBer1e15v:
        """Return the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V`` command.

        Description:
            - This command sets or queries the BER1E15 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V {1 | 0}
            - DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V?
            ```
        """
        return self._ber1e15v

    @property
    def ber1e18v(self) -> DpojetPlotItemCorrelatedeyeBer1e18v:
        """Return the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V`` command.

        Description:
            - This command sets or queries the BER1E18 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V {1 | 0}
            - DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V?
            ```
        """
        return self._ber1e18v

    @property
    def ber1e6v(self) -> DpojetPlotItemCorrelatedeyeBer1e6v:
        """Return the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V`` command.

        Description:
            - This command sets or queries the BER1E6 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V {1 | 0}
            - DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V?
            ```
        """
        return self._ber1e6v

    @property
    def ber1e9v(self) -> DpojetPlotItemCorrelatedeyeBer1e9v:
        """Return the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V`` command.

        Description:
            - This command sets or queries the BER1E9 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V {1 | 0}
            - DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V?
            ```
        """
        return self._ber1e9v

    @property
    def eyeheight(self) -> DpojetPlotItemCorrelatedeyeEyeheight:
        """Return the ``DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT`` command.

        Description:
            - This command sets or queries the eye height of correlated eye diagram.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT  <NR2>
            - DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT?
            ```
        """
        return self._eyeheight

    @property
    def eyewidth(self) -> DpojetPlotItemCorrelatedeyeEyewidth:
        """Return the ``DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH`` command.

        Description:
            - This command sets or queries the eye width of correlated eye diagram.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH  <NR2>
            - DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH?
            ```
        """
        return self._eyewidth

    @property
    def targetber(self) -> DpojetPlotItemCorrelatedeyeTargetber:
        """Return the ``DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER`` command.

        Description:
            - This command sets or queries the TARGETBER Contour display.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER {1 | 0}
            - DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER?
            ```
        """
        return self._targetber


class DpojetPlotItemCompositenoisehistTn(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITENoisehist:TN`` command.

    Description:
        - This command sets or queries the TN Noise component settings.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITENoisehist:TN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:TN?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:TN value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITENoisehist:TN {1 | 0}
        - DPOJET:PLOT<x>:COMPOSITENoisehist:TN?
        ```
    """


class DpojetPlotItemCompositenoisehistRnnpn(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN`` command.

    Description:
        - This command sets or queries the RN+NPN Noise component settings.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN {1 | 0}
        - DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN?
        ```
    """


class DpojetPlotItemCompositenoisehistPn(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITENoisehist:PN`` command.

    Description:
        - This command sets or queries the PN Noise component settings.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITENoisehist:PN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:PN?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:PN value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITENoisehist:PN {1 | 0}
        - DPOJET:PLOT<x>:COMPOSITENoisehist:PN?
        ```
    """


class DpojetPlotItemCompositenoisehistNumbins(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins`` command.

    Description:
        - This command sets or queries the current composite noise histogram resolution.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins { TWENtyfive | FIFTY | HUNdred | TWOFifty | FIVEHundred | TWOThousand | MAXimum}
        - DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins?
        ```
    """  # noqa: E501


class DpojetPlotItemCompositenoisehistHorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE`` command.

    Description:
        - This command sets or queries the Horizontal scale setting for applicable plots, either
          Linear or Log.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE {LINEAR | LOG}
        - DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE?
        ```
    """


class DpojetPlotItemCompositenoisehistHorizontal(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DpojetPlotItemCompositenoisehistHorizontalScale(
            device, f"{self._cmd_syntax}:SCALE"
        )

    @property
    def scale(self) -> DpojetPlotItemCompositenoisehistHorizontalScale:
        """Return the ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE`` command.

        Description:
            - This command sets or queries the Horizontal scale setting for applicable plots, either
              Linear or Log.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE {LINEAR | LOG}
            - DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE?
            ```
        """
        return self._scale


class DpojetPlotItemCompositenoisehistDdnzero(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO`` command.

    Description:
        - This command sets or queries the DDN(0) Noise component settings.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO {1 | 0}
        - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO?
        ```
    """


class DpojetPlotItemCompositenoisehistDdnone(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE`` command.

    Description:
        - This command sets or queries the DDN(1) Noise component settings.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE {1 | 0}
        - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE?
        ```
    """


class DpojetPlotItemCompositenoisehist(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITENoisehist`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITENoisehist?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:COMPOSITENoisehist?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ddnone``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE`` command.
        - ``.ddnzero``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO`` command.
        - ``.horizontal``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal`` command tree.
        - ``.numbins``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins`` command.
        - ``.pn``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:PN`` command.
        - ``.rnnpn``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN`` command.
        - ``.tn``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:TN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ddnone = DpojetPlotItemCompositenoisehistDdnone(device, f"{self._cmd_syntax}:DDNONE")
        self._ddnzero = DpojetPlotItemCompositenoisehistDdnzero(
            device, f"{self._cmd_syntax}:DDNZERO"
        )
        self._horizontal = DpojetPlotItemCompositenoisehistHorizontal(
            device, f"{self._cmd_syntax}:HORizontal"
        )
        self._numbins = DpojetPlotItemCompositenoisehistNumbins(
            device, f"{self._cmd_syntax}:NUMBins"
        )
        self._pn = DpojetPlotItemCompositenoisehistPn(device, f"{self._cmd_syntax}:PN")
        self._rnnpn = DpojetPlotItemCompositenoisehistRnnpn(device, f"{self._cmd_syntax}:RNNPN")
        self._tn = DpojetPlotItemCompositenoisehistTn(device, f"{self._cmd_syntax}:TN")

    @property
    def ddnone(self) -> DpojetPlotItemCompositenoisehistDdnone:
        """Return the ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE`` command.

        Description:
            - This command sets or queries the DDN(1) Noise component settings.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE {1 | 0}
            - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE?
            ```
        """
        return self._ddnone

    @property
    def ddnzero(self) -> DpojetPlotItemCompositenoisehistDdnzero:
        """Return the ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO`` command.

        Description:
            - This command sets or queries the DDN(0) Noise component settings.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO {1 | 0}
            - DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO?
            ```
        """
        return self._ddnzero

    @property
    def horizontal(self) -> DpojetPlotItemCompositenoisehistHorizontal:
        """Return the ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal:SCALE`` command.
        """
        return self._horizontal

    @property
    def numbins(self) -> DpojetPlotItemCompositenoisehistNumbins:
        """Return the ``DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins`` command.

        Description:
            - This command sets or queries the current composite noise histogram resolution.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins { TWENtyfive | FIFTY | HUNdred | TWOFifty | FIVEHundred | TWOThousand | MAXimum}
            - DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins?
            ```
        """  # noqa: E501
        return self._numbins

    @property
    def pn(self) -> DpojetPlotItemCompositenoisehistPn:
        """Return the ``DPOJET:PLOT<x>:COMPOSITENoisehist:PN`` command.

        Description:
            - This command sets or queries the PN Noise component settings.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITENoisehist:PN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:PN?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:PN value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITENoisehist:PN {1 | 0}
            - DPOJET:PLOT<x>:COMPOSITENoisehist:PN?
            ```
        """
        return self._pn

    @property
    def rnnpn(self) -> DpojetPlotItemCompositenoisehistRnnpn:
        """Return the ``DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN`` command.

        Description:
            - This command sets or queries the RN+NPN Noise component settings.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN {1 | 0}
            - DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN?
            ```
        """
        return self._rnnpn

    @property
    def tn(self) -> DpojetPlotItemCompositenoisehistTn:
        """Return the ``DPOJET:PLOT<x>:COMPOSITENoisehist:TN`` command.

        Description:
            - This command sets or queries the TN Noise component settings.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITENoisehist:TN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:TN?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist:TN value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITENoisehist:TN {1 | 0}
            - DPOJET:PLOT<x>:COMPOSITENoisehist:TN?
            ```
        """
        return self._tn


class DpojetPlotItemCompositejitterhistVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE`` command.

    Description:
        - This command sets or queries the vertical scale setting for applicable plots, either
          Linear or Log.Undefined for non-composite jitter histogram plots.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE {LINEAR | LOG}
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE?
        ```
    """


class DpojetPlotItemCompositejitterhistVertical(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DpojetPlotItemCompositejitterhistVerticalScale(
            device, f"{self._cmd_syntax}:SCALE"
        )

    @property
    def scale(self) -> DpojetPlotItemCompositejitterhistVerticalScale:
        """Return the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE`` command.

        Description:
            - This command sets or queries the vertical scale setting for applicable plots, either
              Linear or Log.Undefined for non-composite jitter histogram plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE {LINEAR | LOG}
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE?
            ```
        """
        return self._scale


class DpojetPlotItemCompositejitterhistTj(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ`` command.

    Description:
        - This command sets or queries the TJ Jitter component settings.Undefined for non-composite
          jitter histogram plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ {1 | 0}
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ?
        ```
    """


class DpojetPlotItemCompositejitterhistRjnpj(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ`` command.

    Description:
        - This command sets or queries the RJ+NPJ Jitter component settings.Undefined for
          non-composite jitter histogram plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ {1 | 0}
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ?
        ```
    """


class DpojetPlotItemCompositejitterhistPj(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ`` command.

    Description:
        - This command sets or queries the PJ Jitter component settings.Undefined for non-composite
          jitter histogram plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ {1 | 0}
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ?
        ```
    """


class DpojetPlotItemCompositejitterhistNumbins(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins`` command.

    Description:
        - This command sets or queries the current composite jitter histogram resolution.Undefined
          for non-composite jitter histogram plots.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins {TWENtyfive | FIFTY | HUNdred | TWOFifty | FIVEHundred | TWOThousand | MAXimum}
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins?
        ```
    """  # noqa: E501


class DpojetPlotItemCompositejitterhistDdjdcd(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD`` command.

    Description:
        - This command sets or queries the DDJ+DCD Jitter component settings.Undefined for
          non-composite jitter histogram plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD {1 | 0}
        - DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD?
        ```
    """


class DpojetPlotItemCompositejitterhist(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:COMPOSITEJitterhist`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITEJitterhist?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:COMPOSITEJitterhist?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ddjdcd``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD`` command.
        - ``.numbins``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins`` command.
        - ``.pj``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ`` command.
        - ``.rjnpj``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ`` command.
        - ``.tj``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ`` command.
        - ``.vertical``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ddjdcd = DpojetPlotItemCompositejitterhistDdjdcd(device, f"{self._cmd_syntax}:DDJDCD")
        self._numbins = DpojetPlotItemCompositejitterhistNumbins(
            device, f"{self._cmd_syntax}:NUMBins"
        )
        self._pj = DpojetPlotItemCompositejitterhistPj(device, f"{self._cmd_syntax}:PJ")
        self._rjnpj = DpojetPlotItemCompositejitterhistRjnpj(device, f"{self._cmd_syntax}:RJNPJ")
        self._tj = DpojetPlotItemCompositejitterhistTj(device, f"{self._cmd_syntax}:TJ")
        self._vertical = DpojetPlotItemCompositejitterhistVertical(
            device, f"{self._cmd_syntax}:VERTical"
        )

    @property
    def ddjdcd(self) -> DpojetPlotItemCompositejitterhistDdjdcd:
        """Return the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD`` command.

        Description:
            - This command sets or queries the DDJ+DCD Jitter component settings.Undefined for
              non-composite jitter histogram plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD {1 | 0}
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD?
            ```
        """
        return self._ddjdcd

    @property
    def numbins(self) -> DpojetPlotItemCompositejitterhistNumbins:
        """Return the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins`` command.

        Description:
            - This command sets or queries the current composite jitter histogram
              resolution.Undefined for non-composite jitter histogram plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins {TWENtyfive | FIFTY | HUNdred | TWOFifty | FIVEHundred | TWOThousand | MAXimum}
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins?
            ```
        """  # noqa: E501
        return self._numbins

    @property
    def pj(self) -> DpojetPlotItemCompositejitterhistPj:
        """Return the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ`` command.

        Description:
            - This command sets or queries the PJ Jitter component settings.Undefined for
              non-composite jitter histogram plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ {1 | 0}
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ?
            ```
        """
        return self._pj

    @property
    def rjnpj(self) -> DpojetPlotItemCompositejitterhistRjnpj:
        """Return the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ`` command.

        Description:
            - This command sets or queries the RJ+NPJ Jitter component settings.Undefined for
              non-composite jitter histogram plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ {1 | 0}
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ?
            ```
        """
        return self._rjnpj

    @property
    def tj(self) -> DpojetPlotItemCompositejitterhistTj:
        """Return the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ`` command.

        Description:
            - This command sets or queries the TJ Jitter component settings.Undefined for
              non-composite jitter histogram plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ {1 | 0}
            - DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ?
            ```
        """
        return self._tj

    @property
    def vertical(self) -> DpojetPlotItemCompositejitterhistVertical:
        """Return the ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical:SCALE`` command.
        """
        return self._vertical


class DpojetPlotItemBereyeTargetber(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BEREye:TARGETBER`` command.

    Description:
        - This command sets or queries the TARGETBER Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:TARGETBER?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:TARGETBER?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:TARGETBER value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BEREye:TARGETBER {1 | 0}
        - DPOJET:PLOT<x>:BEREye:TARGETBER?
        ```
    """


class DpojetPlotItemBereyeBer1e9v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BEREye:BER1E9V`` command.

    Description:
        - This command sets or queries the BER1E9 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E9V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E9V?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E9V value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BEREye:BER1E9V {1 | 0}
        - DPOJET:PLOT<x>:BEREye:BER1E9V?
        ```
    """


class DpojetPlotItemBereyeBer1e6v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BEREye:BER1E6V`` command.

    Description:
        - This command sets or queries the BER1E6 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E6V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E6V?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E6V value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BEREye:BER1E6V {1 | 0}
        - DPOJET:PLOT<x>:BEREye:BER1E6V?
        ```
    """


class DpojetPlotItemBereyeBer1e18v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BEREye:BER1E18V`` command.

    Description:
        - This command sets or queries the BER1E18 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E18V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E18V?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E18V value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BEREye:BER1E18V {1 | 0}
        - DPOJET:PLOT<x>:BEREye:BER1E18V?
        ```
    """


class DpojetPlotItemBereyeBer1e15v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BEREye:BER1E15V`` command.

    Description:
        - This command sets or queries the BER1E15 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E15V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E15V?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E15V value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BEREye:BER1E15V {1 | 0}
        - DPOJET:PLOT<x>:BEREye:BER1E15V?
        ```
    """


class DpojetPlotItemBereyeBer1e12v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BEREye:BER1E12V`` command.

    Description:
        - This command sets or queries the BER1E12 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E12V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E12V?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E12V value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BEREye:BER1E12V {1 | 0}
        - DPOJET:PLOT<x>:BEREye:BER1E12V?
        ```
    """


class DpojetPlotItemBereye(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BEREye`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ber1e12v``: The ``DPOJET:PLOT<x>:BEREye:BER1E12V`` command.
        - ``.ber1e15v``: The ``DPOJET:PLOT<x>:BEREye:BER1E15V`` command.
        - ``.ber1e18v``: The ``DPOJET:PLOT<x>:BEREye:BER1E18V`` command.
        - ``.ber1e6v``: The ``DPOJET:PLOT<x>:BEREye:BER1E6V`` command.
        - ``.ber1e9v``: The ``DPOJET:PLOT<x>:BEREye:BER1E9V`` command.
        - ``.targetber``: The ``DPOJET:PLOT<x>:BEREye:TARGETBER`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ber1e12v = DpojetPlotItemBereyeBer1e12v(device, f"{self._cmd_syntax}:BER1E12V")
        self._ber1e15v = DpojetPlotItemBereyeBer1e15v(device, f"{self._cmd_syntax}:BER1E15V")
        self._ber1e18v = DpojetPlotItemBereyeBer1e18v(device, f"{self._cmd_syntax}:BER1E18V")
        self._ber1e6v = DpojetPlotItemBereyeBer1e6v(device, f"{self._cmd_syntax}:BER1E6V")
        self._ber1e9v = DpojetPlotItemBereyeBer1e9v(device, f"{self._cmd_syntax}:BER1E9V")
        self._targetber = DpojetPlotItemBereyeTargetber(device, f"{self._cmd_syntax}:TARGETBER")

    @property
    def ber1e12v(self) -> DpojetPlotItemBereyeBer1e12v:
        """Return the ``DPOJET:PLOT<x>:BEREye:BER1E12V`` command.

        Description:
            - This command sets or queries the BER1E12 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E12V?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E12V?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BEREye:BER1E12V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BEREye:BER1E12V {1 | 0}
            - DPOJET:PLOT<x>:BEREye:BER1E12V?
            ```
        """
        return self._ber1e12v

    @property
    def ber1e15v(self) -> DpojetPlotItemBereyeBer1e15v:
        """Return the ``DPOJET:PLOT<x>:BEREye:BER1E15V`` command.

        Description:
            - This command sets or queries the BER1E15 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E15V?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E15V?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BEREye:BER1E15V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BEREye:BER1E15V {1 | 0}
            - DPOJET:PLOT<x>:BEREye:BER1E15V?
            ```
        """
        return self._ber1e15v

    @property
    def ber1e18v(self) -> DpojetPlotItemBereyeBer1e18v:
        """Return the ``DPOJET:PLOT<x>:BEREye:BER1E18V`` command.

        Description:
            - This command sets or queries the BER1E18 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E18V?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E18V?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BEREye:BER1E18V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BEREye:BER1E18V {1 | 0}
            - DPOJET:PLOT<x>:BEREye:BER1E18V?
            ```
        """
        return self._ber1e18v

    @property
    def ber1e6v(self) -> DpojetPlotItemBereyeBer1e6v:
        """Return the ``DPOJET:PLOT<x>:BEREye:BER1E6V`` command.

        Description:
            - This command sets or queries the BER1E6 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E6V?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E6V?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BEREye:BER1E6V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BEREye:BER1E6V {1 | 0}
            - DPOJET:PLOT<x>:BEREye:BER1E6V?
            ```
        """
        return self._ber1e6v

    @property
    def ber1e9v(self) -> DpojetPlotItemBereyeBer1e9v:
        """Return the ``DPOJET:PLOT<x>:BEREye:BER1E9V`` command.

        Description:
            - This command sets or queries the BER1E9 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E9V?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:BER1E9V?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BEREye:BER1E9V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BEREye:BER1E9V {1 | 0}
            - DPOJET:PLOT<x>:BEREye:BER1E9V?
            ```
        """
        return self._ber1e9v

    @property
    def targetber(self) -> DpojetPlotItemBereyeTargetber:
        """Return the ``DPOJET:PLOT<x>:BEREye:TARGETBER`` command.

        Description:
            - This command sets or queries the TARGETBER Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye:TARGETBER?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye:TARGETBER?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BEREye:TARGETBER value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BEREye:TARGETBER {1 | 0}
            - DPOJET:PLOT<x>:BEREye:TARGETBER?
            ```
        """
        return self._targetber


class DpojetPlotItemBercontourTargetber(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:TARGETBER`` command.

    Description:
        - This command sets or queries the Target BER Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:TARGETBER?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour:TARGETBER?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:TARGETBER value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:TARGETBER {1 | 0}
        - DPOJET:PLOT<x>:BERContour:TARGETBER?
        ```
    """


class DpojetPlotItemBercontourSuperimpose(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:SUPERImpose`` command.

    Description:
        - This command sets or queries whether superimposed eyes are generated in eye diagrams.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:SUPERImpose?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:SUPERImpose?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:SUPERImpose value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:SUPERImpose {1 | 0}
        - DPOJET:PLOT<x>:BERContour:SUPERImpose?
        ```
    """


class DpojetPlotItemBercontourMaskfile(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:MASKFile`` command.

    Description:
        - This command sets or queries the mask file.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:MASKFile?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour:MASKFile?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:MASKFile value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:MASKFile  <string>
        - DPOJET:PLOT<x>:BERContour:MASKFile?
        ```
    """


class DpojetPlotItemBercontourMask(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:MASK`` command.

    Description:
        - This command sets or queries the eye state, either on or off.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:MASK?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour:MASK?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:BERContour:MASK value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:MASK {1 | 0}
        - DPOJET:PLOT<x>:BERContour:MASK?
        ```
    """


class DpojetPlotItemBercontourHorizontalResolution(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:HORizontal:RESolution`` command.

    Description:
        - This command sets or queries the Horizontal Eye resolution.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:PLOT<x>:BERContour:HORizontal:RESolution?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:HORizontal:RESolution?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:HORizontal:RESolution value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:HORizontal:RESolution  <NR3>
        - DPOJET:PLOT<x>:BERContour:HORizontal:RESolution?
        ```
    """


class DpojetPlotItemBercontourHorizontalAutoscale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale`` command.

    Description:
        - This command sets or queries the horizontal auto scale setting.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale {1 | 0}
        - DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale?
        ```
    """


class DpojetPlotItemBercontourHorizontal(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:HORizontal?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:HORizontal?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.autoscale``: The ``DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale`` command.
        - ``.resolution``: The ``DPOJET:PLOT<x>:BERContour:HORizontal:RESolution`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoscale = DpojetPlotItemBercontourHorizontalAutoscale(
            device, f"{self._cmd_syntax}:AUTOscale"
        )
        self._resolution = DpojetPlotItemBercontourHorizontalResolution(
            device, f"{self._cmd_syntax}:RESolution"
        )

    @property
    def autoscale(self) -> DpojetPlotItemBercontourHorizontalAutoscale:
        """Return the ``DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale`` command.

        Description:
            - This command sets or queries the horizontal auto scale setting.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale {1 | 0}
            - DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale?
            ```
        """
        return self._autoscale

    @property
    def resolution(self) -> DpojetPlotItemBercontourHorizontalResolution:
        """Return the ``DPOJET:PLOT<x>:BERContour:HORizontal:RESolution`` command.

        Description:
            - This command sets or queries the Horizontal Eye resolution.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:PLOT<x>:BERContour:HORizontal:RESolution?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:HORizontal:RESolution?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:HORizontal:RESolution value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:HORizontal:RESolution  <NR3>
            - DPOJET:PLOT<x>:BERContour:HORizontal:RESolution?
            ```
        """
        return self._resolution


class DpojetPlotItemBercontourBer1e9v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:BER1E9V`` command.

    Description:
        - This command sets or queries the BER1E9 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E9V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E9V?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:BER1E9V value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:BER1E9V {1 | 0}
        - DPOJET:PLOT<x>:BERContour:BER1E9V?
        ```
    """


class DpojetPlotItemBercontourBer1e6v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:BER1E6V`` command.

    Description:
        - This command sets or queries the BER1E6 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E6V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E6V?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:BER1E6V value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:BER1E6V {1 | 0}
        - DPOJET:PLOT<x>:BERContour:BER1E6V?
        ```
    """


class DpojetPlotItemBercontourBer1e18v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:BER1E18V`` command.

    Description:
        - This command sets or queries the BER1E18 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E18V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E18V?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:BER1E18V value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:BER1E18V {1 | 0}
        - DPOJET:PLOT<x>:BERContour:BER1E18V?
        ```
    """


class DpojetPlotItemBercontourBer1e15v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:BER1E15V`` command.

    Description:
        - This command sets or queries the BER1E15 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E15V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E15V?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:BER1E15V value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:BER1E15V {1 | 0}
        - DPOJET:PLOT<x>:BERContour:BER1E15V?
        ```
    """


class DpojetPlotItemBercontourBer1e12v(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:BER1E12V`` command.

    Description:
        - This command sets or queries the BER1E12 Contour display.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E12V?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E12V?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:BER1E12V value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:BER1E12V {1 | 0}
        - DPOJET:PLOT<x>:BERContour:BER1E12V?
        ```
    """


class DpojetPlotItemBercontourAlignment(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour:ALIGNment`` command.

    Description:
        - This command sets or queries the BER contour alighment.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:ALIGNment?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour:ALIGNment?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BERContour:ALIGNment value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BERContour:ALIGNment {AUTO | LEFT | CENter}
        - DPOJET:PLOT<x>:BERContour:ALIGNment?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetPlotItemBercontour(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BERContour`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.alignment``: The ``DPOJET:PLOT<x>:BERContour:ALIGNment`` command.
        - ``.ber1e12v``: The ``DPOJET:PLOT<x>:BERContour:BER1E12V`` command.
        - ``.ber1e15v``: The ``DPOJET:PLOT<x>:BERContour:BER1E15V`` command.
        - ``.ber1e18v``: The ``DPOJET:PLOT<x>:BERContour:BER1E18V`` command.
        - ``.ber1e6v``: The ``DPOJET:PLOT<x>:BERContour:BER1E6V`` command.
        - ``.ber1e9v``: The ``DPOJET:PLOT<x>:BERContour:BER1E9V`` command.
        - ``.horizontal``: The ``DPOJET:PLOT<x>:BERContour:HORizontal`` command tree.
        - ``.mask``: The ``DPOJET:PLOT<x>:BERContour:MASK`` command.
        - ``.maskfile``: The ``DPOJET:PLOT<x>:BERContour:MASKFile`` command.
        - ``.superimpose``: The ``DPOJET:PLOT<x>:BERContour:SUPERImpose`` command.
        - ``.targetber``: The ``DPOJET:PLOT<x>:BERContour:TARGETBER`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._alignment = DpojetPlotItemBercontourAlignment(device, f"{self._cmd_syntax}:ALIGNment")
        self._ber1e12v = DpojetPlotItemBercontourBer1e12v(device, f"{self._cmd_syntax}:BER1E12V")
        self._ber1e15v = DpojetPlotItemBercontourBer1e15v(device, f"{self._cmd_syntax}:BER1E15V")
        self._ber1e18v = DpojetPlotItemBercontourBer1e18v(device, f"{self._cmd_syntax}:BER1E18V")
        self._ber1e6v = DpojetPlotItemBercontourBer1e6v(device, f"{self._cmd_syntax}:BER1E6V")
        self._ber1e9v = DpojetPlotItemBercontourBer1e9v(device, f"{self._cmd_syntax}:BER1E9V")
        self._horizontal = DpojetPlotItemBercontourHorizontal(
            device, f"{self._cmd_syntax}:HORizontal"
        )
        self._mask = DpojetPlotItemBercontourMask(device, f"{self._cmd_syntax}:MASK")
        self._maskfile = DpojetPlotItemBercontourMaskfile(device, f"{self._cmd_syntax}:MASKFile")
        self._superimpose = DpojetPlotItemBercontourSuperimpose(
            device, f"{self._cmd_syntax}:SUPERImpose"
        )
        self._targetber = DpojetPlotItemBercontourTargetber(device, f"{self._cmd_syntax}:TARGETBER")

    @property
    def alignment(self) -> DpojetPlotItemBercontourAlignment:
        """Return the ``DPOJET:PLOT<x>:BERContour:ALIGNment`` command.

        Description:
            - This command sets or queries the BER contour alighment.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:ALIGNment?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:ALIGNment?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:ALIGNment value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:ALIGNment {AUTO | LEFT | CENter}
            - DPOJET:PLOT<x>:BERContour:ALIGNment?
            ```
        """
        return self._alignment

    @property
    def ber1e12v(self) -> DpojetPlotItemBercontourBer1e12v:
        """Return the ``DPOJET:PLOT<x>:BERContour:BER1E12V`` command.

        Description:
            - This command sets or queries the BER1E12 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E12V?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:BER1E12V?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:BER1E12V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:BER1E12V {1 | 0}
            - DPOJET:PLOT<x>:BERContour:BER1E12V?
            ```
        """
        return self._ber1e12v

    @property
    def ber1e15v(self) -> DpojetPlotItemBercontourBer1e15v:
        """Return the ``DPOJET:PLOT<x>:BERContour:BER1E15V`` command.

        Description:
            - This command sets or queries the BER1E15 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E15V?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:BER1E15V?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:BER1E15V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:BER1E15V {1 | 0}
            - DPOJET:PLOT<x>:BERContour:BER1E15V?
            ```
        """
        return self._ber1e15v

    @property
    def ber1e18v(self) -> DpojetPlotItemBercontourBer1e18v:
        """Return the ``DPOJET:PLOT<x>:BERContour:BER1E18V`` command.

        Description:
            - This command sets or queries the BER1E18 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E18V?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:BER1E18V?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:BER1E18V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:BER1E18V {1 | 0}
            - DPOJET:PLOT<x>:BERContour:BER1E18V?
            ```
        """
        return self._ber1e18v

    @property
    def ber1e6v(self) -> DpojetPlotItemBercontourBer1e6v:
        """Return the ``DPOJET:PLOT<x>:BERContour:BER1E6V`` command.

        Description:
            - This command sets or queries the BER1E6 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E6V?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:BER1E6V?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:BER1E6V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:BER1E6V {1 | 0}
            - DPOJET:PLOT<x>:BERContour:BER1E6V?
            ```
        """
        return self._ber1e6v

    @property
    def ber1e9v(self) -> DpojetPlotItemBercontourBer1e9v:
        """Return the ``DPOJET:PLOT<x>:BERContour:BER1E9V`` command.

        Description:
            - This command sets or queries the BER1E9 Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:BER1E9V?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:BER1E9V?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:BER1E9V value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:BER1E9V {1 | 0}
            - DPOJET:PLOT<x>:BERContour:BER1E9V?
            ```
        """
        return self._ber1e9v

    @property
    def horizontal(self) -> DpojetPlotItemBercontourHorizontal:
        """Return the ``DPOJET:PLOT<x>:BERContour:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.autoscale``: The ``DPOJET:PLOT<x>:BERContour:HORizontal:AUTOscale`` command.
            - ``.resolution``: The ``DPOJET:PLOT<x>:BERContour:HORizontal:RESolution`` command.
        """
        return self._horizontal

    @property
    def mask(self) -> DpojetPlotItemBercontourMask:
        """Return the ``DPOJET:PLOT<x>:BERContour:MASK`` command.

        Description:
            - This command sets or queries the eye state, either on or off.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:MASK?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour:MASK?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:MASK value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:MASK {1 | 0}
            - DPOJET:PLOT<x>:BERContour:MASK?
            ```
        """
        return self._mask

    @property
    def maskfile(self) -> DpojetPlotItemBercontourMaskfile:
        """Return the ``DPOJET:PLOT<x>:BERContour:MASKFile`` command.

        Description:
            - This command sets or queries the mask file.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:MASKFile?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:MASKFile?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:MASKFile value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:MASKFile  <string>
            - DPOJET:PLOT<x>:BERContour:MASKFile?
            ```
        """
        return self._maskfile

    @property
    def superimpose(self) -> DpojetPlotItemBercontourSuperimpose:
        """Return the ``DPOJET:PLOT<x>:BERContour:SUPERImpose`` command.

        Description:
            - This command sets or queries whether superimposed eyes are generated in eye diagrams.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:SUPERImpose?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:SUPERImpose?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:SUPERImpose value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:SUPERImpose {1 | 0}
            - DPOJET:PLOT<x>:BERContour:SUPERImpose?
            ```
        """
        return self._superimpose

    @property
    def targetber(self) -> DpojetPlotItemBercontourTargetber:
        """Return the ``DPOJET:PLOT<x>:BERContour:TARGETBER`` command.

        Description:
            - This command sets or queries the Target BER Contour display.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour:TARGETBER?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:TARGETBER?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BERContour:TARGETBER value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BERContour:TARGETBER {1 | 0}
            - DPOJET:PLOT<x>:BERContour:TARGETBER?
            ```
        """
        return self._targetber


class DpojetPlotItemBathtubXaxisunits(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BATHtub:XAXISUnits`` command.

    Description:
        - This command sets or queries the X-Axis Units of Bathtub.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BATHtub:XAXISUnits?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BATHtub:XAXISUnits?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BATHtub:XAXISUnits value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BATHtub:XAXISUnits { UNITIntervals | SECOnds }
        - DPOJET:PLOT<x>:BATHtub:XAXISUnits?
        ```
    """


class DpojetPlotItemBathtubVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BATHtub:VERTical:SCALE`` command.

    Description:
        - This command sets or queries the vertical scale setting for applicable plots, either
          Linear or Log.Undefined for nonbathtub plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BATHtub:VERTical:SCALE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:PLOT<x>:BATHtub:VERTical:SCALE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:PLOT<x>:BATHtub:VERTical:SCALE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BATHtub:VERTical:SCALE {LINEAR | LOG}
        - DPOJET:PLOT<x>:BATHtub:VERTical:SCALE?
        ```
    """


class DpojetPlotItemBathtubVertical(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BATHtub:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BATHtub:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BATHtub:VERTical?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DPOJET:PLOT<x>:BATHtub:VERTical:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DpojetPlotItemBathtubVerticalScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DpojetPlotItemBathtubVerticalScale:
        """Return the ``DPOJET:PLOT<x>:BATHtub:VERTical:SCALE`` command.

        Description:
            - This command sets or queries the vertical scale setting for applicable plots, either
              Linear or Log.Undefined for nonbathtub plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BATHtub:VERTical:SCALE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BATHtub:VERTical:SCALE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BATHtub:VERTical:SCALE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BATHtub:VERTical:SCALE {LINEAR | LOG}
            - DPOJET:PLOT<x>:BATHtub:VERTical:SCALE?
            ```
        """
        return self._scale


class DpojetPlotItemBathtubBer(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BATHtub:BER`` command.

    Description:
        - This command sets or queries the bathtub BER value.Undefined for nonbathtub plots.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BATHtub:BER?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BATHtub:BER?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:BATHtub:BER value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:PLOT<x>:BATHtub:BER  <NR3>
        - DPOJET:PLOT<x>:BATHtub:BER?
        ```
    """


class DpojetPlotItemBathtub(SCPICmdRead):
    """The ``DPOJET:PLOT<x>:BATHtub`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BATHtub?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BATHtub?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ber``: The ``DPOJET:PLOT<x>:BATHtub:BER`` command.
        - ``.vertical``: The ``DPOJET:PLOT<x>:BATHtub:VERTical`` command tree.
        - ``.xaxisunits``: The ``DPOJET:PLOT<x>:BATHtub:XAXISUnits`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ber = DpojetPlotItemBathtubBer(device, f"{self._cmd_syntax}:BER")
        self._vertical = DpojetPlotItemBathtubVertical(device, f"{self._cmd_syntax}:VERTical")
        self._xaxisunits = DpojetPlotItemBathtubXaxisunits(device, f"{self._cmd_syntax}:XAXISUnits")

    @property
    def ber(self) -> DpojetPlotItemBathtubBer:
        """Return the ``DPOJET:PLOT<x>:BATHtub:BER`` command.

        Description:
            - This command sets or queries the bathtub BER value.Undefined for nonbathtub plots.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BATHtub:BER?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BATHtub:BER?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:PLOT<x>:BATHtub:BER value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BATHtub:BER  <NR3>
            - DPOJET:PLOT<x>:BATHtub:BER?
            ```
        """
        return self._ber

    @property
    def vertical(self) -> DpojetPlotItemBathtubVertical:
        """Return the ``DPOJET:PLOT<x>:BATHtub:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BATHtub:VERTical?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BATHtub:VERTical?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DPOJET:PLOT<x>:BATHtub:VERTical:SCALE`` command.
        """
        return self._vertical

    @property
    def xaxisunits(self) -> DpojetPlotItemBathtubXaxisunits:
        """Return the ``DPOJET:PLOT<x>:BATHtub:XAXISUnits`` command.

        Description:
            - This command sets or queries the X-Axis Units of Bathtub.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BATHtub:XAXISUnits?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:BATHtub:XAXISUnits?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:PLOT<x>:BATHtub:XAXISUnits value`` command.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:BATHtub:XAXISUnits { UNITIntervals | SECOnds }
            - DPOJET:PLOT<x>:BATHtub:XAXISUnits?
            ```
        """
        return self._xaxisunits


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class DpojetPlotItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DPOJET:PLOT<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bathtub``: The ``DPOJET:PLOT<x>:BATHtub`` command tree.
        - ``.bercontour``: The ``DPOJET:PLOT<x>:BERContour`` command tree.
        - ``.bereye``: The ``DPOJET:PLOT<x>:BEREye`` command tree.
        - ``.compositejitterhist``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist`` command tree.
        - ``.compositenoisehist``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist`` command tree.
        - ``.correlatedeye``: The ``DPOJET:PLOT<x>:CORRELATEDEye`` command tree.
        - ``.currentuisacquired``: The ``DPOJET:PLOT<x>:CURRENTUISACquired`` command.
        - ``.currentuisanalyzed``: The ``DPOJET:PLOT<x>:CURRENTUISANalyzed`` command.
        - ``.data``: The ``DPOJET:PLOT<x>:DATA`` command tree.
        - ``.exportraw``: The ``DPOJET:PLOT<x>:EXPORTRaw`` command.
        - ``.eye``: The ``DPOJET:PLOT<x>:EYE`` command tree.
        - ``.histogram``: The ``DPOJET:PLOT<x>:HISTOgram`` command tree.
        - ``.noisebathtub``: The ``DPOJET:PLOT<x>:NOISEBATHtub`` command tree.
        - ``.pdfeye``: The ``DPOJET:PLOT<x>:PDFEye`` command tree.
        - ``.phasenoise``: The ``DPOJET:PLOT<x>:PHASEnoise`` command tree.
        - ``.source``: The ``DPOJET:PLOT<x>:SOUrce`` command.
        - ``.spectrum``: The ``DPOJET:PLOT<x>:SPECtrum`` command tree.
        - ``.totaluisacquired``: The ``DPOJET:PLOT<x>:TOTALUISAcquired`` command.
        - ``.totaluisanalyzed``: The ``DPOJET:PLOT<x>:TOTALUISAnalyzed`` command.
        - ``.transfer``: The ``DPOJET:PLOT<x>:TRANSfer`` command tree.
        - ``.trend``: The ``DPOJET:PLOT<x>:TREND`` command tree.
        - ``.type``: The ``DPOJET:PLOT<x>:TYPe`` command.
        - ``.vertbathtub``: The ``DPOJET:PLOT<x>:VERTBATHtub`` command tree.
        - ``.xunits``: The ``DPOJET:PLOT<x>:XUnits`` command.
        - ``.yunits``: The ``DPOJET:PLOT<x>:YUnits`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bathtub = DpojetPlotItemBathtub(device, f"{self._cmd_syntax}:BATHtub")
        self._bercontour = DpojetPlotItemBercontour(device, f"{self._cmd_syntax}:BERContour")
        self._bereye = DpojetPlotItemBereye(device, f"{self._cmd_syntax}:BEREye")
        self._compositejitterhist = DpojetPlotItemCompositejitterhist(
            device, f"{self._cmd_syntax}:COMPOSITEJitterhist"
        )
        self._compositenoisehist = DpojetPlotItemCompositenoisehist(
            device, f"{self._cmd_syntax}:COMPOSITENoisehist"
        )
        self._correlatedeye = DpojetPlotItemCorrelatedeye(
            device, f"{self._cmd_syntax}:CORRELATEDEye"
        )
        self._currentuisacquired = DpojetPlotItemCurrentuisacquired(
            device, f"{self._cmd_syntax}:CURRENTUISACquired"
        )
        self._currentuisanalyzed = DpojetPlotItemCurrentuisanalyzed(
            device, f"{self._cmd_syntax}:CURRENTUISANalyzed"
        )
        self._data = DpojetPlotItemData(device, f"{self._cmd_syntax}:DATA")
        self._exportraw = DpojetPlotItemExportraw(device, f"{self._cmd_syntax}:EXPORTRaw")
        self._eye = DpojetPlotItemEye(device, f"{self._cmd_syntax}:EYE")
        self._histogram = DpojetPlotItemHistogram(device, f"{self._cmd_syntax}:HISTOgram")
        self._noisebathtub = DpojetPlotItemNoisebathtub(device, f"{self._cmd_syntax}:NOISEBATHtub")
        self._pdfeye = DpojetPlotItemPdfeye(device, f"{self._cmd_syntax}:PDFEye")
        self._phasenoise = DpojetPlotItemPhasenoise(device, f"{self._cmd_syntax}:PHASEnoise")
        self._source = DpojetPlotItemSource(device, f"{self._cmd_syntax}:SOUrce")
        self._spectrum = DpojetPlotItemSpectrum(device, f"{self._cmd_syntax}:SPECtrum")
        self._totaluisacquired = DpojetPlotItemTotaluisacquired(
            device, f"{self._cmd_syntax}:TOTALUISAcquired"
        )
        self._totaluisanalyzed = DpojetPlotItemTotaluisanalyzed(
            device, f"{self._cmd_syntax}:TOTALUISAnalyzed"
        )
        self._transfer = DpojetPlotItemTransfer(device, f"{self._cmd_syntax}:TRANSfer")
        self._trend = DpojetPlotItemTrend(device, f"{self._cmd_syntax}:TREND")
        self._type = DpojetPlotItemType(device, f"{self._cmd_syntax}:TYPe")
        self._vertbathtub = DpojetPlotItemVertbathtub(device, f"{self._cmd_syntax}:VERTBATHtub")
        self._xunits = DpojetPlotItemXunits(device, f"{self._cmd_syntax}:XUnits")
        self._yunits = DpojetPlotItemYunits(device, f"{self._cmd_syntax}:YUnits")

    @property
    def bathtub(self) -> DpojetPlotItemBathtub:
        """Return the ``DPOJET:PLOT<x>:BATHtub`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BATHtub?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BATHtub?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ber``: The ``DPOJET:PLOT<x>:BATHtub:BER`` command.
            - ``.vertical``: The ``DPOJET:PLOT<x>:BATHtub:VERTical`` command tree.
            - ``.xaxisunits``: The ``DPOJET:PLOT<x>:BATHtub:XAXISUnits`` command.
        """
        return self._bathtub

    @property
    def bercontour(self) -> DpojetPlotItemBercontour:
        """Return the ``DPOJET:PLOT<x>:BERContour`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BERContour?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BERContour?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.alignment``: The ``DPOJET:PLOT<x>:BERContour:ALIGNment`` command.
            - ``.ber1e12v``: The ``DPOJET:PLOT<x>:BERContour:BER1E12V`` command.
            - ``.ber1e15v``: The ``DPOJET:PLOT<x>:BERContour:BER1E15V`` command.
            - ``.ber1e18v``: The ``DPOJET:PLOT<x>:BERContour:BER1E18V`` command.
            - ``.ber1e6v``: The ``DPOJET:PLOT<x>:BERContour:BER1E6V`` command.
            - ``.ber1e9v``: The ``DPOJET:PLOT<x>:BERContour:BER1E9V`` command.
            - ``.horizontal``: The ``DPOJET:PLOT<x>:BERContour:HORizontal`` command tree.
            - ``.mask``: The ``DPOJET:PLOT<x>:BERContour:MASK`` command.
            - ``.maskfile``: The ``DPOJET:PLOT<x>:BERContour:MASKFile`` command.
            - ``.superimpose``: The ``DPOJET:PLOT<x>:BERContour:SUPERImpose`` command.
            - ``.targetber``: The ``DPOJET:PLOT<x>:BERContour:TARGETBER`` command.
        """
        return self._bercontour

    @property
    def bereye(self) -> DpojetPlotItemBereye:
        """Return the ``DPOJET:PLOT<x>:BEREye`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:BEREye?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:BEREye?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ber1e12v``: The ``DPOJET:PLOT<x>:BEREye:BER1E12V`` command.
            - ``.ber1e15v``: The ``DPOJET:PLOT<x>:BEREye:BER1E15V`` command.
            - ``.ber1e18v``: The ``DPOJET:PLOT<x>:BEREye:BER1E18V`` command.
            - ``.ber1e6v``: The ``DPOJET:PLOT<x>:BEREye:BER1E6V`` command.
            - ``.ber1e9v``: The ``DPOJET:PLOT<x>:BEREye:BER1E9V`` command.
            - ``.targetber``: The ``DPOJET:PLOT<x>:BEREye:TARGETBER`` command.
        """
        return self._bereye

    @property
    def compositejitterhist(self) -> DpojetPlotItemCompositejitterhist:
        """Return the ``DPOJET:PLOT<x>:COMPOSITEJitterhist`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITEJitterhist?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITEJitterhist?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ddjdcd``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:DDJDCD`` command.
            - ``.numbins``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:NUMBins`` command.
            - ``.pj``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:PJ`` command.
            - ``.rjnpj``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:RJNPJ`` command.
            - ``.tj``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:TJ`` command.
            - ``.vertical``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist:VERTical`` command tree.
        """
        return self._compositejitterhist

    @property
    def compositenoisehist(self) -> DpojetPlotItemCompositenoisehist:
        """Return the ``DPOJET:PLOT<x>:COMPOSITENoisehist`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:COMPOSITENoisehist?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:COMPOSITENoisehist?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ddnone``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNONE`` command.
            - ``.ddnzero``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:DDNZERO`` command.
            - ``.horizontal``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:HORizontal`` command tree.
            - ``.numbins``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:NUMBins`` command.
            - ``.pn``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:PN`` command.
            - ``.rnnpn``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:RNNPN`` command.
            - ``.tn``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist:TN`` command.
        """
        return self._compositenoisehist

    @property
    def correlatedeye(self) -> DpojetPlotItemCorrelatedeye:
        """Return the ``DPOJET:PLOT<x>:CORRELATEDEye`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:CORRELATEDEye?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ber1e12v``: The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E12V`` command.
            - ``.ber1e15v``: The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E15V`` command.
            - ``.ber1e18v``: The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E18V`` command.
            - ``.ber1e6v``: The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E6V`` command.
            - ``.ber1e9v``: The ``DPOJET:PLOT<x>:CORRELATEDEye:BER1E9V`` command.
            - ``.eyeheight``: The ``DPOJET:PLOT<x>:CORRELATEDEye:EYEHEIGHT`` command.
            - ``.eyewidth``: The ``DPOJET:PLOT<x>:CORRELATEDEye:EYEWIDTH`` command.
            - ``.targetber``: The ``DPOJET:PLOT<x>:CORRELATEDEye:TARGETBER`` command.
        """
        return self._correlatedeye

    @property
    def currentuisacquired(self) -> DpojetPlotItemCurrentuisacquired:
        """Return the ``DPOJET:PLOT<x>:CURRENTUISACquired`` command.

        Description:
            - This command queries the current UIs acquired for eye diagram plot.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CURRENTUISACquired?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:CURRENTUISACquired?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:CURRENTUISACquired?
            ```
        """
        return self._currentuisacquired

    @property
    def currentuisanalyzed(self) -> DpojetPlotItemCurrentuisanalyzed:
        """Return the ``DPOJET:PLOT<x>:CURRENTUISANalyzed`` command.

        Description:
            - This command queries the current UIs analyzed for Eye Diagram plot.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:CURRENTUISANalyzed?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:PLOT<x>:CURRENTUISANalyzed?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:CURRENTUISANalyzed?
            ```
        """
        return self._currentuisanalyzed

    @property
    def data(self) -> DpojetPlotItemData:
        """Return the ``DPOJET:PLOT<x>:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.xdata``: The ``DPOJET:PLOT<x>:DATA:XDATa`` command.
            - ``.ydata``: The ``DPOJET:PLOT<x>:DATA:YDATa`` command.
        """
        return self._data

    @property
    def exportraw(self) -> DpojetPlotItemExportraw:
        """Return the ``DPOJET:PLOT<x>:EXPORTRaw`` command.

        Description:
            - This query command returns the raw Eye diagram 2d histogram data in binary format.
              This command is similar to curve query

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EXPORTRaw?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EXPORTRaw?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:EXPORTRaw?
            ```
        """
        return self._exportraw

    @property
    def eye(self) -> DpojetPlotItemEye:
        """Return the ``DPOJET:PLOT<x>:EYE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:EYE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:EYE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.alignment``: The ``DPOJET:PLOT<x>:EYE:ALIGNment`` command.
            - ``.eyeverticalscale``: The ``DPOJET:PLOT<x>:EYE:EYEVerticalscale`` command.
            - ``.horizscale``: The ``DPOJET:PLOT<x>:EYE:HORIZScale`` command.
            - ``.horizontal``: The ``DPOJET:PLOT<x>:EYE:HORizontal`` command tree.
            - ``.interpolationfactor``: The ``DPOJET:PLOT<x>:EYE:INTERPOLATIONFactor`` command.
            - ``.interpolationtype``: The ``DPOJET:PLOT<x>:EYE:INTERPolationtype`` command.
            - ``.maskfile``: The ``DPOJET:PLOT<x>:EYE:MASKfile`` command.
            - ``.state``: The ``DPOJET:PLOT<x>:EYE:STATE`` command.
            - ``.superimpose``: The ``DPOJET:PLOT<x>:EYE:SUPERImpose`` command.
            - ``.verticalalignment``: The ``DPOJET:PLOT<x>:EYE:VERTICALAlignment`` command.
            - ``.vertscale``: The ``DPOJET:PLOT<x>:EYE:VERTScale`` command.
            - ``.vertical``: The ``DPOJET:PLOT<x>:EYE:VERTical`` command tree.
        """
        return self._eye

    @property
    def histogram(self) -> DpojetPlotItemHistogram:
        """Return the ``DPOJET:PLOT<x>:HISTOgram`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:HISTOgram?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:HISTOgram?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autoset``: The ``DPOJET:PLOT<x>:HISTOgram:AUTOset`` command.
            - ``.horizontal``: The ``DPOJET:PLOT<x>:HISTOgram:HORizontal`` command tree.
            - ``.numbins``: The ``DPOJET:PLOT<x>:HISTOgram:NUMBins`` command.
            - ``.vertical``: The ``DPOJET:PLOT<x>:HISTOgram:VERTical`` command tree.
        """
        return self._histogram

    @property
    def noisebathtub(self) -> DpojetPlotItemNoisebathtub:
        """Return the ``DPOJET:PLOT<x>:NOISEBATHtub`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:NOISEBATHtub?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:NOISEBATHtub?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.yaxisunits``: The ``DPOJET:PLOT<x>:NOISEBATHtub:YAXISUnits`` command.
        """
        return self._noisebathtub

    @property
    def pdfeye(self) -> DpojetPlotItemPdfeye:
        """Return the ``DPOJET:PLOT<x>:PDFEye`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PDFEye?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PDFEye?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ber1e12v``: The ``DPOJET:PLOT<x>:PDFEye:BER1E12V`` command.
            - ``.ber1e15v``: The ``DPOJET:PLOT<x>:PDFEye:BER1E15V`` command.
            - ``.ber1e18v``: The ``DPOJET:PLOT<x>:PDFEye:BER1E18V`` command.
            - ``.ber1e6v``: The ``DPOJET:PLOT<x>:PDFEye:BER1E6V`` command.
            - ``.ber1e9v``: The ``DPOJET:PLOT<x>:PDFEye:BER1E9V`` command.
            - ``.targetber``: The ``DPOJET:PLOT<x>:PDFEye:TARGETBER`` command.
        """
        return self._pdfeye

    @property
    def phasenoise(self) -> DpojetPlotItemPhasenoise:
        """Return the ``DPOJET:PLOT<x>:PHASEnoise`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:PHASEnoise?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:PHASEnoise?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.baseline``: The ``DPOJET:PLOT<x>:PHASEnoise:BASEline`` command.
            - ``.smootheningfilter``: The ``DPOJET:PLOT<x>:PHASEnoise:SMOOTHENINGFilter`` command.
        """
        return self._phasenoise

    @property
    def source(self) -> DpojetPlotItemSource:
        """Return the ``DPOJET:PLOT<x>:SOUrce`` command.

        Description:
            - This query-only command returns the source measurement for the selected plot.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:SOUrce?
            ```
        """
        return self._source

    @property
    def spectrum(self) -> DpojetPlotItemSpectrum:
        """Return the ``DPOJET:PLOT<x>:SPECtrum`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:SPECtrum?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:SPECtrum?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.base``: The ``DPOJET:PLOT<x>:SPECtrum:BASE`` command.
            - ``.horizontal``: The ``DPOJET:PLOT<x>:SPECtrum:HORizontal`` command tree.
            - ``.mode``: The ``DPOJET:PLOT<x>:SPECtrum:MODE`` command.
            - ``.vertical``: The ``DPOJET:PLOT<x>:SPECtrum:VERTical`` command tree.
        """
        return self._spectrum

    @property
    def totaluisacquired(self) -> DpojetPlotItemTotaluisacquired:
        """Return the ``DPOJET:PLOT<x>:TOTALUISAcquired`` command.

        Description:
            - This command queries the total UIs acquired for Eye Diagram plot

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TOTALUISAcquired?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TOTALUISAcquired?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:TOTALUISAcquired?
            ```
        """
        return self._totaluisacquired

    @property
    def totaluisanalyzed(self) -> DpojetPlotItemTotaluisanalyzed:
        """Return the ``DPOJET:PLOT<x>:TOTALUISAnalyzed`` command.

        Description:
            - This command queries the total UIs analysed for Eye Diagram plot.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TOTALUISAnalyzed?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TOTALUISAnalyzed?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:TOTALUISAnalyzed?
            ```
        """
        return self._totaluisanalyzed

    @property
    def transfer(self) -> DpojetPlotItemTransfer:
        """Return the ``DPOJET:PLOT<x>:TRANSfer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TRANSfer?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TRANSfer?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.denominator``: The ``DPOJET:PLOT<x>:TRANSfer:DENominator`` command.
            - ``.horizontal``: The ``DPOJET:PLOT<x>:TRANSfer:HORizontal`` command tree.
            - ``.mode``: The ``DPOJET:PLOT<x>:TRANSfer:MODE`` command.
            - ``.numerator``: The ``DPOJET:PLOT<x>:TRANSfer:NUMerator`` command.
            - ``.vertical``: The ``DPOJET:PLOT<x>:TRANSfer:VERTical`` command tree.
        """
        return self._transfer

    @property
    def trend(self) -> DpojetPlotItemTrend:
        """Return the ``DPOJET:PLOT<x>:TREND`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TREND?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TREND?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.type``: The ``DPOJET:PLOT<x>:TREND:TYPe`` command.
        """
        return self._trend

    @property
    def type(self) -> DpojetPlotItemType:
        """Return the ``DPOJET:PLOT<x>:TYPe`` command.

        Description:
            - This query-only command returns the current plot type for the selected plot.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:TYPe?
            ```
        """
        return self._type

    @property
    def vertbathtub(self) -> DpojetPlotItemVertbathtub:
        """Return the ``DPOJET:PLOT<x>:VERTBATHtub`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:VERTBATHtub?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ber``: The ``DPOJET:PLOT<x>:VERTBATHtub:BER`` command.
            - ``.horizontal``: The ``DPOJET:PLOT<x>:VERTBATHtub:HORizontal`` command tree.
            - ``.yaxisunits``: The ``DPOJET:PLOT<x>:VERTBATHtub:YAXISUnits`` command.
        """
        return self._vertbathtub

    @property
    def xunits(self) -> DpojetPlotItemXunits:
        """Return the ``DPOJET:PLOT<x>:XUnits`` command.

        Description:
            - This query-only command returns X units of the plot as a string.Plot units depends on
              the measurement type.Click here to see the possible

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:XUnits?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:XUnits?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:XUnits?
            ```
        """
        return self._xunits

    @property
    def yunits(self) -> DpojetPlotItemYunits:
        """Return the ``DPOJET:PLOT<x>:YUnits`` command.

        Description:
            - This query-only command returns Y units of the plot as a string.Plot units depends on
              the measurement type.Click here to see the possible

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>:YUnits?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>:YUnits?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:PLOT<x>:YUnits?
            ```
        """
        return self._yunits


class DpojetOpticalunittype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:OPTICALUNITType`` command.

    Description:
        - This command sets or queries the current optical unit-type setting for DPOJET, either
          Watt, or dBm.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:OPTICALUNITType?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:OPTICALUNITType?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:OPTICALUNITType value`` command.

    SCPI Syntax:
        ```
        - DPOJET:OPTICALUNITType {WATT | DBM}
        - DPOJET:OPTICALUNITType?
        ```
    """


class DpojetNumplot(SCPICmdRead):
    """The ``DPOJET:NUMPlot`` command.

    Description:
        - This query-only command returns the current number of plots added. If no plots are added,
          then it returns 0, else returns the total number of plots added between value 1 to 4.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:NUMPlot?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:NUMPlot?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:NUMPlot?
        ```
    """


class DpojetNummeas(SCPICmdRead):
    """The ``DPOJET:NUMMeas`` command.

    Description:
        - This query-only command returns the current number of defined measurements.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:NUMMeas?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:NUMMeas?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:NUMMeas?
        ```
    """


class DpojetNoiseenabled(SCPICmdWrite):
    """The ``DPOJET:NOISEENABLED`` command.

    Description:
        - This set-only command turns on or off the Noise measurements.Configure

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:NOISEENABLED value`` command.

    SCPI Syntax:
        ```
        - DPOJET:NOISEENABLED {1 | 0 | ON | OFF}
        ```
    """


class DpojetMinbujui(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MINBUJUI`` command.

    Description:
        - This command sets or queries the minimum number of UI for BUJ analysis.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MINBUJUI?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MINBUJUI?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MINBUJUI value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MINBUJUI  <NR3>
        - DPOJET:MINBUJUI?
        ```
    """


class DpojetMeasItemZoomevent(SCPICmdWrite):
    """The ``DPOJET:MEAS<x>:ZOOMEVENT`` command.

    Description:
        - This command zooms into the waveform where a max/min value occurs in a measurement.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:ZOOMEVENT value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:ZOOMEVENT {MAX | MIN}
        ```
    """


class DpojetMeasItemToedge(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:TOEdge`` command.

    Description:
        - This command sets the TOEdge value for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:TOEdge?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:TOEdge?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:TOEdge value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:TOEdge {SAMEas | OPPositeas}
        - DPOJET:MEAS<x>:TOEdge?
        ```
    """


class DpojetMeasItemTimedata(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:TIMEDATa`` command.

    Description:
        - This query-only command returns the measurement time data. It is similar to the curve
          query, where the output is in the format #<x><yyy><data><newline>, where <x> is the number
          of <y> bytes.For Example: If <yyy>=500, <x>=3<x> is hexadecimal format. The letters A-F
          denote the number of y bytes between 10 and 15 digits.<yyy> is the number of bytes to
          transfer.<data> is curve data.<newline> is a single-byte new line character at the end of
          the data.Time data is not available for all measurements. For Example: Scalar
          measurements.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:TIMEDATa?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:TIMEDATa?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:TIMEDATa?
        ```
    """


class DpojetMeasItemSscNominalfreqSelectiontype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype`` command.

    Description:
        - This command sets or queries the Nominal frequency selection type for the SSC
          configurations.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype {AUTO | MANUAL}
        - DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype?
        ```
    """


class DpojetMeasItemSscNominalfreqManual(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual`` command.

    Description:
        - This command sets or queries the user-defined nominal frequency value for SSC
          configurations.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual  <NR3>
        - DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual?
        ```
    """


class DpojetMeasItemSscNominalfreqAuto(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:SSC:NOMinalfreq:AUTO`` command.

    Description:
        - This query-only command returns the automatically-calculated nominal frequency value for
          SSC configurations.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SSC:NOMinalfreq:AUTO?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:SSC:NOMinalfreq:AUTO?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:SSC:NOMinalfreq:AUTO?
        ```
    """


class DpojetMeasItemSscNominalfreq(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:SSC:NOMinalfreq`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SSC:NOMinalfreq?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:SSC:NOMinalfreq?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.auto``: The ``DPOJET:MEAS<x>:SSC:NOMinalfreq:AUTO`` command.
        - ``.manual``: The ``DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual`` command.
        - ``.selectiontype``: The ``DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._auto = DpojetMeasItemSscNominalfreqAuto(device, f"{self._cmd_syntax}:AUTO")
        self._manual = DpojetMeasItemSscNominalfreqManual(device, f"{self._cmd_syntax}:MANual")
        self._selectiontype = DpojetMeasItemSscNominalfreqSelectiontype(
            device, f"{self._cmd_syntax}:SELECTIONtype"
        )

    @property
    def auto(self) -> DpojetMeasItemSscNominalfreqAuto:
        """Return the ``DPOJET:MEAS<x>:SSC:NOMinalfreq:AUTO`` command.

        Description:
            - This query-only command returns the automatically-calculated nominal frequency value
              for SSC configurations.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SSC:NOMinalfreq:AUTO?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:SSC:NOMinalfreq:AUTO?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:SSC:NOMinalfreq:AUTO?
            ```
        """
        return self._auto

    @property
    def manual(self) -> DpojetMeasItemSscNominalfreqManual:
        """Return the ``DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual`` command.

        Description:
            - This command sets or queries the user-defined nominal frequency value for SSC
              configurations.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual  <NR3>
            - DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual?
            ```
        """
        return self._manual

    @property
    def selectiontype(self) -> DpojetMeasItemSscNominalfreqSelectiontype:
        """Return the ``DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype`` command.

        Description:
            - This command sets or queries the Nominal frequency selection type for the SSC
              configurations.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype {AUTO | MANUAL}
            - DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype?
            ```
        """
        return self._selectiontype


class DpojetMeasItemSsc(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:SSC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SSC?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:SSC?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.nominalfreq``: The ``DPOJET:MEAS<x>:SSC:NOMinalfreq`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._nominalfreq = DpojetMeasItemSscNominalfreq(device, f"{self._cmd_syntax}:NOMinalfreq")

    @property
    def nominalfreq(self) -> DpojetMeasItemSscNominalfreq:
        """Return the ``DPOJET:MEAS<x>:SSC:NOMinalfreq`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SSC:NOMinalfreq?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:SSC:NOMinalfreq?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.auto``: The ``DPOJET:MEAS<x>:SSC:NOMinalfreq:AUTO`` command.
            - ``.manual``: The ``DPOJET:MEAS<x>:SSC:NOMinalfreq:MANual`` command.
            - ``.selectiontype``: The ``DPOJET:MEAS<x>:SSC:NOMinalfreq:SELECTIONtype`` command.
        """
        return self._nominalfreq


class DpojetMeasItemSource2(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:SOUrce2`` command.

    Description:
        - This command sets or queries the Source2 value. May return NONE for single-source
          measurement. Source2 may be the second source used in dual-source measurements, or the
          clock source in others. In either case, it is always the same as the rightmost displayed
          source on the UI.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SOUrce2?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:SOUrce2?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:SOUrce2 value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:SOUrce2 {CH1 - CH4 | MATH1 - MATH4 | REF1 - REF4 | D0 — D15}
        - DPOJET:MEAS<x>:SOUrce2?
        ```
    """


class DpojetMeasItemSource1(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:SOUrce1`` command.

    Description:
        - This command sets or queries the Source1 value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:SOUrce1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:SOUrce1 value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:SOUrce1 {CH1 - CH4 | MATH1 - MATH4 | REF1 - REF4 | D0 — D15}
        - DPOJET:MEAS<x>:SOUrce1?
        ```
    """


class DpojetMeasItemSignaltype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:SIGNALType`` command.

    Description:
        - This command sets the signal type for various measurements.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SIGNALType?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:SIGNALType?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:SIGNALType value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:SIGNALType {CLOCK | DATA | AUTO}
        - DPOJET:MEAS<x>:SIGNALType?
        ```
    """


class DpojetMeasItemRndnWindowlength(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RNDN:WINDOwlength`` command.

    Description:
        - This command sets or queries the current RNDN window length.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:WINDOwlength?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:WINDOwlength?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:RNDN:WINDOwlength value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RNDN:WINDOwlength  <NR3>
        - DPOJET:MEAS<x>:RNDN:WINDOwlength?
        ```
    """


class DpojetMeasItemRndnType(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RNDN:TYPe`` command.

    Description:
        - This command sets or queries the current RNDN measurement type.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:TYPe value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RNDN:TYPe {ARBITrary | REPEating}
        - DPOJET:MEAS<x>:RNDN:TYPe?
        ```
    """


class DpojetMeasItemRndnSncrefid(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RNDN:SNCREFID`` command.

    Description:
        - This command sets or queries the reference id which is used for fetching the noise value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:SNCREFID?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:SNCREFID?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:SNCREFID value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RNDN:SNCREFID  <string>
        - DPOJET:MEAS<x>:RNDN:SNCREFID?
        ```
    """


class DpojetMeasItemRndnScopern(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RNDN:SCOPERN`` command.

    Description:
        - This command to sets or queries the scope noise value from the applicable measurements.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:SCOPERN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:SCOPERN?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:SCOPERN value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RNDN:SCOPERN  <NR3>
        - DPOJET:MEAS<x>:RNDN:SCOPERN?
        ```
    """


class DpojetMeasItemRndnPatlen(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RNDN:PATLen`` command.

    Description:
        - This command sets or queries the current RNDN pattern length.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:PATLen?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:PATLen?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:PATLen value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RNDN:PATLen  <NR3>
        - DPOJET:MEAS<x>:RNDN:PATLen?
        ```
    """


class DpojetMeasItemRndnNcmode(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RNDN:NCMODe`` command.

    Description:
        - This command sets or queries the noise compensation mode.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:NCMODe?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:NCMODe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:NCMODe value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RNDN:NCMODe {1 | 0}
        - DPOJET:MEAS<x>:RNDN:NCMODe?
        ```
    """


class DpojetMeasItemRndnBer(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RNDN:BER`` command.

    Description:
        - This command sets or queries the RNDN Target BER value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:BER?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:BER?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:BER value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RNDN:BER  <NR3>
        - DPOJET:MEAS<x>:RNDN:BER?
        ```
    """


class DpojetMeasItemRndnAutodetectpattern(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RNDN:AUTODETECTpattern`` command.

    Description:
        - This command sets or queries the current pattern detection control plan.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:AUTODETECTpattern?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RNDN:AUTODETECTpattern?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:RNDN:AUTODETECTpattern value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RNDN:AUTODETECTpattern {1 | 0 | ON | OFF}
        - DPOJET:MEAS<x>:RNDN:AUTODETECTpattern?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetMeasItemRndn(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RNDN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autodetectpattern``: The ``DPOJET:MEAS<x>:RNDN:AUTODETECTpattern`` command.
        - ``.ber``: The ``DPOJET:MEAS<x>:RNDN:BER`` command.
        - ``.ncmode``: The ``DPOJET:MEAS<x>:RNDN:NCMODe`` command.
        - ``.patlen``: The ``DPOJET:MEAS<x>:RNDN:PATLen`` command.
        - ``.scopern``: The ``DPOJET:MEAS<x>:RNDN:SCOPERN`` command.
        - ``.sncrefid``: The ``DPOJET:MEAS<x>:RNDN:SNCREFID`` command.
        - ``.type``: The ``DPOJET:MEAS<x>:RNDN:TYPe`` command.
        - ``.windowlength``: The ``DPOJET:MEAS<x>:RNDN:WINDOwlength`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autodetectpattern = DpojetMeasItemRndnAutodetectpattern(
            device, f"{self._cmd_syntax}:AUTODETECTpattern"
        )
        self._ber = DpojetMeasItemRndnBer(device, f"{self._cmd_syntax}:BER")
        self._ncmode = DpojetMeasItemRndnNcmode(device, f"{self._cmd_syntax}:NCMODe")
        self._patlen = DpojetMeasItemRndnPatlen(device, f"{self._cmd_syntax}:PATLen")
        self._scopern = DpojetMeasItemRndnScopern(device, f"{self._cmd_syntax}:SCOPERN")
        self._sncrefid = DpojetMeasItemRndnSncrefid(device, f"{self._cmd_syntax}:SNCREFID")
        self._type = DpojetMeasItemRndnType(device, f"{self._cmd_syntax}:TYPe")
        self._windowlength = DpojetMeasItemRndnWindowlength(
            device, f"{self._cmd_syntax}:WINDOwlength"
        )

    @property
    def autodetectpattern(self) -> DpojetMeasItemRndnAutodetectpattern:
        """Return the ``DPOJET:MEAS<x>:RNDN:AUTODETECTpattern`` command.

        Description:
            - This command sets or queries the current pattern detection control plan.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:AUTODETECTpattern?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RNDN:AUTODETECTpattern?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:RNDN:AUTODETECTpattern value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RNDN:AUTODETECTpattern {1 | 0 | ON | OFF}
            - DPOJET:MEAS<x>:RNDN:AUTODETECTpattern?
            ```
        """
        return self._autodetectpattern

    @property
    def ber(self) -> DpojetMeasItemRndnBer:
        """Return the ``DPOJET:MEAS<x>:RNDN:BER`` command.

        Description:
            - This command sets or queries the RNDN Target BER value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:BER?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:BER?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:BER value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RNDN:BER  <NR3>
            - DPOJET:MEAS<x>:RNDN:BER?
            ```
        """
        return self._ber

    @property
    def ncmode(self) -> DpojetMeasItemRndnNcmode:
        """Return the ``DPOJET:MEAS<x>:RNDN:NCMODe`` command.

        Description:
            - This command sets or queries the noise compensation mode.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:NCMODe?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:NCMODe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:NCMODe value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RNDN:NCMODe {1 | 0}
            - DPOJET:MEAS<x>:RNDN:NCMODe?
            ```
        """
        return self._ncmode

    @property
    def patlen(self) -> DpojetMeasItemRndnPatlen:
        """Return the ``DPOJET:MEAS<x>:RNDN:PATLen`` command.

        Description:
            - This command sets or queries the current RNDN pattern length.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:PATLen?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:PATLen?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:PATLen value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RNDN:PATLen  <NR3>
            - DPOJET:MEAS<x>:RNDN:PATLen?
            ```
        """
        return self._patlen

    @property
    def scopern(self) -> DpojetMeasItemRndnScopern:
        """Return the ``DPOJET:MEAS<x>:RNDN:SCOPERN`` command.

        Description:
            - This command to sets or queries the scope noise value from the applicable
              measurements.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:SCOPERN?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:SCOPERN?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:SCOPERN value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RNDN:SCOPERN  <NR3>
            - DPOJET:MEAS<x>:RNDN:SCOPERN?
            ```
        """
        return self._scopern

    @property
    def sncrefid(self) -> DpojetMeasItemRndnSncrefid:
        """Return the ``DPOJET:MEAS<x>:RNDN:SNCREFID`` command.

        Description:
            - This command sets or queries the reference id which is used for fetching the noise
              value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:SNCREFID?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:SNCREFID?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:RNDN:SNCREFID value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RNDN:SNCREFID  <string>
            - DPOJET:MEAS<x>:RNDN:SNCREFID?
            ```
        """
        return self._sncrefid

    @property
    def type(self) -> DpojetMeasItemRndnType:
        """Return the ``DPOJET:MEAS<x>:RNDN:TYPe`` command.

        Description:
            - This command sets or queries the current RNDN measurement type.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RNDN:TYPe value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RNDN:TYPe {ARBITrary | REPEating}
            - DPOJET:MEAS<x>:RNDN:TYPe?
            ```
        """
        return self._type

    @property
    def windowlength(self) -> DpojetMeasItemRndnWindowlength:
        """Return the ``DPOJET:MEAS<x>:RNDN:WINDOwlength`` command.

        Description:
            - This command sets or queries the current RNDN window length.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN:WINDOwlength?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RNDN:WINDOwlength?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:RNDN:WINDOwlength value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RNDN:WINDOwlength  <NR3>
            - DPOJET:MEAS<x>:RNDN:WINDOwlength?
            ```
        """
        return self._windowlength


class DpojetMeasItemRjdjWindowlength(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RJDJ:WINDOwlength`` command.

    Description:
        - This command sets or queries the current RJDJ window length.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:WINDOwlength?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:WINDOwlength?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:RJDJ:WINDOwlength value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RJDJ:WINDOwlength  <NR3>
        - DPOJET:MEAS<x>:RJDJ:WINDOwlength?
        ```
    """


class DpojetMeasItemRjdjType(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RJDJ:TYPe`` command.

    Description:
        - This command sets or queries the current RJDJ measurement type.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:TYPe value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RJDJ:TYPe {ARBITrary | REPEating}
        - DPOJET:MEAS<x>:RJDJ:TYPe?
        ```
    """


class DpojetMeasItemRjdjSncrefid(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RJDJ:SNCREFID`` command.

    Description:
        - This command sets or queries the reference id which is used for fetching the noise value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:SNCREFID?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:SNCREFID?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:SNCREFID value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RJDJ:SNCREFID  <string>
        - DPOJET:MEAS<x>:RJDJ:SNCREFID?
        ```
    """


class DpojetMeasItemRjdjScopern(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RJDJ:SCOPERN`` command.

    Description:
        - This command to sets or queries the scope noise value from the applicable measurements.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:SCOPERN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:SCOPERN?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:SCOPERN value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RJDJ:SCOPERN  <NR3>
        - DPOJET:MEAS<x>:RJDJ:SCOPERN?
        ```
    """


class DpojetMeasItemRjdjPatlen(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RJDJ:PATLen`` command.

    Description:
        - This command sets or queries the current RJDJ pattern length.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:PATLen?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:PATLen?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:PATLen value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RJDJ:PATLen  <NR3>
        - DPOJET:MEAS<x>:RJDJ:PATLen?
        ```
    """


class DpojetMeasItemRjdjNcmode(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RJDJ:NCMODe`` command.

    Description:
        - This command sets or queries the noise compensation mode, Auto or Manual.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:NCMODe?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:NCMODe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:NCMODe value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RJDJ:NCMODe {1 | 0}
        - DPOJET:MEAS<x>:RJDJ:NCMODe?
        ```
    """


class DpojetMeasItemRjdjDetectplen(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RJDJ:DETECTPLEN`` command.

    Description:
        - This command sets or queries the current detect plan.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:DETECTPLEN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:DETECTPLEN?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:DETECTPLEN value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RJDJ:DETECTPLEN {0 | 1 | ON | OFF}
        - DPOJET:MEAS<x>:RJDJ:DETECTPLEN?
        ```
    """


class DpojetMeasItemRjdjBer(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RJDJ:BER`` command.

    Description:
        - This command sets or queries the RJDJ Target BER value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:BER?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:BER?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:BER value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RJDJ:BER  <NR3>
        - DPOJET:MEAS<x>:RJDJ:BER?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetMeasItemRjdj(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RJDJ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ber``: The ``DPOJET:MEAS<x>:RJDJ:BER`` command.
        - ``.detectplen``: The ``DPOJET:MEAS<x>:RJDJ:DETECTPLEN`` command.
        - ``.ncmode``: The ``DPOJET:MEAS<x>:RJDJ:NCMODe`` command.
        - ``.patlen``: The ``DPOJET:MEAS<x>:RJDJ:PATLen`` command.
        - ``.scopern``: The ``DPOJET:MEAS<x>:RJDJ:SCOPERN`` command.
        - ``.sncrefid``: The ``DPOJET:MEAS<x>:RJDJ:SNCREFID`` command.
        - ``.type``: The ``DPOJET:MEAS<x>:RJDJ:TYPe`` command.
        - ``.windowlength``: The ``DPOJET:MEAS<x>:RJDJ:WINDOwlength`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ber = DpojetMeasItemRjdjBer(device, f"{self._cmd_syntax}:BER")
        self._detectplen = DpojetMeasItemRjdjDetectplen(device, f"{self._cmd_syntax}:DETECTPLEN")
        self._ncmode = DpojetMeasItemRjdjNcmode(device, f"{self._cmd_syntax}:NCMODe")
        self._patlen = DpojetMeasItemRjdjPatlen(device, f"{self._cmd_syntax}:PATLen")
        self._scopern = DpojetMeasItemRjdjScopern(device, f"{self._cmd_syntax}:SCOPERN")
        self._sncrefid = DpojetMeasItemRjdjSncrefid(device, f"{self._cmd_syntax}:SNCREFID")
        self._type = DpojetMeasItemRjdjType(device, f"{self._cmd_syntax}:TYPe")
        self._windowlength = DpojetMeasItemRjdjWindowlength(
            device, f"{self._cmd_syntax}:WINDOwlength"
        )

    @property
    def ber(self) -> DpojetMeasItemRjdjBer:
        """Return the ``DPOJET:MEAS<x>:RJDJ:BER`` command.

        Description:
            - This command sets or queries the RJDJ Target BER value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:BER?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:BER?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:BER value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RJDJ:BER  <NR3>
            - DPOJET:MEAS<x>:RJDJ:BER?
            ```
        """
        return self._ber

    @property
    def detectplen(self) -> DpojetMeasItemRjdjDetectplen:
        """Return the ``DPOJET:MEAS<x>:RJDJ:DETECTPLEN`` command.

        Description:
            - This command sets or queries the current detect plan.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:DETECTPLEN?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:DETECTPLEN?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:RJDJ:DETECTPLEN value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RJDJ:DETECTPLEN {0 | 1 | ON | OFF}
            - DPOJET:MEAS<x>:RJDJ:DETECTPLEN?
            ```
        """
        return self._detectplen

    @property
    def ncmode(self) -> DpojetMeasItemRjdjNcmode:
        """Return the ``DPOJET:MEAS<x>:RJDJ:NCMODe`` command.

        Description:
            - This command sets or queries the noise compensation mode, Auto or Manual.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:NCMODe?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:NCMODe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:NCMODe value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RJDJ:NCMODe {1 | 0}
            - DPOJET:MEAS<x>:RJDJ:NCMODe?
            ```
        """
        return self._ncmode

    @property
    def patlen(self) -> DpojetMeasItemRjdjPatlen:
        """Return the ``DPOJET:MEAS<x>:RJDJ:PATLen`` command.

        Description:
            - This command sets or queries the current RJDJ pattern length.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:PATLen?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:PATLen?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:PATLen value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RJDJ:PATLen  <NR3>
            - DPOJET:MEAS<x>:RJDJ:PATLen?
            ```
        """
        return self._patlen

    @property
    def scopern(self) -> DpojetMeasItemRjdjScopern:
        """Return the ``DPOJET:MEAS<x>:RJDJ:SCOPERN`` command.

        Description:
            - This command to sets or queries the scope noise value from the applicable
              measurements.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:SCOPERN?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:SCOPERN?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:SCOPERN value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RJDJ:SCOPERN  <NR3>
            - DPOJET:MEAS<x>:RJDJ:SCOPERN?
            ```
        """
        return self._scopern

    @property
    def sncrefid(self) -> DpojetMeasItemRjdjSncrefid:
        """Return the ``DPOJET:MEAS<x>:RJDJ:SNCREFID`` command.

        Description:
            - This command sets or queries the reference id which is used for fetching the noise
              value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:SNCREFID?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:SNCREFID?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:RJDJ:SNCREFID value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RJDJ:SNCREFID  <string>
            - DPOJET:MEAS<x>:RJDJ:SNCREFID?
            ```
        """
        return self._sncrefid

    @property
    def type(self) -> DpojetMeasItemRjdjType:
        """Return the ``DPOJET:MEAS<x>:RJDJ:TYPe`` command.

        Description:
            - This command sets or queries the current RJDJ measurement type.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ:TYPe value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RJDJ:TYPe {ARBITrary | REPEating}
            - DPOJET:MEAS<x>:RJDJ:TYPe?
            ```
        """
        return self._type

    @property
    def windowlength(self) -> DpojetMeasItemRjdjWindowlength:
        """Return the ``DPOJET:MEAS<x>:RJDJ:WINDOwlength`` command.

        Description:
            - This command sets or queries the current RJDJ window length.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ:WINDOwlength?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RJDJ:WINDOwlength?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:RJDJ:WINDOwlength value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RJDJ:WINDOwlength  <NR3>
            - DPOJET:MEAS<x>:RJDJ:WINDOwlength?
            ```
        """
        return self._windowlength


class DpojetMeasItemResultsView(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:VIew`` command.

    Description:
        - This query-only command returns the results view type.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:VIew?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:VIew?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:VIew?
        ```
    """


class DpojetMeasItemResultsStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:STATus`` command.

    Description:
        - This query-only command returns the status of the given measurement values in slot
          MEAS<x>. Valid for currently valid measurements, or the error status such as “Not enough
          edges”.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:STATus?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:STATus?
        ```
    """


class DpojetMeasItemResultsGetall(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:GETAll`` command.

    Description:
        - The query-only command returns results of given measurement in xml format with units.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:GETAll?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:GETAll?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:GETAll?
        ```
    """


class DpojetMeasItemResultsCurrentacqStddevStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the standard deviation
          measurement for the currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev:STATus?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev:STATus?
        ```
    """


class DpojetMeasItemResultsCurrentacqStddev(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev`` command.

    Description:
        - This query-only command returns the standard deviation of the measurement value for the
          currently selected measurement for measurement slot <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsCurrentacqStddevStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsCurrentacqStddevStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the standard deviation
              measurement for the currently loaded limit file. (Set using
              ``DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev:STATus?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsCurrentacqPopulationStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the population measurement for
          the currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation:STATus?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation:STATus?
        ```
    """


class DpojetMeasItemResultsCurrentacqPopulation(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation`` command.

    Description:
        - This query-only command returns the population measurement value for the currently
          selected measurement for measurement slot <x>.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsCurrentacqPopulationStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsCurrentacqPopulationStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the population measurement
              for the currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation:STATus?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsCurrentacqPk2pkStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the peak-to-peak measurement for
          the currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK:STATus?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK:STATus?
        ```
    """


class DpojetMeasItemResultsCurrentacqPk2pk(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK`` command.

    Description:
        - This query-only command returns the peak-to-peak value for the currently selected
          measurement for measurement slot <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsCurrentacqPk2pkStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsCurrentacqPk2pkStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the peak-to-peak measurement
              for the currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK:STATus?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsCurrentacqMinccStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the min cycle-to-cycle
          measurement for the currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC:STATus?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC:STATus?
        ```
    """


class DpojetMeasItemResultsCurrentacqMincc(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC`` command.

    Description:
        - This query-only command returns the maximum negative cycle-to-cycle delta of the selected
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsCurrentacqMinccStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsCurrentacqMinccStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the min cycle-to-cycle
              measurement for the currently loaded limit file. (Set using
              ``DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC:STATus?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsCurrentacqMinStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the minimum measurement for the
          currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN:STATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:MIN:STATus?
        ```
    """


class DpojetMeasItemResultsCurrentacqMin(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN`` command.

    Description:
        - This query-only command returns the minimum value for the currently selected measurement
          for measurement slot <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:MIN?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsCurrentacqMinStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsCurrentacqMinStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the minimum measurement for
              the currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN:STATus?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:MIN:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsCurrentacqMeanStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the mean measurement for the
          currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN:STATus?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN:STATus?
        ```
    """


class DpojetMeasItemResultsCurrentacqMean(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN`` command.

    Description:
        - This query-only command returns the mean value of the measurement for the current
          acquisition or for the most recent processing cycle.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsCurrentacqMeanStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsCurrentacqMeanStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the mean measurement for the
              currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN:STATus?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsCurrentacqMaxccStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the Max cycle-to-cycle
          measurement for the currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC:STATus?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC:STATus?
        ```
    """


class DpojetMeasItemResultsCurrentacqMaxcc(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC`` command.

    Description:
        - This query-only command returns the maximum positive cycle-to-cycle delta of the selected
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsCurrentacqMaxccStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsCurrentacqMaxccStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the Max cycle-to-cycle
              measurement for the currently loaded limit file. (Set using
              ``DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC:STATus?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsCurrentacqMaxStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the max measurement for the
          currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX:STATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:MAX:STATus?
        ```
    """


class DpojetMeasItemResultsCurrentacqMax(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX`` command.

    Description:
        - This query-only command returns the maximum value of the measurement value for the
          currently selected measurement for measurement slot <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:CURRentacq:MAX?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsCurrentacqMaxStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsCurrentacqMaxStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the max measurement for the
              currently loaded limit file. (Set using ``DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX:STATus?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:MAX:STATus?
            ```
        """
        return self._status


#  pylint: disable=too-many-instance-attributes
class DpojetMeasItemResultsCurrentacq(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:CURRentacq`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX`` command.
        - ``.maxcc``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC`` command.
        - ``.mean``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN`` command.
        - ``.min``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN`` command.
        - ``.mincc``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC`` command.
        - ``.pk2pk``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK`` command.
        - ``.population``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation`` command.
        - ``.stddev``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = DpojetMeasItemResultsCurrentacqMax(device, f"{self._cmd_syntax}:MAX")
        self._maxcc = DpojetMeasItemResultsCurrentacqMaxcc(device, f"{self._cmd_syntax}:MAXCC")
        self._mean = DpojetMeasItemResultsCurrentacqMean(device, f"{self._cmd_syntax}:MEAN")
        self._min = DpojetMeasItemResultsCurrentacqMin(device, f"{self._cmd_syntax}:MIN")
        self._mincc = DpojetMeasItemResultsCurrentacqMincc(device, f"{self._cmd_syntax}:MINCC")
        self._pk2pk = DpojetMeasItemResultsCurrentacqPk2pk(device, f"{self._cmd_syntax}:PK2PK")
        self._population = DpojetMeasItemResultsCurrentacqPopulation(
            device, f"{self._cmd_syntax}:POPUlation"
        )
        self._stddev = DpojetMeasItemResultsCurrentacqStddev(device, f"{self._cmd_syntax}:STDDev")

    @property
    def max(self) -> DpojetMeasItemResultsCurrentacqMax:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX`` command.

        Description:
            - This query-only command returns the maximum value of the measurement value for the
              currently selected measurement for measurement slot <x>.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:MAX?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX:STATus`` command.
        """
        return self._max

    @property
    def maxcc(self) -> DpojetMeasItemResultsCurrentacqMaxcc:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC`` command.

        Description:
            - This query-only command returns the maximum positive cycle-to-cycle delta of the
              selected measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC:STATus`` command.
        """
        return self._maxcc

    @property
    def mean(self) -> DpojetMeasItemResultsCurrentacqMean:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN`` command.

        Description:
            - This query-only command returns the mean value of the measurement for the current
              acquisition or for the most recent processing cycle.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN:STATus`` command.
        """
        return self._mean

    @property
    def min(self) -> DpojetMeasItemResultsCurrentacqMin:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN`` command.

        Description:
            - This query-only command returns the minimum value for the currently selected
              measurement for measurement slot <x>.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:MIN?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN:STATus`` command.
        """
        return self._min

    @property
    def mincc(self) -> DpojetMeasItemResultsCurrentacqMincc:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC`` command.

        Description:
            - This query-only command returns the maximum negative cycle-to-cycle delta of the
              selected measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC:STATus`` command.
        """
        return self._mincc

    @property
    def pk2pk(self) -> DpojetMeasItemResultsCurrentacqPk2pk:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK`` command.

        Description:
            - This query-only command returns the peak-to-peak value for the currently selected
              measurement for measurement slot <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK:STATus`` command.
        """
        return self._pk2pk

    @property
    def population(self) -> DpojetMeasItemResultsCurrentacqPopulation:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation`` command.

        Description:
            - This query-only command returns the population measurement value for the currently
              selected measurement for measurement slot <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation:STATus`` command.
        """
        return self._population

    @property
    def stddev(self) -> DpojetMeasItemResultsCurrentacqStddev:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev`` command.

        Description:
            - This query-only command returns the standard deviation of the measurement value for
              the currently selected measurement for measurement slot <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev:STATus`` command.
        """
        return self._stddev


class DpojetMeasItemResultsAllacqsStddevStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the standard deviation
          measurement for the currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev:STATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev:STATus?
        ```
    """


class DpojetMeasItemResultsAllacqsStddev(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev`` command.

    Description:
        - This query-only command returns the standard deviation for all accumulated measurement
          acquisitions for slot <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsAllacqsStddevStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsAllacqsStddevStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the standard deviation
              measurement for the currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev:STATus?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsAllacqsSegItemMinhits(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MINHits`` command.

    Description:
        - This query-only command returns the minimum mask hits measurement for the given segment,
          either SEG1, SEG2 or SEG3.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MINHits?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MINHits?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MINHits?
        ```
    """


class DpojetMeasItemResultsAllacqsSegItemMaxhits(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MAXHits`` command.

    Description:
        - This query-only command returnseturns the maximum mask hits measurement for the given
          segment, either SEG1, SEG2 or SEG3.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MAXHits?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MAXHits?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MAXHits?
        ```
    """


class DpojetMeasItemResultsAllacqsSegItemHits(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:Hits`` command.

    Description:
        - This query-only command returns the mask hits measurement for the given segment, either
          SEG1, SEG2 or SEG3.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:Hits?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:Hits?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:Hits?
        ```
    """


class DpojetMeasItemResultsAllacqsSegItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.hits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:Hits`` command.
        - ``.maxhits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MAXHits`` command.
        - ``.minhits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MINHits`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hits = DpojetMeasItemResultsAllacqsSegItemHits(device, f"{self._cmd_syntax}:Hits")
        self._maxhits = DpojetMeasItemResultsAllacqsSegItemMaxhits(
            device, f"{self._cmd_syntax}:MAXHits"
        )
        self._minhits = DpojetMeasItemResultsAllacqsSegItemMinhits(
            device, f"{self._cmd_syntax}:MINHits"
        )

    @property
    def hits(self) -> DpojetMeasItemResultsAllacqsSegItemHits:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:Hits`` command.

        Description:
            - This query-only command returns the mask hits measurement for the given segment,
              either SEG1, SEG2 or SEG3.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:Hits?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:Hits?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:Hits?
            ```
        """
        return self._hits

    @property
    def maxhits(self) -> DpojetMeasItemResultsAllacqsSegItemMaxhits:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MAXHits`` command.

        Description:
            - This query-only command returnseturns the maximum mask hits measurement for the given
              segment, either SEG1, SEG2 or SEG3.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MAXHits?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MAXHits?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MAXHits?
            ```
        """
        return self._maxhits

    @property
    def minhits(self) -> DpojetMeasItemResultsAllacqsSegItemMinhits:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MINHits`` command.

        Description:
            - This query-only command returns the minimum mask hits measurement for the given
              segment, either SEG1, SEG2 or SEG3.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MINHits?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MINHits?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MINHits?
            ```
        """
        return self._minhits


class DpojetMeasItemResultsAllacqsPopulationStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the population measurement for
          the currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation:STATus?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation:STATus?
        ```
    """


class DpojetMeasItemResultsAllacqsPopulation(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation`` command.

    Description:
        - This query-only command returns the mean measurement value for the currently selected
          measurement for measurement slot <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsAllacqsPopulationStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsAllacqsPopulationStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the population measurement
              for the currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation:STATus?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsAllacqsPk2pkStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the peak-to-peak measurement for
          the currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK:STATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK:STATus?
        ```
    """


class DpojetMeasItemResultsAllacqsPk2pk(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK`` command.

    Description:
        - This query-only command returns the peak-to-peak value for all accumulated measurement
          acquisitions for slot <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsAllacqsPk2pkStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def status(self) -> DpojetMeasItemResultsAllacqsPk2pkStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the peak-to-peak measurement
              for the currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK:STATus?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsAllacqsMinhits(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINHits`` command.

    Description:
        - This query-only command returns the minimum mask hits measurement for all segments.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINHits?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINHits?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MINHits?
        ```
    """


class DpojetMeasItemResultsAllacqsMinccStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the negative cycle-to-cycle delta
          of the selected measurement.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC:STATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC:STATus?
        ```
    """


class DpojetMeasItemResultsAllacqsMincc(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC`` command.

    Description:
        - This query-only command returns the maximum negative cycle-to-cycle delta of the selected
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsAllacqsMinccStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def status(self) -> DpojetMeasItemResultsAllacqsMinccStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the negative cycle-to-cycle
              delta of the selected measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC:STATus?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsAllacqsMinStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the minimum measurement for the
          currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:STATus?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:STATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:STATus?
        ```
    """


class DpojetMeasItemResultsAllacqsMinLowmargin(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWMArgin`` command.

    Description:
        - This query-only command returns the low margin value of Min for measurement <x>.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWMArgin?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWMArgin?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWMArgin?
        ```
    """


class DpojetMeasItemResultsAllacqsMinLowlimit(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWLimit`` command.

    Description:
        - This query-only command returns the low limit value of Min for measurement <x>.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWLimit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWLimit?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWLimit?
        ```
    """


class DpojetMeasItemResultsAllacqsMin(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN`` command.

    Description:
        - This query-only command returns the minimum value for all accumulated measurement
          acquisitions for slot <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN?
        ```

    Properties:
        - ``.lowlimit``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWLimit`` command.
        - ``.lowmargin``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWMArgin`` command.
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lowlimit = DpojetMeasItemResultsAllacqsMinLowlimit(
            device, f"{self._cmd_syntax}:LOWLimit"
        )
        self._lowmargin = DpojetMeasItemResultsAllacqsMinLowmargin(
            device, f"{self._cmd_syntax}:LOWMArgin"
        )
        self._status = DpojetMeasItemResultsAllacqsMinStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def lowlimit(self) -> DpojetMeasItemResultsAllacqsMinLowlimit:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWLimit`` command.

        Description:
            - This query-only command returns the low limit value of Min for measurement <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWLimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWLimit?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWLimit?
            ```
        """
        return self._lowlimit

    @property
    def lowmargin(self) -> DpojetMeasItemResultsAllacqsMinLowmargin:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWMArgin`` command.

        Description:
            - This query-only command returns the low margin value of Min for measurement <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWMArgin?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWMArgin?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWMArgin?
            ```
        """
        return self._lowmargin

    @property
    def status(self) -> DpojetMeasItemResultsAllacqsMinStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the minimum measurement for
              the currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:STATus?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsAllacqsMeanStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the mean measurement for the
          currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:STATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:STATus?
        ```
    """


class DpojetMeasItemResultsAllacqsMeanHighlimit(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:HIGHLimit`` command.

    Description:
        - This query-only command returns the high limit value of Mean for measurement <x>.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:HIGHLimit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:HIGHLimit?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:HIGHLimit?
        ```
    """


class DpojetMeasItemResultsAllacqsMean(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN`` command.

    Description:
        - This query-only command returns the mean value for all accumulated measurement
          acquisitions for slot <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN?
        ```

    Properties:
        - ``.highlimit``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:HIGHLimit`` command.
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._highlimit = DpojetMeasItemResultsAllacqsMeanHighlimit(
            device, f"{self._cmd_syntax}:HIGHLimit"
        )
        self._status = DpojetMeasItemResultsAllacqsMeanStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def highlimit(self) -> DpojetMeasItemResultsAllacqsMeanHighlimit:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:HIGHLimit`` command.

        Description:
            - This query-only command returns the high limit value of Mean for measurement <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:HIGHLimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:HIGHLimit?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:HIGHLimit?
            ```
        """
        return self._highlimit

    @property
    def status(self) -> DpojetMeasItemResultsAllacqsMeanStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the mean measurement for the
              currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:STATus?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsAllacqsMaxhits(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXHits`` command.

    Description:
        - This query-only command returns the maximum mask hits measurement for all segments.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXHits?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXHits?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXHits?
        ```
    """


class DpojetMeasItemResultsAllacqsMaxccStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the maximum positive
          cycle-to-cycle delta of the selected measurement (set via ``:DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC:STATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC:STATus?
        ```
    """


class DpojetMeasItemResultsAllacqsMaxcc(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC`` command.

    Description:
        - This query-only command returns the maximum positive cycle-to-cycle delta of the selected
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC?
        ```

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsAllacqsMaxccStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def status(self) -> DpojetMeasItemResultsAllacqsMaxccStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the maximum positive
              cycle-to-cycle delta of the selected measurement (set via
              ``:DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC:STATus?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsAllacqsMaxStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for the max measurement for the
          currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:STATus?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:STATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:STATus?
        ```
    """


class DpojetMeasItemResultsAllacqsMaxHighmargin(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHMArgin`` command.

    Description:
        - This query-only command returns the high margin value of Max for measurement <x>.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHMArgin?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHMArgin?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHMArgin?
        ```
    """


class DpojetMeasItemResultsAllacqsMaxHighlimit(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHLimit`` command.

    Description:
        - This query-only command returns the high limit value of Max for measurement <x>.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHLimit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHLimit?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHLimit?
        ```
    """


class DpojetMeasItemResultsAllacqsMax(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX`` command.

    Description:
        - This query-only command returns the maximum value for all accumulated measurement
          acquisitions for slot <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX?
        ```

    Properties:
        - ``.highlimit``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHLimit`` command.
        - ``.highmargin``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHMArgin`` command.
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._highlimit = DpojetMeasItemResultsAllacqsMaxHighlimit(
            device, f"{self._cmd_syntax}:HIGHLimit"
        )
        self._highmargin = DpojetMeasItemResultsAllacqsMaxHighmargin(
            device, f"{self._cmd_syntax}:HIGHMArgin"
        )
        self._status = DpojetMeasItemResultsAllacqsMaxStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def highlimit(self) -> DpojetMeasItemResultsAllacqsMaxHighlimit:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHLimit`` command.

        Description:
            - This query-only command returns the high limit value of Max for measurement <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHLimit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHLimit?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHLimit?
            ```
        """
        return self._highlimit

    @property
    def highmargin(self) -> DpojetMeasItemResultsAllacqsMaxHighmargin:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHMArgin`` command.

        Description:
            - This query-only command returns the high margin value of Max for measurement <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHMArgin?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHMArgin?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHMArgin?
            ```
        """
        return self._highmargin

    @property
    def status(self) -> DpojetMeasItemResultsAllacqsMaxStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for the max measurement for the
              currently loaded limit file (set via ``:DPOJET:LIMits:FILEName``).

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:STATus?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsAllacqsLimitsStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status per measurement. If any of the
          statistics fails, the cumulative result is fail, otherwise pass.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:STATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:STATus?
        ```
    """


class DpojetMeasItemResultsAllacqsLimitsLowStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for low limit.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw:STATus?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw:STATus?
        ```
    """


class DpojetMeasItemResultsAllacqsLimitsLow(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsAllacqsLimitsLowStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsAllacqsLimitsLowStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for low limit.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw:STATus?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsAllacqsLimitsHighStatus(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh:STATus`` command.

    Description:
        - This query-only command returns the pass/fail status for high limit.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh:STATus?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh:STATus?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh:STATus?
        ```
    """


class DpojetMeasItemResultsAllacqsLimitsHigh(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = DpojetMeasItemResultsAllacqsLimitsHighStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def status(self) -> DpojetMeasItemResultsAllacqsLimitsHighStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status for high limit.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh:STATus?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsAllacqsLimits(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.high``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh`` command tree.
        - ``.low``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw`` command tree.
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = DpojetMeasItemResultsAllacqsLimitsHigh(device, f"{self._cmd_syntax}:HIgh")
        self._low = DpojetMeasItemResultsAllacqsLimitsLow(device, f"{self._cmd_syntax}:LOw")
        self._status = DpojetMeasItemResultsAllacqsLimitsStatus(
            device, f"{self._cmd_syntax}:STATus"
        )

    @property
    def high(self) -> DpojetMeasItemResultsAllacqsLimitsHigh:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh:STATus`` command.
        """
        return self._high

    @property
    def low(self) -> DpojetMeasItemResultsAllacqsLimitsLow:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw:STATus`` command.
        """
        return self._low

    @property
    def status(self) -> DpojetMeasItemResultsAllacqsLimitsStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:STATus`` command.

        Description:
            - This query-only command returns the pass/fail status per measurement. If any of the
              statistics fails, the cumulative result is fail, otherwise pass.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:STATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:STATus?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:STATus?
            ```
        """
        return self._status


class DpojetMeasItemResultsAllacqsHits(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITS`` command.

    Description:
        - This query-only command returns the mask hits measurement for all segments.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITS?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:HITS?
        ```
    """


class DpojetMeasItemResultsAllacqsHitpopulation(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITPopulation`` command.

    Description:
        - This query-only command returns the mask hit population.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITPopulation?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITPopulation?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs:HITPopulation?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetMeasItemResultsAllacqs(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts:ALLAcqs`` command.

    Description:
        - This query-only command returns the measurement results from all acquisitions.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts:ALLAcqs?
        ```

    Properties:
        - ``.hitpopulation``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITPopulation`` command.
        - ``.hits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITS`` command.
        - ``.limits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits`` command tree.
        - ``.max``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX`` command.
        - ``.maxcc``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC`` command.
        - ``.maxhits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXHits`` command.
        - ``.mean``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN`` command.
        - ``.min``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN`` command.
        - ``.mincc``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC`` command.
        - ``.minhits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINHits`` command.
        - ``.pk2pk``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK`` command.
        - ``.population``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation`` command.
        - ``.seg``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>`` command tree.
        - ``.stddev``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hitpopulation = DpojetMeasItemResultsAllacqsHitpopulation(
            device, f"{self._cmd_syntax}:HITPopulation"
        )
        self._hits = DpojetMeasItemResultsAllacqsHits(device, f"{self._cmd_syntax}:HITS")
        self._limits = DpojetMeasItemResultsAllacqsLimits(device, f"{self._cmd_syntax}:LIMits")
        self._max = DpojetMeasItemResultsAllacqsMax(device, f"{self._cmd_syntax}:MAX")
        self._maxcc = DpojetMeasItemResultsAllacqsMaxcc(device, f"{self._cmd_syntax}:MAXCC")
        self._maxhits = DpojetMeasItemResultsAllacqsMaxhits(device, f"{self._cmd_syntax}:MAXHits")
        self._mean = DpojetMeasItemResultsAllacqsMean(device, f"{self._cmd_syntax}:MEAN")
        self._min = DpojetMeasItemResultsAllacqsMin(device, f"{self._cmd_syntax}:MIN")
        self._mincc = DpojetMeasItemResultsAllacqsMincc(device, f"{self._cmd_syntax}:MINCC")
        self._minhits = DpojetMeasItemResultsAllacqsMinhits(device, f"{self._cmd_syntax}:MINHits")
        self._pk2pk = DpojetMeasItemResultsAllacqsPk2pk(device, f"{self._cmd_syntax}:PK2PK")
        self._population = DpojetMeasItemResultsAllacqsPopulation(
            device, f"{self._cmd_syntax}:POPUlation"
        )
        self._seg: Dict[int, DpojetMeasItemResultsAllacqsSegItem] = DefaultDictPassKeyToFactory(
            lambda x: DpojetMeasItemResultsAllacqsSegItem(device, f"{self._cmd_syntax}:SEG{x}")
        )
        self._stddev = DpojetMeasItemResultsAllacqsStddev(device, f"{self._cmd_syntax}:STDDev")

    @property
    def hitpopulation(self) -> DpojetMeasItemResultsAllacqsHitpopulation:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITPopulation`` command.

        Description:
            - This query-only command returns the mask hit population.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITPopulation?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITPopulation?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:HITPopulation?
            ```
        """
        return self._hitpopulation

    @property
    def hits(self) -> DpojetMeasItemResultsAllacqsHits:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITS`` command.

        Description:
            - This query-only command returns the mask hits measurement for all segments.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:HITS?
            ```
        """
        return self._hits

    @property
    def limits(self) -> DpojetMeasItemResultsAllacqsLimits:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:HIgh`` command tree.
            - ``.low``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:LOw`` command tree.
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits:STATus`` command.
        """
        return self._limits

    @property
    def max(self) -> DpojetMeasItemResultsAllacqsMax:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX`` command.

        Description:
            - This query-only command returns the maximum value for all accumulated measurement
              acquisitions for slot <x>.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX?
            ```

        Sub-properties:
            - ``.highlimit``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHLimit`` command.
            - ``.highmargin``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:HIGHMArgin`` command.
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX:STATus`` command.
        """
        return self._max

    @property
    def maxcc(self) -> DpojetMeasItemResultsAllacqsMaxcc:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC`` command.

        Description:
            - This query-only command returns the maximum positive cycle-to-cycle delta of the
              selected measurement.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC:STATus`` command.
        """
        return self._maxcc

    @property
    def maxhits(self) -> DpojetMeasItemResultsAllacqsMaxhits:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXHits`` command.

        Description:
            - This query-only command returns the maximum mask hits measurement for all segments.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXHits?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXHits?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXHits?
            ```
        """
        return self._maxhits

    @property
    def mean(self) -> DpojetMeasItemResultsAllacqsMean:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN`` command.

        Description:
            - This query-only command returns the mean value for all accumulated measurement
              acquisitions for slot <x>.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN?
            ```

        Sub-properties:
            - ``.highlimit``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:HIGHLimit`` command.
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN:STATus`` command.
        """
        return self._mean

    @property
    def min(self) -> DpojetMeasItemResultsAllacqsMin:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN`` command.

        Description:
            - This query-only command returns the minimum value for all accumulated measurement
              acquisitions for slot <x>.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN?
            ```

        Sub-properties:
            - ``.lowlimit``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWLimit`` command.
            - ``.lowmargin``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:LOWMArgin`` command.
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN:STATus`` command.
        """
        return self._min

    @property
    def mincc(self) -> DpojetMeasItemResultsAllacqsMincc:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC`` command.

        Description:
            - This query-only command returns the maximum negative cycle-to-cycle delta of the
              selected measurement.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC:STATus`` command.
        """
        return self._mincc

    @property
    def minhits(self) -> DpojetMeasItemResultsAllacqsMinhits:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINHits`` command.

        Description:
            - This query-only command returns the minimum mask hits measurement for all segments.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINHits?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINHits?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:MINHits?
            ```
        """
        return self._minhits

    @property
    def pk2pk(self) -> DpojetMeasItemResultsAllacqsPk2pk:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK`` command.

        Description:
            - This query-only command returns the peak-to-peak value for all accumulated measurement
              acquisitions for slot <x>.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK:STATus`` command.
        """
        return self._pk2pk

    @property
    def population(self) -> DpojetMeasItemResultsAllacqsPopulation:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation`` command.

        Description:
            - This query-only command returns the mean measurement value for the currently selected
              measurement for measurement slot <x>.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation:STATus`` command.
        """
        return self._population

    @property
    def seg(self) -> Dict[int, DpojetMeasItemResultsAllacqsSegItem]:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:Hits`` command.
            - ``.maxhits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MAXHits`` command.
            - ``.minhits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>:MINHits`` command.
        """
        return self._seg

    @property
    def stddev(self) -> DpojetMeasItemResultsAllacqsStddev:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev`` command.

        Description:
            - This query-only command returns the standard deviation for all accumulated measurement
              acquisitions for slot <x>.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev?
            ```

        Sub-properties:
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev:STATus`` command.
        """
        return self._stddev


class DpojetMeasItemResults(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:RESULts`` command.

    Description:
        - This query-only command returns the measurement branch for the currently selected
          measurement for measurement slot <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:RESULts?
        ```

    Properties:
        - ``.allacqs``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs`` command.
        - ``.currentacq``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq`` command tree.
        - ``.getall``: The ``DPOJET:MEAS<x>:RESULts:GETAll`` command.
        - ``.status``: The ``DPOJET:MEAS<x>:RESULts:STATus`` command.
        - ``.view``: The ``DPOJET:MEAS<x>:RESULts:VIew`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._allacqs = DpojetMeasItemResultsAllacqs(device, f"{self._cmd_syntax}:ALLAcqs")
        self._currentacq = DpojetMeasItemResultsCurrentacq(device, f"{self._cmd_syntax}:CURRentacq")
        self._getall = DpojetMeasItemResultsGetall(device, f"{self._cmd_syntax}:GETAll")
        self._status = DpojetMeasItemResultsStatus(device, f"{self._cmd_syntax}:STATus")
        self._view = DpojetMeasItemResultsView(device, f"{self._cmd_syntax}:VIew")

    @property
    def allacqs(self) -> DpojetMeasItemResultsAllacqs:
        """Return the ``DPOJET:MEAS<x>:RESULts:ALLAcqs`` command.

        Description:
            - This query-only command returns the measurement results from all acquisitions.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:ALLAcqs?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:ALLAcqs?
            ```

        Sub-properties:
            - ``.hitpopulation``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITPopulation`` command.
            - ``.hits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:HITS`` command.
            - ``.limits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:LIMits`` command tree.
            - ``.max``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAX`` command.
            - ``.maxcc``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXCC`` command.
            - ``.maxhits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MAXHits`` command.
            - ``.mean``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MEAN`` command.
            - ``.min``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MIN`` command.
            - ``.mincc``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINCC`` command.
            - ``.minhits``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:MINHits`` command.
            - ``.pk2pk``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:PK2PK`` command.
            - ``.population``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:POPUlation`` command.
            - ``.seg``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:SEG<x>`` command tree.
            - ``.stddev``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs:STDDev`` command.
        """
        return self._allacqs

    @property
    def currentacq(self) -> DpojetMeasItemResultsCurrentacq:
        """Return the ``DPOJET:MEAS<x>:RESULts:CURRentacq`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:CURRentacq?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:RESULts:CURRentacq?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAX`` command.
            - ``.maxcc``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MAXCC`` command.
            - ``.mean``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MEAN`` command.
            - ``.min``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MIN`` command.
            - ``.mincc``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:MINCC`` command.
            - ``.pk2pk``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:PK2PK`` command.
            - ``.population``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:POPUlation`` command.
            - ``.stddev``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq:STDDev`` command.
        """
        return self._currentacq

    @property
    def getall(self) -> DpojetMeasItemResultsGetall:
        """Return the ``DPOJET:MEAS<x>:RESULts:GETAll`` command.

        Description:
            - The query-only command returns results of given measurement in xml format with units.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:GETAll?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:GETAll?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:GETAll?
            ```
        """
        return self._getall

    @property
    def status(self) -> DpojetMeasItemResultsStatus:
        """Return the ``DPOJET:MEAS<x>:RESULts:STATus`` command.

        Description:
            - This query-only command returns the status of the given measurement values in slot
              MEAS<x>. Valid for currently valid measurements, or the error status such as “Not
              enough edges”.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:STATus?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:STATus?
            ```
        """
        return self._status

    @property
    def view(self) -> DpojetMeasItemResultsView:
        """Return the ``DPOJET:MEAS<x>:RESULts:VIew`` command.

        Description:
            - This query-only command returns the results view type.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts:VIew?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts:VIew?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts:VIew?
            ```
        """
        return self._view


class DpojetMeasItemRefvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:REFVoltage`` command.

    Description:
        - This command sets or queries the reference voltage for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:REFVoltage?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:REFVoltage?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:REFVoltage value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:REFVoltage {100 | —100}
        - DPOJET:MEAS<x>:REFVoltage?
        ```
    """


class DpojetMeasItemPlotfiles(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:PLOTFILES`` command.

    Description:
        - The query-only command returns plot file paths of a given measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:PLOTFILES?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:PLOTFILES?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:PLOTFILES?
        ```
    """


class DpojetMeasItemPhasenoiseLowlimit(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:PHASENoise:LOWLimit`` command.

    Description:
        - This command sets or queries the lower phase noise integration limit.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:PHASENoise:LOWLimit?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:PHASENoise:LOWLimit?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:PHASENoise:LOWLimit value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:PHASENoise:LOWLimit  <NR3>
        - DPOJET:MEAS<x>:PHASENoise:LOWLimit?
        ```
    """


class DpojetMeasItemPhasenoiseHighlimit(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:PHASENoise:HIGHLimit`` command.

    Description:
        - This command sets or queries the upper phase noise integration limit.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:PHASENoise:HIGHLimit?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:PHASENoise:HIGHLimit?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:PHASENoise:HIGHLimit value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:PHASENoise:HIGHLimit  <NR3>
        - DPOJET:MEAS<x>:PHASENoise:HIGHLimit?
        ```
    """


class DpojetMeasItemPhasenoise(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:PHASENoise`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:PHASENoise?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:PHASENoise?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.highlimit``: The ``DPOJET:MEAS<x>:PHASENoise:HIGHLimit`` command.
        - ``.lowlimit``: The ``DPOJET:MEAS<x>:PHASENoise:LOWLimit`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._highlimit = DpojetMeasItemPhasenoiseHighlimit(device, f"{self._cmd_syntax}:HIGHLimit")
        self._lowlimit = DpojetMeasItemPhasenoiseLowlimit(device, f"{self._cmd_syntax}:LOWLimit")

    @property
    def highlimit(self) -> DpojetMeasItemPhasenoiseHighlimit:
        """Return the ``DPOJET:MEAS<x>:PHASENoise:HIGHLimit`` command.

        Description:
            - This command sets or queries the upper phase noise integration limit.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:PHASENoise:HIGHLimit?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:PHASENoise:HIGHLimit?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:PHASENoise:HIGHLimit value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:PHASENoise:HIGHLimit  <NR3>
            - DPOJET:MEAS<x>:PHASENoise:HIGHLimit?
            ```
        """
        return self._highlimit

    @property
    def lowlimit(self) -> DpojetMeasItemPhasenoiseLowlimit:
        """Return the ``DPOJET:MEAS<x>:PHASENoise:LOWLimit`` command.

        Description:
            - This command sets or queries the lower phase noise integration limit.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:PHASENoise:LOWLimit?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:PHASENoise:LOWLimit?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:PHASENoise:LOWLimit value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:PHASENoise:LOWLimit  <NR3>
            - DPOJET:MEAS<x>:PHASENoise:LOWLimit?
            ```
        """
        return self._lowlimit


class DpojetMeasItemOpticalWfmtype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:OPTIcal:WFMTYpe`` command.

    Description:
        - This command sets or queries the optical waveform type.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:WFMTYpe?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:WFMTYpe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:WFMTYpe value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:OPTIcal:WFMTYpe {CONTINUOUS | MODULATED}
        - DPOJET:MEAS<x>:OPTIcal:WFMTYpe?
        ```
    """


class DpojetMeasItemOpticalTargetber(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:OPTIcal:TARGETBer`` command.

    Description:
        - This command sets or queries the Target BER value display. The 1E-Value = 10-Value

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:TARGETBer?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:TARGETBer?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:OPTIcal:TARGETBer value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:OPTIcal:TARGETBer  <NR3>
        - DPOJET:MEAS<x>:OPTIcal:TARGETBer?
        ```
    """


class DpojetMeasItemOpticalScopern(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:OPTIcal:SCOPERN`` command.

    Description:
        - This command sets or queries the Scope RN(rms) value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:SCOPERN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:SCOPERN?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:SCOPERN value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:OPTIcal:SCOPERN  <NR3>
        - DPOJET:MEAS<x>:OPTIcal:SCOPERN?
        ```
    """


class DpojetMeasItemOpticalFfetaps(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:OPTIcal:FFETAPS`` command.

    Description:
        - This command sets or queries current FFE tap file with absolute path.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:FFETAPS?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:FFETAPS?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:FFETAPS value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:OPTIcal:FFETAPS  <string>
        - DPOJET:MEAS<x>:OPTIcal:FFETAPS?
        ```
    """


class DpojetMeasItemOpticalBtfilter(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:OPTIcal:BTFILTEr`` command.

    Description:
        - This command sets or queries current BT Filter file with absolute path.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:BTFILTEr?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:BTFILTEr?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:BTFILTEr value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:OPTIcal:BTFILTEr  <string>
        - DPOJET:MEAS<x>:OPTIcal:BTFILTEr?
        ```
    """


class DpojetMeasItemOpticalBandwidth(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:OPTIcal:BANDWIDth`` command.

    Description:
        - This command sets or queries the optical to electrical converted bandwidth value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:BANDWIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:BANDWIDth?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:OPTIcal:BANDWIDth value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:OPTIcal:BANDWIDth  <NR3>
        - DPOJET:MEAS<x>:OPTIcal:BANDWIDth?
        ```
    """


class DpojetMeasItemOptical(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:OPTIcal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bandwidth``: The ``DPOJET:MEAS<x>:OPTIcal:BANDWIDth`` command.
        - ``.btfilter``: The ``DPOJET:MEAS<x>:OPTIcal:BTFILTEr`` command.
        - ``.ffetaps``: The ``DPOJET:MEAS<x>:OPTIcal:FFETAPS`` command.
        - ``.scopern``: The ``DPOJET:MEAS<x>:OPTIcal:SCOPERN`` command.
        - ``.targetber``: The ``DPOJET:MEAS<x>:OPTIcal:TARGETBer`` command.
        - ``.wfmtype``: The ``DPOJET:MEAS<x>:OPTIcal:WFMTYpe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bandwidth = DpojetMeasItemOpticalBandwidth(device, f"{self._cmd_syntax}:BANDWIDth")
        self._btfilter = DpojetMeasItemOpticalBtfilter(device, f"{self._cmd_syntax}:BTFILTEr")
        self._ffetaps = DpojetMeasItemOpticalFfetaps(device, f"{self._cmd_syntax}:FFETAPS")
        self._scopern = DpojetMeasItemOpticalScopern(device, f"{self._cmd_syntax}:SCOPERN")
        self._targetber = DpojetMeasItemOpticalTargetber(device, f"{self._cmd_syntax}:TARGETBer")
        self._wfmtype = DpojetMeasItemOpticalWfmtype(device, f"{self._cmd_syntax}:WFMTYpe")

    @property
    def bandwidth(self) -> DpojetMeasItemOpticalBandwidth:
        """Return the ``DPOJET:MEAS<x>:OPTIcal:BANDWIDth`` command.

        Description:
            - This command sets or queries the optical to electrical converted bandwidth value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:BANDWIDth?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:OPTIcal:BANDWIDth?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:OPTIcal:BANDWIDth value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:OPTIcal:BANDWIDth  <NR3>
            - DPOJET:MEAS<x>:OPTIcal:BANDWIDth?
            ```
        """
        return self._bandwidth

    @property
    def btfilter(self) -> DpojetMeasItemOpticalBtfilter:
        """Return the ``DPOJET:MEAS<x>:OPTIcal:BTFILTEr`` command.

        Description:
            - This command sets or queries current BT Filter file with absolute path.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:BTFILTEr?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:BTFILTEr?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:OPTIcal:BTFILTEr value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:OPTIcal:BTFILTEr  <string>
            - DPOJET:MEAS<x>:OPTIcal:BTFILTEr?
            ```
        """
        return self._btfilter

    @property
    def ffetaps(self) -> DpojetMeasItemOpticalFfetaps:
        """Return the ``DPOJET:MEAS<x>:OPTIcal:FFETAPS`` command.

        Description:
            - This command sets or queries current FFE tap file with absolute path.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:FFETAPS?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:FFETAPS?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:OPTIcal:FFETAPS value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:OPTIcal:FFETAPS  <string>
            - DPOJET:MEAS<x>:OPTIcal:FFETAPS?
            ```
        """
        return self._ffetaps

    @property
    def scopern(self) -> DpojetMeasItemOpticalScopern:
        """Return the ``DPOJET:MEAS<x>:OPTIcal:SCOPERN`` command.

        Description:
            - This command sets or queries the Scope RN(rms) value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:SCOPERN?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:SCOPERN?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:OPTIcal:SCOPERN value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:OPTIcal:SCOPERN  <NR3>
            - DPOJET:MEAS<x>:OPTIcal:SCOPERN?
            ```
        """
        return self._scopern

    @property
    def targetber(self) -> DpojetMeasItemOpticalTargetber:
        """Return the ``DPOJET:MEAS<x>:OPTIcal:TARGETBer`` command.

        Description:
            - This command sets or queries the Target BER value display. The 1E-Value = 10-Value

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:TARGETBer?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:OPTIcal:TARGETBer?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:OPTIcal:TARGETBer value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:OPTIcal:TARGETBer  <NR3>
            - DPOJET:MEAS<x>:OPTIcal:TARGETBer?
            ```
        """
        return self._targetber

    @property
    def wfmtype(self) -> DpojetMeasItemOpticalWfmtype:
        """Return the ``DPOJET:MEAS<x>:OPTIcal:WFMTYpe`` command.

        Description:
            - This command sets or queries the optical waveform type.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal:WFMTYpe?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal:WFMTYpe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:OPTIcal:WFMTYpe value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:OPTIcal:WFMTYpe {CONTINUOUS | MODULATED}
            - DPOJET:MEAS<x>:OPTIcal:WFMTYpe?
            ```
        """
        return self._wfmtype


class DpojetMeasItemName(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:NAME`` command.

    Description:
        - This query-only command returns the measurement name for the measurement in slot x. For
          measurements that include 16-bit characters in their UI names, such as DJDirac, the string
          returned will contain question marks where the UI contains nontext characters.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:NAME?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:NAME?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:NAME?
        ```
    """


class DpojetMeasItemN(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:N`` command.

    Description:
        - This command sets or queries the measurement N value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:N?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:N?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:N value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:N  <NR3>
        - DPOJET:MEAS<x>:N?
        ```
    """


class DpojetMeasItemMeasstart(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MEASStart`` command.

    Description:
        - This command sets or queries the measurement start value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MEASStart?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MEASStart?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:MEASStart value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MEASStart  <NR3>
        - DPOJET:MEAS<x>:MEASStart?
        ```
    """


class DpojetMeasItemMeasrangeState(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MEASRange:STATE`` command.

    Description:
        - This command turns on or off the measurement range limits.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MEASRange:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MEASRange:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:MEASRange:STATE value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MEASRange:STATE {1 | 0}
        - DPOJET:MEAS<x>:MEASRange:STATE?
        ```
    """


class DpojetMeasItemMeasrangeMin(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MEASRange:MIN`` command.

    Description:
        - This command sets or queries the minimum measurement range limit value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MEASRange:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MEASRange:MIN?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:MEASRange:MIN value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MEASRange:MIN  <NR3>
        - DPOJET:MEAS<x>:MEASRange:MIN?
        ```
    """


class DpojetMeasItemMeasrangeMax(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MEASRange:MAX`` command.

    Description:
        - This command sets or queries the maximum measurement range limit value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MEASRange:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MEASRange:MAX?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:MEASRange:MAX value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MEASRange:MAX  <NR3>
        - DPOJET:MEAS<x>:MEASRange:MAX?
        ```
    """


class DpojetMeasItemMeasrange(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MEASRange`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MEASRange?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MEASRange?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``DPOJET:MEAS<x>:MEASRange:MAX`` command.
        - ``.min``: The ``DPOJET:MEAS<x>:MEASRange:MIN`` command.
        - ``.state``: The ``DPOJET:MEAS<x>:MEASRange:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = DpojetMeasItemMeasrangeMax(device, f"{self._cmd_syntax}:MAX")
        self._min = DpojetMeasItemMeasrangeMin(device, f"{self._cmd_syntax}:MIN")
        self._state = DpojetMeasItemMeasrangeState(device, f"{self._cmd_syntax}:STATE")

    @property
    def max(self) -> DpojetMeasItemMeasrangeMax:
        """Return the ``DPOJET:MEAS<x>:MEASRange:MAX`` command.

        Description:
            - This command sets or queries the maximum measurement range limit value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MEASRange:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MEASRange:MAX?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:MEASRange:MAX value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MEASRange:MAX  <NR3>
            - DPOJET:MEAS<x>:MEASRange:MAX?
            ```
        """
        return self._max

    @property
    def min(self) -> DpojetMeasItemMeasrangeMin:
        """Return the ``DPOJET:MEAS<x>:MEASRange:MIN`` command.

        Description:
            - This command sets or queries the minimum measurement range limit value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MEASRange:MIN?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MEASRange:MIN?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:MEASRange:MIN value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MEASRange:MIN  <NR3>
            - DPOJET:MEAS<x>:MEASRange:MIN?
            ```
        """
        return self._min

    @property
    def state(self) -> DpojetMeasItemMeasrangeState:
        """Return the ``DPOJET:MEAS<x>:MEASRange:STATE`` command.

        Description:
            - This command turns on or off the measurement range limits.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MEASRange:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MEASRange:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:MEASRange:STATE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MEASRange:STATE {1 | 0}
            - DPOJET:MEAS<x>:MEASRange:STATE?
            ```
        """
        return self._state


class DpojetMeasItemMaskfile(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MASKfile`` command.

    Description:
        - This command sets or queries the current mask file name.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MASKfile?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MASKfile?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:MASKfile value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MASKfile  <string>
        - DPOJET:MEAS<x>:MASKfile?
        ```
    """


class DpojetMeasItemMaskoffsetHorizontalSelectiontype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype`` command.

    Description:
        - This command sets or queries the selection type.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype { AUTOFIT | MANUAL}
        - DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype?
        ```
    """


class DpojetMeasItemMaskoffsetHorizontalManual(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual`` command.

    Description:
        - This command sets or queries the value for Manual text box.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual  <NR3>
        - DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual?
        ```
    """


class DpojetMeasItemMaskoffsetHorizontalAutofit(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MASKOffset:HORizontal:AUTOfit`` command.

    Description:
        - This query-only command returns the value in the Autofit text box for the Mask Offset
          controls. If the mask offset method selection type is set to Autofit and an acquisition
          cycle has been completed, this field shows the displacement of the mask offset that was
          automatically determined. A positive value means that the mask has moved to the right. If
          the offset has not been determined, the returned string is TBD.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:MASKOffset:HORizontal:AUTOfit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:MASKOffset:HORizontal:AUTOfit?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MASKOffset:HORizontal:AUTOfit?
        ```
    """


class DpojetMeasItemMaskoffsetHorizontal(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MASKOffset:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MASKOffset:HORizontal?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:MASKOffset:HORizontal?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.autofit``: The ``DPOJET:MEAS<x>:MASKOffset:HORizontal:AUTOfit`` command.
        - ``.manual``: The ``DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual`` command.
        - ``.selectiontype``: The ``DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autofit = DpojetMeasItemMaskoffsetHorizontalAutofit(
            device, f"{self._cmd_syntax}:AUTOfit"
        )
        self._manual = DpojetMeasItemMaskoffsetHorizontalManual(
            device, f"{self._cmd_syntax}:MANual"
        )
        self._selectiontype = DpojetMeasItemMaskoffsetHorizontalSelectiontype(
            device, f"{self._cmd_syntax}:SELECTIONtype"
        )

    @property
    def autofit(self) -> DpojetMeasItemMaskoffsetHorizontalAutofit:
        """Return the ``DPOJET:MEAS<x>:MASKOffset:HORizontal:AUTOfit`` command.

        Description:
            - This query-only command returns the value in the Autofit text box for the Mask Offset
              controls. If the mask offset method selection type is set to Autofit and an
              acquisition cycle has been completed, this field shows the displacement of the mask
              offset that was automatically determined. A positive value means that the mask has
              moved to the right. If the offset has not been determined, the returned string is TBD.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:MASKOffset:HORizontal:AUTOfit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:MASKOffset:HORizontal:AUTOfit?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MASKOffset:HORizontal:AUTOfit?
            ```
        """
        return self._autofit

    @property
    def manual(self) -> DpojetMeasItemMaskoffsetHorizontalManual:
        """Return the ``DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual`` command.

        Description:
            - This command sets or queries the value for Manual text box.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual  <NR3>
            - DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual?
            ```
        """
        return self._manual

    @property
    def selectiontype(self) -> DpojetMeasItemMaskoffsetHorizontalSelectiontype:
        """Return the ``DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype`` command.

        Description:
            - This command sets or queries the selection type.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype { AUTOFIT | MANUAL}
            - DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype?
            ```
        """
        return self._selectiontype


class DpojetMeasItemMaskoffset(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MASKOffset`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MASKOffset?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MASKOffset?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.horizontal``: The ``DPOJET:MEAS<x>:MASKOffset:HORizontal`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = DpojetMeasItemMaskoffsetHorizontal(
            device, f"{self._cmd_syntax}:HORizontal"
        )

    @property
    def horizontal(self) -> DpojetMeasItemMaskoffsetHorizontal:
        """Return the ``DPOJET:MEAS<x>:MASKOffset:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MASKOffset:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:MASKOffset:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.autofit``: The ``DPOJET:MEAS<x>:MASKOffset:HORizontal:AUTOfit`` command.
            - ``.manual``: The ``DPOJET:MEAS<x>:MASKOffset:HORizontal:MANual`` command.
            - ``.selectiontype``: The ``DPOJET:MEAS<x>:MASKOffset:HORizontal:SELECTIONtype``
              command.
        """
        return self._horizontal


class DpojetMeasItemMarginResolution(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MARGIN:RESOlution`` command.

    Description:
        - This command sets or queries the resolution value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MARGIN:RESOlution?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MARGIN:RESOlution?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:MARGIN:RESOlution value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MARGIN:RESOlution  <NR3>
        - DPOJET:MEAS<x>:MARGIN:RESOlution?
        ```
    """


class DpojetMeasItemMarginHitratiovalue(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MARGIN:HITRATIOValue`` command.

    Description:
        - This command sets or queries the HitRatio value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MARGIN:HITRATIOValue?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MARGIN:HITRATIOValue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:MARGIN:HITRATIOValue value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MARGIN:HITRATIOValue  <NR3>
        - DPOJET:MEAS<x>:MARGIN:HITRATIOValue?
        ```
    """


class DpojetMeasItemMarginHitratiostate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MARGIN:HITRATIOState`` command.

    Description:
        - This command sets or queries the HitRatio state.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MARGIN:HITRATIOState?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MARGIN:HITRATIOState?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:MARGIN:HITRATIOState value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MARGIN:HITRATIOState {1 | 0}
        - DPOJET:MEAS<x>:MARGIN:HITRATIOState?
        ```
    """


class DpojetMeasItemMarginHitcountvalue(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MARGIN:HITCOUNTValue`` command.

    Description:
        - This command sets or queries the HitCount value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MARGIN:HITCOUNTValue?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MARGIN:HITCOUNTValue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:MARGIN:HITCOUNTValue value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:MARGIN:HITCOUNTValue  <NR3>
        - DPOJET:MEAS<x>:MARGIN:HITCOUNTValue?
        ```
    """


class DpojetMeasItemMargin(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:MARGIN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MARGIN?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MARGIN?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hitcountvalue``: The ``DPOJET:MEAS<x>:MARGIN:HITCOUNTValue`` command.
        - ``.hitratiostate``: The ``DPOJET:MEAS<x>:MARGIN:HITRATIOState`` command.
        - ``.hitratiovalue``: The ``DPOJET:MEAS<x>:MARGIN:HITRATIOValue`` command.
        - ``.resolution``: The ``DPOJET:MEAS<x>:MARGIN:RESOlution`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hitcountvalue = DpojetMeasItemMarginHitcountvalue(
            device, f"{self._cmd_syntax}:HITCOUNTValue"
        )
        self._hitratiostate = DpojetMeasItemMarginHitratiostate(
            device, f"{self._cmd_syntax}:HITRATIOState"
        )
        self._hitratiovalue = DpojetMeasItemMarginHitratiovalue(
            device, f"{self._cmd_syntax}:HITRATIOValue"
        )
        self._resolution = DpojetMeasItemMarginResolution(device, f"{self._cmd_syntax}:RESOlution")

    @property
    def hitcountvalue(self) -> DpojetMeasItemMarginHitcountvalue:
        """Return the ``DPOJET:MEAS<x>:MARGIN:HITCOUNTValue`` command.

        Description:
            - This command sets or queries the HitCount value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MARGIN:HITCOUNTValue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:MARGIN:HITCOUNTValue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:MARGIN:HITCOUNTValue value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MARGIN:HITCOUNTValue  <NR3>
            - DPOJET:MEAS<x>:MARGIN:HITCOUNTValue?
            ```
        """
        return self._hitcountvalue

    @property
    def hitratiostate(self) -> DpojetMeasItemMarginHitratiostate:
        """Return the ``DPOJET:MEAS<x>:MARGIN:HITRATIOState`` command.

        Description:
            - This command sets or queries the HitRatio state.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MARGIN:HITRATIOState?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:MARGIN:HITRATIOState?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:MARGIN:HITRATIOState value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MARGIN:HITRATIOState {1 | 0}
            - DPOJET:MEAS<x>:MARGIN:HITRATIOState?
            ```
        """
        return self._hitratiostate

    @property
    def hitratiovalue(self) -> DpojetMeasItemMarginHitratiovalue:
        """Return the ``DPOJET:MEAS<x>:MARGIN:HITRATIOValue`` command.

        Description:
            - This command sets or queries the HitRatio value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MARGIN:HITRATIOValue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:MARGIN:HITRATIOValue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:MARGIN:HITRATIOValue value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MARGIN:HITRATIOValue  <NR3>
            - DPOJET:MEAS<x>:MARGIN:HITRATIOValue?
            ```
        """
        return self._hitratiovalue

    @property
    def resolution(self) -> DpojetMeasItemMarginResolution:
        """Return the ``DPOJET:MEAS<x>:MARGIN:RESOlution`` command.

        Description:
            - This command sets or queries the resolution value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MARGIN:RESOlution?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:MARGIN:RESOlution?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:MARGIN:RESOlution value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MARGIN:RESOlution  <NR3>
            - DPOJET:MEAS<x>:MARGIN:RESOlution?
            ```
        """
        return self._resolution


class DpojetMeasItemLowrefvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:LOWREFVoltage`` command.

    Description:
        - This command sets or queries the low reference voltage value for the selected
          configuration.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOWREFVoltage?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:LOWREFVoltage?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:LOWREFVoltage value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:LOWREFVoltage  <NR3>
        - DPOJET:MEAS<x>:LOWREFVoltage?
        ```
    """


class DpojetMeasItemLoggingWorstcaseSelect(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:LOGging:WORSTcase:SELect`` command.

    Description:
        - This command sets or queries the given measurement for inclusion in any worst-case
          logging. Statistic logging is turned on or off as a whole, using the ``DPOJET:LOGging``
          branch.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOGging:WORSTcase:SELect?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:LOGging:WORSTcase:SELect?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:LOGging:WORSTcase:SELect value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:LOGging:WORSTcase:SELect {1 | 0}
        - DPOJET:MEAS<x>:LOGging:WORSTcase:SELect?
        ```
    """


class DpojetMeasItemLoggingWorstcase(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:LOGging:WORSTcase`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOGging:WORSTcase?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:LOGging:WORSTcase?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.select``: The ``DPOJET:MEAS<x>:LOGging:WORSTcase:SELect`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._select = DpojetMeasItemLoggingWorstcaseSelect(device, f"{self._cmd_syntax}:SELect")

    @property
    def select(self) -> DpojetMeasItemLoggingWorstcaseSelect:
        """Return the ``DPOJET:MEAS<x>:LOGging:WORSTcase:SELect`` command.

        Description:
            - This command sets or queries the given measurement for inclusion in any worst-case
              logging. Statistic logging is turned on or off as a whole, using the
              ``DPOJET:LOGging`` branch.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:LOGging:WORSTcase:SELect?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:LOGging:WORSTcase:SELect?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:LOGging:WORSTcase:SELect value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:LOGging:WORSTcase:SELect {1 | 0}
            - DPOJET:MEAS<x>:LOGging:WORSTcase:SELect?
            ```
        """
        return self._select


class DpojetMeasItemLoggingStatisticsSelect(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:LOGging:STATistics:SELect`` command.

    Description:
        - This command sets or queries the given measurement for inclusion in any statistic logging.
          Statistic logging is turned on or off as a whole, using the ``DPOJET:LOGging`` branch.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOGging:STATistics:SELect?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:LOGging:STATistics:SELect?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:LOGging:STATistics:SELect value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:LOGging:STATistics:SELect {1 | 0}
        - DPOJET:MEAS<x>:LOGging:STATistics:SELect?
        ```
    """


class DpojetMeasItemLoggingStatistics(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:LOGging:STATistics`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOGging:STATistics?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:LOGging:STATistics?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.select``: The ``DPOJET:MEAS<x>:LOGging:STATistics:SELect`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._select = DpojetMeasItemLoggingStatisticsSelect(device, f"{self._cmd_syntax}:SELect")

    @property
    def select(self) -> DpojetMeasItemLoggingStatisticsSelect:
        """Return the ``DPOJET:MEAS<x>:LOGging:STATistics:SELect`` command.

        Description:
            - This command sets or queries the given measurement for inclusion in any statistic
              logging. Statistic logging is turned on or off as a whole, using the
              ``DPOJET:LOGging`` branch.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:LOGging:STATistics:SELect?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:LOGging:STATistics:SELect?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:LOGging:STATistics:SELect value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:LOGging:STATistics:SELect {1 | 0}
            - DPOJET:MEAS<x>:LOGging:STATistics:SELect?
            ```
        """
        return self._select


class DpojetMeasItemLoggingMeasurementsSelect(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:LOGging:MEASurements:SELect`` command.

    Description:
        - This command sets or queries the given measurement to be included in any measurement
          logging. Statistic logging is turned on or off as a whole, using the ``DPOJET:LOGging``
          branch.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:LOGging:MEASurements:SELect?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:LOGging:MEASurements:SELect?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:LOGging:MEASurements:SELect value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:LOGging:MEASurements:SELect {1 | 0}
        - DPOJET:MEAS<x>:LOGging:MEASurements:SELect?
        ```
    """


class DpojetMeasItemLoggingMeasurementsFilename(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:LOGging:MEASurements:FILEname`` command.

    Description:
        - This command queries the current file name that will be used for the measurement when
          measurement logging is turned on.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:LOGging:MEASurements:FILEname?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:LOGging:MEASurements:FILEname?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:LOGging:MEASurements:FILEname?
        ```
    """


class DpojetMeasItemLoggingMeasurements(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:LOGging:MEASurements`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOGging:MEASurements?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:LOGging:MEASurements?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.filename``: The ``DPOJET:MEAS<x>:LOGging:MEASurements:FILEname`` command.
        - ``.select``: The ``DPOJET:MEAS<x>:LOGging:MEASurements:SELect`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._filename = DpojetMeasItemLoggingMeasurementsFilename(
            device, f"{self._cmd_syntax}:FILEname"
        )
        self._select = DpojetMeasItemLoggingMeasurementsSelect(device, f"{self._cmd_syntax}:SELect")

    @property
    def filename(self) -> DpojetMeasItemLoggingMeasurementsFilename:
        """Return the ``DPOJET:MEAS<x>:LOGging:MEASurements:FILEname`` command.

        Description:
            - This command queries the current file name that will be used for the measurement when
              measurement logging is turned on.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:LOGging:MEASurements:FILEname?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:LOGging:MEASurements:FILEname?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:LOGging:MEASurements:FILEname?
            ```
        """
        return self._filename

    @property
    def select(self) -> DpojetMeasItemLoggingMeasurementsSelect:
        """Return the ``DPOJET:MEAS<x>:LOGging:MEASurements:SELect`` command.

        Description:
            - This command sets or queries the given measurement to be included in any measurement
              logging. Statistic logging is turned on or off as a whole, using the
              ``DPOJET:LOGging`` branch.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:LOGging:MEASurements:SELect?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:LOGging:MEASurements:SELect?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:LOGging:MEASurements:SELect value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:LOGging:MEASurements:SELect {1 | 0}
            - DPOJET:MEAS<x>:LOGging:MEASurements:SELect?
            ```
        """
        return self._select


class DpojetMeasItemLogging(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:LOGging`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOGging?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:LOGging?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.measurements``: The ``DPOJET:MEAS<x>:LOGging:MEASurements`` command tree.
        - ``.statistics``: The ``DPOJET:MEAS<x>:LOGging:STATistics`` command tree.
        - ``.worstcase``: The ``DPOJET:MEAS<x>:LOGging:WORSTcase`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._measurements = DpojetMeasItemLoggingMeasurements(
            device, f"{self._cmd_syntax}:MEASurements"
        )
        self._statistics = DpojetMeasItemLoggingStatistics(device, f"{self._cmd_syntax}:STATistics")
        self._worstcase = DpojetMeasItemLoggingWorstcase(device, f"{self._cmd_syntax}:WORSTcase")

    @property
    def measurements(self) -> DpojetMeasItemLoggingMeasurements:
        """Return the ``DPOJET:MEAS<x>:LOGging:MEASurements`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOGging:MEASurements?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:LOGging:MEASurements?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.filename``: The ``DPOJET:MEAS<x>:LOGging:MEASurements:FILEname`` command.
            - ``.select``: The ``DPOJET:MEAS<x>:LOGging:MEASurements:SELect`` command.
        """
        return self._measurements

    @property
    def statistics(self) -> DpojetMeasItemLoggingStatistics:
        """Return the ``DPOJET:MEAS<x>:LOGging:STATistics`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOGging:STATistics?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:LOGging:STATistics?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.select``: The ``DPOJET:MEAS<x>:LOGging:STATistics:SELect`` command.
        """
        return self._statistics

    @property
    def worstcase(self) -> DpojetMeasItemLoggingWorstcase:
        """Return the ``DPOJET:MEAS<x>:LOGging:WORSTcase`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOGging:WORSTcase?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:LOGging:WORSTcase?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.select``: The ``DPOJET:MEAS<x>:LOGging:WORSTcase:SELect`` command.
        """
        return self._worstcase


class DpojetMeasItemHighrefvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:HIGHREFVoltage`` command.

    Description:
        - This command sets or queries the high reference voltage value for the selected
          configuration.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:HIGHREFVoltage?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:HIGHREFVoltage?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:HIGHREFVoltage value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:HIGHREFVoltage  <NR3>
        - DPOJET:MEAS<x>:HIGHREFVoltage?
        ```
    """


class DpojetMeasItemFromedge(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FROMedge`` command.

    Description:
        - This command sets the FROMedge value for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FROMedge?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FROMedge?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:FROMedge value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:FROMedge {RISe | FALL | BOTH}
        - DPOJET:MEAS<x>:FROMedge?
        ```
    """


class DpojetMeasItemFiltersSjfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FILTers:SJFRequency`` command.

    Description:
        - This command sets or queries the SJ Frequency of SJ@FREQ measurement for the application
          measurement slot with index <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:SJFRequency?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:SJFRequency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:FILTers:SJFRequency value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:FILTers:SJFRequency  <NR3>
        - DPOJET:MEAS<x>:FILTers:SJFRequency?
        ```
    """


class DpojetMeasItemFiltersSjbandwidth(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FILTers:SJBAndwidth`` command.

    Description:
        - This command sets or queries the SJ Bandwidth of SJ@FREQ measurement for the application
          measurement slot with index <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:SJBAndwidth?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:SJBAndwidth?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:FILTers:SJBAndwidth value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:FILTers:SJBAndwidth  <NR3>
        - DPOJET:MEAS<x>:FILTers:SJBAndwidth?
        ```
    """


class DpojetMeasItemFiltersRamptime(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FILTers:RAMPtime`` command.

    Description:
        - This command sets or queries the current filter ramp time.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:RAMPtime?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:RAMPtime?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:RAMPtime value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:FILTers:RAMPtime  <NR3>
        - DPOJET:MEAS<x>:FILTers:RAMPtime?
        ```
    """


class DpojetMeasItemFiltersLowpassSpec(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FILTers:LOWPass:SPEC`` command.

    Description:
        - This command sets or queries the current low pass filter specification.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:LOWPass:SPEC?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:LOWPass:SPEC?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:FILTers:LOWPass:SPEC value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:FILTers:LOWPass:SPEC {NONE | FIRST | SECOND | THIRD}
        - DPOJET:MEAS<x>:FILTers:LOWPass:SPEC?
        ```
    """


class DpojetMeasItemFiltersLowpassFreq(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FILTers:LOWPass:FREQ`` command.

    Description:
        - This command sets or queries the current low pass filter frequency.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:LOWPass:FREQ?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:LOWPass:FREQ?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:FILTers:LOWPass:FREQ value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:FILTers:LOWPass:FREQ  <NR3>
        - DPOJET:MEAS<x>:FILTers:LOWPass:FREQ?
        ```
    """


class DpojetMeasItemFiltersLowpass(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FILTers:LOWPass`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:LOWPass?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:LOWPass?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.freq``: The ``DPOJET:MEAS<x>:FILTers:LOWPass:FREQ`` command.
        - ``.spec``: The ``DPOJET:MEAS<x>:FILTers:LOWPass:SPEC`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._freq = DpojetMeasItemFiltersLowpassFreq(device, f"{self._cmd_syntax}:FREQ")
        self._spec = DpojetMeasItemFiltersLowpassSpec(device, f"{self._cmd_syntax}:SPEC")

    @property
    def freq(self) -> DpojetMeasItemFiltersLowpassFreq:
        """Return the ``DPOJET:MEAS<x>:FILTers:LOWPass:FREQ`` command.

        Description:
            - This command sets or queries the current low pass filter frequency.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:LOWPass:FREQ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:LOWPass:FREQ?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:LOWPass:FREQ value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:FILTers:LOWPass:FREQ  <NR3>
            - DPOJET:MEAS<x>:FILTers:LOWPass:FREQ?
            ```
        """
        return self._freq

    @property
    def spec(self) -> DpojetMeasItemFiltersLowpassSpec:
        """Return the ``DPOJET:MEAS<x>:FILTers:LOWPass:SPEC`` command.

        Description:
            - This command sets or queries the current low pass filter specification.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:LOWPass:SPEC?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:LOWPass:SPEC?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:LOWPass:SPEC value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:FILTers:LOWPass:SPEC {NONE | FIRST | SECOND | THIRD}
            - DPOJET:MEAS<x>:FILTers:LOWPass:SPEC?
            ```
        """
        return self._spec


class DpojetMeasItemFiltersHighpassSpec(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC`` command.

    Description:
        - This command sets or queries the current high pass filter specification.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC {NONE | FIRST | SECOND | THIRD}
        - DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC?
        ```
    """


class DpojetMeasItemFiltersHighpassFreq(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ`` command.

    Description:
        - This command sets or queries the current high pass filter frequency.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ  <NR3>
        - DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ?
        ```
    """


class DpojetMeasItemFiltersHighpass(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FILTers:HIGHPass`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:HIGHPass?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:HIGHPass?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.freq``: The ``DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ`` command.
        - ``.spec``: The ``DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._freq = DpojetMeasItemFiltersHighpassFreq(device, f"{self._cmd_syntax}:FREQ")
        self._spec = DpojetMeasItemFiltersHighpassSpec(device, f"{self._cmd_syntax}:SPEC")

    @property
    def freq(self) -> DpojetMeasItemFiltersHighpassFreq:
        """Return the ``DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ`` command.

        Description:
            - This command sets or queries the current high pass filter frequency.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ  <NR3>
            - DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ?
            ```
        """
        return self._freq

    @property
    def spec(self) -> DpojetMeasItemFiltersHighpassSpec:
        """Return the ``DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC`` command.

        Description:
            - This command sets or queries the current high pass filter specification.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC {NONE | FIRST | SECOND | THIRD}
            - DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC?
            ```
        """
        return self._spec


class DpojetMeasItemFiltersBlankingtime(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FILTers:BLANKingtime`` command.

    Description:
        - This command sets or queries the current filter blanking time.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:BLANKingtime?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:BLANKingtime?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:FILTers:BLANKingtime value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:FILTers:BLANKingtime  <NR3>
        - DPOJET:MEAS<x>:FILTers:BLANKingtime?
        ```
    """


class DpojetMeasItemFilters(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:FILTers`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.blankingtime``: The ``DPOJET:MEAS<x>:FILTers:BLANKingtime`` command.
        - ``.highpass``: The ``DPOJET:MEAS<x>:FILTers:HIGHPass`` command tree.
        - ``.lowpass``: The ``DPOJET:MEAS<x>:FILTers:LOWPass`` command tree.
        - ``.ramptime``: The ``DPOJET:MEAS<x>:FILTers:RAMPtime`` command.
        - ``.sjbandwidth``: The ``DPOJET:MEAS<x>:FILTers:SJBAndwidth`` command.
        - ``.sjfrequency``: The ``DPOJET:MEAS<x>:FILTers:SJFRequency`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._blankingtime = DpojetMeasItemFiltersBlankingtime(
            device, f"{self._cmd_syntax}:BLANKingtime"
        )
        self._highpass = DpojetMeasItemFiltersHighpass(device, f"{self._cmd_syntax}:HIGHPass")
        self._lowpass = DpojetMeasItemFiltersLowpass(device, f"{self._cmd_syntax}:LOWPass")
        self._ramptime = DpojetMeasItemFiltersRamptime(device, f"{self._cmd_syntax}:RAMPtime")
        self._sjbandwidth = DpojetMeasItemFiltersSjbandwidth(
            device, f"{self._cmd_syntax}:SJBAndwidth"
        )
        self._sjfrequency = DpojetMeasItemFiltersSjfrequency(
            device, f"{self._cmd_syntax}:SJFRequency"
        )

    @property
    def blankingtime(self) -> DpojetMeasItemFiltersBlankingtime:
        """Return the ``DPOJET:MEAS<x>:FILTers:BLANKingtime`` command.

        Description:
            - This command sets or queries the current filter blanking time.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:BLANKingtime?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:BLANKingtime?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:BLANKingtime value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:FILTers:BLANKingtime  <NR3>
            - DPOJET:MEAS<x>:FILTers:BLANKingtime?
            ```
        """
        return self._blankingtime

    @property
    def highpass(self) -> DpojetMeasItemFiltersHighpass:
        """Return the ``DPOJET:MEAS<x>:FILTers:HIGHPass`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:HIGHPass?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:HIGHPass?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.freq``: The ``DPOJET:MEAS<x>:FILTers:HIGHPass:FREQ`` command.
            - ``.spec``: The ``DPOJET:MEAS<x>:FILTers:HIGHPass:SPEC`` command.
        """
        return self._highpass

    @property
    def lowpass(self) -> DpojetMeasItemFiltersLowpass:
        """Return the ``DPOJET:MEAS<x>:FILTers:LOWPass`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:LOWPass?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:LOWPass?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.freq``: The ``DPOJET:MEAS<x>:FILTers:LOWPass:FREQ`` command.
            - ``.spec``: The ``DPOJET:MEAS<x>:FILTers:LOWPass:SPEC`` command.
        """
        return self._lowpass

    @property
    def ramptime(self) -> DpojetMeasItemFiltersRamptime:
        """Return the ``DPOJET:MEAS<x>:FILTers:RAMPtime`` command.

        Description:
            - This command sets or queries the current filter ramp time.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:RAMPtime?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers:RAMPtime?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:RAMPtime value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:FILTers:RAMPtime  <NR3>
            - DPOJET:MEAS<x>:FILTers:RAMPtime?
            ```
        """
        return self._ramptime

    @property
    def sjbandwidth(self) -> DpojetMeasItemFiltersSjbandwidth:
        """Return the ``DPOJET:MEAS<x>:FILTers:SJBAndwidth`` command.

        Description:
            - This command sets or queries the SJ Bandwidth of SJ@FREQ measurement for the
              application measurement slot with index <x>.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:SJBAndwidth?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:SJBAndwidth?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:SJBAndwidth value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:FILTers:SJBAndwidth  <NR3>
            - DPOJET:MEAS<x>:FILTers:SJBAndwidth?
            ```
        """
        return self._sjbandwidth

    @property
    def sjfrequency(self) -> DpojetMeasItemFiltersSjfrequency:
        """Return the ``DPOJET:MEAS<x>:FILTers:SJFRequency`` command.

        Description:
            - This command sets or queries the SJ Frequency of SJ@FREQ measurement for the
              application measurement slot with index <x>.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers:SJFRequency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:SJFRequency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:FILTers:SJFRequency value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:FILTers:SJFRequency  <NR3>
            - DPOJET:MEAS<x>:FILTers:SJFRequency?
            ```
        """
        return self._sjfrequency


class DpojetMeasItemEdgesVoltagestate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGES:VOLTAGEState`` command.

    Description:
        - This command sets or queries the user defined voltage state, either on or off.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:VOLTAGEState?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:VOLTAGEState?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:EDGES:VOLTAGEState value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:EDGES:VOLTAGEState {1 | 0}
        - DPOJET:MEAS<x>:EDGES:VOLTAGEState?
        ```
    """


class DpojetMeasItemEdgesUserdefinedvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGES:USERDefinedvoltage`` command.

    Description:
        - This command sets or queries the user defined voltage.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:USERDefinedvoltage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:EDGES:USERDefinedvoltage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:EDGES:USERDefinedvoltage value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:EDGES:USERDefinedvoltage  <NR3>
        - DPOJET:MEAS<x>:EDGES:USERDefinedvoltage?
        ```
    """


class DpojetMeasItemEdgesTolevel(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGES:TOLevel`` command.

    Description:
        - This command sets or queries the ToLevel edge for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:TOLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:TOLevel?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:TOLevel value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:EDGES:TOLevel {HIGH | MID | LOW}
        - DPOJET:MEAS<x>:EDGES:TOLevel?
        ```
    """


class DpojetMeasItemEdgesSubratedivisor(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGES:SUBRATEDivisor`` command.

    Description:
        - This command sets or queries the subrate divisor value for the application measurement
          slot with index <x>.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:SUBRATEDivisor?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:SUBRATEDivisor?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:EDGES:SUBRATEDivisor value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:EDGES:SUBRATEDivisor {TWO | FOUR | EIGHT}
        - DPOJET:MEAS<x>:EDGES:SUBRATEDivisor?
        ```
    """


class DpojetMeasItemEdgesSlewratetechnique(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGES:SLEWRATETechnique`` command.

    Description:
        - This command sets or queries the slew rate technique for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:SLEWRATETechnique?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:EDGES:SLEWRATETechnique?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:EDGES:SLEWRATETechnique value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:EDGES:SLEWRATETechnique {NOMinalmethod | DDRmethod}
        - DPOJET:MEAS<x>:EDGES:SLEWRATETechnique?
        ```
    """


class DpojetMeasItemEdgesLevel(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGES:LEVel`` command.

    Description:
        - This command sets or queries the level used for the edges configuration.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:LEVel?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:LEVel value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:EDGES:LEVel {HIGH | MID | LOW}
        - DPOJET:MEAS<x>:EDGES:LEVel?
        ```
    """


class DpojetMeasItemEdgesFromlevel(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGES:FROMLevel`` command.

    Description:
        - This command sets or queries the FromLevel edge for the measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:FROMLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:FROMLevel?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:FROMLevel value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:EDGES:FROMLevel {HIGH | MID | LOW}
        - DPOJET:MEAS<x>:EDGES:FROMLevel?
        ```
    """


class DpojetMeasItemEdgesEyeheightstate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGES:EYEHeightstate`` command.

    Description:
        - This command sets or queries the automated eye height state, either on or off.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:EYEHeightstate?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:EYEHeightstate?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:EDGES:EYEHeightstate value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:EDGES:EYEHeightstate {1 | 0}
        - DPOJET:MEAS<x>:EDGES:EYEHeightstate?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetMeasItemEdges(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGES`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGES?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.eyeheightstate``: The ``DPOJET:MEAS<x>:EDGES:EYEHeightstate`` command.
        - ``.fromlevel``: The ``DPOJET:MEAS<x>:EDGES:FROMLevel`` command.
        - ``.level``: The ``DPOJET:MEAS<x>:EDGES:LEVel`` command.
        - ``.slewratetechnique``: The ``DPOJET:MEAS<x>:EDGES:SLEWRATETechnique`` command.
        - ``.subratedivisor``: The ``DPOJET:MEAS<x>:EDGES:SUBRATEDivisor`` command.
        - ``.tolevel``: The ``DPOJET:MEAS<x>:EDGES:TOLevel`` command.
        - ``.userdefinedvoltage``: The ``DPOJET:MEAS<x>:EDGES:USERDefinedvoltage`` command.
        - ``.voltagestate``: The ``DPOJET:MEAS<x>:EDGES:VOLTAGEState`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._eyeheightstate = DpojetMeasItemEdgesEyeheightstate(
            device, f"{self._cmd_syntax}:EYEHeightstate"
        )
        self._fromlevel = DpojetMeasItemEdgesFromlevel(device, f"{self._cmd_syntax}:FROMLevel")
        self._level = DpojetMeasItemEdgesLevel(device, f"{self._cmd_syntax}:LEVel")
        self._slewratetechnique = DpojetMeasItemEdgesSlewratetechnique(
            device, f"{self._cmd_syntax}:SLEWRATETechnique"
        )
        self._subratedivisor = DpojetMeasItemEdgesSubratedivisor(
            device, f"{self._cmd_syntax}:SUBRATEDivisor"
        )
        self._tolevel = DpojetMeasItemEdgesTolevel(device, f"{self._cmd_syntax}:TOLevel")
        self._userdefinedvoltage = DpojetMeasItemEdgesUserdefinedvoltage(
            device, f"{self._cmd_syntax}:USERDefinedvoltage"
        )
        self._voltagestate = DpojetMeasItemEdgesVoltagestate(
            device, f"{self._cmd_syntax}:VOLTAGEState"
        )

    @property
    def eyeheightstate(self) -> DpojetMeasItemEdgesEyeheightstate:
        """Return the ``DPOJET:MEAS<x>:EDGES:EYEHeightstate`` command.

        Description:
            - This command sets or queries the automated eye height state, either on or off.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:EYEHeightstate?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:EYEHeightstate?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:EYEHeightstate value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:EDGES:EYEHeightstate {1 | 0}
            - DPOJET:MEAS<x>:EDGES:EYEHeightstate?
            ```
        """
        return self._eyeheightstate

    @property
    def fromlevel(self) -> DpojetMeasItemEdgesFromlevel:
        """Return the ``DPOJET:MEAS<x>:EDGES:FROMLevel`` command.

        Description:
            - This command sets or queries the FromLevel edge for the measurement.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:FROMLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:FROMLevel?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:FROMLevel value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:EDGES:FROMLevel {HIGH | MID | LOW}
            - DPOJET:MEAS<x>:EDGES:FROMLevel?
            ```
        """
        return self._fromlevel

    @property
    def level(self) -> DpojetMeasItemEdgesLevel:
        """Return the ``DPOJET:MEAS<x>:EDGES:LEVel`` command.

        Description:
            - This command sets or queries the level used for the edges configuration.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:LEVel?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:LEVel value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:EDGES:LEVel {HIGH | MID | LOW}
            - DPOJET:MEAS<x>:EDGES:LEVel?
            ```
        """
        return self._level

    @property
    def slewratetechnique(self) -> DpojetMeasItemEdgesSlewratetechnique:
        """Return the ``DPOJET:MEAS<x>:EDGES:SLEWRATETechnique`` command.

        Description:
            - This command sets or queries the slew rate technique for the measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:EDGES:SLEWRATETechnique?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:SLEWRATETechnique?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:SLEWRATETechnique value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:EDGES:SLEWRATETechnique {NOMinalmethod | DDRmethod}
            - DPOJET:MEAS<x>:EDGES:SLEWRATETechnique?
            ```
        """
        return self._slewratetechnique

    @property
    def subratedivisor(self) -> DpojetMeasItemEdgesSubratedivisor:
        """Return the ``DPOJET:MEAS<x>:EDGES:SUBRATEDivisor`` command.

        Description:
            - This command sets or queries the subrate divisor value for the application measurement
              slot with index <x>.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:SUBRATEDivisor?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:SUBRATEDivisor?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:SUBRATEDivisor value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:EDGES:SUBRATEDivisor {TWO | FOUR | EIGHT}
            - DPOJET:MEAS<x>:EDGES:SUBRATEDivisor?
            ```
        """
        return self._subratedivisor

    @property
    def tolevel(self) -> DpojetMeasItemEdgesTolevel:
        """Return the ``DPOJET:MEAS<x>:EDGES:TOLevel`` command.

        Description:
            - This command sets or queries the ToLevel edge for the measurement.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:TOLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGES:TOLevel?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:TOLevel value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:EDGES:TOLevel {HIGH | MID | LOW}
            - DPOJET:MEAS<x>:EDGES:TOLevel?
            ```
        """
        return self._tolevel

    @property
    def userdefinedvoltage(self) -> DpojetMeasItemEdgesUserdefinedvoltage:
        """Return the ``DPOJET:MEAS<x>:EDGES:USERDefinedvoltage`` command.

        Description:
            - This command sets or queries the user defined voltage.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:EDGES:USERDefinedvoltage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:USERDefinedvoltage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:USERDefinedvoltage value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:EDGES:USERDefinedvoltage  <NR3>
            - DPOJET:MEAS<x>:EDGES:USERDefinedvoltage?
            ```
        """
        return self._userdefinedvoltage

    @property
    def voltagestate(self) -> DpojetMeasItemEdgesVoltagestate:
        """Return the ``DPOJET:MEAS<x>:EDGES:VOLTAGEState`` command.

        Description:
            - This command sets or queries the user defined voltage state, either on or off.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES:VOLTAGEState?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:VOLTAGEState?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:EDGES:VOLTAGEState value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:EDGES:VOLTAGEState {1 | 0}
            - DPOJET:MEAS<x>:EDGES:VOLTAGEState?
            ```
        """
        return self._voltagestate


class DpojetMeasItemEdgeincre(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGEIncre`` command.

    Description:
        - This command sets or queries the measurement edge increment value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGEIncre?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGEIncre?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:EDGEIncre value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:EDGEIncre  <NR3>
        - DPOJET:MEAS<x>:EDGEIncre?
        ```
    """


class DpojetMeasItemEdge2(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGE2`` command.

    Description:
        - This command sets or queries the Source2 edge type.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGE2?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGE2?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:EDGE2 value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:EDGE2 {RISe | FALL | BOTH}
        - DPOJET:MEAS<x>:EDGE2?
        ```
    """


class DpojetMeasItemEdge1(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:EDGE1`` command.

    Description:
        - This command sets or queries the Source1 edge type.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGE1?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGE1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:EDGE1 value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:EDGE1 {RISe | FALL | BOTH}
        - DPOJET:MEAS<x>:EDGE1?
        ```
    """


class DpojetMeasItemDisplayname(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DISPLAYNAME`` command.

    Description:
        - This command queries the UI name of the measurement x in the measurement table.If the
          measurement UI name has special character δ, then it is displayed as d.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DISPLAYNAME?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DISPLAYNAME?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DISPLAYNAME?
        ```
    """


class DpojetMeasItemDfeTapvalue(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DFE:TAPValue`` command.

    Description:
        - This command sets or queries the tap value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:TAPValue?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DFE:TAPValue?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:DFE:TAPValue value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DFE:TAPValue  <NR3>
        - DPOJET:MEAS<x>:DFE:TAPValue?
        ```
    """


class DpojetMeasItemDfeTapstate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DFE:TAPState`` command.

    Description:
        - This command sets or queries the tap value state, either on or off.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:TAPState?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DFE:TAPState?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:DFE:TAPState value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DFE:TAPState {0|1}
        - DPOJET:MEAS<x>:DFE:TAPState?
        ```
    """


class DpojetMeasItemDfeResolution(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DFE:RESOlution`` command.

    Description:
        - This command sets or queries the resolution.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:RESOlution?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DFE:RESOlution?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:DFE:RESOlution value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DFE:RESOlution  <NR3>
        - DPOJET:MEAS<x>:DFE:RESOlution?
        ```
    """


class DpojetMeasItemDfeMeasatpercent(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DFE:MEASatpercent`` command.

    Description:
        - This command sets or queries the measure at X% value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:MEASatpercent?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DFE:MEASatpercent?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:DFE:MEASatpercent value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DFE:MEASatpercent  <NR3>
        - DPOJET:MEAS<x>:DFE:MEASatpercent?
        ```
    """


class DpojetMeasItemDfeManualdelay(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DFE:MANUALDELAY`` command.

    Description:
        - This command sets or queries the manual delay value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:MANUALDELAY?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DFE:MANUALDELAY?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:DFE:MANUALDELAY value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DFE:MANUALDELAY  <NR3>
        - DPOJET:MEAS<x>:DFE:MANUALDELAY?
        ```
    """


class DpojetMeasItemDfeDelaycompensation(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION`` command.

    Description:
        - This command sets or queries the DFE delay compensation.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION {MANUAL,AUTO}
        - DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION?
        ```
    """


class DpojetMeasItemDfeAbsolutevoltagevalue(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue`` command.

    Description:
        - This command sets or queries DFE absolute voltage value for ``DFE_EyeWidth`` measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue  <NR3>
        - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue?
        ```
    """


class DpojetMeasItemDfeAbsolutevoltagestate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState`` command.

    Description:
        - This command sets or queries DFE absolute voltage state for ``DFE_EyeWidth`` measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState {0 | 1 | ON | OFF}
        - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState?
        ```
    """


class DpojetMeasItemDfeAbsolutetimevalue(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue`` command.

    Description:
        - This command sets or queries DFE absolute time value for ``DFE_EyeHeight`` measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue  <NR3>
        - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue?
        ```
    """


class DpojetMeasItemDfeAbsolutetimestate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState`` command.

    Description:
        - This command sets or queries DFE absolute time state for ``DFE_EyeHeight`` measurement.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState {0 | 1 | ON | OFF}
        - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetMeasItemDfe(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DFE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DFE?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absolutetimestate``: The ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState`` command.
        - ``.absolutetimevalue``: The ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue`` command.
        - ``.absolutevoltagestate``: The ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState`` command.
        - ``.absolutevoltagevalue``: The ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue`` command.
        - ``.delaycompensation``: The ``DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION`` command.
        - ``.manualdelay``: The ``DPOJET:MEAS<x>:DFE:MANUALDELAY`` command.
        - ``.measatpercent``: The ``DPOJET:MEAS<x>:DFE:MEASatpercent`` command.
        - ``.resolution``: The ``DPOJET:MEAS<x>:DFE:RESOlution`` command.
        - ``.tapstate``: The ``DPOJET:MEAS<x>:DFE:TAPState`` command.
        - ``.tapvalue``: The ``DPOJET:MEAS<x>:DFE:TAPValue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolutetimestate = DpojetMeasItemDfeAbsolutetimestate(
            device, f"{self._cmd_syntax}:ABSOLUTETIMEState"
        )
        self._absolutetimevalue = DpojetMeasItemDfeAbsolutetimevalue(
            device, f"{self._cmd_syntax}:ABSOLUTETIMEValue"
        )
        self._absolutevoltagestate = DpojetMeasItemDfeAbsolutevoltagestate(
            device, f"{self._cmd_syntax}:ABSOLUTEVOLTAGEState"
        )
        self._absolutevoltagevalue = DpojetMeasItemDfeAbsolutevoltagevalue(
            device, f"{self._cmd_syntax}:ABSOLUTEVOLTAGEValue"
        )
        self._delaycompensation = DpojetMeasItemDfeDelaycompensation(
            device, f"{self._cmd_syntax}:DELAYCOMPENSATION"
        )
        self._manualdelay = DpojetMeasItemDfeManualdelay(device, f"{self._cmd_syntax}:MANUALDELAY")
        self._measatpercent = DpojetMeasItemDfeMeasatpercent(
            device, f"{self._cmd_syntax}:MEASatpercent"
        )
        self._resolution = DpojetMeasItemDfeResolution(device, f"{self._cmd_syntax}:RESOlution")
        self._tapstate = DpojetMeasItemDfeTapstate(device, f"{self._cmd_syntax}:TAPState")
        self._tapvalue = DpojetMeasItemDfeTapvalue(device, f"{self._cmd_syntax}:TAPValue")

    @property
    def absolutetimestate(self) -> DpojetMeasItemDfeAbsolutetimestate:
        """Return the ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState`` command.

        Description:
            - This command sets or queries DFE absolute time state for ``DFE_EyeHeight``
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState {0 | 1 | ON | OFF}
            - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState?
            ```
        """
        return self._absolutetimestate

    @property
    def absolutetimevalue(self) -> DpojetMeasItemDfeAbsolutetimevalue:
        """Return the ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue`` command.

        Description:
            - This command sets or queries DFE absolute time value for ``DFE_EyeHeight``
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue  <NR3>
            - DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue?
            ```
        """
        return self._absolutetimevalue

    @property
    def absolutevoltagestate(self) -> DpojetMeasItemDfeAbsolutevoltagestate:
        """Return the ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState`` command.

        Description:
            - This command sets or queries DFE absolute voltage state for ``DFE_EyeWidth``
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState {0 | 1 | ON | OFF}
            - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState?
            ```
        """
        return self._absolutevoltagestate

    @property
    def absolutevoltagevalue(self) -> DpojetMeasItemDfeAbsolutevoltagevalue:
        """Return the ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue`` command.

        Description:
            - This command sets or queries DFE absolute voltage value for ``DFE_EyeWidth``
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue  <NR3>
            - DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue?
            ```
        """
        return self._absolutevoltagevalue

    @property
    def delaycompensation(self) -> DpojetMeasItemDfeDelaycompensation:
        """Return the ``DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION`` command.

        Description:
            - This command sets or queries the DFE delay compensation.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION {MANUAL,AUTO}
            - DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION?
            ```
        """
        return self._delaycompensation

    @property
    def manualdelay(self) -> DpojetMeasItemDfeManualdelay:
        """Return the ``DPOJET:MEAS<x>:DFE:MANUALDELAY`` command.

        Description:
            - This command sets or queries the manual delay value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:MANUALDELAY?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DFE:MANUALDELAY?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:MANUALDELAY value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DFE:MANUALDELAY  <NR3>
            - DPOJET:MEAS<x>:DFE:MANUALDELAY?
            ```
        """
        return self._manualdelay

    @property
    def measatpercent(self) -> DpojetMeasItemDfeMeasatpercent:
        """Return the ``DPOJET:MEAS<x>:DFE:MEASatpercent`` command.

        Description:
            - This command sets or queries the measure at X% value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:MEASatpercent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:MEASatpercent?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:MEASatpercent value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DFE:MEASatpercent  <NR3>
            - DPOJET:MEAS<x>:DFE:MEASatpercent?
            ```
        """
        return self._measatpercent

    @property
    def resolution(self) -> DpojetMeasItemDfeResolution:
        """Return the ``DPOJET:MEAS<x>:DFE:RESOlution`` command.

        Description:
            - This command sets or queries the resolution.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:RESOlution?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DFE:RESOlution?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:DFE:RESOlution value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DFE:RESOlution  <NR3>
            - DPOJET:MEAS<x>:DFE:RESOlution?
            ```
        """
        return self._resolution

    @property
    def tapstate(self) -> DpojetMeasItemDfeTapstate:
        """Return the ``DPOJET:MEAS<x>:DFE:TAPState`` command.

        Description:
            - This command sets or queries the tap value state, either on or off.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:TAPState?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DFE:TAPState?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:DFE:TAPState value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DFE:TAPState {0|1}
            - DPOJET:MEAS<x>:DFE:TAPState?
            ```
        """
        return self._tapstate

    @property
    def tapvalue(self) -> DpojetMeasItemDfeTapvalue:
        """Return the ``DPOJET:MEAS<x>:DFE:TAPValue`` command.

        Description:
            - This command sets or queries the tap value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE:TAPValue?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DFE:TAPValue?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:DFE:TAPValue value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DFE:TAPValue  <NR3>
            - DPOJET:MEAS<x>:DFE:TAPValue?
            ```
        """
        return self._tapvalue


class DpojetMeasItemData(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:DATA`` command.

    Description:
        - This query-only command returns the measurement data. This is similar to the curve query,
          where the output is in the format #<x><yyy><data><newline>, where <x> is the number of <y>
          bytes.For Example: If <yyy>=500, <x>=3<yyy> is the number of bytes to transfer.<data> is
          curve data.<newline> is a single-byte new line character at the end of the data.<x> is
          hexadecimal format. The letters A-F denote the number of y bytes between 10 and 15 digits.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DATA?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:DATA?
        ```
    """


class DpojetMeasItemCustomname(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CUSTomname`` command.

    Description:
        - This command sets or queries the custom measurement name for the measurement in slot x.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CUSTomname?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:CUSTomname?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:CUSTomname value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CUSTomname  <string>
        - DPOJET:MEAS<x>:CUSTomname?
        ```
    """


class DpojetMeasItemCustomgatingToedge(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CUSTOMGATING:TOedge`` command.

    Description:
        - This commands sets or queries the edge type for source2.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CUSTOMGATING:TOedge?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:CUSTOMGATING:TOedge?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CUSTOMGATING:TOedge value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CUSTOMGATING:TOedge {RISe | FALL | BOTH}
        - DPOJET:MEAS<x>:CUSTOMGATING:TOedge?
        ```
    """


class DpojetMeasItemCustomgatingSource2gate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE`` command.

    Description:
        - This commands sets or queries the gate associated with source2.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE {GATE1 | GATE2 | GATE3 GATE4 | GATE5 | GATE6 | GATE7 | GATE8 | GATE9 | GATE10 | GATE11 | GATE12 | GATE13 | GATE14 | GATE15 | GATE16 | NONE }
        - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE?
        ```
    """  # noqa: E501


class DpojetMeasItemCustomgatingSource1gate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE`` command.

    Description:
        - This commands sets or queries the gate associated with source1.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE {GATE1 | GATE2 | GATE3 GATE4 | GATE5 | GATE6 | GATE7 | GATE8 | GATE9 | GATE10 | GATE11 | GATE12 | GATE13 | GATE14 | GATE15 | GATE16 | NONE}
        - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE?
        ```
    """  # noqa: E501


class DpojetMeasItemCustomgatingMeasurementedge(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge`` command.

    Description:
        - This command sets or queries the current measurement edge.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge {FIRST | ALL}
        - DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge?
        ```
    """


class DpojetMeasItemCustomgatingFromedge(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CUSTOMGATING:FROMedge`` command.

    Description:
        - This commands sets or queries the edge type for source1.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CUSTOMGATING:FROMedge?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CUSTOMGATING:FROMedge?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CUSTOMGATING:FROMedge value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CUSTOMGATING:FROMedge {RISe | FALL | BOTH}
        - DPOJET:MEAS<x>:CUSTOMGATING:FROMedge?
        ```
    """


class DpojetMeasItemCustomgating(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CUSTOMGATING`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CUSTOMGATING?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:CUSTOMGATING?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fromedge``: The ``DPOJET:MEAS<x>:CUSTOMGATING:FROMedge`` command.
        - ``.measurementedge``: The ``DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge`` command.
        - ``.source1gate``: The ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE`` command.
        - ``.source2gate``: The ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE`` command.
        - ``.toedge``: The ``DPOJET:MEAS<x>:CUSTOMGATING:TOedge`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fromedge = DpojetMeasItemCustomgatingFromedge(device, f"{self._cmd_syntax}:FROMedge")
        self._measurementedge = DpojetMeasItemCustomgatingMeasurementedge(
            device, f"{self._cmd_syntax}:MEASUREMENTEdge"
        )
        self._source1gate = DpojetMeasItemCustomgatingSource1gate(
            device, f"{self._cmd_syntax}:SOURCE1GATE"
        )
        self._source2gate = DpojetMeasItemCustomgatingSource2gate(
            device, f"{self._cmd_syntax}:SOURCE2GATE"
        )
        self._toedge = DpojetMeasItemCustomgatingToedge(device, f"{self._cmd_syntax}:TOedge")

    @property
    def fromedge(self) -> DpojetMeasItemCustomgatingFromedge:
        """Return the ``DPOJET:MEAS<x>:CUSTOMGATING:FROMedge`` command.

        Description:
            - This commands sets or queries the edge type for source1.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CUSTOMGATING:FROMedge?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:FROMedge?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:FROMedge value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CUSTOMGATING:FROMedge {RISe | FALL | BOTH}
            - DPOJET:MEAS<x>:CUSTOMGATING:FROMedge?
            ```
        """
        return self._fromedge

    @property
    def measurementedge(self) -> DpojetMeasItemCustomgatingMeasurementedge:
        """Return the ``DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge`` command.

        Description:
            - This command sets or queries the current measurement edge.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge {FIRST | ALL}
            - DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge?
            ```
        """
        return self._measurementedge

    @property
    def source1gate(self) -> DpojetMeasItemCustomgatingSource1gate:
        """Return the ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE`` command.

        Description:
            - This commands sets or queries the gate associated with source1.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE {GATE1 | GATE2 | GATE3 GATE4 | GATE5 | GATE6 | GATE7 | GATE8 | GATE9 | GATE10 | GATE11 | GATE12 | GATE13 | GATE14 | GATE15 | GATE16 | NONE}
            - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE?
            ```
        """  # noqa: E501
        return self._source1gate

    @property
    def source2gate(self) -> DpojetMeasItemCustomgatingSource2gate:
        """Return the ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE`` command.

        Description:
            - This commands sets or queries the gate associated with source2.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE {GATE1 | GATE2 | GATE3 GATE4 | GATE5 | GATE6 | GATE7 | GATE8 | GATE9 | GATE10 | GATE11 | GATE12 | GATE13 | GATE14 | GATE15 | GATE16 | NONE }
            - DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE?
            ```
        """  # noqa: E501
        return self._source2gate

    @property
    def toedge(self) -> DpojetMeasItemCustomgatingToedge:
        """Return the ``DPOJET:MEAS<x>:CUSTOMGATING:TOedge`` command.

        Description:
            - This commands sets or queries the edge type for source2.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CUSTOMGATING:TOedge?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:TOedge?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CUSTOMGATING:TOedge value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CUSTOMGATING:TOedge {RISe | FALL | BOTH}
            - DPOJET:MEAS<x>:CUSTOMGATING:TOedge?
            ```
        """
        return self._toedge


class DpojetMeasItemCommonmodeFiltersState(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:COMMONMode:FILTers:STATE`` command.

    Description:
        - This command sets or queries the state of the common mode filter frequency.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:COMMONMode:FILTers:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:COMMONMode:FILTers:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:COMMONMode:FILTers:STATE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:COMMONMode:FILTers:STATE {ON | OFF}
        - DPOJET:MEAS<x>:COMMONMode:FILTers:STATE?
        ```
    """


class DpojetMeasItemCommonmodeFilters(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:COMMONMode:FILTers`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:COMMONMode:FILTers?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:COMMONMode:FILTers?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DPOJET:MEAS<x>:COMMONMode:FILTers:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DpojetMeasItemCommonmodeFiltersState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> DpojetMeasItemCommonmodeFiltersState:
        """Return the ``DPOJET:MEAS<x>:COMMONMode:FILTers:STATE`` command.

        Description:
            - This command sets or queries the state of the common mode filter frequency.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:COMMONMode:FILTers:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:COMMONMode:FILTers:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:COMMONMode:FILTers:STATE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:COMMONMode:FILTers:STATE {ON | OFF}
            - DPOJET:MEAS<x>:COMMONMode:FILTers:STATE?
            ```
        """
        return self._state


class DpojetMeasItemCommonmode(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:COMMONMode`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:COMMONMode?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:COMMONMode?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.filters``: The ``DPOJET:MEAS<x>:COMMONMode:FILTers`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._filters = DpojetMeasItemCommonmodeFilters(device, f"{self._cmd_syntax}:FILTers")

    @property
    def filters(self) -> DpojetMeasItemCommonmodeFilters:
        """Return the ``DPOJET:MEAS<x>:COMMONMode:FILTers`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:COMMONMode:FILTers?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:COMMONMode:FILTers?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DPOJET:MEAS<x>:COMMONMode:FILTers:STATE`` command.
        """
        return self._filters


class DpojetMeasItemClockrecoveryStandard(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:STAndard`` command.

    Description:
        - This command sets or queries the current clock recovery standard, as specified in the user
          interface.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:STAndard?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:STAndard?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:STAndard value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:STAndard  <string>
        - DPOJET:MEAS<x>:CLOCKRecovery:STAndard?
        ```
    """


class DpojetMeasItemClockrecoveryPattern(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:PATTern`` command.

    Description:
        - This command turns on or off the usage of CLOCKPath to a specific known data pattern.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:PATTern?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:PATTern?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:PATTern value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:PATTern {1 | 0}
        - DPOJET:MEAS<x>:CLOCKRecovery:PATTern?
        ```
    """


class DpojetMeasItemClockrecoveryNominaloffsetSelectiontype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype`` command.

    Description:
        - This command sets or queries the selection type.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype {AUTO | MANUAL}
        - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype?
        ```
    """


class DpojetMeasItemClockrecoveryNominaloffsetRecalctype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype`` command.

    Description:
        - This command sets or queries the recalculation list box.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype {FIRST | EVERY}
        - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype?
        ```
    """


class DpojetMeasItemClockrecoveryNominaloffsetManual(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual`` command.

    Description:
        - This command sets or queries the value for Manual text box.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual  <NR3>
        - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual?
        ```
    """


class DpojetMeasItemClockrecoveryNominaloffsetAuto(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:AUTO`` command.

    Description:
        - This query-only command returns the value in the Auto text box for the Nominal Clock
          Offset controls. If the nominal clock offset method selection type is set to Auto and an
          acquisition cycle has been completed, this field shows the clock-to-data offset that was
          automatically determined. A positive value means that the clock leads the data (precedes
          it in time). If the offset has not been determined, the returned string is TBD.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:AUTO?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:AUTO?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:AUTO?
        ```
    """


class DpojetMeasItemClockrecoveryNominaloffset(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset`` command.

    Description:
        - This command sets or queries the clock offset.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset  <NR3>
        - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset?
        ```

    Properties:
        - ``.auto``: The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:AUTO`` command.
        - ``.manual``: The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual`` command.
        - ``.recalctype``: The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype`` command.
        - ``.selectiontype``: The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype``
          command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._auto = DpojetMeasItemClockrecoveryNominaloffsetAuto(
            device, f"{self._cmd_syntax}:AUTO"
        )
        self._manual = DpojetMeasItemClockrecoveryNominaloffsetManual(
            device, f"{self._cmd_syntax}:MANual"
        )
        self._recalctype = DpojetMeasItemClockrecoveryNominaloffsetRecalctype(
            device, f"{self._cmd_syntax}:Recalctype"
        )
        self._selectiontype = DpojetMeasItemClockrecoveryNominaloffsetSelectiontype(
            device, f"{self._cmd_syntax}:SELECTIONtype"
        )

    @property
    def auto(self) -> DpojetMeasItemClockrecoveryNominaloffsetAuto:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:AUTO`` command.

        Description:
            - This query-only command returns the value in the Auto text box for the Nominal Clock
              Offset controls. If the nominal clock offset method selection type is set to Auto and
              an acquisition cycle has been completed, this field shows the clock-to-data offset
              that was automatically determined. A positive value means that the clock leads the
              data (precedes it in time). If the offset has not been determined, the returned string
              is TBD.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:AUTO?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:AUTO?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:AUTO?
            ```
        """
        return self._auto

    @property
    def manual(self) -> DpojetMeasItemClockrecoveryNominaloffsetManual:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual`` command.

        Description:
            - This command sets or queries the value for Manual text box.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual  <NR3>
            - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual?
            ```
        """
        return self._manual

    @property
    def recalctype(self) -> DpojetMeasItemClockrecoveryNominaloffsetRecalctype:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype`` command.

        Description:
            - This command sets or queries the recalculation list box.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype {FIRST | EVERY}
            - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype?
            ```
        """
        return self._recalctype

    @property
    def selectiontype(self) -> DpojetMeasItemClockrecoveryNominaloffsetSelectiontype:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype`` command.

        Description:
            - This command sets or queries the selection type.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype {AUTO | MANUAL}
            - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype?
            ```
        """
        return self._selectiontype


class DpojetMeasItemClockrecoveryModel(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:MODel`` command.

    Description:
        - This command sets or queries the current clock recovery model.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:MODel?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:MODel?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:MODel value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:MODel {ONE | TWO}
        - DPOJET:MEAS<x>:CLOCKRecovery:MODel?
        ```
    """


class DpojetMeasItemClockrecoveryMethod(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:METHod`` command.

    Description:
        - This command sets or queries the current Clock recovery method.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:METHod?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:METHod?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:METHod value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:METHod {STANDARD | CUSTOM | CONSTMEAN | CONSTFIXED | EXPEDGE | EXPPLL | CONSTMEDIAN | BEHAVIORAL}
        - DPOJET:MEAS<x>:CLOCKRecovery:METHod?
        ```
    """  # noqa: E501


class DpojetMeasItemClockrecoveryMeanautocalculate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate`` command.

    Description:
        - This command sets or queries how often the clock is calculated, either FIRST, or on EVERY
          acquisition.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate {FIRST | EVERY}
        - DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate?
        ```
    """


class DpojetMeasItemClockrecoveryLoopbandwidth(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth`` command.

    Description:
        - This command sets or queries the clock recovery loop bandwidth.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth  <NR3>
        - DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth?
        ```
    """


class DpojetMeasItemClockrecoveryDatarate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:DATARate`` command.

    Description:
        - This command turns on or off DATArate usage.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:DATARate?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:DATARate?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:DATARate value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:DATARate {1 | 0}
        - DPOJET:MEAS<x>:CLOCKRecovery:DATARate?
        ```
    """


class DpojetMeasItemClockrecoveryDamping(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:DAMPing`` command.

    Description:
        - This command sets or queries the clock recovery damping value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:DAMPing?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:DAMPing?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:DAMPing value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:DAMPing  <NR3>
        - DPOJET:MEAS<x>:CLOCKRecovery:DAMPing?
        ```
    """


class DpojetMeasItemClockrecoveryClockpath(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath`` command.

    Description:
        - This command sets or queries the current known clock pattern path.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath  <string>
        - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath?
        ```
    """


class DpojetMeasItemClockrecoveryClockmultiplier(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier`` command.

    Description:
        - This command sets or queries the clock multiplier.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier  <NR3>
        - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier?
        ```
    """


class DpojetMeasItemClockrecoveryClockfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency`` command.

    Description:
        - This command sets or queries the clock frequency. Used with Constant Clock - Fixed clock
          recovery method.

    Usage:
        - Using the ``.query()`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency  <NR3>
        - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency?
        ```
    """


class DpojetMeasItemClockrecoveryClockbitrate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate`` command.

    Description:
        - This command sets or queries the clock bit rate. Used if DATARate is 1.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate  <NR3>
        - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate?
        ```
    """


class DpojetMeasItemClockrecoveryBwtype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:BWType`` command.

    Description:
        - This command sets or queries the clock recovery bandwidth type.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:BWType?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:BWType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:BWType value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:BWType {LOOPBW | JTFBW}
        - DPOJET:MEAS<x>:CLOCKRecovery:BWType?
        ```
    """


class DpojetMeasItemClockrecoveryBhvrstandard(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard`` command.

    Description:
        - This command sets or queries the current behavioral standard, as specified in the user
          interface.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard  <string>
        - DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetMeasItemClockrecovery(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:CLOCKRecovery`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bhvrstandard``: The ``DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard`` command.
        - ``.bwtype``: The ``DPOJET:MEAS<x>:CLOCKRecovery:BWType`` command.
        - ``.clockbitrate``: The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate`` command.
        - ``.clockfrequency``: The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency`` command.
        - ``.clockmultiplier``: The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier`` command.
        - ``.clockpath``: The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath`` command.
        - ``.damping``: The ``DPOJET:MEAS<x>:CLOCKRecovery:DAMPing`` command.
        - ``.datarate``: The ``DPOJET:MEAS<x>:CLOCKRecovery:DATARate`` command.
        - ``.loopbandwidth``: The ``DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth`` command.
        - ``.meanautocalculate``: The ``DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate`` command.
        - ``.method``: The ``DPOJET:MEAS<x>:CLOCKRecovery:METHod`` command.
        - ``.model``: The ``DPOJET:MEAS<x>:CLOCKRecovery:MODel`` command.
        - ``.nominaloffset``: The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset`` command.
        - ``.pattern``: The ``DPOJET:MEAS<x>:CLOCKRecovery:PATTern`` command.
        - ``.standard``: The ``DPOJET:MEAS<x>:CLOCKRecovery:STAndard`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bhvrstandard = DpojetMeasItemClockrecoveryBhvrstandard(
            device, f"{self._cmd_syntax}:BHVRSTANdard"
        )
        self._bwtype = DpojetMeasItemClockrecoveryBwtype(device, f"{self._cmd_syntax}:BWType")
        self._clockbitrate = DpojetMeasItemClockrecoveryClockbitrate(
            device, f"{self._cmd_syntax}:CLOCKBitrate"
        )
        self._clockfrequency = DpojetMeasItemClockrecoveryClockfrequency(
            device, f"{self._cmd_syntax}:CLOCKFrequency"
        )
        self._clockmultiplier = DpojetMeasItemClockrecoveryClockmultiplier(
            device, f"{self._cmd_syntax}:CLOCKMultiplier"
        )
        self._clockpath = DpojetMeasItemClockrecoveryClockpath(
            device, f"{self._cmd_syntax}:CLOCKPath"
        )
        self._damping = DpojetMeasItemClockrecoveryDamping(device, f"{self._cmd_syntax}:DAMPing")
        self._datarate = DpojetMeasItemClockrecoveryDatarate(device, f"{self._cmd_syntax}:DATARate")
        self._loopbandwidth = DpojetMeasItemClockrecoveryLoopbandwidth(
            device, f"{self._cmd_syntax}:LOOPBandwidth"
        )
        self._meanautocalculate = DpojetMeasItemClockrecoveryMeanautocalculate(
            device, f"{self._cmd_syntax}:MEANAUTOCalculate"
        )
        self._method = DpojetMeasItemClockrecoveryMethod(device, f"{self._cmd_syntax}:METHod")
        self._model = DpojetMeasItemClockrecoveryModel(device, f"{self._cmd_syntax}:MODel")
        self._nominaloffset = DpojetMeasItemClockrecoveryNominaloffset(
            device, f"{self._cmd_syntax}:NOMINALOFFset"
        )
        self._pattern = DpojetMeasItemClockrecoveryPattern(device, f"{self._cmd_syntax}:PATTern")
        self._standard = DpojetMeasItemClockrecoveryStandard(device, f"{self._cmd_syntax}:STAndard")

    @property
    def bhvrstandard(self) -> DpojetMeasItemClockrecoveryBhvrstandard:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard`` command.

        Description:
            - This command sets or queries the current behavioral standard, as specified in the user
              interface.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard  <string>
            - DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard?
            ```
        """
        return self._bhvrstandard

    @property
    def bwtype(self) -> DpojetMeasItemClockrecoveryBwtype:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:BWType`` command.

        Description:
            - This command sets or queries the clock recovery bandwidth type.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:BWType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:BWType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:BWType value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:BWType {LOOPBW | JTFBW}
            - DPOJET:MEAS<x>:CLOCKRecovery:BWType?
            ```
        """
        return self._bwtype

    @property
    def clockbitrate(self) -> DpojetMeasItemClockrecoveryClockbitrate:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate`` command.

        Description:
            - This command sets or queries the clock bit rate. Used if DATARate is 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate  <NR3>
            - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate?
            ```
        """
        return self._clockbitrate

    @property
    def clockfrequency(self) -> DpojetMeasItemClockrecoveryClockfrequency:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency`` command.

        Description:
            - This command sets or queries the clock frequency. Used with Constant Clock - Fixed
              clock recovery method.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency  <NR3>
            - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency?
            ```
        """
        return self._clockfrequency

    @property
    def clockmultiplier(self) -> DpojetMeasItemClockrecoveryClockmultiplier:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier`` command.

        Description:
            - This command sets or queries the clock multiplier.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier  <NR3>
            - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier?
            ```
        """
        return self._clockmultiplier

    @property
    def clockpath(self) -> DpojetMeasItemClockrecoveryClockpath:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath`` command.

        Description:
            - This command sets or queries the current known clock pattern path.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath  <string>
            - DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath?
            ```
        """
        return self._clockpath

    @property
    def damping(self) -> DpojetMeasItemClockrecoveryDamping:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:DAMPing`` command.

        Description:
            - This command sets or queries the clock recovery damping value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:DAMPing?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:DAMPing?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:DAMPing value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:DAMPing  <NR3>
            - DPOJET:MEAS<x>:CLOCKRecovery:DAMPing?
            ```
        """
        return self._damping

    @property
    def datarate(self) -> DpojetMeasItemClockrecoveryDatarate:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:DATARate`` command.

        Description:
            - This command turns on or off DATArate usage.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:DATARate?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:DATARate?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:DATARate value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:DATARate {1 | 0}
            - DPOJET:MEAS<x>:CLOCKRecovery:DATARate?
            ```
        """
        return self._datarate

    @property
    def loopbandwidth(self) -> DpojetMeasItemClockrecoveryLoopbandwidth:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth`` command.

        Description:
            - This command sets or queries the clock recovery loop bandwidth.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth  <NR3>
            - DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth?
            ```
        """
        return self._loopbandwidth

    @property
    def meanautocalculate(self) -> DpojetMeasItemClockrecoveryMeanautocalculate:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate`` command.

        Description:
            - This command sets or queries how often the clock is calculated, either FIRST, or on
              EVERY acquisition.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate {FIRST | EVERY}
            - DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate?
            ```
        """
        return self._meanautocalculate

    @property
    def method(self) -> DpojetMeasItemClockrecoveryMethod:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:METHod`` command.

        Description:
            - This command sets or queries the current Clock recovery method.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:METHod?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:METHod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:METHod value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:METHod {STANDARD | CUSTOM | CONSTMEAN | CONSTFIXED | EXPEDGE | EXPPLL | CONSTMEDIAN | BEHAVIORAL}
            - DPOJET:MEAS<x>:CLOCKRecovery:METHod?
            ```
        """  # noqa: E501
        return self._method

    @property
    def model(self) -> DpojetMeasItemClockrecoveryModel:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:MODel`` command.

        Description:
            - This command sets or queries the current clock recovery model.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:MODel?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:MODel?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:MODel value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:MODel {ONE | TWO}
            - DPOJET:MEAS<x>:CLOCKRecovery:MODel?
            ```
        """
        return self._model

    @property
    def nominaloffset(self) -> DpojetMeasItemClockrecoveryNominaloffset:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset`` command.

        Description:
            - This command sets or queries the clock offset.

        Usage:
            - Using the ``.query()`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset  <NR3>
            - DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset?
            ```

        Sub-properties:
            - ``.auto``: The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:AUTO`` command.
            - ``.manual``: The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:MANual`` command.
            - ``.recalctype``: The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:Recalctype``
              command.
            - ``.selectiontype``: The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset:SELECTIONtype``
              command.
        """
        return self._nominaloffset

    @property
    def pattern(self) -> DpojetMeasItemClockrecoveryPattern:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:PATTern`` command.

        Description:
            - This command turns on or off the usage of CLOCKPath to a specific known data pattern.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:PATTern?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:PATTern?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:PATTern value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:PATTern {1 | 0}
            - DPOJET:MEAS<x>:CLOCKRecovery:PATTern?
            ```
        """
        return self._pattern

    @property
    def standard(self) -> DpojetMeasItemClockrecoveryStandard:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery:STAndard`` command.

        Description:
            - This command sets or queries the current clock recovery standard, as specified in the
              user interface.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery:STAndard?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:STAndard?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:CLOCKRecovery:STAndard value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CLOCKRecovery:STAndard  <string>
            - DPOJET:MEAS<x>:CLOCKRecovery:STAndard?
            ```
        """
        return self._standard


class DpojetMeasItemBusstateTosymbol(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BUSState:TOSymbol`` command.

    Description:
        - This command sets or queries the symbol to which the Bus state is configured.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:TOSymbol?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BUSState:TOSymbol?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BUSState:TOSymbol value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BUSState:TOSymbol  <string>
        - DPOJET:MEAS<x>:BUSState:TOSymbol?
        ```
    """


class DpojetMeasItemBusstateTopattern(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BUSState:TOPattern`` command.

    Description:
        - This command sets or queries the Pattern to which the Bus state is configured.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:TOPattern?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BUSState:TOPattern?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BUSState:TOPattern value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BUSState:TOPattern  <string>
        - DPOJET:MEAS<x>:BUSState:TOPattern?
        ```
    """


class DpojetMeasItemBusstateMeasuretype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BUSState:MEASUREType`` command.

    Description:
        - This command sets or queries the type for which the bus state is configured.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:MEASUREType?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BUSState:MEASUREType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BUSState:MEASUREType value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BUSState:MEASUREType {SYMbol | PATTern}
        - DPOJET:MEAS<x>:BUSState:MEASUREType?
        ```
    """


class DpojetMeasItemBusstateMeasureto(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BUSState:MEASURETO`` command.

    Description:
        - This command sets or queries from where the bus is measured to.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:MEASURETO?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BUSState:MEASURETO?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BUSState:MEASURETO value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BUSState:MEASURETO {START | STOP | CLOCKEdge}
        - DPOJET:MEAS<x>:BUSState:MEASURETO?
        ```
    """


class DpojetMeasItemBusstateMeasurefrom(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BUSState:MEASUREFrom`` command.

    Description:
        - This command sets or queries where the bus is measured from.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:MEASUREFrom?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BUSState:MEASUREFrom?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BUSState:MEASUREFrom value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BUSState:MEASUREFrom {CLOCKEdge | START | STOP}
        - DPOJET:MEAS<x>:BUSState:MEASUREFrom?
        ```
    """


class DpojetMeasItemBusstateFromsymbol(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BUSState:FROMSymbol`` command.

    Description:
        - This command sets or queries the symbol from which the Bus state is configured.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:FROMSymbol?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BUSState:FROMSymbol?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BUSState:FROMSymbol value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BUSState:FROMSymbol  <string>
        - DPOJET:MEAS<x>:BUSState:FROMSymbol?
        ```
    """


class DpojetMeasItemBusstateFrompattern(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BUSState:FROMPattern`` command.

    Description:
        - This command sets or queries the Pattern from which the Bus state is configured.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:FROMPattern?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BUSState:FROMPattern?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BUSState:FROMPattern value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BUSState:FROMPattern  <string>
        - DPOJET:MEAS<x>:BUSState:FROMPattern?
        ```
    """


class DpojetMeasItemBusstateClockpolarity(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BUSState:CLOCKPolarity`` command.

    Description:
        - This command sets or queries the clock polarity for the clock edge.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:CLOCKPolarity?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:BUSState:CLOCKPolarity?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BUSState:CLOCKPolarity value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BUSState:CLOCKPolarity {RISING | FALLING}
        - DPOJET:MEAS<x>:BUSState:CLOCKPolarity?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetMeasItemBusstate(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BUSState`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BUSState?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clockpolarity``: The ``DPOJET:MEAS<x>:BUSState:CLOCKPolarity`` command.
        - ``.frompattern``: The ``DPOJET:MEAS<x>:BUSState:FROMPattern`` command.
        - ``.fromsymbol``: The ``DPOJET:MEAS<x>:BUSState:FROMSymbol`` command.
        - ``.measurefrom``: The ``DPOJET:MEAS<x>:BUSState:MEASUREFrom`` command.
        - ``.measureto``: The ``DPOJET:MEAS<x>:BUSState:MEASURETO`` command.
        - ``.measuretype``: The ``DPOJET:MEAS<x>:BUSState:MEASUREType`` command.
        - ``.topattern``: The ``DPOJET:MEAS<x>:BUSState:TOPattern`` command.
        - ``.tosymbol``: The ``DPOJET:MEAS<x>:BUSState:TOSymbol`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clockpolarity = DpojetMeasItemBusstateClockpolarity(
            device, f"{self._cmd_syntax}:CLOCKPolarity"
        )
        self._frompattern = DpojetMeasItemBusstateFrompattern(
            device, f"{self._cmd_syntax}:FROMPattern"
        )
        self._fromsymbol = DpojetMeasItemBusstateFromsymbol(
            device, f"{self._cmd_syntax}:FROMSymbol"
        )
        self._measurefrom = DpojetMeasItemBusstateMeasurefrom(
            device, f"{self._cmd_syntax}:MEASUREFrom"
        )
        self._measureto = DpojetMeasItemBusstateMeasureto(device, f"{self._cmd_syntax}:MEASURETO")
        self._measuretype = DpojetMeasItemBusstateMeasuretype(
            device, f"{self._cmd_syntax}:MEASUREType"
        )
        self._topattern = DpojetMeasItemBusstateTopattern(device, f"{self._cmd_syntax}:TOPattern")
        self._tosymbol = DpojetMeasItemBusstateTosymbol(device, f"{self._cmd_syntax}:TOSymbol")

    @property
    def clockpolarity(self) -> DpojetMeasItemBusstateClockpolarity:
        """Return the ``DPOJET:MEAS<x>:BUSState:CLOCKPolarity`` command.

        Description:
            - This command sets or queries the clock polarity for the clock edge.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:CLOCKPolarity?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:CLOCKPolarity?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:CLOCKPolarity value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BUSState:CLOCKPolarity {RISING | FALLING}
            - DPOJET:MEAS<x>:BUSState:CLOCKPolarity?
            ```
        """
        return self._clockpolarity

    @property
    def frompattern(self) -> DpojetMeasItemBusstateFrompattern:
        """Return the ``DPOJET:MEAS<x>:BUSState:FROMPattern`` command.

        Description:
            - This command sets or queries the Pattern from which the Bus state is configured.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:FROMPattern?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:FROMPattern?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:FROMPattern value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BUSState:FROMPattern  <string>
            - DPOJET:MEAS<x>:BUSState:FROMPattern?
            ```
        """
        return self._frompattern

    @property
    def fromsymbol(self) -> DpojetMeasItemBusstateFromsymbol:
        """Return the ``DPOJET:MEAS<x>:BUSState:FROMSymbol`` command.

        Description:
            - This command sets or queries the symbol from which the Bus state is configured.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:FROMSymbol?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:FROMSymbol?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:FROMSymbol value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BUSState:FROMSymbol  <string>
            - DPOJET:MEAS<x>:BUSState:FROMSymbol?
            ```
        """
        return self._fromsymbol

    @property
    def measurefrom(self) -> DpojetMeasItemBusstateMeasurefrom:
        """Return the ``DPOJET:MEAS<x>:BUSState:MEASUREFrom`` command.

        Description:
            - This command sets or queries where the bus is measured from.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:MEASUREFrom?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:MEASUREFrom?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:MEASUREFrom value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BUSState:MEASUREFrom {CLOCKEdge | START | STOP}
            - DPOJET:MEAS<x>:BUSState:MEASUREFrom?
            ```
        """
        return self._measurefrom

    @property
    def measureto(self) -> DpojetMeasItemBusstateMeasureto:
        """Return the ``DPOJET:MEAS<x>:BUSState:MEASURETO`` command.

        Description:
            - This command sets or queries from where the bus is measured to.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:MEASURETO?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:MEASURETO?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:MEASURETO value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BUSState:MEASURETO {START | STOP | CLOCKEdge}
            - DPOJET:MEAS<x>:BUSState:MEASURETO?
            ```
        """
        return self._measureto

    @property
    def measuretype(self) -> DpojetMeasItemBusstateMeasuretype:
        """Return the ``DPOJET:MEAS<x>:BUSState:MEASUREType`` command.

        Description:
            - This command sets or queries the type for which the bus state is configured.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:MEASUREType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:MEASUREType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:MEASUREType value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BUSState:MEASUREType {SYMbol | PATTern}
            - DPOJET:MEAS<x>:BUSState:MEASUREType?
            ```
        """
        return self._measuretype

    @property
    def topattern(self) -> DpojetMeasItemBusstateTopattern:
        """Return the ``DPOJET:MEAS<x>:BUSState:TOPattern`` command.

        Description:
            - This command sets or queries the Pattern to which the Bus state is configured.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:TOPattern?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:TOPattern?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:TOPattern value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BUSState:TOPattern  <string>
            - DPOJET:MEAS<x>:BUSState:TOPattern?
            ```
        """
        return self._topattern

    @property
    def tosymbol(self) -> DpojetMeasItemBusstateTosymbol:
        """Return the ``DPOJET:MEAS<x>:BUSState:TOSymbol`` command.

        Description:
            - This command sets or queries the symbol to which the Bus state is configured.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState:TOSymbol?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:TOSymbol?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BUSState:TOSymbol value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BUSState:TOSymbol  <string>
            - DPOJET:MEAS<x>:BUSState:TOSymbol?
            ```
        """
        return self._tosymbol


class DpojetMeasItemBittype(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BITType`` command.

    Description:
        - This command sets or queries the measurement bit type setting.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITType?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BITType?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:BITType value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BITType {ALLBits | NONTRANsition | TRANsition}
        - DPOJET:MEAS<x>:BITType?
        ```
    """


class DpojetMeasItemBitpcnt(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BITPcnt`` command.

    Description:
        - This command sets or queries the percentage value to be measured for the Bit type
          selected.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITPcnt?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BITPcnt?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:BITPcnt value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BITPcnt  <NR3>
        - DPOJET:MEAS<x>:BITPcnt?
        ```
    """


class DpojetMeasItemBitconfigStartpercent(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BITConfig:STARTPercent`` command.

    Description:
        - This command sets or queries the starting percentage of the bit to measure.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITConfig:STARTPercent?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:BITConfig:STARTPercent?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BITConfig:STARTPercent value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BITConfig:STARTPercent  <NR3>
        - DPOJET:MEAS<x>:BITConfig:STARTPercent?
        ```
    """


class DpojetMeasItemBitconfigNumbins(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BITConfig:NUMBins`` command.

    Description:
        - This command sets or queries the number of bins per window.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITConfig:NUMBins?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BITConfig:NUMBins?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BITConfig:NUMBins value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BITConfig:NUMBins  <NR3>
        - DPOJET:MEAS<x>:BITConfig:NUMBins?
        ```
    """


class DpojetMeasItemBitconfigEndpercent(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BITConfig:ENDPercent`` command.

    Description:
        - This command sets or queries the ending percentage of the bit to measure.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITConfig:ENDPercent?``
          query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BITConfig:ENDPercent?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BITConfig:ENDPercent value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BITConfig:ENDPercent  <NR3>
        - DPOJET:MEAS<x>:BITConfig:ENDPercent?
        ```
    """


class DpojetMeasItemBitconfigAbsrelstate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BITConfig:ABSRELstate`` command.

    Description:
        - This command sets or queries the user absolute/relative state, either on or off.0-> sets
          the Absolute1-> sets the Relative

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITConfig:ABSRELstate?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DPOJET:MEAS<x>:BITConfig:ABSRELstate?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:MEAS<x>:BITConfig:ABSRELstate value`` command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BITConfig:ABSRELstate {0|1}
        - DPOJET:MEAS<x>:BITConfig:ABSRELstate?
        ```
    """


class DpojetMeasItemBitconfig(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BITConfig`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITConfig?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BITConfig?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absrelstate``: The ``DPOJET:MEAS<x>:BITConfig:ABSRELstate`` command.
        - ``.endpercent``: The ``DPOJET:MEAS<x>:BITConfig:ENDPercent`` command.
        - ``.numbins``: The ``DPOJET:MEAS<x>:BITConfig:NUMBins`` command.
        - ``.startpercent``: The ``DPOJET:MEAS<x>:BITConfig:STARTPercent`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absrelstate = DpojetMeasItemBitconfigAbsrelstate(
            device, f"{self._cmd_syntax}:ABSRELstate"
        )
        self._endpercent = DpojetMeasItemBitconfigEndpercent(
            device, f"{self._cmd_syntax}:ENDPercent"
        )
        self._numbins = DpojetMeasItemBitconfigNumbins(device, f"{self._cmd_syntax}:NUMBins")
        self._startpercent = DpojetMeasItemBitconfigStartpercent(
            device, f"{self._cmd_syntax}:STARTPercent"
        )

    @property
    def absrelstate(self) -> DpojetMeasItemBitconfigAbsrelstate:
        """Return the ``DPOJET:MEAS<x>:BITConfig:ABSRELstate`` command.

        Description:
            - This command sets or queries the user absolute/relative state, either on or off.0->
              sets the Absolute1-> sets the Relative

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITConfig:ABSRELstate?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BITConfig:ABSRELstate?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BITConfig:ABSRELstate value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BITConfig:ABSRELstate {0|1}
            - DPOJET:MEAS<x>:BITConfig:ABSRELstate?
            ```
        """
        return self._absrelstate

    @property
    def endpercent(self) -> DpojetMeasItemBitconfigEndpercent:
        """Return the ``DPOJET:MEAS<x>:BITConfig:ENDPercent`` command.

        Description:
            - This command sets or queries the ending percentage of the bit to measure.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITConfig:ENDPercent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BITConfig:ENDPercent?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BITConfig:ENDPercent value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BITConfig:ENDPercent  <NR3>
            - DPOJET:MEAS<x>:BITConfig:ENDPercent?
            ```
        """
        return self._endpercent

    @property
    def numbins(self) -> DpojetMeasItemBitconfigNumbins:
        """Return the ``DPOJET:MEAS<x>:BITConfig:NUMBins`` command.

        Description:
            - This command sets or queries the number of bins per window.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITConfig:NUMBins?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BITConfig:NUMBins?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BITConfig:NUMBins value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BITConfig:NUMBins  <NR3>
            - DPOJET:MEAS<x>:BITConfig:NUMBins?
            ```
        """
        return self._numbins

    @property
    def startpercent(self) -> DpojetMeasItemBitconfigStartpercent:
        """Return the ``DPOJET:MEAS<x>:BITConfig:STARTPercent`` command.

        Description:
            - This command sets or queries the starting percentage of the bit to measure.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITConfig:STARTPercent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:MEAS<x>:BITConfig:STARTPercent?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BITConfig:STARTPercent value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BITConfig:STARTPercent  <NR3>
            - DPOJET:MEAS<x>:BITConfig:STARTPercent?
            ```
        """
        return self._startpercent


class DpojetMeasItemBitcfgmethod(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BITCfgmethod`` command.

    Description:
        - This command sets or queries the measurement bit configure method.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITCfgmethod?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BITCfgmethod?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:BITCfgmethod value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BITCfgmethod {MEAN | MODE}
        - DPOJET:MEAS<x>:BITCfgmethod?
        ```
    """


class DpojetMeasItemBerTargetber(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BER:TARGETBER`` command.

    Description:
        - This command sets or queries the BER value.This command is different from
          ``DPOJET:MEAS:RJDJ:BER`` whose configuration parameter exist in RJDJ tab.This command is
          different from ``DPOJET:MEAS:RNDN:BER`` whose configuration parameter exist in RNDN tab.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BER:TARGETBER?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BER:TARGETBER?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:BER:TARGETBER value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:MEAS<x>:BER:TARGETBER  <NR3>
        - DPOJET:MEAS<x>:BER:TARGETBER?
        ```
    """


class DpojetMeasItemBer(SCPICmdRead):
    """The ``DPOJET:MEAS<x>:BER`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BER?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BER?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.targetber``: The ``DPOJET:MEAS<x>:BER:TARGETBER`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._targetber = DpojetMeasItemBerTargetber(device, f"{self._cmd_syntax}:TARGETBER")

    @property
    def targetber(self) -> DpojetMeasItemBerTargetber:
        """Return the ``DPOJET:MEAS<x>:BER:TARGETBER`` command.

        Description:
            - This command sets or queries the BER value.This command is different from
              ``DPOJET:MEAS:RJDJ:BER`` whose configuration parameter exist in RJDJ tab.This command
              is different from ``DPOJET:MEAS:RNDN:BER`` whose configuration parameter exist in RNDN
              tab.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BER:TARGETBER?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BER:TARGETBER?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:BER:TARGETBER value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BER:TARGETBER  <NR3>
            - DPOJET:MEAS<x>:BER:TARGETBER?
            ```
        """
        return self._targetber


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class DpojetMeasItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DPOJET:MEAS<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ber``: The ``DPOJET:MEAS<x>:BER`` command tree.
        - ``.bitcfgmethod``: The ``DPOJET:MEAS<x>:BITCfgmethod`` command.
        - ``.bitconfig``: The ``DPOJET:MEAS<x>:BITConfig`` command tree.
        - ``.bitpcnt``: The ``DPOJET:MEAS<x>:BITPcnt`` command.
        - ``.bittype``: The ``DPOJET:MEAS<x>:BITType`` command.
        - ``.busstate``: The ``DPOJET:MEAS<x>:BUSState`` command tree.
        - ``.clockrecovery``: The ``DPOJET:MEAS<x>:CLOCKRecovery`` command tree.
        - ``.commonmode``: The ``DPOJET:MEAS<x>:COMMONMode`` command tree.
        - ``.customgating``: The ``DPOJET:MEAS<x>:CUSTOMGATING`` command tree.
        - ``.customname``: The ``DPOJET:MEAS<x>:CUSTomname`` command.
        - ``.data``: The ``DPOJET:MEAS<x>:DATA`` command.
        - ``.dfe``: The ``DPOJET:MEAS<x>:DFE`` command tree.
        - ``.displayname``: The ``DPOJET:MEAS<x>:DISPLAYNAME`` command.
        - ``.edge1``: The ``DPOJET:MEAS<x>:EDGE1`` command.
        - ``.edge2``: The ``DPOJET:MEAS<x>:EDGE2`` command.
        - ``.edgeincre``: The ``DPOJET:MEAS<x>:EDGEIncre`` command.
        - ``.edges``: The ``DPOJET:MEAS<x>:EDGES`` command tree.
        - ``.filters``: The ``DPOJET:MEAS<x>:FILTers`` command tree.
        - ``.fromedge``: The ``DPOJET:MEAS<x>:FROMedge`` command.
        - ``.highrefvoltage``: The ``DPOJET:MEAS<x>:HIGHREFVoltage`` command.
        - ``.logging``: The ``DPOJET:MEAS<x>:LOGging`` command tree.
        - ``.lowrefvoltage``: The ``DPOJET:MEAS<x>:LOWREFVoltage`` command.
        - ``.margin``: The ``DPOJET:MEAS<x>:MARGIN`` command tree.
        - ``.maskoffset``: The ``DPOJET:MEAS<x>:MASKOffset`` command tree.
        - ``.maskfile``: The ``DPOJET:MEAS<x>:MASKfile`` command.
        - ``.measrange``: The ``DPOJET:MEAS<x>:MEASRange`` command tree.
        - ``.measstart``: The ``DPOJET:MEAS<x>:MEASStart`` command.
        - ``.n``: The ``DPOJET:MEAS<x>:N`` command.
        - ``.name``: The ``DPOJET:MEAS<x>:NAME`` command.
        - ``.optical``: The ``DPOJET:MEAS<x>:OPTIcal`` command tree.
        - ``.phasenoise``: The ``DPOJET:MEAS<x>:PHASENoise`` command tree.
        - ``.plotfiles``: The ``DPOJET:MEAS<x>:PLOTFILES`` command.
        - ``.refvoltage``: The ``DPOJET:MEAS<x>:REFVoltage`` command.
        - ``.results``: The ``DPOJET:MEAS<x>:RESULts`` command.
        - ``.rjdj``: The ``DPOJET:MEAS<x>:RJDJ`` command tree.
        - ``.rndn``: The ``DPOJET:MEAS<x>:RNDN`` command tree.
        - ``.signaltype``: The ``DPOJET:MEAS<x>:SIGNALType`` command.
        - ``.source1``: The ``DPOJET:MEAS<x>:SOUrce1`` command.
        - ``.source2``: The ``DPOJET:MEAS<x>:SOUrce2`` command.
        - ``.ssc``: The ``DPOJET:MEAS<x>:SSC`` command tree.
        - ``.timedata``: The ``DPOJET:MEAS<x>:TIMEDATa`` command.
        - ``.toedge``: The ``DPOJET:MEAS<x>:TOEdge`` command.
        - ``.zoomevent``: The ``DPOJET:MEAS<x>:ZOOMEVENT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ber = DpojetMeasItemBer(device, f"{self._cmd_syntax}:BER")
        self._bitcfgmethod = DpojetMeasItemBitcfgmethod(device, f"{self._cmd_syntax}:BITCfgmethod")
        self._bitconfig = DpojetMeasItemBitconfig(device, f"{self._cmd_syntax}:BITConfig")
        self._bitpcnt = DpojetMeasItemBitpcnt(device, f"{self._cmd_syntax}:BITPcnt")
        self._bittype = DpojetMeasItemBittype(device, f"{self._cmd_syntax}:BITType")
        self._busstate = DpojetMeasItemBusstate(device, f"{self._cmd_syntax}:BUSState")
        self._clockrecovery = DpojetMeasItemClockrecovery(
            device, f"{self._cmd_syntax}:CLOCKRecovery"
        )
        self._commonmode = DpojetMeasItemCommonmode(device, f"{self._cmd_syntax}:COMMONMode")
        self._customgating = DpojetMeasItemCustomgating(device, f"{self._cmd_syntax}:CUSTOMGATING")
        self._customname = DpojetMeasItemCustomname(device, f"{self._cmd_syntax}:CUSTomname")
        self._data = DpojetMeasItemData(device, f"{self._cmd_syntax}:DATA")
        self._dfe = DpojetMeasItemDfe(device, f"{self._cmd_syntax}:DFE")
        self._displayname = DpojetMeasItemDisplayname(device, f"{self._cmd_syntax}:DISPLAYNAME")
        self._edge1 = DpojetMeasItemEdge1(device, f"{self._cmd_syntax}:EDGE1")
        self._edge2 = DpojetMeasItemEdge2(device, f"{self._cmd_syntax}:EDGE2")
        self._edgeincre = DpojetMeasItemEdgeincre(device, f"{self._cmd_syntax}:EDGEIncre")
        self._edges = DpojetMeasItemEdges(device, f"{self._cmd_syntax}:EDGES")
        self._filters = DpojetMeasItemFilters(device, f"{self._cmd_syntax}:FILTers")
        self._fromedge = DpojetMeasItemFromedge(device, f"{self._cmd_syntax}:FROMedge")
        self._highrefvoltage = DpojetMeasItemHighrefvoltage(
            device, f"{self._cmd_syntax}:HIGHREFVoltage"
        )
        self._logging = DpojetMeasItemLogging(device, f"{self._cmd_syntax}:LOGging")
        self._lowrefvoltage = DpojetMeasItemLowrefvoltage(
            device, f"{self._cmd_syntax}:LOWREFVoltage"
        )
        self._margin = DpojetMeasItemMargin(device, f"{self._cmd_syntax}:MARGIN")
        self._maskoffset = DpojetMeasItemMaskoffset(device, f"{self._cmd_syntax}:MASKOffset")
        self._maskfile = DpojetMeasItemMaskfile(device, f"{self._cmd_syntax}:MASKfile")
        self._measrange = DpojetMeasItemMeasrange(device, f"{self._cmd_syntax}:MEASRange")
        self._measstart = DpojetMeasItemMeasstart(device, f"{self._cmd_syntax}:MEASStart")
        self._n = DpojetMeasItemN(device, f"{self._cmd_syntax}:N")
        self._name = DpojetMeasItemName(device, f"{self._cmd_syntax}:NAME")
        self._optical = DpojetMeasItemOptical(device, f"{self._cmd_syntax}:OPTIcal")
        self._phasenoise = DpojetMeasItemPhasenoise(device, f"{self._cmd_syntax}:PHASENoise")
        self._plotfiles = DpojetMeasItemPlotfiles(device, f"{self._cmd_syntax}:PLOTFILES")
        self._refvoltage = DpojetMeasItemRefvoltage(device, f"{self._cmd_syntax}:REFVoltage")
        self._results = DpojetMeasItemResults(device, f"{self._cmd_syntax}:RESULts")
        self._rjdj = DpojetMeasItemRjdj(device, f"{self._cmd_syntax}:RJDJ")
        self._rndn = DpojetMeasItemRndn(device, f"{self._cmd_syntax}:RNDN")
        self._signaltype = DpojetMeasItemSignaltype(device, f"{self._cmd_syntax}:SIGNALType")
        self._source1 = DpojetMeasItemSource1(device, f"{self._cmd_syntax}:SOUrce1")
        self._source2 = DpojetMeasItemSource2(device, f"{self._cmd_syntax}:SOUrce2")
        self._ssc = DpojetMeasItemSsc(device, f"{self._cmd_syntax}:SSC")
        self._timedata = DpojetMeasItemTimedata(device, f"{self._cmd_syntax}:TIMEDATa")
        self._toedge = DpojetMeasItemToedge(device, f"{self._cmd_syntax}:TOEdge")
        self._zoomevent = DpojetMeasItemZoomevent(device, f"{self._cmd_syntax}:ZOOMEVENT")

    @property
    def ber(self) -> DpojetMeasItemBer:
        """Return the ``DPOJET:MEAS<x>:BER`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BER?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BER?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.targetber``: The ``DPOJET:MEAS<x>:BER:TARGETBER`` command.
        """
        return self._ber

    @property
    def bitcfgmethod(self) -> DpojetMeasItemBitcfgmethod:
        """Return the ``DPOJET:MEAS<x>:BITCfgmethod`` command.

        Description:
            - This command sets or queries the measurement bit configure method.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITCfgmethod?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BITCfgmethod?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:BITCfgmethod value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BITCfgmethod {MEAN | MODE}
            - DPOJET:MEAS<x>:BITCfgmethod?
            ```
        """
        return self._bitcfgmethod

    @property
    def bitconfig(self) -> DpojetMeasItemBitconfig:
        """Return the ``DPOJET:MEAS<x>:BITConfig`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITConfig?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BITConfig?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.absrelstate``: The ``DPOJET:MEAS<x>:BITConfig:ABSRELstate`` command.
            - ``.endpercent``: The ``DPOJET:MEAS<x>:BITConfig:ENDPercent`` command.
            - ``.numbins``: The ``DPOJET:MEAS<x>:BITConfig:NUMBins`` command.
            - ``.startpercent``: The ``DPOJET:MEAS<x>:BITConfig:STARTPercent`` command.
        """
        return self._bitconfig

    @property
    def bitpcnt(self) -> DpojetMeasItemBitpcnt:
        """Return the ``DPOJET:MEAS<x>:BITPcnt`` command.

        Description:
            - This command sets or queries the percentage value to be measured for the Bit type
              selected.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITPcnt?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BITPcnt?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:BITPcnt value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BITPcnt  <NR3>
            - DPOJET:MEAS<x>:BITPcnt?
            ```
        """
        return self._bitpcnt

    @property
    def bittype(self) -> DpojetMeasItemBittype:
        """Return the ``DPOJET:MEAS<x>:BITType`` command.

        Description:
            - This command sets or queries the measurement bit type setting.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BITType?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BITType?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:BITType value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:BITType {ALLBits | NONTRANsition | TRANsition}
            - DPOJET:MEAS<x>:BITType?
            ```
        """
        return self._bittype

    @property
    def busstate(self) -> DpojetMeasItemBusstate:
        """Return the ``DPOJET:MEAS<x>:BUSState`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:BUSState?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:BUSState?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.clockpolarity``: The ``DPOJET:MEAS<x>:BUSState:CLOCKPolarity`` command.
            - ``.frompattern``: The ``DPOJET:MEAS<x>:BUSState:FROMPattern`` command.
            - ``.fromsymbol``: The ``DPOJET:MEAS<x>:BUSState:FROMSymbol`` command.
            - ``.measurefrom``: The ``DPOJET:MEAS<x>:BUSState:MEASUREFrom`` command.
            - ``.measureto``: The ``DPOJET:MEAS<x>:BUSState:MEASURETO`` command.
            - ``.measuretype``: The ``DPOJET:MEAS<x>:BUSState:MEASUREType`` command.
            - ``.topattern``: The ``DPOJET:MEAS<x>:BUSState:TOPattern`` command.
            - ``.tosymbol``: The ``DPOJET:MEAS<x>:BUSState:TOSymbol`` command.
        """
        return self._busstate

    @property
    def clockrecovery(self) -> DpojetMeasItemClockrecovery:
        """Return the ``DPOJET:MEAS<x>:CLOCKRecovery`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:CLOCKRecovery?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bhvrstandard``: The ``DPOJET:MEAS<x>:CLOCKRecovery:BHVRSTANdard`` command.
            - ``.bwtype``: The ``DPOJET:MEAS<x>:CLOCKRecovery:BWType`` command.
            - ``.clockbitrate``: The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKBitrate`` command.
            - ``.clockfrequency``: The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKFrequency`` command.
            - ``.clockmultiplier``: The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKMultiplier`` command.
            - ``.clockpath``: The ``DPOJET:MEAS<x>:CLOCKRecovery:CLOCKPath`` command.
            - ``.damping``: The ``DPOJET:MEAS<x>:CLOCKRecovery:DAMPing`` command.
            - ``.datarate``: The ``DPOJET:MEAS<x>:CLOCKRecovery:DATARate`` command.
            - ``.loopbandwidth``: The ``DPOJET:MEAS<x>:CLOCKRecovery:LOOPBandwidth`` command.
            - ``.meanautocalculate``: The ``DPOJET:MEAS<x>:CLOCKRecovery:MEANAUTOCalculate``
              command.
            - ``.method``: The ``DPOJET:MEAS<x>:CLOCKRecovery:METHod`` command.
            - ``.model``: The ``DPOJET:MEAS<x>:CLOCKRecovery:MODel`` command.
            - ``.nominaloffset``: The ``DPOJET:MEAS<x>:CLOCKRecovery:NOMINALOFFset`` command.
            - ``.pattern``: The ``DPOJET:MEAS<x>:CLOCKRecovery:PATTern`` command.
            - ``.standard``: The ``DPOJET:MEAS<x>:CLOCKRecovery:STAndard`` command.
        """
        return self._clockrecovery

    @property
    def commonmode(self) -> DpojetMeasItemCommonmode:
        """Return the ``DPOJET:MEAS<x>:COMMONMode`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:COMMONMode?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:COMMONMode?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.filters``: The ``DPOJET:MEAS<x>:COMMONMode:FILTers`` command tree.
        """
        return self._commonmode

    @property
    def customgating(self) -> DpojetMeasItemCustomgating:
        """Return the ``DPOJET:MEAS<x>:CUSTOMGATING`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CUSTOMGATING?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:CUSTOMGATING?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.fromedge``: The ``DPOJET:MEAS<x>:CUSTOMGATING:FROMedge`` command.
            - ``.measurementedge``: The ``DPOJET:MEAS<x>:CUSTOMGATING:MEASUREMENTEdge`` command.
            - ``.source1gate``: The ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE1GATE`` command.
            - ``.source2gate``: The ``DPOJET:MEAS<x>:CUSTOMGATING:SOURCE2GATE`` command.
            - ``.toedge``: The ``DPOJET:MEAS<x>:CUSTOMGATING:TOedge`` command.
        """
        return self._customgating

    @property
    def customname(self) -> DpojetMeasItemCustomname:
        """Return the ``DPOJET:MEAS<x>:CUSTomname`` command.

        Description:
            - This command sets or queries the custom measurement name for the measurement in slot
              x.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:CUSTomname?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:CUSTomname?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:CUSTomname value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:CUSTomname  <string>
            - DPOJET:MEAS<x>:CUSTomname?
            ```
        """
        return self._customname

    @property
    def data(self) -> DpojetMeasItemData:
        """Return the ``DPOJET:MEAS<x>:DATA`` command.

        Description:
            - This query-only command returns the measurement data. This is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For Example: If <yyy>=500, <x>=3<yyy> is the number of bytes to
              transfer.<data> is curve data.<newline> is a single-byte new line character at the end
              of the data.<x> is hexadecimal format. The letters A-F denote the number of y bytes
              between 10 and 15 digits.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DATA?
            ```
        """
        return self._data

    @property
    def dfe(self) -> DpojetMeasItemDfe:
        """Return the ``DPOJET:MEAS<x>:DFE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DFE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DFE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.absolutetimestate``: The ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEState`` command.
            - ``.absolutetimevalue``: The ``DPOJET:MEAS<x>:DFE:ABSOLUTETIMEValue`` command.
            - ``.absolutevoltagestate``: The ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEState`` command.
            - ``.absolutevoltagevalue``: The ``DPOJET:MEAS<x>:DFE:ABSOLUTEVOLTAGEValue`` command.
            - ``.delaycompensation``: The ``DPOJET:MEAS<x>:DFE:DELAYCOMPENSATION`` command.
            - ``.manualdelay``: The ``DPOJET:MEAS<x>:DFE:MANUALDELAY`` command.
            - ``.measatpercent``: The ``DPOJET:MEAS<x>:DFE:MEASatpercent`` command.
            - ``.resolution``: The ``DPOJET:MEAS<x>:DFE:RESOlution`` command.
            - ``.tapstate``: The ``DPOJET:MEAS<x>:DFE:TAPState`` command.
            - ``.tapvalue``: The ``DPOJET:MEAS<x>:DFE:TAPValue`` command.
        """
        return self._dfe

    @property
    def displayname(self) -> DpojetMeasItemDisplayname:
        """Return the ``DPOJET:MEAS<x>:DISPLAYNAME`` command.

        Description:
            - This command queries the UI name of the measurement x in the measurement table.If the
              measurement UI name has special character δ, then it is displayed as d.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:DISPLAYNAME?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:DISPLAYNAME?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:DISPLAYNAME?
            ```
        """
        return self._displayname

    @property
    def edge1(self) -> DpojetMeasItemEdge1:
        """Return the ``DPOJET:MEAS<x>:EDGE1`` command.

        Description:
            - This command sets or queries the Source1 edge type.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGE1?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGE1?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:EDGE1 value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:EDGE1 {RISe | FALL | BOTH}
            - DPOJET:MEAS<x>:EDGE1?
            ```
        """
        return self._edge1

    @property
    def edge2(self) -> DpojetMeasItemEdge2:
        """Return the ``DPOJET:MEAS<x>:EDGE2`` command.

        Description:
            - This command sets or queries the Source2 edge type.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGE2?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGE2?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:EDGE2 value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:EDGE2 {RISe | FALL | BOTH}
            - DPOJET:MEAS<x>:EDGE2?
            ```
        """
        return self._edge2

    @property
    def edgeincre(self) -> DpojetMeasItemEdgeincre:
        """Return the ``DPOJET:MEAS<x>:EDGEIncre`` command.

        Description:
            - This command sets or queries the measurement edge increment value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGEIncre?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGEIncre?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:EDGEIncre value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:EDGEIncre  <NR3>
            - DPOJET:MEAS<x>:EDGEIncre?
            ```
        """
        return self._edgeincre

    @property
    def edges(self) -> DpojetMeasItemEdges:
        """Return the ``DPOJET:MEAS<x>:EDGES`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:EDGES?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:EDGES?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.eyeheightstate``: The ``DPOJET:MEAS<x>:EDGES:EYEHeightstate`` command.
            - ``.fromlevel``: The ``DPOJET:MEAS<x>:EDGES:FROMLevel`` command.
            - ``.level``: The ``DPOJET:MEAS<x>:EDGES:LEVel`` command.
            - ``.slewratetechnique``: The ``DPOJET:MEAS<x>:EDGES:SLEWRATETechnique`` command.
            - ``.subratedivisor``: The ``DPOJET:MEAS<x>:EDGES:SUBRATEDivisor`` command.
            - ``.tolevel``: The ``DPOJET:MEAS<x>:EDGES:TOLevel`` command.
            - ``.userdefinedvoltage``: The ``DPOJET:MEAS<x>:EDGES:USERDefinedvoltage`` command.
            - ``.voltagestate``: The ``DPOJET:MEAS<x>:EDGES:VOLTAGEState`` command.
        """
        return self._edges

    @property
    def filters(self) -> DpojetMeasItemFilters:
        """Return the ``DPOJET:MEAS<x>:FILTers`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FILTers?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FILTers?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.blankingtime``: The ``DPOJET:MEAS<x>:FILTers:BLANKingtime`` command.
            - ``.highpass``: The ``DPOJET:MEAS<x>:FILTers:HIGHPass`` command tree.
            - ``.lowpass``: The ``DPOJET:MEAS<x>:FILTers:LOWPass`` command tree.
            - ``.ramptime``: The ``DPOJET:MEAS<x>:FILTers:RAMPtime`` command.
            - ``.sjbandwidth``: The ``DPOJET:MEAS<x>:FILTers:SJBAndwidth`` command.
            - ``.sjfrequency``: The ``DPOJET:MEAS<x>:FILTers:SJFRequency`` command.
        """
        return self._filters

    @property
    def fromedge(self) -> DpojetMeasItemFromedge:
        """Return the ``DPOJET:MEAS<x>:FROMedge`` command.

        Description:
            - This command sets the FROMedge value for the measurement.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:FROMedge?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:FROMedge?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:FROMedge value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:FROMedge {RISe | FALL | BOTH}
            - DPOJET:MEAS<x>:FROMedge?
            ```
        """
        return self._fromedge

    @property
    def highrefvoltage(self) -> DpojetMeasItemHighrefvoltage:
        """Return the ``DPOJET:MEAS<x>:HIGHREFVoltage`` command.

        Description:
            - This command sets or queries the high reference voltage value for the selected
              configuration.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:HIGHREFVoltage?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:HIGHREFVoltage?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:HIGHREFVoltage value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:HIGHREFVoltage  <NR3>
            - DPOJET:MEAS<x>:HIGHREFVoltage?
            ```
        """
        return self._highrefvoltage

    @property
    def logging(self) -> DpojetMeasItemLogging:
        """Return the ``DPOJET:MEAS<x>:LOGging`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOGging?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:LOGging?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.measurements``: The ``DPOJET:MEAS<x>:LOGging:MEASurements`` command tree.
            - ``.statistics``: The ``DPOJET:MEAS<x>:LOGging:STATistics`` command tree.
            - ``.worstcase``: The ``DPOJET:MEAS<x>:LOGging:WORSTcase`` command tree.
        """
        return self._logging

    @property
    def lowrefvoltage(self) -> DpojetMeasItemLowrefvoltage:
        """Return the ``DPOJET:MEAS<x>:LOWREFVoltage`` command.

        Description:
            - This command sets or queries the low reference voltage value for the selected
              configuration.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:LOWREFVoltage?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:LOWREFVoltage?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:MEAS<x>:LOWREFVoltage value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:LOWREFVoltage  <NR3>
            - DPOJET:MEAS<x>:LOWREFVoltage?
            ```
        """
        return self._lowrefvoltage

    @property
    def margin(self) -> DpojetMeasItemMargin:
        """Return the ``DPOJET:MEAS<x>:MARGIN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MARGIN?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MARGIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hitcountvalue``: The ``DPOJET:MEAS<x>:MARGIN:HITCOUNTValue`` command.
            - ``.hitratiostate``: The ``DPOJET:MEAS<x>:MARGIN:HITRATIOState`` command.
            - ``.hitratiovalue``: The ``DPOJET:MEAS<x>:MARGIN:HITRATIOValue`` command.
            - ``.resolution``: The ``DPOJET:MEAS<x>:MARGIN:RESOlution`` command.
        """
        return self._margin

    @property
    def maskoffset(self) -> DpojetMeasItemMaskoffset:
        """Return the ``DPOJET:MEAS<x>:MASKOffset`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MASKOffset?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MASKOffset?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.horizontal``: The ``DPOJET:MEAS<x>:MASKOffset:HORizontal`` command tree.
        """
        return self._maskoffset

    @property
    def maskfile(self) -> DpojetMeasItemMaskfile:
        """Return the ``DPOJET:MEAS<x>:MASKfile`` command.

        Description:
            - This command sets or queries the current mask file name.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MASKfile?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MASKfile?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:MASKfile value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MASKfile  <string>
            - DPOJET:MEAS<x>:MASKfile?
            ```
        """
        return self._maskfile

    @property
    def measrange(self) -> DpojetMeasItemMeasrange:
        """Return the ``DPOJET:MEAS<x>:MEASRange`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MEASRange?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MEASRange?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``DPOJET:MEAS<x>:MEASRange:MAX`` command.
            - ``.min``: The ``DPOJET:MEAS<x>:MEASRange:MIN`` command.
            - ``.state``: The ``DPOJET:MEAS<x>:MEASRange:STATE`` command.
        """
        return self._measrange

    @property
    def measstart(self) -> DpojetMeasItemMeasstart:
        """Return the ``DPOJET:MEAS<x>:MEASStart`` command.

        Description:
            - This command sets or queries the measurement start value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:MEASStart?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:MEASStart?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:MEASStart value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:MEASStart  <NR3>
            - DPOJET:MEAS<x>:MEASStart?
            ```
        """
        return self._measstart

    @property
    def n(self) -> DpojetMeasItemN:
        """Return the ``DPOJET:MEAS<x>:N`` command.

        Description:
            - This command sets or queries the measurement N value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:N?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:N?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:N value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:N  <NR3>
            - DPOJET:MEAS<x>:N?
            ```
        """
        return self._n

    @property
    def name(self) -> DpojetMeasItemName:
        """Return the ``DPOJET:MEAS<x>:NAME`` command.

        Description:
            - This query-only command returns the measurement name for the measurement in slot x.
              For measurements that include 16-bit characters in their UI names, such as DJDirac,
              the string returned will contain question marks where the UI contains nontext
              characters.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:NAME?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:NAME?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:NAME?
            ```
        """
        return self._name

    @property
    def optical(self) -> DpojetMeasItemOptical:
        """Return the ``DPOJET:MEAS<x>:OPTIcal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:OPTIcal?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:OPTIcal?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bandwidth``: The ``DPOJET:MEAS<x>:OPTIcal:BANDWIDth`` command.
            - ``.btfilter``: The ``DPOJET:MEAS<x>:OPTIcal:BTFILTEr`` command.
            - ``.ffetaps``: The ``DPOJET:MEAS<x>:OPTIcal:FFETAPS`` command.
            - ``.scopern``: The ``DPOJET:MEAS<x>:OPTIcal:SCOPERN`` command.
            - ``.targetber``: The ``DPOJET:MEAS<x>:OPTIcal:TARGETBer`` command.
            - ``.wfmtype``: The ``DPOJET:MEAS<x>:OPTIcal:WFMTYpe`` command.
        """
        return self._optical

    @property
    def phasenoise(self) -> DpojetMeasItemPhasenoise:
        """Return the ``DPOJET:MEAS<x>:PHASENoise`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:PHASENoise?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:PHASENoise?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.highlimit``: The ``DPOJET:MEAS<x>:PHASENoise:HIGHLimit`` command.
            - ``.lowlimit``: The ``DPOJET:MEAS<x>:PHASENoise:LOWLimit`` command.
        """
        return self._phasenoise

    @property
    def plotfiles(self) -> DpojetMeasItemPlotfiles:
        """Return the ``DPOJET:MEAS<x>:PLOTFILES`` command.

        Description:
            - The query-only command returns plot file paths of a given measurement.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:PLOTFILES?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:PLOTFILES?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:PLOTFILES?
            ```
        """
        return self._plotfiles

    @property
    def refvoltage(self) -> DpojetMeasItemRefvoltage:
        """Return the ``DPOJET:MEAS<x>:REFVoltage`` command.

        Description:
            - This command sets or queries the reference voltage for the measurement.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:REFVoltage?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:REFVoltage?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:REFVoltage value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:REFVoltage {100 | —100}
            - DPOJET:MEAS<x>:REFVoltage?
            ```
        """
        return self._refvoltage

    @property
    def results(self) -> DpojetMeasItemResults:
        """Return the ``DPOJET:MEAS<x>:RESULts`` command.

        Description:
            - This query-only command returns the measurement branch for the currently selected
              measurement for measurement slot <x>.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RESULts?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RESULts?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:RESULts?
            ```

        Sub-properties:
            - ``.allacqs``: The ``DPOJET:MEAS<x>:RESULts:ALLAcqs`` command.
            - ``.currentacq``: The ``DPOJET:MEAS<x>:RESULts:CURRentacq`` command tree.
            - ``.getall``: The ``DPOJET:MEAS<x>:RESULts:GETAll`` command.
            - ``.status``: The ``DPOJET:MEAS<x>:RESULts:STATus`` command.
            - ``.view``: The ``DPOJET:MEAS<x>:RESULts:VIew`` command.
        """
        return self._results

    @property
    def rjdj(self) -> DpojetMeasItemRjdj:
        """Return the ``DPOJET:MEAS<x>:RJDJ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RJDJ?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RJDJ?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ber``: The ``DPOJET:MEAS<x>:RJDJ:BER`` command.
            - ``.detectplen``: The ``DPOJET:MEAS<x>:RJDJ:DETECTPLEN`` command.
            - ``.ncmode``: The ``DPOJET:MEAS<x>:RJDJ:NCMODe`` command.
            - ``.patlen``: The ``DPOJET:MEAS<x>:RJDJ:PATLen`` command.
            - ``.scopern``: The ``DPOJET:MEAS<x>:RJDJ:SCOPERN`` command.
            - ``.sncrefid``: The ``DPOJET:MEAS<x>:RJDJ:SNCREFID`` command.
            - ``.type``: The ``DPOJET:MEAS<x>:RJDJ:TYPe`` command.
            - ``.windowlength``: The ``DPOJET:MEAS<x>:RJDJ:WINDOwlength`` command.
        """
        return self._rjdj

    @property
    def rndn(self) -> DpojetMeasItemRndn:
        """Return the ``DPOJET:MEAS<x>:RNDN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:RNDN?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:RNDN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autodetectpattern``: The ``DPOJET:MEAS<x>:RNDN:AUTODETECTpattern`` command.
            - ``.ber``: The ``DPOJET:MEAS<x>:RNDN:BER`` command.
            - ``.ncmode``: The ``DPOJET:MEAS<x>:RNDN:NCMODe`` command.
            - ``.patlen``: The ``DPOJET:MEAS<x>:RNDN:PATLen`` command.
            - ``.scopern``: The ``DPOJET:MEAS<x>:RNDN:SCOPERN`` command.
            - ``.sncrefid``: The ``DPOJET:MEAS<x>:RNDN:SNCREFID`` command.
            - ``.type``: The ``DPOJET:MEAS<x>:RNDN:TYPe`` command.
            - ``.windowlength``: The ``DPOJET:MEAS<x>:RNDN:WINDOwlength`` command.
        """
        return self._rndn

    @property
    def signaltype(self) -> DpojetMeasItemSignaltype:
        """Return the ``DPOJET:MEAS<x>:SIGNALType`` command.

        Description:
            - This command sets the signal type for various measurements.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SIGNALType?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:SIGNALType?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:SIGNALType value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:SIGNALType {CLOCK | DATA | AUTO}
            - DPOJET:MEAS<x>:SIGNALType?
            ```
        """
        return self._signaltype

    @property
    def source1(self) -> DpojetMeasItemSource1:
        """Return the ``DPOJET:MEAS<x>:SOUrce1`` command.

        Description:
            - This command sets or queries the Source1 value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:SOUrce1?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:SOUrce1 {CH1 - CH4 | MATH1 - MATH4 | REF1 - REF4 | D0 — D15}
            - DPOJET:MEAS<x>:SOUrce1?
            ```
        """
        return self._source1

    @property
    def source2(self) -> DpojetMeasItemSource2:
        """Return the ``DPOJET:MEAS<x>:SOUrce2`` command.

        Description:
            - This command sets or queries the Source2 value. May return NONE for single-source
              measurement. Source2 may be the second source used in dual-source measurements, or the
              clock source in others. In either case, it is always the same as the rightmost
              displayed source on the UI.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SOUrce2?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:SOUrce2?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:SOUrce2 value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:SOUrce2 {CH1 - CH4 | MATH1 - MATH4 | REF1 - REF4 | D0 — D15}
            - DPOJET:MEAS<x>:SOUrce2?
            ```
        """
        return self._source2

    @property
    def ssc(self) -> DpojetMeasItemSsc:
        """Return the ``DPOJET:MEAS<x>:SSC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:SSC?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:SSC?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.nominalfreq``: The ``DPOJET:MEAS<x>:SSC:NOMinalfreq`` command tree.
        """
        return self._ssc

    @property
    def timedata(self) -> DpojetMeasItemTimedata:
        """Return the ``DPOJET:MEAS<x>:TIMEDATa`` command.

        Description:
            - This query-only command returns the measurement time data. It is similar to the curve
              query, where the output is in the format #<x><yyy><data><newline>, where <x> is the
              number of <y> bytes.For Example: If <yyy>=500, <x>=3<x> is hexadecimal format. The
              letters A-F denote the number of y bytes between 10 and 15 digits.<yyy> is the number
              of bytes to transfer.<data> is curve data.<newline> is a single-byte new line
              character at the end of the data.Time data is not available for all measurements. For
              Example: Scalar measurements.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:TIMEDATa?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:TIMEDATa?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:TIMEDATa?
            ```
        """
        return self._timedata

    @property
    def toedge(self) -> DpojetMeasItemToedge:
        """Return the ``DPOJET:MEAS<x>:TOEdge`` command.

        Description:
            - This command sets the TOEdge value for the measurement.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>:TOEdge?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>:TOEdge?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:TOEdge value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:TOEdge {SAMEas | OPPositeas}
            - DPOJET:MEAS<x>:TOEdge?
            ```
        """
        return self._toedge

    @property
    def zoomevent(self) -> DpojetMeasItemZoomevent:
        """Return the ``DPOJET:MEAS<x>:ZOOMEVENT`` command.

        Description:
            - This command zooms into the waveform where a max/min value occurs in a measurement.

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:MEAS<x>:ZOOMEVENT value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:MEAS<x>:ZOOMEVENT {MAX | MIN}
            ```
        """
        return self._zoomevent


class DpojetLoggingWorstcaseState(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:LOGging:WORSTcase:STATE`` command.

    Description:
        - This command turns on or off the future logging of worst case waveforms. Individual
          measurements included in the logging are selected using the ``DPOJET:MEAS<x>:LOGging``
          node. This parameter turns on or off the entire set of included measurements.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOGging:WORSTcase:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:WORSTcase:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:LOGging:WORSTcase:STATE value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:LOGging:WORSTcase:STATE {1 | 0}
        - DPOJET:LOGging:WORSTcase:STATE?
        ```
    """


class DpojetLoggingWorstcaseFolder(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:LOGging:WORSTcase:FOLDer`` command.

    Description:
        - This command sets or queries the current folder used for worst case logging.Waveform
          filenames generated while worst case logging is on will follow the syntax of “Measurement
          Name”-“Source”_Min1.wfm and “Measurement Name”-“Source”_Max1.wfm, For example:
          Period1-``Ch1_Max1``.wfm, Period1-``Ch1_Min1``.wfm, Rise Time1-``Ch1_Max1``.wfm, Rise
          Time1-``Ch1_Min1``.wfm.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOGging:WORSTcase:FOLDer?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:WORSTcase:FOLDer?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:LOGging:WORSTcase:FOLDer value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:LOGging:WORSTcase:FOLDer  <string>
        - DPOJET:LOGging:WORSTcase:FOLDer?
        ```
    """


class DpojetLoggingWorstcase(SCPICmdRead):
    """The ``DPOJET:LOGging:WORSTcase`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOGging:WORSTcase?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:WORSTcase?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.folder``: The ``DPOJET:LOGging:WORSTcase:FOLDer`` command.
        - ``.state``: The ``DPOJET:LOGging:WORSTcase:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._folder = DpojetLoggingWorstcaseFolder(device, f"{self._cmd_syntax}:FOLDer")
        self._state = DpojetLoggingWorstcaseState(device, f"{self._cmd_syntax}:STATE")

    @property
    def folder(self) -> DpojetLoggingWorstcaseFolder:
        """Return the ``DPOJET:LOGging:WORSTcase:FOLDer`` command.

        Description:
            - This command sets or queries the current folder used for worst case logging.Waveform
              filenames generated while worst case logging is on will follow the syntax of
              “Measurement Name”-“Source”_Min1.wfm and “Measurement Name”-“Source”_Max1.wfm, For
              example: Period1-``Ch1_Max1``.wfm, Period1-``Ch1_Min1``.wfm, Rise
              Time1-``Ch1_Max1``.wfm, Rise Time1-``Ch1_Min1``.wfm.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOGging:WORSTcase:FOLDer?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:WORSTcase:FOLDer?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:LOGging:WORSTcase:FOLDer value`` command.

        SCPI Syntax:
            ```
            - DPOJET:LOGging:WORSTcase:FOLDer  <string>
            - DPOJET:LOGging:WORSTcase:FOLDer?
            ```
        """
        return self._folder

    @property
    def state(self) -> DpojetLoggingWorstcaseState:
        """Return the ``DPOJET:LOGging:WORSTcase:STATE`` command.

        Description:
            - This command turns on or off the future logging of worst case waveforms. Individual
              measurements included in the logging are selected using the ``DPOJET:MEAS<x>:LOGging``
              node. This parameter turns on or off the entire set of included measurements.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOGging:WORSTcase:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:WORSTcase:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:LOGging:WORSTcase:STATE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:LOGging:WORSTcase:STATE {1 | 0}
            - DPOJET:LOGging:WORSTcase:STATE?
            ```
        """
        return self._state


class DpojetLoggingStatisticsState(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:LOGging:STATistics:STATE`` command.

    Description:
        - This command turns on or off the future logging of statistics. Individual measurements
          included in the logging are selected using the ``DPOJET:MEAS<x>:LOGging`` node. This
          parameter turns on or off the entire set of included measurements.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOGging:STATistics:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:STATistics:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:LOGging:STATistics:STATE value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:LOGging:STATistics:STATE {1 | 0}
        - DPOJET:LOGging:STATistics:STATE?
        ```
    """


class DpojetLoggingStatisticsFilename(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:LOGging:STATistics:FILEName`` command.

    Description:
        - This command sets or queries the current file used for statistics logging.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOGging:STATistics:FILEName?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:STATistics:FILEName?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:LOGging:STATistics:FILEName value`` command.

    SCPI Syntax:
        ```
        - DPOJET:LOGging:STATistics:FILEName  <string>
        - DPOJET:LOGging:STATistics:FILEName?
        ```
    """


class DpojetLoggingStatistics(SCPICmdRead):
    """The ``DPOJET:LOGging:STATistics`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOGging:STATistics?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:STATistics?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.filename``: The ``DPOJET:LOGging:STATistics:FILEName`` command.
        - ``.state``: The ``DPOJET:LOGging:STATistics:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._filename = DpojetLoggingStatisticsFilename(device, f"{self._cmd_syntax}:FILEName")
        self._state = DpojetLoggingStatisticsState(device, f"{self._cmd_syntax}:STATE")

    @property
    def filename(self) -> DpojetLoggingStatisticsFilename:
        """Return the ``DPOJET:LOGging:STATistics:FILEName`` command.

        Description:
            - This command sets or queries the current file used for statistics logging.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOGging:STATistics:FILEName?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:LOGging:STATistics:FILEName?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:LOGging:STATistics:FILEName value`` command.

        SCPI Syntax:
            ```
            - DPOJET:LOGging:STATistics:FILEName  <string>
            - DPOJET:LOGging:STATistics:FILEName?
            ```
        """
        return self._filename

    @property
    def state(self) -> DpojetLoggingStatisticsState:
        """Return the ``DPOJET:LOGging:STATistics:STATE`` command.

        Description:
            - This command turns on or off the future logging of statistics. Individual measurements
              included in the logging are selected using the ``DPOJET:MEAS<x>:LOGging`` node. This
              parameter turns on or off the entire set of included measurements.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOGging:STATistics:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:STATistics:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:LOGging:STATistics:STATE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:LOGging:STATistics:STATE {1 | 0}
            - DPOJET:LOGging:STATistics:STATE?
            ```
        """
        return self._state


class DpojetLoggingSnapshot(SCPICmdWrite):
    """The ``DPOJET:LOGging:SNAPshot`` command.

    Description:
        - This command performs a DPOJET export of the specified type, either for statistics or
          measurements.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:LOGging:SNAPshot value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:LOGging:SNAPshot {STATistics | MEASurements}
        ```
    """


class DpojetLoggingMeasurementsState(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:LOGging:MEASurements:STATE`` command.

    Description:
        - This command turns on or off the future logging of measurements. Individual measurements
          included in the logging are selected using the ``DPOJET:MEAS<x>:LOGging`` node. This
          parameter turns on or off the entire set of included measurements.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOGging:MEASurements:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:MEASurements:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:LOGging:MEASurements:STATE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:LOGging:MEASurements:STATE {1 | 0}
        - DPOJET:LOGging:MEASurements:STATE?
        ```
    """


class DpojetLoggingMeasurementsFolder(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:LOGging:MEASurements:FOLDer`` command.

    Description:
        - This command sets or queries the current folder used for measurement logging.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOGging:MEASurements:FOLDer?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:MEASurements:FOLDer?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DPOJET:LOGging:MEASurements:FOLDer value`` command.

    SCPI Syntax:
        ```
        - DPOJET:LOGging:MEASurements:FOLDer  <string>
        - DPOJET:LOGging:MEASurements:FOLDer?
        ```
    """


class DpojetLoggingMeasurements(SCPICmdRead):
    """The ``DPOJET:LOGging:MEASurements`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOGging:MEASurements?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:MEASurements?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.folder``: The ``DPOJET:LOGging:MEASurements:FOLDer`` command.
        - ``.state``: The ``DPOJET:LOGging:MEASurements:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._folder = DpojetLoggingMeasurementsFolder(device, f"{self._cmd_syntax}:FOLDer")
        self._state = DpojetLoggingMeasurementsState(device, f"{self._cmd_syntax}:STATE")

    @property
    def folder(self) -> DpojetLoggingMeasurementsFolder:
        """Return the ``DPOJET:LOGging:MEASurements:FOLDer`` command.

        Description:
            - This command sets or queries the current folder used for measurement logging.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOGging:MEASurements:FOLDer?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:LOGging:MEASurements:FOLDer?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:LOGging:MEASurements:FOLDer value`` command.

        SCPI Syntax:
            ```
            - DPOJET:LOGging:MEASurements:FOLDer  <string>
            - DPOJET:LOGging:MEASurements:FOLDer?
            ```
        """
        return self._folder

    @property
    def state(self) -> DpojetLoggingMeasurementsState:
        """Return the ``DPOJET:LOGging:MEASurements:STATE`` command.

        Description:
            - This command turns on or off the future logging of measurements. Individual
              measurements included in the logging are selected using the ``DPOJET:MEAS<x>:LOGging``
              node. This parameter turns on or off the entire set of included measurements.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOGging:MEASurements:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DPOJET:LOGging:MEASurements:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:LOGging:MEASurements:STATE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:LOGging:MEASurements:STATE {1 | 0}
            - DPOJET:LOGging:MEASurements:STATE?
            ```
        """
        return self._state


class DpojetLogging(SCPICmdRead):
    """The ``DPOJET:LOGging`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOGging?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.measurements``: The ``DPOJET:LOGging:MEASurements`` command tree.
        - ``.snapshot``: The ``DPOJET:LOGging:SNAPshot`` command.
        - ``.statistics``: The ``DPOJET:LOGging:STATistics`` command tree.
        - ``.worstcase``: The ``DPOJET:LOGging:WORSTcase`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._measurements = DpojetLoggingMeasurements(device, f"{self._cmd_syntax}:MEASurements")
        self._snapshot = DpojetLoggingSnapshot(device, f"{self._cmd_syntax}:SNAPshot")
        self._statistics = DpojetLoggingStatistics(device, f"{self._cmd_syntax}:STATistics")
        self._worstcase = DpojetLoggingWorstcase(device, f"{self._cmd_syntax}:WORSTcase")

    @property
    def measurements(self) -> DpojetLoggingMeasurements:
        """Return the ``DPOJET:LOGging:MEASurements`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOGging:MEASurements?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:MEASurements?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.folder``: The ``DPOJET:LOGging:MEASurements:FOLDer`` command.
            - ``.state``: The ``DPOJET:LOGging:MEASurements:STATE`` command.
        """
        return self._measurements

    @property
    def snapshot(self) -> DpojetLoggingSnapshot:
        """Return the ``DPOJET:LOGging:SNAPshot`` command.

        Description:
            - This command performs a DPOJET export of the specified type, either for statistics or
              measurements.

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:LOGging:SNAPshot value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:LOGging:SNAPshot {STATistics | MEASurements}
            ```
        """
        return self._snapshot

    @property
    def statistics(self) -> DpojetLoggingStatistics:
        """Return the ``DPOJET:LOGging:STATistics`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOGging:STATistics?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:STATistics?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.filename``: The ``DPOJET:LOGging:STATistics:FILEName`` command.
            - ``.state``: The ``DPOJET:LOGging:STATistics:STATE`` command.
        """
        return self._statistics

    @property
    def worstcase(self) -> DpojetLoggingWorstcase:
        """Return the ``DPOJET:LOGging:WORSTcase`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOGging:WORSTcase?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging:WORSTcase?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.folder``: The ``DPOJET:LOGging:WORSTcase:FOLDer`` command.
            - ``.state``: The ``DPOJET:LOGging:WORSTcase:STATE`` command.
        """
        return self._worstcase


class DpojetLockrjvalue(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:LOCKRJValue`` command.

    Description:
        - This command sets or queries the LockRJValue. Inorder to set LockRJValue to be effective,
          LOCKRJ to be 1 (enabled).

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOCKRJValue?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOCKRJValue?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:LOCKRJValue value`` command.

    SCPI Syntax:
        ```
        - DPOJET:LOCKRJValue  <NR3>
        - DPOJET:LOCKRJValue?
        ```
    """


class DpojetLockrj(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:LOCKRJ`` command.

    Description:
        - This command sets or queries the Lock RJ Value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LOCKRJ?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LOCKRJ?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:LOCKRJ value`` command.

    SCPI Syntax:
        ```
        - DPOJET:LOCKRJ {1 | 0 }
        - DPOJET:LOCKRJ?
        ```
    """


class DpojetLimitsState(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:LIMits:STATE`` command.

    Description:
        - This command turns on or off the pass-fail limit system. Pass-fail status can be queried
          using the ``DPOJET:MEAS`` ``<x>:RESULTS`` node.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LIMits:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LIMits:STATE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:LIMits:STATE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:LIMits:STATE {1 | 0}
        - DPOJET:LIMits:STATE?
        ```
    """


class DpojetLimitsFilename(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:LIMits:FILEName`` command.

    Description:
        - This command sets or queries the current limits filename.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LIMits:FILEName?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LIMits:FILEName?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:LIMits:FILEName value`` command.

    SCPI Syntax:
        ```
        - DPOJET:LIMits:FILEName  <string>
        - DPOJET:LIMits:FILEName?
        ```
    """


class DpojetLimits(SCPICmdRead):
    """The ``DPOJET:LIMits`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LIMits?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LIMits?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.filename``: The ``DPOJET:LIMits:FILEName`` command.
        - ``.state``: The ``DPOJET:LIMits:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._filename = DpojetLimitsFilename(device, f"{self._cmd_syntax}:FILEName")
        self._state = DpojetLimitsState(device, f"{self._cmd_syntax}:STATE")

    @property
    def filename(self) -> DpojetLimitsFilename:
        """Return the ``DPOJET:LIMits:FILEName`` command.

        Description:
            - This command sets or queries the current limits filename.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LIMits:FILEName?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LIMits:FILEName?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:LIMits:FILEName value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:LIMits:FILEName  <string>
            - DPOJET:LIMits:FILEName?
            ```
        """
        return self._filename

    @property
    def state(self) -> DpojetLimitsState:
        """Return the ``DPOJET:LIMits:STATE`` command.

        Description:
            - This command turns on or off the pass-fail limit system. Pass-fail status can be
              queried using the ``DPOJET:MEAS`` ``<x>:RESULTS`` node.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LIMits:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LIMits:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:LIMits:STATE value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:LIMits:STATE {1 | 0}
            - DPOJET:LIMits:STATE?
            ```
        """
        return self._state


class DpojetLimitrise(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:LIMITRise`` command.

    Description:
        - This command turns on or off the ability to limit Rise/Fall measurements to transition
          bits only.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LIMITRise?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LIMITRise?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:LIMITRise value`` command.

    SCPI Syntax:
        ```
        - DPOJET:LIMITRise {1 | 0}
        - DPOJET:LIMITRise?
        ```
    """


class DpojetLasterror(SCPICmdRead):
    """The ``DPOJET:LASTError`` command.

    Description:
        - This query-only command returns the contents of the last pop-up warning dialog box. If no
          errors have occurred since startup, or since the last call to ``DPOJET:LASTError?``, this
          command returns an empty string.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:LASTError?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:LASTError?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:LASTError?
        ```
    """


class DpojetJittermodel(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:JITtermodel`` command.

    Description:
        - This command sets the current jitter model.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:JITtermodel?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:JITtermodel?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:JITtermodel value`` command.

    SCPI Syntax:
        ```
        - DPOJET:JITtermodel {BUJ | Legacy}
        - DPOJET:JITtermodel?
        ```
    """


class DpojetJittermode(SCPICmdRead):
    """The ``DPOJET:JITtermode`` command.

    Description:
        - This command queries the current jitter mode.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:JITtermode?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:JITtermode?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DPOJET:JITtermode?
        ```
    """


class DpojetInterp(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:INTERp`` command.

    Description:
        - This command sets or queries the current interpolation model.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:INTERp?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:INTERp?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:INTERp value`` command.

    SCPI Syntax:
        ```
        - DPOJET:INTERp {LINear | SINX}
        - DPOJET:INTERp?
        ```
    """


class DpojetHighperfrendering(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:HIGHPerfrendering`` command.

    Description:
        - This command sets or queries the current high-performance eye rendering setting.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:HIGHPerfrendering?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:HIGHPerfrendering?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:HIGHPerfrendering value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:HIGHPerfrendering  <NR1>
        - DPOJET:HIGHPerfrendering?
        ```
    """


class DpojetHaltfreerunonlimfail(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:HALTFreerunonlimfail`` command.

    Description:
        - This command sets or queries the halt free-run on limit failure (On or Off).

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:HALTFreerunonlimfail?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:HALTFreerunonlimfail?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:HALTFreerunonlimfail value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:HALTFreerunonlimfail {1 | 0}
        - DPOJET:HALTFreerunonlimfail?
        ```
    """


class DpojetGating(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:GATING`` command.

    Description:
        - This command sets or queries the gating state.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:GATING?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:GATING?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:GATING value`` command.

    SCPI Syntax:
        ```
        - DPOJET:GATING {OFF | ZOOM | CURSOR | MARKS}
        - DPOJET:GATING?
        ```
    """


class DpojetExportraw(SCPICmdWrite):
    """The ``DPOJET:EXPORTRaw`` command.

    Description:
        - This set-only command saves the raw Eye diagram 2d histogram data to the specified file
          path. The format is determined through the filename extension. Supported extension include
          .csvEnsure that the Plot window is open while sending this PI command; else a file will be
          not generated.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:EXPORTRaw value`` command.

    SCPI Syntax:
        ```
        - DPOJET:EXPORTRaw {PLOT<x>, <file string>}
        ```
    """


class DpojetExport(SCPICmdWrite):
    """The ``DPOJET:EXPORT`` command.

    Description:
        - This set-only command saves the specified DPOJET plot to the specified file path. The
          Format is determined through the filename extension, with a default of png if no extension
          is specified.Supported extensions include jpeg, jpg, tif, tiff, bmp, emf, .mat, .csv and
          png.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:EXPORT value`` command.

    SCPI Syntax:
        ```
        - DPOJET:EXPORT {PLOT<x>, <file string>}
        ```
    """


class DpojetDiracmodel(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DIRacmodel`` command.

    Description:
        - This command sets or queries the current dirac model.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DIRacmodel?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DIRacmodel?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DIRacmodel value`` command.

    SCPI Syntax:
        ```
        - DPOJET:DIRacmodel {FIBREchannel | PCIExpress}
        - DPOJET:DIRacmodel?
        ```
    """


class DpojetDeskewRefmidlevel(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DESKEW:REFMidlevel`` command.

    Description:
        - This command sets or queries the reference channel midlevel value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DESKEW:REFMidlevel?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:REFMidlevel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:REFMidlevel value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:DESKEW:REFMidlevel  <NR3>
        - DPOJET:DESKEW:REFMidlevel?
        ```
    """


class DpojetDeskewRefhysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DESKEW:REFHysteresis`` command.

    Description:
        - This command sets or queries the reference channel hysteresis value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DESKEW:REFHysteresis?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:REFHysteresis?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:REFHysteresis value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:DESKEW:REFHysteresis  <NR3>
        - DPOJET:DESKEW:REFHysteresis?
        ```
    """


class DpojetDeskewRefchannel(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DESKEW:REFChannel`` command.

    Description:
        - This command sets or queries the reference channel used for deskew operation.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DESKEW:REFChannel?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:REFChannel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:REFChannel value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:DESKEW:REFChannel {CH1 - CH4}
        - DPOJET:DESKEW:REFChannel?
        ```
    """


class DpojetDeskewMinimum(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DESKEW:MINimum`` command.

    Description:
        - This command sets or queries the minimum deskew value possible.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DESKEW:MINimum?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:MINimum?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:MINimum value`` command.

    SCPI Syntax:
        ```
        - DPOJET:DESKEW:MINimum  <NR3>
        - DPOJET:DESKEW:MINimum?
        ```
    """


class DpojetDeskewMaximum(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DESKEW:MAXimum`` command.

    Description:
        - This command sets or queries the maximum deskew value possible.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DESKEW:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:MAXimum?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:MAXimum value`` command.

    SCPI Syntax:
        ```
        - DPOJET:DESKEW:MAXimum  <NR3>
        - DPOJET:DESKEW:MAXimum?
        ```
    """


class DpojetDeskewEdge(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DESKEW:EDGE`` command.

    Description:
        - This command sets or queries the edge types used when calculating deskew.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DESKEW:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:EDGE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:EDGE value`` command.

    SCPI Syntax:
        ```
        - DPOJET:DESKEW:EDGE {RISE | FALL | BOTH}
        - DPOJET:DESKEW:EDGE?
        ```
    """


class DpojetDeskewDeskewchannel(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DESKEW:DESKEWchannel`` command.

    Description:
        - This command sets or queries the channel to be deskewed.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DESKEW:DESKEWchannel?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:DESKEWchannel?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:DESKEWchannel value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:DESKEW:DESKEWchannel {CH<x>}
        - DPOJET:DESKEW:DESKEWchannel?
        ```
    """


class DpojetDeskewDeskewmidlevel(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DESKEW:DESKEWMidlevel`` command.

    Description:
        - This command sets or queries the deskew channel midlevel value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DESKEW:DESKEWMidlevel?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:DESKEWMidlevel?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:DESKEWMidlevel value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:DESKEW:DESKEWMidlevel  <NR3>
        - DPOJET:DESKEW:DESKEWMidlevel?
        ```
    """


class DpojetDeskewDeskewhysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DESKEW:DESKEWHysteresis`` command.

    Description:
        - This command sets or queries the deskew channel hysteresis value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DESKEW:DESKEWHysteresis?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:DESKEWHysteresis?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:DESKEWHysteresis value``
          command.

    SCPI Syntax:
        ```
        - DPOJET:DESKEW:DESKEWHysteresis  <NR3>
        - DPOJET:DESKEW:DESKEWHysteresis?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class DpojetDeskew(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DESKEW`` command.

    Description:
        - This command performs a DPOJET deskew operation with the settings specified in
          ``DPOJET:DESKEW``.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DESKEW?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW value`` command.

    SCPI Syntax:
        ```
        - DPOJET:DESKEW {EXEcute}
        - DPOJET:DESKEW?
        ```

    Properties:
        - ``.deskewhysteresis``: The ``DPOJET:DESKEW:DESKEWHysteresis`` command.
        - ``.deskewmidlevel``: The ``DPOJET:DESKEW:DESKEWMidlevel`` command.
        - ``.deskewchannel``: The ``DPOJET:DESKEW:DESKEWchannel`` command.
        - ``.edge``: The ``DPOJET:DESKEW:EDGE`` command.
        - ``.maximum``: The ``DPOJET:DESKEW:MAXimum`` command.
        - ``.minimum``: The ``DPOJET:DESKEW:MINimum`` command.
        - ``.refchannel``: The ``DPOJET:DESKEW:REFChannel`` command.
        - ``.refhysteresis``: The ``DPOJET:DESKEW:REFHysteresis`` command.
        - ``.refmidlevel``: The ``DPOJET:DESKEW:REFMidlevel`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._deskewhysteresis = DpojetDeskewDeskewhysteresis(
            device, f"{self._cmd_syntax}:DESKEWHysteresis"
        )
        self._deskewmidlevel = DpojetDeskewDeskewmidlevel(
            device, f"{self._cmd_syntax}:DESKEWMidlevel"
        )
        self._deskewchannel = DpojetDeskewDeskewchannel(device, f"{self._cmd_syntax}:DESKEWchannel")
        self._edge = DpojetDeskewEdge(device, f"{self._cmd_syntax}:EDGE")
        self._maximum = DpojetDeskewMaximum(device, f"{self._cmd_syntax}:MAXimum")
        self._minimum = DpojetDeskewMinimum(device, f"{self._cmd_syntax}:MINimum")
        self._refchannel = DpojetDeskewRefchannel(device, f"{self._cmd_syntax}:REFChannel")
        self._refhysteresis = DpojetDeskewRefhysteresis(device, f"{self._cmd_syntax}:REFHysteresis")
        self._refmidlevel = DpojetDeskewRefmidlevel(device, f"{self._cmd_syntax}:REFMidlevel")

    @property
    def deskewhysteresis(self) -> DpojetDeskewDeskewhysteresis:
        """Return the ``DPOJET:DESKEW:DESKEWHysteresis`` command.

        Description:
            - This command sets or queries the deskew channel hysteresis value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DESKEW:DESKEWHysteresis?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:DESKEWHysteresis?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:DESKEW:DESKEWHysteresis value`` command.

        SCPI Syntax:
            ```
            - DPOJET:DESKEW:DESKEWHysteresis  <NR3>
            - DPOJET:DESKEW:DESKEWHysteresis?
            ```
        """
        return self._deskewhysteresis

    @property
    def deskewmidlevel(self) -> DpojetDeskewDeskewmidlevel:
        """Return the ``DPOJET:DESKEW:DESKEWMidlevel`` command.

        Description:
            - This command sets or queries the deskew channel midlevel value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DESKEW:DESKEWMidlevel?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:DESKEWMidlevel?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DPOJET:DESKEW:DESKEWMidlevel value`` command.

        SCPI Syntax:
            ```
            - DPOJET:DESKEW:DESKEWMidlevel  <NR3>
            - DPOJET:DESKEW:DESKEWMidlevel?
            ```
        """
        return self._deskewmidlevel

    @property
    def deskewchannel(self) -> DpojetDeskewDeskewchannel:
        """Return the ``DPOJET:DESKEW:DESKEWchannel`` command.

        Description:
            - This command sets or queries the channel to be deskewed.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DESKEW:DESKEWchannel?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:DESKEWchannel?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:DESKEWchannel value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:DESKEW:DESKEWchannel {CH<x>}
            - DPOJET:DESKEW:DESKEWchannel?
            ```
        """
        return self._deskewchannel

    @property
    def edge(self) -> DpojetDeskewEdge:
        """Return the ``DPOJET:DESKEW:EDGE`` command.

        Description:
            - This command sets or queries the edge types used when calculating deskew.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DESKEW:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:EDGE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:EDGE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:DESKEW:EDGE {RISE | FALL | BOTH}
            - DPOJET:DESKEW:EDGE?
            ```
        """
        return self._edge

    @property
    def maximum(self) -> DpojetDeskewMaximum:
        """Return the ``DPOJET:DESKEW:MAXimum`` command.

        Description:
            - This command sets or queries the maximum deskew value possible.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DESKEW:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:MAXimum?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:MAXimum value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:DESKEW:MAXimum  <NR3>
            - DPOJET:DESKEW:MAXimum?
            ```
        """
        return self._maximum

    @property
    def minimum(self) -> DpojetDeskewMinimum:
        """Return the ``DPOJET:DESKEW:MINimum`` command.

        Description:
            - This command sets or queries the minimum deskew value possible.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DESKEW:MINimum?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:MINimum?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:MINimum value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:DESKEW:MINimum  <NR3>
            - DPOJET:DESKEW:MINimum?
            ```
        """
        return self._minimum

    @property
    def refchannel(self) -> DpojetDeskewRefchannel:
        """Return the ``DPOJET:DESKEW:REFChannel`` command.

        Description:
            - This command sets or queries the reference channel used for deskew operation.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DESKEW:REFChannel?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:REFChannel?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:REFChannel value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:DESKEW:REFChannel {CH1 - CH4}
            - DPOJET:DESKEW:REFChannel?
            ```
        """
        return self._refchannel

    @property
    def refhysteresis(self) -> DpojetDeskewRefhysteresis:
        """Return the ``DPOJET:DESKEW:REFHysteresis`` command.

        Description:
            - This command sets or queries the reference channel hysteresis value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DESKEW:REFHysteresis?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:REFHysteresis?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:REFHysteresis value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:DESKEW:REFHysteresis  <NR3>
            - DPOJET:DESKEW:REFHysteresis?
            ```
        """
        return self._refhysteresis

    @property
    def refmidlevel(self) -> DpojetDeskewRefmidlevel:
        """Return the ``DPOJET:DESKEW:REFMidlevel`` command.

        Description:
            - This command sets or queries the reference channel midlevel value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DESKEW:REFMidlevel?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW:REFMidlevel?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW:REFMidlevel value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:DESKEW:REFMidlevel  <NR3>
            - DPOJET:DESKEW:REFMidlevel?
            ```
        """
        return self._refmidlevel


class DpojetDataratelimits(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:DATAratelimits`` command.

    Description:
        - This command sets or queries the reference bitrate for measurement limits.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:DATAratelimits?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:DATAratelimits?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:DATAratelimits value`` command.

    SCPI Syntax:
        ```
        - DPOJET:DATAratelimits  <NR3>
        - DPOJET:DATAratelimits?
        ```
    """


class DpojetClearallplots(SCPICmdWriteNoArguments):
    """The ``DPOJET:CLEARALLPlots`` command.

    Description:
        - This set-only command clears the entire current list of defined plots in DPOJET.

    Usage:
        - Using the ``.write()`` method will send the ``DPOJET:CLEARALLPlots`` command.

    SCPI Syntax:
        ```
        - DPOJET:CLEARALLPlots
        ```
    """


class DpojetClearallmeas(SCPICmdWriteNoArguments):
    """The ``DPOJET:CLEARALLMeas`` command.

    Description:
        - This set-only command clears the entire current list of defined measurements in DPOJET.

    Usage:
        - Using the ``.write()`` method will send the ``DPOJET:CLEARALLMeas`` command.

    SCPI Syntax:
        ```
        - DPOJET:CLEARALLMeas
        ```
    """


class DpojetBitratestate(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:BITRatestate`` command.

    Description:
        - This command sets or queries the user bitrate state, either on or off.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:BITRatestate?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:BITRatestate?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:BITRatestate value`` command.

    SCPI Syntax:
        ```
        - DPOJET:BITRatestate {0|1}
        - DPOJET:BITRatestate?
        ```
    """


class DpojetApplyall(SCPICmdWrite):
    """The ``DPOJET:APPLYAll`` command.

    Description:
        - This command applies configuration of specified type of the specified DPOJET measurement
          to all other DPOJET measurements.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:APPLYAll value`` command.

    SCPI Syntax:
        ```
        - DPOJET:APPLYAll {FILTers | CLOCKRecovery| RJDJ}, MEAS<x>
        ```
    """


class DpojetAnalysismethod(SCPICmdWrite, SCPICmdRead):
    """The ``DPOJET:ANALYSISMETHOD`` command.

    Description:
        - This command sets or queries the current analysis method value.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET:ANALYSISMETHOD?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET:ANALYSISMETHOD?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DPOJET:ANALYSISMETHOD value`` command.

    SCPI Syntax:
        ```
        - DPOJET:ANALYSISMETHOD { JITTEROnly | JITTERNoise }
        - DPOJET:ANALYSISMETHOD?
        ```
    """


class DpojetAddplot(SCPICmdWrite):
    """The ``DPOJET:ADDPlot`` command.

    Description:
        - This set-only command creates a plot of the specified type on the specified DPOJET
          measurement. Up to four plots can be created.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:ADDPlot value`` command.

    SCPI Syntax:
        ```
        - DPOJET:ADDPlot {TIMEtrend | DATAarray | HISTOgram | SPECtrum | TRANSfer | PHASEnoise | EYE | WAVEform | BATHtub | QBathtub | QPulsewidth | COMPOSITEJitterhist | NOISEBAthtub | BERContour | CORRELATEDEye |PDFEye | BEREye | COMPOSITENoisehist}, MEAS<x>
        ```
    """  # noqa: E501


class DpojetAddmeas(SCPICmdWrite):
    """The ``DPOJET:ADDMeas`` command.

    Description:
        - This set-only command adds the specified measurement to the bottom of the current DPOJET
          list of measurements and will appear in the results summary page.

    Usage:
        - Using the ``.write(value)`` method will send the ``DPOJET:ADDMeas value`` command.

    SCPI Syntax:
        ```
        - DPOJET:ADDMeas {PERIod | CCPeriod | FREQuency | NPERiod | PWIdth | NWIdth | PDUTy | NDUTy | PCCDuty | NCCDuty | DATARATE | TIE | RJ | RJDirac | TJber | DJ | DJDirac | PHASENoise | DCD | DDJ | PJ | J2 | J9 | SRJ | PJrms | SJFREQ | PKPKCLKTJ | PKPKCLKRJ | PKPKCLKDJ | PJRMS | FN | RJH | RJV | PJH | PJV | RN | RNV| RNH | DN | DDN | DDN_1 | DDN_0 | PN | PNV | PNH | NPN | TNBER | NOISESUMMARY | UNITAMPLITUDE | RISEtime | SETup | HIGHTime | FALLtime | HOLD | LOWTime | SKEW | GATEDSKEW | HEIght | WIDth | MASKHits | WIDTHBer | HEIGHTBer |CYCLEMIN | CYCLEMAX | ACRMS | ACCOMmonmode | COMmonmode | HIGH | TNTratio | HIGHLOW | LOW | VDIFFxovr | RISESLEWrate | FALLSLEWrate | OVERShoot | UNDERShoot | CYCLEPktopk | JITTERSummary | PCIETTXDiffpp | PCIEDEemph | PCIETTx | PCIETTXRise | PCIETTXFall | PCIEUI | PCIETMinpulse | PCIEMEdmxjitter | PCIETRfmismch | PCIESSCFReqdev | PCIEMAXMINratio | PCIESSCPROFile | PCIEVEye | PCIETTXUTJ | PCIETTXUDJDD | PCIETTXUPWTJ | PCIETTXUPWDJDD | PCIETTXDDJ | PCIEVTXBOOST | PCIEVTXNOEQ | PCIEVTXEIEOS | PCIEPS21TX | PCIEACCommonmode | VTXDiffpp | TMINPULSETJ | TCDRslewmax | USBUI | USBACCommonmode | TMINPULSEDJ | QFACTOR | EYELOW | EYEHIGH | TCMDTOCMD | TIMEOUTSIDELEVEL | SSCFREQDEVMAX | SSCFREQDEVMIN | SSCFREQDEV |SSCMODrate | SSCPROfile | USBSSCFREQDEVMAX | USBSSCFREQDEVMIN | USBSSCMODrate | USBSSCPROFile | AUTOFITMaskhits | AOP | EXRATIO | OMA | OPTHIGH | OPTLOW| EYECROSSLEVEL | EYECROSSTIME | EYECROSSPERCENT | DFEEW | DFEEH | DFEEYEDIAGRAM | VWOE | MASKMARGIN | MASKHITRATIO | RIN | RINXOMA | TDEC }
        ```
    """  # noqa: E501


class DpojetActivate(SCPICmdWriteNoArguments):
    """The ``DPOJET:ACTIVATE`` command.

    Description:
        - This command launches the DPOJET to active state.

    Usage:
        - Using the ``.write()`` method will send the ``DPOJET:ACTIVATE`` command.

    SCPI Syntax:
        ```
        - DPOJET:ACTIVATE
        ```
    """


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class Dpojet(SCPICmdRead):
    """The ``DPOJET`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DPOJET?`` query.
        - Using the ``.verify(value)`` method will send the ``DPOJET?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.activate``: The ``DPOJET:ACTIVATE`` command.
        - ``.addmeas``: The ``DPOJET:ADDMeas`` command.
        - ``.addplot``: The ``DPOJET:ADDPlot`` command.
        - ``.analysismethod``: The ``DPOJET:ANALYSISMETHOD`` command.
        - ``.applyall``: The ``DPOJET:APPLYAll`` command.
        - ``.bitratestate``: The ``DPOJET:BITRatestate`` command.
        - ``.clearallmeas``: The ``DPOJET:CLEARALLMeas`` command.
        - ``.clearallplots``: The ``DPOJET:CLEARALLPlots`` command.
        - ``.dataratelimits``: The ``DPOJET:DATAratelimits`` command.
        - ``.deskew``: The ``DPOJET:DESKEW`` command.
        - ``.diracmodel``: The ``DPOJET:DIRacmodel`` command.
        - ``.export``: The ``DPOJET:EXPORT`` command.
        - ``.exportraw``: The ``DPOJET:EXPORTRaw`` command.
        - ``.gating``: The ``DPOJET:GATING`` command.
        - ``.haltfreerunonlimfail``: The ``DPOJET:HALTFreerunonlimfail`` command.
        - ``.highperfrendering``: The ``DPOJET:HIGHPerfrendering`` command.
        - ``.interp``: The ``DPOJET:INTERp`` command.
        - ``.jittermode``: The ``DPOJET:JITtermode`` command.
        - ``.jittermodel``: The ``DPOJET:JITtermodel`` command.
        - ``.lasterror``: The ``DPOJET:LASTError`` command.
        - ``.limitrise``: The ``DPOJET:LIMITRise`` command.
        - ``.limits``: The ``DPOJET:LIMits`` command tree.
        - ``.lockrj``: The ``DPOJET:LOCKRJ`` command.
        - ``.lockrjvalue``: The ``DPOJET:LOCKRJValue`` command.
        - ``.logging``: The ``DPOJET:LOGging`` command tree.
        - ``.meas``: The ``DPOJET:MEAS<x>`` command tree.
        - ``.minbujui``: The ``DPOJET:MINBUJUI`` command.
        - ``.noiseenabled``: The ``DPOJET:NOISEENABLED`` command.
        - ``.nummeas``: The ``DPOJET:NUMMeas`` command.
        - ``.numplot``: The ``DPOJET:NUMPlot`` command.
        - ``.opticalunittype``: The ``DPOJET:OPTICALUNITType`` command.
        - ``.plot``: The ``DPOJET:PLOT<x>`` command tree.
        - ``.population``: The ``DPOJET:POPULATION`` command tree.
        - ``.qualify``: The ``DPOJET:QUALify`` command tree.
        - ``.reflevel``: The ``DPOJET:REFLevel`` command tree.
        - ``.reflevels``: The ``DPOJET:REFLevels`` command tree.
        - ``.report``: The ``DPOJET:REPORT`` command.
        - ``.results``: The ``DPOJET:RESULts`` command tree.
        - ``.save``: The ``DPOJET:SAVE`` command.
        - ``.saveallplots``: The ``DPOJET:SAVEALLPLOTS`` command.
        - ``.setimagetpath``: The ``DPOJET:SETIMAGETPath`` command.
        - ``.setloggingpath``: The ``DPOJET:SETLOGGINGPath`` command.
        - ``.setreportpath``: The ``DPOJET:SETREPORTPath`` command.
        - ``.showmeaswarning``: The ``DPOJET:SHOWMEASWARNing`` command.
        - ``.snc``: The ``DPOJET:SNC`` command tree.
        - ``.sourceautoset``: The ``DPOJET:SOURCEAutoset`` command.
        - ``.state``: The ``DPOJET:STATE`` command.
        - ``.tdcompensation``: The ``DPOJET:TDCOMPensation`` command.
        - ``.unittype``: The ``DPOJET:UNITType`` command.
        - ``.vertunittype``: The ``DPOJET:VERTUNITType`` command.
        - ``.version``: The ``DPOJET:VERsion`` command.
    """

    # pylint: disable=too-many-statements
    def __init__(  # noqa: PLR0915
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "DPOJET"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._activate = DpojetActivate(device, f"{self._cmd_syntax}:ACTIVATE")
        self._addmeas = DpojetAddmeas(device, f"{self._cmd_syntax}:ADDMeas")
        self._addplot = DpojetAddplot(device, f"{self._cmd_syntax}:ADDPlot")
        self._analysismethod = DpojetAnalysismethod(device, f"{self._cmd_syntax}:ANALYSISMETHOD")
        self._applyall = DpojetApplyall(device, f"{self._cmd_syntax}:APPLYAll")
        self._bitratestate = DpojetBitratestate(device, f"{self._cmd_syntax}:BITRatestate")
        self._clearallmeas = DpojetClearallmeas(device, f"{self._cmd_syntax}:CLEARALLMeas")
        self._clearallplots = DpojetClearallplots(device, f"{self._cmd_syntax}:CLEARALLPlots")
        self._dataratelimits = DpojetDataratelimits(device, f"{self._cmd_syntax}:DATAratelimits")
        self._deskew = DpojetDeskew(device, f"{self._cmd_syntax}:DESKEW")
        self._diracmodel = DpojetDiracmodel(device, f"{self._cmd_syntax}:DIRacmodel")
        self._export = DpojetExport(device, f"{self._cmd_syntax}:EXPORT")
        self._exportraw = DpojetExportraw(device, f"{self._cmd_syntax}:EXPORTRaw")
        self._gating = DpojetGating(device, f"{self._cmd_syntax}:GATING")
        self._haltfreerunonlimfail = DpojetHaltfreerunonlimfail(
            device, f"{self._cmd_syntax}:HALTFreerunonlimfail"
        )
        self._highperfrendering = DpojetHighperfrendering(
            device, f"{self._cmd_syntax}:HIGHPerfrendering"
        )
        self._interp = DpojetInterp(device, f"{self._cmd_syntax}:INTERp")
        self._jittermode = DpojetJittermode(device, f"{self._cmd_syntax}:JITtermode")
        self._jittermodel = DpojetJittermodel(device, f"{self._cmd_syntax}:JITtermodel")
        self._lasterror = DpojetLasterror(device, f"{self._cmd_syntax}:LASTError")
        self._limitrise = DpojetLimitrise(device, f"{self._cmd_syntax}:LIMITRise")
        self._limits = DpojetLimits(device, f"{self._cmd_syntax}:LIMits")
        self._lockrj = DpojetLockrj(device, f"{self._cmd_syntax}:LOCKRJ")
        self._lockrjvalue = DpojetLockrjvalue(device, f"{self._cmd_syntax}:LOCKRJValue")
        self._logging = DpojetLogging(device, f"{self._cmd_syntax}:LOGging")
        self._meas: Dict[int, DpojetMeasItem] = DefaultDictPassKeyToFactory(
            lambda x: DpojetMeasItem(device, f"{self._cmd_syntax}:MEAS{x}")
        )
        self._minbujui = DpojetMinbujui(device, f"{self._cmd_syntax}:MINBUJUI")
        self._noiseenabled = DpojetNoiseenabled(device, f"{self._cmd_syntax}:NOISEENABLED")
        self._nummeas = DpojetNummeas(device, f"{self._cmd_syntax}:NUMMeas")
        self._numplot = DpojetNumplot(device, f"{self._cmd_syntax}:NUMPlot")
        self._opticalunittype = DpojetOpticalunittype(device, f"{self._cmd_syntax}:OPTICALUNITType")
        self._plot: Dict[int, DpojetPlotItem] = DefaultDictPassKeyToFactory(
            lambda x: DpojetPlotItem(device, f"{self._cmd_syntax}:PLOT{x}")
        )
        self._population = DpojetPopulation(device, f"{self._cmd_syntax}:POPULATION")
        self._qualify = DpojetQualify(device, f"{self._cmd_syntax}:QUALify")
        self._reflevel = DpojetReflevel(device, f"{self._cmd_syntax}:REFLevel")
        self._reflevels = DpojetReflevels(device, f"{self._cmd_syntax}:REFLevels")
        self._report = DpojetReport(device, f"{self._cmd_syntax}:REPORT")
        self._results = DpojetResults(device, f"{self._cmd_syntax}:RESULts")
        self._save = DpojetSave(device, f"{self._cmd_syntax}:SAVE")
        self._saveallplots = DpojetSaveallplots(device, f"{self._cmd_syntax}:SAVEALLPLOTS")
        self._setimagetpath = DpojetSetimagetpath(device, f"{self._cmd_syntax}:SETIMAGETPath")
        self._setloggingpath = DpojetSetloggingpath(device, f"{self._cmd_syntax}:SETLOGGINGPath")
        self._setreportpath = DpojetSetreportpath(device, f"{self._cmd_syntax}:SETREPORTPath")
        self._showmeaswarning = DpojetShowmeaswarning(device, f"{self._cmd_syntax}:SHOWMEASWARNing")
        self._snc = DpojetSnc(device, f"{self._cmd_syntax}:SNC")
        self._sourceautoset = DpojetSourceautoset(device, f"{self._cmd_syntax}:SOURCEAutoset")
        self._state = DpojetState(device, f"{self._cmd_syntax}:STATE")
        self._tdcompensation = DpojetTdcompensation(device, f"{self._cmd_syntax}:TDCOMPensation")
        self._unittype = DpojetUnittype(device, f"{self._cmd_syntax}:UNITType")
        self._vertunittype = DpojetVertunittype(device, f"{self._cmd_syntax}:VERTUNITType")
        self._version = DpojetVersion(device, f"{self._cmd_syntax}:VERsion")

    @property
    def activate(self) -> DpojetActivate:
        """Return the ``DPOJET:ACTIVATE`` command.

        Description:
            - This command launches the DPOJET to active state.

        Usage:
            - Using the ``.write()`` method will send the ``DPOJET:ACTIVATE`` command.

        SCPI Syntax:
            ```
            - DPOJET:ACTIVATE
            ```
        """
        return self._activate

    @property
    def addmeas(self) -> DpojetAddmeas:
        """Return the ``DPOJET:ADDMeas`` command.

        Description:
            - This set-only command adds the specified measurement to the bottom of the current
              DPOJET list of measurements and will appear in the results summary page.

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:ADDMeas value`` command.

        SCPI Syntax:
            ```
            - DPOJET:ADDMeas {PERIod | CCPeriod | FREQuency | NPERiod | PWIdth | NWIdth | PDUTy | NDUTy | PCCDuty | NCCDuty | DATARATE | TIE | RJ | RJDirac | TJber | DJ | DJDirac | PHASENoise | DCD | DDJ | PJ | J2 | J9 | SRJ | PJrms | SJFREQ | PKPKCLKTJ | PKPKCLKRJ | PKPKCLKDJ | PJRMS | FN | RJH | RJV | PJH | PJV | RN | RNV| RNH | DN | DDN | DDN_1 | DDN_0 | PN | PNV | PNH | NPN | TNBER | NOISESUMMARY | UNITAMPLITUDE | RISEtime | SETup | HIGHTime | FALLtime | HOLD | LOWTime | SKEW | GATEDSKEW | HEIght | WIDth | MASKHits | WIDTHBer | HEIGHTBer |CYCLEMIN | CYCLEMAX | ACRMS | ACCOMmonmode | COMmonmode | HIGH | TNTratio | HIGHLOW | LOW | VDIFFxovr | RISESLEWrate | FALLSLEWrate | OVERShoot | UNDERShoot | CYCLEPktopk | JITTERSummary | PCIETTXDiffpp | PCIEDEemph | PCIETTx | PCIETTXRise | PCIETTXFall | PCIEUI | PCIETMinpulse | PCIEMEdmxjitter | PCIETRfmismch | PCIESSCFReqdev | PCIEMAXMINratio | PCIESSCPROFile | PCIEVEye | PCIETTXUTJ | PCIETTXUDJDD | PCIETTXUPWTJ | PCIETTXUPWDJDD | PCIETTXDDJ | PCIEVTXBOOST | PCIEVTXNOEQ | PCIEVTXEIEOS | PCIEPS21TX | PCIEACCommonmode | VTXDiffpp | TMINPULSETJ | TCDRslewmax | USBUI | USBACCommonmode | TMINPULSEDJ | QFACTOR | EYELOW | EYEHIGH | TCMDTOCMD | TIMEOUTSIDELEVEL | SSCFREQDEVMAX | SSCFREQDEVMIN | SSCFREQDEV |SSCMODrate | SSCPROfile | USBSSCFREQDEVMAX | USBSSCFREQDEVMIN | USBSSCMODrate | USBSSCPROFile | AUTOFITMaskhits | AOP | EXRATIO | OMA | OPTHIGH | OPTLOW| EYECROSSLEVEL | EYECROSSTIME | EYECROSSPERCENT | DFEEW | DFEEH | DFEEYEDIAGRAM | VWOE | MASKMARGIN | MASKHITRATIO | RIN | RINXOMA | TDEC }
            ```
        """  # noqa: E501
        return self._addmeas

    @property
    def addplot(self) -> DpojetAddplot:
        """Return the ``DPOJET:ADDPlot`` command.

        Description:
            - This set-only command creates a plot of the specified type on the specified DPOJET
              measurement. Up to four plots can be created.

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:ADDPlot value`` command.

        SCPI Syntax:
            ```
            - DPOJET:ADDPlot {TIMEtrend | DATAarray | HISTOgram | SPECtrum | TRANSfer | PHASEnoise | EYE | WAVEform | BATHtub | QBathtub | QPulsewidth | COMPOSITEJitterhist | NOISEBAthtub | BERContour | CORRELATEDEye |PDFEye | BEREye | COMPOSITENoisehist}, MEAS<x>
            ```
        """  # noqa: E501
        return self._addplot

    @property
    def analysismethod(self) -> DpojetAnalysismethod:
        """Return the ``DPOJET:ANALYSISMETHOD`` command.

        Description:
            - This command sets or queries the current analysis method value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:ANALYSISMETHOD?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:ANALYSISMETHOD?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:ANALYSISMETHOD value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:ANALYSISMETHOD { JITTEROnly | JITTERNoise }
            - DPOJET:ANALYSISMETHOD?
            ```
        """
        return self._analysismethod

    @property
    def applyall(self) -> DpojetApplyall:
        """Return the ``DPOJET:APPLYAll`` command.

        Description:
            - This command applies configuration of specified type of the specified DPOJET
              measurement to all other DPOJET measurements.

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:APPLYAll value`` command.

        SCPI Syntax:
            ```
            - DPOJET:APPLYAll {FILTers | CLOCKRecovery| RJDJ}, MEAS<x>
            ```
        """
        return self._applyall

    @property
    def bitratestate(self) -> DpojetBitratestate:
        """Return the ``DPOJET:BITRatestate`` command.

        Description:
            - This command sets or queries the user bitrate state, either on or off.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:BITRatestate?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:BITRatestate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:BITRatestate value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:BITRatestate {0|1}
            - DPOJET:BITRatestate?
            ```
        """
        return self._bitratestate

    @property
    def clearallmeas(self) -> DpojetClearallmeas:
        """Return the ``DPOJET:CLEARALLMeas`` command.

        Description:
            - This set-only command clears the entire current list of defined measurements in
              DPOJET.

        Usage:
            - Using the ``.write()`` method will send the ``DPOJET:CLEARALLMeas`` command.

        SCPI Syntax:
            ```
            - DPOJET:CLEARALLMeas
            ```
        """
        return self._clearallmeas

    @property
    def clearallplots(self) -> DpojetClearallplots:
        """Return the ``DPOJET:CLEARALLPlots`` command.

        Description:
            - This set-only command clears the entire current list of defined plots in DPOJET.

        Usage:
            - Using the ``.write()`` method will send the ``DPOJET:CLEARALLPlots`` command.

        SCPI Syntax:
            ```
            - DPOJET:CLEARALLPlots
            ```
        """
        return self._clearallplots

    @property
    def dataratelimits(self) -> DpojetDataratelimits:
        """Return the ``DPOJET:DATAratelimits`` command.

        Description:
            - This command sets or queries the reference bitrate for measurement limits.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DATAratelimits?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DATAratelimits?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:DATAratelimits value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:DATAratelimits  <NR3>
            - DPOJET:DATAratelimits?
            ```
        """
        return self._dataratelimits

    @property
    def deskew(self) -> DpojetDeskew:
        """Return the ``DPOJET:DESKEW`` command.

        Description:
            - This command performs a DPOJET deskew operation with the settings specified in
              ``DPOJET:DESKEW``.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DESKEW?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DESKEW?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:DESKEW value`` command.

        SCPI Syntax:
            ```
            - DPOJET:DESKEW {EXEcute}
            - DPOJET:DESKEW?
            ```

        Sub-properties:
            - ``.deskewhysteresis``: The ``DPOJET:DESKEW:DESKEWHysteresis`` command.
            - ``.deskewmidlevel``: The ``DPOJET:DESKEW:DESKEWMidlevel`` command.
            - ``.deskewchannel``: The ``DPOJET:DESKEW:DESKEWchannel`` command.
            - ``.edge``: The ``DPOJET:DESKEW:EDGE`` command.
            - ``.maximum``: The ``DPOJET:DESKEW:MAXimum`` command.
            - ``.minimum``: The ``DPOJET:DESKEW:MINimum`` command.
            - ``.refchannel``: The ``DPOJET:DESKEW:REFChannel`` command.
            - ``.refhysteresis``: The ``DPOJET:DESKEW:REFHysteresis`` command.
            - ``.refmidlevel``: The ``DPOJET:DESKEW:REFMidlevel`` command.
        """
        return self._deskew

    @property
    def diracmodel(self) -> DpojetDiracmodel:
        """Return the ``DPOJET:DIRacmodel`` command.

        Description:
            - This command sets or queries the current dirac model.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:DIRacmodel?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:DIRacmodel?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:DIRacmodel value`` command.

        SCPI Syntax:
            ```
            - DPOJET:DIRacmodel {FIBREchannel | PCIExpress}
            - DPOJET:DIRacmodel?
            ```
        """
        return self._diracmodel

    @property
    def export(self) -> DpojetExport:
        """Return the ``DPOJET:EXPORT`` command.

        Description:
            - This set-only command saves the specified DPOJET plot to the specified file path. The
              Format is determined through the filename extension, with a default of png if no
              extension is specified.Supported extensions include jpeg, jpg, tif, tiff, bmp, emf,
              .mat, .csv and png.

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:EXPORT value`` command.

        SCPI Syntax:
            ```
            - DPOJET:EXPORT {PLOT<x>, <file string>}
            ```
        """
        return self._export

    @property
    def exportraw(self) -> DpojetExportraw:
        """Return the ``DPOJET:EXPORTRaw`` command.

        Description:
            - This set-only command saves the raw Eye diagram 2d histogram data to the specified
              file path. The format is determined through the filename extension. Supported
              extension include .csvEnsure that the Plot window is open while sending this PI
              command; else a file will be not generated.

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:EXPORTRaw value`` command.

        SCPI Syntax:
            ```
            - DPOJET:EXPORTRaw {PLOT<x>, <file string>}
            ```
        """
        return self._exportraw

    @property
    def gating(self) -> DpojetGating:
        """Return the ``DPOJET:GATING`` command.

        Description:
            - This command sets or queries the gating state.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:GATING?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:GATING?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:GATING value`` command.

        SCPI Syntax:
            ```
            - DPOJET:GATING {OFF | ZOOM | CURSOR | MARKS}
            - DPOJET:GATING?
            ```
        """
        return self._gating

    @property
    def haltfreerunonlimfail(self) -> DpojetHaltfreerunonlimfail:
        """Return the ``DPOJET:HALTFreerunonlimfail`` command.

        Description:
            - This command sets or queries the halt free-run on limit failure (On or Off).

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:HALTFreerunonlimfail?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:HALTFreerunonlimfail?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:HALTFreerunonlimfail value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:HALTFreerunonlimfail {1 | 0}
            - DPOJET:HALTFreerunonlimfail?
            ```
        """
        return self._haltfreerunonlimfail

    @property
    def highperfrendering(self) -> DpojetHighperfrendering:
        """Return the ``DPOJET:HIGHPerfrendering`` command.

        Description:
            - This command sets or queries the current high-performance eye rendering setting.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:HIGHPerfrendering?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:HIGHPerfrendering?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:HIGHPerfrendering value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:HIGHPerfrendering  <NR1>
            - DPOJET:HIGHPerfrendering?
            ```
        """
        return self._highperfrendering

    @property
    def interp(self) -> DpojetInterp:
        """Return the ``DPOJET:INTERp`` command.

        Description:
            - This command sets or queries the current interpolation model.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:INTERp?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:INTERp?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:INTERp value`` command.

        SCPI Syntax:
            ```
            - DPOJET:INTERp {LINear | SINX}
            - DPOJET:INTERp?
            ```
        """
        return self._interp

    @property
    def jittermode(self) -> DpojetJittermode:
        """Return the ``DPOJET:JITtermode`` command.

        Description:
            - This command queries the current jitter mode.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:JITtermode?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:JITtermode?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:JITtermode?
            ```
        """
        return self._jittermode

    @property
    def jittermodel(self) -> DpojetJittermodel:
        """Return the ``DPOJET:JITtermodel`` command.

        Description:
            - This command sets the current jitter model.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:JITtermodel?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:JITtermodel?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:JITtermodel value`` command.

        SCPI Syntax:
            ```
            - DPOJET:JITtermodel {BUJ | Legacy}
            - DPOJET:JITtermodel?
            ```
        """
        return self._jittermodel

    @property
    def lasterror(self) -> DpojetLasterror:
        """Return the ``DPOJET:LASTError`` command.

        Description:
            - This query-only command returns the contents of the last pop-up warning dialog box. If
              no errors have occurred since startup, or since the last call to
              ``DPOJET:LASTError?``, this command returns an empty string.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LASTError?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LASTError?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:LASTError?
            ```
        """
        return self._lasterror

    @property
    def limitrise(self) -> DpojetLimitrise:
        """Return the ``DPOJET:LIMITRise`` command.

        Description:
            - This command turns on or off the ability to limit Rise/Fall measurements to transition
              bits only.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LIMITRise?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LIMITRise?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:LIMITRise value`` command.

        SCPI Syntax:
            ```
            - DPOJET:LIMITRise {1 | 0}
            - DPOJET:LIMITRise?
            ```
        """
        return self._limitrise

    @property
    def limits(self) -> DpojetLimits:
        """Return the ``DPOJET:LIMits`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LIMits?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LIMits?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.filename``: The ``DPOJET:LIMits:FILEName`` command.
            - ``.state``: The ``DPOJET:LIMits:STATE`` command.
        """
        return self._limits

    @property
    def lockrj(self) -> DpojetLockrj:
        """Return the ``DPOJET:LOCKRJ`` command.

        Description:
            - This command sets or queries the Lock RJ Value.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOCKRJ?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LOCKRJ?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:LOCKRJ value`` command.

        SCPI Syntax:
            ```
            - DPOJET:LOCKRJ {1 | 0 }
            - DPOJET:LOCKRJ?
            ```
        """
        return self._lockrj

    @property
    def lockrjvalue(self) -> DpojetLockrjvalue:
        """Return the ``DPOJET:LOCKRJValue`` command.

        Description:
            - This command sets or queries the LockRJValue. Inorder to set LockRJValue to be
              effective, LOCKRJ to be 1 (enabled).

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOCKRJValue?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LOCKRJValue?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:LOCKRJValue value`` command.

        SCPI Syntax:
            ```
            - DPOJET:LOCKRJValue  <NR3>
            - DPOJET:LOCKRJValue?
            ```
        """
        return self._lockrjvalue

    @property
    def logging(self) -> DpojetLogging:
        """Return the ``DPOJET:LOGging`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:LOGging?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:LOGging?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.measurements``: The ``DPOJET:LOGging:MEASurements`` command tree.
            - ``.snapshot``: The ``DPOJET:LOGging:SNAPshot`` command.
            - ``.statistics``: The ``DPOJET:LOGging:STATistics`` command tree.
            - ``.worstcase``: The ``DPOJET:LOGging:WORSTcase`` command tree.
        """
        return self._logging

    @property
    def meas(self) -> Dict[int, DpojetMeasItem]:
        """Return the ``DPOJET:MEAS<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MEAS<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MEAS<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ber``: The ``DPOJET:MEAS<x>:BER`` command tree.
            - ``.bitcfgmethod``: The ``DPOJET:MEAS<x>:BITCfgmethod`` command.
            - ``.bitconfig``: The ``DPOJET:MEAS<x>:BITConfig`` command tree.
            - ``.bitpcnt``: The ``DPOJET:MEAS<x>:BITPcnt`` command.
            - ``.bittype``: The ``DPOJET:MEAS<x>:BITType`` command.
            - ``.busstate``: The ``DPOJET:MEAS<x>:BUSState`` command tree.
            - ``.clockrecovery``: The ``DPOJET:MEAS<x>:CLOCKRecovery`` command tree.
            - ``.commonmode``: The ``DPOJET:MEAS<x>:COMMONMode`` command tree.
            - ``.customgating``: The ``DPOJET:MEAS<x>:CUSTOMGATING`` command tree.
            - ``.customname``: The ``DPOJET:MEAS<x>:CUSTomname`` command.
            - ``.data``: The ``DPOJET:MEAS<x>:DATA`` command.
            - ``.dfe``: The ``DPOJET:MEAS<x>:DFE`` command tree.
            - ``.displayname``: The ``DPOJET:MEAS<x>:DISPLAYNAME`` command.
            - ``.edge1``: The ``DPOJET:MEAS<x>:EDGE1`` command.
            - ``.edge2``: The ``DPOJET:MEAS<x>:EDGE2`` command.
            - ``.edgeincre``: The ``DPOJET:MEAS<x>:EDGEIncre`` command.
            - ``.edges``: The ``DPOJET:MEAS<x>:EDGES`` command tree.
            - ``.filters``: The ``DPOJET:MEAS<x>:FILTers`` command tree.
            - ``.fromedge``: The ``DPOJET:MEAS<x>:FROMedge`` command.
            - ``.highrefvoltage``: The ``DPOJET:MEAS<x>:HIGHREFVoltage`` command.
            - ``.logging``: The ``DPOJET:MEAS<x>:LOGging`` command tree.
            - ``.lowrefvoltage``: The ``DPOJET:MEAS<x>:LOWREFVoltage`` command.
            - ``.margin``: The ``DPOJET:MEAS<x>:MARGIN`` command tree.
            - ``.maskoffset``: The ``DPOJET:MEAS<x>:MASKOffset`` command tree.
            - ``.maskfile``: The ``DPOJET:MEAS<x>:MASKfile`` command.
            - ``.measrange``: The ``DPOJET:MEAS<x>:MEASRange`` command tree.
            - ``.measstart``: The ``DPOJET:MEAS<x>:MEASStart`` command.
            - ``.n``: The ``DPOJET:MEAS<x>:N`` command.
            - ``.name``: The ``DPOJET:MEAS<x>:NAME`` command.
            - ``.optical``: The ``DPOJET:MEAS<x>:OPTIcal`` command tree.
            - ``.phasenoise``: The ``DPOJET:MEAS<x>:PHASENoise`` command tree.
            - ``.plotfiles``: The ``DPOJET:MEAS<x>:PLOTFILES`` command.
            - ``.refvoltage``: The ``DPOJET:MEAS<x>:REFVoltage`` command.
            - ``.results``: The ``DPOJET:MEAS<x>:RESULts`` command.
            - ``.rjdj``: The ``DPOJET:MEAS<x>:RJDJ`` command tree.
            - ``.rndn``: The ``DPOJET:MEAS<x>:RNDN`` command tree.
            - ``.signaltype``: The ``DPOJET:MEAS<x>:SIGNALType`` command.
            - ``.source1``: The ``DPOJET:MEAS<x>:SOUrce1`` command.
            - ``.source2``: The ``DPOJET:MEAS<x>:SOUrce2`` command.
            - ``.ssc``: The ``DPOJET:MEAS<x>:SSC`` command tree.
            - ``.timedata``: The ``DPOJET:MEAS<x>:TIMEDATa`` command.
            - ``.toedge``: The ``DPOJET:MEAS<x>:TOEdge`` command.
            - ``.zoomevent``: The ``DPOJET:MEAS<x>:ZOOMEVENT`` command.
        """
        return self._meas

    @property
    def minbujui(self) -> DpojetMinbujui:
        """Return the ``DPOJET:MINBUJUI`` command.

        Description:
            - This command sets or queries the minimum number of UI for BUJ analysis.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:MINBUJUI?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:MINBUJUI?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:MINBUJUI value`` command.

        SCPI Syntax:
            ```
            - DPOJET:MINBUJUI  <NR3>
            - DPOJET:MINBUJUI?
            ```
        """
        return self._minbujui

    @property
    def noiseenabled(self) -> DpojetNoiseenabled:
        """Return the ``DPOJET:NOISEENABLED`` command.

        Description:
            - This set-only command turns on or off the Noise measurements.Configure

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:NOISEENABLED value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:NOISEENABLED {1 | 0 | ON | OFF}
            ```
        """
        return self._noiseenabled

    @property
    def nummeas(self) -> DpojetNummeas:
        """Return the ``DPOJET:NUMMeas`` command.

        Description:
            - This query-only command returns the current number of defined measurements.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:NUMMeas?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:NUMMeas?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:NUMMeas?
            ```
        """
        return self._nummeas

    @property
    def numplot(self) -> DpojetNumplot:
        """Return the ``DPOJET:NUMPlot`` command.

        Description:
            - This query-only command returns the current number of plots added. If no plots are
              added, then it returns 0, else returns the total number of plots added between value 1
              to 4.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:NUMPlot?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:NUMPlot?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:NUMPlot?
            ```
        """
        return self._numplot

    @property
    def opticalunittype(self) -> DpojetOpticalunittype:
        """Return the ``DPOJET:OPTICALUNITType`` command.

        Description:
            - This command sets or queries the current optical unit-type setting for DPOJET, either
              Watt, or dBm.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:OPTICALUNITType?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:OPTICALUNITType?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:OPTICALUNITType value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:OPTICALUNITType {WATT | DBM}
            - DPOJET:OPTICALUNITType?
            ```
        """
        return self._opticalunittype

    @property
    def plot(self) -> Dict[int, DpojetPlotItem]:
        """Return the ``DPOJET:PLOT<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:PLOT<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:PLOT<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bathtub``: The ``DPOJET:PLOT<x>:BATHtub`` command tree.
            - ``.bercontour``: The ``DPOJET:PLOT<x>:BERContour`` command tree.
            - ``.bereye``: The ``DPOJET:PLOT<x>:BEREye`` command tree.
            - ``.compositejitterhist``: The ``DPOJET:PLOT<x>:COMPOSITEJitterhist`` command tree.
            - ``.compositenoisehist``: The ``DPOJET:PLOT<x>:COMPOSITENoisehist`` command tree.
            - ``.correlatedeye``: The ``DPOJET:PLOT<x>:CORRELATEDEye`` command tree.
            - ``.currentuisacquired``: The ``DPOJET:PLOT<x>:CURRENTUISACquired`` command.
            - ``.currentuisanalyzed``: The ``DPOJET:PLOT<x>:CURRENTUISANalyzed`` command.
            - ``.data``: The ``DPOJET:PLOT<x>:DATA`` command tree.
            - ``.exportraw``: The ``DPOJET:PLOT<x>:EXPORTRaw`` command.
            - ``.eye``: The ``DPOJET:PLOT<x>:EYE`` command tree.
            - ``.histogram``: The ``DPOJET:PLOT<x>:HISTOgram`` command tree.
            - ``.noisebathtub``: The ``DPOJET:PLOT<x>:NOISEBATHtub`` command tree.
            - ``.pdfeye``: The ``DPOJET:PLOT<x>:PDFEye`` command tree.
            - ``.phasenoise``: The ``DPOJET:PLOT<x>:PHASEnoise`` command tree.
            - ``.source``: The ``DPOJET:PLOT<x>:SOUrce`` command.
            - ``.spectrum``: The ``DPOJET:PLOT<x>:SPECtrum`` command tree.
            - ``.totaluisacquired``: The ``DPOJET:PLOT<x>:TOTALUISAcquired`` command.
            - ``.totaluisanalyzed``: The ``DPOJET:PLOT<x>:TOTALUISAnalyzed`` command.
            - ``.transfer``: The ``DPOJET:PLOT<x>:TRANSfer`` command tree.
            - ``.trend``: The ``DPOJET:PLOT<x>:TREND`` command tree.
            - ``.type``: The ``DPOJET:PLOT<x>:TYPe`` command.
            - ``.vertbathtub``: The ``DPOJET:PLOT<x>:VERTBATHtub`` command tree.
            - ``.xunits``: The ``DPOJET:PLOT<x>:XUnits`` command.
            - ``.yunits``: The ``DPOJET:PLOT<x>:YUnits`` command.
        """
        return self._plot

    @property
    def population(self) -> DpojetPopulation:
        """Return the ``DPOJET:POPULATION`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:POPULATION?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:POPULATION?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``DPOJET:POPULATION:CONDition`` command.
            - ``.limit``: The ``DPOJET:POPULATION:LIMIT`` command.
            - ``.limitby``: The ``DPOJET:POPULATION:LIMITBY`` command.
            - ``.state``: The ``DPOJET:POPULATION:STATE`` command.
        """
        return self._population

    @property
    def qualify(self) -> DpojetQualify:
        """Return the ``DPOJET:QUALify`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:QUALify?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:QUALify?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.active``: The ``DPOJET:QUALify:ACTIVE`` command.
            - ``.source``: The ``DPOJET:QUALify:SOUrce`` command.
            - ``.state``: The ``DPOJET:QUALify:STATE`` command.
        """
        return self._qualify

    @property
    def reflevel(self) -> DpojetReflevel:
        """Return the ``DPOJET:REFLevel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REFLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevel?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``DPOJET:REFLevel:CH<x>`` command tree.
        """
        return self._reflevel

    @property
    def reflevels(self) -> DpojetReflevels:
        """Return the ``DPOJET:REFLevels`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:REFLevels?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:REFLevels?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autoset``: The ``DPOJET:REFLevels:AUTOset`` command.
            - ``.ch``: The ``DPOJET:REFLevels:CH<x>`` command tree.
        """
        return self._reflevels

    @property
    def report(self) -> DpojetReport:
        """Return the ``DPOJET:REPORT`` command.

        Description:
            - These are set-only commands. EXECute executes a DPOJET report save operation for the
              currently defined report configuration. APPEnd appends new data to the selected
              report.Ensure to close the PDF report before append.

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:REPORT value`` command.

        SCPI Syntax:
            ```
            - DPOJET:REPORT {EXECute | APPEnd}
            ```

        Sub-properties:
            - ``.applicationconfig``: The ``DPOJET:REPORT:APPlicationconfig`` command.
            - ``.autoincrement``: The ``DPOJET:REPORT:AUTOincrement`` command.
            - ``.comments``: The ``DPOJET:REPORT:COMments`` command.
            - ``.detailedresults``: The ``DPOJET:REPORT:DETailedresults`` command.
            - ``.enablecomments``: The ``DPOJET:REPORT:ENABlecomments`` command.
            - ``.getimage``: The ``DPOJET:REPORT:GETIMAGE`` command.
            - ``.getimagename``: The ``DPOJET:REPORT:GETIMAGEName`` command.
            - ``.getxmlreport``: The ``DPOJET:REPORT:GETXMLReport`` command.
            - ``.passfailresults``: The ``DPOJET:REPORT:PASSFailresults`` command.
            - ``.plotimages``: The ``DPOJET:REPORT:PLOTimages`` command.
            - ``.reportname``: The ``DPOJET:REPORT:REPORTName`` command.
            - ``.savewaveforms``: The ``DPOJET:REPORT:SAVEWaveforms`` command.
            - ``.setimagepath``: The ``DPOJET:REPORT:SETIMAGEPath`` command.
            - ``.setupconfig``: The ``DPOJET:REPORT:SETupconfig`` command.
            - ``.state``: The ``DPOJET:REPORT:STATE`` command.
            - ``.type``: The ``DPOJET:REPORT:TYPe`` command.
            - ``.viewreport``: The ``DPOJET:REPORT:VIEWreport`` command.
        """
        return self._report

    @property
    def results(self) -> DpojetResults:
        """Return the ``DPOJET:RESULts`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:RESULts?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:RESULts?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.getallresults``: The ``DPOJET:RESULts:GETALLResults`` command.
            - ``.status``: The ``DPOJET:RESULts:STATus`` command.
            - ``.view``: The ``DPOJET:RESULts:VIew`` command.
        """
        return self._results

    @property
    def save(self) -> DpojetSave:
        """Return the ``DPOJET:SAVE`` command.

        Description:
            - This set-only command saves the specified DPOJET measurement result to the specified
              ref. For Example: ``DPOJET:SAVE`` MEAS4, REF2.

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:SAVE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:SAVE {MEAS<x> | REF<x>}
            ```
        """
        return self._save

    @property
    def saveallplots(self) -> DpojetSaveallplots:
        """Return the ``DPOJET:SAVEALLPLOTS`` command.

        Description:
            - Saves all the plots to Reports/Resource folder.

        Usage:
            - Using the ``.write()`` method will send the ``DPOJET:SAVEALLPLOTS`` command.

        SCPI Syntax:
            ```
            - DPOJET:SAVEALLPLOTS
            ```
        """
        return self._saveallplots

    @property
    def setimagetpath(self) -> DpojetSetimagetpath:
        """Return the ``DPOJET:SETIMAGETPath`` command.

        Description:
            - This command sets or queries the image path of the DPOJET application.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:SETIMAGETPath?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:SETIMAGETPath?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:SETIMAGETPath value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:SETIMAGETPath  <file string>
            - DPOJET:SETIMAGETPath?
            ```
        """
        return self._setimagetpath

    @property
    def setloggingpath(self) -> DpojetSetloggingpath:
        """Return the ``DPOJET:SETLOGGINGPath`` command.

        Description:
            - This command sets or queries the Logging path of the DPOJET application.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:SETLOGGINGPath?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:SETLOGGINGPath?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:SETLOGGINGPath value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:SETLOGGINGPath  <file string>
            - DPOJET:SETLOGGINGPath?
            ```
        """
        return self._setloggingpath

    @property
    def setreportpath(self) -> DpojetSetreportpath:
        """Return the ``DPOJET:SETREPORTPath`` command.

        Description:
            - This command sets or queries the Report path of the DPOJET application.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:SETREPORTPath?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:SETREPORTPath?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:SETREPORTPath value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:SETREPORTPath  <file string>
            - DPOJET:SETREPORTPath?
            ```
        """
        return self._setreportpath

    @property
    def showmeaswarning(self) -> DpojetShowmeaswarning:
        """Return the ``DPOJET:SHOWMEASWARNing`` command.

        Description:
            - This sets or queries the visibility of Reference Level Autoset warnings, either on or
              off.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:SHOWMEASWARNing?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:SHOWMEASWARNing?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:SHOWMEASWARNing value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:SHOWMEASWARNing {1|0}
            - DPOJET:SHOWMEASWARNing?
            ```
        """
        return self._showmeaswarning

    @property
    def snc(self) -> DpojetSnc:
        """Return the ``DPOJET:SNC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:SNC?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:SNC?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.activate``: The ``DPOJET:SNC:ACTIvate`` command.
            - ``.close``: The ``DPOJET:SNC:CLOse`` command.
        """
        return self._snc

    @property
    def sourceautoset(self) -> DpojetSourceautoset:
        """Return the ``DPOJET:SOURCEAutoset`` command.

        Description:
            - This command performs a DPOJET horizontal, vertical, or autoset on both horizontal and
              vertical for any sources used in current measurements.

        Usage:
            - Using the ``.write(value)`` method will send the ``DPOJET:SOURCEAutoset value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:SOURCEAutoset {HORizontal | VERTical | BOTH}
            ```

        Sub-properties:
            - ``.horizontal``: The ``DPOJET:SOURCEAutoset:HORizontal`` command tree.
            - ``.state``: The ``DPOJET:SOURCEAutoset:STATE`` command.
        """
        return self._sourceautoset

    @property
    def state(self) -> DpojetState:
        """Return the ``DPOJET:STATE`` command.

        Description:
            - This command sets or queries the current measurement state of DPOJET.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:STATE value`` command.

        SCPI Syntax:
            ```
            - DPOJET:STATE {RUN | SINGLE | RECALC | CLEAR | STOP}
            - DPOJET:STATE?
            ```
        """
        return self._state

    @property
    def tdcompensation(self) -> DpojetTdcompensation:
        """Return the ``DPOJET:TDCOMPensation`` command.

        Description:
            - This command sets or queries the TD compensation state.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:TDCOMPensation?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:TDCOMPensation?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:TDCOMPensation value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:TDCOMPensation {1 | 0 | ON | OFF}
            - DPOJET:TDCOMPensation?
            ```
        """
        return self._tdcompensation

    @property
    def unittype(self) -> DpojetUnittype:
        """Return the ``DPOJET:UNITType`` command.

        Description:
            - This command sets or queries the current unit-type setting for DPOJET, either Unit
              Interval, or seconds.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:UNITType?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:UNITType?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:UNITType value`` command.

        SCPI Syntax:
            ```
            - DPOJET:UNITType {UNITinterval | SEConds}
            - DPOJET:UNITType?
            ```
        """
        return self._unittype

    @property
    def vertunittype(self) -> DpojetVertunittype:
        """Return the ``DPOJET:VERTUNITType`` command.

        Description:
            - This command sets or queries the vertical Unit.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:VERTUNITType?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:VERTUNITType?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DPOJET:VERTUNITType value``
              command.

        SCPI Syntax:
            ```
            - DPOJET:VERTUNITType {UNITamplitude | VOLts}
            - DPOJET:VERTUNITType?
            ```
        """
        return self._vertunittype

    @property
    def version(self) -> DpojetVersion:
        """Return the ``DPOJET:VERsion`` command.

        Description:
            - This query-only command returns the current DPOJET version string.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET:VERsion?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET:VERsion?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DPOJET:VERsion?
            ```
        """
        return self._version
