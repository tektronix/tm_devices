# pylint: disable=line-too-long
"""The display commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DISplay:CH<x>:INVERTColor COLOR<y>
    - DISplay:CH<x>:INVERTColor?
    - DISplay:CH<x>:NORMALColor COLOR<y>
    - DISplay:CH<x>:NORMALColor?
    - DISplay:COLors {NORMal|INVERTed}
    - DISplay:COLors?
    - DISplay:GLObal:B<x>:STATE {ON|OFF|<NR1>}
    - DISplay:GLObal:B<x>:STATE?
    - DISplay:GLObal:CH<x>:STATE {ON|OFF|<NR1>}
    - DISplay:GLObal:CH<x>:STATE?
    - DISplay:GLObal:DCH<x>:STATE {ON|OFF|<NR1>}
    - DISplay:GLObal:DCH<x>:STATE?
    - DISplay:GLObal:MATH<x>:STATE {ON|OFF|<NR1>}
    - DISplay:GLObal:MATH<x>:STATE?
    - DISplay:GLObal:REF<x>:STATE {ON|OFF|<NR1>}
    - DISplay:GLObal:REF<x>:STATE?
    - DISplay:INTENSITy:BACKLight {LOW|MEDium|HIGH}
    - DISplay:INTENSITy:BACKLight:AUTODim:ENAble {ON|OFF}
    - DISplay:INTENSITy:BACKLight:AUTODim:ENAble?
    - DISplay:INTENSITy:BACKLight:AUTODim:TIMe <NR1>
    - DISplay:INTENSITy:BACKLight:AUTODim:TIMe?
    - DISplay:INTENSITy:BACKLight?
    - DISplay:INTENSITy?
    - DISplay:MATHFFTView1:AUTOScale {ON|OFF|<NR1>}
    - DISplay:MATHFFTView1:AUTOScale?
    - DISplay:MATHFFTView1:CURSor:ASOUrce?
    - DISplay:MATHFFTView1:CURSor:BSOUrce?
    - DISplay:MATHFFTView1:CURSor:DDT?
    - DISplay:MATHFFTView1:CURSor:FUNCtion {WAVEform|VBArs|HBArs|SCREEN}
    - DISplay:MATHFFTView1:CURSor:FUNCtion?
    - DISplay:MATHFFTView1:CURSor:HBArs:APOSition <NR3>
    - DISplay:MATHFFTView1:CURSor:HBArs:APOSition?
    - DISplay:MATHFFTView1:CURSor:HBArs:AUNIts?
    - DISplay:MATHFFTView1:CURSor:HBArs:BPOSition <NR3>
    - DISplay:MATHFFTView1:CURSor:HBArs:BPOSition?
    - DISplay:MATHFFTView1:CURSor:HBArs:BUNIts?
    - DISplay:MATHFFTView1:CURSor:HBArs:DELTa?
    - DISplay:MATHFFTView1:CURSor:MODe {INDEPENDENT|TRACK}
    - DISplay:MATHFFTView1:CURSor:ONEOVERDELTATVALUE?
    - DISplay:MATHFFTView1:CURSor:ROLOCATION {GRATICULE|BADGE}
    - DISplay:MATHFFTView1:CURSor:ROLOCATION?
    - DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition <NR3>
    - DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition?
    - DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition <NR3>
    - DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition?
    - DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition <NR3>
    - DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition?
    - DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition <NR3>
    - DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition?
    - DISplay:MATHFFTView1:CURSor:STATE {ON|OFF|<NR1>}
    - DISplay:MATHFFTView1:CURSor:STATE?
    - DISplay:MATHFFTView1:CURSor:VBArs:APOSition <NR3>
    - DISplay:MATHFFTView1:CURSor:VBArs:APOSition?
    - DISplay:MATHFFTView1:CURSor:VBArs:AUNIts?
    - DISplay:MATHFFTView1:CURSor:VBArs:BPOSition <NR3>
    - DISplay:MATHFFTView1:CURSor:VBArs:BPOSition?
    - DISplay:MATHFFTView1:CURSor:VBArs:BUNIts?
    - DISplay:MATHFFTView1:CURSor:VBArs:DELTa?
    - DISplay:MATHFFTView1:CURSor:WAVEform:APOSition <NR3>
    - DISplay:MATHFFTView1:CURSor:WAVEform:APOSition?
    - DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition <NR3>
    - DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition?
    - DISplay:MATHFFTView1:GRIDlines {HORizontal|VERTical|BOTH}
    - DISplay:MATHFFTView1:GRIDlines?
    - DISplay:MATHFFTView1:MATH:MATH<x>:STATE {ON|OFF|<NR1>}
    - DISplay:MATHFFTView1:MATH:MATH<x>:STATE?
    - DISplay:MATHFFTView1:XAXIS:SCALE {LINEAr|LOG}
    - DISplay:MATHFFTView1:XAXIS:SCALE?
    - DISplay:MATHFFTView1:YAXIS:SCALE {LINEAr|DBM}
    - DISplay:MATHFFTView1:YAXIS:SCALE?
    - DISplay:MATHFFTView1:ZOOM:XAXIS:FROM <NR3>
    - DISplay:MATHFFTView1:ZOOM:XAXIS:FROM?
    - DISplay:MATHFFTView1:ZOOM:XAXIS:TO <NR3>
    - DISplay:MATHFFTView1:ZOOM:XAXIS:TO?
    - DISplay:MATHFFTView1:ZOOM:YAXIS:FROM <NR3>
    - DISplay:MATHFFTView1:ZOOM:YAXIS:FROM?
    - DISplay:MATHFFTView1:ZOOM:YAXIS:TO <NR3>
    - DISplay:MATHFFTView1:ZOOM:YAXIS:TO?
    - DISplay:Math<x>:INVERTColor COLOR<y>
    - DISplay:Math<x>:INVERTColor?
    - DISplay:Math<x>:NORMALColor COLOR<y>
    - DISplay:Math<x>:NORMALColor?
    - DISplay:PERSistence {OFF|AUTO|INFPersist|INFInite|VARpersist|CLEAR}
    - DISplay:PERSistence:RESET
    - DISplay:PERSistence?
    - DISplay:PLOTView1:AUTOScale {ON|OFF|<NR1>}
    - DISplay:PLOTView1:AUTOScale?
    - DISplay:PLOTView1:CURSor:ASOUrce?
    - DISplay:PLOTView1:CURSor:BSOUrce?
    - DISplay:PLOTView1:CURSor:DDT?
    - DISplay:PLOTView1:CURSor:FUNCtion {WAVEFORM|VBArs|HBArs|SCREEN}
    - DISplay:PLOTView1:CURSor:FUNCtion?
    - DISplay:PLOTView1:CURSor:HBArs:APOSition <NR3>
    - DISplay:PLOTView1:CURSor:HBArs:APOSition?
    - DISplay:PLOTView1:CURSor:HBArs:AUNIts?
    - DISplay:PLOTView1:CURSor:HBArs:BPOSition <NR3>
    - DISplay:PLOTView1:CURSor:HBArs:BPOSition?
    - DISplay:PLOTView1:CURSor:HBArs:BUNIts?
    - DISplay:PLOTView1:CURSor:HBArs:DELTa?
    - DISplay:PLOTView1:CURSor:MODe {INDEPENDENT|TRACK}
    - DISplay:PLOTView1:CURSor:MODe?
    - DISplay:PLOTView1:CURSor:ONEOVERDELTATVALUE?
    - DISplay:PLOTView1:CURSor:ROLOCATION {GRATICULE|BADGE}
    - DISplay:PLOTView1:CURSor:ROLOCATION?
    - DISplay:PLOTView1:CURSor:SCREEN:AXPOSition <NR3>
    - DISplay:PLOTView1:CURSor:SCREEN:AXPOSition?
    - DISplay:PLOTView1:CURSor:SCREEN:AYPOSition <NR3>
    - DISplay:PLOTView1:CURSor:SCREEN:AYPOSition?
    - DISplay:PLOTView1:CURSor:SCREEN:BXPOSition <NR3>
    - DISplay:PLOTView1:CURSor:SCREEN:BXPOSition?
    - DISplay:PLOTView1:CURSor:SCREEN:BYPOSition <NR3>
    - DISplay:PLOTView1:CURSor:SCREEN:BYPOSition?
    - DISplay:PLOTView1:CURSor:SPLITMODE {SAME|SPLIT}
    - DISplay:PLOTView1:CURSor:SPLITMODE?
    - DISplay:PLOTView1:CURSor:STATE {ON|OFF|<NR1>}
    - DISplay:PLOTView1:CURSor:STATE?
    - DISplay:PLOTView1:CURSor:VBArs:APOSition <NR3>
    - DISplay:PLOTView1:CURSor:VBArs:APOSition?
    - DISplay:PLOTView1:CURSor:VBArs:BPOSition <NR3>
    - DISplay:PLOTView1:CURSor:VBArs:BPOSition?
    - DISplay:PLOTView1:CURSor:VBArs:DELTa?
    - DISplay:PLOTView1:CURSor:VBArs:UNIts?
    - DISplay:PLOTView1:CURSor:WAVEform:APOSition <NR3>
    - DISplay:PLOTView1:CURSor:WAVEform:APOSition?
    - DISplay:PLOTView1:CURSor:WAVEform:BPOSition <NR3>
    - DISplay:PLOTView1:CURSor:WAVEform:BPOSition?
    - DISplay:PLOTView1:GRIDlines {HORizontal|VERTical|BOTH}
    - DISplay:PLOTView1:GRIDlines?
    - DISplay:PLOTView1:XAXIS:SCALE {LINEAR|LOG}
    - DISplay:PLOTView1:XAXIS:SCALE?
    - DISplay:PLOTView1:YAXIS:SCALE {LINEAR|LOG}
    - DISplay:PLOTView1:YAXIS:SCALE?
    - DISplay:PLOTView1:ZOOM:XAXIS:FROM <NR3>
    - DISplay:PLOTView1:ZOOM:XAXIS:FROM?
    - DISplay:PLOTView1:ZOOM:XAXIS:TO <NR3>
    - DISplay:PLOTView1:ZOOM:XAXIS:TO?
    - DISplay:PLOTView1:ZOOM:YAXIS:FROM <NR3>
    - DISplay:PLOTView1:ZOOM:YAXIS:FROM?
    - DISplay:PLOTView1:ZOOM:YAXIS:TO <NR3>
    - DISplay:PLOTView1:ZOOM:YAXIS:TO?
    - DISplay:REF<x>:INVERTColor COLOR<y>
    - DISplay:REF<x>:INVERTColor?
    - DISplay:REF<x>:NORMALColor COLOR<y>
    - DISplay:REF<x>:NORMALColor?
    - DISplay:REFFFTView<x>:AUTOScale {OFF|ON|0|1|<NR1>}
    - DISplay:REFFFTView<x>:AUTOScale?
    - DISplay:REFFFTView<x>:CURSor:ASOUrce?
    - DISplay:REFFFTView<x>:CURSor:BSOUrce?
    - DISplay:REFFFTView<x>:CURSor:DDT?
    - DISplay:REFFFTView<x>:CURSor:FUNCtion {WAVEform|VBArs|HBArs|SCREEN}
    - DISplay:REFFFTView<x>:CURSor:FUNCtion?
    - DISplay:REFFFTView<x>:CURSor:HBArs:APOSition <NR3>
    - DISplay:REFFFTView<x>:CURSor:HBArs:APOSition?
    - DISplay:REFFFTView<x>:CURSor:HBArs:AUNIts?
    - DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition <NR3>
    - DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition?
    - DISplay:REFFFTView<x>:CURSor:HBArs:BUNIts?
    - DISplay:REFFFTView<x>:CURSor:HBArs:DELTa?
    - DISplay:REFFFTView<x>:CURSor:MODe {INDEPENDENT|TRACK}
    - DISplay:REFFFTView<x>:CURSor:MODe?
    - DISplay:REFFFTView<x>:CURSor:ONEOVERDELTATVALUE?
    - DISplay:REFFFTView<x>:CURSor:ROLOCATION {GRATICULE|BADGE}
    - DISplay:REFFFTView<x>:CURSor:ROLOCATION?
    - DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition <NR3>
    - DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition?
    - DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition <NR3>
    - DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition?
    - DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition <NR3>
    - DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition?
    - DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition <NR3>
    - DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition?
    - DISplay:REFFFTView<x>:CURSor:SPLITMODE {SAME|SPLIT}
    - DISplay:REFFFTView<x>:CURSor:SPLITMODE?
    - DISplay:REFFFTView<x>:CURSor:STATE {OFF|ON|0|1|<NR1>}
    - DISplay:REFFFTView<x>:CURSor:STATE?
    - DISplay:REFFFTView<x>:CURSor:VBArs:APOSition <NR3>
    - DISplay:REFFFTView<x>:CURSor:VBArs:APOSition?
    - DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition <NR3>
    - DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition?
    - DISplay:REFFFTView<x>:CURSor:VBArs:DELTa?
    - DISplay:REFFFTView<x>:CURSor:VBArs:UNIts?
    - DISplay:REFFFTView<x>:CURSor:WAVEform:AHPOSition?
    - DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition <NR3>
    - DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition?
    - DISplay:REFFFTView<x>:CURSor:WAVEform:AVPOSition?
    - DISplay:REFFFTView<x>:CURSor:WAVEform:BHPOSition?
    - DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition <NR3>
    - DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition?
    - DISplay:REFFFTView<x>:CURSor:WAVEform:BVPOSition?
    - DISplay:REFFFTView<x>:GRIDlines {HORizontal|VERTical|BOTH}
    - DISplay:REFFFTView<x>:GRIDlines?
    - DISplay:REFFFTView<x>:REF:REF<x>:STATE {ON|OFF|0|1|<NR1>}
    - DISplay:REFFFTView<x>:REF:REF<x>:STATE?
    - DISplay:REFFFTView<x>:XAXIS:SCALE {LINEAr|LOG}
    - DISplay:REFFFTView<x>:XAXIS:SCALE?
    - DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM <NR3>
    - DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM?
    - DISplay:REFFFTView<x>:ZOOM:XAXIS:TO <NR3>
    - DISplay:REFFFTView<x>:ZOOM:XAXIS:TO?
    - DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM <NR3>
    - DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM?
    - DISplay:REFFFTView<x>:ZOOM:YAXIS:TO <NR3>
    - DISplay:REFFFTView<x>:ZOOM:YAXIS:TO?
    - DISplay:SELect:BUS BUS<x>
    - DISplay:SELect:BUS?
    - DISplay:SELect:MATH MATH<x>
    - DISplay:SELect:MATH?
    - DISplay:SELect:REFerence {NONE|REF<x>}
    - DISplay:SELect:REFerence?
    - DISplay:SELect:SOUrce {NONE|CH<x>|DCH<x>|BUS<x>|MATH<x>|PLOT<x>|REF<x>}
    - DISplay:SELect:SOUrce?
    - DISplay:SELect:VIEW {WAVEVIEW1|MATHFFT<x>|PLOTVIEW<x>|REFFFT<x>}
    - DISplay:SELect:VIEW?
    - DISplay:SELect:WAVEView1:SOUrce {CH<x>|MATH<x>|BUS<x>|REF<x>|PLOT<x>}
    - DISplay:SELect:WAVEView1:SOUrce?
    - DISplay:VARpersist <NR3>
    - DISplay:VARpersist?
    - DISplay:WAVEView1:BUS:B<x>:STATE {OFF|ON|0|1}
    - DISplay:WAVEView1:BUS:B<x>:STATE?
    - DISplay:WAVEView1:BUS:B<x>:VERTical:POSition <NR3>
    - DISplay:WAVEView1:BUS:B<x>:VERTical:POSition?
    - DISplay:WAVEView1:CH<x>:STATE {ON|OFF|<NR1>}
    - DISplay:WAVEView1:CH<x>:STATE?
    - DISplay:WAVEView1:CH<x>:VERTical:POSition <NR3>
    - DISplay:WAVEView1:CH<x>:VERTical:POSition?
    - DISplay:WAVEView1:CH<x>:VERTical:SCAle <NR3>
    - DISplay:WAVEView1:CH<x>:VERTical:SCAle?
    - DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce {AUTO|CH<x>|BUS<x>|DCH<x>_DALL|MATH<x>|REF<x>|PLOT<x>}
    - DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce?
    - DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce {AUTO| CH<x>| BUS<x>| DCH<x>_DALL| MATH<x>| REF<x>| PLOT<x>
    - DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce?
    - DISplay:WAVEView1:CURSor:CURSOR1:DDT?
    - DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion {SCREEN|WAVEFORM|VBArs|HBArs}
    - DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion?
    - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition <NR3>
    - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition?
    - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:AUNIts?
    - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition <NR3>
    - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition?
    - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BUNIts?
    - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:DELTa?
    - DISplay:WAVEView1:CURSor:CURSOR1:MODe {INDEPENDENT|TRACK}
    - DISplay:WAVEView1:CURSor:CURSOR1:ONEOVERDELTATVALUE?
    - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition <NR3>
    - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition?
    - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition <NR3>
    - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition?
    - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition <NR3>
    - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition?
    - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition <NR3>
    - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition?
    - DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE {SAME|SPLIT}
    - DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE?
    - DISplay:WAVEView1:CURSor:CURSOR1:STATE {ON|OFF|<NR1>}
    - DISplay:WAVEView1:CURSor:CURSOR1:STATE?
    - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition <NR3>
    - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition?
    - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition <NR3>
    - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition?
    - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:DELTa?
    - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:UNIts?
    - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition <NR3>
    - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition?
    - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition <NR3>
    - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition?
    - DISplay:WAVEView1:CURSor:CURSOR1?
    - DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition?
    - DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition?
    - DISplay:WAVEView1:CURSor?
    - DISplay:WAVEView1:DCH<x>_D<x>:STATE {ON|OFF|<NR1>}
    - DISplay:WAVEView1:DCH<x>_D<x>:STATE?
    - DISplay:WAVEView1:DCH<x>_DALL:DIGORDER <QString>
    - DISplay:WAVEView1:DCH<x>_DALL:DIGORDER?
    - DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition <NR3>
    - DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition?
    - DISplay:WAVEView1:FILTer {SINX|LINear}
    - DISplay:WAVEView1:GRAticule {GRId|TIMe|FULl|NONe}
    - DISplay:WAVEView1:GRAticule?
    - DISplay:WAVEView1:INTENSITy:GRATicule <NR2>
    - DISplay:WAVEView1:INTENSITy:GRATicule?
    - DISplay:WAVEView1:INTENSITy:WAVEform <NR2>
    - DISplay:WAVEView1:INTENSITy:WAVEform?
    - DISplay:WAVEView1:MATH:MATH<x>:AUTOScale {ON|OFF|<NR1>}
    - DISplay:WAVEView1:MATH:MATH<x>:AUTOScale?
    - DISplay:WAVEView1:MATH:MATH<x>:STATE {ON|OFF|<NR1>}
    - DISplay:WAVEView1:MATH:MATH<x>:STATE?
    - DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition <NR3>
    - DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition?
    - DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle <NR3>
    - DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle?
    - DISplay:WAVEView1:REF:REF<x>:FRAMe <NR1>
    - DISplay:WAVEView1:REF:REF<x>:FRAMe?
    - DISplay:WAVEView1:REF:REF<x>:STATE {ON|OFF|<NR1>}
    - DISplay:WAVEView1:REF:REF<x>:STATE?
    - DISplay:WAVEView1:REF:REF<x>:VERTical:POSition <NR3>
    - DISplay:WAVEView1:REF:REF<x>:VERTical:POSition?
    - DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle <NR3>
    - DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle?
    - DISplay:WAVEView1:REF<x>_DALL:FRAMe <NR1>
    - DISplay:WAVEView1:REF<x>_DALL:FRAMe?
    - DISplay:WAVEView1:STYle {VECtors|DOTsonly}
    - DISplay:WAVEView1:STYle?
    - DISplay:WAVEView1:VIEWStyle {OVErlay|STAcked}
    - DISplay:WAVEView1:VIEWStyle?
    - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition <NR3>
    - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition?
    - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe <NR3>
    - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe?
    - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe <NR3>
    - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe?
    - DISplay:WAVEView1:ZOOM:ZOOM1:STATe {ON|OFF|<NR1>}
    - DISplay:WAVEView1:ZOOM:ZOOM1:STATe?
    - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition <NR3>
    - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition?
    - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe <NR3>
    - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe?
    - DISplay:WAVEView1:ZOOM:ZOOM1?
    - DISplay:WAVEView1:ZOOM?
    - DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION {GRATICULE|BADGE}
    - DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION?
    - DISplay:WAVEView:GRIDTYPE {MOVEABLE|FIXED}
    - DISplay:WAVEView:GRIDTYPE?
    - DISplay:WAVEform {ON|OFF|<NR1>}
    - DISplay:WAVEform?
    - DISplay?
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


class DisplayWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEform`` command.

    Description:
        - This command globally enables or disables the waveform display. When disabled, the
          waveform is still acquired and held in memory, but it is not drawn to the screen.
          Disabling the waveform display may improve processing speed.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEform?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:WAVEform value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEform {ON|OFF|<NR1>}
        - DISplay:WAVEform?
        ```

    Info:
        - ``<NR1>`` enables or disables the waveform display. 0 disables the waveform display; any
          other value enables the waveform display.
        - ``ON`` enables the waveform display.
        - ``OFF`` disables the waveform display.
    """


class DisplayWaveviewGridtype(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView:GRIDTYPE`` command.

    Description:
        - This command sets or queries the Waveform View Graticule type.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView:GRIDTYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView:GRIDTYPE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:WAVEView:GRIDTYPE value``
          command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView:GRIDTYPE {MOVEABLE|FIXED}
        - DISplay:WAVEView:GRIDTYPE?
        ```

    Info:
        - ``MOVEABLE`` sets the Waveform View so that both the waveform and the grid (graticule)
          move together when moving the waveform horizontally.
        - ``FIXED`` sets the Waveform View so that the grid dows not move when moving the waveform
          horizontally.
    """


class DisplayWaveviewCursorCursor1Rolocation(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION`` command.

    Description:
        - This command sets or queries the location to display the Waveform View cursor readouts (in
          the Waveform View graticule or in a badge in the Results Bar).

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION {GRATICULE|BADGE}
        - DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION?
        ```

    Info:
        - ``GRATICULE`` sets the Waveform View cursor readouts to display as part of the cursors in
          the plot view.
        - ``BADGE`` removes the Waveform View cursor readouts from the cursors in the graticule and
          displays the cursor information as a badge in the Results Bar.
    """


class DisplayWaveviewCursorCursor1(SCPICmdRead):
    """The ``DISplay:WAVEView:CURSor:CURSOR1`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView:CURSor:CURSOR1?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView:CURSor:CURSOR1?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.rolocation``: The ``DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rolocation = DisplayWaveviewCursorCursor1Rolocation(
            device, f"{self._cmd_syntax}:ROLOCATION"
        )

    @property
    def rolocation(self) -> DisplayWaveviewCursorCursor1Rolocation:
        """Return the ``DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION`` command.

        Description:
            - This command sets or queries the location to display the Waveform View cursor readouts
              (in the Waveform View graticule or in a badge in the Results Bar).

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION {GRATICULE|BADGE}
            - DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION?
            ```

        Info:
            - ``GRATICULE`` sets the Waveform View cursor readouts to display as part of the cursors
              in the plot view.
            - ``BADGE`` removes the Waveform View cursor readouts from the cursors in the graticule
              and displays the cursor information as a badge in the Results Bar.
        """
        return self._rolocation


class DisplayWaveviewCursor(SCPICmdRead):
    """The ``DISplay:WAVEView:CURSor`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView:CURSor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView:CURSor?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.cursor1``: The ``DISplay:WAVEView:CURSor:CURSOR1`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cursor1 = DisplayWaveviewCursorCursor1(device, f"{self._cmd_syntax}:CURSOR1")

    @property
    def cursor1(self) -> DisplayWaveviewCursorCursor1:
        """Return the ``DISplay:WAVEView:CURSor:CURSOR1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView:CURSor:CURSOR1?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView:CURSor:CURSOR1?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.rolocation``: The ``DISplay:WAVEView:CURSor:CURSOR1:ROLOCATION`` command.
        """
        return self._cursor1


class DisplayWaveview1ZoomZoom1VerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe`` command.

    Description:
        - This command sets or queries the vertical zoom factor of the specified zoom in the
          specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe <NR3>
        - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe?
        ```

    Info:
        - ``<NR3>`` is the amount of vertical expansion or compression. Based on the value that you
          entered, this command uses the nearest scale factor. Setting the vertical scale to 1
          indicates unity (no zoom).
    """


class DisplayWaveview1ZoomZoom1VerticalPosition(SCPICmdWrite, SCPICmdRead):
    r"""The ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition`` command.

    Description:
        - This command sets or queries the vertical position of the specified zoom in the specified
          Waveform View. It is freely movable within the confines of the acquired waveform. It is
          measured from the top to bottom of the acquisition window. The top of the zoom window is
          -5 \* vertical zoom factor. The bottom of the zoom window is +5 \* the vertical zoom
          factor. For a zoom of 5x, the position ranges from -25 to 25.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition <NR3>
        - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition?
        ```

    Info:
        - ``NR3`` is the vertical position of the specified zoom in the specified Waveform View. It
          is freely movable within the confines of the acquired waveform. The top of the zoom window
          is -5 \\* vertical zoom factor. The bottom of the zoom window is +5 \\* the vertical zoom
          factor. For a vertical zoom of 5x, the position ranges from -25 to 25.
    """


class DisplayWaveview1ZoomZoom1Vertical(SCPICmdRead):
    """The ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.position``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition`` command.
        - ``.scale``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = DisplayWaveview1ZoomZoom1VerticalPosition(
            device, f"{self._cmd_syntax}:POSition"
        )
        self._scale = DisplayWaveview1ZoomZoom1VerticalScale(device, f"{self._cmd_syntax}:SCALe")

    @property
    def position(self) -> DisplayWaveview1ZoomZoom1VerticalPosition:
        r"""Return the ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition`` command.

        Description:
            - This command sets or queries the vertical position of the specified zoom in the
              specified Waveform View. It is freely movable within the confines of the acquired
              waveform. It is measured from the top to bottom of the acquisition window. The top of
              the zoom window is -5 \* vertical zoom factor. The bottom of the zoom window is +5 \*
              the vertical zoom factor. For a zoom of 5x, the position ranges from -25 to 25.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition <NR3>
            - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition?
            ```

        Info:
            - ``NR3`` is the vertical position of the specified zoom in the specified Waveform View.
              It is freely movable within the confines of the acquired waveform. The top of the zoom
              window is -5 \\* vertical zoom factor. The bottom of the zoom window is +5 \\* the
              vertical zoom factor. For a vertical zoom of 5x, the position ranges from -25 to 25.
        """
        return self._position

    @property
    def scale(self) -> DisplayWaveview1ZoomZoom1VerticalScale:
        """Return the ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe`` command.

        Description:
            - This command sets or queries the vertical zoom factor of the specified zoom in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe <NR3>
            - DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe?
            ```

        Info:
            - ``<NR3>`` is the amount of vertical expansion or compression. Based on the value that
              you entered, this command uses the nearest scale factor. Setting the vertical scale to
              1 indicates unity (no zoom).
        """
        return self._scale


class DisplayWaveview1ZoomZoom1State(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:ZOOM:ZOOM1:STATe`` command.

    Description:
        - This command sets or queries the zoom display state of the specified zoom in the specified
          Waveform View. This command is equivalent to pushing the zoom button on the front panel.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:ZOOM:ZOOM1:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:ZOOM:ZOOM1:STATe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:STATe value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:ZOOM:ZOOM1:STATe {ON|OFF|<NR1>}
        - DISplay:WAVEView1:ZOOM:ZOOM1:STATe?
        ```

    Info:
        - ``ON`` turns the specified zoom on.
        - ``OFF`` turns specified zoom off.
        - ``<NR1>`` = 0 disables the specified zoom; any other value enables the specified zoom.
    """


class DisplayWaveview1ZoomZoom1HorizontalWinscale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe`` command.

    Description:
        - This command sets or queries the overview window horizontal scale in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe <NR3>
        - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe?
        ```

    Info:
        - ``<NR3>`` is the horizontal scale of the zoom window.
    """


class DisplayWaveview1ZoomZoom1HorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe`` command.

    Description:
        - This command sets or queries the horizontal zoom factor of the specified zoom in the
          specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe <NR3>
        - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe?
        ```

    Info:
        - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-4 increments of
          the specified zoom in the specified Waveform View.
    """


class DisplayWaveview1ZoomZoom1HorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition`` command.

    Description:
        - Sets or queries the horizontal zoom position (of the specified zoom in the specified
          Waveform View) of the zoomed waveform or zoom waveform in the display, around which the
          zoom waveform displays. It is freely movable around the acquisition settings (horizontal
          span). An acquired waveform or reference could extend off screen. The valid zoom area does
          not care about the waveform itself, only the user setting for acquisition. For example, if
          horizontal scale is set to 1 second, position to 50, then the acquisition area will go
          from -5 s to +5 s. Zoom window 0 will focus on -5 s and zoom area 100 will focus on +5 s.
          If the instrument is stopped and the scale changed to 0.5 s, there will be data off the
          ends of the display. However, 0% zoom will put the user focus on -2.5 s, the lower bound
          of the acquisition span.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition <NR3>
        - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to the
          left of screen center, when the zoom factor is 2× or greater.
    """


class DisplayWaveview1ZoomZoom1Horizontal(SCPICmdRead):
    """The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.position``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition`` command.
        - ``.scale``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe`` command.
        - ``.winscale``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = DisplayWaveview1ZoomZoom1HorizontalPosition(
            device, f"{self._cmd_syntax}:POSition"
        )
        self._scale = DisplayWaveview1ZoomZoom1HorizontalScale(device, f"{self._cmd_syntax}:SCALe")
        self._winscale = DisplayWaveview1ZoomZoom1HorizontalWinscale(
            device, f"{self._cmd_syntax}:WINSCALe"
        )

    @property
    def position(self) -> DisplayWaveview1ZoomZoom1HorizontalPosition:
        """Return the ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition`` command.

        Description:
            - Sets or queries the horizontal zoom position (of the specified zoom in the specified
              Waveform View) of the zoomed waveform or zoom waveform in the display, around which
              the zoom waveform displays. It is freely movable around the acquisition settings
              (horizontal span). An acquired waveform or reference could extend off screen. The
              valid zoom area does not care about the waveform itself, only the user setting for
              acquisition. For example, if horizontal scale is set to 1 second, position to 50, then
              the acquisition area will go from -5 s to +5 s. Zoom window 0 will focus on -5 s and
              zoom area 100 will focus on +5 s. If the instrument is stopped and the scale changed
              to 0.5 s, there will be data off the ends of the display. However, 0% zoom will put
              the user focus on -2.5 s, the lower bound of the acquisition span.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition <NR3>
            - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is a value from 0 to 100.00 and is the percent of the waveform that is to
              the left of screen center, when the zoom factor is 2× or greater.
        """
        return self._position

    @property
    def scale(self) -> DisplayWaveview1ZoomZoom1HorizontalScale:
        """Return the ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe`` command.

        Description:
            - This command sets or queries the horizontal zoom factor of the specified zoom in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe <NR3>
            - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe?
            ```

        Info:
            - ``<NR3>`` is the amount of expansion in the horizontal direction in 1-2-4 increments
              of the specified zoom in the specified Waveform View.
        """
        return self._scale

    @property
    def winscale(self) -> DisplayWaveview1ZoomZoom1HorizontalWinscale:
        """Return the ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe`` command.

        Description:
            - This command sets or queries the overview window horizontal scale in the specified
              Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe <NR3>
            - DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe?
            ```

        Info:
            - ``<NR3>`` is the horizontal scale of the zoom window.
        """
        return self._winscale


class DisplayWaveview1ZoomZoom1(SCPICmdRead):
    """The ``DISplay:WAVEView1:ZOOM:ZOOM1`` command.

    Description:
        - This query returns the zoom parameters of the specified zoom in the specified Waveform
          View. <x> must be 1.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:ZOOM:ZOOM1?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:ZOOM:ZOOM1?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:ZOOM:ZOOM1?
        ```

    Properties:
        - ``.horizontal``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal`` command tree.
        - ``.state``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:STATe`` command.
        - ``.vertical``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = DisplayWaveview1ZoomZoom1Horizontal(
            device, f"{self._cmd_syntax}:HORizontal"
        )
        self._state = DisplayWaveview1ZoomZoom1State(device, f"{self._cmd_syntax}:STATe")
        self._vertical = DisplayWaveview1ZoomZoom1Vertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def horizontal(self) -> DisplayWaveview1ZoomZoom1Horizontal:
        """Return the ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:POSition`` command.
            - ``.scale``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:SCALe`` command.
            - ``.winscale``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal:WINSCALe`` command.
        """
        return self._horizontal

    @property
    def state(self) -> DisplayWaveview1ZoomZoom1State:
        """Return the ``DISplay:WAVEView1:ZOOM:ZOOM1:STATe`` command.

        Description:
            - This command sets or queries the zoom display state of the specified zoom in the
              specified Waveform View. This command is equivalent to pushing the zoom button on the
              front panel.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:ZOOM:ZOOM1:STATe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:STATe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:STATe value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:ZOOM:ZOOM1:STATe {ON|OFF|<NR1>}
            - DISplay:WAVEView1:ZOOM:ZOOM1:STATe?
            ```

        Info:
            - ``ON`` turns the specified zoom on.
            - ``OFF`` turns specified zoom off.
            - ``<NR1>`` = 0 disables the specified zoom; any other value enables the specified zoom.
        """
        return self._state

    @property
    def vertical(self) -> DisplayWaveview1ZoomZoom1Vertical:
        """Return the ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:POSition`` command.
            - ``.scale``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical:SCALe`` command.
        """
        return self._vertical


class DisplayWaveview1Zoom(SCPICmdRead):
    """The ``DISplay:WAVEView1:ZOOM`` command.

    Description:
        - This query returns the zoom parameters of the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:ZOOM?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:ZOOM?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:ZOOM?
        ```

    Properties:
        - ``.zoom1``: The ``DISplay:WAVEView1:ZOOM:ZOOM1`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._zoom1 = DisplayWaveview1ZoomZoom1(device, f"{self._cmd_syntax}:ZOOM1")

    @property
    def zoom1(self) -> DisplayWaveview1ZoomZoom1:
        """Return the ``DISplay:WAVEView1:ZOOM:ZOOM1`` command.

        Description:
            - This query returns the zoom parameters of the specified zoom in the specified Waveform
              View. <x> must be 1.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:ZOOM:ZOOM1?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:ZOOM:ZOOM1?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:ZOOM:ZOOM1?
            ```

        Sub-properties:
            - ``.horizontal``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:HORizontal`` command tree.
            - ``.state``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:STATe`` command.
            - ``.vertical``: The ``DISplay:WAVEView1:ZOOM:ZOOM1:VERTical`` command tree.
        """
        return self._zoom1


class DisplayWaveview1Viewstyle(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:VIEWStyle`` command.

    Description:
        - The command sets or queries the waveform layout style used by the display.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:VIEWStyle?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:VIEWStyle?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:WAVEView1:VIEWStyle value``
          command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:VIEWStyle {OVErlay|STAcked}
        - DISplay:WAVEView1:VIEWStyle?
        ```

    Info:
        - ``OVErlay`` specifies that the display view style used by the specified Waveform View is
          overlay.
        - ``STAcked`` specifies that the display view style used by the specified Waveform View is
          stacked.
    """


class DisplayWaveview1Style(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:STYle`` command.

    Description:
        - This command sets or queries how the waveforms are displayed for analysis mode.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:STYle?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:STYle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:WAVEView1:STYle value``
          command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:STYle {VECtors|DOTsonly}
        - DISplay:WAVEView1:STYle?
        ```

    Info:
        - ``DOTs`` displays individual data points. New points immediately replace old ones.
        - ``VECtors`` connects adjacent data points. New points immediately replace old ones.
    """


class DisplayWaveview1RefItemDallFrame(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:REF<x>_DALL:FRAMe`` command.

    Description:
        - This command sets or returns the selected frame of the specified digital ref. Each ref has
          a unique selected frame.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF<x>_DALL:FRAMe?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:REF<x>_DALL:FRAMe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:REF<x>_DALL:FRAMe value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:REF<x>_DALL:FRAMe <NR1>
        - DISplay:WAVEView1:REF<x>_DALL:FRAMe?
        ```

    Info:
        - ``<NR1>`` is the selected frame of the specified digital ref.
    """


class DisplayWaveview1RefItemDall(SCPICmdRead):
    """The ``DISplay:WAVEView1:REF<x>_DALL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF<x>_DALL?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:REF<x>_DALL?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frame``: The ``DISplay:WAVEView1:REF<x>_DALL:FRAMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frame = DisplayWaveview1RefItemDallFrame(device, f"{self._cmd_syntax}:FRAMe")

    @property
    def frame(self) -> DisplayWaveview1RefItemDallFrame:
        """Return the ``DISplay:WAVEView1:REF<x>_DALL:FRAMe`` command.

        Description:
            - This command sets or returns the selected frame of the specified digital ref. Each ref
              has a unique selected frame.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF<x>_DALL:FRAMe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:REF<x>_DALL:FRAMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:REF<x>_DALL:FRAMe value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:REF<x>_DALL:FRAMe <NR1>
            - DISplay:WAVEView1:REF<x>_DALL:FRAMe?
            ```

        Info:
            - ``<NR1>`` is the selected frame of the specified digital ref.
        """
        return self._frame


class DisplayWaveview1RefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:WAVEView1:REF<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:REF<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dall``: The ``DISplay:WAVEView1:REF<x>_DALL`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dall = DisplayWaveview1RefItemDall(device, f"{self._cmd_syntax}_DALL")

    @property
    def dall(self) -> DisplayWaveview1RefItemDall:
        """Return the ``DISplay:WAVEView1:REF<x>_DALL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF<x>_DALL?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:REF<x>_DALL?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frame``: The ``DISplay:WAVEView1:REF<x>_DALL:FRAMe`` command.
        """
        return self._dall


class DisplayWaveview1RefRefItemVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle`` command.

    Description:
        - This command sets or queries the vertical scale of the specified reference in volts per
          div within the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle <NR3>
        - DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is the vertical scale of the specified reference waveform.
    """


class DisplayWaveview1RefRefItemVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:REF:REF<x>:VERTical:POSition`` command.

    Description:
        - This command sets or queries the vertical position in divisions of the specified reference
          in the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:REF:REF<x>:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:REF:REF<x>:VERTical:POSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:REF:REF<x>:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:REF:REF<x>:VERTical:POSition <NR3>
        - DISplay:WAVEView1:REF:REF<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position in divisions.
    """


class DisplayWaveview1RefRefItemVertical(SCPICmdRead):
    """The ``DISplay:WAVEView1:REF:REF<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF:REF<x>:VERTical?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:REF:REF<x>:VERTical?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.position``: The ``DISplay:WAVEView1:REF:REF<x>:VERTical:POSition`` command.
        - ``.scale``: The ``DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = DisplayWaveview1RefRefItemVerticalPosition(
            device, f"{self._cmd_syntax}:POSition"
        )
        self._scale = DisplayWaveview1RefRefItemVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> DisplayWaveview1RefRefItemVerticalPosition:
        """Return the ``DISplay:WAVEView1:REF:REF<x>:VERTical:POSition`` command.

        Description:
            - This command sets or queries the vertical position in divisions of the specified
              reference in the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:REF:REF<x>:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:REF:REF<x>:VERTical:POSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:REF:REF<x>:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:REF:REF<x>:VERTical:POSition <NR3>
            - DISplay:WAVEView1:REF:REF<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position in divisions.
        """
        return self._position

    @property
    def scale(self) -> DisplayWaveview1RefRefItemVerticalScale:
        """Return the ``DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle`` command.

        Description:
            - This command sets or queries the vertical scale of the specified reference in volts
              per div within the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle <NR3>
            - DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is the vertical scale of the specified reference waveform.
        """
        return self._scale


class DisplayWaveview1RefRefItemState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:REF:REF<x>:STATE`` command.

    Description:
        - This command sets or queries the state of the specified reference waveform in the
          specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF:REF<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:REF:REF<x>:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:REF:REF<x>:STATE value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:REF:REF<x>:STATE {ON|OFF|<NR1>}
        - DISplay:WAVEView1:REF:REF<x>:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the specified reference in the specified Waveform View; any other
          value turns this feature on.
        - ``OFF`` disables the specified reference in the specified Waveform View.
        - ``ON`` enables the specified reference in the specified Waveform View.
    """


class DisplayWaveview1RefRefItemFrame(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:REF:REF<x>:FRAMe`` command.

    Description:
        - This command sets or returns the selected frame of the specified analog ref. Each ref has
          a unique selected frame.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF:REF<x>:FRAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:REF:REF<x>:FRAMe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:REF:REF<x>:FRAMe value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:REF:REF<x>:FRAMe <NR1>
        - DISplay:WAVEView1:REF:REF<x>:FRAMe?
        ```

    Info:
        - ``<NR1>`` is the selected frame of the specified analog ref.
    """


class DisplayWaveview1RefRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:WAVEView1:REF:REF<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:REF:REF<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DISplay:WAVEView1:REF:REF<x>:STATE`` command.
        - ``.vertical``: The ``DISplay:WAVEView1:REF:REF<x>:VERTical`` command tree.
        - ``.frame``: The ``DISplay:WAVEView1:REF:REF<x>:FRAMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayWaveview1RefRefItemState(device, f"{self._cmd_syntax}:STATE")
        self._vertical = DisplayWaveview1RefRefItemVertical(device, f"{self._cmd_syntax}:VERTical")
        self._frame = DisplayWaveview1RefRefItemFrame(device, f"{self._cmd_syntax}:FRAMe")

    @property
    def state(self) -> DisplayWaveview1RefRefItemState:
        """Return the ``DISplay:WAVEView1:REF:REF<x>:STATE`` command.

        Description:
            - This command sets or queries the state of the specified reference waveform in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF:REF<x>:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:REF:REF<x>:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:REF:REF<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:REF:REF<x>:STATE {ON|OFF|<NR1>}
            - DISplay:WAVEView1:REF:REF<x>:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the specified reference in the specified Waveform View; any
              other value turns this feature on.
            - ``OFF`` disables the specified reference in the specified Waveform View.
            - ``ON`` enables the specified reference in the specified Waveform View.
        """
        return self._state

    @property
    def vertical(self) -> DisplayWaveview1RefRefItemVertical:
        """Return the ``DISplay:WAVEView1:REF:REF<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF:REF<x>:VERTical?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:REF:REF<x>:VERTical?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``DISplay:WAVEView1:REF:REF<x>:VERTical:POSition`` command.
            - ``.scale``: The ``DISplay:WAVEView1:REF:REF<x>:VERTical:SCAle`` command.
        """
        return self._vertical

    @property
    def frame(self) -> DisplayWaveview1RefRefItemFrame:
        """Return the ``DISplay:WAVEView1:REF:REF<x>:FRAMe`` command.

        Description:
            - This command sets or returns the selected frame of the specified analog ref. Each ref
              has a unique selected frame.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF:REF<x>:FRAMe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:REF:REF<x>:FRAMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:REF:REF<x>:FRAMe value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:REF:REF<x>:FRAMe <NR1>
            - DISplay:WAVEView1:REF:REF<x>:FRAMe?
            ```

        Info:
            - ``<NR1>`` is the selected frame of the specified analog ref.
        """
        return self._frame


class DisplayWaveview1Ref(SCPICmdRead):
    """The ``DISplay:WAVEView1:REF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:REF?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ref``: The ``DISplay:WAVEView1:REF:REF<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ref: Dict[int, DisplayWaveview1RefRefItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayWaveview1RefRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def ref(self) -> Dict[int, DisplayWaveview1RefRefItem]:
        """Return the ``DISplay:WAVEView1:REF:REF<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:REF:REF<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DISplay:WAVEView1:REF:REF<x>:STATE`` command.
            - ``.vertical``: The ``DISplay:WAVEView1:REF:REF<x>:VERTical`` command tree.
            - ``.frame``: The ``DISplay:WAVEView1:REF:REF<x>:FRAMe`` command.
        """
        return self._ref


class DisplayWaveview1MathMathItemVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle`` command.

    Description:
        - Sets or queries the vertical scale of the specified math in volts per division within the
          specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle <NR3>
        - DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is the vertical scale of the specified math waveform.
    """


class DisplayWaveview1MathMathItemVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition`` command.

    Description:
        - This command sets or queries the vertical position in divisions of the specified math
          waveform in the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition <NR3>
        - DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position in divisions of the specified math waveform.
    """


class DisplayWaveview1MathMathItemVertical(SCPICmdRead):
    """The ``DISplay:WAVEView1:MATH:MATH<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:MATH:MATH<x>:VERTical?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:MATH:MATH<x>:VERTical?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.position``: The ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition`` command.
        - ``.scale``: The ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = DisplayWaveview1MathMathItemVerticalPosition(
            device, f"{self._cmd_syntax}:POSition"
        )
        self._scale = DisplayWaveview1MathMathItemVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> DisplayWaveview1MathMathItemVerticalPosition:
        """Return the ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition`` command.

        Description:
            - This command sets or queries the vertical position in divisions of the specified math
              waveform in the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition <NR3>
            - DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position in divisions of the specified math waveform.
        """
        return self._position

    @property
    def scale(self) -> DisplayWaveview1MathMathItemVerticalScale:
        """Return the ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle`` command.

        Description:
            - Sets or queries the vertical scale of the specified math in volts per division within
              the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle <NR3>
            - DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is the vertical scale of the specified math waveform.
        """
        return self._scale


class DisplayWaveview1MathMathItemState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:MATH:MATH<x>:STATE`` command.

    Description:
        - This command sets or queries the state of the specified math waveform in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:MATH:MATH<x>:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:MATH:MATH<x>:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:MATH:MATH<x>:STATE value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:MATH:MATH<x>:STATE {ON|OFF|<NR1>}
        - DISplay:WAVEView1:MATH:MATH<x>:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the specified math in the specified Waveform View; any other value
          turns this feature on.
        - ``OFF`` disables the specified math in the specified Waveform View.
        - ``ON`` enables the specified math in the specified Waveform View.
    """


class DisplayWaveview1MathMathItemAutoscale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:MATH:MATH<x>:AUTOScale`` command.

    Description:
        - This command sets or queries whether the specified math gets auto-scaled when the math
          equation changes within the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:MATH:MATH<x>:AUTOScale?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:MATH:MATH<x>:AUTOScale?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:MATH:MATH<x>:AUTOScale value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:MATH:MATH<x>:AUTOScale {ON|OFF|<NR1>}
        - DISplay:WAVEView1:MATH:MATH<x>:AUTOScale?
        ```

    Info:
        - ``<NR1>`` = 0 disables the autoscaling the math in the specified Waveform View; any other
          value turns this feature on.
        - ``OFF`` disables the autoscaling the math in the specified Waveform View.
        - ``ON`` enables the autoscaling the math in the specified Waveform View.
    """


class DisplayWaveview1MathMathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:WAVEView1:MATH:MATH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:MATH:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:MATH:MATH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autoscale``: The ``DISplay:WAVEView1:MATH:MATH<x>:AUTOScale`` command.
        - ``.state``: The ``DISplay:WAVEView1:MATH:MATH<x>:STATE`` command.
        - ``.vertical``: The ``DISplay:WAVEView1:MATH:MATH<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoscale = DisplayWaveview1MathMathItemAutoscale(
            device, f"{self._cmd_syntax}:AUTOScale"
        )
        self._state = DisplayWaveview1MathMathItemState(device, f"{self._cmd_syntax}:STATE")
        self._vertical = DisplayWaveview1MathMathItemVertical(
            device, f"{self._cmd_syntax}:VERTical"
        )

    @property
    def autoscale(self) -> DisplayWaveview1MathMathItemAutoscale:
        """Return the ``DISplay:WAVEView1:MATH:MATH<x>:AUTOScale`` command.

        Description:
            - This command sets or queries whether the specified math gets auto-scaled when the math
              equation changes within the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:AUTOScale?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:AUTOScale?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:AUTOScale value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:MATH:MATH<x>:AUTOScale {ON|OFF|<NR1>}
            - DISplay:WAVEView1:MATH:MATH<x>:AUTOScale?
            ```

        Info:
            - ``<NR1>`` = 0 disables the autoscaling the math in the specified Waveform View; any
              other value turns this feature on.
            - ``OFF`` disables the autoscaling the math in the specified Waveform View.
            - ``ON`` enables the autoscaling the math in the specified Waveform View.
        """
        return self._autoscale

    @property
    def state(self) -> DisplayWaveview1MathMathItemState:
        """Return the ``DISplay:WAVEView1:MATH:MATH<x>:STATE`` command.

        Description:
            - This command sets or queries the state of the specified math waveform in the specified
              Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:MATH:MATH<x>:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:MATH:MATH<x>:STATE {ON|OFF|<NR1>}
            - DISplay:WAVEView1:MATH:MATH<x>:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the specified math in the specified Waveform View; any other
              value turns this feature on.
            - ``OFF`` disables the specified math in the specified Waveform View.
            - ``ON`` enables the specified math in the specified Waveform View.
        """
        return self._state

    @property
    def vertical(self) -> DisplayWaveview1MathMathItemVertical:
        """Return the ``DISplay:WAVEView1:MATH:MATH<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:MATH:MATH<x>:VERTical?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:POSition`` command.
            - ``.scale``: The ``DISplay:WAVEView1:MATH:MATH<x>:VERTical:SCAle`` command.
        """
        return self._vertical


class DisplayWaveview1Math(SCPICmdRead):
    """The ``DISplay:WAVEView1:MATH`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:MATH?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:MATH?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.math``: The ``DISplay:WAVEView1:MATH:MATH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._math: Dict[int, DisplayWaveview1MathMathItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayWaveview1MathMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )

    @property
    def math(self) -> Dict[int, DisplayWaveview1MathMathItem]:
        """Return the ``DISplay:WAVEView1:MATH:MATH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:MATH:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:MATH:MATH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autoscale``: The ``DISplay:WAVEView1:MATH:MATH<x>:AUTOScale`` command.
            - ``.state``: The ``DISplay:WAVEView1:MATH:MATH<x>:STATE`` command.
            - ``.vertical``: The ``DISplay:WAVEView1:MATH:MATH<x>:VERTical`` command tree.
        """
        return self._math


class DisplayWaveview1IntensityWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:INTENSITy:WAVEform`` command.

    Description:
        - This command sets or queries the waveform saturation level.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:INTENSITy:WAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:INTENSITy:WAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:INTENSITy:WAVEform value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:INTENSITy:WAVEform <NR2>
        - DISplay:WAVEView1:INTENSITy:WAVEform?
        ```

    Info:
        - ``<NR2>`` is the waveform saturation level.
    """


class DisplayWaveview1IntensityGraticule(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:INTENSITy:GRATicule`` command.

    Description:
        - This command sets or queries the graticule saturation level.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:INTENSITy:GRATicule?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:INTENSITy:GRATicule?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:INTENSITy:GRATicule value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:INTENSITy:GRATicule <NR2>
        - DISplay:WAVEView1:INTENSITy:GRATicule?
        ```

    Info:
        - ``<NR2>`` is the graticule saturation level.
    """


class DisplayWaveview1Intensity(SCPICmdRead):
    """The ``DISplay:WAVEView1:INTENSITy`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:INTENSITy?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:INTENSITy?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.graticule``: The ``DISplay:WAVEView1:INTENSITy:GRATicule`` command.
        - ``.waveform``: The ``DISplay:WAVEView1:INTENSITy:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._graticule = DisplayWaveview1IntensityGraticule(
            device, f"{self._cmd_syntax}:GRATicule"
        )
        self._waveform = DisplayWaveview1IntensityWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def graticule(self) -> DisplayWaveview1IntensityGraticule:
        """Return the ``DISplay:WAVEView1:INTENSITy:GRATicule`` command.

        Description:
            - This command sets or queries the graticule saturation level.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:INTENSITy:GRATicule?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:INTENSITy:GRATicule?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:INTENSITy:GRATicule value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:INTENSITy:GRATicule <NR2>
            - DISplay:WAVEView1:INTENSITy:GRATicule?
            ```

        Info:
            - ``<NR2>`` is the graticule saturation level.
        """
        return self._graticule

    @property
    def waveform(self) -> DisplayWaveview1IntensityWaveform:
        """Return the ``DISplay:WAVEView1:INTENSITy:WAVEform`` command.

        Description:
            - This command sets or queries the waveform saturation level.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:INTENSITy:WAVEform?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:INTENSITy:WAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:INTENSITy:WAVEform value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:INTENSITy:WAVEform <NR2>
            - DISplay:WAVEView1:INTENSITy:WAVEform?
            ```

        Info:
            - ``<NR2>`` is the waveform saturation level.
        """
        return self._waveform


class DisplayWaveview1Graticule(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:GRAticule`` command.

    Description:
        - This command selects or queries the type of graticule that is displayed.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:GRAticule?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:GRAticule?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:WAVEView1:GRAticule value``
          command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:GRAticule {GRId|TIMe|FULl|NONe}
        - DISplay:WAVEView1:GRAticule?
        ```

    Info:
        - ``GRId`` specifies a frame and grid only.
        - ``TIMe`` specifies a time graticule only.
        - ``FULl`` specifies a frame, a grid and cross hairs.
        - ``NONe`` specified no graticule.
    """


class DisplayWaveview1Filter(SCPICmdWrite):
    """The ``DISplay:WAVEView1:FILTer`` command.

    Description:
        - This command sets or queries the type of interpolation filter for the display.

    Usage:
        - Using the ``.write(value)`` method will send the ``DISplay:WAVEView1:FILTer value``
          command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:FILTer {SINX|LINear}
        ```

    Info:
        - ``LINEAr`` specifies linear interpolation, where acquired points are connected with
          straight lines.
        - ``SINX`` specifies sin(x)/x interpolation, where acquired points are fit to a curve.
    """


class DisplayWaveview1DchItemDallVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition`` command.

    Description:
        - Sets or queries the vertical position of the specified channel in the specified Waveform
          View in divisions. 0.0 divisions is center, 5.0 top of the window, and -5.0 the bottom of
          the window. 1 is the specified Waveform View and must be WAVEView1. DCH<x> is the
          specified digital channel and must be 1.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition <NR3>
        - DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position in divisions. 0.0 divisions is center, 5.0 top of the
          window, and -5.0 the bottom of the window.
    """


class DisplayWaveview1DchItemDallVertical(SCPICmdRead):
    """The ``DISplay:WAVEView1:DCH<x>_DALL:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:DCH<x>_DALL:VERTical?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:DCH<x>_DALL:VERTical?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.position``: The ``DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = DisplayWaveview1DchItemDallVerticalPosition(
            device, f"{self._cmd_syntax}:POSition"
        )

    @property
    def position(self) -> DisplayWaveview1DchItemDallVerticalPosition:
        """Return the ``DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition`` command.

        Description:
            - Sets or queries the vertical position of the specified channel in the specified
              Waveform View in divisions. 0.0 divisions is center, 5.0 top of the window, and -5.0
              the bottom of the window. 1 is the specified Waveform View and must be WAVEView1.
              DCH<x> is the specified digital channel and must be 1.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition <NR3>
            - DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position in divisions. 0.0 divisions is center, 5.0 top of
              the window, and -5.0 the bottom of the window.
        """
        return self._position


class DisplayWaveview1DchItemDallDigorder(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:DCH<x>_DALL:DIGORDER`` command.

    Description:
        - This command sets or queries the order of the digital channels. 1 is the specified
          Waveform View and must be WAVEView1.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:DCH<x>_DALL:DIGORDER?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:DCH<x>_DALL:DIGORDER?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:DCH<x>_DALL:DIGORDER value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:DCH<x>_DALL:DIGORDER <QString>
        - DISplay:WAVEView1:DCH<x>_DALL:DIGORDER?
        ```

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported digital channel value is 1.
        - ``<QString>`` specifies the ascending or descending order , enclosed in quotes.
    """

    _WRAP_ARG_WITH_QUOTES = True


class DisplayWaveview1DchItemDall(SCPICmdRead):
    """The ``DISplay:WAVEView1:DCH<x>_DALL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:DCH<x>_DALL?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:DCH<x>_DALL?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported digital channel value is 1.

    Properties:
        - ``.digorder``: The ``DISplay:WAVEView1:DCH<x>_DALL:DIGORDER`` command.
        - ``.vertical``: The ``DISplay:WAVEView1:DCH<x>_DALL:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._digorder = DisplayWaveview1DchItemDallDigorder(device, f"{self._cmd_syntax}:DIGORDER")
        self._vertical = DisplayWaveview1DchItemDallVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def digorder(self) -> DisplayWaveview1DchItemDallDigorder:
        """Return the ``DISplay:WAVEView1:DCH<x>_DALL:DIGORDER`` command.

        Description:
            - This command sets or queries the order of the digital channels. 1 is the specified
              Waveform View and must be WAVEView1.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:DCH<x>_DALL:DIGORDER?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:DCH<x>_DALL:DIGORDER?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:DCH<x>_DALL:DIGORDER value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:DCH<x>_DALL:DIGORDER <QString>
            - DISplay:WAVEView1:DCH<x>_DALL:DIGORDER?
            ```

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported digital channel value is 1.
            - ``<QString>`` specifies the ascending or descending order , enclosed in quotes.
        """
        return self._digorder

    @property
    def vertical(self) -> DisplayWaveview1DchItemDallVertical:
        """Return the ``DISplay:WAVEView1:DCH<x>_DALL:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:DCH<x>_DALL:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:DCH<x>_DALL:VERTical?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``DISplay:WAVEView1:DCH<x>_DALL:VERTical:POSition`` command.
        """
        return self._vertical


class DisplayWaveview1DchItemDigitalBitState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:DCH<x>_D<x>:STATE`` command.

    Description:
        - This command sets or queries the display state of the specified digital channel in the
          specified waveview. 1 is the specified Waveform View and must be WAVEView1.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:DCH<x>_D<x>:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:DCH<x>_D<x>:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:DCH<x>_D<x>:STATE value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:DCH<x>_D<x>:STATE {ON|OFF|<NR1>}
        - DISplay:WAVEView1:DCH<x>_D<x>:STATE?
        ```

    Info:
        - ``DCH<x>_D<x>`` specifies the digital channel. The supported digital channel value is 1.
          The supported digital bit values are 0 to 15 and ALL (all digital bits).
        - ``<NR1>`` = 0 disables the specified channel on the specified Waveform View; any other
          value turns this feature on.
        - ``OFF`` disables the display the specified channel on the specified Waveform View.
        - ``ON`` enables the specified channel on the specified Waveform View.
    """


class DisplayWaveview1DchItemDigitalBit(ValidatedDigitalBit, SCPICmdRead):
    """The ``DISplay:WAVEView1:DCH<x>_D<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:DCH<x>_D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:DCH<x>_D<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``DCH<x>_D<x>`` specifies the digital channel. The supported digital channel value is 1.
          The supported digital bit values are 0 to 15 and ALL (all digital bits).

    Properties:
        - ``.state``: The ``DISplay:WAVEView1:DCH<x>_D<x>:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayWaveview1DchItemDigitalBitState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> DisplayWaveview1DchItemDigitalBitState:
        """Return the ``DISplay:WAVEView1:DCH<x>_D<x>:STATE`` command.

        Description:
            - This command sets or queries the display state of the specified digital channel in the
              specified waveview. 1 is the specified Waveform View and must be WAVEView1.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:DCH<x>_D<x>:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:DCH<x>_D<x>:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:DCH<x>_D<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:DCH<x>_D<x>:STATE {ON|OFF|<NR1>}
            - DISplay:WAVEView1:DCH<x>_D<x>:STATE?
            ```

        Info:
            - ``DCH<x>_D<x>`` specifies the digital channel. The supported digital channel value is
              1. The supported digital bit values are 0 to 15 and ALL (all digital bits).
            - ``<NR1>`` = 0 disables the specified channel on the specified Waveform View; any other
              value turns this feature on.
            - ``OFF`` disables the display the specified channel on the specified Waveform View.
            - ``ON`` enables the specified channel on the specified Waveform View.
        """
        return self._state


class DisplayWaveview1DchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:WAVEView1:DCH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:DCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:DCH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.d``: The ``DISplay:WAVEView1:DCH<x>_D<x>`` command tree.
        - ``.dall``: The ``DISplay:WAVEView1:DCH<x>_DALL`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, DisplayWaveview1DchItemDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: DisplayWaveview1DchItemDigitalBit(device, f"{self._cmd_syntax}_D{x}")
        )
        self._dall = DisplayWaveview1DchItemDall(device, f"{self._cmd_syntax}_DALL")

    @property
    def d(self) -> Dict[int, DisplayWaveview1DchItemDigitalBit]:
        """Return the ``DISplay:WAVEView1:DCH<x>_D<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:DCH<x>_D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:DCH<x>_D<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``DCH<x>_D<x>`` specifies the digital channel. The supported digital channel value is
              1. The supported digital bit values are 0 to 15 and ALL (all digital bits).

        Sub-properties:
            - ``.state``: The ``DISplay:WAVEView1:DCH<x>_D<x>:STATE`` command.
        """
        return self._d

    @property
    def dall(self) -> DisplayWaveview1DchItemDall:
        """Return the ``DISplay:WAVEView1:DCH<x>_DALL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:DCH<x>_DALL?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:DCH<x>_DALL?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported digital channel value is 1.

        Sub-properties:
            - ``.digorder``: The ``DISplay:WAVEView1:DCH<x>_DALL:DIGORDER`` command.
            - ``.vertical``: The ``DISplay:WAVEView1:DCH<x>_DALL:VERTical`` command tree.
        """
        return self._dall


class DisplayWaveview1CursorCursorWaveformBvposition(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition`` command.

    Description:
        - This command queries the vertical waveform value at the cursor B position in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition?
        ```

    Info:
        - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
          Waveform View.
    """


class DisplayWaveview1CursorCursorWaveformAvposition(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition`` command.

    Description:
        - This command queries the vertical waveform value at the cursor A position in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition?
        ```

    Info:
        - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
          Waveform View.
    """


class DisplayWaveview1CursorCursorWaveform(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.avposition``: The ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition`` command.
        - ``.bvposition``: The ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._avposition = DisplayWaveview1CursorCursorWaveformAvposition(
            device, f"{self._cmd_syntax}:AVPOSition"
        )
        self._bvposition = DisplayWaveview1CursorCursorWaveformBvposition(
            device, f"{self._cmd_syntax}:BVPOSition"
        )

    @property
    def avposition(self) -> DisplayWaveview1CursorCursorWaveformAvposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition`` command.

        Description:
            - This command queries the vertical waveform value at the cursor A position in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition?
            ```

        Info:
            - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
              Waveform View.
        """
        return self._avposition

    @property
    def bvposition(self) -> DisplayWaveview1CursorCursorWaveformBvposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition`` command.

        Description:
            - This command queries the vertical waveform value at the cursor B position in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition?
            ```

        Info:
            - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
              Waveform View.
        """
        return self._bvposition


class DisplayWaveview1CursorCursor1WaveformBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition`` command.

    Description:
        - This command sets or queries the horizontal cursor B position of the specified cursor in
          the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition <NR3>
        - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition?
        ```

    Info:
        - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
          Waveform View.
    """


class DisplayWaveview1CursorCursor1WaveformAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition`` command.

    Description:
        - This command sets or queries the horizontal cursor A position of the specified cursor in
          the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition <NR3>
        - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition?
        ```

    Info:
        - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
          Waveform View.
    """


class DisplayWaveview1CursorCursor1Waveform(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.aposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition`` command.
        - ``.bposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aposition = DisplayWaveview1CursorCursor1WaveformAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._bposition = DisplayWaveview1CursorCursor1WaveformBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )

    @property
    def aposition(self) -> DisplayWaveview1CursorCursor1WaveformAposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition`` command.

        Description:
            - This command sets or queries the horizontal cursor A position of the specified cursor
              in the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition <NR3>
            - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition?
            ```

        Info:
            - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
              Waveform View.
        """
        return self._aposition

    @property
    def bposition(self) -> DisplayWaveview1CursorCursor1WaveformBposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition`` command.

        Description:
            - This command sets or queries the horizontal cursor B position of the specified cursor
              in the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition <NR3>
            - DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition?
            ```

        Info:
            - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
              Waveform View.
        """
        return self._bposition


class DisplayWaveview1CursorCursor1VbarsUnits(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:UNIts`` command.

    Description:
        - This query returns cursor A vertical units of the specified cursor in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:UNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:UNIts?
        ```
    """


class DisplayWaveview1CursorCursor1VbarsDelta(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:DELTa`` command.

    Description:
        - This query sets or returns the delta T cursor readout value of the specified cursor in the
          specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:DELTa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:DELTa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:DELTa?
        ```
    """


class DisplayWaveview1CursorCursor1VbarsBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition`` command.

    Description:
        - This command sets or queries the cursor B horizontal position of the specified cursor in
          the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition <NR3>
        - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition?
        ```

    Info:
        - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
          Waveform View.
    """


class DisplayWaveview1CursorCursor1VbarsAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition`` command.

    Description:
        - This command sets or queries the cursor A horizontal position of the specified cursor in
          the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition <NR3>
        - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition?
        ```

    Info:
        - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
          Waveform View.
    """


class DisplayWaveview1CursorCursor1Vbars(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.aposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition`` command.
        - ``.bposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition`` command.
        - ``.delta``: The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:DELTa`` command.
        - ``.units``: The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aposition = DisplayWaveview1CursorCursor1VbarsAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._bposition = DisplayWaveview1CursorCursor1VbarsBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )
        self._delta = DisplayWaveview1CursorCursor1VbarsDelta(device, f"{self._cmd_syntax}:DELTa")
        self._units = DisplayWaveview1CursorCursor1VbarsUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def aposition(self) -> DisplayWaveview1CursorCursor1VbarsAposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition`` command.

        Description:
            - This command sets or queries the cursor A horizontal position of the specified cursor
              in the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition <NR3>
            - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition?
            ```

        Info:
            - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
              Waveform View.
        """
        return self._aposition

    @property
    def bposition(self) -> DisplayWaveview1CursorCursor1VbarsBposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition`` command.

        Description:
            - This command sets or queries the cursor B horizontal position of the specified cursor
              in the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition <NR3>
            - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition?
            ```

        Info:
            - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
              Waveform View.
        """
        return self._bposition

    @property
    def delta(self) -> DisplayWaveview1CursorCursor1VbarsDelta:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:DELTa`` command.

        Description:
            - This query sets or returns the delta T cursor readout value of the specified cursor in
              the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:DELTa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:DELTa?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:DELTa?
            ```
        """
        return self._delta

    @property
    def units(self) -> DisplayWaveview1CursorCursor1VbarsUnits:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:UNIts`` command.

        Description:
            - This query returns cursor A vertical units of the specified cursor in the specified
              Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:UNIts?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:VBArs:UNIts?
            ```
        """
        return self._units


class DisplayWaveview1CursorCursor1State(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:STATE`` command.

    Description:
        - This command sets or queries the visible state of the specified cursor in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:STATE value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:STATE {ON|OFF|<NR1>}
        - DISplay:WAVEView1:CURSor:CURSOR1:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the specified cursor in the specified Waveform View; any other
          value turns this feature on.
        - ``OFF`` disables the specified cursor in the specified Waveform View.
        - ``ON`` enables the specified cursor in the specified Waveform View.
    """


class DisplayWaveview1CursorCursor1Splitmode(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE`` command.

    Description:
        - This command sets or queries whether both cursors have the same or different sources.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE {SAME|SPLIT}
        - DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE?
        ```

    Info:
        - ``SAME`` specifies both cursors have the same source.
        - ``SPLIT`` specifies the cursors have different sources.
    """


class DisplayWaveview1CursorCursor1ScreenByposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition`` command.

    Description:
        - This command sets or queries the vertical cursor B position of the specified cursor in the
          specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition <NR3>
        - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition?
        ```

    Info:
        - ``<NR3>`` the vertical cursor B position of the specified cursor in the specified Waveform
          View.
    """


class DisplayWaveview1CursorCursor1ScreenBxposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition`` command.

    Description:
        - Sets or queries the horizontal cursor B position of the specified cursor in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition <NR3>
        - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition?
        ```

    Info:
        - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
          Waveform View.
    """


class DisplayWaveview1CursorCursor1ScreenAyposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition`` command.

    Description:
        - This command sets or queries the vertical cursor A position of the specified cursor in the
          specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition <NR3>
        - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition?
        ```

    Info:
        - ``<NR3>`` the vertical cursor A position of the specified cursor in the specified Waveform
          View.
    """


class DisplayWaveview1CursorCursor1ScreenAxposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition`` command.

    Description:
        - Sets or queries the horizontal cursor A position of the specified cursor in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition <NR3>
        - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition?
        ```

    Info:
        - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
          Waveform View.
    """


class DisplayWaveview1CursorCursor1Screen(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.axposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition`` command.
        - ``.ayposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition`` command.
        - ``.bxposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition`` command.
        - ``.byposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._axposition = DisplayWaveview1CursorCursor1ScreenAxposition(
            device, f"{self._cmd_syntax}:AXPOSition"
        )
        self._ayposition = DisplayWaveview1CursorCursor1ScreenAyposition(
            device, f"{self._cmd_syntax}:AYPOSition"
        )
        self._bxposition = DisplayWaveview1CursorCursor1ScreenBxposition(
            device, f"{self._cmd_syntax}:BXPOSition"
        )
        self._byposition = DisplayWaveview1CursorCursor1ScreenByposition(
            device, f"{self._cmd_syntax}:BYPOSition"
        )

    @property
    def axposition(self) -> DisplayWaveview1CursorCursor1ScreenAxposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition`` command.

        Description:
            - Sets or queries the horizontal cursor A position of the specified cursor in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition <NR3>
            - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition?
            ```

        Info:
            - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
              Waveform View.
        """
        return self._axposition

    @property
    def ayposition(self) -> DisplayWaveview1CursorCursor1ScreenAyposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition`` command.

        Description:
            - This command sets or queries the vertical cursor A position of the specified cursor in
              the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition <NR3>
            - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition?
            ```

        Info:
            - ``<NR3>`` the vertical cursor A position of the specified cursor in the specified
              Waveform View.
        """
        return self._ayposition

    @property
    def bxposition(self) -> DisplayWaveview1CursorCursor1ScreenBxposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition`` command.

        Description:
            - Sets or queries the horizontal cursor B position of the specified cursor in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition <NR3>
            - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition?
            ```

        Info:
            - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
              Waveform View.
        """
        return self._bxposition

    @property
    def byposition(self) -> DisplayWaveview1CursorCursor1ScreenByposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition`` command.

        Description:
            - This command sets or queries the vertical cursor B position of the specified cursor in
              the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition <NR3>
            - DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition?
            ```

        Info:
            - ``<NR3>`` the vertical cursor B position of the specified cursor in the specified
              Waveform View.
        """
        return self._byposition


class DisplayWaveview1CursorCursor1Oneoverdeltatvalue(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:ONEOVERDELTATVALUE`` command.

    Description:
        - This query returns the one over delta T cursor readout value of the specified cursor in
          the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:ONEOVERDELTATVALUE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:ONEOVERDELTATVALUE?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:ONEOVERDELTATVALUE?
        ```
    """


class DisplayWaveview1CursorCursor1Mode(SCPICmdWrite):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:MODe`` command.

    Description:
        - Sets or queries the cursor tracking mode of the specified cursor in the specified Waveform
          View.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:MODe value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:MODe {INDEPENDENT|TRACK}
        ```

    Info:
        - ``TRACK`` ties the navigational functionality of the two cursors together. For cursor 1
          adjustments, this ties the movement of the two cursors together; however, cursor 2
          continues to move independently of cursor 1.
        - ``INDEPENDENT`` allows independent adjustment of the two cursors.
    """


class DisplayWaveview1CursorCursor1HbarsDelta(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:DELTa`` command.

    Description:
        - This command queries the delta V cursor readout value of the specified cursor in the
          specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:DELTa?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:DELTa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:DELTa?
        ```
    """


class DisplayWaveview1CursorCursor1HbarsBunits(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BUNIts`` command.

    Description:
        - This command queries the cursor B vertical units of the specified cursor in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BUNIts?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BUNIts?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BUNIts?
        ```
    """


class DisplayWaveview1CursorCursor1HbarsBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition`` command.

    Description:
        - Sets or queries the HBARs vertical B position of the specified cursor in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition <NR3>
        - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition?
        ```

    Info:
        - ``<NR3>`` is the vertical cursor B position of the specified cursor in the specified
          Waveform View.
    """


class DisplayWaveview1CursorCursor1HbarsAunits(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:AUNIts`` command.

    Description:
        - This command queries the cursor A vertical units of the specified cursor in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:AUNIts?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:AUNIts?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:AUNIts?
        ```

    Info:
        - ``<QString>`` is the cursor A vertical units of the specified cursor in the specified
          Waveform View.
    """


class DisplayWaveview1CursorCursor1HbarsAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition`` command.

    Description:
        - Sets or queries the HBARs vertical A position of the specified cursor in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition <NR3>
        - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition?
        ```

    Info:
        - ``<NR3>`` is the vertical cursor A position of the specified cursor in the specified
          Waveform View. 0.0 divisions is center, 5.0 top of the waveview, and -5.0 the bottom of
          the waveview.
    """


class DisplayWaveview1CursorCursor1Hbars(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.aposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition`` command.
        - ``.aunits``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:AUNIts`` command.
        - ``.bposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition`` command.
        - ``.bunits``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BUNIts`` command.
        - ``.delta``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:DELTa`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aposition = DisplayWaveview1CursorCursor1HbarsAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._aunits = DisplayWaveview1CursorCursor1HbarsAunits(
            device, f"{self._cmd_syntax}:AUNIts"
        )
        self._bposition = DisplayWaveview1CursorCursor1HbarsBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )
        self._bunits = DisplayWaveview1CursorCursor1HbarsBunits(
            device, f"{self._cmd_syntax}:BUNIts"
        )
        self._delta = DisplayWaveview1CursorCursor1HbarsDelta(device, f"{self._cmd_syntax}:DELTa")

    @property
    def aposition(self) -> DisplayWaveview1CursorCursor1HbarsAposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition`` command.

        Description:
            - Sets or queries the HBARs vertical A position of the specified cursor in the specified
              Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition <NR3>
            - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition?
            ```

        Info:
            - ``<NR3>`` is the vertical cursor A position of the specified cursor in the specified
              Waveform View. 0.0 divisions is center, 5.0 top of the waveview, and -5.0 the bottom
              of the waveview.
        """
        return self._aposition

    @property
    def aunits(self) -> DisplayWaveview1CursorCursor1HbarsAunits:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:AUNIts`` command.

        Description:
            - This command queries the cursor A vertical units of the specified cursor in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:AUNIts?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:AUNIts?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:AUNIts?
            ```

        Info:
            - ``<QString>`` is the cursor A vertical units of the specified cursor in the specified
              Waveform View.
        """
        return self._aunits

    @property
    def bposition(self) -> DisplayWaveview1CursorCursor1HbarsBposition:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition`` command.

        Description:
            - Sets or queries the HBARs vertical B position of the specified cursor in the specified
              Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition <NR3>
            - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition?
            ```

        Info:
            - ``<NR3>`` is the vertical cursor B position of the specified cursor in the specified
              Waveform View.
        """
        return self._bposition

    @property
    def bunits(self) -> DisplayWaveview1CursorCursor1HbarsBunits:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BUNIts`` command.

        Description:
            - This command queries the cursor B vertical units of the specified cursor in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BUNIts?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BUNIts?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BUNIts?
            ```
        """
        return self._bunits

    @property
    def delta(self) -> DisplayWaveview1CursorCursor1HbarsDelta:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:DELTa`` command.

        Description:
            - This command queries the delta V cursor readout value of the specified cursor in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:DELTa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:DELTa?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:HBArs:DELTa?
            ```
        """
        return self._delta


class DisplayWaveview1CursorCursor1Function(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion`` command.

    Description:
        - This command sets or queries the cursor type of the specified cursor in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion {SCREEN|WAVEFORM|VBArs|HBArs}
        - DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion?
        ```

    Info:
        - ``HBArs`` specifies horizontal bar cursors, which measure in vertical units.
        - ``VBArs`` specifies vertical bar cursors, which measure in horizontal units.
        - ``SCREEN`` specifies both horizontal and vertical bar cursors, which measure in horizontal
          and vertical units specified by the Cursor 1 and Cursor 2 Sources. Use these cursors to
          measure anywhere in the waveform display area.
        - ``WAVEform`` specifies paired or split cursors in YT display format for measuring waveform
          amplitude and time. In XY and XYZ format, these cursors indicate the amplitude positions
          of an XY pair (Ch1 vs Ch2 voltage, where Ch1 is the X axis and Ch2 is the Y axis) relative
          to the trigger.
    """


class DisplayWaveview1CursorCursor1Ddt(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:DDT`` command.

    Description:
        - This query returns the delta V over delta T cursor readout value of the specified cursor
          in the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1:DDT?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:DDT?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:DDT?
        ```
    """


class DisplayWaveview1CursorCursor1Bsource(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce`` command.

    Description:
        - This command sets or queries the cursor B source of the specified cursor in the specified
          Waveform View. 1 is the specified Waveform View and must be WAVEView1. Cursor<x> is the
          specified cursor and must be CURSOR1.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce {AUTO| CH<x>| BUS<x>| DCH<x>_DALL| MATH<x>| REF<x>| PLOT<x>
        - DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce?
        ```

    Info:
        - ``AUTO`` specifies auto as the cursor B source.
        - ``CH<x>`` specifies an analog channel to use as the cursor B source.
        - ``BUS<x>`` specifies a bus to use as the cursor B source.
        - ``DCH<x>_DALL`` specifies a digital channel to use as the cursor B source The supported
          digital channel value is 1.
        - ``MATH<x>`` specifies a math waveform to use as the cursor B source.
        - ``REF<x>`` specifies a reference waveform to use as the cursor B source.
        - ``PLOT<x>`` specifies a plot as the cursor B source.
    """  # noqa: E501


class DisplayWaveview1CursorCursor1Asource(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce`` command.

    Description:
        - This command sets or queries the cursor A source of the specified cursor in the specified
          Waveform View. 1 is the specified Waveform View and must be WAVEView1. Cursor<x> is the
          specified cursor and must be CURSOR1.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce {AUTO|CH<x>|BUS<x>|DCH<x>_DALL|MATH<x>|REF<x>|PLOT<x>}
        - DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce?
        ```

    Info:
        - ``AUTO`` specifies auto as the cursor A source.
        - ``CH<x>`` specifies an analog channel to use as the cursor A source.
        - ``BUS<x>`` specifies a bus to use as the cursor A source.
        - ``DCH<x>_DALL`` specifies a digital channel to use as the cursor A source The supported
          digital channel value is 1.
        - ``MATH<x>`` specifies a math waveform to use as the cursor A source.
        - ``REF<x>`` specifies a reference waveform to use as the cursor A source.
        - ``PLOT<x>`` specifies a plot as the cursor A source.
    """  # noqa: E501


#  pylint: disable=too-many-instance-attributes
class DisplayWaveview1CursorCursor1(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR1`` command.

    Description:
        - This query returns the cursor parameters for the specified cursor in the specified
          Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor:CURSOR1?
        ```

    Properties:
        - ``.asource``: The ``DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce`` command.
        - ``.bsource``: The ``DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce`` command.
        - ``.ddt``: The ``DISplay:WAVEView1:CURSor:CURSOR1:DDT`` command.
        - ``.function``: The ``DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion`` command.
        - ``.hbars``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs`` command tree.
        - ``.mode``: The ``DISplay:WAVEView1:CURSor:CURSOR1:MODe`` command.
        - ``.oneoverdeltatvalue``: The ``DISplay:WAVEView1:CURSor:CURSOR1:ONEOVERDELTATVALUE``
          command.
        - ``.screen``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN`` command tree.
        - ``.splitmode``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE`` command.
        - ``.state``: The ``DISplay:WAVEView1:CURSor:CURSOR1:STATE`` command.
        - ``.vbars``: The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs`` command tree.
        - ``.waveform``: The ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._asource = DisplayWaveview1CursorCursor1Asource(device, f"{self._cmd_syntax}:ASOUrce")
        self._bsource = DisplayWaveview1CursorCursor1Bsource(device, f"{self._cmd_syntax}:BSOUrce")
        self._ddt = DisplayWaveview1CursorCursor1Ddt(device, f"{self._cmd_syntax}:DDT")
        self._function = DisplayWaveview1CursorCursor1Function(
            device, f"{self._cmd_syntax}:FUNCtion"
        )
        self._hbars = DisplayWaveview1CursorCursor1Hbars(device, f"{self._cmd_syntax}:HBArs")
        self._mode = DisplayWaveview1CursorCursor1Mode(device, f"{self._cmd_syntax}:MODe")
        self._oneoverdeltatvalue = DisplayWaveview1CursorCursor1Oneoverdeltatvalue(
            device, f"{self._cmd_syntax}:ONEOVERDELTATVALUE"
        )
        self._screen = DisplayWaveview1CursorCursor1Screen(device, f"{self._cmd_syntax}:SCREEN")
        self._splitmode = DisplayWaveview1CursorCursor1Splitmode(
            device, f"{self._cmd_syntax}:SPLITMODE"
        )
        self._state = DisplayWaveview1CursorCursor1State(device, f"{self._cmd_syntax}:STATE")
        self._vbars = DisplayWaveview1CursorCursor1Vbars(device, f"{self._cmd_syntax}:VBArs")
        self._waveform = DisplayWaveview1CursorCursor1Waveform(
            device, f"{self._cmd_syntax}:WAVEform"
        )

    @property
    def asource(self) -> DisplayWaveview1CursorCursor1Asource:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce`` command.

        Description:
            - This command sets or queries the cursor A source of the specified cursor in the
              specified Waveform View. 1 is the specified Waveform View and must be WAVEView1.
              Cursor<x> is the specified cursor and must be CURSOR1.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce {AUTO|CH<x>|BUS<x>|DCH<x>_DALL|MATH<x>|REF<x>|PLOT<x>}
            - DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce?
            ```

        Info:
            - ``AUTO`` specifies auto as the cursor A source.
            - ``CH<x>`` specifies an analog channel to use as the cursor A source.
            - ``BUS<x>`` specifies a bus to use as the cursor A source.
            - ``DCH<x>_DALL`` specifies a digital channel to use as the cursor A source The
              supported digital channel value is 1.
            - ``MATH<x>`` specifies a math waveform to use as the cursor A source.
            - ``REF<x>`` specifies a reference waveform to use as the cursor A source.
            - ``PLOT<x>`` specifies a plot as the cursor A source.
        """  # noqa: E501
        return self._asource

    @property
    def bsource(self) -> DisplayWaveview1CursorCursor1Bsource:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce`` command.

        Description:
            - This command sets or queries the cursor B source of the specified cursor in the
              specified Waveform View. 1 is the specified Waveform View and must be WAVEView1.
              Cursor<x> is the specified cursor and must be CURSOR1.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce {AUTO| CH<x>| BUS<x>| DCH<x>_DALL| MATH<x>| REF<x>| PLOT<x>
            - DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce?
            ```

        Info:
            - ``AUTO`` specifies auto as the cursor B source.
            - ``CH<x>`` specifies an analog channel to use as the cursor B source.
            - ``BUS<x>`` specifies a bus to use as the cursor B source.
            - ``DCH<x>_DALL`` specifies a digital channel to use as the cursor B source The
              supported digital channel value is 1.
            - ``MATH<x>`` specifies a math waveform to use as the cursor B source.
            - ``REF<x>`` specifies a reference waveform to use as the cursor B source.
            - ``PLOT<x>`` specifies a plot as the cursor B source.
        """  # noqa: E501
        return self._bsource

    @property
    def ddt(self) -> DisplayWaveview1CursorCursor1Ddt:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:DDT`` command.

        Description:
            - This query returns the delta V over delta T cursor readout value of the specified
              cursor in the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1:DDT?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:DDT?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:DDT?
            ```
        """
        return self._ddt

    @property
    def function(self) -> DisplayWaveview1CursorCursor1Function:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion`` command.

        Description:
            - This command sets or queries the cursor type of the specified cursor in the specified
              Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion {SCREEN|WAVEFORM|VBArs|HBArs}
            - DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion?
            ```

        Info:
            - ``HBArs`` specifies horizontal bar cursors, which measure in vertical units.
            - ``VBArs`` specifies vertical bar cursors, which measure in horizontal units.
            - ``SCREEN`` specifies both horizontal and vertical bar cursors, which measure in
              horizontal and vertical units specified by the Cursor 1 and Cursor 2 Sources. Use
              these cursors to measure anywhere in the waveform display area.
            - ``WAVEform`` specifies paired or split cursors in YT display format for measuring
              waveform amplitude and time. In XY and XYZ format, these cursors indicate the
              amplitude positions of an XY pair (Ch1 vs Ch2 voltage, where Ch1 is the X axis and Ch2
              is the Y axis) relative to the trigger.
        """
        return self._function

    @property
    def hbars(self) -> DisplayWaveview1CursorCursor1Hbars:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.aposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition`` command.
            - ``.aunits``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:AUNIts`` command.
            - ``.bposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition`` command.
            - ``.bunits``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BUNIts`` command.
            - ``.delta``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs:DELTa`` command.
        """
        return self._hbars

    @property
    def mode(self) -> DisplayWaveview1CursorCursor1Mode:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:MODe`` command.

        Description:
            - Sets or queries the cursor tracking mode of the specified cursor in the specified
              Waveform View.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:MODe value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:MODe {INDEPENDENT|TRACK}
            ```

        Info:
            - ``TRACK`` ties the navigational functionality of the two cursors together. For cursor
              1 adjustments, this ties the movement of the two cursors together; however, cursor 2
              continues to move independently of cursor 1.
            - ``INDEPENDENT`` allows independent adjustment of the two cursors.
        """
        return self._mode

    @property
    def oneoverdeltatvalue(self) -> DisplayWaveview1CursorCursor1Oneoverdeltatvalue:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:ONEOVERDELTATVALUE`` command.

        Description:
            - This query returns the one over delta T cursor readout value of the specified cursor
              in the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:ONEOVERDELTATVALUE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:ONEOVERDELTATVALUE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:ONEOVERDELTATVALUE?
            ```
        """
        return self._oneoverdeltatvalue

    @property
    def screen(self) -> DisplayWaveview1CursorCursor1Screen:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.axposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AXPOSition`` command.
            - ``.ayposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:AYPOSition`` command.
            - ``.bxposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BXPOSition`` command.
            - ``.byposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN:BYPOSition`` command.
        """
        return self._screen

    @property
    def splitmode(self) -> DisplayWaveview1CursorCursor1Splitmode:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE`` command.

        Description:
            - This command sets or queries whether both cursors have the same or different sources.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE {SAME|SPLIT}
            - DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE?
            ```

        Info:
            - ``SAME`` specifies both cursors have the same source.
            - ``SPLIT`` specifies the cursors have different sources.
        """
        return self._splitmode

    @property
    def state(self) -> DisplayWaveview1CursorCursor1State:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:STATE`` command.

        Description:
            - This command sets or queries the visible state of the specified cursor in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1:STATE {ON|OFF|<NR1>}
            - DISplay:WAVEView1:CURSor:CURSOR1:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the specified cursor in the specified Waveform View; any other
              value turns this feature on.
            - ``OFF`` disables the specified cursor in the specified Waveform View.
            - ``ON`` enables the specified cursor in the specified Waveform View.
        """
        return self._state

    @property
    def vbars(self) -> DisplayWaveview1CursorCursor1Vbars:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.aposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:APOSition`` command.
            - ``.bposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:BPOSition`` command.
            - ``.delta``: The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:DELTa`` command.
            - ``.units``: The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs:UNIts`` command.
        """
        return self._vbars

    @property
    def waveform(self) -> DisplayWaveview1CursorCursor1Waveform:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.aposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition`` command.
            - ``.bposition``: The ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition`` command.
        """
        return self._waveform


class DisplayWaveview1CursorCursor(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor:CURSOR`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.waveform``: The ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._waveform = DisplayWaveview1CursorCursorWaveform(
            device, f"{self._cmd_syntax}:WAVEform"
        )

    @property
    def waveform(self) -> DisplayWaveview1CursorCursorWaveform:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.avposition``: The ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:AVPOSition`` command.
            - ``.bvposition``: The ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform:BVPOSition`` command.
        """
        return self._waveform


class DisplayWaveview1Cursor(SCPICmdRead):
    """The ``DISplay:WAVEView1:CURSor`` command.

    Description:
        - This query returns the cursor parameters for the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:CURSor?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CURSor?
        ```

    Properties:
        - ``.cursor``: The ``DISplay:WAVEView1:CURSor:CURSOR`` command tree.
        - ``.cursor1``: The ``DISplay:WAVEView1:CURSor:CURSOR1`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cursor = DisplayWaveview1CursorCursor(device, f"{self._cmd_syntax}:CURSOR")
        self._cursor1 = DisplayWaveview1CursorCursor1(device, f"{self._cmd_syntax}:CURSOR1")

    @property
    def cursor(self) -> DisplayWaveview1CursorCursor:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.waveform``: The ``DISplay:WAVEView1:CURSor:CURSOR:WAVEform`` command tree.
        """
        return self._cursor

    @property
    def cursor1(self) -> DisplayWaveview1CursorCursor1:
        """Return the ``DISplay:WAVEView1:CURSor:CURSOR1`` command.

        Description:
            - This query returns the cursor parameters for the specified cursor in the specified
              Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor:CURSOR1?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CURSor:CURSOR1?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor:CURSOR1?
            ```

        Sub-properties:
            - ``.asource``: The ``DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce`` command.
            - ``.bsource``: The ``DISplay:WAVEView1:CURSor:CURSOR1:BSOUrce`` command.
            - ``.ddt``: The ``DISplay:WAVEView1:CURSor:CURSOR1:DDT`` command.
            - ``.function``: The ``DISplay:WAVEView1:CURSor:CURSOR1:FUNCtion`` command.
            - ``.hbars``: The ``DISplay:WAVEView1:CURSor:CURSOR1:HBArs`` command tree.
            - ``.mode``: The ``DISplay:WAVEView1:CURSor:CURSOR1:MODe`` command.
            - ``.oneoverdeltatvalue``: The ``DISplay:WAVEView1:CURSor:CURSOR1:ONEOVERDELTATVALUE``
              command.
            - ``.screen``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SCREEN`` command tree.
            - ``.splitmode``: The ``DISplay:WAVEView1:CURSor:CURSOR1:SPLITMODE`` command.
            - ``.state``: The ``DISplay:WAVEView1:CURSor:CURSOR1:STATE`` command.
            - ``.vbars``: The ``DISplay:WAVEView1:CURSor:CURSOR1:VBArs`` command tree.
            - ``.waveform``: The ``DISplay:WAVEView1:CURSor:CURSOR1:WAVEform`` command tree.
        """
        return self._cursor1


class DisplayWaveview1ChannelVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CH<x>:VERTical:SCAle`` command.

    Description:
        - Sets or queries the vertical scale of the specified channel in volts per division within
          the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CH<x>:VERTical:SCAle?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CH<x>:VERTical:SCAle?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CH<x>:VERTical:SCAle value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CH<x>:VERTical:SCAle <NR3>
        - DISplay:WAVEView1:CH<x>:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is the vertical scale of the specified channel.
    """


class DisplayWaveview1ChannelVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CH<x>:VERTical:POSition`` command.

    Description:
        - Sets or queries the vertical position of the specified channel in the specified Waveform
          View in divisions. 0.0 divisions is center, 5.0 top of the window, and -5.0 the bottom of
          the window.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CH<x>:VERTical:POSition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:CH<x>:VERTical:POSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:CH<x>:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CH<x>:VERTical:POSition <NR3>
        - DISplay:WAVEView1:CH<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position in divisions. 0.0 divisions is center, 5.0 top of the
          window, and -5.0 the bottom of the window.
    """


class DisplayWaveview1ChannelVertical(SCPICmdRead):
    """The ``DISplay:WAVEView1:CH<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CH<x>:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:CH<x>:VERTical?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``DISplay:WAVEView1:CH<x>:VERTical:POSition`` command.
        - ``.scale``: The ``DISplay:WAVEView1:CH<x>:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = DisplayWaveview1ChannelVerticalPosition(
            device, f"{self._cmd_syntax}:POSition"
        )
        self._scale = DisplayWaveview1ChannelVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def position(self) -> DisplayWaveview1ChannelVerticalPosition:
        """Return the ``DISplay:WAVEView1:CH<x>:VERTical:POSition`` command.

        Description:
            - Sets or queries the vertical position of the specified channel in the specified
              Waveform View in divisions. 0.0 divisions is center, 5.0 top of the window, and -5.0
              the bottom of the window.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CH<x>:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CH<x>:VERTical:POSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CH<x>:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CH<x>:VERTical:POSition <NR3>
            - DISplay:WAVEView1:CH<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position in divisions. 0.0 divisions is center, 5.0 top of
              the window, and -5.0 the bottom of the window.
        """
        return self._position

    @property
    def scale(self) -> DisplayWaveview1ChannelVerticalScale:
        """Return the ``DISplay:WAVEView1:CH<x>:VERTical:SCAle`` command.

        Description:
            - Sets or queries the vertical scale of the specified channel in volts per division
              within the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:CH<x>:VERTical:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CH<x>:VERTical:SCAle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CH<x>:VERTical:SCAle value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CH<x>:VERTical:SCAle <NR3>
            - DISplay:WAVEView1:CH<x>:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is the vertical scale of the specified channel.
        """
        return self._scale


class DisplayWaveview1ChannelState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:CH<x>:STATE`` command.

    Description:
        - Sets or queries the state of the specified channel in the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CH<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:CH<x>:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:WAVEView1:CH<x>:STATE value``
          command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:CH<x>:STATE {ON|OFF|<NR1>}
        - DISplay:WAVEView1:CH<x>:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the specified channel on the specified Waveform View; any other
          value turns this feature on.
        - ``OFF`` disables the display the specified channel on the specified Waveform View.
        - ``ON`` enables the specified channel on the specified Waveform View.
    """


class DisplayWaveview1Channel(ValidatedChannel, SCPICmdRead):
    """The ``DISplay:WAVEView1:CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DISplay:WAVEView1:CH<x>:STATE`` command.
        - ``.vertical``: The ``DISplay:WAVEView1:CH<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayWaveview1ChannelState(device, f"{self._cmd_syntax}:STATE")
        self._vertical = DisplayWaveview1ChannelVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def state(self) -> DisplayWaveview1ChannelState:
        """Return the ``DISplay:WAVEView1:CH<x>:STATE`` command.

        Description:
            - Sets or queries the state of the specified channel in the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CH<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:CH<x>:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:CH<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CH<x>:STATE {ON|OFF|<NR1>}
            - DISplay:WAVEView1:CH<x>:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the specified channel on the specified Waveform View; any other
              value turns this feature on.
            - ``OFF`` disables the display the specified channel on the specified Waveform View.
            - ``ON`` enables the specified channel on the specified Waveform View.
        """
        return self._state

    @property
    def vertical(self) -> DisplayWaveview1ChannelVertical:
        """Return the ``DISplay:WAVEView1:CH<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CH<x>:VERTical?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:CH<x>:VERTical?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``DISplay:WAVEView1:CH<x>:VERTical:POSition`` command.
            - ``.scale``: The ``DISplay:WAVEView1:CH<x>:VERTical:SCAle`` command.
        """
        return self._vertical


class DisplayWaveview1BusBItemVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:BUS:B<x>:VERTical:POSition`` command.

    Description:
        - Sets or queries the vertical position of the specified bus in the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:WAVEView1:BUS:B<x>:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:WAVEView1:BUS:B<x>:VERTical:POSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:BUS:B<x>:VERTical:POSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:BUS:B<x>:VERTical:POSition <NR3>
        - DISplay:WAVEView1:BUS:B<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the vertical position of the specified bus.
    """


class DisplayWaveview1BusBItemVertical(SCPICmdRead):
    """The ``DISplay:WAVEView1:BUS:B<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:BUS:B<x>:VERTical?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:BUS:B<x>:VERTical?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``DISplay:WAVEView1:BUS:B<x>:VERTical:POSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = DisplayWaveview1BusBItemVerticalPosition(
            device, f"{self._cmd_syntax}:POSition"
        )

    @property
    def position(self) -> DisplayWaveview1BusBItemVerticalPosition:
        """Return the ``DISplay:WAVEView1:BUS:B<x>:VERTical:POSition`` command.

        Description:
            - Sets or queries the vertical position of the specified bus in the specified Waveform
              View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:WAVEView1:BUS:B<x>:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:BUS:B<x>:VERTical:POSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:BUS:B<x>:VERTical:POSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:BUS:B<x>:VERTical:POSition <NR3>
            - DISplay:WAVEView1:BUS:B<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the vertical position of the specified bus.
        """
        return self._position


class DisplayWaveview1BusBItemState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:WAVEView1:BUS:B<x>:STATE`` command.

    Description:
        - Sets or queries the state of the specified bus in the specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:BUS:B<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:BUS:B<x>:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:WAVEView1:BUS:B<x>:STATE value`` command.

    SCPI Syntax:
        ```
        - DISplay:WAVEView1:BUS:B<x>:STATE {OFF|ON|0|1}
        - DISplay:WAVEView1:BUS:B<x>:STATE?
        ```

    Info:
        - ``0`` turns specified bus off.
        - ``1`` turns the specified bus on.
        - ``ON`` turns the specified bus on.
        - ``OFF`` turns specified bus off.
    """


class DisplayWaveview1BusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:WAVEView1:BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:BUS:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:BUS:B<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DISplay:WAVEView1:BUS:B<x>:STATE`` command.
        - ``.vertical``: The ``DISplay:WAVEView1:BUS:B<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayWaveview1BusBItemState(device, f"{self._cmd_syntax}:STATE")
        self._vertical = DisplayWaveview1BusBItemVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def state(self) -> DisplayWaveview1BusBItemState:
        """Return the ``DISplay:WAVEView1:BUS:B<x>:STATE`` command.

        Description:
            - Sets or queries the state of the specified bus in the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:BUS:B<x>:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:BUS:B<x>:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:WAVEView1:BUS:B<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:BUS:B<x>:STATE {OFF|ON|0|1}
            - DISplay:WAVEView1:BUS:B<x>:STATE?
            ```

        Info:
            - ``0`` turns specified bus off.
            - ``1`` turns the specified bus on.
            - ``ON`` turns the specified bus on.
            - ``OFF`` turns specified bus off.
        """
        return self._state

    @property
    def vertical(self) -> DisplayWaveview1BusBItemVertical:
        """Return the ``DISplay:WAVEView1:BUS:B<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:BUS:B<x>:VERTical?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:WAVEView1:BUS:B<x>:VERTical?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``DISplay:WAVEView1:BUS:B<x>:VERTical:POSition`` command.
        """
        return self._vertical


class DisplayWaveview1Bus(SCPICmdRead):
    """The ``DISplay:WAVEView1:BUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1:BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:BUS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.b``: The ``DISplay:WAVEView1:BUS:B<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._b: Dict[int, DisplayWaveview1BusBItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayWaveview1BusBItem(device, f"{self._cmd_syntax}:B{x}")
        )

    @property
    def b(self) -> Dict[int, DisplayWaveview1BusBItem]:
        """Return the ``DISplay:WAVEView1:BUS:B<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:BUS:B<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:BUS:B<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DISplay:WAVEView1:BUS:B<x>:STATE`` command.
            - ``.vertical``: The ``DISplay:WAVEView1:BUS:B<x>:VERTical`` command tree.
        """
        return self._b


#  pylint: disable=too-many-instance-attributes
class DisplayWaveview1(SCPICmdRead):
    """The ``DISplay:WAVEView1`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView1?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bus``: The ``DISplay:WAVEView1:BUS`` command tree.
        - ``.ch``: The ``DISplay:WAVEView1:CH<x>`` command tree.
        - ``.cursor``: The ``DISplay:WAVEView1:CURSor`` command.
        - ``.dch``: The ``DISplay:WAVEView1:DCH<x>`` command tree.
        - ``.filter``: The ``DISplay:WAVEView1:FILTer`` command.
        - ``.graticule``: The ``DISplay:WAVEView1:GRAticule`` command.
        - ``.intensity``: The ``DISplay:WAVEView1:INTENSITy`` command tree.
        - ``.math``: The ``DISplay:WAVEView1:MATH`` command tree.
        - ``.ref``: The ``DISplay:WAVEView1:REF`` command tree.
        - ``.style``: The ``DISplay:WAVEView1:STYle`` command.
        - ``.viewstyle``: The ``DISplay:WAVEView1:VIEWStyle`` command.
        - ``.zoom``: The ``DISplay:WAVEView1:ZOOM`` command.
        - ``.refx``: The ``DISplay:WAVEView1:REF<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bus = DisplayWaveview1Bus(device, f"{self._cmd_syntax}:BUS")
        self._ch: Dict[int, DisplayWaveview1Channel] = DefaultDictPassKeyToFactory(
            lambda x: DisplayWaveview1Channel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._cursor = DisplayWaveview1Cursor(device, f"{self._cmd_syntax}:CURSor")
        self._dch: Dict[int, DisplayWaveview1DchItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayWaveview1DchItem(device, f"{self._cmd_syntax}:DCH{x}")
        )
        self._filter = DisplayWaveview1Filter(device, f"{self._cmd_syntax}:FILTer")
        self._graticule = DisplayWaveview1Graticule(device, f"{self._cmd_syntax}:GRAticule")
        self._intensity = DisplayWaveview1Intensity(device, f"{self._cmd_syntax}:INTENSITy")
        self._math = DisplayWaveview1Math(device, f"{self._cmd_syntax}:MATH")
        self._style = DisplayWaveview1Style(device, f"{self._cmd_syntax}:STYle")
        self._viewstyle = DisplayWaveview1Viewstyle(device, f"{self._cmd_syntax}:VIEWStyle")
        self._zoom = DisplayWaveview1Zoom(device, f"{self._cmd_syntax}:ZOOM")
        self._ref = DisplayWaveview1Ref(device, f"{self._cmd_syntax}:REF")
        self._refx: Dict[int, DisplayWaveview1RefItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayWaveview1RefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def bus(self) -> DisplayWaveview1Bus:
        """Return the ``DISplay:WAVEView1:BUS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:BUS?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:BUS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.b``: The ``DISplay:WAVEView1:BUS:B<x>`` command tree.
        """
        return self._bus

    @property
    def ch(self) -> Dict[int, DisplayWaveview1Channel]:
        """Return the ``DISplay:WAVEView1:CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:CH<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DISplay:WAVEView1:CH<x>:STATE`` command.
            - ``.vertical``: The ``DISplay:WAVEView1:CH<x>:VERTical`` command tree.
        """
        return self._ch

    @property
    def cursor(self) -> DisplayWaveview1Cursor:
        """Return the ``DISplay:WAVEView1:CURSor`` command.

        Description:
            - This query returns the cursor parameters for the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:CURSor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:CURSor?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:CURSor?
            ```

        Sub-properties:
            - ``.cursor``: The ``DISplay:WAVEView1:CURSor:CURSOR`` command tree.
            - ``.cursor1``: The ``DISplay:WAVEView1:CURSor:CURSOR1`` command.
        """
        return self._cursor

    @property
    def dch(self) -> Dict[int, DisplayWaveview1DchItem]:
        """Return the ``DISplay:WAVEView1:DCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:DCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:DCH<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.d``: The ``DISplay:WAVEView1:DCH<x>_D<x>`` command tree.
            - ``.dall``: The ``DISplay:WAVEView1:DCH<x>_DALL`` command tree.
        """
        return self._dch

    @property
    def filter(self) -> DisplayWaveview1Filter:
        """Return the ``DISplay:WAVEView1:FILTer`` command.

        Description:
            - This command sets or queries the type of interpolation filter for the display.

        Usage:
            - Using the ``.write(value)`` method will send the ``DISplay:WAVEView1:FILTer value``
              command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:FILTer {SINX|LINear}
            ```

        Info:
            - ``LINEAr`` specifies linear interpolation, where acquired points are connected with
              straight lines.
            - ``SINX`` specifies sin(x)/x interpolation, where acquired points are fit to a curve.
        """
        return self._filter

    @property
    def graticule(self) -> DisplayWaveview1Graticule:
        """Return the ``DISplay:WAVEView1:GRAticule`` command.

        Description:
            - This command selects or queries the type of graticule that is displayed.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:GRAticule?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:GRAticule?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:WAVEView1:GRAticule value``
              command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:GRAticule {GRId|TIMe|FULl|NONe}
            - DISplay:WAVEView1:GRAticule?
            ```

        Info:
            - ``GRId`` specifies a frame and grid only.
            - ``TIMe`` specifies a time graticule only.
            - ``FULl`` specifies a frame, a grid and cross hairs.
            - ``NONe`` specified no graticule.
        """
        return self._graticule

    @property
    def intensity(self) -> DisplayWaveview1Intensity:
        """Return the ``DISplay:WAVEView1:INTENSITy`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:INTENSITy?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:INTENSITy?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.graticule``: The ``DISplay:WAVEView1:INTENSITy:GRATicule`` command.
            - ``.waveform``: The ``DISplay:WAVEView1:INTENSITy:WAVEform`` command.
        """
        return self._intensity

    @property
    def math(self) -> DisplayWaveview1Math:
        """Return the ``DISplay:WAVEView1:MATH`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:MATH?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:MATH?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.math``: The ``DISplay:WAVEView1:MATH:MATH<x>`` command tree.
        """
        return self._math

    @property
    def style(self) -> DisplayWaveview1Style:
        """Return the ``DISplay:WAVEView1:STYle`` command.

        Description:
            - This command sets or queries how the waveforms are displayed for analysis mode.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:STYle?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:STYle?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:WAVEView1:STYle value``
              command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:STYle {VECtors|DOTsonly}
            - DISplay:WAVEView1:STYle?
            ```

        Info:
            - ``DOTs`` displays individual data points. New points immediately replace old ones.
            - ``VECtors`` connects adjacent data points. New points immediately replace old ones.
        """
        return self._style

    @property
    def viewstyle(self) -> DisplayWaveview1Viewstyle:
        """Return the ``DISplay:WAVEView1:VIEWStyle`` command.

        Description:
            - The command sets or queries the waveform layout style used by the display.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:VIEWStyle?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:VIEWStyle?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:WAVEView1:VIEWStyle value``
              command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:VIEWStyle {OVErlay|STAcked}
            - DISplay:WAVEView1:VIEWStyle?
            ```

        Info:
            - ``OVErlay`` specifies that the display view style used by the specified Waveform View
              is overlay.
            - ``STAcked`` specifies that the display view style used by the specified Waveform View
              is stacked.
        """
        return self._viewstyle

    @property
    def zoom(self) -> DisplayWaveview1Zoom:
        """Return the ``DISplay:WAVEView1:ZOOM`` command.

        Description:
            - This query returns the zoom parameters of the specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:ZOOM?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:ZOOM?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:WAVEView1:ZOOM?
            ```

        Sub-properties:
            - ``.zoom1``: The ``DISplay:WAVEView1:ZOOM:ZOOM1`` command.
        """
        return self._zoom

    @property
    def ref(self) -> DisplayWaveview1Ref:
        """Return the ``DISplay:WAVEView1:REF`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:REF?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ref``: The ``DISplay:WAVEView1:REF:REF<x>`` command tree.
        """
        return self._ref

    @property
    def refx(self) -> Dict[int, DisplayWaveview1RefItem]:
        """Return the ``DISplay:WAVEView1:REF<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1:REF<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dall``: The ``DISplay:WAVEView1:REF<x>_DALL`` command tree.
        """
        return self._refx


class DisplayWaveview(SCPICmdRead):
    """The ``DISplay:WAVEView`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:WAVEView?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.cursor``: The ``DISplay:WAVEView:CURSor`` command tree.
        - ``.gridtype``: The ``DISplay:WAVEView:GRIDTYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cursor = DisplayWaveviewCursor(device, f"{self._cmd_syntax}:CURSor")
        self._gridtype = DisplayWaveviewGridtype(device, f"{self._cmd_syntax}:GRIDTYPE")

    @property
    def cursor(self) -> DisplayWaveviewCursor:
        """Return the ``DISplay:WAVEView:CURSor`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView:CURSor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView:CURSor?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.cursor1``: The ``DISplay:WAVEView:CURSor:CURSOR1`` command tree.
        """
        return self._cursor

    @property
    def gridtype(self) -> DisplayWaveviewGridtype:
        """Return the ``DISplay:WAVEView:GRIDTYPE`` command.

        Description:
            - This command sets or queries the Waveform View Graticule type.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView:GRIDTYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView:GRIDTYPE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:WAVEView:GRIDTYPE value``
              command.

        SCPI Syntax:
            ```
            - DISplay:WAVEView:GRIDTYPE {MOVEABLE|FIXED}
            - DISplay:WAVEView:GRIDTYPE?
            ```

        Info:
            - ``MOVEABLE`` sets the Waveform View so that both the waveform and the grid (graticule)
              move together when moving the waveform horizontally.
            - ``FIXED`` sets the Waveform View so that the grid dows not move when moving the
              waveform horizontally.
        """
        return self._gridtype


class DisplayVarpersist(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:VARpersist`` command.

    Description:
        - This command sets or queries display persistence decay time, which is the approximate
          decay time for a freshly struck persistence sample.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:VARpersist?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:VARpersist?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:VARpersist value`` command.

    SCPI Syntax:
        ```
        - DISplay:VARpersist <NR3>
        - DISplay:VARpersist?
        ```

    Info:
        - ``<NR3>`` indicates the persistence decay time and ranges from 0.5 to 100.
    """


class DisplaySelectWaveview1Source(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SELect:WAVEView1:SOUrce`` command.

    Description:
        - This command sets or queries the selected source in the given waveview.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SELect:WAVEView1:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SELect:WAVEView1:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:SELect:WAVEView1:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - DISplay:SELect:WAVEView1:SOUrce {CH<x>|MATH<x>|BUS<x>|REF<x>|PLOT<x>}
        - DISplay:SELect:WAVEView1:SOUrce?
        ```

    Info:
        - ``CH<x>``
        - ``MATH<x>``
        - ``BUS<x>``
        - ``REF<x>``
        - ``PLOT<x>``
    """


class DisplaySelectWaveview1(SCPICmdRead):
    """The ``DISplay:SELect:WAVEView1`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SELect:WAVEView1?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SELect:WAVEView1?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``DISplay:SELect:WAVEView1:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = DisplaySelectWaveview1Source(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> DisplaySelectWaveview1Source:
        """Return the ``DISplay:SELect:WAVEView1:SOUrce`` command.

        Description:
            - This command sets or queries the selected source in the given waveview.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SELect:WAVEView1:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:SELect:WAVEView1:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:SELect:WAVEView1:SOUrce value`` command.

        SCPI Syntax:
            ```
            - DISplay:SELect:WAVEView1:SOUrce {CH<x>|MATH<x>|BUS<x>|REF<x>|PLOT<x>}
            - DISplay:SELect:WAVEView1:SOUrce?
            ```

        Info:
            - ``CH<x>``
            - ``MATH<x>``
            - ``BUS<x>``
            - ``REF<x>``
            - ``PLOT<x>``
        """
        return self._source


class DisplaySelectView(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SELect:VIEW`` command.

    Description:
        - This command sets or queries the selected view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SELect:VIEW?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SELect:VIEW?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:SELect:VIEW value`` command.

    SCPI Syntax:
        ```
        - DISplay:SELect:VIEW {WAVEVIEW1|MATHFFT<x>|PLOTVIEW<x>|REFFFT<x>}
        - DISplay:SELect:VIEW?
        ```

    Info:
        - ``WAVEVIEW1``
        - ``MATHFFT<x>``
        - ``PLOTVIEW<x>``
        - ``REFFFT<x>``
    """


class DisplaySelectSource(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SELect:SOUrce`` command.

    Description:
        - This command sets or queries the overall selected source. Sets are applied to all views
          that contain the source and the selected view is changed.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SELect:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SELect:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:SELect:SOUrce value`` command.

    SCPI Syntax:
        ```
        - DISplay:SELect:SOUrce {NONE|CH<x>|DCH<x>|BUS<x>|MATH<x>|PLOT<x>|REF<x>}
        - DISplay:SELect:SOUrce?
        ```

    Info:
        - ``NONE`` disables the selected source.
        - ``CH<x>`` specifies an analog channel to use as the source.
        - ``DCH<x>`` specifies a digital channel to use as the source. The supported digital channel
          value is 1.
        - ``BUS<x>`` specifies a bus to use as the source.
        - ``MATH<x>`` specifies a math waveform to use as the source.
        - ``PLOT<x>`` specifies a plot as the source.
        - ``REF<x>`` specifies a reference waveform to use as the source.
    """


class DisplaySelectReference(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SELect:REFerence`` command.

    Description:
        - This command sets or queries the overall selected reference waveform. Sets are applied to
          all views that contain the source and the selected view is changed.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SELect:REFerence?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SELect:REFerence?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:SELect:REFerence value``
          command.

    SCPI Syntax:
        ```
        - DISplay:SELect:REFerence {NONE|REF<x>}
        - DISplay:SELect:REFerence?
        ```

    Info:
        - ``NONE``
        - ``REF<x>`` where x is the specified reference waveform.
    """


class DisplaySelectMath(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SELect:MATH`` command.

    Description:
        - This command sets or queries the overall selected math. Sets are applied to all views that
          contain the source and the selected view is changed. When multiple Math are open, querying
          the command gives the correct result, but the required Math cannot be set.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SELect:MATH?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SELect:MATH?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:SELect:MATH value`` command.

    SCPI Syntax:
        ```
        - DISplay:SELect:MATH MATH<x>
        - DISplay:SELect:MATH?
        ```

    Info:
        - ``MATH<x>`` is the selected math.
    """


class DisplaySelectBus(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:SELect:BUS`` command.

    Description:
        - This command sets or queries the overall selected bus. Sets are applied to all views that
          contain the source and the selected view is changed. When multiple buses are open,
          querying the command gives the correct result, but the bus cannot set.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SELect:BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SELect:BUS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:SELect:BUS value`` command.

    SCPI Syntax:
        ```
        - DISplay:SELect:BUS BUS<x>
        - DISplay:SELect:BUS?
        ```

    Info:
        - ``BUS<x>`` is the selected bus.
    """


class DisplaySelect(SCPICmdRead):
    """The ``DISplay:SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:SELect?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bus``: The ``DISplay:SELect:BUS`` command.
        - ``.math``: The ``DISplay:SELect:MATH`` command.
        - ``.reference``: The ``DISplay:SELect:REFerence`` command.
        - ``.source``: The ``DISplay:SELect:SOUrce`` command.
        - ``.view``: The ``DISplay:SELect:VIEW`` command.
        - ``.waveview1``: The ``DISplay:SELect:WAVEView1`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bus = DisplaySelectBus(device, f"{self._cmd_syntax}:BUS")
        self._math = DisplaySelectMath(device, f"{self._cmd_syntax}:MATH")
        self._reference = DisplaySelectReference(device, f"{self._cmd_syntax}:REFerence")
        self._source = DisplaySelectSource(device, f"{self._cmd_syntax}:SOUrce")
        self._view = DisplaySelectView(device, f"{self._cmd_syntax}:VIEW")
        self._waveview1 = DisplaySelectWaveview1(device, f"{self._cmd_syntax}:WAVEView1")

    @property
    def bus(self) -> DisplaySelectBus:
        """Return the ``DISplay:SELect:BUS`` command.

        Description:
            - This command sets or queries the overall selected bus. Sets are applied to all views
              that contain the source and the selected view is changed. When multiple buses are
              open, querying the command gives the correct result, but the bus cannot set.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SELect:BUS?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:SELect:BUS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:SELect:BUS value`` command.

        SCPI Syntax:
            ```
            - DISplay:SELect:BUS BUS<x>
            - DISplay:SELect:BUS?
            ```

        Info:
            - ``BUS<x>`` is the selected bus.
        """
        return self._bus

    @property
    def math(self) -> DisplaySelectMath:
        """Return the ``DISplay:SELect:MATH`` command.

        Description:
            - This command sets or queries the overall selected math. Sets are applied to all views
              that contain the source and the selected view is changed. When multiple Math are open,
              querying the command gives the correct result, but the required Math cannot be set.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SELect:MATH?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:SELect:MATH?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:SELect:MATH value``
              command.

        SCPI Syntax:
            ```
            - DISplay:SELect:MATH MATH<x>
            - DISplay:SELect:MATH?
            ```

        Info:
            - ``MATH<x>`` is the selected math.
        """
        return self._math

    @property
    def reference(self) -> DisplaySelectReference:
        """Return the ``DISplay:SELect:REFerence`` command.

        Description:
            - This command sets or queries the overall selected reference waveform. Sets are applied
              to all views that contain the source and the selected view is changed.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SELect:REFerence?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:SELect:REFerence?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:SELect:REFerence value``
              command.

        SCPI Syntax:
            ```
            - DISplay:SELect:REFerence {NONE|REF<x>}
            - DISplay:SELect:REFerence?
            ```

        Info:
            - ``NONE``
            - ``REF<x>`` where x is the specified reference waveform.
        """
        return self._reference

    @property
    def source(self) -> DisplaySelectSource:
        """Return the ``DISplay:SELect:SOUrce`` command.

        Description:
            - This command sets or queries the overall selected source. Sets are applied to all
              views that contain the source and the selected view is changed.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SELect:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:SELect:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:SELect:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - DISplay:SELect:SOUrce {NONE|CH<x>|DCH<x>|BUS<x>|MATH<x>|PLOT<x>|REF<x>}
            - DISplay:SELect:SOUrce?
            ```

        Info:
            - ``NONE`` disables the selected source.
            - ``CH<x>`` specifies an analog channel to use as the source.
            - ``DCH<x>`` specifies a digital channel to use as the source. The supported digital
              channel value is 1.
            - ``BUS<x>`` specifies a bus to use as the source.
            - ``MATH<x>`` specifies a math waveform to use as the source.
            - ``PLOT<x>`` specifies a plot as the source.
            - ``REF<x>`` specifies a reference waveform to use as the source.
        """
        return self._source

    @property
    def view(self) -> DisplaySelectView:
        """Return the ``DISplay:SELect:VIEW`` command.

        Description:
            - This command sets or queries the selected view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SELect:VIEW?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:SELect:VIEW?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:SELect:VIEW value``
              command.

        SCPI Syntax:
            ```
            - DISplay:SELect:VIEW {WAVEVIEW1|MATHFFT<x>|PLOTVIEW<x>|REFFFT<x>}
            - DISplay:SELect:VIEW?
            ```

        Info:
            - ``WAVEVIEW1``
            - ``MATHFFT<x>``
            - ``PLOTVIEW<x>``
            - ``REFFFT<x>``
        """
        return self._view

    @property
    def waveview1(self) -> DisplaySelectWaveview1:
        """Return the ``DISplay:SELect:WAVEView1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SELect:WAVEView1?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:SELect:WAVEView1?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``DISplay:SELect:WAVEView1:SOUrce`` command.
        """
        return self._waveview1


class DisplayReffftviewItemZoomYaxisTo(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:ZOOM:YAXIS:TO`` command.

    Description:
        - This command sets or queries the top value of the zoom y-axis in the specified plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:YAXIS:TO?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:ZOOM:YAXIS:TO?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:ZOOM:YAXIS:TO value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:ZOOM:YAXIS:TO <NR3>
        - DISplay:REFFFTView<x>:ZOOM:YAXIS:TO?
        ```

    Info:
        - ``<NR3>`` is the top value of the zoom y-axis in the specified plot view.
    """


class DisplayReffftviewItemZoomYaxisFrom(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM`` command.

    Description:
        - This command sets or queries the bottom value of the zoom y-axis in the specified plot
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM <NR3>
        - DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM?
        ```

    Info:
        - ``<NR3>`` is the bottom value of the zoom y-axis in the specified plot view.
    """


class DisplayReffftviewItemZoomYaxis(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:ZOOM:YAXIS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:YAXIS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:ZOOM:YAXIS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.from``: The ``DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM`` command.
        - ``.to``: The ``DISplay:REFFFTView<x>:ZOOM:YAXIS:TO`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._from = DisplayReffftviewItemZoomYaxisFrom(device, f"{self._cmd_syntax}:FROM")
        self._to = DisplayReffftviewItemZoomYaxisTo(device, f"{self._cmd_syntax}:TO")

    @property
    def from_(self) -> DisplayReffftviewItemZoomYaxisFrom:
        """Return the ``DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM`` command.

        Description:
            - This command sets or queries the bottom value of the zoom y-axis in the specified plot
              view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM <NR3>
            - DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM?
            ```

        Info:
            - ``<NR3>`` is the bottom value of the zoom y-axis in the specified plot view.
        """
        return self._from

    @property
    def to(self) -> DisplayReffftviewItemZoomYaxisTo:
        """Return the ``DISplay:REFFFTView<x>:ZOOM:YAXIS:TO`` command.

        Description:
            - This command sets or queries the top value of the zoom y-axis in the specified plot
              view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:YAXIS:TO?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:ZOOM:YAXIS:TO?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:ZOOM:YAXIS:TO value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:ZOOM:YAXIS:TO <NR3>
            - DISplay:REFFFTView<x>:ZOOM:YAXIS:TO?
            ```

        Info:
            - ``<NR3>`` is the top value of the zoom y-axis in the specified plot view.
        """
        return self._to


class DisplayReffftviewItemZoomXaxisTo(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:ZOOM:XAXIS:TO`` command.

    Description:
        - This command sets or queries the right edge of the zoom x-axis in the specified plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:XAXIS:TO?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:ZOOM:XAXIS:TO?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:ZOOM:XAXIS:TO value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:ZOOM:XAXIS:TO <NR3>
        - DISplay:REFFFTView<x>:ZOOM:XAXIS:TO?
        ```

    Info:
        - ``<NR3>`` is the right edge of the zoom x-axis in the specified plot view.
    """


class DisplayReffftviewItemZoomXaxisFrom(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM`` command.

    Description:
        - This command sets or returns the left edge of the zoom x-axis in the specified plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM <NR3>
        - DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM?
        ```

    Info:
        - ``<NR3>`` is the left edge of the zoom x-axis in the specified plot view.
    """


class DisplayReffftviewItemZoomXaxis(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:ZOOM:XAXIS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:XAXIS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:ZOOM:XAXIS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.from``: The ``DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM`` command.
        - ``.to``: The ``DISplay:REFFFTView<x>:ZOOM:XAXIS:TO`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._from = DisplayReffftviewItemZoomXaxisFrom(device, f"{self._cmd_syntax}:FROM")
        self._to = DisplayReffftviewItemZoomXaxisTo(device, f"{self._cmd_syntax}:TO")

    @property
    def from_(self) -> DisplayReffftviewItemZoomXaxisFrom:
        """Return the ``DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM`` command.

        Description:
            - This command sets or returns the left edge of the zoom x-axis in the specified plot
              view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM <NR3>
            - DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM?
            ```

        Info:
            - ``<NR3>`` is the left edge of the zoom x-axis in the specified plot view.
        """
        return self._from

    @property
    def to(self) -> DisplayReffftviewItemZoomXaxisTo:
        """Return the ``DISplay:REFFFTView<x>:ZOOM:XAXIS:TO`` command.

        Description:
            - This command sets or queries the right edge of the zoom x-axis in the specified plot
              view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:XAXIS:TO?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:ZOOM:XAXIS:TO?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:ZOOM:XAXIS:TO value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:ZOOM:XAXIS:TO <NR3>
            - DISplay:REFFFTView<x>:ZOOM:XAXIS:TO?
            ```

        Info:
            - ``<NR3>`` is the right edge of the zoom x-axis in the specified plot view.
        """
        return self._to


class DisplayReffftviewItemZoom(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:ZOOM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:ZOOM?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.xaxis``: The ``DISplay:REFFFTView<x>:ZOOM:XAXIS`` command tree.
        - ``.yaxis``: The ``DISplay:REFFFTView<x>:ZOOM:YAXIS`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._xaxis = DisplayReffftviewItemZoomXaxis(device, f"{self._cmd_syntax}:XAXIS")
        self._yaxis = DisplayReffftviewItemZoomYaxis(device, f"{self._cmd_syntax}:YAXIS")

    @property
    def xaxis(self) -> DisplayReffftviewItemZoomXaxis:
        """Return the ``DISplay:REFFFTView<x>:ZOOM:XAXIS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:XAXIS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:ZOOM:XAXIS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.from``: The ``DISplay:REFFFTView<x>:ZOOM:XAXIS:FROM`` command.
            - ``.to``: The ``DISplay:REFFFTView<x>:ZOOM:XAXIS:TO`` command.
        """
        return self._xaxis

    @property
    def yaxis(self) -> DisplayReffftviewItemZoomYaxis:
        """Return the ``DISplay:REFFFTView<x>:ZOOM:YAXIS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM:YAXIS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:ZOOM:YAXIS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.from``: The ``DISplay:REFFFTView<x>:ZOOM:YAXIS:FROM`` command.
            - ``.to``: The ``DISplay:REFFFTView<x>:ZOOM:YAXIS:TO`` command.
        """
        return self._yaxis


class DisplayReffftviewItemXaxisScale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:XAXIS:SCALE`` command.

    Description:
        - This command sets or queries the x-axis scale setting for Ref FFT.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:XAXIS:SCALE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:XAXIS:SCALE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:XAXIS:SCALE value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:XAXIS:SCALE {LINEAr|LOG}
        - DISplay:REFFFTView<x>:XAXIS:SCALE?
        ```

    Info:
        - ``LINEAr`` specifies a linear scale.
        - ``LOG`` specifies a logarithmic scale.
    """


class DisplayReffftviewItemXaxis(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:XAXIS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:XAXIS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:XAXIS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DISplay:REFFFTView<x>:XAXIS:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DisplayReffftviewItemXaxisScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DisplayReffftviewItemXaxisScale:
        """Return the ``DISplay:REFFFTView<x>:XAXIS:SCALE`` command.

        Description:
            - This command sets or queries the x-axis scale setting for Ref FFT.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:XAXIS:SCALE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:XAXIS:SCALE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:XAXIS:SCALE value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:XAXIS:SCALE {LINEAr|LOG}
            - DISplay:REFFFTView<x>:XAXIS:SCALE?
            ```

        Info:
            - ``LINEAr`` specifies a linear scale.
            - ``LOG`` specifies a logarithmic scale.
        """
        return self._scale


class DisplayReffftviewItemRefRefItemState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:REF:REF<x>:STATE`` command.

    Description:
        - This command sets or queries the state of the specified reference waveform in the
          specified Waveform View.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:REF:REF<x>:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:REF:REF<x>:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:REF:REF<x>:STATE value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:REF:REF<x>:STATE {ON|OFF|0|1|<NR1>}
        - DISplay:REFFFTView<x>:REF:REF<x>:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the specified reference; any other value turns this feature on.
        - ``OFF`` disables the display the specified reference.
        - ``0`` disables the display the specified reference.
        - ``ON`` enables the specified reference.
        - ``1`` enables the specified reference.
    """


class DisplayReffftviewItemRefRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:REF:REF<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:REF:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:REF:REF<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DISplay:REFFFTView<x>:REF:REF<x>:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayReffftviewItemRefRefItemState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> DisplayReffftviewItemRefRefItemState:
        """Return the ``DISplay:REFFFTView<x>:REF:REF<x>:STATE`` command.

        Description:
            - This command sets or queries the state of the specified reference waveform in the
              specified Waveform View.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:REF:REF<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:REF:REF<x>:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:REF:REF<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:REF:REF<x>:STATE {ON|OFF|0|1|<NR1>}
            - DISplay:REFFFTView<x>:REF:REF<x>:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the specified reference; any other value turns this feature on.
            - ``OFF`` disables the display the specified reference.
            - ``0`` disables the display the specified reference.
            - ``ON`` enables the specified reference.
            - ``1`` enables the specified reference.
        """
        return self._state


class DisplayReffftviewItemRef(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:REF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:REF?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:REF?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ref``: The ``DISplay:REFFFTView<x>:REF:REF<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ref: Dict[int, DisplayReffftviewItemRefRefItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayReffftviewItemRefRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def ref(self) -> Dict[int, DisplayReffftviewItemRefRefItem]:
        """Return the ``DISplay:REFFFTView<x>:REF:REF<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:REF:REF<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:REF:REF<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DISplay:REFFFTView<x>:REF:REF<x>:STATE`` command.
        """
        return self._ref


class DisplayReffftviewItemGridlines(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:GRIDlines`` command.

    Description:
        - This command sets or returns the grid lines setting of the plot.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:GRIDlines?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:GRIDlines?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:REFFFTView<x>:GRIDlines value``
          command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:GRIDlines {HORizontal|VERTical|BOTH}
        - DISplay:REFFFTView<x>:GRIDlines?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``HORizontal`` specifies horizontal grid lines.
        - ``VERTical`` specifies vertical grid lines.
        - ``BOTH`` specifies both horizontal and vertical grid lines.
    """


class DisplayReffftviewItemCursorWaveformBvposition(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:WAVEform:BVPOSition`` command.

    Description:
        - This query-only command returns the value of the cursor B vertical position.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:BVPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:BVPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:WAVEform:BVPOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorWaveformBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition`` command.

    Description:
        - Sets or returns the waveform cursor B position in the specified plot view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition <NR3>
        - DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``<NR3>`` is the waveform cursor B position in the specified plot view.
    """


class DisplayReffftviewItemCursorWaveformBhposition(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:WAVEform:BHPOSition`` command.

    Description:
        - This query-only command returns the value of the cursor B horizontal position.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:BHPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:BHPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:WAVEform:BHPOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorWaveformAvposition(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:WAVEform:AVPOSition`` command.

    Description:
        - This query-only command returns the value of the cursor A vertical position.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:AVPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:AVPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:WAVEform:AVPOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorWaveformAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition`` command.

    Description:
        - Sets or returns the waveform cursor A position in the specified plot view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition <NR3>
        - DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``<NR3>`` is the waveform cursor A position in the specified plot view.
    """


class DisplayReffftviewItemCursorWaveformAhposition(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:WAVEform:AHPOSition`` command.

    Description:
        - This query-only command returns the value of the cursor A horizontal position.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:AHPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform:AHPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:WAVEform:AHPOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorWaveform(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:WAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:WAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:WAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.

    Properties:
        - ``.ahposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:AHPOSition`` command.
        - ``.aposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition`` command.
        - ``.avposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:AVPOSition`` command.
        - ``.bhposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:BHPOSition`` command.
        - ``.bposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition`` command.
        - ``.bvposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:BVPOSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ahposition = DisplayReffftviewItemCursorWaveformAhposition(
            device, f"{self._cmd_syntax}:AHPOSition"
        )
        self._aposition = DisplayReffftviewItemCursorWaveformAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._avposition = DisplayReffftviewItemCursorWaveformAvposition(
            device, f"{self._cmd_syntax}:AVPOSition"
        )
        self._bhposition = DisplayReffftviewItemCursorWaveformBhposition(
            device, f"{self._cmd_syntax}:BHPOSition"
        )
        self._bposition = DisplayReffftviewItemCursorWaveformBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )
        self._bvposition = DisplayReffftviewItemCursorWaveformBvposition(
            device, f"{self._cmd_syntax}:BVPOSition"
        )

    @property
    def ahposition(self) -> DisplayReffftviewItemCursorWaveformAhposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:WAVEform:AHPOSition`` command.

        Description:
            - This query-only command returns the value of the cursor A horizontal position.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:AHPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:AHPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:WAVEform:AHPOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._ahposition

    @property
    def aposition(self) -> DisplayReffftviewItemCursorWaveformAposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition`` command.

        Description:
            - Sets or returns the waveform cursor A position in the specified plot view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition <NR3>
            - DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``<NR3>`` is the waveform cursor A position in the specified plot view.
        """
        return self._aposition

    @property
    def avposition(self) -> DisplayReffftviewItemCursorWaveformAvposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:WAVEform:AVPOSition`` command.

        Description:
            - This query-only command returns the value of the cursor A vertical position.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:AVPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:AVPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:WAVEform:AVPOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._avposition

    @property
    def bhposition(self) -> DisplayReffftviewItemCursorWaveformBhposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:WAVEform:BHPOSition`` command.

        Description:
            - This query-only command returns the value of the cursor B horizontal position.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:BHPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:BHPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:WAVEform:BHPOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._bhposition

    @property
    def bposition(self) -> DisplayReffftviewItemCursorWaveformBposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition`` command.

        Description:
            - Sets or returns the waveform cursor B position in the specified plot view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition <NR3>
            - DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``<NR3>`` is the waveform cursor B position in the specified plot view.
        """
        return self._bposition

    @property
    def bvposition(self) -> DisplayReffftviewItemCursorWaveformBvposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:WAVEform:BVPOSition`` command.

        Description:
            - This query-only command returns the value of the cursor B vertical position.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:BVPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform:BVPOSition?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:WAVEform:BVPOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._bvposition


class DisplayReffftviewItemCursorVbarsUnits(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:VBArs:UNIts`` command.

    Description:
        - This command returns cursor A vertical units of the specified cursor in the specified
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:VBArs:UNIts?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:VBArs:UNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:VBArs:UNIts?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorVbarsDelta(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:VBArs:DELTa`` command.

    Description:
        - This command returns the delta T cursor readout value of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:VBArs:DELTa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:VBArs:DELTa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:VBArs:DELTa?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorVbarsBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition`` command.

    Description:
        - This command sets or queries the horizontal cursor B position of the specified cursor in
          the specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition <NR3>
        - DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
          view.
    """


class DisplayReffftviewItemCursorVbarsAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:VBArs:APOSition`` command.

    Description:
        - This command sets or queries the horizontal cursor A position of the specified cursor in
          the specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:VBArs:APOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:VBArs:APOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:VBArs:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:VBArs:APOSition <NR3>
        - DISplay:REFFFTView<x>:CURSor:VBArs:APOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
          view.
    """


class DisplayReffftviewItemCursorVbars(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:VBArs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:VBArs?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:CURSor:VBArs?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.

    Properties:
        - ``.aposition``: The ``DISplay:REFFFTView<x>:CURSor:VBArs:APOSition`` command.
        - ``.bposition``: The ``DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition`` command.
        - ``.delta``: The ``DISplay:REFFFTView<x>:CURSor:VBArs:DELTa`` command.
        - ``.units``: The ``DISplay:REFFFTView<x>:CURSor:VBArs:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aposition = DisplayReffftviewItemCursorVbarsAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._bposition = DisplayReffftviewItemCursorVbarsBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )
        self._delta = DisplayReffftviewItemCursorVbarsDelta(device, f"{self._cmd_syntax}:DELTa")
        self._units = DisplayReffftviewItemCursorVbarsUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def aposition(self) -> DisplayReffftviewItemCursorVbarsAposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:VBArs:APOSition`` command.

        Description:
            - This command sets or queries the horizontal cursor A position of the specified cursor
              in the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:VBArs:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:VBArs:APOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:VBArs:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:VBArs:APOSition <NR3>
            - DISplay:REFFFTView<x>:CURSor:VBArs:APOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
              view.
        """
        return self._aposition

    @property
    def bposition(self) -> DisplayReffftviewItemCursorVbarsBposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition`` command.

        Description:
            - This command sets or queries the horizontal cursor B position of the specified cursor
              in the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition <NR3>
            - DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
              view.
        """
        return self._bposition

    @property
    def delta(self) -> DisplayReffftviewItemCursorVbarsDelta:
        """Return the ``DISplay:REFFFTView<x>:CURSor:VBArs:DELTa`` command.

        Description:
            - This command returns the delta T cursor readout value of the specified cursor in the
              specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:VBArs:DELTa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:VBArs:DELTa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:VBArs:DELTa?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._delta

    @property
    def units(self) -> DisplayReffftviewItemCursorVbarsUnits:
        """Return the ``DISplay:REFFFTView<x>:CURSor:VBArs:UNIts`` command.

        Description:
            - This command returns cursor A vertical units of the specified cursor in the specified
              view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:VBArs:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:VBArs:UNIts?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:VBArs:UNIts?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._units


class DisplayReffftviewItemCursorState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:STATE`` command.

    Description:
        - This command sets or queries the visible state of the cursor of the specified cursor n the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:CURSor:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:STATE value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:STATE {OFF|ON|0|1|<NR1>}
        - DISplay:REFFFTView<x>:CURSor:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 specifies the cursor is not visible; any other value displays the cursor.
        - ``OFF`` specifies the cursor is not visible.
        - ``0`` specifies the cursor is not visible.
        - ``ON`` displays the cursor.
        - ``1`` displays the cursor.
    """


class DisplayReffftviewItemCursorSplitmode(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:SPLITMODE`` command.

    Description:
        - This command sets or queries whether both cursors have same or different source.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:SPLITMODE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SPLITMODE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SPLITMODE value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:SPLITMODE {SAME|SPLIT}
        - DISplay:REFFFTView<x>:CURSor:SPLITMODE?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``SAME`` specifies both cursors have the same sources.
        - ``SPLIT`` specifies both cursors have different sources.
    """


class DisplayReffftviewItemCursorScreenByposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition`` command.

    Description:
        - This command sets or queries the vertical cursor B position of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition <NR3>
        - DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``<NR3>`` is the vertical cursor B position of the specified cursor in the specified view.
    """


class DisplayReffftviewItemCursorScreenBxposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition`` command.

    Description:
        - This command sets or queries the horizontal cursor B position of the specified cursor in
          the specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition <NR3>
        - DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
          view.
    """


class DisplayReffftviewItemCursorScreenAyposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition`` command.

    Description:
        - This command sets or queries the vertical cursor A position of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition <NR3>
        - DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``<NR3>`` is the vertical cursor A position of the specified cursor in the specified view.
    """


class DisplayReffftviewItemCursorScreenAxposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition`` command.

    Description:
        - This command sets or queries the horizontal cursor A position of the specified cursor in
          the specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition <NR3>
        - DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
          view.
    """


class DisplayReffftviewItemCursorScreen(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:SCREEN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:SCREEN?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:CURSor:SCREEN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.

    Properties:
        - ``.axposition``: The ``DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition`` command.
        - ``.ayposition``: The ``DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition`` command.
        - ``.bxposition``: The ``DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition`` command.
        - ``.byposition``: The ``DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._axposition = DisplayReffftviewItemCursorScreenAxposition(
            device, f"{self._cmd_syntax}:AXPOSition"
        )
        self._ayposition = DisplayReffftviewItemCursorScreenAyposition(
            device, f"{self._cmd_syntax}:AYPOSition"
        )
        self._bxposition = DisplayReffftviewItemCursorScreenBxposition(
            device, f"{self._cmd_syntax}:BXPOSition"
        )
        self._byposition = DisplayReffftviewItemCursorScreenByposition(
            device, f"{self._cmd_syntax}:BYPOSition"
        )

    @property
    def axposition(self) -> DisplayReffftviewItemCursorScreenAxposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition`` command.

        Description:
            - This command sets or queries the horizontal cursor A position of the specified cursor
              in the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition <NR3>
            - DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``<NR3>`` is the horizontal cursor A position of the specified cursor in the specified
              view.
        """
        return self._axposition

    @property
    def ayposition(self) -> DisplayReffftviewItemCursorScreenAyposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition`` command.

        Description:
            - This command sets or queries the vertical cursor A position of the specified cursor in
              the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition <NR3>
            - DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``<NR3>`` is the vertical cursor A position of the specified cursor in the specified
              view.
        """
        return self._ayposition

    @property
    def bxposition(self) -> DisplayReffftviewItemCursorScreenBxposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition`` command.

        Description:
            - This command sets or queries the horizontal cursor B position of the specified cursor
              in the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition <NR3>
            - DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
              view.
        """
        return self._bxposition

    @property
    def byposition(self) -> DisplayReffftviewItemCursorScreenByposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition`` command.

        Description:
            - This command sets or queries the vertical cursor B position of the specified cursor in
              the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition <NR3>
            - DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``<NR3>`` is the vertical cursor B position of the specified cursor in the specified
              view.
        """
        return self._byposition


class DisplayReffftviewItemCursorRolocation(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:ROLOCATION`` command.

    Description:
        - This command sets or queries the location to display the specified Reference FFT plot
          cursor readouts (in the plot graticule or in a badge in the Results Bar).

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:ROLOCATION?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:ROLOCATION?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:ROLOCATION value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:ROLOCATION {GRATICULE|BADGE}
        - DISplay:REFFFTView<x>:CURSor:ROLOCATION?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``GRATICULE`` sets the Reference FFT plot cursor readouts to display as part of the
          cursors in the plot view.
        - ``BADGE`` removes the Reference FFT plot cursor readouts from the cursors in the graticule
          and displays the cursor information as a badge in the Results Bar.
    """


class DisplayReffftviewItemCursorOneoverdeltatvalue(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:ONEOVERDELTATVALUE`` command.

    Description:
        - This command returns the one over delta T cursor readout value of the specified cursor in
          the specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:ONEOVERDELTATVALUE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:ONEOVERDELTATVALUE?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:ONEOVERDELTATVALUE?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorMode(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:MODe`` command.

    Description:
        - This command sets or queries the cursor tracking mode of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:CURSor:MODe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:MODe value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:MODe {INDEPENDENT|TRACK}
        - DISplay:REFFFTView<x>:CURSor:MODe?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``TRACK`` ties the navigational functionality of the two cursors together. For cursor A
          adjustments, this ties the movement of the two cursors together; however, cursor B
          continues to move independently of cursor A.
        - ``INDEPENDENT`` allows independent adjustment of the two cursors.
    """


class DisplayReffftviewItemCursorHbarsDelta(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:HBArs:DELTa`` command.

    Description:
        - This command returns the delta V cursor readout value of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:HBArs:DELTa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:HBArs:DELTa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:HBArs:DELTa?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorHbarsBunits(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:HBArs:BUNIts`` command.

    Description:
        - This command returns the cursor B vertical units of the specified cursor in the specified
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:HBArs:BUNIts?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:HBArs:BUNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:HBArs:BUNIts?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorHbarsBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition`` command.

    Description:
        - This command sets or queries the vertical cursor B position of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition <NR3>
        - DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``<NR3>`` is the vertical cursor B position of the specified cursor in the specified view.
    """


class DisplayReffftviewItemCursorHbarsAunits(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:HBArs:AUNIts`` command.

    Description:
        - This command returns cursor A vertical units of the specified cursor in the specified
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:HBArs:AUNIts?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:HBArs:AUNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:HBArs:AUNIts?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorHbarsAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:HBArs:APOSition`` command.

    Description:
        - This command sets or queries the vertical cursor A position of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:HBArs:APOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:HBArs:APOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:HBArs:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:HBArs:APOSition <NR3>
        - DISplay:REFFFTView<x>:CURSor:HBArs:APOSition?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``<NR3>`` is the vertical cursor A position of the specified cursor in the specified view.
    """


class DisplayReffftviewItemCursorHbars(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:HBArs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:HBArs?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:CURSor:HBArs?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.

    Properties:
        - ``.aposition``: The ``DISplay:REFFFTView<x>:CURSor:HBArs:APOSition`` command.
        - ``.aunits``: The ``DISplay:REFFFTView<x>:CURSor:HBArs:AUNIts`` command.
        - ``.bposition``: The ``DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition`` command.
        - ``.bunits``: The ``DISplay:REFFFTView<x>:CURSor:HBArs:BUNIts`` command.
        - ``.delta``: The ``DISplay:REFFFTView<x>:CURSor:HBArs:DELTa`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aposition = DisplayReffftviewItemCursorHbarsAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._aunits = DisplayReffftviewItemCursorHbarsAunits(device, f"{self._cmd_syntax}:AUNIts")
        self._bposition = DisplayReffftviewItemCursorHbarsBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )
        self._bunits = DisplayReffftviewItemCursorHbarsBunits(device, f"{self._cmd_syntax}:BUNIts")
        self._delta = DisplayReffftviewItemCursorHbarsDelta(device, f"{self._cmd_syntax}:DELTa")

    @property
    def aposition(self) -> DisplayReffftviewItemCursorHbarsAposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:HBArs:APOSition`` command.

        Description:
            - This command sets or queries the vertical cursor A position of the specified cursor in
              the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:APOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:HBArs:APOSition <NR3>
            - DISplay:REFFFTView<x>:CURSor:HBArs:APOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``<NR3>`` is the vertical cursor A position of the specified cursor in the specified
              view.
        """
        return self._aposition

    @property
    def aunits(self) -> DisplayReffftviewItemCursorHbarsAunits:
        """Return the ``DISplay:REFFFTView<x>:CURSor:HBArs:AUNIts`` command.

        Description:
            - This command returns cursor A vertical units of the specified cursor in the specified
              view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:AUNIts?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:AUNIts?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:HBArs:AUNIts?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._aunits

    @property
    def bposition(self) -> DisplayReffftviewItemCursorHbarsBposition:
        """Return the ``DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition`` command.

        Description:
            - This command sets or queries the vertical cursor B position of the specified cursor in
              the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition <NR3>
            - DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``<NR3>`` is the vertical cursor B position of the specified cursor in the specified
              view.
        """
        return self._bposition

    @property
    def bunits(self) -> DisplayReffftviewItemCursorHbarsBunits:
        """Return the ``DISplay:REFFFTView<x>:CURSor:HBArs:BUNIts`` command.

        Description:
            - This command returns the cursor B vertical units of the specified cursor in the
              specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:BUNIts?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:BUNIts?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:HBArs:BUNIts?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._bunits

    @property
    def delta(self) -> DisplayReffftviewItemCursorHbarsDelta:
        """Return the ``DISplay:REFFFTView<x>:CURSor:HBArs:DELTa`` command.

        Description:
            - This command returns the delta V cursor readout value of the specified cursor in the
              specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:DELTa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs:DELTa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:HBArs:DELTa?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._delta


class DisplayReffftviewItemCursorFunction(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:FUNCtion`` command.

    Description:
        - This command sets or queries the cursor type of the specified cursor in the specified
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:FUNCtion?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:FUNCtion?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:FUNCtion {WAVEform|VBArs|HBArs|SCREEN}
        - DISplay:REFFFTView<x>:CURSor:FUNCtion?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
        - ``HBArs`` specifies horizontal bar cursors, which measure in vertical units.
        - ``VBArs`` specifies vertical bar cursors, which measure in horizontal units.
        - ``SCREEN`` specifies both horizontal and vertical bar cursors, which measure in horizontal
          and vertical units specified by the cursor sources. Use these cursors to measure anywhere
          in the waveform display area.
        - ``WAVEform`` specifies paired or split cursors in YT display format for measuring waveform
          amplitude and time. In XY and XYZ format, these cursors indicate the amplitude positions
          of an XY pair (Ch1 vs Ch2 voltage, where Ch1 is the X axis and Ch2 is the Y axis) relative
          to the trigger.
    """


class DisplayReffftviewItemCursorDdt(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:DDT`` command.

    Description:
        - This command returns the delta V over delta T cursor readout value of the specified cursor
          in the specified view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:DDT?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:CURSor:DDT?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:DDT?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorBsource(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:BSOUrce`` command.

    Description:
        - This command returns the cursor source for plot cursor B.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:BSOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:BSOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:BSOUrce?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


class DisplayReffftviewItemCursorAsource(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor:ASOUrce`` command.

    Description:
        - This command returns the cursor source for plot cursor A

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:ASOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:REFFFTView<x>:CURSor:ASOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:CURSor:ASOUrce?
        ```

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.
    """


#  pylint: disable=too-many-instance-attributes
class DisplayReffftviewItemCursor(SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:CURSor`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:CURSor?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``REFFFTView<x>`` is the Reference FFT plot number.

    Properties:
        - ``.asource``: The ``DISplay:REFFFTView<x>:CURSor:ASOUrce`` command.
        - ``.bsource``: The ``DISplay:REFFFTView<x>:CURSor:BSOUrce`` command.
        - ``.ddt``: The ``DISplay:REFFFTView<x>:CURSor:DDT`` command.
        - ``.function``: The ``DISplay:REFFFTView<x>:CURSor:FUNCtion`` command.
        - ``.hbars``: The ``DISplay:REFFFTView<x>:CURSor:HBArs`` command tree.
        - ``.mode``: The ``DISplay:REFFFTView<x>:CURSor:MODe`` command.
        - ``.oneoverdeltatvalue``: The ``DISplay:REFFFTView<x>:CURSor:ONEOVERDELTATVALUE`` command.
        - ``.rolocation``: The ``DISplay:REFFFTView<x>:CURSor:ROLOCATION`` command.
        - ``.screen``: The ``DISplay:REFFFTView<x>:CURSor:SCREEN`` command tree.
        - ``.splitmode``: The ``DISplay:REFFFTView<x>:CURSor:SPLITMODE`` command.
        - ``.state``: The ``DISplay:REFFFTView<x>:CURSor:STATE`` command.
        - ``.vbars``: The ``DISplay:REFFFTView<x>:CURSor:VBArs`` command tree.
        - ``.waveform``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._asource = DisplayReffftviewItemCursorAsource(device, f"{self._cmd_syntax}:ASOUrce")
        self._bsource = DisplayReffftviewItemCursorBsource(device, f"{self._cmd_syntax}:BSOUrce")
        self._ddt = DisplayReffftviewItemCursorDdt(device, f"{self._cmd_syntax}:DDT")
        self._function = DisplayReffftviewItemCursorFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._hbars = DisplayReffftviewItemCursorHbars(device, f"{self._cmd_syntax}:HBArs")
        self._mode = DisplayReffftviewItemCursorMode(device, f"{self._cmd_syntax}:MODe")
        self._oneoverdeltatvalue = DisplayReffftviewItemCursorOneoverdeltatvalue(
            device, f"{self._cmd_syntax}:ONEOVERDELTATVALUE"
        )
        self._rolocation = DisplayReffftviewItemCursorRolocation(
            device, f"{self._cmd_syntax}:ROLOCATION"
        )
        self._screen = DisplayReffftviewItemCursorScreen(device, f"{self._cmd_syntax}:SCREEN")
        self._splitmode = DisplayReffftviewItemCursorSplitmode(
            device, f"{self._cmd_syntax}:SPLITMODE"
        )
        self._state = DisplayReffftviewItemCursorState(device, f"{self._cmd_syntax}:STATE")
        self._vbars = DisplayReffftviewItemCursorVbars(device, f"{self._cmd_syntax}:VBArs")
        self._waveform = DisplayReffftviewItemCursorWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def asource(self) -> DisplayReffftviewItemCursorAsource:
        """Return the ``DISplay:REFFFTView<x>:CURSor:ASOUrce`` command.

        Description:
            - This command returns the cursor source for plot cursor A

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:ASOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:ASOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:ASOUrce?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._asource

    @property
    def bsource(self) -> DisplayReffftviewItemCursorBsource:
        """Return the ``DISplay:REFFFTView<x>:CURSor:BSOUrce`` command.

        Description:
            - This command returns the cursor source for plot cursor B.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:BSOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:BSOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:BSOUrce?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._bsource

    @property
    def ddt(self) -> DisplayReffftviewItemCursorDdt:
        """Return the ``DISplay:REFFFTView<x>:CURSor:DDT`` command.

        Description:
            - This command returns the delta V over delta T cursor readout value of the specified
              cursor in the specified view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:DDT?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:DDT?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:DDT?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._ddt

    @property
    def function(self) -> DisplayReffftviewItemCursorFunction:
        """Return the ``DISplay:REFFFTView<x>:CURSor:FUNCtion`` command.

        Description:
            - This command sets or queries the cursor type of the specified cursor in the specified
              view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:FUNCtion?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:FUNCtion?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:FUNCtion {WAVEform|VBArs|HBArs|SCREEN}
            - DISplay:REFFFTView<x>:CURSor:FUNCtion?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``HBArs`` specifies horizontal bar cursors, which measure in vertical units.
            - ``VBArs`` specifies vertical bar cursors, which measure in horizontal units.
            - ``SCREEN`` specifies both horizontal and vertical bar cursors, which measure in
              horizontal and vertical units specified by the cursor sources. Use these cursors to
              measure anywhere in the waveform display area.
            - ``WAVEform`` specifies paired or split cursors in YT display format for measuring
              waveform amplitude and time. In XY and XYZ format, these cursors indicate the
              amplitude positions of an XY pair (Ch1 vs Ch2 voltage, where Ch1 is the X axis and Ch2
              is the Y axis) relative to the trigger.
        """
        return self._function

    @property
    def hbars(self) -> DisplayReffftviewItemCursorHbars:
        """Return the ``DISplay:REFFFTView<x>:CURSor:HBArs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:HBArs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:HBArs?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.

        Sub-properties:
            - ``.aposition``: The ``DISplay:REFFFTView<x>:CURSor:HBArs:APOSition`` command.
            - ``.aunits``: The ``DISplay:REFFFTView<x>:CURSor:HBArs:AUNIts`` command.
            - ``.bposition``: The ``DISplay:REFFFTView<x>:CURSor:HBArs:BPOSition`` command.
            - ``.bunits``: The ``DISplay:REFFFTView<x>:CURSor:HBArs:BUNIts`` command.
            - ``.delta``: The ``DISplay:REFFFTView<x>:CURSor:HBArs:DELTa`` command.
        """
        return self._hbars

    @property
    def mode(self) -> DisplayReffftviewItemCursorMode:
        """Return the ``DISplay:REFFFTView<x>:CURSor:MODe`` command.

        Description:
            - This command sets or queries the cursor tracking mode of the specified cursor in the
              specified view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:MODe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:MODe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:MODe value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:MODe {INDEPENDENT|TRACK}
            - DISplay:REFFFTView<x>:CURSor:MODe?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``TRACK`` ties the navigational functionality of the two cursors together. For cursor
              A adjustments, this ties the movement of the two cursors together; however, cursor B
              continues to move independently of cursor A.
            - ``INDEPENDENT`` allows independent adjustment of the two cursors.
        """
        return self._mode

    @property
    def oneoverdeltatvalue(self) -> DisplayReffftviewItemCursorOneoverdeltatvalue:
        """Return the ``DISplay:REFFFTView<x>:CURSor:ONEOVERDELTATVALUE`` command.

        Description:
            - This command returns the one over delta T cursor readout value of the specified cursor
              in the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:ONEOVERDELTATVALUE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:ONEOVERDELTATVALUE?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:ONEOVERDELTATVALUE?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
        """
        return self._oneoverdeltatvalue

    @property
    def rolocation(self) -> DisplayReffftviewItemCursorRolocation:
        """Return the ``DISplay:REFFFTView<x>:CURSor:ROLOCATION`` command.

        Description:
            - This command sets or queries the location to display the specified Reference FFT plot
              cursor readouts (in the plot graticule or in a badge in the Results Bar).

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:ROLOCATION?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:ROLOCATION?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:ROLOCATION value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:ROLOCATION {GRATICULE|BADGE}
            - DISplay:REFFFTView<x>:CURSor:ROLOCATION?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``GRATICULE`` sets the Reference FFT plot cursor readouts to display as part of the
              cursors in the plot view.
            - ``BADGE`` removes the Reference FFT plot cursor readouts from the cursors in the
              graticule and displays the cursor information as a badge in the Results Bar.
        """
        return self._rolocation

    @property
    def screen(self) -> DisplayReffftviewItemCursorScreen:
        """Return the ``DISplay:REFFFTView<x>:CURSor:SCREEN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:SCREEN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SCREEN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.

        Sub-properties:
            - ``.axposition``: The ``DISplay:REFFFTView<x>:CURSor:SCREEN:AXPOSition`` command.
            - ``.ayposition``: The ``DISplay:REFFFTView<x>:CURSor:SCREEN:AYPOSition`` command.
            - ``.bxposition``: The ``DISplay:REFFFTView<x>:CURSor:SCREEN:BXPOSition`` command.
            - ``.byposition``: The ``DISplay:REFFFTView<x>:CURSor:SCREEN:BYPOSition`` command.
        """
        return self._screen

    @property
    def splitmode(self) -> DisplayReffftviewItemCursorSplitmode:
        """Return the ``DISplay:REFFFTView<x>:CURSor:SPLITMODE`` command.

        Description:
            - This command sets or queries whether both cursors have same or different source.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SPLITMODE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SPLITMODE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:SPLITMODE value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:SPLITMODE {SAME|SPLIT}
            - DISplay:REFFFTView<x>:CURSor:SPLITMODE?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``SAME`` specifies both cursors have the same sources.
            - ``SPLIT`` specifies both cursors have different sources.
        """
        return self._splitmode

    @property
    def state(self) -> DisplayReffftviewItemCursorState:
        """Return the ``DISplay:REFFFTView<x>:CURSor:STATE`` command.

        Description:
            - This command sets or queries the visible state of the cursor of the specified cursor n
              the specified view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:CURSor:STATE {OFF|ON|0|1|<NR1>}
            - DISplay:REFFFTView<x>:CURSor:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 specifies the cursor is not visible; any other value displays the
              cursor.
            - ``OFF`` specifies the cursor is not visible.
            - ``0`` specifies the cursor is not visible.
            - ``ON`` displays the cursor.
            - ``1`` displays the cursor.
        """
        return self._state

    @property
    def vbars(self) -> DisplayReffftviewItemCursorVbars:
        """Return the ``DISplay:REFFFTView<x>:CURSor:VBArs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:VBArs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:VBArs?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.

        Sub-properties:
            - ``.aposition``: The ``DISplay:REFFFTView<x>:CURSor:VBArs:APOSition`` command.
            - ``.bposition``: The ``DISplay:REFFFTView<x>:CURSor:VBArs:BPOSition`` command.
            - ``.delta``: The ``DISplay:REFFFTView<x>:CURSor:VBArs:DELTa`` command.
            - ``.units``: The ``DISplay:REFFFTView<x>:CURSor:VBArs:UNIts`` command.
        """
        return self._vbars

    @property
    def waveform(self) -> DisplayReffftviewItemCursorWaveform:
        """Return the ``DISplay:REFFFTView<x>:CURSor:WAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor:WAVEform?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:REFFFTView<x>:CURSor:WAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.

        Sub-properties:
            - ``.ahposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:AHPOSition`` command.
            - ``.aposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:APOSition`` command.
            - ``.avposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:AVPOSition`` command.
            - ``.bhposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:BHPOSition`` command.
            - ``.bposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:BPOSition`` command.
            - ``.bvposition``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform:BVPOSition`` command.
        """
        return self._waveform


class DisplayReffftviewItemAutoscale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>:AUTOScale`` command.

    Description:
        - This command sets or queries the enabled state of auto-scale for plots.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:AUTOScale?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:AUTOScale?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:REFFFTView<x>:AUTOScale value``
          command.

    SCPI Syntax:
        ```
        - DISplay:REFFFTView<x>:AUTOScale {OFF|ON|0|1|<NR1>}
        - DISplay:REFFFTView<x>:AUTOScale?
        ```

    Info:
        - ``REFFFTView<x>`` is the plot number.
        - ``<NR1>`` = 0 disables auto-scale on the specified reffftview; any other value turns this
          feature on.
        - ``OFF`` disables auto-scale on the specified reffftview.
        - ``0`` disables auto-scale on the specified reffftview.
        - ``ON`` enables the specified channel on the specified Waveform View.
        - ``1`` enables the specified channel on the specified Waveform View.
    """


class DisplayReffftviewItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:REFFFTView<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``REFFFTView<x>`` is the plot number.

    Properties:
        - ``.autoscale``: The ``DISplay:REFFFTView<x>:AUTOScale`` command.
        - ``.cursor``: The ``DISplay:REFFFTView<x>:CURSor`` command tree.
        - ``.gridlines``: The ``DISplay:REFFFTView<x>:GRIDlines`` command.
        - ``.ref``: The ``DISplay:REFFFTView<x>:REF`` command tree.
        - ``.xaxis``: The ``DISplay:REFFFTView<x>:XAXIS`` command tree.
        - ``.zoom``: The ``DISplay:REFFFTView<x>:ZOOM`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoscale = DisplayReffftviewItemAutoscale(device, f"{self._cmd_syntax}:AUTOScale")
        self._cursor = DisplayReffftviewItemCursor(device, f"{self._cmd_syntax}:CURSor")
        self._gridlines = DisplayReffftviewItemGridlines(device, f"{self._cmd_syntax}:GRIDlines")
        self._ref = DisplayReffftviewItemRef(device, f"{self._cmd_syntax}:REF")
        self._xaxis = DisplayReffftviewItemXaxis(device, f"{self._cmd_syntax}:XAXIS")
        self._zoom = DisplayReffftviewItemZoom(device, f"{self._cmd_syntax}:ZOOM")

    @property
    def autoscale(self) -> DisplayReffftviewItemAutoscale:
        """Return the ``DISplay:REFFFTView<x>:AUTOScale`` command.

        Description:
            - This command sets or queries the enabled state of auto-scale for plots.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:AUTOScale?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:AUTOScale?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:AUTOScale value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:AUTOScale {OFF|ON|0|1|<NR1>}
            - DISplay:REFFFTView<x>:AUTOScale?
            ```

        Info:
            - ``REFFFTView<x>`` is the plot number.
            - ``<NR1>`` = 0 disables auto-scale on the specified reffftview; any other value turns
              this feature on.
            - ``OFF`` disables auto-scale on the specified reffftview.
            - ``0`` disables auto-scale on the specified reffftview.
            - ``ON`` enables the specified channel on the specified Waveform View.
            - ``1`` enables the specified channel on the specified Waveform View.
        """
        return self._autoscale

    @property
    def cursor(self) -> DisplayReffftviewItemCursor:
        """Return the ``DISplay:REFFFTView<x>:CURSor`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:CURSor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:CURSor?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.

        Sub-properties:
            - ``.asource``: The ``DISplay:REFFFTView<x>:CURSor:ASOUrce`` command.
            - ``.bsource``: The ``DISplay:REFFFTView<x>:CURSor:BSOUrce`` command.
            - ``.ddt``: The ``DISplay:REFFFTView<x>:CURSor:DDT`` command.
            - ``.function``: The ``DISplay:REFFFTView<x>:CURSor:FUNCtion`` command.
            - ``.hbars``: The ``DISplay:REFFFTView<x>:CURSor:HBArs`` command tree.
            - ``.mode``: The ``DISplay:REFFFTView<x>:CURSor:MODe`` command.
            - ``.oneoverdeltatvalue``: The ``DISplay:REFFFTView<x>:CURSor:ONEOVERDELTATVALUE``
              command.
            - ``.rolocation``: The ``DISplay:REFFFTView<x>:CURSor:ROLOCATION`` command.
            - ``.screen``: The ``DISplay:REFFFTView<x>:CURSor:SCREEN`` command tree.
            - ``.splitmode``: The ``DISplay:REFFFTView<x>:CURSor:SPLITMODE`` command.
            - ``.state``: The ``DISplay:REFFFTView<x>:CURSor:STATE`` command.
            - ``.vbars``: The ``DISplay:REFFFTView<x>:CURSor:VBArs`` command tree.
            - ``.waveform``: The ``DISplay:REFFFTView<x>:CURSor:WAVEform`` command tree.
        """
        return self._cursor

    @property
    def gridlines(self) -> DisplayReffftviewItemGridlines:
        """Return the ``DISplay:REFFFTView<x>:GRIDlines`` command.

        Description:
            - This command sets or returns the grid lines setting of the plot.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:GRIDlines?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:GRIDlines?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:REFFFTView<x>:GRIDlines value`` command.

        SCPI Syntax:
            ```
            - DISplay:REFFFTView<x>:GRIDlines {HORizontal|VERTical|BOTH}
            - DISplay:REFFFTView<x>:GRIDlines?
            ```

        Info:
            - ``REFFFTView<x>`` is the Reference FFT plot number.
            - ``HORizontal`` specifies horizontal grid lines.
            - ``VERTical`` specifies vertical grid lines.
            - ``BOTH`` specifies both horizontal and vertical grid lines.
        """
        return self._gridlines

    @property
    def ref(self) -> DisplayReffftviewItemRef:
        """Return the ``DISplay:REFFFTView<x>:REF`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:REF?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:REF?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ref``: The ``DISplay:REFFFTView<x>:REF:REF<x>`` command tree.
        """
        return self._ref

    @property
    def xaxis(self) -> DisplayReffftviewItemXaxis:
        """Return the ``DISplay:REFFFTView<x>:XAXIS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:XAXIS?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:XAXIS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DISplay:REFFFTView<x>:XAXIS:SCALE`` command.
        """
        return self._xaxis

    @property
    def zoom(self) -> DisplayReffftviewItemZoom:
        """Return the ``DISplay:REFFFTView<x>:ZOOM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>:ZOOM?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>:ZOOM?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.xaxis``: The ``DISplay:REFFFTView<x>:ZOOM:XAXIS`` command tree.
            - ``.yaxis``: The ``DISplay:REFFFTView<x>:ZOOM:YAXIS`` command tree.
        """
        return self._zoom


class DisplayRefItemNormalcolor(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REF<x>:NORMALColor`` command.

    Description:
        - This command sets or queries the normal mode color of the specified input source to the
          specified color. You can assign one of 48 unique colors to any channel, math, or reference
          waveform. These colors replace the default normal colors and remain in effect until you
          reset the colors.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REF<x>:NORMALColor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REF<x>:NORMALColor?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:REF<x>:NORMALColor value``
          command.

    SCPI Syntax:
        ```
        - DISplay:REF<x>:NORMALColor COLOR<y>
        - DISplay:REF<x>:NORMALColor?
        ```

    Info:
        - ``REF<x>`` specifies the reference waveform for which you want to change the waveform
          color, where <x> is the reference waveform number.
        - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to 47.
    """


class DisplayRefItemInvertcolor(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:REF<x>:INVERTColor`` command.

    Description:
        - This command sets or queries the Inverted mode color of the specified input source to the
          specified color. You can assign one of 48 unique colors to any channel, math, or reference
          waveform. These colors replace the default Inverted colors and remain in effect until you
          reset the colors.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REF<x>:INVERTColor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REF<x>:INVERTColor?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:REF<x>:INVERTColor value``
          command.

    SCPI Syntax:
        ```
        - DISplay:REF<x>:INVERTColor COLOR<y>
        - DISplay:REF<x>:INVERTColor?
        ```

    Info:
        - ``REF<x>`` specifies the reference waveform for which you want to change the waveform
          color, where <x> is the reference waveform number.
        - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to 47.
    """


class DisplayRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:REF<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``REF<x>`` specifies the reference waveform for which you want to change the waveform
          color, where <x> is the reference waveform number.

    Properties:
        - ``.invertcolor``: The ``DISplay:REF<x>:INVERTColor`` command.
        - ``.normalcolor``: The ``DISplay:REF<x>:NORMALColor`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._invertcolor = DisplayRefItemInvertcolor(device, f"{self._cmd_syntax}:INVERTColor")
        self._normalcolor = DisplayRefItemNormalcolor(device, f"{self._cmd_syntax}:NORMALColor")

    @property
    def invertcolor(self) -> DisplayRefItemInvertcolor:
        """Return the ``DISplay:REF<x>:INVERTColor`` command.

        Description:
            - This command sets or queries the Inverted mode color of the specified input source to
              the specified color. You can assign one of 48 unique colors to any channel, math, or
              reference waveform. These colors replace the default Inverted colors and remain in
              effect until you reset the colors.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REF<x>:INVERTColor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:REF<x>:INVERTColor?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:REF<x>:INVERTColor value``
              command.

        SCPI Syntax:
            ```
            - DISplay:REF<x>:INVERTColor COLOR<y>
            - DISplay:REF<x>:INVERTColor?
            ```

        Info:
            - ``REF<x>`` specifies the reference waveform for which you want to change the waveform
              color, where <x> is the reference waveform number.
            - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to
              47.
        """
        return self._invertcolor

    @property
    def normalcolor(self) -> DisplayRefItemNormalcolor:
        """Return the ``DISplay:REF<x>:NORMALColor`` command.

        Description:
            - This command sets or queries the normal mode color of the specified input source to
              the specified color. You can assign one of 48 unique colors to any channel, math, or
              reference waveform. These colors replace the default normal colors and remain in
              effect until you reset the colors.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REF<x>:NORMALColor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:REF<x>:NORMALColor?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:REF<x>:NORMALColor value``
              command.

        SCPI Syntax:
            ```
            - DISplay:REF<x>:NORMALColor COLOR<y>
            - DISplay:REF<x>:NORMALColor?
            ```

        Info:
            - ``REF<x>`` specifies the reference waveform for which you want to change the waveform
              color, where <x> is the reference waveform number.
            - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to
              47.
        """
        return self._normalcolor


class DisplayPlotview1ZoomYaxisTo(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:ZOOM:YAXIS:TO`` command.

    Description:
        - This command sets or queries the top value of the zoom y-axis in the specified plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS:TO?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS:TO?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS:TO value``
          command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:ZOOM:YAXIS:TO <NR3>
        - DISplay:PLOTView1:ZOOM:YAXIS:TO?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the top value of the zoom y-axis.
    """


class DisplayPlotview1ZoomYaxisFrom(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:ZOOM:YAXIS:FROM`` command.

    Description:
        - This command sets or queries the bottom value of the zoom y-axis in the specified plot
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS:FROM?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS:FROM?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:ZOOM:YAXIS:FROM value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:ZOOM:YAXIS:FROM <NR3>
        - DISplay:PLOTView1:ZOOM:YAXIS:FROM?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the bottom value of the zoom y-axis.
    """


class DisplayPlotview1ZoomYaxis(SCPICmdRead):
    """The ``DISplay:PLOTView1:ZOOM:YAXIS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.from``: The ``DISplay:PLOTView1:ZOOM:YAXIS:FROM`` command.
        - ``.to``: The ``DISplay:PLOTView1:ZOOM:YAXIS:TO`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._from = DisplayPlotview1ZoomYaxisFrom(device, f"{self._cmd_syntax}:FROM")
        self._to = DisplayPlotview1ZoomYaxisTo(device, f"{self._cmd_syntax}:TO")

    @property
    def from_(self) -> DisplayPlotview1ZoomYaxisFrom:
        """Return the ``DISplay:PLOTView1:ZOOM:YAXIS:FROM`` command.

        Description:
            - This command sets or queries the bottom value of the zoom y-axis in the specified plot
              view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS:FROM?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:ZOOM:YAXIS:FROM?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:ZOOM:YAXIS:FROM value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:ZOOM:YAXIS:FROM <NR3>
            - DISplay:PLOTView1:ZOOM:YAXIS:FROM?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the bottom value of the zoom y-axis.
        """
        return self._from

    @property
    def to(self) -> DisplayPlotview1ZoomYaxisTo:
        """Return the ``DISplay:PLOTView1:ZOOM:YAXIS:TO`` command.

        Description:
            - This command sets or queries the top value of the zoom y-axis in the specified plot
              view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS:TO?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS:TO?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:ZOOM:YAXIS:TO value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:ZOOM:YAXIS:TO <NR3>
            - DISplay:PLOTView1:ZOOM:YAXIS:TO?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the top value of the zoom y-axis.
        """
        return self._to


class DisplayPlotview1ZoomXaxisTo(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:ZOOM:XAXIS:TO`` command.

    Description:
        - This command sets or queries the value of the right edge of the specified plot.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS:TO?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS:TO?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS:TO value``
          command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:ZOOM:XAXIS:TO <NR3>
        - DISplay:PLOTView1:ZOOM:XAXIS:TO?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the end of the zoom x-axis.
    """


class DisplayPlotview1ZoomXaxisFrom(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:ZOOM:XAXIS:FROM`` command.

    Description:
        - This command sets or queries the value of the left edge of the specified plot.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS:FROM?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS:FROM?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:ZOOM:XAXIS:FROM value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:ZOOM:XAXIS:FROM <NR3>
        - DISplay:PLOTView1:ZOOM:XAXIS:FROM?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is start of the zoom x-axis.
    """


class DisplayPlotview1ZoomXaxis(SCPICmdRead):
    """The ``DISplay:PLOTView1:ZOOM:XAXIS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.from``: The ``DISplay:PLOTView1:ZOOM:XAXIS:FROM`` command.
        - ``.to``: The ``DISplay:PLOTView1:ZOOM:XAXIS:TO`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._from = DisplayPlotview1ZoomXaxisFrom(device, f"{self._cmd_syntax}:FROM")
        self._to = DisplayPlotview1ZoomXaxisTo(device, f"{self._cmd_syntax}:TO")

    @property
    def from_(self) -> DisplayPlotview1ZoomXaxisFrom:
        """Return the ``DISplay:PLOTView1:ZOOM:XAXIS:FROM`` command.

        Description:
            - This command sets or queries the value of the left edge of the specified plot.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS:FROM?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:ZOOM:XAXIS:FROM?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:ZOOM:XAXIS:FROM value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:ZOOM:XAXIS:FROM <NR3>
            - DISplay:PLOTView1:ZOOM:XAXIS:FROM?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is start of the zoom x-axis.
        """
        return self._from

    @property
    def to(self) -> DisplayPlotview1ZoomXaxisTo:
        """Return the ``DISplay:PLOTView1:ZOOM:XAXIS:TO`` command.

        Description:
            - This command sets or queries the value of the right edge of the specified plot.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS:TO?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS:TO?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:ZOOM:XAXIS:TO value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:ZOOM:XAXIS:TO <NR3>
            - DISplay:PLOTView1:ZOOM:XAXIS:TO?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the end of the zoom x-axis.
        """
        return self._to


class DisplayPlotview1Zoom(SCPICmdRead):
    """The ``DISplay:PLOTView1:ZOOM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.xaxis``: The ``DISplay:PLOTView1:ZOOM:XAXIS`` command tree.
        - ``.yaxis``: The ``DISplay:PLOTView1:ZOOM:YAXIS`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._xaxis = DisplayPlotview1ZoomXaxis(device, f"{self._cmd_syntax}:XAXIS")
        self._yaxis = DisplayPlotview1ZoomYaxis(device, f"{self._cmd_syntax}:YAXIS")

    @property
    def xaxis(self) -> DisplayPlotview1ZoomXaxis:
        """Return the ``DISplay:PLOTView1:ZOOM:XAXIS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM:XAXIS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.from``: The ``DISplay:PLOTView1:ZOOM:XAXIS:FROM`` command.
            - ``.to``: The ``DISplay:PLOTView1:ZOOM:XAXIS:TO`` command.
        """
        return self._xaxis

    @property
    def yaxis(self) -> DisplayPlotview1ZoomYaxis:
        """Return the ``DISplay:PLOTView1:ZOOM:YAXIS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM:YAXIS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.from``: The ``DISplay:PLOTView1:ZOOM:YAXIS:FROM`` command.
            - ``.to``: The ``DISplay:PLOTView1:ZOOM:YAXIS:TO`` command.
        """
        return self._yaxis


class DisplayPlotview1YaxisScale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:YAXIS:SCALE`` command.

    Description:
        - This command sets or queries the vertical scale setting for applicable plots (Linear or
          Log) in the specified plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:YAXIS:SCALE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:YAXIS:SCALE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PLOTView1:YAXIS:SCALE value``
          command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:YAXIS:SCALE {LINEAR|LOG}
        - DISplay:PLOTView1:YAXIS:SCALE?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``LINEAR`` specifies a linear vertical scale.
        - ``LOG`` specifies a logarithmic vertical scale.
    """


class DisplayPlotview1Yaxis(SCPICmdRead):
    """The ``DISplay:PLOTView1:YAXIS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:YAXIS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:YAXIS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DISplay:PLOTView1:YAXIS:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DisplayPlotview1YaxisScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DisplayPlotview1YaxisScale:
        """Return the ``DISplay:PLOTView1:YAXIS:SCALE`` command.

        Description:
            - This command sets or queries the vertical scale setting for applicable plots (Linear
              or Log) in the specified plot view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:YAXIS:SCALE?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:YAXIS:SCALE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:YAXIS:SCALE value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:YAXIS:SCALE {LINEAR|LOG}
            - DISplay:PLOTView1:YAXIS:SCALE?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``LINEAR`` specifies a linear vertical scale.
            - ``LOG`` specifies a logarithmic vertical scale.
        """
        return self._scale


class DisplayPlotview1XaxisScale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:XAXIS:SCALE`` command.

    Description:
        - This command sets or queries the horizontal scale setting for applicable plots (Linear or
          Log) for the specified plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:XAXIS:SCALE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:XAXIS:SCALE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PLOTView1:XAXIS:SCALE value``
          command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:XAXIS:SCALE {LINEAR|LOG}
        - DISplay:PLOTView1:XAXIS:SCALE?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``LINEAR`` creates a plot with linear scales.
        - ``LOG`` creates a plot with logarithmic scales.
    """


class DisplayPlotview1Xaxis(SCPICmdRead):
    """The ``DISplay:PLOTView1:XAXIS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:XAXIS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:XAXIS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DISplay:PLOTView1:XAXIS:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DisplayPlotview1XaxisScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DisplayPlotview1XaxisScale:
        """Return the ``DISplay:PLOTView1:XAXIS:SCALE`` command.

        Description:
            - This command sets or queries the horizontal scale setting for applicable plots (Linear
              or Log) for the specified plot view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:XAXIS:SCALE?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:XAXIS:SCALE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:XAXIS:SCALE value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:XAXIS:SCALE {LINEAR|LOG}
            - DISplay:PLOTView1:XAXIS:SCALE?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``LINEAR`` creates a plot with linear scales.
            - ``LOG`` creates a plot with logarithmic scales.
        """
        return self._scale


class DisplayPlotview1Gridlines(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:GRIDlines`` command.

    Description:
        - This command sets or queries the Grid (graticule) lines setting of the specified plot.
          This command works for plots that have vertical and horizontal units associated with the
          graticule. For example, this command does not work for XY or XYZ plots.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:GRIDlines?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:GRIDlines?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PLOTView1:GRIDlines value``
          command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:GRIDlines {HORizontal|VERTical|BOTH}
        - DISplay:PLOTView1:GRIDlines?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``HORizontal`` specifies horizontal grid lines.
        - ``VERTical`` specifies vertical grid lines.
        - ``BOTH`` specifies both vertical and horizontal grid lines.
    """


class DisplayPlotview1CursorWaveformBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:WAVEform:BPOSition`` command.

    Description:
        - This command sets or queries the waveform cursor B horizontal position of the specified
          cursor in the specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:PLOTView1:CURSor:WAVEform:BPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:WAVEform:BPOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:WAVEform:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:WAVEform:BPOSition <NR3>
        - DISplay:PLOTView1:CURSor:WAVEform:BPOSition?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the horizontal cursor B position.
    """


class DisplayPlotview1CursorWaveformAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:WAVEform:APOSition`` command.

    Description:
        - This command sets or queries the waveform cursor A horizontal position of the specified
          cursor in the specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:PLOTView1:CURSor:WAVEform:APOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:WAVEform:APOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:WAVEform:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:WAVEform:APOSition <NR3>
        - DISplay:PLOTView1:CURSor:WAVEform:APOSition?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the horizontal cursor A position.
    """


class DisplayPlotview1CursorWaveform(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:WAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:WAVEform?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.aposition``: The ``DISplay:PLOTView1:CURSor:WAVEform:APOSition`` command.
        - ``.bposition``: The ``DISplay:PLOTView1:CURSor:WAVEform:BPOSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aposition = DisplayPlotview1CursorWaveformAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._bposition = DisplayPlotview1CursorWaveformBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )

    @property
    def aposition(self) -> DisplayPlotview1CursorWaveformAposition:
        """Return the ``DISplay:PLOTView1:CURSor:WAVEform:APOSition`` command.

        Description:
            - This command sets or queries the waveform cursor A horizontal position of the
              specified cursor in the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:PLOTView1:CURSor:WAVEform:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:WAVEform:APOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:WAVEform:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:WAVEform:APOSition <NR3>
            - DISplay:PLOTView1:CURSor:WAVEform:APOSition?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the horizontal cursor A position.
        """
        return self._aposition

    @property
    def bposition(self) -> DisplayPlotview1CursorWaveformBposition:
        """Return the ``DISplay:PLOTView1:CURSor:WAVEform:BPOSition`` command.

        Description:
            - This command sets or queries the waveform cursor B horizontal position of the
              specified cursor in the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:PLOTView1:CURSor:WAVEform:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:WAVEform:BPOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:WAVEform:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:WAVEform:BPOSition <NR3>
            - DISplay:PLOTView1:CURSor:WAVEform:BPOSition?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the horizontal cursor B position.
        """
        return self._bposition


class DisplayPlotview1CursorVbarsUnits(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:VBArs:UNIts`` command.

    Description:
        - This command queries the VBArs cursor readout units of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:VBArs:UNIts?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:VBArs:UNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:VBArs:UNIts?
        ```

    Info:
        - ``1`` is the Plot waveform number.
    """


class DisplayPlotview1CursorVbarsDelta(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:VBArs:DELTa`` command.

    Description:
        - This command queries the delta T cursor readout value of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:VBArs:DELTa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:VBArs:DELTa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:VBArs:DELTa?
        ```

    Info:
        - ``1`` is the Plot waveform number.
    """


class DisplayPlotview1CursorVbarsBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:VBArs:BPOSition`` command.

    Description:
        - This command sets or queries the vertical cursor B position of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:VBArs:BPOSition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:VBArs:BPOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:VBArs:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:VBArs:BPOSition <NR3>
        - DISplay:PLOTView1:CURSor:VBArs:BPOSition?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the vertical cursor B position.
    """


class DisplayPlotview1CursorVbarsAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:VBArs:APOSition`` command.

    Description:
        - This command sets or queries the vertical cursor A position of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:VBArs:APOSition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:VBArs:APOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:VBArs:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:VBArs:APOSition <NR3>
        - DISplay:PLOTView1:CURSor:VBArs:APOSition?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the vertical cursor A position.
    """


class DisplayPlotview1CursorVbars(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:VBArs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:VBArs?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:VBArs?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.aposition``: The ``DISplay:PLOTView1:CURSor:VBArs:APOSition`` command.
        - ``.bposition``: The ``DISplay:PLOTView1:CURSor:VBArs:BPOSition`` command.
        - ``.delta``: The ``DISplay:PLOTView1:CURSor:VBArs:DELTa`` command.
        - ``.units``: The ``DISplay:PLOTView1:CURSor:VBArs:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aposition = DisplayPlotview1CursorVbarsAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._bposition = DisplayPlotview1CursorVbarsBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )
        self._delta = DisplayPlotview1CursorVbarsDelta(device, f"{self._cmd_syntax}:DELTa")
        self._units = DisplayPlotview1CursorVbarsUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def aposition(self) -> DisplayPlotview1CursorVbarsAposition:
        """Return the ``DISplay:PLOTView1:CURSor:VBArs:APOSition`` command.

        Description:
            - This command sets or queries the vertical cursor A position of the specified cursor in
              the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:PLOTView1:CURSor:VBArs:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:VBArs:APOSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:VBArs:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:VBArs:APOSition <NR3>
            - DISplay:PLOTView1:CURSor:VBArs:APOSition?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the vertical cursor A position.
        """
        return self._aposition

    @property
    def bposition(self) -> DisplayPlotview1CursorVbarsBposition:
        """Return the ``DISplay:PLOTView1:CURSor:VBArs:BPOSition`` command.

        Description:
            - This command sets or queries the vertical cursor B position of the specified cursor in
              the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:PLOTView1:CURSor:VBArs:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:VBArs:BPOSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:VBArs:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:VBArs:BPOSition <NR3>
            - DISplay:PLOTView1:CURSor:VBArs:BPOSition?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the vertical cursor B position.
        """
        return self._bposition

    @property
    def delta(self) -> DisplayPlotview1CursorVbarsDelta:
        """Return the ``DISplay:PLOTView1:CURSor:VBArs:DELTa`` command.

        Description:
            - This command queries the delta T cursor readout value of the specified cursor in the
              specified view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:VBArs:DELTa?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:VBArs:DELTa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:VBArs:DELTa?
            ```

        Info:
            - ``1`` is the Plot waveform number.
        """
        return self._delta

    @property
    def units(self) -> DisplayPlotview1CursorVbarsUnits:
        """Return the ``DISplay:PLOTView1:CURSor:VBArs:UNIts`` command.

        Description:
            - This command queries the VBArs cursor readout units of the specified cursor in the
              specified view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:VBArs:UNIts?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:VBArs:UNIts?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:VBArs:UNIts?
            ```

        Info:
            - ``1`` is the Plot waveform number.
        """
        return self._units


class DisplayPlotview1CursorState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:STATE`` command.

    Description:
        - This command sets or queries the visible state of the cursor of the specified cursor in
          the specified view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PLOTView1:CURSor:STATE value``
          command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:STATE {ON|OFF|<NR1>}
        - DISplay:PLOTView1:CURSor:STATE?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``OFF`` disables the specified cursor.
        - ``ON`` enables the specified cursor.
        - ``<NR1>`` = 0 disables the specified cursor; any other value enables the specified cursor.
    """


class DisplayPlotview1CursorSplitmode(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:SPLITMODE`` command.

    Description:
        - This command sets or queries the cursor source mode in the specified view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:SPLITMODE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:SPLITMODE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:SPLITMODE value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:SPLITMODE {SAME|SPLIT}
        - DISplay:PLOTView1:CURSor:SPLITMODE?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``SAME`` specifies that both cursors are on the same waveform.
        - ``SPLIT`` specifies that the cursors can be on different waveforms.
    """


class DisplayPlotview1CursorScreenByposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:SCREEN:BYPOSition`` command.

    Description:
        - This command sets or queries the vertical cursor B position of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:BYPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:BYPOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:BYPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:SCREEN:BYPOSition <NR3>
        - DISplay:PLOTView1:CURSor:SCREEN:BYPOSition?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the vertical cursor B position.
    """


class DisplayPlotview1CursorScreenBxposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:SCREEN:BXPOSition`` command.

    Description:
        - This command sets or queries the horizontal cursor B position of the specified cursor in
          the specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:BXPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:BXPOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:BXPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:SCREEN:BXPOSition <NR3>
        - DISplay:PLOTView1:CURSor:SCREEN:BXPOSition?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the horizontal cursor B position.
    """


class DisplayPlotview1CursorScreenAyposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:SCREEN:AYPOSition`` command.

    Description:
        - This command sets or queries the vertical cursor A position of the specified cursor in the
          specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:AYPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:AYPOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:AYPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:SCREEN:AYPOSition <NR3>
        - DISplay:PLOTView1:CURSor:SCREEN:AYPOSition?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the vertical cursor A position.
    """


class DisplayPlotview1CursorScreenAxposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:SCREEN:AXPOSition`` command.

    Description:
        - This command sets or queries the horizontal cursor A position of the specified cursor in
          the specified view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:AXPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:AXPOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:SCREEN:AXPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:SCREEN:AXPOSition <NR3>
        - DISplay:PLOTView1:CURSor:SCREEN:AXPOSition?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the horizontal cursor A position.
    """


class DisplayPlotview1CursorScreen(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:SCREEN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:SCREEN?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:SCREEN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.axposition``: The ``DISplay:PLOTView1:CURSor:SCREEN:AXPOSition`` command.
        - ``.ayposition``: The ``DISplay:PLOTView1:CURSor:SCREEN:AYPOSition`` command.
        - ``.bxposition``: The ``DISplay:PLOTView1:CURSor:SCREEN:BXPOSition`` command.
        - ``.byposition``: The ``DISplay:PLOTView1:CURSor:SCREEN:BYPOSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._axposition = DisplayPlotview1CursorScreenAxposition(
            device, f"{self._cmd_syntax}:AXPOSition"
        )
        self._ayposition = DisplayPlotview1CursorScreenAyposition(
            device, f"{self._cmd_syntax}:AYPOSition"
        )
        self._bxposition = DisplayPlotview1CursorScreenBxposition(
            device, f"{self._cmd_syntax}:BXPOSition"
        )
        self._byposition = DisplayPlotview1CursorScreenByposition(
            device, f"{self._cmd_syntax}:BYPOSition"
        )

    @property
    def axposition(self) -> DisplayPlotview1CursorScreenAxposition:
        """Return the ``DISplay:PLOTView1:CURSor:SCREEN:AXPOSition`` command.

        Description:
            - This command sets or queries the horizontal cursor A position of the specified cursor
              in the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:AXPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:AXPOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:AXPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:SCREEN:AXPOSition <NR3>
            - DISplay:PLOTView1:CURSor:SCREEN:AXPOSition?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the horizontal cursor A position.
        """
        return self._axposition

    @property
    def ayposition(self) -> DisplayPlotview1CursorScreenAyposition:
        """Return the ``DISplay:PLOTView1:CURSor:SCREEN:AYPOSition`` command.

        Description:
            - This command sets or queries the vertical cursor A position of the specified cursor in
              the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:AYPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:AYPOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:AYPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:SCREEN:AYPOSition <NR3>
            - DISplay:PLOTView1:CURSor:SCREEN:AYPOSition?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the vertical cursor A position.
        """
        return self._ayposition

    @property
    def bxposition(self) -> DisplayPlotview1CursorScreenBxposition:
        """Return the ``DISplay:PLOTView1:CURSor:SCREEN:BXPOSition`` command.

        Description:
            - This command sets or queries the horizontal cursor B position of the specified cursor
              in the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:BXPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:BXPOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:BXPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:SCREEN:BXPOSition <NR3>
            - DISplay:PLOTView1:CURSor:SCREEN:BXPOSition?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the horizontal cursor B position.
        """
        return self._bxposition

    @property
    def byposition(self) -> DisplayPlotview1CursorScreenByposition:
        """Return the ``DISplay:PLOTView1:CURSor:SCREEN:BYPOSition`` command.

        Description:
            - This command sets or queries the vertical cursor B position of the specified cursor in
              the specified view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:BYPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:BYPOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:SCREEN:BYPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:SCREEN:BYPOSition <NR3>
            - DISplay:PLOTView1:CURSor:SCREEN:BYPOSition?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the vertical cursor B position.
        """
        return self._byposition


class DisplayPlotview1CursorRolocation(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:ROLOCATION`` command.

    Description:
        - This command sets or queries the location to display the specified plot cursor readouts
          (in the plot graticule or in a badge in the Results Bar).

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:ROLOCATION?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:ROLOCATION?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:ROLOCATION value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:ROLOCATION {GRATICULE|BADGE}
        - DISplay:PLOTView1:CURSor:ROLOCATION?
        ```

    Info:
        - ``1`` is the waveform plot number.
        - ``GRATICULE`` sets the plot cursor readouts to display as part of the cursors in the plot
          view.
        - ``BADGE`` removes the plot cursor readouts from the cursors in the graticule and displays
          the cursor information as a badge in the Results Bar.
    """


class DisplayPlotview1CursorOneoverdeltatvalue(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:ONEOVERDELTATVALUE`` command.

    Description:
        - This command sets or queries the one over delta T cursor readout value for the specified
          Plot view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:PLOTView1:CURSor:ONEOVERDELTATVALUE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:ONEOVERDELTATVALUE?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:ONEOVERDELTATVALUE?
        ```

    Info:
        - ``1`` is the Plot waveform number.
    """


class DisplayPlotview1CursorMode(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:MODe`` command.

    Description:
        - This command sets or queries the cursor tracking mode for the specified Plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:MODe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PLOTView1:CURSor:MODe value``
          command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:MODe {INDEPENDENT|TRACK}
        - DISplay:PLOTView1:CURSor:MODe?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``INDEPENDENT`` allows independent adjustment of the two cursors.
        - ``TRACK`` ties the navigational functionality of the two cursors together. For cursor A
          adjustments, this ties the movement of the two cursors together; however, cursor B
          continues to move independently of cursor A.
    """


class DisplayPlotview1CursorHbarsDelta(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:HBArs:DELTa`` command.

    Description:
        - This command queries the delta V cursor readout value for the specified Plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:HBArs:DELTa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:HBArs:DELTa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:HBArs:DELTa?
        ```

    Info:
        - ``1`` is the Plot waveform number.
    """


class DisplayPlotview1CursorHbarsBunits(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:HBArs:BUNIts`` command.

    Description:
        - This command queries the cursor B vertical units for the specified Plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:HBArs:BUNIts?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:HBArs:BUNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:HBArs:BUNIts?
        ```

    Info:
        - ``1`` is the Plot waveform number.
    """


class DisplayPlotview1CursorHbarsBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:HBArs:BPOSition`` command.

    Description:
        - This command sets or queries the horizontal cursor B position for the specified Plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:HBArs:BPOSition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:HBArs:BPOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:HBArs:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:HBArs:BPOSition <NR3>
        - DISplay:PLOTView1:CURSor:HBArs:BPOSition?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the HBArs vertical position.
    """


class DisplayPlotview1CursorHbarsAunits(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:HBArs:AUNIts`` command.

    Description:
        - This command queries the horizontal cursor A vertical units for the specified Plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:HBArs:AUNIts?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:HBArs:AUNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:HBArs:AUNIts?
        ```
    """


class DisplayPlotview1CursorHbarsAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:HBArs:APOSition`` command.

    Description:
        - This command sets or queries the horizontal cursor A position for the specified Plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:HBArs:APOSition?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:HBArs:APOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:HBArs:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:HBArs:APOSition <NR3>
        - DISplay:PLOTView1:CURSor:HBArs:APOSition?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``<NR3>`` is the cursor position.
    """


class DisplayPlotview1CursorHbars(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:HBArs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:HBArs?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:HBArs?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.aposition``: The ``DISplay:PLOTView1:CURSor:HBArs:APOSition`` command.
        - ``.aunits``: The ``DISplay:PLOTView1:CURSor:HBArs:AUNIts`` command.
        - ``.bposition``: The ``DISplay:PLOTView1:CURSor:HBArs:BPOSition`` command.
        - ``.bunits``: The ``DISplay:PLOTView1:CURSor:HBArs:BUNIts`` command.
        - ``.delta``: The ``DISplay:PLOTView1:CURSor:HBArs:DELTa`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aposition = DisplayPlotview1CursorHbarsAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._aunits = DisplayPlotview1CursorHbarsAunits(device, f"{self._cmd_syntax}:AUNIts")
        self._bposition = DisplayPlotview1CursorHbarsBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )
        self._bunits = DisplayPlotview1CursorHbarsBunits(device, f"{self._cmd_syntax}:BUNIts")
        self._delta = DisplayPlotview1CursorHbarsDelta(device, f"{self._cmd_syntax}:DELTa")

    @property
    def aposition(self) -> DisplayPlotview1CursorHbarsAposition:
        """Return the ``DISplay:PLOTView1:CURSor:HBArs:APOSition`` command.

        Description:
            - This command sets or queries the horizontal cursor A position for the specified Plot
              view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:PLOTView1:CURSor:HBArs:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:HBArs:APOSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:HBArs:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:HBArs:APOSition <NR3>
            - DISplay:PLOTView1:CURSor:HBArs:APOSition?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the cursor position.
        """
        return self._aposition

    @property
    def aunits(self) -> DisplayPlotview1CursorHbarsAunits:
        """Return the ``DISplay:PLOTView1:CURSor:HBArs:AUNIts`` command.

        Description:
            - This command queries the horizontal cursor A vertical units for the specified Plot
              view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:HBArs:AUNIts?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:HBArs:AUNIts?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:HBArs:AUNIts?
            ```
        """
        return self._aunits

    @property
    def bposition(self) -> DisplayPlotview1CursorHbarsBposition:
        """Return the ``DISplay:PLOTView1:CURSor:HBArs:BPOSition`` command.

        Description:
            - This command sets or queries the horizontal cursor B position for the specified Plot
              view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:PLOTView1:CURSor:HBArs:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:HBArs:BPOSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:HBArs:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:HBArs:BPOSition <NR3>
            - DISplay:PLOTView1:CURSor:HBArs:BPOSition?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``<NR3>`` is the HBArs vertical position.
        """
        return self._bposition

    @property
    def bunits(self) -> DisplayPlotview1CursorHbarsBunits:
        """Return the ``DISplay:PLOTView1:CURSor:HBArs:BUNIts`` command.

        Description:
            - This command queries the cursor B vertical units for the specified Plot view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:HBArs:BUNIts?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:HBArs:BUNIts?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:HBArs:BUNIts?
            ```

        Info:
            - ``1`` is the Plot waveform number.
        """
        return self._bunits

    @property
    def delta(self) -> DisplayPlotview1CursorHbarsDelta:
        """Return the ``DISplay:PLOTView1:CURSor:HBArs:DELTa`` command.

        Description:
            - This command queries the delta V cursor readout value for the specified Plot view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:HBArs:DELTa?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:HBArs:DELTa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:HBArs:DELTa?
            ```

        Info:
            - ``1`` is the Plot waveform number.
        """
        return self._delta


class DisplayPlotview1CursorFunction(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:FUNCtion`` command.

    Description:
        - This command sets or queries the cursor mode for the specified Plot view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:FUNCtion?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:PLOTView1:CURSor:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:FUNCtion {WAVEFORM|VBArs|HBArs|SCREEN}
        - DISplay:PLOTView1:CURSor:FUNCtion?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``WAVEFORM`` specifies to display the paired cursors in YT display format for measuring
          waveform amplitude and time.
        - ``VBArs`` specifies vertical bar cursors, which measure in horizontal units.
        - ``HBArs`` specifies horizontal bar cursors, which measure in vertical units.
        - ``SCREEN`` specifies to display both horizontal and vertical bar cursors, which measure
          the selected waveform in horizontal and vertical units. Use these cursors to measure
          anywhere in the waveform display area.
    """


class DisplayPlotview1CursorDdt(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:DDT`` command.

    Description:
        - This command returns the delta V over delta T cursor readout value for the specified Plot
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:DDT?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:DDT?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:DDT?
        ```

    Info:
        - ``PlotView<x>`` is the Plot waveform number.
    """


class DisplayPlotview1CursorBsource(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:BSOUrce`` command.

    Description:
        - This command queries the cursor source for plot cursor B.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:BSOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:BSOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:BSOUrce?
        ```

    Info:
        - ``1`` is the Plot waveform number.
    """


class DisplayPlotview1CursorAsource(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor:ASOUrce`` command.

    Description:
        - This command queries the cursor source for plot cursor A.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:ASOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:ASOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:CURSor:ASOUrce?
        ```

    Info:
        - ``1`` is the Plot waveform number.
    """


#  pylint: disable=too-many-instance-attributes
class DisplayPlotview1Cursor(SCPICmdRead):
    """The ``DISplay:PLOTView1:CURSor`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.asource``: The ``DISplay:PLOTView1:CURSor:ASOUrce`` command.
        - ``.bsource``: The ``DISplay:PLOTView1:CURSor:BSOUrce`` command.
        - ``.ddt``: The ``DISplay:PLOTView1:CURSor:DDT`` command.
        - ``.function``: The ``DISplay:PLOTView1:CURSor:FUNCtion`` command.
        - ``.hbars``: The ``DISplay:PLOTView1:CURSor:HBArs`` command tree.
        - ``.mode``: The ``DISplay:PLOTView1:CURSor:MODe`` command.
        - ``.oneoverdeltatvalue``: The ``DISplay:PLOTView1:CURSor:ONEOVERDELTATVALUE`` command.
        - ``.rolocation``: The ``DISplay:PLOTView1:CURSor:ROLOCATION`` command.
        - ``.screen``: The ``DISplay:PLOTView1:CURSor:SCREEN`` command tree.
        - ``.splitmode``: The ``DISplay:PLOTView1:CURSor:SPLITMODE`` command.
        - ``.state``: The ``DISplay:PLOTView1:CURSor:STATE`` command.
        - ``.vbars``: The ``DISplay:PLOTView1:CURSor:VBArs`` command tree.
        - ``.waveform``: The ``DISplay:PLOTView1:CURSor:WAVEform`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._asource = DisplayPlotview1CursorAsource(device, f"{self._cmd_syntax}:ASOUrce")
        self._bsource = DisplayPlotview1CursorBsource(device, f"{self._cmd_syntax}:BSOUrce")
        self._ddt = DisplayPlotview1CursorDdt(device, f"{self._cmd_syntax}:DDT")
        self._function = DisplayPlotview1CursorFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._hbars = DisplayPlotview1CursorHbars(device, f"{self._cmd_syntax}:HBArs")
        self._mode = DisplayPlotview1CursorMode(device, f"{self._cmd_syntax}:MODe")
        self._oneoverdeltatvalue = DisplayPlotview1CursorOneoverdeltatvalue(
            device, f"{self._cmd_syntax}:ONEOVERDELTATVALUE"
        )
        self._rolocation = DisplayPlotview1CursorRolocation(
            device, f"{self._cmd_syntax}:ROLOCATION"
        )
        self._screen = DisplayPlotview1CursorScreen(device, f"{self._cmd_syntax}:SCREEN")
        self._splitmode = DisplayPlotview1CursorSplitmode(device, f"{self._cmd_syntax}:SPLITMODE")
        self._state = DisplayPlotview1CursorState(device, f"{self._cmd_syntax}:STATE")
        self._vbars = DisplayPlotview1CursorVbars(device, f"{self._cmd_syntax}:VBArs")
        self._waveform = DisplayPlotview1CursorWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def asource(self) -> DisplayPlotview1CursorAsource:
        """Return the ``DISplay:PLOTView1:CURSor:ASOUrce`` command.

        Description:
            - This command queries the cursor source for plot cursor A.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:ASOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:ASOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:ASOUrce?
            ```

        Info:
            - ``1`` is the Plot waveform number.
        """
        return self._asource

    @property
    def bsource(self) -> DisplayPlotview1CursorBsource:
        """Return the ``DISplay:PLOTView1:CURSor:BSOUrce`` command.

        Description:
            - This command queries the cursor source for plot cursor B.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:BSOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:BSOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:BSOUrce?
            ```

        Info:
            - ``1`` is the Plot waveform number.
        """
        return self._bsource

    @property
    def ddt(self) -> DisplayPlotview1CursorDdt:
        """Return the ``DISplay:PLOTView1:CURSor:DDT`` command.

        Description:
            - This command returns the delta V over delta T cursor readout value for the specified
              Plot view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:DDT?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:DDT?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:DDT?
            ```

        Info:
            - ``PlotView<x>`` is the Plot waveform number.
        """
        return self._ddt

    @property
    def function(self) -> DisplayPlotview1CursorFunction:
        """Return the ``DISplay:PLOTView1:CURSor:FUNCtion`` command.

        Description:
            - This command sets or queries the cursor mode for the specified Plot view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:FUNCtion?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:FUNCtion?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:FUNCtion {WAVEFORM|VBArs|HBArs|SCREEN}
            - DISplay:PLOTView1:CURSor:FUNCtion?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``WAVEFORM`` specifies to display the paired cursors in YT display format for
              measuring waveform amplitude and time.
            - ``VBArs`` specifies vertical bar cursors, which measure in horizontal units.
            - ``HBArs`` specifies horizontal bar cursors, which measure in vertical units.
            - ``SCREEN`` specifies to display both horizontal and vertical bar cursors, which
              measure the selected waveform in horizontal and vertical units. Use these cursors to
              measure anywhere in the waveform display area.
        """
        return self._function

    @property
    def hbars(self) -> DisplayPlotview1CursorHbars:
        """Return the ``DISplay:PLOTView1:CURSor:HBArs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:HBArs?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:HBArs?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.aposition``: The ``DISplay:PLOTView1:CURSor:HBArs:APOSition`` command.
            - ``.aunits``: The ``DISplay:PLOTView1:CURSor:HBArs:AUNIts`` command.
            - ``.bposition``: The ``DISplay:PLOTView1:CURSor:HBArs:BPOSition`` command.
            - ``.bunits``: The ``DISplay:PLOTView1:CURSor:HBArs:BUNIts`` command.
            - ``.delta``: The ``DISplay:PLOTView1:CURSor:HBArs:DELTa`` command.
        """
        return self._hbars

    @property
    def mode(self) -> DisplayPlotview1CursorMode:
        """Return the ``DISplay:PLOTView1:CURSor:MODe`` command.

        Description:
            - This command sets or queries the cursor tracking mode for the specified Plot view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:MODe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:MODe value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:MODe {INDEPENDENT|TRACK}
            - DISplay:PLOTView1:CURSor:MODe?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``INDEPENDENT`` allows independent adjustment of the two cursors.
            - ``TRACK`` ties the navigational functionality of the two cursors together. For cursor
              A adjustments, this ties the movement of the two cursors together; however, cursor B
              continues to move independently of cursor A.
        """
        return self._mode

    @property
    def oneoverdeltatvalue(self) -> DisplayPlotview1CursorOneoverdeltatvalue:
        """Return the ``DISplay:PLOTView1:CURSor:ONEOVERDELTATVALUE`` command.

        Description:
            - This command sets or queries the one over delta T cursor readout value for the
              specified Plot view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:PLOTView1:CURSor:ONEOVERDELTATVALUE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:ONEOVERDELTATVALUE?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:ONEOVERDELTATVALUE?
            ```

        Info:
            - ``1`` is the Plot waveform number.
        """
        return self._oneoverdeltatvalue

    @property
    def rolocation(self) -> DisplayPlotview1CursorRolocation:
        """Return the ``DISplay:PLOTView1:CURSor:ROLOCATION`` command.

        Description:
            - This command sets or queries the location to display the specified plot cursor
              readouts (in the plot graticule or in a badge in the Results Bar).

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:ROLOCATION?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:ROLOCATION?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:ROLOCATION value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:ROLOCATION {GRATICULE|BADGE}
            - DISplay:PLOTView1:CURSor:ROLOCATION?
            ```

        Info:
            - ``1`` is the waveform plot number.
            - ``GRATICULE`` sets the plot cursor readouts to display as part of the cursors in the
              plot view.
            - ``BADGE`` removes the plot cursor readouts from the cursors in the graticule and
              displays the cursor information as a badge in the Results Bar.
        """
        return self._rolocation

    @property
    def screen(self) -> DisplayPlotview1CursorScreen:
        """Return the ``DISplay:PLOTView1:CURSor:SCREEN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:SCREEN?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:SCREEN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.axposition``: The ``DISplay:PLOTView1:CURSor:SCREEN:AXPOSition`` command.
            - ``.ayposition``: The ``DISplay:PLOTView1:CURSor:SCREEN:AYPOSition`` command.
            - ``.bxposition``: The ``DISplay:PLOTView1:CURSor:SCREEN:BXPOSition`` command.
            - ``.byposition``: The ``DISplay:PLOTView1:CURSor:SCREEN:BYPOSition`` command.
        """
        return self._screen

    @property
    def splitmode(self) -> DisplayPlotview1CursorSplitmode:
        """Return the ``DISplay:PLOTView1:CURSor:SPLITMODE`` command.

        Description:
            - This command sets or queries the cursor source mode in the specified view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:SPLITMODE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:SPLITMODE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:SPLITMODE value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:SPLITMODE {SAME|SPLIT}
            - DISplay:PLOTView1:CURSor:SPLITMODE?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``SAME`` specifies that both cursors are on the same waveform.
            - ``SPLIT`` specifies that the cursors can be on different waveforms.
        """
        return self._splitmode

    @property
    def state(self) -> DisplayPlotview1CursorState:
        """Return the ``DISplay:PLOTView1:CURSor:STATE`` command.

        Description:
            - This command sets or queries the visible state of the cursor of the specified cursor
              in the specified view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:CURSor:STATE {ON|OFF|<NR1>}
            - DISplay:PLOTView1:CURSor:STATE?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``OFF`` disables the specified cursor.
            - ``ON`` enables the specified cursor.
            - ``<NR1>`` = 0 disables the specified cursor; any other value enables the specified
              cursor.
        """
        return self._state

    @property
    def vbars(self) -> DisplayPlotview1CursorVbars:
        """Return the ``DISplay:PLOTView1:CURSor:VBArs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:VBArs?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor:VBArs?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.aposition``: The ``DISplay:PLOTView1:CURSor:VBArs:APOSition`` command.
            - ``.bposition``: The ``DISplay:PLOTView1:CURSor:VBArs:BPOSition`` command.
            - ``.delta``: The ``DISplay:PLOTView1:CURSor:VBArs:DELTa`` command.
            - ``.units``: The ``DISplay:PLOTView1:CURSor:VBArs:UNIts`` command.
        """
        return self._vbars

    @property
    def waveform(self) -> DisplayPlotview1CursorWaveform:
        """Return the ``DISplay:PLOTView1:CURSor:WAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor:WAVEform?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:PLOTView1:CURSor:WAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.aposition``: The ``DISplay:PLOTView1:CURSor:WAVEform:APOSition`` command.
            - ``.bposition``: The ``DISplay:PLOTView1:CURSor:WAVEform:BPOSition`` command.
        """
        return self._waveform


class DisplayPlotview1Autoscale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PLOTView1:AUTOScale`` command.

    Description:
        - This command sets or queries the enabled state of autoscale for the specified plot.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1:AUTOScale?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:AUTOScale?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PLOTView1:AUTOScale value``
          command.

    SCPI Syntax:
        ```
        - DISplay:PLOTView1:AUTOScale {ON|OFF|<NR1>}
        - DISplay:PLOTView1:AUTOScale?
        ```

    Info:
        - ``1`` is the Plot waveform number.
        - ``OFF`` disables the autoscale feature.
        - ``ON`` enables the autoscale feature.
        - ``<NR1>`` = 0 disables the autoscale feature; any other value enables the autoscale
          feature.
    """


class DisplayPlotview1(SCPICmdRead):
    """The ``DISplay:PLOTView1`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PLOTView1?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autoscale``: The ``DISplay:PLOTView1:AUTOScale`` command.
        - ``.cursor``: The ``DISplay:PLOTView1:CURSor`` command tree.
        - ``.gridlines``: The ``DISplay:PLOTView1:GRIDlines`` command.
        - ``.xaxis``: The ``DISplay:PLOTView1:XAXIS`` command tree.
        - ``.yaxis``: The ``DISplay:PLOTView1:YAXIS`` command tree.
        - ``.zoom``: The ``DISplay:PLOTView1:ZOOM`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoscale = DisplayPlotview1Autoscale(device, f"{self._cmd_syntax}:AUTOScale")
        self._cursor = DisplayPlotview1Cursor(device, f"{self._cmd_syntax}:CURSor")
        self._gridlines = DisplayPlotview1Gridlines(device, f"{self._cmd_syntax}:GRIDlines")
        self._xaxis = DisplayPlotview1Xaxis(device, f"{self._cmd_syntax}:XAXIS")
        self._yaxis = DisplayPlotview1Yaxis(device, f"{self._cmd_syntax}:YAXIS")
        self._zoom = DisplayPlotview1Zoom(device, f"{self._cmd_syntax}:ZOOM")

    @property
    def autoscale(self) -> DisplayPlotview1Autoscale:
        """Return the ``DISplay:PLOTView1:AUTOScale`` command.

        Description:
            - This command sets or queries the enabled state of autoscale for the specified plot.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:AUTOScale?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:AUTOScale?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:PLOTView1:AUTOScale value``
              command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:AUTOScale {ON|OFF|<NR1>}
            - DISplay:PLOTView1:AUTOScale?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``OFF`` disables the autoscale feature.
            - ``ON`` enables the autoscale feature.
            - ``<NR1>`` = 0 disables the autoscale feature; any other value enables the autoscale
              feature.
        """
        return self._autoscale

    @property
    def cursor(self) -> DisplayPlotview1Cursor:
        """Return the ``DISplay:PLOTView1:CURSor`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:CURSor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:CURSor?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.asource``: The ``DISplay:PLOTView1:CURSor:ASOUrce`` command.
            - ``.bsource``: The ``DISplay:PLOTView1:CURSor:BSOUrce`` command.
            - ``.ddt``: The ``DISplay:PLOTView1:CURSor:DDT`` command.
            - ``.function``: The ``DISplay:PLOTView1:CURSor:FUNCtion`` command.
            - ``.hbars``: The ``DISplay:PLOTView1:CURSor:HBArs`` command tree.
            - ``.mode``: The ``DISplay:PLOTView1:CURSor:MODe`` command.
            - ``.oneoverdeltatvalue``: The ``DISplay:PLOTView1:CURSor:ONEOVERDELTATVALUE`` command.
            - ``.rolocation``: The ``DISplay:PLOTView1:CURSor:ROLOCATION`` command.
            - ``.screen``: The ``DISplay:PLOTView1:CURSor:SCREEN`` command tree.
            - ``.splitmode``: The ``DISplay:PLOTView1:CURSor:SPLITMODE`` command.
            - ``.state``: The ``DISplay:PLOTView1:CURSor:STATE`` command.
            - ``.vbars``: The ``DISplay:PLOTView1:CURSor:VBArs`` command tree.
            - ``.waveform``: The ``DISplay:PLOTView1:CURSor:WAVEform`` command tree.
        """
        return self._cursor

    @property
    def gridlines(self) -> DisplayPlotview1Gridlines:
        """Return the ``DISplay:PLOTView1:GRIDlines`` command.

        Description:
            - This command sets or queries the Grid (graticule) lines setting of the specified plot.
              This command works for plots that have vertical and horizontal units associated with
              the graticule. For example, this command does not work for XY or XYZ plots.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:GRIDlines?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:GRIDlines?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:PLOTView1:GRIDlines value``
              command.

        SCPI Syntax:
            ```
            - DISplay:PLOTView1:GRIDlines {HORizontal|VERTical|BOTH}
            - DISplay:PLOTView1:GRIDlines?
            ```

        Info:
            - ``1`` is the Plot waveform number.
            - ``HORizontal`` specifies horizontal grid lines.
            - ``VERTical`` specifies vertical grid lines.
            - ``BOTH`` specifies both vertical and horizontal grid lines.
        """
        return self._gridlines

    @property
    def xaxis(self) -> DisplayPlotview1Xaxis:
        """Return the ``DISplay:PLOTView1:XAXIS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:XAXIS?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:XAXIS?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DISplay:PLOTView1:XAXIS:SCALE`` command.
        """
        return self._xaxis

    @property
    def yaxis(self) -> DisplayPlotview1Yaxis:
        """Return the ``DISplay:PLOTView1:YAXIS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:YAXIS?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:YAXIS?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DISplay:PLOTView1:YAXIS:SCALE`` command.
        """
        return self._yaxis

    @property
    def zoom(self) -> DisplayPlotview1Zoom:
        """Return the ``DISplay:PLOTView1:ZOOM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1:ZOOM?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1:ZOOM?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.xaxis``: The ``DISplay:PLOTView1:ZOOM:XAXIS`` command tree.
            - ``.yaxis``: The ``DISplay:PLOTView1:ZOOM:YAXIS`` command tree.
        """
        return self._zoom


class DisplayPersistenceReset(SCPICmdWriteNoArguments):
    """The ``DISplay:PERSistence:RESET`` command.

    Description:
        - This command controls the clearing of persistence data that has been built up over time.
          Persistence is valid for wave views only.

    Usage:
        - Using the ``.write()`` method will send the ``DISplay:PERSistence:RESET`` command.

    SCPI Syntax:
        ```
        - DISplay:PERSistence:RESET
        ```
    """


class DisplayPersistence(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PERSistence`` command.

    Description:
        - This command sets or queries the display persistence for analog waveforms. Persistence is
          valid for wave views only.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PERSistence?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PERSistence?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PERSistence value`` command.

    SCPI Syntax:
        ```
        - DISplay:PERSistence {OFF|AUTO|INFPersist|INFInite|VARpersist|CLEAR}
        - DISplay:PERSistence?
        ```

    Info:
        - ``OFF`` disables the persistence aspect of the display.
        - ``AUTO`` automatically set the persistence.
        - ``INFPersist`` sets a display mode where any pixels, once touched by samples, remain set
          until cleared by a mode change.
        - ``INFInite`` sets a display mode where any pixels, once touched by samples, remain set
          until cleared by a mode change.
        - ``VARPersist`` sets a display mode where set pixels are gradually dimmed.
        - ``CLEAR`` resets the persist time count down and clears the display of acquired points.

    Properties:
        - ``.reset``: The ``DISplay:PERSistence:RESET`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._reset = DisplayPersistenceReset(device, f"{self._cmd_syntax}:RESET")

    @property
    def reset(self) -> DisplayPersistenceReset:
        """Return the ``DISplay:PERSistence:RESET`` command.

        Description:
            - This command controls the clearing of persistence data that has been built up over
              time. Persistence is valid for wave views only.

        Usage:
            - Using the ``.write()`` method will send the ``DISplay:PERSistence:RESET`` command.

        SCPI Syntax:
            ```
            - DISplay:PERSistence:RESET
            ```
        """
        return self._reset


class DisplayMathItemNormalcolor(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:Math<x>:NORMALColor`` command.

    Description:
        - This command sets or queries the normal mode color of the specified input source to the
          specified color. You can assign one of 48 unique colors to any channel, math, or reference
          waveform. These colors replace the default normal colors and remain in effect until you
          reset the colors.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:Math<x>:NORMALColor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:Math<x>:NORMALColor?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:Math<x>:NORMALColor value``
          command.

    SCPI Syntax:
        ```
        - DISplay:Math<x>:NORMALColor COLOR<y>
        - DISplay:Math<x>:NORMALColor?
        ```

    Info:
        - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to 47.
    """


class DisplayMathItemInvertcolor(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:Math<x>:INVERTColor`` command.

    Description:
        - This command sets or queries the Inverted mode color of the specified input source to the
          specified color. You can assign one of 48 unique colors to any channel, math, or reference
          waveform. These colors replace the default Inverted colors and remain in effect until you
          reset the colors.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:Math<x>:INVERTColor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:Math<x>:INVERTColor?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:Math<x>:INVERTColor value``
          command.

    SCPI Syntax:
        ```
        - DISplay:Math<x>:INVERTColor COLOR<y>
        - DISplay:Math<x>:INVERTColor?
        ```

    Info:
        - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to 47.
    """


class DisplayMathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:Math<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:Math<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:Math<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.invertcolor``: The ``DISplay:Math<x>:INVERTColor`` command.
        - ``.normalcolor``: The ``DISplay:Math<x>:NORMALColor`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._invertcolor = DisplayMathItemInvertcolor(device, f"{self._cmd_syntax}:INVERTColor")
        self._normalcolor = DisplayMathItemNormalcolor(device, f"{self._cmd_syntax}:NORMALColor")

    @property
    def invertcolor(self) -> DisplayMathItemInvertcolor:
        """Return the ``DISplay:Math<x>:INVERTColor`` command.

        Description:
            - This command sets or queries the Inverted mode color of the specified input source to
              the specified color. You can assign one of 48 unique colors to any channel, math, or
              reference waveform. These colors replace the default Inverted colors and remain in
              effect until you reset the colors.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:Math<x>:INVERTColor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:Math<x>:INVERTColor?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:Math<x>:INVERTColor value``
              command.

        SCPI Syntax:
            ```
            - DISplay:Math<x>:INVERTColor COLOR<y>
            - DISplay:Math<x>:INVERTColor?
            ```

        Info:
            - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to
              47.
        """
        return self._invertcolor

    @property
    def normalcolor(self) -> DisplayMathItemNormalcolor:
        """Return the ``DISplay:Math<x>:NORMALColor`` command.

        Description:
            - This command sets or queries the normal mode color of the specified input source to
              the specified color. You can assign one of 48 unique colors to any channel, math, or
              reference waveform. These colors replace the default normal colors and remain in
              effect until you reset the colors.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:Math<x>:NORMALColor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:Math<x>:NORMALColor?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:Math<x>:NORMALColor value``
              command.

        SCPI Syntax:
            ```
            - DISplay:Math<x>:NORMALColor COLOR<y>
            - DISplay:Math<x>:NORMALColor?
            ```

        Info:
            - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to
              47.
        """
        return self._normalcolor


class DisplayMathfftview1ZoomYaxisTo(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:ZOOM:YAXIS:TO`` command.

    Description:
        - This command sets or queries the top edge value of the zoom y-axis area for the specified
          Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:YAXIS:TO?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:ZOOM:YAXIS:TO?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:ZOOM:YAXIS:TO value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:ZOOM:YAXIS:TO <NR3>
        - DISplay:MATHFFTView1:ZOOM:YAXIS:TO?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the top value of the zoom y axis in the specified plot view.
    """


class DisplayMathfftview1ZoomYaxisFrom(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:ZOOM:YAXIS:FROM`` command.

    Description:
        - This command sets or queries the bottom edge value of the zoom y-axis area for the
          specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:YAXIS:FROM?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:ZOOM:YAXIS:FROM?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:ZOOM:YAXIS:FROM value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:ZOOM:YAXIS:FROM <NR3>
        - DISplay:MATHFFTView1:ZOOM:YAXIS:FROM?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the bottom value of the zoom y axis in the specified plot view.
    """


class DisplayMathfftview1ZoomYaxis(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:ZOOM:YAXIS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:YAXIS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:ZOOM:YAXIS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.from``: The ``DISplay:MATHFFTView1:ZOOM:YAXIS:FROM`` command.
        - ``.to``: The ``DISplay:MATHFFTView1:ZOOM:YAXIS:TO`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._from = DisplayMathfftview1ZoomYaxisFrom(device, f"{self._cmd_syntax}:FROM")
        self._to = DisplayMathfftview1ZoomYaxisTo(device, f"{self._cmd_syntax}:TO")

    @property
    def from_(self) -> DisplayMathfftview1ZoomYaxisFrom:
        """Return the ``DISplay:MATHFFTView1:ZOOM:YAXIS:FROM`` command.

        Description:
            - This command sets or queries the bottom edge value of the zoom y-axis area for the
              specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:YAXIS:FROM?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:ZOOM:YAXIS:FROM?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:ZOOM:YAXIS:FROM value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:ZOOM:YAXIS:FROM <NR3>
            - DISplay:MATHFFTView1:ZOOM:YAXIS:FROM?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the bottom value of the zoom y axis in the specified plot view.
        """
        return self._from

    @property
    def to(self) -> DisplayMathfftview1ZoomYaxisTo:
        """Return the ``DISplay:MATHFFTView1:ZOOM:YAXIS:TO`` command.

        Description:
            - This command sets or queries the top edge value of the zoom y-axis area for the
              specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:YAXIS:TO?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:ZOOM:YAXIS:TO?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:ZOOM:YAXIS:TO value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:ZOOM:YAXIS:TO <NR3>
            - DISplay:MATHFFTView1:ZOOM:YAXIS:TO?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the top value of the zoom y axis in the specified plot view.
        """
        return self._to


class DisplayMathfftview1ZoomXaxisTo(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:ZOOM:XAXIS:TO`` command.

    Description:
        - This command sets or queries the value of the right edge value of the zoom area for the
          specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:XAXIS:TO?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:ZOOM:XAXIS:TO?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:ZOOM:XAXIS:TO value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:ZOOM:XAXIS:TO <NR3>
        - DISplay:MATHFFTView1:ZOOM:XAXIS:TO?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the value of the right edge of the zoom x axis in the specified plot view.
    """


class DisplayMathfftview1ZoomXaxisFrom(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:ZOOM:XAXIS:FROM`` command.

    Description:
        - This command sets or queries the value of the left edge of the zoom area for the specified
          Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:XAXIS:FROM?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:ZOOM:XAXIS:FROM?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:ZOOM:XAXIS:FROM value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:ZOOM:XAXIS:FROM <NR3>
        - DISplay:MATHFFTView1:ZOOM:XAXIS:FROM?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the value of the left edge of the zoom x axis in the specified plot view.
    """


class DisplayMathfftview1ZoomXaxis(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:ZOOM:XAXIS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:XAXIS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:ZOOM:XAXIS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.from``: The ``DISplay:MATHFFTView1:ZOOM:XAXIS:FROM`` command.
        - ``.to``: The ``DISplay:MATHFFTView1:ZOOM:XAXIS:TO`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._from = DisplayMathfftview1ZoomXaxisFrom(device, f"{self._cmd_syntax}:FROM")
        self._to = DisplayMathfftview1ZoomXaxisTo(device, f"{self._cmd_syntax}:TO")

    @property
    def from_(self) -> DisplayMathfftview1ZoomXaxisFrom:
        """Return the ``DISplay:MATHFFTView1:ZOOM:XAXIS:FROM`` command.

        Description:
            - This command sets or queries the value of the left edge of the zoom area for the
              specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:XAXIS:FROM?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:ZOOM:XAXIS:FROM?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:ZOOM:XAXIS:FROM value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:ZOOM:XAXIS:FROM <NR3>
            - DISplay:MATHFFTView1:ZOOM:XAXIS:FROM?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the value of the left edge of the zoom x axis in the specified plot view.
        """
        return self._from

    @property
    def to(self) -> DisplayMathfftview1ZoomXaxisTo:
        """Return the ``DISplay:MATHFFTView1:ZOOM:XAXIS:TO`` command.

        Description:
            - This command sets or queries the value of the right edge value of the zoom area for
              the specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:XAXIS:TO?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:ZOOM:XAXIS:TO?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:ZOOM:XAXIS:TO value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:ZOOM:XAXIS:TO <NR3>
            - DISplay:MATHFFTView1:ZOOM:XAXIS:TO?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the value of the right edge of the zoom x axis in the specified plot
              view.
        """
        return self._to


class DisplayMathfftview1Zoom(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:ZOOM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:ZOOM?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.xaxis``: The ``DISplay:MATHFFTView1:ZOOM:XAXIS`` command tree.
        - ``.yaxis``: The ``DISplay:MATHFFTView1:ZOOM:YAXIS`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._xaxis = DisplayMathfftview1ZoomXaxis(device, f"{self._cmd_syntax}:XAXIS")
        self._yaxis = DisplayMathfftview1ZoomYaxis(device, f"{self._cmd_syntax}:YAXIS")

    @property
    def xaxis(self) -> DisplayMathfftview1ZoomXaxis:
        """Return the ``DISplay:MATHFFTView1:ZOOM:XAXIS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:XAXIS?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:ZOOM:XAXIS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.from``: The ``DISplay:MATHFFTView1:ZOOM:XAXIS:FROM`` command.
            - ``.to``: The ``DISplay:MATHFFTView1:ZOOM:XAXIS:TO`` command.
        """
        return self._xaxis

    @property
    def yaxis(self) -> DisplayMathfftview1ZoomYaxis:
        """Return the ``DISplay:MATHFFTView1:ZOOM:YAXIS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM:YAXIS?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:ZOOM:YAXIS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.from``: The ``DISplay:MATHFFTView1:ZOOM:YAXIS:FROM`` command.
            - ``.to``: The ``DISplay:MATHFFTView1:ZOOM:YAXIS:TO`` command.
        """
        return self._yaxis


class DisplayMathfftview1YaxisScale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:YAXIS:SCALE`` command.

    Description:
        - This command sets or queries the vertical scale setting (Linear or dBm) for the specified
          Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:YAXIS:SCALE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:YAXIS:SCALE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:YAXIS:SCALE value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:YAXIS:SCALE {LINEAr|DBM}
        - DISplay:MATHFFTView1:YAXIS:SCALE?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``LINEAr`` specifies a linear scale.
        - ``DBM`` specifies a dBm scale.
    """


class DisplayMathfftview1Yaxis(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:YAXIS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:YAXIS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:YAXIS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DISplay:MATHFFTView1:YAXIS:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DisplayMathfftview1YaxisScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DisplayMathfftview1YaxisScale:
        """Return the ``DISplay:MATHFFTView1:YAXIS:SCALE`` command.

        Description:
            - This command sets or queries the vertical scale setting (Linear or dBm) for the
              specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:YAXIS:SCALE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:YAXIS:SCALE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:YAXIS:SCALE value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:YAXIS:SCALE {LINEAr|DBM}
            - DISplay:MATHFFTView1:YAXIS:SCALE?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``LINEAr`` specifies a linear scale.
            - ``DBM`` specifies a dBm scale.
        """
        return self._scale


class DisplayMathfftview1XaxisScale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:XAXIS:SCALE`` command.

    Description:
        - This command sets or queries the x-axis scale (Linear or Log) for the specified Math-FFT
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:XAXIS:SCALE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:XAXIS:SCALE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:XAXIS:SCALE value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:XAXIS:SCALE {LINEAr|LOG}
        - DISplay:MATHFFTView1:XAXIS:SCALE?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``LINEAr`` specifies a linear scale.
        - ``LOG`` specifies a logarithmic scale.
    """


class DisplayMathfftview1Xaxis(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:XAXIS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:XAXIS?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:XAXIS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.scale``: The ``DISplay:MATHFFTView1:XAXIS:SCALE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._scale = DisplayMathfftview1XaxisScale(device, f"{self._cmd_syntax}:SCALE")

    @property
    def scale(self) -> DisplayMathfftview1XaxisScale:
        """Return the ``DISplay:MATHFFTView1:XAXIS:SCALE`` command.

        Description:
            - This command sets or queries the x-axis scale (Linear or Log) for the specified
              Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:XAXIS:SCALE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:XAXIS:SCALE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:XAXIS:SCALE value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:XAXIS:SCALE {LINEAr|LOG}
            - DISplay:MATHFFTView1:XAXIS:SCALE?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``LINEAr`` specifies a linear scale.
            - ``LOG`` specifies a logarithmic scale.
        """
        return self._scale


class DisplayMathfftview1MathMathItemState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:MATH:MATH<x>:STATE`` command.

    Description:
        - This command sets or queries the display state of the specified math waveform for the
          specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:MATH:MATH<x>:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:MATH:MATH<x>:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:MATH:MATH<x>:STATE value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:MATH:MATH<x>:STATE {ON|OFF|<NR1>}
        - DISplay:MATHFFTView1:MATH:MATH<x>:STATE?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``OFF`` disables displaying the specified Math-FFT view.
        - ``ON`` enables displaying the specified Math-FFT view.
        - ``<NR1>`` = 0 disables the specified Math-FFT view; any other value enables the specified
          Math-FFT view.
    """


class DisplayMathfftview1MathMathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:MATH:MATH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:MATH:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:MATH:MATH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DISplay:MATHFFTView1:MATH:MATH<x>:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayMathfftview1MathMathItemState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> DisplayMathfftview1MathMathItemState:
        """Return the ``DISplay:MATHFFTView1:MATH:MATH<x>:STATE`` command.

        Description:
            - This command sets or queries the display state of the specified math waveform for the
              specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:MATH:MATH<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:MATH:MATH<x>:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:MATH:MATH<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:MATH:MATH<x>:STATE {ON|OFF|<NR1>}
            - DISplay:MATHFFTView1:MATH:MATH<x>:STATE?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``OFF`` disables displaying the specified Math-FFT view.
            - ``ON`` enables displaying the specified Math-FFT view.
            - ``<NR1>`` = 0 disables the specified Math-FFT view; any other value enables the
              specified Math-FFT view.
        """
        return self._state


class DisplayMathfftview1Math(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:MATH`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:MATH?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:MATH?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.math``: The ``DISplay:MATHFFTView1:MATH:MATH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._math: Dict[int, DisplayMathfftview1MathMathItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayMathfftview1MathMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )

    @property
    def math(self) -> Dict[int, DisplayMathfftview1MathMathItem]:
        """Return the ``DISplay:MATHFFTView1:MATH:MATH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:MATH:MATH<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:MATH:MATH<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DISplay:MATHFFTView1:MATH:MATH<x>:STATE`` command.
        """
        return self._math


class DisplayMathfftview1Gridlines(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:GRIDlines`` command.

    Description:
        - This command sets or queries the grid lines setting for the specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:GRIDlines?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:GRIDlines?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:MATHFFTView1:GRIDlines value``
          command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:GRIDlines {HORizontal|VERTical|BOTH}
        - DISplay:MATHFFTView1:GRIDlines?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``HORizontal`` specifies horizontal grid lines.
        - ``VERTical`` specifies vertical grid lines.
        - ``BOTH`` specifies both vertical and horizontal grid lines.
    """


class DisplayMathfftview1CursorWaveformBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition`` command.

    Description:
        - This command sets or queries the waveform cursor B position for the specified Math-FFT
          view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition <NR3>
        - DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the waveform cursor B position in the specified plot view.
    """


class DisplayMathfftview1CursorWaveformAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:WAVEform:APOSition`` command.

    Description:
        - This command sets or queries the waveform cursor A position for the specified Math-FFT
          view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:MATHFFTView1:CURSor:WAVEform:APOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:WAVEform:APOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:WAVEform:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:WAVEform:APOSition <NR3>
        - DISplay:MATHFFTView1:CURSor:WAVEform:APOSition?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the waveform cursor A position in the specified plot view.
    """


class DisplayMathfftview1CursorWaveform(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:WAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:WAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:WAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.aposition``: The ``DISplay:MATHFFTView1:CURSor:WAVEform:APOSition`` command.
        - ``.bposition``: The ``DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aposition = DisplayMathfftview1CursorWaveformAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._bposition = DisplayMathfftview1CursorWaveformBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )

    @property
    def aposition(self) -> DisplayMathfftview1CursorWaveformAposition:
        """Return the ``DISplay:MATHFFTView1:CURSor:WAVEform:APOSition`` command.

        Description:
            - This command sets or queries the waveform cursor A position for the specified Math-FFT
              view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:WAVEform:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:WAVEform:APOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:WAVEform:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:WAVEform:APOSition <NR3>
            - DISplay:MATHFFTView1:CURSor:WAVEform:APOSition?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the waveform cursor A position in the specified plot view.
        """
        return self._aposition

    @property
    def bposition(self) -> DisplayMathfftview1CursorWaveformBposition:
        """Return the ``DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition`` command.

        Description:
            - This command sets or queries the waveform cursor B position for the specified Math-FFT
              view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition <NR3>
            - DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the waveform cursor B position in the specified plot view.
        """
        return self._bposition


class DisplayMathfftview1CursorVbarsDelta(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:VBArs:DELTa`` command.

    Description:
        - This command queries the vertical cursor's delta T readout value for the specified
          Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:VBArs:DELTa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:VBArs:DELTa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:VBArs:DELTa?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
    """


class DisplayMathfftview1CursorVbarsBunits(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:VBArs:BUNIts`` command.

    Description:
        - This command queries the vertical cursor B measurement units for the specified Math-FFT
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:VBArs:BUNIts?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:VBArs:BUNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:VBArs:BUNIts?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
    """


class DisplayMathfftview1CursorVbarsBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:VBArs:BPOSition`` command.

    Description:
        - This command sets or queries the vertical cursor B position for the specified Math-FFT
          view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:MATHFFTView1:CURSor:VBArs:BPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:VBArs:BPOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:VBArs:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:VBArs:BPOSition <NR3>
        - DISplay:MATHFFTView1:CURSor:VBArs:BPOSition?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` sets the vertical cursor B position in the specified view.
    """


class DisplayMathfftview1CursorVbarsAunits(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:VBArs:AUNIts`` command.

    Description:
        - This command queries the vertical cursor A measurement units for the specified Math-FFT
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:VBArs:AUNIts?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:VBArs:AUNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:VBArs:AUNIts?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
    """


class DisplayMathfftview1CursorVbarsAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:VBArs:APOSition`` command.

    Description:
        - This command sets or queries the horizontal cursor A position for the specified Math-FFT
          view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:MATHFFTView1:CURSor:VBArs:APOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:VBArs:APOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:VBArs:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:VBArs:APOSition <NR3>
        - DISplay:MATHFFTView1:CURSor:VBArs:APOSition?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` sets the vertical cursor A position in the specified view.
    """


class DisplayMathfftview1CursorVbars(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:VBArs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:VBArs?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:CURSor:VBArs?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.aposition``: The ``DISplay:MATHFFTView1:CURSor:VBArs:APOSition`` command.
        - ``.aunits``: The ``DISplay:MATHFFTView1:CURSor:VBArs:AUNIts`` command.
        - ``.bposition``: The ``DISplay:MATHFFTView1:CURSor:VBArs:BPOSition`` command.
        - ``.bunits``: The ``DISplay:MATHFFTView1:CURSor:VBArs:BUNIts`` command.
        - ``.delta``: The ``DISplay:MATHFFTView1:CURSor:VBArs:DELTa`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aposition = DisplayMathfftview1CursorVbarsAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._aunits = DisplayMathfftview1CursorVbarsAunits(device, f"{self._cmd_syntax}:AUNIts")
        self._bposition = DisplayMathfftview1CursorVbarsBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )
        self._bunits = DisplayMathfftview1CursorVbarsBunits(device, f"{self._cmd_syntax}:BUNIts")
        self._delta = DisplayMathfftview1CursorVbarsDelta(device, f"{self._cmd_syntax}:DELTa")

    @property
    def aposition(self) -> DisplayMathfftview1CursorVbarsAposition:
        """Return the ``DISplay:MATHFFTView1:CURSor:VBArs:APOSition`` command.

        Description:
            - This command sets or queries the horizontal cursor A position for the specified
              Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:APOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:VBArs:APOSition <NR3>
            - DISplay:MATHFFTView1:CURSor:VBArs:APOSition?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` sets the vertical cursor A position in the specified view.
        """
        return self._aposition

    @property
    def aunits(self) -> DisplayMathfftview1CursorVbarsAunits:
        """Return the ``DISplay:MATHFFTView1:CURSor:VBArs:AUNIts`` command.

        Description:
            - This command queries the vertical cursor A measurement units for the specified
              Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:AUNIts?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:AUNIts?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:VBArs:AUNIts?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
        """
        return self._aunits

    @property
    def bposition(self) -> DisplayMathfftview1CursorVbarsBposition:
        """Return the ``DISplay:MATHFFTView1:CURSor:VBArs:BPOSition`` command.

        Description:
            - This command sets or queries the vertical cursor B position for the specified Math-FFT
              view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:BPOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:VBArs:BPOSition <NR3>
            - DISplay:MATHFFTView1:CURSor:VBArs:BPOSition?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` sets the vertical cursor B position in the specified view.
        """
        return self._bposition

    @property
    def bunits(self) -> DisplayMathfftview1CursorVbarsBunits:
        """Return the ``DISplay:MATHFFTView1:CURSor:VBArs:BUNIts`` command.

        Description:
            - This command queries the vertical cursor B measurement units for the specified
              Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:BUNIts?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:BUNIts?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:VBArs:BUNIts?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
        """
        return self._bunits

    @property
    def delta(self) -> DisplayMathfftview1CursorVbarsDelta:
        """Return the ``DISplay:MATHFFTView1:CURSor:VBArs:DELTa`` command.

        Description:
            - This command queries the vertical cursor's delta T readout value for the specified
              Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:DELTa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs:DELTa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:VBArs:DELTa?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
        """
        return self._delta


class DisplayMathfftview1CursorState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:STATE`` command.

    Description:
        - This command sets or queries the visible state of cursors for the specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:CURSor:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:STATE value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:STATE {ON|OFF|<NR1>}
        - DISplay:MATHFFTView1:CURSor:STATE?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``ON`` enables the cursors.
        - ``1`` enables the cursors.
        - ``OFF`` disables the cursors.
        - ``0`` disables the cursors.
        - ``<NR1>`` = 0 turns off cursors; any other value displays cursors.
    """


class DisplayMathfftview1CursorScreenByposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition`` command.

    Description:
        - This command sets or returns the vertical cursor B y-axis amplitude measurement value of
          the specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition <NR3>
        - DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the vertical cursor B position of the specified cursor in the specified view.
    """


class DisplayMathfftview1CursorScreenBxposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition`` command.

    Description:
        - This command sets or returns the vertical cursor Bx-axis waveform time measurement
          position of the specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition <NR3>
        - DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
          view.
    """


class DisplayMathfftview1CursorScreenAyposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition`` command.

    Description:
        - This command sets or returns the vertical cursor A y-axis amplitude measurement value of
          the specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition <NR3>
        - DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the cursor A position of the specified cursor in the specified view.
    """


class DisplayMathfftview1CursorScreenAxposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition`` command.

    Description:
        - This command sets or returns the vertical cursor A x-axis waveform measurement position of
          the specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition <NR3>
        - DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the cursor position in MHz.
    """


class DisplayMathfftview1CursorScreen(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:SCREEN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:SCREEN?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:CURSor:SCREEN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.axposition``: The ``DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition`` command.
        - ``.ayposition``: The ``DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition`` command.
        - ``.bxposition``: The ``DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition`` command.
        - ``.byposition``: The ``DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._axposition = DisplayMathfftview1CursorScreenAxposition(
            device, f"{self._cmd_syntax}:AXPOSition"
        )
        self._ayposition = DisplayMathfftview1CursorScreenAyposition(
            device, f"{self._cmd_syntax}:AYPOSition"
        )
        self._bxposition = DisplayMathfftview1CursorScreenBxposition(
            device, f"{self._cmd_syntax}:BXPOSition"
        )
        self._byposition = DisplayMathfftview1CursorScreenByposition(
            device, f"{self._cmd_syntax}:BYPOSition"
        )

    @property
    def axposition(self) -> DisplayMathfftview1CursorScreenAxposition:
        """Return the ``DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition`` command.

        Description:
            - This command sets or returns the vertical cursor A x-axis waveform measurement
              position of the specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition <NR3>
            - DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the cursor position in MHz.
        """
        return self._axposition

    @property
    def ayposition(self) -> DisplayMathfftview1CursorScreenAyposition:
        """Return the ``DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition`` command.

        Description:
            - This command sets or returns the vertical cursor A y-axis amplitude measurement value
              of the specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition <NR3>
            - DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the cursor A position of the specified cursor in the specified view.
        """
        return self._ayposition

    @property
    def bxposition(self) -> DisplayMathfftview1CursorScreenBxposition:
        """Return the ``DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition`` command.

        Description:
            - This command sets or returns the vertical cursor Bx-axis waveform time measurement
              position of the specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition <NR3>
            - DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the horizontal cursor B position of the specified cursor in the specified
              view.
        """
        return self._bxposition

    @property
    def byposition(self) -> DisplayMathfftview1CursorScreenByposition:
        """Return the ``DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition`` command.

        Description:
            - This command sets or returns the vertical cursor B y-axis amplitude measurement value
              of the specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition <NR3>
            - DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the vertical cursor B position of the specified cursor in the specified
              view.
        """
        return self._byposition


class DisplayMathfftview1CursorRolocation(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:ROLOCATION`` command.

    Description:
        - This command sets or queries the location to display the specified Math FFT plot cursor
          readouts (in the plot graticule or in a badge in the Results Bar).

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:ROLOCATION?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:ROLOCATION?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:ROLOCATION value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:ROLOCATION {GRATICULE|BADGE}
        - DISplay:MATHFFTView1:CURSor:ROLOCATION?
        ```

    Info:
        - ``1`` is the Math FFT plot number.
        - ``GRATICULE`` sets the Math FFT plot cursor readouts to display as part of the cursors in
          the plot view.
        - ``BADGE`` removes the Math FFT plot cursor readouts from the cursors in the graticule and
          displays the cursor information as a badge in the Results Bar.
    """


class DisplayMathfftview1CursorOneoverdeltatvalue(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:ONEOVERDELTATVALUE`` command.

    Description:
        - This command queries the one over delta cursor readout value of the specified Math-FFT
          view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:MATHFFTView1:CURSor:ONEOVERDELTATVALUE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:ONEOVERDELTATVALUE?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:ONEOVERDELTATVALUE?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
    """


class DisplayMathfftview1CursorMode(SCPICmdWrite):
    """The ``DISplay:MATHFFTView1:CURSor:MODe`` command.

    Description:
        - This command sets or queries the cursor tracking mode of the specified Math-FFT view.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:MODe value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:MODe {INDEPENDENT|TRACK}
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``INDEPENDENT`` allows independent adjustment of the two cursors.
        - ``TRACK`` ties the navigational functionality of the two cursors together. For cursor 1
          adjustments, this ties the movement of the two cursors together; however, cursor 2
          continues to move independently of cursor 1.
    """


class DisplayMathfftview1CursorHbarsDelta(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:HBArs:DELTa`` command.

    Description:
        - This command queries the horizontal cursor's delta value of the specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:HBArs:DELTa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:HBArs:DELTa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:HBArs:DELTa?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
    """


class DisplayMathfftview1CursorHbarsBunits(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:HBArs:BUNIts`` command.

    Description:
        - This command queries the vertical units of horizontal cursor B for the specified Math-FFT
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:HBArs:BUNIts?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:HBArs:BUNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:HBArs:BUNIts?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
    """


class DisplayMathfftview1CursorHbarsBposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:HBArs:BPOSition`` command.

    Description:
        - This command sets or returns the position of horizontal cursor B for the specified
          Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:MATHFFTView1:CURSor:HBArs:BPOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:HBArs:BPOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:HBArs:BPOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:HBArs:BPOSition <NR3>
        - DISplay:MATHFFTView1:CURSor:HBArs:BPOSition?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the vertical cursor B position for the specified Math-FFT view.
    """


class DisplayMathfftview1CursorHbarsAunits(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:HBArs:AUNIts`` command.

    Description:
        - This command queries the vertical units of horizontal cursor A for the specified Math-FFT
          view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:HBArs:AUNIts?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:HBArs:AUNIts?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:HBArs:AUNIts?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
    """


class DisplayMathfftview1CursorHbarsAposition(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:HBArs:APOSition`` command.

    Description:
        - This command sets or returns the position of horizontal cursor A for the specified
          Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:MATHFFTView1:CURSor:HBArs:APOSition?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:HBArs:APOSition?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:HBArs:APOSition value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:HBArs:APOSition <NR3>
        - DISplay:MATHFFTView1:CURSor:HBArs:APOSition?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``<NR3>`` is the cursor position of the specified cursor in the specified view.
    """


class DisplayMathfftview1CursorHbars(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:HBArs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:HBArs?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:CURSor:HBArs?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.aposition``: The ``DISplay:MATHFFTView1:CURSor:HBArs:APOSition`` command.
        - ``.aunits``: The ``DISplay:MATHFFTView1:CURSor:HBArs:AUNIts`` command.
        - ``.bposition``: The ``DISplay:MATHFFTView1:CURSor:HBArs:BPOSition`` command.
        - ``.bunits``: The ``DISplay:MATHFFTView1:CURSor:HBArs:BUNIts`` command.
        - ``.delta``: The ``DISplay:MATHFFTView1:CURSor:HBArs:DELTa`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aposition = DisplayMathfftview1CursorHbarsAposition(
            device, f"{self._cmd_syntax}:APOSition"
        )
        self._aunits = DisplayMathfftview1CursorHbarsAunits(device, f"{self._cmd_syntax}:AUNIts")
        self._bposition = DisplayMathfftview1CursorHbarsBposition(
            device, f"{self._cmd_syntax}:BPOSition"
        )
        self._bunits = DisplayMathfftview1CursorHbarsBunits(device, f"{self._cmd_syntax}:BUNIts")
        self._delta = DisplayMathfftview1CursorHbarsDelta(device, f"{self._cmd_syntax}:DELTa")

    @property
    def aposition(self) -> DisplayMathfftview1CursorHbarsAposition:
        """Return the ``DISplay:MATHFFTView1:CURSor:HBArs:APOSition`` command.

        Description:
            - This command sets or returns the position of horizontal cursor A for the specified
              Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:APOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:APOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:APOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:HBArs:APOSition <NR3>
            - DISplay:MATHFFTView1:CURSor:HBArs:APOSition?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the cursor position of the specified cursor in the specified view.
        """
        return self._aposition

    @property
    def aunits(self) -> DisplayMathfftview1CursorHbarsAunits:
        """Return the ``DISplay:MATHFFTView1:CURSor:HBArs:AUNIts`` command.

        Description:
            - This command queries the vertical units of horizontal cursor A for the specified
              Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:AUNIts?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:AUNIts?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:HBArs:AUNIts?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
        """
        return self._aunits

    @property
    def bposition(self) -> DisplayMathfftview1CursorHbarsBposition:
        """Return the ``DISplay:MATHFFTView1:CURSor:HBArs:BPOSition`` command.

        Description:
            - This command sets or returns the position of horizontal cursor B for the specified
              Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:BPOSition?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:BPOSition?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:BPOSition value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:HBArs:BPOSition <NR3>
            - DISplay:MATHFFTView1:CURSor:HBArs:BPOSition?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``<NR3>`` is the vertical cursor B position for the specified Math-FFT view.
        """
        return self._bposition

    @property
    def bunits(self) -> DisplayMathfftview1CursorHbarsBunits:
        """Return the ``DISplay:MATHFFTView1:CURSor:HBArs:BUNIts`` command.

        Description:
            - This command queries the vertical units of horizontal cursor B for the specified
              Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:BUNIts?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:BUNIts?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:HBArs:BUNIts?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
        """
        return self._bunits

    @property
    def delta(self) -> DisplayMathfftview1CursorHbarsDelta:
        """Return the ``DISplay:MATHFFTView1:CURSor:HBArs:DELTa`` command.

        Description:
            - This command queries the horizontal cursor's delta value of the specified Math-FFT
              view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:DELTa?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs:DELTa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:HBArs:DELTa?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
        """
        return self._delta


class DisplayMathfftview1CursorFunction(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:FUNCtion`` command.

    Description:
        - This command sets or queries the cursor type for the specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:FUNCtion?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:FUNCtion?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:MATHFFTView1:CURSor:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:FUNCtion {WAVEform|VBArs|HBArs|SCREEN}
        - DISplay:MATHFFTView1:CURSor:FUNCtion?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``WAVEFORM`` specifies to display the paired vertical cursors in YT display format for
          measuring waveform amplitude and time. Measurements are taken at where the cursor
          intersects the waveform, and tracks waveform changes.
        - ``VBArs`` specifies vertical bar cursors, which measure in horizontal units.
        - ``HBArs`` specifies horizontal bar cursors, which measure in vertical units.
        - ``SCREEN`` specifies to display both horizontal and vertical bar cursors, which display
          the horizontal and vertical positions of the cursors, not waveform levels. Use these
          cursors to measure anywhere in the waveform display area.
    """


class DisplayMathfftview1CursorDdt(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:DDT`` command.

    Description:
        - This command queries the delta Y over delta X (ΔY/Δ X) cursor readout value of the
          specified cursor in the specified Math-FFT view.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:DDT?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:CURSor:DDT?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:DDT?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
    """


class DisplayMathfftview1CursorBsource(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:BSOUrce`` command.

    Description:
        - This command queries the Math-FFT waveform view source for cursor B.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:BSOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:CURSor:BSOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:BSOUrce?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
    """


class DisplayMathfftview1CursorAsource(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor:ASOUrce`` command.

    Description:
        - This command queries the Math-FFT waveform view source for cursor A.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:ASOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:CURSor:ASOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:CURSor:ASOUrce?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
    """


#  pylint: disable=too-many-instance-attributes
class DisplayMathfftview1Cursor(SCPICmdRead):
    """The ``DISplay:MATHFFTView1:CURSor`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:CURSor?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.asource``: The ``DISplay:MATHFFTView1:CURSor:ASOUrce`` command.
        - ``.bsource``: The ``DISplay:MATHFFTView1:CURSor:BSOUrce`` command.
        - ``.ddt``: The ``DISplay:MATHFFTView1:CURSor:DDT`` command.
        - ``.function``: The ``DISplay:MATHFFTView1:CURSor:FUNCtion`` command.
        - ``.hbars``: The ``DISplay:MATHFFTView1:CURSor:HBArs`` command tree.
        - ``.mode``: The ``DISplay:MATHFFTView1:CURSor:MODe`` command.
        - ``.oneoverdeltatvalue``: The ``DISplay:MATHFFTView1:CURSor:ONEOVERDELTATVALUE`` command.
        - ``.rolocation``: The ``DISplay:MATHFFTView1:CURSor:ROLOCATION`` command.
        - ``.screen``: The ``DISplay:MATHFFTView1:CURSor:SCREEN`` command tree.
        - ``.state``: The ``DISplay:MATHFFTView1:CURSor:STATE`` command.
        - ``.vbars``: The ``DISplay:MATHFFTView1:CURSor:VBArs`` command tree.
        - ``.waveform``: The ``DISplay:MATHFFTView1:CURSor:WAVEform`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._asource = DisplayMathfftview1CursorAsource(device, f"{self._cmd_syntax}:ASOUrce")
        self._bsource = DisplayMathfftview1CursorBsource(device, f"{self._cmd_syntax}:BSOUrce")
        self._ddt = DisplayMathfftview1CursorDdt(device, f"{self._cmd_syntax}:DDT")
        self._function = DisplayMathfftview1CursorFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._hbars = DisplayMathfftview1CursorHbars(device, f"{self._cmd_syntax}:HBArs")
        self._mode = DisplayMathfftview1CursorMode(device, f"{self._cmd_syntax}:MODe")
        self._oneoverdeltatvalue = DisplayMathfftview1CursorOneoverdeltatvalue(
            device, f"{self._cmd_syntax}:ONEOVERDELTATVALUE"
        )
        self._rolocation = DisplayMathfftview1CursorRolocation(
            device, f"{self._cmd_syntax}:ROLOCATION"
        )
        self._screen = DisplayMathfftview1CursorScreen(device, f"{self._cmd_syntax}:SCREEN")
        self._state = DisplayMathfftview1CursorState(device, f"{self._cmd_syntax}:STATE")
        self._vbars = DisplayMathfftview1CursorVbars(device, f"{self._cmd_syntax}:VBArs")
        self._waveform = DisplayMathfftview1CursorWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def asource(self) -> DisplayMathfftview1CursorAsource:
        """Return the ``DISplay:MATHFFTView1:CURSor:ASOUrce`` command.

        Description:
            - This command queries the Math-FFT waveform view source for cursor A.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:ASOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:ASOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:ASOUrce?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
        """
        return self._asource

    @property
    def bsource(self) -> DisplayMathfftview1CursorBsource:
        """Return the ``DISplay:MATHFFTView1:CURSor:BSOUrce`` command.

        Description:
            - This command queries the Math-FFT waveform view source for cursor B.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:BSOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:BSOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:BSOUrce?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
        """
        return self._bsource

    @property
    def ddt(self) -> DisplayMathfftview1CursorDdt:
        """Return the ``DISplay:MATHFFTView1:CURSor:DDT`` command.

        Description:
            - This command queries the delta Y over delta X (ΔY/Δ X) cursor readout value of the
              specified cursor in the specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:DDT?``
              query.
            - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:CURSor:DDT?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:DDT?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
        """
        return self._ddt

    @property
    def function(self) -> DisplayMathfftview1CursorFunction:
        """Return the ``DISplay:MATHFFTView1:CURSor:FUNCtion`` command.

        Description:
            - This command sets or queries the cursor type for the specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:FUNCtion?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:FUNCtion?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:FUNCtion {WAVEform|VBArs|HBArs|SCREEN}
            - DISplay:MATHFFTView1:CURSor:FUNCtion?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``WAVEFORM`` specifies to display the paired vertical cursors in YT display format for
              measuring waveform amplitude and time. Measurements are taken at where the cursor
              intersects the waveform, and tracks waveform changes.
            - ``VBArs`` specifies vertical bar cursors, which measure in horizontal units.
            - ``HBArs`` specifies horizontal bar cursors, which measure in vertical units.
            - ``SCREEN`` specifies to display both horizontal and vertical bar cursors, which
              display the horizontal and vertical positions of the cursors, not waveform levels. Use
              these cursors to measure anywhere in the waveform display area.
        """
        return self._function

    @property
    def hbars(self) -> DisplayMathfftview1CursorHbars:
        """Return the ``DISplay:MATHFFTView1:CURSor:HBArs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:HBArs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:HBArs?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.aposition``: The ``DISplay:MATHFFTView1:CURSor:HBArs:APOSition`` command.
            - ``.aunits``: The ``DISplay:MATHFFTView1:CURSor:HBArs:AUNIts`` command.
            - ``.bposition``: The ``DISplay:MATHFFTView1:CURSor:HBArs:BPOSition`` command.
            - ``.bunits``: The ``DISplay:MATHFFTView1:CURSor:HBArs:BUNIts`` command.
            - ``.delta``: The ``DISplay:MATHFFTView1:CURSor:HBArs:DELTa`` command.
        """
        return self._hbars

    @property
    def mode(self) -> DisplayMathfftview1CursorMode:
        """Return the ``DISplay:MATHFFTView1:CURSor:MODe`` command.

        Description:
            - This command sets or queries the cursor tracking mode of the specified Math-FFT view.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:MODe value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:MODe {INDEPENDENT|TRACK}
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``INDEPENDENT`` allows independent adjustment of the two cursors.
            - ``TRACK`` ties the navigational functionality of the two cursors together. For cursor
              1 adjustments, this ties the movement of the two cursors together; however, cursor 2
              continues to move independently of cursor 1.
        """
        return self._mode

    @property
    def oneoverdeltatvalue(self) -> DisplayMathfftview1CursorOneoverdeltatvalue:
        """Return the ``DISplay:MATHFFTView1:CURSor:ONEOVERDELTATVALUE`` command.

        Description:
            - This command queries the one over delta cursor readout value of the specified Math-FFT
              view.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:ONEOVERDELTATVALUE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:ONEOVERDELTATVALUE?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:ONEOVERDELTATVALUE?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
        """
        return self._oneoverdeltatvalue

    @property
    def rolocation(self) -> DisplayMathfftview1CursorRolocation:
        """Return the ``DISplay:MATHFFTView1:CURSor:ROLOCATION`` command.

        Description:
            - This command sets or queries the location to display the specified Math FFT plot
              cursor readouts (in the plot graticule or in a badge in the Results Bar).

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:MATHFFTView1:CURSor:ROLOCATION?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:ROLOCATION?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:ROLOCATION value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:ROLOCATION {GRATICULE|BADGE}
            - DISplay:MATHFFTView1:CURSor:ROLOCATION?
            ```

        Info:
            - ``1`` is the Math FFT plot number.
            - ``GRATICULE`` sets the Math FFT plot cursor readouts to display as part of the cursors
              in the plot view.
            - ``BADGE`` removes the Math FFT plot cursor readouts from the cursors in the graticule
              and displays the cursor information as a badge in the Results Bar.
        """
        return self._rolocation

    @property
    def screen(self) -> DisplayMathfftview1CursorScreen:
        """Return the ``DISplay:MATHFFTView1:CURSor:SCREEN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:SCREEN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:SCREEN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.axposition``: The ``DISplay:MATHFFTView1:CURSor:SCREEN:AXPOSition`` command.
            - ``.ayposition``: The ``DISplay:MATHFFTView1:CURSor:SCREEN:AYPOSition`` command.
            - ``.bxposition``: The ``DISplay:MATHFFTView1:CURSor:SCREEN:BXPOSition`` command.
            - ``.byposition``: The ``DISplay:MATHFFTView1:CURSor:SCREEN:BYPOSition`` command.
        """
        return self._screen

    @property
    def state(self) -> DisplayMathfftview1CursorState:
        """Return the ``DISplay:MATHFFTView1:CURSor:STATE`` command.

        Description:
            - This command sets or queries the visible state of cursors for the specified Math-FFT
              view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:CURSor:STATE {ON|OFF|<NR1>}
            - DISplay:MATHFFTView1:CURSor:STATE?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``ON`` enables the cursors.
            - ``1`` enables the cursors.
            - ``OFF`` disables the cursors.
            - ``0`` disables the cursors.
            - ``<NR1>`` = 0 turns off cursors; any other value displays cursors.
        """
        return self._state

    @property
    def vbars(self) -> DisplayMathfftview1CursorVbars:
        """Return the ``DISplay:MATHFFTView1:CURSor:VBArs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:VBArs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:VBArs?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.aposition``: The ``DISplay:MATHFFTView1:CURSor:VBArs:APOSition`` command.
            - ``.aunits``: The ``DISplay:MATHFFTView1:CURSor:VBArs:AUNIts`` command.
            - ``.bposition``: The ``DISplay:MATHFFTView1:CURSor:VBArs:BPOSition`` command.
            - ``.bunits``: The ``DISplay:MATHFFTView1:CURSor:VBArs:BUNIts`` command.
            - ``.delta``: The ``DISplay:MATHFFTView1:CURSor:VBArs:DELTa`` command.
        """
        return self._vbars

    @property
    def waveform(self) -> DisplayMathfftview1CursorWaveform:
        """Return the ``DISplay:MATHFFTView1:CURSor:WAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor:WAVEform?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:MATHFFTView1:CURSor:WAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.aposition``: The ``DISplay:MATHFFTView1:CURSor:WAVEform:APOSition`` command.
            - ``.bposition``: The ``DISplay:MATHFFTView1:CURSor:WAVEform:BPOSition`` command.
        """
        return self._waveform


class DisplayMathfftview1Autoscale(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:MATHFFTView1:AUTOScale`` command.

    Description:
        - This command sets or returns the enabled state of autoscale for Math/FFT waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:AUTOScale?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:AUTOScale?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:MATHFFTView1:AUTOScale value``
          command.

    SCPI Syntax:
        ```
        - DISplay:MATHFFTView1:AUTOScale {ON|OFF|<NR1>}
        - DISplay:MATHFFTView1:AUTOScale?
        ```

    Info:
        - ``1`` is the Math-FFT waveform number.
        - ``OFF`` disables the autoscale feature.
        - ``ON`` enables the autoscale feature.
        - ``<NR1>`` = 0 disables the autoscale feature; any other value enables the autoscale
          feature.
    """


class DisplayMathfftview1(SCPICmdRead):
    """The ``DISplay:MATHFFTView1`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autoscale``: The ``DISplay:MATHFFTView1:AUTOScale`` command.
        - ``.cursor``: The ``DISplay:MATHFFTView1:CURSor`` command tree.
        - ``.gridlines``: The ``DISplay:MATHFFTView1:GRIDlines`` command.
        - ``.math``: The ``DISplay:MATHFFTView1:MATH`` command tree.
        - ``.xaxis``: The ``DISplay:MATHFFTView1:XAXIS`` command tree.
        - ``.yaxis``: The ``DISplay:MATHFFTView1:YAXIS`` command tree.
        - ``.zoom``: The ``DISplay:MATHFFTView1:ZOOM`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoscale = DisplayMathfftview1Autoscale(device, f"{self._cmd_syntax}:AUTOScale")
        self._cursor = DisplayMathfftview1Cursor(device, f"{self._cmd_syntax}:CURSor")
        self._gridlines = DisplayMathfftview1Gridlines(device, f"{self._cmd_syntax}:GRIDlines")
        self._math = DisplayMathfftview1Math(device, f"{self._cmd_syntax}:MATH")
        self._xaxis = DisplayMathfftview1Xaxis(device, f"{self._cmd_syntax}:XAXIS")
        self._yaxis = DisplayMathfftview1Yaxis(device, f"{self._cmd_syntax}:YAXIS")
        self._zoom = DisplayMathfftview1Zoom(device, f"{self._cmd_syntax}:ZOOM")

    @property
    def autoscale(self) -> DisplayMathfftview1Autoscale:
        """Return the ``DISplay:MATHFFTView1:AUTOScale`` command.

        Description:
            - This command sets or returns the enabled state of autoscale for Math/FFT waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:AUTOScale?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:AUTOScale?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:AUTOScale value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:AUTOScale {ON|OFF|<NR1>}
            - DISplay:MATHFFTView1:AUTOScale?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``OFF`` disables the autoscale feature.
            - ``ON`` enables the autoscale feature.
            - ``<NR1>`` = 0 disables the autoscale feature; any other value enables the autoscale
              feature.
        """
        return self._autoscale

    @property
    def cursor(self) -> DisplayMathfftview1Cursor:
        """Return the ``DISplay:MATHFFTView1:CURSor`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:CURSor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:CURSor?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.asource``: The ``DISplay:MATHFFTView1:CURSor:ASOUrce`` command.
            - ``.bsource``: The ``DISplay:MATHFFTView1:CURSor:BSOUrce`` command.
            - ``.ddt``: The ``DISplay:MATHFFTView1:CURSor:DDT`` command.
            - ``.function``: The ``DISplay:MATHFFTView1:CURSor:FUNCtion`` command.
            - ``.hbars``: The ``DISplay:MATHFFTView1:CURSor:HBArs`` command tree.
            - ``.mode``: The ``DISplay:MATHFFTView1:CURSor:MODe`` command.
            - ``.oneoverdeltatvalue``: The ``DISplay:MATHFFTView1:CURSor:ONEOVERDELTATVALUE``
              command.
            - ``.rolocation``: The ``DISplay:MATHFFTView1:CURSor:ROLOCATION`` command.
            - ``.screen``: The ``DISplay:MATHFFTView1:CURSor:SCREEN`` command tree.
            - ``.state``: The ``DISplay:MATHFFTView1:CURSor:STATE`` command.
            - ``.vbars``: The ``DISplay:MATHFFTView1:CURSor:VBArs`` command tree.
            - ``.waveform``: The ``DISplay:MATHFFTView1:CURSor:WAVEform`` command tree.
        """
        return self._cursor

    @property
    def gridlines(self) -> DisplayMathfftview1Gridlines:
        """Return the ``DISplay:MATHFFTView1:GRIDlines`` command.

        Description:
            - This command sets or queries the grid lines setting for the specified Math-FFT view.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:GRIDlines?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:GRIDlines?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:MATHFFTView1:GRIDlines value`` command.

        SCPI Syntax:
            ```
            - DISplay:MATHFFTView1:GRIDlines {HORizontal|VERTical|BOTH}
            - DISplay:MATHFFTView1:GRIDlines?
            ```

        Info:
            - ``1`` is the Math-FFT waveform number.
            - ``HORizontal`` specifies horizontal grid lines.
            - ``VERTical`` specifies vertical grid lines.
            - ``BOTH`` specifies both vertical and horizontal grid lines.
        """
        return self._gridlines

    @property
    def math(self) -> DisplayMathfftview1Math:
        """Return the ``DISplay:MATHFFTView1:MATH`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:MATH?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:MATH?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.math``: The ``DISplay:MATHFFTView1:MATH:MATH<x>`` command tree.
        """
        return self._math

    @property
    def xaxis(self) -> DisplayMathfftview1Xaxis:
        """Return the ``DISplay:MATHFFTView1:XAXIS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:XAXIS?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:XAXIS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DISplay:MATHFFTView1:XAXIS:SCALE`` command.
        """
        return self._xaxis

    @property
    def yaxis(self) -> DisplayMathfftview1Yaxis:
        """Return the ``DISplay:MATHFFTView1:YAXIS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:YAXIS?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:YAXIS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.scale``: The ``DISplay:MATHFFTView1:YAXIS:SCALE`` command.
        """
        return self._yaxis

    @property
    def zoom(self) -> DisplayMathfftview1Zoom:
        """Return the ``DISplay:MATHFFTView1:ZOOM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1:ZOOM?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1:ZOOM?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.xaxis``: The ``DISplay:MATHFFTView1:ZOOM:XAXIS`` command tree.
            - ``.yaxis``: The ``DISplay:MATHFFTView1:ZOOM:YAXIS`` command tree.
        """
        return self._zoom


class DisplayIntensityBacklightAutodimTime(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe`` command.

    Description:
        - Sets or queries the amount of time, in minutes, to wait for no user interface activity
          before automatically dimming the display. The time can range from a minimum of 10 minutes
          to a maximum of 1440 minutes (24 hours). The default is 10 minutes.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe value`` command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:BACKLight:AUTODim:TIMe <NR1>
        - DISplay:INTENSITy:BACKLight:AUTODim:TIMe?
        ```

    Info:
        - ``<NR1>`` is the amount of time, in minutes, to wait for no user interface activity before
          automatically dimming the display.
    """


class DisplayIntensityBacklightAutodimEnable(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble`` command.

    Description:
        - Sets or queries the state of the display auto-dim feature. The default is enabled. Once
          the backlight has dimmed, any button push, knob turn or mouse movement returns the
          backlight value to the value set by ``:DISplay:INTENSITy:BACKLight``.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble value`` command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:BACKLight:AUTODim:ENAble {ON|OFF}
        - DISplay:INTENSITy:BACKLight:AUTODim:ENAble?
        ```

    Info:
        - ``ON`` enables the display auto-dim feature.
        - ``OFF`` disables the display auto-dim feature.
    """


class DisplayIntensityBacklightAutodim(SCPICmdRead):
    """The ``DISplay:INTENSITy:BACKLight:AUTODim`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight:AUTODim?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:BACKLight:AUTODim?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble`` command.
        - ``.time``: The ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = DisplayIntensityBacklightAutodimEnable(device, f"{self._cmd_syntax}:ENAble")
        self._time = DisplayIntensityBacklightAutodimTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def enable(self) -> DisplayIntensityBacklightAutodimEnable:
        """Return the ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble`` command.

        Description:
            - Sets or queries the state of the display auto-dim feature. The default is enabled.
              Once the backlight has dimmed, any button push, knob turn or mouse movement returns
              the backlight value to the value set by ``:DISplay:INTENSITy:BACKLight``.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble value`` command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:BACKLight:AUTODim:ENAble {ON|OFF}
            - DISplay:INTENSITy:BACKLight:AUTODim:ENAble?
            ```

        Info:
            - ``ON`` enables the display auto-dim feature.
            - ``OFF`` disables the display auto-dim feature.
        """
        return self._enable

    @property
    def time(self) -> DisplayIntensityBacklightAutodimTime:
        """Return the ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe`` command.

        Description:
            - Sets or queries the amount of time, in minutes, to wait for no user interface activity
              before automatically dimming the display. The time can range from a minimum of 10
              minutes to a maximum of 1440 minutes (24 hours). The default is 10 minutes.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe value`` command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:BACKLight:AUTODim:TIMe <NR1>
            - DISplay:INTENSITy:BACKLight:AUTODim:TIMe?
            ```

        Info:
            - ``<NR1>`` is the amount of time, in minutes, to wait for no user interface activity
              before automatically dimming the display.
        """
        return self._time


class DisplayIntensityBacklight(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:BACKLight`` command.

    Description:
        - This command sets or queries the display backlight intensity setting.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:BACKLight?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:BACKLight value``
          command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:BACKLight {LOW|MEDium|HIGH}
        - DISplay:INTENSITy:BACKLight?
        ```

    Info:
        - ``LOW`` selects a low brightness level.
        - ``MEDium`` selects a moderate brightness level.
        - ``HIGH`` selects a full brightness level.

    Properties:
        - ``.autodim``: The ``DISplay:INTENSITy:BACKLight:AUTODim`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autodim = DisplayIntensityBacklightAutodim(device, f"{self._cmd_syntax}:AUTODim")

    @property
    def autodim(self) -> DisplayIntensityBacklightAutodim:
        """Return the ``DISplay:INTENSITy:BACKLight:AUTODim`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight:AUTODim?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble`` command.
            - ``.time``: The ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe`` command.
        """
        return self._autodim


class DisplayIntensity(SCPICmdRead):
    """The ``DISplay:INTENSITy`` command.

    Description:
        - This query-only command returns the waveform saturation level and screen saver settings.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy?
        ```

    Properties:
        - ``.backlight``: The ``DISplay:INTENSITy:BACKLight`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._backlight = DisplayIntensityBacklight(device, f"{self._cmd_syntax}:BACKLight")

    @property
    def backlight(self) -> DisplayIntensityBacklight:
        """Return the ``DISplay:INTENSITy:BACKLight`` command.

        Description:
            - This command sets or queries the display backlight intensity setting.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:BACKLight?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:BACKLight value``
              command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:BACKLight {LOW|MEDium|HIGH}
            - DISplay:INTENSITy:BACKLight?
            ```

        Info:
            - ``LOW`` selects a low brightness level.
            - ``MEDium`` selects a moderate brightness level.
            - ``HIGH`` selects a full brightness level.

        Sub-properties:
            - ``.autodim``: The ``DISplay:INTENSITy:BACKLight:AUTODim`` command tree.
        """
        return self._backlight


class DisplayGlobalRefItemState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:GLObal:REF<x>:STATE`` command.

    Description:
        - this command sets or queries the global state (display mode On or Off) of the specified
          reference waveform. Setting this value true (On or NR1 ≠ 0 ) turns on the source in the
          waveform view. Setting this value false (Off or NR1 = 0 ) turns off the source in the
          waveform view. This command only works if the specified reference waveform is added
          already.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLObal:REF<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:REF<x>:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:GLObal:REF<x>:STATE value``
          command.

    SCPI Syntax:
        ```
        - DISplay:GLObal:REF<x>:STATE {ON|OFF|<NR1>}
        - DISplay:GLObal:REF<x>:STATE?
        ```

    Info:
        - ``REF<x>`` is the Reference waveform number.
        - ``<NR1>`` = 0 disables the display of the specified reference; any other value enables
          display of the reference.
        - ``ON`` enables display of the specified reference.
        - ``OFF`` disables display of the specified reference.
    """


class DisplayGlobalRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:GLObal:REF<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLObal:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:REF<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``REF<x>`` is the Reference waveform number.

    Properties:
        - ``.state``: The ``DISplay:GLObal:REF<x>:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayGlobalRefItemState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> DisplayGlobalRefItemState:
        """Return the ``DISplay:GLObal:REF<x>:STATE`` command.

        Description:
            - this command sets or queries the global state (display mode On or Off) of the
              specified reference waveform. Setting this value true (On or NR1 ≠ 0 ) turns on the
              source in the waveform view. Setting this value false (Off or NR1 = 0 ) turns off the
              source in the waveform view. This command only works if the specified reference
              waveform is added already.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLObal:REF<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:REF<x>:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:GLObal:REF<x>:STATE value``
              command.

        SCPI Syntax:
            ```
            - DISplay:GLObal:REF<x>:STATE {ON|OFF|<NR1>}
            - DISplay:GLObal:REF<x>:STATE?
            ```

        Info:
            - ``REF<x>`` is the Reference waveform number.
            - ``<NR1>`` = 0 disables the display of the specified reference; any other value enables
              display of the reference.
            - ``ON`` enables display of the specified reference.
            - ``OFF`` disables display of the specified reference.
        """
        return self._state


class DisplayGlobalMathItemState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:GLObal:MATH<x>:STATE`` command.

    Description:
        - This command sets or queries the global state (display mode On or Off) of the specified
          math. Setting this value true (On or NR1 ≠ 0 ) turns on the source in the waveform view.
          Setting this value false (Off or NR1 = 0 ) turns off the source in the waveform view. This
          command only works if the specified math waveform is added already.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLObal:MATH<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:MATH<x>:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:GLObal:MATH<x>:STATE value``
          command.

    SCPI Syntax:
        ```
        - DISplay:GLObal:MATH<x>:STATE {ON|OFF|<NR1>}
        - DISplay:GLObal:MATH<x>:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the display of the specified math; any other value enables display
          of the math.
        - ``ON`` enables display of the specified math.
        - ``OFF`` disables display of the specified math.
    """


class DisplayGlobalMathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:GLObal:MATH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLObal:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:MATH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DISplay:GLObal:MATH<x>:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayGlobalMathItemState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> DisplayGlobalMathItemState:
        """Return the ``DISplay:GLObal:MATH<x>:STATE`` command.

        Description:
            - This command sets or queries the global state (display mode On or Off) of the
              specified math. Setting this value true (On or NR1 ≠ 0 ) turns on the source in the
              waveform view. Setting this value false (Off or NR1 = 0 ) turns off the source in the
              waveform view. This command only works if the specified math waveform is added
              already.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLObal:MATH<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:MATH<x>:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:GLObal:MATH<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - DISplay:GLObal:MATH<x>:STATE {ON|OFF|<NR1>}
            - DISplay:GLObal:MATH<x>:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the display of the specified math; any other value enables
              display of the math.
            - ``ON`` enables display of the specified math.
            - ``OFF`` disables display of the specified math.
        """
        return self._state


class DisplayGlobalDchItemState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:GLObal:DCH<x>:STATE`` command.

    Description:
        - This command sets or queries the global state (display mode On or Off) of the specified
          channel (digital). Setting this value true (On or NR1 ≠ 0 ) turns on the source in the
          waveform view. Setting this value false (Off or NR1 = 0 ) turns off the source in the
          waveform view. This command only works if the specified channel is added already.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLObal:DCH<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:DCH<x>:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:GLObal:DCH<x>:STATE value``
          command.

    SCPI Syntax:
        ```
        - DISplay:GLObal:DCH<x>:STATE {ON|OFF|<NR1>}
        - DISplay:GLObal:DCH<x>:STATE?
        ```

    Info:
        - ``DCH<x>`` = specifies the digital channel. The supported value is 1.
        - ``<NR1>`` = 0 disables the display of the specified digital channel; any other value
          enables display of the channel.
        - ``ON`` enables display of the specified digital channel.
        - ``OFF`` disables display of the specified digital channel.
    """


class DisplayGlobalDchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:GLObal:DCH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLObal:DCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:DCH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``DCH<x>`` = specifies the digital channel. The supported value is 1.

    Properties:
        - ``.state``: The ``DISplay:GLObal:DCH<x>:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayGlobalDchItemState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> DisplayGlobalDchItemState:
        """Return the ``DISplay:GLObal:DCH<x>:STATE`` command.

        Description:
            - This command sets or queries the global state (display mode On or Off) of the
              specified channel (digital). Setting this value true (On or NR1 ≠ 0 ) turns on the
              source in the waveform view. Setting this value false (Off or NR1 = 0 ) turns off the
              source in the waveform view. This command only works if the specified channel is added
              already.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLObal:DCH<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:DCH<x>:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:GLObal:DCH<x>:STATE value``
              command.

        SCPI Syntax:
            ```
            - DISplay:GLObal:DCH<x>:STATE {ON|OFF|<NR1>}
            - DISplay:GLObal:DCH<x>:STATE?
            ```

        Info:
            - ``DCH<x>`` = specifies the digital channel. The supported value is 1.
            - ``<NR1>`` = 0 disables the display of the specified digital channel; any other value
              enables display of the channel.
            - ``ON`` enables display of the specified digital channel.
            - ``OFF`` disables display of the specified digital channel.
        """
        return self._state


class DisplayGlobalChannelState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:GLObal:CH<x>:STATE`` command.

    Description:
        - This command sets or queries the global state (display mode On or Off) of the specified
          channel (both analog and digital). Setting this value true (On or NR1 ≠ 0 ) turns on the
          source in the waveform view. Setting this value false (Off or NR1 = 0 ) turns off the
          source in the waveform view. This command only works if the specified channel is added
          already.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLObal:CH<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:CH<x>:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:GLObal:CH<x>:STATE value``
          command.

    SCPI Syntax:
        ```
        - DISplay:GLObal:CH<x>:STATE {ON|OFF|<NR1>}
        - DISplay:GLObal:CH<x>:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the display of the specified channel; any other value enables
          display of the channel.
        - ``ON`` enables display of the specified channel.
        - ``OFF`` disables display of the specified channel.
    """


class DisplayGlobalChannel(ValidatedChannel, SCPICmdRead):
    """The ``DISplay:GLObal:CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLObal:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DISplay:GLObal:CH<x>:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayGlobalChannelState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> DisplayGlobalChannelState:
        """Return the ``DISplay:GLObal:CH<x>:STATE`` command.

        Description:
            - This command sets or queries the global state (display mode On or Off) of the
              specified channel (both analog and digital). Setting this value true (On or NR1 ≠ 0 )
              turns on the source in the waveform view. Setting this value false (Off or NR1 = 0 )
              turns off the source in the waveform view. This command only works if the specified
              channel is added already.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLObal:CH<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:CH<x>:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:GLObal:CH<x>:STATE value``
              command.

        SCPI Syntax:
            ```
            - DISplay:GLObal:CH<x>:STATE {ON|OFF|<NR1>}
            - DISplay:GLObal:CH<x>:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the display of the specified channel; any other value enables
              display of the channel.
            - ``ON`` enables display of the specified channel.
            - ``OFF`` disables display of the specified channel.
        """
        return self._state


class DisplayGlobalBItemState(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:GLObal:B<x>:STATE`` command.

    Description:
        - This command sets or queries the global state (display mode On or Off) of the specified
          bus. Setting this value true (On or NR1 ≠ 0 ) turns on the source in the waveform view.
          Setting this value false (Off or NR1 = 0 ) turns off the source in the waveform view. This
          command only works if the specified bus is added already.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLObal:B<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:B<x>:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:GLObal:B<x>:STATE value``
          command.

    SCPI Syntax:
        ```
        - DISplay:GLObal:B<x>:STATE {ON|OFF|<NR1>}
        - DISplay:GLObal:B<x>:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables the display of the specified bus; any other value enables display
          of the bus.
        - ``ON`` enables display of the specified bus.
        - ``OFF`` disables display of the specified bus.
    """


class DisplayGlobalBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DISplay:GLObal:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLObal:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:B<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DISplay:GLObal:B<x>:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayGlobalBItemState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> DisplayGlobalBItemState:
        """Return the ``DISplay:GLObal:B<x>:STATE`` command.

        Description:
            - This command sets or queries the global state (display mode On or Off) of the
              specified bus. Setting this value true (On or NR1 ≠ 0 ) turns on the source in the
              waveform view. Setting this value false (Off or NR1 = 0 ) turns off the source in the
              waveform view. This command only works if the specified bus is added already.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLObal:B<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:B<x>:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:GLObal:B<x>:STATE value``
              command.

        SCPI Syntax:
            ```
            - DISplay:GLObal:B<x>:STATE {ON|OFF|<NR1>}
            - DISplay:GLObal:B<x>:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables the display of the specified bus; any other value enables
              display of the bus.
            - ``ON`` enables display of the specified bus.
            - ``OFF`` disables display of the specified bus.
        """
        return self._state


class DisplayGlobal(SCPICmdRead):
    """The ``DISplay:GLObal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLObal?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLObal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.b``: The ``DISplay:GLObal:B<x>`` command tree.
        - ``.ch``: The ``DISplay:GLObal:CH<x>`` command tree.
        - ``.dch``: The ``DISplay:GLObal:DCH<x>`` command tree.
        - ``.math``: The ``DISplay:GLObal:MATH<x>`` command tree.
        - ``.ref``: The ``DISplay:GLObal:REF<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._b: Dict[int, DisplayGlobalBItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayGlobalBItem(device, f"{self._cmd_syntax}:B{x}")
        )
        self._ch: Dict[int, DisplayGlobalChannel] = DefaultDictPassKeyToFactory(
            lambda x: DisplayGlobalChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._dch: Dict[int, DisplayGlobalDchItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayGlobalDchItem(device, f"{self._cmd_syntax}:DCH{x}")
        )
        self._math: Dict[int, DisplayGlobalMathItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayGlobalMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )
        self._ref: Dict[int, DisplayGlobalRefItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayGlobalRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def b(self) -> Dict[int, DisplayGlobalBItem]:
        """Return the ``DISplay:GLObal:B<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLObal:B<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:B<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DISplay:GLObal:B<x>:STATE`` command.
        """
        return self._b

    @property
    def ch(self) -> Dict[int, DisplayGlobalChannel]:
        """Return the ``DISplay:GLObal:CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLObal:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DISplay:GLObal:CH<x>:STATE`` command.
        """
        return self._ch

    @property
    def dch(self) -> Dict[int, DisplayGlobalDchItem]:
        """Return the ``DISplay:GLObal:DCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLObal:DCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:DCH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``DCH<x>`` = specifies the digital channel. The supported value is 1.

        Sub-properties:
            - ``.state``: The ``DISplay:GLObal:DCH<x>:STATE`` command.
        """
        return self._dch

    @property
    def math(self) -> Dict[int, DisplayGlobalMathItem]:
        """Return the ``DISplay:GLObal:MATH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLObal:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:MATH<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DISplay:GLObal:MATH<x>:STATE`` command.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, DisplayGlobalRefItem]:
        """Return the ``DISplay:GLObal:REF<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLObal:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLObal:REF<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``REF<x>`` is the Reference waveform number.

        Sub-properties:
            - ``.state``: The ``DISplay:GLObal:REF<x>:STATE`` command.
        """
        return self._ref


class DisplayColors(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLors`` command.

    Description:
        - Sets or queries the color mode for the graticule and waveform display.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLors?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLors?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:COLors value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLors {NORMal|INVERTed}
        - DISplay:COLors?
        ```

    Info:
        - ``NORMal`` specifies normal color mode.
        - ``INVERTed`` specifies inverted color mode.
    """


class DisplayChannelNormalcolor(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:CH<x>:NORMALColor`` command.

    Description:
        - This command sets or queries the normal mode color of the specified input source to the
          specified color. You can assign one of 48 unique colors to any channel, math, or reference
          waveform. These colors replace the default normal colors and remain in effect until you
          reset the colors.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:CH<x>:NORMALColor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:CH<x>:NORMALColor?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:CH<x>:NORMALColor value``
          command.

    SCPI Syntax:
        ```
        - DISplay:CH<x>:NORMALColor COLOR<y>
        - DISplay:CH<x>:NORMALColor?
        ```

    Info:
        - ``CH<x>`` specifies the input channel for which you want to change the waveform color,
          where <x> is the channel number.
        - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to 47.
    """


class DisplayChannelInvertcolor(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:CH<x>:INVERTColor`` command.

    Description:
        - This command sets or queries the Inverted mode color of the specified input source to the
          specified color. You can assign one of 48 unique colors to any channel, math, or reference
          waveform. These colors replace the default Inverted colors and remain in effect until you
          reset the colors.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:CH<x>:INVERTColor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:CH<x>:INVERTColor?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:CH<x>:INVERTColor value``
          command.

    SCPI Syntax:
        ```
        - DISplay:CH<x>:INVERTColor COLOR<y>
        - DISplay:CH<x>:INVERTColor?
        ```

    Info:
        - ``CH<x>`` specifies the input channel for which you want to change the waveform color,
          where <x> is the channel number.
        - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to 47.
    """


class DisplayChannel(ValidatedChannel, SCPICmdRead):
    """The ``DISplay:CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` specifies the input channel for which you want to change the waveform color,
          where <x> is the channel number.

    Properties:
        - ``.invertcolor``: The ``DISplay:CH<x>:INVERTColor`` command.
        - ``.normalcolor``: The ``DISplay:CH<x>:NORMALColor`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._invertcolor = DisplayChannelInvertcolor(device, f"{self._cmd_syntax}:INVERTColor")
        self._normalcolor = DisplayChannelNormalcolor(device, f"{self._cmd_syntax}:NORMALColor")

    @property
    def invertcolor(self) -> DisplayChannelInvertcolor:
        """Return the ``DISplay:CH<x>:INVERTColor`` command.

        Description:
            - This command sets or queries the Inverted mode color of the specified input source to
              the specified color. You can assign one of 48 unique colors to any channel, math, or
              reference waveform. These colors replace the default Inverted colors and remain in
              effect until you reset the colors.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:CH<x>:INVERTColor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:CH<x>:INVERTColor?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:CH<x>:INVERTColor value``
              command.

        SCPI Syntax:
            ```
            - DISplay:CH<x>:INVERTColor COLOR<y>
            - DISplay:CH<x>:INVERTColor?
            ```

        Info:
            - ``CH<x>`` specifies the input channel for which you want to change the waveform color,
              where <x> is the channel number.
            - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to
              47.
        """
        return self._invertcolor

    @property
    def normalcolor(self) -> DisplayChannelNormalcolor:
        """Return the ``DISplay:CH<x>:NORMALColor`` command.

        Description:
            - This command sets or queries the normal mode color of the specified input source to
              the specified color. You can assign one of 48 unique colors to any channel, math, or
              reference waveform. These colors replace the default normal colors and remain in
              effect until you reset the colors.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:CH<x>:NORMALColor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:CH<x>:NORMALColor?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:CH<x>:NORMALColor value``
              command.

        SCPI Syntax:
            ```
            - DISplay:CH<x>:NORMALColor COLOR<y>
            - DISplay:CH<x>:NORMALColor?
            ```

        Info:
            - ``CH<x>`` specifies the input channel for which you want to change the waveform color,
              where <x> is the channel number.
            - ``COLOR<y>`` specifies the color to assign to the specified waveform, where <y> = 0 to
              47.
        """
        return self._normalcolor


#  pylint: disable=too-many-instance-attributes
class Display(SCPICmdRead):
    """The ``DISplay`` command.

    Description:
        - This query-only command returns the current Display settings.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay?
        ```

    Properties:
        - ``.colors``: The ``DISplay:COLors`` command.
        - ``.global``: The ``DISplay:GLObal`` command tree.
        - ``.intensity``: The ``DISplay:INTENSITy`` command.
        - ``.mathfftview1``: The ``DISplay:MATHFFTView1`` command tree.
        - ``.persistence``: The ``DISplay:PERSistence`` command.
        - ``.plotview1``: The ``DISplay:PLOTView1`` command tree.
        - ``.reffftview``: The ``DISplay:REFFFTView<x>`` command tree.
        - ``.select``: The ``DISplay:SELect`` command tree.
        - ``.varpersist``: The ``DISplay:VARpersist`` command.
        - ``.waveview``: The ``DISplay:WAVEView`` command tree.
        - ``.waveview1``: The ``DISplay:WAVEView1`` command tree.
        - ``.waveform``: The ``DISplay:WAVEform`` command.
        - ``.ch``: The ``DISplay:CH<x>`` command tree.
        - ``.math``: The ``DISplay:Math<x>`` command tree.
        - ``.ref``: The ``DISplay:REF<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DISplay") -> None:
        super().__init__(device, cmd_syntax)
        self._colors = DisplayColors(device, f"{self._cmd_syntax}:COLors")
        self._global = DisplayGlobal(device, f"{self._cmd_syntax}:GLObal")
        self._intensity = DisplayIntensity(device, f"{self._cmd_syntax}:INTENSITy")
        self._mathfftview1 = DisplayMathfftview1(device, f"{self._cmd_syntax}:MATHFFTView1")
        self._persistence = DisplayPersistence(device, f"{self._cmd_syntax}:PERSistence")
        self._plotview1 = DisplayPlotview1(device, f"{self._cmd_syntax}:PLOTView1")
        self._reffftview: Dict[int, DisplayReffftviewItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayReffftviewItem(device, f"{self._cmd_syntax}:REFFFTView{x}")
        )
        self._select = DisplaySelect(device, f"{self._cmd_syntax}:SELect")
        self._varpersist = DisplayVarpersist(device, f"{self._cmd_syntax}:VARpersist")
        self._waveview = DisplayWaveview(device, f"{self._cmd_syntax}:WAVEView")
        self._waveview1 = DisplayWaveview1(device, f"{self._cmd_syntax}:WAVEView1")
        self._waveform = DisplayWaveform(device, f"{self._cmd_syntax}:WAVEform")
        self._ch: Dict[int, DisplayChannel] = DefaultDictPassKeyToFactory(
            lambda x: DisplayChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._math: Dict[int, DisplayMathItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayMathItem(device, f"{self._cmd_syntax}:Math{x}")
        )
        self._ref: Dict[int, DisplayRefItem] = DefaultDictPassKeyToFactory(
            lambda x: DisplayRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def colors(self) -> DisplayColors:
        """Return the ``DISplay:COLors`` command.

        Description:
            - Sets or queries the color mode for the graticule and waveform display.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLors?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:COLors?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:COLors value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLors {NORMal|INVERTed}
            - DISplay:COLors?
            ```

        Info:
            - ``NORMal`` specifies normal color mode.
            - ``INVERTed`` specifies inverted color mode.
        """
        return self._colors

    @property
    def global_(self) -> DisplayGlobal:
        """Return the ``DISplay:GLObal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLObal?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLObal?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.b``: The ``DISplay:GLObal:B<x>`` command tree.
            - ``.ch``: The ``DISplay:GLObal:CH<x>`` command tree.
            - ``.dch``: The ``DISplay:GLObal:DCH<x>`` command tree.
            - ``.math``: The ``DISplay:GLObal:MATH<x>`` command tree.
            - ``.ref``: The ``DISplay:GLObal:REF<x>`` command tree.
        """
        return self._global

    @property
    def intensity(self) -> DisplayIntensity:
        """Return the ``DISplay:INTENSITy`` command.

        Description:
            - This query-only command returns the waveform saturation level and screen saver
              settings.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy?
            ```

        Sub-properties:
            - ``.backlight``: The ``DISplay:INTENSITy:BACKLight`` command.
        """
        return self._intensity

    @property
    def mathfftview1(self) -> DisplayMathfftview1:
        """Return the ``DISplay:MATHFFTView1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:MATHFFTView1?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:MATHFFTView1?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autoscale``: The ``DISplay:MATHFFTView1:AUTOScale`` command.
            - ``.cursor``: The ``DISplay:MATHFFTView1:CURSor`` command tree.
            - ``.gridlines``: The ``DISplay:MATHFFTView1:GRIDlines`` command.
            - ``.math``: The ``DISplay:MATHFFTView1:MATH`` command tree.
            - ``.xaxis``: The ``DISplay:MATHFFTView1:XAXIS`` command tree.
            - ``.yaxis``: The ``DISplay:MATHFFTView1:YAXIS`` command tree.
            - ``.zoom``: The ``DISplay:MATHFFTView1:ZOOM`` command tree.
        """
        return self._mathfftview1

    @property
    def persistence(self) -> DisplayPersistence:
        """Return the ``DISplay:PERSistence`` command.

        Description:
            - This command sets or queries the display persistence for analog waveforms. Persistence
              is valid for wave views only.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PERSistence?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PERSistence?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:PERSistence value``
              command.

        SCPI Syntax:
            ```
            - DISplay:PERSistence {OFF|AUTO|INFPersist|INFInite|VARpersist|CLEAR}
            - DISplay:PERSistence?
            ```

        Info:
            - ``OFF`` disables the persistence aspect of the display.
            - ``AUTO`` automatically set the persistence.
            - ``INFPersist`` sets a display mode where any pixels, once touched by samples, remain
              set until cleared by a mode change.
            - ``INFInite`` sets a display mode where any pixels, once touched by samples, remain set
              until cleared by a mode change.
            - ``VARPersist`` sets a display mode where set pixels are gradually dimmed.
            - ``CLEAR`` resets the persist time count down and clears the display of acquired
              points.

        Sub-properties:
            - ``.reset``: The ``DISplay:PERSistence:RESET`` command.
        """
        return self._persistence

    @property
    def plotview1(self) -> DisplayPlotview1:
        """Return the ``DISplay:PLOTView1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PLOTView1?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PLOTView1?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autoscale``: The ``DISplay:PLOTView1:AUTOScale`` command.
            - ``.cursor``: The ``DISplay:PLOTView1:CURSor`` command tree.
            - ``.gridlines``: The ``DISplay:PLOTView1:GRIDlines`` command.
            - ``.xaxis``: The ``DISplay:PLOTView1:XAXIS`` command tree.
            - ``.yaxis``: The ``DISplay:PLOTView1:YAXIS`` command tree.
            - ``.zoom``: The ``DISplay:PLOTView1:ZOOM`` command tree.
        """
        return self._plotview1

    @property
    def reffftview(self) -> Dict[int, DisplayReffftviewItem]:
        """Return the ``DISplay:REFFFTView<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REFFFTView<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:REFFFTView<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``REFFFTView<x>`` is the plot number.

        Sub-properties:
            - ``.autoscale``: The ``DISplay:REFFFTView<x>:AUTOScale`` command.
            - ``.cursor``: The ``DISplay:REFFFTView<x>:CURSor`` command tree.
            - ``.gridlines``: The ``DISplay:REFFFTView<x>:GRIDlines`` command.
            - ``.ref``: The ``DISplay:REFFFTView<x>:REF`` command tree.
            - ``.xaxis``: The ``DISplay:REFFFTView<x>:XAXIS`` command tree.
            - ``.zoom``: The ``DISplay:REFFFTView<x>:ZOOM`` command tree.
        """
        return self._reffftview

    @property
    def select(self) -> DisplaySelect:
        """Return the ``DISplay:SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:SELect?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bus``: The ``DISplay:SELect:BUS`` command.
            - ``.math``: The ``DISplay:SELect:MATH`` command.
            - ``.reference``: The ``DISplay:SELect:REFerence`` command.
            - ``.source``: The ``DISplay:SELect:SOUrce`` command.
            - ``.view``: The ``DISplay:SELect:VIEW`` command.
            - ``.waveview1``: The ``DISplay:SELect:WAVEView1`` command tree.
        """
        return self._select

    @property
    def varpersist(self) -> DisplayVarpersist:
        """Return the ``DISplay:VARpersist`` command.

        Description:
            - This command sets or queries display persistence decay time, which is the approximate
              decay time for a freshly struck persistence sample.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:VARpersist?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:VARpersist?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:VARpersist value`` command.

        SCPI Syntax:
            ```
            - DISplay:VARpersist <NR3>
            - DISplay:VARpersist?
            ```

        Info:
            - ``<NR3>`` indicates the persistence decay time and ranges from 0.5 to 100.
        """
        return self._varpersist

    @property
    def waveview(self) -> DisplayWaveview:
        """Return the ``DISplay:WAVEView`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.cursor``: The ``DISplay:WAVEView:CURSor`` command tree.
            - ``.gridtype``: The ``DISplay:WAVEView:GRIDTYPE`` command.
        """
        return self._waveview

    @property
    def waveview1(self) -> DisplayWaveview1:
        """Return the ``DISplay:WAVEView1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEView1?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEView1?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bus``: The ``DISplay:WAVEView1:BUS`` command tree.
            - ``.ch``: The ``DISplay:WAVEView1:CH<x>`` command tree.
            - ``.cursor``: The ``DISplay:WAVEView1:CURSor`` command.
            - ``.dch``: The ``DISplay:WAVEView1:DCH<x>`` command tree.
            - ``.filter``: The ``DISplay:WAVEView1:FILTer`` command.
            - ``.graticule``: The ``DISplay:WAVEView1:GRAticule`` command.
            - ``.intensity``: The ``DISplay:WAVEView1:INTENSITy`` command tree.
            - ``.math``: The ``DISplay:WAVEView1:MATH`` command tree.
            - ``.ref``: The ``DISplay:WAVEView1:REF`` command tree.
            - ``.style``: The ``DISplay:WAVEView1:STYle`` command.
            - ``.viewstyle``: The ``DISplay:WAVEView1:VIEWStyle`` command.
            - ``.zoom``: The ``DISplay:WAVEView1:ZOOM`` command.
            - ``.refx``: The ``DISplay:WAVEView1:REF<x>`` command tree.
        """
        return self._waveview1

    @property
    def waveform(self) -> DisplayWaveform:
        """Return the ``DISplay:WAVEform`` command.

        Description:
            - This command globally enables or disables the waveform display. When disabled, the
              waveform is still acquired and held in memory, but it is not drawn to the screen.
              Disabling the waveform display may improve processing speed.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:WAVEform?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:WAVEform value`` command.

        SCPI Syntax:
            ```
            - DISplay:WAVEform {ON|OFF|<NR1>}
            - DISplay:WAVEform?
            ```

        Info:
            - ``<NR1>`` enables or disables the waveform display. 0 disables the waveform display;
              any other value enables the waveform display.
            - ``ON`` enables the waveform display.
            - ``OFF`` disables the waveform display.
        """
        return self._waveform

    @property
    def ch(self) -> Dict[int, DisplayChannel]:
        """Return the ``DISplay:CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:CH<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` specifies the input channel for which you want to change the waveform color,
              where <x> is the channel number.

        Sub-properties:
            - ``.invertcolor``: The ``DISplay:CH<x>:INVERTColor`` command.
            - ``.normalcolor``: The ``DISplay:CH<x>:NORMALColor`` command.
        """
        return self._ch

    @property
    def math(self) -> Dict[int, DisplayMathItem]:
        """Return the ``DISplay:Math<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:Math<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:Math<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.invertcolor``: The ``DISplay:Math<x>:INVERTColor`` command.
            - ``.normalcolor``: The ``DISplay:Math<x>:NORMALColor`` command.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, DisplayRefItem]:
        """Return the ``DISplay:REF<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:REF<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``REF<x>`` specifies the reference waveform for which you want to change the waveform
              color, where <x> is the reference waveform number.

        Sub-properties:
            - ``.invertcolor``: The ``DISplay:REF<x>:INVERTColor`` command.
            - ``.normalcolor``: The ``DISplay:REF<x>:NORMALColor`` command.
        """
        return self._ref
