"""The MP5103 commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional

from tm_devices.driver_mixins.device_control.tsp_control import TSPControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_3skc3w_mp.bit import Bit
from .gen_3skc3w_mp.digio import Digio
from .gen_3skc3w_mp.eventlog import Eventlog
from .gen_3skc3w_mp.firmware import Firmware
from .gen_3skc3w_mp.format import Format
from .gen_3skc3w_mp.fs import Fs
from .gen_3skc3w_mp.lan import Lan
from .gen_3skc3w_mp.localnode import Localnode
from .gen_3skc3w_mp.node import NodeItem
from .gen_3skc3w_mp.os import Os
from .gen_3skc3w_mp.script import Script
from .gen_3skc3w_mp.slot import SlotItem
from .gen_3skc3w_mp.status import Status
from .gen_3skc3w_mp.timer import Timer
from .gen_3skc3w_mp.trigger import Trigger
from .gen_3skc3w_mp.tsplink import Tsplink
from .gen_3skc3w_mp.tspnet import Tspnet
from .gen_3skc3w_mp.usbtmc import Usbtmc
from .gen_3skc3w_mp.user import User
from .gen_4dh8ja_mpmpsumsmu.buffervar import Buffervar
from .gen_fnz1de_mpsmuss.io import Io
from .gen_fs14fx_daqdmmmpsmuss.dataqueue import Dataqueue
from .gen_fs14fx_daqdmmmpsmuss.userstring import Userstring
from .gen_fualds_mpsmu.scriptvar import Scriptvar
from .helpers import DefaultDictPassKeyToFactory, NoDeviceProvidedError


# pylint: disable=too-few-public-methods
class MP5103CommandConstants:
    """The MP5103 command argument constants.

    This provides access to all the string constants which can be used as arguments for MP5103
    commands.
    """

    DATAQUEUE_CAPACITY = "dataqueue.CAPACITY"
    DIGIO_TRIGGER_N_EVENT_ID = "digio.trigger[N].EVENT_ID"
    TRIGGER_EVENT_ID = "trigger.EVENT_ID"
    TRIGGER_EVENT_NONE = "trigger.EVENT_NONE"
    TRIGGER_GENERATOR_N_EVENT_ID = "trigger.generator[N].EVENT_ID"
    TRIGGER_TIMER_N_EVENT_ID = "trigger.timer[N].EVENT_ID"
    TSPLINK_TRIGGER_N_EVENT_ID = "tsplink.trigger[N].EVENT_ID"


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class MP5103Commands:
    """The MP5103 commands.

    This provides access to all the commands for the MP5103 device. See the documentation of each
    property for more usage information.

    Properties and methods:
        - ``.bit``: The ``bit`` command tree.
        - ``.buffer_var``: The ``bufferVar`` command tree.
        - ``.dataqueue``: The ``dataqueue`` command tree.
        - ``.delay()``: The ``delay()`` function.
        - ``.digio``: The ``digio`` command tree.
        - ``.eventlog``: The ``eventlog`` command tree.
        - ``.exit()``: The ``exit()`` function.
        - ``.firmware``: The ``firmware`` command tree.
        - ``.format``: The ``format`` command tree.
        - ``.fs``: The ``fs`` command tree.
        - ``.gettimezone()``: The ``gettimezone()`` function.
        - ``.io``: The ``io`` command tree.
        - ``.lan``: The ``lan`` command tree.
        - ``.localnode``: The ``localnode`` command tree.
        - ``.login()``: The ``login()`` function.
        - ``.logout()``: The ``logout()`` function.
        - ``.makegetter()``: The ``makegetter()`` function.
        - ``.makesetter()``: The ``makesetter()`` function.
        - ``.node``: The ``node[N]`` command tree.
        - ``.opc()``: The ``opc()`` function.
        - ``.os``: The ``os`` command tree.
        - ``.print()``: The ``print()`` function.
        - ``.printbuffer()``: The ``printbuffer()`` function.
        - ``.printnumber()``: The ``printnumber()`` function.
        - ``.reset()``: The ``reset()`` function.
        - ``.script_var``: The ``scriptVar`` command tree.
        - ``.script``: The ``script`` command tree.
        - ``.settime()``: The ``settime()`` function.
        - ``.settimezone()``: The ``settimezone()`` function.
        - ``.slot``: The ``slot[Z]`` command tree.
        - ``.status``: The ``status`` command tree.
        - ``.timer``: The ``timer`` command tree.
        - ``.trigger``: The ``trigger`` command tree.
        - ``.tsplink``: The ``tsplink`` command tree.
        - ``.tspnet``: The ``tspnet`` command tree.
        - ``.usbtmc``: The ``usbtmc`` command tree.
        - ``.user``: The ``user`` command tree.
        - ``.userstring``: The ``userstring`` command tree.
        - ``.waitcomplete()``: The ``waitcomplete()`` function.
    """

    def __init__(self, device: Optional[TSPControl] = None) -> None:
        self._device = device
        self._bit = Bit(device)
        self._buffer_var: Dict[str, Buffervar] = DefaultDictPassKeyToFactory(
            lambda x: Buffervar(device, str(x))
        )
        self._dataqueue = Dataqueue(device)
        self._digio = Digio(device)
        self._eventlog = Eventlog(device)
        self._firmware = Firmware(device)
        self._format = Format(device)
        self._fs = Fs(device)
        self._io = Io(device)
        self._lan = Lan(device)
        self._localnode = Localnode(device)
        self._node: Dict[int, NodeItem] = DefaultDictPassKeyToFactory(
            lambda x: NodeItem(device, f"node[{x}]")
        )
        self._os = Os(device)
        self._script = Script(device)
        self._script_var: Dict[str, Scriptvar] = DefaultDictPassKeyToFactory(
            lambda x: Scriptvar(device, str(x))
        )
        self._slot: Dict[int, SlotItem] = DefaultDictPassKeyToFactory(
            lambda x: SlotItem(device, f"slot[{x}]")
        )
        self._status = Status(device)
        self._timer = Timer(device)
        self._trigger = Trigger(device)
        self._tsplink = Tsplink(device)
        self._tspnet = Tspnet(device)
        self._usbtmc = Usbtmc(device)
        self._user = User(device)
        self._userstring = Userstring(device)

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
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Sub-properties and sub-methods:
            - ``.appendmode``: The ``bufferVar.appendmode`` attribute.
            - ``.cachemode``: The ``bufferVar.cachemode`` attribute.
            - ``.capacity``: The ``bufferVar.capacity`` attribute.
            - ``.clear()``: The ``bufferVar.clear()`` function.
            - ``.clearcache()``: The ``bufferVar.clearcache()`` function.
            - ``.columnname``: The ``bufferVar.columnname`` command tree.
            - ``.fillcount``: The ``bufferVar.fillcount`` attribute.
            - ``.fillmode``: The ``bufferVar.fillmode`` attribute.
            - ``.fractionalseconds``: The ``bufferVar.fractionalseconds[N]`` attribute.
            - ``.measurefunctions``: The ``bufferVar.measurefunctions[N]`` attribute.
            - ``.measureranges``: The ``bufferVar.measureranges[N]`` attribute.
            - ``.n``: The ``bufferVar.n`` attribute.
            - ``.readings``: The ``bufferVar.readings[N]`` attribute.
            - ``.seconds``: The ``bufferVar.seconds[N]`` attribute.
            - ``.sourcefunctions``: The ``bufferVar.sourcefunctions[N]`` attribute.
            - ``.sourceoutputstates``: The ``bufferVar.sourceoutputstates[N]`` attribute.
            - ``.sourceranges``: The ``bufferVar.sourceranges[N]`` attribute.
            - ``.sourcevalues``: The ``bufferVar.sourcevalues[N]`` attribute.
            - ``.statuses``: The ``bufferVar.statuses[N]`` attribute.
            - ``.timestampresolution``: The ``bufferVar.timestampresolution`` attribute.
            - ``.timestamps``: The ``bufferVar.timestamps[N]`` attribute.
        """
        return self._buffer_var

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
    def eventlog(self) -> Eventlog:
        """Return the ``eventlog`` command tree.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``eventlog.clear()`` function.
            - ``.count``: The ``eventlog.count`` attribute.
            - ``.next()``: The ``eventlog.next()`` function.
        """
        return self._eventlog

    @property
    def firmware(self) -> Firmware:
        """Return the ``firmware`` command tree.

        Sub-properties and sub-methods:
            - ``.load()``: The ``firmware.load()`` function.
            - ``.update()``: The ``firmware.update()`` function.
        """
        return self._firmware

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
            - ``.cwd()``: The ``fs.cwd()`` function.
            - ``.is_dir()``: The ``fs.is_dir()`` function.
            - ``.is_file()``: The ``fs.is_file()`` function.
            - ``.mkdir()``: The ``fs.mkdir()`` function.
            - ``.readdir()``: The ``fs.readdir()`` function.
            - ``.rmdir()``: The ``fs.rmdir()`` function.
        """
        return self._fs

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
            - ``.autoconnect``: The ``lan.autoconnect`` attribute.
            - ``.config``: The ``lan.config`` command tree.
            - ``.enable``: The ``lan.enable`` attribute.
            - ``.hislip``: The ``lan.hislip`` command tree.
            - ``.identify``: The ``lan.identify`` attribute.
            - ``.ipconfig()``: The ``lan.ipconfig()`` function.
            - ``.linktimeout``: The ``lan.linktimeout`` attribute.
            - ``.nagle``: The ``lan.nagle`` attribute.
            - ``.rawsocket``: The ``lan.rawsocket`` command tree.
            - ``.reset()``: The ``lan.reset()`` function.
            - ``.restoredefaults()``: The ``lan.restoredefaults()`` function.
            - ``.status``: The ``lan.status`` command tree.
            - ``.telnet``: The ``lan.telnet`` command tree.
        """
        return self._lan

    @property
    def localnode(self) -> Localnode:
        """Return the ``localnode`` command tree.

        Sub-properties and sub-methods:
            - ``.license``: The ``localnode.license`` attribute.
            - ``.linefreq``: The ``localnode.linefreq`` attribute.
            - ``.manufacturer``: The ``localnode.manufacturer`` attribute.
            - ``.model``: The ``localnode.model`` attribute.
            - ``.prompts``: The ``localnode.prompts`` attribute.
            - ``.prompts4882``: The ``localnode.prompts4882`` attribute.
            - ``.serialno``: The ``localnode.serialno`` attribute.
            - ``.showerrors``: The ``localnode.showerrors`` attribute.
            - ``.version``: The ``localnode.version`` attribute.
        """
        return self._localnode

    @property
    def node(self) -> Dict[int, NodeItem]:
        """Return the ``node[N]`` command tree.

        Info:
            - ``N``, the node number of the specified instrument.

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
            - ``.clock()``: The ``os.clock()`` function.
            - ``.remove()``: The ``os.remove()`` function.
            - ``.rename()``: The ``os.rename()`` function.
            - ``.time()``: The ``os.time()`` function.
        """
        return self._os

    @property
    def script(self) -> Script:
        """Return the ``script`` command tree.

        Sub-properties and sub-methods:
            - ``.delete()``: The ``script.delete()`` function.
            - ``.load()``: The ``script.load()`` function.
            - ``.new()``: The ``script.new()`` function.
            - ``.newautorun()``: The ``script.newautorun()`` function.
            - ``.restore()``: The ``script.restore()`` function.
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
    def slot(self) -> Dict[int, SlotItem]:
        """Return the ``slot[Z]`` command tree.

        Info:
            - ``Z``, the module slot number.

        Sub-properties and sub-methods:
            - ``.firmware``: The ``slot[Z].firmware`` command tree.
            - ``.license``: The ``slot[Z].license`` attribute.
            - ``.manufacturer``: The ``slot[Z].manufacturer`` attribute.
            - ``.model``: The ``slot[Z].model`` attribute.
            - ``.psu``: The ``slot[Z].psu[X]`` command tree.
            - ``.serialno``: The ``slot[Z].serialno`` attribute.
            - ``.smu``: The ``slot[Z].smu[X]`` command tree.
            - ``.status``: The ``slot[Z].status`` command tree.
            - ``.trigger``: The ``slot[Z].trigger`` command tree.
            - ``.version``: The ``slot[Z].version`` attribute.
        """
        return self._slot

    @property
    def status(self) -> Status:
        """Return the ``status`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.condition`` attribute.
            - ``.node_enable``: The ``status.node_enable`` attribute.
            - ``.node_event``: The ``status.node_event`` attribute.
            - ``.operation``: The ``status.operation`` command tree.
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
            - ``.cleartime()``: The ``timer.cleartime()`` function.
            - ``.measure``: The ``timer.measure`` command tree.
            - ``.readtime()``: The ``timer.readtime()`` function.
        """
        return self._timer

    @property
    def trigger(self) -> Trigger:
        """Return the ``trigger`` command tree.

        Constants:
            - ``.EVENT_ID``: The command interface trigger event number.
            - ``.EVENT_NONE``: This trigger event ID is never generated. It is used to disconnect
              stimulus inputs.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``trigger.clear()`` function.
            - ``.detector``: The ``trigger.detector[N]`` command tree.
            - ``.generator``: The ``trigger.generator[N]`` command tree.
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
    def usbtmc(self) -> Usbtmc:
        """Return the ``usbtmc`` command tree.

        Sub-properties and sub-methods:
            - ``.access``: The ``usbtmc.access`` attribute.
        """
        return self._usbtmc

    @property
    def user(self) -> User:
        """Return the ``user`` command tree.

        Sub-properties and sub-methods:
            - ``.password``: The ``user.password`` command tree.
        """
        return self._user

    @property
    def userstring(self) -> Userstring:
        """Return the ``userstring`` command tree.

        Sub-properties and sub-methods:
            - ``.add()``: The ``userstring.add()`` function.
            - ``.delete()``: The ``userstring.delete()`` function.
            - ``.get()``: The ``userstring.get()`` function.
        """
        return self._userstring

    def delay(self, seconds: int) -> None:
        """Run the ``delay()`` function.

        Description:
            - This function delays the execution of the commands that follow it.

        TSP Syntax:
            ```
            - delay()
            ```

        Args:
            seconds: The number of seconds to delay.

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
            - This function stops a script that is presently running

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

    def login(self, password: str) -> None:
        """Run the ``login()`` function.

        Description:
            - This command logs a user in to the mainframe and allows remote access.

        TSP Syntax:
            ```
            - login()
            ```

        Args:
            password: A string that represents the login password. The default value is no password.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'login("{password}")'
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``login()`` function."
            raise NoDeviceProvidedError(msg) from error

    def logout(self) -> None:
        """Run the ``logout()`` function.

        Description:
            - This function logs a user out of the mainframe.

        TSP Syntax:
            ```
            - logout()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                "logout()"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``logout()`` function."
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
            - This function sets the operation complete status bit when all overlapped commands are
              completed.

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
            buffer_var: First table or reading buffer subtable to print.

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
            - This function resets commands on all slots and channels to their default settings.

        TSP Syntax:
            ```
            - reset()
            ```

        Args:
            system (optional): What to reset.

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

    def settime(self, seconds: str, fractional: Optional[int] = None) -> None:
        """Run the ``settime()`` function.

        Description:
            - This function sets the present time and the real time clock.

        TSP Syntax:
            ```
            - settime()
            ```

        Args:
            seconds: The time in seconds since January 1, 1970, UTC.
            fractional (optional): The number of fractional seconds.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    seconds,
                    fractional,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"settime({function_args})"
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


class MP5103Mixin:
    """A mixin that provides access to the MP5103 commands and constants.

    Properties:
        - ``.command_argument_constants``: The MP5103 command argument constants.
        - ``.commands``: The MP5103 commands.
    """

    @cached_property
    def command_argument_constants(self) -> MP5103CommandConstants:  # pylint: disable=no-self-use
        """Return the MP5103 command argument constants.

        This provides access to all the string constants which can be used as arguments for MP5103
        commands.
        """
        return MP5103CommandConstants()

    @cached_property
    def commands(self) -> MP5103Commands:
        """Return the MP5103 commands.

        This provides access to all the commands for the MP5103 device. See the documentation of
        each sub-property for more usage information.

        Sub-properties and sub-methods:
            - ``.bit``: The ``bit`` command tree.
            - ``.buffer_var``: The ``bufferVar`` command tree.
            - ``.dataqueue``: The ``dataqueue`` command tree.
            - ``.delay()``: The ``delay()`` function.
            - ``.digio``: The ``digio`` command tree.
            - ``.eventlog``: The ``eventlog`` command tree.
            - ``.exit()``: The ``exit()`` function.
            - ``.firmware``: The ``firmware`` command tree.
            - ``.format``: The ``format`` command tree.
            - ``.fs``: The ``fs`` command tree.
            - ``.gettimezone()``: The ``gettimezone()`` function.
            - ``.io``: The ``io`` command tree.
            - ``.lan``: The ``lan`` command tree.
            - ``.localnode``: The ``localnode`` command tree.
            - ``.login()``: The ``login()`` function.
            - ``.logout()``: The ``logout()`` function.
            - ``.makegetter()``: The ``makegetter()`` function.
            - ``.makesetter()``: The ``makesetter()`` function.
            - ``.node``: The ``node[N]`` command tree.
            - ``.opc()``: The ``opc()`` function.
            - ``.os``: The ``os`` command tree.
            - ``.print()``: The ``print()`` function.
            - ``.printbuffer()``: The ``printbuffer()`` function.
            - ``.printnumber()``: The ``printnumber()`` function.
            - ``.reset()``: The ``reset()`` function.
            - ``.script_var``: The ``scriptVar`` command tree.
            - ``.script``: The ``script`` command tree.
            - ``.settime()``: The ``settime()`` function.
            - ``.settimezone()``: The ``settimezone()`` function.
            - ``.slot``: The ``slot[Z]`` command tree.
            - ``.status``: The ``status`` command tree.
            - ``.timer``: The ``timer`` command tree.
            - ``.trigger``: The ``trigger`` command tree.
            - ``.tsplink``: The ``tsplink`` command tree.
            - ``.tspnet``: The ``tspnet`` command tree.
            - ``.usbtmc``: The ``usbtmc`` command tree.
            - ``.user``: The ``user`` command tree.
            - ``.userstring``: The ``userstring`` command tree.
            - ``.waitcomplete()``: The ``waitcomplete()`` function.
        """
        device = self if isinstance(self, TSPControl) else None
        return MP5103Commands(device)
