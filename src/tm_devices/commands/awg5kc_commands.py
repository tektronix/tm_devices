"""The AWG5KC commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_32dszm_awg.awgcontrol import Awgcontrol
from .gen_32dszm_awg.diagnostic import Diagnostic
from .gen_32dszm_awg.display import Display
from .gen_32dszm_awg.event import Event
from .gen_32dszm_awg.instrument import Instrument
from .gen_32dszm_awg.mmemory import Mmemory
from .gen_32dszm_awg.output import OutputItem
from .gen_32dszm_awg.sequence import Sequence
from .gen_32dszm_awg.slist import Slist
from .gen_32dszm_awg.source import SourceItem
from .gen_32dszm_awg.status import Status
from .gen_32dszm_awg.system import System
from .gen_32dszm_awg.trigger import Trigger
from .gen_32dszm_awg.wlist import Wlist
from .gen_33ijgq_afgawg.abort import Abort
from .gen_33ijgq_afgawg.calibration import Calibration
from .gen_fsksdy_lpdmsotekscopepcdpomdoafgawgdsa.miscellaneous import Idn, Tst
from .gen_fsksdy_lpdmsotekscopepcdpomdoafgawgdsa.status_and_error import (
    Cls,
    Esr,
    Opc,
    Rst,
    Stb,
    Wai,
)
from .gen_fst7sp_lpdmsotekscopepcmdodpoafgawgdsa.status_and_error import Opt
from .gen_ft5uww_lpdmsodpomdoafgawgdsa.calibration import Cal
from .gen_ft5uww_lpdmsodpomdoafgawgdsa.miscellaneous import Trg
from .gen_fu6dog_lpdmsotekscopepcdpomdoawgdsa.status_and_error import Ese, Sre
from .helpers import DefaultDictPassKeyToFactory


# pylint: disable=too-few-public-methods
class AWG5KCCommandConstants:
    """The AWG5KC command argument constants.

    This provides access to all the string constants which can be used as arguments for AWG5KC
    commands.
    """

    CONTINUOUS = "CONTINUOUS"  # CONTinuous
    ENHANCED = "ENHANCED"  # ENHanced
    EVENT_PATTERN = "EVENT_PATTERN"  # event_pattern
    FIRST = "FIRST"  # FIRSt
    FIXED = "FIXED"  # FIXed
    GATED = "GATED"  # GATed
    INDEX = "INDEX"  # INDex
    JUMP_MODE = "JUMP_MODE"  # jump_mode
    JUMP_TARGET = "JUMP_TARGET"  # jump_target
    LAST = "LAST"
    NEGATIVE = "NEGATIVE"  # NEGative
    NEXT = "NEXT"
    OFF = "OFF"
    POSITIVE = "POSITIVE"  # POSitive
    SEQUENCE = "SEQUENCE"  # SEQuence
    TRIGGERED = "TRIGGERED"  # TRIGgered
    VARIABLE = "VARIABLE"  # VARiable


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class AWG5KCCommands:
    """The AWG5KC commands.

    This provides access to all the commands for the AWG5KC device. See the documentation of each
    property for more usage information.

    Properties:
        - ``.abort``: The ``ABORt`` command.
        - ``.awgcontrol``: The ``AWGControl`` command tree.
        - ``.cal``: The ``*CAL`` command.
        - ``.calibration``: The ``CALibration`` command tree.
        - ``.cls``: The ``*CLS`` command.
        - ``.diagnostic``: The ``DIAGnostic`` command tree.
        - ``.display``: The ``DISPlay`` command tree.
        - ``.ese``: The ``*ESE`` command.
        - ``.esr``: The ``*ESR`` command.
        - ``.event``: The ``EVENt`` command tree.
        - ``.idn``: The ``*IDN`` command.
        - ``.instrument``: The ``INSTrument`` command tree.
        - ``.mmemory``: The ``MMEMory`` command tree.
        - ``.opc``: The ``*OPC`` command.
        - ``.opt``: The ``*OPT`` command.
        - ``.output``: The ``OUTPut[n]`` command tree.
        - ``.rst``: The ``*RST`` command.
        - ``.sequence``: The ``SEQuence`` command tree.
        - ``.slist``: The ``SLISt`` command tree.
        - ``.source``: The ``SOURce[n]`` command tree.
        - ``.sre``: The ``*SRE`` command.
        - ``.status``: The ``STATus`` command tree.
        - ``.stb``: The ``*STB`` command.
        - ``.system``: The ``SYSTem`` command tree.
        - ``.trg``: The ``*TRG`` command.
        - ``.trigger``: The ``TRIGger`` command tree.
        - ``.tst``: The ``*TST`` command.
        - ``.wai``: The ``*WAI`` command.
        - ``.wlist``: The ``WLISt`` command tree.
    """

    def __init__(self, device: Optional[PIControl] = None) -> None:
        self._abort = Abort(device)
        self._awgcontrol = Awgcontrol(device)
        self._cal = Cal(device)
        self._calibration = Calibration(device)
        self._cls = Cls(device)
        self._diagnostic = Diagnostic(device)
        self._display = Display(device)
        self._ese = Ese(device)
        self._esr = Esr(device)
        self._event = Event(device)
        self._idn = Idn(device)
        self._instrument = Instrument(device)
        self._mmemory = Mmemory(device)
        self._opc = Opc(device)
        self._opt = Opt(device)
        self._output: Dict[int, OutputItem] = DefaultDictPassKeyToFactory(
            lambda x: OutputItem(device, f"OUTPut{x}")
        )
        self._rst = Rst(device)
        self._sequence = Sequence(device)
        self._slist = Slist(device)
        self._source: Dict[int, SourceItem] = DefaultDictPassKeyToFactory(
            lambda x: SourceItem(device, f"SOURce{x}")
        )
        self._sre = Sre(device)
        self._status = Status(device)
        self._stb = Stb(device)
        self._system = System(device)
        self._trg = Trg(device)
        self._trigger = Trigger(device)
        self._tst = Tst(device)
        self._wai = Wai(device)
        self._wlist = Wlist(device)

    @property
    def abort(self) -> Abort:
        """Return the ``ABORt`` command.

        Description:
            - Initializes all the current trigger system parameters and resets all trigger
              sequences.

        Usage:
            - Using the ``.write()`` method will send the ``ABORt`` command.

        SCPI Syntax:
            ```
            - ABORt
            ```
        """
        return self._abort

    @property
    def awgcontrol(self) -> Awgcontrol:
        """Return the ``AWGControl`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.application``: The ``AWGControl:APPLication`` command tree.
            - ``.clock``: The ``AWGControl:CLOCk`` command tree.
            - ``.compile``: The ``AWGControl:COMPile`` command.
            - ``.configure``: The ``AWGControl:CONFigure`` command tree.
            - ``.dc``: The ``AWGControl:DC[n]`` command tree.
            - ``.doutput``: The ``AWGControl:DOUTput[n]`` command tree.
            - ``.enhanced``: The ``AWGControl:ENHanced`` command tree.
            - ``.event``: The ``AWGControl:EVENt`` command tree.
            - ``.interleave``: The ``AWGControl:INTerleave`` command tree.
            - ``.rmode``: The ``AWGControl:RMODe`` command.
            - ``.rrate``: The ``AWGControl:RRATe`` command.
            - ``.rstate``: The ``AWGControl:RSTate`` command.
            - ``.run``: The ``AWGControl:RUN`` command tree.
            - ``.sequencer``: The ``AWGControl:SEQuencer`` command tree.
            - ``.sname``: The ``AWGControl:SNAMe`` command.
            - ``.srestore``: The ``AWGControl:SREStore`` command.
            - ``.ssave``: The ``AWGControl:SSAVe`` command.
            - ``.stop``: The ``AWGControl:STOP`` command tree.
        """
        return self._awgcontrol

    @property
    def cal(self) -> Cal:
        """Return the ``*CAL`` command.

        Description:
            - This query-only command starts signal path calibration (SPC) and returns the status
              upon completion.

        Usage:
            - Using the ``.query()`` method will send the ``*CAL?`` query.
            - Using the ``.verify(value)`` method will send the ``*CAL?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - *CAL?
            ```
        """
        return self._cal

    @property
    def calibration(self) -> Calibration:
        """Return the ``CALibration`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.all``: The ``CALibration:ALL`` command.
        """
        return self._calibration

    @property
    def cls(self) -> Cls:
        """Return the ``*CLS`` command.

        Description:
            - This command (no query form) clears the following: Event Queue Standard Event Status
              Register Status Byte Register (except the MAV bit) If the ``*CLS`` command immediately
              follows an <EOI>, the Output Queue and MAV bit (Status Byte Register bit 4) are also
              cleared. MAV indicates that information is in the output queue. The device clear (DCL)
              control message will clear the output queue and thus MAV. ``*CLS`` does not clear the
              output queue or MAV. ``*CLS`` can suppress a Service Request that is to be generated
              by an ``*OPC``. This will happen if a single sequence acquisition operation is still
              being processed when the ``*CLS`` command is executed.

        Usage:
            - Using the ``.write()`` method will send the ``*CLS`` command.

        SCPI Syntax:
            ```
            - *CLS
            ```
        """
        return self._cls

    @property
    def diagnostic(self) -> Diagnostic:
        """Return the ``DIAGnostic`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``DIAGnostic:DATA`` command.
            - ``.select``: The ``DIAGnostic:SELect`` command.
            - ``.immediate``: The ``DIAGnostic:IMMediate`` command.
        """
        return self._diagnostic

    @property
    def display(self) -> Display:
        """Return the ``DISPlay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.window1``: The ``DISPlay:WINDow1`` command tree.
            - ``.window2``: The ``DISPlay:WINDow2`` command tree.
        """
        return self._display

    @property
    def ese(self) -> Ese:
        """Return the ``*ESE`` command.

        Description:
            - This command sets and queries the bits in the Event Status Enable Register (ESER). The
              ESER prevents events from being reported to the Status Byte Register (STB). For a more
              detailed discussion of the use of these registers, see Registers.

        Usage:
            - Using the ``.query()`` method will send the ``*ESE?`` query.
            - Using the ``.verify(value)`` method will send the ``*ESE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``*ESE value`` command.

        SCPI Syntax:
            ```
            - *ESE <NR1>
            - *ESE?
            ```

        Info:
            - ``<NR1>`` specifies the binary bits of the ESER according to this value, which ranges
              from 0 through 255.
        """
        return self._ese

    @property
    def esr(self) -> Esr:
        """Return the ``*ESR`` command.

        Description:
            - This query-only command returns the contents of the Standard Event Status Register
              (SESR). ``*ESR?`` also clears the SESR (since reading the SESR clears it). For a more
              detailed discussion of the use of these registers, see Registers.

        Usage:
            - Using the ``.query()`` method will send the ``*ESR?`` query.
            - Using the ``.verify(value)`` method will send the ``*ESR?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - *ESR?
            ```
        """
        return self._esr

    @property
    def event(self) -> Event:
        """Return the ``EVENt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``EVENt?`` query.
            - Using the ``.verify(value)`` method will send the ``EVENt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.impedance``: The ``EVENt:IMPedance`` command.
            - ``.jtiming``: The ``EVENt:JTIMing`` command.
            - ``.level``: The ``EVENt:LEVel`` command.
            - ``.polarity``: The ``EVENt:POLarity`` command.
            - ``.immediate``: The ``EVENt:IMMediate`` command.
        """
        return self._event

    @property
    def idn(self) -> Idn:
        """Return the ``*IDN`` command.

        Description:
            - This query-only command returns the instrument identification code.

        Usage:
            - Using the ``.query()`` method will send the ``*IDN?`` query.
            - Using the ``.verify(value)`` method will send the ``*IDN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - *IDN?
            ```
        """
        return self._idn

    @property
    def instrument(self) -> Instrument:
        """Return the ``INSTrument`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``INSTrument?`` query.
            - Using the ``.verify(value)`` method will send the ``INSTrument?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.couple``: The ``INSTrument:COUPle`` command tree.
        """
        return self._instrument

    @property
    def mmemory(self) -> Mmemory:
        """Return the ``MMEMory`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.catalog``: The ``MMEMory:CATalog`` command.
            - ``.cdirectory``: The ``MMEMory:CDIRectory`` command.
            - ``.data``: The ``MMEMory:DATA`` command.
            - ``.delete``: The ``MMEMory:DELete`` command.
            - ``.export``: The ``MMEMory:EXPort`` command.
            - ``.import``: The ``MMEMory:IMPort`` command.
            - ``.mdirectory``: The ``MMEMory:MDIRectory`` command.
            - ``.msis``: The ``MMEMory:MSIS`` command.
        """
        return self._mmemory

    @property
    def opc(self) -> Opc:
        """Return the ``*OPC`` command.

        Description:
            - This command generates the operation complete message in the Standard Event Status
              Register (SESR) when all pending commands that generate an OPC message are complete.
              The ``*OPC?`` query places the ASCII character '1' into the output queue when all such
              OPC commands are complete. The ``*OPC?`` response is not available to read until all
              pending operations finish. For a complete discussion of the use of these registers and
              the output queue, see Registers and Queues. The ``*OPC`` command allows you to
              synchronize the operation of the instrument with your application program. For more
              information, see Synchronization Methods. Refer to the Oscilloscope operations that
              can generate OPC table for a list of commands that generate an OPC message.

        Usage:
            - Using the ``.query()`` method will send the ``*OPC?`` query.
            - Using the ``.verify(value)`` method will send the ``*OPC?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``*OPC`` command.

        SCPI Syntax:
            ```
            - *OPC
            - *OPC?
            ```
        """
        return self._opc

    @property
    def opt(self) -> Opt:
        """Return the ``*OPT`` command.

        Description:
            - This query-only command returns a comma separated list of installed options as an
              arbitrary ASCII string (no quotes) of the form:
              ``<optionCode>:<optionDescription>``,``<optionCode>:<optionDescription>``... The last
              section of each entry (the text following the last hyphen) indicates the license type.
              If no options are found, NONE is returned.

        Usage:
            - Using the ``.query()`` method will send the ``*OPT?`` query.
            - Using the ``.verify(value)`` method will send the ``*OPT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - *OPT?
            ```
        """
        return self._opt

    @property
    def output(self) -> Dict[int, OutputItem]:
        """Return the ``OUTPut[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.filter``: The ``OUTPut[n]:FILTer`` command tree.
            - ``.state``: The ``OUTPut[n]:STATe`` command.
        """
        return self._output

    @property
    def rst(self) -> Rst:
        """Return the ``*RST`` command.

        Description:
            - This command (no query form) resets the instrument to the factory default settings.
              This command does the following: Recalls the default instrument setup. Clears the
              current ``*DDT`` command. Disables aliases (``:ALIAS:STATE 0``). Disables the user
              password (for the ``*PUD`` command). The ``*RST`` command does not change the
              following: The current working directory ( ``:FILESystem:CWD`` command). The state of
              command headers ( ``:HEADer`` command). The state of keyword and enumeration verbosity
              ( ``:VERBose`` command). The Power-on Status Clear Flag ( ``*PSC`` command). The Event
              Status Enable Register ( ``*ESE`` command). The Service Request Enable Register (
              ``*SRE`` command). The Device Event Status Enable Register ( DESE command). The user
              password for protected user data ( ``:PASSWord`` command). The content of protected
              user data ( ``*PUD`` command). The enabled state of the socket server (
              ``:SOCKETServer:ENAble`` command). The socket server port number (
              ``:SOCKETServer:PORT`` command). The socket server protocol (
              ``:SOCKETServer:PROTOCol`` command). The USBTMC port configuration (
              ``:USBDevice:CONFigure`` command). The destination reference waveform or file path for
              the ``:CURVe`` command ( ``:DATa:DESTination`` command). The source waveform for the
              ``:CURVe?`` or ``:WAVFrm?`` queries ( ``:DATa:SOUrce`` command). The waveform data
              encoding for the ``:CURVe`` command or query or the ``:WAVFrm?`` query (
              ``:DATa:ENCdg`` command). The starting point for ``:CURVe?`` queries ( ``:DATa:STARt``
              command). The ending point for ``:CURVe?`` queries ( ``:DATa:STOP`` command). All
              settings associated the ``:WFMInpre`` commands. All user settable settings associated
              with the WFMOutpre commands. ``*RST`` only resets the programmable interface settings,
              it does not change the user interface settings.

        Usage:
            - Using the ``.write()`` method will send the ``*RST`` command.

        SCPI Syntax:
            ```
            - *RST
            ```
        """
        return self._rst

    @property
    def sequence(self) -> Sequence:
        """Return the ``SEQuence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence?`` query.
            - Using the ``.verify(value)`` method will send the ``SEQuence?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.element``: The ``SEQuence:ELEMent[n]`` command tree.
            - ``.jump``: The ``SEQuence:JUMP`` command tree.
            - ``.length``: The ``SEQuence:LENGth`` command.
        """
        return self._sequence

    @property
    def slist(self) -> Slist:
        """Return the ``SLISt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.name``: The ``SLISt:NAME`` command.
            - ``.size``: The ``SLISt:SIZE`` command.
            - ``.subsequence``: The ``SLISt:SUBSequence`` command tree.
        """
        return self._slist

    @property
    def source(self) -> Dict[int, SourceItem]:
        """Return the ``SOURce[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``SOURce[n]:FREQuency`` command tree.
            - ``.roscillator``: The ``SOURce[n]:ROSCillator`` command tree.
            - ``.combine``: The ``SOURce[n]:COMBine`` command tree.
            - ``.dac``: The ``SOURce[n]:DAC`` command tree.
            - ``.delay``: The ``SOURce[n]:DELay`` command tree.
            - ``.digital``: The ``SOURce[n]:DIGital`` command tree.
            - ``.function``: The ``SOURce[n]:FUNCtion`` command tree.
            - ``.marker1``: The ``SOURce[n]:MARKer1`` command tree.
            - ``.marker2``: The ``SOURce[n]:MARKer2`` command tree.
            - ``.pdelay``: The ``SOURce[n]:PDELay`` command tree.
            - ``.phase``: The ``SOURce[n]:PHASe`` command tree.
            - ``.skew``: The ``SOURce[n]:SKEW`` command.
            - ``.voltage``: The ``SOURce[n]:VOLTage`` command tree.
            - ``.waveform``: The ``SOURce[n]:WAVeform`` command.
        """
        return self._source

    @property
    def sre(self) -> Sre:
        """Return the ``*SRE`` command.

        Description:
            - The ``*SRE`` (Service Request Enable) command sets and queries the bits in the Service
              Request Enable Register. For more information, refer to Registers.

        Usage:
            - Using the ``.query()`` method will send the ``*SRE?`` query.
            - Using the ``.verify(value)`` method will send the ``*SRE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``*SRE value`` command.

        SCPI Syntax:
            ```
            - *SRE <NR1>
            - *SRE?
            ```

        Info:
            - ``<NR1>`` is a value in the range from 0 through 255. The binary bits of the SRER are
              set according to this value. Using an out-of-range value causes an execution error.
              The power-on default for SRER is 0 if ``*PSC`` is 1. If ``*PSC`` is 0, the SRER
              maintains the previous power cycle value through the current power cycle.
        """
        return self._sre

    @property
    def status(self) -> Status:
        """Return the ``STATus`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``STATus?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.operation``: The ``STATus:OPERation`` command tree.
            - ``.preset``: The ``STATus:PRESet`` command.
            - ``.questionable``: The ``STATus:QUEStionable`` command tree.
        """
        return self._status

    @property
    def stb(self) -> Stb:
        """Return the ``*STB`` command.

        Description:
            - The ``*STB?`` (Read Status Byte) query returns the contents of the Status Byte
              Register (SBR) using the Master Summary Status (MSS) bit. For more information, refer
              to Registers.

        Usage:
            - Using the ``.query()`` method will send the ``*STB?`` query.
            - Using the ``.verify(value)`` method will send the ``*STB?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - *STB?
            ```
        """
        return self._stb

    @property
    def system(self) -> System:
        """Return the ``SYSTem`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.date``: The ``SYSTem:DATE`` command.
            - ``.error``: The ``SYSTem:ERRor`` command tree.
            - ``.klock``: The ``SYSTem:KLOCk`` command.
            - ``.time``: The ``SYSTem:TIME`` command.
            - ``.version``: The ``SYSTem:VERSion`` command.
        """
        return self._system

    @property
    def trg(self) -> Trg:
        """Return the ``*TRG`` command.

        Description:
            - Performs a group execute trigger on commands defined by ``*DDT``.

        Usage:
            - Using the ``.write()`` method will send the ``*TRG`` command.

        SCPI Syntax:
            ```
            - *TRG
            ```
        """
        return self._trg

    @property
    def trigger(self) -> Trigger:
        """Return the ``TRIGger`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.sequence``: The ``TRIGger:SEQuence`` command tree.
        """
        return self._trigger

    @property
    def tst(self) -> Tst:
        """Return the ``*TST`` command.

        Description:
            - Tests (self-test) the interface and returns a 0.

        Usage:
            - Using the ``.query()`` method will send the ``*TST?`` query.
            - Using the ``.verify(value)`` method will send the ``*TST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - *TST?
            ```
        """
        return self._tst

    @property
    def wai(self) -> Wai:
        """Return the ``*WAI`` command.

        Description:
            - The ``*WAI`` (Wait) command (no query form) prevents the instrument from executing
              further commands or queries until all pending commands that generate an OPC message
              are complete. This command allows you to synchronize the operation of the instrument
              with your application program. For more information, refer to Synchronization Methods.

        Usage:
            - Using the ``.write()`` method will send the ``*WAI`` command.

        SCPI Syntax:
            ```
            - *WAI
            ```
        """
        return self._wai

    @property
    def wlist(self) -> Wlist:
        """Return the ``WLISt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.name``: The ``WLISt:NAME`` command.
            - ``.size``: The ``WLISt:SIZE`` command.
            - ``.waveform``: The ``WLISt:WAVeform`` command tree.
        """
        return self._wlist


class AWG5KCMixin:
    """A mixin that provides access to the AWG5KC commands and constants.

    Properties:
        - ``.command_argument_constants``: The AWG5KC command argument constants.
        - ``.commands``: The AWG5KC commands.
    """

    @cached_property
    def command_argument_constants(self) -> AWG5KCCommandConstants:  # pylint: disable=no-self-use
        """Return the AWG5KC command argument constants.

        This provides access to all the string constants which can be used as arguments for AWG5KC
        commands.
        """
        return AWG5KCCommandConstants()

    @cached_property
    def commands(self) -> AWG5KCCommands:
        """Return the AWG5KC commands.

        This provides access to all the commands for the AWG5KC device. See the documentation of
        each sub-property for more usage information.

        Sub-properties:
            - ``.abort``: The ``ABORt`` command.
            - ``.awgcontrol``: The ``AWGControl`` command tree.
            - ``.cal``: The ``*CAL`` command.
            - ``.calibration``: The ``CALibration`` command tree.
            - ``.cls``: The ``*CLS`` command.
            - ``.diagnostic``: The ``DIAGnostic`` command tree.
            - ``.display``: The ``DISPlay`` command tree.
            - ``.ese``: The ``*ESE`` command.
            - ``.esr``: The ``*ESR`` command.
            - ``.event``: The ``EVENt`` command tree.
            - ``.idn``: The ``*IDN`` command.
            - ``.instrument``: The ``INSTrument`` command tree.
            - ``.mmemory``: The ``MMEMory`` command tree.
            - ``.opc``: The ``*OPC`` command.
            - ``.opt``: The ``*OPT`` command.
            - ``.output``: The ``OUTPut[n]`` command tree.
            - ``.rst``: The ``*RST`` command.
            - ``.sequence``: The ``SEQuence`` command tree.
            - ``.slist``: The ``SLISt`` command tree.
            - ``.source``: The ``SOURce[n]`` command tree.
            - ``.sre``: The ``*SRE`` command.
            - ``.status``: The ``STATus`` command tree.
            - ``.stb``: The ``*STB`` command.
            - ``.system``: The ``SYSTem`` command tree.
            - ``.trg``: The ``*TRG`` command.
            - ``.trigger``: The ``TRIGger`` command tree.
            - ``.tst``: The ``*TST`` command.
            - ``.wai``: The ``*WAI`` command.
            - ``.wlist``: The ``WLISt`` command tree.
        """
        device = self if isinstance(self, PIControl) else None
        return AWG5KCCommands(device)
