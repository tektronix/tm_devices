# ruff: noqa: D402,PLR0913
"""The SS3706A commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional

from tm_devices.driver_mixins.device_control.tsp_control import TSPControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_e3pief_ss.beeper import Beeper
from .gen_e3pief_ss.buffervar import Buffervar
from .gen_e3pief_ss.channel import Channel
from .gen_e3pief_ss.comm import Comm
from .gen_e3pief_ss.digio import Digio
from .gen_e3pief_ss.display import Display
from .gen_e3pief_ss.dmm import Dmm
from .gen_e3pief_ss.eventlog import Eventlog
from .gen_e3pief_ss.format import Format
from .gen_e3pief_ss.lan import Lan
from .gen_e3pief_ss.localnode import Localnode
from .gen_e3pief_ss.memory import Memory
from .gen_e3pief_ss.os import Os
from .gen_e3pief_ss.ptp import Ptp
from .gen_e3pief_ss.scan import Scan
from .gen_e3pief_ss.schedule import Schedule
from .gen_e3pief_ss.script import Script
from .gen_e3pief_ss.scriptvar import Scriptvar
from .gen_e3pief_ss.setup_1 import Setup
from .gen_e3pief_ss.slot import SlotItem
from .gen_e3pief_ss.status import Status
from .gen_e3pief_ss.trigger import Trigger
from .gen_e3pief_ss.tsplink import Tsplink
from .gen_e3pief_ss.upgrade import Upgrade
from .gen_e7aqno_smudaqss.node import NodeItem
from .gen_eat5s3_smudaqdmmss.dataqueue import Dataqueue
from .gen_eat5s3_smudaqdmmss.fs import Fs
from .gen_eat5s3_smudaqdmmss.userstring import Userstring
from .gen_ed9nkc_daqss.tspnet import Tspnet
from .gen_efap3f_smuss.bit import Bit
from .gen_efap3f_smuss.errorqueue import Errorqueue
from .gen_efap3f_smuss.io import Io
from .gen_efap3f_smuss.timer import Timer
from .gen_eg5ll2_smudaqdmmss.gpib import Gpib
from .helpers import DefaultDictPassKeyToFactory, NoDeviceProvidedError


# pylint: disable=too-few-public-methods
class SS3706ACommandConstants:
    """The SS3706A command argument constants.

    This provides access to all the string constants which can be used as arguments for SS3706A
    commands.
    """

    CHANNEL_TRIGGER_N_EVENT_ID = "channel.trigger[N].EVENT_ID"
    DATAQUEUE_CAPACITY = "dataqueue.CAPACITY"
    DIGIO_TRIGGER_N_EVENT_ID = "digio.trigger[N].EVENT_ID"
    DISPLAY_TRIGGER_EVENT_ID = "display.trigger.EVENT_ID"
    LAN_TRIGGER_N_EVENT_ID = "lan.trigger[N].EVENT_ID"
    SCHEDULE_ALARM_N_EVENT_ID = "schedule.alarm[N].EVENT_ID"
    TRIGGER_BLENDER_N_EVENT_ID = "trigger.blender[N].EVENT_ID"
    TRIGGER_EVENT_ID = "trigger.EVENT_ID"
    TRIGGER_TIMER_N_EVENT_ID = "trigger.timer[N].EVENT_ID"
    TSPLINK_TRIGGER_N_EVENT_ID = "tsplink.trigger[N].EVENT_ID"


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class SS3706ACommands:
    """The SS3706A commands.

    This provides access to all the commands for the SS3706A device. See the documentation of each
    property for more usage information.

    Properties and methods:
        - ``.beeper``: The ``beeper`` command tree.
        - ``.bit``: The ``bit`` command tree.
        - ``.buffer_var``: The ``bufferVar`` command tree.
        - ``.channel``: The ``channel`` command tree.
        - ``.comm``: The ``comm`` command tree.
        - ``.createconfigscript()``: The ``createconfigscript()`` function.
        - ``.dataqueue``: The ``dataqueue`` command tree.
        - ``.delay()``: The ``delay()`` function.
        - ``.digio``: The ``digio`` command tree.
        - ``.display``: The ``display`` command tree.
        - ``.dmm``: The ``dmm`` command tree.
        - ``.errorqueue``: The ``errorqueue`` command tree.
        - ``.eventlog``: The ``eventlog`` command tree.
        - ``.exit()``: The ``exit()`` function.
        - ``.format``: The ``format`` command tree.
        - ``.fs``: The ``fs`` command tree.
        - ``.gettimezone()``: The ``gettimezone()`` function.
        - ``.gpib``: The ``gpib`` command tree.
        - ``.io``: The ``io`` command tree.
        - ``.lan``: The ``lan`` command tree.
        - ``.localnode``: The ``localnode`` command tree.
        - ``.makegetter()``: The ``makegetter()`` function.
        - ``.makesetter()``: The ``makesetter()`` function.
        - ``.memory``: The ``memory`` command tree.
        - ``.node``: The ``node[N]`` command tree.
        - ``.opc()``: The ``opc()`` function.
        - ``.os``: The ``os`` command tree.
        - ``.print()``: The ``print()`` function.
        - ``.printbuffer()``: The ``printbuffer()`` function.
        - ``.printnumber()``: The ``printnumber()`` function.
        - ``.ptp``: The ``ptp`` command tree.
        - ``.reset()``: The ``reset()`` function.
        - ``.scan``: The ``scan`` command tree.
        - ``.schedule``: The ``schedule`` command tree.
        - ``.script_var``: The ``scriptVar`` command tree.
        - ``.script``: The ``script`` command tree.
        - ``.settime()``: The ``settime()`` function.
        - ``.settimezone()``: The ``settimezone()`` function.
        - ``.setup``: The ``setup`` command tree.
        - ``.slot``: The ``slot[slot]`` command tree.
        - ``.status``: The ``status`` command tree.
        - ``.timer``: The ``timer`` command tree.
        - ``.trigger``: The ``trigger`` command tree.
        - ``.tsplink``: The ``tsplink`` command tree.
        - ``.tspnet``: The ``tspnet`` command tree.
        - ``.upgrade``: The ``upgrade`` command tree.
        - ``.userstring``: The ``userstring`` command tree.
        - ``.waitcomplete()``: The ``waitcomplete()`` function.
    """

    def __init__(self, device: Optional[TSPControl] = None) -> None:
        self._device = device
        self._beeper = Beeper(device)
        self._bit = Bit(device)
        self._buffer_var: Dict[str, Buffervar] = DefaultDictPassKeyToFactory(
            lambda x: Buffervar(device, str(x))
        )
        self._channel = Channel(device)
        self._comm = Comm(device)
        self._dataqueue = Dataqueue(device)
        self._digio = Digio(device)
        self._display = Display(device)
        self._dmm = Dmm(device)
        self._errorqueue = Errorqueue(device)
        self._eventlog = Eventlog(device)
        self._format = Format(device)
        self._fs = Fs(device)
        self._gpib = Gpib(device)
        self._io = Io(device)
        self._lan = Lan(device)
        self._localnode = Localnode(device)
        self._memory = Memory(device)
        self._node: Dict[int, NodeItem] = DefaultDictPassKeyToFactory(
            lambda x: NodeItem(device, f"node[{x}]")
        )
        self._os = Os(device)
        self._ptp = Ptp(device)
        self._scan = Scan(device)
        self._schedule = Schedule(device)
        self._script = Script(device)
        self._script_var: Dict[str, Scriptvar] = DefaultDictPassKeyToFactory(
            lambda x: Scriptvar(device, str(x))
        )
        self._setup = Setup(device)
        self._slot: Dict[int, SlotItem] = DefaultDictPassKeyToFactory(
            lambda x: SlotItem(device, f"slot[{x}]")
        )
        self._status = Status(device)
        self._timer = Timer(device)
        self._trigger = Trigger(device)
        self._tsplink = Tsplink(device)
        self._tspnet = Tspnet(device)
        self._upgrade = Upgrade(device)
        self._userstring = Userstring(device)

    @property
    def beeper(self) -> Beeper:
        """Return the ``beeper`` command tree.

        Sub-properties and sub-methods:
            - ``.beep()``: The ``beeper.beep()`` function.
            - ``.enable``: The ``beeper.enable`` attribute.
        """
        return self._beeper

    @property
    def bit(self) -> Bit:
        """Return the ``bit`` command tree.

        Sub-properties and sub-methods:
            - ``.bitand()``: The ``bit.bitand()`` function.
            - ``.bitor()``: The ``bit.bitor()`` function.
            - ``.bitxor()``: The ``bit.bitxor()`` function.
            - ``.clear()``: The ``bit.clear()`` function.
            - ``.get()``: The ``bit.get()`` function.
            - ``.getfield()``: The ``bit.getfield()`` function.
            - ``.set()``: The ``bit.set()`` function.
            - ``.setfield()``: The ``bit.setfield()`` function.
            - ``.test()``: The ``bit.test()`` function.
            - ``.toggle()``: The ``bit.toggle()`` function.
        """
        return self._bit

    @property
    def buffer_var(self) -> Dict[str, Buffervar]:
        """Return the ``bufferVar`` command tree.

        Info:
            - ``bufferVar``, the reading buffer.

        Sub-properties and sub-methods:
            - ``.appendmode``: The ``bufferVar.appendmode`` attribute.
            - ``.basetimefractional``: The ``bufferVar.basetimefractional`` attribute.
            - ``.basetimeseconds``: The ``bufferVar.basetimeseconds`` attribute.
            - ``.cachemode``: The ``bufferVar.cachemode`` attribute.
            - ``.capacity``: The ``bufferVar.capacity`` attribute.
            - ``.channels``: The ``bufferVar.channels[N]`` attribute.
            - ``.clear()``: The ``bufferVar.clear()`` function.
            - ``.clearcache()``: The ``bufferVar.clearcache()`` function.
            - ``.collectchannels``: The ``bufferVar.collectchannels`` attribute.
            - ``.collecttimestamps``: The ``bufferVar.collecttimestamps`` attribute.
            - ``.dates``: The ``bufferVar.dates[N]`` attribute.
            - ``.formattedreadings``: The ``bufferVar.formattedreadings[N]`` attribute.
            - ``.fractionalseconds``: The ``bufferVar.fractionalseconds[N]`` attribute.
            - ``.n``: The ``bufferVar.n`` attribute.
            - ``.ptpseconds``: The ``bufferVar.ptpseconds[N]`` attribute.
            - ``.readings``: The ``bufferVar.readings[N]`` attribute.
            - ``.relativetimestamps``: The ``bufferVar.relativetimestamps[N]`` attribute.
            - ``.seconds``: The ``bufferVar.seconds[N]`` attribute.
            - ``.statuses``: The ``bufferVar.statuses[N]`` attribute.
            - ``.times``: The ``bufferVar.times[N]`` attribute.
            - ``.timestampresolution``: The ``bufferVar.timestampresolution`` attribute.
            - ``.timestamps``: The ``bufferVar.timestamps[N]`` attribute.
            - ``.units``: The ``bufferVar.units[N]`` attribute.
        """
        return self._buffer_var

    @property
    def channel(self) -> Channel:
        """Return the ``channel`` command tree.

        Sub-properties and sub-methods:
            - ``.calibration``: The ``channel.calibration`` command tree.
            - ``.clearforbidden()``: The ``channel.clearforbidden()`` function.
            - ``.close()``: The ``channel.close()`` function.
            - ``.connectrule``: The ``channel.connectrule`` attribute.
            - ``.connectsequential``: The ``channel.connectsequential`` attribute.
            - ``.exclusiveclose()``: The ``channel.exclusiveclose()`` function.
            - ``.exclusiveslotclose()``: The ``channel.exclusiveslotclose()`` function.
            - ``.getbackplane()``: The ``channel.getbackplane()`` function.
            - ``.getclose()``: The ``channel.getclose()`` function.
            - ``.getcount()``: The ``channel.getcount()`` function.
            - ``.getdelay()``: The ``channel.getdelay()`` function.
            - ``.getforbidden()``: The ``channel.getforbidden()`` function.
            - ``.getimage()``: The ``channel.getimage()`` function.
            - ``.getlabel()``: The ``channel.getlabel()`` function.
            - ``.getmatch()``: The ``channel.getmatch()`` function.
            - ``.getmatchtype()``: The ``channel.getmatchtype()`` function.
            - ``.getmode()``: The ``channel.getmode()`` function.
            - ``.getoutputenable()``: The ``channel.getoutputenable()`` function.
            - ``.getpole()``: The ``channel.getpole()`` function.
            - ``.getpowerstate()``: The ``channel.getpowerstate()`` function.
            - ``.getstate()``: The ``channel.getstate()`` function.
            - ``.getstatelatch()``: The ``channel.getstatelatch()`` function.
            - ``.gettype()``: The ``channel.gettype()`` function.
            - ``.open()``: The ``channel.open()`` function.
            - ``.pattern``: The ``channel.pattern`` command tree.
            - ``.read()``: The ``channel.read()`` function.
            - ``.reset()``: The ``channel.reset()`` function.
            - ``.resetstatelatch()``: The ``channel.resetstatelatch()`` function.
            - ``.setbackplane()``: The ``channel.setbackplane()`` function.
            - ``.setdelay()``: The ``channel.setdelay()`` function.
            - ``.setforbidden()``: The ``channel.setforbidden()`` function.
            - ``.setlabel()``: The ``channel.setlabel()`` function.
            - ``.setmatch()``: The ``channel.setmatch()`` function.
            - ``.setmatchtype()``: The ``channel.setmatchtype()`` function.
            - ``.setmode()``: The ``channel.setmode()`` function.
            - ``.setoutputenable()``: The ``channel.setoutputenable()`` function.
            - ``.setpole()``: The ``channel.setpole()`` function.
            - ``.setstatelatch()``: The ``channel.setstatelatch()`` function.
            - ``.trigger``: The ``channel.trigger[N]`` command tree.
            - ``.write()``: The ``channel.write()`` function.
        """
        return self._channel

    @property
    def comm(self) -> Comm:
        """Return the ``comm`` command tree.

        Sub-properties and sub-methods:
            - ``.gpib``: The ``comm.gpib`` command tree.
            - ``.lan``: The ``comm.lan`` command tree.
        """
        return self._comm

    @property
    def dataqueue(self) -> Dataqueue:
        """Return the ``dataqueue`` command tree.

        Constants:
            - ``.CAPACITY``: The maximum number of entries that you can store in the data queue.

        Sub-properties and sub-methods:
            - ``.add()``: The ``dataqueue.add()`` function.
            - ``.clear()``: The ``dataqueue.clear()`` function.
            - ``.count``: The ``dataqueue.count`` attribute.
            - ``.next()``: The ``dataqueue.next()`` function.
        """
        return self._dataqueue

    @property
    def digio(self) -> Digio:
        """Return the ``digio`` command tree.

        Sub-properties and sub-methods:
            - ``.readbit()``: The ``digio.readbit()`` function.
            - ``.readport()``: The ``digio.readport()`` function.
            - ``.trigger``: The ``digio.trigger[N]`` command tree.
            - ``.writebit()``: The ``digio.writebit()`` function.
            - ``.writeport()``: The ``digio.writeport()`` function.
            - ``.writeprotect``: The ``digio.writeprotect`` attribute.
        """
        return self._digio

    @property
    def display(self) -> Display:
        """Return the ``display`` command tree.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``display.clear()`` function.
            - ``.getannunciators()``: The ``display.getannunciators()`` function.
            - ``.getcursor()``: The ``display.getcursor()`` function.
            - ``.getlastkey()``: The ``display.getlastkey()`` function.
            - ``.gettext()``: The ``display.gettext()`` function.
            - ``.inputvalue()``: The ``display.inputvalue()`` function.
            - ``.loadmenu``: The ``display.loadmenu`` command tree.
            - ``.locallockout``: The ``display.locallockout`` attribute.
            - ``.menu()``: The ``display.menu()`` function.
            - ``.prompt()``: The ``display.prompt()`` function.
            - ``.screen``: The ``display.screen`` attribute.
            - ``.sendkey()``: The ``display.sendkey()`` function.
            - ``.setcursor()``: The ``display.setcursor()`` function.
            - ``.settext()``: The ``display.settext()`` function.
            - ``.trigger``: The ``display.trigger`` command tree.
            - ``.waitkey()``: The ``display.waitkey()`` function.
        """
        return self._display

    @property
    def dmm(self) -> Dmm:
        """Return the ``dmm`` command tree.

        Sub-properties and sub-methods:
            - ``.adjustment``: The ``dmm.adjustment`` command tree.
            - ``.aperture``: The ``dmm.aperture`` attribute.
            - ``.appendbuffer()``: The ``dmm.appendbuffer()`` function.
            - ``.autorange``: The ``dmm.autorange`` attribute.
            - ``.autozero``: The ``dmm.autozero`` attribute.
            - ``.buffer``: The ``dmm.buffer`` command tree.
            - ``.calibration``: The ``dmm.calibration`` command tree.
            - ``.close()``: The ``dmm.close()`` function.
            - ``.configure``: The ``dmm.configure`` command tree.
            - ``.connect``: The ``dmm.connect`` attribute.
            - ``.dbreference``: The ``dmm.dbreference`` attribute.
            - ``.detectorbandwidth``: The ``dmm.detectorbandwidth`` attribute.
            - ``.displaydigits``: The ``dmm.displaydigits`` attribute.
            - ``.drycircuit``: The ``dmm.drycircuit`` attribute.
            - ``.filter``: The ``dmm.filter`` command tree.
            - ``.fourrtd``: The ``dmm.fourrtd`` attribute.
            - ``.func``: The ``dmm.func`` attribute.
            - ``.getconfig()``: The ``dmm.getconfig()`` function.
            - ``.inputdivider``: The ``dmm.inputdivider`` attribute.
            - ``.limit``: The ``dmm.limit[r]`` command tree.
            - ``.linesync``: The ``dmm.linesync`` attribute.
            - ``.makebuffer()``: The ``dmm.makebuffer()`` function.
            - ``.math``: The ``dmm.math`` command tree.
            - ``.measure()``: The ``dmm.measure()`` function.
            - ``.measurecount``: The ``dmm.measurecount`` attribute.
            - ``.measurewithptp()``: The ``dmm.measurewithptp()`` function.
            - ``.measurewithtime()``: The ``dmm.measurewithtime()`` function.
            - ``.nplc``: The ``dmm.nplc`` attribute.
            - ``.offsetcompensation``: The ``dmm.offsetcompensation`` attribute.
            - ``.open()``: The ``dmm.open()`` function.
            - ``.opendetector``: The ``dmm.opendetector`` attribute.
            - ``.range``: The ``dmm.range`` attribute.
            - ``.refjunction``: The ``dmm.refjunction`` attribute.
            - ``.rel``: The ``dmm.rel`` command tree.
            - ``.reset()``: The ``dmm.reset()`` function.
            - ``.rtdalpha``: The ``dmm.rtdalpha`` attribute.
            - ``.rtdbeta``: The ``dmm.rtdbeta`` attribute.
            - ``.rtddelta``: The ``dmm.rtddelta`` attribute.
            - ``.rtdzero``: The ``dmm.rtdzero`` attribute.
            - ``.savebuffer()``: The ``dmm.savebuffer()`` function.
            - ``.setconfig()``: The ``dmm.setconfig()`` function.
            - ``.simreftemperature``: The ``dmm.simreftemperature`` attribute.
            - ``.thermocouple``: The ``dmm.thermocouple`` attribute.
            - ``.threertd``: The ``dmm.threertd`` attribute.
            - ``.threshold``: The ``dmm.threshold`` attribute.
            - ``.transducer``: The ``dmm.transducer`` attribute.
        """
        return self._dmm

    @property
    def errorqueue(self) -> Errorqueue:
        """Return the ``errorqueue`` command tree.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``errorqueue.clear()`` function.
            - ``.count``: The ``errorqueue.count`` attribute.
            - ``.next()``: The ``errorqueue.next()`` function.
        """
        return self._errorqueue

    @property
    def eventlog(self) -> Eventlog:
        """Return the ``eventlog`` command tree.

        Sub-properties and sub-methods:
            - ``.all()``: The ``eventlog.all()`` function.
            - ``.clear()``: The ``eventlog.clear()`` function.
            - ``.count``: The ``eventlog.count`` attribute.
            - ``.enable``: The ``eventlog.enable`` attribute.
            - ``.next()``: The ``eventlog.next()`` function.
            - ``.overwritemethod``: The ``eventlog.overwritemethod`` attribute.
        """
        return self._eventlog

    @property
    def format(self) -> Format:
        """Return the ``format`` command tree.

        Sub-properties and sub-methods:
            - ``.asciiprecision``: The ``format.asciiprecision`` attribute.
            - ``.byteorder``: The ``format.byteorder`` attribute.
            - ``.data``: The ``format.data`` attribute.
        """
        return self._format

    @property
    def fs(self) -> Fs:
        """Return the ``fs`` command tree.

        Sub-properties and sub-methods:
            - ``.chdir()``: The ``fs.chdir()`` function.
            - ``.cwd()``: The ``fs.cwd()`` function.
            - ``.is_dir()``: The ``fs.is_dir()`` function.
            - ``.is_file()``: The ``fs.is_file()`` function.
            - ``.mkdir()``: The ``fs.mkdir()`` function.
            - ``.readdir()``: The ``fs.readdir()`` function.
            - ``.rmdir()``: The ``fs.rmdir()`` function.
        """
        return self._fs

    @property
    def gpib(self) -> Gpib:
        """Return the ``gpib`` command tree.

        Sub-properties and sub-methods:
            - ``.address``: The ``gpib.address`` attribute.
        """
        return self._gpib

    @property
    def io(self) -> Io:
        """Return the ``io`` command tree.

        Sub-properties and sub-methods:
            - ``.close()``: The ``io.close()`` function.
            - ``.flush()``: The ``io.flush()`` function.
            - ``.input()``: The ``io.input()`` function.
            - ``.open()``: The ``io.open()`` function.
            - ``.output()``: The ``io.output()`` function.
            - ``.read()``: The ``io.read()`` function.
            - ``.type()``: The ``io.type()`` function.
            - ``.write()``: The ``io.write()`` function.
        """
        return self._io

    @property
    def lan(self) -> Lan:
        """Return the ``lan`` command tree.

        Sub-properties and sub-methods:
            - ``.applysettings()``: The ``lan.applysettings()`` function.
            - ``.config``: The ``lan.config`` command tree.
            - ``.lxidomain``: The ``lan.lxidomain`` attribute.
            - ``.nagle``: The ``lan.nagle`` attribute.
            - ``.reset()``: The ``lan.reset()`` function.
            - ``.restoredefaults()``: The ``lan.restoredefaults()`` function.
            - ``.status``: The ``lan.status`` command tree.
            - ``.trigger``: The ``lan.trigger[N]`` command tree.
        """
        return self._lan

    @property
    def localnode(self) -> Localnode:
        """Return the ``localnode`` command tree.

        Sub-properties and sub-methods:
            - ``.description``: The ``localnode.description`` attribute.
            - ``.emulation``: The ``localnode.emulation`` attribute.
            - ``.license``: The ``localnode.license`` attribute.
            - ``.linefreq``: The ``localnode.linefreq`` attribute.
            - ``.model``: The ``localnode.model`` attribute.
            - ``.password``: The ``localnode.password`` attribute.
            - ``.passwordmode``: The ``localnode.passwordmode`` attribute.
            - ``.prompts``: The ``localnode.prompts`` attribute.
            - ``.prompts4882``: The ``localnode.prompts4882`` attribute.
            - ``.reset()``: The ``localnode.reset()`` function.
            - ``.revision``: The ``localnode.revision`` attribute.
            - ``.serialno``: The ``localnode.serialno`` attribute.
            - ``.showerrors``: The ``localnode.showerrors`` attribute.
        """
        return self._localnode

    @property
    def memory(self) -> Memory:
        """Return the ``memory`` command tree.

        Sub-properties and sub-methods:
            - ``.available()``: The ``memory.available()`` function.
            - ``.used()``: The ``memory.used()`` function.
        """
        return self._memory

    @property
    def node(self) -> Dict[int, NodeItem]:
        """Return the ``node[N]`` command tree.

        Info:
            - ``N``, the node number of this instrument (1 to 63).

        Sub-properties and sub-methods:
            - ``.execute()``: The ``node[N].execute()`` function.
            - ``.getglobal()``: The ``node[N].getglobal()`` function.
            - ``.setglobal()``: The ``node[N].setglobal()`` function.
        """
        return self._node

    @property
    def os(self) -> Os:
        """Return the ``os`` command tree.

        Sub-properties and sub-methods:
            - ``.time()``: The ``os.time()`` function.
        """
        return self._os

    @property
    def ptp(self) -> Ptp:
        """Return the ``ptp`` command tree.

        Sub-properties and sub-methods:
            - ``.domain``: The ``ptp.domain`` attribute.
            - ``.ds``: The ``ptp.ds`` command tree.
            - ``.enable``: The ``ptp.enable`` attribute.
            - ``.portstate``: The ``ptp.portstate`` attribute.
            - ``.slavepreferred``: The ``ptp.slavepreferred`` attribute.
            - ``.time()``: The ``ptp.time()`` function.
            - ``.utcoffset``: The ``ptp.utcoffset`` attribute.
        """
        return self._ptp

    @property
    def scan(self) -> Scan:
        """Return the ``scan`` command tree.

        Sub-properties and sub-methods:
            - ``.abort()``: The ``scan.abort()`` function.
            - ``.add()``: The ``scan.add()`` function.
            - ``.addimagestep()``: The ``scan.addimagestep()`` function.
            - ``.addwrite()``: The ``scan.addwrite()`` function.
            - ``.background()``: The ``scan.background()`` function.
            - ``.bypass``: The ``scan.bypass`` attribute.
            - ``.create()``: The ``scan.create()`` function.
            - ``.execute()``: The ``scan.execute()`` function.
            - ``.list()``: The ``scan.list()`` function.
            - ``.measurecount``: The ``scan.measurecount`` attribute.
            - ``.mode``: The ``scan.mode`` attribute.
            - ``.nobufferbackground()``: The ``scan.nobufferbackground()`` function.
            - ``.nobufferexecute()``: The ``scan.nobufferexecute()`` function.
            - ``.reset()``: The ``scan.reset()`` function.
            - ``.scancount``: The ``scan.scancount`` attribute.
            - ``.state()``: The ``scan.state()`` function.
            - ``.stepcount``: The ``scan.stepcount`` attribute.
            - ``.trigger``: The ``scan.trigger`` command tree.
        """
        return self._scan

    @property
    def schedule(self) -> Schedule:
        """Return the ``schedule`` command tree.

        Sub-properties and sub-methods:
            - ``.alarm``: The ``schedule.alarm[N]`` command tree.
            - ``.disable()``: The ``schedule.disable()`` function.
        """
        return self._schedule

    @property
    def script(self) -> Script:
        """Return the ``script`` command tree.

        Sub-properties and sub-methods:
            - ``.anonymous``: The ``script.anonymous`` attribute.
            - ``.delete()``: The ``script.delete()`` function.
            - ``.load()``: The ``script.load()`` function.
            - ``.new()``: The ``script.new()`` function.
            - ``.newautorun()``: The ``script.newautorun()`` function.
            - ``.restore()``: The ``script.restore()`` function.
            - ``.run()``: The ``script.run()`` function.
        """
        return self._script

    @property
    def script_var(self) -> Dict[str, Scriptvar]:
        """Return the ``scriptVar`` command tree.

        Info:
            - ``scriptVar``, the name of the variable that references the script.

        Sub-properties and sub-methods:
            - ``.autorun``: The ``scriptVar.autorun`` attribute.
            - ``.list()``: The ``scriptVar.list()`` function.
            - ``.name``: The ``scriptVar.name`` attribute.
            - ``.run()``: The ``scriptVar.run()`` function.
            - ``.save()``: The ``scriptVar.save()`` function.
            - ``.source``: The ``scriptVar.source`` attribute.
        """
        return self._script_var

    @property
    def setup(self) -> Setup:
        """Return the ``setup`` command tree.

        Sub-properties and sub-methods:
            - ``.poweron``: The ``setup.poweron`` attribute.
            - ``.recall()``: The ``setup.recall()`` function.
            - ``.save()``: The ``setup.save()`` function.
        """
        return self._setup

    @property
    def slot(self) -> Dict[int, SlotItem]:
        """Return the ``slot[slot]`` command tree.

        Info:
            - ``slot``, the slot number.

        Sub-properties and sub-methods:
            - ``.banks``: The ``slot[slot].banks`` command tree.
            - ``.columns``: The ``slot[slot].columns`` command tree.
            - ``.commonsideohms``: The ``slot[slot].commonsideohms`` attribute.
            - ``.digio``: The ``slot[slot].digio`` attribute.
            - ``.idn``: The ``slot[slot].idn`` attribute.
            - ``.interlock``: The ``slot[slot].interlock`` command tree.
            - ``.isolated``: The ``slot[slot].isolated`` attribute.
            - ``.matrix``: The ``slot[slot].matrix`` attribute.
            - ``.maxvoltage``: The ``slot[slot].maxvoltage`` attribute.
            - ``.multiplexer``: The ``slot[slot].multiplexer`` attribute.
            - ``.poles``: The ``slot[slot].poles`` command tree.
            - ``.pseudocard``: The ``slot[slot].pseudocard`` attribute.
            - ``.rows``: The ``slot[slot].rows`` command tree.
            - ``.tempsensor``: The ``slot[slot].tempsensor`` attribute.
            - ``.thermal``: The ``slot[slot].thermal`` command tree.
        """
        return self._slot

    @property
    def status(self) -> Status:
        """Return the ``status`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.condition`` attribute.
            - ``.measurement``: The ``status.measurement`` command tree.
            - ``.node_enable``: The ``status.node_enable`` attribute.
            - ``.node_event``: The ``status.node_event`` attribute.
            - ``.operation``: The ``status.operation`` command tree.
            - ``.questionable``: The ``status.questionable`` command tree.
            - ``.request_enable``: The ``status.request_enable`` attribute.
            - ``.request_event``: The ``status.request_event`` attribute.
            - ``.reset()``: The ``status.reset()`` function.
            - ``.standard``: The ``status.standard`` command tree.
            - ``.system``: The ``status.system`` command tree.
            - ``.system2``: The ``status.system2`` command tree.
            - ``.system3``: The ``status.system3`` command tree.
            - ``.system4``: The ``status.system4`` command tree.
            - ``.system5``: The ``status.system5`` command tree.
        """
        return self._status

    @property
    def timer(self) -> Timer:
        """Return the ``timer`` command tree.

        Sub-properties and sub-methods:
            - ``.measure``: The ``timer.measure`` command tree.
            - ``.reset()``: The ``timer.reset()`` function.
        """
        return self._timer

    @property
    def trigger(self) -> Trigger:
        """Return the ``trigger`` command tree.

        Constants:
            - ``.EVENT_ID``: The command interface trigger event number.

        Sub-properties and sub-methods:
            - ``.blender``: The ``trigger.blender[N]`` command tree.
            - ``.clear()``: The ``trigger.clear()`` function.
            - ``.timer``: The ``trigger.timer[N]`` command tree.
            - ``.wait()``: The ``trigger.wait()`` function.
        """
        return self._trigger

    @property
    def tsplink(self) -> Tsplink:
        """Return the ``tsplink`` command tree.

        Sub-properties and sub-methods:
            - ``.group``: The ``tsplink.group`` attribute.
            - ``.master``: The ``tsplink.master`` attribute.
            - ``.node``: The ``tsplink.node`` attribute.
            - ``.readbit()``: The ``tsplink.readbit()`` function.
            - ``.readport()``: The ``tsplink.readport()`` function.
            - ``.reset()``: The ``tsplink.reset()`` function.
            - ``.state``: The ``tsplink.state`` attribute.
            - ``.trigger``: The ``tsplink.trigger[N]`` command tree.
            - ``.writebit()``: The ``tsplink.writebit()`` function.
            - ``.writeport()``: The ``tsplink.writeport()`` function.
            - ``.writeprotect``: The ``tsplink.writeprotect`` attribute.
        """
        return self._tsplink

    @property
    def tspnet(self) -> Tspnet:
        """Return the ``tspnet`` command tree.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``tspnet.clear()`` function.
            - ``.connect()``: The ``tspnet.connect()`` function.
            - ``.disconnect()``: The ``tspnet.disconnect()`` function.
            - ``.execute()``: The ``tspnet.execute()`` function.
            - ``.idn()``: The ``tspnet.idn()`` function.
            - ``.read()``: The ``tspnet.read()`` function.
            - ``.readavailable()``: The ``tspnet.readavailable()`` function.
            - ``.reset()``: The ``tspnet.reset()`` function.
            - ``.termination()``: The ``tspnet.termination()`` function.
            - ``.timeout``: The ``tspnet.timeout`` attribute.
            - ``.tsp``: The ``tspnet.tsp`` command tree.
            - ``.write()``: The ``tspnet.write()`` function.
        """
        return self._tspnet

    @property
    def upgrade(self) -> Upgrade:
        """Return the ``upgrade`` command tree.

        Sub-properties and sub-methods:
            - ``.previous()``: The ``upgrade.previous()`` function.
            - ``.unit()``: The ``upgrade.unit()`` function.
        """
        return self._upgrade

    @property
    def userstring(self) -> Userstring:
        """Return the ``userstring`` command tree.

        Sub-properties and sub-methods:
            - ``.add()``: The ``userstring.add()`` function.
            - ``.delete()``: The ``userstring.delete()`` function.
            - ``.get()``: The ``userstring.get()`` function.
        """
        return self._userstring

    def createconfigscript(self, script_name: str) -> None:
        """Run the ``createconfigscript()`` function.

        Description:
            - This function creates a setup file that captures most of the present settings of the
              instrument.

        TSP Syntax:
            ```
            - createconfigscript()
            ```

        Args:
            script_name: A string that represents the name of the script that will be created.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'createconfigscript("{script_name}")'
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``createconfigscript()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def delay(self, seconds: int) -> None:
        """Run the ``delay()`` function.

        Description:
            - This function delays the execution of the commands that follow it.

        TSP Syntax:
            ```
            - delay()
            ```

        Args:
            seconds: The number of seconds to delay (0 s to 100 ks).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"delay({seconds})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``delay()`` function."
            raise NoDeviceProvidedError(msg) from error

    def exit(self) -> None:
        """Run the ``exit()`` function.

        Description:
            - This function stops a script that is presently running.

        TSP Syntax:
            ```
            - exit()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                "exit()"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``exit()`` function."
            raise NoDeviceProvidedError(msg) from error

    def gettimezone(self) -> str:
        """Run the ``gettimezone()`` function.

        Description:
            - This function retrieves the local time zone.

        TSP Syntax:
            ```
            - gettimezone()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                "print(gettimezone())"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``gettimezone()`` function."
            raise NoDeviceProvidedError(msg) from error

    def makegetter(self, table: str, attribute_name: str) -> str:
        """Run the ``makegetter()`` function.

        Description:
            - This function creates a function to get the value of an attribute.

        TSP Syntax:
            ```
            - makegetter()
            ```

        Args:
            table: Read-only table where the attribute is located.
            attribute_name: A string representing the name of the attribute.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print(makegetter({table}, "{attribute_name}"))'
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``makegetter()`` function."
            raise NoDeviceProvidedError(msg) from error

    def makesetter(self, table: str, attribute_name: str) -> str:
        """Run the ``makesetter()`` function.

        Description:
            - This function creates a function that, when called, sets the value of an attribute.

        TSP Syntax:
            ```
            - makesetter()
            ```

        Args:
            table: Read-only table where the attribute is located.
            attribute_name: The string name of the attribute.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print(makesetter({table}, "{attribute_name}"))'
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``makesetter()`` function."
            raise NoDeviceProvidedError(msg) from error

    def opc(self) -> None:
        """Run the ``opc()`` function.

        Description:
            - This function sets the operation complete (OPC) bit after all pending commands,
              including overlapped commands, have been executed.

        TSP Syntax:
            ```
            - opc()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                "opc()"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``opc()`` function."
            raise NoDeviceProvidedError(msg) from error

    def print(self, value: str) -> None:
        """Run the ``print()`` function.

        Description:
            - This function generates a response message.

        TSP Syntax:
            ```
            - print()
            ```

        Args:
            value: The first argument to output.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"print({value})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``print()`` function."
            raise NoDeviceProvidedError(msg) from error

    def printbuffer(self, start_index: int, end_index: int, buffer_var: str) -> str:
        """Run the ``printbuffer()`` function.

        Description:
            - This function prints data from tables or reading buffer subtables.

        TSP Syntax:
            ```
            - printbuffer()
            ```

        Args:
            start_index: Beginning index of the buffer to print; this must be more than one and less
                than endIndex.
            end_index: Ending index of the buffer to print; this must be more than startIndex and
                less than the index of the last entry in the tables.
            buffer_var: Name of first table or reading buffer subtable to print; may be a default
                buffer (defbuffer1 or defbuffer2) or a user-defined buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"printbuffer({start_index}, {end_index}, {buffer_var})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``printbuffer()`` function."
            raise NoDeviceProvidedError(msg) from error

    def printnumber(self, value: str) -> str:
        """Run the ``printnumber()`` function.

        Description:
            - This function prints numbers using the configured format.

        TSP Syntax:
            ```
            - printnumber()
            ```

        Args:
            value: First value to print in the configured format.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"printnumber({value})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``printnumber()`` function."
            raise NoDeviceProvidedError(msg) from error

    def reset(self, system: Optional[str] = None) -> None:
        """Run the ``reset()`` function.

        Description:
            - This function resets commands to their default settings and clears the buffers.

        TSP Syntax:
            ```
            - reset()
            ```

        Args:
            system (optional): If the node is the master, the entire system is reset.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (system,) if x is not None)
            self._device.write(  # type: ignore[union-attr]
                f"reset({function_args})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``reset()`` function."
            raise NoDeviceProvidedError(msg) from error

    def settime(self, time: str) -> None:
        """Run the ``settime()`` function.

        Description:
            - This function sets the real-time clock (sets present time of the system).

        TSP Syntax:
            ```
            - settime()
            ```

        Args:
            time: The time in seconds since January 1, 1970 UTC.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"settime({time})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``settime()`` function."
            raise NoDeviceProvidedError(msg) from error

    def settimezone(
        self,
        offset: str,
        dst_offset: Optional[str] = None,
        dst_start: Optional[str] = None,
        dst_end: Optional[str] = None,
    ) -> None:
        """Run the ``settimezone()`` function.

        Description:
            - This function sets the local time zone.

        TSP Syntax:
            ```
            - settimezone()
            ```

        Args:
            offset: String representing offset from UTC.
            dst_offset (optional): String representing the daylight savings offset from UTC.
            dst_start (optional): String representing when daylight savings time starts.
            dst_end (optional): String representing when daylight savings time ends.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{offset}"',
                    f'"{dst_offset}"' if dst_offset is not None else None,
                    f'"{dst_start}"' if dst_start is not None else None,
                    f'"{dst_end}"' if dst_end is not None else None,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"settimezone({function_args})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``settimezone()`` function."
            raise NoDeviceProvidedError(msg) from error

    def waitcomplete(self, group: Optional[str] = None) -> None:
        """Run the ``waitcomplete()`` function.

        Description:
            - This function waits for all previously started overlapped commands to complete.

        TSP Syntax:
            ```
            - waitcomplete()
            ```

        Args:
            group (optional): Specifies which TSP-Link group on which to wait.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (group,) if x is not None)
            self._device.write(  # type: ignore[union-attr]
                f"waitcomplete({function_args})"
            )
        except AttributeError as error:
            msg = (
                "No TSPControl object was provided, unable to run the ``waitcomplete()`` function."
            )
            raise NoDeviceProvidedError(msg) from error


class SS3706AMixin:
    """A mixin that provides access to the SS3706A commands and constants.

    Properties:
        - ``.command_argument_constants``: The SS3706A command argument constants.
        - ``.commands``: The SS3706A commands.
    """

    @cached_property
    def command_argument_constants(self) -> SS3706ACommandConstants:  # pylint: disable=no-self-use
        """Return the SS3706A command argument constants.

        This provides access to all the string constants which can be used as arguments for SS3706A
        commands.
        """
        return SS3706ACommandConstants()

    @cached_property
    def commands(self) -> SS3706ACommands:
        """Return the SS3706A commands.

        This provides access to all the commands for the SS3706A device. See the documentation of
        each sub-property for more usage information.

        Sub-properties and sub-methods:
            - ``.beeper``: The ``beeper`` command tree.
            - ``.bit``: The ``bit`` command tree.
            - ``.buffer_var``: The ``bufferVar`` command tree.
            - ``.channel``: The ``channel`` command tree.
            - ``.comm``: The ``comm`` command tree.
            - ``.createconfigscript()``: The ``createconfigscript()`` function.
            - ``.dataqueue``: The ``dataqueue`` command tree.
            - ``.delay()``: The ``delay()`` function.
            - ``.digio``: The ``digio`` command tree.
            - ``.display``: The ``display`` command tree.
            - ``.dmm``: The ``dmm`` command tree.
            - ``.errorqueue``: The ``errorqueue`` command tree.
            - ``.eventlog``: The ``eventlog`` command tree.
            - ``.exit()``: The ``exit()`` function.
            - ``.format``: The ``format`` command tree.
            - ``.fs``: The ``fs`` command tree.
            - ``.gettimezone()``: The ``gettimezone()`` function.
            - ``.gpib``: The ``gpib`` command tree.
            - ``.io``: The ``io`` command tree.
            - ``.lan``: The ``lan`` command tree.
            - ``.localnode``: The ``localnode`` command tree.
            - ``.makegetter()``: The ``makegetter()`` function.
            - ``.makesetter()``: The ``makesetter()`` function.
            - ``.memory``: The ``memory`` command tree.
            - ``.node``: The ``node[N]`` command tree.
            - ``.opc()``: The ``opc()`` function.
            - ``.os``: The ``os`` command tree.
            - ``.print()``: The ``print()`` function.
            - ``.printbuffer()``: The ``printbuffer()`` function.
            - ``.printnumber()``: The ``printnumber()`` function.
            - ``.ptp``: The ``ptp`` command tree.
            - ``.reset()``: The ``reset()`` function.
            - ``.scan``: The ``scan`` command tree.
            - ``.schedule``: The ``schedule`` command tree.
            - ``.script_var``: The ``scriptVar`` command tree.
            - ``.script``: The ``script`` command tree.
            - ``.settime()``: The ``settime()`` function.
            - ``.settimezone()``: The ``settimezone()`` function.
            - ``.setup``: The ``setup`` command tree.
            - ``.slot``: The ``slot[slot]`` command tree.
            - ``.status``: The ``status`` command tree.
            - ``.timer``: The ``timer`` command tree.
            - ``.trigger``: The ``trigger`` command tree.
            - ``.tsplink``: The ``tsplink`` command tree.
            - ``.tspnet``: The ``tspnet`` command tree.
            - ``.upgrade``: The ``upgrade`` command tree.
            - ``.userstring``: The ``userstring`` command tree.
            - ``.waitcomplete()``: The ``waitcomplete()`` function.
        """
        device = self if isinstance(self, TSPControl) else None
        return SS3706ACommands(device)
