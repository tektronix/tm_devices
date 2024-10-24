# ruff: noqa: D402,PLR0913
"""The SMU2450 commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional

from tm_devices.driver_mixins.device_control.tsp_control import TSPControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_6w7311_smu.trigger import Trigger
from .gen_7kqm9p_smu.buffervar import Buffervar
from .gen_7kqm9p_smu.display import Display
from .gen_7kqm9p_smu.tsplink import Tsplink
from .gen_7kqm9p_smu.tspnet import Tspnet
from .gen_60xy3r_smu.buffer import Buffer
from .gen_60xy3r_smu.script import Script
from .gen_60xy3r_smu.smu import Smu
from .gen_60xy3r_smu.upgrade import Upgrade
from .gen_by991s_smudaq.digio import Digio
from .gen_by991s_smudaq.status import Status
from .gen_dawv9y_smudaqdmm.localnode import Localnode
from .gen_dbdq3i_smudaqdmm.beeper import Beeper
from .gen_dbdq3i_smudaqdmm.eventlog import Eventlog
from .gen_dbdq3i_smudaqdmm.file import File
from .gen_dbdq3i_smudaqdmm.format import Format
from .gen_dbdq3i_smudaqdmm.lan import Lan
from .gen_dbdq3i_smudaqdmm.scriptvar import Scriptvar
from .gen_dbdq3i_smudaqdmm.timer import Timer
from .gen_e7aqno_smudaqss.node import NodeItem
from .gen_eat5s3_smudaqdmmss.dataqueue import Dataqueue
from .gen_eat5s3_smudaqdmmss.fs import Fs
from .gen_eat5s3_smudaqdmmss.userstring import Userstring
from .gen_eg5ll2_smudaqdmmss.gpib import Gpib
from .helpers import DefaultDictPassKeyToFactory, NoDeviceProvidedError


# pylint: disable=too-few-public-methods
class SMU2450CommandConstants:
    """The SMU2450 command argument constants.

    This provides access to all the string constants which can be used as arguments for SMU2450
    commands.
    """

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
    BUFFER_STAT_LIMIT = "buffer.STAT_LIMIT"
    BUFFER_STAT_LIMIT1_HIGH = "buffer.STAT_LIMIT1_HIGH"
    BUFFER_STAT_LIMIT1_LOW = "buffer.STAT_LIMIT1_LOW"
    BUFFER_STAT_LIMIT2_HIGH = "buffer.STAT_LIMIT2_HIGH"
    BUFFER_STAT_LIMIT2_LOW = "buffer.STAT_LIMIT2_LOW"
    BUFFER_STAT_ORIGIN = "buffer.STAT_ORIGIN"
    BUFFER_STAT_OUTPUT = "buffer.STAT_OUTPUT"
    BUFFER_STAT_OVER_TEMP = "buffer.STAT_OVER_TEMP"
    BUFFER_STAT_PROTECTION = "buffer.STAT_PROTECTION"
    BUFFER_STAT_QUESTIONABLE = "buffer.STAT_QUESTIONABLE"
    BUFFER_STAT_READBACK = "buffer.STAT_READBACK"
    BUFFER_STAT_REL = "buffer.STAT_REL"
    BUFFER_STAT_SCAN = "buffer.STAT_SCAN"
    BUFFER_STAT_SENSE = "buffer.STAT_SENSE"
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
    DISPLAY_SCREEN_SOURCE_SWIPE = "display.SCREEN_SOURCE_SWIPE"
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
    DISPLAY_TEXT1 = "display.TEXT1"
    DISPLAY_TEXT2 = "display.TEXT2"
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
    SMU_ATTR_MEAS_AUTO_ZERO = "smu.ATTR_MEAS_AUTO_ZERO"
    SMU_ATTR_MEAS_COUNT = "smu.ATTR_MEAS_COUNT"
    SMU_ATTR_MEAS_DIGITS = "smu.ATTR_MEAS_DIGITS"
    SMU_ATTR_MEAS_FILTER_COUNT = "smu.ATTR_MEAS_FILTER_COUNT"
    SMU_ATTR_MEAS_FILTER_ENABLE = "smu.ATTR_MEAS_FILTER_ENABLE"
    SMU_ATTR_MEAS_FILTER_TYPE = "smu.ATTR_MEAS_FILTER_TYPE"
    SMU_ATTR_MEAS_LIMIT_AUDIBLE_1 = "smu.ATTR_MEAS_LIMIT_AUDIBLE_1"
    SMU_ATTR_MEAS_LIMIT_AUDIBLE_2 = "smu.ATTR_MEAS_LIMIT_AUDIBLE_2"
    SMU_ATTR_MEAS_LIMIT_AUTO_CLEAR_1 = "smu.ATTR_MEAS_LIMIT_AUTO_CLEAR_1"
    SMU_ATTR_MEAS_LIMIT_AUTO_CLEAR_2 = "smu.ATTR_MEAS_LIMIT_AUTO_CLEAR_2"
    SMU_ATTR_MEAS_LIMIT_ENABLE_1 = "smu.ATTR_MEAS_LIMIT_ENABLE_1"
    SMU_ATTR_MEAS_LIMIT_ENABLE_2 = "smu.ATTR_MEAS_LIMIT_ENABLE_2"
    SMU_ATTR_MEAS_LIMIT_FAIL_1 = "smu.ATTR_MEAS_LIMIT_FAIL_1"
    SMU_ATTR_MEAS_LIMIT_FAIL_2 = "smu.ATTR_MEAS_LIMIT_FAIL_2"
    SMU_ATTR_MEAS_LIMIT_HIGH_1 = "smu.ATTR_MEAS_LIMIT_HIGH_1"
    SMU_ATTR_MEAS_LIMIT_HIGH_2 = "smu.ATTR_MEAS_LIMIT_HIGH_2"
    SMU_ATTR_MEAS_LIMIT_LOW_1 = "smu.ATTR_MEAS_LIMIT_LOW_1"
    SMU_ATTR_MEAS_LIMIT_LOW_2 = "smu.ATTR_MEAS_LIMIT_LOW_2"
    SMU_ATTR_MEAS_MATH_ENABLE = "smu.ATTR_MEAS_MATH_ENABLE"
    SMU_ATTR_MEAS_MATH_FORMAT = "smu.ATTR_MEAS_MATH_FORMAT"
    SMU_ATTR_MEAS_MATH_MXB_BF = "smu.ATTR_MEAS_MATH_MXB_BF"
    SMU_ATTR_MEAS_MATH_MXB_MF = "smu.ATTR_MEAS_MATH_MXB_MF"
    SMU_ATTR_MEAS_MATH_PERCENT = "smu.ATTR_MEAS_MATH_PERCENT"
    SMU_ATTR_MEAS_NPLC = "smu.ATTR_MEAS_NPLC"
    SMU_ATTR_MEAS_OFFSET_COMP = "smu.ATTR_MEAS_OFFSET_COMP"
    SMU_ATTR_MEAS_RANGE = "smu.ATTR_MEAS_RANGE"
    SMU_ATTR_MEAS_RANGE_AUTO = "smu.ATTR_MEAS_RANGE_AUTO"
    SMU_ATTR_MEAS_RANGE_HIGH = "smu.ATTR_MEAS_RANGE_HIGH"
    SMU_ATTR_MEAS_RANGE_LOW = "smu.ATTR_MEAS_RANGE_LOW"
    SMU_ATTR_MEAS_RANGE_REBOUND = "smu.ATTR_MEAS_RANGE_REBOUND"
    SMU_ATTR_MEAS_REL_ENABLE = "smu.ATTR_MEAS_REL_ENABLE"
    SMU_ATTR_MEAS_REL_LEVEL = "smu.ATTR_MEAS_REL_LEVEL"
    SMU_ATTR_MEAS_SENSE = "smu.ATTR_MEAS_SENSE"
    SMU_ATTR_MEAS_UNIT = "smu.ATTR_MEAS_UNIT"
    SMU_ATTR_MEAS_USER_DELAY_N = "smu.ATTR_MEAS_USER_DELAY_N"
    SMU_ATTR_SRC_DELAY = "smu.ATTR_SRC_DELAY"
    SMU_ATTR_SRC_DELAY_AUTO = "smu.ATTR_SRC_DELAY_AUTO"
    SMU_ATTR_SRC_FUNCTION = "smu.ATTR_SRC_FUNCTION"
    SMU_ATTR_SRC_HIGHC = "smu.ATTR_SRC_HIGHC"
    SMU_ATTR_SRC_LEVEL = "smu.ATTR_SRC_LEVEL"
    SMU_ATTR_SRC_LIMIT_LEVEL = "smu.ATTR_SRC_LIMIT_LEVEL"
    SMU_ATTR_SRC_LIMIT_TRIPPED = "smu.ATTR_SRC_LIMIT_TRIPPED"
    SMU_ATTR_SRC_OFFMODE = "smu.ATTR_SRC_OFFMODE"
    SMU_ATTR_SRC_PROTECT_LEVEL = "smu.ATTR_SRC_PROTECT_LEVEL"
    SMU_ATTR_SRC_PROTECT_TRIPPED = "smu.ATTR_SRC_PROTECT_TRIPPED"
    SMU_ATTR_SRC_RANGE = "smu.ATTR_SRC_RANGE"
    SMU_ATTR_SRC_RANGE_AUTO = "smu.ATTR_SRC_RANGE_AUTO"
    SMU_ATTR_SRC_READBACK = "smu.ATTR_SRC_READBACK"
    SMU_ATTR_SRC_USER_DELAY_N = "smu.ATTR_SRC_USER_DELAY_N"
    SMU_AUDIBLE_FAIL = "smu.AUDIBLE_FAIL"
    SMU_AUDIBLE_NONE = "smu.AUDIBLE_NONE"
    SMU_AUDIBLE_PASS = "smu.AUDIBLE_PASS"
    SMU_DELAY_AUTO = "smu.DELAY_AUTO"
    SMU_DIGITS_3_5 = "smu.DIGITS_3_5"
    SMU_DIGITS_4_5 = "smu.DIGITS_4_5"
    SMU_DIGITS_5_5 = "smu.DIGITS_5_5"
    SMU_DIGITS_6_5 = "smu.DIGITS_6_5"
    SMU_FAIL_BOTH = "smu.FAIL_BOTH"
    SMU_FAIL_HIGH = "smu.FAIL_HIGH"
    SMU_FAIL_LOW = "smu.FAIL_LOW"
    SMU_FAIL_NONE = "smu.FAIL_NONE"
    SMU_FILTER_MOVING_AVG = "smu.FILTER_MOVING_AVG"
    SMU_FILTER_REPEAT_AVG = "smu.FILTER_REPEAT_AVG"
    SMU_FUNC_DC_CURRENT = "smu.FUNC_DC_CURRENT"
    SMU_FUNC_DC_VOLTAGE = "smu.FUNC_DC_VOLTAGE"
    SMU_FUNC_RESISTANCE = "smu.FUNC_RESISTANCE"
    SMU_INFINITE = "smu.INFINITE"
    SMU_MATH_MXB = "smu.MATH_MXB"
    SMU_MATH_PERCENT = "smu.MATH_PERCENT"
    SMU_MATH_RECIPROCAL = "smu.MATH_RECIPROCAL"
    SMU_OFF = "smu.OFF"
    SMU_OFFMODE_GUARD = "smu.OFFMODE_GUARD"
    SMU_OFFMODE_HIGHZ = "smu.OFFMODE_HIGHZ"
    SMU_OFFMODE_NORMAL = "smu.OFFMODE_NORMAL"
    SMU_OFFMODE_ZERO = "smu.OFFMODE_ZERO"
    SMU_ON = "smu.ON"
    SMU_PROTECT_100V = "smu.PROTECT_100V"
    SMU_PROTECT_10V = "smu.PROTECT_10V"
    SMU_PROTECT_120V = "smu.PROTECT_120V"
    SMU_PROTECT_140V = "smu.PROTECT_140V"
    SMU_PROTECT_160V = "smu.PROTECT_160V"
    SMU_PROTECT_180V = "smu.PROTECT_180V"
    SMU_PROTECT_20V = "smu.PROTECT_20V"
    SMU_PROTECT_2V = "smu.PROTECT_2V"
    SMU_PROTECT_40V = "smu.PROTECT_40V"
    SMU_PROTECT_5V = "smu.PROTECT_5V"
    SMU_PROTECT_60V = "smu.PROTECT_60V"
    SMU_PROTECT_80V = "smu.PROTECT_80V"
    SMU_PROTECT_NONE = "smu.PROTECT_NONE"
    SMU_RANGE_AUTO = "smu.RANGE_AUTO"
    SMU_RANGE_BEST = "smu.RANGE_BEST"
    SMU_RANGE_FIXED = "smu.RANGE_FIXED"
    SMU_SENSE_2WIRE = "smu.SENSE_2WIRE"
    SMU_SENSE_4WIRE = "smu.SENSE_4WIRE"
    SMU_TERMINALS_FRONT = "smu.TERMINALS_FRONT"
    SMU_TERMINALS_REAR = "smu.TERMINALS_REAR"
    SMU_UNIT_AMP = "smu.UNIT_AMP"
    SMU_UNIT_OHM = "smu.UNIT_OHM"
    SMU_UNIT_VOLT = "smu.UNIT_VOLT"
    SMU_UNIT_WATT = "smu.UNIT_WATT"
    STATUS_EAV = "status.EAV"
    STATUS_ESB = "status.ESB"
    STATUS_MAV = "status.MAV"
    STATUS_MSB = "status.MSB"
    STATUS_MSS = "status.MSS"
    STATUS_OSB = "status.OSB"
    STATUS_QSB = "status.QSB"
    STATUS_STANDARD_OPC = "status.standard.OPC"
    STATUS_STANDARD_PON = "status.standard.PON"
    STATUS_STANDARD_QYE = "status.standard.QYE"
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
    TRIGGER_BLOCK_CONFIG_RECALL = "trigger.BLOCK_CONFIG_RECALL"
    TRIGGER_BLOCK_DELAY_CONSTANT = "trigger.BLOCK_DELAY_CONSTANT"
    TRIGGER_BLOCK_DELAY_DYNAMIC = "trigger.BLOCK_DELAY_DYNAMIC"
    TRIGGER_BLOCK_DIGITAL_IO = "trigger.BLOCK_DIGITAL_IO"
    TRIGGER_BLOCK_LOG_EVENT = "trigger.BLOCK_LOG_EVENT"
    TRIGGER_BLOCK_MEASURE = "trigger.BLOCK_MEASURE"
    TRIGGER_BLOCK_MEASURE_DIGITIZE = "trigger.BLOCK_MEASURE_DIGITIZE"
    TRIGGER_BLOCK_NOP = "trigger.BLOCK_NOP"
    TRIGGER_BLOCK_NOTIFY = "trigger.BLOCK_NOTIFY"
    TRIGGER_BLOCK_RESET_BRANCH_COUNT = "trigger.BLOCK_RESET_BRANCH_COUNT"
    TRIGGER_BLOCK_SOURCE_OUTPUT = "trigger.BLOCK_SOURCE_OUTPUT"
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
    TRIGGER_EVENT_BLENDER1 = "trigger.EVENT_BLENDER1"
    TRIGGER_EVENT_BLENDER2 = "trigger.EVENT_BLENDER2"
    TRIGGER_EVENT_COMMAND = "trigger.EVENT_COMMAND"
    TRIGGER_EVENT_DIGIO1 = "trigger.EVENT_DIGIO1"
    TRIGGER_EVENT_DIGIO2 = "trigger.EVENT_DIGIO2"
    TRIGGER_EVENT_DIGIO3 = "trigger.EVENT_DIGIO3"
    TRIGGER_EVENT_DIGIO4 = "trigger.EVENT_DIGIO4"
    TRIGGER_EVENT_DIGIO5 = "trigger.EVENT_DIGIO5"
    TRIGGER_EVENT_DIGIO6 = "trigger.EVENT_DIGIO6"
    TRIGGER_EVENT_DIGION = "trigger.EVENT_DIGION"
    TRIGGER_EVENT_DISPLAY = "trigger.EVENT_DISPLAY"
    TRIGGER_EVENT_LANN = "trigger.EVENT_LANN"
    TRIGGER_EVENT_NONE = "trigger.EVENT_NONE"
    TRIGGER_EVENT_NOTIFY1 = "trigger.EVENT_NOTIFY1"
    TRIGGER_EVENT_NOTIFY2 = "trigger.EVENT_NOTIFY2"
    TRIGGER_EVENT_NOTIFY3 = "trigger.EVENT_NOTIFY3"
    TRIGGER_EVENT_NOTIFY4 = "trigger.EVENT_NOTIFY4"
    TRIGGER_EVENT_NOTIFY5 = "trigger.EVENT_NOTIFY5"
    TRIGGER_EVENT_NOTIFY6 = "trigger.EVENT_NOTIFY6"
    TRIGGER_EVENT_NOTIFY7 = "trigger.EVENT_NOTIFY7"
    TRIGGER_EVENT_NOTIFY8 = "trigger.EVENT_NOTIFY8"
    TRIGGER_EVENT_NOTIFYN = "trigger.EVENT_NOTIFYN"
    TRIGGER_EVENT_SOURCE_LIMIT = "trigger.EVENT_SOURCE_LIMIT"
    TRIGGER_EVENT_TIMER1 = "trigger.EVENT_TIMER1"
    TRIGGER_EVENT_TIMER2 = "trigger.EVENT_TIMER2"
    TRIGGER_EVENT_TIMER3 = "trigger.EVENT_TIMER3"
    TRIGGER_EVENT_TIMER4 = "trigger.EVENT_TIMER4"
    TRIGGER_EVENT_TSPLINK1 = "trigger.EVENT_TSPLINK1"
    TRIGGER_EVENT_TSPLINK2 = "trigger.EVENT_TSPLINK2"
    TRIGGER_EVENT_TSPLINK3 = "trigger.EVENT_TSPLINK3"
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
    TRIGGER_USER_DELAY_M1 = "trigger.USER_DELAY_M1"
    TRIGGER_USER_DELAY_M2 = "trigger.USER_DELAY_M2"
    TRIGGER_USER_DELAY_M3 = "trigger.USER_DELAY_M3"
    TRIGGER_USER_DELAY_M4 = "trigger.USER_DELAY_M4"
    TRIGGER_USER_DELAY_M5 = "trigger.USER_DELAY_M5"
    TRIGGER_USER_DELAY_S1 = "trigger.USER_DELAY_S1"
    TRIGGER_USER_DELAY_S2 = "trigger.USER_DELAY_S2"
    TRIGGER_USER_DELAY_S3 = "trigger.USER_DELAY_S3"
    TRIGGER_USER_DELAY_S4 = "trigger.USER_DELAY_S4"
    TRIGGER_USER_DELAY_S5 = "trigger.USER_DELAY_S5"
    TRIGGER_WAIT_AND = "trigger.WAIT_AND"
    TRIGGER_WAIT_OR = "trigger.WAIT_OR"
    TSPLINK_MODE_DIGITAL_OPEN_DRAIN = "tsplink.MODE_DIGITAL_OPEN_DRAIN"
    TSPLINK_MODE_SYNCHRONOUS_ACCEPTOR = "tsplink.MODE_SYNCHRONOUS_ACCEPTOR"
    TSPLINK_MODE_SYNCHRONOUS_MASTER = "tsplink.MODE_SYNCHRONOUS_MASTER"
    TSPLINK_MODE_TRIGGER_OPEN_DRAIN = "tsplink.MODE_TRIGGER_OPEN_DRAIN"
    TSPLINK_STATE_HIGH = "tsplink.STATE_HIGH"
    TSPLINK_STATE_LOW = "tsplink.STATE_LOW"
    TSPNET_TERM_CR = "tspnet.TERM_CR"
    TSPNET_TERM_CRLF = "tspnet.TERM_CRLF"
    TSPNET_TERM_LF = "tspnet.TERM_LF"
    TSPNET_TERM_LFCR = "tspnet.TERM_LFCR"


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class SMU2450Commands:
    """The SMU2450 commands.

    This provides access to all the commands for the SMU2450 device. See the documentation of each
    property for more usage information.

    Properties and methods:
        - ``.available()``: The ``available()`` function.
        - ``.beeper``: The ``beeper`` command tree.
        - ``.buffer_var``: The ``bufferVar`` command tree.
        - ``.buffer``: The ``buffer`` command tree.
        - ``.createconfigscript()``: The ``createconfigscript()`` function.
        - ``.dataqueue``: The ``dataqueue`` command tree.
        - ``.delay()``: The ``delay()`` function.
        - ``.digio``: The ``digio`` command tree.
        - ``.display``: The ``display`` command tree.
        - ``.eventlog``: The ``eventlog`` command tree.
        - ``.exit()``: The ``exit()`` function.
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
        self._beeper = Beeper(device)
        self._buffer = Buffer(device)
        self._buffer_var: Dict[str, Buffervar] = DefaultDictPassKeyToFactory(
            lambda x: Buffervar(device, str(x))
        )
        self._dataqueue = Dataqueue(device)
        self._digio = Digio(device)
        self._display = Display(device)
        self._eventlog = Eventlog(device)
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
            - ``.STAT_LIMIT``: Source function level was limited.
            - ``.STAT_LIMIT1_HIGH``: Reading is above high limit 1.
            - ``.STAT_LIMIT1_LOW``: Reading is below low limit 1.
            - ``.STAT_LIMIT2_HIGH``: Reading is above high limit 2.
            - ``.STAT_LIMIT2_LOW``: Reading is below low limit 2.
            - ``.STAT_ORIGIN``: A/D converter from which reading originated; for most instruments,
              this will always be 0 (main). For digitizing instruments, can be 2 (digitize).
            - ``.STAT_OUTPUT``: Output was on.
            - ``.STAT_OVER_TEMP``: Overtemperature condition was active.
            - ``.STAT_PROTECTION``: Overvoltage protection was active.
            - ``.STAT_QUESTIONABLE``: Measure status questionable.
            - ``.STAT_READBACK``: Measured source value was read.
            - ``.STAT_REL``: Relative offset.
            - ``.STAT_SCAN``: Scan.
            - ``.STAT_SENSE``: Four-wire sense was used.
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
            - ``.getstats()``: The ``buffer.getstats()`` function.
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
            - ``.sourceformattedvalues``: The ``bufferVar.sourceformattedvalues[N]`` attribute.
            - ``.sourcestatuses``: The ``bufferVar.sourcestatuses[N]`` attribute.
            - ``.sourceunits``: The ``bufferVar.sourceunits[N]`` attribute.
            - ``.sourcevalues``: The ``bufferVar.sourcevalues[N]`` attribute.
            - ``.startindex``: The ``bufferVar.startindex`` attribute.
            - ``.statuses``: The ``bufferVar.statuses[N]`` attribute.
            - ``.times``: The ``bufferVar.times[N]`` attribute.
            - ``.timestamps``: The ``bufferVar.timestamps[N]`` attribute.
            - ``.units``: The ``bufferVar.units[N]`` attribute.
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
            - ``.SCREEN_SOURCE_SWIPE``: Display SOURCE swipe screen.
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
            - ``.TEXT1``: display text line for Line 1.
            - ``.TEXT2``: display text line for Line 2.

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
            - ``.ATTR_MEAS_AUTO_ZERO``: Autozero enable.
            - ``.ATTR_MEAS_COUNT``: Set the measure count.
            - ``.ATTR_MEAS_DIGITS``: Display digits.
            - ``.ATTR_MEAS_FILTER_COUNT``: Set filter count.
            - ``.ATTR_MEAS_FILTER_ENABLE``: Enable or disable filter.
            - ``.ATTR_MEAS_FILTER_TYPE``: Set filter type.
            - ``.ATTR_MEAS_LIMIT_AUDIBLE_1``: Set limit 1 audible.
            - ``.ATTR_MEAS_LIMIT_AUDIBLE_2``: Set limit 2 audible.
            - ``.ATTR_MEAS_LIMIT_AUTO_CLEAR_1``: Enable or disable limit 1 autoclear.
            - ``.ATTR_MEAS_LIMIT_AUTO_CLEAR_2``: Enable or disable limit 2 autoclear.
            - ``.ATTR_MEAS_LIMIT_ENABLE_1``: Enable or disable limit 1.
            - ``.ATTR_MEAS_LIMIT_ENABLE_2``: Limit 2 enable.
            - ``.ATTR_MEAS_LIMIT_FAIL_1``: Limit 1 fail.
            - ``.ATTR_MEAS_LIMIT_FAIL_2``: Limit 2 fail.
            - ``.ATTR_MEAS_LIMIT_HIGH_1``: Set limit 1 high value.
            - ``.ATTR_MEAS_LIMIT_HIGH_2``: Set limit 2 high value.
            - ``.ATTR_MEAS_LIMIT_LOW_1``: Set limit 1 low value.
            - ``.ATTR_MEAS_LIMIT_LOW_2``: Set limit 2 low value.
            - ``.ATTR_MEAS_MATH_ENABLE``: Enable or disable math.
            - ``.ATTR_MEAS_MATH_FORMAT``: Select the math format.
            - ``.ATTR_MEAS_MATH_MXB_BF``: Set the mxb b (offset) value.
            - ``.ATTR_MEAS_MATH_MXB_MF``: Set the mxb m (scalar) value.
            - ``.ATTR_MEAS_MATH_PERCENT``: Set the percent match function.
            - ``.ATTR_MEAS_NPLC``: NPLC.
            - ``.ATTR_MEAS_OFFSET_COMP``: Offset compensation.
            - ``.ATTR_MEAS_RANGE``: Range.
            - ``.ATTR_MEAS_RANGE_AUTO``: Set up autorange.
            - ``.ATTR_MEAS_RANGE_HIGH``: Set up autorange high limit.
            - ``.ATTR_MEAS_RANGE_LOW``: Set up autorange low limit.
            - ``.ATTR_MEAS_RANGE_REBOUND``: Set autorange rebound.
            - ``.ATTR_MEAS_REL_ENABLE``: Relative offset enable.
            - ``.ATTR_MEAS_REL_LEVEL``: Relative offset level.
            - ``.ATTR_MEAS_SENSE``: Sense (2-wire or 4-wire).
            - ``.ATTR_MEAS_UNIT``: Measurement unit.
            - ``.ATTR_MEAS_USER_DELAY_N``: Set user delay, where N is 1 to 5.
            - ``.ATTR_SRC_DELAY``: Delay in addition to normal settling times after turning on the
              source.
            - ``.ATTR_SRC_DELAY_AUTO``: Set autodelay.
            - ``.ATTR_SRC_FUNCTION``: Set the function.
            - ``.ATTR_SRC_HIGHC``: Set high capacitance.
            - ``.ATTR_SRC_LEVEL``: Set level.
            - ``.ATTR_SRC_LIMIT_LEVEL``: Set limit level.
            - ``.ATTR_SRC_LIMIT_TRIPPED``: Source limit exceeded.
            - ``.ATTR_SRC_OFFMODE``: Set output off mode.
            - ``.ATTR_SRC_PROTECT_LEVEL``: Set overvoltage protection limit.
            - ``.ATTR_SRC_PROTECT_TRIPPED``: The overvoltage protection limit is active.
            - ``.ATTR_SRC_RANGE``: Set range.
            - ``.ATTR_SRC_RANGE_AUTO``: Set autorange.
            - ``.ATTR_SRC_READBACK``: Set source readback.
            - ``.ATTR_SRC_USER_DELAY_N``: User delay N, where N is the user delay, 1 to 5.
            - ``.AUDIBLE_FAIL``: Beeper sound on test failure.
            - ``.AUDIBLE_NONE``: Beeper never sounds.
            - ``.AUDIBLE_PASS``: Beeper sound on test pass.
            - ``.DELAY_AUTO``: Delay between measurement points set to autodelay.
            - ``.DIGITS_3_5``: Set display to 3.5 digits.
            - ``.DIGITS_4_5``: Set display to 4.5 digits.
            - ``.DIGITS_5_5``: Set display to 5.5 digits.
            - ``.DIGITS_6_5``: Set display to 6.5 digits.
            - ``.FAIL_BOTH``: Test failed; measurement exceeded both limits.
            - ``.FAIL_HIGH``: Test failed; measurement exceeded high limit.
            - ``.FAIL_LOW``: Test failed; measurement exceeded low limit.
            - ``.FAIL_NONE``: Test passed; measurement under or equal to the high limit.
            - ``.FILTER_MOVING_AVG``: Use the moving average filter for the selected measure
              function when the measurement filter is enabled.
            - ``.FILTER_REPEAT_AVG``: Use the repeatinter average filter for the selected measure
              function when the measurement filter is enabled.
            - ``.FUNC_DC_CURRENT``: Current measurement function.
            - ``.FUNC_DC_VOLTAGE``: Voltage measurement function.
            - ``.FUNC_RESISTANCE``: Resistance measurement function.
            - ``.INFINITE``: Set count to infinite.
            - ``.MATH_MXB``: Perform y = mx+b operation on measurement.
            - ``.MATH_PERCENT``: Perform percent operation on measurements.
            - ``.MATH_RECIPROCAL``: Perform reciprocal math operation on measurements.
            - ``.OFF``: Allow the output to be turned on when the interlock is not engaged.
            - ``.OFFMODE_GUARD``: Set the state when the output is turned off to guard.
            - ``.OFFMODE_HIGHZ``: Set the state when the output is turned off to  high impedance.
            - ``.OFFMODE_NORMAL``: Set the state when the output is turned off to normal.
            - ``.OFFMODE_ZERO``: Set the state when the output is turned off to zero.
            - ``.ON``: Only allow the output to be turned on if the interlock is engaged.
            - ``.PROTECT_100V``: The overvoltage protection value.
            - ``.PROTECT_10V``: The overvoltage protection value.
            - ``.PROTECT_120V``: The overvoltage protection value.
            - ``.PROTECT_140V``: The overvoltage protection value.
            - ``.PROTECT_160V``: The overvoltage protection value.
            - ``.PROTECT_180V``: The overvoltage protection value.
            - ``.PROTECT_20V``: The overvoltage protection value.
            - ``.PROTECT_2V``: The overvoltage protection value.
            - ``.PROTECT_40V``: The overvoltage protection value.
            - ``.PROTECT_5V``: The overvoltage protection value.
            - ``.PROTECT_60V``: The overvoltage protection value.
            - ``.PROTECT_80V``: The overvoltage protection value.
            - ``.PROTECT_NONE``: The overvoltage protection value.
            - ``.RANGE_AUTO``: Most sensitive source range for each source level in the sweep.
            - ``.RANGE_BEST``: Best fixed range.
            - ``.RANGE_FIXED``: Present source range for the entire sweep.
            - ``.SENSE_2WIRE``: Use two-wire sensing.
            - ``.SENSE_4WIRE``: Use four-wire sensing.
            - ``.TERMINALS_FRONT``: Use the front-panel input and output terminals.
            - ``.TERMINALS_REAR``: Use the rear-panel input and output terminals.
            - ``.UNIT_AMP``: Set unit of measure to amps (only available for current measurements).
            - ``.UNIT_OHM``: Set unit of measure to ohms (available for voltage, current, or
              resistance measurements).
            - ``.UNIT_VOLT``: Set unit of measure to volts (only available for voltage
              measurements).
            - ``.UNIT_WATT``: Set unit of measure to power (only available for voltage or current
              measurements).

        Sub-properties and sub-methods:
            - ``.interlock``: The ``smu.interlock`` command tree.
            - ``.measure``: The ``smu.measure`` command tree.
            - ``.reset()``: The ``smu.reset()`` function.
            - ``.source``: The ``smu.source`` command tree.
            - ``.terminals``: The ``smu.terminals`` attribute.
        """
        return self._smu

    @property
    def status(self) -> Status:
        """Return the ``status`` command tree.

        Constants:
            - ``.EAV``: B2. Set summary bit indicates that an error or status message is present in
              the Error Queue.
            - ``.ESB``: B5. Set summary bit indicates that an enabled standard event has occurred.
            - ``.MAV``: B4. Set summary bit indicates that a response message is present in the
              Output Queue.
            - ``.MSB``: B0. Set summary bit indicates that an enabled measurement event has
              occurred.
            - ``.MSS``: An enabled summary bit of the status byte register is set.
            - ``.OSB``: B7. Set summary bit indicates that an enabled operation event has occurred.
            - ``.QSB``: B3. Set summary bit indicates that an enabled questionable event has
              occurred.

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
            - ``.BLOCK_CONFIG_RECALL``: Recalls the system settings that are stored in a source or
              measure configuration list, or both a source and measure configuration list.
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
            - ``.BLOCK_SOURCE_OUTPUT``: Defines a trigger block that turns the output source on or
              off.
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
            - ``.EVENT_BLENDER1``: Trigger event blender1, which combines trigger events.
            - ``.EVENT_BLENDER2``: Trigger event blender2, which combines trigger events.
            - ``.EVENT_COMMAND``: A command interface trigger.
            - ``.EVENT_DIGIO1``: Digital input line edge (either rising, falling, or either based on
              the configuration of the line) detected on digital input line 1.
            - ``.EVENT_DIGIO2``: Digital input line edge (either rising, falling, or either based on
              the configuration of the line) detected on digital input line 2.
            - ``.EVENT_DIGIO3``: Digital input line edge (either rising, falling, or either based on
              the configuration of the line) detected on digital input line 3.
            - ``.EVENT_DIGIO4``: Digital input line edge (either rising, falling, or either based on
              the configuration of the line) detected on digital input line 4.
            - ``.EVENT_DIGIO5``: Digital input line edge (either rising, falling, or either based on
              the configuration of the line) detected on digital input line 5.
            - ``.EVENT_DIGIO6``: Digital input line edge (either rising, falling, or either based on
              the configuration of the line) detected on digital input line 6.
            - ``.EVENT_DIGION``: Line edge (either rising, falling, or either based on the
              configuration of the line) detected on digital input line N (1 to 6).
            - ``.EVENT_DISPLAY``: Front-panel TRIGGER key press.
            - ``.EVENT_LANN``: Appropriate LXI trigger packet is received on LAN trigger object N (1
              to 8).
            - ``.EVENT_NONE``: No trigger event.
            - ``.EVENT_NOTIFY1``: Notify trigger block1  generates a trigger event when the trigger
              model executes it.
            - ``.EVENT_NOTIFY2``: Notify trigger block2  generates a trigger event when the trigger
              model executes it.
            - ``.EVENT_NOTIFY3``: Notify trigger block3 generates a trigger event when the trigger
              model executes it.
            - ``.EVENT_NOTIFY4``: Notify trigger block4 generates a trigger event when the trigger
              model executes it.
            - ``.EVENT_NOTIFY5``: Notify trigger block5 generates a trigger event when the trigger
              model executes it.
            - ``.EVENT_NOTIFY6``: Notify trigger block6 generates a trigger event when the trigger
              model executes it.
            - ``.EVENT_NOTIFY7``: Notify trigger block7 generates a trigger event when the trigger
              model executes it.
            - ``.EVENT_NOTIFY8``: Notify trigger block8 generates a trigger event when the trigger
              model executes it.
            - ``.EVENT_NOTIFYN``: Notify trigger block N (1 to 3) generates a trigger event when the
              trigger model executes it.
            - ``.EVENT_SOURCE_LIMIT``: Before asserting a trigger on the selected digital output
              line, wait until a source limit condition occurs.
            - ``.EVENT_TIMER1``: Trigger timer 1 expired.
            - ``.EVENT_TIMER2``: Trigger timer 2 expired.
            - ``.EVENT_TIMER3``: Trigger timer 3 expired.
            - ``.EVENT_TIMER4``: Trigger timer 4 expired.
            - ``.EVENT_TSPLINK1``: Line edge detected on TSP-Link synchronization line 1.
            - ``.EVENT_TSPLINK2``: Line edge detected on TSP-Link synchronization line 2.
            - ``.EVENT_TSPLINK3``: Line edge detected on TSP-Link synchronization line 3.
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
            - ``.USER_DELAY_M1``: trigger.USER_DELAY_M1, where the user delay 1 is set by
              smu.measure.userdelay[N].
            - ``.USER_DELAY_M2``: trigger.USER_DELAY_M2, where the user delay 2 is set by
              smu.measure.userdelay[N].
            - ``.USER_DELAY_M3``: trigger.USER_DELAY_M3, where the user delay 3 is set by
              smu.measure.userdelay[N].
            - ``.USER_DELAY_M4``: trigger.USER_DELAY_M4, where the user delay 4 is set by
              smu.measure.userdelay[N].
            - ``.USER_DELAY_M5``: trigger.USER_DELAY_M5, where the user delay 5 is set by
              smu.measure.userdelay[N].
            - ``.USER_DELAY_S1``: Delay 1 is set by smu.source.userdelay[N].
            - ``.USER_DELAY_S2``: Delay 1 is set by smu.source.userdelay[N].
            - ``.USER_DELAY_S3``: Delay 1 is set by smu.source.userdelay[N].
            - ``.USER_DELAY_S4``: Delay 1 is set by smu.source.userdelay[N].
            - ``.USER_DELAY_S5``: Delay 1 is set by smu.source.userdelay[N].
            - ``.WAIT_AND``: Each event must occur before the trigger model continues.
            - ``.WAIT_OR``: At least one of the events must occur before the trigger model
              continues.

        Sub-properties and sub-methods:
            - ``.blender``: The ``trigger.blender[N]`` command tree.
            - ``.clear()``: The ``trigger.clear()`` function.
            - ``.continuous``: The ``trigger.continuous`` attribute.
            - ``.digin``: The ``trigger.digin[N]`` command tree.
            - ``.digout``: The ``trigger.digout[N]`` command tree.
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

        Constants:
            - ``.TERM_CR``: Set the device line termination sequence to CR.
            - ``.TERM_CRLF``: Set the device line termination sequence to CRLF.
            - ``.TERM_LF``: Set the device line termination sequence to LF.
            - ``.TERM_LFCR``: Set the device line termination sequence to LFCR.

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
            script_name: A string that represents the name of the script to be created.

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


class SMU2450Mixin:
    """A mixin that provides access to the SMU2450 commands and constants.

    Properties:
        - ``.command_argument_constants``: The SMU2450 command argument constants.
        - ``.commands``: The SMU2450 commands.
    """

    @cached_property
    def command_argument_constants(self) -> SMU2450CommandConstants:  # pylint: disable=no-self-use
        """Return the SMU2450 command argument constants.

        This provides access to all the string constants which can be used as arguments for SMU2450
        commands.
        """
        return SMU2450CommandConstants()

    @cached_property
    def commands(self) -> SMU2450Commands:
        """Return the SMU2450 commands.

        This provides access to all the commands for the SMU2450 device. See the documentation of
        each sub-property for more usage information.

        Sub-properties and sub-methods:
            - ``.available()``: The ``available()`` function.
            - ``.beeper``: The ``beeper`` command tree.
            - ``.buffer_var``: The ``bufferVar`` command tree.
            - ``.buffer``: The ``buffer`` command tree.
            - ``.createconfigscript()``: The ``createconfigscript()`` function.
            - ``.dataqueue``: The ``dataqueue`` command tree.
            - ``.delay()``: The ``delay()`` function.
            - ``.digio``: The ``digio`` command tree.
            - ``.display``: The ``display`` command tree.
            - ``.eventlog``: The ``eventlog`` command tree.
            - ``.exit()``: The ``exit()`` function.
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
        return SMU2450Commands(device)
