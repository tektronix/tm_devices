"""The power commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - POWer:CURRENTSOurce {CH<x>|REF<x>}
    - POWer:CURRENTSOurce?
    - POWer:DISplay {OFF|ON|0|1}
    - POWer:DISplay?
    - POWer:GATESOurce {CH<x>|REF<x>|NONe}
    - POWer:GATESOurce?
    - POWer:GATing {OFF|SCREen|CURSor}
    - POWer:GATing?
    - POWer:HARMonics:DISplay:SELect {ODD|EVEN|ALL}
    - POWer:HARMonics:DISplay:SELect?
    - POWer:HARMonics:DISplay:TYPe {GRAph|TABle}
    - POWer:HARMonics:DISplay:TYPe?
    - POWer:HARMonics:FREQRef {VOLTage|CURRent|HARMSOURce|FIXEDFREQuency}
    - POWer:HARMonics:FREQRef:FIXEDFREQValue <NR3>
    - POWer:HARMonics:FREQRef:FIXEDFREQValue?
    - POWer:HARMonics:FREQRef?
    - POWer:HARMonics:IEC:CLAss {A|B|C<x>|D}
    - POWer:HARMonics:IEC:CLAss?
    - POWer:HARMonics:IEC:FILter {OFF|ON|0|1}
    - POWer:HARMonics:IEC:FILter?
    - POWer:HARMonics:IEC:FUNDamental <NR3>
    - POWer:HARMonics:IEC:FUNDamental?
    - POWer:HARMonics:IEC:GROUPing {OFF|ON|1|0}
    - POWer:HARMonics:IEC:GROUPing?
    - POWer:HARMonics:IEC:INPUTPOWer <NR3>
    - POWer:HARMonics:IEC:INPUTPOWer?
    - POWer:HARMonics:IEC:LINEFREQuency <NR1>
    - POWer:HARMonics:IEC:LINEFREQuency?
    - POWer:HARMonics:IEC:OBSPERiod <NR3>
    - POWer:HARMonics:IEC:OBSPERiod?
    - POWer:HARMonics:IEC:POWERFACtor <NR3>
    - POWer:HARMonics:IEC:POWERFACtor?
    - POWer:HARMonics:MIL:FUNDamental:CALCmethod {MEAS|USER}
    - POWer:HARMonics:MIL:FUNDamental:CALCmethod?
    - POWer:HARMonics:MIL:FUNDamental:USER:CURrent <NR3>
    - POWer:HARMonics:MIL:FUNDamental:USER:CURrent?
    - POWer:HARMonics:MIL:LINEFREQuency <NR1>
    - POWer:HARMonics:MIL:LINEFREQuency?
    - POWer:HARMonics:MIL:POWERLEVel {LOW|HIGH}
    - POWer:HARMonics:MIL:POWERLEVel?
    - POWer:HARMonics:NR_HARMonics <NR3>
    - POWer:HARMonics:NR_HARMonics?
    - POWer:HARMonics:RESults:HAR<x>:FREQuency?
    - POWer:HARMonics:RESults:HAR<x>:IECMAX?
    - POWer:HARMonics:RESults:HAR<x>:LIMit?
    - POWer:HARMonics:RESults:HAR<x>:PHASe?
    - POWer:HARMonics:RESults:HAR<x>:RMS:ABSolute?
    - POWer:HARMonics:RESults:HAR<x>:RMS:PERCent?
    - POWer:HARMonics:RESults:HAR<x>:TEST:IEC:CLASSALIMit?
    - POWer:HARMonics:RESults:HAR<x>:TEST:IEC:NORMAL?
    - POWer:HARMonics:RESults:HAR<x>:TEST:IEC:POHCLIMit?
    - POWer:HARMonics:RESults:HAR<x>:TEST:MIL:NORMAL?
    - POWer:HARMonics:RESults:IEC:FUNDamental?
    - POWer:HARMonics:RESults:IEC:HARM3ALTernate?
    - POWer:HARMonics:RESults:IEC:HARM5ALTernate?
    - POWer:HARMonics:RESults:IEC:POHC?
    - POWer:HARMonics:RESults:IEC:POHL?
    - POWer:HARMonics:RESults:IEC:POWERFactor?
    - POWer:HARMonics:RESults:IEC:POWer?
    - POWer:HARMonics:RESults:PASSFail?
    - POWer:HARMonics:RESults:RMS?
    - POWer:HARMonics:RESults:SAVe <String>
    - POWer:HARMonics:RESults:THDF?
    - POWer:HARMonics:RESults:THDR?
    - POWer:HARMonics:SOURce {VOLTage|CURRent}
    - POWer:HARMonics:SOURce?
    - POWer:HARMonics:STANDard {NONe|IEC|MIL}
    - POWer:HARMonics:STANDard?
    - POWer:INDICators {OFF|ON|0|1}
    - POWer:INDICators?
    - POWer:MODulation:SOUrce {VOLTage|CURRent}
    - POWer:MODulation:SOUrce?
    - POWer:MODulation:TYPe {PWIdth|NWIdth|PERIod|PDUty|NDUty|FREQuency}
    - POWer:MODulation:TYPe?
    - POWer:QUALity:APPpwr?
    - POWer:QUALity:DISplay:APPpwr {OFF|ON|0|1}
    - POWer:QUALity:DISplay:APPpwr?
    - POWer:QUALity:DISplay:FREQuency {OFF|ON|0|1}
    - POWer:QUALity:DISplay:FREQuency?
    - POWer:QUALity:DISplay:ICRESTfactor {OFF|ON|0|1}
    - POWer:QUALity:DISplay:ICRESTfactor?
    - POWer:QUALity:DISplay:IRMS {OFF|ON|0|1}
    - POWer:QUALity:DISplay:IRMS?
    - POWer:QUALity:DISplay:PHASEangle {OFF|ON|0|1}
    - POWer:QUALity:DISplay:PHASEangle?
    - POWer:QUALity:DISplay:POWERFACtor {OFF|ON|0|1}
    - POWer:QUALity:DISplay:POWERFACtor?
    - POWer:QUALity:DISplay:REACTpwr {OFF|ON|0|1}
    - POWer:QUALity:DISplay:REACTpwr?
    - POWer:QUALity:DISplay:TRUEpwr {OFF|ON|0|1}
    - POWer:QUALity:DISplay:TRUEpwr?
    - POWer:QUALity:DISplay:VCRESTfactor {OFF|ON|0|1}
    - POWer:QUALity:DISplay:VCRESTfactor?
    - POWer:QUALity:DISplay:VRMS {OFF|ON|0|1}
    - POWer:QUALity:DISplay:VRMS?
    - POWer:QUALity:FREQREFerence {VOLTage|CURRent}
    - POWer:QUALity:FREQREFerence?
    - POWer:QUALity:FREQuency?
    - POWer:QUALity:ICRESTfactor?
    - POWer:QUALity:IRMS?
    - POWer:QUALity:PHASEangle?
    - POWer:QUALity:POWERFACtor?
    - POWer:QUALity:REACTpwr?
    - POWer:QUALity:TRUEpwr?
    - POWer:QUALity:VCRESTfactor?
    - POWer:QUALity:VRMS?
    - POWer:REFLevel:ABSolute {SETTODEFaults}
    - POWer:REFLevel:ABSolute:HIGH <NR3>; Ranges={D,-1e6,+1E6}
    - POWer:REFLevel:ABSolute:HIGH?
    - POWer:REFLevel:ABSolute:LOW <NR3>; Ranges={D,-1e6,+1E6}
    - POWer:REFLevel:ABSolute:LOW?
    - POWer:REFLevel:ABSolute:MID<x> <NR3>; Ranges={D,-1e6,+1E6}
    - POWer:REFLevel:ABSolute:MID<x>?
    - POWer:REFLevel:HYSTeresis <NR3>
    - POWer:REFLevel:HYSTeresis?
    - POWer:REFLevel:METHod {ABSolute|PERCent}
    - POWer:REFLevel:METHod?
    - POWer:REFLevel:PERCent <SETTODEFaults>
    - POWer:REFLevel:PERCent:HIGH <NR3>; Ranges={D,0.0,100.0}
    - POWer:REFLevel:PERCent:HIGH?
    - POWer:REFLevel:PERCent:LOW <NR3>; Ranges={D,0.0,100.0}
    - POWer:REFLevel:PERCent:LOW?
    - POWer:REFLevel:PERCent:MID<x> <NR3>; Ranges={D,0.0,100.0}
    - POWer:REFLevel:PERCent:MID<x>?
    - POWer:RIPPle {VERTAUTOset|VERTDEFault}
    - POWer:RIPPle:RESults:AMPLitude?
    - POWer:RIPPle:RESults:MAX?
    - POWer:RIPPle:RESults:MEAN?
    - POWer:RIPPle:RESults:MIN?
    - POWer:RIPPle:RESults:STDdev?
    - POWer:RIPPle:SOUrce {VOLTage|CURRent}
    - POWer:SOA:LINear:XMAX <NR3>
    - POWer:SOA:LINear:XMAX?
    - POWer:SOA:LINear:XMIN <NR3>
    - POWer:SOA:LINear:XMIN?
    - POWer:SOA:LINear:YMAX <NR3>
    - POWer:SOA:LINear:YMAX?
    - POWer:SOA:LINear:YMIN <NR3>
    - POWer:SOA:LINear:YMIN?
    - POWer:SOA:LOG:XMAX <NR3>
    - POWer:SOA:LOG:XMAX?
    - POWer:SOA:LOG:XMIN <NR3>
    - POWer:SOA:LOG:XMIN?
    - POWer:SOA:LOG:YMAX <NR3>
    - POWer:SOA:LOG:YMAX?
    - POWer:SOA:LOG:YMIN <NR3>
    - POWer:SOA:LOG:YMIN?
    - POWer:SOA:MASK:DEFine <NR3>
    - POWer:SOA:MASK:DEFine?
    - POWer:SOA:MASK:MAXAmps <NR3>
    - POWer:SOA:MASK:MAXAmps?
    - POWer:SOA:MASK:MAXVolts <NR3>
    - POWer:SOA:MASK:MAXVolts?
    - POWer:SOA:MASK:MAXWatts <NR3>
    - POWer:SOA:MASK:MAXWatts?
    - POWer:SOA:MASK:NR_Pt?
    - POWer:SOA:MASK:STATE {OFF|LIMITS|POINTS}
    - POWer:SOA:MASK:STATE?
    - POWer:SOA:MASK:STOPOnviol {OFF|ON|0|1}
    - POWer:SOA:MASK:STOPOnviol?
    - POWer:SOA:PLOTTYPe {LOG|LINear}
    - POWer:SOA:PLOTTYPe?
    - POWer:SOA:RESult:FAILures:QTY?
    - POWer:SOA:RESult:NUMACq?
    - POWer:SOA:RESult:STATE?
    - POWer:STATIstics {RESET}
    - POWer:STATIstics:MODe {OFF|ALL}
    - POWer:STATIstics:MODe?
    - POWer:STATIstics:WEIghting <NR1>;Ranges {L,2,1000}
    - POWer:STATIstics:WEIghting?
    - POWer:SWLoss:CONDCALCmethod {VOLTage|RDSon|VCEsat}
    - POWer:SWLoss:CONDCALCmethod?
    - POWer:SWLoss:CONDuction:ENERGY:MAX?
    - POWer:SWLoss:CONDuction:ENERGY:MEAN?
    - POWer:SWLoss:CONDuction:ENERGY:MIN?
    - POWer:SWLoss:CONDuction:POWer:MAX?
    - POWer:SWLoss:CONDuction:POWer:MEAN?
    - POWer:SWLoss:CONDuction:POWer:MIN?
    - POWer:SWLoss:DISplay {ALL|ENERGYLoss|POWERLoss}
    - POWer:SWLoss:DISplay?
    - POWer:SWLoss:GATe:POLarity {FALL|RISe}
    - POWer:SWLoss:GATe:POLarity?
    - POWer:SWLoss:GATe:TURNON <NR3>
    - POWer:SWLoss:GATe:TURNON?
    - POWer:SWLoss:NUMCYCles? <NR3>
    - POWer:SWLoss:RDSon <NR3>
    - POWer:SWLoss:RDSon?
    - POWer:SWLoss:REFLevel:ABSolute:GATEMid <NR3>
    - POWer:SWLoss:REFLevel:ABSolute:GATEMid?
    - POWer:SWLoss:REFLevel:ABSolute:LOWCurrent <NR3>
    - POWer:SWLoss:REFLevel:ABSolute:LOWCurrent?
    - POWer:SWLoss:REFLevel:ABSolute:LOWVoltage <NR3>
    - POWer:SWLoss:REFLevel:ABSolute:LOWVoltage?
    - POWer:SWLoss:REFLevel:PERCent:GATEMid <NR3>
    - POWer:SWLoss:REFLevel:PERCent:GATEMid?
    - POWer:SWLoss:REFLevel:PERCent:LOWCurrent <NR3>
    - POWer:SWLoss:REFLevel:PERCent:LOWCurrent?
    - POWer:SWLoss:REFLevel:PERCent:LOWVoltage <NR3>
    - POWer:SWLoss:REFLevel:PERCent:LOWVoltage?
    - POWer:SWLoss:TOFF:ENERGY:MAX?
    - POWer:SWLoss:TOFF:ENERGY:MEAN?
    - POWer:SWLoss:TOFF:ENERGY:MIN?
    - POWer:SWLoss:TOFF:POWer:MAX?
    - POWer:SWLoss:TOFF:POWer:MEAN?
    - POWer:SWLoss:TOFF:POWer:MIN?
    - POWer:SWLoss:TON:ENERGY:MAX?
    - POWer:SWLoss:TON:ENERGY:MEAN?
    - POWer:SWLoss:TON:ENERGY:MIN?
    - POWer:SWLoss:TON:POWer:MAX?
    - POWer:SWLoss:TON:POWer:MEAN?
    - POWer:SWLoss:TON:POWer:MIN?
    - POWer:SWLoss:TOTal:ENERGY:MAX?
    - POWer:SWLoss:TOTal:ENERGY:MEAN?
    - POWer:SWLoss:TOTal:ENERGY:MIN?
    - POWer:SWLoss:TOTal:POWer:MAX?
    - POWer:SWLoss:TOTal:POWer:MEAN?
    - POWer:SWLoss:TOTal:POWer:MIN?
    - POWer:SWLoss:VCEsat <NR3>
    - POWer:SWLoss:VCEsat?
    - POWer:TYPe {NONe|QUALity|SWITCHingloss|SOA|HARMonics|RIPPle|MODULationanalysis|DESKew}
    - POWer:TYPe?
    - POWer:VOLTAGESOurce {CH<x>|REF<x>}
    - POWer:VOLTAGESOurce?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdReadWithArguments,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class PowerVoltagesource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:VOLTAGESOurce`` command.

    Description:
        - This command specifies the voltage source for the power application.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:VOLTAGESOurce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:VOLTAGESOurce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:VOLTAGESOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:VOLTAGESOurce {CH<x>|REF<x>}
        - POWer:VOLTAGESOurce?
        ```

    Info:
        - ``CH<x>`` sets the analog channel as the voltage source.
        - ``REF<x>`` sets the reference waveform as the voltage source.
    """


class PowerType(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:TYPe`` command.

    Description:
        - This command specifies the power application measurement type.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:TYPe value`` command.

    SCPI Syntax:
        ```
        - POWer:TYPe {NONe|QUALity|SWITCHingloss|SOA|HARMonics|RIPPle|MODULationanalysis|DESKew}
        - POWer:TYPe?
        ```

    Info:
        - ``NONe`` Use to set the measurement type to None.
        - ``QUALity`` Use the power quality functions to obtain measurements and statistics about
          the general power quality in your test circuit.
        - ``SWITCHingloss`` Use the switching loss functions to obtain the power loss and energy
          loss across the acquired waveform, including turn-on loss, turn-off loss, conduction loss,
          and total loss. Typically, use these functions to characterize losses in power supply
          switching devices, as they switch on and off.
        - ``SOA`` Use the safe operating functions to obtain an X-Y display of the switching
          device-under-test's voltage and current. Also use them to perform a mask test of the X-Y
          signal relative to the graphical X-Y description of the device specification table. The
          safe operating area is typically the voltage and current values that a semiconductor can
          operate without damaging itself.
        - ``HARMonics`` Use the harmonics functions to obtain the frequency spectrum of the source
          waveform and associated measurement values. Harmonic measurements can help one perform
          in-depth troubleshooting of power quality problems.
        - ``RIPPle`` Use the ripple functions to obtain measurements and statistics for the AC
          components of the acquired waveform. Ripples are often found on top of a large DC signal.
        - ``MODULationanalysis`` Use the modulation functions to obtain a trend plot of a
          measurement value across the acquired waveform. This is useful for showing the variations
          in the modulated switching signal.
        - ``DESKew`` Run the deskew procedure to match the delays through the probes. Different
          probes introduce different delays between the probe tip and the oscilloscope. Many
          oscilloscope users do not have to worry about this because they use the same type of probe
          on all channels. Power measurement users, however, frequently use both a voltage probe and
          a current probe. A current probe typically has a larger delay than a voltage probe, so
          setting deskew values becomes important.
    """


class PowerSwlossVcesat(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:VCEsat`` command.

    Description:
        - This command specifies VCESAT value for use in switching loss calculations when the
          conduction calculation method is VCESAT.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:VCEsat?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:VCEsat?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SWLoss:VCEsat value`` command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:VCEsat <NR3>
        - POWer:SWLoss:VCEsat?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the VCEsat switching loss calculation.
    """


class PowerSwlossTotalPowerMin(SCPICmdRead):
    """The ``POWer:SWLoss:TOTal:POWer:MIN`` command.

    Description:
        - Returns the minimum total power loss.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:POWer:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:POWer:MIN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOTal:POWer:MIN?
        ```
    """


class PowerSwlossTotalPowerMean(SCPICmdRead):
    """The ``POWer:SWLoss:TOTal:POWer:MEAN`` command.

    Description:
        - Returns the mean total power loss.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:POWer:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:POWer:MEAN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOTal:POWer:MEAN?
        ```
    """


class PowerSwlossTotalPowerMax(SCPICmdRead):
    """The ``POWer:SWLoss:TOTal:POWer:MAX`` command.

    Description:
        - Returns the maximum total power loss.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:POWer:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:POWer:MAX?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOTal:POWer:MAX?
        ```
    """


class PowerSwlossTotalPower(SCPICmdRead):
    """The ``POWer:SWLoss:TOTal:POWer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:POWer?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``POWer:SWLoss:TOTal:POWer:MAX`` command.
        - ``.mean``: The ``POWer:SWLoss:TOTal:POWer:MEAN`` command.
        - ``.min``: The ``POWer:SWLoss:TOTal:POWer:MIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = PowerSwlossTotalPowerMax(device, f"{self._cmd_syntax}:MAX")
        self._mean = PowerSwlossTotalPowerMean(device, f"{self._cmd_syntax}:MEAN")
        self._min = PowerSwlossTotalPowerMin(device, f"{self._cmd_syntax}:MIN")

    @property
    def max(self) -> PowerSwlossTotalPowerMax:
        """Return the ``POWer:SWLoss:TOTal:POWer:MAX`` command.

        Description:
            - Returns the maximum total power loss.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:POWer:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:POWer:MAX?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOTal:POWer:MAX?
            ```
        """
        return self._max

    @property
    def mean(self) -> PowerSwlossTotalPowerMean:
        """Return the ``POWer:SWLoss:TOTal:POWer:MEAN`` command.

        Description:
            - Returns the mean total power loss.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:POWer:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:POWer:MEAN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOTal:POWer:MEAN?
            ```
        """
        return self._mean

    @property
    def min(self) -> PowerSwlossTotalPowerMin:
        """Return the ``POWer:SWLoss:TOTal:POWer:MIN`` command.

        Description:
            - Returns the minimum total power loss.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:POWer:MIN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:POWer:MIN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOTal:POWer:MIN?
            ```
        """
        return self._min


class PowerSwlossTotalEnergyMin(SCPICmdRead):
    """The ``POWer:SWLoss:TOTal:ENERGY:MIN`` command.

    Description:
        - Returns the minimum total energy for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MIN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOTal:ENERGY:MIN?
        ```
    """


class PowerSwlossTotalEnergyMean(SCPICmdRead):
    """The ``POWer:SWLoss:TOTal:ENERGY:MEAN`` command.

    Description:
        - Returns the mean total energy for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MEAN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOTal:ENERGY:MEAN?
        ```
    """


class PowerSwlossTotalEnergyMax(SCPICmdRead):
    """The ``POWer:SWLoss:TOTal:ENERGY:MAX`` command.

    Description:
        - Returns the maximum total energy for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MAX?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOTal:ENERGY:MAX?
        ```
    """


class PowerSwlossTotalEnergy(SCPICmdRead):
    """The ``POWer:SWLoss:TOTal:ENERGY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:ENERGY?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:ENERGY?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``POWer:SWLoss:TOTal:ENERGY:MAX`` command.
        - ``.mean``: The ``POWer:SWLoss:TOTal:ENERGY:MEAN`` command.
        - ``.min``: The ``POWer:SWLoss:TOTal:ENERGY:MIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = PowerSwlossTotalEnergyMax(device, f"{self._cmd_syntax}:MAX")
        self._mean = PowerSwlossTotalEnergyMean(device, f"{self._cmd_syntax}:MEAN")
        self._min = PowerSwlossTotalEnergyMin(device, f"{self._cmd_syntax}:MIN")

    @property
    def max(self) -> PowerSwlossTotalEnergyMax:
        """Return the ``POWer:SWLoss:TOTal:ENERGY:MAX`` command.

        Description:
            - Returns the maximum total energy for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MAX?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOTal:ENERGY:MAX?
            ```
        """
        return self._max

    @property
    def mean(self) -> PowerSwlossTotalEnergyMean:
        """Return the ``POWer:SWLoss:TOTal:ENERGY:MEAN`` command.

        Description:
            - Returns the mean total energy for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MEAN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOTal:ENERGY:MEAN?
            ```
        """
        return self._mean

    @property
    def min(self) -> PowerSwlossTotalEnergyMin:
        """Return the ``POWer:SWLoss:TOTal:ENERGY:MIN`` command.

        Description:
            - Returns the minimum total energy for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MIN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:ENERGY:MIN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOTal:ENERGY:MIN?
            ```
        """
        return self._min


class PowerSwlossTotal(SCPICmdRead):
    """The ``POWer:SWLoss:TOTal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.energy``: The ``POWer:SWLoss:TOTal:ENERGY`` command tree.
        - ``.power``: The ``POWer:SWLoss:TOTal:POWer`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._energy = PowerSwlossTotalEnergy(device, f"{self._cmd_syntax}:ENERGY")
        self._power = PowerSwlossTotalPower(device, f"{self._cmd_syntax}:POWer")

    @property
    def energy(self) -> PowerSwlossTotalEnergy:
        """Return the ``POWer:SWLoss:TOTal:ENERGY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:ENERGY?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:ENERGY?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``POWer:SWLoss:TOTal:ENERGY:MAX`` command.
            - ``.mean``: The ``POWer:SWLoss:TOTal:ENERGY:MEAN`` command.
            - ``.min``: The ``POWer:SWLoss:TOTal:ENERGY:MIN`` command.
        """
        return self._energy

    @property
    def power(self) -> PowerSwlossTotalPower:
        """Return the ``POWer:SWLoss:TOTal:POWer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal:POWer?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal:POWer?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``POWer:SWLoss:TOTal:POWer:MAX`` command.
            - ``.mean``: The ``POWer:SWLoss:TOTal:POWer:MEAN`` command.
            - ``.min``: The ``POWer:SWLoss:TOTal:POWer:MIN`` command.
        """
        return self._power


class PowerSwlossTonPowerMin(SCPICmdRead):
    """The ``POWer:SWLoss:TON:POWer:MIN`` command.

    Description:
        - Returns the minimum Ton power for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:POWer:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:POWer:MIN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TON:POWer:MIN?
        ```
    """


class PowerSwlossTonPowerMean(SCPICmdRead):
    """The ``POWer:SWLoss:TON:POWer:MEAN`` command.

    Description:
        - Returns the mean Ton power for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:POWer:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:POWer:MEAN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TON:POWer:MEAN?
        ```
    """


class PowerSwlossTonPowerMax(SCPICmdRead):
    """The ``POWer:SWLoss:TON:POWer:MAX`` command.

    Description:
        - Returns the maximum Ton power for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:POWer:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:POWer:MAX?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TON:POWer:MAX?
        ```
    """


class PowerSwlossTonPower(SCPICmdRead):
    """The ``POWer:SWLoss:TON:POWer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:POWer?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``POWer:SWLoss:TON:POWer:MAX`` command.
        - ``.mean``: The ``POWer:SWLoss:TON:POWer:MEAN`` command.
        - ``.min``: The ``POWer:SWLoss:TON:POWer:MIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = PowerSwlossTonPowerMax(device, f"{self._cmd_syntax}:MAX")
        self._mean = PowerSwlossTonPowerMean(device, f"{self._cmd_syntax}:MEAN")
        self._min = PowerSwlossTonPowerMin(device, f"{self._cmd_syntax}:MIN")

    @property
    def max(self) -> PowerSwlossTonPowerMax:
        """Return the ``POWer:SWLoss:TON:POWer:MAX`` command.

        Description:
            - Returns the maximum Ton power for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:POWer:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:POWer:MAX?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TON:POWer:MAX?
            ```
        """
        return self._max

    @property
    def mean(self) -> PowerSwlossTonPowerMean:
        """Return the ``POWer:SWLoss:TON:POWer:MEAN`` command.

        Description:
            - Returns the mean Ton power for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:POWer:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:POWer:MEAN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TON:POWer:MEAN?
            ```
        """
        return self._mean

    @property
    def min(self) -> PowerSwlossTonPowerMin:
        """Return the ``POWer:SWLoss:TON:POWer:MIN`` command.

        Description:
            - Returns the minimum Ton power for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:POWer:MIN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:POWer:MIN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TON:POWer:MIN?
            ```
        """
        return self._min


class PowerSwlossTonEnergyMin(SCPICmdRead):
    """The ``POWer:SWLoss:TON:ENERGY:MIN`` command.

    Description:
        - Returns the minimum Ton energy for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:ENERGY:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:ENERGY:MIN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TON:ENERGY:MIN?
        ```
    """


class PowerSwlossTonEnergyMean(SCPICmdRead):
    """The ``POWer:SWLoss:TON:ENERGY:MEAN`` command.

    Description:
        - Returns the mean Ton energy for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:ENERGY:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:ENERGY:MEAN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TON:ENERGY:MEAN?
        ```
    """


class PowerSwlossTonEnergyMax(SCPICmdRead):
    """The ``POWer:SWLoss:TON:ENERGY:MAX`` command.

    Description:
        - Returns the maximum Ton energy for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:ENERGY:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:ENERGY:MAX?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TON:ENERGY:MAX?
        ```
    """


class PowerSwlossTonEnergy(SCPICmdRead):
    """The ``POWer:SWLoss:TON:ENERGY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:ENERGY?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:ENERGY?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``POWer:SWLoss:TON:ENERGY:MAX`` command.
        - ``.mean``: The ``POWer:SWLoss:TON:ENERGY:MEAN`` command.
        - ``.min``: The ``POWer:SWLoss:TON:ENERGY:MIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = PowerSwlossTonEnergyMax(device, f"{self._cmd_syntax}:MAX")
        self._mean = PowerSwlossTonEnergyMean(device, f"{self._cmd_syntax}:MEAN")
        self._min = PowerSwlossTonEnergyMin(device, f"{self._cmd_syntax}:MIN")

    @property
    def max(self) -> PowerSwlossTonEnergyMax:
        """Return the ``POWer:SWLoss:TON:ENERGY:MAX`` command.

        Description:
            - Returns the maximum Ton energy for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:ENERGY:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:ENERGY:MAX?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TON:ENERGY:MAX?
            ```
        """
        return self._max

    @property
    def mean(self) -> PowerSwlossTonEnergyMean:
        """Return the ``POWer:SWLoss:TON:ENERGY:MEAN`` command.

        Description:
            - Returns the mean Ton energy for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:ENERGY:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:ENERGY:MEAN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TON:ENERGY:MEAN?
            ```
        """
        return self._mean

    @property
    def min(self) -> PowerSwlossTonEnergyMin:
        """Return the ``POWer:SWLoss:TON:ENERGY:MIN`` command.

        Description:
            - Returns the minimum Ton energy for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:ENERGY:MIN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:ENERGY:MIN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TON:ENERGY:MIN?
            ```
        """
        return self._min


class PowerSwlossTon(SCPICmdRead):
    """The ``POWer:SWLoss:TON`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TON?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.energy``: The ``POWer:SWLoss:TON:ENERGY`` command tree.
        - ``.power``: The ``POWer:SWLoss:TON:POWer`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._energy = PowerSwlossTonEnergy(device, f"{self._cmd_syntax}:ENERGY")
        self._power = PowerSwlossTonPower(device, f"{self._cmd_syntax}:POWer")

    @property
    def energy(self) -> PowerSwlossTonEnergy:
        """Return the ``POWer:SWLoss:TON:ENERGY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:ENERGY?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:ENERGY?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``POWer:SWLoss:TON:ENERGY:MAX`` command.
            - ``.mean``: The ``POWer:SWLoss:TON:ENERGY:MEAN`` command.
            - ``.min``: The ``POWer:SWLoss:TON:ENERGY:MIN`` command.
        """
        return self._energy

    @property
    def power(self) -> PowerSwlossTonPower:
        """Return the ``POWer:SWLoss:TON:POWer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TON:POWer?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON:POWer?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``POWer:SWLoss:TON:POWer:MAX`` command.
            - ``.mean``: The ``POWer:SWLoss:TON:POWer:MEAN`` command.
            - ``.min``: The ``POWer:SWLoss:TON:POWer:MIN`` command.
        """
        return self._power


class PowerSwlossToffPowerMin(SCPICmdRead):
    """The ``POWer:SWLoss:TOFF:POWer:MIN`` command.

    Description:
        - Returns the minimum Toff power for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:POWer:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:POWer:MIN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOFF:POWer:MIN?
        ```
    """


class PowerSwlossToffPowerMean(SCPICmdRead):
    """The ``POWer:SWLoss:TOFF:POWer:MEAN`` command.

    Description:
        - Returns the mean Toff power for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:POWer:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:POWer:MEAN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOFF:POWer:MEAN?
        ```
    """


class PowerSwlossToffPowerMax(SCPICmdRead):
    """The ``POWer:SWLoss:TOFF:POWer:MAX`` command.

    Description:
        - Returns the maximum Toff power for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:POWer:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:POWer:MAX?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOFF:POWer:MAX?
        ```
    """


class PowerSwlossToffPower(SCPICmdRead):
    """The ``POWer:SWLoss:TOFF:POWer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:POWer?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``POWer:SWLoss:TOFF:POWer:MAX`` command.
        - ``.mean``: The ``POWer:SWLoss:TOFF:POWer:MEAN`` command.
        - ``.min``: The ``POWer:SWLoss:TOFF:POWer:MIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = PowerSwlossToffPowerMax(device, f"{self._cmd_syntax}:MAX")
        self._mean = PowerSwlossToffPowerMean(device, f"{self._cmd_syntax}:MEAN")
        self._min = PowerSwlossToffPowerMin(device, f"{self._cmd_syntax}:MIN")

    @property
    def max(self) -> PowerSwlossToffPowerMax:
        """Return the ``POWer:SWLoss:TOFF:POWer:MAX`` command.

        Description:
            - Returns the maximum Toff power for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:POWer:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:POWer:MAX?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOFF:POWer:MAX?
            ```
        """
        return self._max

    @property
    def mean(self) -> PowerSwlossToffPowerMean:
        """Return the ``POWer:SWLoss:TOFF:POWer:MEAN`` command.

        Description:
            - Returns the mean Toff power for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:POWer:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:POWer:MEAN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOFF:POWer:MEAN?
            ```
        """
        return self._mean

    @property
    def min(self) -> PowerSwlossToffPowerMin:
        """Return the ``POWer:SWLoss:TOFF:POWer:MIN`` command.

        Description:
            - Returns the minimum Toff power for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:POWer:MIN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:POWer:MIN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOFF:POWer:MIN?
            ```
        """
        return self._min


class PowerSwlossToffEnergyMin(SCPICmdRead):
    """The ``POWer:SWLoss:TOFF:ENERGY:MIN`` command.

    Description:
        - Returns the minimum Toff energy for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MIN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOFF:ENERGY:MIN?
        ```
    """


class PowerSwlossToffEnergyMean(SCPICmdRead):
    """The ``POWer:SWLoss:TOFF:ENERGY:MEAN`` command.

    Description:
        - Returns the mean Toff energy for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MEAN?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOFF:ENERGY:MEAN?
        ```
    """


class PowerSwlossToffEnergyMax(SCPICmdRead):
    """The ``POWer:SWLoss:TOFF:ENERGY:MAX`` command.

    Description:
        - Returns the maximum Toff energy for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MAX?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:TOFF:ENERGY:MAX?
        ```
    """


class PowerSwlossToffEnergy(SCPICmdRead):
    """The ``POWer:SWLoss:TOFF:ENERGY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:ENERGY?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:ENERGY?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``POWer:SWLoss:TOFF:ENERGY:MAX`` command.
        - ``.mean``: The ``POWer:SWLoss:TOFF:ENERGY:MEAN`` command.
        - ``.min``: The ``POWer:SWLoss:TOFF:ENERGY:MIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = PowerSwlossToffEnergyMax(device, f"{self._cmd_syntax}:MAX")
        self._mean = PowerSwlossToffEnergyMean(device, f"{self._cmd_syntax}:MEAN")
        self._min = PowerSwlossToffEnergyMin(device, f"{self._cmd_syntax}:MIN")

    @property
    def max(self) -> PowerSwlossToffEnergyMax:
        """Return the ``POWer:SWLoss:TOFF:ENERGY:MAX`` command.

        Description:
            - Returns the maximum Toff energy for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MAX?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOFF:ENERGY:MAX?
            ```
        """
        return self._max

    @property
    def mean(self) -> PowerSwlossToffEnergyMean:
        """Return the ``POWer:SWLoss:TOFF:ENERGY:MEAN`` command.

        Description:
            - Returns the mean Toff energy for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MEAN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOFF:ENERGY:MEAN?
            ```
        """
        return self._mean

    @property
    def min(self) -> PowerSwlossToffEnergyMin:
        """Return the ``POWer:SWLoss:TOFF:ENERGY:MIN`` command.

        Description:
            - Returns the minimum Toff energy for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MIN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:ENERGY:MIN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:TOFF:ENERGY:MIN?
            ```
        """
        return self._min


class PowerSwlossToff(SCPICmdRead):
    """The ``POWer:SWLoss:TOFF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.energy``: The ``POWer:SWLoss:TOFF:ENERGY`` command tree.
        - ``.power``: The ``POWer:SWLoss:TOFF:POWer`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._energy = PowerSwlossToffEnergy(device, f"{self._cmd_syntax}:ENERGY")
        self._power = PowerSwlossToffPower(device, f"{self._cmd_syntax}:POWer")

    @property
    def energy(self) -> PowerSwlossToffEnergy:
        """Return the ``POWer:SWLoss:TOFF:ENERGY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:ENERGY?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:ENERGY?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``POWer:SWLoss:TOFF:ENERGY:MAX`` command.
            - ``.mean``: The ``POWer:SWLoss:TOFF:ENERGY:MEAN`` command.
            - ``.min``: The ``POWer:SWLoss:TOFF:ENERGY:MIN`` command.
        """
        return self._energy

    @property
    def power(self) -> PowerSwlossToffPower:
        """Return the ``POWer:SWLoss:TOFF:POWer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF:POWer?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF:POWer?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``POWer:SWLoss:TOFF:POWer:MAX`` command.
            - ``.mean``: The ``POWer:SWLoss:TOFF:POWer:MEAN`` command.
            - ``.min``: The ``POWer:SWLoss:TOFF:POWer:MIN`` command.
        """
        return self._power


class PowerSwlossReflevelPercentLowvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:REFLevel:PERCent:LOWVoltage`` command.

    Description:
        - This command specifies the low voltage reference level used in switching loss power
          measurements in percent.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel:PERCent:LOWVoltage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:SWLoss:REFLevel:PERCent:LOWVoltage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:SWLoss:REFLevel:PERCent:LOWVoltage value`` command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:REFLevel:PERCent:LOWVoltage <NR3>
        - POWer:SWLoss:REFLevel:PERCent:LOWVoltage?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the low voltage reference level in
          percent.
    """


class PowerSwlossReflevelPercentLowcurrent(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:REFLevel:PERCent:LOWCurrent`` command.

    Description:
        - This command specifies the low current reference level used in switching loss power
          measurements in percent.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel:PERCent:LOWCurrent?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:SWLoss:REFLevel:PERCent:LOWCurrent?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:SWLoss:REFLevel:PERCent:LOWCurrent value`` command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:REFLevel:PERCent:LOWCurrent <NR3>
        - POWer:SWLoss:REFLevel:PERCent:LOWCurrent?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the low voltage reference level
          percent.
    """


class PowerSwlossReflevelPercentGatemid(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:REFLevel:PERCent:GATEMid`` command.

    Description:
        - This command specifies the mid voltage reference level used in switching loss power
          measurements in percent.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel:PERCent:GATEMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:SWLoss:REFLevel:PERCent:GATEMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:SWLoss:REFLevel:PERCent:GATEMid value`` command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:REFLevel:PERCent:GATEMid <NR3>
        - POWer:SWLoss:REFLevel:PERCent:GATEMid?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the mid voltage reference level in
          volts.
    """


class PowerSwlossReflevelPercent(SCPICmdRead):
    """The ``POWer:SWLoss:REFLevel:PERCent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel:PERCent?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:REFLevel:PERCent?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.gatemid``: The ``POWer:SWLoss:REFLevel:PERCent:GATEMid`` command.
        - ``.lowcurrent``: The ``POWer:SWLoss:REFLevel:PERCent:LOWCurrent`` command.
        - ``.lowvoltage``: The ``POWer:SWLoss:REFLevel:PERCent:LOWVoltage`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._gatemid = PowerSwlossReflevelPercentGatemid(device, f"{self._cmd_syntax}:GATEMid")
        self._lowcurrent = PowerSwlossReflevelPercentLowcurrent(
            device, f"{self._cmd_syntax}:LOWCurrent"
        )
        self._lowvoltage = PowerSwlossReflevelPercentLowvoltage(
            device, f"{self._cmd_syntax}:LOWVoltage"
        )

    @property
    def gatemid(self) -> PowerSwlossReflevelPercentGatemid:
        """Return the ``POWer:SWLoss:REFLevel:PERCent:GATEMid`` command.

        Description:
            - This command specifies the mid voltage reference level used in switching loss power
              measurements in percent.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel:PERCent:GATEMid?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:REFLevel:PERCent:GATEMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:SWLoss:REFLevel:PERCent:GATEMid value`` command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:REFLevel:PERCent:GATEMid <NR3>
            - POWer:SWLoss:REFLevel:PERCent:GATEMid?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the mid voltage reference level in
              volts.
        """
        return self._gatemid

    @property
    def lowcurrent(self) -> PowerSwlossReflevelPercentLowcurrent:
        """Return the ``POWer:SWLoss:REFLevel:PERCent:LOWCurrent`` command.

        Description:
            - This command specifies the low current reference level used in switching loss power
              measurements in percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:SWLoss:REFLevel:PERCent:LOWCurrent?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:REFLevel:PERCent:LOWCurrent?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:SWLoss:REFLevel:PERCent:LOWCurrent value`` command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:REFLevel:PERCent:LOWCurrent <NR3>
            - POWer:SWLoss:REFLevel:PERCent:LOWCurrent?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the low voltage reference level
              percent.
        """
        return self._lowcurrent

    @property
    def lowvoltage(self) -> PowerSwlossReflevelPercentLowvoltage:
        """Return the ``POWer:SWLoss:REFLevel:PERCent:LOWVoltage`` command.

        Description:
            - This command specifies the low voltage reference level used in switching loss power
              measurements in percent.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:SWLoss:REFLevel:PERCent:LOWVoltage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:REFLevel:PERCent:LOWVoltage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:SWLoss:REFLevel:PERCent:LOWVoltage value`` command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:REFLevel:PERCent:LOWVoltage <NR3>
            - POWer:SWLoss:REFLevel:PERCent:LOWVoltage?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the low voltage reference level in
              percent.
        """
        return self._lowvoltage


class PowerSwlossReflevelAbsoluteLowvoltage(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:REFLevel:ABSolute:LOWVoltage`` command.

    Description:
        - This command specifies the low voltage reference level used in switching loss power
          measurements in volts.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel:ABSolute:LOWVoltage?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:SWLoss:REFLevel:ABSolute:LOWVoltage?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:SWLoss:REFLevel:ABSolute:LOWVoltage value`` command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:REFLevel:ABSolute:LOWVoltage <NR3>
        - POWer:SWLoss:REFLevel:ABSolute:LOWVoltage?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the low voltage reference level in
          volts.
    """


class PowerSwlossReflevelAbsoluteLowcurrent(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:REFLevel:ABSolute:LOWCurrent`` command.

    Description:
        - This command specifies the low current reference level used in switching loss power
          measurements in amperes.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel:ABSolute:LOWCurrent?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:SWLoss:REFLevel:ABSolute:LOWCurrent?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:SWLoss:REFLevel:ABSolute:LOWCurrent value`` command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:REFLevel:ABSolute:LOWCurrent <NR3>
        - POWer:SWLoss:REFLevel:ABSolute:LOWCurrent?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the low voltage current level in
          amperes.
    """


class PowerSwlossReflevelAbsoluteGatemid(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:REFLevel:ABSolute:GATEMid`` command.

    Description:
        - This command specifies the mid voltage reference level used in switching loss power
          measurements in volts.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel:ABSolute:GATEMid?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:SWLoss:REFLevel:ABSolute:GATEMid?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:SWLoss:REFLevel:ABSolute:GATEMid value`` command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:REFLevel:ABSolute:GATEMid <NR3>
        - POWer:SWLoss:REFLevel:ABSolute:GATEMid?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the mid voltage reference level in
          volts.
    """


class PowerSwlossReflevelAbsolute(SCPICmdRead):
    """The ``POWer:SWLoss:REFLevel:ABSolute`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel:ABSolute?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:REFLevel:ABSolute?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.gatemid``: The ``POWer:SWLoss:REFLevel:ABSolute:GATEMid`` command.
        - ``.lowcurrent``: The ``POWer:SWLoss:REFLevel:ABSolute:LOWCurrent`` command.
        - ``.lowvoltage``: The ``POWer:SWLoss:REFLevel:ABSolute:LOWVoltage`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._gatemid = PowerSwlossReflevelAbsoluteGatemid(device, f"{self._cmd_syntax}:GATEMid")
        self._lowcurrent = PowerSwlossReflevelAbsoluteLowcurrent(
            device, f"{self._cmd_syntax}:LOWCurrent"
        )
        self._lowvoltage = PowerSwlossReflevelAbsoluteLowvoltage(
            device, f"{self._cmd_syntax}:LOWVoltage"
        )

    @property
    def gatemid(self) -> PowerSwlossReflevelAbsoluteGatemid:
        """Return the ``POWer:SWLoss:REFLevel:ABSolute:GATEMid`` command.

        Description:
            - This command specifies the mid voltage reference level used in switching loss power
              measurements in volts.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:SWLoss:REFLevel:ABSolute:GATEMid?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:REFLevel:ABSolute:GATEMid?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:SWLoss:REFLevel:ABSolute:GATEMid value`` command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:REFLevel:ABSolute:GATEMid <NR3>
            - POWer:SWLoss:REFLevel:ABSolute:GATEMid?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the mid voltage reference level in
              volts.
        """
        return self._gatemid

    @property
    def lowcurrent(self) -> PowerSwlossReflevelAbsoluteLowcurrent:
        """Return the ``POWer:SWLoss:REFLevel:ABSolute:LOWCurrent`` command.

        Description:
            - This command specifies the low current reference level used in switching loss power
              measurements in amperes.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:SWLoss:REFLevel:ABSolute:LOWCurrent?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:REFLevel:ABSolute:LOWCurrent?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:SWLoss:REFLevel:ABSolute:LOWCurrent value`` command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:REFLevel:ABSolute:LOWCurrent <NR3>
            - POWer:SWLoss:REFLevel:ABSolute:LOWCurrent?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the low voltage current level in
              amperes.
        """
        return self._lowcurrent

    @property
    def lowvoltage(self) -> PowerSwlossReflevelAbsoluteLowvoltage:
        """Return the ``POWer:SWLoss:REFLevel:ABSolute:LOWVoltage`` command.

        Description:
            - This command specifies the low voltage reference level used in switching loss power
              measurements in volts.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:SWLoss:REFLevel:ABSolute:LOWVoltage?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:REFLevel:ABSolute:LOWVoltage?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:SWLoss:REFLevel:ABSolute:LOWVoltage value`` command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:REFLevel:ABSolute:LOWVoltage <NR3>
            - POWer:SWLoss:REFLevel:ABSolute:LOWVoltage?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the low voltage reference level in
              volts.
        """
        return self._lowvoltage


class PowerSwlossReflevel(SCPICmdRead):
    """The ``POWer:SWLoss:REFLevel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:REFLevel?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absolute``: The ``POWer:SWLoss:REFLevel:ABSolute`` command tree.
        - ``.percent``: The ``POWer:SWLoss:REFLevel:PERCent`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = PowerSwlossReflevelAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._percent = PowerSwlossReflevelPercent(device, f"{self._cmd_syntax}:PERCent")

    @property
    def absolute(self) -> PowerSwlossReflevelAbsolute:
        """Return the ``POWer:SWLoss:REFLevel:ABSolute`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel:ABSolute?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:REFLevel:ABSolute?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.gatemid``: The ``POWer:SWLoss:REFLevel:ABSolute:GATEMid`` command.
            - ``.lowcurrent``: The ``POWer:SWLoss:REFLevel:ABSolute:LOWCurrent`` command.
            - ``.lowvoltage``: The ``POWer:SWLoss:REFLevel:ABSolute:LOWVoltage`` command.
        """
        return self._absolute

    @property
    def percent(self) -> PowerSwlossReflevelPercent:
        """Return the ``POWer:SWLoss:REFLevel:PERCent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel:PERCent?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:REFLevel:PERCent?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.gatemid``: The ``POWer:SWLoss:REFLevel:PERCent:GATEMid`` command.
            - ``.lowcurrent``: The ``POWer:SWLoss:REFLevel:PERCent:LOWCurrent`` command.
            - ``.lowvoltage``: The ``POWer:SWLoss:REFLevel:PERCent:LOWVoltage`` command.
        """
        return self._percent


class PowerSwlossRdson(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:RDSon`` command.

    Description:
        - This command specifies the user RDSON value for use in switching loss calculations when
          the conduction calculation method is RDSON.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:RDSon?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:RDSon?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SWLoss:RDSon value`` command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:RDSon <NR3>
        - POWer:SWLoss:RDSon?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the RDSON switching loss calculation.
    """


class PowerSwlossNumcycles(SCPICmdReadWithArguments):
    """The ``POWer:SWLoss:NUMCYCles`` command.

    Description:
        - Returns the number of cycles counted for the switching loss calculation.

    Usage:
        - Using the ``.query(argument)`` method will send the ``POWer:SWLoss:NUMCYCles? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:SWLoss:NUMCYCles? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:NUMCYCles? <NR3>
        ```
    """


class PowerSwlossGateTurnon(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:GATe:TURNON`` command.

    Description:
        - This command specifies the gate turn on level for switching loss power measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:GATe:TURNON?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:GATe:TURNON?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SWLoss:GATe:TURNON value``
          command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:GATe:TURNON <NR3>
        - POWer:SWLoss:GATe:TURNON?
        ```
    """


class PowerSwlossGatePolarity(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:GATe:POLarity`` command.

    Description:
        - This command specifies the switching loss gate polarity.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:GATe:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:GATe:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SWLoss:GATe:POLarity value``
          command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:GATe:POLarity {FALL|RISe}
        - POWer:SWLoss:GATe:POLarity?
        ```

    Info:
        - ``FALL`` sets falling edge as the switching loss gate polarity.
        - ``RISe`` sets rising edge as the switching loss gate polarity.
    """


class PowerSwlossGate(SCPICmdRead):
    """The ``POWer:SWLoss:GATe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:GATe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:GATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``POWer:SWLoss:GATe:POLarity`` command.
        - ``.turnon``: The ``POWer:SWLoss:GATe:TURNON`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = PowerSwlossGatePolarity(device, f"{self._cmd_syntax}:POLarity")
        self._turnon = PowerSwlossGateTurnon(device, f"{self._cmd_syntax}:TURNON")

    @property
    def polarity(self) -> PowerSwlossGatePolarity:
        """Return the ``POWer:SWLoss:GATe:POLarity`` command.

        Description:
            - This command specifies the switching loss gate polarity.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:GATe:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:GATe:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SWLoss:GATe:POLarity value``
              command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:GATe:POLarity {FALL|RISe}
            - POWer:SWLoss:GATe:POLarity?
            ```

        Info:
            - ``FALL`` sets falling edge as the switching loss gate polarity.
            - ``RISe`` sets rising edge as the switching loss gate polarity.
        """
        return self._polarity

    @property
    def turnon(self) -> PowerSwlossGateTurnon:
        """Return the ``POWer:SWLoss:GATe:TURNON`` command.

        Description:
            - This command specifies the gate turn on level for switching loss power measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:GATe:TURNON?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:GATe:TURNON?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SWLoss:GATe:TURNON value``
              command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:GATe:TURNON <NR3>
            - POWer:SWLoss:GATe:TURNON?
            ```
        """
        return self._turnon


class PowerSwlossDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:DISplay`` command.

    Description:
        - This command specifies the display selection for switching loss results: All measurements,
          energy loss measurements or power loss measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:DISplay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SWLoss:DISplay value`` command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:DISplay {ALL|ENERGYLoss|POWERLoss}
        - POWer:SWLoss:DISplay?
        ```

    Info:
        - ``ALL`` displays both energy and power loss measurements in the results.
        - ``ENERGYLoss`` displays only energy loss measurements in the results.
        - ``POWERLoss`` displays only power loss measurements in the results.
    """


class PowerSwlossConductionPowerMin(SCPICmdRead):
    """The ``POWer:SWLoss:CONDuction:POWer:MIN`` command.

    Description:
        - Returns the minimum conduction power for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:POWer:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction:POWer:MIN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:CONDuction:POWer:MIN?
        ```
    """


class PowerSwlossConductionPowerMean(SCPICmdRead):
    """The ``POWer:SWLoss:CONDuction:POWer:MEAN`` command.

    Description:
        - Returns the mean conduction power for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:POWer:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction:POWer:MEAN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:CONDuction:POWer:MEAN?
        ```
    """


class PowerSwlossConductionPowerMax(SCPICmdRead):
    """The ``POWer:SWLoss:CONDuction:POWer:MAX`` command.

    Description:
        - Returns the maximum conduction power for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:POWer:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction:POWer:MAX?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:CONDuction:POWer:MAX?
        ```
    """


class PowerSwlossConductionPower(SCPICmdRead):
    """The ``POWer:SWLoss:CONDuction:POWer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction:POWer?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``POWer:SWLoss:CONDuction:POWer:MAX`` command.
        - ``.mean``: The ``POWer:SWLoss:CONDuction:POWer:MEAN`` command.
        - ``.min``: The ``POWer:SWLoss:CONDuction:POWer:MIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = PowerSwlossConductionPowerMax(device, f"{self._cmd_syntax}:MAX")
        self._mean = PowerSwlossConductionPowerMean(device, f"{self._cmd_syntax}:MEAN")
        self._min = PowerSwlossConductionPowerMin(device, f"{self._cmd_syntax}:MIN")

    @property
    def max(self) -> PowerSwlossConductionPowerMax:
        """Return the ``POWer:SWLoss:CONDuction:POWer:MAX`` command.

        Description:
            - Returns the maximum conduction power for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:POWer:MAX?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:CONDuction:POWer:MAX?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:CONDuction:POWer:MAX?
            ```
        """
        return self._max

    @property
    def mean(self) -> PowerSwlossConductionPowerMean:
        """Return the ``POWer:SWLoss:CONDuction:POWer:MEAN`` command.

        Description:
            - Returns the mean conduction power for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:POWer:MEAN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:CONDuction:POWer:MEAN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:CONDuction:POWer:MEAN?
            ```
        """
        return self._mean

    @property
    def min(self) -> PowerSwlossConductionPowerMin:
        """Return the ``POWer:SWLoss:CONDuction:POWer:MIN`` command.

        Description:
            - Returns the minimum conduction power for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:POWer:MIN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:CONDuction:POWer:MIN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:CONDuction:POWer:MIN?
            ```
        """
        return self._min


class PowerSwlossConductionEnergyMin(SCPICmdRead):
    """The ``POWer:SWLoss:CONDuction:ENERGY:MIN`` command.

    Description:
        - Returns the minimum conduction energy for the switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:ENERGY:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction:ENERGY:MIN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:CONDuction:ENERGY:MIN?
        ```
    """


class PowerSwlossConductionEnergyMean(SCPICmdRead):
    """The ``POWer:SWLoss:CONDuction:ENERGY:MEAN`` command.

    Description:
        - Returns the mean conduction energy in the conduction period for the switching loss
          calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:ENERGY:MEAN?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction:ENERGY:MEAN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:CONDuction:ENERGY:MEAN?
        ```
    """


class PowerSwlossConductionEnergyMax(SCPICmdRead):
    """The ``POWer:SWLoss:CONDuction:ENERGY:MAX`` command.

    Description:
        - Returns the maximum conduction energy for switching loss calculation.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:ENERGY:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction:ENERGY:MAX?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SWLoss:CONDuction:ENERGY:MAX?
        ```
    """


class PowerSwlossConductionEnergy(SCPICmdRead):
    """The ``POWer:SWLoss:CONDuction:ENERGY`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:ENERGY?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction:ENERGY?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``POWer:SWLoss:CONDuction:ENERGY:MAX`` command.
        - ``.mean``: The ``POWer:SWLoss:CONDuction:ENERGY:MEAN`` command.
        - ``.min``: The ``POWer:SWLoss:CONDuction:ENERGY:MIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = PowerSwlossConductionEnergyMax(device, f"{self._cmd_syntax}:MAX")
        self._mean = PowerSwlossConductionEnergyMean(device, f"{self._cmd_syntax}:MEAN")
        self._min = PowerSwlossConductionEnergyMin(device, f"{self._cmd_syntax}:MIN")

    @property
    def max(self) -> PowerSwlossConductionEnergyMax:
        """Return the ``POWer:SWLoss:CONDuction:ENERGY:MAX`` command.

        Description:
            - Returns the maximum conduction energy for switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:ENERGY:MAX?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:CONDuction:ENERGY:MAX?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:CONDuction:ENERGY:MAX?
            ```
        """
        return self._max

    @property
    def mean(self) -> PowerSwlossConductionEnergyMean:
        """Return the ``POWer:SWLoss:CONDuction:ENERGY:MEAN`` command.

        Description:
            - Returns the mean conduction energy in the conduction period for the switching loss
              calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:ENERGY:MEAN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:CONDuction:ENERGY:MEAN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:CONDuction:ENERGY:MEAN?
            ```
        """
        return self._mean

    @property
    def min(self) -> PowerSwlossConductionEnergyMin:
        """Return the ``POWer:SWLoss:CONDuction:ENERGY:MIN`` command.

        Description:
            - Returns the minimum conduction energy for the switching loss calculation.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:ENERGY:MIN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:SWLoss:CONDuction:ENERGY:MIN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:CONDuction:ENERGY:MIN?
            ```
        """
        return self._min


class PowerSwlossConduction(SCPICmdRead):
    """The ``POWer:SWLoss:CONDuction`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.energy``: The ``POWer:SWLoss:CONDuction:ENERGY`` command tree.
        - ``.power``: The ``POWer:SWLoss:CONDuction:POWer`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._energy = PowerSwlossConductionEnergy(device, f"{self._cmd_syntax}:ENERGY")
        self._power = PowerSwlossConductionPower(device, f"{self._cmd_syntax}:POWer")

    @property
    def energy(self) -> PowerSwlossConductionEnergy:
        """Return the ``POWer:SWLoss:CONDuction:ENERGY`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:ENERGY?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction:ENERGY?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``POWer:SWLoss:CONDuction:ENERGY:MAX`` command.
            - ``.mean``: The ``POWer:SWLoss:CONDuction:ENERGY:MEAN`` command.
            - ``.min``: The ``POWer:SWLoss:CONDuction:ENERGY:MIN`` command.
        """
        return self._energy

    @property
    def power(self) -> PowerSwlossConductionPower:
        """Return the ``POWer:SWLoss:CONDuction:POWer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction:POWer?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction:POWer?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``POWer:SWLoss:CONDuction:POWer:MAX`` command.
            - ``.mean``: The ``POWer:SWLoss:CONDuction:POWer:MEAN`` command.
            - ``.min``: The ``POWer:SWLoss:CONDuction:POWer:MIN`` command.
        """
        return self._power


class PowerSwlossCondcalcmethod(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SWLoss:CONDCALCmethod`` command.

    Description:
        - This command specifies the power application switching loss conduction calculation method.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDCALCmethod?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDCALCmethod?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SWLoss:CONDCALCmethod value``
          command.

    SCPI Syntax:
        ```
        - POWer:SWLoss:CONDCALCmethod {VOLTage|RDSon|VCEsat}
        - POWer:SWLoss:CONDCALCmethod?
        ```

    Info:
        - ``VOLTage`` sets voltage as the conduction calculation method.
        - ``RDSon`` sets RDSon as the conduction calculation method.
        - ``VCEsat`` sets VCEsat as the conduction calculation method.
    """


#  pylint: disable=too-many-instance-attributes
class PowerSwloss(SCPICmdRead):
    """The ``POWer:SWLoss`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SWLoss?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SWLoss?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condcalcmethod``: The ``POWer:SWLoss:CONDCALCmethod`` command.
        - ``.conduction``: The ``POWer:SWLoss:CONDuction`` command tree.
        - ``.display``: The ``POWer:SWLoss:DISplay`` command.
        - ``.gate``: The ``POWer:SWLoss:GATe`` command tree.
        - ``.numcycles``: The ``POWer:SWLoss:NUMCYCles`` command.
        - ``.rdson``: The ``POWer:SWLoss:RDSon`` command.
        - ``.reflevel``: The ``POWer:SWLoss:REFLevel`` command tree.
        - ``.toff``: The ``POWer:SWLoss:TOFF`` command tree.
        - ``.ton``: The ``POWer:SWLoss:TON`` command tree.
        - ``.total``: The ``POWer:SWLoss:TOTal`` command tree.
        - ``.vcesat``: The ``POWer:SWLoss:VCEsat`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condcalcmethod = PowerSwlossCondcalcmethod(
            device, f"{self._cmd_syntax}:CONDCALCmethod"
        )
        self._conduction = PowerSwlossConduction(device, f"{self._cmd_syntax}:CONDuction")
        self._display = PowerSwlossDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._gate = PowerSwlossGate(device, f"{self._cmd_syntax}:GATe")
        self._numcycles = PowerSwlossNumcycles(device, f"{self._cmd_syntax}:NUMCYCles")
        self._rdson = PowerSwlossRdson(device, f"{self._cmd_syntax}:RDSon")
        self._reflevel = PowerSwlossReflevel(device, f"{self._cmd_syntax}:REFLevel")
        self._toff = PowerSwlossToff(device, f"{self._cmd_syntax}:TOFF")
        self._ton = PowerSwlossTon(device, f"{self._cmd_syntax}:TON")
        self._total = PowerSwlossTotal(device, f"{self._cmd_syntax}:TOTal")
        self._vcesat = PowerSwlossVcesat(device, f"{self._cmd_syntax}:VCEsat")

    @property
    def condcalcmethod(self) -> PowerSwlossCondcalcmethod:
        """Return the ``POWer:SWLoss:CONDCALCmethod`` command.

        Description:
            - This command specifies the power application switching loss conduction calculation
              method.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDCALCmethod?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDCALCmethod?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SWLoss:CONDCALCmethod value``
              command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:CONDCALCmethod {VOLTage|RDSon|VCEsat}
            - POWer:SWLoss:CONDCALCmethod?
            ```

        Info:
            - ``VOLTage`` sets voltage as the conduction calculation method.
            - ``RDSon`` sets RDSon as the conduction calculation method.
            - ``VCEsat`` sets VCEsat as the conduction calculation method.
        """
        return self._condcalcmethod

    @property
    def conduction(self) -> PowerSwlossConduction:
        """Return the ``POWer:SWLoss:CONDuction`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:CONDuction?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:CONDuction?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.energy``: The ``POWer:SWLoss:CONDuction:ENERGY`` command tree.
            - ``.power``: The ``POWer:SWLoss:CONDuction:POWer`` command tree.
        """
        return self._conduction

    @property
    def display(self) -> PowerSwlossDisplay:
        """Return the ``POWer:SWLoss:DISplay`` command.

        Description:
            - This command specifies the display selection for switching loss results: All
              measurements, energy loss measurements or power loss measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:DISplay?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SWLoss:DISplay value``
              command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:DISplay {ALL|ENERGYLoss|POWERLoss}
            - POWer:SWLoss:DISplay?
            ```

        Info:
            - ``ALL`` displays both energy and power loss measurements in the results.
            - ``ENERGYLoss`` displays only energy loss measurements in the results.
            - ``POWERLoss`` displays only power loss measurements in the results.
        """
        return self._display

    @property
    def gate(self) -> PowerSwlossGate:
        """Return the ``POWer:SWLoss:GATe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:GATe?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:GATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``POWer:SWLoss:GATe:POLarity`` command.
            - ``.turnon``: The ``POWer:SWLoss:GATe:TURNON`` command.
        """
        return self._gate

    @property
    def numcycles(self) -> PowerSwlossNumcycles:
        """Return the ``POWer:SWLoss:NUMCYCles`` command.

        Description:
            - Returns the number of cycles counted for the switching loss calculation.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:SWLoss:NUMCYCles? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:SWLoss:NUMCYCles? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SWLoss:NUMCYCles? <NR3>
            ```
        """
        return self._numcycles

    @property
    def rdson(self) -> PowerSwlossRdson:
        """Return the ``POWer:SWLoss:RDSon`` command.

        Description:
            - This command specifies the user RDSON value for use in switching loss calculations
              when the conduction calculation method is RDSON.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:RDSon?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:RDSon?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SWLoss:RDSon value`` command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:RDSon <NR3>
            - POWer:SWLoss:RDSon?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the RDSON switching loss
              calculation.
        """
        return self._rdson

    @property
    def reflevel(self) -> PowerSwlossReflevel:
        """Return the ``POWer:SWLoss:REFLevel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:REFLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:REFLevel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.absolute``: The ``POWer:SWLoss:REFLevel:ABSolute`` command tree.
            - ``.percent``: The ``POWer:SWLoss:REFLevel:PERCent`` command tree.
        """
        return self._reflevel

    @property
    def toff(self) -> PowerSwlossToff:
        """Return the ``POWer:SWLoss:TOFF`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOFF?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOFF?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.energy``: The ``POWer:SWLoss:TOFF:ENERGY`` command tree.
            - ``.power``: The ``POWer:SWLoss:TOFF:POWer`` command tree.
        """
        return self._toff

    @property
    def ton(self) -> PowerSwlossTon:
        """Return the ``POWer:SWLoss:TON`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TON?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TON?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.energy``: The ``POWer:SWLoss:TON:ENERGY`` command tree.
            - ``.power``: The ``POWer:SWLoss:TON:POWer`` command tree.
        """
        return self._ton

    @property
    def total(self) -> PowerSwlossTotal:
        """Return the ``POWer:SWLoss:TOTal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:TOTal?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:TOTal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.energy``: The ``POWer:SWLoss:TOTal:ENERGY`` command tree.
            - ``.power``: The ``POWer:SWLoss:TOTal:POWer`` command tree.
        """
        return self._total

    @property
    def vcesat(self) -> PowerSwlossVcesat:
        """Return the ``POWer:SWLoss:VCEsat`` command.

        Description:
            - This command specifies VCESAT value for use in switching loss calculations when the
              conduction calculation method is VCESAT.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss:VCEsat?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss:VCEsat?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SWLoss:VCEsat value``
              command.

        SCPI Syntax:
            ```
            - POWer:SWLoss:VCEsat <NR3>
            - POWer:SWLoss:VCEsat?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the VCEsat switching loss
              calculation.
        """
        return self._vcesat


class PowerStatisticsWeighting(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:STATIstics:WEIghting`` command.

    Description:
        - Sets the number of samples which are included for the statistics computations for mean and
          the standard deviation. Performs the same function as the
          ``MEASUREMENT:STATISTICS:WEIGHTING`` command.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:STATIstics:WEIghting?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:STATIstics:WEIghting?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:STATIstics:WEIghting value``
          command.

    SCPI Syntax:
        ```
        - POWer:STATIstics:WEIghting <NR1>;Ranges {L,2,1000}
        - POWer:STATIstics:WEIghting?
        ```

    Info:
        - ``<NR1>`` is the number of samples used for the mean and standard deviation statistical
          accumulations.
    """


class PowerStatisticsMode(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:STATIstics:MODe`` command.

    Description:
        - Enables or disables the display of the measurement statistics. Performs the same function
          as the ``MEASUREMENT:STATISTICS:MODE`` command.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:STATIstics:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:STATIstics:MODe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:STATIstics:MODe value`` command.

    SCPI Syntax:
        ```
        - POWer:STATIstics:MODe {OFF|ALL}
        - POWer:STATIstics:MODe?
        ```

    Info:
        - ``ALL`` turns on measurement statistics display.
        - ``OFF`` turns all measurements statistics off.
    """


class PowerStatistics(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:STATIstics`` command.

    Description:
        - Clears all the accumulated statistics of all measurements. Performs the same function as
          the ``MEASUREMENT:STATISTICS`` command.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:STATIstics value`` command.

    SCPI Syntax:
        ```
        - POWer:STATIstics {RESET}
        ```

    Info:
        - ``RESET`` clears the measurement statistics.

    Properties:
        - ``.mode``: The ``POWer:STATIstics:MODe`` command.
        - ``.weighting``: The ``POWer:STATIstics:WEIghting`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = PowerStatisticsMode(device, f"{self._cmd_syntax}:MODe")
        self._weighting = PowerStatisticsWeighting(device, f"{self._cmd_syntax}:WEIghting")

    @property
    def mode(self) -> PowerStatisticsMode:
        """Return the ``POWer:STATIstics:MODe`` command.

        Description:
            - Enables or disables the display of the measurement statistics. Performs the same
              function as the ``MEASUREMENT:STATISTICS:MODE`` command.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:STATIstics:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:STATIstics:MODe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:STATIstics:MODe value``
              command.

        SCPI Syntax:
            ```
            - POWer:STATIstics:MODe {OFF|ALL}
            - POWer:STATIstics:MODe?
            ```

        Info:
            - ``ALL`` turns on measurement statistics display.
            - ``OFF`` turns all measurements statistics off.
        """
        return self._mode

    @property
    def weighting(self) -> PowerStatisticsWeighting:
        """Return the ``POWer:STATIstics:WEIghting`` command.

        Description:
            - Sets the number of samples which are included for the statistics computations for mean
              and the standard deviation. Performs the same function as the
              ``MEASUREMENT:STATISTICS:WEIGHTING`` command.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:STATIstics:WEIghting?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:STATIstics:WEIghting?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:STATIstics:WEIghting value``
              command.

        SCPI Syntax:
            ```
            - POWer:STATIstics:WEIghting <NR1>;Ranges {L,2,1000}
            - POWer:STATIstics:WEIghting?
            ```

        Info:
            - ``<NR1>`` is the number of samples used for the mean and standard deviation
              statistical accumulations.
        """
        return self._weighting


class PowerSoaResultState(SCPICmdRead):
    """The ``POWer:SOA:RESult:STATE`` command.

    Description:
        - Returns the pass/fail state of the SOA test.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:RESult:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:RESult:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SOA:RESult:STATE?
        ```
    """


class PowerSoaResultNumacq(SCPICmdRead):
    """The ``POWer:SOA:RESult:NUMACq`` command.

    Description:
        - Returns the number of acquisitions in the test.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:RESult:NUMACq?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:RESult:NUMACq?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SOA:RESult:NUMACq?
        ```
    """


class PowerSoaResultFailuresQty(SCPICmdRead):
    """The ``POWer:SOA:RESult:FAILures:QTY`` command.

    Description:
        - Returns the number of failures in the test.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:RESult:FAILures:QTY?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:RESult:FAILures:QTY?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SOA:RESult:FAILures:QTY?
        ```
    """


class PowerSoaResultFailures(SCPICmdRead):
    """The ``POWer:SOA:RESult:FAILures`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:RESult:FAILures?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:RESult:FAILures?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.qty``: The ``POWer:SOA:RESult:FAILures:QTY`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._qty = PowerSoaResultFailuresQty(device, f"{self._cmd_syntax}:QTY")

    @property
    def qty(self) -> PowerSoaResultFailuresQty:
        """Return the ``POWer:SOA:RESult:FAILures:QTY`` command.

        Description:
            - Returns the number of failures in the test.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:RESult:FAILures:QTY?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:RESult:FAILures:QTY?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SOA:RESult:FAILures:QTY?
            ```
        """
        return self._qty


class PowerSoaResult(SCPICmdRead):
    """The ``POWer:SOA:RESult`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:RESult?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:RESult?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.failures``: The ``POWer:SOA:RESult:FAILures`` command tree.
        - ``.numacq``: The ``POWer:SOA:RESult:NUMACq`` command.
        - ``.state``: The ``POWer:SOA:RESult:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._failures = PowerSoaResultFailures(device, f"{self._cmd_syntax}:FAILures")
        self._numacq = PowerSoaResultNumacq(device, f"{self._cmd_syntax}:NUMACq")
        self._state = PowerSoaResultState(device, f"{self._cmd_syntax}:STATE")

    @property
    def failures(self) -> PowerSoaResultFailures:
        """Return the ``POWer:SOA:RESult:FAILures`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:RESult:FAILures?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:RESult:FAILures?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.qty``: The ``POWer:SOA:RESult:FAILures:QTY`` command.
        """
        return self._failures

    @property
    def numacq(self) -> PowerSoaResultNumacq:
        """Return the ``POWer:SOA:RESult:NUMACq`` command.

        Description:
            - Returns the number of acquisitions in the test.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:RESult:NUMACq?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:RESult:NUMACq?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SOA:RESult:NUMACq?
            ```
        """
        return self._numacq

    @property
    def state(self) -> PowerSoaResultState:
        """Return the ``POWer:SOA:RESult:STATE`` command.

        Description:
            - Returns the pass/fail state of the SOA test.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:RESult:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:RESult:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SOA:RESult:STATE?
            ```
        """
        return self._state


class PowerSoaPlottype(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:PLOTTYPe`` command.

    Description:
        - This command specifies the Safe Operating Area (SOA) plot type.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:PLOTTYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:PLOTTYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:PLOTTYPe value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:PLOTTYPe {LOG|LINear}
        - POWer:SOA:PLOTTYPe?
        ```

    Info:
        - ``LOG`` for logarithmic SOA plot type.
        - ``LINear`` for linear SOA plot type.
    """


class PowerSoaMaskStoponviol(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:MASK:STOPOnviol`` command.

    Description:
        - This command specifies the enabled state of the mask stop on violation condition.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:MASK:STOPOnviol?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:STOPOnviol?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:STOPOnviol value``
          command.

    SCPI Syntax:
        ```
        - POWer:SOA:MASK:STOPOnviol {OFF|ON|0|1}
        - POWer:SOA:MASK:STOPOnviol?
        ```

    Info:
        - ``OFF`` or 0 enables mask stop on violations.
        - ``ON`` or 1 disables mask stop on violations.
    """


class PowerSoaMaskState(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:MASK:STATE`` command.

    Description:
        - This command specifies the state of the mask for SOA calculations.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:MASK:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:STATE value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:MASK:STATE {OFF|LIMITS|POINTS}
        - POWer:SOA:MASK:STATE?
        ```

    Info:
        - ``OFF`` disables mask testing.
        - ``LIMITS`` enables mask testing based on limits specified using
          ``POWER:SOA:MASK:MAXAMPS``, ``POWER:SOA:MASK:MAXVOLTS``, and ``POWER:SOA:MASK:MAXWATTS``
          commands.
        - ``POINTS`` enables mask testing based on masks points defined.
    """


class PowerSoaMaskNrPt(SCPICmdRead):
    """The ``POWer:SOA:MASK:NR_Pt`` command.

    Description:
        - Returns the number of mask points defined.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:MASK:NR_Pt?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:NR_Pt?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:SOA:MASK:NR_Pt?
        ```
    """


class PowerSoaMaskMaxwatts(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:MASK:MAXWatts`` command.

    Description:
        - This command specifies the maximum power applied to SOA mask testing.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:MASK:MAXWatts?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:MAXWatts?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:MAXWatts value``
          command.

    SCPI Syntax:
        ```
        - POWer:SOA:MASK:MAXWatts <NR3>
        - POWer:SOA:MASK:MAXWatts?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the maximum power applied to SOA mask
          testing.
    """


class PowerSoaMaskMaxvolts(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:MASK:MAXVolts`` command.

    Description:
        - This command specifies the maximum voltage applied to SOA mask testing.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:MASK:MAXVolts?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:MAXVolts?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:MAXVolts value``
          command.

    SCPI Syntax:
        ```
        - POWer:SOA:MASK:MAXVolts <NR3>
        - POWer:SOA:MASK:MAXVolts?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the maximum voltage applied to SOA
          mask testing.
    """


class PowerSoaMaskMaxamps(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:MASK:MAXAmps`` command.

    Description:
        - This command specifies the maximum current applied to SOA mask testing.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:MASK:MAXAmps?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:MAXAmps?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:MAXAmps value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:MASK:MAXAmps <NR3>
        - POWer:SOA:MASK:MAXAmps?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the maximum current applied to SOA
          mask testing.
    """


class PowerSoaMaskDefine(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:MASK:DEFine`` command.

    Description:
        - This command specifies the X (volts) and Y (Amps) coordinates of the current SOA mask. You
          can specify the number of points from 2 to 10, minimum being 2. Successive X values must
          be ≥ the preceding X values. The number of XY points sent determines the value of
          ``NR_PT``.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:MASK:DEFine?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:DEFine?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:DEFine value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:MASK:DEFine <NR3>
        - POWer:SOA:MASK:DEFine?
        ```

    Info:
        - ``<NR3>`` is a floating point number that represents the SOA mask coordinates.
    """


class PowerSoaMask(SCPICmdRead):
    """The ``POWer:SOA:MASK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:MASK?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.define``: The ``POWer:SOA:MASK:DEFine`` command.
        - ``.maxamps``: The ``POWer:SOA:MASK:MAXAmps`` command.
        - ``.maxvolts``: The ``POWer:SOA:MASK:MAXVolts`` command.
        - ``.maxwatts``: The ``POWer:SOA:MASK:MAXWatts`` command.
        - ``.nr_pt``: The ``POWer:SOA:MASK:NR_Pt`` command.
        - ``.state``: The ``POWer:SOA:MASK:STATE`` command.
        - ``.stoponviol``: The ``POWer:SOA:MASK:STOPOnviol`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._define = PowerSoaMaskDefine(device, f"{self._cmd_syntax}:DEFine")
        self._maxamps = PowerSoaMaskMaxamps(device, f"{self._cmd_syntax}:MAXAmps")
        self._maxvolts = PowerSoaMaskMaxvolts(device, f"{self._cmd_syntax}:MAXVolts")
        self._maxwatts = PowerSoaMaskMaxwatts(device, f"{self._cmd_syntax}:MAXWatts")
        self._nr_pt = PowerSoaMaskNrPt(device, f"{self._cmd_syntax}:NR_Pt")
        self._state = PowerSoaMaskState(device, f"{self._cmd_syntax}:STATE")
        self._stoponviol = PowerSoaMaskStoponviol(device, f"{self._cmd_syntax}:STOPOnviol")

    @property
    def define(self) -> PowerSoaMaskDefine:
        """Return the ``POWer:SOA:MASK:DEFine`` command.

        Description:
            - This command specifies the X (volts) and Y (Amps) coordinates of the current SOA mask.
              You can specify the number of points from 2 to 10, minimum being 2. Successive X
              values must be ≥ the preceding X values. The number of XY points sent determines the
              value of ``NR_PT``.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:MASK:DEFine?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:DEFine?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:DEFine value``
              command.

        SCPI Syntax:
            ```
            - POWer:SOA:MASK:DEFine <NR3>
            - POWer:SOA:MASK:DEFine?
            ```

        Info:
            - ``<NR3>`` is a floating point number that represents the SOA mask coordinates.
        """
        return self._define

    @property
    def maxamps(self) -> PowerSoaMaskMaxamps:
        """Return the ``POWer:SOA:MASK:MAXAmps`` command.

        Description:
            - This command specifies the maximum current applied to SOA mask testing.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:MASK:MAXAmps?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:MAXAmps?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:MAXAmps value``
              command.

        SCPI Syntax:
            ```
            - POWer:SOA:MASK:MAXAmps <NR3>
            - POWer:SOA:MASK:MAXAmps?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the maximum current applied to SOA
              mask testing.
        """
        return self._maxamps

    @property
    def maxvolts(self) -> PowerSoaMaskMaxvolts:
        """Return the ``POWer:SOA:MASK:MAXVolts`` command.

        Description:
            - This command specifies the maximum voltage applied to SOA mask testing.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:MASK:MAXVolts?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:MAXVolts?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:MAXVolts value``
              command.

        SCPI Syntax:
            ```
            - POWer:SOA:MASK:MAXVolts <NR3>
            - POWer:SOA:MASK:MAXVolts?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the maximum voltage applied to SOA
              mask testing.
        """
        return self._maxvolts

    @property
    def maxwatts(self) -> PowerSoaMaskMaxwatts:
        """Return the ``POWer:SOA:MASK:MAXWatts`` command.

        Description:
            - This command specifies the maximum power applied to SOA mask testing.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:MASK:MAXWatts?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:MAXWatts?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:MAXWatts value``
              command.

        SCPI Syntax:
            ```
            - POWer:SOA:MASK:MAXWatts <NR3>
            - POWer:SOA:MASK:MAXWatts?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the maximum power applied to SOA
              mask testing.
        """
        return self._maxwatts

    @property
    def nr_pt(self) -> PowerSoaMaskNrPt:
        """Return the ``POWer:SOA:MASK:NR_Pt`` command.

        Description:
            - Returns the number of mask points defined.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:MASK:NR_Pt?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:NR_Pt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:SOA:MASK:NR_Pt?
            ```
        """
        return self._nr_pt

    @property
    def state(self) -> PowerSoaMaskState:
        """Return the ``POWer:SOA:MASK:STATE`` command.

        Description:
            - This command specifies the state of the mask for SOA calculations.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:MASK:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:STATE value``
              command.

        SCPI Syntax:
            ```
            - POWer:SOA:MASK:STATE {OFF|LIMITS|POINTS}
            - POWer:SOA:MASK:STATE?
            ```

        Info:
            - ``OFF`` disables mask testing.
            - ``LIMITS`` enables mask testing based on limits specified using
              ``POWER:SOA:MASK:MAXAMPS``, ``POWER:SOA:MASK:MAXVOLTS``, and
              ``POWER:SOA:MASK:MAXWATTS`` commands.
            - ``POINTS`` enables mask testing based on masks points defined.
        """
        return self._state

    @property
    def stoponviol(self) -> PowerSoaMaskStoponviol:
        """Return the ``POWer:SOA:MASK:STOPOnviol`` command.

        Description:
            - This command specifies the enabled state of the mask stop on violation condition.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:MASK:STOPOnviol?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK:STOPOnviol?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:MASK:STOPOnviol value``
              command.

        SCPI Syntax:
            ```
            - POWer:SOA:MASK:STOPOnviol {OFF|ON|0|1}
            - POWer:SOA:MASK:STOPOnviol?
            ```

        Info:
            - ``OFF`` or 0 enables mask stop on violations.
            - ``ON`` or 1 disables mask stop on violations.
        """
        return self._stoponviol


class PowerSoaLogYmin(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:LOG:YMIN`` command.

    Description:
        - This command specifies the user YMIN value for use in Log SOA calculations.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:LOG:YMIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:LOG:YMIN?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:LOG:YMIN value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:LOG:YMIN <NR3>
        - POWer:SOA:LOG:YMIN?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the YMIN value used for log SOA
          calculations.
    """


class PowerSoaLogYmax(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:LOG:YMAX`` command.

    Description:
        - This command specifies the user YMAX value for use in Log SOA calculations.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:LOG:YMAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:LOG:YMAX?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:LOG:YMAX value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:LOG:YMAX <NR3>
        - POWer:SOA:LOG:YMAX?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the YMAX value used for log SOA
          calculations.
    """


class PowerSoaLogXmin(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:LOG:XMIN`` command.

    Description:
        - This command specifies the user XMIN value for use in Log SOA calculations.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:LOG:XMIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:LOG:XMIN?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:LOG:XMIN value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:LOG:XMIN <NR3>
        - POWer:SOA:LOG:XMIN?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the XMIN value used for log SOA
          calculations.
    """


class PowerSoaLogXmax(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:LOG:XMAX`` command.

    Description:
        - This command specifies the user XMAX value for use in Log SOA calculations.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:LOG:XMAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:LOG:XMAX?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:LOG:XMAX value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:LOG:XMAX <NR3>
        - POWer:SOA:LOG:XMAX?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the XMAX value used for log SOA
          calculations.
    """


class PowerSoaLog(SCPICmdRead):
    """The ``POWer:SOA:LOG`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:LOG?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:LOG?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.xmax``: The ``POWer:SOA:LOG:XMAX`` command.
        - ``.xmin``: The ``POWer:SOA:LOG:XMIN`` command.
        - ``.ymax``: The ``POWer:SOA:LOG:YMAX`` command.
        - ``.ymin``: The ``POWer:SOA:LOG:YMIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._xmax = PowerSoaLogXmax(device, f"{self._cmd_syntax}:XMAX")
        self._xmin = PowerSoaLogXmin(device, f"{self._cmd_syntax}:XMIN")
        self._ymax = PowerSoaLogYmax(device, f"{self._cmd_syntax}:YMAX")
        self._ymin = PowerSoaLogYmin(device, f"{self._cmd_syntax}:YMIN")

    @property
    def xmax(self) -> PowerSoaLogXmax:
        """Return the ``POWer:SOA:LOG:XMAX`` command.

        Description:
            - This command specifies the user XMAX value for use in Log SOA calculations.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:LOG:XMAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:LOG:XMAX?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:LOG:XMAX value`` command.

        SCPI Syntax:
            ```
            - POWer:SOA:LOG:XMAX <NR3>
            - POWer:SOA:LOG:XMAX?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the XMAX value used for log SOA
              calculations.
        """
        return self._xmax

    @property
    def xmin(self) -> PowerSoaLogXmin:
        """Return the ``POWer:SOA:LOG:XMIN`` command.

        Description:
            - This command specifies the user XMIN value for use in Log SOA calculations.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:LOG:XMIN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:LOG:XMIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:LOG:XMIN value`` command.

        SCPI Syntax:
            ```
            - POWer:SOA:LOG:XMIN <NR3>
            - POWer:SOA:LOG:XMIN?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the XMIN value used for log SOA
              calculations.
        """
        return self._xmin

    @property
    def ymax(self) -> PowerSoaLogYmax:
        """Return the ``POWer:SOA:LOG:YMAX`` command.

        Description:
            - This command specifies the user YMAX value for use in Log SOA calculations.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:LOG:YMAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:LOG:YMAX?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:LOG:YMAX value`` command.

        SCPI Syntax:
            ```
            - POWer:SOA:LOG:YMAX <NR3>
            - POWer:SOA:LOG:YMAX?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the YMAX value used for log SOA
              calculations.
        """
        return self._ymax

    @property
    def ymin(self) -> PowerSoaLogYmin:
        """Return the ``POWer:SOA:LOG:YMIN`` command.

        Description:
            - This command specifies the user YMIN value for use in Log SOA calculations.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:LOG:YMIN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:LOG:YMIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:LOG:YMIN value`` command.

        SCPI Syntax:
            ```
            - POWer:SOA:LOG:YMIN <NR3>
            - POWer:SOA:LOG:YMIN?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the YMIN value used for log SOA
              calculations.
        """
        return self._ymin


class PowerSoaLinearYmin(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:LINear:YMIN`` command.

    Description:
        - This command specifies the user YMIN value for use in linear SOA calculations.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:LINear:YMIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:LINear:YMIN?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:LINear:YMIN value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:LINear:YMIN <NR3>
        - POWer:SOA:LINear:YMIN?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the YMIN value used for linear SOA
          calculations.
    """


class PowerSoaLinearYmax(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:LINear:YMAX`` command.

    Description:
        - This command specifies the user YMAX value for use in linear SOA calculations.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:LINear:YMAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:LINear:YMAX?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:LINear:YMAX value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:LINear:YMAX <NR3>
        - POWer:SOA:LINear:YMAX?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the YMAX value used for linear SOA
          calculations.
    """


class PowerSoaLinearXmin(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:LINear:XMIN`` command.

    Description:
        - This command specifies the user XMIN value for use in linear SOA calculations.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:LINear:XMIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:LINear:XMIN?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:LINear:XMIN value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:LINear:XMIN <NR3>
        - POWer:SOA:LINear:XMIN?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the XMIN value used for linear SOA
          calculations.
    """


class PowerSoaLinearXmax(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:SOA:LINear:XMAX`` command.

    Description:
        - This command specifies the user XMAX value for use in linear SOA calculations.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:LINear:XMAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:LINear:XMAX?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:SOA:LINear:XMAX value`` command.

    SCPI Syntax:
        ```
        - POWer:SOA:LINear:XMAX <NR3>
        - POWer:SOA:LINear:XMAX?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the XMAX value used for linear SOA
          calculations.
    """


class PowerSoaLinear(SCPICmdRead):
    """The ``POWer:SOA:LINear`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA:LINear?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA:LINear?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.xmax``: The ``POWer:SOA:LINear:XMAX`` command.
        - ``.xmin``: The ``POWer:SOA:LINear:XMIN`` command.
        - ``.ymax``: The ``POWer:SOA:LINear:YMAX`` command.
        - ``.ymin``: The ``POWer:SOA:LINear:YMIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._xmax = PowerSoaLinearXmax(device, f"{self._cmd_syntax}:XMAX")
        self._xmin = PowerSoaLinearXmin(device, f"{self._cmd_syntax}:XMIN")
        self._ymax = PowerSoaLinearYmax(device, f"{self._cmd_syntax}:YMAX")
        self._ymin = PowerSoaLinearYmin(device, f"{self._cmd_syntax}:YMIN")

    @property
    def xmax(self) -> PowerSoaLinearXmax:
        """Return the ``POWer:SOA:LINear:XMAX`` command.

        Description:
            - This command specifies the user XMAX value for use in linear SOA calculations.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:LINear:XMAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:LINear:XMAX?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:LINear:XMAX value``
              command.

        SCPI Syntax:
            ```
            - POWer:SOA:LINear:XMAX <NR3>
            - POWer:SOA:LINear:XMAX?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the XMAX value used for linear SOA
              calculations.
        """
        return self._xmax

    @property
    def xmin(self) -> PowerSoaLinearXmin:
        """Return the ``POWer:SOA:LINear:XMIN`` command.

        Description:
            - This command specifies the user XMIN value for use in linear SOA calculations.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:LINear:XMIN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:LINear:XMIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:LINear:XMIN value``
              command.

        SCPI Syntax:
            ```
            - POWer:SOA:LINear:XMIN <NR3>
            - POWer:SOA:LINear:XMIN?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the XMIN value used for linear SOA
              calculations.
        """
        return self._xmin

    @property
    def ymax(self) -> PowerSoaLinearYmax:
        """Return the ``POWer:SOA:LINear:YMAX`` command.

        Description:
            - This command specifies the user YMAX value for use in linear SOA calculations.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:LINear:YMAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:LINear:YMAX?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:LINear:YMAX value``
              command.

        SCPI Syntax:
            ```
            - POWer:SOA:LINear:YMAX <NR3>
            - POWer:SOA:LINear:YMAX?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the YMAX value used for linear SOA
              calculations.
        """
        return self._ymax

    @property
    def ymin(self) -> PowerSoaLinearYmin:
        """Return the ``POWer:SOA:LINear:YMIN`` command.

        Description:
            - This command specifies the user YMIN value for use in linear SOA calculations.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:LINear:YMIN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:LINear:YMIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:LINear:YMIN value``
              command.

        SCPI Syntax:
            ```
            - POWer:SOA:LINear:YMIN <NR3>
            - POWer:SOA:LINear:YMIN?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the YMIN value used for linear SOA
              calculations.
        """
        return self._ymin


class PowerSoa(SCPICmdRead):
    """The ``POWer:SOA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:SOA?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:SOA?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.linear``: The ``POWer:SOA:LINear`` command tree.
        - ``.log``: The ``POWer:SOA:LOG`` command tree.
        - ``.mask``: The ``POWer:SOA:MASK`` command tree.
        - ``.plottype``: The ``POWer:SOA:PLOTTYPe`` command.
        - ``.result``: The ``POWer:SOA:RESult`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._linear = PowerSoaLinear(device, f"{self._cmd_syntax}:LINear")
        self._log = PowerSoaLog(device, f"{self._cmd_syntax}:LOG")
        self._mask = PowerSoaMask(device, f"{self._cmd_syntax}:MASK")
        self._plottype = PowerSoaPlottype(device, f"{self._cmd_syntax}:PLOTTYPe")
        self._result = PowerSoaResult(device, f"{self._cmd_syntax}:RESult")

    @property
    def linear(self) -> PowerSoaLinear:
        """Return the ``POWer:SOA:LINear`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:LINear?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:LINear?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.xmax``: The ``POWer:SOA:LINear:XMAX`` command.
            - ``.xmin``: The ``POWer:SOA:LINear:XMIN`` command.
            - ``.ymax``: The ``POWer:SOA:LINear:YMAX`` command.
            - ``.ymin``: The ``POWer:SOA:LINear:YMIN`` command.
        """
        return self._linear

    @property
    def log(self) -> PowerSoaLog:
        """Return the ``POWer:SOA:LOG`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:LOG?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:LOG?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.xmax``: The ``POWer:SOA:LOG:XMAX`` command.
            - ``.xmin``: The ``POWer:SOA:LOG:XMIN`` command.
            - ``.ymax``: The ``POWer:SOA:LOG:YMAX`` command.
            - ``.ymin``: The ``POWer:SOA:LOG:YMIN`` command.
        """
        return self._log

    @property
    def mask(self) -> PowerSoaMask:
        """Return the ``POWer:SOA:MASK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:MASK?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:MASK?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.define``: The ``POWer:SOA:MASK:DEFine`` command.
            - ``.maxamps``: The ``POWer:SOA:MASK:MAXAmps`` command.
            - ``.maxvolts``: The ``POWer:SOA:MASK:MAXVolts`` command.
            - ``.maxwatts``: The ``POWer:SOA:MASK:MAXWatts`` command.
            - ``.nr_pt``: The ``POWer:SOA:MASK:NR_Pt`` command.
            - ``.state``: The ``POWer:SOA:MASK:STATE`` command.
            - ``.stoponviol``: The ``POWer:SOA:MASK:STOPOnviol`` command.
        """
        return self._mask

    @property
    def plottype(self) -> PowerSoaPlottype:
        """Return the ``POWer:SOA:PLOTTYPe`` command.

        Description:
            - This command specifies the Safe Operating Area (SOA) plot type.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:PLOTTYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:PLOTTYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:SOA:PLOTTYPe value`` command.

        SCPI Syntax:
            ```
            - POWer:SOA:PLOTTYPe {LOG|LINear}
            - POWer:SOA:PLOTTYPe?
            ```

        Info:
            - ``LOG`` for logarithmic SOA plot type.
            - ``LINear`` for linear SOA plot type.
        """
        return self._plottype

    @property
    def result(self) -> PowerSoaResult:
        """Return the ``POWer:SOA:RESult`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA:RESult?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA:RESult?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.failures``: The ``POWer:SOA:RESult:FAILures`` command tree.
            - ``.numacq``: The ``POWer:SOA:RESult:NUMACq`` command.
            - ``.state``: The ``POWer:SOA:RESult:STATE`` command.
        """
        return self._result


class PowerRippleSource(SCPICmdWrite):
    """The ``POWer:RIPPle:SOUrce`` command.

    Description:
        - This command specifies the source waveform for ripple tests. The voltage source waveform
          is specified using the ``POWER:VOLTAGESOURCE`` command and the current waveform is
          specified using the ``POWER:CURRENTSOURCE`` command.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:RIPPle:SOUrce value`` command.

    SCPI Syntax:
        ```
        - POWer:RIPPle:SOUrce {VOLTage|CURRent}
        ```

    Info:
        - ``VOLTage`` specifies voltage source waveform for ripple tests.
        - ``CURRent`` specifies current source waveform for ripple tests.
    """


class PowerRippleResultsStddev(SCPICmdRead):
    """The ``POWer:RIPPle:RESults:STDdev`` command.

    Description:
        - Returns the standard deviation of the peak-to-peak ripple measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults:STDdev?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults:STDdev?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:RIPPle:RESults:STDdev?
        ```
    """


class PowerRippleResultsMin(SCPICmdRead):
    """The ``POWer:RIPPle:RESults:MIN`` command.

    Description:
        - Returns the minimum of the peak-to-peak ripple measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults:MIN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults:MIN?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:RIPPle:RESults:MIN?
        ```
    """


class PowerRippleResultsMean(SCPICmdRead):
    """The ``POWer:RIPPle:RESults:MEAN`` command.

    Description:
        - Returns the mean of the peak-to-peak ripple measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults:MEAN?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:RIPPle:RESults:MEAN?
        ```
    """


class PowerRippleResultsMax(SCPICmdRead):
    """The ``POWer:RIPPle:RESults:MAX`` command.

    Description:
        - Returns the maximum of the peak-to-peak ripple measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults:MAX?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:RIPPle:RESults:MAX?
        ```
    """


class PowerRippleResultsAmplitude(SCPICmdRead):
    """The ``POWer:RIPPle:RESults:AMPLitude`` command.

    Description:
        - Returns the peak-to-peak ripple measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults:AMPLitude?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:RIPPle:RESults:AMPLitude?
        ```
    """


class PowerRippleResults(SCPICmdRead):
    """The ``POWer:RIPPle:RESults`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``POWer:RIPPle:RESults:AMPLitude`` command.
        - ``.max``: The ``POWer:RIPPle:RESults:MAX`` command.
        - ``.mean``: The ``POWer:RIPPle:RESults:MEAN`` command.
        - ``.min``: The ``POWer:RIPPle:RESults:MIN`` command.
        - ``.stddev``: The ``POWer:RIPPle:RESults:STDdev`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = PowerRippleResultsAmplitude(device, f"{self._cmd_syntax}:AMPLitude")
        self._max = PowerRippleResultsMax(device, f"{self._cmd_syntax}:MAX")
        self._mean = PowerRippleResultsMean(device, f"{self._cmd_syntax}:MEAN")
        self._min = PowerRippleResultsMin(device, f"{self._cmd_syntax}:MIN")
        self._stddev = PowerRippleResultsStddev(device, f"{self._cmd_syntax}:STDdev")

    @property
    def amplitude(self) -> PowerRippleResultsAmplitude:
        """Return the ``POWer:RIPPle:RESults:AMPLitude`` command.

        Description:
            - Returns the peak-to-peak ripple measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults:AMPLitude?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:RIPPle:RESults:AMPLitude?
            ```
        """
        return self._amplitude

    @property
    def max(self) -> PowerRippleResultsMax:
        """Return the ``POWer:RIPPle:RESults:MAX`` command.

        Description:
            - Returns the maximum of the peak-to-peak ripple measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults:MAX?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:RIPPle:RESults:MAX?
            ```
        """
        return self._max

    @property
    def mean(self) -> PowerRippleResultsMean:
        """Return the ``POWer:RIPPle:RESults:MEAN`` command.

        Description:
            - Returns the mean of the peak-to-peak ripple measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults:MEAN?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:RIPPle:RESults:MEAN?
            ```
        """
        return self._mean

    @property
    def min(self) -> PowerRippleResultsMin:
        """Return the ``POWer:RIPPle:RESults:MIN`` command.

        Description:
            - Returns the minimum of the peak-to-peak ripple measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults:MIN?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults:MIN?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:RIPPle:RESults:MIN?
            ```
        """
        return self._min

    @property
    def stddev(self) -> PowerRippleResultsStddev:
        """Return the ``POWer:RIPPle:RESults:STDdev`` command.

        Description:
            - Returns the standard deviation of the peak-to-peak ripple measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults:STDdev?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults:STDdev?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:RIPPle:RESults:STDdev?
            ```
        """
        return self._stddev


class PowerRipple(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:RIPPle`` command.

    Description:
        - This command performs a vertical autoset for ripple measurements or sets the vertical
          offset to 0.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:RIPPle value`` command.

    SCPI Syntax:
        ```
        - POWer:RIPPle {VERTAUTOset|VERTDEFault}
        ```

    Info:
        - ``VERTAUTOset`` automatically scales the source waveform to optimize ripple measurements.
        - ``VERTDEFault`` sets the vertical offset of the source waveform to 0 volts (for voltage
          source) or 0 amperes (for current source).

    Properties:
        - ``.results``: The ``POWer:RIPPle:RESults`` command tree.
        - ``.source``: The ``POWer:RIPPle:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._results = PowerRippleResults(device, f"{self._cmd_syntax}:RESults")
        self._source = PowerRippleSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def results(self) -> PowerRippleResults:
        """Return the ``POWer:RIPPle:RESults`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:RIPPle:RESults?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:RIPPle:RESults?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``POWer:RIPPle:RESults:AMPLitude`` command.
            - ``.max``: The ``POWer:RIPPle:RESults:MAX`` command.
            - ``.mean``: The ``POWer:RIPPle:RESults:MEAN`` command.
            - ``.min``: The ``POWer:RIPPle:RESults:MIN`` command.
            - ``.stddev``: The ``POWer:RIPPle:RESults:STDdev`` command.
        """
        return self._results

    @property
    def source(self) -> PowerRippleSource:
        """Return the ``POWer:RIPPle:SOUrce`` command.

        Description:
            - This command specifies the source waveform for ripple tests. The voltage source
              waveform is specified using the ``POWER:VOLTAGESOURCE`` command and the current
              waveform is specified using the ``POWER:CURRENTSOURCE`` command.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:RIPPle:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - POWer:RIPPle:SOUrce {VOLTage|CURRent}
            ```

        Info:
            - ``VOLTage`` specifies voltage source waveform for ripple tests.
            - ``CURRent`` specifies current source waveform for ripple tests.
        """
        return self._source


class PowerReflevelPercentMidItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``POWer:REFLevel:PERCent:MID<x>`` command.

    Description:
        - This command specifies one of 3 mid reference percentage levels to be used for power
          measurements. MID1 is used on the user's voltage waveform. MID2 is used on the user's
          current waveform. MID3 is used on the user's gate waveform. (MID3 is specific to power
          applications.)

    Usage:
        - Using the ``.query()`` method will send the ``POWer:REFLevel:PERCent:MID<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:PERCent:MID<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:REFLevel:PERCent:MID<x> value``
          command.

    SCPI Syntax:
        ```
        - POWer:REFLevel:PERCent:MID<x> <NR3>; Ranges={D,0.0,100.0}
        - POWer:REFLevel:PERCent:MID<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the mid value in percentage.
    """


class PowerReflevelPercentLow(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:REFLevel:PERCent:LOW`` command.

    Description:
        - This command specifies the low reference percent level to be used for power measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:REFLevel:PERCent:LOW?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:PERCent:LOW?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:REFLevel:PERCent:LOW value``
          command.

    SCPI Syntax:
        ```
        - POWer:REFLevel:PERCent:LOW <NR3>; Ranges={D,0.0,100.0}
        - POWer:REFLevel:PERCent:LOW?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the low value in percentage.
    """


class PowerReflevelPercentHigh(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:REFLevel:PERCent:HIGH`` command.

    Description:
        - This command specifies the top reference percent level to be used for power measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:REFLevel:PERCent:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:PERCent:HIGH?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:REFLevel:PERCent:HIGH value``
          command.

    SCPI Syntax:
        ```
        - POWer:REFLevel:PERCent:HIGH <NR3>; Ranges={D,0.0,100.0}
        - POWer:REFLevel:PERCent:HIGH?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the high value in percent.
    """


class PowerReflevelPercent(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:REFLevel:PERCent`` command.

    Description:
        - This command sets the reference levels to be used for power measurements to the default
          percentage values.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:REFLevel:PERCent value`` command.

    SCPI Syntax:
        ```
        - POWer:REFLevel:PERCent <SETTODEFaults>
        ```

    Info:
        - ``SETTODEFaults`` sets the reference levels to their default percentage values.

    Properties:
        - ``.high``: The ``POWer:REFLevel:PERCent:HIGH`` command.
        - ``.low``: The ``POWer:REFLevel:PERCent:LOW`` command.
        - ``.mid``: The ``POWer:REFLevel:PERCent:MID<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = PowerReflevelPercentHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = PowerReflevelPercentLow(device, f"{self._cmd_syntax}:LOW")
        self._mid: Dict[int, PowerReflevelPercentMidItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerReflevelPercentMidItem(device, f"{self._cmd_syntax}:MID{x}")
        )

    @property
    def high(self) -> PowerReflevelPercentHigh:
        """Return the ``POWer:REFLevel:PERCent:HIGH`` command.

        Description:
            - This command specifies the top reference percent level to be used for power
              measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:REFLevel:PERCent:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:PERCent:HIGH?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:REFLevel:PERCent:HIGH value``
              command.

        SCPI Syntax:
            ```
            - POWer:REFLevel:PERCent:HIGH <NR3>; Ranges={D,0.0,100.0}
            - POWer:REFLevel:PERCent:HIGH?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the high value in percent.
        """
        return self._high

    @property
    def low(self) -> PowerReflevelPercentLow:
        """Return the ``POWer:REFLevel:PERCent:LOW`` command.

        Description:
            - This command specifies the low reference percent level to be used for power
              measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:REFLevel:PERCent:LOW?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:PERCent:LOW?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:REFLevel:PERCent:LOW value``
              command.

        SCPI Syntax:
            ```
            - POWer:REFLevel:PERCent:LOW <NR3>; Ranges={D,0.0,100.0}
            - POWer:REFLevel:PERCent:LOW?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the low value in percentage.
        """
        return self._low

    @property
    def mid(self) -> Dict[int, PowerReflevelPercentMidItem]:
        """Return the ``POWer:REFLevel:PERCent:MID<x>`` command.

        Description:
            - This command specifies one of 3 mid reference percentage levels to be used for power
              measurements. MID1 is used on the user's voltage waveform. MID2 is used on the user's
              current waveform. MID3 is used on the user's gate waveform. (MID3 is specific to power
              applications.)

        Usage:
            - Using the ``.query()`` method will send the ``POWer:REFLevel:PERCent:MID<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:PERCent:MID<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:REFLevel:PERCent:MID<x> value`` command.

        SCPI Syntax:
            ```
            - POWer:REFLevel:PERCent:MID<x> <NR3>; Ranges={D,0.0,100.0}
            - POWer:REFLevel:PERCent:MID<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the mid value in percentage.
        """
        return self._mid


class PowerReflevelMethod(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:REFLevel:METHod`` command.

    Description:
        - This command specifies the method used to calculate the 0% and 100% reference level to be
          used for power measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:REFLevel:METHod?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:METHod?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:REFLevel:METHod value`` command.

    SCPI Syntax:
        ```
        - POWer:REFLevel:METHod {ABSolute|PERCent}
        - POWer:REFLevel:METHod?
        ```

    Info:
        - ``ABSolute`` specifies that the reference levels are set explicitly using the
          ``MEASUrement:REFLevel:ABSolute`` commands. This method is useful when precise values are
          required.
        - ``PERCent`` specifies that the reference levels are calculated as a percent of the signal
          amplitude. The percentages are defined using the ``MEASUrement:REFLevel:PERCent``
          commands.
    """


class PowerReflevelHysteresis(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:REFLevel:HYSTeresis`` command.

    Description:
        - This command specifies the reference level hysteresis value to be used for power
          measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:REFLevel:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:HYSTeresis?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:REFLevel:HYSTeresis value``
          command.

    SCPI Syntax:
        ```
        - POWer:REFLevel:HYSTeresis <NR3>
        - POWer:REFLevel:HYSTeresis?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the hysteresis value.
    """


class PowerReflevelAbsoluteMidItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``POWer:REFLevel:ABSolute:MID<x>`` command.

    Description:
        - This command specifies the mid reference level to be used for power measurements. MID1 is
          used on the user's voltage waveform. MID2 is used on the user's current waveform. MID3 is
          used on the user's gate waveform. (MID3 is specific to the power application.)

    Usage:
        - Using the ``.query()`` method will send the ``POWer:REFLevel:ABSolute:MID<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:ABSolute:MID<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:REFLevel:ABSolute:MID<x> value``
          command.

    SCPI Syntax:
        ```
        - POWer:REFLevel:ABSolute:MID<x> <NR3>; Ranges={D,-1e6,+1E6}
        - POWer:REFLevel:ABSolute:MID<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the absolute mid reference value.
    """


class PowerReflevelAbsoluteLow(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:REFLevel:ABSolute:LOW`` command.

    Description:
        - This command specifies the low reference level to be used for power measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:REFLevel:ABSolute:LOW?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:ABSolute:LOW?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:REFLevel:ABSolute:LOW value``
          command.

    SCPI Syntax:
        ```
        - POWer:REFLevel:ABSolute:LOW <NR3>; Ranges={D,-1e6,+1E6}
        - POWer:REFLevel:ABSolute:LOW?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the absolute low value in volts.
          Default value is 0.0E+0.
    """


class PowerReflevelAbsoluteHigh(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:REFLevel:ABSolute:HIGH`` command.

    Description:
        - This command specifies the top reference level to be used for power measurements.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:REFLevel:ABSolute:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:ABSolute:HIGH?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:REFLevel:ABSolute:HIGH value``
          command.

    SCPI Syntax:
        ```
        - POWer:REFLevel:ABSolute:HIGH <NR3>; Ranges={D,-1e6,+1E6}
        - POWer:REFLevel:ABSolute:HIGH?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the absolute high value in volts.
          Default value is 0.0E+0.
    """


class PowerReflevelAbsolute(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:REFLevel:ABSolute`` command.

    Description:
        - This command sets the reference levels to be used for power measurements their default
          unit values.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:REFLevel:ABSolute value``
          command.

    SCPI Syntax:
        ```
        - POWer:REFLevel:ABSolute {SETTODEFaults}
        ```

    Info:
        - ``SETTODEFaults`` sets the reference levels to their default values.

    Properties:
        - ``.high``: The ``POWer:REFLevel:ABSolute:HIGH`` command.
        - ``.low``: The ``POWer:REFLevel:ABSolute:LOW`` command.
        - ``.mid``: The ``POWer:REFLevel:ABSolute:MID<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = PowerReflevelAbsoluteHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = PowerReflevelAbsoluteLow(device, f"{self._cmd_syntax}:LOW")
        self._mid: Dict[int, PowerReflevelAbsoluteMidItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerReflevelAbsoluteMidItem(device, f"{self._cmd_syntax}:MID{x}")
        )

    @property
    def high(self) -> PowerReflevelAbsoluteHigh:
        """Return the ``POWer:REFLevel:ABSolute:HIGH`` command.

        Description:
            - This command specifies the top reference level to be used for power measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:REFLevel:ABSolute:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:ABSolute:HIGH?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:REFLevel:ABSolute:HIGH value`` command.

        SCPI Syntax:
            ```
            - POWer:REFLevel:ABSolute:HIGH <NR3>; Ranges={D,-1e6,+1E6}
            - POWer:REFLevel:ABSolute:HIGH?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the absolute high value in volts.
              Default value is 0.0E+0.
        """
        return self._high

    @property
    def low(self) -> PowerReflevelAbsoluteLow:
        """Return the ``POWer:REFLevel:ABSolute:LOW`` command.

        Description:
            - This command specifies the low reference level to be used for power measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:REFLevel:ABSolute:LOW?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:ABSolute:LOW?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:REFLevel:ABSolute:LOW value``
              command.

        SCPI Syntax:
            ```
            - POWer:REFLevel:ABSolute:LOW <NR3>; Ranges={D,-1e6,+1E6}
            - POWer:REFLevel:ABSolute:LOW?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the absolute low value in volts.
              Default value is 0.0E+0.
        """
        return self._low

    @property
    def mid(self) -> Dict[int, PowerReflevelAbsoluteMidItem]:
        """Return the ``POWer:REFLevel:ABSolute:MID<x>`` command.

        Description:
            - This command specifies the mid reference level to be used for power measurements. MID1
              is used on the user's voltage waveform. MID2 is used on the user's current waveform.
              MID3 is used on the user's gate waveform. (MID3 is specific to the power application.)

        Usage:
            - Using the ``.query()`` method will send the ``POWer:REFLevel:ABSolute:MID<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:ABSolute:MID<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:REFLevel:ABSolute:MID<x> value`` command.

        SCPI Syntax:
            ```
            - POWer:REFLevel:ABSolute:MID<x> <NR3>; Ranges={D,-1e6,+1E6}
            - POWer:REFLevel:ABSolute:MID<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the absolute mid reference value.
        """
        return self._mid


class PowerReflevel(SCPICmdRead):
    """The ``POWer:REFLevel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:REFLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:REFLevel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absolute``: The ``POWer:REFLevel:ABSolute`` command.
        - ``.hysteresis``: The ``POWer:REFLevel:HYSTeresis`` command.
        - ``.method``: The ``POWer:REFLevel:METHod`` command.
        - ``.percent``: The ``POWer:REFLevel:PERCent`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = PowerReflevelAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._hysteresis = PowerReflevelHysteresis(device, f"{self._cmd_syntax}:HYSTeresis")
        self._method = PowerReflevelMethod(device, f"{self._cmd_syntax}:METHod")
        self._percent = PowerReflevelPercent(device, f"{self._cmd_syntax}:PERCent")

    @property
    def absolute(self) -> PowerReflevelAbsolute:
        """Return the ``POWer:REFLevel:ABSolute`` command.

        Description:
            - This command sets the reference levels to be used for power measurements their default
              unit values.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:REFLevel:ABSolute value``
              command.

        SCPI Syntax:
            ```
            - POWer:REFLevel:ABSolute {SETTODEFaults}
            ```

        Info:
            - ``SETTODEFaults`` sets the reference levels to their default values.

        Sub-properties:
            - ``.high``: The ``POWer:REFLevel:ABSolute:HIGH`` command.
            - ``.low``: The ``POWer:REFLevel:ABSolute:LOW`` command.
            - ``.mid``: The ``POWer:REFLevel:ABSolute:MID<x>`` command.
        """
        return self._absolute

    @property
    def hysteresis(self) -> PowerReflevelHysteresis:
        """Return the ``POWer:REFLevel:HYSTeresis`` command.

        Description:
            - This command specifies the reference level hysteresis value to be used for power
              measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:REFLevel:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:HYSTeresis?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:REFLevel:HYSTeresis value``
              command.

        SCPI Syntax:
            ```
            - POWer:REFLevel:HYSTeresis <NR3>
            - POWer:REFLevel:HYSTeresis?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the hysteresis value.
        """
        return self._hysteresis

    @property
    def method(self) -> PowerReflevelMethod:
        """Return the ``POWer:REFLevel:METHod`` command.

        Description:
            - This command specifies the method used to calculate the 0% and 100% reference level to
              be used for power measurements.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:REFLevel:METHod?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:REFLevel:METHod?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:REFLevel:METHod value``
              command.

        SCPI Syntax:
            ```
            - POWer:REFLevel:METHod {ABSolute|PERCent}
            - POWer:REFLevel:METHod?
            ```

        Info:
            - ``ABSolute`` specifies that the reference levels are set explicitly using the
              ``MEASUrement:REFLevel:ABSolute`` commands. This method is useful when precise values
              are required.
            - ``PERCent`` specifies that the reference levels are calculated as a percent of the
              signal amplitude. The percentages are defined using the
              ``MEASUrement:REFLevel:PERCent`` commands.
        """
        return self._method

    @property
    def percent(self) -> PowerReflevelPercent:
        """Return the ``POWer:REFLevel:PERCent`` command.

        Description:
            - This command sets the reference levels to be used for power measurements to the
              default percentage values.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:REFLevel:PERCent value``
              command.

        SCPI Syntax:
            ```
            - POWer:REFLevel:PERCent <SETTODEFaults>
            ```

        Info:
            - ``SETTODEFaults`` sets the reference levels to their default percentage values.

        Sub-properties:
            - ``.high``: The ``POWer:REFLevel:PERCent:HIGH`` command.
            - ``.low``: The ``POWer:REFLevel:PERCent:LOW`` command.
            - ``.mid``: The ``POWer:REFLevel:PERCent:MID<x>`` command.
        """
        return self._percent


class PowerQualityVrms(SCPICmdRead):
    """The ``POWer:QUALity:VRMS`` command.

    Description:
        - Returns the RMS voltage measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:VRMS?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:VRMS?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:QUALity:VRMS?
        ```
    """


class PowerQualityVcrestfactor(SCPICmdRead):
    """The ``POWer:QUALity:VCRESTfactor`` command.

    Description:
        - This query returns the measurement for the voltage crest factor.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:VCRESTfactor?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:VCRESTfactor?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:QUALity:VCRESTfactor?
        ```
    """


class PowerQualityTruepwr(SCPICmdRead):
    """The ``POWer:QUALity:TRUEpwr`` command.

    Description:
        - Returns the true power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:TRUEpwr?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:TRUEpwr?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:QUALity:TRUEpwr?
        ```
    """


class PowerQualityReactpwr(SCPICmdRead):
    """The ``POWer:QUALity:REACTpwr`` command.

    Description:
        - Returns the reactive power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:REACTpwr?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:REACTpwr?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:QUALity:REACTpwr?
        ```
    """


class PowerQualityPowerfactor(SCPICmdRead):
    """The ``POWer:QUALity:POWERFACtor`` command.

    Description:
        - Returns the power factor measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:POWERFACtor?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:POWERFACtor?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:QUALity:POWERFACtor?
        ```
    """


class PowerQualityPhaseangle(SCPICmdRead):
    """The ``POWer:QUALity:PHASEangle`` command.

    Description:
        - Returns the phase angle measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:PHASEangle?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:PHASEangle?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:QUALity:PHASEangle?
        ```
    """


class PowerQualityIrms(SCPICmdRead):
    """The ``POWer:QUALity:IRMS`` command.

    Description:
        - Returns the RMS current measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:IRMS?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:IRMS?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:QUALity:IRMS?
        ```
    """


class PowerQualityIcrestfactor(SCPICmdRead):
    """The ``POWer:QUALity:ICRESTfactor`` command.

    Description:
        - Returns the current crest factor measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:ICRESTfactor?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:ICRESTfactor?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:QUALity:ICRESTfactor?
        ```
    """


class PowerQualityFrequency(SCPICmdRead):
    """The ``POWer:QUALity:FREQuency`` command.

    Description:
        - Returns the frequency measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:FREQuency?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:QUALity:FREQuency?
        ```
    """


class PowerQualityFreqreference(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:QUALity:FREQREFerence`` command.

    Description:
        - This command specifies the power quality frequency reference.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:FREQREFerence?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:FREQREFerence?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:QUALity:FREQREFerence value``
          command.

    SCPI Syntax:
        ```
        - POWer:QUALity:FREQREFerence {VOLTage|CURRent}
        - POWer:QUALity:FREQREFerence?
        ```

    Info:
        - ``VOLTage`` sets voltage as the power quality frequency reference source.
        - ``CURRent`` sets current as the power quality frequency reference source.
    """


class PowerQualityDisplayVrms(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:QUALity:DISplay:VRMS`` command.

    Description:
        - This command specifies the display state for the rms voltage readout.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:VRMS?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:VRMS?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:QUALity:DISplay:VRMS value``
          command.

    SCPI Syntax:
        ```
        - POWer:QUALity:DISplay:VRMS {OFF|ON|0|1}
        - POWer:QUALity:DISplay:VRMS?
        ```

    Info:
        - ``OFF`` or 0 turns off the rms voltage display.
        - ``ON`` or 1 turns on the rms voltage display.
    """


class PowerQualityDisplayVcrestfactor(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:QUALity:DISplay:VCRESTfactor`` command.

    Description:
        - This command specifies the display state for the voltage crest factor readout.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:VCRESTfactor?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:VCRESTfactor?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:QUALity:DISplay:VCRESTfactor value`` command.

    SCPI Syntax:
        ```
        - POWer:QUALity:DISplay:VCRESTfactor {OFF|ON|0|1}
        - POWer:QUALity:DISplay:VCRESTfactor?
        ```

    Info:
        - ``OFF`` or 0 turns off the voltage crest factor display.
        - ``ON`` or 1 turns on the voltage crest factor display.
    """


class PowerQualityDisplayTruepwr(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:QUALity:DISplay:TRUEpwr`` command.

    Description:
        - This command specifies the display state for the true power readout.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:TRUEpwr?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:TRUEpwr?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:QUALity:DISplay:TRUEpwr value``
          command.

    SCPI Syntax:
        ```
        - POWer:QUALity:DISplay:TRUEpwr {OFF|ON|0|1}
        - POWer:QUALity:DISplay:TRUEpwr?
        ```

    Info:
        - ``OFF`` or 0 turns off the true power display.
        - ``ON`` or 1 turns on the true power display.
    """


class PowerQualityDisplayReactpwr(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:QUALity:DISplay:REACTpwr`` command.

    Description:
        - This command specifies the display state for the reactor power readout.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:REACTpwr?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:REACTpwr?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:QUALity:DISplay:REACTpwr value``
          command.

    SCPI Syntax:
        ```
        - POWer:QUALity:DISplay:REACTpwr {OFF|ON|0|1}
        - POWer:QUALity:DISplay:REACTpwr?
        ```

    Info:
        - ``OFF`` or 0 turns off the reactor power display.
        - ``ON`` or 1 turns on the reactor power display.
    """


class PowerQualityDisplayPowerfactor(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:QUALity:DISplay:POWERFACtor`` command.

    Description:
        - This command specifies the display state for the power factor readout.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:POWERFACtor?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:POWERFACtor?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:QUALity:DISplay:POWERFACtor value`` command.

    SCPI Syntax:
        ```
        - POWer:QUALity:DISplay:POWERFACtor {OFF|ON|0|1}
        - POWer:QUALity:DISplay:POWERFACtor?
        ```

    Info:
        - ``OFF`` or 0 turns off the power factor display.
        - ``ON`` or 1 turns on the power factor display.
    """


class PowerQualityDisplayPhaseangle(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:QUALity:DISplay:PHASEangle`` command.

    Description:
        - This command specifies the display state for the phase angle readout.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:PHASEangle?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:PHASEangle?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:QUALity:DISplay:PHASEangle value`` command.

    SCPI Syntax:
        ```
        - POWer:QUALity:DISplay:PHASEangle {OFF|ON|0|1}
        - POWer:QUALity:DISplay:PHASEangle?
        ```

    Info:
        - ``OFF`` or 0 turns off the phase angle display.
        - ``ON`` or 1 turns on the phase angle display.
    """


class PowerQualityDisplayIrms(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:QUALity:DISplay:IRMS`` command.

    Description:
        - This command specifies the display state for the rms current readout.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:IRMS?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:IRMS?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:QUALity:DISplay:IRMS value``
          command.

    SCPI Syntax:
        ```
        - POWer:QUALity:DISplay:IRMS {OFF|ON|0|1}
        - POWer:QUALity:DISplay:IRMS?
        ```

    Info:
        - ``OFF`` or 0 turns off the rms current display.
        - ``ON`` or 1 turns on the rms current display.
    """


class PowerQualityDisplayIcrestfactor(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:QUALity:DISplay:ICRESTfactor`` command.

    Description:
        - This command specifies the display state for the current crest factor readout.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:ICRESTfactor?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:ICRESTfactor?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:QUALity:DISplay:ICRESTfactor value`` command.

    SCPI Syntax:
        ```
        - POWer:QUALity:DISplay:ICRESTfactor {OFF|ON|0|1}
        - POWer:QUALity:DISplay:ICRESTfactor?
        ```

    Info:
        - ``OFF`` or 0 turns off the current crest factor display.
        - ``ON`` or 1 turns on the current crest factor display.
    """


class PowerQualityDisplayFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:QUALity:DISplay:FREQuency`` command.

    Description:
        - This command specifies the display state for the frequency readout.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:FREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:QUALity:DISplay:FREQuency value``
          command.

    SCPI Syntax:
        ```
        - POWer:QUALity:DISplay:FREQuency {OFF|ON|0|1}
        - POWer:QUALity:DISplay:FREQuency?
        ```

    Info:
        - ``OFF`` or 0 turns off the frequency display.
        - ``ON`` or 1 turns on the frequency display.
    """


class PowerQualityDisplayApppwr(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:QUALity:DISplay:APPpwr`` command.

    Description:
        - This command specifies the display state for the apparent power readout.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:APPpwr?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:APPpwr?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:QUALity:DISplay:APPpwr value``
          command.

    SCPI Syntax:
        ```
        - POWer:QUALity:DISplay:APPpwr {OFF|ON|0|1}
        - POWer:QUALity:DISplay:APPpwr?
        ```

    Info:
        - ``OFF`` or 0 turns off the apparent power display.
        - ``ON`` or 1 turns on the apparent power display.
    """


#  pylint: disable=too-many-instance-attributes
class PowerQualityDisplay(SCPICmdRead):
    """The ``POWer:QUALity:DISplay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.apppwr``: The ``POWer:QUALity:DISplay:APPpwr`` command.
        - ``.frequency``: The ``POWer:QUALity:DISplay:FREQuency`` command.
        - ``.icrestfactor``: The ``POWer:QUALity:DISplay:ICRESTfactor`` command.
        - ``.irms``: The ``POWer:QUALity:DISplay:IRMS`` command.
        - ``.phaseangle``: The ``POWer:QUALity:DISplay:PHASEangle`` command.
        - ``.powerfactor``: The ``POWer:QUALity:DISplay:POWERFACtor`` command.
        - ``.reactpwr``: The ``POWer:QUALity:DISplay:REACTpwr`` command.
        - ``.truepwr``: The ``POWer:QUALity:DISplay:TRUEpwr`` command.
        - ``.vcrestfactor``: The ``POWer:QUALity:DISplay:VCRESTfactor`` command.
        - ``.vrms``: The ``POWer:QUALity:DISplay:VRMS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._apppwr = PowerQualityDisplayApppwr(device, f"{self._cmd_syntax}:APPpwr")
        self._frequency = PowerQualityDisplayFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._icrestfactor = PowerQualityDisplayIcrestfactor(
            device, f"{self._cmd_syntax}:ICRESTfactor"
        )
        self._irms = PowerQualityDisplayIrms(device, f"{self._cmd_syntax}:IRMS")
        self._phaseangle = PowerQualityDisplayPhaseangle(device, f"{self._cmd_syntax}:PHASEangle")
        self._powerfactor = PowerQualityDisplayPowerfactor(
            device, f"{self._cmd_syntax}:POWERFACtor"
        )
        self._reactpwr = PowerQualityDisplayReactpwr(device, f"{self._cmd_syntax}:REACTpwr")
        self._truepwr = PowerQualityDisplayTruepwr(device, f"{self._cmd_syntax}:TRUEpwr")
        self._vcrestfactor = PowerQualityDisplayVcrestfactor(
            device, f"{self._cmd_syntax}:VCRESTfactor"
        )
        self._vrms = PowerQualityDisplayVrms(device, f"{self._cmd_syntax}:VRMS")

    @property
    def apppwr(self) -> PowerQualityDisplayApppwr:
        """Return the ``POWer:QUALity:DISplay:APPpwr`` command.

        Description:
            - This command specifies the display state for the apparent power readout.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:APPpwr?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:APPpwr?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:QUALity:DISplay:APPpwr value`` command.

        SCPI Syntax:
            ```
            - POWer:QUALity:DISplay:APPpwr {OFF|ON|0|1}
            - POWer:QUALity:DISplay:APPpwr?
            ```

        Info:
            - ``OFF`` or 0 turns off the apparent power display.
            - ``ON`` or 1 turns on the apparent power display.
        """
        return self._apppwr

    @property
    def frequency(self) -> PowerQualityDisplayFrequency:
        """Return the ``POWer:QUALity:DISplay:FREQuency`` command.

        Description:
            - This command specifies the display state for the frequency readout.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:FREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:FREQuency?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:QUALity:DISplay:FREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:QUALity:DISplay:FREQuency {OFF|ON|0|1}
            - POWer:QUALity:DISplay:FREQuency?
            ```

        Info:
            - ``OFF`` or 0 turns off the frequency display.
            - ``ON`` or 1 turns on the frequency display.
        """
        return self._frequency

    @property
    def icrestfactor(self) -> PowerQualityDisplayIcrestfactor:
        """Return the ``POWer:QUALity:DISplay:ICRESTfactor`` command.

        Description:
            - This command specifies the display state for the current crest factor readout.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:ICRESTfactor?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:QUALity:DISplay:ICRESTfactor?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:QUALity:DISplay:ICRESTfactor value`` command.

        SCPI Syntax:
            ```
            - POWer:QUALity:DISplay:ICRESTfactor {OFF|ON|0|1}
            - POWer:QUALity:DISplay:ICRESTfactor?
            ```

        Info:
            - ``OFF`` or 0 turns off the current crest factor display.
            - ``ON`` or 1 turns on the current crest factor display.
        """
        return self._icrestfactor

    @property
    def irms(self) -> PowerQualityDisplayIrms:
        """Return the ``POWer:QUALity:DISplay:IRMS`` command.

        Description:
            - This command specifies the display state for the rms current readout.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:IRMS?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:IRMS?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:QUALity:DISplay:IRMS value``
              command.

        SCPI Syntax:
            ```
            - POWer:QUALity:DISplay:IRMS {OFF|ON|0|1}
            - POWer:QUALity:DISplay:IRMS?
            ```

        Info:
            - ``OFF`` or 0 turns off the rms current display.
            - ``ON`` or 1 turns on the rms current display.
        """
        return self._irms

    @property
    def phaseangle(self) -> PowerQualityDisplayPhaseangle:
        """Return the ``POWer:QUALity:DISplay:PHASEangle`` command.

        Description:
            - This command specifies the display state for the phase angle readout.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:PHASEangle?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:QUALity:DISplay:PHASEangle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:QUALity:DISplay:PHASEangle value`` command.

        SCPI Syntax:
            ```
            - POWer:QUALity:DISplay:PHASEangle {OFF|ON|0|1}
            - POWer:QUALity:DISplay:PHASEangle?
            ```

        Info:
            - ``OFF`` or 0 turns off the phase angle display.
            - ``ON`` or 1 turns on the phase angle display.
        """
        return self._phaseangle

    @property
    def powerfactor(self) -> PowerQualityDisplayPowerfactor:
        """Return the ``POWer:QUALity:DISplay:POWERFACtor`` command.

        Description:
            - This command specifies the display state for the power factor readout.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:POWERFACtor?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:QUALity:DISplay:POWERFACtor?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:QUALity:DISplay:POWERFACtor value`` command.

        SCPI Syntax:
            ```
            - POWer:QUALity:DISplay:POWERFACtor {OFF|ON|0|1}
            - POWer:QUALity:DISplay:POWERFACtor?
            ```

        Info:
            - ``OFF`` or 0 turns off the power factor display.
            - ``ON`` or 1 turns on the power factor display.
        """
        return self._powerfactor

    @property
    def reactpwr(self) -> PowerQualityDisplayReactpwr:
        """Return the ``POWer:QUALity:DISplay:REACTpwr`` command.

        Description:
            - This command specifies the display state for the reactor power readout.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:REACTpwr?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:REACTpwr?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:QUALity:DISplay:REACTpwr value`` command.

        SCPI Syntax:
            ```
            - POWer:QUALity:DISplay:REACTpwr {OFF|ON|0|1}
            - POWer:QUALity:DISplay:REACTpwr?
            ```

        Info:
            - ``OFF`` or 0 turns off the reactor power display.
            - ``ON`` or 1 turns on the reactor power display.
        """
        return self._reactpwr

    @property
    def truepwr(self) -> PowerQualityDisplayTruepwr:
        """Return the ``POWer:QUALity:DISplay:TRUEpwr`` command.

        Description:
            - This command specifies the display state for the true power readout.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:TRUEpwr?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:TRUEpwr?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:QUALity:DISplay:TRUEpwr value`` command.

        SCPI Syntax:
            ```
            - POWer:QUALity:DISplay:TRUEpwr {OFF|ON|0|1}
            - POWer:QUALity:DISplay:TRUEpwr?
            ```

        Info:
            - ``OFF`` or 0 turns off the true power display.
            - ``ON`` or 1 turns on the true power display.
        """
        return self._truepwr

    @property
    def vcrestfactor(self) -> PowerQualityDisplayVcrestfactor:
        """Return the ``POWer:QUALity:DISplay:VCRESTfactor`` command.

        Description:
            - This command specifies the display state for the voltage crest factor readout.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:VCRESTfactor?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:QUALity:DISplay:VCRESTfactor?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:QUALity:DISplay:VCRESTfactor value`` command.

        SCPI Syntax:
            ```
            - POWer:QUALity:DISplay:VCRESTfactor {OFF|ON|0|1}
            - POWer:QUALity:DISplay:VCRESTfactor?
            ```

        Info:
            - ``OFF`` or 0 turns off the voltage crest factor display.
            - ``ON`` or 1 turns on the voltage crest factor display.
        """
        return self._vcrestfactor

    @property
    def vrms(self) -> PowerQualityDisplayVrms:
        """Return the ``POWer:QUALity:DISplay:VRMS`` command.

        Description:
            - This command specifies the display state for the rms voltage readout.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay:VRMS?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay:VRMS?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:QUALity:DISplay:VRMS value``
              command.

        SCPI Syntax:
            ```
            - POWer:QUALity:DISplay:VRMS {OFF|ON|0|1}
            - POWer:QUALity:DISplay:VRMS?
            ```

        Info:
            - ``OFF`` or 0 turns off the rms voltage display.
            - ``ON`` or 1 turns on the rms voltage display.
        """
        return self._vrms


class PowerQualityApppwr(SCPICmdRead):
    """The ``POWer:QUALity:APPpwr`` command.

    Description:
        - Returns the apparent power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity:APPpwr?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity:APPpwr?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:QUALity:APPpwr?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class PowerQuality(SCPICmdRead):
    """The ``POWer:QUALity`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:QUALity?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:QUALity?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.apppwr``: The ``POWer:QUALity:APPpwr`` command.
        - ``.display``: The ``POWer:QUALity:DISplay`` command tree.
        - ``.freqreference``: The ``POWer:QUALity:FREQREFerence`` command.
        - ``.frequency``: The ``POWer:QUALity:FREQuency`` command.
        - ``.icrestfactor``: The ``POWer:QUALity:ICRESTfactor`` command.
        - ``.irms``: The ``POWer:QUALity:IRMS`` command.
        - ``.phaseangle``: The ``POWer:QUALity:PHASEangle`` command.
        - ``.powerfactor``: The ``POWer:QUALity:POWERFACtor`` command.
        - ``.reactpwr``: The ``POWer:QUALity:REACTpwr`` command.
        - ``.truepwr``: The ``POWer:QUALity:TRUEpwr`` command.
        - ``.vcrestfactor``: The ``POWer:QUALity:VCRESTfactor`` command.
        - ``.vrms``: The ``POWer:QUALity:VRMS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._apppwr = PowerQualityApppwr(device, f"{self._cmd_syntax}:APPpwr")
        self._display = PowerQualityDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._freqreference = PowerQualityFreqreference(device, f"{self._cmd_syntax}:FREQREFerence")
        self._frequency = PowerQualityFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._icrestfactor = PowerQualityIcrestfactor(device, f"{self._cmd_syntax}:ICRESTfactor")
        self._irms = PowerQualityIrms(device, f"{self._cmd_syntax}:IRMS")
        self._phaseangle = PowerQualityPhaseangle(device, f"{self._cmd_syntax}:PHASEangle")
        self._powerfactor = PowerQualityPowerfactor(device, f"{self._cmd_syntax}:POWERFACtor")
        self._reactpwr = PowerQualityReactpwr(device, f"{self._cmd_syntax}:REACTpwr")
        self._truepwr = PowerQualityTruepwr(device, f"{self._cmd_syntax}:TRUEpwr")
        self._vcrestfactor = PowerQualityVcrestfactor(device, f"{self._cmd_syntax}:VCRESTfactor")
        self._vrms = PowerQualityVrms(device, f"{self._cmd_syntax}:VRMS")

    @property
    def apppwr(self) -> PowerQualityApppwr:
        """Return the ``POWer:QUALity:APPpwr`` command.

        Description:
            - Returns the apparent power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:APPpwr?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:APPpwr?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:QUALity:APPpwr?
            ```
        """
        return self._apppwr

    @property
    def display(self) -> PowerQualityDisplay:
        """Return the ``POWer:QUALity:DISplay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:DISplay?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.apppwr``: The ``POWer:QUALity:DISplay:APPpwr`` command.
            - ``.frequency``: The ``POWer:QUALity:DISplay:FREQuency`` command.
            - ``.icrestfactor``: The ``POWer:QUALity:DISplay:ICRESTfactor`` command.
            - ``.irms``: The ``POWer:QUALity:DISplay:IRMS`` command.
            - ``.phaseangle``: The ``POWer:QUALity:DISplay:PHASEangle`` command.
            - ``.powerfactor``: The ``POWer:QUALity:DISplay:POWERFACtor`` command.
            - ``.reactpwr``: The ``POWer:QUALity:DISplay:REACTpwr`` command.
            - ``.truepwr``: The ``POWer:QUALity:DISplay:TRUEpwr`` command.
            - ``.vcrestfactor``: The ``POWer:QUALity:DISplay:VCRESTfactor`` command.
            - ``.vrms``: The ``POWer:QUALity:DISplay:VRMS`` command.
        """
        return self._display

    @property
    def freqreference(self) -> PowerQualityFreqreference:
        """Return the ``POWer:QUALity:FREQREFerence`` command.

        Description:
            - This command specifies the power quality frequency reference.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:FREQREFerence?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:FREQREFerence?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:QUALity:FREQREFerence value``
              command.

        SCPI Syntax:
            ```
            - POWer:QUALity:FREQREFerence {VOLTage|CURRent}
            - POWer:QUALity:FREQREFerence?
            ```

        Info:
            - ``VOLTage`` sets voltage as the power quality frequency reference source.
            - ``CURRent`` sets current as the power quality frequency reference source.
        """
        return self._freqreference

    @property
    def frequency(self) -> PowerQualityFrequency:
        """Return the ``POWer:QUALity:FREQuency`` command.

        Description:
            - Returns the frequency measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:FREQuency?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:QUALity:FREQuency?
            ```
        """
        return self._frequency

    @property
    def icrestfactor(self) -> PowerQualityIcrestfactor:
        """Return the ``POWer:QUALity:ICRESTfactor`` command.

        Description:
            - Returns the current crest factor measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:ICRESTfactor?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:ICRESTfactor?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:QUALity:ICRESTfactor?
            ```
        """
        return self._icrestfactor

    @property
    def irms(self) -> PowerQualityIrms:
        """Return the ``POWer:QUALity:IRMS`` command.

        Description:
            - Returns the RMS current measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:IRMS?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:IRMS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:QUALity:IRMS?
            ```
        """
        return self._irms

    @property
    def phaseangle(self) -> PowerQualityPhaseangle:
        """Return the ``POWer:QUALity:PHASEangle`` command.

        Description:
            - Returns the phase angle measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:PHASEangle?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:PHASEangle?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:QUALity:PHASEangle?
            ```
        """
        return self._phaseangle

    @property
    def powerfactor(self) -> PowerQualityPowerfactor:
        """Return the ``POWer:QUALity:POWERFACtor`` command.

        Description:
            - Returns the power factor measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:POWERFACtor?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:POWERFACtor?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:QUALity:POWERFACtor?
            ```
        """
        return self._powerfactor

    @property
    def reactpwr(self) -> PowerQualityReactpwr:
        """Return the ``POWer:QUALity:REACTpwr`` command.

        Description:
            - Returns the reactive power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:REACTpwr?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:REACTpwr?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:QUALity:REACTpwr?
            ```
        """
        return self._reactpwr

    @property
    def truepwr(self) -> PowerQualityTruepwr:
        """Return the ``POWer:QUALity:TRUEpwr`` command.

        Description:
            - Returns the true power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:TRUEpwr?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:TRUEpwr?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:QUALity:TRUEpwr?
            ```
        """
        return self._truepwr

    @property
    def vcrestfactor(self) -> PowerQualityVcrestfactor:
        """Return the ``POWer:QUALity:VCRESTfactor`` command.

        Description:
            - This query returns the measurement for the voltage crest factor.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:VCRESTfactor?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:VCRESTfactor?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:QUALity:VCRESTfactor?
            ```
        """
        return self._vcrestfactor

    @property
    def vrms(self) -> PowerQualityVrms:
        """Return the ``POWer:QUALity:VRMS`` command.

        Description:
            - Returns the RMS voltage measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity:VRMS?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity:VRMS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:QUALity:VRMS?
            ```
        """
        return self._vrms


class PowerModulationType(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:MODulation:TYPe`` command.

    Description:
        - This command specifies the modulation type.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:MODulation:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:MODulation:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:MODulation:TYPe value`` command.

    SCPI Syntax:
        ```
        - POWer:MODulation:TYPe {PWIdth|NWIdth|PERIod|PDUty|NDUty|FREQuency}
        - POWer:MODulation:TYPe?
        ```

    Info:
        - ``PWIdth`` (positive width) is the distance (time) between the middle reference (default =
          50%) amplitude points of a positive pulse. The measurement is made on all the cycles in
          the waveform or gated region.
        - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
          reference (default = 50%) amplitude points of a negative pulse. The measurement is made on
          all the cycles in the waveform or gated region.
        - ``PERIod`` is the time required to complete the first cycle in a waveform or the gated
          region. The time is measured between the mid reference (default being 50%) amplitude
          points of the waveform.
        - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
          period, expressed as a percentage. It is measured on all the cycles in the waveform or
          gated region.
        - ``Positive Duty Cycle = ((Positive Width)/Period) × 100%``
        - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
          period, expressed as a percentage. The duty cycle is measured on all the cycles in the
          waveform or gated region.
        - ``Negative Duty Cycle = ((Negative Width) / Period) × 100%``
        - ``FREQuency`` measures all the cycles in the waveform or gated region. Frequency is the
          reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per second.
        - ``Frequency = 1 / Period``
    """


class PowerModulationSource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:MODulation:SOUrce`` command.

    Description:
        - This command specifies the source waveform for modulation tests. The voltage source
          waveform is specified using the ``POWER:VOLTAGESOURCE`` command and the current waveform
          is specified using the ``POWER:CURRENTSOURCE`` command.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:MODulation:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:MODulation:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:MODulation:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - POWer:MODulation:SOUrce {VOLTage|CURRent}
        - POWer:MODulation:SOUrce?
        ```

    Info:
        - ``VOLTage`` specifies voltage source waveform for modulation tests.
        - ``CURRent`` specifies current source waveform for modulation tests.
    """


class PowerModulation(SCPICmdRead):
    """The ``POWer:MODulation`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:MODulation?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:MODulation?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``POWer:MODulation:SOUrce`` command.
        - ``.type``: The ``POWer:MODulation:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = PowerModulationSource(device, f"{self._cmd_syntax}:SOUrce")
        self._type = PowerModulationType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def source(self) -> PowerModulationSource:
        """Return the ``POWer:MODulation:SOUrce`` command.

        Description:
            - This command specifies the source waveform for modulation tests. The voltage source
              waveform is specified using the ``POWER:VOLTAGESOURCE`` command and the current
              waveform is specified using the ``POWER:CURRENTSOURCE`` command.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:MODulation:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:MODulation:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:MODulation:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - POWer:MODulation:SOUrce {VOLTage|CURRent}
            - POWer:MODulation:SOUrce?
            ```

        Info:
            - ``VOLTage`` specifies voltage source waveform for modulation tests.
            - ``CURRent`` specifies current source waveform for modulation tests.
        """
        return self._source

    @property
    def type(self) -> PowerModulationType:
        """Return the ``POWer:MODulation:TYPe`` command.

        Description:
            - This command specifies the modulation type.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:MODulation:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:MODulation:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:MODulation:TYPe value``
              command.

        SCPI Syntax:
            ```
            - POWer:MODulation:TYPe {PWIdth|NWIdth|PERIod|PDUty|NDUty|FREQuency}
            - POWer:MODulation:TYPe?
            ```

        Info:
            - ``PWIdth`` (positive width) is the distance (time) between the middle reference
              (default = 50%) amplitude points of a positive pulse. The measurement is made on all
              the cycles in the waveform or gated region.
            - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
              reference (default = 50%) amplitude points of a negative pulse. The measurement is
              made on all the cycles in the waveform or gated region.
            - ``PERIod`` is the time required to complete the first cycle in a waveform or the gated
              region. The time is measured between the mid reference (default being 50%) amplitude
              points of the waveform.
            - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
              period, expressed as a percentage. It is measured on all the cycles in the waveform or
              gated region.
            - ``Positive Duty Cycle = ((Positive Width)/Period) × 100%``
            - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
              period, expressed as a percentage. The duty cycle is measured on all the cycles in the
              waveform or gated region.
            - ``Negative Duty Cycle = ((Negative Width) / Period) × 100%``
            - ``FREQuency`` measures all the cycles in the waveform or gated region. Frequency is
              the reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per
              second.
            - ``Frequency = 1 / Period``
        """
        return self._type


class PowerIndicators(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:INDICators`` command.

    Description:
        - This command specifies the state of the measurement indicators for the power application.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:INDICators?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:INDICators?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:INDICators value`` command.

    SCPI Syntax:
        ```
        - POWer:INDICators {OFF|ON|0|1}
        - POWer:INDICators?
        ```

    Info:
        - ``OFF`` or 0 turns off the measurement indicators.
        - ``ON`` or 1 turns on the measurement indicators.
    """


class PowerHarmonicsStandard(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:STANDard`` command.

    Description:
        - This command specifies the standard for harmonics tests.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:STANDard?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:STANDard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:STANDard value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:STANDard {NONe|IEC|MIL}
        - POWer:HARMonics:STANDard?
        ```

    Info:
        - ``NONe`` sets no standard for harmonic tests.
        - ``IEC`` sets IEC 610003-2 standard for harmonic tests.
        - ``MIL`` sets MIL1399 standard for harmonic tests.
    """


class PowerHarmonicsSource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:SOURce`` command.

    Description:
        - This command specifies the source waveform for harmonics tests. The voltage source
          waveform is specified using the ``POWER:VOLTAGESOURCE`` command and the current waveform
          is specified using the ``POWER:CURRENTSOURCE`` command.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:SOURce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:SOURce value`` command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:SOURce {VOLTage|CURRent}
        - POWer:HARMonics:SOURce?
        ```

    Info:
        - ``VOLTage`` specifies voltage source waveform for harmonic tests.
        - ``CURRent`` specifies current source waveform for harmonic tests.
    """


class PowerHarmonicsResultsThdr(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:THDR`` command.

    Description:
        - Returns the Total Harmonic Distortion (THD) in percentage, measured as a ratio to the RMS
          value of the source waveform.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:THDR?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:THDR?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:THDR?
        ```
    """


class PowerHarmonicsResultsThdf(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:THDF`` command.

    Description:
        - Returns the Total Harmonic Distortion (THD) in percentage, measured as a ratio to the RMS
          value of the fundamental component of the source waveform.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:THDF?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:THDF?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:THDF?
        ```
    """


class PowerHarmonicsResultsSave(SCPICmdWrite):
    """The ``POWer:HARMonics:RESults:SAVe`` command.

    Description:
        - Saves the harmonic results to the specified file in CSV format.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:RESults:SAVe value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:SAVe <String>
        ```
    """


class PowerHarmonicsResultsRms(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:RMS`` command.

    Description:
        - Returns the root mean square value of the harmonics source waveform.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:RMS?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:RMS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:RMS?
        ```
    """


class PowerHarmonicsResultsPassfail(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:PASSFail`` command.

    Description:
        - Returns the overall harmonics test result: PASS, FAIL or NA.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:PASSFail?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:PASSFail?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:PASSFail?
        ```
    """


class PowerHarmonicsResultsIecPower(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:IEC:POWer`` command.

    Description:
        - Returns the IEC input power that is used to calculate limits.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:IEC:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:IEC:POWer?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:IEC:POWer?
        ```
    """


class PowerHarmonicsResultsIecPowerfactor(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:IEC:POWERFactor`` command.

    Description:
        - Returns the IEC power factor measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:IEC:POWERFactor?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:IEC:POWERFactor?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:IEC:POWERFactor?
        ```
    """


class PowerHarmonicsResultsIecPohl(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:IEC:POHL`` command.

    Description:
        - Returns the IEC POHL measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:IEC:POHL?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:IEC:POHL?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:IEC:POHL?
        ```
    """


class PowerHarmonicsResultsIecPohc(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:IEC:POHC`` command.

    Description:
        - Returns the IEC POHC measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:IEC:POHC?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:IEC:POHC?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:IEC:POHC?
        ```
    """


class PowerHarmonicsResultsIecHarm5alternate(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:IEC:HARM5ALTernate`` command.

    Description:
        - Returns the overall harmonics test result for the 5th harmonic.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:HARMonics:RESults:IEC:HARM5ALTernate?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:IEC:HARM5ALTernate?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:IEC:HARM5ALTernate?
        ```
    """


class PowerHarmonicsResultsIecHarm3alternate(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:IEC:HARM3ALTernate`` command.

    Description:
        - Returns the IEC harmonics test result for the 3rd harmonic.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:HARMonics:RESults:IEC:HARM3ALTernate?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:IEC:HARM3ALTernate?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:IEC:HARM3ALTernate?
        ```
    """


class PowerHarmonicsResultsIecFundamental(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:IEC:FUNDamental`` command.

    Description:
        - Returns the IEC fundamental current used in calculating limits.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:IEC:FUNDamental?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:IEC:FUNDamental?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:IEC:FUNDamental?
        ```
    """


class PowerHarmonicsResultsIec(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:IEC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:IEC?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:IEC?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fundamental``: The ``POWer:HARMonics:RESults:IEC:FUNDamental`` command.
        - ``.harm3alternate``: The ``POWer:HARMonics:RESults:IEC:HARM3ALTernate`` command.
        - ``.harm5alternate``: The ``POWer:HARMonics:RESults:IEC:HARM5ALTernate`` command.
        - ``.pohc``: The ``POWer:HARMonics:RESults:IEC:POHC`` command.
        - ``.pohl``: The ``POWer:HARMonics:RESults:IEC:POHL`` command.
        - ``.powerfactor``: The ``POWer:HARMonics:RESults:IEC:POWERFactor`` command.
        - ``.power``: The ``POWer:HARMonics:RESults:IEC:POWer`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fundamental = PowerHarmonicsResultsIecFundamental(
            device, f"{self._cmd_syntax}:FUNDamental"
        )
        self._harm3alternate = PowerHarmonicsResultsIecHarm3alternate(
            device, f"{self._cmd_syntax}:HARM3ALTernate"
        )
        self._harm5alternate = PowerHarmonicsResultsIecHarm5alternate(
            device, f"{self._cmd_syntax}:HARM5ALTernate"
        )
        self._pohc = PowerHarmonicsResultsIecPohc(device, f"{self._cmd_syntax}:POHC")
        self._pohl = PowerHarmonicsResultsIecPohl(device, f"{self._cmd_syntax}:POHL")
        self._powerfactor = PowerHarmonicsResultsIecPowerfactor(
            device, f"{self._cmd_syntax}:POWERFactor"
        )
        self._power = PowerHarmonicsResultsIecPower(device, f"{self._cmd_syntax}:POWer")

    @property
    def fundamental(self) -> PowerHarmonicsResultsIecFundamental:
        """Return the ``POWer:HARMonics:RESults:IEC:FUNDamental`` command.

        Description:
            - Returns the IEC fundamental current used in calculating limits.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:IEC:FUNDamental?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:IEC:FUNDamental?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:IEC:FUNDamental?
            ```
        """
        return self._fundamental

    @property
    def harm3alternate(self) -> PowerHarmonicsResultsIecHarm3alternate:
        """Return the ``POWer:HARMonics:RESults:IEC:HARM3ALTernate`` command.

        Description:
            - Returns the IEC harmonics test result for the 3rd harmonic.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:IEC:HARM3ALTernate?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:IEC:HARM3ALTernate?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:IEC:HARM3ALTernate?
            ```
        """
        return self._harm3alternate

    @property
    def harm5alternate(self) -> PowerHarmonicsResultsIecHarm5alternate:
        """Return the ``POWer:HARMonics:RESults:IEC:HARM5ALTernate`` command.

        Description:
            - Returns the overall harmonics test result for the 5th harmonic.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:IEC:HARM5ALTernate?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:IEC:HARM5ALTernate?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:IEC:HARM5ALTernate?
            ```
        """
        return self._harm5alternate

    @property
    def pohc(self) -> PowerHarmonicsResultsIecPohc:
        """Return the ``POWer:HARMonics:RESults:IEC:POHC`` command.

        Description:
            - Returns the IEC POHC measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:IEC:POHC?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:IEC:POHC?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:IEC:POHC?
            ```
        """
        return self._pohc

    @property
    def pohl(self) -> PowerHarmonicsResultsIecPohl:
        """Return the ``POWer:HARMonics:RESults:IEC:POHL`` command.

        Description:
            - Returns the IEC POHL measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:IEC:POHL?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:IEC:POHL?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:IEC:POHL?
            ```
        """
        return self._pohl

    @property
    def powerfactor(self) -> PowerHarmonicsResultsIecPowerfactor:
        """Return the ``POWer:HARMonics:RESults:IEC:POWERFactor`` command.

        Description:
            - Returns the IEC power factor measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:IEC:POWERFactor?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:IEC:POWERFactor?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:IEC:POWERFactor?
            ```
        """
        return self._powerfactor

    @property
    def power(self) -> PowerHarmonicsResultsIecPower:
        """Return the ``POWer:HARMonics:RESults:IEC:POWer`` command.

        Description:
            - Returns the IEC input power that is used to calculate limits.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:IEC:POWer?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:IEC:POWer?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:IEC:POWer?
            ```
        """
        return self._power


class PowerHarmonicsResultsHarItemTestMilNormal(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL:NORMAL`` command.

    Description:
        - Returns the test result for the specified harmonic for the MIL-STD-1399 Section 300A
          testing standard. This query is analogous to that for the IEC 61000-3-2 standard
          ``POWER:HARMONICS:RESULTS:HAR1400:TEST:IEC:NORMAL`` command.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL:NORMAL?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL:NORMAL?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:HAR<x>:TEST:MIL:NORMAL?
        ```
    """


class PowerHarmonicsResultsHarItemTestMil(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.normal``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL:NORMAL`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._normal = PowerHarmonicsResultsHarItemTestMilNormal(
            device, f"{self._cmd_syntax}:NORMAL"
        )

    @property
    def normal(self) -> PowerHarmonicsResultsHarItemTestMilNormal:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL:NORMAL`` command.

        Description:
            - Returns the test result for the specified harmonic for the MIL-STD-1399 Section 300A
              testing standard. This query is analogous to that for the IEC 61000-3-2 standard
              ``POWER:HARMONICS:RESULTS:HAR1400:TEST:IEC:NORMAL`` command.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL:NORMAL?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL:NORMAL?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:HAR<x>:TEST:MIL:NORMAL?
            ```
        """
        return self._normal


class PowerHarmonicsResultsHarItemTestIecPohclimit(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:POHCLIMit`` command.

    Description:
        - Specifies if the higher harmonic limit (and conditions) for the 21st and higher order odd
          harmonics are met.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:POHCLIMit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:POHCLIMit?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:HAR<x>:TEST:IEC:POHCLIMit?
        ```
    """


class PowerHarmonicsResultsHarItemTestIecNormal(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:NORMAL`` command.

    Description:
        - Specifies if the Normal IEC harmonic limits are met.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:NORMAL?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:NORMAL?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:HAR<x>:TEST:IEC:NORMAL?
        ```
    """


class PowerHarmonicsResultsHarItemTestIecClassalimit(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:CLASSALIMit`` command.

    Description:
        - Specifies if the IEC Class A higher harmonic limit (and conditions) are met.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:CLASSALIMit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:CLASSALIMit?`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:HAR<x>:TEST:IEC:CLASSALIMit?
        ```
    """


class PowerHarmonicsResultsHarItemTestIec(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.classalimit``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:CLASSALIMit`` command.
        - ``.normal``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:NORMAL`` command.
        - ``.pohclimit``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:POHCLIMit`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._classalimit = PowerHarmonicsResultsHarItemTestIecClassalimit(
            device, f"{self._cmd_syntax}:CLASSALIMit"
        )
        self._normal = PowerHarmonicsResultsHarItemTestIecNormal(
            device, f"{self._cmd_syntax}:NORMAL"
        )
        self._pohclimit = PowerHarmonicsResultsHarItemTestIecPohclimit(
            device, f"{self._cmd_syntax}:POHCLIMit"
        )

    @property
    def classalimit(self) -> PowerHarmonicsResultsHarItemTestIecClassalimit:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:CLASSALIMit`` command.

        Description:
            - Specifies if the IEC Class A higher harmonic limit (and conditions) are met.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:CLASSALIMit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:CLASSALIMit?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:HAR<x>:TEST:IEC:CLASSALIMit?
            ```
        """
        return self._classalimit

    @property
    def normal(self) -> PowerHarmonicsResultsHarItemTestIecNormal:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:NORMAL`` command.

        Description:
            - Specifies if the Normal IEC harmonic limits are met.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:NORMAL?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:NORMAL?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:HAR<x>:TEST:IEC:NORMAL?
            ```
        """
        return self._normal

    @property
    def pohclimit(self) -> PowerHarmonicsResultsHarItemTestIecPohclimit:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:POHCLIMit`` command.

        Description:
            - Specifies if the higher harmonic limit (and conditions) for the 21st and higher order
              odd harmonics are met.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:POHCLIMit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:POHCLIMit?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:HAR<x>:TEST:IEC:POHCLIMit?
            ```
        """
        return self._pohclimit


class PowerHarmonicsResultsHarItemTest(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:TEST`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:TEST?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:HAR<x>:TEST?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.iec``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC`` command tree.
        - ``.mil``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._iec = PowerHarmonicsResultsHarItemTestIec(device, f"{self._cmd_syntax}:IEC")
        self._mil = PowerHarmonicsResultsHarItemTestMil(device, f"{self._cmd_syntax}:MIL")

    @property
    def iec(self) -> PowerHarmonicsResultsHarItemTestIec:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.classalimit``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:CLASSALIMit`` command.
            - ``.normal``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:NORMAL`` command.
            - ``.pohclimit``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC:POHCLIMit`` command.
        """
        return self._iec

    @property
    def mil(self) -> PowerHarmonicsResultsHarItemTestMil:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.normal``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL:NORMAL`` command.
        """
        return self._mil


class PowerHarmonicsResultsHarItemRmsPercent(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:RMS:PERCent`` command.

    Description:
        - Returns the RMS magnitude of the harmonic expressed as a percentage of the fundamental.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:RMS:PERCent?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:RMS:PERCent?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:HAR<x>:RMS:PERCent?
        ```
    """


class PowerHarmonicsResultsHarItemRmsAbsolute(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:RMS:ABSolute`` command.

    Description:
        - Returns the RMS magnitude of the harmonic in absolute units.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:RMS:ABSolute?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:RMS:ABSolute?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:HAR<x>:RMS:ABSolute?
        ```
    """


class PowerHarmonicsResultsHarItemRms(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:RMS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:RMS?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:HAR<x>:RMS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absolute``: The ``POWer:HARMonics:RESults:HAR<x>:RMS:ABSolute`` command.
        - ``.percent``: The ``POWer:HARMonics:RESults:HAR<x>:RMS:PERCent`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = PowerHarmonicsResultsHarItemRmsAbsolute(
            device, f"{self._cmd_syntax}:ABSolute"
        )
        self._percent = PowerHarmonicsResultsHarItemRmsPercent(
            device, f"{self._cmd_syntax}:PERCent"
        )

    @property
    def absolute(self) -> PowerHarmonicsResultsHarItemRmsAbsolute:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:RMS:ABSolute`` command.

        Description:
            - Returns the RMS magnitude of the harmonic in absolute units.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:RMS:ABSolute?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:RMS:ABSolute?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:HAR<x>:RMS:ABSolute?
            ```
        """
        return self._absolute

    @property
    def percent(self) -> PowerHarmonicsResultsHarItemRmsPercent:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:RMS:PERCent`` command.

        Description:
            - Returns the RMS magnitude of the harmonic expressed as a percentage of the
              fundamental.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:RMS:PERCent?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:RMS:PERCent?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:HAR<x>:RMS:PERCent?
            ```
        """
        return self._percent


class PowerHarmonicsResultsHarItemPhase(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:PHASe`` command.

    Description:
        - Returns the phase of the harmonic in degrees. The phase is measured relative to the
          zero-crossing of the reference waveform. When there is no reference waveform, the phase is
          relative to the fundamental component.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:PHASe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:PHASe?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:HAR<x>:PHASe?
        ```
    """


class PowerHarmonicsResultsHarItemLimit(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:LIMit`` command.

    Description:
        - The IEC and MIL standards specify a limit for each harmonic magnitude. Returns the limit
          in absolute units, or as a percentage of the fundamental as specified by the standard. IEC
          Class C (Table 2) and MIL standards specify the limit as a percentage of the fundamental.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:LIMit?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:LIMit?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:HAR<x>:LIMit?
        ```
    """


class PowerHarmonicsResultsHarItemIecmax(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:IECMAX`` command.

    Description:
        - The IEC Standard specifies harmonics measurements to be computed in time windows, with
          each time window being nominally 200 ms. This returns the maximum of the RMS magnitude of
          the harmonic, computed across successive 200 ms time windows within an observation period
          entered by the user.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:IECMAX?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:IECMAX?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:HAR<x>:IECMAX?
        ```
    """


class PowerHarmonicsResultsHarItemFrequency(SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>:FREQuency`` command.

    Description:
        - Returns the frequency of the harmonic.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:FREQuency?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:RESults:HAR<x>:FREQuency?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:HARMonics:RESults:HAR<x>:FREQuency?
        ```
    """


class PowerHarmonicsResultsHarItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``POWer:HARMonics:RESults:HAR<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:HAR<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``POWer:HARMonics:RESults:HAR<x>:FREQuency`` command.
        - ``.iecmax``: The ``POWer:HARMonics:RESults:HAR<x>:IECMAX`` command.
        - ``.limit``: The ``POWer:HARMonics:RESults:HAR<x>:LIMit`` command.
        - ``.phase``: The ``POWer:HARMonics:RESults:HAR<x>:PHASe`` command.
        - ``.rms``: The ``POWer:HARMonics:RESults:HAR<x>:RMS`` command tree.
        - ``.test``: The ``POWer:HARMonics:RESults:HAR<x>:TEST`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = PowerHarmonicsResultsHarItemFrequency(
            device, f"{self._cmd_syntax}:FREQuency"
        )
        self._iecmax = PowerHarmonicsResultsHarItemIecmax(device, f"{self._cmd_syntax}:IECMAX")
        self._limit = PowerHarmonicsResultsHarItemLimit(device, f"{self._cmd_syntax}:LIMit")
        self._phase = PowerHarmonicsResultsHarItemPhase(device, f"{self._cmd_syntax}:PHASe")
        self._rms = PowerHarmonicsResultsHarItemRms(device, f"{self._cmd_syntax}:RMS")
        self._test = PowerHarmonicsResultsHarItemTest(device, f"{self._cmd_syntax}:TEST")

    @property
    def frequency(self) -> PowerHarmonicsResultsHarItemFrequency:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:FREQuency`` command.

        Description:
            - Returns the frequency of the harmonic.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:FREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:HAR<x>:FREQuency?
            ```
        """
        return self._frequency

    @property
    def iecmax(self) -> PowerHarmonicsResultsHarItemIecmax:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:IECMAX`` command.

        Description:
            - The IEC Standard specifies harmonics measurements to be computed in time windows, with
              each time window being nominally 200 ms. This returns the maximum of the RMS magnitude
              of the harmonic, computed across successive 200 ms time windows within an observation
              period entered by the user.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:IECMAX?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:IECMAX?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:HAR<x>:IECMAX?
            ```
        """
        return self._iecmax

    @property
    def limit(self) -> PowerHarmonicsResultsHarItemLimit:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:LIMit`` command.

        Description:
            - The IEC and MIL standards specify a limit for each harmonic magnitude. Returns the
              limit in absolute units, or as a percentage of the fundamental as specified by the
              standard. IEC Class C (Table 2) and MIL standards specify the limit as a percentage of
              the fundamental.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:LIMit?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:LIMit?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:HAR<x>:LIMit?
            ```
        """
        return self._limit

    @property
    def phase(self) -> PowerHarmonicsResultsHarItemPhase:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:PHASe`` command.

        Description:
            - Returns the phase of the harmonic in degrees. The phase is measured relative to the
              zero-crossing of the reference waveform. When there is no reference waveform, the
              phase is relative to the fundamental component.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:PHASe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:PHASe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:HAR<x>:PHASe?
            ```
        """
        return self._phase

    @property
    def rms(self) -> PowerHarmonicsResultsHarItemRms:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:RMS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:RMS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:RMS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.absolute``: The ``POWer:HARMonics:RESults:HAR<x>:RMS:ABSolute`` command.
            - ``.percent``: The ``POWer:HARMonics:RESults:HAR<x>:RMS:PERCent`` command.
        """
        return self._rms

    @property
    def test(self) -> PowerHarmonicsResultsHarItemTest:
        """Return the ``POWer:HARMonics:RESults:HAR<x>:TEST`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>:TEST?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:HAR<x>:TEST?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.iec``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:IEC`` command tree.
            - ``.mil``: The ``POWer:HARMonics:RESults:HAR<x>:TEST:MIL`` command tree.
        """
        return self._test


class PowerHarmonicsResults(SCPICmdRead):
    """The ``POWer:HARMonics:RESults`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.har``: The ``POWer:HARMonics:RESults:HAR<x>`` command tree.
        - ``.iec``: The ``POWer:HARMonics:RESults:IEC`` command tree.
        - ``.passfail``: The ``POWer:HARMonics:RESults:PASSFail`` command.
        - ``.rms``: The ``POWer:HARMonics:RESults:RMS`` command.
        - ``.save``: The ``POWer:HARMonics:RESults:SAVe`` command.
        - ``.thdf``: The ``POWer:HARMonics:RESults:THDF`` command.
        - ``.thdr``: The ``POWer:HARMonics:RESults:THDR`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._har: Dict[int, PowerHarmonicsResultsHarItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerHarmonicsResultsHarItem(device, f"{self._cmd_syntax}:HAR{x}")
        )
        self._iec = PowerHarmonicsResultsIec(device, f"{self._cmd_syntax}:IEC")
        self._passfail = PowerHarmonicsResultsPassfail(device, f"{self._cmd_syntax}:PASSFail")
        self._rms = PowerHarmonicsResultsRms(device, f"{self._cmd_syntax}:RMS")
        self._save = PowerHarmonicsResultsSave(device, f"{self._cmd_syntax}:SAVe")
        self._thdf = PowerHarmonicsResultsThdf(device, f"{self._cmd_syntax}:THDF")
        self._thdr = PowerHarmonicsResultsThdr(device, f"{self._cmd_syntax}:THDR")

    @property
    def har(self) -> Dict[int, PowerHarmonicsResultsHarItem]:
        """Return the ``POWer:HARMonics:RESults:HAR<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:HAR<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:HAR<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``POWer:HARMonics:RESults:HAR<x>:FREQuency`` command.
            - ``.iecmax``: The ``POWer:HARMonics:RESults:HAR<x>:IECMAX`` command.
            - ``.limit``: The ``POWer:HARMonics:RESults:HAR<x>:LIMit`` command.
            - ``.phase``: The ``POWer:HARMonics:RESults:HAR<x>:PHASe`` command.
            - ``.rms``: The ``POWer:HARMonics:RESults:HAR<x>:RMS`` command tree.
            - ``.test``: The ``POWer:HARMonics:RESults:HAR<x>:TEST`` command tree.
        """
        return self._har

    @property
    def iec(self) -> PowerHarmonicsResultsIec:
        """Return the ``POWer:HARMonics:RESults:IEC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:IEC?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:IEC?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.fundamental``: The ``POWer:HARMonics:RESults:IEC:FUNDamental`` command.
            - ``.harm3alternate``: The ``POWer:HARMonics:RESults:IEC:HARM3ALTernate`` command.
            - ``.harm5alternate``: The ``POWer:HARMonics:RESults:IEC:HARM5ALTernate`` command.
            - ``.pohc``: The ``POWer:HARMonics:RESults:IEC:POHC`` command.
            - ``.pohl``: The ``POWer:HARMonics:RESults:IEC:POHL`` command.
            - ``.powerfactor``: The ``POWer:HARMonics:RESults:IEC:POWERFactor`` command.
            - ``.power``: The ``POWer:HARMonics:RESults:IEC:POWer`` command.
        """
        return self._iec

    @property
    def passfail(self) -> PowerHarmonicsResultsPassfail:
        """Return the ``POWer:HARMonics:RESults:PASSFail`` command.

        Description:
            - Returns the overall harmonics test result: PASS, FAIL or NA.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:PASSFail?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:RESults:PASSFail?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:PASSFail?
            ```
        """
        return self._passfail

    @property
    def rms(self) -> PowerHarmonicsResultsRms:
        """Return the ``POWer:HARMonics:RESults:RMS`` command.

        Description:
            - Returns the root mean square value of the harmonics source waveform.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:RMS?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:RMS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:RMS?
            ```
        """
        return self._rms

    @property
    def save(self) -> PowerHarmonicsResultsSave:
        """Return the ``POWer:HARMonics:RESults:SAVe`` command.

        Description:
            - Saves the harmonic results to the specified file in CSV format.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:RESults:SAVe value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:SAVe <String>
            ```
        """
        return self._save

    @property
    def thdf(self) -> PowerHarmonicsResultsThdf:
        """Return the ``POWer:HARMonics:RESults:THDF`` command.

        Description:
            - Returns the Total Harmonic Distortion (THD) in percentage, measured as a ratio to the
              RMS value of the fundamental component of the source waveform.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:THDF?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:THDF?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:THDF?
            ```
        """
        return self._thdf

    @property
    def thdr(self) -> PowerHarmonicsResultsThdr:
        """Return the ``POWer:HARMonics:RESults:THDR`` command.

        Description:
            - Returns the Total Harmonic Distortion (THD) in percentage, measured as a ratio to the
              RMS value of the source waveform.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults:THDR?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults:THDR?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:HARMonics:RESults:THDR?
            ```
        """
        return self._thdr


class PowerHarmonicsNrHarmonics(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:NR_HARMonics`` command.

    Description:
        - This command specifies the number of harmonics (value ranging from 20 to 400) when the
          harmonics standard is NONe.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:NR_HARMonics?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:NR_HARMonics?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:NR_HARMonics value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:NR_HARMonics <NR3>
        - POWer:HARMonics:NR_HARMonics?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the number of harmonics.
    """


class PowerHarmonicsMilPowerlevel(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:MIL:POWERLEVel`` command.

    Description:
        - This command specifies the power level for calculating limits for MIL-STD-1399 Section
          300A harmonics tests.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:MIL:POWERLEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:MIL:POWERLEVel?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:MIL:POWERLEVel value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:MIL:POWERLEVel {LOW|HIGH}
        - POWer:HARMonics:MIL:POWERLEVel?
        ```

    Info:
        - ``LOW`` specifies low power level for MIL-STD-1399 harmonics tests.
        - ``HIGH`` specifies high power level for MIL-STD-1399 harmonics tests.
    """


class PowerHarmonicsMilLinefrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:MIL:LINEFREQuency`` command.

    Description:
        - This command specifies the line frequency for MIL-STD-1399 Section 300A harmonics tests.
          Valid values are 60 or 400 Hz.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:MIL:LINEFREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:MIL:LINEFREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:HARMonics:MIL:LINEFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:MIL:LINEFREQuency <NR1>
        - POWer:HARMonics:MIL:LINEFREQuency?
        ```

    Info:
        - ``<NR1>`` is an unsigned integer that specifies the line frequency for the MIL standard.
    """


class PowerHarmonicsMilFundamentalUserCurrent(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:MIL:FUNDamental:USER:CURrent`` command.

    Description:
        - This command specifies RMS amperes for USER CALCmethod.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:HARMonics:MIL:FUNDamental:USER:CURrent?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:MIL:FUNDamental:USER:CURrent?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:HARMonics:MIL:FUNDamental:USER:CURrent value`` command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:MIL:FUNDamental:USER:CURrent <NR3>
        - POWer:HARMonics:MIL:FUNDamental:USER:CURrent?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the current in amperes for USER
          CALCmethod.
    """


class PowerHarmonicsMilFundamentalUser(SCPICmdRead):
    """The ``POWer:HARMonics:MIL:FUNDamental:USER`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:MIL:FUNDamental:USER?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:MIL:FUNDamental:USER?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.current``: The ``POWer:HARMonics:MIL:FUNDamental:USER:CURrent`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._current = PowerHarmonicsMilFundamentalUserCurrent(
            device, f"{self._cmd_syntax}:CURrent"
        )

    @property
    def current(self) -> PowerHarmonicsMilFundamentalUserCurrent:
        """Return the ``POWer:HARMonics:MIL:FUNDamental:USER:CURrent`` command.

        Description:
            - This command specifies RMS amperes for USER CALCmethod.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:MIL:FUNDamental:USER:CURrent?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:MIL:FUNDamental:USER:CURrent?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:MIL:FUNDamental:USER:CURrent value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:MIL:FUNDamental:USER:CURrent <NR3>
            - POWer:HARMonics:MIL:FUNDamental:USER:CURrent?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the current in amperes for USER
              CALCmethod.
        """
        return self._current


class PowerHarmonicsMilFundamentalCalcmethod(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:MIL:FUNDamental:CALCmethod`` command.

    Description:
        - This command specifies the measurement method for the MIL harmonics fundamental current
          for use in calculating limits.

    Usage:
        - Using the ``.query()`` method will send the
          ``POWer:HARMonics:MIL:FUNDamental:CALCmethod?`` query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:MIL:FUNDamental:CALCmethod?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:HARMonics:MIL:FUNDamental:CALCmethod value`` command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:MIL:FUNDamental:CALCmethod {MEAS|USER}
        - POWer:HARMonics:MIL:FUNDamental:CALCmethod?
        ```

    Info:
        - ``MEAS`` specifies that the value of the fundamental current used in calculating limits is
          measured.
        - ``USER`` specifies that the value of the fundamental current used in calculated limits is
          user defined.
    """


class PowerHarmonicsMilFundamental(SCPICmdRead):
    """The ``POWer:HARMonics:MIL:FUNDamental`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:MIL:FUNDamental?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:MIL:FUNDamental?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.calcmethod``: The ``POWer:HARMonics:MIL:FUNDamental:CALCmethod`` command.
        - ``.user``: The ``POWer:HARMonics:MIL:FUNDamental:USER`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._calcmethod = PowerHarmonicsMilFundamentalCalcmethod(
            device, f"{self._cmd_syntax}:CALCmethod"
        )
        self._user = PowerHarmonicsMilFundamentalUser(device, f"{self._cmd_syntax}:USER")

    @property
    def calcmethod(self) -> PowerHarmonicsMilFundamentalCalcmethod:
        """Return the ``POWer:HARMonics:MIL:FUNDamental:CALCmethod`` command.

        Description:
            - This command specifies the measurement method for the MIL harmonics fundamental
              current for use in calculating limits.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:MIL:FUNDamental:CALCmethod?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:MIL:FUNDamental:CALCmethod?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:MIL:FUNDamental:CALCmethod value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:MIL:FUNDamental:CALCmethod {MEAS|USER}
            - POWer:HARMonics:MIL:FUNDamental:CALCmethod?
            ```

        Info:
            - ``MEAS`` specifies that the value of the fundamental current used in calculating
              limits is measured.
            - ``USER`` specifies that the value of the fundamental current used in calculated limits
              is user defined.
        """
        return self._calcmethod

    @property
    def user(self) -> PowerHarmonicsMilFundamentalUser:
        """Return the ``POWer:HARMonics:MIL:FUNDamental:USER`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:MIL:FUNDamental:USER?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:MIL:FUNDamental:USER?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.current``: The ``POWer:HARMonics:MIL:FUNDamental:USER:CURrent`` command.
        """
        return self._user


class PowerHarmonicsMil(SCPICmdRead):
    """The ``POWer:HARMonics:MIL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:MIL?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:MIL?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fundamental``: The ``POWer:HARMonics:MIL:FUNDamental`` command tree.
        - ``.linefrequency``: The ``POWer:HARMonics:MIL:LINEFREQuency`` command.
        - ``.powerlevel``: The ``POWer:HARMonics:MIL:POWERLEVel`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fundamental = PowerHarmonicsMilFundamental(device, f"{self._cmd_syntax}:FUNDamental")
        self._linefrequency = PowerHarmonicsMilLinefrequency(
            device, f"{self._cmd_syntax}:LINEFREQuency"
        )
        self._powerlevel = PowerHarmonicsMilPowerlevel(device, f"{self._cmd_syntax}:POWERLEVel")

    @property
    def fundamental(self) -> PowerHarmonicsMilFundamental:
        """Return the ``POWer:HARMonics:MIL:FUNDamental`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:MIL:FUNDamental?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:MIL:FUNDamental?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.calcmethod``: The ``POWer:HARMonics:MIL:FUNDamental:CALCmethod`` command.
            - ``.user``: The ``POWer:HARMonics:MIL:FUNDamental:USER`` command tree.
        """
        return self._fundamental

    @property
    def linefrequency(self) -> PowerHarmonicsMilLinefrequency:
        """Return the ``POWer:HARMonics:MIL:LINEFREQuency`` command.

        Description:
            - This command specifies the line frequency for MIL-STD-1399 Section 300A harmonics
              tests. Valid values are 60 or 400 Hz.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:MIL:LINEFREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:MIL:LINEFREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:MIL:LINEFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:MIL:LINEFREQuency <NR1>
            - POWer:HARMonics:MIL:LINEFREQuency?
            ```

        Info:
            - ``<NR1>`` is an unsigned integer that specifies the line frequency for the MIL
              standard.
        """
        return self._linefrequency

    @property
    def powerlevel(self) -> PowerHarmonicsMilPowerlevel:
        """Return the ``POWer:HARMonics:MIL:POWERLEVel`` command.

        Description:
            - This command specifies the power level for calculating limits for MIL-STD-1399 Section
              300A harmonics tests.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:MIL:POWERLEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:MIL:POWERLEVel?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:MIL:POWERLEVel value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:MIL:POWERLEVel {LOW|HIGH}
            - POWer:HARMonics:MIL:POWERLEVel?
            ```

        Info:
            - ``LOW`` specifies low power level for MIL-STD-1399 harmonics tests.
            - ``HIGH`` specifies high power level for MIL-STD-1399 harmonics tests.
        """
        return self._powerlevel


class PowerHarmonicsIecPowerfactor(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:IEC:POWERFACtor`` command.

    Description:
        - This command specifies the rated power factor for IEC harmonics.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:POWERFACtor?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:POWERFACtor?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:IEC:POWERFACtor value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:IEC:POWERFACtor <NR3>
        - POWer:HARMonics:IEC:POWERFACtor?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the power factor. Valid values ranges
          from 0 to 1 in increments of 0.1.
    """


class PowerHarmonicsIecObsperiod(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:IEC:OBSPERiod`` command.

    Description:
        - This command specifies the IEC observation period.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:OBSPERiod?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:OBSPERiod?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:IEC:OBSPERiod value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:IEC:OBSPERiod <NR3>
        - POWer:HARMonics:IEC:OBSPERiod?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the IEC observation period. Valid
          values ranges from 0.2 to 10 s.
    """


class PowerHarmonicsIecLinefrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:IEC:LINEFREQuency`` command.

    Description:
        - This command specifies the line frequency for the IEC standard.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:LINEFREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:LINEFREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:HARMonics:IEC:LINEFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:IEC:LINEFREQuency <NR1>
        - POWer:HARMonics:IEC:LINEFREQuency?
        ```

    Info:
        - ``<NR1>`` is an unsigned integer that specifies the line frequency. The valid values are
          50 and 60.
    """


class PowerHarmonicsIecInputpower(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:IEC:INPUTPOWer`` command.

    Description:
        - This command specifies the class D rated input power for IEC harmonics.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:INPUTPOWer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:INPUTPOWer?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:IEC:INPUTPOWer value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:IEC:INPUTPOWer <NR3>
        - POWer:HARMonics:IEC:INPUTPOWer?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the class D input power. Valid values
          ranges from 0 to 600 in increments of 10. The unit of measure is watt.
    """


class PowerHarmonicsIecGrouping(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:IEC:GROUPing`` command.

    Description:
        - This command specifies the enabled state for grouping of IEC harmonics.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:GROUPing?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:GROUPing?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:IEC:GROUPing value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:IEC:GROUPing {OFF|ON|1|0}
        - POWer:HARMonics:IEC:GROUPing?
        ```

    Info:
        - ``ON`` or 1 enables grouping of IEC harmonics.
        - ``OFF`` or 0 disables grouping of IEC harmonics.
    """


class PowerHarmonicsIecFundamental(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:IEC:FUNDamental`` command.

    Description:
        - This command specifies the rated fundamental current for IEC harmonics. Valid values
          ranges from 0 to 16 in increments of 0.1. The unit is ampere.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:FUNDamental?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:FUNDamental?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:IEC:FUNDamental value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:IEC:FUNDamental <NR3>
        - POWer:HARMonics:IEC:FUNDamental?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the fundamental current in amperes.
    """


class PowerHarmonicsIecFilter(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:IEC:FILter`` command.

    Description:
        - This command specifies the enabled state for filtering of IEC harmonics.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:FILter?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:FILter?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:IEC:FILter value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:IEC:FILter {OFF|ON|0|1}
        - POWer:HARMonics:IEC:FILter?
        ```

    Info:
        - ``ON`` or 1 enables filtering of IEC harmonics.
        - ``OFF`` or 0 disables filtering of IEC harmonics.
    """


class PowerHarmonicsIecClass(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:IEC:CLAss`` command.

    Description:
        - This command specifies the equipment class for IEC harmonics.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:CLAss?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:CLAss?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:IEC:CLAss value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:IEC:CLAss {A|B|C<x>|D}
        - POWer:HARMonics:IEC:CLAss?
        ```

    Info:
        - ``A`` specifies Class A Equipment.
        - ``B`` specifies Class B Equipment.
        - ``C1`` specifies Class C Equipment that use Table 1 limits of the IEC standard.
        - ``C2`` specifies Class C Equipment that use Table 2 limits of the IEC standard.
        - ``C3`` specifies Class C Equipment that use Table 3 limits of the IEC standard.
        - ``D`` specifies Class D Equipment.
    """


#  pylint: disable=too-many-instance-attributes
class PowerHarmonicsIec(SCPICmdRead):
    """The ``POWer:HARMonics:IEC`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.class``: The ``POWer:HARMonics:IEC:CLAss`` command.
        - ``.filter``: The ``POWer:HARMonics:IEC:FILter`` command.
        - ``.fundamental``: The ``POWer:HARMonics:IEC:FUNDamental`` command.
        - ``.grouping``: The ``POWer:HARMonics:IEC:GROUPing`` command.
        - ``.inputpower``: The ``POWer:HARMonics:IEC:INPUTPOWer`` command.
        - ``.linefrequency``: The ``POWer:HARMonics:IEC:LINEFREQuency`` command.
        - ``.obsperiod``: The ``POWer:HARMonics:IEC:OBSPERiod`` command.
        - ``.powerfactor``: The ``POWer:HARMonics:IEC:POWERFACtor`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._class = PowerHarmonicsIecClass(device, f"{self._cmd_syntax}:CLAss")
        self._filter = PowerHarmonicsIecFilter(device, f"{self._cmd_syntax}:FILter")
        self._fundamental = PowerHarmonicsIecFundamental(device, f"{self._cmd_syntax}:FUNDamental")
        self._grouping = PowerHarmonicsIecGrouping(device, f"{self._cmd_syntax}:GROUPing")
        self._inputpower = PowerHarmonicsIecInputpower(device, f"{self._cmd_syntax}:INPUTPOWer")
        self._linefrequency = PowerHarmonicsIecLinefrequency(
            device, f"{self._cmd_syntax}:LINEFREQuency"
        )
        self._obsperiod = PowerHarmonicsIecObsperiod(device, f"{self._cmd_syntax}:OBSPERiod")
        self._powerfactor = PowerHarmonicsIecPowerfactor(device, f"{self._cmd_syntax}:POWERFACtor")

    @property
    def class_(self) -> PowerHarmonicsIecClass:
        """Return the ``POWer:HARMonics:IEC:CLAss`` command.

        Description:
            - This command specifies the equipment class for IEC harmonics.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:CLAss?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:CLAss?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:HARMonics:IEC:CLAss value``
              command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:IEC:CLAss {A|B|C<x>|D}
            - POWer:HARMonics:IEC:CLAss?
            ```

        Info:
            - ``A`` specifies Class A Equipment.
            - ``B`` specifies Class B Equipment.
            - ``C1`` specifies Class C Equipment that use Table 1 limits of the IEC standard.
            - ``C2`` specifies Class C Equipment that use Table 2 limits of the IEC standard.
            - ``C3`` specifies Class C Equipment that use Table 3 limits of the IEC standard.
            - ``D`` specifies Class D Equipment.
        """
        return self._class

    @property
    def filter(self) -> PowerHarmonicsIecFilter:
        """Return the ``POWer:HARMonics:IEC:FILter`` command.

        Description:
            - This command specifies the enabled state for filtering of IEC harmonics.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:FILter?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:FILter?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:HARMonics:IEC:FILter value``
              command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:IEC:FILter {OFF|ON|0|1}
            - POWer:HARMonics:IEC:FILter?
            ```

        Info:
            - ``ON`` or 1 enables filtering of IEC harmonics.
            - ``OFF`` or 0 disables filtering of IEC harmonics.
        """
        return self._filter

    @property
    def fundamental(self) -> PowerHarmonicsIecFundamental:
        """Return the ``POWer:HARMonics:IEC:FUNDamental`` command.

        Description:
            - This command specifies the rated fundamental current for IEC harmonics. Valid values
              ranges from 0 to 16 in increments of 0.1. The unit is ampere.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:FUNDamental?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:FUNDamental?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:IEC:FUNDamental value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:IEC:FUNDamental <NR3>
            - POWer:HARMonics:IEC:FUNDamental?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the fundamental current in
              amperes.
        """
        return self._fundamental

    @property
    def grouping(self) -> PowerHarmonicsIecGrouping:
        """Return the ``POWer:HARMonics:IEC:GROUPing`` command.

        Description:
            - This command specifies the enabled state for grouping of IEC harmonics.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:GROUPing?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:GROUPing?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:IEC:GROUPing value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:IEC:GROUPing {OFF|ON|1|0}
            - POWer:HARMonics:IEC:GROUPing?
            ```

        Info:
            - ``ON`` or 1 enables grouping of IEC harmonics.
            - ``OFF`` or 0 disables grouping of IEC harmonics.
        """
        return self._grouping

    @property
    def inputpower(self) -> PowerHarmonicsIecInputpower:
        """Return the ``POWer:HARMonics:IEC:INPUTPOWer`` command.

        Description:
            - This command specifies the class D rated input power for IEC harmonics.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:INPUTPOWer?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:INPUTPOWer?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:IEC:INPUTPOWer value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:IEC:INPUTPOWer <NR3>
            - POWer:HARMonics:IEC:INPUTPOWer?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the class D input power. Valid
              values ranges from 0 to 600 in increments of 10. The unit of measure is watt.
        """
        return self._inputpower

    @property
    def linefrequency(self) -> PowerHarmonicsIecLinefrequency:
        """Return the ``POWer:HARMonics:IEC:LINEFREQuency`` command.

        Description:
            - This command specifies the line frequency for the IEC standard.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:LINEFREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:IEC:LINEFREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:IEC:LINEFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:IEC:LINEFREQuency <NR1>
            - POWer:HARMonics:IEC:LINEFREQuency?
            ```

        Info:
            - ``<NR1>`` is an unsigned integer that specifies the line frequency. The valid values
              are 50 and 60.
        """
        return self._linefrequency

    @property
    def obsperiod(self) -> PowerHarmonicsIecObsperiod:
        """Return the ``POWer:HARMonics:IEC:OBSPERiod`` command.

        Description:
            - This command specifies the IEC observation period.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:OBSPERiod?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:OBSPERiod?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:IEC:OBSPERiod value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:IEC:OBSPERiod <NR3>
            - POWer:HARMonics:IEC:OBSPERiod?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the IEC observation period. Valid
              values ranges from 0.2 to 10 s.
        """
        return self._obsperiod

    @property
    def powerfactor(self) -> PowerHarmonicsIecPowerfactor:
        """Return the ``POWer:HARMonics:IEC:POWERFACtor`` command.

        Description:
            - This command specifies the rated power factor for IEC harmonics.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC:POWERFACtor?``
              query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC:POWERFACtor?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:IEC:POWERFACtor value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:IEC:POWERFACtor <NR3>
            - POWer:HARMonics:IEC:POWERFACtor?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the power factor. Valid values
              ranges from 0 to 1 in increments of 0.1.
        """
        return self._powerfactor


class PowerHarmonicsFreqrefFixedfreqvalue(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:FREQRef:FIXEDFREQValue`` command.

    Description:
        - This command specifies the frequency value when the ``:FREQRef`` selection is
          FIXEDFREQuency.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:FREQRef:FIXEDFREQValue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:HARMonics:FREQRef:FIXEDFREQValue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:HARMonics:FREQRef:FIXEDFREQValue value`` command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:FREQRef:FIXEDFREQValue <NR3>
        - POWer:HARMonics:FREQRef:FIXEDFREQValue?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the fixed frequency value.
    """


class PowerHarmonicsFreqref(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:FREQRef`` command.

    Description:
        - This command specifies the frequency reference used when the harmonic standard is None.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:FREQRef?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:FREQRef?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:FREQRef value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:FREQRef {VOLTage|CURRent|HARMSOURce|FIXEDFREQuency}
        - POWer:HARMonics:FREQRef?
        ```

    Info:
        - ``VOLTage`` to use a voltage waveform as the frequency reference.
        - ``CURRent`` to use a current waveform as the frequency reference.
        - ``HARMSOURce`` to use a harmonic source waveform as the frequency reference.
        - ``FIXEDFREQuency`` to use a fixed frequency value instead of a waveform for the frequency
          reference.

    Properties:
        - ``.fixedfreqvalue``: The ``POWer:HARMonics:FREQRef:FIXEDFREQValue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fixedfreqvalue = PowerHarmonicsFreqrefFixedfreqvalue(
            device, f"{self._cmd_syntax}:FIXEDFREQValue"
        )

    @property
    def fixedfreqvalue(self) -> PowerHarmonicsFreqrefFixedfreqvalue:
        """Return the ``POWer:HARMonics:FREQRef:FIXEDFREQValue`` command.

        Description:
            - This command specifies the frequency value when the ``:FREQRef`` selection is
              FIXEDFREQuency.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:HARMonics:FREQRef:FIXEDFREQValue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:HARMonics:FREQRef:FIXEDFREQValue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:FREQRef:FIXEDFREQValue value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:FREQRef:FIXEDFREQValue <NR3>
            - POWer:HARMonics:FREQRef:FIXEDFREQValue?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the fixed frequency value.
        """
        return self._fixedfreqvalue


class PowerHarmonicsDisplayType(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:DISplay:TYPe`` command.

    Description:
        - This command specifies the display type for harmonics tests.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:DISplay:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:DISplay:TYPe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:DISplay:TYPe value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:DISplay:TYPe {GRAph|TABle}
        - POWer:HARMonics:DISplay:TYPe?
        ```

    Info:
        - ``GRAph`` displays harmonic tests results in graphical format.
        - ``TABle`` displays harmonic tests results in tabular format.
    """


class PowerHarmonicsDisplaySelect(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:HARMonics:DISplay:SELect`` command.

    Description:
        - This command specifies the harmonics to be displayed when the harmonics standard is NONe.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:DISplay:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:DISplay:SELect?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:HARMonics:DISplay:SELect value``
          command.

    SCPI Syntax:
        ```
        - POWer:HARMonics:DISplay:SELect {ODD|EVEN|ALL}
        - POWer:HARMonics:DISplay:SELect?
        ```

    Info:
        - ``ODD`` to display only odd harmonics.
        - ``EVEN`` to display only even harmonics.
        - ``ALL`` to display both odd and even harmonics.
    """


class PowerHarmonicsDisplay(SCPICmdRead):
    """The ``POWer:HARMonics:DISplay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:DISplay?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.select``: The ``POWer:HARMonics:DISplay:SELect`` command.
        - ``.type``: The ``POWer:HARMonics:DISplay:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._select = PowerHarmonicsDisplaySelect(device, f"{self._cmd_syntax}:SELect")
        self._type = PowerHarmonicsDisplayType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def select(self) -> PowerHarmonicsDisplaySelect:
        """Return the ``POWer:HARMonics:DISplay:SELect`` command.

        Description:
            - This command specifies the harmonics to be displayed when the harmonics standard is
              NONe.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:DISplay:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:DISplay:SELect?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:DISplay:SELect value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:DISplay:SELect {ODD|EVEN|ALL}
            - POWer:HARMonics:DISplay:SELect?
            ```

        Info:
            - ``ODD`` to display only odd harmonics.
            - ``EVEN`` to display only even harmonics.
            - ``ALL`` to display both odd and even harmonics.
        """
        return self._select

    @property
    def type(self) -> PowerHarmonicsDisplayType:
        """Return the ``POWer:HARMonics:DISplay:TYPe`` command.

        Description:
            - This command specifies the display type for harmonics tests.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:DISplay:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:DISplay:TYPe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:DISplay:TYPe value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:DISplay:TYPe {GRAph|TABle}
            - POWer:HARMonics:DISplay:TYPe?
            ```

        Info:
            - ``GRAph`` displays harmonic tests results in graphical format.
            - ``TABle`` displays harmonic tests results in tabular format.
        """
        return self._type


#  pylint: disable=too-many-instance-attributes
class PowerHarmonics(SCPICmdRead):
    """The ``POWer:HARMonics`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:HARMonics?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:HARMonics?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.display``: The ``POWer:HARMonics:DISplay`` command tree.
        - ``.freqref``: The ``POWer:HARMonics:FREQRef`` command.
        - ``.iec``: The ``POWer:HARMonics:IEC`` command tree.
        - ``.mil``: The ``POWer:HARMonics:MIL`` command tree.
        - ``.nr_harmonics``: The ``POWer:HARMonics:NR_HARMonics`` command.
        - ``.results``: The ``POWer:HARMonics:RESults`` command tree.
        - ``.source``: The ``POWer:HARMonics:SOURce`` command.
        - ``.standard``: The ``POWer:HARMonics:STANDard`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._display = PowerHarmonicsDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._freqref = PowerHarmonicsFreqref(device, f"{self._cmd_syntax}:FREQRef")
        self._iec = PowerHarmonicsIec(device, f"{self._cmd_syntax}:IEC")
        self._mil = PowerHarmonicsMil(device, f"{self._cmd_syntax}:MIL")
        self._nr_harmonics = PowerHarmonicsNrHarmonics(device, f"{self._cmd_syntax}:NR_HARMonics")
        self._results = PowerHarmonicsResults(device, f"{self._cmd_syntax}:RESults")
        self._source = PowerHarmonicsSource(device, f"{self._cmd_syntax}:SOURce")
        self._standard = PowerHarmonicsStandard(device, f"{self._cmd_syntax}:STANDard")

    @property
    def display(self) -> PowerHarmonicsDisplay:
        """Return the ``POWer:HARMonics:DISplay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:DISplay?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.select``: The ``POWer:HARMonics:DISplay:SELect`` command.
            - ``.type``: The ``POWer:HARMonics:DISplay:TYPe`` command.
        """
        return self._display

    @property
    def freqref(self) -> PowerHarmonicsFreqref:
        """Return the ``POWer:HARMonics:FREQRef`` command.

        Description:
            - This command specifies the frequency reference used when the harmonic standard is
              None.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:FREQRef?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:FREQRef?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:HARMonics:FREQRef value``
              command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:FREQRef {VOLTage|CURRent|HARMSOURce|FIXEDFREQuency}
            - POWer:HARMonics:FREQRef?
            ```

        Info:
            - ``VOLTage`` to use a voltage waveform as the frequency reference.
            - ``CURRent`` to use a current waveform as the frequency reference.
            - ``HARMSOURce`` to use a harmonic source waveform as the frequency reference.
            - ``FIXEDFREQuency`` to use a fixed frequency value instead of a waveform for the
              frequency reference.

        Sub-properties:
            - ``.fixedfreqvalue``: The ``POWer:HARMonics:FREQRef:FIXEDFREQValue`` command.
        """
        return self._freqref

    @property
    def iec(self) -> PowerHarmonicsIec:
        """Return the ``POWer:HARMonics:IEC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:IEC?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:IEC?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.class``: The ``POWer:HARMonics:IEC:CLAss`` command.
            - ``.filter``: The ``POWer:HARMonics:IEC:FILter`` command.
            - ``.fundamental``: The ``POWer:HARMonics:IEC:FUNDamental`` command.
            - ``.grouping``: The ``POWer:HARMonics:IEC:GROUPing`` command.
            - ``.inputpower``: The ``POWer:HARMonics:IEC:INPUTPOWer`` command.
            - ``.linefrequency``: The ``POWer:HARMonics:IEC:LINEFREQuency`` command.
            - ``.obsperiod``: The ``POWer:HARMonics:IEC:OBSPERiod`` command.
            - ``.powerfactor``: The ``POWer:HARMonics:IEC:POWERFACtor`` command.
        """
        return self._iec

    @property
    def mil(self) -> PowerHarmonicsMil:
        """Return the ``POWer:HARMonics:MIL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:MIL?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:MIL?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.fundamental``: The ``POWer:HARMonics:MIL:FUNDamental`` command tree.
            - ``.linefrequency``: The ``POWer:HARMonics:MIL:LINEFREQuency`` command.
            - ``.powerlevel``: The ``POWer:HARMonics:MIL:POWERLEVel`` command.
        """
        return self._mil

    @property
    def nr_harmonics(self) -> PowerHarmonicsNrHarmonics:
        """Return the ``POWer:HARMonics:NR_HARMonics`` command.

        Description:
            - This command specifies the number of harmonics (value ranging from 20 to 400) when the
              harmonics standard is NONe.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:NR_HARMonics?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:NR_HARMonics?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:HARMonics:NR_HARMonics value`` command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:NR_HARMonics <NR3>
            - POWer:HARMonics:NR_HARMonics?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the number of harmonics.
        """
        return self._nr_harmonics

    @property
    def results(self) -> PowerHarmonicsResults:
        """Return the ``POWer:HARMonics:RESults`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:RESults?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:RESults?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.har``: The ``POWer:HARMonics:RESults:HAR<x>`` command tree.
            - ``.iec``: The ``POWer:HARMonics:RESults:IEC`` command tree.
            - ``.passfail``: The ``POWer:HARMonics:RESults:PASSFail`` command.
            - ``.rms``: The ``POWer:HARMonics:RESults:RMS`` command.
            - ``.save``: The ``POWer:HARMonics:RESults:SAVe`` command.
            - ``.thdf``: The ``POWer:HARMonics:RESults:THDF`` command.
            - ``.thdr``: The ``POWer:HARMonics:RESults:THDR`` command.
        """
        return self._results

    @property
    def source(self) -> PowerHarmonicsSource:
        """Return the ``POWer:HARMonics:SOURce`` command.

        Description:
            - This command specifies the source waveform for harmonics tests. The voltage source
              waveform is specified using the ``POWER:VOLTAGESOURCE`` command and the current
              waveform is specified using the ``POWER:CURRENTSOURCE`` command.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:SOURce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:HARMonics:SOURce value``
              command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:SOURce {VOLTage|CURRent}
            - POWer:HARMonics:SOURce?
            ```

        Info:
            - ``VOLTage`` specifies voltage source waveform for harmonic tests.
            - ``CURRent`` specifies current source waveform for harmonic tests.
        """
        return self._source

    @property
    def standard(self) -> PowerHarmonicsStandard:
        """Return the ``POWer:HARMonics:STANDard`` command.

        Description:
            - This command specifies the standard for harmonics tests.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics:STANDard?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics:STANDard?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:HARMonics:STANDard value``
              command.

        SCPI Syntax:
            ```
            - POWer:HARMonics:STANDard {NONe|IEC|MIL}
            - POWer:HARMonics:STANDard?
            ```

        Info:
            - ``NONe`` sets no standard for harmonic tests.
            - ``IEC`` sets IEC 610003-2 standard for harmonic tests.
            - ``MIL`` sets MIL1399 standard for harmonic tests.
        """
        return self._standard


class PowerGating(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:GATing`` command.

    Description:
        - This command specifies the power application gating.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:GATing?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:GATing?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:GATing value`` command.

    SCPI Syntax:
        ```
        - POWer:GATing {OFF|SCREen|CURSor}
        - POWer:GATing?
        ```

    Info:
        - ``OFF`` turns off measurement gating (full record).
        - ``SCREen`` turns on gating, using the left and right edges of the screen.
        - ``CURSor`` limits measurements to the portion of the waveform between the vertical bar
          cursors, even if they are off screen.
    """


class PowerGatesource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:GATESOurce`` command.

    Description:
        - This command specifies the gate source for the power application.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:GATESOurce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:GATESOurce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:GATESOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:GATESOurce {CH<x>|REF<x>|NONe}
        - POWer:GATESOurce?
        ```

    Info:
        - ``CH<x>`` sets an analog channel as the gate source.
        - ``REF<x>`` sets a reference waveform as the gate source.
        - ``NONe`` is set when the gate source is not used in the application.
    """


class PowerDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:DISplay`` command.

    Description:
        - This command controls whether or not to display the power test results. This is the
          equivalent to pressing the Test button and then selecting the power application. The same
          control is provided for each application.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:DISplay value`` command.

    SCPI Syntax:
        ```
        - POWer:DISplay {OFF|ON|0|1}
        - POWer:DISplay?
        ```

    Info:
        - ``OFF`` or 0 turns off the display settings.
        - ``ON`` or 1 turns on the display settings.
    """


class PowerCurrentsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:CURRENTSOurce`` command.

    Description:
        - This command specifies the current source for the power application.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:CURRENTSOurce?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:CURRENTSOurce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:CURRENTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:CURRENTSOurce {CH<x>|REF<x>}
        - POWer:CURRENTSOurce?
        ```

    Info:
        - ``CH<x>`` sets an analog channel as the current source.
        - ``REF<x>`` sets a reference waveform as the current source.
    """


#  pylint: disable=too-many-instance-attributes
class Power(SCPICmdRead):
    """The ``POWer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.currentsource``: The ``POWer:CURRENTSOurce`` command.
        - ``.display``: The ``POWer:DISplay`` command.
        - ``.gatesource``: The ``POWer:GATESOurce`` command.
        - ``.gating``: The ``POWer:GATing`` command.
        - ``.harmonics``: The ``POWer:HARMonics`` command tree.
        - ``.indicators``: The ``POWer:INDICators`` command.
        - ``.modulation``: The ``POWer:MODulation`` command tree.
        - ``.quality``: The ``POWer:QUALity`` command tree.
        - ``.reflevel``: The ``POWer:REFLevel`` command tree.
        - ``.ripple``: The ``POWer:RIPPle`` command.
        - ``.soa``: The ``POWer:SOA`` command tree.
        - ``.statistics``: The ``POWer:STATIstics`` command.
        - ``.swloss``: The ``POWer:SWLoss`` command tree.
        - ``.type``: The ``POWer:TYPe`` command.
        - ``.voltagesource``: The ``POWer:VOLTAGESOurce`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "POWer") -> None:
        super().__init__(device, cmd_syntax)
        self._currentsource = PowerCurrentsource(device, f"{self._cmd_syntax}:CURRENTSOurce")
        self._display = PowerDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._gatesource = PowerGatesource(device, f"{self._cmd_syntax}:GATESOurce")
        self._gating = PowerGating(device, f"{self._cmd_syntax}:GATing")
        self._harmonics = PowerHarmonics(device, f"{self._cmd_syntax}:HARMonics")
        self._indicators = PowerIndicators(device, f"{self._cmd_syntax}:INDICators")
        self._modulation = PowerModulation(device, f"{self._cmd_syntax}:MODulation")
        self._quality = PowerQuality(device, f"{self._cmd_syntax}:QUALity")
        self._reflevel = PowerReflevel(device, f"{self._cmd_syntax}:REFLevel")
        self._ripple = PowerRipple(device, f"{self._cmd_syntax}:RIPPle")
        self._soa = PowerSoa(device, f"{self._cmd_syntax}:SOA")
        self._statistics = PowerStatistics(device, f"{self._cmd_syntax}:STATIstics")
        self._swloss = PowerSwloss(device, f"{self._cmd_syntax}:SWLoss")
        self._type = PowerType(device, f"{self._cmd_syntax}:TYPe")
        self._voltagesource = PowerVoltagesource(device, f"{self._cmd_syntax}:VOLTAGESOurce")

    @property
    def currentsource(self) -> PowerCurrentsource:
        """Return the ``POWer:CURRENTSOurce`` command.

        Description:
            - This command specifies the current source for the power application.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:CURRENTSOurce?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:CURRENTSOurce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:CURRENTSOurce value``
              command.

        SCPI Syntax:
            ```
            - POWer:CURRENTSOurce {CH<x>|REF<x>}
            - POWer:CURRENTSOurce?
            ```

        Info:
            - ``CH<x>`` sets an analog channel as the current source.
            - ``REF<x>`` sets a reference waveform as the current source.
        """
        return self._currentsource

    @property
    def display(self) -> PowerDisplay:
        """Return the ``POWer:DISplay`` command.

        Description:
            - This command controls whether or not to display the power test results. This is the
              equivalent to pressing the Test button and then selecting the power application. The
              same control is provided for each application.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:DISplay?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:DISplay value`` command.

        SCPI Syntax:
            ```
            - POWer:DISplay {OFF|ON|0|1}
            - POWer:DISplay?
            ```

        Info:
            - ``OFF`` or 0 turns off the display settings.
            - ``ON`` or 1 turns on the display settings.
        """
        return self._display

    @property
    def gatesource(self) -> PowerGatesource:
        """Return the ``POWer:GATESOurce`` command.

        Description:
            - This command specifies the gate source for the power application.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:GATESOurce?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:GATESOurce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:GATESOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:GATESOurce {CH<x>|REF<x>|NONe}
            - POWer:GATESOurce?
            ```

        Info:
            - ``CH<x>`` sets an analog channel as the gate source.
            - ``REF<x>`` sets a reference waveform as the gate source.
            - ``NONe`` is set when the gate source is not used in the application.
        """
        return self._gatesource

    @property
    def gating(self) -> PowerGating:
        """Return the ``POWer:GATing`` command.

        Description:
            - This command specifies the power application gating.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:GATing?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:GATing?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:GATing value`` command.

        SCPI Syntax:
            ```
            - POWer:GATing {OFF|SCREen|CURSor}
            - POWer:GATing?
            ```

        Info:
            - ``OFF`` turns off measurement gating (full record).
            - ``SCREen`` turns on gating, using the left and right edges of the screen.
            - ``CURSor`` limits measurements to the portion of the waveform between the vertical bar
              cursors, even if they are off screen.
        """
        return self._gating

    @property
    def harmonics(self) -> PowerHarmonics:
        """Return the ``POWer:HARMonics`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:HARMonics?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:HARMonics?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.display``: The ``POWer:HARMonics:DISplay`` command tree.
            - ``.freqref``: The ``POWer:HARMonics:FREQRef`` command.
            - ``.iec``: The ``POWer:HARMonics:IEC`` command tree.
            - ``.mil``: The ``POWer:HARMonics:MIL`` command tree.
            - ``.nr_harmonics``: The ``POWer:HARMonics:NR_HARMonics`` command.
            - ``.results``: The ``POWer:HARMonics:RESults`` command tree.
            - ``.source``: The ``POWer:HARMonics:SOURce`` command.
            - ``.standard``: The ``POWer:HARMonics:STANDard`` command.
        """
        return self._harmonics

    @property
    def indicators(self) -> PowerIndicators:
        """Return the ``POWer:INDICators`` command.

        Description:
            - This command specifies the state of the measurement indicators for the power
              application.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:INDICators?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:INDICators?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:INDICators value`` command.

        SCPI Syntax:
            ```
            - POWer:INDICators {OFF|ON|0|1}
            - POWer:INDICators?
            ```

        Info:
            - ``OFF`` or 0 turns off the measurement indicators.
            - ``ON`` or 1 turns on the measurement indicators.
        """
        return self._indicators

    @property
    def modulation(self) -> PowerModulation:
        """Return the ``POWer:MODulation`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:MODulation?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:MODulation?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``POWer:MODulation:SOUrce`` command.
            - ``.type``: The ``POWer:MODulation:TYPe`` command.
        """
        return self._modulation

    @property
    def quality(self) -> PowerQuality:
        """Return the ``POWer:QUALity`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:QUALity?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:QUALity?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.apppwr``: The ``POWer:QUALity:APPpwr`` command.
            - ``.display``: The ``POWer:QUALity:DISplay`` command tree.
            - ``.freqreference``: The ``POWer:QUALity:FREQREFerence`` command.
            - ``.frequency``: The ``POWer:QUALity:FREQuency`` command.
            - ``.icrestfactor``: The ``POWer:QUALity:ICRESTfactor`` command.
            - ``.irms``: The ``POWer:QUALity:IRMS`` command.
            - ``.phaseangle``: The ``POWer:QUALity:PHASEangle`` command.
            - ``.powerfactor``: The ``POWer:QUALity:POWERFACtor`` command.
            - ``.reactpwr``: The ``POWer:QUALity:REACTpwr`` command.
            - ``.truepwr``: The ``POWer:QUALity:TRUEpwr`` command.
            - ``.vcrestfactor``: The ``POWer:QUALity:VCRESTfactor`` command.
            - ``.vrms``: The ``POWer:QUALity:VRMS`` command.
        """
        return self._quality

    @property
    def reflevel(self) -> PowerReflevel:
        """Return the ``POWer:REFLevel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:REFLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:REFLevel?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.absolute``: The ``POWer:REFLevel:ABSolute`` command.
            - ``.hysteresis``: The ``POWer:REFLevel:HYSTeresis`` command.
            - ``.method``: The ``POWer:REFLevel:METHod`` command.
            - ``.percent``: The ``POWer:REFLevel:PERCent`` command.
        """
        return self._reflevel

    @property
    def ripple(self) -> PowerRipple:
        """Return the ``POWer:RIPPle`` command.

        Description:
            - This command performs a vertical autoset for ripple measurements or sets the vertical
              offset to 0.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:RIPPle value`` command.

        SCPI Syntax:
            ```
            - POWer:RIPPle {VERTAUTOset|VERTDEFault}
            ```

        Info:
            - ``VERTAUTOset`` automatically scales the source waveform to optimize ripple
              measurements.
            - ``VERTDEFault`` sets the vertical offset of the source waveform to 0 volts (for
              voltage source) or 0 amperes (for current source).

        Sub-properties:
            - ``.results``: The ``POWer:RIPPle:RESults`` command tree.
            - ``.source``: The ``POWer:RIPPle:SOUrce`` command.
        """
        return self._ripple

    @property
    def soa(self) -> PowerSoa:
        """Return the ``POWer:SOA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SOA?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SOA?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.linear``: The ``POWer:SOA:LINear`` command tree.
            - ``.log``: The ``POWer:SOA:LOG`` command tree.
            - ``.mask``: The ``POWer:SOA:MASK`` command tree.
            - ``.plottype``: The ``POWer:SOA:PLOTTYPe`` command.
            - ``.result``: The ``POWer:SOA:RESult`` command tree.
        """
        return self._soa

    @property
    def statistics(self) -> PowerStatistics:
        """Return the ``POWer:STATIstics`` command.

        Description:
            - Clears all the accumulated statistics of all measurements. Performs the same function
              as the ``MEASUREMENT:STATISTICS`` command.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:STATIstics value`` command.

        SCPI Syntax:
            ```
            - POWer:STATIstics {RESET}
            ```

        Info:
            - ``RESET`` clears the measurement statistics.

        Sub-properties:
            - ``.mode``: The ``POWer:STATIstics:MODe`` command.
            - ``.weighting``: The ``POWer:STATIstics:WEIghting`` command.
        """
        return self._statistics

    @property
    def swloss(self) -> PowerSwloss:
        """Return the ``POWer:SWLoss`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:SWLoss?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:SWLoss?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condcalcmethod``: The ``POWer:SWLoss:CONDCALCmethod`` command.
            - ``.conduction``: The ``POWer:SWLoss:CONDuction`` command tree.
            - ``.display``: The ``POWer:SWLoss:DISplay`` command.
            - ``.gate``: The ``POWer:SWLoss:GATe`` command tree.
            - ``.numcycles``: The ``POWer:SWLoss:NUMCYCles`` command.
            - ``.rdson``: The ``POWer:SWLoss:RDSon`` command.
            - ``.reflevel``: The ``POWer:SWLoss:REFLevel`` command tree.
            - ``.toff``: The ``POWer:SWLoss:TOFF`` command tree.
            - ``.ton``: The ``POWer:SWLoss:TON`` command tree.
            - ``.total``: The ``POWer:SWLoss:TOTal`` command tree.
            - ``.vcesat``: The ``POWer:SWLoss:VCEsat`` command.
        """
        return self._swloss

    @property
    def type(self) -> PowerType:
        """Return the ``POWer:TYPe`` command.

        Description:
            - This command specifies the power application measurement type.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:TYPe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:TYPe value`` command.

        SCPI Syntax:
            ```
            - POWer:TYPe {NONe|QUALity|SWITCHingloss|SOA|HARMonics|RIPPle|MODULationanalysis|DESKew}
            - POWer:TYPe?
            ```

        Info:
            - ``NONe`` Use to set the measurement type to None.
            - ``QUALity`` Use the power quality functions to obtain measurements and statistics
              about the general power quality in your test circuit.
            - ``SWITCHingloss`` Use the switching loss functions to obtain the power loss and energy
              loss across the acquired waveform, including turn-on loss, turn-off loss, conduction
              loss, and total loss. Typically, use these functions to characterize losses in power
              supply switching devices, as they switch on and off.
            - ``SOA`` Use the safe operating functions to obtain an X-Y display of the switching
              device-under-test's voltage and current. Also use them to perform a mask test of the
              X-Y signal relative to the graphical X-Y description of the device specification
              table. The safe operating area is typically the voltage and current values that a
              semiconductor can operate without damaging itself.
            - ``HARMonics`` Use the harmonics functions to obtain the frequency spectrum of the
              source waveform and associated measurement values. Harmonic measurements can help one
              perform in-depth troubleshooting of power quality problems.
            - ``RIPPle`` Use the ripple functions to obtain measurements and statistics for the AC
              components of the acquired waveform. Ripples are often found on top of a large DC
              signal.
            - ``MODULationanalysis`` Use the modulation functions to obtain a trend plot of a
              measurement value across the acquired waveform. This is useful for showing the
              variations in the modulated switching signal.
            - ``DESKew`` Run the deskew procedure to match the delays through the probes. Different
              probes introduce different delays between the probe tip and the oscilloscope. Many
              oscilloscope users do not have to worry about this because they use the same type of
              probe on all channels. Power measurement users, however, frequently use both a voltage
              probe and a current probe. A current probe typically has a larger delay than a voltage
              probe, so setting deskew values becomes important.
        """
        return self._type

    @property
    def voltagesource(self) -> PowerVoltagesource:
        """Return the ``POWer:VOLTAGESOurce`` command.

        Description:
            - This command specifies the voltage source for the power application.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:VOLTAGESOurce?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:VOLTAGESOurce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``POWer:VOLTAGESOurce value``
              command.

        SCPI Syntax:
            ```
            - POWer:VOLTAGESOurce {CH<x>|REF<x>}
            - POWer:VOLTAGESOurce?
            ```

        Info:
            - ``CH<x>`` sets the analog channel as the voltage source.
            - ``REF<x>`` sets the reference waveform as the voltage source.
        """
        return self._voltagesource
