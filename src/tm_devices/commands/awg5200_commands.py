"""The AWG5200 commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_2i1z2s_awg.abort import Abort
from .gen_2i1z2s_awg.auxoutput import AuxoutputItem
from .gen_2i1z2s_awg.awgcontrol import Awgcontrol
from .gen_2i1z2s_awg.bwaveform import Bwaveform
from .gen_2i1z2s_awg.clock import Clock
from .gen_2i1z2s_awg.cplayback import Cplayback
from .gen_2i1z2s_awg.diagnostic import Diagnostic
from .gen_2i1z2s_awg.fgen import Fgen
from .gen_2i1z2s_awg.instrument import Instrument
from .gen_2i1z2s_awg.mmemory import Mmemory
from .gen_2i1z2s_awg.output import OutputItem
from .gen_2i1z2s_awg.source import Source, SourceItem
from .gen_2i1z2s_awg.synchronize import Synchronize
from .gen_2i1z2s_awg.system import System
from .gen_2i1z2s_awg.trigger import Trigger
from .gen_2i1z2s_awg.wlist import Wlist
from .gen_3n9auv_awg.active import Active
from .gen_3n9auv_awg.calibration import Calibration
from .gen_3n9auv_awg.connectivity import Connectivity
from .gen_3n9auv_awg.display import Display
from .gen_3n9auv_awg.output import Output
from .gen_3n9auv_awg.slist import Slist
from .gen_3n9auv_awg.status import Status
from .gen_3n9auv_awg.wplugin import Wplugin
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
class AWG5200CommandConstants:
    """The AWG5200 command argument constants.

    This provides access to all the string constants which can be used as arguments for AWG5200
    commands.
    """

    ATRIGGER = "ATRIGGER"  # ATRigger
    AWG = "AWG"
    CALIBRATION = "CALIBRATION"  # CALibration
    CONTINUOUS = "CONTINUOUS"  # CONTinuous
    COUNT = "COUNT"  # COUNt
    DCHB = "DCHB"
    DIAGNOSTIC = "DIAGNOSTIC"  # DIAGnostic
    END = "END"
    FALLING = "FALLING"  # FALLing
    FIRST = "FIRST"  # FIRSt
    ITRIGGER = "ITRIGGER"  # ITRigger
    NCHANGE = "NCHANGE"  # NCHange
    NORMAL = "NORMAL"  # NORMal
    OFF = "OFF"
    ONCE = "ONCE"
    POSITIVE = "POSITIVE"  # POSitive
    RISING = "RISING"  # RISing
    SYNCHRONOUS = "SYNCHRONOUS"  # SYNChronous


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class AWG5200Commands:
    """The AWG5200 commands.

    This provides access to all the commands for the AWG5200 device. See the documentation of each
    property for more usage information.

    Properties:
        - ``.abort``: The ``ABORt`` command.
        - ``.active``: The ``ACTive`` command tree.
        - ``.auxoutput``: The ``AUXoutput[n]`` command tree.
        - ``.awgcontrol``: The ``AWGControl`` command tree.
        - ``.bwaveform``: The ``BWAVeform`` command tree.
        - ``.cal``: The ``*CAL`` command.
        - ``.calibration``: The ``CALibration`` command tree.
        - ``.clock``: The ``CLOCk`` command tree.
        - ``.cls``: The ``*CLS`` command.
        - ``.connectivity``: The ``CONNectivity`` command tree.
        - ``.cplayback``: The ``CPLayback`` command tree.
        - ``.diagnostic``: The ``DIAGnostic`` command tree.
        - ``.display``: The ``DISPlay`` command tree.
        - ``.ese``: The ``*ESE`` command.
        - ``.esr``: The ``*ESR`` command.
        - ``.fgen``: The ``FGEN`` command tree.
        - ``.idn``: The ``*IDN`` command.
        - ``.instrument``: The ``INSTrument`` command tree.
        - ``.mmemory``: The ``MMEMory`` command tree.
        - ``.opc``: The ``*OPC`` command.
        - ``.opt``: The ``*OPT`` command.
        - ``.output``: The ``OUTPut`` command tree.
        - ``.outputx``: The ``OUTPut[n]`` command tree.
        - ``.rst``: The ``*RST`` command.
        - ``.slist``: The ``SLISt`` command tree.
        - ``.source``: The ``SOURce`` command tree.
        - ``.sourcex``: The ``SOURce[n]`` command tree.
        - ``.sre``: The ``*SRE`` command.
        - ``.status``: The ``STATus`` command tree.
        - ``.stb``: The ``*STB`` command.
        - ``.synchronize``: The ``SYNChronize`` command tree.
        - ``.system``: The ``SYSTem`` command tree.
        - ``.trg``: The ``*TRG`` command.
        - ``.trigger``: The ``TRIGger`` command tree.
        - ``.tst``: The ``*TST`` command.
        - ``.wai``: The ``*WAI`` command.
        - ``.wlist``: The ``WLISt`` command tree.
        - ``.wplugin``: The ``WPLugin`` command tree.
    """

    def __init__(self, device: Optional[PIControl] = None) -> None:
        self._abort = Abort(device)
        self._active = Active(device)
        self._auxoutput: Dict[int, AuxoutputItem] = DefaultDictPassKeyToFactory(
            lambda x: AuxoutputItem(device, f"AUXoutput{x}")
        )
        self._awgcontrol = Awgcontrol(device)
        self._bwaveform = Bwaveform(device)
        self._cal = Cal(device)
        self._calibration = Calibration(device)
        self._clock = Clock(device)
        self._cls = Cls(device)
        self._connectivity = Connectivity(device)
        self._cplayback = Cplayback(device)
        self._diagnostic = Diagnostic(device)
        self._display = Display(device)
        self._ese = Ese(device)
        self._esr = Esr(device)
        self._fgen = Fgen(device)
        self._idn = Idn(device)
        self._instrument = Instrument(device)
        self._mmemory = Mmemory(device)
        self._opc = Opc(device)
        self._opt = Opt(device)
        self._output = Output(device)
        self._outputx: Dict[int, OutputItem] = DefaultDictPassKeyToFactory(
            lambda x: OutputItem(device, f"OUTPut{x}")
        )
        self._rst = Rst(device)
        self._slist = Slist(device)
        self._source = Source(device)
        self._sourcex: Dict[int, SourceItem] = DefaultDictPassKeyToFactory(
            lambda x: SourceItem(device, f"SOURce{x}")
        )
        self._sre = Sre(device)
        self._status = Status(device)
        self._stb = Stb(device)
        self._synchronize = Synchronize(device)
        self._system = System(device)
        self._trg = Trg(device)
        self._trigger = Trigger(device)
        self._tst = Tst(device)
        self._wai = Wai(device)
        self._wlist = Wlist(device)
        self._wplugin = Wplugin(device)

    @property
    def abort(self) -> Abort:
        """Return the ``ABORt`` command.

        Description:
            - This command stops waveform playout when the Run Mode is set to Gated. This is
              equivalent to releasing the Force Trig button on the front panel when the instrument
              is in gated mode.

        Usage:
            - Using the ``.write(value)`` method will send the ``ABORt value`` command.

        SCPI Syntax:
            ```
            - ABORt [{ATRigger|BTRigger}]
            ```
        """
        return self._abort

    @property
    def active(self) -> Active:
        """Return the ``ACTive`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTive?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTive?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``ACTive:MODE`` command.
        """
        return self._active

    @property
    def auxoutput(self) -> Dict[int, AuxoutputItem]:
        """Return the ``AUXoutput[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXoutput[n]?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXoutput[n]?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``AUXoutput[n]:SOURce`` command.
        """
        return self._auxoutput

    @property
    def awgcontrol(self) -> Awgcontrol:
        """Return the ``AWGControl`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AWGControl?`` query.
            - Using the ``.verify(value)`` method will send the ``AWGControl?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.arsettings``: The ``AWGControl:ARSettings`` command.
            - ``.clock``: The ``AWGControl:CLOCk`` command tree.
            - ``.compile``: The ``AWGControl:COMPile`` command.
            - ``.configure``: The ``AWGControl:CONFigure`` command tree.
            - ``.pjump``: The ``AWGControl:PJUMp`` command tree.
            - ``.rmode``: The ``AWGControl:RMODe`` command.
            - ``.rstate``: The ``AWGControl:RSTate`` command.
            - ``.run``: The ``AWGControl:RUN`` command tree.
            - ``.sname``: The ``AWGControl:SNAMe`` command.
            - ``.srestore``: The ``AWGControl:SREStore`` command.
            - ``.ssave``: The ``AWGControl:SSAVe`` command.
            - ``.stop``: The ``AWGControl:STOP`` command tree.
        """
        return self._awgcontrol

    @property
    def bwaveform(self) -> Bwaveform:
        """Return the ``BWAVeform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BWAVeform?`` query.
            - Using the ``.verify(value)`` method will send the ``BWAVeform?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``BWAVeform:AMPLitude`` command.
            - ``.auto``: The ``BWAVeform:AUTO`` command.
            - ``.compile``: The ``BWAVeform:COMPile`` command.
            - ``.cycle``: The ``BWAVeform:CYCLe`` command.
            - ``.fdrange``: The ``BWAVeform:FDRange`` command.
            - ``.frequency``: The ``BWAVeform:FREQuency`` command.
            - ``.function``: The ``BWAVeform:FUNCtion`` command.
            - ``.high``: The ``BWAVeform:HIGH`` command.
            - ``.length``: The ``BWAVeform:LENGth`` command.
            - ``.low``: The ``BWAVeform:LOW`` command.
            - ``.offset``: The ``BWAVeform:OFFSet`` command.
            - ``.reset``: The ``BWAVeform:RESet`` command.
            - ``.srate``: The ``BWAVeform:SRATe`` command.
        """
        return self._bwaveform

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
            - ``.abort``: The ``CALibration:ABORt`` command.
            - ``.catalog``: The ``CALibration:CATalog`` command.
            - ``.log``: The ``CALibration:LOG`` command.
            - ``.restore``: The ``CALibration:RESTore`` command.
            - ``.result``: The ``CALibration:RESult`` command.
            - ``.running``: The ``CALibration:RUNNing`` command.
            - ``.start``: The ``CALibration:STARt`` command.
            - ``.state``: The ``CALibration:STATe`` command tree.
            - ``.stop``: The ``CALibration:STOP`` command tree.
            - ``.all``: The ``CALibration:ALL`` command.
        """
        return self._calibration

    @property
    def clock(self) -> Clock:
        """Return the ``CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``CLOCk?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.eclock``: The ``CLOCk:ECLock`` command tree.
            - ``.ereference``: The ``CLOCk:EREFerence`` command tree.
            - ``.jitter``: The ``CLOCk:JITTer`` command.
            - ``.output``: The ``CLOCk:OUTPut`` command tree.
            - ``.phase``: The ``CLOCk:PHASe`` command tree.
            - ``.source``: The ``CLOCk:SOURce`` command.
            - ``.sout``: The ``CLOCk:SOUT`` command tree.
            - ``.srate``: The ``CLOCk:SRATe`` command.
        """
        return self._clock

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
    def connectivity(self) -> Connectivity:
        """Return the ``CONNectivity`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONNectivity?`` query.
            - Using the ``.verify(value)`` method will send the ``CONNectivity?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.active``: The ``CONNectivity:ACTive`` command.
            - ``.connect``: The ``CONNectivity:CONNect`` command.
            - ``.disconnect``: The ``CONNectivity:DISConnect`` command.
            - ``.gang``: The ``CONNectivity:GANG`` command tree.
            - ``.remove``: The ``CONNectivity:REMove`` command.
            - ``.status``: The ``CONNectivity:STATus`` command.
        """
        return self._connectivity

    @property
    def cplayback(self) -> Cplayback:
        """Return the ``CPLayback`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback?`` query.
            - Using the ``.verify(value)`` method will send the ``CPLayback?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.capture``: The ``CPLayback:CAPTure`` command tree.
            - ``.clist``: The ``CPLayback:CLISt`` command tree.
            - ``.compile``: The ``CPLayback:COMPile`` command.
        """
        return self._cplayback

    @property
    def diagnostic(self) -> Diagnostic:
        """Return the ``DIAGnostic`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.abort``: The ``DIAGnostic:ABORt`` command.
            - ``.catalog``: The ``DIAGnostic:CATalog`` command.
            - ``.control``: The ``DIAGnostic:CONTrol`` command tree.
            - ``.data``: The ``DIAGnostic:DATA`` command.
            - ``.log``: The ``DIAGnostic:LOG`` command.
            - ``.loops``: The ``DIAGnostic:LOOPs`` command.
            - ``.result``: The ``DIAGnostic:RESult`` command.
            - ``.running``: The ``DIAGnostic:RUNNing`` command.
            - ``.select``: The ``DIAGnostic:SELect`` command.
            - ``.start``: The ``DIAGnostic:STARt`` command.
            - ``.stop``: The ``DIAGnostic:STOP`` command.
            - ``.type``: The ``DIAGnostic:TYPE`` command.
            - ``.unselect``: The ``DIAGnostic:UNSelect`` command.
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
            - ``.plot``: The ``DISPlay:PLOT`` command tree.
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
    def fgen(self) -> Fgen:
        """Return the ``FGEN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.channel``: The ``FGEN:CHANnel[n]`` command tree.
        """
        return self._fgen

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
            - ``.mode``: The ``INSTrument:MODE`` command.
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
            - ``.import``: The ``MMEMory:IMPort`` command.
            - ``.mdirectory``: The ``MMEMory:MDIRectory`` command.
            - ``.msis``: The ``MMEMory:MSIS`` command.
            - ``.open``: The ``MMEMory:OPEN`` command.
            - ``.save``: The ``MMEMory:SAVE`` command tree.
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
    def output(self) -> Output:
        """Return the ``OUTPut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.off``: The ``OUTPut:OFF`` command.
        """
        return self._output

    @property
    def outputx(self) -> Dict[int, OutputItem]:
        """Return the ``OUTPut[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.path``: The ``OUTPut[n]:PATH`` command.
            - ``.svalue``: The ``OUTPut[n]:SVALue`` command tree.
            - ``.wvalue``: The ``OUTPut[n]:WVALue`` command tree.
            - ``.state``: The ``OUTPut[n]:STATe`` command.
        """
        return self._outputx

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
    def slist(self) -> Slist:
        """Return the ``SLISt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.name``: The ``SLISt:NAME`` command.
            - ``.sequence``: The ``SLISt:SEQuence`` command tree.
            - ``.size``: The ``SLISt:SIZE`` command.
        """
        return self._slist

    @property
    def source(self) -> Source:
        """Return the ``SOURce`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``SOURce:FREQuency`` command.
            - ``.iqimode``: The ``SOURce:IQIMode`` command.
            - ``.rccouple``: The ``SOURce:RCCouple`` command.
            - ``.roscillator``: The ``SOURce:ROSCillator`` command tree.
        """
        return self._source

    @property
    def sourcex(self) -> Dict[int, SourceItem]:
        """Return the ``SOURce[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce[n]?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce[n]?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.casset``: The ``SOURce[n]:CASSet`` command.
            - ``.cfrequency``: The ``SOURce[n]:CFRequency`` command.
            - ``.dac``: The ``SOURce[n]:DAC`` command tree.
            - ``.ddr``: The ``SOURce[n]:DDR`` command.
            - ``.dmode``: The ``SOURce[n]:DMODe`` command.
            - ``.marker``: The ``SOURce[n]:MARKer[m]`` command tree.
            - ``.power``: The ``SOURce[n]:POWer`` command tree.
            - ``.rmode``: The ``SOURce[n]:RMODe`` command.
            - ``.scstep``: The ``SOURce[n]:SCSTep`` command.
            - ``.skew``: The ``SOURce[n]:SKEW`` command.
            - ``.tinput``: The ``SOURce[n]:TINPut`` command.
            - ``.voltage``: The ``SOURce[n]:VOLTage`` command tree.
            - ``.waveform``: The ``SOURce[n]:WAVeform`` command.
            - ``.jump``: The ``SOURce[n]:JUMP`` command tree.
        """
        return self._sourcex

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
    def synchronize(self) -> Synchronize:
        """Return the ``SYNChronize`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYNChronize?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.adjust``: The ``SYNChronize:ADJust`` command tree.
            - ``.deskew``: The ``SYNChronize:DESKew`` command tree.
            - ``.enable``: The ``SYNChronize:ENABle`` command.
            - ``.type``: The ``SYNChronize:TYPE`` command.
        """
        return self._synchronize

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
            - ``.impedance``: The ``TRIGger:IMPedance`` command.
            - ``.interval``: The ``TRIGger:INTerval`` command.
            - ``.level``: The ``TRIGger:LEVel`` command.
            - ``.mode``: The ``TRIGger:MODE`` command.
            - ``.slope``: The ``TRIGger:SLOPe`` command.
            - ``.source``: The ``TRIGger:SOURce`` command.
            - ``.wvalue``: The ``TRIGger:WVALue`` command.
            - ``.immediate``: The ``TRIGger:IMMediate`` command.
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
            - ``.last``: The ``WLISt:LAST`` command.
            - ``.list``: The ``WLISt:LIST`` command.
            - ``.name``: The ``WLISt:NAME`` command.
            - ``.size``: The ``WLISt:SIZE`` command.
            - ``.sparameter``: The ``WLISt:SPARameter`` command tree.
            - ``.waveform``: The ``WLISt:WAVeform`` command tree.
        """
        return self._wlist

    @property
    def wplugin(self) -> Wplugin:
        """Return the ``WPLugin`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WPLugin?`` query.
            - Using the ``.verify(value)`` method will send the ``WPLugin?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.active``: The ``WPLugin:ACTive`` command.
            - ``.plugins``: The ``WPLugin:PLUGins`` command.
        """
        return self._wplugin


class AWG5200Mixin:
    """A mixin that provides access to the AWG5200 commands and constants.

    Properties:
        - ``.command_argument_constants``: The AWG5200 command argument constants.
        - ``.commands``: The AWG5200 commands.
    """

    @cached_property
    def command_argument_constants(self) -> AWG5200CommandConstants:  # pylint: disable=no-self-use
        """Return the AWG5200 command argument constants.

        This provides access to all the string constants which can be used as arguments for AWG5200
        commands.
        """
        return AWG5200CommandConstants()

    @cached_property
    def commands(self) -> AWG5200Commands:
        """Return the AWG5200 commands.

        This provides access to all the commands for the AWG5200 device. See the documentation of
        each sub-property for more usage information.

        Sub-properties:
            - ``.abort``: The ``ABORt`` command.
            - ``.active``: The ``ACTive`` command tree.
            - ``.auxoutput``: The ``AUXoutput[n]`` command tree.
            - ``.awgcontrol``: The ``AWGControl`` command tree.
            - ``.bwaveform``: The ``BWAVeform`` command tree.
            - ``.cal``: The ``*CAL`` command.
            - ``.calibration``: The ``CALibration`` command tree.
            - ``.clock``: The ``CLOCk`` command tree.
            - ``.cls``: The ``*CLS`` command.
            - ``.connectivity``: The ``CONNectivity`` command tree.
            - ``.cplayback``: The ``CPLayback`` command tree.
            - ``.diagnostic``: The ``DIAGnostic`` command tree.
            - ``.display``: The ``DISPlay`` command tree.
            - ``.ese``: The ``*ESE`` command.
            - ``.esr``: The ``*ESR`` command.
            - ``.fgen``: The ``FGEN`` command tree.
            - ``.idn``: The ``*IDN`` command.
            - ``.instrument``: The ``INSTrument`` command tree.
            - ``.mmemory``: The ``MMEMory`` command tree.
            - ``.opc``: The ``*OPC`` command.
            - ``.opt``: The ``*OPT`` command.
            - ``.output``: The ``OUTPut`` command tree.
            - ``.outputx``: The ``OUTPut[n]`` command tree.
            - ``.rst``: The ``*RST`` command.
            - ``.slist``: The ``SLISt`` command tree.
            - ``.source``: The ``SOURce`` command tree.
            - ``.sourcex``: The ``SOURce[n]`` command tree.
            - ``.sre``: The ``*SRE`` command.
            - ``.status``: The ``STATus`` command tree.
            - ``.stb``: The ``*STB`` command.
            - ``.synchronize``: The ``SYNChronize`` command tree.
            - ``.system``: The ``SYSTem`` command tree.
            - ``.trg``: The ``*TRG`` command.
            - ``.trigger``: The ``TRIGger`` command tree.
            - ``.tst``: The ``*TST`` command.
            - ``.wai``: The ``*WAI`` command.
            - ``.wlist``: The ``WLISt`` command tree.
            - ``.wplugin``: The ``WPLugin`` command tree.
        """
        device = self if isinstance(self, PIControl) else None
        return AWG5200Commands(device)
