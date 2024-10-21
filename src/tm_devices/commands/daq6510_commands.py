# ruff: noqa: D402,PLR0913
"""The DAQ6510 commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional

from tm_devices.driver_mixins.device_control.tsp_control import TSPControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_by991s_smudaq.digio import Digio
from .gen_by991s_smudaq.status import Status
from .gen_canxny_daq.buffer import Buffer
from .gen_canxny_daq.buffervar import Buffervar
from .gen_canxny_daq.channel import Channel
from .gen_canxny_daq.display import Display
from .gen_canxny_daq.dmm import Dmm
from .gen_canxny_daq.scan import Scan
from .gen_canxny_daq.slot import Slot, SlotItem
from .gen_canxny_daq.trigger import Trigger
from .gen_canxny_daq.tsplink import Tsplink
from .gen_canxny_daq.upgrade import Upgrade
from .gen_dawv9y_smudaqdmm.localnode import Localnode
from .gen_dbdq3i_smudaqdmm.beeper import Beeper
from .gen_dbdq3i_smudaqdmm.eventlog import Eventlog
from .gen_dbdq3i_smudaqdmm.file import File
from .gen_dbdq3i_smudaqdmm.format import Format
from .gen_dbdq3i_smudaqdmm.lan import Lan
from .gen_dbdq3i_smudaqdmm.scriptvar import Scriptvar
from .gen_dbdq3i_smudaqdmm.timer import Timer
from .gen_dcpheg_daqdmm.smu import Smu
from .gen_dd4xnb_smudaqdmm.script import Script
from .gen_e7aqno_smudaqss.node import NodeItem
from .gen_eat5s3_smudaqdmmss.dataqueue import Dataqueue
from .gen_eat5s3_smudaqdmmss.fs import Fs
from .gen_eat5s3_smudaqdmmss.userstring import Userstring
from .gen_ed9nkc_daqss.tspnet import Tspnet
from .gen_eg5ll2_smudaqdmmss.gpib import Gpib
from .helpers import DefaultDictPassKeyToFactory, NoDeviceProvidedError


# pylint: disable=too-few-public-methods
class DAQ6510CommandConstants:
    """The DAQ6510 command argument constants.

    This provides access to all the string constants which can be used as arguments for DAQ6510
    commands.
    """

    BUFFER_COL_ALL = "buffer.COL_ALL"
    BUFFER_COL_BRIEF = "buffer.COL_BRIEF"
    BUFFER_COL_CHANNEL = "buffer.COL_CHANNEL"
    BUFFER_COL_CSV_CHAN_COLS = "buffer.COL_CSV_CHAN_COLS"
    BUFFER_COL_CSV_EASY_GRAPH = "buffer.COL_CSV_EASY_GRAPH"
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
    CHANNEL_COUNT_INTERVAL_10M = "channel.COUNT_INTERVAL_10M"
    CHANNEL_COUNT_INTERVAL_15M = "channel.COUNT_INTERVAL_15M"
    CHANNEL_COUNT_INTERVAL_1M = "channel.COUNT_INTERVAL_1M"
    CHANNEL_COUNT_INTERVAL_24H = "channel.COUNT_INTERVAL_24H"
    CHANNEL_COUNT_INTERVAL_30M = "channel.COUNT_INTERVAL_30M"
    CHANNEL_COUNT_INTERVAL_5M = "channel.COUNT_INTERVAL_5M"
    CHANNEL_COUNT_INTERVAL_60M = "channel.COUNT_INTERVAL_60M"
    CHANNEL_IND_CLOSED = "channel.IND_CLOSED"
    CHANNEL_IND_MATCH = "channel.IND_MATCH"
    CHANNEL_IND_OVERFLOW = "channel.IND_OVERFLOW"
    CHANNEL_MATCH_ANY = "channel.MATCH_ANY"
    CHANNEL_MATCH_EXACT = "channel.MATCH_EXACT"
    CHANNEL_MATCH_NONE = "channel.MATCH_NONE"
    CHANNEL_MATCH_UNCHANGED = "channel.MATCH_UNCHANGED"
    CHANNEL_MODE_FALLING_EDGE = "channel.MODE_FALLING_EDGE"
    CHANNEL_MODE_FALLING_EDGE_READ_RESET = "channel.MODE_FALLING_EDGE_READ_RESET"
    CHANNEL_MODE_INPUT = "channel.MODE_INPUT"
    CHANNEL_MODE_OUTPUT = "channel.MODE_OUTPUT"
    CHANNEL_MODE_RISING_EDGE = "channel.MODE_RISING_EDGE"
    CHANNEL_MODE_RISING_EDGE_READ_RESET = "channel.MODE_RISING_EDGE_READ_RESET"
    CHANNEL_TYPE_BACKPLANE = "channel.TYPE_BACKPLANE"
    CHANNEL_TYPE_DAC = "channel.TYPE_DAC"
    CHANNEL_TYPE_DIGITAL = "channel.TYPE_DIGITAL"
    CHANNEL_TYPE_POLE = "channel.TYPE_POLE"
    CHANNEL_TYPE_RADIO = "channel.TYPE_RADIO"
    CHANNEL_TYPE_SWITCH = "channel.TYPE_SWITCH"
    CHANNEL_TYPE_TOTALIZER = "channel.TYPE_TOTALIZER"
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
    DISPLAY_SCREEN_CHANNEL_CONTROL = "display.SCREEN_CHANNEL_CONTROL"
    DISPLAY_SCREEN_CHANNEL_SCAN = "display.SCREEN_CHANNEL_SCAN"
    DISPLAY_SCREEN_CHANNEL_SETTINGS = "display.SCREEN_CHANNEL_SETTINGS"
    DISPLAY_SCREEN_CHANNEL_SWIPE = "display.SCREEN_CHANNEL_SWIPE"
    DISPLAY_SCREEN_FUNCTIONS_SWIPE = "display.SCREEN_FUNCTIONS_SWIPE"
    DISPLAY_SCREEN_GRAPH = "display.SCREEN_GRAPH"
    DISPLAY_SCREEN_GRAPH_SWIPE = "display.SCREEN_GRAPH_SWIPE"
    DISPLAY_SCREEN_HISTOGRAM = "display.SCREEN_HISTOGRAM"
    DISPLAY_SCREEN_HOME = "display.SCREEN_HOME"
    DISPLAY_SCREEN_HOME_LARGE_READING = "display.SCREEN_HOME_LARGE_READING"
    DISPLAY_SCREEN_NONSWITCH_SWIPE = "display.SCREEN_NONSWITCH_SWIPE"
    DISPLAY_SCREEN_PROCESSING = "display.SCREEN_PROCESSING"
    DISPLAY_SCREEN_READING_TABLE = "display.SCREEN_READING_TABLE"
    DISPLAY_SCREEN_SCAN_SWIPE = "display.SCREEN_SCAN_SWIPE"
    DISPLAY_SCREEN_SECONDARY_SWIPE = "display.SCREEN_SECONDARY_SWIPE"
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
    DMM_APERTURE_AUTO = "dmm.APERTURE_AUTO"
    DMM_ATTR_DIGI_APERTURE = "dmm.ATTR_DIGI_APERTURE"
    DMM_ATTR_DIGI_ATRIG_EDGE_LEVEL = "dmm.ATTR_DIGI_ATRIG_EDGE_LEVEL"
    DMM_ATTR_DIGI_ATRIG_EDGE_SLOPE = "dmm.ATTR_DIGI_ATRIG_EDGE_SLOPE"
    DMM_ATTR_DIGI_ATRIG_MODE = "dmm.ATTR_DIGI_ATRIG_MODE"
    DMM_ATTR_DIGI_ATRIG_WINDOW_DIRECTION = "dmm.ATTR_DIGI_ATRIG_WINDOW_DIRECTION"
    DMM_ATTR_DIGI_ATRIG_WINDOW_LEVEL_HIGH = "dmm.ATTR_DIGI_ATRIG_WINDOW_LEVEL_HIGH"
    DMM_ATTR_DIGI_ATRIG_WINDOW_LEVEL_LOW = "dmm.ATTR_DIGI_ATRIG_WINDOW_LEVEL_LOW"
    DMM_ATTR_DIGI_COUNT = "dmm.ATTR_DIGI_COUNT"
    DMM_ATTR_DIGI_DBM_REFERENCE = "dmm.ATTR_DIGI_DBM_REFERENCE"
    DMM_ATTR_DIGI_DB_REFERENCE = "dmm.ATTR_DIGI_DB_REFERENCE"
    DMM_ATTR_DIGI_DIGITS = "dmm.ATTR_DIGI_DIGITS"
    DMM_ATTR_DIGI_FUNCTION = "dmm.ATTR_DIGI_FUNCTION"
    DMM_ATTR_DIGI_INPUT_IMPEDANCE = "dmm.ATTR_DIGI_INPUT_IMPEDANCE"
    DMM_ATTR_DIGI_LIMIT_AUDIBLE_1 = "dmm.ATTR_DIGI_LIMIT_AUDIBLE_1"
    DMM_ATTR_DIGI_LIMIT_AUDIBLE_2 = "dmm.ATTR_DIGI_LIMIT_AUDIBLE_2"
    DMM_ATTR_DIGI_LIMIT_AUTO_CLEAR_1 = "dmm.ATTR_DIGI_LIMIT_AUTO_CLEAR_1"
    DMM_ATTR_DIGI_LIMIT_AUTO_CLEAR_2 = "dmm.ATTR_DIGI_LIMIT_AUTO_CLEAR_2"
    DMM_ATTR_DIGI_LIMIT_ENABLE_1 = "dmm.ATTR_DIGI_LIMIT_ENABLE_1"
    DMM_ATTR_DIGI_LIMIT_ENABLE_2 = "dmm.ATTR_DIGI_LIMIT_ENABLE_2"
    DMM_ATTR_DIGI_LIMIT_FAIL_1 = "dmm.ATTR_DIGI_LIMIT_FAIL_1"
    DMM_ATTR_DIGI_LIMIT_FAIL_2 = "dmm.ATTR_DIGI_LIMIT_FAIL_2"
    DMM_ATTR_DIGI_LIMIT_HIGH_1 = "dmm.ATTR_DIGI_LIMIT_HIGH_1"
    DMM_ATTR_DIGI_LIMIT_HIGH_2 = "dmm.ATTR_DIGI_LIMIT_HIGH_2"
    DMM_ATTR_DIGI_LIMIT_LOW_1 = "dmm.ATTR_DIGI_LIMIT_LOW_1"
    DMM_ATTR_DIGI_LIMIT_LOW_2 = "dmm.ATTR_DIGI_LIMIT_LOW_2"
    DMM_ATTR_DIGI_MATH_ENABLE = "dmm.ATTR_DIGI_MATH_ENABLE"
    DMM_ATTR_DIGI_MATH_FORMAT = "dmm.ATTR_DIGI_MATH_FORMAT"
    DMM_ATTR_DIGI_MATH_MXB_BF = "dmm.ATTR_DIGI_MATH_MXB_BF"
    DMM_ATTR_DIGI_MATH_MXB_MF = "dmm.ATTR_DIGI_MATH_MXB_MF"
    DMM_ATTR_DIGI_MATH_PERCENT = "dmm.ATTR_DIGI_MATH_PERCENT"
    DMM_ATTR_DIGI_RANGE = "dmm.ATTR_DIGI_RANGE"
    DMM_ATTR_DIGI_REL_ENABLE = "dmm.ATTR_DIGI_REL_ENABLE"
    DMM_ATTR_DIGI_REL_LEVEL = "dmm.ATTR_DIGI_REL_LEVEL"
    DMM_ATTR_DIGI_SAMPLE_RATE = "dmm.ATTR_DIGI_SAMPLE_RATE"
    DMM_ATTR_DIGI_UNIT = "dmm.ATTR_DIGI_UNIT"
    DMM_ATTR_DIGI_USER_DELAY_1 = "dmm.ATTR_DIGI_USER_DELAY_1"
    DMM_ATTR_DIGI_USER_DELAY_2 = "dmm.ATTR_DIGI_USER_DELAY_2"
    DMM_ATTR_DIGI_USER_DELAY_3 = "dmm.ATTR_DIGI_USER_DELAY_3"
    DMM_ATTR_DIGI_USER_DELAY_4 = "dmm.ATTR_DIGI_USER_DELAY_4"
    DMM_ATTR_DIGI_USER_DELAY_5 = "dmm.ATTR_DIGI_USER_DELAY_5"
    DMM_ATTR_DIGI_WINDOW_DIRECTION = "dmm.ATTR_DIGI_WINDOW_DIRECTION"
    DMM_ATTR_DIGI_WINDOW_LEVEL_HIGH = "dmm.ATTR_DIGI_WINDOW_LEVEL_HIGH"
    DMM_ATTR_DIGI_WINDOW_LEVEL_LOW = "dmm.ATTR_DIGI_WINDOW_LEVEL_LOW"
    DMM_ATTR_MEAS_APERTURE = "dmm.ATTR_MEAS_APERTURE"
    DMM_ATTR_MEAS_ATRIG_EDGE_LEVEL = "dmm.ATTR_MEAS_ATRIG_EDGE_LEVEL"
    DMM_ATTR_MEAS_ATRIG_EDGE_SLOPE = "dmm.ATTR_MEAS_ATRIG_EDGE_SLOPE"
    DMM_ATTR_MEAS_ATRIG_MODE = "dmm.ATTR_MEAS_ATRIG_MODE"
    DMM_ATTR_MEAS_ATRIG_WINDOW_DIRECTION = "dmm.ATTR_MEAS_ATRIG_WINDOW_DIRECTION"
    DMM_ATTR_MEAS_ATRIG_WINDOW_LEVEL_HIGH = "dmm.ATTR_MEAS_ATRIG_WINDOW_LEVEL_HIGH"
    DMM_ATTR_MEAS_ATRIG_WINDOW_LEVEL_LOW = "dmm.ATTR_MEAS_ATRIG_WINDOW_LEVEL_LOW"
    DMM_ATTR_MEAS_AUTO_DELAY = "dmm.ATTR_MEAS_AUTO_DELAY"
    DMM_ATTR_MEAS_AUTO_ZERO = "dmm.ATTR_MEAS_AUTO_ZERO"
    DMM_ATTR_MEAS_BIAS_LEVEL = "dmm.ATTR_MEAS_BIAS_LEVEL"
    DMM_ATTR_MEAS_COUNT = "dmm.ATTR_MEAS_COUNT"
    DMM_ATTR_MEAS_DBM_REFERENCE = "dmm.ATTR_MEAS_DBM_REFERENCE"
    DMM_ATTR_MEAS_DB_REFERENCE = "dmm.ATTR_MEAS_DB_REFERENCE"
    DMM_ATTR_MEAS_DETECTBW = "dmm.ATTR_MEAS_DETECTBW"
    DMM_ATTR_MEAS_DIGITS = "dmm.ATTR_MEAS_DIGITS"
    DMM_ATTR_MEAS_FILTER_COUNT = "dmm.ATTR_MEAS_FILTER_COUNT"
    DMM_ATTR_MEAS_FILTER_ENABLE = "dmm.ATTR_MEAS_FILTER_ENABLE"
    DMM_ATTR_MEAS_FILTER_TYPE = "dmm.ATTR_MEAS_FILTER_TYPE"
    DMM_ATTR_MEAS_FILTER_WINDOW = "dmm.ATTR_MEAS_FILTER_WINDOW"
    DMM_ATTR_MEAS_FOUR_RTD = "dmm.ATTR_MEAS_FOUR_RTD"
    DMM_ATTR_MEAS_INPUT_IMPEDANCE = "dmm.ATTR_MEAS_INPUT_IMPEDANCE"
    DMM_ATTR_MEAS_LIMIT_AUDIBLE_1 = "dmm.ATTR_MEAS_LIMIT_AUDIBLE_1"
    DMM_ATTR_MEAS_LIMIT_AUDIBLE_2 = "dmm.ATTR_MEAS_LIMIT_AUDIBLE_2"
    DMM_ATTR_MEAS_LIMIT_AUTO_CLEAR_1 = "dmm.ATTR_MEAS_LIMIT_AUTO_CLEAR_1"
    DMM_ATTR_MEAS_LIMIT_AUTO_CLEAR_2 = "dmm.ATTR_MEAS_LIMIT_AUTO_CLEAR_2"
    DMM_ATTR_MEAS_LIMIT_ENABLE_1 = "dmm.ATTR_MEAS_LIMIT_ENABLE_1"
    DMM_ATTR_MEAS_LIMIT_ENABLE_2 = "dmm.ATTR_MEAS_LIMIT_ENABLE_2"
    DMM_ATTR_MEAS_LIMIT_FAIL_1 = "dmm.ATTR_MEAS_LIMIT_FAIL_1"
    DMM_ATTR_MEAS_LIMIT_FAIL_2 = "dmm.ATTR_MEAS_LIMIT_FAIL_2"
    DMM_ATTR_MEAS_LIMIT_HIGH_1 = "dmm.ATTR_MEAS_LIMIT_HIGH_1"
    DMM_ATTR_MEAS_LIMIT_HIGH_2 = "dmm.ATTR_MEAS_LIMIT_HIGH_2"
    DMM_ATTR_MEAS_LIMIT_LOW_1 = "dmm.ATTR_MEAS_LIMIT_LOW_1"
    DMM_ATTR_MEAS_LIMIT_LOW_2 = "dmm.ATTR_MEAS_LIMIT_LOW_2"
    DMM_ATTR_MEAS_LINE_SYNC = "dmm.ATTR_MEAS_LINE_SYNC"
    DMM_ATTR_MEAS_MATH_ENABLE = "dmm.ATTR_MEAS_MATH_ENABLE"
    DMM_ATTR_MEAS_MATH_FORMAT = "dmm.ATTR_MEAS_MATH_FORMAT"
    DMM_ATTR_MEAS_MATH_MXB_BF = "dmm.ATTR_MEAS_MATH_MXB_BF"
    DMM_ATTR_MEAS_MATH_MXB_MF = "dmm.ATTR_MEAS_MATH_MXB_MF"
    DMM_ATTR_MEAS_MATH_PERCENT = "dmm.ATTR_MEAS_MATH_PERCENT"
    DMM_ATTR_MEAS_NPLC = "dmm.ATTR_MEAS_NPLC"
    DMM_ATTR_MEAS_OFFCOMP_ENABLE = "dmm.ATTR_MEAS_OFFCOMP_ENABLE"
    DMM_ATTR_MEAS_OPEN_DETECTOR = "dmm.ATTR_MEAS_OPEN_DETECTOR"
    DMM_ATTR_MEAS_RANGE = "dmm.ATTR_MEAS_RANGE"
    DMM_ATTR_MEAS_RANGE_AUTO = "dmm.ATTR_MEAS_RANGE_AUTO"
    DMM_ATTR_MEAS_REF_JUNCTION = "dmm.ATTR_MEAS_REF_JUNCTION"
    DMM_ATTR_MEAS_REL_ENABLE = "dmm.ATTR_MEAS_REL_ENABLE"
    DMM_ATTR_MEAS_REL_LEVEL = "dmm.ATTR_MEAS_REL_LEVEL"
    DMM_ATTR_MEAS_REL_METHOD = "dmm.ATTR_MEAS_REL_METHOD"
    DMM_ATTR_MEAS_RTD_ALPHA = "dmm.ATTR_MEAS_RTD_ALPHA"
    DMM_ATTR_MEAS_RTD_BETA = "dmm.ATTR_MEAS_RTD_BETA"
    DMM_ATTR_MEAS_RTD_DELTA = "dmm.ATTR_MEAS_RTD_DELTA"
    DMM_ATTR_MEAS_RTD_ZERO = "dmm.ATTR_MEAS_RTD_ZERO"
    DMM_ATTR_MEAS_SENSE_RANGE = "dmm.ATTR_MEAS_SENSE_RANGE"
    DMM_ATTR_MEAS_SIM_REF_TEMP = "dmm.ATTR_MEAS_SIM_REF_TEMP"
    DMM_ATTR_MEAS_THERMISTOR = "dmm.ATTR_MEAS_THERMISTOR"
    DMM_ATTR_MEAS_THERMOCOUPLE = "dmm.ATTR_MEAS_THERMOCOUPLE"
    DMM_ATTR_MEAS_THREE_RTD = "dmm.ATTR_MEAS_THREE_RTD"
    DMM_ATTR_MEAS_THRESHOLD_RANGE = "dmm.ATTR_MEAS_THRESHOLD_RANGE"
    DMM_ATTR_MEAS_THRESHOLD_RANGE_AUTO = "dmm.ATTR_MEAS_THRESHOLD_RANGE_AUTO"
    DMM_ATTR_MEAS_TRANSDUCER = "dmm.ATTR_MEAS_TRANSDUCER"
    DMM_ATTR_MEAS_TWO_RTD = "dmm.ATTR_MEAS_TWO_RTD"
    DMM_ATTR_MEAS_UNIT = "dmm.ATTR_MEAS_UNIT"
    DMM_ATTR_MEAS_USER_DELAY_1 = "dmm.ATTR_MEAS_USER_DELAY_1"
    DMM_ATTR_MEAS_USER_DELAY_2 = "dmm.ATTR_MEAS_USER_DELAY_2"
    DMM_ATTR_MEAS_USER_DELAY_3 = "dmm.ATTR_MEAS_USER_DELAY_3"
    DMM_ATTR_MEAS_USER_DELAY_4 = "dmm.ATTR_MEAS_USER_DELAY_4"
    DMM_ATTR_MEAS_USER_DELAY_5 = "dmm.ATTR_MEAS_USER_DELAY_5"
    DMM_AUDIBLE_FAIL = "dmm.AUDIBLE_FAIL"
    DMM_AUDIBLE_NONE = "dmm.AUDIBLE_NONE"
    DMM_AUDIBLE_PASS = "dmm.AUDIBLE_PASS"
    DMM_DELAY_OFF = "dmm.DELAY_OFF"
    DMM_DELAY_ON = "dmm.DELAY_ON"
    DMM_DETECTBW_300HZ = "dmm.DETECTBW_300HZ"
    DMM_DETECTBW_30HZ = "dmm.DETECTBW_30HZ"
    DMM_DETECTBW_3HZ = "dmm.DETECTBW_3HZ"
    DMM_DIGITS_3_5 = "dmm.DIGITS_3_5"
    DMM_DIGITS_4_5 = "dmm.DIGITS_4_5"
    DMM_DIGITS_5_5 = "dmm.DIGITS_5_5"
    DMM_DIGITS_6_5 = "dmm.DIGITS_6_5"
    DMM_DIRECTION_ENTER = "dmm.DIRECTION_ENTER"
    DMM_DIRECTION_LEAVE = "dmm.DIRECTION_LEAVE"
    DMM_FAIL_BOTH = "dmm.FAIL_BOTH"
    DMM_FAIL_HIGH = "dmm.FAIL_HIGH"
    DMM_FAIL_LOW = "dmm.FAIL_LOW"
    DMM_FAIL_NONE = "dmm.FAIL_NONE"
    DMM_FILTER_HYBRID_AVG = "dmm.FILTER_HYBRID_AVG"
    DMM_FILTER_MOVING_AVG = "dmm.FILTER_MOVING_AVG"
    DMM_FILTER_REPEAT_AVG = "dmm.FILTER_REPEAT_AVG"
    DMM_FUNC_4W_RESISTANCE = "dmm.FUNC_4W_RESISTANCE"
    DMM_FUNC_ACV_FREQUENCY = "dmm.FUNC_ACV_FREQUENCY"
    DMM_FUNC_ACV_PERIOD = "dmm.FUNC_ACV_PERIOD"
    DMM_FUNC_AC_CURRENT = "dmm.FUNC_AC_CURRENT"
    DMM_FUNC_AC_VOLTAGE = "dmm.FUNC_AC_VOLTAGE"
    DMM_FUNC_CAPACITANCE = "dmm.FUNC_CAPACITANCE"
    DMM_FUNC_CONTINUITY = "dmm.FUNC_CONTINUITY"
    DMM_FUNC_DCV_RATIO = "dmm.FUNC_DCV_RATIO"
    DMM_FUNC_DC_CURRENT = "dmm.FUNC_DC_CURRENT"
    DMM_FUNC_DC_VOLTAGE = "dmm.FUNC_DC_VOLTAGE"
    DMM_FUNC_DIGITIZE_CURRENT = "dmm.FUNC_DIGITIZE_CURRENT"
    DMM_FUNC_DIGITIZE_VOLTAGE = "dmm.FUNC_DIGITIZE_VOLTAGE"
    DMM_FUNC_DIODE = "dmm.FUNC_DIODE"
    DMM_FUNC_NONE = "dmm.FUNC_NONE"
    DMM_FUNC_RESISTANCE = "dmm.FUNC_RESISTANCE"
    DMM_FUNC_TEMPERATURE = "dmm.FUNC_TEMPERATURE"
    DMM_IMPEDANCE_10M = "dmm.IMPEDANCE_10M"
    DMM_IMPEDANCE_AUTO = "dmm.IMPEDANCE_AUTO"
    DMM_MATH_MXB = "dmm.MATH_MXB"
    DMM_MATH_PERCENT = "dmm.MATH_PERCENT"
    DMM_MATH_RECIPROCAL = "dmm.MATH_RECIPROCAL"
    DMM_METHOD_PARTS = "dmm.METHOD_PARTS"
    DMM_METHOD_RESULT = "dmm.METHOD_RESULT"
    DMM_MODE_EDGE = "dmm.MODE_EDGE"
    DMM_MODE_OFF = "dmm.MODE_OFF"
    DMM_MODE_WINDOW = "dmm.MODE_WINDOW"
    DMM_OCOMP_AUTO = "dmm.OCOMP_AUTO"
    DMM_OCOMP_OFF = "dmm.OCOMP_OFF"
    DMM_OCOMP_ON = "dmm.OCOMP_ON"
    DMM_OFF = "dmm.OFF"
    DMM_ON = "dmm.ON"
    DMM_RTD_D100 = "dmm.RTD_D100"
    DMM_RTD_F100 = "dmm.RTD_F100"
    DMM_RTD_PT100 = "dmm.RTD_PT100"
    DMM_RTD_PT385 = "dmm.RTD_PT385"
    DMM_RTD_PT3916 = "dmm.RTD_PT3916"
    DMM_RTD_USER = "dmm.RTD_USER"
    DMM_SLOPE_FALLING = "dmm.SLOPE_FALLING"
    DMM_SLOPE_RISING = "dmm.SLOPE_RISING"
    DMM_TERMINALS_FRONT = "dmm.TERMINALS_FRONT"
    DMM_TERMINALS_REAR = "dmm.TERMINALS_REAR"
    DMM_THERMOCOUPLE_B = "dmm.THERMOCOUPLE_B"
    DMM_THERMOCOUPLE_E = "dmm.THERMOCOUPLE_E"
    DMM_THERMOCOUPLE_J = "dmm.THERMOCOUPLE_J"
    DMM_THERMOCOUPLE_K = "dmm.THERMOCOUPLE_K"
    DMM_THERMOCOUPLE_N = "dmm.THERMOCOUPLE_N"
    DMM_THERMOCOUPLE_R = "dmm.THERMOCOUPLE_R"
    DMM_THERMOCOUPLE_S = "dmm.THERMOCOUPLE_S"
    DMM_THERMOCOUPLE_T = "dmm.THERMOCOUPLE_T"
    DMM_THERM_10000 = "dmm.THERM_10000"
    DMM_THERM_2252 = "dmm.THERM_2252"
    DMM_THERM_5000 = "dmm.THERM_5000"
    DMM_TRANS_FOURRTD = "dmm.TRANS_FOURRTD"
    DMM_TRANS_THERMISTOR = "dmm.TRANS_THERMISTOR"
    DMM_TRANS_THERMOCOUPLE = "dmm.TRANS_THERMOCOUPLE"
    DMM_TRANS_THREERTD = "dmm.TRANS_THREERTD"
    DMM_TRANS_TWORTD = "dmm.TRANS_TWORTD"
    DMM_UNIT_AMP = "dmm.UNIT_AMP"
    DMM_UNIT_CELSIUS = "dmm.UNIT_CELSIUS"
    DMM_UNIT_DB = "dmm.UNIT_DB"
    DMM_UNIT_DBM = "dmm.UNIT_DBM"
    DMM_UNIT_FAHRENHEIT = "dmm.UNIT_FAHRENHEIT"
    DMM_UNIT_KELVIN = "dmm.UNIT_KELVIN"
    DMM_UNIT_VOLT = "dmm.UNIT_VOLT"
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
    SCAN_ABORTED = "scan.ABORTED"
    SCAN_ALARM_LIMIT = "SCAN_ALARM_LIMIT"
    SCAN_BUILDING = "scan.BUILDING"
    SCAN_COUNT_INFINITE = "scan.COUNT_INFINITE"
    SCAN_EMPTY = "scan.EMPTY"
    SCAN_FAILED = "scan.FAILED"
    SCAN_MODE_FIXED_ABR = "scan.MODE_FIXED_ABR"
    SCAN_MODE_HIGH = "scan.MODE_HIGH"
    SCAN_MODE_LOW = "scan.MODE_LOW"
    SCAN_MODE_OFF = "scan.MODE_OFF"
    SCAN_MODE_OPEN_ALL = "scan.MODE_OPEN_ALL"
    SCAN_MODE_OPEN_USED = "scan.MODE_OPEN_USED"
    SCAN_MODE_OUTSIDE = "scan.MODE_OUTSIDE"
    SCAN_MODE_WINDOW = "scan.MODE_WINDOW"
    SCAN_OFF = "scan.OFF"
    SCAN_ON = "scan.ON"
    SCAN_PAUSED = "scan.PAUSED"
    SCAN_RUNNING = "scan.RUNNING"
    SCAN_STEPPING = "scan.STEPPING"
    SCAN_SUCCESS = "scan.SUCCESS"
    SCAN_WRITE_AFTER_SCAN = "scan.WRITE_AFTER_SCAN"
    SCAN_WRITE_AFTER_STEP = "scan.WRITE_AFTER_STEP"
    SCAN_WRITE_AT_END = "scan.WRITE_AT_END"
    SCAN_WRITE_NEVER = "scan.WRITE_NEVER"
    SLOT_PSEUDO_NONE = "slot.PSEUDO_NONE"
    SMU_AUDIBLE_FAIL = "smu.AUDIBLE_FAIL"
    SMU_AUDIBLE_NONE = "smu.AUDIBLE_NONE"
    SMU_AUDIBLE_PASS = "smu.AUDIBLE_PASS"
    SMU_OFF = "smu.OFF"
    SMU_ON = "smu.ON"
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
    TRIGGER_EVENT_ANALOGTRIGGER = "trigger.EVENT_ANALOGTRIGGER"
    TRIGGER_EVENT_BLENDERN = "trigger.EVENT_BLENDERN"
    TRIGGER_EVENT_COMMAND = "trigger.EVENT_COMMAND"
    TRIGGER_EVENT_DIGION = "trigger.EVENT_DIGION"
    TRIGGER_EVENT_DISPLAY = "trigger.EVENT_DISPLAY"
    TRIGGER_EVENT_EXTERNAL = "trigger.EVENT_EXTERNAL"
    TRIGGER_EVENT_LANN = "trigger.EVENT_LANN"
    TRIGGER_EVENT_NONE = "trigger.EVENT_NONE"
    TRIGGER_EVENT_NOTIFYN = "trigger.EVENT_NOTIFYN"
    TRIGGER_EVENT_SCAN_ALARM_LIMIT = "trigger.EVENT_SCAN_ALARM_LIMIT"
    TRIGGER_EVENT_SCAN_CHANNEL_READY = "trigger.EVENT_SCAN_CHANNEL_READY"
    TRIGGER_EVENT_SCAN_COMPLETE = "trigger.EVENT_SCAN_COMPLETE"
    TRIGGER_EVENT_SCAN_MEASURE_COMPLETE = "trigger.EVENT_SCAN_MEASURE_COMPLETE"
    TRIGGER_EVENT_TIMER1 = "trigger.EVENT_TIMER1"
    TRIGGER_EVENT_TIMER2 = "trigger.EVENT_TIMER2"
    TRIGGER_EVENT_TIMER3 = "trigger.EVENT_TIMER3"
    TRIGGER_EVENT_TIMER4 = "trigger.EVENT_TIMER4"
    TRIGGER_EVENT_TIMERN = "trigger.EVENT_TIMERN"
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
    TRIGGER_SCAN_ALARM_LIMIT = "trigger.SCAN_ALARM_LIMIT"
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
class DAQ6510Commands:
    """The DAQ6510 commands.

    This provides access to all the commands for the DAQ6510 device. See the documentation of each
    property for more usage information.

    Properties and methods:
        - ``.available()``: The ``available()`` function.
        - ``.beeper``: The ``beeper`` command tree.
        - ``.buffer_var``: The ``bufferVar`` command tree.
        - ``.buffer``: The ``buffer`` command tree.
        - ``.channel``: The ``channel`` command tree.
        - ``.createconfigscript()``: The ``createconfigscript()`` function.
        - ``.dataqueue``: The ``dataqueue`` command tree.
        - ``.delay()``: The ``delay()`` function.
        - ``.digio``: The ``digio`` command tree.
        - ``.display``: The ``display`` command tree.
        - ``.dmm``: The ``dmm`` command tree.
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
        - ``.scan``: The ``scan`` command tree.
        - ``.script_var``: The ``scriptVar`` command tree.
        - ``.script``: The ``script`` command tree.
        - ``.slot``: The ``slot`` command tree.
        - ``.slotx``: The ``slot[slot]`` command tree.
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
        self._channel = Channel(device)
        self._dataqueue = Dataqueue(device)
        self._digio = Digio(device)
        self._display = Display(device)
        self._dmm = Dmm(device)
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
        self._scan = Scan(device)
        self._script = Script(device)
        self._script_var: Dict[str, Scriptvar] = DefaultDictPassKeyToFactory(
            lambda x: Scriptvar(device, str(x))
        )
        self._slot = Slot(device)
        self._slotx: Dict[int, SlotItem] = DefaultDictPassKeyToFactory(
            lambda x: SlotItem(device, f"slot[{x}]")
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
            - ``.COL_ALL``: Save all data from the specified reading buffer.
            - ``.COL_BRIEF``: Save reading and relative time data from the specified reading buffer.
            - ``.COL_CHANNEL``: Save channel data from the specified reading buffer.
            - ``.COL_CSV_CHAN_COLS``: Ignore other columns and use a special format with a column
              per channel.
            - ``.COL_CSV_EASY_GRAPH``: Ignore other columns and use special format that is easy to
              graph in Microsoft Excel.
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
            - ``.channelmath()``: The ``buffer.channelmath()`` function.
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
            - ``.channels``: The ``bufferVar.channels[N]`` attribute.
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
            - ``.units``: The ``bufferVar.units[N]`` attribute.
        """
        return self._buffer_var

    @property
    def channel(self) -> Channel:
        """Return the ``channel`` command tree.

        Constants:
            - ``.COUNT_INTERVAL_10M``: The storage of channel relay closure count is set to 10
              minutes.
            - ``.COUNT_INTERVAL_15M``: The storage of channel relay closure count is set to 15
              minutes.
            - ``.COUNT_INTERVAL_1M``: The storage of channel relay closure count is set to 1 minute.
            - ``.COUNT_INTERVAL_24H``: The storage of channel relay closure count is set to 24
              hours.
            - ``.COUNT_INTERVAL_30M``: The storage of channel relay closure count is set to 30
              minutes.
            - ``.COUNT_INTERVAL_5M``: The storage of channel relay closure count is set to 5
              minutes.
            - ``.COUNT_INTERVAL_60M``: The storage of channel relay closure count is set to 60
              minutes.
            - ``.IND_CLOSED``: Channel is closed.
            - ``.IND_MATCH``: Digital I/O or totalizer channel value is matched.
            - ``.IND_OVERFLOW``: Totalizer channel has overflowed.
            - ``.MATCH_ANY``: For an any match, a match is when the match value equals the
              channel-read value.
            - ``.MATCH_EXACT``: The state match indicator only becomes true when the match value
              equals the channel-read value.
            - ``.MATCH_NONE``: When none is set, matching is disabled.
            - ``.MATCH_UNCHANGED``: For an unchanged match, the value should be the same as the
              original. If not, a match is declared.
            - ``.MODE_FALLING_EDGE``: For totalizer channels, select falling edge.
            - ``.MODE_FALLING_EDGE_READ_RESET``: For totalizer channels, select falling edge, then
              reset the count on read.
            - ``.MODE_INPUT``: Set digital channel to input.
            - ``.MODE_OUTPUT``: Set digital channel to output.
            - ``.MODE_RISING_EDGE``: For totalizer channels, select rising edge.
            - ``.MODE_RISING_EDGE_READ_RESET``: For totalizer channels, select rising edge, then
              reset the count on read.
            - ``.TYPE_BACKPLANE``: Backplane.
            - ``.TYPE_DAC``: DAC channel.
            - ``.TYPE_DIGITAL``: Digital channel.
            - ``.TYPE_POLE``: Pole channel.
            - ``.TYPE_RADIO``: Radio channel.
            - ``.TYPE_SWITCH``: Switch channel.
            - ``.TYPE_TOTALIZER``: Totalizer channel.

        Sub-properties and sub-methods:
            - ``.close()``: The ``channel.close()`` function.
            - ``.getclose()``: The ``channel.getclose()`` function.
            - ``.getcommonside()``: The ``channel.getcommonside()`` function.
            - ``.getcount()``: The ``channel.getcount()`` function.
            - ``.getcountinterval()``: The ``channel.getcountinterval()`` function.
            - ``.getdelay()``: The ``channel.getdelay()`` function.
            - ``.getdmm()``: The ``channel.getdmm()`` function.
            - ``.getlabel()``: The ``channel.getlabel()`` function.
            - ``.getmatch()``: The ``channel.getmatch()`` function.
            - ``.getmatchtype()``: The ``channel.getmatchtype()`` function.
            - ``.getmode()``: The ``channel.getmode()`` function.
            - ``.getstate()``: The ``channel.getstate()`` function.
            - ``.gettype()``: The ``channel.gettype()`` function.
            - ``.getwidth()``: The ``channel.getwidth()`` function.
            - ``.multiple``: The ``channel.multiple`` command tree.
            - ``.open()``: The ``channel.open()`` function.
            - ``.read()``: The ``channel.read()`` function.
            - ``.setcommonside()``: The ``channel.setcommonside()`` function.
            - ``.setcountinterval()``: The ``channel.setcountinterval()`` function.
            - ``.setdelay()``: The ``channel.setdelay()`` function.
            - ``.setdmm()``: The ``channel.setdmm()`` function.
            - ``.setlabel()``: The ``channel.setlabel()`` function.
            - ``.setmatch()``: The ``channel.setmatch()`` function.
            - ``.setmatchtype()``: The ``channel.setmatchtype()`` function.
            - ``.setmode()``: The ``channel.setmode()`` function.
            - ``.setwidth()``: The ``channel.setwidth()`` function.
            - ``.write()``: The ``channel.write()`` function.
        """
        return self._channel

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
            - ``.SCREEN_CHANNEL_CONTROL``: Display the channel control screen.
            - ``.SCREEN_CHANNEL_SCAN``: Display channel scan screen.
            - ``.SCREEN_CHANNEL_SETTINGS``: Display channel settings screen.
            - ``.SCREEN_CHANNEL_SWIPE``: Display CHANNEL swipe screen (only available when a card is
              installed and rear terminals are selected).
            - ``.SCREEN_FUNCTIONS_SWIPE``: Display the Functions swipe screen.
            - ``.SCREEN_GRAPH``: Display the last selected graph screen tab.
            - ``.SCREEN_GRAPH_SWIPE``: Display graph swipe screen.
            - ``.SCREEN_HISTOGRAM``: Display Histogram.
            - ``.SCREEN_HOME``: Display Home screen.
            - ``.SCREEN_HOME_LARGE_READING``: Display Home screen with large readings.
            - ``.SCREEN_NONSWITCH_SWIPE``: Display NONSWITCH swipe screen (only available when a
              card with non-switching  channels is installed and rear terminals are selected).
            - ``.SCREEN_PROCESSING``: Open a screen that uses minimal CPU resources.
            - ``.SCREEN_READING_TABLE``: Display Reading Table screen.
            - ``.SCREEN_SCAN_SWIPE``: Display SCAN swipe screen (only available when a card is
              installed and rear terminals are selected).
            - ``.SCREEN_SECONDARY_SWIPE``: Display the SECONDARY swipe screen.
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
            - ``.watchchannels``: The ``display.watchchannels`` attribute.
        """
        return self._display

    @property
    def dmm(self) -> Dmm:
        """Return the ``dmm`` command tree.

        Constants:
            - ``.APERTURE_AUTO``: The aperture setting for the selected function.
            - ``.ATTR_DIGI_APERTURE``: Aperture setting for digitize.
            - ``.ATTR_DIGI_ATRIG_EDGE_LEVEL``: Analog trigger edge level.
            - ``.ATTR_DIGI_ATRIG_EDGE_SLOPE``: Analog trigger edge slope.
            - ``.ATTR_DIGI_ATRIG_MODE``: Analog trigger mode.
            - ``.ATTR_DIGI_ATRIG_WINDOW_DIRECTION``: Analog trigger window direction.
            - ``.ATTR_DIGI_ATRIG_WINDOW_LEVEL_HIGH``: Analog trigger window level high.
            - ``.ATTR_DIGI_ATRIG_WINDOW_LEVEL_LOW``: Analog trigger window level low.
            - ``.ATTR_DIGI_COUNT``: The number of measurements to digitize when a measurement is
              requested.
            - ``.ATTR_DIGI_DBM_REFERENCE``: Decibel-milliwatts (dBm) reference for digitize voltage.
            - ``.ATTR_DIGI_DB_REFERENCE``: Decibel (dB) reference for digitize voltage.
            - ``.ATTR_DIGI_DIGITS``: Display digits setting for digitize.
            - ``.ATTR_DIGI_FUNCTION``: Digitize function.
            - ``.ATTR_DIGI_INPUT_IMPEDANCE``: Input impedance setting.
            - ``.ATTR_DIGI_LIMIT_AUDIBLE_1``: Set limit 1 audible.
            - ``.ATTR_DIGI_LIMIT_AUDIBLE_2``: Set limit 2 audible.
            - ``.ATTR_DIGI_LIMIT_AUTO_CLEAR_1``: Enable or disable limit 1 autoclear.
            - ``.ATTR_DIGI_LIMIT_AUTO_CLEAR_2``: Enable or disable limit 2 autoclear.
            - ``.ATTR_DIGI_LIMIT_ENABLE_1``: Enable or disable limit 1.
            - ``.ATTR_DIGI_LIMIT_ENABLE_2``: Limit 2 enable.
            - ``.ATTR_DIGI_LIMIT_FAIL_1``: Limit 1 fail.
            - ``.ATTR_DIGI_LIMIT_FAIL_2``: Limit 2 fail.
            - ``.ATTR_DIGI_LIMIT_HIGH_1``: Set limit 1 high value.
            - ``.ATTR_DIGI_LIMIT_HIGH_2``: Set limit 2 high value.
            - ``.ATTR_DIGI_LIMIT_LOW_1``: Set limit 1 low value.
            - ``.ATTR_DIGI_LIMIT_LOW_2``: Set limit 2 low value.
            - ``.ATTR_DIGI_MATH_ENABLE``: Enable math operations for the selected measurement
              function.
            - ``.ATTR_DIGI_MATH_FORMAT``: Math format.
            - ``.ATTR_DIGI_MATH_MXB_BF``: b (offset) value.
            - ``.ATTR_DIGI_MATH_MXB_MF``: m (scalar) value.
            - ``.ATTR_DIGI_MATH_PERCENT``: Percent.
            - ``.ATTR_DIGI_RANGE``: Measure range setting for digitize.
            - ``.ATTR_DIGI_REL_ENABLE``: Relative enable.
            - ``.ATTR_DIGI_REL_LEVEL``: Relative level.
            - ``.ATTR_DIGI_SAMPLE_RATE``: Sample rate for digitize.
            - ``.ATTR_DIGI_UNIT``: Measure unit setting for digitize.
            - ``.ATTR_DIGI_USER_DELAY_1``: User delay 1 setting for digitize.
            - ``.ATTR_DIGI_USER_DELAY_2``: User delay 2 setting for digitize.
            - ``.ATTR_DIGI_USER_DELAY_3``: User delay 3 setting for digitize.
            - ``.ATTR_DIGI_USER_DELAY_4``: User delay 4 setting for digitize.
            - ``.ATTR_DIGI_USER_DELAY_5``: User delay 5 setting for digitize.
            - ``.ATTR_DIGI_WINDOW_DIRECTION``: Defines if the analog trigger occurs when the signal
              enters or leaves the defined high and low analog signal level boundaries.
            - ``.ATTR_DIGI_WINDOW_LEVEL_HIGH``: The upper boundary of the analog trigger window.
            - ``.ATTR_DIGI_WINDOW_LEVEL_LOW``: The lower boundary of the analog trigger window.
            - ``.ATTR_MEAS_APERTURE``: Aperture setting.
            - ``.ATTR_MEAS_ATRIG_EDGE_LEVEL``: Analog trigger edge level.
            - ``.ATTR_MEAS_ATRIG_EDGE_SLOPE``: Analog trigger edge slope.
            - ``.ATTR_MEAS_ATRIG_MODE``: Analog trigger mode.
            - ``.ATTR_MEAS_ATRIG_WINDOW_DIRECTION``: Analog trigger window direction.
            - ``.ATTR_MEAS_ATRIG_WINDOW_LEVEL_HIGH``: Analog trigger window level high.
            - ``.ATTR_MEAS_ATRIG_WINDOW_LEVEL_LOW``: Analog trigger window level low.
            - ``.ATTR_MEAS_AUTO_DELAY``: Autodelay setting.
            - ``.ATTR_MEAS_AUTO_ZERO``: Autozero setting.
            - ``.ATTR_MEAS_BIAS_LEVEL``: Bias level.
            - ``.ATTR_MEAS_COUNT``: Measure count setting.
            - ``.ATTR_MEAS_DBM_REFERENCE``: dBm reference setting.
            - ``.ATTR_MEAS_DB_REFERENCE``: dB reference setting.
            - ``.ATTR_MEAS_DETECTBW``: Detector bandwidth setting.
            - ``.ATTR_MEAS_DIGITS``: Display digits setting.
            - ``.ATTR_MEAS_FILTER_COUNT``: Set filter count.
            - ``.ATTR_MEAS_FILTER_ENABLE``: Enable or disable filter.
            - ``.ATTR_MEAS_FILTER_TYPE``: Set filter type.
            - ``.ATTR_MEAS_FILTER_WINDOW``: Filter window.
            - ``.ATTR_MEAS_FOUR_RTD``: 4-wire RTD type.
            - ``.ATTR_MEAS_INPUT_IMPEDANCE``: Input impedance setting.
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
            - ``.ATTR_MEAS_LINE_SYNC``: Line sync setting.
            - ``.ATTR_MEAS_MATH_ENABLE``: Enable math operations for the selected measurement
              function.
            - ``.ATTR_MEAS_MATH_FORMAT``: Math format.
            - ``.ATTR_MEAS_MATH_MXB_BF``: b (offset) value.
            - ``.ATTR_MEAS_MATH_MXB_MF``: m (scalar) value.
            - ``.ATTR_MEAS_MATH_PERCENT``: Percent.
            - ``.ATTR_MEAS_NPLC``: NPLC setting.
            - ``.ATTR_MEAS_OFFCOMP_ENABLE``: Offset compensation.
            - ``.ATTR_MEAS_OPEN_DETECTOR``: Open lead detector.
            - ``.ATTR_MEAS_RANGE``: Measure range setting.
            - ``.ATTR_MEAS_RANGE_AUTO``: Autorange setting.
            - ``.ATTR_MEAS_REF_JUNCTION``: Reference junction.
            - ``.ATTR_MEAS_REL_ENABLE``: Relative offset enable.
            - ``.ATTR_MEAS_REL_LEVEL``: Relative offset level.
            - ``.ATTR_MEAS_REL_METHOD``: Relative offset method for DCV ratio measurements.
            - ``.ATTR_MEAS_RTD_ALPHA``: RTD alpha.
            - ``.ATTR_MEAS_RTD_BETA``: RTD beta.
            - ``.ATTR_MEAS_RTD_DELTA``: RTD delta.
            - ``.ATTR_MEAS_RTD_ZERO``: RTD zero.
            - ``.ATTR_MEAS_SENSE_RANGE``: Sense range (read only).
            - ``.ATTR_MEAS_SIM_REF_TEMP``: Simulated reference temperature.
            - ``.ATTR_MEAS_THERMISTOR``: Thermistor.
            - ``.ATTR_MEAS_THERMOCOUPLE``: Thermocouple.
            - ``.ATTR_MEAS_THREE_RTD``: 3-wire RTD type.
            - ``.ATTR_MEAS_THRESHOLD_RANGE``: Threshold range.
            - ``.ATTR_MEAS_THRESHOLD_RANGE_AUTO``: Threshold autorange.
            - ``.ATTR_MEAS_TRANSDUCER``: Transducer.
            - ``.ATTR_MEAS_TWO_RTD``: 2-wire RTD type.
            - ``.ATTR_MEAS_UNIT``: Measure unit setting.
            - ``.ATTR_MEAS_USER_DELAY_1``: User delay 1 setting.
            - ``.ATTR_MEAS_USER_DELAY_2``: User delay 2 setting.
            - ``.ATTR_MEAS_USER_DELAY_3``: User delay 3 setting.
            - ``.ATTR_MEAS_USER_DELAY_4``: User delay 4 setting.
            - ``.ATTR_MEAS_USER_DELAY_5``: User delay 5 setting.
            - ``.AUDIBLE_FAIL``: Sound a beeper when a limit test passes or fails.
            - ``.AUDIBLE_NONE``: Do not sound a beeper when a limit test passes or fails.
            - ``.AUDIBLE_PASS``: Sound a beeper when a limit test passes or passes.
            - ``.DELAY_OFF``: Disable the delay.
            - ``.DELAY_ON``: Enable the delay.
            - ``.DETECTBW_300HZ``: Sets the detector bandwidth to 300 Hz for AC current and AC
              voltage measurements.
            - ``.DETECTBW_30HZ``: Sets the detector bandwidth to 30 Hz for AC current and AC voltage
              measurements.
            - ``.DETECTBW_3HZ``: Sets the detector bandwidth to 3 Hz for AC current and AC voltage
              measurements.
            - ``.DIGITS_3_5``: 3½ display digits.
            - ``.DIGITS_4_5``: 4½ display digits.
            - ``.DIGITS_5_5``: 5½ display digits.
            - ``.DIGITS_6_5``: 6½ display digits.
            - ``.DIRECTION_ENTER``: The analog trigger occurs when the signal enters the defined
              signal boundaries.
            - ``.DIRECTION_LEAVE``: The analog trigger occurs when the signal leaves the defined
              signal boundaries.
            - ``.FAIL_BOTH``: Test failed; measurement exceeded both limits.
            - ``.FAIL_HIGH``: Test failed; measurement exceeded high limit.
            - ``.FAIL_LOW``: Test failed; measurement exceeded low limit.
            - ``.FAIL_NONE``: Test passed; measurement under or equal to the high limit.
            - ``.FILTER_HYBRID_AVG``: Selects the hybrid filter when measurement filter is enabled.
            - ``.FILTER_MOVING_AVG``: Selects the moving filter when measurement filter is enabled.
            - ``.FILTER_REPEAT_AVG``: Selects the repeating filter when measurement filter is
              enabled.
            - ``.FUNC_4W_RESISTANCE``: 4W resistance measurement function.
            - ``.FUNC_ACV_FREQUENCY``: ACV frequency function.
            - ``.FUNC_ACV_PERIOD``: ACV period function.
            - ``.FUNC_AC_CURRENT``: AC current.
            - ``.FUNC_AC_VOLTAGE``: AC voltage function.
            - ``.FUNC_CAPACITANCE``: Capacitance function.
            - ``.FUNC_CONTINUITY``: Continuity function.
            - ``.FUNC_DCV_RATIO``: DCV ratio function.
            - ``.FUNC_DC_CURRENT``: Current measurement function.
            - ``.FUNC_DC_VOLTAGE``: DC voltage function.
            - ``.FUNC_DIGITIZE_CURRENT``: Digitize current.
            - ``.FUNC_DIGITIZE_VOLTAGE``: Digitize voltage.
            - ``.FUNC_DIODE``: Diode function.
            - ``.FUNC_NONE``: No digitize function selected (read only).
            - ``.FUNC_RESISTANCE``: 2W resistance measurement function.
            - ``.FUNC_TEMPERATURE``: Temperature.
            - ``.IMPEDANCE_10M``: Enable the 10 MΩ input divider for all ranges.
            - ``.IMPEDANCE_AUTO``: Automatically enable the 10 MΩ input divider.
            - ``.MATH_MXB``: Perform y = mx+b operation on measurement.
            - ``.MATH_PERCENT``: Perform percent operation on measurements.
            - ``.MATH_RECIPROCAL``: Perform reciprocal math operation on measurements.
            - ``.METHOD_PARTS``: Apply relative offset to the measurements before calculating the dc
              voltage ratio value.
            - ``.METHOD_RESULT``: Do not apply relative offset to the measurements before
              calculating the dc voltage ratio value.
            - ``.MODE_EDGE``: Set analog trigger event mode to edge (signal crosses one level).
            - ``.MODE_OFF``: Set analog trigger event mode off.
            - ``.MODE_WINDOW``: Set analog trigger event mode to window (signal enters or exits a
              window defined by two levels).
            - ``.OCOMP_AUTO``: Set offset compensation automatically.
            - ``.OCOMP_OFF``: Disable offset compensation.
            - ``.OCOMP_ON``: Enable offset compensation (for 4-wire resistance, not available for
              ranges more than 10 kΩ).
            - ``.OFF``: Set the threshold range manually.
            - ``.ON``: Set the threshold range automatically.
            - ``.RTD_D100``: D100 three-wire RTD.
            - ``.RTD_F100``: F100 4-wire RTD.
            - ``.RTD_PT100``: PT100 three-wire RTD.
            - ``.RTD_PT385``: PT385 three-wire RTD.
            - ``.RTD_PT3916``: PT3916 three-wire RTD.
            - ``.RTD_USER``: User-specified three-wire RTD.
            - ``.SLOPE_FALLING``: Falling slope for the analog trigger edge.
            - ``.SLOPE_RISING``: Rising slope for the analog trigger edge.
            - ``.TERMINALS_FRONT``: Instrument is using the front-panel input and output terminals.
            - ``.TERMINALS_REAR``: Instrument is using the rear-panel input and output terminals.
            - ``.THERMOCOUPLE_B``: B thermocouple type.
            - ``.THERMOCOUPLE_E``: E thermocouple type.
            - ``.THERMOCOUPLE_J``: J thermocouple type.
            - ``.THERMOCOUPLE_K``: K thermocouple type.
            - ``.THERMOCOUPLE_N``: N thermocouple type.
            - ``.THERMOCOUPLE_R``: R thermocouple type.
            - ``.THERMOCOUPLE_S``: S thermocouple type.
            - ``.THERMOCOUPLE_T``: T thermocouple type.
            - ``.THERM_10000``: 10000 ohm thermistor.
            - ``.THERM_2252``: 2252 ohm thermistor.
            - ``.THERM_5000``: 5000 ohm thermistor.
            - ``.TRANS_FOURRTD``: Set the transducer type to  four-wire RTD.
            - ``.TRANS_THERMISTOR``: Set the transducer type to thermistor.
            - ``.TRANS_THERMOCOUPLE``: Set the transducer type to thermocouple.
            - ``.TRANS_THREERTD``: Set the transducer type to  three-wire RTD.
            - ``.TRANS_TWORTD``: Set the transducer type to two-wire RTD.
            - ``.UNIT_AMP``: Set unit of measure to amps (only available for current measurements).
            - ``.UNIT_CELSIUS``: Display Celsius as units of measurement.
            - ``.UNIT_DB``: Display decibels as units for the measure voltage function.
            - ``.UNIT_DBM``: Display decibel-millwatts as units for the  voltage function.
            - ``.UNIT_FAHRENHEIT``: Display Fahrenheit as units of measurement.
            - ``.UNIT_KELVIN``: Display Kelvin as units of measurement.
            - ``.UNIT_VOLT``: Display voltage as units for the voltage function.

        Sub-properties and sub-methods:
            - ``.digitize``: The ``dmm.digitize`` command tree.
            - ``.measure``: The ``dmm.measure`` command tree.
            - ``.reset()``: The ``dmm.reset()`` function.
            - ``.terminals``: The ``dmm.terminals`` attribute.
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
    def scan(self) -> Scan:
        """Return the ``scan`` command tree.

        Constants:
            - ``.ABORTED``: The scan was canceled.
            - ``.BUILDING``: The instrument is building the scan.
            - ``.COUNT_INFINITE``: Set the number of times the scan is repeated to repeated until
              aborted.
            - ``.EMPTY``: Scan is not set up.
            - ``.FAILED``: The scan failed.
            - ``.MODE_FIXED_ABR``: Sets the relay action when the scan starts to automatic backplane
              relay.
            - ``.MODE_HIGH``: Start the scan when the measurement exceeds the value set by
              scan.monitor.limit.high.value.
            - ``.MODE_LOW``: Start the scan when the measurement is below the value set by
              scan.monitor.limit.low.value.
            - ``.MODE_OFF``: Start the scan without waiting for a specific value.
            - ``.MODE_OPEN_ALL``: Sets the relay action when the scan starts to open all.
            - ``.MODE_OPEN_USED``: Sets the relay action when the scan starts to use an intelligent
              open.
            - ``.MODE_OUTSIDE``: Start the scan when the measurement is less than the lower limit or
              more than the upper limit.
            - ``.MODE_WINDOW``: Start the scan when the measurement is between the lower limit and
              the upper limit.
            - ``.OFF``: Do not restart scan.
            - ``.ON``: Restart scan.
            - ``.PAUSED``: The scan was paused.
            - ``.RUNNING``: The scan is running the trigger model portion of the scan.
            - ``.STEPPING``: The scan is running the channel action portion of the scan.
            - ``.SUCCESS``: The scan completed successfully.
            - ``.WRITE_AFTER_SCAN``: Write scan data to a file on a USB flash drive at completion of
              each scan.
            - ``.WRITE_AFTER_STEP``: Write scan data to a file on a USB flash drive at completion of
              each scan step.
            - ``.WRITE_AT_END``: Write scan data to a file on a USB flash drive at completion of all
              scans.
            - ``.WRITE_NEVER``: Do not write data to a file.

        Sub-properties and sub-methods:
            - ``.add()``: The ``scan.add()`` function.
            - ``.addsinglestep()``: The ``scan.addsinglestep()`` function.
            - ``.addwrite()``: The ``scan.addwrite()`` function.
            - ``.buffer``: The ``scan.buffer`` attribute.
            - ``.bypass``: The ``scan.bypass`` attribute.
            - ``.channel``: The ``scan.channel`` command tree.
            - ``.create()``: The ``scan.create()`` function.
            - ``.export()``: The ``scan.export()`` function.
            - ``.learnlimits()``: The ``scan.learnlimits()`` function.
            - ``.list()``: The ``scan.list()`` function.
            - ``.measure``: The ``scan.measure`` command tree.
            - ``.mode``: The ``scan.mode`` attribute.
            - ``.monitor``: The ``scan.monitor`` command tree.
            - ``.restart``: The ``scan.restart`` attribute.
            - ``.scancount``: The ``scan.scancount`` attribute.
            - ``.scaninterval``: The ``scan.scaninterval`` attribute.
            - ``.start``: The ``scan.start`` command tree.
            - ``.state()``: The ``scan.state()`` function.
            - ``.stepcount``: The ``scan.stepcount`` attribute.
        """
        return self._scan

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
    def slot(self) -> Slot:
        """Return the ``slot`` command tree.

        Constants:
            - ``.PSEUDO_NONE``: No pseudocard.
        """
        return self._slot

    @property
    def slotx(self) -> Dict[int, SlotItem]:
        """Return the ``slot[slot]`` command tree.

        Info:
            - ``slot``, the slot number.

        Sub-properties and sub-methods:
            - ``.amps``: The ``slot[slot].amps`` command tree.
            - ``.analogoutput``: The ``slot[slot].analogoutput`` command tree.
            - ``.commonsideohms``: The ``slot[slot].commonsideohms`` attribute.
            - ``.digitalio``: The ``slot[slot].digitalio`` command tree.
            - ``.idn``: The ``slot[slot].idn`` attribute.
            - ``.isolated``: The ``slot[slot].isolated`` command tree.
            - ``.matrix``: The ``slot[slot].matrix`` command tree.
            - ``.maxvoltage``: The ``slot[slot].maxvoltage`` attribute.
            - ``.pseudocard``: The ``slot[slot].pseudocard`` attribute.
            - ``.tempsensor``: The ``slot[slot].tempsensor`` attribute.
            - ``.totalizer``: The ``slot[slot].totalizer`` command tree.
            - ``.voltage``: The ``slot[slot].voltage`` command tree.
        """
        return self._slotx

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
            - ``.EVENT_ANALOGTRIGGER``: Analog trigger.
            - ``.EVENT_BLENDERN``: Trigger event blender N (1 to 2), which combines trigger events.
            - ``.EVENT_COMMAND``: A command interface trigger.
            - ``.EVENT_DIGION``: Line edge (either rising, falling, or either based on the
              configuration of the line) detected on digital input line N (1 to 6).
            - ``.EVENT_DISPLAY``: Front-panel TRIGGER key press.
            - ``.EVENT_EXTERNAL``: External in trigger.
            - ``.EVENT_LANN``: Appropriate LXI trigger packet is received on LAN trigger object N (1
              to 8).
            - ``.EVENT_NONE``: No trigger event.
            - ``.EVENT_NOTIFYN``: Notify trigger block N (1 to 3) generates a trigger event when the
              trigger model executes it.
            - ``.EVENT_SCAN_ALARM_LIMIT``: Limit value for scan reached (returns
              trigger.EVENT_NOTIFY3).
            - ``.EVENT_SCAN_CHANNEL_READY``: Channel closed (returns trigger.EVENT_NOTIFY6).
            - ``.EVENT_SCAN_COMPLETE``: Scan completed (returns trigger.EVENT_NOTIFY8).
            - ``.EVENT_SCAN_MEASURE_COMPLETE``: Measure completed (returns trigger.EVENT_NOTIFY7).
            - ``.EVENT_TIMER1``: Trigger timer 1 expired.
            - ``.EVENT_TIMER2``: Trigger timer 2 expired.
            - ``.EVENT_TIMER3``: Trigger timer 3 expired.
            - ``.EVENT_TIMER4``: Trigger timer 4 expired.
            - ``.EVENT_TIMERN``: Trigger timer N (1 to 4) expired.
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
            - ``.SCAN_ALARM_LIMIT``: Scan alarm limit exceeded.
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


class DAQ6510Mixin:
    """A mixin that provides access to the DAQ6510 commands and constants.

    Properties:
        - ``.command_argument_constants``: The DAQ6510 command argument constants.
        - ``.commands``: The DAQ6510 commands.
    """

    @cached_property
    def command_argument_constants(self) -> DAQ6510CommandConstants:  # pylint: disable=no-self-use
        """Return the DAQ6510 command argument constants.

        This provides access to all the string constants which can be used as arguments for DAQ6510
        commands.
        """
        return DAQ6510CommandConstants()

    @cached_property
    def commands(self) -> DAQ6510Commands:
        """Return the DAQ6510 commands.

        This provides access to all the commands for the DAQ6510 device. See the documentation of
        each sub-property for more usage information.

        Sub-properties and sub-methods:
            - ``.available()``: The ``available()`` function.
            - ``.beeper``: The ``beeper`` command tree.
            - ``.buffer_var``: The ``bufferVar`` command tree.
            - ``.buffer``: The ``buffer`` command tree.
            - ``.channel``: The ``channel`` command tree.
            - ``.createconfigscript()``: The ``createconfigscript()`` function.
            - ``.dataqueue``: The ``dataqueue`` command tree.
            - ``.delay()``: The ``delay()`` function.
            - ``.digio``: The ``digio`` command tree.
            - ``.display``: The ``display`` command tree.
            - ``.dmm``: The ``dmm`` command tree.
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
            - ``.scan``: The ``scan`` command tree.
            - ``.script_var``: The ``scriptVar`` command tree.
            - ``.script``: The ``script`` command tree.
            - ``.slot``: The ``slot`` command tree.
            - ``.slotx``: The ``slot[slot]`` command tree.
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
        return DAQ6510Commands(device)
