"""The AFG3K commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Optional

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_22daqs_afg.afgcontrol import Afgcontrol
from .gen_22daqs_afg.data import Data
from .gen_22daqs_afg.diagnostic import Diagnostic
from .gen_22daqs_afg.display import Display
from .gen_22daqs_afg.hcopy import Hcopy
from .gen_22daqs_afg.memory import Memory, Rcl, Sav
from .gen_22daqs_afg.mmemory import Mmemory
from .gen_22daqs_afg.output import Output
from .gen_22daqs_afg.output1 import Output1
from .gen_22daqs_afg.output2 import Output2
from .gen_22daqs_afg.source import Source
from .gen_22daqs_afg.source1 import Source1
from .gen_22daqs_afg.source2 import Source2
from .gen_22daqs_afg.source3 import Source3
from .gen_22daqs_afg.source4 import Source4
from .gen_22daqs_afg.status import Ese, Psc, Sre, Status
from .gen_22daqs_afg.system import System
from .gen_22daqs_afg.trigger import Trigger
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


# pylint: disable=too-few-public-methods
class AFG3KCommandConstants:
    """The AFG3K command argument constants.

    This provides access to all the string constants which can be used as arguments for AFG3K
    commands.
    """

    EMEMORY = "EMEMORY"  # EMEMory
    EMEMORY2 = "EMEMORY2"  # EMEMory2
    EXTERNAL = "EXTERNAL"  # EXTernal
    NEGATIVE = "NEGATIVE"  # NEGative
    POSITIVE = "POSITIVE"  # POSitive
    TIMER = "TIMER"  # TIMer


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class AFG3KCommands:
    """The AFG3K commands.

    This provides access to all the commands for the AFG3K device. See the documentation of each
    property for more usage information.

    Properties:
        - ``.abort``: The ``ABORt`` command.
        - ``.afgcontrol``: The ``AFGControl`` command tree.
        - ``.cal``: The ``*CAL`` command.
        - ``.calibration``: The ``CALibration`` command tree.
        - ``.cls``: The ``*CLS`` command.
        - ``.data``: The ``DATA`` command tree.
        - ``.diagnostic``: The ``DIAGnostic`` command tree.
        - ``.display``: The ``DISPlay`` command tree.
        - ``.ese``: The ``*ESE`` command.
        - ``.esr``: The ``*ESR`` command.
        - ``.hcopy``: The ``HCOPy`` command tree.
        - ``.idn``: The ``*IDN`` command.
        - ``.memory``: The ``MEMory`` command tree.
        - ``.mmemory``: The ``MMEMory`` command tree.
        - ``.opc``: The ``*OPC`` command.
        - ``.opt``: The ``*OPT`` command.
        - ``.output1``: The ``OUTPut1`` command tree.
        - ``.output2``: The ``OUTPut2`` command tree.
        - ``.output``: The ``OUTPut`` command tree.
        - ``.psc``: The ``*PSC`` command.
        - ``.rcl``: The ``*RCL`` command.
        - ``.rst``: The ``*RST`` command.
        - ``.sav``: The ``*SAV`` command.
        - ``.source1``: The ``SOURce1`` command tree.
        - ``.source2``: The ``SOURce2`` command tree.
        - ``.source3``: The ``SOURce3`` command tree.
        - ``.source4``: The ``SOURce4`` command tree.
        - ``.source``: The ``SOURce`` command tree.
        - ``.sre``: The ``*SRE`` command.
        - ``.status``: The ``STATus`` command tree.
        - ``.stb``: The ``*STB`` command.
        - ``.system``: The ``SYSTem`` command tree.
        - ``.trg``: The ``*TRG`` command.
        - ``.trigger``: The ``TRIGger`` command tree.
        - ``.tst``: The ``*TST`` command.
        - ``.wai``: The ``*WAI`` command.
    """

    def __init__(self, device: Optional[PIControl] = None) -> None:
        self._abort = Abort(device)
        self._afgcontrol = Afgcontrol(device)
        self._cal = Cal(device)
        self._calibration = Calibration(device)
        self._cls = Cls(device)
        self._data = Data(device)
        self._diagnostic = Diagnostic(device)
        self._display = Display(device)
        self._ese = Ese(device)
        self._esr = Esr(device)
        self._hcopy = Hcopy(device)
        self._idn = Idn(device)
        self._memory = Memory(device)
        self._mmemory = Mmemory(device)
        self._opc = Opc(device)
        self._opt = Opt(device)
        self._output = Output(device)
        self._output1 = Output1(device)
        self._output2 = Output2(device)
        self._psc = Psc(device)
        self._rcl = Rcl(device)
        self._rst = Rst(device)
        self._sav = Sav(device)
        self._source = Source(device)
        self._source1 = Source1(device)
        self._source2 = Source2(device)
        self._source3 = Source3(device)
        self._source4 = Source4(device)
        self._sre = Sre(device)
        self._status = Status(device)
        self._stb = Stb(device)
        self._system = System(device)
        self._trg = Trg(device)
        self._trigger = Trigger(device)
        self._tst = Tst(device)
        self._wai = Wai(device)

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
    def afgcontrol(self) -> Afgcontrol:
        """Return the ``AFGControl`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFGControl?`` query.
            - Using the ``.verify(value)`` method will send the ``AFGControl?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.cscopy``: The ``AFGControl:CSCopy`` command.
        """
        return self._afgcontrol

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
    def data(self) -> Data:
        """Return the ``DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``DATA?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.catalog``: The ``DATA:CATalog`` command.
            - ``.copy``: The ``DATA:COPY`` command.
            - ``.define``: The ``DATA:DEFine`` command.
            - ``.delete``: The ``DATA:DELete`` command tree.
            - ``.ememcopy``: The ``DATA:EMEMCOPY`` command.
            - ``.lock``: The ``DATA:LOCK`` command tree.
            - ``.points``: The ``DATA:POINts`` command.
            - ``.data``: The ``DATA:DATA`` command.
        """
        return self._data

    @property
    def diagnostic(self) -> Diagnostic:
        """Return the ``DIAGnostic`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.all``: The ``DIAGnostic:ALL`` command.
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
            - ``.brightness``: The ``DISPlay:BRIGHtness`` command.
            - ``.contrast``: The ``DISPlay:CONTrast`` command.
            - ``.saver``: The ``DISPlay:SAVer`` command tree.
            - ``.window``: The ``DISPlay:WINDow`` command tree.
        """
        return self._display

    @property
    def ese(self) -> Ese:
        """Return the ``*ESE`` command.

        Description:
            - This command sets or queries the bits in the Event Status Enable Register (ESER) used
              in the status and events reporting system of the arbitrary function generator. The
              query command returns the contents of the ESER.

        Usage:
            - Using the ``.query()`` method will send the ``*ESE?`` query.
            - Using the ``.verify(value)`` method will send the ``*ESE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``*ESE value`` command.

        SCPI Syntax:
            ```
            - *ESE <bit_value>
            - *ESE?
            ```

        Info:
            - ``<bit_value>::=<NR1>``
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
    def hcopy(self) -> Hcopy:
        """Return the ``HCOPy`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HCOPy?`` query.
            - Using the ``.verify(value)`` method will send the ``HCOPy?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.sdump``: The ``HCOPy:SDUMp`` command tree.
        """
        return self._hcopy

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
    def memory(self) -> Memory:
        """Return the ``MEMory`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEMory?`` query.
            - Using the ``.verify(value)`` method will send the ``MEMory?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``MEMory:STATe`` command tree.
        """
        return self._memory

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
            - ``.delete``: The ``MMEMory:DELete`` command.
            - ``.load``: The ``MMEMory:LOAD`` command tree.
            - ``.lock``: The ``MMEMory:LOCK`` command tree.
            - ``.mdirectory``: The ``MMEMory:MDIRectory`` command.
            - ``.store``: The ``MMEMory:STORe`` command tree.
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
            - ``.trigger``: The ``OUTPut:TRIGger`` command tree.
        """
        return self._output

    @property
    def output1(self) -> Output1:
        """Return the ``OUTPut1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut1?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut1?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.impedance``: The ``OUTPut1:IMPedance`` command.
            - ``.polarity``: The ``OUTPut1:POLarity`` command.
            - ``.state``: The ``OUTPut1:STATe`` command.
        """
        return self._output1

    @property
    def output2(self) -> Output2:
        """Return the ``OUTPut2`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut2?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut2?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.impedance``: The ``OUTPut2:IMPedance`` command.
            - ``.polarity``: The ``OUTPut2:POLarity`` command.
            - ``.state``: The ``OUTPut2:STATe`` command.
        """
        return self._output2

    @property
    def psc(self) -> Psc:
        """Return the ``*PSC`` command.

        Description:
            - This command sets and queries the power-on status flag that controls the automatic
              power-on execution of SRER and ESER. When ``*PSC`` is true, SRER and ESER are set to 0
              at power-on. When ``*PSC`` is false, the current values in the SRER and ESER are
              preserved in nonvolatile memory when power is shut off and are restored at power-on.

        Usage:
            - Using the ``.query()`` method will send the ``*PSC?`` query.
            - Using the ``.verify(value)`` method will send the ``*PSC?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``*PSC value`` command.

        SCPI Syntax:
            ```
            - *PSC <NR1>
            - *PSC?
            ```
        """
        return self._psc

    @property
    def rcl(self) -> Rcl:
        """Return the ``*RCL`` command.

        Description:
            - This command restores the state of the instrument from a copy of the settings stored
              in the setup memory. The settings are stored using the ``*SAV`` command. If the
              specified setup memory is deleted, this command causes an error.

        Usage:
            - Using the ``.write(value)`` method will send the ``*RCL value`` command.

        SCPI Syntax:
            ```
            - *RCL {0|1|2|3|4}
            ```
        """
        return self._rcl

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
    def sav(self) -> Sav:
        """Return the ``*SAV`` command.

        Description:
            - This command stores the current settings of the arbitrary function generator to a
              specified setup memory location. A setup memory location numbered 0 ( last setup
              memory) is automatically overwritten by the setups when you power off the instrument.
              If a specified numbered setup memory is locked, this command causes an error.

        Usage:
            - Using the ``.write(value)`` method will send the ``*SAV value`` command.

        SCPI Syntax:
            ```
            - *SAV {0|1|2|3|4}
            ```
        """
        return self._sav

    @property
    def source(self) -> Source:
        """Return the ``SOURce`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.roscillator``: The ``SOURce:ROSCillator`` command tree.
        """
        return self._source

    @property
    def source1(self) -> Source1:
        """Return the ``SOURce1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce1?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce1?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.am``: The ``SOURce1:AM`` command tree.
            - ``.burst``: The ``SOURce1:BURSt`` command tree.
            - ``.combine``: The ``SOURce1:COMBine`` command tree.
            - ``.fm``: The ``SOURce1:FM`` command tree.
            - ``.frequency``: The ``SOURce1:FREQuency`` command tree.
            - ``.fskey``: The ``SOURce1:FSKey`` command tree.
            - ``.function``: The ``SOURce1:FUNCtion`` command tree.
            - ``.phase``: The ``SOURce1:PHASe`` command tree.
            - ``.pm``: The ``SOURce1:PM`` command tree.
            - ``.pulse``: The ``SOURce1:PULSe`` command tree.
            - ``.pwm``: The ``SOURce1:PWM`` command tree.
            - ``.sweep``: The ``SOURce1:SWEep`` command tree.
            - ``.voltage``: The ``SOURce1:VOLTage`` command tree.
        """
        return self._source1

    @property
    def source2(self) -> Source2:
        """Return the ``SOURce2`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce2?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce2?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.am``: The ``SOURce2:AM`` command tree.
            - ``.burst``: The ``SOURce2:BURSt`` command tree.
            - ``.combine``: The ``SOURce2:COMBine`` command tree.
            - ``.fm``: The ``SOURce2:FM`` command tree.
            - ``.frequency``: The ``SOURce2:FREQuency`` command tree.
            - ``.fskey``: The ``SOURce2:FSKey`` command tree.
            - ``.function``: The ``SOURce2:FUNCtion`` command tree.
            - ``.phase``: The ``SOURce2:PHASe`` command tree.
            - ``.pm``: The ``SOURce2:PM`` command tree.
            - ``.pulse``: The ``SOURce2:PULSe`` command tree.
            - ``.pwm``: The ``SOURce2:PWM`` command tree.
            - ``.sweep``: The ``SOURce2:SWEep`` command tree.
            - ``.voltage``: The ``SOURce2:VOLTage`` command tree.
        """
        return self._source2

    @property
    def source3(self) -> Source3:
        """Return the ``SOURce3`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce3?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce3?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.power``: The ``SOURce3:POWer`` command tree.
        """
        return self._source3

    @property
    def source4(self) -> Source4:
        """Return the ``SOURce4`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce4?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce4?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.power``: The ``SOURce4:POWer`` command tree.
        """
        return self._source4

    @property
    def sre(self) -> Sre:
        """Return the ``*SRE`` command.

        Description:
            - This command sets and queries the bits in the Service Request Enable Register (SRER).

        Usage:
            - Using the ``.query()`` method will send the ``*SRE?`` query.
            - Using the ``.verify(value)`` method will send the ``*SRE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``*SRE value`` command.

        SCPI Syntax:
            ```
            - *SRE <bit_value>
            - *SRE?
            ```
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
            - ``.beeper``: The ``SYSTem:BEEPer`` command tree.
            - ``.error``: The ``SYSTem:ERRor`` command tree.
            - ``.kclick``: The ``SYSTem:KCLick`` command tree.
            - ``.klock``: The ``SYSTem:KLOCk`` command tree.
            - ``.password``: The ``SYSTem:PASSword`` command tree.
            - ``.security``: The ``SYSTem:SECurity`` command tree.
            - ``.ulanguage``: The ``SYSTem:ULANguage`` command.
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


class AFG3KMixin:
    """A mixin that provides access to the AFG3K commands and constants.

    Properties:
        - ``.command_argument_constants``: The AFG3K command argument constants.
        - ``.commands``: The AFG3K commands.
    """

    @cached_property
    def command_argument_constants(self) -> AFG3KCommandConstants:  # pylint: disable=no-self-use
        """Return the AFG3K command argument constants.

        This provides access to all the string constants which can be used as arguments for AFG3K
        commands.
        """
        return AFG3KCommandConstants()

    @cached_property
    def commands(self) -> AFG3KCommands:
        """Return the AFG3K commands.

        This provides access to all the commands for the AFG3K device. See the documentation of each
        sub-property for more usage information.

        Sub-properties:
            - ``.abort``: The ``ABORt`` command.
            - ``.afgcontrol``: The ``AFGControl`` command tree.
            - ``.cal``: The ``*CAL`` command.
            - ``.calibration``: The ``CALibration`` command tree.
            - ``.cls``: The ``*CLS`` command.
            - ``.data``: The ``DATA`` command tree.
            - ``.diagnostic``: The ``DIAGnostic`` command tree.
            - ``.display``: The ``DISPlay`` command tree.
            - ``.ese``: The ``*ESE`` command.
            - ``.esr``: The ``*ESR`` command.
            - ``.hcopy``: The ``HCOPy`` command tree.
            - ``.idn``: The ``*IDN`` command.
            - ``.memory``: The ``MEMory`` command tree.
            - ``.mmemory``: The ``MMEMory`` command tree.
            - ``.opc``: The ``*OPC`` command.
            - ``.opt``: The ``*OPT`` command.
            - ``.output1``: The ``OUTPut1`` command tree.
            - ``.output2``: The ``OUTPut2`` command tree.
            - ``.output``: The ``OUTPut`` command tree.
            - ``.psc``: The ``*PSC`` command.
            - ``.rcl``: The ``*RCL`` command.
            - ``.rst``: The ``*RST`` command.
            - ``.sav``: The ``*SAV`` command.
            - ``.source1``: The ``SOURce1`` command tree.
            - ``.source2``: The ``SOURce2`` command tree.
            - ``.source3``: The ``SOURce3`` command tree.
            - ``.source4``: The ``SOURce4`` command tree.
            - ``.source``: The ``SOURce`` command tree.
            - ``.sre``: The ``*SRE`` command.
            - ``.status``: The ``STATus`` command tree.
            - ``.stb``: The ``*STB`` command.
            - ``.system``: The ``SYSTem`` command tree.
            - ``.trg``: The ``*TRG`` command.
            - ``.trigger``: The ``TRIGger`` command tree.
            - ``.tst``: The ``*TST`` command.
            - ``.wai``: The ``*WAI`` command.
        """
        device = self if isinstance(self, PIControl) else None
        return AFG3KCommands(device)
