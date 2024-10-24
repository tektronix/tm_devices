# pylint: disable=line-too-long
# ruff: noqa: D402,PLR0913
"""The SMU2606B commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional

from tm_devices.driver_mixins.device_control.tsp_control import TSPControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_8ojdkz_smu.display import Display
from .gen_8ojdkz_smu.node import NodeItem
from .gen_8ojdkz_smu.smux import SmuxItem
from .gen_8ojdkz_smu.status import Status
from .gen_ahkybr_smu.beeper import Beeper
from .gen_ahkybr_smu.buffervar import Buffervar
from .gen_ahkybr_smu.eventlog import Eventlog
from .gen_ahkybr_smu.lan import Lan
from .gen_ahkybr_smu.os import Os
from .gen_ahkybr_smu.script import Script
from .gen_ahkybr_smu.scriptvar import Scriptvar
from .gen_ahkybr_smu.setup_1 import Setup
from .gen_ahkybr_smu.tspnet import Tspnet
from .gen_aih9e2_smu.trigger import Trigger
from .gen_aqr1t1_smu.localnode import Localnode
from .gen_au597k_smu.digio import Digio
from .gen_au597k_smu.format import Format
from .gen_au597k_smu.tsplink import Tsplink
from .gen_eat5s3_smudaqdmmss.dataqueue import Dataqueue
from .gen_eat5s3_smudaqdmmss.fs import Fs
from .gen_eat5s3_smudaqdmmss.userstring import Userstring
from .gen_efap3f_smuss.bit import Bit
from .gen_efap3f_smuss.errorqueue import Errorqueue
from .gen_efap3f_smuss.io import Io
from .gen_efap3f_smuss.timer import Timer
from .helpers import DefaultDictPassKeyToFactory, NoDeviceProvidedError


# pylint: disable=too-few-public-methods
class SMU2606BCommandConstants:
    """The SMU2606B command argument constants.

    This provides access to all the string constants which can be used as arguments for SMU2606B
    commands.
    """

    BEEPER_OFF = "beeper.OFF"
    BEEPER_ON = "beeper.ON"
    DATAQUEUE_CAPACITY = "dataqueue.CAPACITY"
    DIGIO_TRIGGER_N_EVENT_ID = "digio.trigger[N].EVENT_ID"
    DIGIO_TRIG_BYPASS = "digio.TRIG_BYPASS"
    DIGIO_TRIG_EITHER = "digio.TRIG_EITHER"
    DIGIO_TRIG_FALLING = "digio.TRIG_FALLING"
    DIGIO_TRIG_RISING = "digio.TRIG_RISING"
    DIGIO_TRIG_RISINGA = "digio.TRIG_RISINGA"
    DIGIO_TRIG_RISINGM = "digio.TRIG_RISINGM"
    DIGIO_TRIG_SYNCHRONOUS = "digio.TRIG_SYNCHRONOUS"
    DIGIO_TRIG_SYNCHRONOUSA = "digio.TRIG_SYNCHRONOUSA"
    DIGIO_TRIG_SYNCHRONOUSM = "digio.TRIG_SYNCHRONOUSM"
    DISPLAY_ANNUNCIATOR_4_WIRE = "display.ANNUNCIATOR_4_WIRE"
    DISPLAY_ANNUNCIATOR_ARM = "display.ANNUNCIATOR_ARM"
    DISPLAY_ANNUNCIATOR_AUTO = "display.ANNUNCIATOR_AUTO"
    DISPLAY_ANNUNCIATOR_EDIT = "display.ANNUNCIATOR_EDIT"
    DISPLAY_ANNUNCIATOR_ERROR = "display.ANNUNCIATOR_ERROR"
    DISPLAY_ANNUNCIATOR_FILTER = "display.ANNUNCIATOR_FILTER"
    DISPLAY_ANNUNCIATOR_LISTEN = "display.ANNUNCIATOR_LISTEN"
    DISPLAY_ANNUNCIATOR_MATH = "display.ANNUNCIATOR_MATH"
    DISPLAY_ANNUNCIATOR_REAR = "display.ANNUNCIATOR_REAR"
    DISPLAY_ANNUNCIATOR_REL = "display.ANNUNCIATOR_REL"
    DISPLAY_ANNUNCIATOR_REMOTE = "display.ANNUNCIATOR_REMOTE"
    DISPLAY_ANNUNCIATOR_SAMPLE = "display.ANNUNCIATOR_SAMPLE"
    DISPLAY_ANNUNCIATOR_SRQ = "display.ANNUNCIATOR_SRQ"
    DISPLAY_ANNUNCIATOR_STAR = "display.ANNUNCIATOR_STAR"
    DISPLAY_ANNUNCIATOR_TALK = "display.ANNUNCIATOR_TALK"
    DISPLAY_ANNUNCIATOR_TRIGGER = "display.ANNUNCIATOR_TRIGGER"
    DISPLAY_DIGITS_4_5 = "display.DIGITS_4_5"
    DISPLAY_DIGITS_5_5 = "display.DIGITS_5_5"
    DISPLAY_DIGITS_6_5 = "display.DIGITS_6_5"
    DISPLAY_DISABLE = "display.DISABLE"
    DISPLAY_DONT_SAVE = "display.DONT_SAVE"
    DISPLAY_ENABLE = "display.ENABLE"
    DISPLAY_KEY_AUTO = "display.KEY_AUTO"
    DISPLAY_KEY_CONFIG = "display.KEY_CONFIG"
    DISPLAY_KEY_DIGITSA = "display.KEY_DIGITSA"
    DISPLAY_KEY_DIGITSB = "display.KEY_DIGITSB"
    DISPLAY_KEY_DISPLAY = "display.KEY_DISPLAY"
    DISPLAY_KEY_ENTER = "display.KEY_ENTER"
    DISPLAY_KEY_EXIT = "display.KEY_EXIT"
    DISPLAY_KEY_FILTERA = "display.KEY_FILTERA"
    DISPLAY_KEY_FILTERB = "display.KEY_FILTERB"
    DISPLAY_KEY_LEFT = "display.KEY_LEFT"
    DISPLAY_KEY_LIMITA = "display.KEY_LIMITA"
    DISPLAY_KEY_LIMITB = "display.KEY_LIMITB"
    DISPLAY_KEY_LOAD = "display.KEY_LOAD"
    DISPLAY_KEY_MEASA = "display.KEY_MEASA"
    DISPLAY_KEY_MEASB = "display.KEY_MEASB"
    DISPLAY_KEY_MENU = "display.KEY_MENU"
    DISPLAY_KEY_MODEA = "display.KEY_MODEA"
    DISPLAY_KEY_MODEB = "display.KEY_MODEB"
    DISPLAY_KEY_NONE = "display.KEY_NONE"
    DISPLAY_KEY_OUTPUTA = "display.KEY_OUTPUTA"
    DISPLAY_KEY_OUTPUTB = "display.KEY_OUTPUTB"
    DISPLAY_KEY_RANGEDOWN = "display.KEY_RANGEDOWN"
    DISPLAY_KEY_RANGEUP = "display.KEY_RANGEUP"
    DISPLAY_KEY_RECALL = "display.KEY_RECALL"
    DISPLAY_KEY_RELA = "display.KEY_RELA"
    DISPLAY_KEY_RELB = "display.KEY_RELB"
    DISPLAY_KEY_RIGHT = "display.KEY_RIGHT"
    DISPLAY_KEY_RUN = "display.KEY_RUN"
    DISPLAY_KEY_SPEEDA = "display.KEY_SPEEDA"
    DISPLAY_KEY_SPEEDB = "display.KEY_SPEEDB"
    DISPLAY_KEY_SRCA = "display.KEY_SRCA"
    DISPLAY_KEY_SRCB = "display.KEY_SRCB"
    DISPLAY_KEY_STORE = "display.KEY_STORE"
    DISPLAY_KEY_TRIG = "display.KEY_TRIG"
    DISPLAY_LIMIT_IV = "display.LIMIT_IV"
    DISPLAY_LIMIT_P = "display.LIMIT_P"
    DISPLAY_LOCK = "display.LOCK"
    DISPLAY_MEASURE_DCAMPS = "display.MEASURE_DCAMPS"
    DISPLAY_MEASURE_DCVOLTS = "display.MEASURE_DCVOLTS"
    DISPLAY_MEASURE_OHMS = "display.MEASURE_OHMS"
    DISPLAY_MEASURE_WATTS = "display.MEASURE_WATTS"
    DISPLAY_SAVE = "display.SAVE"
    DISPLAY_SMUA = "display.SMUA"
    DISPLAY_SMUA_SMUB = "display.SMUA_SMUB"
    DISPLAY_SMUB = "display.SMUB"
    DISPLAY_TRIGGER_EVENT_ID = "display.trigger.EVENT_ID"
    DISPLAY_UNLOCK = "display.UNLOCK"
    DISPLAY_USER = "display.USER"
    DISPLAY_WHEEL_ENTER = "display.WHEEL_ENTER"
    DISPLAY_WHEEL_LEFT = "display.WHEEL_LEFT"
    DISPLAY_WHEEL_RIGHT = "display.WHEEL_RIGHT"
    EVENTLOG_DISABLE = "eventlog.DISABLE"
    EVENTLOG_DISCARD_NEWEST = "eventlog.DISCARD_NEWEST"
    EVENTLOG_DISCARD_OLDEST = "eventlog.DISCARD_OLDEST"
    EVENTLOG_ENABLE = "eventlog.ENABLE"
    FORMAT_ASCII = "format.ASCII"
    FORMAT_BIGENDIAN = "format.BIGENDIAN"
    FORMAT_DREAL = "format.DREAL"
    FORMAT_LITTLEENDIAN = "format.LITTLEENDIAN"
    FORMAT_NETWORK = "format.NETWORK"
    FORMAT_NORMAL = "format.NORMAL"
    FORMAT_REAL = "format.REAL"
    FORMAT_REAL32 = "format.REAL32"
    FORMAT_REAL64 = "format.REAL64"
    FORMAT_SREAL = "format.SREAL"
    FORMAT_SWAPPED = "format.SWAPPED"
    LAN_AUTO = "lan.AUTO"
    LAN_DISABLE = "lan.DISABLE"
    LAN_ENABLE = "lan.ENABLE"
    LAN_FULL = "lan.FULL"
    LAN_HALF = "lan.HALF"
    LAN_MANUAL = "lan.MANUAL"
    LAN_MULTICAST = "lan.MULTICAST"
    LAN_TCP = "lan.TCP"
    LAN_TRIGGER_N_EVENT_ID = "lan.trigger[N].EVENT_ID"
    LAN_TRIG_EITHER = "lan.TRIG_EITHER"
    LAN_TRIG_FALLING = "lan.TRIG_FALLING"
    LAN_TRIG_RISING = "lan.TRIG_RISING"
    LAN_TRIG_RISINGA = "lan.TRIG_RISINGA"
    LAN_TRIG_RISINGM = "lan.TRIG_RISINGM"
    LAN_TRIG_SYNCHRONOUS = "lan.TRIG_SYNCHRONOUS"
    LAN_TRIG_SYNCHRONOUSA = "lan.TRIG_SYNCHRONOUSA"
    LAN_TRIG_SYNCHRONOUSM = "lan.TRIG_SYNCHRONOUSM"
    LAN_UDP = "lan.UDP"
    LOCALNODE_PASSWORD_ALL = "localnode.PASSWORD_ALL"
    LOCALNODE_PASSWORD_LAN = "localnode.PASSWORD_LAN"
    LOCALNODE_PASSWORD_NONE = "localnode.PASSWORD_NONE"
    LOCALNODE_PASSWORD_WEB = "localnode.PASSWORD_WEB"
    SMUX_ASYNC = "smuX.ASYNC"
    SMUX_AUTORANGE_FOLLOW_LIMIT = "smuX.AUTORANGE_FOLLOW_LIMIT"
    SMUX_AUTORANGE_OFF = "smuX.AUTORANGE_OFF"
    SMUX_AUTORANGE_ON = "smuX.AUTORANGE_ON"
    SMUX_AUTOZERO_AUTO = "smuX.AUTOZERO_AUTO"
    SMUX_AUTOZERO_OFF = "smuX.AUTOZERO_OFF"
    SMUX_AUTOZERO_ONCE = "smuX.AUTOZERO_ONCE"
    SMUX_CALSET_DEFAULT = "smuX.CALSET_DEFAULT"
    SMUX_CALSET_FACTORY = "smuX.CALSET_FACTORY"
    SMUX_CALSET_NOMINAL = "smuX.CALSET_NOMINAL"
    SMUX_CALSET_PREVIOUS = "smuX.CALSET_PREVIOUS"
    SMUX_CALSTATE_CALIBRATING = "smuX.CALSTATE_CALIBRATING"
    SMUX_CALSTATE_LOCKED = "smuX.CALSTATE_LOCKED"
    SMUX_CALSTATE_UNLOCKED = "smuX.CALSTATE_UNLOCKED"
    SMUX_CAL_AUTO = "smuX.CAL_AUTO"
    SMUX_CAL_NEGATIVE = "smuX.CAL_NEGATIVE"
    SMUX_CAL_POSITIVE = "smuX.CAL_POSITIVE"
    SMUX_CONTACT_FAST = "smuX.CONTACT_FAST"
    SMUX_CONTACT_MEDIUM = "smuX.CONTACT_MEDIUM"
    SMUX_CONTACT_SLOW = "smuX.CONTACT_SLOW"
    SMUX_DELAY_AUTO = "smuX.DELAY_AUTO"
    SMUX_DELAY_OFF = "smuX.DELAY_OFF"
    SMUX_DISABLE = "smuX.DISABLE"
    SMUX_ENABLE = "smuX.ENABLE"
    SMUX_FILL_ONCE = "smuX.FILL_ONCE"
    SMUX_FILL_WINDOW = "smuX.FILL_WINDOW"
    SMUX_FILTER_MEDIAN = "smuX.FILTER_MEDIAN"
    SMUX_FILTER_MOVING_AVG = "smuX.FILTER_MOVING_AVG"
    SMUX_FILTER_OFF = "smuX.FILTER_OFF"
    SMUX_FILTER_ON = "smuX.FILTER_ON"
    SMUX_FILTER_REPEAT_AVG = "smuX.FILTER_REPEAT_AVG"
    SMUX_LIMIT_AUTO = "smuX.LIMIT_AUTO"
    SMUX_OE_NONE = "smuX.OE_NONE"
    SMUX_OE_OUTPUT_OFF = "smuX.OE_OUTPUT_OFF"
    SMUX_OUTPUT_DCAMPS = "smuX.OUTPUT_DCAMPS"
    SMUX_OUTPUT_DCVOLTS = "smuX.OUTPUT_DCVOLTS"
    SMUX_OUTPUT_HIGH_Z = "smuX.OUTPUT_HIGH_Z"
    SMUX_OUTPUT_NORMAL = "smuX.OUTPUT_NORMAL"
    SMUX_OUTPUT_OFF = "smuX.OUTPUT_OFF"
    SMUX_OUTPUT_ON = "smuX.OUTPUT_ON"
    SMUX_OUTPUT_ZERO = "smuX.OUTPUT_ZERO"
    SMUX_REL_OFF = "smuX.REL_OFF"
    SMUX_REL_ON = "smuX.REL_ON"
    SMUX_SENSE_CALA = "smuX.SENSE_CALA"
    SMUX_SENSE_LOCAL = "smuX.SENSE_LOCAL"
    SMUX_SENSE_REMOTE = "smuX.SENSE_REMOTE"
    SMUX_SETTLE_DIRECT_IRANGE = "smuX.SETTLE_DIRECT_IRANGE"
    SMUX_SETTLE_FAST_ALL = "smuX.SETTLE_FAST_ALL"
    SMUX_SETTLE_FAST_POLARITY = "smuX.SETTLE_FAST_POLARITY"
    SMUX_SETTLE_FAST_RANGE = "smuX.SETTLE_FAST_RANGE"
    SMUX_SETTLE_SMOOTH = "smuX.SETTLE_SMOOTH"
    SMUX_SOURCE_HOLD = "smuX.SOURCE_HOLD"
    SMUX_SOURCE_IDLE = "smuX.SOURCE_IDLE"
    SMUX_TRIGGER_ARMED_EVENT_ID = "smuX.trigger.ARMED_EVENT_ID"
    SMUX_TRIGGER_IDLE_EVENT_ID = "smuX.trigger.IDLE_EVENT_ID"
    SMUX_TRIGGER_MEASURE_COMPLETE_EVENT_ID = "smuX.trigger.MEASURE_COMPLETE_EVENT_ID"
    SMUX_TRIGGER_PULSE_COMPLETE_EVENT_ID = "smuX.trigger.PULSE_COMPLETE_EVENT_ID"
    SMUX_TRIGGER_SOURCE_COMPLETE_EVENT_ID = "smuX.trigger.SOURCE_COMPLETE_EVENT_ID"
    SMUX_TRIGGER_SWEEPING_EVENT_ID = "smuX.trigger.SWEEPING_EVENT_ID"
    SMUX_TRIGGER_SWEEP_COMPLETE_EVENT_ID = "smuX.trigger.SWEEP_COMPLETE_EVENT_ID"
    STATUS_EAV = "status.EAV"
    STATUS_ERROR_AVAILABLE = "status.ERROR_AVAILABLE"
    STATUS_ESB = "status.ESB"
    STATUS_EVENT_SUMMARY_BIT = "status.EVENT_SUMMARY_BIT"
    STATUS_MASTER_SUMMARY_STATUS = "status.MASTER_SUMMARY_STATUS"
    STATUS_MAV = "status.MAV"
    STATUS_MEASUREMENT_BAV = "status.measurement.BAV"
    STATUS_MEASUREMENT_BUFFER_AVAILABLE = "status.measurement.BUFFER_AVAILABLE"
    STATUS_MEASUREMENT_BUFFER_AVAILABLE_SMUA = "status.measurement.buffer_available.SMUA"
    STATUS_MEASUREMENT_BUFFER_AVAILABLE_SMUB = "status.measurement.buffer_available.SMUB"
    STATUS_MEASUREMENT_CURRENT_LIMIT = "status.measurement.CURRENT_LIMIT"
    STATUS_MEASUREMENT_CURRENT_LIMIT_SMUA = "status.measurement.current_limit.SMUA"
    STATUS_MEASUREMENT_CURRENT_LIMIT_SMUB = "status.measurement.current_limit.SMUB"
    STATUS_MEASUREMENT_ILMT = "status.measurement.ILMT"
    STATUS_MEASUREMENT_INST = "status.measurement.INST"
    STATUS_MEASUREMENT_INSTRUMENT_SMUA = "status.measurement.instrument.SMUA"
    STATUS_MEASUREMENT_INSTRUMENT_SMUB = "status.measurement.instrument.SMUB"
    STATUS_MEASUREMENT_INSTRUMENT_SMUX_BAV = "status.measurement.instrument.smuX.BAV"
    STATUS_MEASUREMENT_INSTRUMENT_SMUX_BUFFER_AVAILABLE = (
        "status.measurement.instrument.smuX.BUFFER_AVAILABLE"
    )
    STATUS_MEASUREMENT_INSTRUMENT_SMUX_CURRENT_LIMIT = (
        "status.measurement.instrument.smuX.CURRENT_LIMIT"
    )
    STATUS_MEASUREMENT_INSTRUMENT_SMUX_ILMT = "status.measurement.instrument.smuX.ILMT"
    STATUS_MEASUREMENT_INSTRUMENT_SMUX_READING_OVERFLOW = (
        "status.measurement.instrument.smuX.READING_OVERFLOW"
    )
    STATUS_MEASUREMENT_INSTRUMENT_SMUX_ROF = "status.measurement.instrument.smuX.ROF"
    STATUS_MEASUREMENT_INSTRUMENT_SMUX_VLMT = "status.measurement.instrument.smuX.VLMT"
    STATUS_MEASUREMENT_INSTRUMENT_SMUX_VOLTAGE_LIMIT = (
        "status.measurement.instrument.smuX.VOLTAGE_LIMIT"
    )
    STATUS_MEASUREMENT_INSTRUMENT_SUMMARY = "status.measurement.INSTRUMENT_SUMMARY"
    STATUS_MEASUREMENT_OE = "status.measurement.OE"
    STATUS_MEASUREMENT_OUTPUT_ENABLE = "status.measurement.OUTPUT_ENABLE"
    STATUS_MEASUREMENT_READING_OVERFLOW = "status.measurement.READING_OVERFLOW"
    STATUS_MEASUREMENT_READING_OVERFLOW_SMUA = "status.measurement.reading_overflow.SMUA"
    STATUS_MEASUREMENT_READING_OVERFLOW_SMUB = "status.measurement.reading_overflow.SMUB"
    STATUS_MEASUREMENT_ROF = "status.measurement.ROF"
    STATUS_MEASUREMENT_SUMMARY_BIT = "status.MEASUREMENT_SUMMARY_BIT"
    STATUS_MEASUREMENT_VLMT = "status.measurement.VLMT"
    STATUS_MEASUREMENT_VOLTAGE_LIMIT = "status.measurement.VOLTAGE_LIMIT"
    STATUS_MEASUREMENT_VOLTAGE_LIMIT_SMUA = "status.measurement.voltage_limit.SMUA"
    STATUS_MEASUREMENT_VOLTAGE_LIMIT_SMUB = "status.measurement.voltage_limit.SMUB"
    STATUS_MESSAGE_AVAILABLE = "status.MESSAGE_AVAILABLE"
    STATUS_MSB = "status.MSB"
    STATUS_MSS = "status.MSS"
    STATUS_OPERATION_CAL = "status.operation.CAL"
    STATUS_OPERATION_CALIBRATING = "status.operation.CALIBRATING"
    STATUS_OPERATION_CALIBRATING_SMUA = "status.operation.calibrating.SMUA"
    STATUS_OPERATION_CALIBRATING_SMUB = "status.operation.calibrating.SMUB"
    STATUS_OPERATION_INST = "status.operation.INST"
    STATUS_OPERATION_INSTRUMENT_DIGIO = "status.operation.instrument.DIGIO"
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRGOVR = "status.operation.instrument.digio.TRGOVR"
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN = (
        "status.operation.instrument.digio.TRIGGER_OVERRUN"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE1 = (
        "status.operation.instrument.digio.trigger_overrun.LINE1"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE10 = (
        "status.operation.instrument.digio.trigger_overrun.LINE10"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE11 = (
        "status.operation.instrument.digio.trigger_overrun.LINE11"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE12 = (
        "status.operation.instrument.digio.trigger_overrun.LINE12"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE13 = (
        "status.operation.instrument.digio.trigger_overrun.LINE13"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE14 = (
        "status.operation.instrument.digio.trigger_overrun.LINE14"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE2 = (
        "status.operation.instrument.digio.trigger_overrun.LINE2"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE3 = (
        "status.operation.instrument.digio.trigger_overrun.LINE3"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE4 = (
        "status.operation.instrument.digio.trigger_overrun.LINE4"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE5 = (
        "status.operation.instrument.digio.trigger_overrun.LINE5"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE6 = (
        "status.operation.instrument.digio.trigger_overrun.LINE6"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE7 = (
        "status.operation.instrument.digio.trigger_overrun.LINE7"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE8 = (
        "status.operation.instrument.digio.trigger_overrun.LINE8"
    )
    STATUS_OPERATION_INSTRUMENT_DIGIO_TRIGGER_OVERRUN_LINE9 = (
        "status.operation.instrument.digio.trigger_overrun.LINE9"
    )
    STATUS_OPERATION_INSTRUMENT_DIGITAL_IO = "status.operation.instrument.DIGITAL_IO"
    STATUS_OPERATION_INSTRUMENT_LAN = "status.operation.instrument.LAN"
    STATUS_OPERATION_INSTRUMENT_LAN_CON = "status.operation.instrument.lan.CON"
    STATUS_OPERATION_INSTRUMENT_LAN_CONF = "status.operation.instrument.lan.CONF"
    STATUS_OPERATION_INSTRUMENT_LAN_CONFIGURING = "status.operation.instrument.lan.CONFIGURING"
    STATUS_OPERATION_INSTRUMENT_LAN_CONNECTION = "status.operation.instrument.lan.CONNECTION"
    STATUS_OPERATION_INSTRUMENT_LAN_TRGOVR = "status.operation.instrument.lan.TRGOVR"
    STATUS_OPERATION_INSTRUMENT_LAN_TRIGGER_OVERRUN = (
        "status.operation.instrument.lan.TRIGGER_OVERRUN"
    )
    STATUS_OPERATION_INSTRUMENT_LAN_TRIGGER_OVERRUN_LAN1 = (
        "status.operation.instrument.lan.trigger_overrun.LAN1"
    )
    STATUS_OPERATION_INSTRUMENT_LAN_TRIGGER_OVERRUN_LAN2 = (
        "status.operation.instrument.lan.trigger_overrun.LAN2"
    )
    STATUS_OPERATION_INSTRUMENT_LAN_TRIGGER_OVERRUN_LAN3 = (
        "status.operation.instrument.lan.trigger_overrun.LAN3"
    )
    STATUS_OPERATION_INSTRUMENT_LAN_TRIGGER_OVERRUN_LAN4 = (
        "status.operation.instrument.lan.trigger_overrun.LAN4"
    )
    STATUS_OPERATION_INSTRUMENT_LAN_TRIGGER_OVERRUN_LAN5 = (
        "status.operation.instrument.lan.trigger_overrun.LAN5"
    )
    STATUS_OPERATION_INSTRUMENT_LAN_TRIGGER_OVERRUN_LAN6 = (
        "status.operation.instrument.lan.trigger_overrun.LAN6"
    )
    STATUS_OPERATION_INSTRUMENT_LAN_TRIGGER_OVERRUN_LAN7 = (
        "status.operation.instrument.lan.trigger_overrun.LAN7"
    )
    STATUS_OPERATION_INSTRUMENT_LAN_TRIGGER_OVERRUN_LAN8 = (
        "status.operation.instrument.lan.trigger_overrun.LAN8"
    )
    STATUS_OPERATION_INSTRUMENT_SMUA = "status.operation.instrument.SMUA"
    STATUS_OPERATION_INSTRUMENT_SMUB = "status.operation.instrument.SMUB"
    STATUS_OPERATION_INSTRUMENT_SMUX_CAL = "status.operation.instrument.smuX.CAL"
    STATUS_OPERATION_INSTRUMENT_SMUX_CALIBRATING = "status.operation.instrument.smuX.CALIBRATING"
    STATUS_OPERATION_INSTRUMENT_SMUX_MEAS = "status.operation.instrument.smuX.MEAS"
    STATUS_OPERATION_INSTRUMENT_SMUX_MEASURING = "status.operation.instrument.smuX.MEASURING"
    STATUS_OPERATION_INSTRUMENT_SMUX_SWE = "status.operation.instrument.smuX.SWE"
    STATUS_OPERATION_INSTRUMENT_SMUX_SWEEPING = "status.operation.instrument.smuX.SWEEPING"
    STATUS_OPERATION_INSTRUMENT_SMUX_TRGOVR = "status.operation.instrument.smuX.TRGOVR"
    STATUS_OPERATION_INSTRUMENT_SMUX_TRIGGER_OVERRUN = (
        "status.operation.instrument.smuX.TRIGGER_OVERRUN"
    )
    STATUS_OPERATION_INSTRUMENT_SMUX_TRIGGER_OVERRUN_ARM = (
        "status.operation.instrument.smuX.trigger_overrun.ARM"
    )
    STATUS_OPERATION_INSTRUMENT_SMUX_TRIGGER_OVERRUN_ENDP = (
        "status.operation.instrument.smuX.trigger_overrun.ENDP"
    )
    STATUS_OPERATION_INSTRUMENT_SMUX_TRIGGER_OVERRUN_MEAS = (
        "status.operation.instrument.smuX.trigger_overrun.MEAS"
    )
    STATUS_OPERATION_INSTRUMENT_SMUX_TRIGGER_OVERRUN_SRC = (
        "status.operation.instrument.smuX.trigger_overrun.SRC"
    )
    STATUS_OPERATION_INSTRUMENT_SUMMARY = "status.operation.INSTRUMENT_SUMMARY"
    STATUS_OPERATION_INSTRUMENT_TRGBLND = "status.operation.instrument.TRGBLND"
    STATUS_OPERATION_INSTRUMENT_TRGTMR = "status.operation.instrument.TRGTMR"
    STATUS_OPERATION_INSTRUMENT_TRIGGER_BLENDER = "status.operation.instrument.TRIGGER_BLENDER"
    STATUS_OPERATION_INSTRUMENT_TRIGGER_BLENDER_TRGOVR = (
        "status.operation.instrument.trigger_blender.TRGOVR"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_BLENDER_TRIGGER_OVERRUN = (
        "status.operation.instrument.trigger_blender.TRIGGER_OVERRUN"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_BLENDER_TRIGGER_OVERRUN_BLND1 = (
        "status.operation.instrument.trigger_blender.trigger_overrun.BLND1"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_BLENDER_TRIGGER_OVERRUN_BLND2 = (
        "status.operation.instrument.trigger_blender.trigger_overrun.BLND2"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_BLENDER_TRIGGER_OVERRUN_BLND3 = (
        "status.operation.instrument.trigger_blender.trigger_overrun.BLND3"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_BLENDER_TRIGGER_OVERRUN_BLND4 = (
        "status.operation.instrument.trigger_blender.trigger_overrun.BLND4"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_BLENDER_TRIGGER_OVERRUN_BLND5 = (
        "status.operation.instrument.trigger_blender.trigger_overrun.BLND5"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_BLENDER_TRIGGER_OVERRUN_BLND6 = (
        "status.operation.instrument.trigger_blender.trigger_overrun.BLND6"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_TIMER = "status.operation.instrument.TRIGGER_TIMER"
    STATUS_OPERATION_INSTRUMENT_TRIGGER_TIMER_TRGOVR = (
        "status.operation.instrument.trigger_timer.TRGOVR"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_TIMER_TRIGGER_OVERRUN = (
        "status.operation.instrument.trigger_timer.TRIGGER_OVERRUN"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_TIMER_TRIGGER_OVERRUN_TMR1 = (
        "status.operation.instrument.trigger_timer.trigger_overrun.TMR1"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_TIMER_TRIGGER_OVERRUN_TMR2 = (
        "status.operation.instrument.trigger_timer.trigger_overrun.TMR2"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_TIMER_TRIGGER_OVERRUN_TMR3 = (
        "status.operation.instrument.trigger_timer.trigger_overrun.TMR3"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_TIMER_TRIGGER_OVERRUN_TMR4 = (
        "status.operation.instrument.trigger_timer.trigger_overrun.TMR4"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_TIMER_TRIGGER_OVERRUN_TMR5 = (
        "status.operation.instrument.trigger_timer.trigger_overrun.TMR5"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_TIMER_TRIGGER_OVERRUN_TMR6 = (
        "status.operation.instrument.trigger_timer.trigger_overrun.TMR6"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_TIMER_TRIGGER_OVERRUN_TMR7 = (
        "status.operation.instrument.trigger_timer.trigger_overrun.TMR7"
    )
    STATUS_OPERATION_INSTRUMENT_TRIGGER_TIMER_TRIGGER_OVERRUN_TMR8 = (
        "status.operation.instrument.trigger_timer.trigger_overrun.TMR8"
    )
    STATUS_OPERATION_INSTRUMENT_TSPLINK = "status.operation.instrument.TSPLINK"
    STATUS_OPERATION_INSTRUMENT_TSPLINK_TRGOVR = "status.operation.instrument.tsplink.TRGOVR"
    STATUS_OPERATION_INSTRUMENT_TSPLINK_TRIGGER_OVERRUN = (
        "status.operation.instrument.tsplink.TRIGGER_OVERRUN"
    )
    STATUS_OPERATION_INSTRUMENT_TSPLINK_TRIGGER_OVERRUN_LINE1 = (
        "status.operation.instrument.tsplink.trigger_overrun.LINE1"
    )
    STATUS_OPERATION_INSTRUMENT_TSPLINK_TRIGGER_OVERRUN_LINE2 = (
        "status.operation.instrument.tsplink.trigger_overrun.LINE2"
    )
    STATUS_OPERATION_INSTRUMENT_TSPLINK_TRIGGER_OVERRUN_LINE3 = (
        "status.operation.instrument.tsplink.trigger_overrun.LINE3"
    )
    STATUS_OPERATION_MEAS = "status.operation.MEAS"
    STATUS_OPERATION_MEASURING = "status.operation.MEASURING"
    STATUS_OPERATION_MEASURING_SMUA = "status.operation.measuring.SMUA"
    STATUS_OPERATION_MEASURING_SMUB = "status.operation.measuring.SMUB"
    STATUS_OPERATION_PROG = "status.operation.PROG"
    STATUS_OPERATION_PROGRAM_RUNNING = "status.operation.PROGRAM_RUNNING"
    STATUS_OPERATION_REM = "status.operation.REM"
    STATUS_OPERATION_REMOTE_CAV = "status.operation.remote.CAV"
    STATUS_OPERATION_REMOTE_COMMAND_AVAILABLE = "status.operation.remote.COMMAND_AVAILABLE"
    STATUS_OPERATION_REMOTE_PRMPT = "status.operation.remote.PRMPT"
    STATUS_OPERATION_REMOTE_PROMPTS_ENABLED = "status.operation.remote.PROMPTS_ENABLED"
    STATUS_OPERATION_REMOTE_SUMMARY = "status.operation.REMOTE_SUMMARY"
    STATUS_OPERATION_SUMMARY_BIT = "status.OPERATION_SUMMARY_BIT"
    STATUS_OPERATION_SWE = "status.operation.SWE"
    STATUS_OPERATION_SWEEPING = "status.operation.SWEEPING"
    STATUS_OPERATION_SWEEPING_SMUA = "status.operation.sweeping.SMUA"
    STATUS_OPERATION_SWEEPING_SMUB = "status.operation.sweeping.SMUB"
    STATUS_OPERATION_TRGOVR = "status.operation.TRGOVR"
    STATUS_OPERATION_TRIGGER_OVERRUN = "status.operation.TRIGGER_OVERRUN"
    STATUS_OPERATION_TRIGGER_OVERRUN_DIGIO = "status.operation.trigger_overrun.DIGIO"
    STATUS_OPERATION_TRIGGER_OVERRUN_DIGITAL_IO = "status.operation.trigger_overrun.DIGITAL_IO"
    STATUS_OPERATION_TRIGGER_OVERRUN_LAN = "status.operation.trigger_overrun.LAN"
    STATUS_OPERATION_TRIGGER_OVERRUN_SMUA = "status.operation.trigger_overrun.SMUA"
    STATUS_OPERATION_TRIGGER_OVERRUN_SMUB = "status.operation.trigger_overrun.SMUB"
    STATUS_OPERATION_TRIGGER_OVERRUN_TRGBLND = "status.operation.trigger_overrun.TRGBLND"
    STATUS_OPERATION_TRIGGER_OVERRUN_TRGTMR = "status.operation.trigger_overrun.TRGTMR"
    STATUS_OPERATION_TRIGGER_OVERRUN_TRIGGER_BLENDER = (
        "status.operation.trigger_overrun.TRIGGER_BLENDER"
    )
    STATUS_OPERATION_TRIGGER_OVERRUN_TRIGGER_TIMER = (
        "status.operation.trigger_overrun.TRIGGER_TIMER"
    )
    STATUS_OPERATION_TRIGGER_OVERRUN_TSPLINK = "status.operation.trigger_overrun.TSPLINK"
    STATUS_OPERATION_USER = "status.operation.USER"
    STATUS_OPERATION_USER_BIT0 = "status.operation.user.BIT0"
    STATUS_OPERATION_USER_BIT1 = "status.operation.user.BIT1"
    STATUS_OPERATION_USER_BIT10 = "status.operation.user.BIT10"
    STATUS_OPERATION_USER_BIT11 = "status.operation.user.BIT11"
    STATUS_OPERATION_USER_BIT12 = "status.operation.user.BIT12"
    STATUS_OPERATION_USER_BIT13 = "status.operation.user.BIT13"
    STATUS_OPERATION_USER_BIT14 = "status.operation.user.BIT14"
    STATUS_OPERATION_USER_BIT2 = "status.operation.user.BIT2"
    STATUS_OPERATION_USER_BIT3 = "status.operation.user.BIT3"
    STATUS_OPERATION_USER_BIT4 = "status.operation.user.BIT4"
    STATUS_OPERATION_USER_BIT5 = "status.operation.user.BIT5"
    STATUS_OPERATION_USER_BIT6 = "status.operation.user.BIT6"
    STATUS_OPERATION_USER_BIT7 = "status.operation.user.BIT7"
    STATUS_OPERATION_USER_BIT8 = "status.operation.user.BIT8"
    STATUS_OPERATION_USER_BIT9 = "status.operation.user.BIT9"
    STATUS_OSB = "status.OSB"
    STATUS_QSB = "status.QSB"
    STATUS_QUESTIONABLE_CAL = "status.questionable.CAL"
    STATUS_QUESTIONABLE_CALIBRATION = "status.questionable.CALIBRATION"
    STATUS_QUESTIONABLE_CALIBRATION_SMUA = "status.questionable.calibration.SMUA"
    STATUS_QUESTIONABLE_CALIBRATION_SMUB = "status.questionable.calibration.SMUB"
    STATUS_QUESTIONABLE_INST = "status.questionable.INST"
    STATUS_QUESTIONABLE_INSTRUMENT_SMUA = "status.questionable.instrument.SMUA"
    STATUS_QUESTIONABLE_INSTRUMENT_SMUB = "status.questionable.instrument.SMUB"
    STATUS_QUESTIONABLE_INSTRUMENT_SMUX_CAL = "status.questionable.instrument.smuX.CAL"
    STATUS_QUESTIONABLE_INSTRUMENT_SMUX_CALIBRATION = (
        "status.questionable.instrument.smuX.CALIBRATION"
    )
    STATUS_QUESTIONABLE_INSTRUMENT_SMUX_OTEMP = "status.questionable.instrument.smuX.OTEMP"
    STATUS_QUESTIONABLE_INSTRUMENT_SMUX_OVER_TEMPERATURE = (
        "status.questionable.instrument.smuX.OVER_TEMPERATURE"
    )
    STATUS_QUESTIONABLE_INSTRUMENT_SMUX_UNSTABLE_OUTPUT = (
        "status.questionable.instrument.smuX.UNSTABLE_OUTPUT"
    )
    STATUS_QUESTIONABLE_INSTRUMENT_SMUX_UO = "status.questionable.instrument.smuX.UO"
    STATUS_QUESTIONABLE_INSTRUMENT_SUMMARY = "status.questionable.INSTRUMENT_SUMMARY"
    STATUS_QUESTIONABLE_OTEMP = "status.questionable.OTEMP"
    STATUS_QUESTIONABLE_OVER_TEMPERATURE = "status.questionable.OVER_TEMPERATURE"
    STATUS_QUESTIONABLE_OVER_TEMPERATURE_SMUA = "status.questionable.over_temperature.SMUA"
    STATUS_QUESTIONABLE_OVER_TEMPERATURE_SMUB = "status.questionable.over_temperature.SMUB"
    STATUS_QUESTIONABLE_SUMMARY_BIT = "status.QUESTIONABLE_SUMMARY_BIT"
    STATUS_QUESTIONABLE_UNSTABLE_OUTPUT = "status.questionable.UNSTABLE_OUTPUT"
    STATUS_QUESTIONABLE_UNSTABLE_OUTPUT_SMUA = "status.questionable.unstable_output.SMUA"
    STATUS_QUESTIONABLE_UNSTABLE_OUTPUT_SMUB = "status.questionable.unstable_output.SMUB"
    STATUS_QUESTIONABLE_UO = "status.questionable.UO"
    STATUS_SSB = "status.SSB"
    STATUS_STANDARD_CME = "status.standard.CME"
    STATUS_STANDARD_COMMAND_ERROR = "status.standard.COMMAND_ERROR"
    STATUS_STANDARD_DDE = "status.standard.DDE"
    STATUS_STANDARD_DEVICE_DEPENDENT_ERROR = "status.standard.DEVICE_DEPENDENT_ERROR"
    STATUS_STANDARD_EXE = "status.standard.EXE"
    STATUS_STANDARD_EXECUTION_ERROR = "status.standard.EXECUTION_ERROR"
    STATUS_STANDARD_OPC = "status.standard.OPC"
    STATUS_STANDARD_OPERATION_COMPLETE = "status.standard.OPERATION_COMPLETE"
    STATUS_STANDARD_PON = "status.standard.PON"
    STATUS_STANDARD_POWER_ON = "status.standard.POWER_ON"
    STATUS_STANDARD_QUERY_ERROR = "status.standard.QUERY_ERROR"
    STATUS_STANDARD_QYE = "status.standard.QYE"
    STATUS_STANDARD_URQ = "status.standard.URQ"
    STATUS_STANDARD_USER_REQUEST = "status.standard.USER_REQUEST"
    STATUS_SYSTEM2_EXT = "status.system2.EXT"
    STATUS_SYSTEM2_EXTENSION_BIT = "status.system2.EXTENSION_BIT"
    STATUS_SYSTEM2_NODE15 = "status.system2.NODE15"
    STATUS_SYSTEM2_NODE16 = "status.system2.NODE16"
    STATUS_SYSTEM2_NODE17 = "status.system2.NODE17"
    STATUS_SYSTEM2_NODE18 = "status.system2.NODE18"
    STATUS_SYSTEM2_NODE19 = "status.system2.NODE19"
    STATUS_SYSTEM2_NODE20 = "status.system2.NODE20"
    STATUS_SYSTEM2_NODE21 = "status.system2.NODE21"
    STATUS_SYSTEM2_NODE22 = "status.system2.NODE22"
    STATUS_SYSTEM2_NODE23 = "status.system2.NODE23"
    STATUS_SYSTEM2_NODE24 = "status.system2.NODE24"
    STATUS_SYSTEM2_NODE25 = "status.system2.NODE25"
    STATUS_SYSTEM2_NODE26 = "status.system2.NODE26"
    STATUS_SYSTEM2_NODE27 = "status.system2.NODE27"
    STATUS_SYSTEM2_NODE28 = "status.system2.NODE28"
    STATUS_SYSTEM3_EXT = "status.system3.EXT"
    STATUS_SYSTEM3_EXTENSION_BIT = "status.system3.EXTENSION_BIT"
    STATUS_SYSTEM3_NODE29 = "status.system3.NODE29"
    STATUS_SYSTEM3_NODE30 = "status.system3.NODE30"
    STATUS_SYSTEM3_NODE31 = "status.system3.NODE31"
    STATUS_SYSTEM3_NODE32 = "status.system3.NODE32"
    STATUS_SYSTEM3_NODE33 = "status.system3.NODE33"
    STATUS_SYSTEM3_NODE34 = "status.system3.NODE34"
    STATUS_SYSTEM3_NODE35 = "status.system3.NODE35"
    STATUS_SYSTEM3_NODE36 = "status.system3.NODE36"
    STATUS_SYSTEM3_NODE37 = "status.system3.NODE37"
    STATUS_SYSTEM3_NODE38 = "status.system3.NODE38"
    STATUS_SYSTEM3_NODE39 = "status.system3.NODE39"
    STATUS_SYSTEM3_NODE40 = "status.system3.NODE40"
    STATUS_SYSTEM3_NODE41 = "status.system3.NODE41"
    STATUS_SYSTEM3_NODE42 = "status.system3.NODE42"
    STATUS_SYSTEM4_EXT = "status.system4.EXT"
    STATUS_SYSTEM4_EXTENSION_BIT = "status.system4.EXTENSION_BIT"
    STATUS_SYSTEM4_NODE43 = "status.system4.NODE43"
    STATUS_SYSTEM4_NODE44 = "status.system4.NODE44"
    STATUS_SYSTEM4_NODE45 = "status.system4.NODE45"
    STATUS_SYSTEM4_NODE46 = "status.system4.NODE46"
    STATUS_SYSTEM4_NODE47 = "status.system4.NODE47"
    STATUS_SYSTEM4_NODE48 = "status.system4.NODE48"
    STATUS_SYSTEM4_NODE49 = "status.system4.NODE49"
    STATUS_SYSTEM4_NODE50 = "status.system4.NODE50"
    STATUS_SYSTEM4_NODE51 = "status.system4.NODE51"
    STATUS_SYSTEM4_NODE52 = "status.system4.NODE52"
    STATUS_SYSTEM4_NODE53 = "status.system4.NODE53"
    STATUS_SYSTEM4_NODE54 = "status.system4.NODE54"
    STATUS_SYSTEM4_NODE55 = "status.system4.NODE55"
    STATUS_SYSTEM4_NODE56 = "status.system4.NODE56"
    STATUS_SYSTEM5_NODE57 = "status.system5.NODE57"
    STATUS_SYSTEM5_NODE58 = "status.system5.NODE58"
    STATUS_SYSTEM5_NODE59 = "status.system5.NODE59"
    STATUS_SYSTEM5_NODE60 = "status.system5.NODE60"
    STATUS_SYSTEM5_NODE61 = "status.system5.NODE61"
    STATUS_SYSTEM5_NODE62 = "status.system5.NODE62"
    STATUS_SYSTEM5_NODE63 = "status.system5.NODE63"
    STATUS_SYSTEM5_NODE64 = "status.system5.NODE64"
    STATUS_SYSTEM_EXT = "status.system.EXT"
    STATUS_SYSTEM_EXTENSION_BIT = "status.system.EXTENSION_BIT"
    STATUS_SYSTEM_NODE1 = "status.system.NODE1"
    STATUS_SYSTEM_NODE10 = "status.system.NODE10"
    STATUS_SYSTEM_NODE11 = "status.system.NODE11"
    STATUS_SYSTEM_NODE12 = "status.system.NODE12"
    STATUS_SYSTEM_NODE13 = "status.system.NODE13"
    STATUS_SYSTEM_NODE14 = "status.system.NODE14"
    STATUS_SYSTEM_NODE2 = "status.system.NODE2"
    STATUS_SYSTEM_NODE3 = "status.system.NODE3"
    STATUS_SYSTEM_NODE4 = "status.system.NODE4"
    STATUS_SYSTEM_NODE5 = "status.system.NODE5"
    STATUS_SYSTEM_NODE6 = "status.system.NODE6"
    STATUS_SYSTEM_NODE7 = "status.system.NODE7"
    STATUS_SYSTEM_NODE8 = "status.system.NODE8"
    STATUS_SYSTEM_NODE9 = "status.system.NODE9"
    STATUS_SYSTEM_SUMMARY_BIT = "status.SYSTEM_SUMMARY_BIT"
    TRIGGER_BLENDER_N_EVENT_ID = "trigger.blender[N].EVENT_ID"
    TRIGGER_EVENT_ID = "trigger.EVENT_ID"
    TRIGGER_GENERATOR_N_EVENT_ID = "trigger.generator[N].EVENT_ID"
    TRIGGER_TIMER_N_EVENT_ID = "trigger.timer[N].EVENT_ID"
    TSPLINK_TRIGGER_N_EVENT_ID = "tsplink.trigger[N].EVENT_ID"
    TSPLINK_TRIG_BYPASS = "tsplink.TRIG_BYPASS"
    TSPLINK_TRIG_EITHER = "tsplink.TRIG_EITHER"
    TSPLINK_TRIG_FALLING = "tsplink.TRIG_FALLING"
    TSPLINK_TRIG_RISING = "tsplink.TRIG_RISING"
    TSPLINK_TRIG_RISINGA = "tsplink.TRIG_RISINGA"
    TSPLINK_TRIG_RISINGM = "tsplink.TRIG_RISINGM"
    TSPLINK_TRIG_SYNCHRONOUS = "tsplink.TRIG_SYNCHRONOUS"
    TSPLINK_TRIG_SYNCHRONOUSA = "tsplink.TRIG_SYNCHRONOUSA"
    TSPLINK_TRIG_SYNCHRONOUSM = "tsplink.TRIG_SYNCHRONOUSM"
    TSPNET_TERM_CR = "tspnet.TERM_CR"
    TSPNET_TERM_CRLF = "tspnet.TERM_CRLF"
    TSPNET_TERM_LF = "tspnet.TERM_LF"
    TSPNET_TERM_LFCR = "tspnet.TERM_LFCR"


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class SMU2606BCommands:
    """The SMU2606B commands.

    This provides access to all the commands for the SMU2606B device. See the documentation of each
    property for more usage information.

    Properties and methods:
        - ``.beeper``: The ``beeper`` command tree.
        - ``.bit``: The ``bit`` command tree.
        - ``.buffer_var``: The ``bufferVar`` command tree.
        - ``.config_pulse_i_measure_v()``: The ``ConfigPulseIMeasureV()`` function.
        - ``.config_pulse_i_measure_v_sweep_lin()``: The ``ConfigPulseIMeasureVSweepLin()``
          function.
        - ``.config_pulse_i_measure_v_sweep_log()``: The ``ConfigPulseIMeasureVSweepLog()``
          function.
        - ``.config_pulse_v_measure_i()``: The ``ConfigPulseVMeasureI()`` function.
        - ``.config_pulse_v_measure_i_sweep_lin()``: The ``ConfigPulseVMeasureISweepLin()``
          function.
        - ``.config_pulse_v_measure_i_sweep_log()``: The ``ConfigPulseVMeasureISweepLog()``
          function.
        - ``.dataqueue``: The ``dataqueue`` command tree.
        - ``.delay()``: The ``delay()`` function.
        - ``.digio``: The ``digio`` command tree.
        - ``.display``: The ``display`` command tree.
        - ``.errorqueue``: The ``errorqueue`` command tree.
        - ``.eventlog``: The ``eventlog`` command tree.
        - ``.exit()``: The ``exit()`` function.
        - ``.format``: The ``format`` command tree.
        - ``.fs``: The ``fs`` command tree.
        - ``.gettimezone()``: The ``gettimezone()`` function.
        - ``.gm_isweep()``: The ``gm_isweep()`` function.
        - ``.gm_vsweep()``: The ``gm_vsweep()`` function.
        - ``.i_leakage_measure()``: The ``i_leakage_measure()`` function.
        - ``.i_leakage_threshold()``: The ``i_leakage_threshold()`` function.
        - ``.initiate_pulse_test()``: The ``InitiatePulseTest()`` function.
        - ``.initiate_pulse_test_dual()``: The ``InitiatePulseTestDual()`` function.
        - ``.io``: The ``io`` command tree.
        - ``.lan``: The ``lan`` command tree.
        - ``.localnode``: The ``localnode`` command tree.
        - ``.makegetter()``: The ``makegetter()`` function.
        - ``.makesetter()``: The ``makesetter()`` function.
        - ``.meminfo()``: The ``meminfo()`` function.
        - ``.node``: The ``node[N]`` command tree.
        - ``.opc()``: The ``opc()`` function.
        - ``.os``: The ``os`` command tree.
        - ``.print()``: The ``print()`` function.
        - ``.printbuffer()``: The ``printbuffer()`` function.
        - ``.printnumber()``: The ``printnumber()`` function.
        - ``.pulse_i_measure_v()``: The ``PulseIMeasureV()`` function.
        - ``.pulse_v_measure_i()``: The ``PulseVMeasureI()`` function.
        - ``.query_pulse_config()``: The ``QueryPulseConfig()`` function.
        - ``.reset()``: The ``reset()`` function.
        - ``.savebuffer()``: The ``savebuffer()`` function.
        - ``.script_var``: The ``scriptVar`` command tree.
        - ``.script``: The ``script`` command tree.
        - ``.settime()``: The ``settime()`` function.
        - ``.settimezone()``: The ``settimezone()`` function.
        - ``.setup``: The ``setup`` command tree.
        - ``.smu``: The ``smuX`` command tree.
        - ``.status``: The ``status`` command tree.
        - ``.sweep_i_lin_measure_v()``: The ``SweepILinMeasureV()`` function.
        - ``.sweep_i_list_measure_v()``: The ``SweepIListMeasureV()`` function.
        - ``.sweep_i_log_measure_v()``: The ``SweepILogMeasureV()`` function.
        - ``.sweep_v_lin_measure_i()``: The ``SweepVLinMeasureI()`` function.
        - ``.sweep_v_list_measure_i()``: The ``SweepVListMeasureI()`` function.
        - ``.sweep_v_log_measure_i()``: The ``SweepVLogMeasureI()`` function.
        - ``.timer``: The ``timer`` command tree.
        - ``.trigger``: The ``trigger`` command tree.
        - ``.tsplink``: The ``tsplink`` command tree.
        - ``.tspnet``: The ``tspnet`` command tree.
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
        self._dataqueue = Dataqueue(device)
        self._digio = Digio(device)
        self._display = Display(device)
        self._errorqueue = Errorqueue(device)
        self._eventlog = Eventlog(device)
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
        self._setup = Setup(device)
        self._smu: Dict[str, SmuxItem] = DefaultDictPassKeyToFactory(
            lambda x: SmuxItem(device, f"smu{x}")
        )
        self._status = Status(device)
        self._timer = Timer(device)
        self._trigger = Trigger(device)
        self._tsplink = Tsplink(device)
        self._tspnet = Tspnet(device)
        self._userstring = Userstring(device)

    @property
    def beeper(self) -> Beeper:
        """Return the ``beeper`` command tree.

        Constants:
            - ``.OFF``: This command turns the beeper off.
            - ``.ON``: This command turns the beeper on.

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
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Sub-properties and sub-methods:
            - ``.appendmode``: The ``bufferVar.appendmode`` attribute.
            - ``.basetimestamp``: The ``bufferVar.basetimestamp`` attribute.
            - ``.cachemode``: The ``bufferVar.cachemode`` attribute.
            - ``.capacity``: The ``bufferVar.capacity`` attribute.
            - ``.clear()``: The ``bufferVar.clear()`` function.
            - ``.clearcache()``: The ``bufferVar.clearcache()`` function.
            - ``.collectsourcevalues``: The ``bufferVar.collectsourcevalues`` attribute.
            - ``.collecttimestamps``: The ``bufferVar.collecttimestamps`` attribute.
            - ``.fillcount``: The ``bufferVar.fillcount`` attribute.
            - ``.fillmode``: The ``bufferVar.fillmode`` attribute.
            - ``.measurefunctions``: The ``bufferVar.measurefunctions[N]`` attribute.
            - ``.measureranges``: The ``bufferVar.measureranges[N]`` attribute.
            - ``.n``: The ``bufferVar.n`` attribute.
            - ``.readings``: The ``bufferVar.readings[N]`` attribute.
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

        Constants:
            - ``.TRIG_BYPASS``: Sets the mode in which the trigger event detector and the output
              trigger generator operate on the specified trigger line to allow direct control of the
              line.
            - ``.TRIG_EITHER``: Sets the mode in which the trigger event detector and the output
              trigger generator operate on the specified trigger line to detect rising- or
              falling-edge triggers as input and assert a TTL-low pulse for output.
            - ``.TRIG_FALLING``: Sets the mode in which the trigger event detector and the output
              trigger generator operate on the specified trigger line to detect falling-edge
              triggers as input and assert a TTL-low pulse for output.
            - ``.TRIG_RISING``: Sets the mode in which the trigger event detector and the output
              trigger generator operate on the specified trigger line so that if the programmed
              state of the line is high, the digio.TRIG_RISING mode behavior is similar to
              digio.TRIG_RISINGA. If the programmed state of the line is low, the digio.TRIG_RISING
              mode behavior is similar to digio.TRIG_RISINGM. Only use this setting if necessary for
              compatibility with other Keithley Instruments products.
            - ``.TRIG_RISINGA``: Sets the mode in which the trigger event detector and the output
              trigger generator operate on the specified trigger line to detect rising-edge triggers
              as input and assert a TTL-low pulse for output.
            - ``.TRIG_RISINGM``: Sets the mode in which the trigger event detector and the output
              trigger generator operate on the specified trigger line to assert a TTL-high pulse for
              output. Input edge detection is not possible in this mode.
            - ``.TRIG_SYNCHRONOUS``: Sets the mode in which the trigger event detector and the
              output trigger generator operate on the specified trigger line to detect the
              falling-edge input triggers and automatically latch and drive the trigger line low.
              Asserts a TTL-low pulse as an output trigger.
            - ``.TRIG_SYNCHRONOUSA``: Sets the mode in which the trigger event detector and the
              output trigger generator operate on the specified trigger line to detect the
              falling-edge input triggers and automatically latch and drive the trigger line low.
              Asserting the output trigger releases the latched line.
            - ``.TRIG_SYNCHRONOUSM``: Sets the mode in which the trigger event detector and the
              output trigger generator operate on the specified trigger line to detect rising-edge
              triggers as input and assert a TTL-low pulse for output.

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

        Constants:
            - ``.ANNUNCIATOR_4_WIRE``: 4W indicator on.
            - ``.ANNUNCIATOR_ARM``: ARM indicator on.
            - ``.ANNUNCIATOR_AUTO``: AUTO indicator on.
            - ``.ANNUNCIATOR_EDIT``: EDIT indicator on.
            - ``.ANNUNCIATOR_ERROR``: ERR indicator on.
            - ``.ANNUNCIATOR_FILTER``: FILT indicator on.
            - ``.ANNUNCIATOR_LISTEN``: LSTN indicator on.
            - ``.ANNUNCIATOR_MATH``: MATH indicator on.
            - ``.ANNUNCIATOR_REAR``: REAR indicator on.
            - ``.ANNUNCIATOR_REL``: REL indicator on.
            - ``.ANNUNCIATOR_REMOTE``: REM indicator on.
            - ``.ANNUNCIATOR_SAMPLE``: SMPL indicator on.
            - ``.ANNUNCIATOR_SRQ``: SRQ indicator on.
            - ``.ANNUNCIATOR_STAR``: * (asterisk) indicator on.
            - ``.ANNUNCIATOR_TALK``: TALK indicator on.
            - ``.ANNUNCIATOR_TRIGGER``: TRIG indicator on.
            - ``.DIGITS_4_5``: Set the front-panel display resolution to 4.5 digits.
            - ``.DIGITS_5_5``: Set the front-panel display resolution to 5.5 digits.
            - ``.DIGITS_6_5``: Set the front-panel display resolution to 6.5 digits.
            - ``.DISABLE``: Disable the front-panel keys for numeric entry when entering a value.
            - ``.DONT_SAVE``: Do not save code to nonvolatile memory.
            - ``.ENABLE``: Enable the front-panel keys for numeric entry when entering a value.
            - ``.KEY_AUTO``: Represents the range AUTO key.
            - ``.KEY_CONFIG``: Represents the CONFIG key.
            - ``.KEY_DIGITSA``: Represents the DIGITS (display resolution) key.
              For two-channel products, this is the DIGITS key for Channel A.
            - ``.KEY_DIGITSB``: Represents the DIGITS (display resolution) key for Channel B.
            - ``.KEY_DISPLAY``: Represents the DISPLAY key.
            - ``.KEY_ENTER``: Represents the ENTER key.
            - ``.KEY_EXIT``: Represents the EXIT key.
            - ``.KEY_FILTERA``: Represents the FILTER key.
              For two-channel products, this is the FILTER key for Channel A.
            - ``.KEY_FILTERB``: Represents the FILTER key for Channel B.
            - ``.KEY_LEFT``: Represents the left CURSOR key.
            - ``.KEY_LIMITA``: Represents the LIMIT key.
              For two-channel products, this is the LIMIT key for Channel A.
            - ``.KEY_LIMITB``: Represents the LIMIT key.
              For two-channel products, this is the LIMIT key for Channel B.
            - ``.KEY_LOAD``: Represents the LOAD (load test) key.
            - ``.KEY_MEASA``: Represents the MEAS (Measure) key.
              For two-channel products, this is the MEAS key for Channel A.
            - ``.KEY_MEASB``: Represents the MEAS (Measure) key for Channel B.
            - ``.KEY_MENU``: Represents the MENU key.
            - ``.KEY_MODEA``: Represents the MODE (meter mode) key
              For two-channel products, this is the MODE key for Channel A.
            - ``.KEY_MODEB``: Represents the MODE (meter mode) key for Channel B.
            - ``.KEY_NONE``: No key was pressed.
            - ``.KEY_OUTPUTA``: Represents the OUTPUT ON/OFF key.
              For two-channel products, this is the OUTPUT ON/OFF key for Channel A.
            - ``.KEY_OUTPUTB``: Represents the OUTPUT ON/OFF key.
              For two-channel products, this is the OUTPUT ON/OFF key for Channel B.
            - ``.KEY_RANGEDOWN``: Represents the RANGE down key.
            - ``.KEY_RANGEUP``: Represents the RANGE up key.
            - ``.KEY_RECALL``: Represents the RECALL key.
            - ``.KEY_RELA``: Represents the REL key.
              For two-channel products, this is the REL key for Channel A.
            - ``.KEY_RELB``: Represents the REL key for Channel B.
            - ``.KEY_RIGHT``: Represents the right CURSOR key.
            - ``.KEY_RUN``: Represents the RUN key.
            - ``.KEY_SPEEDA``: Represents the SPEED key.
              For two-channel products, this is the SPEED key for Channel A.
            - ``.KEY_SPEEDB``: Represents the SPEED key.
              For two-channel products, this is the SPEED key for Channel B.
            - ``.KEY_SRCA``: Represents the SRC (Source) key.
              For two-channel products, this is the SRC key for Channel A.
            - ``.KEY_SRCB``: Represents the SRC (Source) key for Channel B.
            - ``.KEY_STORE``: Represents the STORE key.
            - ``.KEY_TRIG``: Represents the TRIG key.
            - ``.LIMIT_IV``: Display the primary limit value.
            - ``.LIMIT_P``: Display the power limit value.
            - ``.LOCK``: Unlock the EXIT (LOCAL) key.
            - ``.MEASURE_DCAMPS``: Display the current measurement function.
            - ``.MEASURE_DCVOLTS``: Display the voltage measurement function.
            - ``.MEASURE_OHMS``: Display the resistance measurement function.
            - ``.MEASURE_WATTS``: Display the power measurement function.
            - ``.SAVE``: Save code to nonvolatile memory.
            - ``.SMUA``: Displays source-measure and compliance screen for SMU A.
            - ``.SMUA_SMUB``: Displays source-measure screen for SMU A and SMU B.
            - ``.SMUB``: Displays source-measure and compliance screen for SMU B.
            - ``.UNLOCK``: Lock out the EXIT (LOCAL) key.
            - ``.USER``: Displays the user screen.
            - ``.WHEEL_ENTER``: Represents pressing the navigation wheel.
            - ``.WHEEL_LEFT``: Represents turning the Navigation wheel left.
            - ``.WHEEL_RIGHT``: Represents turning the Navigation wheel right.

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
            - ``.numpad``: The ``display.numpad`` attribute.
            - ``.prompt()``: The ``display.prompt()`` function.
            - ``.screen``: The ``display.screen`` attribute.
            - ``.sendkey()``: The ``display.sendkey()`` function.
            - ``.setcursor()``: The ``display.setcursor()`` function.
            - ``.settext()``: The ``display.settext()`` function.
            - ``.smu``: The ``display.smuX`` command tree.
            - ``.trigger``: The ``display.trigger`` command tree.
            - ``.waitkey()``: The ``display.waitkey()`` function.
        """
        return self._display

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

        Constants:
            - ``.DISABLE``: Disable the event log.
            - ``.DISCARD_NEWEST``: Do not log new entries.
            - ``.DISCARD_OLDEST``: Delete old entries are deleted as new events are logged.
            - ``.ENABLE``: Enable the event log.

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

        Constants:
            - ``.ASCII``: Sets the data format for data that is printed using the printnumber() and
              printbuffer() functions to be ASCII format.
            - ``.BIGENDIAN``: Sets the binary byte order for the data that is printed using the
              printnumber() and
              printbuffer() functions to be most significant byte first.
            - ``.DREAL``: Sets the data format for data that is printed using the printnumber() and
              printbuffer() functions to be double-precision IEEE Std 754 binary format.
            - ``.LITTLEENDIAN``: Sets the binary byte order for the data that is printed using the
              printnumber() and
              printbuffer() functions to be least significant byte first.
            - ``.NETWORK``: Sets the binary byte order for the data that is printed using the
              printnumber() and
              printbuffer() functions to be most significant byte first.
            - ``.NORMAL``: Sets the binary byte order for the data that is printed using the
              printnumber() and
              printbuffer() functions to be most significant byte first.
            - ``.REAL``: Sets the data format for data that is printed using the printnumber() and
              printbuffer() functions to be double-precision IEEE Std 754 binary format.
            - ``.REAL32``: Sets the data format for data that is printed using the printnumber() and
              printbuffer() functions to be single-precision IEEE Std 754 binary format.
            - ``.REAL64``: Sets the data format for data that is printed using the printnumber() and
              printbuffer() functions to be double-precision IEEE Std 754 binary format.
            - ``.SREAL``: Sets the data format for data that is printed using the printnumber() and
              printbuffer() functions to be single-precision IEEE Std 754 binary format.
            - ``.SWAPPED``: Sets the binary byte order for the data that is printed using the
              printnumber() and
              printbuffer() functions to be least significant byte first.

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

        Constants:
            - ``.AUTO``: Selects automatic sequencing of configuration.
            - ``.DISABLE``: Disables automatic link reconnection and monitoring.
            - ``.ENABLE``: Enables automatic link reconnection and monitoring.
            - ``.FULL``: Full-duplex operation.
            - ``.HALF``: Half-duplex operation.
            - ``.MANUAL``: Use only manually specified configuration settings.
            - ``.MULTICAST``: Sets the LAN protocol to use for sending trigger messages to
              multicast.
            - ``.TCP``: Use TCP protocol.
            - ``.TRIG_EITHER``: Sets the trigger operation and detection mode of the specified LAN
              event to rising or falling edge (positive or negative state).
            - ``.TRIG_FALLING``: Sets the trigger operation and detection mode of the specified LAN
              event to falling edge (negative state).
            - ``.TRIG_RISING``: Sets the trigger operation and detection mode of the specified LAN
              event to rising edge (positive state).
            - ``.TRIG_RISINGA``: Sets the trigger operation and detection mode of the specified LAN
              event to rising edge (positive state).
            - ``.TRIG_RISINGM``: Sets the trigger operation and detection mode of the specified LAN
              event to rising edge (positive state).
            - ``.TRIG_SYNCHRONOUS``: Use for compatibility with older instruments; sets the trigger
              operation and detection mode of the specified LAN event to falling edge (negative
              state).
            - ``.TRIG_SYNCHRONOUSA``: Sets the trigger operation and detection mode of the specified
              LAN event to falling edge (negative state).
            - ``.TRIG_SYNCHRONOUSM``: Sets the trigger operation and detection mode of the specified
              LAN event to rising edge (positive state).
            - ``.UDP``: Use UDP protocol.

        Sub-properties and sub-methods:
            - ``.applysettings()``: The ``lan.applysettings()`` function.
            - ``.autoconnect``: The ``lan.autoconnect`` attribute.
            - ``.config``: The ``lan.config`` command tree.
            - ``.linktimeout``: The ``lan.linktimeout`` attribute.
            - ``.lxidomain``: The ``lan.lxidomain`` attribute.
            - ``.nagle``: The ``lan.nagle`` attribute.
            - ``.reset()``: The ``lan.reset()`` function.
            - ``.restoredefaults()``: The ``lan.restoredefaults()`` function.
            - ``.status``: The ``lan.status`` command tree.
            - ``.timedwait``: The ``lan.timedwait`` attribute.
            - ``.trigger``: The ``lan.trigger[N]`` command tree.
        """
        return self._lan

    @property
    def localnode(self) -> Localnode:
        """Return the ``localnode`` command tree.

        Constants:
            - ``.PASSWORD_ALL``: Use passwords on the web interface and all remote command
              interfaces.
            - ``.PASSWORD_LAN``: Use passwords on the web interface and all LAN interfaces.
            - ``.PASSWORD_NONE``: Disable passwords everywhere.
            - ``.PASSWORD_WEB``: Use passwords on the web interface only.

        Sub-properties and sub-methods:
            - ``.autolinefreq``: The ``localnode.autolinefreq`` attribute.
            - ``.description``: The ``localnode.description`` attribute.
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
    def node(self) -> Dict[int, NodeItem]:
        """Return the ``node[N]`` command tree.

        Info:
            - ``N``, the node number of this instrument.

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
            - ``.remove()``: The ``os.remove()`` function.
            - ``.rename()``: The ``os.rename()`` function.
            - ``.time()``: The ``os.time()`` function.
        """
        return self._os

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
    def smu(self) -> Dict[str, SmuxItem]:
        """Return the ``smuX`` command tree.

        Constants:
            - ``.ASYNC``: Make measurements during the sweep, but asynchronously with the source
              area of the trigger model.
            - ``.AUTORANGE_FOLLOW_LIMIT``: Set the measure range to the limit range.
            - ``.AUTORANGE_OFF``: Disable autorange.
            - ``.AUTORANGE_ON``: Enable autorange.
            - ``.AUTOZERO_AUTO``: Automatically check reference and zero measurements and perform an
              autozero when needed.
            - ``.AUTOZERO_OFF``: Disable autozero.
            - ``.AUTOZERO_ONCE``: Performs autozero once, then disables autozero.
            - ``.CALSET_DEFAULT``: Load normal calibration constants.
            - ``.CALSET_FACTORY``: Load calibration constants when the instrument left the factory.
            - ``.CALSET_NOMINAL``: Load calibration constants that are uncalibrated, but set to
              nominal values to allow rudimentary functioning of the instrument.
            - ``.CALSET_PREVIOUS``: Load the calibration constants that were used before the last
              default set was overwritten.
            - ``.CALSTATE_CALIBRATING``: Calibration constants or dates have been changed but not
              yet saved to nonvolatile memory.
            - ``.CALSTATE_LOCKED``: Calibration is locked.
            - ``.CALSTATE_UNLOCKED``: Calibration is unlocked but none of the calibration constants
              or dates have changed since the last save/restore.
            - ``.CAL_AUTO``: Use automatic polarity detection for calibration constants.
            - ``.CAL_NEGATIVE``: Measure with negative polarity calibration constants.
            - ``.CAL_POSITIVE``: Measure with positive polarity calibration constants.
            - ``.CONTACT_FAST``: Select the fast speed setting.
            - ``.CONTACT_MEDIUM``: Select the medium speed setting.
            - ``.CONTACT_SLOW``: Select the slow speed setting.
            - ``.DELAY_AUTO``: Use the automatic delay value.
            - ``.DELAY_OFF``: Do not include a delay before measurements.
            - ``.DISABLE``: Use conventional pulsing and full source-measure unit (SMU)
              functionality.
            - ``.ENABLE``: Allow fast-edge pulsing using the trigger model.
            - ``.FILL_ONCE``: Set the reading buffer fill mode to not overwrite old data.
            - ``.FILL_WINDOW``: Set the reading buffer fill mode to restart new readings at index 1
              after acquiring
              reading at index bufferVar.fillcount.
            - ``.FILTER_MEDIAN``: Selects the median filter when measurement filter is enabled.
            - ``.FILTER_MOVING_AVG``: Selects the moving filter when measurement filter is enabled.
            - ``.FILTER_OFF``: Disable filter measurements.
            - ``.FILTER_ON``: Enable filter measurements.
            - ``.FILTER_REPEAT_AVG``: Selects the repeating filter when measurement filter is
              enabled.
            - ``.LIMIT_AUTO``: Set the sweep source limit to automatic.
            - ``.OE_NONE``: When output enable is deasserted, take no action.
            - ``.OE_OUTPUT_OFF``: When output enable is deasserted, turn the source output off.
            - ``.OUTPUT_DCAMPS``: Select the current function for the pulse.
            - ``.OUTPUT_DCVOLTS``: Select the voltage function for the pulse.
            - ``.OUTPUT_HIGH_Z``: Opens the output relay when the output is turned off.
            - ``.OUTPUT_NORMAL``: Configures the source function according to smuX.source.offfunc
              attribute.
            - ``.OUTPUT_OFF``: Turns off the source output.
            - ``.OUTPUT_ON``: Turn on the source output.
            - ``.OUTPUT_ZERO``: Configures source to output 0 V as smuX.OUTPUT_NORMAL with different
              compliance handling.
            - ``.REL_OFF``: Disables relative measurements.
            - ``.REL_ON``: Enables relative measurements.
            - ``.SENSE_CALA``: Set the sense mode to calibration.
            - ``.SENSE_LOCAL``: Set the sense mode to local sense (2-wire).
            - ``.SENSE_REMOTE``: Set the sense mode to remote sense (4-wire).
            - ``.SETTLE_DIRECT_IRANGE``: Instructs the SMU to change the current range directly.
            - ``.SETTLE_FAST_ALL``: Enable the smuX.SETTLE_FAST_RANGE and smuX.SETTLE_FASTPOLARITY
              operations.
            - ``.SETTLE_FAST_POLARITY``: Instructs the SMU to change polarity without going to zero.
            - ``.SETTLE_FAST_RANGE``: Instructs the source-measure unit (SMU) to use a faster
              procedure when changing ranges.
            - ``.SETTLE_SMOOTH``: Turn off additional settling operations.
            - ``.SOURCE_HOLD``: Disables pulse mode sweeps, holding the source level for the
              remainder of the step.
            - ``.SOURCE_IDLE``: Sets the source level to the programmed (idle) level at the end of
              the pulse.

        Sub-properties and sub-methods:
            - ``.abort()``: The ``smuX.abort()`` function.
            - ``.buffer``: The ``smuX.buffer`` command tree.
            - ``.cal``: The ``smuX.cal`` command tree.
            - ``.contact``: The ``smuX.contact`` command tree.
            - ``.makebuffer()``: The ``smuX.makebuffer()`` function.
            - ``.measure``: The ``smuX.measure`` command tree.
            - ``.measureiandstep()``: The ``smuX.measureiandstep()`` function.
            - ``.measureivandstep()``: The ``smuX.measureivandstep()`` function.
            - ``.measurepandstep()``: The ``smuX.measurepandstep()`` function.
            - ``.measurerandstep()``: The ``smuX.measurerandstep()`` function.
            - ``.measurevandstep()``: The ``smuX.measurevandstep()`` function.
            - ``.nvbuffer1``: The ``smuX.nvbuffer1`` attribute.
            - ``.nvbuffer2``: The ``smuX.nvbuffer2`` attribute.
            - ``.reset()``: The ``smuX.reset()`` function.
            - ``.savebuffer()``: The ``smuX.savebuffer()`` function.
            - ``.sense``: The ``smuX.sense`` attribute.
            - ``.source``: The ``smuX.source`` command tree.
            - ``.trigger``: The ``smuX.trigger`` command tree.
        """
        return self._smu

    @property
    def status(self) -> Status:
        """Return the ``status`` command tree.

        Constants:
            - ``.EAV``: B2. Set summary bit indicates that an error or status message is present in
              the Error Queue.
            - ``.ERROR_AVAILABLE``: B2. Set summary bit indicates that an error or status message is
              present in the Error Queue.
            - ``.ESB``: B5. Set summary bit indicates that an enabled standard event has occurred.
            - ``.EVENT_SUMMARY_BIT``: B5. Set summary bit indicates that an enabled standard event
              has occurred.
            - ``.MASTER_SUMMARY_STATUS``: B6. Request Service (RQS)/Master Summary Status (MSS).
              Depending on how it is used, bit B6 of the status byte register is either the Request
              for Service (RQS) bit or the Master Summary Status (MSS) bit.
            - ``.MAV``: B4. Set summary bit indicates that a response message is present in the
              Output Queue.
            - ``.MEASUREMENT_SUMMARY_BIT``: B0. Set summary bit indicates that an enabled
              measurement event has occurred.
            - ``.MESSAGE_AVAILABLE``: B4. Set summary bit indicates that a response message is
              present in the Output Queue.
            - ``.MSB``: B0. Set summary bit indicates that an enabled measurement event has
              occurred.
            - ``.MSS``: An enabled summary bit of the status byte register is set.
            - ``.OPERATION_SUMMARY_BIT``: B7. Set summary bit indicates that an enabled operation
              event has occurred.
            - ``.OSB``: B7. Set summary bit indicates that an enabled operation event has occurred.
            - ``.QSB``: B3. Set summary bit indicates that an enabled questionable event has
              occurred.
            - ``.QUESTIONABLE_SUMMARY_BIT``: B3. Set summary bit indicates that an enabled
              questionable event has occurred.
            - ``.SSB``: B1. Set summary bit indicates that an enabled system event has occurred.
            - ``.SYSTEM_SUMMARY_BIT``: B1. Set summary bit indicates that an enabled system event
              has occurred.

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
            - ``.generator``: The ``trigger.generator[N]`` command tree.
            - ``.timer``: The ``trigger.timer[N]`` command tree.
            - ``.wait()``: The ``trigger.wait()`` function.
        """
        return self._trigger

    @property
    def tsplink(self) -> Tsplink:
        """Return the ``tsplink`` command tree.

        Constants:
            - ``.TRIG_BYPASS``: Allows direct control of the line as a digital I/O line.
            - ``.TRIG_EITHER``: Detects rising-edge or falling-edge triggers as input. Asserts a
              TTL-low pulse for output.
            - ``.TRIG_FALLING``: Detects falling-edge triggers as input. Asserts a TTL-low pulse for
              output.
            - ``.TRIG_RISING``: If the programmed state of the line is high, the tsplink.TRIG_RISING
              mode behaves similarly to tsplink.TRIG_RISINGA.
              If the programmed state of the line is low, the tsplink.TRIG_RISING mode behaves similarly
              to tsplink.TRIG_RISINGM.
              Use tsplink.TRIG_RISINGA if the line is in the high output state.
              Use tsplink.TRIG_RISINGM if the line is in the low output state.
            - ``.TRIG_RISINGA``: Detects rising-edge triggers as input. Asserts a TTL-low pulse for
              output.
            - ``.TRIG_RISINGM``: Edge detection as an input is not available. Generates a TTL-high
              pulse as an output trigger.
            - ``.TRIG_SYNCHRONOUS``: Detects the falling-edge input triggers and automatically
              latches and drives the trigger line low. Asserts a TTL-low pulse as an output trigger.
            - ``.TRIG_SYNCHRONOUSA``: Detects the falling-edge input triggers and automatically
              latches and drives the trigger line low.
            - ``.TRIG_SYNCHRONOUSM``: Detects rising-edge triggers as an input. Asserts a TTL-low
              pulse for output.

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
        """  # noqa: E501
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
    def userstring(self) -> Userstring:
        """Return the ``userstring`` command tree.

        Sub-properties and sub-methods:
            - ``.add()``: The ``userstring.add()`` function.
            - ``.delete()``: The ``userstring.delete()`` function.
            - ``.get()``: The ``userstring.get()`` function.
        """
        return self._userstring

    # pylint: disable=too-many-arguments,too-many-locals
    def config_pulse_i_measure_v(
        self,
        smu: str,
        bias: float,
        level: float,
        limit: float,
        ton: float,
        toff: float,
        points: int,
        buffer: str,
        tag: int,
        sync_in: Optional[str] = None,
        sync_out: Optional[str] = None,
        sync_in_timeout: Optional[float] = None,
        sync_in_abort: Optional[str] = None,
    ) -> str:
        """Run the ``ConfigPulseIMeasureV()`` function.

        Description:
            - This KIPulse factory script function configures a current pulse train with a voltage
              measurement at each point.

        TSP Syntax:
            ```
            - ConfigPulseIMeasureV()
            ```

        Args:
            smu: Instrument channel (for example, smua refers to SMU channel A).
            bias: Bias level in amperes.
            level: Pulse level in amperes.
            limit: Voltage limit (for example, compliance) in volts.
            ton: Pulse on time in seconds.
            toff: Pulse off time in seconds.
            points: Number of pulse-measure cycles.
            buffer: Reading buffer where pulsed measurements are stored; if this is nil when the
                function is called, no measurements are made when the pulse train is initiated.
            tag: Numeric identifier to be assigned to the defined pulse train.
            sync_in (optional): Defines a digital I/O trigger input line; if programmed, the pulse
                train waits for a trigger input before executing each pulse.
            sync_out (optional): Defines a digital I/O trigger output line; if programmed, the pulse
                train generates a trigger output immediately before the start of ton.
            sync_in_timeout (optional): Specifies the length of time (in seconds) to wait for input
                trigger; default value is 10 s.
            sync_in_abort (optional): Specifies whether or not to abort the pulse if an input
                trigger is not received; if pulse aborts because of a missed trigger, a timer
                timeout message is returned; true or false.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    smu,
                    bias,
                    level,
                    limit,
                    ton,
                    toff,
                    points,
                    buffer,
                    tag,
                    sync_in,
                    sync_out,
                    sync_in_timeout,
                    sync_in_abort,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print(ConfigPulseIMeasureV({function_args}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``ConfigPulseIMeasureV()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    # pylint: disable=too-many-arguments,too-many-locals
    def config_pulse_i_measure_v_sweep_lin(
        self,
        smu: str,
        bias: float,
        start: float,
        stop: float,
        limit: float,
        ton: float,
        toff: float,
        points: int,
        buffer: str,
        tag: int,
        sync_in: Optional[str] = None,
        sync_out: Optional[str] = None,
        sync_in_timeout: Optional[float] = None,
        sync_in_abort: Optional[str] = None,
    ) -> str:
        """Run the ``ConfigPulseIMeasureVSweepLin()`` function.

        Description:
            - This KIPulse factory script function configures a linear pulsed current sweep with a
              voltage measurement at each point.

        TSP Syntax:
            ```
            - ConfigPulseIMeasureVSweepLin()
            ```

        Args:
            smu: Instrument channel (for example, smua refers to SMU channel A).
            bias: Bias level in amperes.
            start: Pulse sweep start level in amperes.
            stop: Pulse sweep stop level in amperes.
            limit: Voltage limit (for example, compliance) in volts.
            ton: Pulse on time in seconds.
            toff: Pulse off time in seconds.
            points: Number of pulse-measure cycles.
            buffer: Reading buffer where pulsed measurements are stored; if this is nil when the
                function is called, no measurements are made when the pulse train is initiated.
            tag: Numeric identifier to be assigned to the defined pulse train.
            sync_in (optional): Defines a digital I/O trigger input line; if programmed, the pulse
                train waits for a trigger input before executing each pulse.
            sync_out (optional): Defines a digital I/O trigger output line; if programmed, the pulse
                train generates a trigger output immediately before the start of ton.
            sync_in_timeout (optional): Specifies the length of time (in seconds) to wait for input
                trigger; default value is 10 s.
            sync_in_abort (optional): Specifies whether or not to abort pulse if input trigger is
                not received; if pulse aborts because of a missed trigger, a timer timeout message
                is returned; true or false.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    smu,
                    bias,
                    start,
                    stop,
                    limit,
                    ton,
                    toff,
                    points,
                    buffer,
                    tag,
                    sync_in,
                    sync_out,
                    sync_in_timeout,
                    sync_in_abort,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print(ConfigPulseIMeasureVSweepLin({function_args}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``ConfigPulseIMeasureVSweepLin()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    # pylint: disable=too-many-arguments,too-many-locals
    def config_pulse_i_measure_v_sweep_log(
        self,
        smu: str,
        bias: float,
        start: float,
        stop: float,
        limit: float,
        ton: float,
        toff: float,
        points: int,
        buffer: str,
        tag: int,
        sync_in: Optional[str] = None,
        sync_out: Optional[str] = None,
        sync_in_timeout: Optional[float] = None,
        sync_in_abort: Optional[str] = None,
    ) -> str:
        """Run the ``ConfigPulseIMeasureVSweepLog()`` function.

        Description:
            - This KIPulse factory script function configures a voltage pulse train with a current
              measurement at each point.

        TSP Syntax:
            ```
            - ConfigPulseIMeasureVSweepLog()
            ```

        Args:
            smu: Instrument channel (for example, smua refers to SMU channel A).
            bias: Bias level in amperes.
            start: Pulse sweep start level in amperes.
            stop: Pulse sweep stop level in amperes.
            limit: Voltage limit (for example, compliance) in volts.
            ton: Pulse on time in seconds.
            toff: Pulse off time in seconds.
            points: Number of pulse-measure cycles.
            buffer: Reading buffer where pulsed measurements are stored; if this is nil when the
                function is called, no measurements are made when the pulse train is initiated.
            tag: Numeric identifier to be assigned to the defined pulse train.
            sync_in (optional): Defines a digital I/O trigger input line; if programmed, the pulse
                train waits for a trigger input before executing each pulse.
            sync_out (optional): Defines a digital I/O trigger output line; if programmed, the pulse
                train generates a trigger output immediately before the start of ton.
            sync_in_timeout (optional): Specifies the length of time (in seconds) to wait for input
                trigger; default value is 10 s.
            sync_in_abort (optional): Specifies whether or not to abort pulse if input trigger is
                not received; if pulse aborts because of a missed trigger, a timer timeout message
                is returned; true or false.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    smu,
                    bias,
                    start,
                    stop,
                    limit,
                    ton,
                    toff,
                    points,
                    buffer,
                    tag,
                    sync_in,
                    sync_out,
                    sync_in_timeout,
                    sync_in_abort,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print(ConfigPulseIMeasureVSweepLog({function_args}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``ConfigPulseIMeasureVSweepLog()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    # pylint: disable=too-many-arguments,too-many-locals
    def config_pulse_v_measure_i(
        self,
        smu: str,
        bias: float,
        level: float,
        limit: float,
        ton: float,
        toff: float,
        points: int,
        buffer: str,
        tag: int,
        sync_in: Optional[str] = None,
        sync_out: Optional[str] = None,
        sync_in_timeout: Optional[float] = None,
        sync_in_abort: Optional[str] = None,
    ) -> str:
        """Run the ``ConfigPulseVMeasureI()`` function.

        Description:
            - This KIPulse factory script function configures a voltage pulse train with a current
              measurement at each point.

        TSP Syntax:
            ```
            - ConfigPulseVMeasureI()
            ```

        Args:
            smu: Instrument channel (for example, smua refers to SMU channel A).
            bias: Bias level in volts.
            level: Pulse level in volts.
            limit: Current limit (for example, compliance) in amperes.
            ton: Pulse on time in seconds.
            toff: Pulse off time in seconds.
            points: Number of pulse-measure cycles.
            buffer: Reading buffer where pulsed measurements are stored; if this is nil when the
                function is called, no measurements are made when the pulse train is initiated.
            tag: Numeric identifier to be assigned to the defined pulse train.
            sync_in (optional): Defines a digital I/O trigger input line; if programmed, the pulse
                train waits for a trigger input before executing each pulse.
            sync_out (optional): Defines a digital I/O trigger output line; if programmed, the pulse
                train generates a trigger output immediately before the start of ton.
            sync_in_timeout (optional): Specifies the length of time (in seconds) to wait for input
                trigger; default value is 10 s.
            sync_in_abort (optional): Specifies whether or not to abort pulse if input trigger is
                not received; if pulse aborts because of a missed trigger, a timer timeout message
                is returned; true or false.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    smu,
                    bias,
                    level,
                    limit,
                    ton,
                    toff,
                    points,
                    buffer,
                    tag,
                    sync_in,
                    sync_out,
                    sync_in_timeout,
                    sync_in_abort,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print(ConfigPulseVMeasureI({function_args}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``ConfigPulseVMeasureI()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    # pylint: disable=too-many-arguments,too-many-locals
    def config_pulse_v_measure_i_sweep_lin(
        self,
        smu: str,
        bias: float,
        start: float,
        stop: float,
        limit: float,
        ton: float,
        toff: float,
        points: int,
        buffer: str,
        tag: int,
        sync_in: Optional[str] = None,
        sync_out: Optional[str] = None,
        sync_in_timeout: Optional[float] = None,
        sync_in_abort: Optional[str] = None,
    ) -> str:
        """Run the ``ConfigPulseVMeasureISweepLin()`` function.

        Description:
            - This KIPulse factory script function configures a voltage pulse train with a current
              measurement at each point.

        TSP Syntax:
            ```
            - ConfigPulseVMeasureISweepLin()
            ```

        Args:
            smu: Instrument channel (for example, smua refers to SMU channel A).
            bias: Bias level in volts.
            start: Pulse sweep start level in volts.
            stop: Pulse sweep stop level in volts.
            limit: Current limit (for example, compliance) in amperes.
            ton: Pulse on time in seconds.
            toff: Pulse off time in seconds.
            points: Number of pulse-measure cycles.
            buffer: Reading buffer where pulsed measurements are stored; if this is nil when the
                function is called, no measurements are made when the pulse train is initiated.
            tag: Numeric identifier to be assigned to the defined pulse train.
            sync_in (optional): Defines a digital I/O trigger input line; if programmed, the pulse
                train waits for a trigger input before executing each pulse.
            sync_out (optional): Defines a digital I/O trigger output line; if programmed, the pulse
                train generates a trigger output immediately before the start of ton.
            sync_in_timeout (optional): Specifies the length of time (in seconds) to wait for input
                trigger; default value is 10 s.
            sync_in_abort (optional): Specifies whether or not to abort pulse if input trigger is
                not received; if pulse aborts because of a missed trigger, a timer timeout message
                is returned; true or false.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    smu,
                    bias,
                    start,
                    stop,
                    limit,
                    ton,
                    toff,
                    points,
                    buffer,
                    tag,
                    sync_in,
                    sync_out,
                    sync_in_timeout,
                    sync_in_abort,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print(ConfigPulseVMeasureISweepLin({function_args}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``ConfigPulseVMeasureISweepLin()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    # pylint: disable=too-many-arguments,too-many-locals
    def config_pulse_v_measure_i_sweep_log(
        self,
        smu: str,
        bias: float,
        start: float,
        stop: float,
        limit: float,
        ton: float,
        toff: float,
        points: int,
        buffer: str,
        tag: int,
        sync_in: Optional[str] = None,
        sync_out: Optional[str] = None,
        sync_in_timeout: Optional[float] = None,
        sync_in_abort: Optional[str] = None,
    ) -> str:
        """Run the ``ConfigPulseVMeasureISweepLog()`` function.

        Description:
            - This KIPulse factory script function configures a voltage pulse train with a current
              measurement at each point.

        TSP Syntax:
            ```
            - ConfigPulseVMeasureISweepLog()
            ```

        Args:
            smu: Instrument channel (for example, smua refers to SMU channel A).
            bias: Bias level in volts.
            start: Pulse sweep start level in volts.
            stop: Pulse sweep stop level in volts.
            limit: Current limit (for example, compliance) in amperes.
            ton: Pulse on time in seconds.
            toff: Pulse off time in seconds.
            points: Number of pulse-measure cycles.
            buffer: Reading buffer where pulsed measurements are stored; if this is nil when the
                function is called, no measurements are made when the pulse train is initiated.
            tag: Numeric identifier to be assigned to the defined pulse train.
            sync_in (optional): Defines a digital I/O trigger input line; if programmed, the pulse
                train waits for a trigger input before executing each pulse.
            sync_out (optional): Defines a digital I/O trigger output line; if programmed, the pulse
                train generates a trigger output immediately before the start of ton.
            sync_in_timeout (optional): Specifies the length of time (in seconds) to wait for input
                trigger; default value is 10 s.
            sync_in_abort (optional): Specifies whether or not to abort pulse if input trigger is
                not received; if pulse aborts because of a missed trigger, a timer timeout message
                is returned; true or false.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    smu,
                    bias,
                    start,
                    stop,
                    limit,
                    ton,
                    toff,
                    points,
                    buffer,
                    tag,
                    sync_in,
                    sync_out,
                    sync_in_timeout,
                    sync_in_abort,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print(ConfigPulseVMeasureISweepLog({function_args}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``ConfigPulseVMeasureISweepLog()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def initiate_pulse_test(self, tag: int) -> str:
        """Run the ``InitiatePulseTest()`` function.

        Description:
            - This KIPulse factory script function initiates the pulse configuration assigned to
              tag.

        TSP Syntax:
            ```
            - InitiatePulseTest()
            ```

        Args:
            tag: Numeric identifier of the pulse configuration to be initiated.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print(InitiatePulseTest({tag}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``InitiatePulseTest()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def initiate_pulse_test_dual(self, tag1: int, tag2: int) -> str:
        """Run the ``InitiatePulseTestDual()`` function.

        Description:
            - This KIPulse factory script function initiates the pulse configuration assigned tag1
              and tag2.

        TSP Syntax:
            ```
            - InitiatePulseTestDual()
            ```

        Args:
            tag1: Numeric identifier of the first pulse configuration to be initiated.
            tag2: Numeric identifier of the second pulse configuration to be initiated.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print(InitiatePulseTestDual({tag1}, {tag2}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``InitiatePulseTestDual()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def pulse_i_measure_v(
        self, smu: str, bias: float, level: float, ton: float, toff: float, points: int
    ) -> None:
        """Run the ``PulseIMeasureV()`` function.

        Description:
            - This KIPulse factory script function performs a specified number of pulse I, measure V
              cycles.

        TSP Syntax:
            ```
            - PulseIMeasureV()
            ```

        Args:
            smu: Instrument channel (for example, smua refers to SMU channel A).
            bias: Bias level in amperes.
            level: Pulse level in amperes.
            ton: Pulse on time in seconds.
            toff: Pulse off time in seconds.
            points: Number of pulse-measure cycles.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"PulseIMeasureV({smu}, {bias}, {level}, {ton}, {toff}, {points})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``PulseIMeasureV()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def pulse_v_measure_i(
        self, smu: str, bias: float, level: float, ton: float, toff: float, points: int
    ) -> None:
        """Run the ``PulseVMeasureI()`` function.

        Description:
            - This KIPulse factory script function performs a specified number of pulse V, measure I
              cycles.

        TSP Syntax:
            ```
            - PulseVMeasureI()
            ```

        Args:
            smu: Instrument channel (for example, smua refers to SMU channel A).
            bias: Bias level in volts.
            level: Pulse level in volts.
            ton: Pulse on time in seconds.
            toff: Pulse off time in seconds.
            points: Number of pulse-measure cycles.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"PulseVMeasureI({smu}, {bias}, {level}, {ton}, {toff}, {points})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``PulseVMeasureI()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def query_pulse_config(self, tag: int) -> str:
        """Run the ``QueryPulseConfig()`` function.

        Description:
            - This KIPulse factory script function allows you to inspect the settings of the
              preconfigured pulse train assigned to tag.

        TSP Syntax:
            ```
            - QueryPulseConfig()
            ```

        Args:
            tag: Numeric identifier to be assigned to the defined pulse train.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print(QueryPulseConfig({tag}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``QueryPulseConfig()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def sweep_i_lin_measure_v(
        self, smu_x: str, starti: str, stopi: str, stime: str, points: str
    ) -> None:
        """Run the ``SweepILinMeasureV()`` function.

        Description:
            - This KISweep factory script function performs a linear current sweep with voltage
              measured at every step (point).

        TSP Syntax:
            ```
            - SweepILinMeasureV()
            ```

        Args:
            smu_x: Source-measure unit (SMU) channel (for example, smua refers to SMU channel A).
            starti: Sweep start current in amperes.
            stopi: Sweep stop current in amperes.
            stime: Settling time in seconds; occurs after stepping the source and before making a
                measurement.
            points: Number of sweep points (must be ≥ 2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"SweepILinMeasureV({smu_x}, {starti}, {stopi}, {stime}, {points})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``SweepILinMeasureV()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def sweep_i_list_measure_v(self, smu_x: str, ilist: str, stime: str, points: str) -> None:
        """Run the ``SweepIListMeasureV()`` function.

        Description:
            - This KISweep factory script function performs a current list sweep with voltage
              measured at every step (point).

        TSP Syntax:
            ```
            - SweepIListMeasureV()
            ```

        Args:
            smu_x: Source-measure unit (SMU) channel (for example, smua refers to SMU channel A).
            ilist: Arbitrary list of current source values; ilist = {value1, value2, ...valueN}.
            stime: Settling time in seconds; occurs after stepping the source and before making a
                measurement.
            points: Number of sweep points (must be ≥ 2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"SweepIListMeasureV({smu_x}, {ilist}, {stime}, {points})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``SweepIListMeasureV()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def sweep_i_log_measure_v(
        self, smu_x: str, starti: str, stopi: str, stime: str, points: str
    ) -> None:
        """Run the ``SweepILogMeasureV()`` function.

        Description:
            - This KISweep factory script function performs a logarithmic current sweep with voltage
              measured at every step (point).

        TSP Syntax:
            ```
            - SweepILogMeasureV()
            ```

        Args:
            smu_x: Source-measure unit (SMU) channel (for example, smua.reset() applies to SMU
                channel A).
            starti: Sweep start current in amperes.
            stopi: Sweep stop current in amperes.
            stime: Settling time in seconds; occurs after stepping the source and before making a
                measurement.
            points: Number of sweep points (must be ≥ 2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"SweepILogMeasureV({smu_x}, {starti}, {stopi}, {stime}, {points})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``SweepILogMeasureV()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def sweep_v_lin_measure_i(
        self, smu_x: str, startv: str, stopv: str, stime: str, points: str
    ) -> None:
        """Run the ``SweepVLinMeasureI()`` function.

        Description:
            - This KISweep factory script function performs a linear voltage sweep with current
              measured at every step (point).

        TSP Syntax:
            ```
            - SweepVLinMeasureI()
            ```

        Args:
            smu_x: Source-measure unit (SMU) channel (for example, smua.reset() applies to SMU
                channel A).
            startv: Sweep start voltage in volts.
            stopv: Sweep stop voltage in volts.
            stime: Settling time in seconds; occurs after stepping the source and before making a
                measurement.
            points: Number of sweep points (must be ≥ 2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"SweepVLinMeasureI({smu_x}, {startv}, {stopv}, {stime}, {points})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``SweepVLinMeasureI()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def sweep_v_list_measure_i(self, smu_x: str, vlist: str, stime: str, points: str) -> None:
        """Run the ``SweepVListMeasureI()`` function.

        Description:
            - This KISweep factory script function performs a voltage list sweep with current
              measured at every step (point).

        TSP Syntax:
            ```
            - SweepVListMeasureI()
            ```

        Args:
            smu_x: Source-measure unit (SMU) channel (for example, smua.reset() applies to SMU
                channel A).
            vlist: Arbitrary list of voltage source values; vlist = {value1, value2, ... valueN}.
            stime: Settling time in seconds; occurs after stepping the source and before making a
                measurement.
            points: Number of sweep points (must be ≥ 2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"SweepVListMeasureI({smu_x}, {vlist}, {stime}, {points})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``SweepVListMeasureI()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def sweep_v_log_measure_i(
        self, smu_x: str, startv: str, stopv: str, stime: str, points: str
    ) -> None:
        """Run the ``SweepVLogMeasureI()`` function.

        Description:
            - This KISweep factory script function performs a logarithmic voltage sweep with current
              measured at every step (point).

        TSP Syntax:
            ```
            - SweepVLogMeasureI()
            ```

        Args:
            smu_x: Source-measure unit (SMU) channel (for example, smua applies to SMU channel A).
            startv: Sweep start voltage in volts.
            stopv: Sweep stop voltage in volts.
            stime: Settling time in seconds; occurs after stepping the source and before making a
                measurement.
            points: Number of sweep points (must be ≥ 2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"SweepVLogMeasureI({smu_x}, {startv}, {stopv}, {stime}, {points})"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``SweepVLogMeasureI()`` function."  # noqa: E501
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

    def gm_isweep(self, smu: str, start_i: str, stop_i: str, points: str) -> str:
        """Run the ``gm_isweep()`` function.

        Description:
            - This KIParlib factory script function performs a linear current sweep and calculates
              the transconductance (Gm) at each point.

        TSP Syntax:
            ```
            - gm_isweep()
            ```

        Args:
            smu: Instrument channel (for example, smua refers to SMU channel A).
            start_i: Starting current level of the sweep.
            stop_i: Ending current level of the sweep.
            points: Number of measurements between start_i and stop_i (must be ≥2).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print(gm_isweep({smu}, {start_i}, {stop_i}, {points}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``gm_isweep()`` function."
            raise NoDeviceProvidedError(msg) from error

    def gm_vsweep(self, smu: str, start_v: str, stop_v: str, points: str) -> str:
        """Run the ``gm_vsweep()`` function.

        Description:
            - This KIParlib factory script function performs a linear voltage sweep and calculates
              the transconductance (Gm) at each point.

        TSP Syntax:
            ```
            - gm_vsweep()
            ```

        Args:
            smu: Instrument channel (for example, smua refers to SMU channel A).
            start_v: Starting voltage level of the sweep.
            stop_v: Ending voltage level of the sweep.
            points: Number of measurements between start_v and stop_v (must be ≥ 2).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print(gm_vsweep({smu}, {start_v}, {stop_v}, {points}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``gm_vsweep()`` function."
            raise NoDeviceProvidedError(msg) from error

    def i_leakage_measure(
        self,
        smu_x: str,
        levelv: float,
        limiti: float,
        sourcedelay: float,
        measurei: float,
        measuredelay: float,
    ) -> str:
        """Run the ``i_leakage_measure()`` function.

        Description:
            - This KIHighC factory script function performs a current leakage measurement after
              stepping the output voltage.

        TSP Syntax:
            ```
            - i_leakage_measure()
            ```

        Args:
            smu_x: Instrument channel (for example, smua refers to SMU channel A).
            levelv: Voltage level to step to when this function is called.
            limiti: Current limit setting for the voltage step.
            sourcedelay: Delay to wait before lowering the current limit for measurement.
            measurei: Current limit (and measure range); the current limit is lower at this level
                and because high-capacitance mode is active, the measure range follows.
            measuredelay: Delay to wait after lowering the current limit before making the
                measurement.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print(i_leakage_measure({smu_x}, "
                f"{levelv}, "
                f"{limiti}, "
                f"{sourcedelay}, "
                f"{measurei}, "
                f"{measuredelay}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``i_leakage_measure()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    # pylint: disable=too-many-arguments
    def i_leakage_threshold(
        self,
        smu_x: str,
        levelv: float,
        limiti: float,
        sourcedelay: float,
        measurei: float,
        measuredelay: float,
        threshold: float,
        timeout: float,
    ) -> str:
        """Run the ``i_leakage_threshold()`` function.

        Description:
            - This KIHighC factory script function measures the current and compares it to a
              threshold. This continues until either the measured current drops below the threshold
              or the timeout expires.

        TSP Syntax:
            ```
            - i_leakage_threshold()
            ```

        Args:
            smu_x: Source-measure unit (SMU) channel (for example, smua applies to SMU channel A).
            levelv: Voltage level to step to when this function is called.
            limiti: Current limit setting for the voltage step.
            sourcedelay: Delay to wait before lowering the current limit for measurement.
            measurei: Current limit (and measure range); the current limit is lower at this level
                and because high-capacitance mode is active, the measure range follows.
            measuredelay: Delay before the first measurement after measure range is changed.
            threshold: The specified current that establishes the test limit.
            timeout: Amount of time (in seconds) to wait for the current to drop to threshold after
                all the delays have occurred.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print(i_leakage_threshold({smu_x}, "
                f"{levelv}, "
                f"{limiti}, "
                f"{sourcedelay}, "
                f"{measurei}, "
                f"{measuredelay}, "
                f"{threshold}, "
                f"{timeout}))"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``i_leakage_threshold()`` function."  # noqa: E501
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

    def meminfo(self) -> str:
        """Run the ``meminfo()`` function.

        Description:
            - This function returns the present amount of available memory and the total amount of
              memory in the instrument.

        TSP Syntax:
            ```
            - meminfo()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                "print(meminfo())"
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``meminfo()`` function."
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
            - This function resets commands to their default settings.

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

    def savebuffer(self, buffer: str, format_type: str, file_name: str) -> None:
        """Run the ``savebuffer()`` function.

        Description:
            - This KISavebuffer factory script function saves a specified reading buffer as either a
              .csv file or an .xml file.

        TSP Syntax:
            ```
            - savebuffer()
            ```

        Args:
            buffer: The reading buffer to save.
            format_type: A string indicating which file type to use.
            file_name: The file name of the saved buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'savebuffer({buffer}, "{format_type}", "{file_name}")'
            )
        except AttributeError as error:
            msg = "No TSPControl object was provided, unable to run the ``savebuffer()`` function."
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


class SMU2606BMixin:
    """A mixin that provides access to the SMU2606B commands and constants.

    Properties:
        - ``.command_argument_constants``: The SMU2606B command argument constants.
        - ``.commands``: The SMU2606B commands.
    """

    @cached_property
    def command_argument_constants(self) -> SMU2606BCommandConstants:  # pylint: disable=no-self-use
        """Return the SMU2606B command argument constants.

        This provides access to all the string constants which can be used as arguments for SMU2606B
        commands.
        """
        return SMU2606BCommandConstants()

    @cached_property
    def commands(self) -> SMU2606BCommands:
        """Return the SMU2606B commands.

        This provides access to all the commands for the SMU2606B device. See the documentation of
        each sub-property for more usage information.

        Sub-properties and sub-methods:
            - ``.beeper``: The ``beeper`` command tree.
            - ``.bit``: The ``bit`` command tree.
            - ``.buffer_var``: The ``bufferVar`` command tree.
            - ``.config_pulse_i_measure_v()``: The ``ConfigPulseIMeasureV()`` function.
            - ``.config_pulse_i_measure_v_sweep_lin()``: The ``ConfigPulseIMeasureVSweepLin()``
              function.
            - ``.config_pulse_i_measure_v_sweep_log()``: The ``ConfigPulseIMeasureVSweepLog()``
              function.
            - ``.config_pulse_v_measure_i()``: The ``ConfigPulseVMeasureI()`` function.
            - ``.config_pulse_v_measure_i_sweep_lin()``: The ``ConfigPulseVMeasureISweepLin()``
              function.
            - ``.config_pulse_v_measure_i_sweep_log()``: The ``ConfigPulseVMeasureISweepLog()``
              function.
            - ``.dataqueue``: The ``dataqueue`` command tree.
            - ``.delay()``: The ``delay()`` function.
            - ``.digio``: The ``digio`` command tree.
            - ``.display``: The ``display`` command tree.
            - ``.errorqueue``: The ``errorqueue`` command tree.
            - ``.eventlog``: The ``eventlog`` command tree.
            - ``.exit()``: The ``exit()`` function.
            - ``.format``: The ``format`` command tree.
            - ``.fs``: The ``fs`` command tree.
            - ``.gettimezone()``: The ``gettimezone()`` function.
            - ``.gm_isweep()``: The ``gm_isweep()`` function.
            - ``.gm_vsweep()``: The ``gm_vsweep()`` function.
            - ``.i_leakage_measure()``: The ``i_leakage_measure()`` function.
            - ``.i_leakage_threshold()``: The ``i_leakage_threshold()`` function.
            - ``.initiate_pulse_test()``: The ``InitiatePulseTest()`` function.
            - ``.initiate_pulse_test_dual()``: The ``InitiatePulseTestDual()`` function.
            - ``.io``: The ``io`` command tree.
            - ``.lan``: The ``lan`` command tree.
            - ``.localnode``: The ``localnode`` command tree.
            - ``.makegetter()``: The ``makegetter()`` function.
            - ``.makesetter()``: The ``makesetter()`` function.
            - ``.meminfo()``: The ``meminfo()`` function.
            - ``.node``: The ``node[N]`` command tree.
            - ``.opc()``: The ``opc()`` function.
            - ``.os``: The ``os`` command tree.
            - ``.print()``: The ``print()`` function.
            - ``.printbuffer()``: The ``printbuffer()`` function.
            - ``.printnumber()``: The ``printnumber()`` function.
            - ``.pulse_i_measure_v()``: The ``PulseIMeasureV()`` function.
            - ``.pulse_v_measure_i()``: The ``PulseVMeasureI()`` function.
            - ``.query_pulse_config()``: The ``QueryPulseConfig()`` function.
            - ``.reset()``: The ``reset()`` function.
            - ``.savebuffer()``: The ``savebuffer()`` function.
            - ``.script_var``: The ``scriptVar`` command tree.
            - ``.script``: The ``script`` command tree.
            - ``.settime()``: The ``settime()`` function.
            - ``.settimezone()``: The ``settimezone()`` function.
            - ``.setup``: The ``setup`` command tree.
            - ``.smu``: The ``smuX`` command tree.
            - ``.status``: The ``status`` command tree.
            - ``.sweep_i_lin_measure_v()``: The ``SweepILinMeasureV()`` function.
            - ``.sweep_i_list_measure_v()``: The ``SweepIListMeasureV()`` function.
            - ``.sweep_i_log_measure_v()``: The ``SweepILogMeasureV()`` function.
            - ``.sweep_v_lin_measure_i()``: The ``SweepVLinMeasureI()`` function.
            - ``.sweep_v_list_measure_i()``: The ``SweepVListMeasureI()`` function.
            - ``.sweep_v_log_measure_i()``: The ``SweepVLogMeasureI()`` function.
            - ``.timer``: The ``timer`` command tree.
            - ``.trigger``: The ``trigger`` command tree.
            - ``.tsplink``: The ``tsplink`` command tree.
            - ``.tspnet``: The ``tspnet`` command tree.
            - ``.userstring``: The ``userstring`` command tree.
            - ``.waitcomplete()``: The ``waitcomplete()`` function.
        """
        device = self if isinstance(self, TSPControl) else None
        return SMU2606BCommands(device)
