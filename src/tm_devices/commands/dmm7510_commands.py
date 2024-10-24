# ruff: noqa: D402,PLR0913
"""The DMM7510 commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional

from tm_devices.driver_mixins.device_control.tsp_control import TSPControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_d6b496_dmm.acal import Acal
from .gen_d6b496_dmm.buffer import Buffer
from .gen_d6b496_dmm.buffervar import Buffervar
from .gen_d6b496_dmm.display import Display
from .gen_d6b496_dmm.dmm import Dmm
from .gen_d6b496_dmm.fan import Fan
from .gen_d6b496_dmm.localnode import Localnode
from .gen_d6b496_dmm.trigger import Trigger
from .gen_dbdq3i_smudaqdmm.beeper import Beeper
from .gen_dbdq3i_smudaqdmm.eventlog import Eventlog
from .gen_dbdq3i_smudaqdmm.file import File
from .gen_dbdq3i_smudaqdmm.format import Format
from .gen_dbdq3i_smudaqdmm.lan import Lan
from .gen_dbdq3i_smudaqdmm.scriptvar import Scriptvar
from .gen_dbdq3i_smudaqdmm.timer import Timer
from .gen_dbqd7k_dmm.digio import Digio
from .gen_dbqd7k_dmm.node import NodeItem
from .gen_dbqd7k_dmm.status import Status
from .gen_dbqd7k_dmm.tsplink import Tsplink
from .gen_dbqd7k_dmm.tspnet import Tspnet
from .gen_dbqd7k_dmm.upgrade import Upgrade
from .gen_dcpheg_daqdmm.smu import Smu
from .gen_dd4xnb_smudaqdmm.script import Script
from .gen_eat5s3_smudaqdmmss.dataqueue import Dataqueue
from .gen_eat5s3_smudaqdmmss.fs import Fs
from .gen_eat5s3_smudaqdmmss.userstring import Userstring
from .gen_eg5ll2_smudaqdmmss.gpib import Gpib
from .helpers import DefaultDictPassKeyToFactory, NoDeviceProvidedError


# pylint: disable=too-few-public-methods
class DMM7510CommandConstants:
    """The DMM7510 command argument constants.

    This provides access to all the string constants which can be used as arguments for DMM7510
    commands.
    """

    BUFFER_COL_ALL = "buffer.COL_ALL"
    BUFFER_COL_BRIEF = "buffer.COL_BRIEF"
    BUFFER_COL_DISPLAY_DIGITS = "buffer.COL_DISPLAY_DIGITS"
    BUFFER_COL_EXTRA = "buffer.COL_EXTRA"
    BUFFER_COL_EXTRA_RANGE = "buffer.COL_EXTRA_RANGE"
    BUFFER_COL_EXTRA_UNIT = "buffer.COL_EXTRA_UNIT"
    BUFFER_COL_EXTRA_VALUE = "buffer.COL_EXTRA_VALUE"
    BUFFER_COL_INDEX = "buffer.COL_INDEX"
    BUFFER_COL_LIMITS = "buffer.COL_LIMITS"
    BUFFER_COL_MATH = "buffer.COL_MATH"
    BUFFER_COL_ORIGIN = "buffer.COL_ORIGIN"
    BUFFER_COL_QUESTIONABLE = "buffer.COL_QUESTIONABLE"
    BUFFER_COL_RANGE_DIGITS = "buffer.COL_RANGE_DIGITS"
    BUFFER_COL_READING = "buffer.COL_READING"
    BUFFER_COL_STANDARD = "buffer.COL_STANDARD"
    BUFFER_COL_START = "buffer.COL_START"
    BUFFER_COL_STATUS = "buffer.COL_STATUS"
    BUFFER_COL_TERMINAL = "buffer.COL_TERMINAL"
    BUFFER_COL_TIMESTAMP_READING = "buffer.COL_TIMESTAMP_READING"
    BUFFER_COL_TIME_ABSOLUTE = "buffer.COL_TIME_ABSOLUTE"
    BUFFER_COL_TIME_PARTS = "buffer.COL_TIME_PARTS"
    BUFFER_COL_TIME_RAW = "buffer.COL_TIME_RAW"
    BUFFER_COL_TIME_RELATIVE = "buffer.COL_TIME_RELATIVE"
    BUFFER_COL_UNIT = "buffer.COL_UNIT"
    BUFFER_DIGITS_3_5 = "buffer.DIGITS_3_5"
    BUFFER_DIGITS_4_5 = "buffer.DIGITS_4_5"
    BUFFER_DIGITS_5_5 = "buffer.DIGITS_5_5"
    BUFFER_DIGITS_6_5 = "buffer.DIGITS_6_5"
    BUFFER_DIGITS_7_5 = "buffer.DIGITS_7_5"
    BUFFER_DIGITS_8_5 = "buffer.DIGITS_8_5"
    BUFFER_EXPR_ADD = "buffer.EXPR_ADD"
    BUFFER_EXPR_AVERAGE = "buffer.EXPR_AVERAGE"
    BUFFER_EXPR_DIVIDE = "buffer.EXPR_DIVIDE"
    BUFFER_EXPR_EXPONENT = "buffer.EXPR_EXPONENT"
    BUFFER_EXPR_LOG10 = "buffer.EXPR_LOG10"
    BUFFER_EXPR_MULTIPLY = "buffer.EXPR_MULTIPLY"
    BUFFER_EXPR_NONE = "buffer.EXPR_NONE"
    BUFFER_EXPR_POLY = "buffer.EXPR_POLY"
    BUFFER_EXPR_POWER = "buffer.EXPR_POWER"
    BUFFER_EXPR_RATE = "buffer.EXPR_RATE"
    BUFFER_EXPR_RECIPROCAL = "buffer.EXPR_RECIPROCAL"
    BUFFER_EXPR_SQROOT = "buffer.EXPR_SQROOT"
    BUFFER_EXPR_SUBTRACT = "buffer.EXPR_SUBTRACT"
    BUFFER_FILL_CONTINUOUS = "buffer.FILL_CONTINUOUS"
    BUFFER_FILL_ONCE = "buffer.FILL_ONCE"
    BUFFER_OFF = "buffer.OFF"
    BUFFER_ON = "buffer.ON"
    BUFFER_SAVE_FORMAT_TIME = "buffer.SAVE_FORMAT_TIME"
    BUFFER_SAVE_RAW_TIME = "buffer.SAVE_RAW_TIME"
    BUFFER_SAVE_RELATIVE_TIME = "buffer.SAVE_RELATIVE_TIME"
    BUFFER_SAVE_TIMESTAMP_TIME = "buffer.SAVE_TIMESTAMP_TIME"
    BUFFER_STAT_LIMIT1_HIGH = "buffer.STAT_LIMIT1_HIGH"
    BUFFER_STAT_LIMIT1_LOW = "buffer.STAT_LIMIT1_LOW"
    BUFFER_STAT_LIMIT2_HIGH = "buffer.STAT_LIMIT2_HIGH"
    BUFFER_STAT_LIMIT2_LOW = "buffer.STAT_LIMIT2_LOW"
    BUFFER_STAT_ORIGIN = "buffer.STAT_ORIGIN"
    BUFFER_STAT_QUESTIONABLE = "buffer.STAT_QUESTIONABLE"
    BUFFER_STAT_REL = "buffer.STAT_REL"
    BUFFER_STAT_SCAN = "buffer.STAT_SCAN"
    BUFFER_STAT_START_GROUP = "buffer.STAT_START_GROUP"
    BUFFER_STAT_TERMINAL = "buffer.STAT_TERMINAL"
    BUFFER_STYLE_COMPACT = "buffer.STYLE_COMPACT"
    BUFFER_STYLE_FULL = "buffer.STYLE_FULL"
    BUFFER_STYLE_STANDARD = "buffer.STYLE_STANDARD"
    BUFFER_STYLE_WRITABLE = "buffer.STYLE_WRITABLE"
    BUFFER_STYLE_WRITABLE_FULL = "buffer.STYLE_WRITABLE_FULL"
    BUFFER_UNIT_AMP = "buffer.UNIT_AMP"
    BUFFER_UNIT_AMP_AC = "buffer.UNIT_AMP_AC"
    BUFFER_UNIT_CELSIUS = "buffer.UNIT_CELSIUS"
    BUFFER_UNIT_CUSTOM1 = "buffer.UNIT_CUSTOM1"
    BUFFER_UNIT_CUSTOM2 = "buffer.UNIT_CUSTOM2"
    BUFFER_UNIT_CUSTOM3 = "buffer.UNIT_CUSTOM3"
    BUFFER_UNIT_DAC = "buffer.UNIT_DAC"
    BUFFER_UNIT_DBM = "buffer.UNIT_DBM"
    BUFFER_UNIT_DECIBEL = "buffer.UNIT_DECIBEL"
    BUFFER_UNIT_DIO = "buffer.UNIT_DIO"
    BUFFER_UNIT_FAHRENHEIT = "buffer.UNIT_FAHRENHEIT"
    BUFFER_UNIT_FARAD = "buffer.UNIT_FARAD"
    BUFFER_UNIT_HERTZ = "buffer.UNIT_HERTZ"
    BUFFER_UNIT_KELVIN = "buffer.UNIT_KELVIN"
    BUFFER_UNIT_NONE = "buffer.UNIT_NONE"
    BUFFER_UNIT_OHM = "buffer.UNIT_OHM"
    BUFFER_UNIT_PERCENT = "buffer.UNIT_PERCENT"
    BUFFER_UNIT_RATIO = "buffer.UNIT_RATIO"
    BUFFER_UNIT_RECIPROCAL = "buffer.UNIT_RECIPROCAL"
    BUFFER_UNIT_SECOND = "buffer.UNIT_SECOND"
    BUFFER_UNIT_TOT = "buffer.UNIT_TOT"
    BUFFER_UNIT_VOLT = "buffer.UNIT_VOLT"
    BUFFER_UNIT_VOLT_AC = "buffer.UNIT_VOLT_AC"
    BUFFER_UNIT_WATT = "buffer.UNIT_WATT"
    BUFFER_UNIT_X = "buffer.UNIT_X"
    DATAQUEUE_CAPACITY = "dataqueue.CAPACITY"
    DIGIO_MODE_DIGITAL_IN = "digio.MODE_DIGITAL_IN"
    DIGIO_MODE_DIGITAL_OPEN_DRAIN = "digio.MODE_DIGITAL_OPEN_DRAIN"
    DIGIO_MODE_DIGITAL_OUT = "digio.MODE_DIGITAL_OUT"
    DIGIO_MODE_SYNCHRONOUS_ACCEPTOR = "digio.MODE_SYNCHRONOUS_ACCEPTOR"
    DIGIO_MODE_SYNCHRONOUS_MASTER = "digio.MODE_SYNCHRONOUS_MASTER"
    DIGIO_MODE_TRIGGER_IN = "digio.MODE_TRIGGER_IN"
    DIGIO_MODE_TRIGGER_OPEN_DRAIN = "digio.MODE_TRIGGER_OPEN_DRAIN"
    DIGIO_MODE_TRIGGER_OUT = "digio.MODE_TRIGGER_OUT"
    DIGIO_STATE_HIGH = "digio.STATE_HIGH"
    DIGIO_STATE_LOW = "digio.STATE_LOW"
    DISPLAY_BUTTONS_CANCEL = "display.BUTTONS_CANCEL"
    DISPLAY_BUTTONS_NONE = "display.BUTTONS_NONE"
    DISPLAY_BUTTONS_OK = "display.BUTTONS_OK"
    DISPLAY_BUTTONS_OKCANCEL = "display.BUTTONS_OKCANCEL"
    DISPLAY_BUTTONS_YESNO = "display.BUTTONS_YESNO"
    DISPLAY_BUTTONS_YESNOCANCEL = "display.BUTTONS_YESNOCANCEL"
    DISPLAY_BUTTON_CANCEL = "display.BUTTON_CANCEL"
    DISPLAY_BUTTON_NO = "display.BUTTON_NO"
    DISPLAY_BUTTON_OK = "display.BUTTON_OK"
    DISPLAY_BUTTON_YES = "display.BUTTON_YES"
    DISPLAY_DIGITS_4_5 = "display.DIGITS_4_5"
    DISPLAY_DIGITS_5_5 = "display.DIGITS_5_5"
    DISPLAY_DIGITS_6_5 = "display.DIGITS_6_5"
    DISPLAY_FORMAT_EXPONENT = "display.FORMAT_EXPONENT"
    DISPLAY_FORMAT_PREFIX = "display.FORMAT_PREFIX"
    DISPLAY_NFORMAT_DECIMAL = "display.NFORMAT_DECIMAL"
    DISPLAY_NFORMAT_EXPONENT = "display.NFORMAT_EXPONENT"
    DISPLAY_NFORMAT_INTEGER = "display.NFORMAT_INTEGER"
    DISPLAY_NFORMAT_PREFIX = "display.NFORMAT_PREFIX"
    DISPLAY_SCREEN_GRAPH = "display.SCREEN_GRAPH"
    DISPLAY_SCREEN_GRAPH_SWIPE = "display.SCREEN_GRAPH_SWIPE"
    DISPLAY_SCREEN_HISTOGRAM = "display.SCREEN_HISTOGRAM"
    DISPLAY_SCREEN_HOME = "display.SCREEN_HOME"
    DISPLAY_SCREEN_HOME_LARGE_READING = "display.SCREEN_HOME_LARGE_READING"
    DISPLAY_SCREEN_PROCESSING = "display.SCREEN_PROCESSING"
    DISPLAY_SCREEN_READING_TABLE = "display.SCREEN_READING_TABLE"
    DISPLAY_SCREEN_SETTINGS_SWIPE = "display.SCREEN_SETTINGS_SWIPE"
    DISPLAY_SCREEN_STATS_SWIPE = "display.SCREEN_STATS_SWIPE"
    DISPLAY_SCREEN_USER_SWIPE = "display.SCREEN_USER_SWIPE"
    DISPLAY_SFORMAT_ANY = "display.SFORMAT_ANY"
    DISPLAY_SFORMAT_BUFFER_NAME = "display.SFORMAT_BUFFER_NAME"
    DISPLAY_SFORMAT_UPPER = "display.SFORMAT_UPPER"
    DISPLAY_SFORMAT_UPPER_LOWER = "display.SFORMAT_UPPER_LOWER"
    DISPLAY_STATE_BLACKOUT = "display.STATE_BLACKOUT"
    DISPLAY_STATE_LCD_100 = "display.STATE_LCD_100"
    DISPLAY_STATE_LCD_25 = "display.STATE_LCD_25"
    DISPLAY_STATE_LCD_50 = "display.STATE_LCD_50"
    DISPLAY_STATE_LCD_75 = "display.STATE_LCD_75"
    DISPLAY_STATE_LCD_OFF = "display.STATE_LCD_OFF"
    DMM_OFF = "dmm.OFF"
    DMM_ON = "dmm.ON"
    EVENTLOG_SEV_ALL = "eventlog.SEV_ALL"
    EVENTLOG_SEV_ERROR = "eventlog.SEV_ERROR"
    EVENTLOG_SEV_INFO = "eventlog.SEV_INFO"
    EVENTLOG_SEV_WARN = "eventlog.SEV_WARN"
    FILE_MODE_APPEND = "file.MODE_APPEND"
    FILE_MODE_READ = "file.MODE_READ"
    FILE_MODE_WRITE = "file.MODE_WRITE"
    FILE_READ_ALL = "file.READ_ALL"
    FILE_READ_LINE = "file.READ_LINE"
    FILE_READ_NUMBER = "file.READ_NUMBER"
    FORMAT_ASCII = "format.ASCII"
    FORMAT_BIGENDIAN = "format.BIGENDIAN"
    FORMAT_LITTLEENDIAN = "format.LITTLEENDIAN"
    FORMAT_REAL32 = "format.REAL32"
    FORMAT_REAL64 = "format.REAL64"
    LAN_MODE_AUTO = "lan.MODE_AUTO"
    LAN_MODE_MANUAL = "lan.MODE_MANUAL"
    LAN_OFF = "lan.OFF"
    LAN_ON = "lan.ON"
    LAN_PROTOCOL_MULTICAST = "lan.PROTOCOL_MULTICAST"
    LAN_PROTOCOL_TCP = "lan.PROTOCOL_TCP"
    LAN_PROTOCOL_UDP = "lan.PROTOCOL_UDP"
    LOCALNODE_ACCESS_EXCLUSIVE = "localnode.ACCESS_EXCLUSIVE"
    LOCALNODE_ACCESS_FULL = "localnode.ACCESS_FULL"
    LOCALNODE_ACCESS_LOCKOUT = "localnode.ACCESS_LOCKOUT"
    LOCALNODE_ACCESS_PROTECTED = "localnode.ACCESS_PROTECTED"
    LOCALNODE_DISABLE = "localnode.DISABLE"
    LOCALNODE_ENABLE = "localnode.ENABLE"
    SMU_AUDIBLE_FAIL = "smu.AUDIBLE_FAIL"
    SMU_AUDIBLE_NONE = "smu.AUDIBLE_NONE"
    SMU_AUDIBLE_PASS = "smu.AUDIBLE_PASS"
    SMU_OFF = "smu.OFF"
    SMU_ON = "smu.ON"
    TRIGGER_BLOCK_BRANCH_ALWAYS = "trigger.BLOCK_BRANCH_ALWAYS"
    TRIGGER_BLOCK_BRANCH_COUNTER = "trigger.BLOCK_BRANCH_COUNTER"
    TRIGGER_BLOCK_BRANCH_DELTA = "trigger.BLOCK_BRANCH_DELTA"
    TRIGGER_BLOCK_BRANCH_LIMIT_CONSTANT = "trigger.BLOCK_BRANCH_LIMIT_CONSTANT"
    TRIGGER_BLOCK_BRANCH_LIMIT_DYNAMIC = "trigger.BLOCK_BRANCH_LIMIT_DYNAMIC"
    TRIGGER_BLOCK_BRANCH_ONCE = "trigger.BLOCK_BRANCH_ONCE"
    TRIGGER_BLOCK_BRANCH_ONCE_EXCLUDED = "trigger.BLOCK_BRANCH_ONCE_EXCLUDED"
    TRIGGER_BLOCK_BRANCH_ON_EVENT = "trigger.BLOCK_BRANCH_ON_EVENT"
    TRIGGER_BLOCK_BUFFER_CLEAR = "trigger.BLOCK_BUFFER_CLEAR"
    TRIGGER_BLOCK_CONFIG_NEXT = "trigger.BLOCK_CONFIG_NEXT"
    TRIGGER_BLOCK_CONFIG_PREV = "trigger.BLOCK_CONFIG_PREV"
    TRIGGER_BLOCK_DELAY_CONSTANT = "trigger.BLOCK_DELAY_CONSTANT"
    TRIGGER_BLOCK_DELAY_DYNAMIC = "trigger.BLOCK_DELAY_DYNAMIC"
    TRIGGER_BLOCK_DIGITAL_IO = "trigger.BLOCK_DIGITAL_IO"
    TRIGGER_BLOCK_LOG_EVENT = "trigger.BLOCK_LOG_EVENT"
    TRIGGER_BLOCK_MEASURE = "trigger.BLOCK_MEASURE"
    TRIGGER_BLOCK_MEASURE_DIGITIZE = "trigger.BLOCK_MEASURE_DIGITIZE"
    TRIGGER_BLOCK_NOP = "trigger.BLOCK_NOP"
    TRIGGER_BLOCK_NOTIFY = "trigger.BLOCK_NOTIFY"
    TRIGGER_BLOCK_RESET_BRANCH_COUNT = "trigger.BLOCK_RESET_BRANCH_COUNT"
    TRIGGER_BLOCK_WAIT = "trigger.BLOCK_WAIT"
    TRIGGER_CLEAR_ENTER = "trigger.CLEAR_ENTER"
    TRIGGER_CLEAR_NEVER = "trigger.CLEAR_NEVER"
    TRIGGER_CONT_AUTO = "trigger.CONT_AUTO"
    TRIGGER_CONT_OFF = "trigger.CONT_OFF"
    TRIGGER_CONT_RESTART = "trigger.CONT_RESTART"
    TRIGGER_COUNT_AUTO = "trigger.COUNT_AUTO"
    TRIGGER_COUNT_INFINITE = "trigger.COUNT_INFINITE"
    TRIGGER_COUNT_STOP = "trigger.COUNT_STOP"
    TRIGGER_EDGE_EITHER = "trigger.EDGE_EITHER"
    TRIGGER_EDGE_FALLING = "trigger.EDGE_FALLING"
    TRIGGER_EDGE_RISING = "trigger.EDGE_RISING"
    TRIGGER_EVENT_BLENDERN = "trigger.EVENT_BLENDERN"
    TRIGGER_EVENT_COMMAND = "trigger.EVENT_COMMAND"
    TRIGGER_EVENT_DIGION = "trigger.EVENT_DIGION"
    TRIGGER_EVENT_DISPLAY = "trigger.EVENT_DISPLAY"
    TRIGGER_EVENT_LANN = "trigger.EVENT_LANN"
    TRIGGER_EVENT_NONE = "trigger.EVENT_NONE"
    TRIGGER_EVENT_NOTIFYN = "trigger.EVENT_NOTIFYN"
    TRIGGER_EVENT_TIMER1 = "trigger.EVENT_TIMER1"
    TRIGGER_EVENT_TIMER2 = "trigger.EVENT_TIMER2"
    TRIGGER_EVENT_TIMER3 = "trigger.EVENT_TIMER3"
    TRIGGER_EVENT_TIMER4 = "trigger.EVENT_TIMER4"
    TRIGGER_EVENT_TSPLINKN = "trigger.EVENT_TSPLINKN"
    TRIGGER_LIMIT_ABOVE = "trigger.LIMIT_ABOVE"
    TRIGGER_LIMIT_BELOW = "trigger.LIMIT_BELOW"
    TRIGGER_LIMIT_INSIDE = "trigger.LIMIT_INSIDE"
    TRIGGER_LIMIT_OUTSIDE = "trigger.LIMIT_OUTSIDE"
    TRIGGER_LOGIC_NEGATIVE = "trigger.LOGIC_NEGATIVE"
    TRIGGER_LOGIC_POSITIVE = "trigger.LOGIC_POSITIVE"
    TRIGGER_LOG_ERROR1 = "trigger.LOG_ERROR1"
    TRIGGER_LOG_ERROR2 = "trigger.LOG_ERROR2"
    TRIGGER_LOG_ERROR3 = "trigger.LOG_ERROR3"
    TRIGGER_LOG_ERROR4 = "trigger.LOG_ERROR4"
    TRIGGER_LOG_INFO1 = "trigger.LOG_INFO1"
    TRIGGER_LOG_INFO2 = "trigger.LOG_INFO2"
    TRIGGER_LOG_INFO3 = "trigger.LOG_INFO3"
    TRIGGER_LOG_INFO4 = "trigger.LOG_INFO4"
    TRIGGER_LOG_WARN1 = "trigger.LOG_WARN1"
    TRIGGER_LOG_WARN2 = "trigger.LOG_WARN2"
    TRIGGER_LOG_WARN3 = "trigger.LOG_WARN3"
    TRIGGER_LOG_WARN4 = "trigger.LOG_WARN4"
    TRIGGER_LOG_WARN_ABORT = "trigger.LOG_WARN_ABORT"
    TRIGGER_OFF = "trigger.OFF"
    TRIGGER_ON = "trigger.ON"
    TRIGGER_STATE_ABORTED = "trigger.STATE_ABORTED"
    TRIGGER_STATE_ABORTING = "trigger.STATE_ABORTING"
    TRIGGER_STATE_BUILDING = "trigger.STATE_BUILDING"
    TRIGGER_STATE_EMPTY = "trigger.STATE_EMPTY"
    TRIGGER_STATE_FAILED = "trigger.STATE_FAILED"
    TRIGGER_STATE_IDLE = "trigger.STATE_IDLE"
    TRIGGER_STATE_RUNNING = "trigger.STATE_RUNNING"
    TRIGGER_STATE_WAITING = "trigger.STATE_WAITING"
    TRIGGER_WAIT_AND = "trigger.WAIT_AND"
    TRIGGER_WAIT_OR = "trigger.WAIT_OR"
    TSPLINK_MODE_DIGITAL_OPEN_DRAIN = "tsplink.MODE_DIGITAL_OPEN_DRAIN"
    TSPLINK_MODE_SYNCHRONOUS_ACCEPTOR = "tsplink.MODE_SYNCHRONOUS_ACCEPTOR"
    TSPLINK_MODE_SYNCHRONOUS_MASTER = "tsplink.MODE_SYNCHRONOUS_MASTER"
    TSPLINK_MODE_TRIGGER_OPEN_DRAIN = "tsplink.MODE_TRIGGER_OPEN_DRAIN"
    TSPLINK_STATE_HIGH = "tsplink.STATE_HIGH"
    TSPLINK_STATE_LOW = "tsplink.STATE_LOW"


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class DMM7510Commands:
    """The DMM7510 commands.

    This provides access to all the commands for the DMM7510 device. See the documentation of each
    property for more usage information.

    Properties and methods:
        - ``.acal``: The ``acal`` command tree.
        - ``.available()``: The ``available()`` function.
        - ``.beeper``: The ``beeper`` command tree.
        - ``.buffer_var``: The ``bufferVar`` command tree.
        - ``.buffer``: The ``buffer`` command tree.
        - ``.createconfigscript()``: The ``createconfigscript()`` function.
        - ``.dataqueue``: The ``dataqueue`` command tree.
        - ``.delay()``: The ``delay()`` function.
        - ``.digio``: The ``digio`` command tree.
        - ``.display``: The ``display`` command tree.
        - ``.dmm``: The ``dmm`` command tree.
        - ``.eventlog``: The ``eventlog`` command tree.
        - ``.exit()``: The ``exit()`` function.
        - ``.fan``: The ``fan`` command tree.
        - ``.file``: The ``file`` command tree.
        - ``.format``: The ``format`` command tree.
        - ``.fs``: The ``fs`` command tree.
        - ``.gpib``: The ``gpib`` command tree.
        - ``.lan``: The ``lan`` command tree.
        - ``.localnode``: The ``localnode`` command tree.
        - ``.node``: The ``node[N]`` command tree.
        - ``.opc()``: The ``opc()`` function.
        - ``.print()``: The ``print()`` function.
        - ``.printbuffer()``: The ``printbuffer()`` function.
        - ``.printnumber()``: The ``printnumber()`` function.
        - ``.reset()``: The ``reset()`` function.
        - ``.script_var``: The ``scriptVar`` command tree.
        - ``.script``: The ``script`` command tree.
        - ``.smu``: The ``smu`` command tree.
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
        self._acal = Acal(device)
        self._beeper = Beeper(device)
        self._buffer = Buffer(device)
        self._buffer_var: Dict[str, Buffervar] = DefaultDictPassKeyToFactory(
            lambda x: Buffervar(device, str(x))
        )
        self._dataqueue = Dataqueue(device)
        self._digio = Digio(device)
        self._display = Display(device)
        self._dmm = Dmm(device)
        self._eventlog = Eventlog(device)
        self._fan = Fan(device)
        self._file = File(device)
        self._format = Format(device)
        self._fs = Fs(device)
        self._gpib = Gpib(device)
        self._lan = Lan(device)
        self._localnode = Localnode(device)
        self._node: Dict[int, NodeItem] = DefaultDictPassKeyToFactory(
            lambda x: NodeItem(device, f"node[{x}]")
        )
        self._script = Script(device)
        self._script_var: Dict[str, Scriptvar] = DefaultDictPassKeyToFactory(
            lambda x: Scriptvar(device, str(x))
        )
        self._smu = Smu(device)
        self._status = Status(device)
        self._timer = Timer(device)
        self._trigger = Trigger(device)
        self._tsplink = Tsplink(device)
        self._tspnet = Tspnet(device)
        self._upgrade = Upgrade(device)
        self._userstring = Userstring(device)

    @property
    def acal(self) -> Acal:
        """Return the ``acal`` command tree.

        Sub-properties and sub-methods:
            - ``.count``: The ``acal.count`` attribute.
            - ``.lastrun``: The ``acal.lastrun`` command tree.
            - ``.nextrun``: The ``acal.nextrun`` command tree.
            - ``.revert()``: The ``acal.revert()`` function.
            - ``.run()``: The ``acal.run()`` function.
            - ``.schedule()``: The ``acal.schedule()`` function.
        """
        return self._acal

    @property
    def beeper(self) -> Beeper:
        """Return the ``beeper`` command tree.

        Sub-properties and sub-methods:
            - ``.beep()``: The ``beeper.beep()`` function.
        """
        return self._beeper

    @property
    def buffer(self) -> Buffer:
        """Return the ``buffer`` command tree.

        Constants:
            - ``.COL_ALL``: Save all data from the specified reading buffer.
            - ``.COL_BRIEF``: Save reading and relative time data from the specified reading buffer.
            - ``.COL_DISPLAY_DIGITS``: Save display digits from the specified reading buffer.
            - ``.COL_EXTRA``: Relative time and additional values if they exist (such as the sense
              voltage from a dc voltage ratio measurement).
            - ``.COL_EXTRA_RANGE``: Save sxtra value range digits from the specified reading buffer.
            - ``.COL_EXTRA_UNIT``: Save extra value units from the specified reading buffer.
            - ``.COL_EXTRA_VALUE``: Save extra values from the specified reading buffer.
            - ``.COL_INDEX``: Save index into buffer from the specified reading buffer.
            - ``.COL_LIMITS``: The status of all limits.
            - ``.COL_MATH``: Math enabled (F is math is not enabled; T if math is enabled) and
              relative time.
            - ``.COL_ORIGIN``: Save origin status from the specified reading buffer.
            - ``.COL_QUESTIONABLE``: Save questionable status from the specified reading buffer.
            - ``.COL_RANGE_DIGITS``: Save range digits from the specified reading buffer.
            - ``.COL_READING``: Save the measurement reading from the specified reading buffer.
            - ``.COL_STANDARD``: Save the relative time, reading, channel, and source value from the
              specified reading buffer.
            - ``.COL_START``: Save the status of the start group from the specified reading buffer.
            - ``.COL_STATUS``: Save the status information associated with the measurement from the
              specified reading buffer.
            - ``.COL_TERMINAL``: Save the terminal status from the specified reading buffer.
            - ``.COL_TIMESTAMP_READING``: Save the timestamp reading from the specified reading
              buffer.
            - ``.COL_TIME_ABSOLUTE``: Save the time when the data point was measured as an absolute
              from the specified reading buffer.
            - ``.COL_TIME_PARTS``: Save absolute time in multiple columns from the specified reading
              buffer.
            - ``.COL_TIME_RAW``: Save absolute time in seconds from the specified reading buffer.
            - ``.COL_TIME_RELATIVE``: Save the relative time when the data point was measured in
              seconds from the specified reading buffer.
            - ``.COL_UNIT``: Save the reading and the unit of measure from the specified reading
              buffer.
            - ``.DIGITS_3_5``: The number of digits to use for the  first measurement.
            - ``.DIGITS_4_5``: The number of digits to use for the  first measurement.
            - ``.DIGITS_5_5``: The number of digits to use for the  first measurement.
            - ``.DIGITS_6_5``: The number of digits to use for the  first measurement.
            - ``.DIGITS_7_5``: The number of digits to use for the  first measurement.
            - ``.DIGITS_8_5``: The number of digits to use for the  first measurement.
            - ``.EXPR_ADD``: Add the present and previous measurements.
            - ``.EXPR_AVERAGE``: Average the present and previous measurements.
            - ``.EXPR_DIVIDE``: Divide the present reading by the previous reading.
            - ``.EXPR_EXPONENT``: Exponent (10^present reading).
            - ``.EXPR_LOG10``: Log10 (log10(present reading)).
            - ``.EXPR_MULTIPLY``: Multiply the present and previous measurements.
            - ``.EXPR_NONE``: Remove the math expression.
            - ``.EXPR_POLY``: Polynomial where r is present reading and c is constant.
            - ``.EXPR_POWER``: Present reading raised to power of defined constant.
            - ``.EXPR_RATE``: Rate of change (present reading - previous reading)/(timestamp of
              present reading - timestamp of previous reading).
            - ``.EXPR_RECIPROCAL``: Reciprocal (1/present reading).
            - ``.EXPR_SQROOT``: Square root of the present reading.
            - ``.EXPR_SUBTRACT``: Present reading - previous reading.
            - ``.FILL_CONTINUOUS``: Fill the buffer continuously.
            - ``.FILL_ONCE``: Fill the buffer, then stop.
            - ``.OFF``: Do not log information events.
            - ``.ON``: Log information events.
            - ``.SAVE_FORMAT_TIME``: Include dates, times, and fractional seconds in the buffer.
            - ``.SAVE_RAW_TIME``: Include seconds and fractional seconds in the buffer.
            - ``.SAVE_RELATIVE_TIME``: Include relative timestamps in the buffer.
            - ``.SAVE_TIMESTAMP_TIME``: Include timestamps in the buffer.
            - ``.STAT_LIMIT1_HIGH``: Reading is above high limit 1.
            - ``.STAT_LIMIT1_LOW``: Reading is below low limit 1.
            - ``.STAT_LIMIT2_HIGH``: Reading is above high limit 2.
            - ``.STAT_LIMIT2_LOW``: Reading is below low limit 2.
            - ``.STAT_ORIGIN``: A/D converter from which reading originated; for most instruments,
              this will always be 0 (main). For digitizing instruments, can be 2 (digitize).
            - ``.STAT_QUESTIONABLE``: Measure status questionable.
            - ``.STAT_REL``: Relative offset.
            - ``.STAT_SCAN``: Scan.
            - ``.STAT_START_GROUP``: First reading in a group.
            - ``.STAT_TERMINAL``: Measure terminal, front is 1, rear is 0.
            - ``.STYLE_COMPACT``: Store readings with reduced accuracy (6.5 digits) with no
              formatting information, 1 μs accurate timestamp.
            - ``.STYLE_FULL``: Store the same information with full accuracy with formatting, plus
              additional information.
            - ``.STYLE_STANDARD``: Store readings with full accuracy with formatting.
            - ``.STYLE_WRITABLE``: Store external reading buffer data.
            - ``.STYLE_WRITABLE_FULL``: Store external reading buffer data with two reading values.
            - ``.UNIT_AMP``: Set units of measure to dc current.
            - ``.UNIT_AMP_AC``: Set units of measure to ac current.
            - ``.UNIT_CELSIUS``: Set units of measure to Celsius.
            - ``.UNIT_CUSTOM1``: Custom unit 1 (defined by buffer.unit()).
            - ``.UNIT_CUSTOM2``: Custom unit 2 (defined by buffer.unit()).
            - ``.UNIT_CUSTOM3``: Custom unit 3 (defined by buffer.unit()).
            - ``.UNIT_DAC``: Set units of measure to DAC (voltage).
            - ``.UNIT_DBM``: Set units of measure to decibel-milliwatts.
            - ``.UNIT_DECIBEL``: Set units of measure to decibels.
            - ``.UNIT_DIO``: Set units of measure to digital I/O.
            - ``.UNIT_FAHRENHEIT``: Set units of measure to Fahrenheit.
            - ``.UNIT_FARAD``: Set units of measure to capacitance.
            - ``.UNIT_HERTZ``: Set units of measure to frequency.
            - ``.UNIT_KELVIN``: Set units of measure to Kelvin.
            - ``.UNIT_NONE``: Set units of measure to no units.
            - ``.UNIT_OHM``: Set units of measure to ohms.
            - ``.UNIT_PERCENT``: Set units of measure to percent.
            - ``.UNIT_RATIO``: Set units of measure to dc voltage ratio.
            - ``.UNIT_RECIPROCAL``: Set units of measure to reciprocal.
            - ``.UNIT_SECOND``: Set units of measure to period.
            - ``.UNIT_TOT``: Set units of measure to totalizer.
            - ``.UNIT_VOLT``: Set units of measure to dc voltage.
            - ``.UNIT_VOLT_AC``: Set units of measure to ac voltage.
            - ``.UNIT_WATT``: Set units of measure to watts.
            - ``.UNIT_X``: Set units of measure to buffer.UNIT_X.

        Sub-properties and sub-methods:
            - ``.clearstats()``: The ``buffer.clearstats()`` function.
            - ``.delete()``: The ``buffer.delete()`` function.
            - ``.make()``: The ``buffer.make()`` function.
            - ``.save()``: The ``buffer.save()`` function.
            - ``.saveappend()``: The ``buffer.saveappend()`` function.
            - ``.write``: The ``buffer.write`` command tree.
        """
        return self._buffer

    @property
    def buffer_var(self) -> Dict[str, Buffervar]:
        """Return the ``bufferVar`` command tree.

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.

        Sub-properties and sub-methods:
            - ``.capacity``: The ``bufferVar.capacity`` attribute.
            - ``.clear()``: The ``bufferVar.clear()`` function.
            - ``.dates``: The ``bufferVar.dates[N]`` attribute.
            - ``.endindex``: The ``bufferVar.endindex`` attribute.
            - ``.extraformattedvalues``: The ``bufferVar.extraformattedvalues[N]`` attribute.
            - ``.extravalues``: The ``bufferVar.extravalues[N]`` attribute.
            - ``.extravalueunits``: The ``bufferVar.extravalueunits[N]`` attribute.
            - ``.fillmode``: The ``bufferVar.fillmode`` attribute.
            - ``.formattedreadings``: The ``bufferVar.formattedreadings[N]`` attribute.
            - ``.fractionalseconds``: The ``bufferVar.fractionalseconds[N]`` attribute.
            - ``.logstate``: The ``bufferVar.logstate`` attribute.
            - ``.n``: The ``bufferVar.n`` attribute.
            - ``.readings``: The ``bufferVar.readings[N]`` attribute.
            - ``.relativetimestamps``: The ``bufferVar.relativetimestamps[N]`` attribute.
            - ``.seconds``: The ``bufferVar.seconds[N]`` attribute.
            - ``.startindex``: The ``bufferVar.startindex`` attribute.
            - ``.statuses``: The ``bufferVar.statuses[N]`` attribute.
            - ``.times``: The ``bufferVar.times[N]`` attribute.
            - ``.timestamps``: The ``bufferVar.timestamps[N]`` attribute.
            - ``.units``: The ``bufferVar.units`` attribute.
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

        Constants:
            - ``.MODE_DIGITAL_IN``: Set the digital I/O mode to digital control, input.
            - ``.MODE_DIGITAL_OPEN_DRAIN``: Set the digital I/O mode to digital control, open-drain.
            - ``.MODE_DIGITAL_OUT``: Set the digital I/O mode to digital control, output.
            - ``.MODE_SYNCHRONOUS_ACCEPTOR``: Set the digital I/O mode to synchronous acceptor.
            - ``.MODE_SYNCHRONOUS_MASTER``: Set the digital I/O mode to synchronous master.
            - ``.MODE_TRIGGER_IN``: Set the digital I/O mode to trigger control, input.
            - ``.MODE_TRIGGER_OPEN_DRAIN``: Set the digital I/O mode to trigger control, open-drain.
            - ``.MODE_TRIGGER_OUT``: Set the digital I/O mode to trigger control, output.
            - ``.STATE_HIGH``: Set the line high.
            - ``.STATE_LOW``: Set the line low.

        Sub-properties and sub-methods:
            - ``.line``: The ``digio.line[N]`` command tree.
            - ``.readport()``: The ``digio.readport()`` function.
            - ``.writeport()``: The ``digio.writeport()`` function.
        """
        return self._digio

    @property
    def display(self) -> Display:
        """Return the ``display`` command tree.

        Constants:
            - ``.BUTTONS_CANCEL``: Display CANCEL on dialog.
            - ``.BUTTONS_NONE``: Display nothing on dialog.
            - ``.BUTTONS_OK``: Display OK on dialog.
            - ``.BUTTONS_OKCANCEL``: Display OK and CANCEL on dialog.
            - ``.BUTTONS_YESNO``: Display YES and NO on dialog.
            - ``.BUTTONS_YESNOCANCEL``: Display YES, NO, and CANCEL on dialog.
            - ``.BUTTON_CANCEL``: Return if CANCEL selected.
            - ``.BUTTON_NO``: Return if NO selected.
            - ``.BUTTON_OK``: Return if OK selected.
            - ``.BUTTON_YES``: Return if YES selected.
            - ``.DIGITS_4_5``: Set the front-panel display resolution to 4.5 digits.
            - ``.DIGITS_5_5``: Set the front-panel display resolution to 5.5 digits.
            - ``.DIGITS_6_5``: Set the front-panel display resolution to 6.5 digits.
            - ``.FORMAT_EXPONENT``: Use exponent format to display measurement readings on the
              front-panel display of
              the instrument.
            - ``.FORMAT_PREFIX``: Add a prefix to the units symbol, such as k, m, or u, to display
              measurement readings on the front-panel display of
              the instrument.
            - ``.NFORMAT_DECIMAL``: Allow decimal values.
            - ``.NFORMAT_EXPONENT``: Display numbers in exponent format.
            - ``.NFORMAT_INTEGER``: Allow integers (negative or positive) only.
            - ``.NFORMAT_PREFIX``: Display numbers with prefixes before the units symbol, such as n,
              m, or u.
            - ``.SCREEN_GRAPH``: Display the last selected graph screen tab.
            - ``.SCREEN_GRAPH_SWIPE``: Display graph swipe screen.
            - ``.SCREEN_HISTOGRAM``: Display Histogram.
            - ``.SCREEN_HOME``: Display Home screen.
            - ``.SCREEN_HOME_LARGE_READING``: Display Home screen with large readings.
            - ``.SCREEN_PROCESSING``: Open a screen that uses minimal CPU resources.
            - ``.SCREEN_READING_TABLE``: Display Reading Table screen.
            - ``.SCREEN_SETTINGS_SWIPE``: Display SETTINGS swipe screen.
            - ``.SCREEN_STATS_SWIPE``: Display STATISTICS swipe screen.
            - ``.SCREEN_USER_SWIPE``: Display USER swipe screen.
            - ``.SFORMAT_ANY``: Allow any characters.
            - ``.SFORMAT_BUFFER_NAME``: Allow both upper- and lower-case letters (no special
              characters).
            - ``.SFORMAT_UPPER``: Allow only upper-case letters.
            - ``.SFORMAT_UPPER_LOWER``: Allow both upper- and lower-case letters (no special
              characters).
            - ``.STATE_BLACKOUT``: Set display and all indicators off.
            - ``.STATE_LCD_100``: Set display to full brightness.
            - ``.STATE_LCD_25``: Set display to 25% brightness.
            - ``.STATE_LCD_50``: Set display to 50% brightness.
            - ``.STATE_LCD_75``: Set display to 75% brightness.
            - ``.STATE_LCD_OFF``: Set display to off.

        Sub-properties and sub-methods:
            - ``.activebuffer``: The ``display.activebuffer`` attribute.
            - ``.changescreen()``: The ``display.changescreen()`` function.
            - ``.clear()``: The ``display.clear()`` function.
            - ``.delete()``: The ``display.delete()`` function.
            - ``.input``: The ``display.input`` command tree.
            - ``.lightstate``: The ``display.lightstate`` attribute.
            - ``.prompt()``: The ``display.prompt()`` function.
            - ``.readingformat``: The ``display.readingformat`` attribute.
            - ``.settext()``: The ``display.settext()`` function.
            - ``.waitevent()``: The ``display.waitevent()`` function.
        """
        return self._display

    @property
    def dmm(self) -> Dmm:
        """Return the ``dmm`` command tree.

        Constants:
            - ``.OFF``: Set the threshold range manually.
            - ``.ON``: Set the threshold range automatically.

        Sub-properties and sub-methods:
            - ``.digitize``: The ``dmm.digitize`` command tree.
            - ``.measure``: The ``dmm.measure`` command tree.
            - ``.reset()``: The ``dmm.reset()`` function.
            - ``.terminals``: The ``dmm.terminals`` attribute.
            - ``.trigger``: The ``dmm.trigger`` command tree.
        """
        return self._dmm

    @property
    def eventlog(self) -> Eventlog:
        """Return the ``eventlog`` command tree.

        Constants:
            - ``.SEV_ALL``: Returns the total number of unread events in the event log.
            - ``.SEV_ERROR``: Returns the number of error events in the event log.
            - ``.SEV_INFO``: Returns the number of information messages in the event log.
            - ``.SEV_WARN``: Returns the number of warnings in the event log.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``eventlog.clear()`` function.
            - ``.getcount()``: The ``eventlog.getcount()`` function.
            - ``.next()``: The ``eventlog.next()`` function.
            - ``.post()``: The ``eventlog.post()`` function.
            - ``.save()``: The ``eventlog.save()`` function.
        """
        return self._eventlog

    @property
    def fan(self) -> Fan:
        """Return the ``fan`` command tree.

        Sub-properties and sub-methods:
            - ``.level``: The ``fan.level`` attribute.
        """
        return self._fan

    @property
    def file(self) -> File:
        """Return the ``file`` command tree.

        Constants:
            - ``.MODE_APPEND``: Append the file.
            - ``.MODE_READ``: Read the file.
            - ``.MODE_WRITE``: Write to the file.
            - ``.READ_ALL``: Return the whole file, starting at the present position; returns nil if
              the present file position is at the end of the file.
            - ``.READ_LINE``: Return the next line; returns nil if the present file position is at
              the end of the file.
            - ``.READ_NUMBER``: Return a string that represents the number found; returns an event
              string if no number was found; returns nil if the current file position is at the end
              of file.

        Sub-properties and sub-methods:
            - ``.close()``: The ``file.close()`` function.
            - ``.flush()``: The ``file.flush()`` function.
            - ``.mkdir()``: The ``file.mkdir()`` function.
            - ``.open()``: The ``file.open()`` function.
            - ``.read()``: The ``file.read()`` function.
            - ``.usbdriveexists()``: The ``file.usbdriveexists()`` function.
            - ``.write()``: The ``file.write()`` function.
        """
        return self._file

    @property
    def format(self) -> Format:
        """Return the ``format`` command tree.

        Constants:
            - ``.ASCII``: Sets the data format for data that is printed using the printnumber() and
              printbuffer() functions to be ASCII format.
            - ``.BIGENDIAN``: Sets the binary byte order for the data that is printed using the
              printnumber() and
              printbuffer() functions to be most significant byte first.
            - ``.LITTLEENDIAN``: Sets the binary byte order for the data that is printed using the
              printnumber() and
              printbuffer() functions to be least significant byte first.
            - ``.REAL32``: Sets the data format for data that is printed using the printnumber() and
              printbuffer() functions to be single-precision IEEE Std 754 binary format.
            - ``.REAL64``: Sets the data format for data that is printed using the printnumber() and
              printbuffer() functions to be double-precision IEEE Std 754 binary format.

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
    def lan(self) -> Lan:
        """Return the ``lan`` command tree.

        Constants:
            - ``.MODE_AUTO``: The instrument automatically assigns LAN settings.
            - ``.MODE_MANUAL``: You specify the LAN settings.
            - ``.OFF``: An open and close on the DST port (5030) closes all open LAN connections.
            - ``.ON``: The DST port needs to be opened, receive the login + <system password>, then
              close the DST port to close all open LAN connections. By turning DST protection ON,
              you are protecting LAN connections from being inadvertently closed by your IT
              department doing a port scan across the corporate network.
            - ``.PROTOCOL_MULTICAST``: Sets the LAN protocol to use for sending trigger messages to
              multicast.
            - ``.PROTOCOL_TCP``: Sets the LAN protocol to use for sending trigger messages to TCP.
            - ``.PROTOCOL_UDP``: Sets the LAN protocol to use for sending trigger messages to UDP.

        Sub-properties and sub-methods:
            - ``.ipconfig()``: The ``lan.ipconfig()`` function.
            - ``.lxidomain``: The ``lan.lxidomain`` attribute.
            - ``.macaddress``: The ``lan.macaddress`` attribute.
        """
        return self._lan

    @property
    def localnode(self) -> Localnode:
        """Return the ``localnode`` command tree.

        Constants:
            - ``.ACCESS_EXCLUSIVE``: Allows access by one remote interface at a time with logins
              required from other interfaces.
            - ``.ACCESS_FULL``: Full access for all users from all interfaces.
            - ``.ACCESS_LOCKOUT``: Allows access by one interface (including the front panel) at a
              time with passwords required on all interfaces.
            - ``.ACCESS_PROTECTED``: Allows access by one remote interface at a time with passwords
              required on all interfaces.
            - ``.DISABLE``: Do not generate prompts in response to command messages.
            - ``.ENABLE``: Generate prompts in response to command messages.

        Sub-properties and sub-methods:
            - ``.access``: The ``localnode.access`` attribute.
            - ``.gettime()``: The ``localnode.gettime()`` function.
            - ``.internaltemp``: The ``localnode.internaltemp`` attribute.
            - ``.linefreq``: The ``localnode.linefreq`` attribute.
            - ``.model``: The ``localnode.model`` attribute.
            - ``.password``: The ``localnode.password`` attribute.
            - ``.prompts``: The ``localnode.prompts`` attribute.
            - ``.prompts4882``: The ``localnode.prompts4882`` attribute.
            - ``.serialno``: The ``localnode.serialno`` attribute.
            - ``.settime()``: The ``localnode.settime()`` function.
            - ``.showevents``: The ``localnode.showevents`` attribute.
            - ``.version``: The ``localnode.version`` attribute.
        """
        return self._localnode

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
    def script(self) -> Script:
        """Return the ``script`` command tree.

        Sub-properties and sub-methods:
            - ``.delete()``: The ``script.delete()`` function.
            - ``.load()``: The ``script.load()`` function.
        """
        return self._script

    @property
    def script_var(self) -> Dict[str, Scriptvar]:
        """Return the ``scriptVar`` command tree.

        Info:
            - ``scriptVar``, the name of the variable that references the script.

        Sub-properties and sub-methods:
            - ``.run()``: The ``scriptVar.run()`` function.
            - ``.save()``: The ``scriptVar.save()`` function.
            - ``.source``: The ``scriptVar.source`` attribute.
        """
        return self._script_var

    @property
    def smu(self) -> Smu:
        """Return the ``smu`` command tree.

        Constants:
            - ``.AUDIBLE_FAIL``: Beeper sound on test failure.
            - ``.AUDIBLE_NONE``: Beeper never sounds.
            - ``.AUDIBLE_PASS``: Beeper sound on test pass.
            - ``.OFF``: Allow the output to be turned on when the interlock is not engaged.
            - ``.ON``: Only allow the output to be turned on if the interlock is engaged.
        """
        return self._smu

    @property
    def status(self) -> Status:
        """Return the ``status`` command tree.

        Sub-properties and sub-methods:
            - ``.clear()``: The ``status.clear()`` function.
            - ``.condition``: The ``status.condition`` attribute.
            - ``.operation``: The ``status.operation`` command tree.
            - ``.preset()``: The ``status.preset()`` function.
            - ``.questionable``: The ``status.questionable`` command tree.
            - ``.request_enable``: The ``status.request_enable`` attribute.
            - ``.standard``: The ``status.standard`` command tree.
        """
        return self._status

    @property
    def timer(self) -> Timer:
        """Return the ``timer`` command tree.

        Sub-properties and sub-methods:
            - ``.cleartime()``: The ``timer.cleartime()`` function.
            - ``.gettime()``: The ``timer.gettime()`` function.
        """
        return self._timer

    @property
    def trigger(self) -> Trigger:
        """Return the ``trigger`` command tree.

        Constants:
            - ``.BLOCK_BRANCH_ALWAYS``: Defines a trigger model block that always goes to a specific
              block.
            - ``.BLOCK_BRANCH_COUNTER``: Defines a trigger model block that branches to a specified
              block a specified number of times.
            - ``.BLOCK_BRANCH_DELTA``: Defines a trigger model block that goes to a specified block
              if the difference of two measurements meets preset criteria.
            - ``.BLOCK_BRANCH_LIMIT_CONSTANT``: Defines a trigger model block that goes to a
              specified block if a measurement meets preset criteria.
            - ``.BLOCK_BRANCH_LIMIT_DYNAMIC``: Defines a trigger model block that goes to a
              specified block in the trigger model if a measurement meets user-defined criteria.
            - ``.BLOCK_BRANCH_ONCE``: Causes the trigger model to branch to a specified building
              block the first time it is encountered in the trigger model.
            - ``.BLOCK_BRANCH_ONCE_EXCLUDED``: Causes the trigger model to go to a specified
              building block every time the trigger model encounters it, except for the first time.
            - ``.BLOCK_BRANCH_ON_EVENT``: Branches to a specified block when a specified trigger
              event occurs.
            - ``.BLOCK_BUFFER_CLEAR``: Defines a trigger model block that clears the reading buffer.
            - ``.BLOCK_CONFIG_NEXT``: Recalls the settings at the next index of a configuration
              list.
            - ``.BLOCK_CONFIG_PREV``: Recalls the settings stored at the previous  index of a
              configuration list.
            - ``.BLOCK_DELAY_CONSTANT``: Adds a constant delay to the execution of a trigger model.
            - ``.BLOCK_DELAY_DYNAMIC``: Adds a user delay to the execution of the trigger model.
            - ``.BLOCK_DIGITAL_IO``: Defines a trigger model block that sets the lines on the
              digital I/O port high or low.
            - ``.BLOCK_LOG_EVENT``: Allows you to log an event in the event log when the trigger
              model is running.
            - ``.BLOCK_MEASURE``: Deprecated; use trigger.BLOCK_MEASURE_DIGITIZE instead.
            - ``.BLOCK_MEASURE_DIGITIZE``: defines a trigger block that makes or digitizes a
              measurement.
            - ``.BLOCK_NOP``: Creates a placeholder that performs no action in the trigger model.
            - ``.BLOCK_NOTIFY``: Defines a trigger-model block that generates a trigger event and
              immediately continues to the next block.
            - ``.BLOCK_RESET_BRANCH_COUNT``: Creates a block in the trigger model that resets a
              branch counter to 0.
            - ``.BLOCK_WAIT``: Defines a trigger model block that waits for an event before allowing
              the trigger model to continue.
            - ``.CLEAR_ENTER``: Clear previously detected trigger events when entering the wait
              block.
            - ``.CLEAR_NEVER``: Immediately act on any previously detected triggers and not clear
              them (default).
            - ``.CONT_AUTO``: Start continuous measurements after boot.
            - ``.CONT_OFF``: Do not start continuous measurements after boot.
            - ``.CONT_RESTART``: Place the instrument into local control and start continuous
              measurements after boot.
            - ``.COUNT_AUTO``: Use most recent count value.
            - ``.COUNT_INFINITE``: Infinite (run continuously until stopped).
            - ``.COUNT_STOP``: Stop infinite to stop the block.
            - ``.EDGE_EITHER``: Sets the selected trigger line to detect either rising-edge or
              falling-edge triggers as input when the line is configured as an input or open drain.
            - ``.EDGE_FALLING``: Sets the selected trigger line to detect falling-edge triggers as
              input when the line is configured as an input or open drain.
            - ``.EDGE_RISING``: Sets the selected trigger line to detect rising-edge triggers as
              input when the line is configured as an input or open drain.
            - ``.EVENT_BLENDERN``: Trigger event blender N (1 to 2), which combines trigger events.
            - ``.EVENT_COMMAND``: A command interface trigger.
            - ``.EVENT_DIGION``: Line edge (either rising, falling, or either based on the
              configuration of the line) detected on digital input line N (1 to 6).
            - ``.EVENT_DISPLAY``: Front-panel TRIGGER key press.
            - ``.EVENT_LANN``: Appropriate LXI trigger packet is received on LAN trigger object N (1
              to 8).
            - ``.EVENT_NONE``: No trigger event.
            - ``.EVENT_NOTIFYN``: Notify trigger block N (1 to 3) generates a trigger event when the
              trigger model executes it.
            - ``.EVENT_TIMER1``: Trigger timer 1 expired.
            - ``.EVENT_TIMER2``: Trigger timer 2 expired.
            - ``.EVENT_TIMER3``: Trigger timer 3 expired.
            - ``.EVENT_TIMER4``: Trigger timer 4 expired.
            - ``.EVENT_TSPLINKN``: Line edge detected on TSP-Link synchronization line N (1 to 3).
            - ``.LIMIT_ABOVE``: The measurement is above the value set by limit B; limit A must be
              set, but is ignored when this type is selected.
            - ``.LIMIT_BELOW``: The measurement is below the value set by limit A; limit B must be
              set, but is ignored when this type is selected.
            - ``.LIMIT_INSIDE``: The measurement is inside the values set by limits A and B; limit A
              must be the low value and Limit B must be the high value.
            - ``.LIMIT_OUTSIDE``: The measurement is outside the values set by limits A and B; limit
              A must be the low value and Limit B must be the high value.
            - ``.LOGIC_NEGATIVE``: Asserts a TTL-low pulse for the output logic of the trigger event
              generator for the specified line.
            - ``.LOGIC_POSITIVE``: Asserts a TTL-high pulse for the output logic of the trigger
              event generator for the specified line.
            - ``.LOG_ERROR1``: Log error event 1 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_ERROR2``: Log error event 2 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_ERROR3``: Log error event 3 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_ERROR4``: Log error event 4 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_INFO1``: Log information event 1 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_INFO2``: Log information event 2 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_INFO3``: Log information event 3 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_INFO4``: Log information event 4 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_WARN1``: Log warning event 1 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_WARN2``: Log warning event 2 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_WARN3``: Log warning event 3 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_WARN4``: Log warning event 4 in the event log when trigger model execution
              reaches this block.
            - ``.LOG_WARN_ABORT``: Abort the trigger model immediately and post a warning event log
              message.
            - ``.OFF``: Disable the trigger timer.
            - ``.ON``: Enable the trigger timer.
            - ``.STATE_ABORTED``: The trigger model is stopped.
            - ``.STATE_ABORTING``: The trigger model is stopping.
            - ``.STATE_BUILDING``: Blocks have been added.
            - ``.STATE_EMPTY``: The trigger model is selected, but no blocks are defined.
            - ``.STATE_FAILED``: The trigger model is stopped because of an error.
            - ``.STATE_IDLE``: The trigger model is stopped.
            - ``.STATE_RUNNING``: The trigger model is running.
            - ``.STATE_WAITING``: The trigger model has been in the same wait block for more than
              100 ms.
            - ``.WAIT_AND``: Each event must occur before the trigger model continues.
            - ``.WAIT_OR``: At least one of the events must occur before the trigger model
              continues.

        Sub-properties and sub-methods:
            - ``.blender``: The ``trigger.blender[N]`` command tree.
            - ``.clear()``: The ``trigger.clear()`` function.
            - ``.continuous``: The ``trigger.continuous`` attribute.
            - ``.digin``: The ``trigger.digin[N]`` command tree.
            - ``.digout``: The ``trigger.digout[N]`` command tree.
            - ``.ext``: The ``trigger.ext`` command tree.
            - ``.extin``: The ``trigger.extin`` command tree.
            - ``.extout``: The ``trigger.extout`` command tree.
            - ``.lanin``: The ``trigger.lanin[N]`` command tree.
            - ``.lanout``: The ``trigger.lanout[N]`` command tree.
            - ``.model``: The ``trigger.model`` command tree.
            - ``.timer``: The ``trigger.timer[N]`` command tree.
            - ``.tsplinkin``: The ``trigger.tsplinkin[N]`` command tree.
            - ``.tsplinkout``: The ``trigger.tsplinkout[N]`` command tree.
            - ``.wait()``: The ``trigger.wait()`` function.
        """
        return self._trigger

    @property
    def tsplink(self) -> Tsplink:
        """Return the ``tsplink`` command tree.

        Constants:
            - ``.MODE_DIGITAL_OPEN_DRAIN``: TSP-Link digital open drain line.
            - ``.MODE_SYNCHRONOUS_ACCEPTOR``: TSP-Link trigger synchronous acceptor.
            - ``.MODE_SYNCHRONOUS_MASTER``: TSP-Link trigger synchronous master.
            - ``.MODE_TRIGGER_OPEN_DRAIN``: TSP-Link trigger open drain line.
            - ``.STATE_HIGH``: High state of the synchronization line.
            - ``.STATE_LOW``: Low state of the synchronization line.

        Sub-properties and sub-methods:
            - ``.group``: The ``tsplink.group`` attribute.
            - ``.initialize()``: The ``tsplink.initialize()`` function.
            - ``.line``: The ``tsplink.line[N]`` command tree.
            - ``.master``: The ``tsplink.master`` attribute.
            - ``.node``: The ``tsplink.node`` attribute.
            - ``.readport()``: The ``tsplink.readport()`` function.
            - ``.state``: The ``tsplink.state`` attribute.
            - ``.writeport()``: The ``tsplink.writeport()`` function.
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

    def available(self, functionality: str) -> str:
        """Run the ``available()`` function.

        Description:
            - This function checks for the presence of specific instrument functionality.

        TSP Syntax:
            ```
            - available()
            ```

        Args:
            functionality: The functionality to check for.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print(available({functionality}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``available()`` function."
            raise NoDeviceProvidedError(msg) from error

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


class DMM7510Mixin:
    """A mixin that provides access to the DMM7510 commands and constants.

    Properties:
        - ``.command_argument_constants``: The DMM7510 command argument constants.
        - ``.commands``: The DMM7510 commands.
    """

    @cached_property
    def command_argument_constants(self) -> DMM7510CommandConstants:  # pylint: disable=no-self-use
        """Return the DMM7510 command argument constants.

        This provides access to all the string constants which can be used as arguments for DMM7510
        commands.
        """
        return DMM7510CommandConstants()

    @cached_property
    def commands(self) -> DMM7510Commands:
        """Return the DMM7510 commands.

        This provides access to all the commands for the DMM7510 device. See the documentation of
        each sub-property for more usage information.

        Sub-properties and sub-methods:
            - ``.acal``: The ``acal`` command tree.
            - ``.available()``: The ``available()`` function.
            - ``.beeper``: The ``beeper`` command tree.
            - ``.buffer_var``: The ``bufferVar`` command tree.
            - ``.buffer``: The ``buffer`` command tree.
            - ``.createconfigscript()``: The ``createconfigscript()`` function.
            - ``.dataqueue``: The ``dataqueue`` command tree.
            - ``.delay()``: The ``delay()`` function.
            - ``.digio``: The ``digio`` command tree.
            - ``.display``: The ``display`` command tree.
            - ``.dmm``: The ``dmm`` command tree.
            - ``.eventlog``: The ``eventlog`` command tree.
            - ``.exit()``: The ``exit()`` function.
            - ``.fan``: The ``fan`` command tree.
            - ``.file``: The ``file`` command tree.
            - ``.format``: The ``format`` command tree.
            - ``.fs``: The ``fs`` command tree.
            - ``.gpib``: The ``gpib`` command tree.
            - ``.lan``: The ``lan`` command tree.
            - ``.localnode``: The ``localnode`` command tree.
            - ``.node``: The ``node[N]`` command tree.
            - ``.opc()``: The ``opc()`` function.
            - ``.print()``: The ``print()`` function.
            - ``.printbuffer()``: The ``printbuffer()`` function.
            - ``.printnumber()``: The ``printnumber()`` function.
            - ``.reset()``: The ``reset()`` function.
            - ``.script_var``: The ``scriptVar`` command tree.
            - ``.script``: The ``script`` command tree.
            - ``.smu``: The ``smu`` command tree.
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
        return DMM7510Commands(device)
