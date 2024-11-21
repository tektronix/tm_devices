# pylint: disable=line-too-long
"""The power commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - POWer:ADDNew 'POWER<x>'
    - POWer:DELete 'POWER<x>'
    - POWer:POWer<x>:AUTOSet EXECute
    - POWer:POWer<x>:CLRESPONSE:AMP<x>Val <NR3>
    - POWer:POWer<x>:CLRESPONSE:AMP<x>Val?
    - POWer:POWer<x>:CLRESPONSE:AMPMode {CONSTant|PROFile}
    - POWer:POWer<x>:CLRESPONSE:AMPMode?
    - POWer:POWer<x>:CLRESPONSE:ANALYSISMethod {SV|FFT}
    - POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?
    - POWer:POWer<x>:CLRESPONSE:AUTORbw {True|False}
    - POWer:POWer<x>:CLRESPONSE:AUTORbw?
    - POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?
    - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude <NR3>
    - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?
    - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val <NR3>
    - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?
    - POWer:POWer<x>:CLRESPONSE:GENIPADDress <NR2>
    - POWer:POWer<x>:CLRESPONSE:GENIPADDress?
    - POWer:POWer<x>:CLRESPONSE:GENerator {INTernal}
    - POWer:POWer<x>:CLRESPONSE:GENerator?
    - POWer:POWer<x>:CLRESPONSE:IMPEDance {FIFTy|HIGHZ}
    - POWer:POWer<x>:CLRESPONSE:IMPEDance?
    - POWer:POWer<x>:CLRESPONSE:INPUTSOurce CH<x>
    - POWer:POWer<x>:CLRESPONSE:INPUTSOurce?
    - POWer:POWer<x>:CLRESPONSE:MON {SAVG|SSEQ}
    - POWer:POWer<x>:CLRESPONSE:MON?
    - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce CH<x>
    - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?
    - POWer:POWer<x>:CLRESPONSE:PPD <NR3>
    - POWer:POWer<x>:CLRESPONSE:PPD?
    - POWer:POWer<x>:CLRESPONSE:STARTFREQuency <NR3>
    - POWer:POWer<x>:CLRESPONSE:STARTFREQuency?
    - POWer:POWer<x>:CLRESPONSE:STOPFREQuency <NR3>
    - POWer:POWer<x>:CLRESPONSE:STOPFREQuency?
    - POWer:POWer<x>:CLRESPONSE:TESTCONNection EXECute
    - POWer:POWer<x>:CYCLEAmp:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:CYCLEAmp:INPUTSOurce?
    - POWer:POWer<x>:CYCLEBase:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:CYCLEBase:INPUTSOurce?
    - POWer:POWer<x>:CYCLEMAX:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:CYCLEMAX:INPUTSOurce?
    - POWer:POWer<x>:CYCLEMin:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:CYCLEMin:INPUTSOurce?
    - POWer:POWer<x>:CYCLEPKPK:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:CYCLEPKPK:INPUTSOurce?
    - POWer:POWer<x>:CYCLETop:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:CYCLETop:INPUTSOurce?
    - POWer:POWer<x>:DIDT:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:DIDT:INPUTSOurce?
    - POWer:POWer<x>:DIDT:SOURCEEDGEType {RISE|FALL}
    - POWer:POWer<x>:DIDT:SOURCEEDGEType?
    - POWer:POWer<x>:DVDT:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:DVDT:INPUTSOurce?
    - POWer:POWer<x>:DVDT:SOURCEEDGEType {RISE|FALL}
    - POWer:POWer<x>:DVDT:SOURCEEDGEType?
    - POWer:POWer<x>:EFFICIENCY:INPUTType {AC|DC}
    - POWer:POWer<x>:EFFICIENCY:INPUTType?
    - POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce?
    - POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce?
    - POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce?
    - POWer:POWer<x>:EFFICIENCY:ISOUrce
    - POWer:POWer<x>:EFFICIENCY:ISOUrce?
    - POWer:POWer<x>:EFFICIENCY:NUMOFOutputs {ONE|TWO|THREE}
    - POWer:POWer<x>:EFFICIENCY:NUMOFOutputs?
    - POWer:POWer<x>:EFFICIENCY:OUTPUT1Type {AC|DC}
    - POWer:POWer<x>:EFFICIENCY:OUTPUT1Type?
    - POWer:POWer<x>:EFFICIENCY:OUTPUT2Type {AC|DC}
    - POWer:POWer<x>:EFFICIENCY:OUTPUT2Type?
    - POWer:POWer<x>:EFFICIENCY:OUTPUT3Type {AC|DC}
    - POWer:POWer<x>:EFFICIENCY:OUTPUT3Type?
    - POWer:POWer<x>:EFFICIENCY:OUTPUTType {AC|DC}
    - POWer:POWer<x>:EFFICIENCY:OUTPUTType?
    - POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce?
    - POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce?
    - POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce?
    - POWer:POWer<x>:EFFICIENCY:VSOUrce
    - POWer:POWer<x>:EFFICIENCY:VSOUrce?
    - POWer:POWer<x>:FREQUENCY:EDGe {RISE|FALL}
    - POWer:POWer<x>:FREQUENCY:EDGe?
    - POWer:POWer<x>:FREQUENCY:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:FREQUENCY:INPUTSOurce?
    - POWer:POWer<x>:GATing {NONE|CURSOR|SCREEN|LOGIC}
    - POWer:POWer<x>:GATing:GLOBal {ON|OFF|1|0}
    - POWer:POWer<x>:GATing:GLOBal?
    - POWer:POWer<x>:GATing?
    - POWer:POWer<x>:HARMONICS:CLASs {CLASSA|CLASSB|CLASSC|CLASSD}
    - POWer:POWer<x>:HARMONICS:CLASs?
    - POWer:POWer<x>:HARMONICS:CLFile <QString>
    - POWer:POWer<x>:HARMONICS:CLFile?
    - POWer:POWer<x>:HARMONICS:CMEThod {RATed|MEASured}
    - POWer:POWer<x>:HARMONICS:CMEThod?
    - POWer:POWer<x>:HARMONICS:FUNDCURRent <NR1>
    - POWer:POWer<x>:HARMONICS:FUNDCURRent?
    - POWer:POWer<x>:HARMONICS:HORDer <NR1>
    - POWer:POWer<x>:HARMONICS:HORDer?
    - POWer:POWer<x>:HARMONICS:HSOURce {CURRent|VOLTage}
    - POWer:POWer<x>:HARMONICS:HSOURce?
    - POWer:POWer<x>:HARMONICS:IPOWer <NR1>
    - POWer:POWer<x>:HARMONICS:IPOWer?
    - POWer:POWer<x>:HARMONICS:ISOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:HARMONICS:ISOURce?
    - POWer:POWer<x>:HARMONICS:LINEFREQUEncy {Auto|FIFTyhz|SIXTyhz |THREESIXTyhz|FOURHUNDREdhz|SIXFIFTyhz|EIGHTHUNDREdhz|CUSTom
    - POWer:POWer<x>:HARMONICS:LINEFREQUEncy?
    - POWer:POWer<x>:HARMONICS:ODDEVen {ALL|ODD|EVEN}
    - POWer:POWer<x>:HARMONICS:ODDEVen?
    - POWer:POWer<x>:HARMONICS:PFACtor <NR1>
    - POWer:POWer<x>:HARMONICS:PFACtor?
    - POWer:POWer<x>:HARMONICS:POWERRating {HIGH|LOW}
    - POWer:POWer<x>:HARMONICS:POWERRating?
    - POWer:POWer<x>:HARMONICS:RCURRent <NR1>
    - POWer:POWer<x>:HARMONICS:RCURRent?
    - POWer:POWer<x>:HARMONICS:STANDard {NONe|IEC|MIL|AM14|DO160|CUSTOM}
    - POWer:POWer<x>:HARMONICS:STANDard?
    - POWer:POWer<x>:HARMONICS:STARTFREQUEncy <NR2>
    - POWer:POWer<x>:HARMONICS:STARTFREQUEncy?
    - POWer:POWer<x>:HARMONICS:UNITs {LOG|LINear}
    - POWer:POWer<x>:HARMONICS:UNITs?
    - POWer:POWer<x>:HARMONICS:VSOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:HARMONICS:VSOURce?
    - POWer:POWer<x>:IMPEDANCE:AMP<x>Val <NR3>
    - POWer:POWer<x>:IMPEDANCE:AMP<x>Val?
    - POWer:POWer<x>:IMPEDANCE:AMPMode {CONSTant|PROFile}
    - POWer:POWer<x>:IMPEDANCE:AMPMode?
    - POWer:POWer<x>:IMPEDANCE:ANALYSISMethod {SV|FFT}
    - POWer:POWer<x>:IMPEDANCE:ANALYSISMethod?
    - POWer:POWer<x>:IMPEDANCE:AUTORbw {True|False}
    - POWer:POWer<x>:IMPEDANCE:AUTORbw?
    - POWer:POWer<x>:IMPEDANCE:CONNECTSTATus?
    - POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude <NR3>
    - POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude?
    - POWer:POWer<x>:IMPEDANCE:FREQ<x>Val <NR3>
    - POWer:POWer<x>:IMPEDANCE:FREQ<x>Val?
    - POWer:POWer<x>:IMPEDANCE:GENIPADDress <String>
    - POWer:POWer<x>:IMPEDANCE:GENIPADDress?
    - POWer:POWer<x>:IMPEDANCE:GENerator {INTernal|EXTernal}
    - POWer:POWer<x>:IMPEDANCE:GENerator?
    - POWer:POWer<x>:IMPEDANCE:IMPEDANCE {FIFTy|HIGHZ}
    - POWer:POWer<x>:IMPEDANCE:IMPEDANCE?
    - POWer:POWer<x>:IMPEDANCE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:IMPEDANCE:INPUTSOurce?
    - POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce?
    - POWer:POWer<x>:IMPEDANCE:PPD <NR1>
    - POWer:POWer<x>:IMPEDANCE:PPD?
    - POWer:POWer<x>:IMPEDANCE:STARTFREQuency <NR3>
    - POWer:POWer<x>:IMPEDANCE:STARTFREQuency?
    - POWer:POWer<x>:IMPEDANCE:STOPFREQuency <NR3>
    - POWer:POWer<x>:IMPEDANCE:STOPFREQuency?
    - POWer:POWer<x>:IMPEDANCE:TESTCONNection {EXECute}
    - POWer:POWer<x>:INDUCTANCE:EDGESource {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:INDUCTANCE:EDGESource?
    - POWer:POWer<x>:INDUCTANCE:ISOUrce
    - POWer:POWer<x>:INDUCTANCE:ISOUrce?
    - POWer:POWer<x>:INDUCTANCE:VSOURce
    - POWer:POWer<x>:INDUCTANCE:VSOURce?
    - POWer:POWer<x>:INPUTCAP:ISOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:INPUTCAP:ISOURce?
    - POWer:POWer<x>:INPUTCAP:PEAKCURRent <NR3>
    - POWer:POWer<x>:INPUTCAP:PEAKCURRent?
    - POWer:POWer<x>:INPUTCAP:PEAKVOLTage <NR3>
    - POWer:POWer<x>:INPUTCAP:PEAKVOLTage?
    - POWer:POWer<x>:INPUTCAP:VSOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:INPUTCAP:VSOURce?
    - POWer:POWer<x>:INRUSHcurrent:INPUTSOurce
    - POWer:POWer<x>:INRUSHcurrent:INPUTSOurce?
    - POWer:POWer<x>:INRUSHcurrent:PEAKCURRent <NR3>
    - POWer:POWer<x>:INRUSHcurrent:PEAKCURRent?
    - POWer:POWer<x>:IVSINTEGRALV:ISOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:IVSINTEGRALV:ISOURce?
    - POWer:POWer<x>:IVSINTEGRALV:VSOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:IVSINTEGRALV:VSOURce?
    - POWer:POWer<x>:LABel <QString>
    - POWer:POWer<x>:LABel?
    - POWer:POWer<x>:LINERIPPLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:LINERIPPLE:INPUTSOurce?
    - POWer:POWer<x>:LINERIPPLE:LFREQuency {FIFty|SIXty|FOURHundred}
    - POWer:POWer<x>:LINERIPPLE:LFREQuency?
    - POWer:POWer<x>:MAGNETICLOSS:ISOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:MAGNETICLOSS:ISOURce?
    - POWer:POWer<x>:MAGNETICLOSS:VSOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:MAGNETICLOSS:VSOURce?
    - POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection <NR2>
    - POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection?
    - POWer:POWer<x>:MAGPROPERTY:EDGESOURce {Current|VOLTAGE}
    - POWer:POWer<x>:MAGPROPERTY:EDGESOURce?
    - POWer:POWer<x>:MAGPROPERTY:ISOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:MAGPROPERTY:ISOURce?
    - POWer:POWer<x>:MAGPROPERTY:LENgth <NR2>
    - POWer:POWer<x>:MAGPROPERTY:LENgth?
    - POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs <NR1>
    - POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs?
    - POWer:POWer<x>:MAGPROPERTY:SEC1SOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:MAGPROPERTY:SEC1SOURce?
    - POWer:POWer<x>:MAGPROPERTY:SEC1TURNs <NR1>
    - POWer:POWer<x>:MAGPROPERTY:SEC1TURNs?
    - POWer:POWer<x>:MAGPROPERTY:SEC2SOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:MAGPROPERTY:SEC2SOURce?
    - POWer:POWer<x>:MAGPROPERTY:SEC2TURNs <NR1>
    - POWer:POWer<x>:MAGPROPERTY:SEC2TURNs?
    - POWer:POWer<x>:MAGPROPERTY:SEC3SOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:MAGPROPERTY:SEC3SOURce?
    - POWer:POWer<x>:MAGPROPERTY:SEC3TURNs <NR1>
    - POWer:POWer<x>:MAGPROPERTY:SEC3TURNs?
    - POWer:POWer<x>:MAGPROPERTY:SEC4SOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:MAGPROPERTY:SEC4SOURce?
    - POWer:POWer<x>:MAGPROPERTY:SEC4TURNs <NR1>
    - POWer:POWer<x>:MAGPROPERTY:SEC4TURNs?
    - POWer:POWer<x>:MAGPROPERTY:SEC5SOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:MAGPROPERTY:SEC5SOURce?
    - POWer:POWer<x>:MAGPROPERTY:SEC5TURNs <NR1>
    - POWer:POWer<x>:MAGPROPERTY:SEC5TURNs?
    - POWer:POWer<x>:MAGPROPERTY:SEC6SOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:MAGPROPERTY:SEC6SOURce?
    - POWer:POWer<x>:MAGPROPERTY:SEC6TURNs <NR1>
    - POWer:POWer<x>:MAGPROPERTY:SEC6TURNs?
    - POWer:POWer<x>:MAGPROPERTY:SECPhase <NR3>
    - POWer:POWer<x>:MAGPROPERTY:SECPhase?
    - POWer:POWer<x>:MAGPROPERTY:SECVolt {True|False}
    - POWer:POWer<x>:MAGPROPERTY:SECVolt?
    - POWer:POWer<x>:MAGPROPERTY:SECWINDings {None|ONE|TWO|THREE|FOUR|FIVE|SIX}
    - POWer:POWer<x>:MAGPROPERTY:SECWINDings?
    - POWer:POWer<x>:MAGPROPERTY:UNITs {SI|CGS}
    - POWer:POWer<x>:MAGPROPERTY:UNITs?
    - POWer:POWer<x>:MAGPROPERTY:VSOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:MAGPROPERTY:VSOURce?
    - POWer:POWer<x>:NDUTYCYCLE:EDGEType {RISE|FALL|BOTH}
    - POWer:POWer<x>:NDUTYCYCLE:EDGEType?
    - POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce?
    - POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce?
    - POWer:POWer<x>:PDUTYCYCLE:EDGEType {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:PDUTYCYCLE:EDGEType?
    - POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce?
    - POWer:POWer<x>:PERIOD:EDGe {RISE|FALL}
    - POWer:POWer<x>:PERIOD:EDGe?
    - POWer:POWer<x>:PERIOD:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:PERIOD:INPUTSOurce?
    - POWer:POWer<x>:POWERQUALITY:CCYCles {ON|OFF|1|0}
    - POWer:POWer<x>:POWERQUALITY:CCYCles?
    - POWer:POWer<x>:POWERQUALITY:FREFerence {VOLTage|CURRent}
    - POWer:POWer<x>:POWERQUALITY:FREFerence?
    - POWer:POWer<x>:POWERQUALITY:ISOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:POWERQUALITY:ISOURce?
    - POWer:POWer<x>:POWERQUALITY:STYPe {AC|DC}
    - POWer:POWer<x>:POWERQUALITY:STYPe?
    - POWer:POWer<x>:POWERQUALITY:VSOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:POWERQUALITY:VSOURce?
    - POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce?
    - POWer:POWer<x>:PRESET {EXECute}
    - POWer:POWer<x>:PSRR:AMP<x>Val <NR3>
    - POWer:POWer<x>:PSRR:AMP<x>Val?
    - POWer:POWer<x>:PSRR:AMPMode {CONSTant|PROFile}
    - POWer:POWer<x>:PSRR:AMPMode?
    - POWer:POWer<x>:PSRR:ANALYSISMethod {SV|FFT}
    - POWer:POWer<x>:PSRR:ANALYSISMethod?
    - POWer:POWer<x>:PSRR:AUTORbw {True|False}
    - POWer:POWer<x>:PSRR:AUTORbw?
    - POWer:POWer<x>:PSRR:CONNECTSTATus?
    - POWer:POWer<x>:PSRR:CONSTAMPlitude <NR3>
    - POWer:POWer<x>:PSRR:CONSTAMPlitude?
    - POWer:POWer<x>:PSRR:FREQ<x>Val <NR3>
    - POWer:POWer<x>:PSRR:FREQ<x>Val?
    - POWer:POWer<x>:PSRR:GENIPADDress <Qstring>
    - POWer:POWer<x>:PSRR:GENIPADDress?
    - POWer:POWer<x>:PSRR:GENerator {INTernal|EXTernal}
    - POWer:POWer<x>:PSRR:GENerator?
    - POWer:POWer<x>:PSRR:IMPEDance {FIFTy|HIGHZ}
    - POWer:POWer<x>:PSRR:IMPEDance?
    - POWer:POWer<x>:PSRR:INPUTSOurce CH<x>
    - POWer:POWer<x>:PSRR:INPUTSOurce?
    - POWer:POWer<x>:PSRR:OUTPUTSOurce CH<x>
    - POWer:POWer<x>:PSRR:OUTPUTSOurce?
    - POWer:POWer<x>:PSRR:PPD <NR3>
    - POWer:POWer<x>:PSRR:PPD?
    - POWer:POWer<x>:PSRR:STARTFREQuency <NR3>
    - POWer:POWer<x>:PSRR:STARTFREQuency?
    - POWer:POWer<x>:PSRR:STOPFREQuency <NR3>
    - POWer:POWer<x>:PSRR:STOPFREQuency?
    - POWer:POWer<x>:PSRR:TESTCONNection {EXECute}
    - POWer:POWer<x>:RDSON:DEVICEType {SWITCHING|PNJUNCTION}
    - POWer:POWer<x>:RDSON:DEVICEType?
    - POWer:POWer<x>:RDSON:ISOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:RDSON:ISOURce?
    - POWer:POWer<x>:RDSON:VSOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:RDSON:VSOURce?
    - POWer:POWer<x>:REFLevels:ABSolute:FALLHigh <NR1>
    - POWer:POWer<x>:REFLevels:ABSolute:FALLHigh?
    - POWer:POWer<x>:REFLevels:ABSolute:FALLLow <NR1>
    - POWer:POWer<x>:REFLevels:ABSolute:FALLLow?
    - POWer:POWer<x>:REFLevels:ABSolute:FALLMid <NR1>
    - POWer:POWer<x>:REFLevels:ABSolute:FALLMid?
    - POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis <NR1>
    - POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis?
    - POWer:POWer<x>:REFLevels:ABSolute:RISEHigh <NR1>
    - POWer:POWer<x>:REFLevels:ABSolute:RISEHigh?
    - POWer:POWer<x>:REFLevels:ABSolute:RISELow <NR1>
    - POWer:POWer<x>:REFLevels:ABSolute:RISELow?
    - POWer:POWer<x>:REFLevels:ABSolute:RISEMid <NR1>
    - POWer:POWer<x>:REFLevels:ABSolute:RISEMid?
    - POWer:POWer<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
    - POWer:POWer<x>:REFLevels:ABSolute:TYPE?
    - POWer:POWer<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
    - POWer:POWer<x>:REFLevels:BASETop?
    - POWer:POWer<x>:REFLevels:METHod {PERCent|ABSolute}
    - POWer:POWer<x>:REFLevels:METHod?
    - POWer:POWer<x>:REFLevels:PERCent:FALLHigh <NR1>
    - POWer:POWer<x>:REFLevels:PERCent:FALLHigh?
    - POWer:POWer<x>:REFLevels:PERCent:FALLLow <NR1>
    - POWer:POWer<x>:REFLevels:PERCent:FALLLow?
    - POWer:POWer<x>:REFLevels:PERCent:FALLMid <NR1>
    - POWer:POWer<x>:REFLevels:PERCent:FALLMid?
    - POWer:POWer<x>:REFLevels:PERCent:HYSTeresis <NR1>
    - POWer:POWer<x>:REFLevels:PERCent:HYSTeresis?
    - POWer:POWer<x>:REFLevels:PERCent:RISEHigh <NR1>
    - POWer:POWer<x>:REFLevels:PERCent:RISEHigh?
    - POWer:POWer<x>:REFLevels:PERCent:RISELow <NR1>
    - POWer:POWer<x>:REFLevels:PERCent:RISELow?
    - POWer:POWer<x>:REFLevels:PERCent:RISEMid <NR1>
    - POWer:POWer<x>:REFLevels:PERCent:RISEMid?
    - POWer:POWer<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
    - POWer:POWer<x>:REFLevels:PERCent:TYPE?
    - POWer:POWer<x>:RESUlts:ALLAcqs:MAXimum? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability| RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR|PHASE| PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG| TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL| PKPK|HIGH|LOW|MAX|MIN| INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:ALLAcqs:MEAN? {InputPwr|Output1Pwr|Output2Pwr| Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency| INDUCT|IVSINTV|MAGLOSS|Bpeak|Br|Hc|Hmax| IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ| ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG| TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL| PKPK|HIGH|LOW|MAX|MIN| INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:ALLAcqs:MINimum? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS| Bpeak|Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR| PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR| IRMS|VRMS|TONENRG|TONLOSS|TOFFENRG| TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS|TTLENRG| DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY| NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:ALLAcqs:PK2PK? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR| PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR| IRMS|VRMS|TONENRG|TONLOSS|TOFFENRG| TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS|TTLENRG| DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY| NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:ALLAcqs:POPUlation? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR| PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS| TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE| AMPL|PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:ALLAcqs:STDDev? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br|Hc| Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS| TRUEPWR|APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ| ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG|TONLOSS| TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS| TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS| LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY| NDUTY|PPULSE|NPULSE|AMPL|PKPK|HIGH|LOW|MAX|MIN| INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:CURRentacq:F1MAG? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:F3MAG? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:FREQUENCY? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:IRMS? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS| Bpeak|Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR| PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS| TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:CURRentacq:MEAN? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS| VRMS|TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE| AMPL|PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:CURRentacq:MINimum? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br| Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS| VRMS|TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL| PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:CURRentacq:PK2PK? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br| Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR|APPPWR| REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS| TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS| TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK|SWRIPRMS| SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:CURRentacq:POHCL? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:POHCM? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:POHCS? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:POPUlation? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br| Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS| VRMS|TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE| AMPL|PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:CURRentacq:RMS? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:STATUS? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:STDDev? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br|Hc|Hmax|IRipple| DeltaB|DeltaH|Permeability|RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR| PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG|TONLOSS| TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS|TTLENRG|DVBYDT| DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL|PKPK|HIGH|LOW|MAX|MIN |INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
    - POWer:POWer<x>:RESUlts:CURRentacq:THDF? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:THDR? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:TRPWR? 'harmonics'
    - POWer:POWer<x>:RESUlts:CURRentacq:VRMS? 'harmonics'
    - POWer:POWer<x>:SEQSETup Execute
    - POWer:POWer<x>:SEQuence {RUN|RERUN}
    - POWer:POWer<x>:SEQuence?
    - POWer:POWer<x>:SOA:ISOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:SOA:ISOURce?
    - POWer:POWer<x>:SOA:POINT<x> <NR1>
    - POWer:POWer<x>:SOA:POINT<x>?
    - POWer:POWer<x>:SOA:RECAllmask
    - POWer:POWer<x>:SOA:RECAllmask:FILEName
    - POWer:POWer<x>:SOA:RECAllmask:FILEName?
    - POWer:POWer<x>:SOA:RECAllmask?
    - POWer:POWer<x>:SOA:SAVemask
    - POWer:POWer<x>:SOA:SAVemask:AUTOINCrement
    - POWer:POWer<x>:SOA:SAVemask:AUTOINCrement?
    - POWer:POWer<x>:SOA:SAVemask:FILEName
    - POWer:POWer<x>:SOA:SAVemask:FILEName?
    - POWer:POWer<x>:SOA:SAVemask:FOLDer
    - POWer:POWer<x>:SOA:SAVemask:FOLDer?
    - POWer:POWer<x>:SOA:SAVemask?
    - POWer:POWer<x>:SOA:VSOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:SOA:VSOURce?
    - POWer:POWer<x>:SWITCHINGLOSS:DEVICEType {MOSFET|BJT}
    - POWer:POWer<x>:SWITCHINGLOSS:DEVICEType?
    - POWer:POWer<x>:SWITCHINGLOSS:GATESOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:SWITCHINGLOSS:GATESOurce?
    - POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs <NR1>
    - POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs?
    - POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct <NR1>
    - POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct?
    - POWer:POWer<x>:SWITCHINGLOSS:ISOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:SWITCHINGLOSS:ISOURce?
    - POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts {PERCent|ABSolute}
    - POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts?
    - POWer:POWer<x>:SWITCHINGLOSS:RDSOn <NR1>
    - POWer:POWer<x>:SWITCHINGLOSS:RDSOn?
    - POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType {SMPS|PFC|FLYBACK}
    - POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType?
    - POWer:POWer<x>:SWITCHINGLOSS:VCESat <NR1>
    - POWer:POWer<x>:SWITCHINGLOSS:VCESat?
    - POWer:POWer<x>:SWITCHINGLOSS:VGLevel <NR1>
    - POWer:POWer<x>:SWITCHINGLOSS:VGLevel?
    - POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs <NR1>
    - POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs?
    - POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct <NR1>
    - POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct?
    - POWer:POWer<x>:SWITCHINGLOSS:VSOURce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:SWITCHINGLOSS:VSOURce?
    - POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
    - POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce?
    - POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency <NR1>
    - POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency?
    - POWer:POWer<x>:TURNOFFtime:FREQuency <NR3>
    - POWer:POWer<x>:TURNOFFtime:FREQuency?
    - POWer:POWer<x>:TURNOFFtime:INPUTLEVel <NR3>
    - POWer:POWer<x>:TURNOFFtime:INPUTLEVel?
    - POWer:POWer<x>:TURNOFFtime:INPUTSOurce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNOFFtime:INPUTSOurce?
    - POWer:POWer<x>:TURNOFFtime:MAXTIMe <NR3>
    - POWer:POWer<x>:TURNOFFtime:MAXTIMe?
    - POWer:POWer<x>:TURNOFFtime:MAXVoltage <NR3>
    - POWer:POWer<x>:TURNOFFtime:MAXVoltage?
    - POWer:POWer<x>:TURNOFFtime:NUMOUTputs {ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN}
    - POWer:POWer<x>:TURNOFFtime:NUMOUTputs?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage <NR2>
    - POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage <NR2>
    - POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage <NR2>
    - POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage <NR2>
    - POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage <NR2>
    - POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage <NR2>
    - POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce?
    - POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage <NR2>
    - POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage?
    - POWer:POWer<x>:TURNOFFtime:TYPE {DCDC|ACDC}
    - POWer:POWer<x>:TURNOFFtime:TYPE?
    - POWer:POWer<x>:TURNONtime:FREQuency <NR3>
    - POWer:POWer<x>:TURNONtime:FREQuency?
    - POWer:POWer<x>:TURNONtime:INPUTLEVel <NR3>
    - POWer:POWer<x>:TURNONtime:INPUTLEVel?
    - POWer:POWer<x>:TURNONtime:INPUTSOurce
    - POWer:POWer<x>:TURNONtime:INPUTSOurce?
    - POWer:POWer<x>:TURNONtime:MAXTIMe <NR3>
    - POWer:POWer<x>:TURNONtime:MAXTIMe?
    - POWer:POWer<x>:TURNONtime:MAXVoltage <NR3>
    - POWer:POWer<x>:TURNONtime:MAXVoltage?
    - POWer:POWer<x>:TURNONtime:NUMOUTputs {ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN}
    - POWer:POWer<x>:TURNONtime:NUMOUTputs?
    - POWer:POWer<x>:TURNONtime:OUTPUT1SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNONtime:OUTPUT1SOURce?
    - POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage <NR2>
    - POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage?
    - POWer:POWer<x>:TURNONtime:OUTPUT2SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNONtime:OUTPUT2SOURce?
    - POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage <NR2>
    - POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage?
    - POWer:POWer<x>:TURNONtime:OUTPUT3SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNONtime:OUTPUT3SOURce?
    - POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage <NR2>
    - POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage?
    - POWer:POWer<x>:TURNONtime:OUTPUT4SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNONtime:OUTPUT4SOURce?
    - POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage <NR2>
    - POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage?
    - POWer:POWer<x>:TURNONtime:OUTPUT5SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNONtime:OUTPUT5SOURce?
    - POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage <NR2>
    - POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage?
    - POWer:POWer<x>:TURNONtime:OUTPUT6SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNONtime:OUTPUT6SOURce?
    - POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage <NR2>
    - POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage?
    - POWer:POWer<x>:TURNONtime:OUTPUT7SOURce {CH<x>|REF<x>|MATH<x>}
    - POWer:POWer<x>:TURNONtime:OUTPUT7SOURce?
    - POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage <NR2>
    - POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage?
    - POWer:POWer<x>:TURNONtime:TYPE {DCDC|ACDC}
    - POWer:POWer<x>:TURNONtime:TYPE?
    - POWer:POWer<x>:TYPe <Measurement Type>
    - POWer:POWer<x>:TYPe?
    - POWer:POWer<x>:WRAP:DEGrees NR3
    - POWer:POWer<x>:WRAP:DEGrees?
    - POWer:POWer<x>:WRAP:STATE {ON|OFF}
    - POWer:POWer<x>:WRAP:STATE?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdReadWithArguments,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class PowerPowerItemWrapState(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:WRAP:STATE`` command.

    Description:
        - This command sets or returns the phase wrap status for FRA measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:WRAP:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:WRAP:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:WRAP:STATE value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:WRAP:STATE {ON|OFF}
        - POWer:POWer<x>:WRAP:STATE?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``ON`` specifies that phase wrap has been turned on for FRA measurements.
        - ``OFF`` specifies that phase wrap has been turned off for FRA measurements.
    """


class PowerPowerItemWrapDegrees(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:WRAP:DEGrees`` command.

    Description:
        - This command sets or returns the phase wrap value for FRA measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:WRAP:DEGrees?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:WRAP:DEGrees?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:WRAP:DEGrees value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:WRAP:DEGrees NR3
        - POWer:POWer<x>:WRAP:DEGrees?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``NR3`` specifies the phase wrap value for FRA measurements.
    """


class PowerPowerItemWrap(SCPICmdRead):
    """The ``POWer:POWer<x>:WRAP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:WRAP?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:WRAP?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.degrees``: The ``POWer:POWer<x>:WRAP:DEGrees`` command.
        - ``.state``: The ``POWer:POWer<x>:WRAP:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._degrees = PowerPowerItemWrapDegrees(device, f"{self._cmd_syntax}:DEGrees")
        self._state = PowerPowerItemWrapState(device, f"{self._cmd_syntax}:STATE")

    @property
    def degrees(self) -> PowerPowerItemWrapDegrees:
        """Return the ``POWer:POWer<x>:WRAP:DEGrees`` command.

        Description:
            - This command sets or returns the phase wrap value for FRA measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:WRAP:DEGrees?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:WRAP:DEGrees?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:WRAP:DEGrees value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:WRAP:DEGrees NR3
            - POWer:POWer<x>:WRAP:DEGrees?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``NR3`` specifies the phase wrap value for FRA measurements.
        """
        return self._degrees

    @property
    def state(self) -> PowerPowerItemWrapState:
        """Return the ``POWer:POWer<x>:WRAP:STATE`` command.

        Description:
            - This command sets or returns the phase wrap status for FRA measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:WRAP:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:WRAP:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:WRAP:STATE value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:WRAP:STATE {ON|OFF}
            - POWer:POWer<x>:WRAP:STATE?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``ON`` specifies that phase wrap has been turned on for FRA measurements.
            - ``OFF`` specifies that phase wrap has been turned off for FRA measurements.
        """
        return self._state


class PowerPowerItemType(SCPICmdWrite, SCPICmdRead):
    r"""The ``POWer:POWer<x>:TYPe`` command.

    Description:
        - This command sets or queries the measurement type of the specified power measurement
          number. If the measurement number does not exist, this command creates a new power
          measurement, assigns the specified measurement number to the new measurement, and then
          assigns the measurement type to the new measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:TYPe value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TYPe <Measurement Type>
        - POWer:POWer<x>:TYPe?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<Measurement Type>`` = CYCLEAmp \| CYCLEBase \| CYCLEMAx \| CYCLEMIn \| CYCLEPKpk \|
          CYCLETop \| DIDT \| DVDT \| EFFICIENCY \| FREQuency \| HARMonics \|IMPEDANCE\| INDUCTANCE
          \| INPUTCAP \| INRUSHcurrent\| \| IVSINTEGRALV \| LINERIpple \| MAGNETICLOSS \|
          MAGPROPERTY \| NDUTYCycle \| NPULSEWidth \| PDUTYCycle \| PERIod \| POWERQUALity \|
          PPULSEWidth \| RDSON \| SOA \| SWITCHINGLOss \| SWITCHINGRIpple \| TURNOFFtime \|
          TURNONtime\| CLRESPONSE \| PSRR.
    """


class PowerPowerItemTurnontimeType(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:TYPE`` command.

    Description:
        - This command sets or queries the type of AC/DC converter used in the specified Turn On
          Time power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TURNONtime:TYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:TURNONtime:TYPE value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:TYPE {DCDC|ACDC}
        - POWer:POWer<x>:TURNONtime:TYPE?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``DCDC`` sets the measurement to use a DC to DC converter.
        - ``ACDC`` sets the measurement to use an AC to DC converter.
    """


class PowerPowerItemTurnontimeOutput7voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage`` command.

    Description:
        - This command sets or queries the output 7 voltage level of the specified Turn On Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage <NR2>
        - POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnontimeOutput7source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT7SOURce`` command.

    Description:
        - This command sets or queries the output 7 source of the specified Turn On Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT7SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT7SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT7SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT7SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNONtime:OUTPUT7SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnontimeOutput6voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage`` command.

    Description:
        - This command sets or queries the output 6 voltage level of the specified Turn On Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage <NR2>
        - POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnontimeOutput6source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT6SOURce`` command.

    Description:
        - This command sets or queries the output 6 source of the specified Turn On Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT6SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT6SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT6SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT6SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNONtime:OUTPUT6SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnontimeOutput5voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage`` command.

    Description:
        - This command sets or queries the output 5 voltage level of the specified Turn On Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage <NR2>
        - POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnontimeOutput5source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT5SOURce`` command.

    Description:
        - This command sets or queries the output 5 source of the specified Turn On Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT5SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT5SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT5SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT5SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNONtime:OUTPUT5SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnontimeOutput4voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage`` command.

    Description:
        - This command sets or queries the output 4 voltage level of the specified Turn On Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage <NR2>
        - POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnontimeOutput4source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT4SOURce`` command.

    Description:
        - This command sets or queries the output 4 source of the specified Turn On Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT4SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT4SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT4SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT4SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNONtime:OUTPUT4SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnontimeOutput3voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage`` command.

    Description:
        - This command sets or queries the output 3 voltage level of the specified Turn On Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage <NR2>
        - POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnontimeOutput3source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT3SOURce`` command.

    Description:
        - This command sets or queries the output 3 source of the specified Turn On Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT3SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT3SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT3SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT3SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNONtime:OUTPUT3SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnontimeOutput2voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage`` command.

    Description:
        - This command sets or queries the output 2 voltage level of the specified Turn On Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage <NR2>
        - POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnontimeOutput2source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT2SOURce`` command.

    Description:
        - This command sets or queries the output 2 source of the specified Turn On Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT2SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT2SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT2SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT2SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNONtime:OUTPUT2SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnontimeOutput1voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage`` command.

    Description:
        - This command sets or queries the output 1 voltage level of the specified Turn On Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage <NR2>
        - POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnontimeOutput1source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:OUTPUT1SOURce`` command.

    Description:
        - This command sets or queries the output 1 source of the specified Turn On Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:OUTPUT1SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT1SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:OUTPUT1SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:OUTPUT1SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNONtime:OUTPUT1SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnontimeNumoutputs(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:NUMOUTputs`` command.

    Description:
        - This command sets or queries the number of outputs for the specified Turn On Time power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:NUMOUTputs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:NUMOUTputs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:NUMOUTputs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:NUMOUTputs {ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN}
        - POWer:POWer<x>:TURNONtime:NUMOUTputs?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``ONE`` through SEVEN sets the number of outputs for the specified Turn On Time power
          measurement.
    """


class PowerPowerItemTurnontimeMaxvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:MAXVoltage`` command.

    Description:
        - This command sets or returns the maximum voltage setting of the specified Turn On Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:MAXVoltage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:MAXVoltage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:MAXVoltage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:MAXVoltage <NR3>
        - POWer:POWer<x>:TURNONtime:MAXVoltage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR3>`` is a floating point number that represents the maximum voltage in the range 1 V
          to 500 V.
    """


class PowerPowerItemTurnontimeMaxtime(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:MAXTIMe`` command.

    Description:
        - This command sets or returns the maximum turn on time of the specified Turn On Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:MAXTIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TURNONtime:MAXTIMe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:MAXTIMe value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:MAXTIMe <NR3>
        - POWer:POWer<x>:TURNONtime:MAXTIMe?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR3>`` is a floating point number that represents the maximum time value, in seconds,
          in the range 1 second to 500 seconds.
    """


class PowerPowerItemTurnontimeInputsource(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source of the specified Turn On Time measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:TURNONtime:INPUTSOurce``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:INPUTSOurce
        - POWer:POWer<x>:TURNONtime:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` is the channel specifier in the range of 1 through 8 and is limited by the
          number of instrument input channels.
        - ``REF<x>`` is the Reference waveform specifier ≥1. This is the equivalent of the number
          shown on a Reference waveform badge in the UI.
        - ``MATH<x>`` is the Math waveform specifier ≥1. This is the equivalent of the number shown
          on a Math waveform badge in the UI.
    """


class PowerPowerItemTurnontimeInputlevel(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:INPUTLEVel`` command.

    Description:
        - This command sets or returns the input voltage level of the specified Turn On Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:INPUTLEVel?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:INPUTLEVel?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:INPUTLEVel value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:INPUTLEVel <NR3>
        - POWer:POWer<x>:TURNONtime:INPUTLEVel?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR3>`` is a floating point number that represents the voltage level, in volts, from
          -500 V to 500 V.
    """


class PowerPowerItemTurnontimeFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime:FREQuency`` command.

    Description:
        - This command sets or queries the input frequency used by the AC or DC converter of the
          specified Turn On Time measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:FREQuency?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TURNONtime:FREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNONtime:FREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNONtime:FREQuency <NR3>
        - POWer:POWer<x>:TURNONtime:FREQuency?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR3>`` is a floating point number that represents the frequency, in Hertz, from 1 Hz to
          500 Hz.
    """


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class PowerPowerItemTurnontime(SCPICmdRead):
    """The ``POWer:POWer<x>:TURNONtime`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TURNONtime?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``POWer:POWer<x>:TURNONtime:FREQuency`` command.
        - ``.inputlevel``: The ``POWer:POWer<x>:TURNONtime:INPUTLEVel`` command.
        - ``.inputsource``: The ``POWer:POWer<x>:TURNONtime:INPUTSOurce`` command.
        - ``.maxtime``: The ``POWer:POWer<x>:TURNONtime:MAXTIMe`` command.
        - ``.maxvoltage``: The ``POWer:POWer<x>:TURNONtime:MAXVoltage`` command.
        - ``.numoutputs``: The ``POWer:POWer<x>:TURNONtime:NUMOUTputs`` command.
        - ``.output1source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT1SOURce`` command.
        - ``.output1voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage`` command.
        - ``.output2source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT2SOURce`` command.
        - ``.output2voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage`` command.
        - ``.output3source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT3SOURce`` command.
        - ``.output3voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage`` command.
        - ``.output4source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT4SOURce`` command.
        - ``.output4voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage`` command.
        - ``.output5source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT5SOURce`` command.
        - ``.output5voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage`` command.
        - ``.output6source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT6SOURce`` command.
        - ``.output6voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage`` command.
        - ``.output7source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT7SOURce`` command.
        - ``.output7voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage`` command.
        - ``.type``: The ``POWer:POWer<x>:TURNONtime:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = PowerPowerItemTurnontimeFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._inputlevel = PowerPowerItemTurnontimeInputlevel(
            device, f"{self._cmd_syntax}:INPUTLEVel"
        )
        self._inputsource = PowerPowerItemTurnontimeInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )
        self._maxtime = PowerPowerItemTurnontimeMaxtime(device, f"{self._cmd_syntax}:MAXTIMe")
        self._maxvoltage = PowerPowerItemTurnontimeMaxvoltage(
            device, f"{self._cmd_syntax}:MAXVoltage"
        )
        self._numoutputs = PowerPowerItemTurnontimeNumoutputs(
            device, f"{self._cmd_syntax}:NUMOUTputs"
        )
        self._output1source = PowerPowerItemTurnontimeOutput1source(
            device, f"{self._cmd_syntax}:OUTPUT1SOURce"
        )
        self._output1voltage = PowerPowerItemTurnontimeOutput1voltage(
            device, f"{self._cmd_syntax}:OUTPUT1VOLTage"
        )
        self._output2source = PowerPowerItemTurnontimeOutput2source(
            device, f"{self._cmd_syntax}:OUTPUT2SOURce"
        )
        self._output2voltage = PowerPowerItemTurnontimeOutput2voltage(
            device, f"{self._cmd_syntax}:OUTPUT2VOLTage"
        )
        self._output3source = PowerPowerItemTurnontimeOutput3source(
            device, f"{self._cmd_syntax}:OUTPUT3SOURce"
        )
        self._output3voltage = PowerPowerItemTurnontimeOutput3voltage(
            device, f"{self._cmd_syntax}:OUTPUT3VOLTage"
        )
        self._output4source = PowerPowerItemTurnontimeOutput4source(
            device, f"{self._cmd_syntax}:OUTPUT4SOURce"
        )
        self._output4voltage = PowerPowerItemTurnontimeOutput4voltage(
            device, f"{self._cmd_syntax}:OUTPUT4VOLTage"
        )
        self._output5source = PowerPowerItemTurnontimeOutput5source(
            device, f"{self._cmd_syntax}:OUTPUT5SOURce"
        )
        self._output5voltage = PowerPowerItemTurnontimeOutput5voltage(
            device, f"{self._cmd_syntax}:OUTPUT5VOLTage"
        )
        self._output6source = PowerPowerItemTurnontimeOutput6source(
            device, f"{self._cmd_syntax}:OUTPUT6SOURce"
        )
        self._output6voltage = PowerPowerItemTurnontimeOutput6voltage(
            device, f"{self._cmd_syntax}:OUTPUT6VOLTage"
        )
        self._output7source = PowerPowerItemTurnontimeOutput7source(
            device, f"{self._cmd_syntax}:OUTPUT7SOURce"
        )
        self._output7voltage = PowerPowerItemTurnontimeOutput7voltage(
            device, f"{self._cmd_syntax}:OUTPUT7VOLTage"
        )
        self._type = PowerPowerItemTurnontimeType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def frequency(self) -> PowerPowerItemTurnontimeFrequency:
        """Return the ``POWer:POWer<x>:TURNONtime:FREQuency`` command.

        Description:
            - This command sets or queries the input frequency used by the AC or DC converter of the
              specified Turn On Time measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:FREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:FREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:FREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:FREQuency <NR3>
            - POWer:POWer<x>:TURNONtime:FREQuency?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR3>`` is a floating point number that represents the frequency, in Hertz, from 1
              Hz to 500 Hz.
        """
        return self._frequency

    @property
    def inputlevel(self) -> PowerPowerItemTurnontimeInputlevel:
        """Return the ``POWer:POWer<x>:TURNONtime:INPUTLEVel`` command.

        Description:
            - This command sets or returns the input voltage level of the specified Turn On Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:INPUTLEVel?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:INPUTLEVel?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:INPUTLEVel value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:INPUTLEVel <NR3>
            - POWer:POWer<x>:TURNONtime:INPUTLEVel?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR3>`` is a floating point number that represents the voltage level, in volts, from
              -500 V to 500 V.
        """
        return self._inputlevel

    @property
    def inputsource(self) -> PowerPowerItemTurnontimeInputsource:
        """Return the ``POWer:POWer<x>:TURNONtime:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source of the specified Turn On Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``POWer:POWer<x>:TURNONtime:INPUTSOurce``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:INPUTSOurce
            - POWer:POWer<x>:TURNONtime:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` is the channel specifier in the range of 1 through 8 and is limited by the
              number of instrument input channels.
            - ``REF<x>`` is the Reference waveform specifier ≥1. This is the equivalent of the
              number shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` is the Math waveform specifier ≥1. This is the equivalent of the number
              shown on a Math waveform badge in the UI.
        """
        return self._inputsource

    @property
    def maxtime(self) -> PowerPowerItemTurnontimeMaxtime:
        """Return the ``POWer:POWer<x>:TURNONtime:MAXTIMe`` command.

        Description:
            - This command sets or returns the maximum turn on time of the specified Turn On Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:MAXTIMe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:MAXTIMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:MAXTIMe value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:MAXTIMe <NR3>
            - POWer:POWer<x>:TURNONtime:MAXTIMe?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR3>`` is a floating point number that represents the maximum time value, in
              seconds, in the range 1 second to 500 seconds.
        """
        return self._maxtime

    @property
    def maxvoltage(self) -> PowerPowerItemTurnontimeMaxvoltage:
        """Return the ``POWer:POWer<x>:TURNONtime:MAXVoltage`` command.

        Description:
            - This command sets or returns the maximum voltage setting of the specified Turn On Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:MAXVoltage?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:MAXVoltage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:MAXVoltage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:MAXVoltage <NR3>
            - POWer:POWer<x>:TURNONtime:MAXVoltage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR3>`` is a floating point number that represents the maximum voltage in the range
              1 V to 500 V.
        """
        return self._maxvoltage

    @property
    def numoutputs(self) -> PowerPowerItemTurnontimeNumoutputs:
        """Return the ``POWer:POWer<x>:TURNONtime:NUMOUTputs`` command.

        Description:
            - This command sets or queries the number of outputs for the specified Turn On Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:NUMOUTputs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:NUMOUTputs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:NUMOUTputs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:NUMOUTputs {ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN}
            - POWer:POWer<x>:TURNONtime:NUMOUTputs?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``ONE`` through SEVEN sets the number of outputs for the specified Turn On Time power
              measurement.
        """
        return self._numoutputs

    @property
    def output1source(self) -> PowerPowerItemTurnontimeOutput1source:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT1SOURce`` command.

        Description:
            - This command sets or queries the output 1 source of the specified Turn On Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT1SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT1SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT1SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT1SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNONtime:OUTPUT1SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output1source

    @property
    def output1voltage(self) -> PowerPowerItemTurnontimeOutput1voltage:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage`` command.

        Description:
            - This command sets or queries the output 1 voltage level of the specified Turn On Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage <NR2>
            - POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output1voltage

    @property
    def output2source(self) -> PowerPowerItemTurnontimeOutput2source:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT2SOURce`` command.

        Description:
            - This command sets or queries the output 2 source of the specified Turn On Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT2SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT2SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT2SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT2SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNONtime:OUTPUT2SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output2source

    @property
    def output2voltage(self) -> PowerPowerItemTurnontimeOutput2voltage:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage`` command.

        Description:
            - This command sets or queries the output 2 voltage level of the specified Turn On Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage <NR2>
            - POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output2voltage

    @property
    def output3source(self) -> PowerPowerItemTurnontimeOutput3source:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT3SOURce`` command.

        Description:
            - This command sets or queries the output 3 source of the specified Turn On Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT3SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT3SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT3SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT3SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNONtime:OUTPUT3SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output3source

    @property
    def output3voltage(self) -> PowerPowerItemTurnontimeOutput3voltage:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage`` command.

        Description:
            - This command sets or queries the output 3 voltage level of the specified Turn On Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage <NR2>
            - POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output3voltage

    @property
    def output4source(self) -> PowerPowerItemTurnontimeOutput4source:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT4SOURce`` command.

        Description:
            - This command sets or queries the output 4 source of the specified Turn On Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT4SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT4SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT4SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT4SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNONtime:OUTPUT4SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output4source

    @property
    def output4voltage(self) -> PowerPowerItemTurnontimeOutput4voltage:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage`` command.

        Description:
            - This command sets or queries the output 4 voltage level of the specified Turn On Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage <NR2>
            - POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output4voltage

    @property
    def output5source(self) -> PowerPowerItemTurnontimeOutput5source:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT5SOURce`` command.

        Description:
            - This command sets or queries the output 5 source of the specified Turn On Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT5SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT5SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT5SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT5SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNONtime:OUTPUT5SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output5source

    @property
    def output5voltage(self) -> PowerPowerItemTurnontimeOutput5voltage:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage`` command.

        Description:
            - This command sets or queries the output 5 voltage level of the specified Turn On Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage <NR2>
            - POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output5voltage

    @property
    def output6source(self) -> PowerPowerItemTurnontimeOutput6source:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT6SOURce`` command.

        Description:
            - This command sets or queries the output 6 source of the specified Turn On Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT6SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT6SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT6SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT6SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNONtime:OUTPUT6SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output6source

    @property
    def output6voltage(self) -> PowerPowerItemTurnontimeOutput6voltage:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage`` command.

        Description:
            - This command sets or queries the output 6 voltage level of the specified Turn On Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage <NR2>
            - POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output6voltage

    @property
    def output7source(self) -> PowerPowerItemTurnontimeOutput7source:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT7SOURce`` command.

        Description:
            - This command sets or queries the output 7 source of the specified Turn On Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT7SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT7SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT7SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT7SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNONtime:OUTPUT7SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output7source

    @property
    def output7voltage(self) -> PowerPowerItemTurnontimeOutput7voltage:
        """Return the ``POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage`` command.

        Description:
            - This command sets or queries the output 7 voltage level of the specified Turn On Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage <NR2>
            - POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output7voltage

    @property
    def type(self) -> PowerPowerItemTurnontimeType:
        """Return the ``POWer:POWer<x>:TURNONtime:TYPE`` command.

        Description:
            - This command sets or queries the type of AC/DC converter used in the specified Turn On
              Time power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TURNONtime:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNONtime:TYPE value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNONtime:TYPE {DCDC|ACDC}
            - POWer:POWer<x>:TURNONtime:TYPE?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``DCDC`` sets the measurement to use a DC to DC converter.
            - ``ACDC`` sets the measurement to use an AC to DC converter.
        """
        return self._type


class PowerPowerItemTurnofftimeType(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:TYPE`` command.

    Description:
        - This command sets or queries the type of AC/DC converter used in the specified Turn Off
          Time power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TURNOFFtime:TYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:TURNOFFtime:TYPE value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:TYPE {DCDC|ACDC}
        - POWer:POWer<x>:TURNOFFtime:TYPE?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``DCDC`` sets the measurement to use a DC to DC converter.
        - ``ACDC`` sets the measurement to use an AC to DC converter.
    """


class PowerPowerItemTurnofftimeOutput7voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage`` command.

    Description:
        - This command sets or queries the output 7 voltage level of the specified Turn Off Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage <NR2>
        - POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnofftimeOutput7source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce`` command.

    Description:
        - This command sets or queries the output 7 source of the specified Turn Off Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnofftimeOutput6voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage`` command.

    Description:
        - This command sets or queries the output 6 voltage level of the specified Turn Off Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage <NR2>
        - POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnofftimeOutput6source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce`` command.

    Description:
        - This command sets or queries the output 6 source of the specified Turn Off Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnofftimeOutput5voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage`` command.

    Description:
        - This command sets or queries the output 5 voltage level of the specified Turn Off Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage <NR2>
        - POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnofftimeOutput5source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce`` command.

    Description:
        - This command sets or queries the output 5 source of the specified Turn Off Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnofftimeOutput4voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage`` command.

    Description:
        - This command sets or queries the output 4 voltage level of the specified Turn Off Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage <NR2>
        - POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnofftimeOutput4source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce`` command.

    Description:
        - This command sets or queries the output 4 source of the specified Turn Off Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnofftimeOutput3voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage`` command.

    Description:
        - This command sets or queries the output 3 voltage level of the specified Turn Off Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage <NR2>
        - POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnofftimeOutput3source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce`` command.

    Description:
        - This command sets or queries the output 3 source of the specified Turn Off Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnofftimeOutput2voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage`` command.

    Description:
        - This command sets or queries the output 2 voltage level of the specified Turn Off Time
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage <NR2>
        - POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnofftimeOutput2source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce`` command.

    Description:
        - This command sets or queries the output 2 source of the specified Turn Off Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnofftimeOutput1voltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage`` command.

    Description:
        - This command sets or queries the output 1 voltage level of the of the specified Turn Off
          Time power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage <NR2>
        - POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
    """


class PowerPowerItemTurnofftimeOutput1source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce`` command.

    Description:
        - This command sets or queries the output 1 source of the specified Turn Off Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number of
          instrument input channels.
        - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number shown
          on a Reference waveform badge in the UI.
        - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown on a
          Math waveform badge in the UI.
    """


class PowerPowerItemTurnofftimeNumoutputs(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:NUMOUTputs`` command.

    Description:
        - This command sets or queries the number of outputs of the specified Turn Off Time power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:NUMOUTputs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:NUMOUTputs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:NUMOUTputs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:NUMOUTputs {ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN}
        - POWer:POWer<x>:TURNOFFtime:NUMOUTputs?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``ONE`` through SEVEN sets the number of outputs for the Turn Off Time measurement.
    """


class PowerPowerItemTurnofftimeMaxvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:MAXVoltage`` command.

    Description:
        - This command sets or queries the maximum voltage of the specified Turn OffTime
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:MAXVoltage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:MAXVoltage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:MAXVoltage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:MAXVoltage <NR3>
        - POWer:POWer<x>:TURNOFFtime:MAXVoltage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR3>`` is a floating point number that represents the maximum voltage in the range 1 V
          to 500 V.
    """


class PowerPowerItemTurnofftimeMaxtime(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:MAXTIMe`` command.

    Description:
        - This command sets or queries the maximum turn off time of the specified Turn Off Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:MAXTIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TURNOFFtime:MAXTIMe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:MAXTIMe value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:MAXTIMe <NR3>
        - POWer:POWer<x>:TURNOFFtime:MAXTIMe?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR3>`` is a floating point number that represents the maximum time value, in seconds,
          in the range 1 second to 500 seconds.
    """


class PowerPowerItemTurnofftimeInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source of the specified Turn Off Time measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:INPUTSOurce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:TURNOFFtime:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` is the channel specifier in the range of 1 through 8 and is limited by the
          number of instrument input channels.
        - ``REF<x>`` is the Reference waveform specifier ≥1. This is the equivalent of the number
          shown on a Reference waveform badge in the UI.
        - ``MATH<x>`` is the Math waveform specifier ≥1. This is the equivalent of the number shown
          on a Math waveform badge in the UI.
    """


class PowerPowerItemTurnofftimeInputlevel(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:INPUTLEVel`` command.

    Description:
        - This command sets or queries the input voltage level of the specified Turn Off Time
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:INPUTLEVel?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:INPUTLEVel?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:INPUTLEVel value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:INPUTLEVel <NR3>
        - POWer:POWer<x>:TURNOFFtime:INPUTLEVel?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR3>`` is a floating point number that represents the voltage level, in volts, from
          -500 V to 500 V.
    """


class PowerPowerItemTurnofftimeFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime:FREQuency`` command.

    Description:
        - This command sets or queries the input frequency used by the AC or DC converter of the
          specified Turn Off Time measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:FREQuency?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:FREQuency?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:TURNOFFtime:FREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:TURNOFFtime:FREQuency <NR3>
        - POWer:POWer<x>:TURNOFFtime:FREQuency?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR3>`` is a floating point number that represents the frequency, in Hertz, from 1 Hz to
          500 Hz.
    """


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class PowerPowerItemTurnofftime(SCPICmdRead):
    """The ``POWer:POWer<x>:TURNOFFtime`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TURNOFFtime?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``POWer:POWer<x>:TURNOFFtime:FREQuency`` command.
        - ``.inputlevel``: The ``POWer:POWer<x>:TURNOFFtime:INPUTLEVel`` command.
        - ``.inputsource``: The ``POWer:POWer<x>:TURNOFFtime:INPUTSOurce`` command.
        - ``.maxtime``: The ``POWer:POWer<x>:TURNOFFtime:MAXTIMe`` command.
        - ``.maxvoltage``: The ``POWer:POWer<x>:TURNOFFtime:MAXVoltage`` command.
        - ``.numoutputs``: The ``POWer:POWer<x>:TURNOFFtime:NUMOUTputs`` command.
        - ``.output1source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce`` command.
        - ``.output1voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage`` command.
        - ``.output2source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce`` command.
        - ``.output2voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage`` command.
        - ``.output3source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce`` command.
        - ``.output3voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage`` command.
        - ``.output4source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce`` command.
        - ``.output4voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage`` command.
        - ``.output5source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce`` command.
        - ``.output5voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage`` command.
        - ``.output6source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce`` command.
        - ``.output6voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage`` command.
        - ``.output7source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce`` command.
        - ``.output7voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage`` command.
        - ``.type``: The ``POWer:POWer<x>:TURNOFFtime:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = PowerPowerItemTurnofftimeFrequency(
            device, f"{self._cmd_syntax}:FREQuency"
        )
        self._inputlevel = PowerPowerItemTurnofftimeInputlevel(
            device, f"{self._cmd_syntax}:INPUTLEVel"
        )
        self._inputsource = PowerPowerItemTurnofftimeInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )
        self._maxtime = PowerPowerItemTurnofftimeMaxtime(device, f"{self._cmd_syntax}:MAXTIMe")
        self._maxvoltage = PowerPowerItemTurnofftimeMaxvoltage(
            device, f"{self._cmd_syntax}:MAXVoltage"
        )
        self._numoutputs = PowerPowerItemTurnofftimeNumoutputs(
            device, f"{self._cmd_syntax}:NUMOUTputs"
        )
        self._output1source = PowerPowerItemTurnofftimeOutput1source(
            device, f"{self._cmd_syntax}:OUTPUT1SOURce"
        )
        self._output1voltage = PowerPowerItemTurnofftimeOutput1voltage(
            device, f"{self._cmd_syntax}:OUTPUT1VOLTage"
        )
        self._output2source = PowerPowerItemTurnofftimeOutput2source(
            device, f"{self._cmd_syntax}:OUTPUT2SOURce"
        )
        self._output2voltage = PowerPowerItemTurnofftimeOutput2voltage(
            device, f"{self._cmd_syntax}:OUTPUT2VOLTage"
        )
        self._output3source = PowerPowerItemTurnofftimeOutput3source(
            device, f"{self._cmd_syntax}:OUTPUT3SOURce"
        )
        self._output3voltage = PowerPowerItemTurnofftimeOutput3voltage(
            device, f"{self._cmd_syntax}:OUTPUT3VOLTage"
        )
        self._output4source = PowerPowerItemTurnofftimeOutput4source(
            device, f"{self._cmd_syntax}:OUTPUT4SOURce"
        )
        self._output4voltage = PowerPowerItemTurnofftimeOutput4voltage(
            device, f"{self._cmd_syntax}:OUTPUT4VOLTage"
        )
        self._output5source = PowerPowerItemTurnofftimeOutput5source(
            device, f"{self._cmd_syntax}:OUTPUT5SOURce"
        )
        self._output5voltage = PowerPowerItemTurnofftimeOutput5voltage(
            device, f"{self._cmd_syntax}:OUTPUT5VOLTage"
        )
        self._output6source = PowerPowerItemTurnofftimeOutput6source(
            device, f"{self._cmd_syntax}:OUTPUT6SOURce"
        )
        self._output6voltage = PowerPowerItemTurnofftimeOutput6voltage(
            device, f"{self._cmd_syntax}:OUTPUT6VOLTage"
        )
        self._output7source = PowerPowerItemTurnofftimeOutput7source(
            device, f"{self._cmd_syntax}:OUTPUT7SOURce"
        )
        self._output7voltage = PowerPowerItemTurnofftimeOutput7voltage(
            device, f"{self._cmd_syntax}:OUTPUT7VOLTage"
        )
        self._type = PowerPowerItemTurnofftimeType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def frequency(self) -> PowerPowerItemTurnofftimeFrequency:
        """Return the ``POWer:POWer<x>:TURNOFFtime:FREQuency`` command.

        Description:
            - This command sets or queries the input frequency used by the AC or DC converter of the
              specified Turn Off Time measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:FREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:FREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:FREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:FREQuency <NR3>
            - POWer:POWer<x>:TURNOFFtime:FREQuency?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR3>`` is a floating point number that represents the frequency, in Hertz, from 1
              Hz to 500 Hz.
        """
        return self._frequency

    @property
    def inputlevel(self) -> PowerPowerItemTurnofftimeInputlevel:
        """Return the ``POWer:POWer<x>:TURNOFFtime:INPUTLEVel`` command.

        Description:
            - This command sets or queries the input voltage level of the specified Turn Off Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:INPUTLEVel?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:INPUTLEVel?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:INPUTLEVel value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:INPUTLEVel <NR3>
            - POWer:POWer<x>:TURNOFFtime:INPUTLEVel?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR3>`` is a floating point number that represents the voltage level, in volts, from
              -500 V to 500 V.
        """
        return self._inputlevel

    @property
    def inputsource(self) -> PowerPowerItemTurnofftimeInputsource:
        """Return the ``POWer:POWer<x>:TURNOFFtime:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source of the specified Turn Off Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:INPUTSOurce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:INPUTSOurce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNOFFtime:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` is the channel specifier in the range of 1 through 8 and is limited by the
              number of instrument input channels.
            - ``REF<x>`` is the Reference waveform specifier ≥1. This is the equivalent of the
              number shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` is the Math waveform specifier ≥1. This is the equivalent of the number
              shown on a Math waveform badge in the UI.
        """
        return self._inputsource

    @property
    def maxtime(self) -> PowerPowerItemTurnofftimeMaxtime:
        """Return the ``POWer:POWer<x>:TURNOFFtime:MAXTIMe`` command.

        Description:
            - This command sets or queries the maximum turn off time of the specified Turn Off Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:MAXTIMe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:MAXTIMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:MAXTIMe value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:MAXTIMe <NR3>
            - POWer:POWer<x>:TURNOFFtime:MAXTIMe?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR3>`` is a floating point number that represents the maximum time value, in
              seconds, in the range 1 second to 500 seconds.
        """
        return self._maxtime

    @property
    def maxvoltage(self) -> PowerPowerItemTurnofftimeMaxvoltage:
        """Return the ``POWer:POWer<x>:TURNOFFtime:MAXVoltage`` command.

        Description:
            - This command sets or queries the maximum voltage of the specified Turn OffTime
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:MAXVoltage?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:MAXVoltage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:MAXVoltage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:MAXVoltage <NR3>
            - POWer:POWer<x>:TURNOFFtime:MAXVoltage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR3>`` is a floating point number that represents the maximum voltage in the range
              1 V to 500 V.
        """
        return self._maxvoltage

    @property
    def numoutputs(self) -> PowerPowerItemTurnofftimeNumoutputs:
        """Return the ``POWer:POWer<x>:TURNOFFtime:NUMOUTputs`` command.

        Description:
            - This command sets or queries the number of outputs of the specified Turn Off Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:NUMOUTputs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:NUMOUTputs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:NUMOUTputs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:NUMOUTputs {ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN}
            - POWer:POWer<x>:TURNOFFtime:NUMOUTputs?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``ONE`` through SEVEN sets the number of outputs for the Turn Off Time measurement.
        """
        return self._numoutputs

    @property
    def output1source(self) -> PowerPowerItemTurnofftimeOutput1source:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce`` command.

        Description:
            - This command sets or queries the output 1 source of the specified Turn Off Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output1source

    @property
    def output1voltage(self) -> PowerPowerItemTurnofftimeOutput1voltage:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage`` command.

        Description:
            - This command sets or queries the output 1 voltage level of the of the specified Turn
              Off Time power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage <NR2>
            - POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output1voltage

    @property
    def output2source(self) -> PowerPowerItemTurnofftimeOutput2source:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce`` command.

        Description:
            - This command sets or queries the output 2 source of the specified Turn Off Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output2source

    @property
    def output2voltage(self) -> PowerPowerItemTurnofftimeOutput2voltage:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage`` command.

        Description:
            - This command sets or queries the output 2 voltage level of the specified Turn Off Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage <NR2>
            - POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output2voltage

    @property
    def output3source(self) -> PowerPowerItemTurnofftimeOutput3source:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce`` command.

        Description:
            - This command sets or queries the output 3 source of the specified Turn Off Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output3source

    @property
    def output3voltage(self) -> PowerPowerItemTurnofftimeOutput3voltage:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage`` command.

        Description:
            - This command sets or queries the output 3 voltage level of the specified Turn Off Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage <NR2>
            - POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output3voltage

    @property
    def output4source(self) -> PowerPowerItemTurnofftimeOutput4source:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce`` command.

        Description:
            - This command sets or queries the output 4 source of the specified Turn Off Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output4source

    @property
    def output4voltage(self) -> PowerPowerItemTurnofftimeOutput4voltage:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage`` command.

        Description:
            - This command sets or queries the output 4 voltage level of the specified Turn Off Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage <NR2>
            - POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output4voltage

    @property
    def output5source(self) -> PowerPowerItemTurnofftimeOutput5source:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce`` command.

        Description:
            - This command sets or queries the output 5 source of the specified Turn Off Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output5source

    @property
    def output5voltage(self) -> PowerPowerItemTurnofftimeOutput5voltage:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage`` command.

        Description:
            - This command sets or queries the output 5 voltage level of the specified Turn Off Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage <NR2>
            - POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output5voltage

    @property
    def output6source(self) -> PowerPowerItemTurnofftimeOutput6source:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce`` command.

        Description:
            - This command sets or queries the output 6 source of the specified Turn Off Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output6source

    @property
    def output6voltage(self) -> PowerPowerItemTurnofftimeOutput6voltage:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage`` command.

        Description:
            - This command sets or queries the output 6 voltage level of the specified Turn Off Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage <NR2>
            - POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output6voltage

    @property
    def output7source(self) -> PowerPowerItemTurnofftimeOutput7source:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce`` command.

        Description:
            - This command sets or queries the output 7 source of the specified Turn Off Time
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` A channel specifier in the range of 1 through 8 and is limited by the number
              of instrument input channels.
            - ``REF<x>`` A Reference waveform specifier ≥1. This is the equivalent of the number
              shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` A Math waveform specifier ≥1. This is the equivalent of the number shown
              on a Math waveform badge in the UI.
        """
        return self._output7source

    @property
    def output7voltage(self) -> PowerPowerItemTurnofftimeOutput7voltage:
        """Return the ``POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage`` command.

        Description:
            - This command sets or queries the output 7 voltage level of the specified Turn Off Time
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage <NR2>
            - POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR2>`` sets the output voltage value, in the range of -6,000 volts to +6,000 volts.
        """
        return self._output7voltage

    @property
    def type(self) -> PowerPowerItemTurnofftimeType:
        """Return the ``POWer:POWer<x>:TURNOFFtime:TYPE`` command.

        Description:
            - This command sets or queries the type of AC/DC converter used in the specified Turn
              Off Time power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime:TYPE?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TURNOFFtime:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:TURNOFFtime:TYPE value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TURNOFFtime:TYPE {DCDC|ACDC}
            - POWer:POWer<x>:TURNOFFtime:TYPE?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``DCDC`` sets the measurement to use a DC to DC converter.
            - ``ACDC`` sets the measurement to use an AC to DC converter.
        """
        return self._type


class PowerPowerItemSwitchingrippleLfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency`` command.

    Description:
        - This command sets or queries the switching frequency for switching ripple measurement in
          the specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency <NR1>
        - POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 50 to 1000000.
    """


class PowerPowerItemSwitchingrippleInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for switching ripple measurement in the
          specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemSwitchingripple(SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGRIPPLE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGRIPPLE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SWITCHINGRIPPLE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce`` command.
        - ``.lfrequency``: The ``POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemSwitchingrippleInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )
        self._lfrequency = PowerPowerItemSwitchingrippleLfrequency(
            device, f"{self._cmd_syntax}:LFREQuency"
        )

    @property
    def inputsource(self) -> PowerPowerItemSwitchingrippleInputsource:
        """Return the ``POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for switching ripple measurement in the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource

    @property
    def lfrequency(self) -> PowerPowerItemSwitchingrippleLfrequency:
        """Return the ``POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency`` command.

        Description:
            - This command sets or queries the switching frequency for switching ripple measurement
              in the specified power measurement number. The power measurement number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency <NR1>
            - POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 50 to 1000000.
        """
        return self._lfrequency


class PowerPowerItemSwitchinglossVsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:VSOURce`` command.

    Description:
        - This command sets or queries the voltage source for the switching loss measurement in the
          specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:VSOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:VSOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:VSOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:VSOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:SWITCHINGLOSS:VSOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemSwitchinglossVlevelpct(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct`` command.

    Description:
        - This command sets or queries the voltage level (Ton-Start & Stop) in percentage for
          switching loss measurement in the specified power measurement number. The power
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct <NR1>
        - POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 0.0001 to 90.
    """


class PowerPowerItemSwitchinglossVlevelabs(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs`` command.

    Description:
        - This command sets or queries the voltage level (Ton-Start & Stop) in absolute units for
          switching loss measurement in the specified power measurement number. The power
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs <NR1>
        - POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from -100 to 100.
    """


class PowerPowerItemSwitchinglossVglevel(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:VGLevel`` command.

    Description:
        - This command sets or queries the gate voltage value (V g Level Ton-Start) for the
          switching loss measurement in the specified power measurement number. The power
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:VGLevel?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:VGLevel?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:VGLevel value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:VGLevel <NR1>
        - POWer:POWer<x>:SWITCHINGLOSS:VGLevel?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from -100 to 100.
    """


class PowerPowerItemSwitchinglossVcesat(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:VCESat`` command.

    Description:
        - This command sets or queries the value for the VCE(sat) value for switching loss
          measurement in the specified power measurement number. The power measurement number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:VCESat?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:VCESat?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:VCESat value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:VCESat <NR1>
        - POWer:POWer<x>:SWITCHINGLOSS:VCESat?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 0.001 to 100.
    """


class PowerPowerItemSwitchinglossSwlconfigtype(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType`` command.

    Description:
        - This command sets or queries the configuration type for the switching loss measurement in
          the specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType {SMPS|PFC|FLYBACK}
        - POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``SMPS`` : Select this option in case of signals without noise and ringing. The Vg source
          is not required. Select Vg souce (Source 3), in case of noisy signal.
        - ``PFC`` : Select this option when input DUT signals are from Power Factor Correction
          Circuit. For this case, Vg source is mandatory.
        - ``FLYBACK`` : Select this option when input signals are ringing. This option does not
          require a Vg source.
    """


class PowerPowerItemSwitchinglossRdson(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:RDSOn`` command.

    Description:
        - This command sets or queries the RDS(on) value for switching loss measurement in the
          specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:RDSOn?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:RDSOn?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:RDSOn value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:RDSOn <NR1>
        - POWer:POWer<x>:SWITCHINGLOSS:RDSOn?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 0 to 100.
    """


class PowerPowerItemSwitchinglossLevelunits(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts`` command.

    Description:
        - This command sets or queries the level units for switching loss measurement in the
          specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts {PERCent|ABSolute}
        - POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``PERCent`` to set the High, Mid, and Low reference levels in percentage.
        - ``ABSolute`` to set the High, Mid, and Low reference levels to specific signal levels.
    """


class PowerPowerItemSwitchinglossIsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:ISOURce`` command.

    Description:
        - This command sets or queries the current source for the switching loss measurement in the
          specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:ISOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:ISOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:ISOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:ISOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:SWITCHINGLOSS:ISOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemSwitchinglossIlevelpct(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct`` command.

    Description:
        - This command sets or queries the current level (Ton-Start & Stop) in percentage for
          switching loss measurement in the specified power measurement number. The power
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct <NR1>
        - POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 0.0001 to 90.
    """


class PowerPowerItemSwitchinglossIlevelabs(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs`` command.

    Description:
        - This command sets or queries the current level (Ton-Start & Stop) in absolute units for
          switching loss measurement in the specified power measurement number. The power
          measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs <NR1>
        - POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from -100 to 100.
    """


class PowerPowerItemSwitchinglossGatesource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:GATESOurce`` command.

    Description:
        - This command sets or queries the gate voltage (V g ) for the switching loss measurement in
          the specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:GATESOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:GATESOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:GATESOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:GATESOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:SWITCHINGLOSS:GATESOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemSwitchinglossDevicetype(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS:DEVICEType`` command.

    Description:
        - This command sets or queries the conduction calculation method for switching loss
          measurement in the specified power measurement number. The power measurement number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:DEVICEType?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:DEVICEType?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:SWITCHINGLOSS:DEVICEType value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SWITCHINGLOSS:DEVICEType {MOSFET|BJT}
        - POWer:POWer<x>:SWITCHINGLOSS:DEVICEType?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class PowerPowerItemSwitchingloss(SCPICmdRead):
    """The ``POWer:POWer<x>:SWITCHINGLOSS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.devicetype``: The ``POWer:POWer<x>:SWITCHINGLOSS:DEVICEType`` command.
        - ``.gatesource``: The ``POWer:POWer<x>:SWITCHINGLOSS:GATESOurce`` command.
        - ``.ilevelabs``: The ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs`` command.
        - ``.ilevelpct``: The ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct`` command.
        - ``.isource``: The ``POWer:POWer<x>:SWITCHINGLOSS:ISOURce`` command.
        - ``.levelunits``: The ``POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts`` command.
        - ``.rdson``: The ``POWer:POWer<x>:SWITCHINGLOSS:RDSOn`` command.
        - ``.swlconfigtype``: The ``POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType`` command.
        - ``.vcesat``: The ``POWer:POWer<x>:SWITCHINGLOSS:VCESat`` command.
        - ``.vglevel``: The ``POWer:POWer<x>:SWITCHINGLOSS:VGLevel`` command.
        - ``.vlevelabs``: The ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs`` command.
        - ``.vlevelpct``: The ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct`` command.
        - ``.vsource``: The ``POWer:POWer<x>:SWITCHINGLOSS:VSOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._devicetype = PowerPowerItemSwitchinglossDevicetype(
            device, f"{self._cmd_syntax}:DEVICEType"
        )
        self._gatesource = PowerPowerItemSwitchinglossGatesource(
            device, f"{self._cmd_syntax}:GATESOurce"
        )
        self._ilevelabs = PowerPowerItemSwitchinglossIlevelabs(
            device, f"{self._cmd_syntax}:ILEVELAbs"
        )
        self._ilevelpct = PowerPowerItemSwitchinglossIlevelpct(
            device, f"{self._cmd_syntax}:ILEVELPct"
        )
        self._isource = PowerPowerItemSwitchinglossIsource(device, f"{self._cmd_syntax}:ISOURce")
        self._levelunits = PowerPowerItemSwitchinglossLevelunits(
            device, f"{self._cmd_syntax}:LEVELUNIts"
        )
        self._rdson = PowerPowerItemSwitchinglossRdson(device, f"{self._cmd_syntax}:RDSOn")
        self._swlconfigtype = PowerPowerItemSwitchinglossSwlconfigtype(
            device, f"{self._cmd_syntax}:SWLCONFIGType"
        )
        self._vcesat = PowerPowerItemSwitchinglossVcesat(device, f"{self._cmd_syntax}:VCESat")
        self._vglevel = PowerPowerItemSwitchinglossVglevel(device, f"{self._cmd_syntax}:VGLevel")
        self._vlevelabs = PowerPowerItemSwitchinglossVlevelabs(
            device, f"{self._cmd_syntax}:VLEVELAbs"
        )
        self._vlevelpct = PowerPowerItemSwitchinglossVlevelpct(
            device, f"{self._cmd_syntax}:VLEVELPct"
        )
        self._vsource = PowerPowerItemSwitchinglossVsource(device, f"{self._cmd_syntax}:VSOURce")

    @property
    def devicetype(self) -> PowerPowerItemSwitchinglossDevicetype:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:DEVICEType`` command.

        Description:
            - This command sets or queries the conduction calculation method for switching loss
              measurement in the specified power measurement number. The power measurement number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:DEVICEType?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:DEVICEType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:DEVICEType value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:DEVICEType {MOSFET|BJT}
            - POWer:POWer<x>:SWITCHINGLOSS:DEVICEType?
            ```
        """
        return self._devicetype

    @property
    def gatesource(self) -> PowerPowerItemSwitchinglossGatesource:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:GATESOurce`` command.

        Description:
            - This command sets or queries the gate voltage (V g ) for the switching loss
              measurement in the specified power measurement number. The power measurement number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:GATESOurce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:GATESOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:GATESOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:GATESOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:SWITCHINGLOSS:GATESOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._gatesource

    @property
    def ilevelabs(self) -> PowerPowerItemSwitchinglossIlevelabs:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs`` command.

        Description:
            - This command sets or queries the current level (Ton-Start & Stop) in absolute units
              for switching loss measurement in the specified power measurement number. The power
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs <NR1>
            - POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from -100 to 100.
        """
        return self._ilevelabs

    @property
    def ilevelpct(self) -> PowerPowerItemSwitchinglossIlevelpct:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct`` command.

        Description:
            - This command sets or queries the current level (Ton-Start & Stop) in percentage for
              switching loss measurement in the specified power measurement number. The power
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct <NR1>
            - POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 0.0001 to 90.
        """
        return self._ilevelpct

    @property
    def isource(self) -> PowerPowerItemSwitchinglossIsource:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:ISOURce`` command.

        Description:
            - This command sets or queries the current source for the switching loss measurement in
              the specified power measurement number. The power measurement number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:ISOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:ISOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:ISOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:ISOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:SWITCHINGLOSS:ISOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._isource

    @property
    def levelunits(self) -> PowerPowerItemSwitchinglossLevelunits:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts`` command.

        Description:
            - This command sets or queries the level units for switching loss measurement in the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts {PERCent|ABSolute}
            - POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``PERCent`` to set the High, Mid, and Low reference levels in percentage.
            - ``ABSolute`` to set the High, Mid, and Low reference levels to specific signal levels.
        """
        return self._levelunits

    @property
    def rdson(self) -> PowerPowerItemSwitchinglossRdson:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:RDSOn`` command.

        Description:
            - This command sets or queries the RDS(on) value for switching loss measurement in the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:RDSOn?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:RDSOn?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:RDSOn value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:RDSOn <NR1>
            - POWer:POWer<x>:SWITCHINGLOSS:RDSOn?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 0 to 100.
        """
        return self._rdson

    @property
    def swlconfigtype(self) -> PowerPowerItemSwitchinglossSwlconfigtype:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType`` command.

        Description:
            - This command sets or queries the configuration type for the switching loss measurement
              in the specified power measurement number. The power measurement number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType {SMPS|PFC|FLYBACK}
            - POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``SMPS`` : Select this option in case of signals without noise and ringing. The Vg
              source is not required. Select Vg souce (Source 3), in case of noisy signal.
            - ``PFC`` : Select this option when input DUT signals are from Power Factor Correction
              Circuit. For this case, Vg source is mandatory.
            - ``FLYBACK`` : Select this option when input signals are ringing. This option does not
              require a Vg source.
        """
        return self._swlconfigtype

    @property
    def vcesat(self) -> PowerPowerItemSwitchinglossVcesat:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:VCESat`` command.

        Description:
            - This command sets or queries the value for the VCE(sat) value for switching loss
              measurement in the specified power measurement number. The power measurement number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:VCESat?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VCESat?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VCESat value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:VCESat <NR1>
            - POWer:POWer<x>:SWITCHINGLOSS:VCESat?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 0.001 to 100.
        """
        return self._vcesat

    @property
    def vglevel(self) -> PowerPowerItemSwitchinglossVglevel:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:VGLevel`` command.

        Description:
            - This command sets or queries the gate voltage value (V g Level Ton-Start) for the
              switching loss measurement in the specified power measurement number. The power
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:VGLevel?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VGLevel?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VGLevel value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:VGLevel <NR1>
            - POWer:POWer<x>:SWITCHINGLOSS:VGLevel?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from -100 to 100.
        """
        return self._vglevel

    @property
    def vlevelabs(self) -> PowerPowerItemSwitchinglossVlevelabs:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs`` command.

        Description:
            - This command sets or queries the voltage level (Ton-Start & Stop) in absolute units
              for switching loss measurement in the specified power measurement number. The power
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs <NR1>
            - POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from -100 to 100.
        """
        return self._vlevelabs

    @property
    def vlevelpct(self) -> PowerPowerItemSwitchinglossVlevelpct:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct`` command.

        Description:
            - This command sets or queries the voltage level (Ton-Start & Stop) in percentage for
              switching loss measurement in the specified power measurement number. The power
              measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct <NR1>
            - POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 0.0001 to 90.
        """
        return self._vlevelpct

    @property
    def vsource(self) -> PowerPowerItemSwitchinglossVsource:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS:VSOURce`` command.

        Description:
            - This command sets or queries the voltage source for the switching loss measurement in
              the specified power measurement number. The power measurement number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS:VSOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VSOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:SWITCHINGLOSS:VSOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SWITCHINGLOSS:VSOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:SWITCHINGLOSS:VSOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vsource


class PowerPowerItemSoaVsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SOA:VSOURce`` command.

    Description:
        - This command sets or queries the voltage source for SOA measurement in the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:VSOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA:VSOURce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:SOA:VSOURce value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SOA:VSOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:SOA:VSOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemSoaSavemaskFolder(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:SOA:SAVemask:FOLDer`` command.

    Description:
        - This command sets or queries the mask file folder path for SOA measurement in the
          specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:SAVemask:FOLDer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA:SAVemask:FOLDer?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:SOA:SAVemask:FOLDer``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SOA:SAVemask:FOLDer
        - POWer:POWer<x>:SOA:SAVemask:FOLDer?
        ```
    """


class PowerPowerItemSoaSavemaskFilename(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:SOA:SAVemask:FILEName`` command.

    Description:
        - This command sets or queries the mask file name for SOA measurement in the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:SAVemask:FILEName?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SOA:SAVemask:FILEName?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:SOA:SAVemask:FILEName``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SOA:SAVemask:FILEName
        - POWer:POWer<x>:SOA:SAVemask:FILEName?
        ```
    """


class PowerPowerItemSoaSavemaskAutoincrement(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:SOA:SAVemask:AUTOINCrement`` command.

    Description:
        - This command sets or queries the state of auto-increment for saved SOA mask file names in
          the specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:SAVemask:AUTOINCrement?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SOA:SAVemask:AUTOINCrement?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:SOA:SAVemask:AUTOINCrement``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SOA:SAVemask:AUTOINCrement
        - POWer:POWer<x>:SOA:SAVemask:AUTOINCrement?
        ```
    """


class PowerPowerItemSoaSavemask(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:SOA:SAVemask`` command.

    Description:
        - This command saves the mask file as per the name configured and at the configured path or
          queries the mask file name, path, and file type for the SOA measurement in the specified
          power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:SAVemask?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA:SAVemask?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:SOA:SAVemask`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SOA:SAVemask
        - POWer:POWer<x>:SOA:SAVemask?
        ```

    Properties:
        - ``.autoincrement``: The ``POWer:POWer<x>:SOA:SAVemask:AUTOINCrement`` command.
        - ``.filename``: The ``POWer:POWer<x>:SOA:SAVemask:FILEName`` command.
        - ``.folder``: The ``POWer:POWer<x>:SOA:SAVemask:FOLDer`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoincrement = PowerPowerItemSoaSavemaskAutoincrement(
            device, f"{self._cmd_syntax}:AUTOINCrement"
        )
        self._filename = PowerPowerItemSoaSavemaskFilename(device, f"{self._cmd_syntax}:FILEName")
        self._folder = PowerPowerItemSoaSavemaskFolder(device, f"{self._cmd_syntax}:FOLDer")

    @property
    def autoincrement(self) -> PowerPowerItemSoaSavemaskAutoincrement:
        """Return the ``POWer:POWer<x>:SOA:SAVemask:AUTOINCrement`` command.

        Description:
            - This command sets or queries the state of auto-increment for saved SOA mask file names
              in the specified power measurement number. The power measurement number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SOA:SAVemask:AUTOINCrement?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SOA:SAVemask:AUTOINCrement?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write()`` method will send the
              ``POWer:POWer<x>:SOA:SAVemask:AUTOINCrement`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SOA:SAVemask:AUTOINCrement
            - POWer:POWer<x>:SOA:SAVemask:AUTOINCrement?
            ```
        """
        return self._autoincrement

    @property
    def filename(self) -> PowerPowerItemSoaSavemaskFilename:
        """Return the ``POWer:POWer<x>:SOA:SAVemask:FILEName`` command.

        Description:
            - This command sets or queries the mask file name for SOA measurement in the specified
              power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:SAVemask:FILEName?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SOA:SAVemask:FILEName?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``POWer:POWer<x>:SOA:SAVemask:FILEName``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SOA:SAVemask:FILEName
            - POWer:POWer<x>:SOA:SAVemask:FILEName?
            ```
        """
        return self._filename

    @property
    def folder(self) -> PowerPowerItemSoaSavemaskFolder:
        """Return the ``POWer:POWer<x>:SOA:SAVemask:FOLDer`` command.

        Description:
            - This command sets or queries the mask file folder path for SOA measurement in the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:SAVemask:FOLDer?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SOA:SAVemask:FOLDer?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``POWer:POWer<x>:SOA:SAVemask:FOLDer``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SOA:SAVemask:FOLDer
            - POWer:POWer<x>:SOA:SAVemask:FOLDer?
            ```
        """
        return self._folder


class PowerPowerItemSoaRecallmaskFilename(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:SOA:RECAllmask:FILEName`` command.

    Description:
        - This command sets or queries the file name for saving SOA mask file name in the specified
          power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:RECAllmask:FILEName?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:SOA:RECAllmask:FILEName?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:SOA:RECAllmask:FILEName``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SOA:RECAllmask:FILEName
        - POWer:POWer<x>:SOA:RECAllmask:FILEName?
        ```
    """


class PowerPowerItemSoaRecallmask(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:SOA:RECAllmask`` command.

    Description:
        - This command recalls or queries the recall mask file name in the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:RECAllmask?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA:RECAllmask?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:SOA:RECAllmask`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SOA:RECAllmask
        - POWer:POWer<x>:SOA:RECAllmask?
        ```

    Properties:
        - ``.filename``: The ``POWer:POWer<x>:SOA:RECAllmask:FILEName`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._filename = PowerPowerItemSoaRecallmaskFilename(device, f"{self._cmd_syntax}:FILEName")

    @property
    def filename(self) -> PowerPowerItemSoaRecallmaskFilename:
        """Return the ``POWer:POWer<x>:SOA:RECAllmask:FILEName`` command.

        Description:
            - This command sets or queries the file name for saving SOA mask file name in the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:SOA:RECAllmask:FILEName?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:SOA:RECAllmask:FILEName?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``POWer:POWer<x>:SOA:RECAllmask:FILEName``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SOA:RECAllmask:FILEName
            - POWer:POWer<x>:SOA:RECAllmask:FILEName?
            ```
        """
        return self._filename


class PowerPowerItemSoaPointItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    r"""The ``POWer:POWer<x>:SOA:POINT<x>`` command.

    Description:
        - This command sets or queries the X or Y coordinate value for an SOA mask of a specified
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:POINT<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA:POINT<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:SOA:POINT<x> value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SOA:POINT<x> <NR1>
        - POWer:POWer<x>:SOA:POINT<x>?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``POINT<x>`` = 1X \| 2X \| 3X \| 4X \| 5X \| 6X \| 7X \| 8X \| 9X \| 10X \| 11X \| 12X \|
          13X \| 14X \| 15X \| 16X \| 17X \| 18X \| 19X \| 20X \| 21X \| 22X \| 23X \| 24X \| 25X \|
          26X \| 27X \| 28X \| 29X \| 30X \| 31X \| 32X \| 1Y \| 2Y \| 3Y \| 4Y \| 5Y \| 6Y \| 7Y \|
          8Y \| 9Y \| 10Y \| 11Y \| 12Y \| 13Y \| 14Y \| 15Y \| 16Y \| 17Y \| 18Y \| 19Y \| 20Y \|
          21Y \| 22Y \| 23Y \| 24Y \| 25Y \| 26Y \| 27Y \| 28Y \| 29Y \| 30Y \| 31Y \| 32Y.
        - ``<NR1>`` sets the specified SOA mask X or Y point value, as a floating number, in the
          range from -5000 to 5000.
    """


class PowerPowerItemSoaIsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SOA:ISOURce`` command.

    Description:
        - This command sets or queries the current source for SOA measurement in the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:ISOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA:ISOURce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:SOA:ISOURce value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SOA:ISOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:SOA:ISOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels on your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemSoa(SCPICmdRead):
    """The ``POWer:POWer<x>:SOA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.isource``: The ``POWer:POWer<x>:SOA:ISOURce`` command.
        - ``.point``: The ``POWer:POWer<x>:SOA:POINT<x>`` command.
        - ``.recallmask``: The ``POWer:POWer<x>:SOA:RECAllmask`` command.
        - ``.savemask``: The ``POWer:POWer<x>:SOA:SAVemask`` command.
        - ``.vsource``: The ``POWer:POWer<x>:SOA:VSOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._isource = PowerPowerItemSoaIsource(device, f"{self._cmd_syntax}:ISOURce")
        self._point: Dict[int, PowerPowerItemSoaPointItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerPowerItemSoaPointItem(device, f"{self._cmd_syntax}:POINT{x}")
        )
        self._recallmask = PowerPowerItemSoaRecallmask(device, f"{self._cmd_syntax}:RECAllmask")
        self._savemask = PowerPowerItemSoaSavemask(device, f"{self._cmd_syntax}:SAVemask")
        self._vsource = PowerPowerItemSoaVsource(device, f"{self._cmd_syntax}:VSOURce")

    @property
    def isource(self) -> PowerPowerItemSoaIsource:
        """Return the ``POWer:POWer<x>:SOA:ISOURce`` command.

        Description:
            - This command sets or queries the current source for SOA measurement in the specified
              power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:ISOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA:ISOURce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:SOA:ISOURce value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SOA:ISOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:SOA:ISOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels on your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._isource

    @property
    def point(self) -> Dict[int, PowerPowerItemSoaPointItem]:
        r"""Return the ``POWer:POWer<x>:SOA:POINT<x>`` command.

        Description:
            - This command sets or queries the X or Y coordinate value for an SOA mask of a
              specified power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:POINT<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA:POINT<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:SOA:POINT<x> value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SOA:POINT<x> <NR1>
            - POWer:POWer<x>:SOA:POINT<x>?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``POINT<x>`` = 1X \| 2X \| 3X \| 4X \| 5X \| 6X \| 7X \| 8X \| 9X \| 10X \| 11X \| 12X
              \| 13X \| 14X \| 15X \| 16X \| 17X \| 18X \| 19X \| 20X \| 21X \| 22X \| 23X \| 24X \|
              25X \| 26X \| 27X \| 28X \| 29X \| 30X \| 31X \| 32X \| 1Y \| 2Y \| 3Y \| 4Y \| 5Y \|
              6Y \| 7Y \| 8Y \| 9Y \| 10Y \| 11Y \| 12Y \| 13Y \| 14Y \| 15Y \| 16Y \| 17Y \| 18Y \|
              19Y \| 20Y \| 21Y \| 22Y \| 23Y \| 24Y \| 25Y \| 26Y \| 27Y \| 28Y \| 29Y \| 30Y \|
              31Y \| 32Y.
            - ``<NR1>`` sets the specified SOA mask X or Y point value, as a floating number, in the
              range from -5000 to 5000.
        """
        return self._point

    @property
    def recallmask(self) -> PowerPowerItemSoaRecallmask:
        """Return the ``POWer:POWer<x>:SOA:RECAllmask`` command.

        Description:
            - This command recalls or queries the recall mask file name in the specified power
              measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:RECAllmask?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA:RECAllmask?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``POWer:POWer<x>:SOA:RECAllmask`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SOA:RECAllmask
            - POWer:POWer<x>:SOA:RECAllmask?
            ```

        Sub-properties:
            - ``.filename``: The ``POWer:POWer<x>:SOA:RECAllmask:FILEName`` command.
        """
        return self._recallmask

    @property
    def savemask(self) -> PowerPowerItemSoaSavemask:
        """Return the ``POWer:POWer<x>:SOA:SAVemask`` command.

        Description:
            - This command saves the mask file as per the name configured and at the configured path
              or queries the mask file name, path, and file type for the SOA measurement in the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:SAVemask?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA:SAVemask?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``POWer:POWer<x>:SOA:SAVemask`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SOA:SAVemask
            - POWer:POWer<x>:SOA:SAVemask?
            ```

        Sub-properties:
            - ``.autoincrement``: The ``POWer:POWer<x>:SOA:SAVemask:AUTOINCrement`` command.
            - ``.filename``: The ``POWer:POWer<x>:SOA:SAVemask:FILEName`` command.
            - ``.folder``: The ``POWer:POWer<x>:SOA:SAVemask:FOLDer`` command.
        """
        return self._savemask

    @property
    def vsource(self) -> PowerPowerItemSoaVsource:
        """Return the ``POWer:POWer<x>:SOA:VSOURce`` command.

        Description:
            - This command sets or queries the voltage source for SOA measurement in the specified
              power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA:VSOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA:VSOURce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:SOA:VSOURce value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SOA:VSOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:SOA:VSOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vsource


class PowerPowerItemSequence(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:SEQuence`` command.

    Description:
        - This command sets or queries the run state of a single sequence power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:SEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SEQuence?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:SEQuence value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SEQuence {RUN|RERUN}
        - POWer:POWer<x>:SEQuence?
        ```

    Info:
        - ``POWer<x>`` is the Power measurement identifier number. The number must be for a power
          measurement that requires a single sequence acquisition.
        - ``RUN`` sets the measurement to run an acquisition and acquire data for the specified
          single sequence power measurement.
        - ``RERUN`` sets the measurement to rerun an acquisition and acquire data for the specified
          single sequence power measurement.
    """


class PowerPowerItemSeqsetup(SCPICmdWrite):
    """The ``POWer:POWer<x>:SEQSETup`` command.

    Description:
        - This command sets up the instrument's horizontal, vertical, and trigger parameters to
          optimize for taking the specified power measurement.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:SEQSETup value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:SEQSETup Execute
        ```

    Info:
        - ``POWer<x>`` is the Power measurement identifier number. The number must be for a power
          measurement that requires a single sequence acquisition.
        - ``Execute`` sets the measurement to run an acquisition and acquire data for the specified
          single sequence power measurement.
    """


class PowerPowerItemResultsCurrentacqVrms(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:VRMS`` command.

    Description:
        - This command queries the RMS voltage value for the specified power measurement number. The
          power measurement number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:VRMS? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:VRMS? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:VRMS? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


class PowerPowerItemResultsCurrentacqTrpwr(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:TRPWR`` command.

    Description:
        - This command queries the true power value for the specified power measurement number. The
          power measurement number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:TRPWR? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:TRPWR? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:TRPWR? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


class PowerPowerItemResultsCurrentacqThdr(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:THDR`` command.

    Description:
        - This command queries the total harmonic distortion (RMS) value for the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:THDR? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:THDR? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:THDR? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


class PowerPowerItemResultsCurrentacqThdf(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:THDF`` command.

    Description:
        - This command queries the total harmonic distortion (fundamental) value for the specified
          power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:THDF? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:THDF? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:THDF? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


class PowerPowerItemResultsCurrentacqStddev(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:STDDev`` command.

    Description:
        - This command queries the standard deviation value of the current acquisition for the
          measurement parameter in the specified power measurement number. The power measurement
          number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:STDDev? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:STDDev? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:STDDev? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br|Hc|Hmax|IRipple| DeltaB|DeltaH|Permeability|RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR| PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG|TONLOSS| TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS|TTLENRG|DVBYDT| DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL|PKPK|HIGH|LOW|MAX|MIN |INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
    """  # noqa: E501


class PowerPowerItemResultsCurrentacqStatus(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:STATUS`` command.

    Description:
        - This command queries the status of the measurement for the specified power measurement
          number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:STATUS? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:STATUS? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:STATUS? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


class PowerPowerItemResultsCurrentacqRms(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:RMS`` command.

    Description:
        - This command queries the RMS value of the source selected for the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:RMS? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:RMS? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:RMS? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


class PowerPowerItemResultsCurrentacqPopulation(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:POPUlation`` command.

    Description:
        - This command queries the population (number of complete cycles) of the current acquisition
          for the measurement parameter in the specified power measurement number. The power
          measurement number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:POPUlation? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:POPUlation? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:POPUlation? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br| Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS| VRMS|TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE| AMPL|PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
    """  # noqa: E501


class PowerPowerItemResultsCurrentacqPohcs(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:POHCS`` command.

    Description:
        - This command queries the status of partial odd harmonic current for the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:POHCS? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:POHCS? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:POHCS? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


class PowerPowerItemResultsCurrentacqPohcm(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:POHCM`` command.

    Description:
        - This command queries the measured value of partial odd harmonic current for the specified
          power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:POHCM? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:POHCM? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:POHCM? 'harmonics'
        ```
    """


class PowerPowerItemResultsCurrentacqPohcl(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:POHCL`` command.

    Description:
        - This command queries the limit of partial odd harmonic current for the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:POHCL? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:POHCL? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:POHCL? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


class PowerPowerItemResultsCurrentacqPk2pk(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:PK2PK`` command.

    Description:
        - This command queries the peak-to-peak value of the current acquisition for the measurement
          parameter in the specified power measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:PK2PK? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:PK2PK? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:PK2PK? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br| Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR|APPPWR| REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS| TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS| TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK|SWRIPRMS| SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
        - ``'LRIPPKPK'`` are the parameters for the Line Ripple measurement.
    """  # noqa: E501


class PowerPowerItemResultsCurrentacqMinimum(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum`` command.

    Description:
        - This command queries the minimum value of the current acquisition for the measurement
          parameter in the specified power measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:MINimum? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br| Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS| VRMS|TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL| PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
        - ``'SWRIPPKPK'`` are the parameters for the Switching Ripple measurement.
    """  # noqa: E501


class PowerPowerItemResultsCurrentacqMean(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN`` command.

    Description:
        - This command queries the mean value of the current acquisition for the measurement
          parameter of the specified power measurement <x>.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:MEAN? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS| VRMS|TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE| AMPL|PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
    """  # noqa: E501


class PowerPowerItemResultsCurrentacqMaximum(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum`` command.

    Description:
        - This command queries the maximum value of the current acquisition for the measurement
          parameter in the specified power measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS| Bpeak|Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR| PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS| TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
    """  # noqa: E501


class PowerPowerItemResultsCurrentacqIrms(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:IRMS`` command.

    Description:
        - This command queries the RMS current value for the specified power measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:IRMS? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:IRMS? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:IRMS? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


class PowerPowerItemResultsCurrentacqFrequency(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:FREQUENCY`` command.

    Description:
        - This command queries the fundamental frequency for the specified power measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:FREQUENCY? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:FREQUENCY? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:FREQUENCY? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


class PowerPowerItemResultsCurrentacqF3mag(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:F3MAG`` command.

    Description:
        - This command queries the third harmonics magnitude value for the specified power
          measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:F3MAG? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:F3MAG? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:F3MAG? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


class PowerPowerItemResultsCurrentacqF1mag(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:F1MAG`` command.

    Description:
        - This command queries the first harmonics magnitude value for the specified power
          measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:F1MAG? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:F1MAG? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:F1MAG? 'harmonics'
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
    """


#  pylint: disable=too-many-instance-attributes
class PowerPowerItemResultsCurrentacq(SCPICmdRead):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:RESUlts:CURRentacq?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RESUlts:CURRentacq?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.f1mag``: The ``POWer:POWer<x>:RESUlts:CURRentacq:F1MAG`` command.
        - ``.f3mag``: The ``POWer:POWer<x>:RESUlts:CURRentacq:F3MAG`` command.
        - ``.frequency``: The ``POWer:POWer<x>:RESUlts:CURRentacq:FREQUENCY`` command.
        - ``.irms``: The ``POWer:POWer<x>:RESUlts:CURRentacq:IRMS`` command.
        - ``.maximum``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum`` command.
        - ``.mean``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN`` command.
        - ``.minimum``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum`` command.
        - ``.pk2pk``: The ``POWer:POWer<x>:RESUlts:CURRentacq:PK2PK`` command.
        - ``.pohcl``: The ``POWer:POWer<x>:RESUlts:CURRentacq:POHCL`` command.
        - ``.pohcm``: The ``POWer:POWer<x>:RESUlts:CURRentacq:POHCM`` command.
        - ``.pohcs``: The ``POWer:POWer<x>:RESUlts:CURRentacq:POHCS`` command.
        - ``.population``: The ``POWer:POWer<x>:RESUlts:CURRentacq:POPUlation`` command.
        - ``.rms``: The ``POWer:POWer<x>:RESUlts:CURRentacq:RMS`` command.
        - ``.status``: The ``POWer:POWer<x>:RESUlts:CURRentacq:STATUS`` command.
        - ``.stddev``: The ``POWer:POWer<x>:RESUlts:CURRentacq:STDDev`` command.
        - ``.thdf``: The ``POWer:POWer<x>:RESUlts:CURRentacq:THDF`` command.
        - ``.thdr``: The ``POWer:POWer<x>:RESUlts:CURRentacq:THDR`` command.
        - ``.trpwr``: The ``POWer:POWer<x>:RESUlts:CURRentacq:TRPWR`` command.
        - ``.vrms``: The ``POWer:POWer<x>:RESUlts:CURRentacq:VRMS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._f1mag = PowerPowerItemResultsCurrentacqF1mag(device, f"{self._cmd_syntax}:F1MAG")
        self._f3mag = PowerPowerItemResultsCurrentacqF3mag(device, f"{self._cmd_syntax}:F3MAG")
        self._frequency = PowerPowerItemResultsCurrentacqFrequency(
            device, f"{self._cmd_syntax}:FREQUENCY"
        )
        self._irms = PowerPowerItemResultsCurrentacqIrms(device, f"{self._cmd_syntax}:IRMS")
        self._maximum = PowerPowerItemResultsCurrentacqMaximum(
            device, f"{self._cmd_syntax}:MAXimum"
        )
        self._mean = PowerPowerItemResultsCurrentacqMean(device, f"{self._cmd_syntax}:MEAN")
        self._minimum = PowerPowerItemResultsCurrentacqMinimum(
            device, f"{self._cmd_syntax}:MINimum"
        )
        self._pk2pk = PowerPowerItemResultsCurrentacqPk2pk(device, f"{self._cmd_syntax}:PK2PK")
        self._pohcl = PowerPowerItemResultsCurrentacqPohcl(device, f"{self._cmd_syntax}:POHCL")
        self._pohcm = PowerPowerItemResultsCurrentacqPohcm(device, f"{self._cmd_syntax}:POHCM")
        self._pohcs = PowerPowerItemResultsCurrentacqPohcs(device, f"{self._cmd_syntax}:POHCS")
        self._population = PowerPowerItemResultsCurrentacqPopulation(
            device, f"{self._cmd_syntax}:POPUlation"
        )
        self._rms = PowerPowerItemResultsCurrentacqRms(device, f"{self._cmd_syntax}:RMS")
        self._status = PowerPowerItemResultsCurrentacqStatus(device, f"{self._cmd_syntax}:STATUS")
        self._stddev = PowerPowerItemResultsCurrentacqStddev(device, f"{self._cmd_syntax}:STDDev")
        self._thdf = PowerPowerItemResultsCurrentacqThdf(device, f"{self._cmd_syntax}:THDF")
        self._thdr = PowerPowerItemResultsCurrentacqThdr(device, f"{self._cmd_syntax}:THDR")
        self._trpwr = PowerPowerItemResultsCurrentacqTrpwr(device, f"{self._cmd_syntax}:TRPWR")
        self._vrms = PowerPowerItemResultsCurrentacqVrms(device, f"{self._cmd_syntax}:VRMS")

    @property
    def f1mag(self) -> PowerPowerItemResultsCurrentacqF1mag:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:F1MAG`` command.

        Description:
            - This command queries the first harmonics magnitude value for the specified power
              measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:F1MAG? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:F1MAG? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:F1MAG? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._f1mag

    @property
    def f3mag(self) -> PowerPowerItemResultsCurrentacqF3mag:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:F3MAG`` command.

        Description:
            - This command queries the third harmonics magnitude value for the specified power
              measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:F3MAG? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:F3MAG? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:F3MAG? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._f3mag

    @property
    def frequency(self) -> PowerPowerItemResultsCurrentacqFrequency:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:FREQUENCY`` command.

        Description:
            - This command queries the fundamental frequency for the specified power measurement
              number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:FREQUENCY? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:FREQUENCY? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:FREQUENCY? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._frequency

    @property
    def irms(self) -> PowerPowerItemResultsCurrentacqIrms:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:IRMS`` command.

        Description:
            - This command queries the RMS current value for the specified power measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:IRMS? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:IRMS? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:IRMS? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._irms

    @property
    def maximum(self) -> PowerPowerItemResultsCurrentacqMaximum:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum`` command.

        Description:
            - This command queries the maximum value of the current acquisition for the measurement
              parameter in the specified power measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS| Bpeak|Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR| PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS| TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
        """  # noqa: E501
        return self._maximum

    @property
    def mean(self) -> PowerPowerItemResultsCurrentacqMean:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN`` command.

        Description:
            - This command queries the mean value of the current acquisition for the measurement
              parameter of the specified power measurement <x>.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:MEAN? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS| VRMS|TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE| AMPL|PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
        """  # noqa: E501
        return self._mean

    @property
    def minimum(self) -> PowerPowerItemResultsCurrentacqMinimum:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum`` command.

        Description:
            - This command queries the minimum value of the current acquisition for the measurement
              parameter in the specified power measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:MINimum? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br| Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS| VRMS|TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL| PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
            - ``'SWRIPPKPK'`` are the parameters for the Switching Ripple measurement.
        """  # noqa: E501
        return self._minimum

    @property
    def pk2pk(self) -> PowerPowerItemResultsCurrentacqPk2pk:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:PK2PK`` command.

        Description:
            - This command queries the peak-to-peak value of the current acquisition for the
              measurement parameter in the specified power measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:PK2PK? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:PK2PK? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:PK2PK? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br| Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR|APPPWR| REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS| TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS| TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK|SWRIPRMS| SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
            - ``'LRIPPKPK'`` are the parameters for the Line Ripple measurement.
        """  # noqa: E501
        return self._pk2pk

    @property
    def pohcl(self) -> PowerPowerItemResultsCurrentacqPohcl:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:POHCL`` command.

        Description:
            - This command queries the limit of partial odd harmonic current for the specified power
              measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:POHCL? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:POHCL? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:POHCL? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._pohcl

    @property
    def pohcm(self) -> PowerPowerItemResultsCurrentacqPohcm:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:POHCM`` command.

        Description:
            - This command queries the measured value of partial odd harmonic current for the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:POHCM? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:POHCM? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:POHCM? 'harmonics'
            ```
        """
        return self._pohcm

    @property
    def pohcs(self) -> PowerPowerItemResultsCurrentacqPohcs:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:POHCS`` command.

        Description:
            - This command queries the status of partial odd harmonic current for the specified
              power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:POHCS? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:POHCS? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:POHCS? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._pohcs

    @property
    def population(self) -> PowerPowerItemResultsCurrentacqPopulation:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:POPUlation`` command.

        Description:
            - This command queries the population (number of complete cycles) of the current
              acquisition for the measurement parameter in the specified power measurement number.
              The power measurement number is specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:POPUlation? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:POPUlation? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:POPUlation? {InputPwr| Output1Pwr|Output2Pwr|Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br| Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS| VRMS|TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY|NDUTY|PPULSE|NPULSE| AMPL|PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
        """  # noqa: E501
        return self._population

    @property
    def rms(self) -> PowerPowerItemResultsCurrentacqRms:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:RMS`` command.

        Description:
            - This command queries the RMS value of the source selected for the specified power
              measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:RMS? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:RMS? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:RMS? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._rms

    @property
    def status(self) -> PowerPowerItemResultsCurrentacqStatus:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:STATUS`` command.

        Description:
            - This command queries the status of the measurement for the specified power measurement
              number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:STATUS? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:STATUS? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:STATUS? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._status

    @property
    def stddev(self) -> PowerPowerItemResultsCurrentacqStddev:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:STDDev`` command.

        Description:
            - This command queries the standard deviation value of the current acquisition for the
              measurement parameter in the specified power measurement number. The power measurement
              number is specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:STDDev? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:STDDev? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:STDDev? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br|Hc|Hmax|IRipple| DeltaB|DeltaH|Permeability|RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR| PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG|TONLOSS| TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS|TTLENRG|DVBYDT| DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL|PKPK|HIGH|LOW|MAX|MIN |INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
        """  # noqa: E501
        return self._stddev

    @property
    def thdf(self) -> PowerPowerItemResultsCurrentacqThdf:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:THDF`` command.

        Description:
            - This command queries the total harmonic distortion (fundamental) value for the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:THDF? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:THDF? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:THDF? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._thdf

    @property
    def thdr(self) -> PowerPowerItemResultsCurrentacqThdr:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:THDR`` command.

        Description:
            - This command queries the total harmonic distortion (RMS) value for the specified power
              measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:THDR? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:THDR? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:THDR? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._thdr

    @property
    def trpwr(self) -> PowerPowerItemResultsCurrentacqTrpwr:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:TRPWR`` command.

        Description:
            - This command queries the true power value for the specified power measurement number.
              The power measurement number is specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:TRPWR? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:TRPWR? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:TRPWR? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._trpwr

    @property
    def vrms(self) -> PowerPowerItemResultsCurrentacqVrms:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:VRMS`` command.

        Description:
            - This command queries the RMS voltage value for the specified power measurement number.
              The power measurement number is specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:VRMS? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:VRMS? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:VRMS? 'harmonics'
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
        """
        return self._vrms


class PowerPowerItemResultsAllacqsStddev(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:ALLAcqs:STDDev`` command.

    Description:
        - This command queries the standard deviation value of all acquisitions for the measurement
          parameter in the specified power measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:STDDev? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:STDDev? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:ALLAcqs:STDDev? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br|Hc| Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS| TRUEPWR|APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ| ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG|TONLOSS| TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS| TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS| LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY| NDUTY|PPULSE|NPULSE|AMPL|PKPK|HIGH|LOW|MAX|MIN| INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
    """  # noqa: E501


class PowerPowerItemResultsAllacqsPopulation(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:ALLAcqs:POPUlation`` command.

    Description:
        - This command queries the population (number of complete cycles) of all acquisitions for
          the measurement parameter in the specified power measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:POPUlation? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:POPUlation? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:ALLAcqs:POPUlation? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR| PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS| TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE| AMPL|PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
    """  # noqa: E501


class PowerPowerItemResultsAllacqsPk2pk(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:ALLAcqs:PK2PK`` command.

    Description:
        - This command queries the peak-to-peak value of all acquisitions for the measurement
          parameter in the specified power measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:PK2PK? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:PK2PK? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:ALLAcqs:PK2PK? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR| PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR| IRMS|VRMS|TONENRG|TONLOSS|TOFFENRG| TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS|TTLENRG| DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY| NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
        - ``'SWRIPPKPK'`` are the parameters for the Switching Ripple measurement.
    """  # noqa: E501


class PowerPowerItemResultsAllacqsMinimum(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:ALLAcqs:MINimum`` command.

    Description:
        - This command queries the minimum value of all acquisitions for the measurement parameter
          of the specified power measurement <x>.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:MINimum? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:MINimum? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:ALLAcqs:MINimum? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS| Bpeak|Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR| PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR| IRMS|VRMS|TONENRG|TONLOSS|TOFFENRG| TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS|TTLENRG| DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY| NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
    """  # noqa: E501


class PowerPowerItemResultsAllacqsMean(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:ALLAcqs:MEAN`` command.

    Description:
        - This command queries the mean value of all acquisitions for the measurement parameter in
          the specified power measurement number <x>.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:MEAN? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:MEAN? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:ALLAcqs:MEAN? {InputPwr|Output1Pwr|Output2Pwr| Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency| INDUCT|IVSINTV|MAGLOSS|Bpeak|Br|Hc|Hmax| IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ| ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG| TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL| PKPK|HIGH|LOW|MAX|MIN| INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
    """  # noqa: E501


class PowerPowerItemResultsAllacqsMaximum(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:ALLAcqs:MAXimum`` command.

    Description:
        - This command queries the maximum value of all acquisitions for the measurement parameter
          in the specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:MAXimum? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:ALLAcqs:MAXimum? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:ALLAcqs:MAXimum? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability| RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR|PHASE| PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG| TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL| PKPK|HIGH|LOW|MAX|MIN| INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<QString>`` = the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
    """  # noqa: E501


class PowerPowerItemResultsAllacqs(SCPICmdRead):
    """The ``POWer:POWer<x>:RESUlts:ALLAcqs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:RESUlts:ALLAcqs?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RESUlts:ALLAcqs?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.maximum``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:MAXimum`` command.
        - ``.mean``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:MEAN`` command.
        - ``.minimum``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:MINimum`` command.
        - ``.pk2pk``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:PK2PK`` command.
        - ``.population``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:POPUlation`` command.
        - ``.stddev``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:STDDev`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._maximum = PowerPowerItemResultsAllacqsMaximum(device, f"{self._cmd_syntax}:MAXimum")
        self._mean = PowerPowerItemResultsAllacqsMean(device, f"{self._cmd_syntax}:MEAN")
        self._minimum = PowerPowerItemResultsAllacqsMinimum(device, f"{self._cmd_syntax}:MINimum")
        self._pk2pk = PowerPowerItemResultsAllacqsPk2pk(device, f"{self._cmd_syntax}:PK2PK")
        self._population = PowerPowerItemResultsAllacqsPopulation(
            device, f"{self._cmd_syntax}:POPUlation"
        )
        self._stddev = PowerPowerItemResultsAllacqsStddev(device, f"{self._cmd_syntax}:STDDev")

    @property
    def maximum(self) -> PowerPowerItemResultsAllacqsMaximum:
        """Return the ``POWer:POWer<x>:RESUlts:ALLAcqs:MAXimum`` command.

        Description:
            - This command queries the maximum value of all acquisitions for the measurement
              parameter in the specified power measurement number. The power measurement number is
              specified by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:MAXimum? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:MAXimum? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:ALLAcqs:MAXimum? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH|Permeability| RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR|PHASE| PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG| TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL| PKPK|HIGH|LOW|MAX|MIN| INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
        """  # noqa: E501
        return self._maximum

    @property
    def mean(self) -> PowerPowerItemResultsAllacqsMean:
        """Return the ``POWer:POWer<x>:RESUlts:ALLAcqs:MEAN`` command.

        Description:
            - This command queries the mean value of all acquisitions for the measurement parameter
              in the specified power measurement number <x>.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:MEAN? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:MEAN? argument`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:ALLAcqs:MEAN? {InputPwr|Output1Pwr|Output2Pwr| Output3Pwr|Efficiency1|Efficiency2| Efficiency3|TotalEfficiency| INDUCT|IVSINTV|MAGLOSS|Bpeak|Br|Hc|Hmax| IRipple|DeltaB|DeltaH|Permeability|RDS|TRUEPWR| APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ| ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG| TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE|AMPL| PKPK|HIGH|LOW|MAX|MIN| INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
        """  # noqa: E501
        return self._mean

    @property
    def minimum(self) -> PowerPowerItemResultsAllacqsMinimum:
        """Return the ``POWer:POWer<x>:RESUlts:ALLAcqs:MINimum`` command.

        Description:
            - This command queries the minimum value of all acquisitions for the measurement
              parameter of the specified power measurement <x>.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:MINimum? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:MINimum? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:ALLAcqs:MINimum? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS| Bpeak|Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR| PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR| IRMS|VRMS|TONENRG|TONLOSS|TOFFENRG| TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS|TTLENRG| DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY| NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
        """  # noqa: E501
        return self._minimum

    @property
    def pk2pk(self) -> PowerPowerItemResultsAllacqsPk2pk:
        """Return the ``POWer:POWer<x>:RESUlts:ALLAcqs:PK2PK`` command.

        Description:
            - This command queries the peak-to-peak value of all acquisitions for the measurement
              parameter in the specified power measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:PK2PK? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:PK2PK? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:ALLAcqs:PK2PK? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR| PWRFACTOR|PHASE|PWRFREQ|ICFACTOR|VCFACTOR| IRMS|VRMS|TONENRG|TONLOSS|TOFFENRG| TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS|TTLENRG| DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS|LRIPPKPK| SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY| NDUTY|PPULSE|NPULSE|AMPL|PKPK| HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
            - ``'SWRIPPKPK'`` are the parameters for the Switching Ripple measurement.
        """  # noqa: E501
        return self._pk2pk

    @property
    def population(self) -> PowerPowerItemResultsAllacqsPopulation:
        """Return the ``POWer:POWer<x>:RESUlts:ALLAcqs:POPUlation`` command.

        Description:
            - This command queries the population (number of complete cycles) of all acquisitions
              for the measurement parameter in the specified power measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:POPUlation? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:POPUlation? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:ALLAcqs:POPUlation? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak| Br|Hc|Hmax|IRipple|DeltaB|DeltaH| Permeability|RDS|TRUEPWR|APPPWR|REPWR|PWRFACTOR| PHASE|PWRFREQ|ICFACTOR|VCFACTOR|IRMS|VRMS| TONENRG|TONLOSS|TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS| TTLLOSS|TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT| LRIPRMS|LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD| FREQ|PDUTY|NDUTY|PPULSE|NPULSE| AMPL|PKPK|HIGH|LOW|MAX|MIN|INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
        """  # noqa: E501
        return self._population

    @property
    def stddev(self) -> PowerPowerItemResultsAllacqsStddev:
        """Return the ``POWer:POWer<x>:RESUlts:ALLAcqs:STDDev`` command.

        Description:
            - This command queries the standard deviation value of all acquisitions for the
              measurement parameter in the specified power measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:STDDev? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:ALLAcqs:STDDev? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:ALLAcqs:STDDev? {InputPwr|Output1Pwr| Output2Pwr|Output3Pwr|Efficiency1|Efficiency2|Efficiency3| TotalEfficiency|INDUCT|IVSINTV|MAGLOSS|Bpeak|Br|Hc| Hmax|IRipple|DeltaB|DeltaH|Permeability|RDS| TRUEPWR|APPPWR|REPWR|PWRFACTOR|PHASE|PWRFREQ| ICFACTOR|VCFACTOR|IRMS|VRMS|TONENRG|TONLOSS| TOFFENRG|TOFFLOSS|CONDENRG|CONDLOSS|TTLLOSS| TTLENRG|DVBYDT|DIBYDT|SOAHITSCNT|LRIPRMS| LRIPPKPK|SWRIPRMS|SWRIPPKPK|PRIOD|FREQ|PDUTY| NDUTY|PPULSE|NPULSE|AMPL|PKPK|HIGH|LOW|MAX|MIN| INRUSH|CAPACITANCE|OUTPUT1| OUTPUT2|OUTPUT3|OUTPUT4|OUTPUT5|OUTPUT6|OUTPUT7| GAINCROSSOVERFREQ|PHASECROSSOVERFREQ|GM|PM| MAXPSRR|MAXPSRRFREQ|MINPSRR|MINPSRRFREQ}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<QString>`` = the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
        """  # noqa: E501
        return self._stddev


class PowerPowerItemResults(SCPICmdRead):
    """The ``POWer:POWer<x>:RESUlts`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:RESUlts?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RESUlts?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.allacqs``: The ``POWer:POWer<x>:RESUlts:ALLAcqs`` command tree.
        - ``.currentacq``: The ``POWer:POWer<x>:RESUlts:CURRentacq`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._allacqs = PowerPowerItemResultsAllacqs(device, f"{self._cmd_syntax}:ALLAcqs")
        self._currentacq = PowerPowerItemResultsCurrentacq(device, f"{self._cmd_syntax}:CURRentacq")

    @property
    def allacqs(self) -> PowerPowerItemResultsAllacqs:
        """Return the ``POWer:POWer<x>:RESUlts:ALLAcqs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:RESUlts:ALLAcqs?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RESUlts:ALLAcqs?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.maximum``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:MAXimum`` command.
            - ``.mean``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:MEAN`` command.
            - ``.minimum``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:MINimum`` command.
            - ``.pk2pk``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:PK2PK`` command.
            - ``.population``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:POPUlation`` command.
            - ``.stddev``: The ``POWer:POWer<x>:RESUlts:ALLAcqs:STDDev`` command.
        """
        return self._allacqs

    @property
    def currentacq(self) -> PowerPowerItemResultsCurrentacq:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:RESUlts:CURRentacq?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.f1mag``: The ``POWer:POWer<x>:RESUlts:CURRentacq:F1MAG`` command.
            - ``.f3mag``: The ``POWer:POWer<x>:RESUlts:CURRentacq:F3MAG`` command.
            - ``.frequency``: The ``POWer:POWer<x>:RESUlts:CURRentacq:FREQUENCY`` command.
            - ``.irms``: The ``POWer:POWer<x>:RESUlts:CURRentacq:IRMS`` command.
            - ``.maximum``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum`` command.
            - ``.mean``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN`` command.
            - ``.minimum``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum`` command.
            - ``.pk2pk``: The ``POWer:POWer<x>:RESUlts:CURRentacq:PK2PK`` command.
            - ``.pohcl``: The ``POWer:POWer<x>:RESUlts:CURRentacq:POHCL`` command.
            - ``.pohcm``: The ``POWer:POWer<x>:RESUlts:CURRentacq:POHCM`` command.
            - ``.pohcs``: The ``POWer:POWer<x>:RESUlts:CURRentacq:POHCS`` command.
            - ``.population``: The ``POWer:POWer<x>:RESUlts:CURRentacq:POPUlation`` command.
            - ``.rms``: The ``POWer:POWer<x>:RESUlts:CURRentacq:RMS`` command.
            - ``.status``: The ``POWer:POWer<x>:RESUlts:CURRentacq:STATUS`` command.
            - ``.stddev``: The ``POWer:POWer<x>:RESUlts:CURRentacq:STDDev`` command.
            - ``.thdf``: The ``POWer:POWer<x>:RESUlts:CURRentacq:THDF`` command.
            - ``.thdr``: The ``POWer:POWer<x>:RESUlts:CURRentacq:THDR`` command.
            - ``.trpwr``: The ``POWer:POWer<x>:RESUlts:CURRentacq:TRPWR`` command.
            - ``.vrms``: The ``POWer:POWer<x>:RESUlts:CURRentacq:VRMS`` command.
        """
        return self._currentacq


class PowerPowerItemReflevelsPercentType(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:PERCent:TYPE`` command.

    Description:
        - This command sets or queries the reference levels for the specified power measurement
          number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:PERCent:TYPE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:TYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:TYPE value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
        - POWer:POWer<x>:REFLevels:PERCent:TYPE?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``TENNinety`` to set the low reference levels as 10% and high reference levels as 90%.
        - ``TWENtyeighty`` to set the low reference levels as 20% and high reference levels as 80%.
        - ``CUSTom`` to set the custom low, high, and mid reference levels for rising and falling
          edges.
    """


class PowerPowerItemReflevelsPercentRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:PERCent:RISEMid`` command.

    Description:
        - This command sets or queries the rising edge for mid reference level in percentage for the
          specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:PERCent:RISEMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:RISEMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:RISEMid value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:PERCent:RISEMid <NR1>
        - POWer:POWer<x>:REFLevels:PERCent:RISEMid?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 1 to 99.
    """


class PowerPowerItemReflevelsPercentRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:PERCent:RISELow`` command.

    Description:
        - This command sets or queries the rising edge for low reference level in percentage for the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:PERCent:RISELow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:RISELow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:RISELow value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:PERCent:RISELow <NR1>
        - POWer:POWer<x>:REFLevels:PERCent:RISELow?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 1 to 99.
    """


class PowerPowerItemReflevelsPercentRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:PERCent:RISEHigh`` command.

    Description:
        - This command sets or queries the rising edge for high reference level in percentage for
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:PERCent:RISEHigh?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:RISEHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:PERCent:RISEHigh <NR1>
        - POWer:POWer<x>:REFLevels:PERCent:RISEHigh?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 1 to 99.
    """


class PowerPowerItemReflevelsPercentHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:PERCent:HYSTeresis`` command.

    Description:
        - This command sets or queries the hysteresis in percentage for the specified power
          measurement number.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:HYSTeresis?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:PERCent:HYSTeresis <NR1>
        - POWer:POWer<x>:REFLevels:PERCent:HYSTeresis?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 1 to 99.
    """


class PowerPowerItemReflevelsPercentFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:PERCent:FALLMid`` command.

    Description:
        - This command sets or queries the falling edge for mid reference level in percentage for
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:PERCent:FALLMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:FALLMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:FALLMid value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:PERCent:FALLMid <NR1>
        - POWer:POWer<x>:REFLevels:PERCent:FALLMid?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 1 to 99.
    """


class PowerPowerItemReflevelsPercentFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:PERCent:FALLLow`` command.

    Description:
        - This command sets or queries the falling edge for low reference level in percentage for
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:PERCent:FALLLow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:FALLLow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:FALLLow value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:PERCent:FALLLow <NR1>
        - POWer:POWer<x>:REFLevels:PERCent:FALLLow?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 1 to 99.
    """


class PowerPowerItemReflevelsPercentFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:PERCent:FALLHigh`` command.

    Description:
        - This command sets or queries the falling edge for high reference level in percentage for
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:PERCent:FALLHigh?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:FALLHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:PERCent:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:PERCent:FALLHigh <NR1>
        - POWer:POWer<x>:REFLevels:PERCent:FALLHigh?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 1 to 99.
    """


#  pylint: disable=too-many-instance-attributes
class PowerPowerItemReflevelsPercent(SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:PERCent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:PERCent?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:REFLevels:PERCent?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fallhigh``: The ``POWer:POWer<x>:REFLevels:PERCent:FALLHigh`` command.
        - ``.falllow``: The ``POWer:POWer<x>:REFLevels:PERCent:FALLLow`` command.
        - ``.fallmid``: The ``POWer:POWer<x>:REFLevels:PERCent:FALLMid`` command.
        - ``.hysteresis``: The ``POWer:POWer<x>:REFLevels:PERCent:HYSTeresis`` command.
        - ``.risehigh``: The ``POWer:POWer<x>:REFLevels:PERCent:RISEHigh`` command.
        - ``.riselow``: The ``POWer:POWer<x>:REFLevels:PERCent:RISELow`` command.
        - ``.risemid``: The ``POWer:POWer<x>:REFLevels:PERCent:RISEMid`` command.
        - ``.type``: The ``POWer:POWer<x>:REFLevels:PERCent:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = PowerPowerItemReflevelsPercentFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = PowerPowerItemReflevelsPercentFalllow(device, f"{self._cmd_syntax}:FALLLow")
        self._fallmid = PowerPowerItemReflevelsPercentFallmid(device, f"{self._cmd_syntax}:FALLMid")
        self._hysteresis = PowerPowerItemReflevelsPercentHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = PowerPowerItemReflevelsPercentRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = PowerPowerItemReflevelsPercentRiselow(device, f"{self._cmd_syntax}:RISELow")
        self._risemid = PowerPowerItemReflevelsPercentRisemid(device, f"{self._cmd_syntax}:RISEMid")
        self._type = PowerPowerItemReflevelsPercentType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def fallhigh(self) -> PowerPowerItemReflevelsPercentFallhigh:
        """Return the ``POWer:POWer<x>:REFLevels:PERCent:FALLHigh`` command.

        Description:
            - This command sets or queries the falling edge for high reference level in percentage
              for the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:FALLHigh?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:PERCent:FALLHigh <NR1>
            - POWer:POWer<x>:REFLevels:PERCent:FALLHigh?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 1 to 99.
        """
        return self._fallhigh

    @property
    def falllow(self) -> PowerPowerItemReflevelsPercentFalllow:
        """Return the ``POWer:POWer<x>:REFLevels:PERCent:FALLLow`` command.

        Description:
            - This command sets or queries the falling edge for low reference level in percentage
              for the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:FALLLow?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:FALLLow value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:PERCent:FALLLow <NR1>
            - POWer:POWer<x>:REFLevels:PERCent:FALLLow?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 1 to 99.
        """
        return self._falllow

    @property
    def fallmid(self) -> PowerPowerItemReflevelsPercentFallmid:
        """Return the ``POWer:POWer<x>:REFLevels:PERCent:FALLMid`` command.

        Description:
            - This command sets or queries the falling edge for mid reference level in percentage
              for the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:FALLMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:FALLMid value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:PERCent:FALLMid <NR1>
            - POWer:POWer<x>:REFLevels:PERCent:FALLMid?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 1 to 99.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> PowerPowerItemReflevelsPercentHysteresis:
        """Return the ``POWer:POWer<x>:REFLevels:PERCent:HYSTeresis`` command.

        Description:
            - This command sets or queries the hysteresis in percentage for the specified power
              measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:HYSTeresis?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:PERCent:HYSTeresis <NR1>
            - POWer:POWer<x>:REFLevels:PERCent:HYSTeresis?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 1 to 99.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> PowerPowerItemReflevelsPercentRisehigh:
        """Return the ``POWer:POWer<x>:REFLevels:PERCent:RISEHigh`` command.

        Description:
            - This command sets or queries the rising edge for high reference level in percentage
              for the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:RISEHigh?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:PERCent:RISEHigh <NR1>
            - POWer:POWer<x>:REFLevels:PERCent:RISEHigh?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 1 to 99.
        """
        return self._risehigh

    @property
    def riselow(self) -> PowerPowerItemReflevelsPercentRiselow:
        """Return the ``POWer:POWer<x>:REFLevels:PERCent:RISELow`` command.

        Description:
            - This command sets or queries the rising edge for low reference level in percentage for
              the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:RISELow?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:RISELow value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:PERCent:RISELow <NR1>
            - POWer:POWer<x>:REFLevels:PERCent:RISELow?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 1 to 99.
        """
        return self._riselow

    @property
    def risemid(self) -> PowerPowerItemReflevelsPercentRisemid:
        """Return the ``POWer:POWer<x>:REFLevels:PERCent:RISEMid`` command.

        Description:
            - This command sets or queries the rising edge for mid reference level in percentage for
              the specified power measurement number. The power measurement number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:RISEMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:RISEMid value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:PERCent:RISEMid <NR1>
            - POWer:POWer<x>:REFLevels:PERCent:RISEMid?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 1 to 99.
        """
        return self._risemid

    @property
    def type(self) -> PowerPowerItemReflevelsPercentType:
        """Return the ``POWer:POWer<x>:REFLevels:PERCent:TYPE`` command.

        Description:
            - This command sets or queries the reference levels for the specified power measurement
              number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:PERCent:TYPE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:TYPE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent:TYPE value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:PERCent:TYPE {TENNinety|TWENtyeighty|CUSTom}
            - POWer:POWer<x>:REFLevels:PERCent:TYPE?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``TENNinety`` to set the low reference levels as 10% and high reference levels as 90%.
            - ``TWENtyeighty`` to set the low reference levels as 20% and high reference levels as
              80%.
            - ``CUSTom`` to set the custom low, high, and mid reference levels for rising and
              falling edges.
        """
        return self._type


class PowerPowerItemReflevelsMethod(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:METHod`` command.

    Description:
        - This command sets or queries the method to configure reference level values for the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:METHod?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:REFLevels:METHod?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:REFLevels:METHod value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:METHod {PERCent|ABSolute}
        - POWer:POWer<x>:REFLevels:METHod?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``PERCent`` sets the power measurement to use absolute values to configure reference level
          values.
        - ``ABSolute`` sets the power measurement to use percentage to configure reference level
          values.
    """


class PowerPowerItemReflevelsBasetop(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:BASETop`` command.

    Description:
        - This command sets or queries the reference level base top method for the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:BASETop?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:REFLevels:BASETop?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:BASETop value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
        - POWer:POWer<x>:REFLevels:BASETop?
        ```
    """


class PowerPowerItemReflevelsAbsoluteType(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:ABSolute:TYPE`` command.

    Description:
        - This command sets or queries the type of measurement levels when reference level is set to
          absolute for the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:ABSolute:TYPE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:TYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:TYPE value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
        - POWer:POWer<x>:REFLevels:ABSolute:TYPE?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``SAME`` : select when the rising edge and falling edge reference levels are same.
        - ``UNIQue`` : select when the rising edge and falling edge reference levels are different.
    """


class PowerPowerItemReflevelsAbsoluteRisemid(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:ABSolute:RISEMid`` command.

    Description:
        - This command sets or queries the rising edge for mid reference level in absolute units for
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:ABSolute:RISEMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:RISEMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:RISEMid value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:ABSolute:RISEMid <NR1>
        - POWer:POWer<x>:REFLevels:ABSolute:RISEMid?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from -40000 to 40000.
    """


class PowerPowerItemReflevelsAbsoluteRiselow(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:ABSolute:RISELow`` command.

    Description:
        - This command sets or queries the rising edge for low reference level in absolute units for
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:ABSolute:RISELow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:RISELow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:RISELow value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:ABSolute:RISELow <NR1>
        - POWer:POWer<x>:REFLevels:ABSolute:RISELow?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from -40000 to 40000.
    """


class PowerPowerItemReflevelsAbsoluteRisehigh(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:ABSolute:RISEHigh`` command.

    Description:
        - This command sets or queries the rising edge for high reference level in absolute units
          for the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:RISEHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:RISEHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:RISEHigh value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:ABSolute:RISEHigh <NR1>
        - POWer:POWer<x>:REFLevels:ABSolute:RISEHigh?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from -40000 to 40000.
    """


class PowerPowerItemReflevelsAbsoluteHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis`` command.

    Description:
        - This command sets or queries the absolute hysteresis value for the specified power
          measurement number.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis <NR1>
        - POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from 0.0000005 to 10.
    """


class PowerPowerItemReflevelsAbsoluteFallmid(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:ABSolute:FALLMid`` command.

    Description:
        - This command sets or queries the falling edge for mid reference level in absolute units
          for the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:ABSolute:FALLMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:FALLMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:FALLMid value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:ABSolute:FALLMid <NR1>
        - POWer:POWer<x>:REFLevels:ABSolute:FALLMid?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from -40000 to 40000.
    """


class PowerPowerItemReflevelsAbsoluteFalllow(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:ABSolute:FALLLow`` command.

    Description:
        - This command sets or queries the falling edge for low reference level in absolute units
          for the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:ABSolute:FALLLow?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:FALLLow?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:FALLLow value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:ABSolute:FALLLow <NR1>
        - POWer:POWer<x>:REFLevels:ABSolute:FALLLow?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from -40000 to 40000.
    """


class PowerPowerItemReflevelsAbsoluteFallhigh(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:ABSolute:FALLHigh`` command.

    Description:
        - This command sets or queries the falling edge for high reference level in absolute units
          for the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:FALLHigh?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:REFLevels:ABSolute:FALLHigh value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:REFLevels:ABSolute:FALLHigh <NR1>
        - POWer:POWer<x>:REFLevels:ABSolute:FALLHigh?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR1>`` ranges from -40000 to 40000.
    """


#  pylint: disable=too-many-instance-attributes
class PowerPowerItemReflevelsAbsolute(SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels:ABSolute`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:ABSolute?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:REFLevels:ABSolute?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fallhigh``: The ``POWer:POWer<x>:REFLevels:ABSolute:FALLHigh`` command.
        - ``.falllow``: The ``POWer:POWer<x>:REFLevels:ABSolute:FALLLow`` command.
        - ``.fallmid``: The ``POWer:POWer<x>:REFLevels:ABSolute:FALLMid`` command.
        - ``.hysteresis``: The ``POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis`` command.
        - ``.risehigh``: The ``POWer:POWer<x>:REFLevels:ABSolute:RISEHigh`` command.
        - ``.riselow``: The ``POWer:POWer<x>:REFLevels:ABSolute:RISELow`` command.
        - ``.risemid``: The ``POWer:POWer<x>:REFLevels:ABSolute:RISEMid`` command.
        - ``.type``: The ``POWer:POWer<x>:REFLevels:ABSolute:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fallhigh = PowerPowerItemReflevelsAbsoluteFallhigh(
            device, f"{self._cmd_syntax}:FALLHigh"
        )
        self._falllow = PowerPowerItemReflevelsAbsoluteFalllow(
            device, f"{self._cmd_syntax}:FALLLow"
        )
        self._fallmid = PowerPowerItemReflevelsAbsoluteFallmid(
            device, f"{self._cmd_syntax}:FALLMid"
        )
        self._hysteresis = PowerPowerItemReflevelsAbsoluteHysteresis(
            device, f"{self._cmd_syntax}:HYSTeresis"
        )
        self._risehigh = PowerPowerItemReflevelsAbsoluteRisehigh(
            device, f"{self._cmd_syntax}:RISEHigh"
        )
        self._riselow = PowerPowerItemReflevelsAbsoluteRiselow(
            device, f"{self._cmd_syntax}:RISELow"
        )
        self._risemid = PowerPowerItemReflevelsAbsoluteRisemid(
            device, f"{self._cmd_syntax}:RISEMid"
        )
        self._type = PowerPowerItemReflevelsAbsoluteType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def fallhigh(self) -> PowerPowerItemReflevelsAbsoluteFallhigh:
        """Return the ``POWer:POWer<x>:REFLevels:ABSolute:FALLHigh`` command.

        Description:
            - This command sets or queries the falling edge for high reference level in absolute
              units for the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:FALLHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:FALLHigh?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:FALLHigh value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:ABSolute:FALLHigh <NR1>
            - POWer:POWer<x>:REFLevels:ABSolute:FALLHigh?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from -40000 to 40000.
        """
        return self._fallhigh

    @property
    def falllow(self) -> PowerPowerItemReflevelsAbsoluteFalllow:
        """Return the ``POWer:POWer<x>:REFLevels:ABSolute:FALLLow`` command.

        Description:
            - This command sets or queries the falling edge for low reference level in absolute
              units for the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:FALLLow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:FALLLow?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:FALLLow value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:ABSolute:FALLLow <NR1>
            - POWer:POWer<x>:REFLevels:ABSolute:FALLLow?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from -40000 to 40000.
        """
        return self._falllow

    @property
    def fallmid(self) -> PowerPowerItemReflevelsAbsoluteFallmid:
        """Return the ``POWer:POWer<x>:REFLevels:ABSolute:FALLMid`` command.

        Description:
            - This command sets or queries the falling edge for mid reference level in absolute
              units for the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:FALLMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:FALLMid?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:FALLMid value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:ABSolute:FALLMid <NR1>
            - POWer:POWer<x>:REFLevels:ABSolute:FALLMid?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from -40000 to 40000.
        """
        return self._fallmid

    @property
    def hysteresis(self) -> PowerPowerItemReflevelsAbsoluteHysteresis:
        """Return the ``POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis`` command.

        Description:
            - This command sets or queries the absolute hysteresis value for the specified power
              measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis <NR1>
            - POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from 0.0000005 to 10.
        """
        return self._hysteresis

    @property
    def risehigh(self) -> PowerPowerItemReflevelsAbsoluteRisehigh:
        """Return the ``POWer:POWer<x>:REFLevels:ABSolute:RISEHigh`` command.

        Description:
            - This command sets or queries the rising edge for high reference level in absolute
              units for the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:RISEHigh?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:RISEHigh?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:RISEHigh value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:ABSolute:RISEHigh <NR1>
            - POWer:POWer<x>:REFLevels:ABSolute:RISEHigh?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from -40000 to 40000.
        """
        return self._risehigh

    @property
    def riselow(self) -> PowerPowerItemReflevelsAbsoluteRiselow:
        """Return the ``POWer:POWer<x>:REFLevels:ABSolute:RISELow`` command.

        Description:
            - This command sets or queries the rising edge for low reference level in absolute units
              for the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:RISELow?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:RISELow?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:RISELow value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:ABSolute:RISELow <NR1>
            - POWer:POWer<x>:REFLevels:ABSolute:RISELow?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from -40000 to 40000.
        """
        return self._riselow

    @property
    def risemid(self) -> PowerPowerItemReflevelsAbsoluteRisemid:
        """Return the ``POWer:POWer<x>:REFLevels:ABSolute:RISEMid`` command.

        Description:
            - This command sets or queries the rising edge for mid reference level in absolute units
              for the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:RISEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:RISEMid?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:RISEMid value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:ABSolute:RISEMid <NR1>
            - POWer:POWer<x>:REFLevels:ABSolute:RISEMid?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR1>`` ranges from -40000 to 40000.
        """
        return self._risemid

    @property
    def type(self) -> PowerPowerItemReflevelsAbsoluteType:
        """Return the ``POWer:POWer<x>:REFLevels:ABSolute:TYPE`` command.

        Description:
            - This command sets or queries the type of measurement levels when reference level is
              set to absolute for the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:TYPE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute:TYPE value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:ABSolute:TYPE {SAME|UNIQue}
            - POWer:POWer<x>:REFLevels:ABSolute:TYPE?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``SAME`` : select when the rising edge and falling edge reference levels are same.
            - ``UNIQue`` : select when the rising edge and falling edge reference levels are
              different.
        """
        return self._type


class PowerPowerItemReflevels(SCPICmdRead):
    """The ``POWer:POWer<x>:REFLevels`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:REFLevels?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absolute``: The ``POWer:POWer<x>:REFLevels:ABSolute`` command tree.
        - ``.basetop``: The ``POWer:POWer<x>:REFLevels:BASETop`` command.
        - ``.method``: The ``POWer:POWer<x>:REFLevels:METHod`` command.
        - ``.percent``: The ``POWer:POWer<x>:REFLevels:PERCent`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = PowerPowerItemReflevelsAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._basetop = PowerPowerItemReflevelsBasetop(device, f"{self._cmd_syntax}:BASETop")
        self._method = PowerPowerItemReflevelsMethod(device, f"{self._cmd_syntax}:METHod")
        self._percent = PowerPowerItemReflevelsPercent(device, f"{self._cmd_syntax}:PERCent")

    @property
    def absolute(self) -> PowerPowerItemReflevelsAbsolute:
        """Return the ``POWer:POWer<x>:REFLevels:ABSolute`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:ABSolute?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:ABSolute?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.fallhigh``: The ``POWer:POWer<x>:REFLevels:ABSolute:FALLHigh`` command.
            - ``.falllow``: The ``POWer:POWer<x>:REFLevels:ABSolute:FALLLow`` command.
            - ``.fallmid``: The ``POWer:POWer<x>:REFLevels:ABSolute:FALLMid`` command.
            - ``.hysteresis``: The ``POWer:POWer<x>:REFLevels:ABSolute:HYSTeresis`` command.
            - ``.risehigh``: The ``POWer:POWer<x>:REFLevels:ABSolute:RISEHigh`` command.
            - ``.riselow``: The ``POWer:POWer<x>:REFLevels:ABSolute:RISELow`` command.
            - ``.risemid``: The ``POWer:POWer<x>:REFLevels:ABSolute:RISEMid`` command.
            - ``.type``: The ``POWer:POWer<x>:REFLevels:ABSolute:TYPE`` command.
        """
        return self._absolute

    @property
    def basetop(self) -> PowerPowerItemReflevelsBasetop:
        """Return the ``POWer:POWer<x>:REFLevels:BASETop`` command.

        Description:
            - This command sets or queries the reference level base top method for the specified
              power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:BASETop?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:BASETop?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:BASETop value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:BASETop {AUTO|MINMax|MEANhistogram|MODEhistogram|EYEhistogram}
            - POWer:POWer<x>:REFLevels:BASETop?
            ```
        """  # noqa: E501
        return self._basetop

    @property
    def method(self) -> PowerPowerItemReflevelsMethod:
        """Return the ``POWer:POWer<x>:REFLevels:METHod`` command.

        Description:
            - This command sets or queries the method to configure reference level values for the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:METHod?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:REFLevels:METHod?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:METHod value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:REFLevels:METHod {PERCent|ABSolute}
            - POWer:POWer<x>:REFLevels:METHod?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``PERCent`` sets the power measurement to use absolute values to configure reference
              level values.
            - ``ABSolute`` sets the power measurement to use percentage to configure reference level
              values.
        """
        return self._method

    @property
    def percent(self) -> PowerPowerItemReflevelsPercent:
        """Return the ``POWer:POWer<x>:REFLevels:PERCent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels:PERCent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:REFLevels:PERCent?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.fallhigh``: The ``POWer:POWer<x>:REFLevels:PERCent:FALLHigh`` command.
            - ``.falllow``: The ``POWer:POWer<x>:REFLevels:PERCent:FALLLow`` command.
            - ``.fallmid``: The ``POWer:POWer<x>:REFLevels:PERCent:FALLMid`` command.
            - ``.hysteresis``: The ``POWer:POWer<x>:REFLevels:PERCent:HYSTeresis`` command.
            - ``.risehigh``: The ``POWer:POWer<x>:REFLevels:PERCent:RISEHigh`` command.
            - ``.riselow``: The ``POWer:POWer<x>:REFLevels:PERCent:RISELow`` command.
            - ``.risemid``: The ``POWer:POWer<x>:REFLevels:PERCent:RISEMid`` command.
            - ``.type``: The ``POWer:POWer<x>:REFLevels:PERCent:TYPE`` command.
        """
        return self._percent


class PowerPowerItemRdsonVsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:RDSON:VSOURce`` command.

    Description:
        - This command sets or queries the voltage source for RDSon measurement of the specified
          power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:RDSON:VSOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RDSON:VSOURce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:RDSON:VSOURce value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RDSON:VSOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:RDSON:VSOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemRdsonIsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:RDSON:ISOURce`` command.

    Description:
        - This command sets or queries the current source for RDSon measurement of the specified
          power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:RDSON:ISOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RDSON:ISOURce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:RDSON:ISOURce value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RDSON:ISOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:RDSON:ISOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemRdsonDevicetype(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:RDSON:DEVICEType`` command.

    Description:
        - This command sets or queries the device type for the power drain source on resistance
          measurement for RDSon measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:RDSON:DEVICEType?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RDSON:DEVICEType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:RDSON:DEVICEType value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RDSON:DEVICEType {SWITCHING|PNJUNCTION}
        - POWer:POWer<x>:RDSON:DEVICEType?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``SWITCHING`` sets the Device Type to a switching device (v/i).
        - ``PNJUNCTION`` sets the Device Type to a PN Junction device (dv/di).
    """


class PowerPowerItemRdson(SCPICmdRead):
    """The ``POWer:POWer<x>:RDSON`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:RDSON?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RDSON?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.devicetype``: The ``POWer:POWer<x>:RDSON:DEVICEType`` command.
        - ``.isource``: The ``POWer:POWer<x>:RDSON:ISOURce`` command.
        - ``.vsource``: The ``POWer:POWer<x>:RDSON:VSOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._devicetype = PowerPowerItemRdsonDevicetype(device, f"{self._cmd_syntax}:DEVICEType")
        self._isource = PowerPowerItemRdsonIsource(device, f"{self._cmd_syntax}:ISOURce")
        self._vsource = PowerPowerItemRdsonVsource(device, f"{self._cmd_syntax}:VSOURce")

    @property
    def devicetype(self) -> PowerPowerItemRdsonDevicetype:
        """Return the ``POWer:POWer<x>:RDSON:DEVICEType`` command.

        Description:
            - This command sets or queries the device type for the power drain source on resistance
              measurement for RDSon measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:RDSON:DEVICEType?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RDSON:DEVICEType?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:RDSON:DEVICEType value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RDSON:DEVICEType {SWITCHING|PNJUNCTION}
            - POWer:POWer<x>:RDSON:DEVICEType?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``SWITCHING`` sets the Device Type to a switching device (v/i).
            - ``PNJUNCTION`` sets the Device Type to a PN Junction device (dv/di).
        """
        return self._devicetype

    @property
    def isource(self) -> PowerPowerItemRdsonIsource:
        """Return the ``POWer:POWer<x>:RDSON:ISOURce`` command.

        Description:
            - This command sets or queries the current source for RDSon measurement of the specified
              power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:RDSON:ISOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RDSON:ISOURce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:RDSON:ISOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RDSON:ISOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:RDSON:ISOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._isource

    @property
    def vsource(self) -> PowerPowerItemRdsonVsource:
        """Return the ``POWer:POWer<x>:RDSON:VSOURce`` command.

        Description:
            - This command sets or queries the voltage source for RDSon measurement of the specified
              power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:RDSON:VSOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RDSON:VSOURce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:RDSON:VSOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RDSON:VSOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:RDSON:VSOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vsource


class PowerPowerItemPsrrTestconnection(SCPICmdWrite):
    """The ``POWer:POWer<x>:PSRR:TESTCONNection`` command.

    Description:
        - This command tests the connection with the external instrument for the specified Power
          Supply Rejection Ratio (PSRR) measurement.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:PSRR:TESTCONNection value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:TESTCONNection {EXECute}
        ```

    Info:
        - ``POWer<x>`` is the number of the PSRR power measurement.
        - ``EXECute`` runs the test connection function.
    """


class PowerPowerItemPsrrStopfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:STOPFREQuency`` command.

    Description:
        - This command sets or queries the stop frequency value for the Power Supply Rejection Ratio
          (PSRR) power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:STOPFREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:STOPFREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:PSRR:STOPFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:STOPFREQuency <NR3>
        - POWer:POWer<x>:PSRR:STOPFREQuency?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the stop frequency for the measurement, in the range of 10 Hz to 50 MHz.
    """


class PowerPowerItemPsrrStartfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:STARTFREQuency`` command.

    Description:
        - This command sets or queries the start frequency value for the Power Supply Rejection
          Ratio (PSRR) power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:STARTFREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:STARTFREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:PSRR:STARTFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:STARTFREQuency <NR3>
        - POWer:POWer<x>:PSRR:STARTFREQuency?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the starting frequency for the measurement, in the range of 10 Hz to 50 MHz.
    """


class PowerPowerItemPsrrPpd(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:PPD`` command.

    Description:
        - This command sets or queries the points per decade (PPD) value for the Power Supply
          Rejection Ratio (PSRR) power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:PPD?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:PPD?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PSRR:PPD value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:PPD <NR3>
        - POWer:POWer<x>:PSRR:PPD?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the PPD value for the measurement, in the range of 10 to 100 points.
    """


class PowerPowerItemPsrrOutputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:OUTPUTSOurce`` command.

    Description:
        - This command sets or queries the output source for the Power Supply Rejection Ratio (PSRR)
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:OUTPUTSOurce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:OUTPUTSOurce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:PSRR:OUTPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:OUTPUTSOurce CH<x>
        - POWer:POWer<x>:PSRR:OUTPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` sets the channel to use for the output source.
    """


class PowerPowerItemPsrrInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for the Power Supply Rejection Ratio (PSRR)
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:INPUTSOurce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:INPUTSOurce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PSRR:INPUTSOurce value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:INPUTSOurce CH<x>
        - POWer:POWer<x>:PSRR:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` sets the channel to use for the input source.
    """


class PowerPowerItemPsrrImpedance(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:IMPEDance`` command.

    Description:
        - This command sets or queries the vertical termination impedance for the Power Supply
          Rejection Ratio (PSRR) power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:IMPEDance?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:IMPEDance?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PSRR:IMPEDance value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:IMPEDance {FIFTy|HIGHZ}
        - POWer:POWer<x>:PSRR:IMPEDance?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``FIFTy`` sets the impedance to be 50 Ω.
        - ``HIGHZ`` sets the impedance to be 1 MΩ.
    """


class PowerPowerItemPsrrGenerator(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:GENerator`` command.

    Description:
        - Sets or queries the generator source for the Power Supply Rejection Ratio (PSRR) power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:GENerator?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:GENerator?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PSRR:GENerator value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:GENerator {INTernal|EXTernal}
        - POWer:POWer<x>:PSRR:GENerator?
        ```

    Info:
        - ``POWer<x>`` is the number of the PSRR power measurement.
        - ``INTernal`` sets the internal generator as the source for the Power Supply Rejection
          Ratio (PSRR) power measurement.
        - ``EXTernal`` sets the external generator as the source for the Power Supply Rejection
          Ratio (PSRR) power measurement.
    """


class PowerPowerItemPsrrGenipaddress(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:GENIPADDress`` command.

    Description:
        - Sets or queries the instrument's IP Address associated with the specified Power Supply
          Rejection Ratio (PSRR) measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:GENIPADDress?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:GENIPADDress?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:PSRR:GENIPADDress value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:GENIPADDress <Qstring>
        - POWer:POWer<x>:PSRR:GENIPADDress?
        ```

    Info:
        - ``POWer<x>`` is the number of the PSRR power measurement.<NR2> is the IP address of the
          generator.
    """


class PowerPowerItemPsrrFreqvalItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:FREQ<x>Val`` command.

    Description:
        - This command sets or queries the generator frequency value of the specified configuration
          step for the Power Supply Rejection Ratio (PSRR) power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:FREQ<x>Val?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:FREQ<x>Val?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PSRR:FREQ<x>Val value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:FREQ<x>Val <NR3>
        - POWer:POWer<x>:PSRR:FREQ<x>Val?
        ```

    Info:
        - ``Power<x>`` sets the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``FREQ<x>`` sets the configuration step number, in the range of 1 to 11. Values outside
          this range will report an error.
        - ``<NR3>`` sets the frequency of the specified configuration step number, in the range of
          10 Hz to 50 MHz.
    """


class PowerPowerItemPsrrConstamplitude(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:CONSTAMPlitude`` command.

    Description:
        - This command sets or queries the constant amplitude voltage for the Power Supply Rejection
          Ratio (PSRR) power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:CONSTAMPlitude?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:CONSTAMPlitude?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:PSRR:CONSTAMPlitude value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:CONSTAMPlitude <NR3>
        - POWer:POWer<x>:PSRR:CONSTAMPlitude?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the constant amplitude voltage value for the measurement, in the range of
          -100 V to 100 V.
    """


class PowerPowerItemPsrrConnectstatus(SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:CONNECTSTATus`` command.

    Description:
        - Queries the external instrument's connection status for the specified Power Supply
          Rejection Ratio (PSRR) measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:CONNECTSTATus?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:CONNECTSTATus?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:CONNECTSTATus?
        ```

    Info:
        - ``POWer<x>`` is the number of the PSRR power measurement.
    """


class PowerPowerItemPsrrAutorbw(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:AUTORbw`` command.

    Description:
        - This command enables Auto RBW computation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:AUTORbw?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:AUTORbw?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PSRR:AUTORbw value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:AUTORbw {True|False}
        - POWer:POWer<x>:PSRR:AUTORbw?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``True`` enables Auto RBW computation.
        - ``False`` disables Auto RBW computation.
    """


class PowerPowerItemPsrrAnalysismethod(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:ANALYSISMethod`` command.

    Description:
        - This command sets or queries the Analysis Method for PSRR measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:ANALYSISMethod?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:ANALYSISMethod?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:PSRR:ANALYSISMethod value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:ANALYSISMethod {SV|FFT}
        - POWer:POWer<x>:PSRR:ANALYSISMethod?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``SV`` sets the Analysis Method as Spectrum View.
        - ``FFT`` sets the Analysis Method as FFT.
    """


class PowerPowerItemPsrrAmpmode(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:AMPMode`` command.

    Description:
        - This command sets or queries the amplitude mode for the Power Supply Rejection Ratio
          (PSRR) power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:AMPMode?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:AMPMode?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PSRR:AMPMode value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:AMPMode {CONSTant|PROFile}
        - POWer:POWer<x>:PSRR:AMPMode?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CONSTant`` sets the amplitude mode to output a constant amplitude signal from the DUT
          stimulus generator for all frequency bands.
        - ``PROFile`` enables configuring the generator to set amplitude values for each frequency
          band.
    """


class PowerPowerItemPsrrAmpvalItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR:AMP<x>Val`` command.

    Description:
        - This command sets or queries the generator amplitude value of the specified configuration
          step for the Power Supply Rejection Ratio (PSRR) power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:AMP<x>Val?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:AMP<x>Val?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PSRR:AMP<x>Val value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PSRR:AMP<x>Val <NR3>
        - POWer:POWer<x>:PSRR:AMP<x>Val?
        ```

    Info:
        - ``Power<x>`` sets the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``AMP<x>`` sets the configuration step number, in the range of 1 to 10. Values outside
          this range will report an error.
        - ``<NR3>`` sets the generator amplitude for the specified configuration step, in the range
          of -100 V to 100 V.
    """


#  pylint: disable=too-many-instance-attributes
class PowerPowerItemPsrr(SCPICmdRead):
    """The ``POWer:POWer<x>:PSRR`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ampval``: The ``POWer:POWer<x>:PSRR:AMP<x>Val`` command.
        - ``.ampmode``: The ``POWer:POWer<x>:PSRR:AMPMode`` command.
        - ``.analysismethod``: The ``POWer:POWer<x>:PSRR:ANALYSISMethod`` command.
        - ``.autorbw``: The ``POWer:POWer<x>:PSRR:AUTORbw`` command.
        - ``.connectstatus``: The ``POWer:POWer<x>:PSRR:CONNECTSTATus`` command.
        - ``.constamplitude``: The ``POWer:POWer<x>:PSRR:CONSTAMPlitude`` command.
        - ``.freqval``: The ``POWer:POWer<x>:PSRR:FREQ<x>Val`` command.
        - ``.genipaddress``: The ``POWer:POWer<x>:PSRR:GENIPADDress`` command.
        - ``.generator``: The ``POWer:POWer<x>:PSRR:GENerator`` command.
        - ``.impedance``: The ``POWer:POWer<x>:PSRR:IMPEDance`` command.
        - ``.inputsource``: The ``POWer:POWer<x>:PSRR:INPUTSOurce`` command.
        - ``.outputsource``: The ``POWer:POWer<x>:PSRR:OUTPUTSOurce`` command.
        - ``.ppd``: The ``POWer:POWer<x>:PSRR:PPD`` command.
        - ``.startfrequency``: The ``POWer:POWer<x>:PSRR:STARTFREQuency`` command.
        - ``.stopfrequency``: The ``POWer:POWer<x>:PSRR:STOPFREQuency`` command.
        - ``.testconnection``: The ``POWer:POWer<x>:PSRR:TESTCONNection`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ampval: Dict[int, PowerPowerItemPsrrAmpvalItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerPowerItemPsrrAmpvalItem(device, f"{self._cmd_syntax}:AMP{x}Val")
        )
        self._ampmode = PowerPowerItemPsrrAmpmode(device, f"{self._cmd_syntax}:AMPMode")
        self._analysismethod = PowerPowerItemPsrrAnalysismethod(
            device, f"{self._cmd_syntax}:ANALYSISMethod"
        )
        self._autorbw = PowerPowerItemPsrrAutorbw(device, f"{self._cmd_syntax}:AUTORbw")
        self._connectstatus = PowerPowerItemPsrrConnectstatus(
            device, f"{self._cmd_syntax}:CONNECTSTATus"
        )
        self._constamplitude = PowerPowerItemPsrrConstamplitude(
            device, f"{self._cmd_syntax}:CONSTAMPlitude"
        )
        self._freqval: Dict[int, PowerPowerItemPsrrFreqvalItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerPowerItemPsrrFreqvalItem(device, f"{self._cmd_syntax}:FREQ{x}Val")
        )
        self._genipaddress = PowerPowerItemPsrrGenipaddress(
            device, f"{self._cmd_syntax}:GENIPADDress"
        )
        self._generator = PowerPowerItemPsrrGenerator(device, f"{self._cmd_syntax}:GENerator")
        self._impedance = PowerPowerItemPsrrImpedance(device, f"{self._cmd_syntax}:IMPEDance")
        self._inputsource = PowerPowerItemPsrrInputsource(device, f"{self._cmd_syntax}:INPUTSOurce")
        self._outputsource = PowerPowerItemPsrrOutputsource(
            device, f"{self._cmd_syntax}:OUTPUTSOurce"
        )
        self._ppd = PowerPowerItemPsrrPpd(device, f"{self._cmd_syntax}:PPD")
        self._startfrequency = PowerPowerItemPsrrStartfrequency(
            device, f"{self._cmd_syntax}:STARTFREQuency"
        )
        self._stopfrequency = PowerPowerItemPsrrStopfrequency(
            device, f"{self._cmd_syntax}:STOPFREQuency"
        )
        self._testconnection = PowerPowerItemPsrrTestconnection(
            device, f"{self._cmd_syntax}:TESTCONNection"
        )

    @property
    def ampval(self) -> Dict[int, PowerPowerItemPsrrAmpvalItem]:
        """Return the ``POWer:POWer<x>:PSRR:AMP<x>Val`` command.

        Description:
            - This command sets or queries the generator amplitude value of the specified
              configuration step for the Power Supply Rejection Ratio (PSRR) power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:AMP<x>Val?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:AMP<x>Val?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:AMP<x>Val value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:AMP<x>Val <NR3>
            - POWer:POWer<x>:PSRR:AMP<x>Val?
            ```

        Info:
            - ``Power<x>`` sets the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``AMP<x>`` sets the configuration step number, in the range of 1 to 10. Values outside
              this range will report an error.
            - ``<NR3>`` sets the generator amplitude for the specified configuration step, in the
              range of -100 V to 100 V.
        """
        return self._ampval

    @property
    def ampmode(self) -> PowerPowerItemPsrrAmpmode:
        """Return the ``POWer:POWer<x>:PSRR:AMPMode`` command.

        Description:
            - This command sets or queries the amplitude mode for the Power Supply Rejection Ratio
              (PSRR) power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:AMPMode?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:AMPMode?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PSRR:AMPMode value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:AMPMode {CONSTant|PROFile}
            - POWer:POWer<x>:PSRR:AMPMode?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CONSTant`` sets the amplitude mode to output a constant amplitude signal from the
              DUT stimulus generator for all frequency bands.
            - ``PROFile`` enables configuring the generator to set amplitude values for each
              frequency band.
        """
        return self._ampmode

    @property
    def analysismethod(self) -> PowerPowerItemPsrrAnalysismethod:
        """Return the ``POWer:POWer<x>:PSRR:ANALYSISMethod`` command.

        Description:
            - This command sets or queries the Analysis Method for PSRR measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:ANALYSISMethod?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:PSRR:ANALYSISMethod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:ANALYSISMethod value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:ANALYSISMethod {SV|FFT}
            - POWer:POWer<x>:PSRR:ANALYSISMethod?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``SV`` sets the Analysis Method as Spectrum View.
            - ``FFT`` sets the Analysis Method as FFT.
        """
        return self._analysismethod

    @property
    def autorbw(self) -> PowerPowerItemPsrrAutorbw:
        """Return the ``POWer:POWer<x>:PSRR:AUTORbw`` command.

        Description:
            - This command enables Auto RBW computation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:AUTORbw?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:AUTORbw?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PSRR:AUTORbw value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:AUTORbw {True|False}
            - POWer:POWer<x>:PSRR:AUTORbw?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``True`` enables Auto RBW computation.
            - ``False`` disables Auto RBW computation.
        """
        return self._autorbw

    @property
    def connectstatus(self) -> PowerPowerItemPsrrConnectstatus:
        """Return the ``POWer:POWer<x>:PSRR:CONNECTSTATus`` command.

        Description:
            - Queries the external instrument's connection status for the specified Power Supply
              Rejection Ratio (PSRR) measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:CONNECTSTATus?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:PSRR:CONNECTSTATus?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:CONNECTSTATus?
            ```

        Info:
            - ``POWer<x>`` is the number of the PSRR power measurement.
        """
        return self._connectstatus

    @property
    def constamplitude(self) -> PowerPowerItemPsrrConstamplitude:
        """Return the ``POWer:POWer<x>:PSRR:CONSTAMPlitude`` command.

        Description:
            - This command sets or queries the constant amplitude voltage for the Power Supply
              Rejection Ratio (PSRR) power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:CONSTAMPlitude?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:PSRR:CONSTAMPlitude?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:CONSTAMPlitude value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:CONSTAMPlitude <NR3>
            - POWer:POWer<x>:PSRR:CONSTAMPlitude?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the constant amplitude voltage value for the measurement, in the range of
              -100 V to 100 V.
        """
        return self._constamplitude

    @property
    def freqval(self) -> Dict[int, PowerPowerItemPsrrFreqvalItem]:
        """Return the ``POWer:POWer<x>:PSRR:FREQ<x>Val`` command.

        Description:
            - This command sets or queries the generator frequency value of the specified
              configuration step for the Power Supply Rejection Ratio (PSRR) power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:FREQ<x>Val?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:FREQ<x>Val?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:FREQ<x>Val value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:FREQ<x>Val <NR3>
            - POWer:POWer<x>:PSRR:FREQ<x>Val?
            ```

        Info:
            - ``Power<x>`` sets the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``FREQ<x>`` sets the configuration step number, in the range of 1 to 11. Values
              outside this range will report an error.
            - ``<NR3>`` sets the frequency of the specified configuration step number, in the range
              of 10 Hz to 50 MHz.
        """
        return self._freqval

    @property
    def genipaddress(self) -> PowerPowerItemPsrrGenipaddress:
        """Return the ``POWer:POWer<x>:PSRR:GENIPADDress`` command.

        Description:
            - Sets or queries the instrument's IP Address associated with the specified Power Supply
              Rejection Ratio (PSRR) measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:GENIPADDress?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:PSRR:GENIPADDress?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:GENIPADDress value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:GENIPADDress <Qstring>
            - POWer:POWer<x>:PSRR:GENIPADDress?
            ```

        Info:
            - ``POWer<x>`` is the number of the PSRR power measurement.<NR2> is the IP address of
              the generator.
        """
        return self._genipaddress

    @property
    def generator(self) -> PowerPowerItemPsrrGenerator:
        """Return the ``POWer:POWer<x>:PSRR:GENerator`` command.

        Description:
            - Sets or queries the generator source for the Power Supply Rejection Ratio (PSRR) power
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:GENerator?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:GENerator?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:GENerator value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:GENerator {INTernal|EXTernal}
            - POWer:POWer<x>:PSRR:GENerator?
            ```

        Info:
            - ``POWer<x>`` is the number of the PSRR power measurement.
            - ``INTernal`` sets the internal generator as the source for the Power Supply Rejection
              Ratio (PSRR) power measurement.
            - ``EXTernal`` sets the external generator as the source for the Power Supply Rejection
              Ratio (PSRR) power measurement.
        """
        return self._generator

    @property
    def impedance(self) -> PowerPowerItemPsrrImpedance:
        """Return the ``POWer:POWer<x>:PSRR:IMPEDance`` command.

        Description:
            - This command sets or queries the vertical termination impedance for the Power Supply
              Rejection Ratio (PSRR) power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:IMPEDance?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:IMPEDance?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:IMPEDance value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:IMPEDance {FIFTy|HIGHZ}
            - POWer:POWer<x>:PSRR:IMPEDance?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``FIFTy`` sets the impedance to be 50 Ω.
            - ``HIGHZ`` sets the impedance to be 1 MΩ.
        """
        return self._impedance

    @property
    def inputsource(self) -> PowerPowerItemPsrrInputsource:
        """Return the ``POWer:POWer<x>:PSRR:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for the Power Supply Rejection Ratio
              (PSRR) power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:INPUTSOurce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:INPUTSOurce CH<x>
            - POWer:POWer<x>:PSRR:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` sets the channel to use for the input source.
        """
        return self._inputsource

    @property
    def outputsource(self) -> PowerPowerItemPsrrOutputsource:
        """Return the ``POWer:POWer<x>:PSRR:OUTPUTSOurce`` command.

        Description:
            - This command sets or queries the output source for the Power Supply Rejection Ratio
              (PSRR) power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:OUTPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:PSRR:OUTPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:OUTPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:OUTPUTSOurce CH<x>
            - POWer:POWer<x>:PSRR:OUTPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` sets the channel to use for the output source.
        """
        return self._outputsource

    @property
    def ppd(self) -> PowerPowerItemPsrrPpd:
        """Return the ``POWer:POWer<x>:PSRR:PPD`` command.

        Description:
            - This command sets or queries the points per decade (PPD) value for the Power Supply
              Rejection Ratio (PSRR) power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:PPD?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR:PPD?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PSRR:PPD value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:PPD <NR3>
            - POWer:POWer<x>:PSRR:PPD?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the PPD value for the measurement, in the range of 10 to 100 points.
        """
        return self._ppd

    @property
    def startfrequency(self) -> PowerPowerItemPsrrStartfrequency:
        """Return the ``POWer:POWer<x>:PSRR:STARTFREQuency`` command.

        Description:
            - This command sets or queries the start frequency value for the Power Supply Rejection
              Ratio (PSRR) power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:STARTFREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:PSRR:STARTFREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:STARTFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:STARTFREQuency <NR3>
            - POWer:POWer<x>:PSRR:STARTFREQuency?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the starting frequency for the measurement, in the range of 10 Hz to 50
              MHz.
        """
        return self._startfrequency

    @property
    def stopfrequency(self) -> PowerPowerItemPsrrStopfrequency:
        """Return the ``POWer:POWer<x>:PSRR:STOPFREQuency`` command.

        Description:
            - This command sets or queries the stop frequency value for the Power Supply Rejection
              Ratio (PSRR) power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR:STOPFREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:PSRR:STOPFREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:STOPFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:STOPFREQuency <NR3>
            - POWer:POWer<x>:PSRR:STOPFREQuency?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the stop frequency for the measurement, in the range of 10 Hz to 50 MHz.
        """
        return self._stopfrequency

    @property
    def testconnection(self) -> PowerPowerItemPsrrTestconnection:
        """Return the ``POWer:POWer<x>:PSRR:TESTCONNection`` command.

        Description:
            - This command tests the connection with the external instrument for the specified Power
              Supply Rejection Ratio (PSRR) measurement.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PSRR:TESTCONNection value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PSRR:TESTCONNection {EXECute}
            ```

        Info:
            - ``POWer<x>`` is the number of the PSRR power measurement.
            - ``EXECute`` runs the test connection function.
        """
        return self._testconnection


class PowerPowerItemPreset(SCPICmdWrite):
    """The ``POWer:POWer<x>:PRESET`` command.

    Description:
        - This command runs a power preset action for the specified power measurement number.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PRESET value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PRESET {EXECute}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``EXECute`` runs the power preset action.
    """


class PowerPowerItemPpulsewidthInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for positive pulse width measurement in the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemPpulsewidth(SCPICmdRead):
    """The ``POWer:POWer<x>:PPULSEWIDTH`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PPULSEWIDTH?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PPULSEWIDTH?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemPpulsewidthInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def inputsource(self) -> PowerPowerItemPpulsewidthInputsource:
        """Return the ``POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for positive pulse width measurement in
              the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemPowerqualityVsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:POWERQUALITY:VSOURce`` command.

    Description:
        - This command sets or queries the voltage source for power quality measurement in the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:POWERQUALITY:VSOURce?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:POWERQUALITY:VSOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:POWERQUALITY:VSOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:POWERQUALITY:VSOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:POWERQUALITY:VSOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemPowerqualityStype(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:POWERQUALITY:STYPe`` command.

    Description:
        - This command sets or queries the source type.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:POWERQUALITY:STYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:POWERQUALITY:STYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:POWERQUALITY:STYPe value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:POWERQUALITY:STYPe {AC|DC}
        - POWer:POWer<x>:POWERQUALITY:STYPe?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``AC`` sets the signal type as AC.
        - ``DC`` sets the signal type as DC.
    """


class PowerPowerItemPowerqualityIsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:POWERQUALITY:ISOURce`` command.

    Description:
        - This command sets or queries the current source for power quality measurement in the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:POWERQUALITY:ISOURce?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:POWERQUALITY:ISOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:POWERQUALITY:ISOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:POWERQUALITY:ISOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:POWERQUALITY:ISOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemPowerqualityFreference(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:POWERQUALITY:FREFerence`` command.

    Description:
        - This command sets or queries the frequency reference type for power quality measurement in
          the specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:POWERQUALITY:FREFerence?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:POWERQUALITY:FREFerence?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:POWERQUALITY:FREFerence value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:POWERQUALITY:FREFerence {VOLTage|CURRent}
        - POWer:POWer<x>:POWERQUALITY:FREFerence?
        ```
    """


class PowerPowerItemPowerqualityCcycles(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:POWERQUALITY:CCYCles`` command.

    Description:
        - This command sets or queries the calculate cycles over full cycles settings for the
          specified power quality measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:POWERQUALITY:CCYCles?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:POWERQUALITY:CCYCles?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:POWERQUALITY:CCYCles value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:POWERQUALITY:CCYCles {ON|OFF|1|0}
        - POWer:POWer<x>:POWERQUALITY:CCYCles?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``1`` selects the calculate cycles over full cycles.
        - ``ON`` selects the calculate cycles over full cycles.
        - ``0`` deselects the calculate cycles over full cycles.
        - ``OFF`` deselects the calculate cycles over full cycles.
    """


class PowerPowerItemPowerquality(SCPICmdRead):
    """The ``POWer:POWer<x>:POWERQUALITY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:POWERQUALITY?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:POWERQUALITY?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ccycles``: The ``POWer:POWer<x>:POWERQUALITY:CCYCles`` command.
        - ``.freference``: The ``POWer:POWer<x>:POWERQUALITY:FREFerence`` command.
        - ``.isource``: The ``POWer:POWer<x>:POWERQUALITY:ISOURce`` command.
        - ``.stype``: The ``POWer:POWer<x>:POWERQUALITY:STYPe`` command.
        - ``.vsource``: The ``POWer:POWer<x>:POWERQUALITY:VSOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ccycles = PowerPowerItemPowerqualityCcycles(device, f"{self._cmd_syntax}:CCYCles")
        self._freference = PowerPowerItemPowerqualityFreference(
            device, f"{self._cmd_syntax}:FREFerence"
        )
        self._isource = PowerPowerItemPowerqualityIsource(device, f"{self._cmd_syntax}:ISOURce")
        self._stype = PowerPowerItemPowerqualityStype(device, f"{self._cmd_syntax}:STYPe")
        self._vsource = PowerPowerItemPowerqualityVsource(device, f"{self._cmd_syntax}:VSOURce")

    @property
    def ccycles(self) -> PowerPowerItemPowerqualityCcycles:
        """Return the ``POWer:POWer<x>:POWERQUALITY:CCYCles`` command.

        Description:
            - This command sets or queries the calculate cycles over full cycles settings for the
              specified power quality measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:POWERQUALITY:CCYCles?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:POWERQUALITY:CCYCles?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:POWERQUALITY:CCYCles value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:POWERQUALITY:CCYCles {ON|OFF|1|0}
            - POWer:POWer<x>:POWERQUALITY:CCYCles?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``1`` selects the calculate cycles over full cycles.
            - ``ON`` selects the calculate cycles over full cycles.
            - ``0`` deselects the calculate cycles over full cycles.
            - ``OFF`` deselects the calculate cycles over full cycles.
        """
        return self._ccycles

    @property
    def freference(self) -> PowerPowerItemPowerqualityFreference:
        """Return the ``POWer:POWer<x>:POWERQUALITY:FREFerence`` command.

        Description:
            - This command sets or queries the frequency reference type for power quality
              measurement in the specified power measurement number. The power measurement number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:POWERQUALITY:FREFerence?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:POWERQUALITY:FREFerence?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:POWERQUALITY:FREFerence value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:POWERQUALITY:FREFerence {VOLTage|CURRent}
            - POWer:POWer<x>:POWERQUALITY:FREFerence?
            ```
        """
        return self._freference

    @property
    def isource(self) -> PowerPowerItemPowerqualityIsource:
        """Return the ``POWer:POWer<x>:POWERQUALITY:ISOURce`` command.

        Description:
            - This command sets or queries the current source for power quality measurement in the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:POWERQUALITY:ISOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:POWERQUALITY:ISOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:POWERQUALITY:ISOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:POWERQUALITY:ISOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:POWERQUALITY:ISOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._isource

    @property
    def stype(self) -> PowerPowerItemPowerqualityStype:
        """Return the ``POWer:POWer<x>:POWERQUALITY:STYPe`` command.

        Description:
            - This command sets or queries the source type.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:POWERQUALITY:STYPe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:POWERQUALITY:STYPe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:POWERQUALITY:STYPe value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:POWERQUALITY:STYPe {AC|DC}
            - POWer:POWer<x>:POWERQUALITY:STYPe?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``AC`` sets the signal type as AC.
            - ``DC`` sets the signal type as DC.
        """
        return self._stype

    @property
    def vsource(self) -> PowerPowerItemPowerqualityVsource:
        """Return the ``POWer:POWer<x>:POWERQUALITY:VSOURce`` command.

        Description:
            - This command sets or queries the voltage source for power quality measurement in the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:POWERQUALITY:VSOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:POWERQUALITY:VSOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:POWERQUALITY:VSOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:POWERQUALITY:VSOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:POWERQUALITY:VSOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vsource


class PowerPowerItemPeriodInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PERIOD:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for period measurement in the specified
          power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PERIOD:INPUTSOurce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PERIOD:INPUTSOurce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:PERIOD:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PERIOD:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:PERIOD:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemPeriodEdge(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PERIOD:EDGe`` command.

    Description:
        - This command sets or queries the edge type for period measurement in the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PERIOD:EDGe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PERIOD:EDGe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PERIOD:EDGe value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PERIOD:EDGe {RISE|FALL}
        - POWer:POWer<x>:PERIOD:EDGe?
        ```
    """


class PowerPowerItemPeriod(SCPICmdRead):
    """The ``POWer:POWer<x>:PERIOD`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PERIOD?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PERIOD?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``POWer:POWer<x>:PERIOD:EDGe`` command.
        - ``.inputsource``: The ``POWer:POWer<x>:PERIOD:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = PowerPowerItemPeriodEdge(device, f"{self._cmd_syntax}:EDGe")
        self._inputsource = PowerPowerItemPeriodInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def edge(self) -> PowerPowerItemPeriodEdge:
        """Return the ``POWer:POWer<x>:PERIOD:EDGe`` command.

        Description:
            - This command sets or queries the edge type for period measurement in the specified
              power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PERIOD:EDGe?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PERIOD:EDGe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PERIOD:EDGe value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PERIOD:EDGe {RISE|FALL}
            - POWer:POWer<x>:PERIOD:EDGe?
            ```
        """
        return self._edge

    @property
    def inputsource(self) -> PowerPowerItemPeriodInputsource:
        """Return the ``POWer:POWer<x>:PERIOD:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for period measurement in the specified
              power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PERIOD:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:PERIOD:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PERIOD:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PERIOD:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:PERIOD:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemPdutycycleInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for positive duty cycle measurement in the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemPdutycycleEdgetype(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:PDUTYCYCLE:EDGEType`` command.

    Description:
        - This command sets or queries the clock edge type for positive duty cycle measurement in
          the specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PDUTYCYCLE:EDGEType?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PDUTYCYCLE:EDGEType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:PDUTYCYCLE:EDGEType value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PDUTYCYCLE:EDGEType {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:PDUTYCYCLE:EDGEType?
        ```
    """


class PowerPowerItemPdutycycle(SCPICmdRead):
    """The ``POWer:POWer<x>:PDUTYCYCLE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:PDUTYCYCLE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PDUTYCYCLE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edgetype``: The ``POWer:POWer<x>:PDUTYCYCLE:EDGEType`` command.
        - ``.inputsource``: The ``POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edgetype = PowerPowerItemPdutycycleEdgetype(device, f"{self._cmd_syntax}:EDGEType")
        self._inputsource = PowerPowerItemPdutycycleInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def edgetype(self) -> PowerPowerItemPdutycycleEdgetype:
        """Return the ``POWer:POWer<x>:PDUTYCYCLE:EDGEType`` command.

        Description:
            - This command sets or queries the clock edge type for positive duty cycle measurement
              in the specified power measurement number. The power measurement number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PDUTYCYCLE:EDGEType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:PDUTYCYCLE:EDGEType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PDUTYCYCLE:EDGEType value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PDUTYCYCLE:EDGEType {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:PDUTYCYCLE:EDGEType?
            ```
        """
        return self._edgetype

    @property
    def inputsource(self) -> PowerPowerItemPdutycycleInputsource:
        """Return the ``POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for positive duty cycle measurement in
              the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemNpulsewidthInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for negative pulse width measurement in the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemNpulsewidth(SCPICmdRead):
    """The ``POWer:POWer<x>:NPULSEWIDTH`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:NPULSEWIDTH?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:NPULSEWIDTH?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemNpulsewidthInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def inputsource(self) -> PowerPowerItemNpulsewidthInputsource:
        """Return the ``POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for negative pulse width measurement in
              the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemNdutycycleInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for negative duty cycle measurement in the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemNdutycycleEdgetype(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:NDUTYCYCLE:EDGEType`` command.

    Description:
        - This command sets or queries the clock edge type for negative duty cycle measurement in
          the specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:NDUTYCYCLE:EDGEType?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:NDUTYCYCLE:EDGEType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:NDUTYCYCLE:EDGEType value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:NDUTYCYCLE:EDGEType {RISE|FALL|BOTH}
        - POWer:POWer<x>:NDUTYCYCLE:EDGEType?
        ```
    """


class PowerPowerItemNdutycycle(SCPICmdRead):
    """The ``POWer:POWer<x>:NDUTYCYCLE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:NDUTYCYCLE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:NDUTYCYCLE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edgetype``: The ``POWer:POWer<x>:NDUTYCYCLE:EDGEType`` command.
        - ``.inputsource``: The ``POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edgetype = PowerPowerItemNdutycycleEdgetype(device, f"{self._cmd_syntax}:EDGEType")
        self._inputsource = PowerPowerItemNdutycycleInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def edgetype(self) -> PowerPowerItemNdutycycleEdgetype:
        """Return the ``POWer:POWer<x>:NDUTYCYCLE:EDGEType`` command.

        Description:
            - This command sets or queries the clock edge type for negative duty cycle measurement
              in the specified power measurement number. The power measurement number is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:NDUTYCYCLE:EDGEType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:NDUTYCYCLE:EDGEType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:NDUTYCYCLE:EDGEType value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:NDUTYCYCLE:EDGEType {RISE|FALL|BOTH}
            - POWer:POWer<x>:NDUTYCYCLE:EDGEType?
            ```
        """
        return self._edgetype

    @property
    def inputsource(self) -> PowerPowerItemNdutycycleInputsource:
        """Return the ``POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for negative duty cycle measurement in
              the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemMagpropertyVsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:VSOURce`` command.

    Description:
        - This command sets or queries the primary winding voltage source for the magnetic
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:VSOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGPROPERTY:VSOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:VSOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:VSOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:MAGPROPERTY:VSOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemMagpropertyUnits(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:UNITs`` command.

    Description:
        - This command sets or queries the units for magnetic measurements of the specified power
          measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:UNITs?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGPROPERTY:UNITs?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:UNITs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:UNITs {SI|CGS}
        - POWer:POWer<x>:MAGPROPERTY:UNITs?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``SI`` sets the measurement to International System of Units.
        - ``CGS`` sets the measurement to Gaussian units.
    """


class PowerPowerItemMagpropertySecwindings(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SECWINDings`` command.

    Description:
        - This command sets or queries the number of secondary windings for the magnetic property
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SECWINDings?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SECWINDings?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SECWINDings value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SECWINDings {None|ONE|TWO|THREE|FOUR|FIVE|SIX}
        - POWer:POWer<x>:MAGPROPERTY:SECWINDings?
        ```

    Info:
        - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``None`` , ONE, TWO, THREE, FOUR, FIVE, SIX sets the number of secondary windings to the
          specified value.
    """


class PowerPowerItemMagpropertySecvolt(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SECVolt`` command.

    Description:
        - This command enables or disables secondary voltage input for measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SECVolt?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SECVolt?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SECVolt value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SECVolt {True|False}
        - POWer:POWer<x>:MAGPROPERTY:SECVolt?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``True`` enables secondary voltage source.
        - ``False`` disables secondary voltage source.
    """


class PowerPowerItemMagpropertySecphase(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SECPhase`` command.

    Description:
        - This command sets or returns the value for the phase difference between secondary and
          primary voltage.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SECPhase?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SECPhase?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SECPhase value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SECPhase <NR3>
        - POWer:POWer<x>:MAGPROPERTY:SECPhase?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` sets the value for the phase difference between secondary and primary voltage,
          in the range of -180 to 180 degrees.
    """


class PowerPowerItemMagpropertySec6turns(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC6TURNs`` command.

    Description:
        - This command sets or queries the number of turns of secondary winding 6 for magnetic
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC6TURNs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC6TURNs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC6TURNs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC6TURNs <NR1>
        - POWer:POWer<x>:MAGPROPERTY:SEC6TURNs?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to 1,000,000.
    """


class PowerPowerItemMagpropertySec6source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC6SOURce`` command.

    Description:
        - This command sets or queries the current source for secondary winding 6 for magnetic
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC6SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC6SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC6SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC6SOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:MAGPROPERTY:SEC6SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemMagpropertySec5turns(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC5TURNs`` command.

    Description:
        - This command sets or queries the number of turns of secondary winding 5 for magnetic
          measurement of the specified power measurement badge.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC5TURNs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC5TURNs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC5TURNs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC5TURNs <NR1>
        - POWer:POWer<x>:MAGPROPERTY:SEC5TURNs?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to 1,000,000.
    """


class PowerPowerItemMagpropertySec5source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC5SOURce`` command.

    Description:
        - This command sets or queries the current source for secondary winding 5 for magnetic
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC5SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC5SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC5SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC5SOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:MAGPROPERTY:SEC5SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemMagpropertySec4turns(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC4TURNs`` command.

    Description:
        - This command sets or queries the number of turns of secondary winding 4 for magnetic
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC4TURNs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC4TURNs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC4TURNs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC4TURNs <NR1>
        - POWer:POWer<x>:MAGPROPERTY:SEC4TURNs?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to 1,000,000.
    """


class PowerPowerItemMagpropertySec4source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC4SOURce`` command.

    Description:
        - This command sets or queries the current source for secondary winding 4 for magnetic
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC4SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC4SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC4SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC4SOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:MAGPROPERTY:SEC4SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemMagpropertySec3turns(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC3TURNs`` command.

    Description:
        - This command sets or queries the number of turns of secondary winding 3 for magnetic
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC3TURNs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC3TURNs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC3TURNs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC3TURNs <NR1>
        - POWer:POWer<x>:MAGPROPERTY:SEC3TURNs?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to 1,000,000.
    """


class PowerPowerItemMagpropertySec3source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC3SOURce`` command.

    Description:
        - This command sets or queries the current source channel for secondary winding 3 for
          magnetic measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC3SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC3SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC3SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC3SOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:MAGPROPERTY:SEC3SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemMagpropertySec2turns(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC2TURNs`` command.

    Description:
        - This command sets or queries the number of turns of secondary winding 2 for magnetic
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC2TURNs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC2TURNs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC2TURNs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC2TURNs <NR1>
        - POWer:POWer<x>:MAGPROPERTY:SEC2TURNs?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to 1,000,000.
    """


class PowerPowerItemMagpropertySec2source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC2SOURce`` command.

    Description:
        - This command sets or queries the current source for secondary winding2 for magnetic
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC2SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC2SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC2SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC2SOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:MAGPROPERTY:SEC2SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemMagpropertySec1turns(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC1TURNs`` command.

    Description:
        - This command sets or queries the number of turns of secondary winding 1 for magnetic
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC1TURNs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC1TURNs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC1TURNs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC1TURNs <NR1>
        - POWer:POWer<x>:MAGPROPERTY:SEC1TURNs?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to 1,000,000.
    """


class PowerPowerItemMagpropertySec1source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:SEC1SOURce`` command.

    Description:
        - This command sets or queries the current source channel for secondary winding 1 for
          magnetic measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC1SOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC1SOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:SEC1SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:SEC1SOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:MAGPROPERTY:SEC1SOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemMagpropertyPrimaryturns(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs`` command.

    Description:
        - This command sets or queries the number of primary turns for magnetic measurement of the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs <NR1>
        - POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs?
        ```

    Info:
        - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``<NR1>`` is the integer number of turns in the primary winding, in the range of 1 to 1 M.
    """


class PowerPowerItemMagpropertyLength(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:LENgth`` command.

    Description:
        - This command sets or queries the conductor length of the primary winding for magnetic
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:LENgth?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGPROPERTY:LENgth?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:LENgth value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:LENgth <NR2>
        - POWer:POWer<x>:MAGPROPERTY:LENgth?
        ```

    Info:
        - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``<NR2>`` is the magnetic length, in the range of 1.00E-09 through 1,000,000.
    """


class PowerPowerItemMagpropertyIsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:ISOURce`` command.

    Description:
        - This command sets or queries the current source for the magnetic property measurement of
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:ISOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGPROPERTY:ISOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:ISOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:ISOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:MAGPROPERTY:ISOURce?
        ```

    Info:
        - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemMagpropertyEdgesource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:EDGESOURce`` command.

    Description:
        - This command sets or queries the edge source type for the magnetic property measurement of
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:EDGESOURce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:EDGESOURce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:EDGESOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:EDGESOURce {Current|VOLTAGE}
        - POWer:POWer<x>:MAGPROPERTY:EDGESOURce?
        ```

    Info:
        - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent of
          the number shown on a power measurement badge in the UI.
        - ``Current`` sets the measurement to use the primary voltage source as the signal edge for
          the magnetic property measurement.
        - ``VOLTAGE`` sets the measurement to use the primary current source as the signal edge for
          the magnetic property measurement.
    """


class PowerPowerItemMagpropertyAreaofcrosssection(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection`` command.

    Description:
        - This command sets or queries the coil cross section area for magnetic measurement of the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection <NR2>
        - POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection?
        ```

    Info:
        - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``<NR2>`` is the cross section area in square meters, in the range of 1 nanometer2 to 1
          M2.
    """


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class PowerPowerItemMagproperty(SCPICmdRead):
    """The ``POWer:POWer<x>:MAGPROPERTY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGPROPERTY?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.areaofcrosssection``: The ``POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection`` command.
        - ``.edgesource``: The ``POWer:POWer<x>:MAGPROPERTY:EDGESOURce`` command.
        - ``.isource``: The ``POWer:POWer<x>:MAGPROPERTY:ISOURce`` command.
        - ``.length``: The ``POWer:POWer<x>:MAGPROPERTY:LENgth`` command.
        - ``.primaryturns``: The ``POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs`` command.
        - ``.sec1source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC1SOURce`` command.
        - ``.sec1turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC1TURNs`` command.
        - ``.sec2source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC2SOURce`` command.
        - ``.sec2turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC2TURNs`` command.
        - ``.sec3source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC3SOURce`` command.
        - ``.sec3turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC3TURNs`` command.
        - ``.sec4source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC4SOURce`` command.
        - ``.sec4turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC4TURNs`` command.
        - ``.sec5source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC5SOURce`` command.
        - ``.sec5turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC5TURNs`` command.
        - ``.sec6source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC6SOURce`` command.
        - ``.sec6turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC6TURNs`` command.
        - ``.secphase``: The ``POWer:POWer<x>:MAGPROPERTY:SECPhase`` command.
        - ``.secvolt``: The ``POWer:POWer<x>:MAGPROPERTY:SECVolt`` command.
        - ``.secwindings``: The ``POWer:POWer<x>:MAGPROPERTY:SECWINDings`` command.
        - ``.units``: The ``POWer:POWer<x>:MAGPROPERTY:UNITs`` command.
        - ``.vsource``: The ``POWer:POWer<x>:MAGPROPERTY:VSOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._areaofcrosssection = PowerPowerItemMagpropertyAreaofcrosssection(
            device, f"{self._cmd_syntax}:AREAofcrosssection"
        )
        self._edgesource = PowerPowerItemMagpropertyEdgesource(
            device, f"{self._cmd_syntax}:EDGESOURce"
        )
        self._isource = PowerPowerItemMagpropertyIsource(device, f"{self._cmd_syntax}:ISOURce")
        self._length = PowerPowerItemMagpropertyLength(device, f"{self._cmd_syntax}:LENgth")
        self._primaryturns = PowerPowerItemMagpropertyPrimaryturns(
            device, f"{self._cmd_syntax}:PRIMARYTURNs"
        )
        self._sec1source = PowerPowerItemMagpropertySec1source(
            device, f"{self._cmd_syntax}:SEC1SOURce"
        )
        self._sec1turns = PowerPowerItemMagpropertySec1turns(
            device, f"{self._cmd_syntax}:SEC1TURNs"
        )
        self._sec2source = PowerPowerItemMagpropertySec2source(
            device, f"{self._cmd_syntax}:SEC2SOURce"
        )
        self._sec2turns = PowerPowerItemMagpropertySec2turns(
            device, f"{self._cmd_syntax}:SEC2TURNs"
        )
        self._sec3source = PowerPowerItemMagpropertySec3source(
            device, f"{self._cmd_syntax}:SEC3SOURce"
        )
        self._sec3turns = PowerPowerItemMagpropertySec3turns(
            device, f"{self._cmd_syntax}:SEC3TURNs"
        )
        self._sec4source = PowerPowerItemMagpropertySec4source(
            device, f"{self._cmd_syntax}:SEC4SOURce"
        )
        self._sec4turns = PowerPowerItemMagpropertySec4turns(
            device, f"{self._cmd_syntax}:SEC4TURNs"
        )
        self._sec5source = PowerPowerItemMagpropertySec5source(
            device, f"{self._cmd_syntax}:SEC5SOURce"
        )
        self._sec5turns = PowerPowerItemMagpropertySec5turns(
            device, f"{self._cmd_syntax}:SEC5TURNs"
        )
        self._sec6source = PowerPowerItemMagpropertySec6source(
            device, f"{self._cmd_syntax}:SEC6SOURce"
        )
        self._sec6turns = PowerPowerItemMagpropertySec6turns(
            device, f"{self._cmd_syntax}:SEC6TURNs"
        )
        self._secphase = PowerPowerItemMagpropertySecphase(device, f"{self._cmd_syntax}:SECPhase")
        self._secvolt = PowerPowerItemMagpropertySecvolt(device, f"{self._cmd_syntax}:SECVolt")
        self._secwindings = PowerPowerItemMagpropertySecwindings(
            device, f"{self._cmd_syntax}:SECWINDings"
        )
        self._units = PowerPowerItemMagpropertyUnits(device, f"{self._cmd_syntax}:UNITs")
        self._vsource = PowerPowerItemMagpropertyVsource(device, f"{self._cmd_syntax}:VSOURce")

    @property
    def areaofcrosssection(self) -> PowerPowerItemMagpropertyAreaofcrosssection:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection`` command.

        Description:
            - This command sets or queries the coil cross section area for magnetic measurement of
              the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection <NR2>
            - POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection?
            ```

        Info:
            - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``<NR2>`` is the cross section area in square meters, in the range of 1 nanometer2 to
              1 M2.
        """
        return self._areaofcrosssection

    @property
    def edgesource(self) -> PowerPowerItemMagpropertyEdgesource:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:EDGESOURce`` command.

        Description:
            - This command sets or queries the edge source type for the magnetic property
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:EDGESOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:EDGESOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:EDGESOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:EDGESOURce {Current|VOLTAGE}
            - POWer:POWer<x>:MAGPROPERTY:EDGESOURce?
            ```

        Info:
            - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent
              of the number shown on a power measurement badge in the UI.
            - ``Current`` sets the measurement to use the primary voltage source as the signal edge
              for the magnetic property measurement.
            - ``VOLTAGE`` sets the measurement to use the primary current source as the signal edge
              for the magnetic property measurement.
        """
        return self._edgesource

    @property
    def isource(self) -> PowerPowerItemMagpropertyIsource:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:ISOURce`` command.

        Description:
            - This command sets or queries the current source for the magnetic property measurement
              of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:ISOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:ISOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:ISOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:ISOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:MAGPROPERTY:ISOURce?
            ```

        Info:
            - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._isource

    @property
    def length(self) -> PowerPowerItemMagpropertyLength:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:LENgth`` command.

        Description:
            - This command sets or queries the conductor length of the primary winding for magnetic
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:LENgth?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:LENgth?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:LENgth value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:LENgth <NR2>
            - POWer:POWer<x>:MAGPROPERTY:LENgth?
            ```

        Info:
            - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``<NR2>`` is the magnetic length, in the range of 1.00E-09 through 1,000,000.
        """
        return self._length

    @property
    def primaryturns(self) -> PowerPowerItemMagpropertyPrimaryturns:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs`` command.

        Description:
            - This command sets or queries the number of primary turns for magnetic measurement of
              the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs <NR1>
            - POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs?
            ```

        Info:
            - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``<NR1>`` is the integer number of turns in the primary winding, in the range of 1 to
              1 M.
        """
        return self._primaryturns

    @property
    def sec1source(self) -> PowerPowerItemMagpropertySec1source:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC1SOURce`` command.

        Description:
            - This command sets or queries the current source channel for secondary winding 1 for
              magnetic measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC1SOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC1SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC1SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC1SOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:MAGPROPERTY:SEC1SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._sec1source

    @property
    def sec1turns(self) -> PowerPowerItemMagpropertySec1turns:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC1TURNs`` command.

        Description:
            - This command sets or queries the number of turns of secondary winding 1 for magnetic
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC1TURNs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC1TURNs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC1TURNs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC1TURNs <NR1>
            - POWer:POWer<x>:MAGPROPERTY:SEC1TURNs?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to
              1,000,000.
        """
        return self._sec1turns

    @property
    def sec2source(self) -> PowerPowerItemMagpropertySec2source:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC2SOURce`` command.

        Description:
            - This command sets or queries the current source for secondary winding2 for magnetic
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC2SOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC2SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC2SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC2SOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:MAGPROPERTY:SEC2SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._sec2source

    @property
    def sec2turns(self) -> PowerPowerItemMagpropertySec2turns:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC2TURNs`` command.

        Description:
            - This command sets or queries the number of turns of secondary winding 2 for magnetic
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC2TURNs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC2TURNs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC2TURNs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC2TURNs <NR1>
            - POWer:POWer<x>:MAGPROPERTY:SEC2TURNs?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to
              1,000,000.
        """
        return self._sec2turns

    @property
    def sec3source(self) -> PowerPowerItemMagpropertySec3source:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC3SOURce`` command.

        Description:
            - This command sets or queries the current source channel for secondary winding 3 for
              magnetic measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC3SOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC3SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC3SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC3SOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:MAGPROPERTY:SEC3SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._sec3source

    @property
    def sec3turns(self) -> PowerPowerItemMagpropertySec3turns:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC3TURNs`` command.

        Description:
            - This command sets or queries the number of turns of secondary winding 3 for magnetic
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC3TURNs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC3TURNs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC3TURNs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC3TURNs <NR1>
            - POWer:POWer<x>:MAGPROPERTY:SEC3TURNs?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to
              1,000,000.
        """
        return self._sec3turns

    @property
    def sec4source(self) -> PowerPowerItemMagpropertySec4source:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC4SOURce`` command.

        Description:
            - This command sets or queries the current source for secondary winding 4 for magnetic
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC4SOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC4SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC4SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC4SOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:MAGPROPERTY:SEC4SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._sec4source

    @property
    def sec4turns(self) -> PowerPowerItemMagpropertySec4turns:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC4TURNs`` command.

        Description:
            - This command sets or queries the number of turns of secondary winding 4 for magnetic
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC4TURNs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC4TURNs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC4TURNs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC4TURNs <NR1>
            - POWer:POWer<x>:MAGPROPERTY:SEC4TURNs?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to
              1,000,000.
        """
        return self._sec4turns

    @property
    def sec5source(self) -> PowerPowerItemMagpropertySec5source:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC5SOURce`` command.

        Description:
            - This command sets or queries the current source for secondary winding 5 for magnetic
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC5SOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC5SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC5SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC5SOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:MAGPROPERTY:SEC5SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._sec5source

    @property
    def sec5turns(self) -> PowerPowerItemMagpropertySec5turns:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC5TURNs`` command.

        Description:
            - This command sets or queries the number of turns of secondary winding 5 for magnetic
              measurement of the specified power measurement badge.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC5TURNs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC5TURNs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC5TURNs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC5TURNs <NR1>
            - POWer:POWer<x>:MAGPROPERTY:SEC5TURNs?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to
              1,000,000.
        """
        return self._sec5turns

    @property
    def sec6source(self) -> PowerPowerItemMagpropertySec6source:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC6SOURce`` command.

        Description:
            - This command sets or queries the current source for secondary winding 6 for magnetic
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC6SOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC6SOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC6SOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC6SOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:MAGPROPERTY:SEC6SOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._sec6source

    @property
    def sec6turns(self) -> PowerPowerItemMagpropertySec6turns:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SEC6TURNs`` command.

        Description:
            - This command sets or queries the number of turns of secondary winding 6 for magnetic
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SEC6TURNs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC6TURNs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SEC6TURNs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SEC6TURNs <NR1>
            - POWer:POWer<x>:MAGPROPERTY:SEC6TURNs?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``<NR1>`` is the number of turns on the secondary winding, and ranges from 0 to
              1,000,000.
        """
        return self._sec6turns

    @property
    def secphase(self) -> PowerPowerItemMagpropertySecphase:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SECPhase`` command.

        Description:
            - This command sets or returns the value for the phase difference between secondary and
              primary voltage.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SECPhase?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SECPhase?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SECPhase value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SECPhase <NR3>
            - POWer:POWer<x>:MAGPROPERTY:SECPhase?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` sets the value for the phase difference between secondary and primary
              voltage, in the range of -180 to 180 degrees.
        """
        return self._secphase

    @property
    def secvolt(self) -> PowerPowerItemMagpropertySecvolt:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SECVolt`` command.

        Description:
            - This command enables or disables secondary voltage input for measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:SECVolt?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SECVolt?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SECVolt value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SECVolt {True|False}
            - POWer:POWer<x>:MAGPROPERTY:SECVolt?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``True`` enables secondary voltage source.
            - ``False`` disables secondary voltage source.
        """
        return self._secvolt

    @property
    def secwindings(self) -> PowerPowerItemMagpropertySecwindings:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:SECWINDings`` command.

        Description:
            - This command sets or queries the number of secondary windings for the magnetic
              property measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SECWINDings?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SECWINDings?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:SECWINDings value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:SECWINDings {None|ONE|TWO|THREE|FOUR|FIVE|SIX}
            - POWer:POWer<x>:MAGPROPERTY:SECWINDings?
            ```

        Info:
            - ``Power<x>`` is the magnetic property power measurement number. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``None`` , ONE, TWO, THREE, FOUR, FIVE, SIX sets the number of secondary windings to
              the specified value.
        """
        return self._secwindings

    @property
    def units(self) -> PowerPowerItemMagpropertyUnits:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:UNITs`` command.

        Description:
            - This command sets or queries the units for magnetic measurements of the specified
              power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:UNITs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:UNITs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:UNITs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:UNITs {SI|CGS}
            - POWer:POWer<x>:MAGPROPERTY:UNITs?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``SI`` sets the measurement to International System of Units.
            - ``CGS`` sets the measurement to Gaussian units.
        """
        return self._units

    @property
    def vsource(self) -> PowerPowerItemMagpropertyVsource:
        """Return the ``POWer:POWer<x>:MAGPROPERTY:VSOURce`` command.

        Description:
            - This command sets or queries the primary winding voltage source for the magnetic
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY:VSOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:VSOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGPROPERTY:VSOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGPROPERTY:VSOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:MAGPROPERTY:VSOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vsource


class PowerPowerItemMagneticlossVsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGNETICLOSS:VSOURce`` command.

    Description:
        - This command sets or queries the voltage source for magnetic measurement of the specified
          power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGNETICLOSS:VSOURce?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGNETICLOSS:VSOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGNETICLOSS:VSOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGNETICLOSS:VSOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:MAGNETICLOSS:VSOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemMagneticlossIsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:MAGNETICLOSS:ISOURce`` command.

    Description:
        - This command sets or queries the current source for the magnetic loss measurement of the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGNETICLOSS:ISOURce?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGNETICLOSS:ISOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:MAGNETICLOSS:ISOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:MAGNETICLOSS:ISOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:MAGNETICLOSS:ISOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemMagneticloss(SCPICmdRead):
    """The ``POWer:POWer<x>:MAGNETICLOSS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGNETICLOSS?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGNETICLOSS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.isource``: The ``POWer:POWer<x>:MAGNETICLOSS:ISOURce`` command.
        - ``.vsource``: The ``POWer:POWer<x>:MAGNETICLOSS:VSOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._isource = PowerPowerItemMagneticlossIsource(device, f"{self._cmd_syntax}:ISOURce")
        self._vsource = PowerPowerItemMagneticlossVsource(device, f"{self._cmd_syntax}:VSOURce")

    @property
    def isource(self) -> PowerPowerItemMagneticlossIsource:
        """Return the ``POWer:POWer<x>:MAGNETICLOSS:ISOURce`` command.

        Description:
            - This command sets or queries the current source for the magnetic loss measurement of
              the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGNETICLOSS:ISOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGNETICLOSS:ISOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGNETICLOSS:ISOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGNETICLOSS:ISOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:MAGNETICLOSS:ISOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._isource

    @property
    def vsource(self) -> PowerPowerItemMagneticlossVsource:
        """Return the ``POWer:POWer<x>:MAGNETICLOSS:VSOURce`` command.

        Description:
            - This command sets or queries the voltage source for magnetic measurement of the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGNETICLOSS:VSOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:MAGNETICLOSS:VSOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:MAGNETICLOSS:VSOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:MAGNETICLOSS:VSOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:MAGNETICLOSS:VSOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vsource


class PowerPowerItemLinerippleLfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:LINERIPPLE:LFREQuency`` command.

    Description:
        - This command sets or queries the frequency present for line ripple measurement of the
          specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:LINERIPPLE:LFREQuency?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:LINERIPPLE:LFREQuency?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:LINERIPPLE:LFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:LINERIPPLE:LFREQuency {FIFty|SIXty|FOURHundred}
        - POWer:POWer<x>:LINERIPPLE:LFREQuency?
        ```
    """


class PowerPowerItemLinerippleInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:LINERIPPLE:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for line ripple measurement of the specified
          power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:LINERIPPLE:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:LINERIPPLE:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:LINERIPPLE:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:LINERIPPLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:LINERIPPLE:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemLineripple(SCPICmdRead):
    """The ``POWer:POWer<x>:LINERIPPLE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:LINERIPPLE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:LINERIPPLE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:LINERIPPLE:INPUTSOurce`` command.
        - ``.lfrequency``: The ``POWer:POWer<x>:LINERIPPLE:LFREQuency`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemLinerippleInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )
        self._lfrequency = PowerPowerItemLinerippleLfrequency(
            device, f"{self._cmd_syntax}:LFREQuency"
        )

    @property
    def inputsource(self) -> PowerPowerItemLinerippleInputsource:
        """Return the ``POWer:POWer<x>:LINERIPPLE:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for line ripple measurement of the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:LINERIPPLE:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:LINERIPPLE:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:LINERIPPLE:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:LINERIPPLE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:LINERIPPLE:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource

    @property
    def lfrequency(self) -> PowerPowerItemLinerippleLfrequency:
        """Return the ``POWer:POWer<x>:LINERIPPLE:LFREQuency`` command.

        Description:
            - This command sets or queries the frequency present for line ripple measurement of the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:LINERIPPLE:LFREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:LINERIPPLE:LFREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:LINERIPPLE:LFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:LINERIPPLE:LFREQuency {FIFty|SIXty|FOURHundred}
            - POWer:POWer<x>:LINERIPPLE:LFREQuency?
            ```
        """
        return self._lfrequency


class PowerPowerItemLabel(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:LABel`` command.

    Description:
        - This command sets or queries the label for the specified power measurement. As the label
          can contain non 7-bit ASCII text, it is stored in Percent Encoding format. The power
          measurement badge is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:LABel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:LABel value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:LABel <QString>
        - POWer:POWer<x>:LABel?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class PowerPowerItemIvsintegralvVsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IVSINTEGRALV:VSOURce`` command.

    Description:
        - This command sets or queries the voltage source for I vs Integral V measurement of the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IVSINTEGRALV:VSOURce?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IVSINTEGRALV:VSOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IVSINTEGRALV:VSOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IVSINTEGRALV:VSOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:IVSINTEGRALV:VSOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemIvsintegralvIsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IVSINTEGRALV:ISOURce`` command.

    Description:
        - This command sets or queries the current source for I vs Integral V measurement of the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IVSINTEGRALV:ISOURce?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IVSINTEGRALV:ISOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IVSINTEGRALV:ISOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IVSINTEGRALV:ISOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:IVSINTEGRALV:ISOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
        - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemIvsintegralv(SCPICmdRead):
    """The ``POWer:POWer<x>:IVSINTEGRALV`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IVSINTEGRALV?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IVSINTEGRALV?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.isource``: The ``POWer:POWer<x>:IVSINTEGRALV:ISOURce`` command.
        - ``.vsource``: The ``POWer:POWer<x>:IVSINTEGRALV:VSOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._isource = PowerPowerItemIvsintegralvIsource(device, f"{self._cmd_syntax}:ISOURce")
        self._vsource = PowerPowerItemIvsintegralvVsource(device, f"{self._cmd_syntax}:VSOURce")

    @property
    def isource(self) -> PowerPowerItemIvsintegralvIsource:
        """Return the ``POWer:POWer<x>:IVSINTEGRALV:ISOURce`` command.

        Description:
            - This command sets or queries the current source for I vs Integral V measurement of the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IVSINTEGRALV:ISOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IVSINTEGRALV:ISOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IVSINTEGRALV:ISOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IVSINTEGRALV:ISOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:IVSINTEGRALV:ISOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._isource

    @property
    def vsource(self) -> PowerPowerItemIvsintegralvVsource:
        """Return the ``POWer:POWer<x>:IVSINTEGRALV:VSOURce`` command.

        Description:
            - This command sets or queries the voltage source for I vs Integral V measurement of the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IVSINTEGRALV:VSOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IVSINTEGRALV:VSOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IVSINTEGRALV:VSOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IVSINTEGRALV:VSOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:IVSINTEGRALV:VSOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
            - ``CH<x>`` sets the channel specifier; <x> is 1 through 8 and is limited by the number
              of FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vsource


class PowerPowerItemInrushcurrentPeakcurrent(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:INRUSHcurrent:PEAKCURRent`` command.

    Description:
        - This command sets or returns the peak current value of the specified Inrush Current
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INRUSHcurrent:PEAKCURRent?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:INRUSHcurrent:PEAKCURRent?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:INRUSHcurrent:PEAKCURRent value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:INRUSHcurrent:PEAKCURRent <NR3>
        - POWer:POWer<x>:INRUSHcurrent:PEAKCURRent?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR3>`` is a floating point number that represents the peak current value, in amps, in
          the range -100 A to 100 A.
    """


class PowerPowerItemInrushcurrentInputsource(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:INRUSHcurrent:INPUTSOurce`` command.

    Description:
        - This command sets or returns the input source of the specified Inrush Current measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INRUSHcurrent:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:INRUSHcurrent:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:INRUSHcurrent:INPUTSOurce``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:INRUSHcurrent:INPUTSOurce
        - POWer:POWer<x>:INRUSHcurrent:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` is the channel specifier in the range of 1 through 8 and is limited by the
          number of instrument input channels.
        - ``REF<x>`` is the Reference waveform specifier ≥1. This is the equivalent of the number
          shown on a Reference waveform badge in the UI.
        - ``MATH<x>`` is the Math waveform specifier ≥1. This is the equivalent of the number shown
          on a Math waveform badge in the UI.
    """


class PowerPowerItemInrushcurrent(SCPICmdRead):
    """The ``POWer:POWer<x>:INRUSHcurrent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INRUSHcurrent?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INRUSHcurrent?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:INRUSHcurrent:INPUTSOurce`` command.
        - ``.peakcurrent``: The ``POWer:POWer<x>:INRUSHcurrent:PEAKCURRent`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemInrushcurrentInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )
        self._peakcurrent = PowerPowerItemInrushcurrentPeakcurrent(
            device, f"{self._cmd_syntax}:PEAKCURRent"
        )

    @property
    def inputsource(self) -> PowerPowerItemInrushcurrentInputsource:
        """Return the ``POWer:POWer<x>:INRUSHcurrent:INPUTSOurce`` command.

        Description:
            - This command sets or returns the input source of the specified Inrush Current
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:INRUSHcurrent:INPUTSOurce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:INRUSHcurrent:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the
              ``POWer:POWer<x>:INRUSHcurrent:INPUTSOurce`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:INRUSHcurrent:INPUTSOurce
            - POWer:POWer<x>:INRUSHcurrent:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` is the channel specifier in the range of 1 through 8 and is limited by the
              number of instrument input channels.
            - ``REF<x>`` is the Reference waveform specifier ≥1. This is the equivalent of the
              number shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` is the Math waveform specifier ≥1. This is the equivalent of the number
              shown on a Math waveform badge in the UI.
        """
        return self._inputsource

    @property
    def peakcurrent(self) -> PowerPowerItemInrushcurrentPeakcurrent:
        """Return the ``POWer:POWer<x>:INRUSHcurrent:PEAKCURRent`` command.

        Description:
            - This command sets or returns the peak current value of the specified Inrush Current
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:INRUSHcurrent:PEAKCURRent?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:INRUSHcurrent:PEAKCURRent?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:INRUSHcurrent:PEAKCURRent value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:INRUSHcurrent:PEAKCURRent <NR3>
            - POWer:POWer<x>:INRUSHcurrent:PEAKCURRent?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR3>`` is a floating point number that represents the peak current value, in amps,
              in the range -100 A to 100 A.
        """
        return self._peakcurrent


class PowerPowerItemInputcapVsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:INPUTCAP:VSOURce`` command.

    Description:
        - This command sets or queries the input voltage source of the specified Input Capacitance
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INPUTCAP:VSOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INPUTCAP:VSOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:INPUTCAP:VSOURce value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:INPUTCAP:VSOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:INPUTCAP:VSOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` is the channel specifier in the range of 1 through 8 and is limited by the
          number of instrument input channels.
        - ``REF<x>`` is the Reference waveform specifier ≥1. This is the equivalent of the number
          shown on a Reference waveform badge in the UI.
        - ``MATH<x>`` is the Math waveform specifier ≥1. This is the equivalent of the number shown
          on a Math waveform badge in the UI.
    """


class PowerPowerItemInputcapPeakvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:INPUTCAP:PEAKVOLTage`` command.

    Description:
        - This command sets or queries the peak voltage value of the specified Input Capacitance
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INPUTCAP:PEAKVOLTage?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INPUTCAP:PEAKVOLTage?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:INPUTCAP:PEAKVOLTage value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:INPUTCAP:PEAKVOLTage <NR3>
        - POWer:POWer<x>:INPUTCAP:PEAKVOLTage?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR3>`` is a floating point number that represents the peak voltage value in the range
          -100 V to 100 V.
    """


class PowerPowerItemInputcapPeakcurrent(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:INPUTCAP:PEAKCURRent`` command.

    Description:
        - This command sets or queries the peak current value of the specified Input Capacitance
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INPUTCAP:PEAKCURRent?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INPUTCAP:PEAKCURRent?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:INPUTCAP:PEAKCURRent value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:INPUTCAP:PEAKCURRent <NR3>
        - POWer:POWer<x>:INPUTCAP:PEAKCURRent?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR3>`` is a floating point number that represents the peak current value, in amps, in
          the range -100 A to 100 A.
    """


class PowerPowerItemInputcapIsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:INPUTCAP:ISOURce`` command.

    Description:
        - This command sets or queries the inrush current input source of the specified Input
          Capacitance measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INPUTCAP:ISOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INPUTCAP:ISOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:INPUTCAP:ISOURce value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:INPUTCAP:ISOURce {CH<x>|REF<x>|MATH<x>}
        - POWer:POWer<x>:INPUTCAP:ISOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` is the channel specifier in the range of 1 through 8 and is limited by the
          number of instrument input channels.
        - ``REF<x>`` is the Reference waveform specifier ≥1. This is the equivalent of the number
          shown on a Reference waveform badge in the UI.
        - ``MATH<x>`` is the Math waveform specifier ≥1. This is the equivalent of the number shown
          on a Math waveform badge in the UI.
    """


class PowerPowerItemInputcap(SCPICmdRead):
    """The ``POWer:POWer<x>:INPUTCAP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INPUTCAP?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INPUTCAP?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.isource``: The ``POWer:POWer<x>:INPUTCAP:ISOURce`` command.
        - ``.peakcurrent``: The ``POWer:POWer<x>:INPUTCAP:PEAKCURRent`` command.
        - ``.peakvoltage``: The ``POWer:POWer<x>:INPUTCAP:PEAKVOLTage`` command.
        - ``.vsource``: The ``POWer:POWer<x>:INPUTCAP:VSOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._isource = PowerPowerItemInputcapIsource(device, f"{self._cmd_syntax}:ISOURce")
        self._peakcurrent = PowerPowerItemInputcapPeakcurrent(
            device, f"{self._cmd_syntax}:PEAKCURRent"
        )
        self._peakvoltage = PowerPowerItemInputcapPeakvoltage(
            device, f"{self._cmd_syntax}:PEAKVOLTage"
        )
        self._vsource = PowerPowerItemInputcapVsource(device, f"{self._cmd_syntax}:VSOURce")

    @property
    def isource(self) -> PowerPowerItemInputcapIsource:
        """Return the ``POWer:POWer<x>:INPUTCAP:ISOURce`` command.

        Description:
            - This command sets or queries the inrush current input source of the specified Input
              Capacitance measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:INPUTCAP:ISOURce?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INPUTCAP:ISOURce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:INPUTCAP:ISOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:INPUTCAP:ISOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:INPUTCAP:ISOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` is the channel specifier in the range of 1 through 8 and is limited by the
              number of instrument input channels.
            - ``REF<x>`` is the Reference waveform specifier ≥1. This is the equivalent of the
              number shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` is the Math waveform specifier ≥1. This is the equivalent of the number
              shown on a Math waveform badge in the UI.
        """
        return self._isource

    @property
    def peakcurrent(self) -> PowerPowerItemInputcapPeakcurrent:
        """Return the ``POWer:POWer<x>:INPUTCAP:PEAKCURRent`` command.

        Description:
            - This command sets or queries the peak current value of the specified Input Capacitance
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:INPUTCAP:PEAKCURRent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:INPUTCAP:PEAKCURRent?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:INPUTCAP:PEAKCURRent value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:INPUTCAP:PEAKCURRent <NR3>
            - POWer:POWer<x>:INPUTCAP:PEAKCURRent?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR3>`` is a floating point number that represents the peak current value, in amps,
              in the range -100 A to 100 A.
        """
        return self._peakcurrent

    @property
    def peakvoltage(self) -> PowerPowerItemInputcapPeakvoltage:
        """Return the ``POWer:POWer<x>:INPUTCAP:PEAKVOLTage`` command.

        Description:
            - This command sets or queries the peak voltage value of the specified Input Capacitance
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:INPUTCAP:PEAKVOLTage?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:INPUTCAP:PEAKVOLTage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:INPUTCAP:PEAKVOLTage value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:INPUTCAP:PEAKVOLTage <NR3>
            - POWer:POWer<x>:INPUTCAP:PEAKVOLTage?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR3>`` is a floating point number that represents the peak voltage value in the
              range -100 V to 100 V.
        """
        return self._peakvoltage

    @property
    def vsource(self) -> PowerPowerItemInputcapVsource:
        """Return the ``POWer:POWer<x>:INPUTCAP:VSOURce`` command.

        Description:
            - This command sets or queries the input voltage source of the specified Input
              Capacitance measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:INPUTCAP:VSOURce?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INPUTCAP:VSOURce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:INPUTCAP:VSOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:INPUTCAP:VSOURce {CH<x>|REF<x>|MATH<x>}
            - POWer:POWer<x>:INPUTCAP:VSOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` is the channel specifier in the range of 1 through 8 and is limited by the
              number of instrument input channels.
            - ``REF<x>`` is the Reference waveform specifier ≥1. This is the equivalent of the
              number shown on a Reference waveform badge in the UI.
            - ``MATH<x>`` is the Math waveform specifier ≥1. This is the equivalent of the number
              shown on a Math waveform badge in the UI.
        """
        return self._vsource


class PowerPowerItemInductanceVsource(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:INDUCTANCE:VSOURce`` command.

    Description:
        - This command sets or queries the voltage source for inductance measurement of the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INDUCTANCE:VSOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INDUCTANCE:VSOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:INDUCTANCE:VSOURce`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:INDUCTANCE:VSOURce
        - POWer:POWer<x>:INDUCTANCE:VSOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemInductanceIsource(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:INDUCTANCE:ISOUrce`` command.

    Description:
        - This command sets or queries the current signal source for the inductance measurement of
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INDUCTANCE:ISOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INDUCTANCE:ISOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:INDUCTANCE:ISOUrce`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:INDUCTANCE:ISOUrce
        - POWer:POWer<x>:INDUCTANCE:ISOUrce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemInductanceEdgesource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:INDUCTANCE:EDGESource`` command.

    Description:
        - This command sets or queries the edge source for the power inductance measurement of the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INDUCTANCE:EDGESource?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:INDUCTANCE:EDGESource?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:INDUCTANCE:EDGESource value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:INDUCTANCE:EDGESource {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:INDUCTANCE:EDGESource?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemInductance(SCPICmdRead):
    """The ``POWer:POWer<x>:INDUCTANCE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:INDUCTANCE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INDUCTANCE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edgesource``: The ``POWer:POWer<x>:INDUCTANCE:EDGESource`` command.
        - ``.isource``: The ``POWer:POWer<x>:INDUCTANCE:ISOUrce`` command.
        - ``.vsource``: The ``POWer:POWer<x>:INDUCTANCE:VSOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edgesource = PowerPowerItemInductanceEdgesource(
            device, f"{self._cmd_syntax}:EDGESource"
        )
        self._isource = PowerPowerItemInductanceIsource(device, f"{self._cmd_syntax}:ISOUrce")
        self._vsource = PowerPowerItemInductanceVsource(device, f"{self._cmd_syntax}:VSOURce")

    @property
    def edgesource(self) -> PowerPowerItemInductanceEdgesource:
        """Return the ``POWer:POWer<x>:INDUCTANCE:EDGESource`` command.

        Description:
            - This command sets or queries the edge source for the power inductance measurement of
              the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:INDUCTANCE:EDGESource?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:INDUCTANCE:EDGESource?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:INDUCTANCE:EDGESource value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:INDUCTANCE:EDGESource {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:INDUCTANCE:EDGESource?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._edgesource

    @property
    def isource(self) -> PowerPowerItemInductanceIsource:
        """Return the ``POWer:POWer<x>:INDUCTANCE:ISOUrce`` command.

        Description:
            - This command sets or queries the current signal source for the inductance measurement
              of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:INDUCTANCE:ISOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:INDUCTANCE:ISOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``POWer:POWer<x>:INDUCTANCE:ISOUrce``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:INDUCTANCE:ISOUrce
            - POWer:POWer<x>:INDUCTANCE:ISOUrce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._isource

    @property
    def vsource(self) -> PowerPowerItemInductanceVsource:
        """Return the ``POWer:POWer<x>:INDUCTANCE:VSOURce`` command.

        Description:
            - This command sets or queries the voltage source for inductance measurement of the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:INDUCTANCE:VSOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:INDUCTANCE:VSOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``POWer:POWer<x>:INDUCTANCE:VSOURce``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:INDUCTANCE:VSOURce
            - POWer:POWer<x>:INDUCTANCE:VSOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vsource


class PowerPowerItemImpedanceTestconnection(SCPICmdWrite):
    """The ``POWer:POWer<x>:IMPEDANCE:TESTCONNection`` command.

    Description:
        - This command tests the connection with the external instrument for the specified Impedance
          measurement.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:TESTCONNection value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:TESTCONNection {EXECute}
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``EXECute`` runs the test connection function.
    """


class PowerPowerItemImpedanceStopfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:STOPFREQuency`` command.

    Description:
        - Sets or queries the value of the specified Impedance measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:STOPFREQuency?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:STOPFREQuency?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:STOPFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:STOPFREQuency <NR3>
        - POWer:POWer<x>:IMPEDANCE:STOPFREQuency?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``<NR3>`` specifies the start frequency, in the range of 10 Hz to 50 MHz.
    """


class PowerPowerItemImpedanceStartfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:STARTFREQuency`` command.

    Description:
        - Sets or queries the value for the start frequency of the specified Impedance measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:STARTFREQuency?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:STARTFREQuency?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:STARTFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:STARTFREQuency <NR3>
        - POWer:POWer<x>:IMPEDANCE:STARTFREQuency?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``<NR3>`` is a floating point number representing the start frequency, in the range of 10
          Hz to 50 MHz.
    """


class PowerPowerItemImpedancePpd(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:PPD`` command.

    Description:
        - Sets or queries the value for points per decade for the specified Impedance measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:PPD?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IMPEDANCE:PPD?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:IMPEDANCE:PPD value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:PPD <NR1>
        - POWer:POWer<x>:IMPEDANCE:PPD?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``<NR1>`` specifies the number of frequency points between the start and stop frequency in
          terms of log scale, in the range of 10 to 100 points.
    """


class PowerPowerItemImpedanceOutputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce`` command.

    Description:
        - Sets or queries the source for the Impedance output measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``CH<x>`` specifies the instrument input channel number.
        - ``MATH<x>`` specifies the instrument math waveform number.
        - ``REF<x>`` specifies the instrument reference waveform number.
    """


class PowerPowerItemImpedanceInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:INPUTSOurce`` command.

    Description:
        - Sets or queries the source for the Impedance input measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:IMPEDANCE:INPUTSOurce?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``CH<x>`` specifies the instrument input channel number.
        - ``MATH<x>`` specifies the instrument math waveform number.
        - ``REF<x>`` specifies the instrument reference waveform number.
    """


class PowerPowerItemImpedanceImpedance(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:IMPEDANCE`` command.

    Description:
        - Sets or queries the output impedance of the generator for the specified Impedance power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:IMPEDANCE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IMPEDANCE:IMPEDANCE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:IMPEDANCE value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:IMPEDANCE {FIFTy|HIGHZ}
        - POWer:POWer<x>:IMPEDANCE:IMPEDANCE?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``FIFTy`` sets the measurement impedance to 50`Ω.
        - ``HIGHZ`` sets the measurement impedance to 1`MΩ.
    """


class PowerPowerItemImpedanceGenerator(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:GENerator`` command.

    Description:
        - Sets or queries the generator source for the Impedance power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:GENerator?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IMPEDANCE:GENerator?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:GENerator value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:GENerator {INTernal|EXTernal}
        - POWer:POWer<x>:IMPEDANCE:GENerator?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``INTernal`` sets the internal generator as the source for the Impedance power
          measurement.
        - ``EXTernal`` sets the external generator as the source for the Impedance power
          measurement. Supported external generators are the Tektronix AFG31000 and AFG3000 series.
    """


class PowerPowerItemImpedanceGenipaddress(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:GENIPADDress`` command.

    Description:
        - Sets or queries the external generator IP Address associated with the specified Impedance
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:GENIPADDress?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:GENIPADDress?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:GENIPADDress value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:GENIPADDress <String>
        - POWer:POWer<x>:IMPEDANCE:GENIPADDress?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.<string> is the IP address
          of the generator.
    """


class PowerPowerItemImpedanceFreqvalItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:FREQ<x>Val`` command.

    Description:
        - Sets or queries the signal generator start frequency of the specified profile step, for
          the specified Impedance measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:FREQ<x>Val?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IMPEDANCE:FREQ<x>Val?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:FREQ<x>Val value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:FREQ<x>Val <NR3>
        - POWer:POWer<x>:IMPEDANCE:FREQ<x>Val?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``FREQ<x>`` specifies the number of the profile step. The valid range is 1 to 10.
        - ``<NR3>`` sets the start frequency, in the range of 10 Hz to 50 MHz, for the specified
          profile step. You can only set the starting frequency for each profile step; the stop
          frequency is automatically set to same value as the start frequency of the next profile
          step. For example, if Step one is set to 1`MHz, and Step two is set to 2`MHz, then the
          Step one stop frequency is 2`MHz.
    """


class PowerPowerItemImpedanceConstamplitude(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude`` command.

    Description:
        - Sets or queries the constant amplitude value for the specified Impedance measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude <NR3>
        - POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``<NR3>`` specifies the constant amplitude value, in the range of -100 V to 100 V.
    """


class PowerPowerItemImpedanceConnectstatus(SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:CONNECTSTATus`` command.

    Description:
        - Queries the instrument's connection status to the external generator, for the specified
          Impedance measurement. The Impedance measurement generator IP address (for external
          generators) is set with ``POWER:POWERX:IMPEDANCE:GENIPADDRESS``.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:CONNECTSTATus?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:CONNECTSTATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:CONNECTSTATus?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
    """


class PowerPowerItemImpedanceAutorbw(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:AUTORbw`` command.

    Description:
        - This command enables Auto RBW computation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:AUTORbw?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IMPEDANCE:AUTORbw?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:AUTORbw value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:AUTORbw {True|False}
        - POWer:POWer<x>:IMPEDANCE:AUTORbw?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``True`` enables Auto RBW computation.
        - ``False`` disables Auto RBW computation.
    """


class PowerPowerItemImpedanceAnalysismethod(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:ANALYSISMethod`` command.

    Description:
        - This command sets or queries the Analysis Method for Impedance measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:ANALYSISMethod?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:ANALYSISMethod?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:ANALYSISMethod value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:ANALYSISMethod {SV|FFT}
        - POWer:POWer<x>:IMPEDANCE:ANALYSISMethod?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``SV`` sets the Analysis Method as Spectrum View.
        - ``FFT`` sets the Analysis Method as FFT.
    """


class PowerPowerItemImpedanceAmpmode(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:AMPMode`` command.

    Description:
        - Sets or queries the power amplitude mode for the Impedance measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:AMPMode?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IMPEDANCE:AMPMode?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:AMPMode value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:AMPMode {CONSTant|PROFile}
        - POWer:POWer<x>:IMPEDANCE:AMPMode?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``CONSTant`` sets the generator to output a constant level signal.
        - ``PROFile`` uses related commands to set the generator output signal profile (Start
          frequency, Stop frequency, and Amplitude for each profile step).
    """


class PowerPowerItemImpedanceAmpvalItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE:AMP<x>Val`` command.

    Description:
        - Sets or queries the signal generator amplitude setting of the specified profile step, for
          the specified Impedance measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:AMP<x>Val?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IMPEDANCE:AMP<x>Val?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:IMPEDANCE:AMP<x>Val value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:IMPEDANCE:AMP<x>Val <NR3>
        - POWer:POWer<x>:IMPEDANCE:AMP<x>Val?
        ```

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.
        - ``AMP<x>`` specifies the number of the profile step. The valid range is 1 to 10.
        - ``<NR3>`` sets the generator output amplitude for the specified profile step, in the range
          -100 V to 100 V.
    """


#  pylint: disable=too-many-instance-attributes
class PowerPowerItemImpedance(SCPICmdRead):
    """The ``POWer:POWer<x>:IMPEDANCE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IMPEDANCE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``POWer<x>`` is the number of the Impedance power measurement.

    Properties:
        - ``.ampval``: The ``POWer:POWer<x>:IMPEDANCE:AMP<x>Val`` command.
        - ``.ampmode``: The ``POWer:POWer<x>:IMPEDANCE:AMPMode`` command.
        - ``.analysismethod``: The ``POWer:POWer<x>:IMPEDANCE:ANALYSISMethod`` command.
        - ``.autorbw``: The ``POWer:POWer<x>:IMPEDANCE:AUTORbw`` command.
        - ``.connectstatus``: The ``POWer:POWer<x>:IMPEDANCE:CONNECTSTATus`` command.
        - ``.constamplitude``: The ``POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude`` command.
        - ``.freqval``: The ``POWer:POWer<x>:IMPEDANCE:FREQ<x>Val`` command.
        - ``.genipaddress``: The ``POWer:POWer<x>:IMPEDANCE:GENIPADDress`` command.
        - ``.generator``: The ``POWer:POWer<x>:IMPEDANCE:GENerator`` command.
        - ``.impedance``: The ``POWer:POWer<x>:IMPEDANCE:IMPEDANCE`` command.
        - ``.inputsource``: The ``POWer:POWer<x>:IMPEDANCE:INPUTSOurce`` command.
        - ``.outputsource``: The ``POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce`` command.
        - ``.ppd``: The ``POWer:POWer<x>:IMPEDANCE:PPD`` command.
        - ``.startfrequency``: The ``POWer:POWer<x>:IMPEDANCE:STARTFREQuency`` command.
        - ``.stopfrequency``: The ``POWer:POWer<x>:IMPEDANCE:STOPFREQuency`` command.
        - ``.testconnection``: The ``POWer:POWer<x>:IMPEDANCE:TESTCONNection`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ampval: Dict[int, PowerPowerItemImpedanceAmpvalItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerPowerItemImpedanceAmpvalItem(device, f"{self._cmd_syntax}:AMP{x}Val")
        )
        self._ampmode = PowerPowerItemImpedanceAmpmode(device, f"{self._cmd_syntax}:AMPMode")
        self._analysismethod = PowerPowerItemImpedanceAnalysismethod(
            device, f"{self._cmd_syntax}:ANALYSISMethod"
        )
        self._autorbw = PowerPowerItemImpedanceAutorbw(device, f"{self._cmd_syntax}:AUTORbw")
        self._connectstatus = PowerPowerItemImpedanceConnectstatus(
            device, f"{self._cmd_syntax}:CONNECTSTATus"
        )
        self._constamplitude = PowerPowerItemImpedanceConstamplitude(
            device, f"{self._cmd_syntax}:CONSTAMPlitude"
        )
        self._freqval: Dict[int, PowerPowerItemImpedanceFreqvalItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerPowerItemImpedanceFreqvalItem(device, f"{self._cmd_syntax}:FREQ{x}Val")
        )
        self._genipaddress = PowerPowerItemImpedanceGenipaddress(
            device, f"{self._cmd_syntax}:GENIPADDress"
        )
        self._generator = PowerPowerItemImpedanceGenerator(device, f"{self._cmd_syntax}:GENerator")
        self._impedance = PowerPowerItemImpedanceImpedance(device, f"{self._cmd_syntax}:IMPEDANCE")
        self._inputsource = PowerPowerItemImpedanceInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )
        self._outputsource = PowerPowerItemImpedanceOutputsource(
            device, f"{self._cmd_syntax}:OUTPUTSOurce"
        )
        self._ppd = PowerPowerItemImpedancePpd(device, f"{self._cmd_syntax}:PPD")
        self._startfrequency = PowerPowerItemImpedanceStartfrequency(
            device, f"{self._cmd_syntax}:STARTFREQuency"
        )
        self._stopfrequency = PowerPowerItemImpedanceStopfrequency(
            device, f"{self._cmd_syntax}:STOPFREQuency"
        )
        self._testconnection = PowerPowerItemImpedanceTestconnection(
            device, f"{self._cmd_syntax}:TESTCONNection"
        )

    @property
    def ampval(self) -> Dict[int, PowerPowerItemImpedanceAmpvalItem]:
        """Return the ``POWer:POWer<x>:IMPEDANCE:AMP<x>Val`` command.

        Description:
            - Sets or queries the signal generator amplitude setting of the specified profile step,
              for the specified Impedance measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:AMP<x>Val?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:AMP<x>Val?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:AMP<x>Val value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:AMP<x>Val <NR3>
            - POWer:POWer<x>:IMPEDANCE:AMP<x>Val?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``AMP<x>`` specifies the number of the profile step. The valid range is 1 to 10.
            - ``<NR3>`` sets the generator output amplitude for the specified profile step, in the
              range -100 V to 100 V.
        """
        return self._ampval

    @property
    def ampmode(self) -> PowerPowerItemImpedanceAmpmode:
        """Return the ``POWer:POWer<x>:IMPEDANCE:AMPMode`` command.

        Description:
            - Sets or queries the power amplitude mode for the Impedance measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:AMPMode?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:AMPMode?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:AMPMode value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:AMPMode {CONSTant|PROFile}
            - POWer:POWer<x>:IMPEDANCE:AMPMode?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``CONSTant`` sets the generator to output a constant level signal.
            - ``PROFile`` uses related commands to set the generator output signal profile (Start
              frequency, Stop frequency, and Amplitude for each profile step).
        """
        return self._ampmode

    @property
    def analysismethod(self) -> PowerPowerItemImpedanceAnalysismethod:
        """Return the ``POWer:POWer<x>:IMPEDANCE:ANALYSISMethod`` command.

        Description:
            - This command sets or queries the Analysis Method for Impedance measurements.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:ANALYSISMethod?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:ANALYSISMethod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:ANALYSISMethod value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:ANALYSISMethod {SV|FFT}
            - POWer:POWer<x>:IMPEDANCE:ANALYSISMethod?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``SV`` sets the Analysis Method as Spectrum View.
            - ``FFT`` sets the Analysis Method as FFT.
        """
        return self._analysismethod

    @property
    def autorbw(self) -> PowerPowerItemImpedanceAutorbw:
        """Return the ``POWer:POWer<x>:IMPEDANCE:AUTORbw`` command.

        Description:
            - This command enables Auto RBW computation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:AUTORbw?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:AUTORbw?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:AUTORbw value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:AUTORbw {True|False}
            - POWer:POWer<x>:IMPEDANCE:AUTORbw?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``True`` enables Auto RBW computation.
            - ``False`` disables Auto RBW computation.
        """
        return self._autorbw

    @property
    def connectstatus(self) -> PowerPowerItemImpedanceConnectstatus:
        """Return the ``POWer:POWer<x>:IMPEDANCE:CONNECTSTATus`` command.

        Description:
            - Queries the instrument's connection status to the external generator, for the
              specified Impedance measurement. The Impedance measurement generator IP address (for
              external generators) is set with ``POWER:POWERX:IMPEDANCE:GENIPADDRESS``.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:CONNECTSTATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:CONNECTSTATus?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:CONNECTSTATus?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
        """
        return self._connectstatus

    @property
    def constamplitude(self) -> PowerPowerItemImpedanceConstamplitude:
        """Return the ``POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude`` command.

        Description:
            - Sets or queries the constant amplitude value for the specified Impedance measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude <NR3>
            - POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``<NR3>`` specifies the constant amplitude value, in the range of -100 V to 100 V.
        """
        return self._constamplitude

    @property
    def freqval(self) -> Dict[int, PowerPowerItemImpedanceFreqvalItem]:
        """Return the ``POWer:POWer<x>:IMPEDANCE:FREQ<x>Val`` command.

        Description:
            - Sets or queries the signal generator start frequency of the specified profile step,
              for the specified Impedance measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:FREQ<x>Val?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:FREQ<x>Val?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:FREQ<x>Val value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:FREQ<x>Val <NR3>
            - POWer:POWer<x>:IMPEDANCE:FREQ<x>Val?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``FREQ<x>`` specifies the number of the profile step. The valid range is 1 to 10.
            - ``<NR3>`` sets the start frequency, in the range of 10 Hz to 50 MHz, for the specified
              profile step. You can only set the starting frequency for each profile step; the stop
              frequency is automatically set to same value as the start frequency of the next
              profile step. For example, if Step one is set to 1`MHz, and Step two is set to 2`MHz,
              then the Step one stop frequency is 2`MHz.
        """
        return self._freqval

    @property
    def genipaddress(self) -> PowerPowerItemImpedanceGenipaddress:
        """Return the ``POWer:POWer<x>:IMPEDANCE:GENIPADDress`` command.

        Description:
            - Sets or queries the external generator IP Address associated with the specified
              Impedance measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:GENIPADDress?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:GENIPADDress?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:GENIPADDress value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:GENIPADDress <String>
            - POWer:POWer<x>:IMPEDANCE:GENIPADDress?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.<string> is the IP
              address of the generator.
        """
        return self._genipaddress

    @property
    def generator(self) -> PowerPowerItemImpedanceGenerator:
        """Return the ``POWer:POWer<x>:IMPEDANCE:GENerator`` command.

        Description:
            - Sets or queries the generator source for the Impedance power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:GENerator?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:GENerator?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:GENerator value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:GENerator {INTernal|EXTernal}
            - POWer:POWer<x>:IMPEDANCE:GENerator?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``INTernal`` sets the internal generator as the source for the Impedance power
              measurement.
            - ``EXTernal`` sets the external generator as the source for the Impedance power
              measurement. Supported external generators are the Tektronix AFG31000 and AFG3000
              series.
        """
        return self._generator

    @property
    def impedance(self) -> PowerPowerItemImpedanceImpedance:
        """Return the ``POWer:POWer<x>:IMPEDANCE:IMPEDANCE`` command.

        Description:
            - Sets or queries the output impedance of the generator for the specified Impedance
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:IMPEDANCE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:IMPEDANCE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:IMPEDANCE value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:IMPEDANCE {FIFTy|HIGHZ}
            - POWer:POWer<x>:IMPEDANCE:IMPEDANCE?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``FIFTy`` sets the measurement impedance to 50`Ω.
            - ``HIGHZ`` sets the measurement impedance to 1`MΩ.
        """
        return self._impedance

    @property
    def inputsource(self) -> PowerPowerItemImpedanceInputsource:
        """Return the ``POWer:POWer<x>:IMPEDANCE:INPUTSOurce`` command.

        Description:
            - Sets or queries the source for the Impedance input measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:IMPEDANCE:INPUTSOurce?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``CH<x>`` specifies the instrument input channel number.
            - ``MATH<x>`` specifies the instrument math waveform number.
            - ``REF<x>`` specifies the instrument reference waveform number.
        """
        return self._inputsource

    @property
    def outputsource(self) -> PowerPowerItemImpedanceOutputsource:
        """Return the ``POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce`` command.

        Description:
            - Sets or queries the source for the Impedance output measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``CH<x>`` specifies the instrument input channel number.
            - ``MATH<x>`` specifies the instrument math waveform number.
            - ``REF<x>`` specifies the instrument reference waveform number.
        """
        return self._outputsource

    @property
    def ppd(self) -> PowerPowerItemImpedancePpd:
        """Return the ``POWer:POWer<x>:IMPEDANCE:PPD`` command.

        Description:
            - Sets or queries the value for points per decade for the specified Impedance
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE:PPD?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IMPEDANCE:PPD?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:PPD value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:PPD <NR1>
            - POWer:POWer<x>:IMPEDANCE:PPD?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``<NR1>`` specifies the number of frequency points between the start and stop
              frequency in terms of log scale, in the range of 10 to 100 points.
        """
        return self._ppd

    @property
    def startfrequency(self) -> PowerPowerItemImpedanceStartfrequency:
        """Return the ``POWer:POWer<x>:IMPEDANCE:STARTFREQuency`` command.

        Description:
            - Sets or queries the value for the start frequency of the specified Impedance
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:STARTFREQuency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:STARTFREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:STARTFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:STARTFREQuency <NR3>
            - POWer:POWer<x>:IMPEDANCE:STARTFREQuency?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``<NR3>`` is a floating point number representing the start frequency, in the range of
              10 Hz to 50 MHz.
        """
        return self._startfrequency

    @property
    def stopfrequency(self) -> PowerPowerItemImpedanceStopfrequency:
        """Return the ``POWer:POWer<x>:IMPEDANCE:STOPFREQuency`` command.

        Description:
            - Sets or queries the value of the specified Impedance measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:STOPFREQuency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:STOPFREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:STOPFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:STOPFREQuency <NR3>
            - POWer:POWer<x>:IMPEDANCE:STOPFREQuency?
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``<NR3>`` specifies the start frequency, in the range of 10 Hz to 50 MHz.
        """
        return self._stopfrequency

    @property
    def testconnection(self) -> PowerPowerItemImpedanceTestconnection:
        """Return the ``POWer:POWer<x>:IMPEDANCE:TESTCONNection`` command.

        Description:
            - This command tests the connection with the external instrument for the specified
              Impedance measurement.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:IMPEDANCE:TESTCONNection value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:IMPEDANCE:TESTCONNection {EXECute}
            ```

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.
            - ``EXECute`` runs the test connection function.
        """
        return self._testconnection


class PowerPowerItemHarmonicsVsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:VSOURce`` command.

    Description:
        - This command sets or queries the voltage source for SOA measurement of the specified power
          measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:VSOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:VSOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:VSOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:VSOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:HARMONICS:VSOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemHarmonicsUnits(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:UNITs`` command.

    Description:
        - This command sets or queries the harmonics results units of the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:UNITs?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:UNITs?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:HARMONICS:UNITs value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:UNITs {LOG|LINear}
        - POWer:POWer<x>:HARMONICS:UNITs?
        ```
    """


class PowerPowerItemHarmonicsStartfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:STARTFREQUEncy`` command.

    Description:
        - This command sets or queries the value for the start frequency for the Harmonics
          measurement. in the range of 1 Hz to 1 GHz.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:STARTFREQUEncy?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:STARTFREQUEncy?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:STARTFREQUEncy value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:STARTFREQUEncy <NR2>
        - POWer:POWer<x>:HARMONICS:STARTFREQUEncy?
        ```

    Info:
        - ``POWer<x>`` is the Power measurement.
        - ``<NR2>`` sets the starting frequency, in hertz.
    """


class PowerPowerItemHarmonicsStandard(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:STANDard`` command.

    Description:
        - This command sets or queries the test mode for harmonics measurement of the specified
          power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:STANDard?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:STANDard?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:STANDard value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:STANDard {NONe|IEC|MIL|AM14|DO160|CUSTOM}
        - POWer:POWer<x>:HARMONICS:STANDard?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``NONe`` = No standard.
        - ``IEC`` = IEC 61000-3-2 standard.
        - ``MIL`` = MIL-STD-1399 standard.
        - ``AM14`` = AM14 standard.
        - ``DO160`` = DO160 standard.
        - ``CUSTOM`` = CUSTOM standard.
    """


class PowerPowerItemHarmonicsRcurrent(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:RCURRent`` command.

    Description:
        - This command sets or queries the rated current for the harmonics measurement of the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:RCURRent?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:RCURRent?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:RCURRent value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:RCURRent <NR1>
        - POWer:POWer<x>:HARMONICS:RCURRent?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR1>`` ranges from 0 to 100.
    """


class PowerPowerItemHarmonicsPowerrating(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:POWERRating`` command.

    Description:
        - This command sets or queries the power level for the harmonics measurement of the
          specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:POWERRating?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:POWERRating?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:POWERRating value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:POWERRating {HIGH|LOW}
        - POWer:POWer<x>:HARMONICS:POWERRating?
        ```
    """


class PowerPowerItemHarmonicsPfactor(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:PFACtor`` command.

    Description:
        - This command sets or queries the value of power factor for the harmonics measurement of
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:PFACtor?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:PFACtor?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:PFACtor value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:PFACtor <NR1>
        - POWer:POWer<x>:HARMONICS:PFACtor?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR1>`` ranges from 0 to 1.
    """


class PowerPowerItemHarmonicsOddeven(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:ODDEVen`` command.

    Description:
        - This command sets or queries the harmonics value analysis format of the specified power
          measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:ODDEVen?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:ODDEVen?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:ODDEVen value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:ODDEVen {ALL|ODD|EVEN}
        - POWer:POWer<x>:HARMONICS:ODDEVen?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``ALL`` to display all harmonics values.
        - ``ODD`` to display only the odd values of harmonics.
        - ``EVEN`` to display only the even values of harmonics.
    """


class PowerPowerItemHarmonicsLinefrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:LINEFREQUEncy`` command.

    Description:
        - This command sets or queries the value for the line frequency for the Harmonics
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:LINEFREQUEncy?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:LINEFREQUEncy?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:LINEFREQUEncy value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:LINEFREQUEncy {Auto|FIFTyhz|SIXTyhz |THREESIXTyhz|FOURHUNDREdhz|SIXFIFTyhz|EIGHTHUNDREdhz|CUSTom
        - POWer:POWer<x>:HARMONICS:LINEFREQUEncy?
        ```

    Info:
        - ``POWer<x>`` is the Power measurement identifier number.
        - ``Auto`` automatically detects and sets the line frequency value.
        - ``FIFTyhz`` sets the line frequency value to 50 Hz.
        - ``SIXTyhz`` sets the line frequency value to 60 Hz.
        - ``THREESIXTyhz`` sets the line frequency value to 360 Hz.
        - ``FOURHUNDREdhz`` sets the line frequency value to 400 Hz.
        - ``SIXFIFTyhz`` sets the line frequency value to 650 Hz.
        - ``EIGHTHUNDREdhz`` sets the line frequency value to 800 Hz.
        - ``CUSTom`` sets the line frequency value to Custom. The default value for custom is 100
          Hz. Use the ``POWER:POWERX:HARMONICS:LINEFREQUENCY`` command to set a custom line
          frequency value.
    """  # noqa: E501


class PowerPowerItemHarmonicsIsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:ISOURce`` command.

    Description:
        - This command sets or queries the current source for SOA measurement of the specified power
          measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:ISOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:ISOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:ISOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:ISOURce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:HARMONICS:ISOURce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemHarmonicsIpower(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:IPOWer`` command.

    Description:
        - This command sets or queries the input power value for the harmonics measurement of the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:IPOWer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:IPOWer?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:HARMONICS:IPOWer value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:IPOWer <NR1>
        - POWer:POWer<x>:HARMONICS:IPOWer?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR1>`` ranges from 0 to 600.
    """


class PowerPowerItemHarmonicsHsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:HSOURce`` command.

    Description:
        - This command sets or queries the source type for the harmonics measurement of the
          specified power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:HSOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:HSOURce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:HSOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:HSOURce {CURRent|VOLTage}
        - POWer:POWer<x>:HARMONICS:HSOURce?
        ```
    """


class PowerPowerItemHarmonicsHorder(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:HORDer`` command.

    Description:
        - This command sets or queries the order value for the harmonics measurement of the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:HORDer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:HORDer?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:HARMONICS:HORDer value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:HORDer <NR1>
        - POWer:POWer<x>:HARMONICS:HORDer?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR1>`` ranges from 40 to 100.
    """


class PowerPowerItemHarmonicsFundcurrent(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:FUNDCURRent`` command.

    Description:
        - This command sets or queries the fundamental current value for the harmonics measurement
          of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:FUNDCURRent?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:FUNDCURRent?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:FUNDCURRent value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:FUNDCURRent <NR1>
        - POWer:POWer<x>:HARMONICS:FUNDCURRent?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``<NR1>`` ranges from 0 to 16.
    """


class PowerPowerItemHarmonicsCmethod(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:CMEThod`` command.

    Description:
        - This command sets or queries the fundamental current method for the harmonics measurement
          of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:CMEThod?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:CMEThod?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:HARMONICS:CMEThod value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:CMEThod {RATed|MEASured}
        - POWer:POWer<x>:HARMONICS:CMEThod?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``RATed`` : select to use the standard input current values in the measurement.
        - ``MEASured`` : select to use the measured the input current values in the measurement.
    """


class PowerPowerItemHarmonicsClfile(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:CLFile`` command.

    Description:
        - This command sets or queries the custom limits file path for the harmonics measurement.
          The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:CLFile?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:CLFile?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:HARMONICS:CLFile value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:CLFile <QString>
        - POWer:POWer<x>:HARMONICS:CLFile?
        ```

    Info:
        - ``<QString>`` specifies the custom limits file path that can be loaded when the harmonics
          standard type selected is CUSTom.
    """

    _WRAP_ARG_WITH_QUOTES = True


class PowerPowerItemHarmonicsClass(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS:CLASs`` command.

    Description:
        - This command sets or queries the class type for the harmonics measurement in the specified
          power measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:CLASs?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:CLASs?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:HARMONICS:CLASs value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:HARMONICS:CLASs {CLASSA|CLASSB|CLASSC|CLASSD}
        - POWer:POWer<x>:HARMONICS:CLASs?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class PowerPowerItemHarmonics(SCPICmdRead):
    """The ``POWer:POWer<x>:HARMONICS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.class``: The ``POWer:POWer<x>:HARMONICS:CLASs`` command.
        - ``.clfile``: The ``POWer:POWer<x>:HARMONICS:CLFile`` command.
        - ``.cmethod``: The ``POWer:POWer<x>:HARMONICS:CMEThod`` command.
        - ``.fundcurrent``: The ``POWer:POWer<x>:HARMONICS:FUNDCURRent`` command.
        - ``.horder``: The ``POWer:POWer<x>:HARMONICS:HORDer`` command.
        - ``.hsource``: The ``POWer:POWer<x>:HARMONICS:HSOURce`` command.
        - ``.ipower``: The ``POWer:POWer<x>:HARMONICS:IPOWer`` command.
        - ``.isource``: The ``POWer:POWer<x>:HARMONICS:ISOURce`` command.
        - ``.linefrequency``: The ``POWer:POWer<x>:HARMONICS:LINEFREQUEncy`` command.
        - ``.oddeven``: The ``POWer:POWer<x>:HARMONICS:ODDEVen`` command.
        - ``.pfactor``: The ``POWer:POWer<x>:HARMONICS:PFACtor`` command.
        - ``.powerrating``: The ``POWer:POWer<x>:HARMONICS:POWERRating`` command.
        - ``.rcurrent``: The ``POWer:POWer<x>:HARMONICS:RCURRent`` command.
        - ``.standard``: The ``POWer:POWer<x>:HARMONICS:STANDard`` command.
        - ``.startfrequency``: The ``POWer:POWer<x>:HARMONICS:STARTFREQUEncy`` command.
        - ``.units``: The ``POWer:POWer<x>:HARMONICS:UNITs`` command.
        - ``.vsource``: The ``POWer:POWer<x>:HARMONICS:VSOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._class = PowerPowerItemHarmonicsClass(device, f"{self._cmd_syntax}:CLASs")
        self._clfile = PowerPowerItemHarmonicsClfile(device, f"{self._cmd_syntax}:CLFile")
        self._cmethod = PowerPowerItemHarmonicsCmethod(device, f"{self._cmd_syntax}:CMEThod")
        self._fundcurrent = PowerPowerItemHarmonicsFundcurrent(
            device, f"{self._cmd_syntax}:FUNDCURRent"
        )
        self._horder = PowerPowerItemHarmonicsHorder(device, f"{self._cmd_syntax}:HORDer")
        self._hsource = PowerPowerItemHarmonicsHsource(device, f"{self._cmd_syntax}:HSOURce")
        self._ipower = PowerPowerItemHarmonicsIpower(device, f"{self._cmd_syntax}:IPOWer")
        self._isource = PowerPowerItemHarmonicsIsource(device, f"{self._cmd_syntax}:ISOURce")
        self._linefrequency = PowerPowerItemHarmonicsLinefrequency(
            device, f"{self._cmd_syntax}:LINEFREQUEncy"
        )
        self._oddeven = PowerPowerItemHarmonicsOddeven(device, f"{self._cmd_syntax}:ODDEVen")
        self._pfactor = PowerPowerItemHarmonicsPfactor(device, f"{self._cmd_syntax}:PFACtor")
        self._powerrating = PowerPowerItemHarmonicsPowerrating(
            device, f"{self._cmd_syntax}:POWERRating"
        )
        self._rcurrent = PowerPowerItemHarmonicsRcurrent(device, f"{self._cmd_syntax}:RCURRent")
        self._standard = PowerPowerItemHarmonicsStandard(device, f"{self._cmd_syntax}:STANDard")
        self._startfrequency = PowerPowerItemHarmonicsStartfrequency(
            device, f"{self._cmd_syntax}:STARTFREQUEncy"
        )
        self._units = PowerPowerItemHarmonicsUnits(device, f"{self._cmd_syntax}:UNITs")
        self._vsource = PowerPowerItemHarmonicsVsource(device, f"{self._cmd_syntax}:VSOURce")

    @property
    def class_(self) -> PowerPowerItemHarmonicsClass:
        """Return the ``POWer:POWer<x>:HARMONICS:CLASs`` command.

        Description:
            - This command sets or queries the class type for the harmonics measurement in the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:CLASs?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:CLASs?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:CLASs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:CLASs {CLASSA|CLASSB|CLASSC|CLASSD}
            - POWer:POWer<x>:HARMONICS:CLASs?
            ```
        """
        return self._class

    @property
    def clfile(self) -> PowerPowerItemHarmonicsClfile:
        """Return the ``POWer:POWer<x>:HARMONICS:CLFile`` command.

        Description:
            - This command sets or queries the custom limits file path for the harmonics
              measurement. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:CLFile?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:CLFile?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:CLFile value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:CLFile <QString>
            - POWer:POWer<x>:HARMONICS:CLFile?
            ```

        Info:
            - ``<QString>`` specifies the custom limits file path that can be loaded when the
              harmonics standard type selected is CUSTom.
        """
        return self._clfile

    @property
    def cmethod(self) -> PowerPowerItemHarmonicsCmethod:
        """Return the ``POWer:POWer<x>:HARMONICS:CMEThod`` command.

        Description:
            - This command sets or queries the fundamental current method for the harmonics
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:CMEThod?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:CMEThod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:CMEThod value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:CMEThod {RATed|MEASured}
            - POWer:POWer<x>:HARMONICS:CMEThod?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``RATed`` : select to use the standard input current values in the measurement.
            - ``MEASured`` : select to use the measured the input current values in the measurement.
        """
        return self._cmethod

    @property
    def fundcurrent(self) -> PowerPowerItemHarmonicsFundcurrent:
        """Return the ``POWer:POWer<x>:HARMONICS:FUNDCURRent`` command.

        Description:
            - This command sets or queries the fundamental current value for the harmonics
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:FUNDCURRent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:FUNDCURRent?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:FUNDCURRent value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:FUNDCURRent <NR1>
            - POWer:POWer<x>:HARMONICS:FUNDCURRent?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR1>`` ranges from 0 to 16.
        """
        return self._fundcurrent

    @property
    def horder(self) -> PowerPowerItemHarmonicsHorder:
        """Return the ``POWer:POWer<x>:HARMONICS:HORDer`` command.

        Description:
            - This command sets or queries the order value for the harmonics measurement of the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:HORDer?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:HORDer?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:HORDer value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:HORDer <NR1>
            - POWer:POWer<x>:HARMONICS:HORDer?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR1>`` ranges from 40 to 100.
        """
        return self._horder

    @property
    def hsource(self) -> PowerPowerItemHarmonicsHsource:
        """Return the ``POWer:POWer<x>:HARMONICS:HSOURce`` command.

        Description:
            - This command sets or queries the source type for the harmonics measurement of the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:HSOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:HSOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:HSOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:HSOURce {CURRent|VOLTage}
            - POWer:POWer<x>:HARMONICS:HSOURce?
            ```
        """
        return self._hsource

    @property
    def ipower(self) -> PowerPowerItemHarmonicsIpower:
        """Return the ``POWer:POWer<x>:HARMONICS:IPOWer`` command.

        Description:
            - This command sets or queries the input power value for the harmonics measurement of
              the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:IPOWer?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:IPOWer?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:IPOWer value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:IPOWer <NR1>
            - POWer:POWer<x>:HARMONICS:IPOWer?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR1>`` ranges from 0 to 600.
        """
        return self._ipower

    @property
    def isource(self) -> PowerPowerItemHarmonicsIsource:
        """Return the ``POWer:POWer<x>:HARMONICS:ISOURce`` command.

        Description:
            - This command sets or queries the current source for SOA measurement of the specified
              power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:ISOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:ISOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:ISOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:ISOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:HARMONICS:ISOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._isource

    @property
    def linefrequency(self) -> PowerPowerItemHarmonicsLinefrequency:
        """Return the ``POWer:POWer<x>:HARMONICS:LINEFREQUEncy`` command.

        Description:
            - This command sets or queries the value for the line frequency for the Harmonics
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:HARMONICS:LINEFREQUEncy?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:LINEFREQUEncy?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:LINEFREQUEncy value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:LINEFREQUEncy {Auto|FIFTyhz|SIXTyhz |THREESIXTyhz|FOURHUNDREdhz|SIXFIFTyhz|EIGHTHUNDREdhz|CUSTom
            - POWer:POWer<x>:HARMONICS:LINEFREQUEncy?
            ```

        Info:
            - ``POWer<x>`` is the Power measurement identifier number.
            - ``Auto`` automatically detects and sets the line frequency value.
            - ``FIFTyhz`` sets the line frequency value to 50 Hz.
            - ``SIXTyhz`` sets the line frequency value to 60 Hz.
            - ``THREESIXTyhz`` sets the line frequency value to 360 Hz.
            - ``FOURHUNDREdhz`` sets the line frequency value to 400 Hz.
            - ``SIXFIFTyhz`` sets the line frequency value to 650 Hz.
            - ``EIGHTHUNDREdhz`` sets the line frequency value to 800 Hz.
            - ``CUSTom`` sets the line frequency value to Custom. The default value for custom is
              100 Hz. Use the ``POWER:POWERX:HARMONICS:LINEFREQUENCY`` command to set a custom line
              frequency value.
        """  # noqa: E501
        return self._linefrequency

    @property
    def oddeven(self) -> PowerPowerItemHarmonicsOddeven:
        """Return the ``POWer:POWer<x>:HARMONICS:ODDEVen`` command.

        Description:
            - This command sets or queries the harmonics value analysis format of the specified
              power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:ODDEVen?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:ODDEVen?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:ODDEVen value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:ODDEVen {ALL|ODD|EVEN}
            - POWer:POWer<x>:HARMONICS:ODDEVen?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``ALL`` to display all harmonics values.
            - ``ODD`` to display only the odd values of harmonics.
            - ``EVEN`` to display only the even values of harmonics.
        """
        return self._oddeven

    @property
    def pfactor(self) -> PowerPowerItemHarmonicsPfactor:
        """Return the ``POWer:POWer<x>:HARMONICS:PFACtor`` command.

        Description:
            - This command sets or queries the value of power factor for the harmonics measurement
              of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:PFACtor?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:PFACtor?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:PFACtor value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:PFACtor <NR1>
            - POWer:POWer<x>:HARMONICS:PFACtor?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR1>`` ranges from 0 to 1.
        """
        return self._pfactor

    @property
    def powerrating(self) -> PowerPowerItemHarmonicsPowerrating:
        """Return the ``POWer:POWer<x>:HARMONICS:POWERRating`` command.

        Description:
            - This command sets or queries the power level for the harmonics measurement of the
              specified power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:POWERRating?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:POWERRating?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:POWERRating value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:POWERRating {HIGH|LOW}
            - POWer:POWer<x>:HARMONICS:POWERRating?
            ```
        """
        return self._powerrating

    @property
    def rcurrent(self) -> PowerPowerItemHarmonicsRcurrent:
        """Return the ``POWer:POWer<x>:HARMONICS:RCURRent`` command.

        Description:
            - This command sets or queries the rated current for the harmonics measurement of the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:RCURRent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:RCURRent?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:RCURRent value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:RCURRent <NR1>
            - POWer:POWer<x>:HARMONICS:RCURRent?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``<NR1>`` ranges from 0 to 100.
        """
        return self._rcurrent

    @property
    def standard(self) -> PowerPowerItemHarmonicsStandard:
        """Return the ``POWer:POWer<x>:HARMONICS:STANDard`` command.

        Description:
            - This command sets or queries the test mode for harmonics measurement of the specified
              power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:STANDard?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:STANDard?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:STANDard value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:STANDard {NONe|IEC|MIL|AM14|DO160|CUSTOM}
            - POWer:POWer<x>:HARMONICS:STANDard?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``NONe`` = No standard.
            - ``IEC`` = IEC 61000-3-2 standard.
            - ``MIL`` = MIL-STD-1399 standard.
            - ``AM14`` = AM14 standard.
            - ``DO160`` = DO160 standard.
            - ``CUSTOM`` = CUSTOM standard.
        """
        return self._standard

    @property
    def startfrequency(self) -> PowerPowerItemHarmonicsStartfrequency:
        """Return the ``POWer:POWer<x>:HARMONICS:STARTFREQUEncy`` command.

        Description:
            - This command sets or queries the value for the start frequency for the Harmonics
              measurement. in the range of 1 Hz to 1 GHz.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:HARMONICS:STARTFREQUEncy?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:STARTFREQUEncy?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:STARTFREQUEncy value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:STARTFREQUEncy <NR2>
            - POWer:POWer<x>:HARMONICS:STARTFREQUEncy?
            ```

        Info:
            - ``POWer<x>`` is the Power measurement.
            - ``<NR2>`` sets the starting frequency, in hertz.
        """
        return self._startfrequency

    @property
    def units(self) -> PowerPowerItemHarmonicsUnits:
        """Return the ``POWer:POWer<x>:HARMONICS:UNITs`` command.

        Description:
            - This command sets or queries the harmonics results units of the specified power
              measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:UNITs?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS:UNITs?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:UNITs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:UNITs {LOG|LINear}
            - POWer:POWer<x>:HARMONICS:UNITs?
            ```
        """
        return self._units

    @property
    def vsource(self) -> PowerPowerItemHarmonicsVsource:
        """Return the ``POWer:POWer<x>:HARMONICS:VSOURce`` command.

        Description:
            - This command sets or queries the voltage source for SOA measurement of the specified
              power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS:VSOURce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:VSOURce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:HARMONICS:VSOURce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:HARMONICS:VSOURce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:HARMONICS:VSOURce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vsource


class PowerPowerItemGatingGlobal(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:GATing:GLOBal`` command.

    Description:
        - This command sets or queries the gating settings for the specified power measurement
          number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:GATing:GLOBal?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:GATing:GLOBal?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:GATing:GLOBal value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:GATing:GLOBal {ON|OFF|1|0}
        - POWer:POWer<x>:GATing:GLOBal?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``1`` selects the gating settings as Global.
        - ``ON`` selects the gating settings as Global.
        - ``0`` selects the gating settings as Local.
        - ``OFF`` selects the gating settings as Local.
    """


class PowerPowerItemGating(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:GATing`` command.

    Description:
        - This command sets or queries the gating type for the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:GATing?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:GATing?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:GATing value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:GATing {NONE|CURSOR|SCREEN|LOGIC}
        - POWer:POWer<x>:GATing?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``NONE`` makes measurement across the entire waveform record.
        - ``CURSOR`` makes measurements on that portion of the waveform between the cursors.
          Selecting Cursors opens cursors on the measurement source. Set the cursors so that the
          waveform area of interest is in between the cursors.
        - ``SCREEN`` takes measurements on that portion of the waveform shown in the display. When
          Zoom is on, the display is the zoom window.
        - ``LOGIC`` takes measurements only when the logical state of a specified waveform is true.

    Properties:
        - ``.global``: The ``POWer:POWer<x>:GATing:GLOBal`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._global = PowerPowerItemGatingGlobal(device, f"{self._cmd_syntax}:GLOBal")

    @property
    def global_(self) -> PowerPowerItemGatingGlobal:
        """Return the ``POWer:POWer<x>:GATing:GLOBal`` command.

        Description:
            - This command sets or queries the gating settings for the specified power measurement
              number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:GATing:GLOBal?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:GATing:GLOBal?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:GATing:GLOBal value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:GATing:GLOBal {ON|OFF|1|0}
            - POWer:POWer<x>:GATing:GLOBal?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``1`` selects the gating settings as Global.
            - ``ON`` selects the gating settings as Global.
            - ``0`` selects the gating settings as Local.
            - ``OFF`` selects the gating settings as Local.
        """
        return self._global


class PowerPowerItemFrequencyInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:FREQUENCY:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for frequency measurement of the specified
          power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:FREQUENCY:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:FREQUENCY:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:FREQUENCY:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:FREQUENCY:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:FREQUENCY:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemFrequencyEdge(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:FREQUENCY:EDGe`` command.

    Description:
        - This command sets or queries the edge type for frequency measurement of the specified
          power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:FREQUENCY:EDGe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:FREQUENCY:EDGe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:FREQUENCY:EDGe value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:FREQUENCY:EDGe {RISE|FALL}
        - POWer:POWer<x>:FREQUENCY:EDGe?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the power measurement badge on the UI.
    """


class PowerPowerItemFrequency(SCPICmdRead):
    """The ``POWer:POWer<x>:FREQUENCY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:FREQUENCY?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:FREQUENCY?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``POWer:POWer<x>:FREQUENCY:EDGe`` command.
        - ``.inputsource``: The ``POWer:POWer<x>:FREQUENCY:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = PowerPowerItemFrequencyEdge(device, f"{self._cmd_syntax}:EDGe")
        self._inputsource = PowerPowerItemFrequencyInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def edge(self) -> PowerPowerItemFrequencyEdge:
        """Return the ``POWer:POWer<x>:FREQUENCY:EDGe`` command.

        Description:
            - This command sets or queries the edge type for frequency measurement of the specified
              power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:FREQUENCY:EDGe?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:FREQUENCY:EDGe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:FREQUENCY:EDGe value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:FREQUENCY:EDGe {RISE|FALL}
            - POWer:POWer<x>:FREQUENCY:EDGe?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the power measurement badge on the UI.
        """
        return self._edge

    @property
    def inputsource(self) -> PowerPowerItemFrequencyInputsource:
        """Return the ``POWer:POWer<x>:FREQUENCY:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for frequency measurement of the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:FREQUENCY:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:FREQUENCY:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:FREQUENCY:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:FREQUENCY:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:FREQUENCY:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemEfficiencyVsource(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:VSOUrce`` command.

    Description:
        - This command sets or queries the voltage source for the power Efficiency measurement of
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:VSOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:EFFICIENCY:VSOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:EFFICIENCY:VSOUrce`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:VSOUrce
        - POWer:POWer<x>:EFFICIENCY:VSOUrce?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemEfficiencyVout3source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce`` command.

    Description:
        - This command sets or queries the output 3 voltage source for the power Efficiency
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown on the power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemEfficiencyVout2source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce`` command.

    Description:
        - This command sets or queries the output 2 voltage source for the power Efficiency
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemEfficiencyVout1source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce`` command.

    Description:
        - This command sets or queries the output 1 voltage source for the power Efficiency
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemEfficiencyOutputtype(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:OUTPUTType`` command.

    Description:
        - This command sets or queries the output type (AC or DC) for power Efficiency measurement
          of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:OUTPUTType?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:OUTPUTType?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:OUTPUTType value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:OUTPUTType {AC|DC}
        - POWer:POWer<x>:EFFICIENCY:OUTPUTType?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown on the power measurement badge of the UI.
        - ``AC`` sets the output voltage type to AC.
        - ``DC`` sets the output voltage type to DC.
    """


class PowerPowerItemEfficiencyOutput3type(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type`` command.

    Description:
        - ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type This`` command sets or queries the Output3 type
          (AC or DC) for the power Efficiency measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:OUTPUT3Type {AC|DC}
        - POWer:POWer<x>:EFFICIENCY:OUTPUT3Type?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown on the power measurement badge of the UI.
        - ``AC`` sets the Output3 voltage type to AC.
        - ``DC`` sets the Output3 voltage type to DC.
    """


class PowerPowerItemEfficiencyOutput2type(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type`` command.

    Description:
        - ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type This`` command sets or queries the Output2 type
          (AC or DC) for the power Efficiency measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:OUTPUT2Type {AC|DC}
        - POWer:POWer<x>:EFFICIENCY:OUTPUT2Type?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown on the power measurement badge of the UI.
        - ``AC`` sets the Output2 voltage type to AC.
        - ``DC`` sets the Output2 voltage type to DC.
    """


class PowerPowerItemEfficiencyOutput1type(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type`` command.

    Description:
        - ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type This`` command sets or queries the Output1 type
          (AC or DC) for the power Efficiency measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:OUTPUT1Type {AC|DC}
        - POWer:POWer<x>:EFFICIENCY:OUTPUT1Type?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown on the power measurement badge of the UI.
        - ``AC`` sets the output1 voltage type to AC.
        - ``DC`` sets the output1 voltage type to DC.
    """


class PowerPowerItemEfficiencyNumofoutputs(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:NUMOFOutputs`` command.

    Description:
        - This command sets or queries the number of outputs for the power Efficiency measurement of
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:NUMOFOutputs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:NUMOFOutputs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:NUMOFOutputs value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:NUMOFOutputs {ONE|TWO|THREE}
        - POWer:POWer<x>:EFFICIENCY:NUMOFOutputs?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``ONE`` , TWO, THREE sets the number of outputs to test in the power efficiency
          measurement.
    """


class PowerPowerItemEfficiencyIsource(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:ISOUrce`` command.

    Description:
        - This command sets or queries the current source for the power Efficiency measurement of
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:ISOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:EFFICIENCY:ISOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``POWer:POWer<x>:EFFICIENCY:ISOUrce`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:ISOUrce
        - POWer:POWer<x>:EFFICIENCY:ISOUrce?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemEfficiencyIout3source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce`` command.

    Description:
        - This command sets or queries the output 3 current source for the power Efficiency
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown on the power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemEfficiencyIout2source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce`` command.

    Description:
        - This command sets or queries the output 2 current source for the power Efficiency
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemEfficiencyIout1source(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce`` command.

    Description:
        - This command sets or queries the output 1 current source for the power Efficiency
          measurement of the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown in the power measurement badge on the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemEfficiencyInputtype(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY:INPUTType`` command.

    Description:
        - This command sets or queries the input type (AC or DC) for power Efficiency measurement of
          the specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:INPUTType?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:EFFICIENCY:INPUTType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:EFFICIENCY:INPUTType value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:EFFICIENCY:INPUTType {AC|DC}
        - POWer:POWer<x>:EFFICIENCY:INPUTType?
        ```

    Info:
        - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent of
          the number shown on the power measurement badge of the UI.
        - ``AC`` sets the input voltage type to AC.
        - ``DC`` sets the input voltage type to DC.
    """


#  pylint: disable=too-many-instance-attributes
class PowerPowerItemEfficiency(SCPICmdRead):
    """The ``POWer:POWer<x>:EFFICIENCY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:EFFICIENCY?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputtype``: The ``POWer:POWer<x>:EFFICIENCY:INPUTType`` command.
        - ``.iout1source``: The ``POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce`` command.
        - ``.iout2source``: The ``POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce`` command.
        - ``.iout3source``: The ``POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce`` command.
        - ``.isource``: The ``POWer:POWer<x>:EFFICIENCY:ISOUrce`` command.
        - ``.numofoutputs``: The ``POWer:POWer<x>:EFFICIENCY:NUMOFOutputs`` command.
        - ``.output1type``: The ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type`` command.
        - ``.output2type``: The ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type`` command.
        - ``.output3type``: The ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type`` command.
        - ``.outputtype``: The ``POWer:POWer<x>:EFFICIENCY:OUTPUTType`` command.
        - ``.vout1source``: The ``POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce`` command.
        - ``.vout2source``: The ``POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce`` command.
        - ``.vout3source``: The ``POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce`` command.
        - ``.vsource``: The ``POWer:POWer<x>:EFFICIENCY:VSOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputtype = PowerPowerItemEfficiencyInputtype(device, f"{self._cmd_syntax}:INPUTType")
        self._iout1source = PowerPowerItemEfficiencyIout1source(
            device, f"{self._cmd_syntax}:IOUT1SOUrce"
        )
        self._iout2source = PowerPowerItemEfficiencyIout2source(
            device, f"{self._cmd_syntax}:IOUT2SOUrce"
        )
        self._iout3source = PowerPowerItemEfficiencyIout3source(
            device, f"{self._cmd_syntax}:IOUT3SOUrce"
        )
        self._isource = PowerPowerItemEfficiencyIsource(device, f"{self._cmd_syntax}:ISOUrce")
        self._numofoutputs = PowerPowerItemEfficiencyNumofoutputs(
            device, f"{self._cmd_syntax}:NUMOFOutputs"
        )
        self._output1type = PowerPowerItemEfficiencyOutput1type(
            device, f"{self._cmd_syntax}:OUTPUT1Type"
        )
        self._output2type = PowerPowerItemEfficiencyOutput2type(
            device, f"{self._cmd_syntax}:OUTPUT2Type"
        )
        self._output3type = PowerPowerItemEfficiencyOutput3type(
            device, f"{self._cmd_syntax}:OUTPUT3Type"
        )
        self._outputtype = PowerPowerItemEfficiencyOutputtype(
            device, f"{self._cmd_syntax}:OUTPUTType"
        )
        self._vout1source = PowerPowerItemEfficiencyVout1source(
            device, f"{self._cmd_syntax}:VOUT1SOUrce"
        )
        self._vout2source = PowerPowerItemEfficiencyVout2source(
            device, f"{self._cmd_syntax}:VOUT2SOUrce"
        )
        self._vout3source = PowerPowerItemEfficiencyVout3source(
            device, f"{self._cmd_syntax}:VOUT3SOUrce"
        )
        self._vsource = PowerPowerItemEfficiencyVsource(device, f"{self._cmd_syntax}:VSOUrce")

    @property
    def inputtype(self) -> PowerPowerItemEfficiencyInputtype:
        """Return the ``POWer:POWer<x>:EFFICIENCY:INPUTType`` command.

        Description:
            - This command sets or queries the input type (AC or DC) for power Efficiency
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:INPUTType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:INPUTType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:INPUTType value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:INPUTType {AC|DC}
            - POWer:POWer<x>:EFFICIENCY:INPUTType?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown on the power measurement badge of the UI.
            - ``AC`` sets the input voltage type to AC.
            - ``DC`` sets the input voltage type to DC.
        """
        return self._inputtype

    @property
    def iout1source(self) -> PowerPowerItemEfficiencyIout1source:
        """Return the ``POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce`` command.

        Description:
            - This command sets or queries the output 1 current source for the power Efficiency
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._iout1source

    @property
    def iout2source(self) -> PowerPowerItemEfficiencyIout2source:
        """Return the ``POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce`` command.

        Description:
            - This command sets or queries the output 2 current source for the power Efficiency
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._iout2source

    @property
    def iout3source(self) -> PowerPowerItemEfficiencyIout3source:
        """Return the ``POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce`` command.

        Description:
            - This command sets or queries the output 3 current source for the power Efficiency
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown on the power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._iout3source

    @property
    def isource(self) -> PowerPowerItemEfficiencyIsource:
        """Return the ``POWer:POWer<x>:EFFICIENCY:ISOUrce`` command.

        Description:
            - This command sets or queries the current source for the power Efficiency measurement
              of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:ISOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:ISOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``POWer:POWer<x>:EFFICIENCY:ISOUrce``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:ISOUrce
            - POWer:POWer<x>:EFFICIENCY:ISOUrce?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._isource

    @property
    def numofoutputs(self) -> PowerPowerItemEfficiencyNumofoutputs:
        """Return the ``POWer:POWer<x>:EFFICIENCY:NUMOFOutputs`` command.

        Description:
            - This command sets or queries the number of outputs for the power Efficiency
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:NUMOFOutputs?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:NUMOFOutputs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:NUMOFOutputs value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:NUMOFOutputs {ONE|TWO|THREE}
            - POWer:POWer<x>:EFFICIENCY:NUMOFOutputs?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``ONE`` , TWO, THREE sets the number of outputs to test in the power efficiency
              measurement.
        """
        return self._numofoutputs

    @property
    def output1type(self) -> PowerPowerItemEfficiencyOutput1type:
        """Return the ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type`` command.

        Description:
            - ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type This`` command sets or queries the Output1
              type (AC or DC) for the power Efficiency measurement of the specified power
              measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:OUTPUT1Type {AC|DC}
            - POWer:POWer<x>:EFFICIENCY:OUTPUT1Type?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown on the power measurement badge of the UI.
            - ``AC`` sets the output1 voltage type to AC.
            - ``DC`` sets the output1 voltage type to DC.
        """
        return self._output1type

    @property
    def output2type(self) -> PowerPowerItemEfficiencyOutput2type:
        """Return the ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type`` command.

        Description:
            - ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type This`` command sets or queries the Output2
              type (AC or DC) for the power Efficiency measurement of the specified power
              measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:OUTPUT2Type {AC|DC}
            - POWer:POWer<x>:EFFICIENCY:OUTPUT2Type?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown on the power measurement badge of the UI.
            - ``AC`` sets the Output2 voltage type to AC.
            - ``DC`` sets the Output2 voltage type to DC.
        """
        return self._output2type

    @property
    def output3type(self) -> PowerPowerItemEfficiencyOutput3type:
        """Return the ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type`` command.

        Description:
            - ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type This`` command sets or queries the Output3
              type (AC or DC) for the power Efficiency measurement of the specified power
              measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:OUTPUT3Type {AC|DC}
            - POWer:POWer<x>:EFFICIENCY:OUTPUT3Type?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown on the power measurement badge of the UI.
            - ``AC`` sets the Output3 voltage type to AC.
            - ``DC`` sets the Output3 voltage type to DC.
        """
        return self._output3type

    @property
    def outputtype(self) -> PowerPowerItemEfficiencyOutputtype:
        """Return the ``POWer:POWer<x>:EFFICIENCY:OUTPUTType`` command.

        Description:
            - This command sets or queries the output type (AC or DC) for power Efficiency
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:OUTPUTType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:OUTPUTType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:OUTPUTType value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:OUTPUTType {AC|DC}
            - POWer:POWer<x>:EFFICIENCY:OUTPUTType?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown on the power measurement badge of the UI.
            - ``AC`` sets the output voltage type to AC.
            - ``DC`` sets the output voltage type to DC.
        """
        return self._outputtype

    @property
    def vout1source(self) -> PowerPowerItemEfficiencyVout1source:
        """Return the ``POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce`` command.

        Description:
            - This command sets or queries the output 1 voltage source for the power Efficiency
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vout1source

    @property
    def vout2source(self) -> PowerPowerItemEfficiencyVout2source:
        """Return the ``POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce`` command.

        Description:
            - This command sets or queries the output 2 voltage source for the power Efficiency
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vout2source

    @property
    def vout3source(self) -> PowerPowerItemEfficiencyVout3source:
        """Return the ``POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce`` command.

        Description:
            - This command sets or queries the output 3 voltage source for the power Efficiency
              measurement of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown on the power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vout3source

    @property
    def vsource(self) -> PowerPowerItemEfficiencyVsource:
        """Return the ``POWer:POWer<x>:EFFICIENCY:VSOUrce`` command.

        Description:
            - This command sets or queries the voltage source for the power Efficiency measurement
              of the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY:VSOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:EFFICIENCY:VSOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``POWer:POWer<x>:EFFICIENCY:VSOUrce``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:EFFICIENCY:VSOUrce
            - POWer:POWer<x>:EFFICIENCY:VSOUrce?
            ```

        Info:
            - ``Power<x>`` is the number of a power efficiency measurement. This is the equivalent
              of the number shown in the power measurement badge on the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._vsource


class PowerPowerItemDvdtSourceedgetype(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:DVDT:SOURCEEDGEType`` command.

    Description:
        - This command sets or queries the edge type for dv/dt measurement in the specified power
          measurement number. The power measurement number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:DVDT:SOURCEEDGEType?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:DVDT:SOURCEEDGEType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:DVDT:SOURCEEDGEType value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:DVDT:SOURCEEDGEType {RISE|FALL}
        - POWer:POWer<x>:DVDT:SOURCEEDGEType?
        ```
    """


class PowerPowerItemDvdtInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:DVDT:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for dv/dt measurement of the specified power
          measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:DVDT:INPUTSOurce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:DVDT:INPUTSOurce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:DVDT:INPUTSOurce value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:DVDT:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:DVDT:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemDvdt(SCPICmdRead):
    """The ``POWer:POWer<x>:DVDT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:DVDT?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:DVDT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:DVDT:INPUTSOurce`` command.
        - ``.sourceedgetype``: The ``POWer:POWer<x>:DVDT:SOURCEEDGEType`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemDvdtInputsource(device, f"{self._cmd_syntax}:INPUTSOurce")
        self._sourceedgetype = PowerPowerItemDvdtSourceedgetype(
            device, f"{self._cmd_syntax}:SOURCEEDGEType"
        )

    @property
    def inputsource(self) -> PowerPowerItemDvdtInputsource:
        """Return the ``POWer:POWer<x>:DVDT:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for dv/dt measurement of the specified
              power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:DVDT:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:DVDT:INPUTSOurce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:DVDT:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:DVDT:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:DVDT:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource

    @property
    def sourceedgetype(self) -> PowerPowerItemDvdtSourceedgetype:
        """Return the ``POWer:POWer<x>:DVDT:SOURCEEDGEType`` command.

        Description:
            - This command sets or queries the edge type for dv/dt measurement in the specified
              power measurement number. The power measurement number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:DVDT:SOURCEEDGEType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:DVDT:SOURCEEDGEType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:DVDT:SOURCEEDGEType value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:DVDT:SOURCEEDGEType {RISE|FALL}
            - POWer:POWer<x>:DVDT:SOURCEEDGEType?
            ```
        """
        return self._sourceedgetype


class PowerPowerItemDidtSourceedgetype(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:DIDT:SOURCEEDGEType`` command.

    Description:
        - This command sets or queries the edge type for di/dt measurement of the specified power
          measurement number. <x> specifies the number of the power measurement badge.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:DIDT:SOURCEEDGEType?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:DIDT:SOURCEEDGEType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:DIDT:SOURCEEDGEType value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:DIDT:SOURCEEDGEType {RISE|FALL}
        - POWer:POWer<x>:DIDT:SOURCEEDGEType?
        ```
    """


class PowerPowerItemDidtInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:DIDT:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for di/dt measurement in the specified power
          measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:DIDT:INPUTSOurce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:DIDT:INPUTSOurce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:DIDT:INPUTSOurce value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:DIDT:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:DIDT:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemDidt(SCPICmdRead):
    """The ``POWer:POWer<x>:DIDT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:DIDT?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:DIDT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:DIDT:INPUTSOurce`` command.
        - ``.sourceedgetype``: The ``POWer:POWer<x>:DIDT:SOURCEEDGEType`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemDidtInputsource(device, f"{self._cmd_syntax}:INPUTSOurce")
        self._sourceedgetype = PowerPowerItemDidtSourceedgetype(
            device, f"{self._cmd_syntax}:SOURCEEDGEType"
        )

    @property
    def inputsource(self) -> PowerPowerItemDidtInputsource:
        """Return the ``POWer:POWer<x>:DIDT:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for di/dt measurement in the specified
              power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:DIDT:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:DIDT:INPUTSOurce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:DIDT:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:DIDT:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:DIDT:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource

    @property
    def sourceedgetype(self) -> PowerPowerItemDidtSourceedgetype:
        """Return the ``POWer:POWer<x>:DIDT:SOURCEEDGEType`` command.

        Description:
            - This command sets or queries the edge type for di/dt measurement of the specified
              power measurement number. <x> specifies the number of the power measurement badge.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:DIDT:SOURCEEDGEType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:DIDT:SOURCEEDGEType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:DIDT:SOURCEEDGEType value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:DIDT:SOURCEEDGEType {RISE|FALL}
            - POWer:POWer<x>:DIDT:SOURCEEDGEType?
            ```
        """
        return self._sourceedgetype


class PowerPowerItemCycletopInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLETop:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for cycle top measurement in the specified
          power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLETop:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLETop:INPUTSOurce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CYCLETop:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CYCLETop:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:CYCLETop:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemCycletop(SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLETop`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLETop?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLETop?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:CYCLETop:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemCycletopInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def inputsource(self) -> PowerPowerItemCycletopInputsource:
        """Return the ``POWer:POWer<x>:CYCLETop:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for cycle top measurement in the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLETop:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CYCLETop:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CYCLETop:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CYCLETop:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:CYCLETop:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemCyclepkpkInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLEPKPK:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for cycle peak-to-peak measurement in the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEPKPK:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CYCLEPKPK:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CYCLEPKPK:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CYCLEPKPK:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:CYCLEPKPK:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemCyclepkpk(SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLEPKPK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEPKPK?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEPKPK?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:CYCLEPKPK:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemCyclepkpkInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def inputsource(self) -> PowerPowerItemCyclepkpkInputsource:
        """Return the ``POWer:POWer<x>:CYCLEPKPK:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for cycle peak-to-peak measurement in
              the specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEPKPK:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CYCLEPKPK:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CYCLEPKPK:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CYCLEPKPK:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:CYCLEPKPK:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemCycleminInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLEMin:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for cycle minimum measurement in the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEMin:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEMin:INPUTSOurce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CYCLEMin:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CYCLEMin:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:CYCLEMin:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemCyclemin(SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLEMin`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEMin?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEMin?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:CYCLEMin:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemCycleminInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def inputsource(self) -> PowerPowerItemCycleminInputsource:
        """Return the ``POWer:POWer<x>:CYCLEMin:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for cycle minimum measurement in the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEMin:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CYCLEMin:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CYCLEMin:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CYCLEMin:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:CYCLEMin:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemCyclemaxInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLEMAX:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for cycle maximum measurement in the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEMAX:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEMAX:INPUTSOurce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CYCLEMAX:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CYCLEMAX:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:CYCLEMAX:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemCyclemax(SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLEMAX`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEMAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEMAX?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:CYCLEMAX:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemCyclemaxInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def inputsource(self) -> PowerPowerItemCyclemaxInputsource:
        """Return the ``POWer:POWer<x>:CYCLEMAX:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for cycle maximum measurement in the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEMAX:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CYCLEMAX:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CYCLEMAX:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CYCLEMAX:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:CYCLEMAX:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemCyclebaseInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLEBase:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for cycle base measurement of the specified
          power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEBase:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CYCLEBase:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CYCLEBase:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CYCLEBase:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:CYCLEBase:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemCyclebase(SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLEBase`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEBase?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEBase?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:CYCLEBase:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemCyclebaseInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def inputsource(self) -> PowerPowerItemCyclebaseInputsource:
        """Return the ``POWer:POWer<x>:CYCLEBase:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for cycle base measurement of the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEBase:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CYCLEBase:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CYCLEBase:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CYCLEBase:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:CYCLEBase:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemCycleampInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLEAmp:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for cycle amplitude measurement of the
          specified power measurement number.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEAmp:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEAmp:INPUTSOurce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CYCLEAmp:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CYCLEAmp:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
        - POWer:POWer<x>:CYCLEAmp:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
        - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
          FlexChannels in your instrument.
        - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
        - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
    """


class PowerPowerItemCycleamp(SCPICmdRead):
    """The ``POWer:POWer<x>:CYCLEAmp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEAmp?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEAmp?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.inputsource``: The ``POWer:POWer<x>:CYCLEAmp:INPUTSOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputsource = PowerPowerItemCycleampInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )

    @property
    def inputsource(self) -> PowerPowerItemCycleampInputsource:
        """Return the ``POWer:POWer<x>:CYCLEAmp:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for cycle amplitude measurement of the
              specified power measurement number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEAmp:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CYCLEAmp:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CYCLEAmp:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CYCLEAmp:INPUTSOurce {CH<x>|MATH<x>|REF<x>}
            - POWer:POWer<x>:CYCLEAmp:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``CH<x>`` = A channel specifier; <x> is 1 through 8 and is limited by the number of
              FlexChannels in your instrument.
            - ``MATH<x>`` = A math waveform specifier; <x> is ≥1.
            - ``REF<x>`` = A reference waveform specifier; <x> is ≥1.
        """
        return self._inputsource


class PowerPowerItemClresponseTestconnection(SCPICmdWrite):
    """The ``POWer:POWer<x>:CLRESPONSE:TESTCONNection`` command.

    Description:
        - This command tests the connection to the external generator used with the specified
          Control Loop Response power measurement.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:TESTCONNection value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:TESTCONNection EXECute
        ```

    Info:
        - ``POWer<x>`` is the number of the PSRR power measurement.
        - ``EXECute`` runs the test connection function.
    """


class PowerPowerItemClresponseStopfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency`` command.

    Description:
        - This command sets or queries the stop frequency value for the Control Loop Response power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:STOPFREQuency <NR3>
        - POWer:POWer<x>:CLRESPONSE:STOPFREQuency?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the stop frequency for the measurement, in the range of 10 Hz to 50 MHz.
    """


class PowerPowerItemClresponseStartfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency`` command.

    Description:
        - This command sets or queries the start frequency value for the Control Loop Response power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:STARTFREQuency <NR3>
        - POWer:POWer<x>:CLRESPONSE:STARTFREQuency?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the starting frequency for the measurement, in the range of 10 Hz to 50 MHz.
    """


class PowerPowerItemClresponsePpd(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:PPD`` command.

    Description:
        - This command sets or queries the points per decade (PPD) value for the Control Loop
          Response power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:PPD?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:PPD?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:PPD value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:PPD <NR3>
        - POWer:POWer<x>:CLRESPONSE:PPD?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the PPD value for the measurement, in the range of 10 to 100 points.
    """


class PowerPowerItemClresponseOutputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce`` command.

    Description:
        - This command sets or queries the output source for the Control Loop Response power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce CH<x>
        - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` sets the channel to use for the output signal source.
    """


class PowerPowerItemClresponseMon(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:MON`` command.

    Description:
        - This command sets or returns the measure on for the control loop response, PSRR or
          impedance measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:MON?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:MON?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:MON value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:MON {SAVG|SSEQ}
        - POWer:POWer<x>:CLRESPONSE:MON?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``SAVG`` specifies the measure analysis method for the Control Loop Response/PSRR or
          Impedance measurement to SAVG.
        - ``SSEQ`` specifies the measure analysis method for the Control Loop Response/PSRR or
          Impedance measurement to SSEQ.
    """


class PowerPowerItemClresponseInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for the Control Loop Response power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:INPUTSOurce CH<x>
        - POWer:POWer<x>:CLRESPONSE:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` sets the channel to use for the output signal source.
    """


class PowerPowerItemClresponseImpedance(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:IMPEDance`` command.

    Description:
        - This command sets or queries the vertical termination impedance for the Control Loop
          Response power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:IMPEDance?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:IMPEDance?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:IMPEDance value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:IMPEDance {FIFTy|HIGHZ}
        - POWer:POWer<x>:CLRESPONSE:IMPEDance?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``FIFTy`` sets the impedance to be 50 Ω.
        - ``HIGHZ`` sets the impedance to be 1 MΩ.
    """


class PowerPowerItemClresponseGenerator(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:GENerator`` command.

    Description:
        - This command sets or queries the generator source used to send stimulus signals to the
          DUT, for the Control Loop Response power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:GENerator?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:GENerator?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:GENerator value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:GENerator {INTernal}
        - POWer:POWer<x>:CLRESPONSE:GENerator?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``INTernal`` sets the generator to the instrument AFG. This is the only valid argument.
    """


class PowerPowerItemClresponseGenipaddress(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:GENIPADDress`` command.

    Description:
        - Sets or queries the IP address of the external generator to be used with the specified
          Control Loop Response measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:GENIPADDress?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:GENIPADDress?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:GENIPADDress value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:GENIPADDress <NR2>
        - POWer:POWer<x>:CLRESPONSE:GENIPADDress?
        ```

    Info:
        - ``POWer<x>`` is the number of the power measurement.<NR2> is the IP address of the
          generator.
    """


class PowerPowerItemClresponseFreqvalItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val`` command.

    Description:
        - This command sets or queries the generator frequency value of the specified configuration
          step for the Control Loop Response power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val <NR3>
        - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?
        ```

    Info:
        - ``Power<x>`` sets the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``FREQ<x>`` sets the configuration step number, in the range of 1 to 11. Values outside
          this range will report an error.
        - ``<NR3>`` sets the frequency of the specified configuration step number, in the range of
          10 Hz to 50 MHz.
    """


class PowerPowerItemClresponseConstamplitude(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude`` command.

    Description:
        - This command sets or queries the constant amplitude voltage for the Control Loop Response
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude <NR3>
        - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the constant amplitude voltage value for the measurement, in the range of
          -100 V to 100 V.
    """


class PowerPowerItemClresponseConnectstatus(SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus`` command.

    Description:
        - Queries connection status to the external generator used with the specified Control Loop
          Response power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?
        ```

    Info:
        - ``POWer<x>`` is the number of the power measurement.
    """


class PowerPowerItemClresponseAutorbw(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:AUTORbw`` command.

    Description:
        - This command enables Auto RBW computation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:AUTORbw?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:AUTORbw?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:AUTORbw value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:AUTORbw {True|False}
        - POWer:POWer<x>:CLRESPONSE:AUTORbw?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``True`` enables Auto RBW computation.
        - ``False`` disables Auto RBW computation.
    """


class PowerPowerItemClresponseAnalysismethod(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod`` command.

    Description:
        - This command sets or queries the Analysis Method for Control Loop Response measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:ANALYSISMethod {SV|FFT}
        - POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``SV`` sets the Analysis Method as Spectrum View.
        - ``FFT`` sets the Analysis Method as FFT.
    """


class PowerPowerItemClresponseAmpmode(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:AMPMode`` command.

    Description:
        - This command sets or queries the amplitude mode for the Control Loop Response power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMPMode?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMPMode?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:AMPMode value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:AMPMode {CONSTant|PROFile}
        - POWer:POWer<x>:CLRESPONSE:AMPMode?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CONSTant`` sets the amplitude mode to output a constant amplitude signal from the DUT
          stimulus generator for all frequency bands.
        - ``PROFile`` enables configuring the generator to set amplitude values for each frequency
          band.
    """


class PowerPowerItemClresponseAmpvalItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val`` command.

    Description:
        - This command sets or queries the generator amplitude value of the specified configuration
          step for the Control Loop Response power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:AMP<x>Val <NR3>
        - POWer:POWer<x>:CLRESPONSE:AMP<x>Val?
        ```

    Info:
        - ``Power<x>`` sets the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``AMP<x>`` sets the configuration step number, in the range of 1 to 10. Values outside
          this range will report an error.
        - ``<NR3>`` sets the generator amplitude for the specified configuration step, in the range
          of -100 V to 100 V.
    """


#  pylint: disable=too-many-instance-attributes
class PowerPowerItemClresponse(SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ampval``: The ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val`` command.
        - ``.ampmode``: The ``POWer:POWer<x>:CLRESPONSE:AMPMode`` command.
        - ``.analysismethod``: The ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod`` command.
        - ``.autorbw``: The ``POWer:POWer<x>:CLRESPONSE:AUTORbw`` command.
        - ``.connectstatus``: The ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus`` command.
        - ``.constamplitude``: The ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude`` command.
        - ``.freqval``: The ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val`` command.
        - ``.genipaddress``: The ``POWer:POWer<x>:CLRESPONSE:GENIPADDress`` command.
        - ``.generator``: The ``POWer:POWer<x>:CLRESPONSE:GENerator`` command.
        - ``.impedance``: The ``POWer:POWer<x>:CLRESPONSE:IMPEDance`` command.
        - ``.inputsource``: The ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce`` command.
        - ``.mon``: The ``POWer:POWer<x>:CLRESPONSE:MON`` command.
        - ``.outputsource``: The ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce`` command.
        - ``.ppd``: The ``POWer:POWer<x>:CLRESPONSE:PPD`` command.
        - ``.startfrequency``: The ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency`` command.
        - ``.stopfrequency``: The ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency`` command.
        - ``.testconnection``: The ``POWer:POWer<x>:CLRESPONSE:TESTCONNection`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ampval: Dict[int, PowerPowerItemClresponseAmpvalItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerPowerItemClresponseAmpvalItem(device, f"{self._cmd_syntax}:AMP{x}Val")
        )
        self._ampmode = PowerPowerItemClresponseAmpmode(device, f"{self._cmd_syntax}:AMPMode")
        self._analysismethod = PowerPowerItemClresponseAnalysismethod(
            device, f"{self._cmd_syntax}:ANALYSISMethod"
        )
        self._autorbw = PowerPowerItemClresponseAutorbw(device, f"{self._cmd_syntax}:AUTORbw")
        self._connectstatus = PowerPowerItemClresponseConnectstatus(
            device, f"{self._cmd_syntax}:CONNECTSTATus"
        )
        self._constamplitude = PowerPowerItemClresponseConstamplitude(
            device, f"{self._cmd_syntax}:CONSTAMPlitude"
        )
        self._freqval: Dict[int, PowerPowerItemClresponseFreqvalItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerPowerItemClresponseFreqvalItem(device, f"{self._cmd_syntax}:FREQ{x}Val")
        )
        self._genipaddress = PowerPowerItemClresponseGenipaddress(
            device, f"{self._cmd_syntax}:GENIPADDress"
        )
        self._generator = PowerPowerItemClresponseGenerator(device, f"{self._cmd_syntax}:GENerator")
        self._impedance = PowerPowerItemClresponseImpedance(device, f"{self._cmd_syntax}:IMPEDance")
        self._inputsource = PowerPowerItemClresponseInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )
        self._mon = PowerPowerItemClresponseMon(device, f"{self._cmd_syntax}:MON")
        self._outputsource = PowerPowerItemClresponseOutputsource(
            device, f"{self._cmd_syntax}:OUTPUTSOurce"
        )
        self._ppd = PowerPowerItemClresponsePpd(device, f"{self._cmd_syntax}:PPD")
        self._startfrequency = PowerPowerItemClresponseStartfrequency(
            device, f"{self._cmd_syntax}:STARTFREQuency"
        )
        self._stopfrequency = PowerPowerItemClresponseStopfrequency(
            device, f"{self._cmd_syntax}:STOPFREQuency"
        )
        self._testconnection = PowerPowerItemClresponseTestconnection(
            device, f"{self._cmd_syntax}:TESTCONNection"
        )

    @property
    def ampval(self) -> Dict[int, PowerPowerItemClresponseAmpvalItem]:
        """Return the ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val`` command.

        Description:
            - This command sets or queries the generator amplitude value of the specified
              configuration step for the Control Loop Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:AMP<x>Val <NR3>
            - POWer:POWer<x>:CLRESPONSE:AMP<x>Val?
            ```

        Info:
            - ``Power<x>`` sets the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``AMP<x>`` sets the configuration step number, in the range of 1 to 10. Values outside
              this range will report an error.
            - ``<NR3>`` sets the generator amplitude for the specified configuration step, in the
              range of -100 V to 100 V.
        """
        return self._ampval

    @property
    def ampmode(self) -> PowerPowerItemClresponseAmpmode:
        """Return the ``POWer:POWer<x>:CLRESPONSE:AMPMode`` command.

        Description:
            - This command sets or queries the amplitude mode for the Control Loop Response power
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMPMode?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:AMPMode?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:AMPMode value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:AMPMode {CONSTant|PROFile}
            - POWer:POWer<x>:CLRESPONSE:AMPMode?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CONSTant`` sets the amplitude mode to output a constant amplitude signal from the
              DUT stimulus generator for all frequency bands.
            - ``PROFile`` enables configuring the generator to set amplitude values for each
              frequency band.
        """
        return self._ampmode

    @property
    def analysismethod(self) -> PowerPowerItemClresponseAnalysismethod:
        """Return the ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod`` command.

        Description:
            - This command sets or queries the Analysis Method for Control Loop Response
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:ANALYSISMethod {SV|FFT}
            - POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``SV`` sets the Analysis Method as Spectrum View.
            - ``FFT`` sets the Analysis Method as FFT.
        """
        return self._analysismethod

    @property
    def autorbw(self) -> PowerPowerItemClresponseAutorbw:
        """Return the ``POWer:POWer<x>:CLRESPONSE:AUTORbw`` command.

        Description:
            - This command enables Auto RBW computation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:AUTORbw?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:AUTORbw?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:AUTORbw value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:AUTORbw {True|False}
            - POWer:POWer<x>:CLRESPONSE:AUTORbw?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``True`` enables Auto RBW computation.
            - ``False`` disables Auto RBW computation.
        """
        return self._autorbw

    @property
    def connectstatus(self) -> PowerPowerItemClresponseConnectstatus:
        """Return the ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus`` command.

        Description:
            - Queries connection status to the external generator used with the specified Control
              Loop Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?
            ```

        Info:
            - ``POWer<x>`` is the number of the power measurement.
        """
        return self._connectstatus

    @property
    def constamplitude(self) -> PowerPowerItemClresponseConstamplitude:
        """Return the ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude`` command.

        Description:
            - This command sets or queries the constant amplitude voltage for the Control Loop
              Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude <NR3>
            - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the constant amplitude voltage value for the measurement, in the range of
              -100 V to 100 V.
        """
        return self._constamplitude

    @property
    def freqval(self) -> Dict[int, PowerPowerItemClresponseFreqvalItem]:
        """Return the ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val`` command.

        Description:
            - This command sets or queries the generator frequency value of the specified
              configuration step for the Control Loop Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val <NR3>
            - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?
            ```

        Info:
            - ``Power<x>`` sets the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``FREQ<x>`` sets the configuration step number, in the range of 1 to 11. Values
              outside this range will report an error.
            - ``<NR3>`` sets the frequency of the specified configuration step number, in the range
              of 10 Hz to 50 MHz.
        """
        return self._freqval

    @property
    def genipaddress(self) -> PowerPowerItemClresponseGenipaddress:
        """Return the ``POWer:POWer<x>:CLRESPONSE:GENIPADDress`` command.

        Description:
            - Sets or queries the IP address of the external generator to be used with the specified
              Control Loop Response measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:GENIPADDress?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:GENIPADDress?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:GENIPADDress value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:GENIPADDress <NR2>
            - POWer:POWer<x>:CLRESPONSE:GENIPADDress?
            ```

        Info:
            - ``POWer<x>`` is the number of the power measurement.<NR2> is the IP address of the
              generator.
        """
        return self._genipaddress

    @property
    def generator(self) -> PowerPowerItemClresponseGenerator:
        """Return the ``POWer:POWer<x>:CLRESPONSE:GENerator`` command.

        Description:
            - This command sets or queries the generator source used to send stimulus signals to the
              DUT, for the Control Loop Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:GENerator?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:GENerator?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:GENerator value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:GENerator {INTernal}
            - POWer:POWer<x>:CLRESPONSE:GENerator?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``INTernal`` sets the generator to the instrument AFG. This is the only valid
              argument.
        """
        return self._generator

    @property
    def impedance(self) -> PowerPowerItemClresponseImpedance:
        """Return the ``POWer:POWer<x>:CLRESPONSE:IMPEDance`` command.

        Description:
            - This command sets or queries the vertical termination impedance for the Control Loop
              Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:IMPEDance?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:IMPEDance?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:IMPEDance value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:IMPEDance {FIFTy|HIGHZ}
            - POWer:POWer<x>:CLRESPONSE:IMPEDance?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``FIFTy`` sets the impedance to be 50 Ω.
            - ``HIGHZ`` sets the impedance to be 1 MΩ.
        """
        return self._impedance

    @property
    def inputsource(self) -> PowerPowerItemClresponseInputsource:
        """Return the ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for the Control Loop Response power
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:INPUTSOurce CH<x>
            - POWer:POWer<x>:CLRESPONSE:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` sets the channel to use for the output signal source.
        """
        return self._inputsource

    @property
    def mon(self) -> PowerPowerItemClresponseMon:
        """Return the ``POWer:POWer<x>:CLRESPONSE:MON`` command.

        Description:
            - This command sets or returns the measure on for the control loop response, PSRR or
              impedance measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:MON?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:MON?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:MON value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:MON {SAVG|SSEQ}
            - POWer:POWer<x>:CLRESPONSE:MON?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``SAVG`` specifies the measure analysis method for the Control Loop Response/PSRR or
              Impedance measurement to SAVG.
            - ``SSEQ`` specifies the measure analysis method for the Control Loop Response/PSRR or
              Impedance measurement to SSEQ.
        """
        return self._mon

    @property
    def outputsource(self) -> PowerPowerItemClresponseOutputsource:
        """Return the ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce`` command.

        Description:
            - This command sets or queries the output source for the Control Loop Response power
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce CH<x>
            - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` sets the channel to use for the output signal source.
        """
        return self._outputsource

    @property
    def ppd(self) -> PowerPowerItemClresponsePpd:
        """Return the ``POWer:POWer<x>:CLRESPONSE:PPD`` command.

        Description:
            - This command sets or queries the points per decade (PPD) value for the Control Loop
              Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:PPD?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:PPD?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:PPD value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:PPD <NR3>
            - POWer:POWer<x>:CLRESPONSE:PPD?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the PPD value for the measurement, in the range of 10 to 100 points.
        """
        return self._ppd

    @property
    def startfrequency(self) -> PowerPowerItemClresponseStartfrequency:
        """Return the ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency`` command.

        Description:
            - This command sets or queries the start frequency value for the Control Loop Response
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:STARTFREQuency <NR3>
            - POWer:POWer<x>:CLRESPONSE:STARTFREQuency?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the starting frequency for the measurement, in the range of 10 Hz to 50
              MHz.
        """
        return self._startfrequency

    @property
    def stopfrequency(self) -> PowerPowerItemClresponseStopfrequency:
        """Return the ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency`` command.

        Description:
            - This command sets or queries the stop frequency value for the Control Loop Response
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:STOPFREQuency <NR3>
            - POWer:POWer<x>:CLRESPONSE:STOPFREQuency?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the stop frequency for the measurement, in the range of 10 Hz to 50 MHz.
        """
        return self._stopfrequency

    @property
    def testconnection(self) -> PowerPowerItemClresponseTestconnection:
        """Return the ``POWer:POWer<x>:CLRESPONSE:TESTCONNection`` command.

        Description:
            - This command tests the connection to the external generator used with the specified
              Control Loop Response power measurement.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:TESTCONNection value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:TESTCONNection EXECute
            ```

        Info:
            - ``POWer<x>`` is the number of the PSRR power measurement.
            - ``EXECute`` runs the test connection function.
        """
        return self._testconnection


class PowerPowerItemAutoset(SCPICmdWrite):
    """The ``POWer:POWer<x>:AUTOSet`` command.

    Description:
        - This command executes power autoset for the specified power measurement number.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:AUTOSet value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:AUTOSet EXECute
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          on a power measurement badge in the UI.
    """


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class PowerPowerItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``POWer:POWer<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autoset``: The ``POWer:POWer<x>:AUTOSet`` command.
        - ``.clresponse``: The ``POWer:POWer<x>:CLRESPONSE`` command tree.
        - ``.cycleamp``: The ``POWer:POWer<x>:CYCLEAmp`` command tree.
        - ``.cyclebase``: The ``POWer:POWer<x>:CYCLEBase`` command tree.
        - ``.cyclemax``: The ``POWer:POWer<x>:CYCLEMAX`` command tree.
        - ``.cyclemin``: The ``POWer:POWer<x>:CYCLEMin`` command tree.
        - ``.cyclepkpk``: The ``POWer:POWer<x>:CYCLEPKPK`` command tree.
        - ``.cycletop``: The ``POWer:POWer<x>:CYCLETop`` command tree.
        - ``.didt``: The ``POWer:POWer<x>:DIDT`` command tree.
        - ``.dvdt``: The ``POWer:POWer<x>:DVDT`` command tree.
        - ``.efficiency``: The ``POWer:POWer<x>:EFFICIENCY`` command tree.
        - ``.frequency``: The ``POWer:POWer<x>:FREQUENCY`` command tree.
        - ``.gating``: The ``POWer:POWer<x>:GATing`` command.
        - ``.harmonics``: The ``POWer:POWer<x>:HARMONICS`` command tree.
        - ``.impedance``: The ``POWer:POWer<x>:IMPEDANCE`` command tree.
        - ``.inductance``: The ``POWer:POWer<x>:INDUCTANCE`` command tree.
        - ``.inputcap``: The ``POWer:POWer<x>:INPUTCAP`` command tree.
        - ``.inrushcurrent``: The ``POWer:POWer<x>:INRUSHcurrent`` command tree.
        - ``.ivsintegralv``: The ``POWer:POWer<x>:IVSINTEGRALV`` command tree.
        - ``.label``: The ``POWer:POWer<x>:LABel`` command.
        - ``.lineripple``: The ``POWer:POWer<x>:LINERIPPLE`` command tree.
        - ``.magneticloss``: The ``POWer:POWer<x>:MAGNETICLOSS`` command tree.
        - ``.magproperty``: The ``POWer:POWer<x>:MAGPROPERTY`` command tree.
        - ``.ndutycycle``: The ``POWer:POWer<x>:NDUTYCYCLE`` command tree.
        - ``.npulsewidth``: The ``POWer:POWer<x>:NPULSEWIDTH`` command tree.
        - ``.pdutycycle``: The ``POWer:POWer<x>:PDUTYCYCLE`` command tree.
        - ``.period``: The ``POWer:POWer<x>:PERIOD`` command tree.
        - ``.powerquality``: The ``POWer:POWer<x>:POWERQUALITY`` command tree.
        - ``.ppulsewidth``: The ``POWer:POWer<x>:PPULSEWIDTH`` command tree.
        - ``.preset``: The ``POWer:POWer<x>:PRESET`` command.
        - ``.psrr``: The ``POWer:POWer<x>:PSRR`` command tree.
        - ``.rdson``: The ``POWer:POWer<x>:RDSON`` command tree.
        - ``.reflevels``: The ``POWer:POWer<x>:REFLevels`` command tree.
        - ``.results``: The ``POWer:POWer<x>:RESUlts`` command tree.
        - ``.seqsetup``: The ``POWer:POWer<x>:SEQSETup`` command.
        - ``.sequence``: The ``POWer:POWer<x>:SEQuence`` command.
        - ``.soa``: The ``POWer:POWer<x>:SOA`` command tree.
        - ``.switchingloss``: The ``POWer:POWer<x>:SWITCHINGLOSS`` command tree.
        - ``.switchingripple``: The ``POWer:POWer<x>:SWITCHINGRIPPLE`` command tree.
        - ``.turnofftime``: The ``POWer:POWer<x>:TURNOFFtime`` command tree.
        - ``.turnontime``: The ``POWer:POWer<x>:TURNONtime`` command tree.
        - ``.type``: The ``POWer:POWer<x>:TYPe`` command.
        - ``.wrap``: The ``POWer:POWer<x>:WRAP`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoset = PowerPowerItemAutoset(device, f"{self._cmd_syntax}:AUTOSet")
        self._clresponse = PowerPowerItemClresponse(device, f"{self._cmd_syntax}:CLRESPONSE")
        self._cycleamp = PowerPowerItemCycleamp(device, f"{self._cmd_syntax}:CYCLEAmp")
        self._cyclebase = PowerPowerItemCyclebase(device, f"{self._cmd_syntax}:CYCLEBase")
        self._cyclemax = PowerPowerItemCyclemax(device, f"{self._cmd_syntax}:CYCLEMAX")
        self._cyclemin = PowerPowerItemCyclemin(device, f"{self._cmd_syntax}:CYCLEMin")
        self._cyclepkpk = PowerPowerItemCyclepkpk(device, f"{self._cmd_syntax}:CYCLEPKPK")
        self._cycletop = PowerPowerItemCycletop(device, f"{self._cmd_syntax}:CYCLETop")
        self._didt = PowerPowerItemDidt(device, f"{self._cmd_syntax}:DIDT")
        self._dvdt = PowerPowerItemDvdt(device, f"{self._cmd_syntax}:DVDT")
        self._efficiency = PowerPowerItemEfficiency(device, f"{self._cmd_syntax}:EFFICIENCY")
        self._frequency = PowerPowerItemFrequency(device, f"{self._cmd_syntax}:FREQUENCY")
        self._gating = PowerPowerItemGating(device, f"{self._cmd_syntax}:GATing")
        self._harmonics = PowerPowerItemHarmonics(device, f"{self._cmd_syntax}:HARMONICS")
        self._impedance = PowerPowerItemImpedance(device, f"{self._cmd_syntax}:IMPEDANCE")
        self._inductance = PowerPowerItemInductance(device, f"{self._cmd_syntax}:INDUCTANCE")
        self._inputcap = PowerPowerItemInputcap(device, f"{self._cmd_syntax}:INPUTCAP")
        self._inrushcurrent = PowerPowerItemInrushcurrent(
            device, f"{self._cmd_syntax}:INRUSHcurrent"
        )
        self._ivsintegralv = PowerPowerItemIvsintegralv(device, f"{self._cmd_syntax}:IVSINTEGRALV")
        self._label = PowerPowerItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._lineripple = PowerPowerItemLineripple(device, f"{self._cmd_syntax}:LINERIPPLE")
        self._magneticloss = PowerPowerItemMagneticloss(device, f"{self._cmd_syntax}:MAGNETICLOSS")
        self._magproperty = PowerPowerItemMagproperty(device, f"{self._cmd_syntax}:MAGPROPERTY")
        self._ndutycycle = PowerPowerItemNdutycycle(device, f"{self._cmd_syntax}:NDUTYCYCLE")
        self._npulsewidth = PowerPowerItemNpulsewidth(device, f"{self._cmd_syntax}:NPULSEWIDTH")
        self._pdutycycle = PowerPowerItemPdutycycle(device, f"{self._cmd_syntax}:PDUTYCYCLE")
        self._period = PowerPowerItemPeriod(device, f"{self._cmd_syntax}:PERIOD")
        self._powerquality = PowerPowerItemPowerquality(device, f"{self._cmd_syntax}:POWERQUALITY")
        self._ppulsewidth = PowerPowerItemPpulsewidth(device, f"{self._cmd_syntax}:PPULSEWIDTH")
        self._preset = PowerPowerItemPreset(device, f"{self._cmd_syntax}:PRESET")
        self._psrr = PowerPowerItemPsrr(device, f"{self._cmd_syntax}:PSRR")
        self._rdson = PowerPowerItemRdson(device, f"{self._cmd_syntax}:RDSON")
        self._reflevels = PowerPowerItemReflevels(device, f"{self._cmd_syntax}:REFLevels")
        self._results = PowerPowerItemResults(device, f"{self._cmd_syntax}:RESUlts")
        self._seqsetup = PowerPowerItemSeqsetup(device, f"{self._cmd_syntax}:SEQSETup")
        self._sequence = PowerPowerItemSequence(device, f"{self._cmd_syntax}:SEQuence")
        self._soa = PowerPowerItemSoa(device, f"{self._cmd_syntax}:SOA")
        self._switchingloss = PowerPowerItemSwitchingloss(
            device, f"{self._cmd_syntax}:SWITCHINGLOSS"
        )
        self._switchingripple = PowerPowerItemSwitchingripple(
            device, f"{self._cmd_syntax}:SWITCHINGRIPPLE"
        )
        self._turnofftime = PowerPowerItemTurnofftime(device, f"{self._cmd_syntax}:TURNOFFtime")
        self._turnontime = PowerPowerItemTurnontime(device, f"{self._cmd_syntax}:TURNONtime")
        self._type = PowerPowerItemType(device, f"{self._cmd_syntax}:TYPe")
        self._wrap = PowerPowerItemWrap(device, f"{self._cmd_syntax}:WRAP")

    @property
    def autoset(self) -> PowerPowerItemAutoset:
        """Return the ``POWer:POWer<x>:AUTOSet`` command.

        Description:
            - This command executes power autoset for the specified power measurement number.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:AUTOSet value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:AUTOSet EXECute
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
        """
        return self._autoset

    @property
    def clresponse(self) -> PowerPowerItemClresponse:
        """Return the ``POWer:POWer<x>:CLRESPONSE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ampval``: The ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val`` command.
            - ``.ampmode``: The ``POWer:POWer<x>:CLRESPONSE:AMPMode`` command.
            - ``.analysismethod``: The ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod`` command.
            - ``.autorbw``: The ``POWer:POWer<x>:CLRESPONSE:AUTORbw`` command.
            - ``.connectstatus``: The ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus`` command.
            - ``.constamplitude``: The ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude`` command.
            - ``.freqval``: The ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val`` command.
            - ``.genipaddress``: The ``POWer:POWer<x>:CLRESPONSE:GENIPADDress`` command.
            - ``.generator``: The ``POWer:POWer<x>:CLRESPONSE:GENerator`` command.
            - ``.impedance``: The ``POWer:POWer<x>:CLRESPONSE:IMPEDance`` command.
            - ``.inputsource``: The ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce`` command.
            - ``.mon``: The ``POWer:POWer<x>:CLRESPONSE:MON`` command.
            - ``.outputsource``: The ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce`` command.
            - ``.ppd``: The ``POWer:POWer<x>:CLRESPONSE:PPD`` command.
            - ``.startfrequency``: The ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency`` command.
            - ``.stopfrequency``: The ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency`` command.
            - ``.testconnection``: The ``POWer:POWer<x>:CLRESPONSE:TESTCONNection`` command.
        """
        return self._clresponse

    @property
    def cycleamp(self) -> PowerPowerItemCycleamp:
        """Return the ``POWer:POWer<x>:CYCLEAmp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEAmp?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEAmp?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:CYCLEAmp:INPUTSOurce`` command.
        """
        return self._cycleamp

    @property
    def cyclebase(self) -> PowerPowerItemCyclebase:
        """Return the ``POWer:POWer<x>:CYCLEBase`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEBase?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEBase?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:CYCLEBase:INPUTSOurce`` command.
        """
        return self._cyclebase

    @property
    def cyclemax(self) -> PowerPowerItemCyclemax:
        """Return the ``POWer:POWer<x>:CYCLEMAX`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEMAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEMAX?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:CYCLEMAX:INPUTSOurce`` command.
        """
        return self._cyclemax

    @property
    def cyclemin(self) -> PowerPowerItemCyclemin:
        """Return the ``POWer:POWer<x>:CYCLEMin`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEMin?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEMin?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:CYCLEMin:INPUTSOurce`` command.
        """
        return self._cyclemin

    @property
    def cyclepkpk(self) -> PowerPowerItemCyclepkpk:
        """Return the ``POWer:POWer<x>:CYCLEPKPK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLEPKPK?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLEPKPK?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:CYCLEPKPK:INPUTSOurce`` command.
        """
        return self._cyclepkpk

    @property
    def cycletop(self) -> PowerPowerItemCycletop:
        """Return the ``POWer:POWer<x>:CYCLETop`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CYCLETop?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CYCLETop?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:CYCLETop:INPUTSOurce`` command.
        """
        return self._cycletop

    @property
    def didt(self) -> PowerPowerItemDidt:
        """Return the ``POWer:POWer<x>:DIDT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:DIDT?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:DIDT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:DIDT:INPUTSOurce`` command.
            - ``.sourceedgetype``: The ``POWer:POWer<x>:DIDT:SOURCEEDGEType`` command.
        """
        return self._didt

    @property
    def dvdt(self) -> PowerPowerItemDvdt:
        """Return the ``POWer:POWer<x>:DVDT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:DVDT?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:DVDT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:DVDT:INPUTSOurce`` command.
            - ``.sourceedgetype``: The ``POWer:POWer<x>:DVDT:SOURCEEDGEType`` command.
        """
        return self._dvdt

    @property
    def efficiency(self) -> PowerPowerItemEfficiency:
        """Return the ``POWer:POWer<x>:EFFICIENCY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:EFFICIENCY?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:EFFICIENCY?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputtype``: The ``POWer:POWer<x>:EFFICIENCY:INPUTType`` command.
            - ``.iout1source``: The ``POWer:POWer<x>:EFFICIENCY:IOUT1SOUrce`` command.
            - ``.iout2source``: The ``POWer:POWer<x>:EFFICIENCY:IOUT2SOUrce`` command.
            - ``.iout3source``: The ``POWer:POWer<x>:EFFICIENCY:IOUT3SOUrce`` command.
            - ``.isource``: The ``POWer:POWer<x>:EFFICIENCY:ISOUrce`` command.
            - ``.numofoutputs``: The ``POWer:POWer<x>:EFFICIENCY:NUMOFOutputs`` command.
            - ``.output1type``: The ``POWer:POWer<x>:EFFICIENCY:OUTPUT1Type`` command.
            - ``.output2type``: The ``POWer:POWer<x>:EFFICIENCY:OUTPUT2Type`` command.
            - ``.output3type``: The ``POWer:POWer<x>:EFFICIENCY:OUTPUT3Type`` command.
            - ``.outputtype``: The ``POWer:POWer<x>:EFFICIENCY:OUTPUTType`` command.
            - ``.vout1source``: The ``POWer:POWer<x>:EFFICIENCY:VOUT1SOUrce`` command.
            - ``.vout2source``: The ``POWer:POWer<x>:EFFICIENCY:VOUT2SOUrce`` command.
            - ``.vout3source``: The ``POWer:POWer<x>:EFFICIENCY:VOUT3SOUrce`` command.
            - ``.vsource``: The ``POWer:POWer<x>:EFFICIENCY:VSOUrce`` command.
        """
        return self._efficiency

    @property
    def frequency(self) -> PowerPowerItemFrequency:
        """Return the ``POWer:POWer<x>:FREQUENCY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:FREQUENCY?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:FREQUENCY?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``POWer:POWer<x>:FREQUENCY:EDGe`` command.
            - ``.inputsource``: The ``POWer:POWer<x>:FREQUENCY:INPUTSOurce`` command.
        """
        return self._frequency

    @property
    def gating(self) -> PowerPowerItemGating:
        """Return the ``POWer:POWer<x>:GATing`` command.

        Description:
            - This command sets or queries the gating type for the specified power measurement
              number.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:GATing?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:GATing?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:GATing value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:GATing {NONE|CURSOR|SCREEN|LOGIC}
            - POWer:POWer<x>:GATing?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown on a power measurement badge in the UI.
            - ``NONE`` makes measurement across the entire waveform record.
            - ``CURSOR`` makes measurements on that portion of the waveform between the cursors.
              Selecting Cursors opens cursors on the measurement source. Set the cursors so that the
              waveform area of interest is in between the cursors.
            - ``SCREEN`` takes measurements on that portion of the waveform shown in the display.
              When Zoom is on, the display is the zoom window.
            - ``LOGIC`` takes measurements only when the logical state of a specified waveform is
              true.

        Sub-properties:
            - ``.global``: The ``POWer:POWer<x>:GATing:GLOBal`` command.
        """
        return self._gating

    @property
    def harmonics(self) -> PowerPowerItemHarmonics:
        """Return the ``POWer:POWer<x>:HARMONICS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:HARMONICS?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:HARMONICS?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.class``: The ``POWer:POWer<x>:HARMONICS:CLASs`` command.
            - ``.clfile``: The ``POWer:POWer<x>:HARMONICS:CLFile`` command.
            - ``.cmethod``: The ``POWer:POWer<x>:HARMONICS:CMEThod`` command.
            - ``.fundcurrent``: The ``POWer:POWer<x>:HARMONICS:FUNDCURRent`` command.
            - ``.horder``: The ``POWer:POWer<x>:HARMONICS:HORDer`` command.
            - ``.hsource``: The ``POWer:POWer<x>:HARMONICS:HSOURce`` command.
            - ``.ipower``: The ``POWer:POWer<x>:HARMONICS:IPOWer`` command.
            - ``.isource``: The ``POWer:POWer<x>:HARMONICS:ISOURce`` command.
            - ``.linefrequency``: The ``POWer:POWer<x>:HARMONICS:LINEFREQUEncy`` command.
            - ``.oddeven``: The ``POWer:POWer<x>:HARMONICS:ODDEVen`` command.
            - ``.pfactor``: The ``POWer:POWer<x>:HARMONICS:PFACtor`` command.
            - ``.powerrating``: The ``POWer:POWer<x>:HARMONICS:POWERRating`` command.
            - ``.rcurrent``: The ``POWer:POWer<x>:HARMONICS:RCURRent`` command.
            - ``.standard``: The ``POWer:POWer<x>:HARMONICS:STANDard`` command.
            - ``.startfrequency``: The ``POWer:POWer<x>:HARMONICS:STARTFREQUEncy`` command.
            - ``.units``: The ``POWer:POWer<x>:HARMONICS:UNITs`` command.
            - ``.vsource``: The ``POWer:POWer<x>:HARMONICS:VSOURce`` command.
        """
        return self._harmonics

    @property
    def impedance(self) -> PowerPowerItemImpedance:
        """Return the ``POWer:POWer<x>:IMPEDANCE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IMPEDANCE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IMPEDANCE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``POWer<x>`` is the number of the Impedance power measurement.

        Sub-properties:
            - ``.ampval``: The ``POWer:POWer<x>:IMPEDANCE:AMP<x>Val`` command.
            - ``.ampmode``: The ``POWer:POWer<x>:IMPEDANCE:AMPMode`` command.
            - ``.analysismethod``: The ``POWer:POWer<x>:IMPEDANCE:ANALYSISMethod`` command.
            - ``.autorbw``: The ``POWer:POWer<x>:IMPEDANCE:AUTORbw`` command.
            - ``.connectstatus``: The ``POWer:POWer<x>:IMPEDANCE:CONNECTSTATus`` command.
            - ``.constamplitude``: The ``POWer:POWer<x>:IMPEDANCE:CONSTAMPlitude`` command.
            - ``.freqval``: The ``POWer:POWer<x>:IMPEDANCE:FREQ<x>Val`` command.
            - ``.genipaddress``: The ``POWer:POWer<x>:IMPEDANCE:GENIPADDress`` command.
            - ``.generator``: The ``POWer:POWer<x>:IMPEDANCE:GENerator`` command.
            - ``.impedance``: The ``POWer:POWer<x>:IMPEDANCE:IMPEDANCE`` command.
            - ``.inputsource``: The ``POWer:POWer<x>:IMPEDANCE:INPUTSOurce`` command.
            - ``.outputsource``: The ``POWer:POWer<x>:IMPEDANCE:OUTPUTSOurce`` command.
            - ``.ppd``: The ``POWer:POWer<x>:IMPEDANCE:PPD`` command.
            - ``.startfrequency``: The ``POWer:POWer<x>:IMPEDANCE:STARTFREQuency`` command.
            - ``.stopfrequency``: The ``POWer:POWer<x>:IMPEDANCE:STOPFREQuency`` command.
            - ``.testconnection``: The ``POWer:POWer<x>:IMPEDANCE:TESTCONNection`` command.
        """
        return self._impedance

    @property
    def inductance(self) -> PowerPowerItemInductance:
        """Return the ``POWer:POWer<x>:INDUCTANCE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:INDUCTANCE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INDUCTANCE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edgesource``: The ``POWer:POWer<x>:INDUCTANCE:EDGESource`` command.
            - ``.isource``: The ``POWer:POWer<x>:INDUCTANCE:ISOUrce`` command.
            - ``.vsource``: The ``POWer:POWer<x>:INDUCTANCE:VSOURce`` command.
        """
        return self._inductance

    @property
    def inputcap(self) -> PowerPowerItemInputcap:
        """Return the ``POWer:POWer<x>:INPUTCAP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:INPUTCAP?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INPUTCAP?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.isource``: The ``POWer:POWer<x>:INPUTCAP:ISOURce`` command.
            - ``.peakcurrent``: The ``POWer:POWer<x>:INPUTCAP:PEAKCURRent`` command.
            - ``.peakvoltage``: The ``POWer:POWer<x>:INPUTCAP:PEAKVOLTage`` command.
            - ``.vsource``: The ``POWer:POWer<x>:INPUTCAP:VSOURce`` command.
        """
        return self._inputcap

    @property
    def inrushcurrent(self) -> PowerPowerItemInrushcurrent:
        """Return the ``POWer:POWer<x>:INRUSHcurrent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:INRUSHcurrent?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:INRUSHcurrent?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:INRUSHcurrent:INPUTSOurce`` command.
            - ``.peakcurrent``: The ``POWer:POWer<x>:INRUSHcurrent:PEAKCURRent`` command.
        """
        return self._inrushcurrent

    @property
    def ivsintegralv(self) -> PowerPowerItemIvsintegralv:
        """Return the ``POWer:POWer<x>:IVSINTEGRALV`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:IVSINTEGRALV?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:IVSINTEGRALV?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.isource``: The ``POWer:POWer<x>:IVSINTEGRALV:ISOURce`` command.
            - ``.vsource``: The ``POWer:POWer<x>:IVSINTEGRALV:VSOURce`` command.
        """
        return self._ivsintegralv

    @property
    def label(self) -> PowerPowerItemLabel:
        """Return the ``POWer:POWer<x>:LABel`` command.

        Description:
            - This command sets or queries the label for the specified power measurement. As the
              label can contain non 7-bit ASCII text, it is stored in Percent Encoding format. The
              power measurement badge is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:LABel value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:LABel <QString>
            - POWer:POWer<x>:LABel?
            ```
        """
        return self._label

    @property
    def lineripple(self) -> PowerPowerItemLineripple:
        """Return the ``POWer:POWer<x>:LINERIPPLE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:LINERIPPLE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:LINERIPPLE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:LINERIPPLE:INPUTSOurce`` command.
            - ``.lfrequency``: The ``POWer:POWer<x>:LINERIPPLE:LFREQuency`` command.
        """
        return self._lineripple

    @property
    def magneticloss(self) -> PowerPowerItemMagneticloss:
        """Return the ``POWer:POWer<x>:MAGNETICLOSS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGNETICLOSS?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGNETICLOSS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.isource``: The ``POWer:POWer<x>:MAGNETICLOSS:ISOURce`` command.
            - ``.vsource``: The ``POWer:POWer<x>:MAGNETICLOSS:VSOURce`` command.
        """
        return self._magneticloss

    @property
    def magproperty(self) -> PowerPowerItemMagproperty:
        """Return the ``POWer:POWer<x>:MAGPROPERTY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:MAGPROPERTY?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:MAGPROPERTY?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.areaofcrosssection``: The ``POWer:POWer<x>:MAGPROPERTY:AREAofcrosssection``
              command.
            - ``.edgesource``: The ``POWer:POWer<x>:MAGPROPERTY:EDGESOURce`` command.
            - ``.isource``: The ``POWer:POWer<x>:MAGPROPERTY:ISOURce`` command.
            - ``.length``: The ``POWer:POWer<x>:MAGPROPERTY:LENgth`` command.
            - ``.primaryturns``: The ``POWer:POWer<x>:MAGPROPERTY:PRIMARYTURNs`` command.
            - ``.sec1source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC1SOURce`` command.
            - ``.sec1turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC1TURNs`` command.
            - ``.sec2source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC2SOURce`` command.
            - ``.sec2turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC2TURNs`` command.
            - ``.sec3source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC3SOURce`` command.
            - ``.sec3turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC3TURNs`` command.
            - ``.sec4source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC4SOURce`` command.
            - ``.sec4turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC4TURNs`` command.
            - ``.sec5source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC5SOURce`` command.
            - ``.sec5turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC5TURNs`` command.
            - ``.sec6source``: The ``POWer:POWer<x>:MAGPROPERTY:SEC6SOURce`` command.
            - ``.sec6turns``: The ``POWer:POWer<x>:MAGPROPERTY:SEC6TURNs`` command.
            - ``.secphase``: The ``POWer:POWer<x>:MAGPROPERTY:SECPhase`` command.
            - ``.secvolt``: The ``POWer:POWer<x>:MAGPROPERTY:SECVolt`` command.
            - ``.secwindings``: The ``POWer:POWer<x>:MAGPROPERTY:SECWINDings`` command.
            - ``.units``: The ``POWer:POWer<x>:MAGPROPERTY:UNITs`` command.
            - ``.vsource``: The ``POWer:POWer<x>:MAGPROPERTY:VSOURce`` command.
        """
        return self._magproperty

    @property
    def ndutycycle(self) -> PowerPowerItemNdutycycle:
        """Return the ``POWer:POWer<x>:NDUTYCYCLE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:NDUTYCYCLE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:NDUTYCYCLE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edgetype``: The ``POWer:POWer<x>:NDUTYCYCLE:EDGEType`` command.
            - ``.inputsource``: The ``POWer:POWer<x>:NDUTYCYCLE:INPUTSOurce`` command.
        """
        return self._ndutycycle

    @property
    def npulsewidth(self) -> PowerPowerItemNpulsewidth:
        """Return the ``POWer:POWer<x>:NPULSEWIDTH`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:NPULSEWIDTH?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:NPULSEWIDTH?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:NPULSEWIDTH:INPUTSOurce`` command.
        """
        return self._npulsewidth

    @property
    def pdutycycle(self) -> PowerPowerItemPdutycycle:
        """Return the ``POWer:POWer<x>:PDUTYCYCLE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PDUTYCYCLE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PDUTYCYCLE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edgetype``: The ``POWer:POWer<x>:PDUTYCYCLE:EDGEType`` command.
            - ``.inputsource``: The ``POWer:POWer<x>:PDUTYCYCLE:INPUTSOurce`` command.
        """
        return self._pdutycycle

    @property
    def period(self) -> PowerPowerItemPeriod:
        """Return the ``POWer:POWer<x>:PERIOD`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PERIOD?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PERIOD?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``POWer:POWer<x>:PERIOD:EDGe`` command.
            - ``.inputsource``: The ``POWer:POWer<x>:PERIOD:INPUTSOurce`` command.
        """
        return self._period

    @property
    def powerquality(self) -> PowerPowerItemPowerquality:
        """Return the ``POWer:POWer<x>:POWERQUALITY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:POWERQUALITY?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:POWERQUALITY?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ccycles``: The ``POWer:POWer<x>:POWERQUALITY:CCYCles`` command.
            - ``.freference``: The ``POWer:POWer<x>:POWERQUALITY:FREFerence`` command.
            - ``.isource``: The ``POWer:POWer<x>:POWERQUALITY:ISOURce`` command.
            - ``.stype``: The ``POWer:POWer<x>:POWERQUALITY:STYPe`` command.
            - ``.vsource``: The ``POWer:POWer<x>:POWERQUALITY:VSOURce`` command.
        """
        return self._powerquality

    @property
    def ppulsewidth(self) -> PowerPowerItemPpulsewidth:
        """Return the ``POWer:POWer<x>:PPULSEWIDTH`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PPULSEWIDTH?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PPULSEWIDTH?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:PPULSEWIDTH:INPUTSOurce`` command.
        """
        return self._ppulsewidth

    @property
    def preset(self) -> PowerPowerItemPreset:
        """Return the ``POWer:POWer<x>:PRESET`` command.

        Description:
            - This command runs a power preset action for the specified power measurement number.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PRESET value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PRESET {EXECute}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``EXECute`` runs the power preset action.
        """
        return self._preset

    @property
    def psrr(self) -> PowerPowerItemPsrr:
        """Return the ``POWer:POWer<x>:PSRR`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:PSRR?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:PSRR?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ampval``: The ``POWer:POWer<x>:PSRR:AMP<x>Val`` command.
            - ``.ampmode``: The ``POWer:POWer<x>:PSRR:AMPMode`` command.
            - ``.analysismethod``: The ``POWer:POWer<x>:PSRR:ANALYSISMethod`` command.
            - ``.autorbw``: The ``POWer:POWer<x>:PSRR:AUTORbw`` command.
            - ``.connectstatus``: The ``POWer:POWer<x>:PSRR:CONNECTSTATus`` command.
            - ``.constamplitude``: The ``POWer:POWer<x>:PSRR:CONSTAMPlitude`` command.
            - ``.freqval``: The ``POWer:POWer<x>:PSRR:FREQ<x>Val`` command.
            - ``.genipaddress``: The ``POWer:POWer<x>:PSRR:GENIPADDress`` command.
            - ``.generator``: The ``POWer:POWer<x>:PSRR:GENerator`` command.
            - ``.impedance``: The ``POWer:POWer<x>:PSRR:IMPEDance`` command.
            - ``.inputsource``: The ``POWer:POWer<x>:PSRR:INPUTSOurce`` command.
            - ``.outputsource``: The ``POWer:POWer<x>:PSRR:OUTPUTSOurce`` command.
            - ``.ppd``: The ``POWer:POWer<x>:PSRR:PPD`` command.
            - ``.startfrequency``: The ``POWer:POWer<x>:PSRR:STARTFREQuency`` command.
            - ``.stopfrequency``: The ``POWer:POWer<x>:PSRR:STOPFREQuency`` command.
            - ``.testconnection``: The ``POWer:POWer<x>:PSRR:TESTCONNection`` command.
        """
        return self._psrr

    @property
    def rdson(self) -> PowerPowerItemRdson:
        """Return the ``POWer:POWer<x>:RDSON`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:RDSON?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RDSON?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.devicetype``: The ``POWer:POWer<x>:RDSON:DEVICEType`` command.
            - ``.isource``: The ``POWer:POWer<x>:RDSON:ISOURce`` command.
            - ``.vsource``: The ``POWer:POWer<x>:RDSON:VSOURce`` command.
        """
        return self._rdson

    @property
    def reflevels(self) -> PowerPowerItemReflevels:
        """Return the ``POWer:POWer<x>:REFLevels`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:REFLevels?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:REFLevels?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.absolute``: The ``POWer:POWer<x>:REFLevels:ABSolute`` command tree.
            - ``.basetop``: The ``POWer:POWer<x>:REFLevels:BASETop`` command.
            - ``.method``: The ``POWer:POWer<x>:REFLevels:METHod`` command.
            - ``.percent``: The ``POWer:POWer<x>:REFLevels:PERCent`` command tree.
        """
        return self._reflevels

    @property
    def results(self) -> PowerPowerItemResults:
        """Return the ``POWer:POWer<x>:RESUlts`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:RESUlts?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RESUlts?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.allacqs``: The ``POWer:POWer<x>:RESUlts:ALLAcqs`` command tree.
            - ``.currentacq``: The ``POWer:POWer<x>:RESUlts:CURRentacq`` command tree.
        """
        return self._results

    @property
    def seqsetup(self) -> PowerPowerItemSeqsetup:
        """Return the ``POWer:POWer<x>:SEQSETup`` command.

        Description:
            - This command sets up the instrument's horizontal, vertical, and trigger parameters to
              optimize for taking the specified power measurement.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:SEQSETup value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SEQSETup Execute
            ```

        Info:
            - ``POWer<x>`` is the Power measurement identifier number. The number must be for a
              power measurement that requires a single sequence acquisition.
            - ``Execute`` sets the measurement to run an acquisition and acquire data for the
              specified single sequence power measurement.
        """
        return self._seqsetup

    @property
    def sequence(self) -> PowerPowerItemSequence:
        """Return the ``POWer:POWer<x>:SEQuence`` command.

        Description:
            - This command sets or queries the run state of a single sequence power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SEQuence?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SEQuence?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:SEQuence value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:SEQuence {RUN|RERUN}
            - POWer:POWer<x>:SEQuence?
            ```

        Info:
            - ``POWer<x>`` is the Power measurement identifier number. The number must be for a
              power measurement that requires a single sequence acquisition.
            - ``RUN`` sets the measurement to run an acquisition and acquire data for the specified
              single sequence power measurement.
            - ``RERUN`` sets the measurement to rerun an acquisition and acquire data for the
              specified single sequence power measurement.
        """
        return self._sequence

    @property
    def soa(self) -> PowerPowerItemSoa:
        """Return the ``POWer:POWer<x>:SOA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SOA?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SOA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.isource``: The ``POWer:POWer<x>:SOA:ISOURce`` command.
            - ``.point``: The ``POWer:POWer<x>:SOA:POINT<x>`` command.
            - ``.recallmask``: The ``POWer:POWer<x>:SOA:RECAllmask`` command.
            - ``.savemask``: The ``POWer:POWer<x>:SOA:SAVemask`` command.
            - ``.vsource``: The ``POWer:POWer<x>:SOA:VSOURce`` command.
        """
        return self._soa

    @property
    def switchingloss(self) -> PowerPowerItemSwitchingloss:
        """Return the ``POWer:POWer<x>:SWITCHINGLOSS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SWITCHINGLOSS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.devicetype``: The ``POWer:POWer<x>:SWITCHINGLOSS:DEVICEType`` command.
            - ``.gatesource``: The ``POWer:POWer<x>:SWITCHINGLOSS:GATESOurce`` command.
            - ``.ilevelabs``: The ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELAbs`` command.
            - ``.ilevelpct``: The ``POWer:POWer<x>:SWITCHINGLOSS:ILEVELPct`` command.
            - ``.isource``: The ``POWer:POWer<x>:SWITCHINGLOSS:ISOURce`` command.
            - ``.levelunits``: The ``POWer:POWer<x>:SWITCHINGLOSS:LEVELUNIts`` command.
            - ``.rdson``: The ``POWer:POWer<x>:SWITCHINGLOSS:RDSOn`` command.
            - ``.swlconfigtype``: The ``POWer:POWer<x>:SWITCHINGLOSS:SWLCONFIGType`` command.
            - ``.vcesat``: The ``POWer:POWer<x>:SWITCHINGLOSS:VCESat`` command.
            - ``.vglevel``: The ``POWer:POWer<x>:SWITCHINGLOSS:VGLevel`` command.
            - ``.vlevelabs``: The ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELAbs`` command.
            - ``.vlevelpct``: The ``POWer:POWer<x>:SWITCHINGLOSS:VLEVELPct`` command.
            - ``.vsource``: The ``POWer:POWer<x>:SWITCHINGLOSS:VSOURce`` command.
        """
        return self._switchingloss

    @property
    def switchingripple(self) -> PowerPowerItemSwitchingripple:
        """Return the ``POWer:POWer<x>:SWITCHINGRIPPLE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:SWITCHINGRIPPLE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:SWITCHINGRIPPLE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.inputsource``: The ``POWer:POWer<x>:SWITCHINGRIPPLE:INPUTSOurce`` command.
            - ``.lfrequency``: The ``POWer:POWer<x>:SWITCHINGRIPPLE:LFREQuency`` command.
        """
        return self._switchingripple

    @property
    def turnofftime(self) -> PowerPowerItemTurnofftime:
        """Return the ``POWer:POWer<x>:TURNOFFtime`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNOFFtime?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TURNOFFtime?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``POWer:POWer<x>:TURNOFFtime:FREQuency`` command.
            - ``.inputlevel``: The ``POWer:POWer<x>:TURNOFFtime:INPUTLEVel`` command.
            - ``.inputsource``: The ``POWer:POWer<x>:TURNOFFtime:INPUTSOurce`` command.
            - ``.maxtime``: The ``POWer:POWer<x>:TURNOFFtime:MAXTIMe`` command.
            - ``.maxvoltage``: The ``POWer:POWer<x>:TURNOFFtime:MAXVoltage`` command.
            - ``.numoutputs``: The ``POWer:POWer<x>:TURNOFFtime:NUMOUTputs`` command.
            - ``.output1source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT1SOURce`` command.
            - ``.output1voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT1VOLTage`` command.
            - ``.output2source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT2SOURce`` command.
            - ``.output2voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT2VOLTage`` command.
            - ``.output3source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT3SOURce`` command.
            - ``.output3voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT3VOLTage`` command.
            - ``.output4source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT4SOURce`` command.
            - ``.output4voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT4VOLTage`` command.
            - ``.output5source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT5SOURce`` command.
            - ``.output5voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT5VOLTage`` command.
            - ``.output6source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT6SOURce`` command.
            - ``.output6voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT6VOLTage`` command.
            - ``.output7source``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT7SOURce`` command.
            - ``.output7voltage``: The ``POWer:POWer<x>:TURNOFFtime:OUTPUT7VOLTage`` command.
            - ``.type``: The ``POWer:POWer<x>:TURNOFFtime:TYPE`` command.
        """
        return self._turnofftime

    @property
    def turnontime(self) -> PowerPowerItemTurnontime:
        """Return the ``POWer:POWer<x>:TURNONtime`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TURNONtime?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TURNONtime?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``POWer:POWer<x>:TURNONtime:FREQuency`` command.
            - ``.inputlevel``: The ``POWer:POWer<x>:TURNONtime:INPUTLEVel`` command.
            - ``.inputsource``: The ``POWer:POWer<x>:TURNONtime:INPUTSOurce`` command.
            - ``.maxtime``: The ``POWer:POWer<x>:TURNONtime:MAXTIMe`` command.
            - ``.maxvoltage``: The ``POWer:POWer<x>:TURNONtime:MAXVoltage`` command.
            - ``.numoutputs``: The ``POWer:POWer<x>:TURNONtime:NUMOUTputs`` command.
            - ``.output1source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT1SOURce`` command.
            - ``.output1voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT1VOLTage`` command.
            - ``.output2source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT2SOURce`` command.
            - ``.output2voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT2VOLTage`` command.
            - ``.output3source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT3SOURce`` command.
            - ``.output3voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT3VOLTage`` command.
            - ``.output4source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT4SOURce`` command.
            - ``.output4voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT4VOLTage`` command.
            - ``.output5source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT5SOURce`` command.
            - ``.output5voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT5VOLTage`` command.
            - ``.output6source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT6SOURce`` command.
            - ``.output6voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT6VOLTage`` command.
            - ``.output7source``: The ``POWer:POWer<x>:TURNONtime:OUTPUT7SOURce`` command.
            - ``.output7voltage``: The ``POWer:POWer<x>:TURNONtime:OUTPUT7VOLTage`` command.
            - ``.type``: The ``POWer:POWer<x>:TURNONtime:TYPE`` command.
        """
        return self._turnontime

    @property
    def type(self) -> PowerPowerItemType:
        r"""Return the ``POWer:POWer<x>:TYPe`` command.

        Description:
            - This command sets or queries the measurement type of the specified power measurement
              number. If the measurement number does not exist, this command creates a new power
              measurement, assigns the specified measurement number to the new measurement, and then
              assigns the measurement type to the new measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:TYPe value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:TYPe <Measurement Type>
            - POWer:POWer<x>:TYPe?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<Measurement Type>`` = CYCLEAmp \| CYCLEBase \| CYCLEMAx \| CYCLEMIn \| CYCLEPKpk \|
              CYCLETop \| DIDT \| DVDT \| EFFICIENCY \| FREQuency \| HARMonics \|IMPEDANCE\|
              INDUCTANCE \| INPUTCAP \| INRUSHcurrent\| \| IVSINTEGRALV \| LINERIpple \|
              MAGNETICLOSS \| MAGPROPERTY \| NDUTYCycle \| NPULSEWidth \| PDUTYCycle \| PERIod \|
              POWERQUALity \| PPULSEWidth \| RDSON \| SOA \| SWITCHINGLOss \| SWITCHINGRIpple \|
              TURNOFFtime \| TURNONtime\| CLRESPONSE \| PSRR.
        """
        return self._type

    @property
    def wrap(self) -> PowerPowerItemWrap:
        """Return the ``POWer:POWer<x>:WRAP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:WRAP?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:WRAP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.degrees``: The ``POWer:POWer<x>:WRAP:DEGrees`` command.
            - ``.state``: The ``POWer:POWer<x>:WRAP:STATE`` command.
        """
        return self._wrap


class PowerDelete(SCPICmdWrite):
    """The ``POWer:DELete`` command.

    Description:
        - This command deletes the specified power measurement number. The power measurement number
          is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:DELete value`` command.

    SCPI Syntax:
        ```
        - POWer:DELete 'POWER<x>'
        ```
    """


class PowerAddnew(SCPICmdWrite):
    """The ``POWer:ADDNew`` command.

    Description:
        - This command adds the specified power measurement number. The power measurement number is
          specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:ADDNew value`` command.

    SCPI Syntax:
        ```
        - POWer:ADDNew 'POWER<x>'
        ```
    """


class Power(SCPICmdRead):
    """The ``POWer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``POWer:ADDNew`` command.
        - ``.delete``: The ``POWer:DELete`` command.
        - ``.power``: The ``POWer:POWer<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "POWer") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = PowerAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = PowerDelete(device, f"{self._cmd_syntax}:DELete")
        self._power: Dict[int, PowerPowerItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerPowerItem(device, f"{self._cmd_syntax}:POWer{x}")
        )

    @property
    def addnew(self) -> PowerAddnew:
        """Return the ``POWer:ADDNew`` command.

        Description:
            - This command adds the specified power measurement number. The power measurement number
              is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:ADDNew value`` command.

        SCPI Syntax:
            ```
            - POWer:ADDNew 'POWER<x>'
            ```
        """
        return self._addnew

    @property
    def delete(self) -> PowerDelete:
        """Return the ``POWer:DELete`` command.

        Description:
            - This command deletes the specified power measurement number. The power measurement
              number is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:DELete value`` command.

        SCPI Syntax:
            ```
            - POWer:DELete 'POWER<x>'
            ```
        """
        return self._delete

    @property
    def power(self) -> Dict[int, PowerPowerItem]:
        """Return the ``POWer:POWer<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autoset``: The ``POWer:POWer<x>:AUTOSet`` command.
            - ``.clresponse``: The ``POWer:POWer<x>:CLRESPONSE`` command tree.
            - ``.cycleamp``: The ``POWer:POWer<x>:CYCLEAmp`` command tree.
            - ``.cyclebase``: The ``POWer:POWer<x>:CYCLEBase`` command tree.
            - ``.cyclemax``: The ``POWer:POWer<x>:CYCLEMAX`` command tree.
            - ``.cyclemin``: The ``POWer:POWer<x>:CYCLEMin`` command tree.
            - ``.cyclepkpk``: The ``POWer:POWer<x>:CYCLEPKPK`` command tree.
            - ``.cycletop``: The ``POWer:POWer<x>:CYCLETop`` command tree.
            - ``.didt``: The ``POWer:POWer<x>:DIDT`` command tree.
            - ``.dvdt``: The ``POWer:POWer<x>:DVDT`` command tree.
            - ``.efficiency``: The ``POWer:POWer<x>:EFFICIENCY`` command tree.
            - ``.frequency``: The ``POWer:POWer<x>:FREQUENCY`` command tree.
            - ``.gating``: The ``POWer:POWer<x>:GATing`` command.
            - ``.harmonics``: The ``POWer:POWer<x>:HARMONICS`` command tree.
            - ``.impedance``: The ``POWer:POWer<x>:IMPEDANCE`` command tree.
            - ``.inductance``: The ``POWer:POWer<x>:INDUCTANCE`` command tree.
            - ``.inputcap``: The ``POWer:POWer<x>:INPUTCAP`` command tree.
            - ``.inrushcurrent``: The ``POWer:POWer<x>:INRUSHcurrent`` command tree.
            - ``.ivsintegralv``: The ``POWer:POWer<x>:IVSINTEGRALV`` command tree.
            - ``.label``: The ``POWer:POWer<x>:LABel`` command.
            - ``.lineripple``: The ``POWer:POWer<x>:LINERIPPLE`` command tree.
            - ``.magneticloss``: The ``POWer:POWer<x>:MAGNETICLOSS`` command tree.
            - ``.magproperty``: The ``POWer:POWer<x>:MAGPROPERTY`` command tree.
            - ``.ndutycycle``: The ``POWer:POWer<x>:NDUTYCYCLE`` command tree.
            - ``.npulsewidth``: The ``POWer:POWer<x>:NPULSEWIDTH`` command tree.
            - ``.pdutycycle``: The ``POWer:POWer<x>:PDUTYCYCLE`` command tree.
            - ``.period``: The ``POWer:POWer<x>:PERIOD`` command tree.
            - ``.powerquality``: The ``POWer:POWer<x>:POWERQUALITY`` command tree.
            - ``.ppulsewidth``: The ``POWer:POWer<x>:PPULSEWIDTH`` command tree.
            - ``.preset``: The ``POWer:POWer<x>:PRESET`` command.
            - ``.psrr``: The ``POWer:POWer<x>:PSRR`` command tree.
            - ``.rdson``: The ``POWer:POWer<x>:RDSON`` command tree.
            - ``.reflevels``: The ``POWer:POWer<x>:REFLevels`` command tree.
            - ``.results``: The ``POWer:POWer<x>:RESUlts`` command tree.
            - ``.seqsetup``: The ``POWer:POWer<x>:SEQSETup`` command.
            - ``.sequence``: The ``POWer:POWer<x>:SEQuence`` command.
            - ``.soa``: The ``POWer:POWer<x>:SOA`` command tree.
            - ``.switchingloss``: The ``POWer:POWer<x>:SWITCHINGLOSS`` command tree.
            - ``.switchingripple``: The ``POWer:POWer<x>:SWITCHINGRIPPLE`` command tree.
            - ``.turnofftime``: The ``POWer:POWer<x>:TURNOFFtime`` command tree.
            - ``.turnontime``: The ``POWer:POWer<x>:TURNONtime`` command tree.
            - ``.type``: The ``POWer:POWer<x>:TYPe`` command.
            - ``.wrap``: The ``POWer:POWer<x>:WRAP`` command tree.
        """
        return self._power
