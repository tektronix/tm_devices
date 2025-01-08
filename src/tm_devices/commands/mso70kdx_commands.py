"""The MSO70KDX commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_5xwdsk_dpodsamso.errordetector import Errordetector
from .gen_5y90wx_dpodsamso.dpojet import Dpojet
from .gen_5yyb4r_mso.trigger import Trigger
from .gen_ffz2xs_dpodsamso.bus import Bus
from .gen_fhrp27_msodpomdodsa.curve import Curve
from .gen_fhrp27_msodpomdodsa.date import Date
from .gen_fhrp27_msodpomdodsa.mathvar import Mathvar
from .gen_fhrp27_msodpomdodsa.save_and_recall import Rcl, Sav
from .gen_fk3z56_dpodsamso.acquire import Acquire
from .gen_fk3z56_dpodsamso.allocate import Allocate
from .gen_fk3z56_dpodsamso.application import Application
from .gen_fk3z56_dpodsamso.autoset import Autoset
from .gen_fk3z56_dpodsamso.auxin import Auxin
from .gen_fk3z56_dpodsamso.auxout import Auxout
from .gen_fk3z56_dpodsamso.bell import Bell
from .gen_fk3z56_dpodsamso.calibrate import Calibrate
from .gen_fk3z56_dpodsamso.ch import Channel
from .gen_fk3z56_dpodsamso.clear import Clear
from .gen_fk3z56_dpodsamso.cmdbatch import Cmdbatch
from .gen_fk3z56_dpodsamso.cq import CqItem
from .gen_fk3z56_dpodsamso.cursor import Cursor
from .gen_fk3z56_dpodsamso.curvenext import Curvenext
from .gen_fk3z56_dpodsamso.curvestream import Curvestream
from .gen_fk3z56_dpodsamso.custom import Custom
from .gen_fk3z56_dpodsamso.d import DigitalBit
from .gen_fk3z56_dpodsamso.data import Data
from .gen_fk3z56_dpodsamso.delete import Delete
from .gen_fk3z56_dpodsamso.diag import Diag
from .gen_fk3z56_dpodsamso.display import Display
from .gen_fk3z56_dpodsamso.email import Email
from .gen_fk3z56_dpodsamso.export import Export
from .gen_fk3z56_dpodsamso.fastacq import Fastacq
from .gen_fk3z56_dpodsamso.filesystem import Filesystem
from .gen_fk3z56_dpodsamso.gpibusb import Gpibusb
from .gen_fk3z56_dpodsamso.hardcopy import Hardcopy
from .gen_fk3z56_dpodsamso.hdr import Hdr
from .gen_fk3z56_dpodsamso.histogram import Histogram
from .gen_fk3z56_dpodsamso.horizontal import Horizontal
from .gen_fk3z56_dpodsamso.limit import Limit
from .gen_fk3z56_dpodsamso.mark import Mark
from .gen_fk3z56_dpodsamso.mask import Mask
from .gen_fk3z56_dpodsamso.math import MathItem
from .gen_fk3z56_dpodsamso.matharbflt import MatharbfltItem
from .gen_fk3z56_dpodsamso.mch import MchItem
from .gen_fk3z56_dpodsamso.measurement import Measurement
from .gen_fk3z56_dpodsamso.multiscope import Multiscope
from .gen_fk3z56_dpodsamso.opcextended import Opcextended
from .gen_fk3z56_dpodsamso.pcenable import Pcenable
from .gen_fk3z56_dpodsamso.recall import Recall
from .gen_fk3z56_dpodsamso.ref import RefItem
from .gen_fk3z56_dpodsamso.save import Save
from .gen_fk3z56_dpodsamso.save_and_recall import Sds
from .gen_fk3z56_dpodsamso.saveon import Saveon
from .gen_fk3z56_dpodsamso.search import Search
from .gen_fk3z56_dpodsamso.select import Select
from .gen_fk3z56_dpodsamso.setup_1 import Setup
from .gen_fk3z56_dpodsamso.system import System
from .gen_fk3z56_dpodsamso.teklink import Teklink
from .gen_fk3z56_dpodsamso.test import Test
from .gen_fk3z56_dpodsamso.trig import Trig
from .gen_fk3z56_dpodsamso.usbtmc import Usbtmc
from .gen_fk3z56_dpodsamso.visual import Visual
from .gen_fk3z56_dpodsamso.wavfrmstream import Wavfrmstream
from .gen_fk3z56_dpodsamso.wfminpre import Wfminpre
from .gen_fk3z56_dpodsamso.wfmoutpre import Wfmoutpre
from .gen_fk3z56_dpodsamso.wfmpre import Wfmpre
from .gen_fk3z56_dpodsamso.zoom import Zoom
from .gen_fkjfe8_msodpodsa.time import Time
from .gen_fpx9s1_dpodsamso.counter import Counter
from .gen_fpx9s1_dpodsamso.linktraining import Linktraining
from .gen_fpx9s1_dpodsamso.rosc import Rosc
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
from .gen_fuq1mi_lpdmsotekscopepcdpodsa.alias import Alias
from .gen_fx54ua_lpdmsodpomdodsa.miscellaneous import Ddt
from .gen_fx54ua_lpdmsodpomdodsa.newpass import Newpass
from .gen_fx54ua_lpdmsodpomdodsa.password import Password
from .gen_fx54ua_lpdmsodpomdodsa.teksecure import Teksecure
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.allev import Allev
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.busy import Busy
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.dese import Dese
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.event import Event
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.evmsg import Evmsg
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.evqty import Evqty
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.factory import Factory
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.id import Id
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.miscellaneous import Lrn
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.rem import Rem
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.set import Set
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.status_and_error import Psc, Pud
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.verbose import Verbose
from .gen_fxvtmy_lpdmsotekscopepcdpomdodsa.wavfrm import Wavfrm
from .gen_fzd77z_lpdmsotekscopepcdpomdodsa.header import Header
from .gen_fzn174_lpdmsodpomdodsa.lock import Lock
from .gen_fzn174_lpdmsodpomdodsa.unlock import Unlock
from .helpers import DefaultDictPassKeyToFactory


# pylint: disable=too-few-public-methods
class MSO70KDXCommandConstants:
    """The MSO70KDX command argument constants.

    This provides access to all the string constants which can be used as arguments for MSO70KDX
    commands.
    """

    A = "A"
    ABSOLUTE = "ABSOLUTE"  # ABSolute
    AC = "AC"
    ACCEPT = "ACCEPT"  # ACCept
    ACK = "ACK"
    ACKERRORREPORT = "ACKERRORREPORT"  # ACKErrorreport
    ACKMISS = "ACKMISS"
    ADDR10 = "ADDR10"
    ADDR7 = "ADDR7"
    ADDRANDDATA = "ADDRANDDATA"
    ADDRESS = "ADDRESS"  # ADDress
    ALL = "ALL"
    ALLFIELDS = "ALLFIELDS"  # ALLFields
    ALLLINES = "ALLLINES"  # ALLLines
    AMI = "AMI"
    AMPLITUDE = "AMPLITUDE"  # AMPlitude
    ANALOG = "ANALOG"  # ANALog
    AND = "AND"
    ANY = "ANY"
    AREA = "AREA"
    # AREA = "AREa"
    ARMATRIGB = "ARMATRIGB"  # ARMAtrigb
    ASCII = "ASCII"  # ASCIi
    # ASCII = "ASCii"
    ATI = "ATI"
    ATRIGGER = "ATRIGGER"  # ATRIGger
    AUTO = "AUTO"
    AUXILIARY = "AUXILIARY"  # AUXiliary
    AVERAGE = "AVERAGE"  # AVErage
    B = "B"
    B3ZS = "B3ZS"
    B6ZS = "B6ZS"
    B8ZS = "B8ZS"
    BACKWARDS = "BACKWARDS"  # BACKWards
    BASE = "BASE"  # BASe
    BILEVELCUSTOM = "BILEVELCUSTOM"  # BILevelcustom
    BINARY = "BINARY"
    # BINARY = "BINary"
    # BINARY = "Binary"
    BIT = "BIT"
    BITSTUFFING = "BITSTUFFING"  # BITSTUFFing
    BLACKMANHARRIS = "BLACKMANHARRIS"  # BLACKMANHarris
    BLANK = "BLANK"
    BLOCK = "BLOCK"
    BLOCK1THEN2 = "BLOCK1THEN2"
    BMP = "BMP"
    BOTH = "BOTH"  # BOTh
    BTA = "BTA"
    BTRIGGER = "BTRIGGER"  # BTRIGger
    BURST = "BURST"  # BURst
    BUS = "BUS"
    BYPASS = "BYPASS"  # BYPass
    CAN = "CAN"
    CANH = "CANH"
    CANL = "CANL"
    CAREA = "CAREA"  # CARea
    CH4 = "CH4"
    CHAR = "CHAR"
    CHARACTER = "CHARACTER"
    CHECKSUM = "CHECKSUM"  # CHecksum
    CHECKSUMERROR = "CHECKSUMERROR"  # CHECKsumerror
    CHKSUMERROR = "CHKSUMERROR"  # CHKSUMError
    CLEAR = "CLEAR"
    CLOCK = "CLOCK"  # CLOCk
    CMEAN = "CMEAN"  # CMEan
    CMI = "CMI"
    COLOR = "COLOR"  # COLOr
    COLOROFF = "COLOROFF"
    COLORON = "COLORON"
    COLUMN = "COLUMN"
    COMMAND = "COMMAND"
    COMMONMODE = "COMMONMODE"  # COMmonmode
    COMMUNICATION = "COMMUNICATION"  # COMMunication
    COMPAT = "COMPAT"
    CONTENTION = "CONTENTION"  # CONTention
    CONTROL = "CONTROL"  # CONtrol
    COUNT = "COUNT"
    CQ = "CQ"
    CR = "CR"
    CRC16 = "CRC16"
    CRC5 = "CRC5"
    CRMS = "CRMS"  # CRMs
    CROSSHAIR = "CROSSHAIR"  # CROSSHair
    CSPLIT = "CSPLIT"
    CTRLSKP = "CTRLSKP"
    CUSTOM = "CUSTOM"
    # CUSTOM = "CUSTom"
    DASHED = "DASHED"  # DASHed
    DATA = "DATA"
    # DATA = "DATa"
    DATAPACKET = "DATAPACKET"  # DATAPacket
    DB = "DB"
    DBM = "DBM"
    DC = "DC"
    DCREJECT = "DCREJECT"  # DCREJect
    DCSLONGREAD = "DCSLONGREAD"  # DCSLONGRead
    DCSLONGWRITE = "DCSLONGWRITE"  # DCSLONGWrite
    DCSR = "DCSR"
    DCSRR2 = "DCSRR2"
    DCSSRR1 = "DCSSRR1"
    DDRREAD = "DDRREAD"  # DDRRead
    DDRREADWRITE = "DDRREADWRITE"  # DDRREADWrite
    DDRWRITE = "DDRWRITE"  # DDRWrite
    DECIMAL = "DECIMAL"  # DECImal
    DECODEFILENAME = "DECODEFILENAME"  # decodeFileName
    DEFAULT = "DEFAULT"
    # DEFAULT = "DEFAult"
    # DEFAULT = "DEFault"
    DELAY = "DELAY"  # DELay
    DELAYED = "DELAYED"  # DELayed
    DELETE = "DELETE"  # DELEte
    DETAILED = "DETAILED"  # DETAiled
    DIFFERENTIAL = "DIFFERENTIAL"  # DIFFerential
    DIGITAL = "DIGITAL"  # DIGItal
    DISABLE = "DISABLE"  # DISable
    DISTDUTY = "DISTDUTY"  # DISTDUty
    DONE = "DONE"
    DONTCARE = "DONTCARE"  # DONTCare
    # DONTCARE = "DONTcare"
    DP = "DP"
    DSINR = "DSINR"
    DSIVC = "DSIVC"
    DSIVIOLATION = "DSIVIOLATION"  # DSIViolation
    DYNAMIC = "DYNAMIC"
    ECCERROR = "ECCERROR"  # ECCError
    ECCMBERROR = "ECCMBERROR"  # ECCMBError
    ECCSBERROR = "ECCSBERROR"  # ECCSBError
    ECCWARN = "ECCWARN"  # ECCWarn
    ECL = "ECL"
    EDGE = "EDGE"
    EI = "EI"
    EIE = "EIE"
    EIGHTYTWENTY = "EIGHTYTWENTY"  # EIGHtytwenty
    EITHER = "EITHER"
    # EITHER = "EITHer"
    # EITHER = "EITher"
    EMBEDDED = "EMBEDDED"  # EMBEDded
    ENABLE = "ENABLE"  # ENable
    ENET100BASETX = "ENET100BASETX"
    ENET100FX = "ENET100FX"
    ENET10BASET = "ENET10BASET"
    ENET1250 = "ENET1250"
    ENETXAUI = "ENETXAUI"
    ENETXAUI2 = "ENETXAUI2"
    ENTERSWINDOW = "ENTERSWINDOW"  # ENTERSWindow
    ENV = "ENV"
    ENVELOPE = "ENVELOPE"  # ENVelope
    EOF = "EOF"
    EOP = "EOP"
    # EOP = "EOp"
    EOT = "EOT"
    EOTSYNC = "EOTSYNC"  # EOTSync
    EQUAL = "EQUAL"  # EQUal
    # EQUAL = "EQual"
    ERR = "ERR"
    ERROR = "ERROR"
    # ERROR = "ERRor"
    ESCMODE = "ESCMODE"  # ESCMode
    ESCMODEERROR = "ESCMODEERROR"  # ESCMODEError
    ET = "ET"
    ETHERNET = "ETHERNET"  # ETHernet
    EVEN = "EVEN"
    EVENT = "EVENT"
    EVENTS = "EVENTS"
    EXECUTE = "EXECUTE"  # EXECute
    EXITSWINDOW = "EXITSWINDOW"  # EXITSWindow
    EXTENDED = "EXTENDED"  # EXTENDed
    # EXTENDED = "EXTENded"
    EXTINCTDB = "EXTINCTDB"
    EXTINCTPCT = "EXTINCTPCT"
    EXTINCTRATIO = "EXTINCTRATIO"
    EYE = "EYE"
    EYEDIAGRAM = "EYEDIAGRAM"  # EYEdiagram
    EYEHEIGHT = "EYEHEIGHT"  # EYEHeight
    FALL = "FALL"
    FALLING = "FALLING"  # FALling
    FALSE = "FALSE"  # FALSe
    FAST = "FAST"
    FASTERTHAN = "FASTERTHAN"  # FASTERthan
    FASTEST = "FASTEST"  # FAStest
    FC1063 = "FC1063"
    FC133 = "FC133"
    FC2125 = "FC2125"
    FC266 = "FC266"
    FC4250 = "FC4250"
    FC531 = "FC531"
    FCE = "FCE"
    FCSERROR = "FCSERROR"  # FCSError
    FFWD = "FFWD"
    FIFTYFIFTY = "FIFTYFIFTY"  # FIFtyfifty
    FIRST = "FIRST"  # FIRst
    FLATTOP2 = "FLATTOP2"
    FLEXRAY = "FLEXRAY"
    FORCE = "FORCE"  # FORCe
    FORWARD = "FORWARD"  # FORWard
    FORWARDS = "FORWARDS"  # FORWards
    FP = "FP"
    FPBINARY = "FPBINARY"  # FPBinary
    FRAME = "FRAME"
    # FRAME = "FRAme"
    FRAMEEND = "FRAMEEND"  # FRAMEEnd
    FRAMESTART = "FRAMESTART"  # FRAMEStart
    FRAMETYPE = "FRAMETYPE"  # FRAMEtype
    FREQUENCY = "FREQUENCY"  # FREQuency
    FREV = "FREV"
    FTS = "FTS"
    FULL = "FULL"
    # FULL = "FULl"
    FULLNOMENU = "FULLNOMENU"  # FULLNOmenu
    FULLSCREEN = "FULLSCREEN"
    FULLSPEED = "FULLSPEED"  # FULLSPeed
    FW1394BS1600B = "FW1394BS1600B"
    FW1394BS400B = "FW1394BS400B"
    FW1394BS800B = "FW1394BS800B"
    FWD = "FWD"
    GAUSSIAN = "GAUSSIAN"  # GAUSSian
    GLITCH = "GLITCH"  # GLItch
    GLONGREAD = "GLONGREAD"  # GLONGRead
    GLONGWRITE = "GLONGWRITE"  # GLONGWrite
    GND = "GND"
    GPIB = "GPIB"  # GPIb
    GRATICULE = "GRATICULE"  # GRAticule
    GREATERTHAN = "GREATERTHAN"  # GREATerthan
    GRID = "GRID"  # GRId
    HAMMING = "HAMMING"  # HAMMing
    HANDSHAKEPACKET = "HANDSHAKEPACKET"  # HANDSHAKEPacket
    HANNING = "HANNING"  # HANNing
    HBARS = "HBARS"  # HBArs
    HD1080I50 = "HD1080I50"
    HD1080I60 = "HD1080I60"
    HD1080P24 = "HD1080P24"
    HD1080P25 = "HD1080P25"
    HD1080P30 = "HD1080P30"
    HD1080P50 = "HD1080P50"
    HD1080P60 = "HD1080P60"
    HD1080SF24 = "HD1080SF24"
    HD480P60 = "HD480P60"
    HD576P50 = "HD576P50"
    HD720P30 = "HD720P30"
    HD720P50 = "HD720P50"
    HD720P60 = "HD720P60"
    HD875I60 = "HD875I60"
    HDB3 = "HDB3"
    HERTZ = "HERTZ"  # HERtz
    HEX = "HEX"
    HEXADECIMAL = "HEXADECIMAL"  # HEXadecimal
    HFREJ = "HFREJ"  # HFRej
    HIGH = "HIGH"
    # HIGH = "high"
    HIRES = "HIRES"  # HIRes
    HISTOGRAM = "HISTOGRAM"  # HIStogram
    HITS = "HITS"  # HITs
    HLS = "HLS"
    HORIZONTAL = "HORIZONTAL"
    # HORIZONTAL = "HORizontal"
    HSRTERROR = "HSRTERROR"  # HSRTError
    HSYNCEND = "HSYNCEND"  # HSYNCEnd
    HSYNCSTART = "HSYNCSTART"  # HSYNCStart
    I2C = "I2C"
    IDANDDATA = "IDANDDATA"
    IDENTIFIER = "IDENTIFIER"  # IDENTifier
    IDLE = "IDLE"
    IN = "IN"
    INDEPENDENT = "INDEPENDENT"  # INDependent
    INFINIBAND = "INFINIBAND"
    INFPERSIST = "INFPERSIST"  # INFPersist
    INHERIT = "INHERIT"
    INIT = "INIT"
    INKSAVER = "INKSAVER"  # INKSaver
    INRANGE = "INRANGE"  # INrange
    INSIDE = "INSIDE"  # INSide
    INSIDEGREATER = "INSIDEGREATER"  # INSIDEGreater
    INVALID = "INVALID"
    INVERTED = "INVERTED"  # INVERTed
    # INVERTED = "INVerted"
    IRE = "IRE"
    ISOALL = "ISOALL"
    ISOEND = "ISOEND"
    ISOMID = "ISOMID"
    ISOSTART = "ISOSTART"
    IT = "IT"
    ITP = "ITP"
    JPEG = "JPEG"
    KAISERBESSEL = "KAISERBESSEL"  # KAISERBessel
    LANDSCAPE = "LANDSCAPE"  # LANdscape
    LARGE = "LARGE"
    # LARGE = "LARge"
    LAST = "LAST"
    LEARN = "LEARN"
    LESSEQUAL = "LESSEQUAL"  # LESSEQual
    LESSTHAN = "LESSTHAN"  # LESSThan
    # LESSTHAN = "LESSthan"
    LF = "LF"
    LFREJ = "LFREJ"  # LFRej
    LIN = "LIN"
    LINE = "LINE"
    LINEAR = "LINEAR"  # LINEAr
    LINEEND = "LINEEND"  # LINEEnd
    LINES = "LINES"
    LINESTART = "LINESTART"  # LINEStart
    LINE_X = "LINE_X"
    LIVE = "LIVE"
    LMP = "LMP"
    LMPCONFIG = "LMPCONFIG"  # LMPConfig
    LMPDEVICE = "LMPDEVICE"  # LMPDevice
    LMPLINK = "LMPLINK"  # LMPLink
    LMPRESPONSE = "LMPRESPONSE"  # LMPResponse
    LMPUTWO = "LMPUTWO"  # LMPUtwo
    LOCK = "LOCK"
    # LOCK = "LOck"
    LOGIC = "LOGIC"
    # LOGIC = "LOGIc"
    LONG = "LONG"
    LOW = "LOW"
    # LOW = "low"
    LOWSPEED = "LOWSPEED"  # LOWSPeed
    LPDATA = "LPDATA"
    LPS666 = "LPS666"
    LPTSERROR = "LPTSERROR"  # LPTSError
    LSB = "LSB"
    MACADDRESS = "MACADDRESS"  # MACADDRess
    MANCHESTER = "MANCHESTER"  # MANCHester
    MANUAL = "MANUAL"
    # MANUAL = "MANual"
    MAXIMUM = "MAXIMUM"  # MAXimum
    MAXRETSIZE = "MAXRETSIZE"  # MAXRETsize
    MDATA = "MDATA"
    MEAN = "MEAN"
    MEANSTDDEV = "MEANSTDDEV"  # MEANSTDdev
    MEDIAN = "MEDIAN"  # MEDian
    MEDIUM = "MEDIUM"  # MEDium
    MHZ10 = "MHZ10"
    MHZ100 = "MHZ100"
    MINIMIZED = "MINIMIZED"
    MINIMUM = "MINIMUM"  # MINImum
    MINMAX = "MINMAX"  # MINMax
    MINUSONE = "MINUSONE"  # MINUSOne
    MIPICSITWO = "MIPICSITWO"  # MIPICSITWo
    MIPIDSIONE = "MIPIDSIONE"  # MIPIDSIOne
    MISO = "MISO"
    MISOMOSI = "MISOMOSI"
    MIXED = "MIXED"  # MIXed
    MLT3 = "MLT3"
    MONOGRAY = "MONOGRAY"
    MONOGREEN = "MONOGREEN"
    MOREEQUA = "MOREEQUA"  # MOREEQua
    MOREEQUAL = "MOREEQUAL"  # MOREEQual
    MORETHAN = "MORETHAN"  # MOREThan
    # MORETHAN = "MOREthan"
    MOSI = "MOSI"
    MSB = "MSB"
    MV = "MV"
    NAK = "NAK"
    NAND = "NAND"  # NANd
    NCROSS = "NCROSS"  # NCROss
    NDUTY = "NDUTY"  # NDUty
    NEGATIVE = "NEGATIVE"  # NEGAtive
    NEXT = "NEXT"
    NO = "NO"
    # NO = "No"
    NOCARE = "NOCARE"
    NOISEREJ = "NOISEREJ"  # NOISErej
    NOPARITY = "NOPARITY"  # NOPARity
    NOR = "NOR"
    NORMAL = "NORMAL"  # NORMal
    NOVERSHOOT = "NOVERSHOOT"  # NOVershoot
    NRZ = "NRZ"
    NTSC = "NTSC"
    # NTSC = "NTSc"
    NULL = "NULL"
    NUMERIC = "NUMERIC"  # NUMERic
    NWIDTH = "NWIDTH"  # NWIdth
    NYET = "NYET"
    OC1 = "OC1"
    OC12 = "OC12"
    OC3 = "OC3"
    OCCURS = "OCCURS"  # OCCurs
    ODD = "ODD"
    OFF = "OFF"
    ON = "ON"
    ONE = "ONE"
    OR = "OR"
    OUT = "OUT"
    OUTRANGE = "OUTRANGE"  # OUTrange
    OUTSIDE = "OUTSIDE"  # OUTside
    OUTSIDEGREATER = "OUTSIDEGREATER"  # OUTSIDEGreater
    OVERLAY = "OVERLAY"  # OVERlay
    OVERLOAD = "OVERLOAD"
    # OVERLOAD = "OVERLoad"
    PACKET = "PACKET"
    PAL = "PAL"
    PARALLEL = "PARALLEL"  # PARallel
    PARITY = "PARITY"  # PARity
    PARITYERROR = "PARITYERROR"  # PARItyerror
    PASS = "PASS"
    PATTERN = "PATTERN"  # PATtern
    PAYLOAD = "PAYLOAD"  # PAYload
    PBASE = "PBASE"  # PBASe
    PCIE = "PCIE"
    PCIEXPRESS = "PCIEXPRESS"  # PCIExpress
    PCIEXPRESS2 = "PCIEXPRESS2"  # PCIExpress2
    PCROSS = "PCROSS"  # PCROss
    PCTCROSS = "PCTCROSS"  # PCTCROss
    PCX = "PCX"
    PDUTY = "PDUTY"  # PDUty
    PEAKDETECT = "PEAKDETECT"  # PEAKdetect
    PEAKHITS = "PEAKHITS"  # PEAKHits
    PENDING = "PENDING"
    PERCENT = "PERCENT"  # PERCent
    PERIOD = "PERIOD"  # PERIod
    PHASE = "PHASE"  # PHAse
    PID = "PID"
    PING = "PING"
    PK2PK = "PK2PK"  # PK2Pk
    PKPKJITTER = "PKPKJITTER"  # PKPKJitter
    PKPKNOISE = "PKPKNOISE"  # PKPKNoise
    PLUSONE = "PLUSONE"  # PLUSOne
    PNG = "PNG"
    POLARCOORD = "POLARCOORD"  # POLARCoord
    PORTRAIT = "PORTRAIT"  # PORTRait
    POSITIVE = "POSITIVE"  # POSITIVe
    PPS101010 = "PPS101010"
    PPS121212 = "PPS121212"
    PPS565 = "PPS565"
    PPS666 = "PPS666"
    PPS888 = "PPS888"
    PRBS7 = "PRBS7"
    PRBS9 = "PRBS9"
    PRE = "PRE"
    PREVIOUS = "PREVIOUS"  # PREVious
    PRODUCT = "PRODUCT"  # PRODuct
    PULSE = "PULSE"  # PULse
    PWIDTH = "PWIDTH"  # PWIdth
    QFACTOR = "QFACTOR"  # QFACtor
    QTAG = "QTAG"
    RANDOM = "RANDOM"
    RATE10000 = "RATE10000"
    RATE12000 = "RATE12000"
    RATE1250 = "RATE1250"
    RATE14000 = "RATE14000"
    RATE1500 = "RATE1500"
    RATE2125 = "RATE2125"
    RATE2500 = "RATE2500"
    RATE3000 = "RATE3000"
    RATE3125 = "RATE3125"
    RATE4250 = "RATE4250"
    RATE5000 = "RATE5000"
    RATE6000 = "RATE6000"
    RATE6250 = "RATE6250"
    RATIO = "RATIO"  # RATio
    RAW10 = "RAW10"
    RAW12 = "RAW12"
    RAW14 = "RAW14"
    RDMINUS = "RDMINUS"
    RDPLUS = "RDPLUS"
    READ = "READ"
    RECOVERED = "RECOVERED"  # RECOVered
    RECTANGULAR = "RECTANGULAR"  # RECTANGular
    # RECTANGULAR = "RECTangular"
    REFOUT = "REFOUT"
    REJECT = "REJECT"  # REJect
    RELOAD = "RELOAD"  # RELoad
    REMOTE = "REMOTE"  # REMote
    REPEATSTART = "REPEATSTART"  # REPEATstart
    RESERVED = "RESERVED"
    RESET = "RESET"
    # RESET = "RESet"
    RESETLIVE = "RESETLIVE"  # RESETLive
    RESTORE = "RESTORE"  # RESTore
    RESUME = "RESUME"
    REV = "REV"
    REVERSE = "REVERSE"  # REVErse
    RGB444 = "RGB444"
    RGB555 = "RGB555"
    RGB565 = "RGB565"
    RGB666 = "RGB666"
    RGB888 = "RGB888"
    RI = "RI"
    RIBINARY = "RIBINARY"  # RIBinary
    RIO_1G = "RIO_1G"
    RIO_2G = "RIO_2G"
    RIO_500M = "RIO_500M"
    RIO_750M = "RIO_750M"
    RIO_SERIAL_1G = "RIO_SERIAL_1G"
    RIO_SERIAL_2_5G = "RIO_SERIAL_2_5G"
    RIO_SERIAL_3G = "RIO_SERIAL_3G"
    RISE = "RISE"
    # RISE = "RISe"
    RISING = "RISING"  # RISing
    RMS = "RMS"
    RMSJITTER = "RMSJITTER"  # RMSJitter
    RMSNOISE = "RMSNOISE"  # RMSNoise
    RP = "RP"
    RPBINARY = "RPBINARY"  # RPBinary
    RS232 = "RS232"
    RT = "RT"
    RUNSTOP = "RUNSTOP"  # RUNSTop
    RUNT = "RUNT"
    RX = "RX"
    S8B10B = "S8B10B"
    SAMPLE = "SAMPLE"  # SAMple
    SAS6_0 = "SAS6_0"
    SATA1_5 = "SATA1_5"
    SATA3_0 = "SATA3_0"
    SATA6_0 = "SATA6_0"
    SAVE = "SAVE"  # SAVe
    SCREEN = "SCREEN"
    SDASHED = "SDASHED"  # SDASHed
    SDS = "SDS"
    SEARCHTOTRIGGER = "SEARCHTOTRIGGER"  # SEARCHtotrigger
    SECAM = "SECAM"
    SECONDS = "SECONDS"  # SECOnds
    SELECTED = "SELECTED"
    SEQUENCE = "SEQUENCE"  # SEQuence
    SEQUENTIAL = "SEQUENTIAL"
    SERIAL = "SERIAL"
    SETHOLD = "SETHOLD"  # SETHold
    SETLEVEL = "SETLEVEL"  # SETLevel
    SETUP = "SETUP"
    SFPBINARY = "SFPBINARY"  # SFPbinary
    SHORT = "SHORT"
    # SHORT = "SHORt"
    SHUTDOWN = "SHUTDOWN"  # SHUTDown
    SIGMA1 = "SIGMA1"
    SIGMA2 = "SIGMA2"
    SIGMA3 = "SIGMA3"
    SINGLEENDED = "SINGLEENDED"  # SINGleended
    SINX = "SINX"
    SIXSIGMAJIT = "SIXSIGMAJIT"  # SIXSigmajit
    SKP = "SKP"
    SLOWERTHAN = "SLOWERTHAN"  # SLOWERthan
    SMALL = "SMALL"  # SMAll
    SNAP = "SNAP"  # SNAp
    SNRATIO = "SNRATIO"  # SNRatio
    SOF = "SOF"
    SOLID = "SOLID"
    SOT = "SOT"
    SOTERROR = "SOTERROR"  # SOTError
    SOTSYNC = "SOTSYNC"  # SOTSync
    SPACE = "SPACE"  # SPace
    SPECIALPACKET = "SPECIALPACKET"  # SPECIALPacket
    SPECTRAL = "SPECTRAL"  # SPECTral
    SPI = "SPI"
    SPLIT = "SPLIT"
    SRCDEPENDENT = "SRCDEPENDENT"  # SRCDependent
    SRCINDEPENDENT = "SRCINDEPENDENT"  # SRCIndependent
    SRIBINARY = "SRIBINARY"  # SRIbinary
    SRPBINARY = "SRPBINARY"  # SRPbinary
    SS = "SS"
    SSPLIT = "SSPLIT"
    STABLE = "STABLE"  # STABle
    STALL = "STALL"
    STANDARD = "STANDARD"
    # STANDARD = "STANdard"
    # STANDARD = "STandard"
    START = "START"
    # START = "STARt"
    STARTUP = "STARTUP"  # STARTup
    STATE = "STATE"
    STATIC = "STATIC"
    STATUS = "STATUS"
    # STATUS = "STATus"
    STAYSHIGH = "STAYSHIGH"  # STAYSHigh
    STAYSLOW = "STAYSLOW"  # STAYSLow
    STDDEV = "STDDEV"  # STDdev
    STOP = "STOP"
    SUBSYS = "SUBSYS"
    SUSPEND = "SUSPEND"
    SYMBOL = "SYMBOL"
    SYMBOLIC = "SYMBOLIC"  # SYMBolic
    SYNC = "SYNC"
    TCPHEADER = "TCPHEADER"  # TCPHeader
    TEAR = "TEAR"
    TEKEXPONENTIAL = "TEKEXPONENTIAL"  # TEKEXPonential
    TEMPERATURE = "TEMPERATURE"  # TEMPErature
    TEST = "TEST"
    # TEST = "TESt"
    TIFF = "TIFF"
    TIME = "TIME"
    # TIME = "TIMe"
    TIMEOUT = "TIMEOUT"  # TIMEOut
    TOGGLE = "TOGGLE"
    TOKENPACKET = "TOKENPACKET"  # TOKENPacket
    TP = "TP"
    TPACK = "TPACK"
    TPERDY = "TPERDY"
    TPNOTIFY = "TPNOTIFY"  # TPNotify
    TPNRDY = "TPNRDY"
    TPPING = "TPPING"  # TPPing
    TPRESPONSE = "TPRESPONSE"  # TPResponse
    TPSTALL = "TPSTALL"  # TPSTall
    TPSTATUS = "TPSTATUS"  # TPStatus
    TRACK = "TRACK"  # TRACk
    TRAINING = "TRAINING"  # TRAining
    TRANSITION = "TRANSITION"  # TRANsition
    TRIGGERTOSEARCH = "TRIGGERTOSEARCH"  # TRIGgertosearch
    TRILEVELCUSTOM = "TRILEVELCUSTOM"  # TRILevelcustom
    TRUE = "TRUE"  # TRUe
    TTL = "TTL"
    TURNON = "TURNON"
    TX = "TX"
    ULTRALP = "ULTRALP"
    UNDEFINED = "UNDEFINED"
    UNDO = "UNDO"  # UNDo
    UNEQUAL = "UNEQUAL"  # UNEQual
    UNLOCK = "UNLOCK"
    USB = "USB"
    USER = "USER"  # USEr
    V1X = "V1X"
    V2X = "V2X"
    VALUEMEAN = "VALUEMEAN"  # VALUEMean
    VBARS = "VBARS"  # VBArs
    VERTICAL = "VERTICAL"
    # VERTICAL = "VERTical"
    VFIELDS = "VFIELDS"  # VFields
    VIDEO = "VIDEO"  # VIDeo
    VLINES = "VLINES"  # VLines
    VSROC192 = "VSROC192"
    VSYNCEND = "VSYNCEND"  # VSYNCEnd
    VSYNCSTART = "VSYNCSTART"  # VSYNCStart
    WAIT = "WAIT"
    WARNING = "WARNING"  # WARNing
    WAVEFORM = "WAVEFORM"  # WAVEform
    WAVEFORMS = "WAVEFORMS"
    WFMDB = "WFMDB"
    WIDERTHAN = "WIDERTHAN"  # WIDERthan
    WIDTH = "WIDTH"  # WIDth
    WINDOW = "WINDOW"  # WINdow
    WITHIN = "WITHIN"  # WITHin
    # WITHIN = "WIThin"
    WRITE = "WRITE"
    X = "X"
    XFF = "XFF"
    XLARGE = "XLARGE"
    XSMALL = "XSMALL"  # XSMAll
    XY = "XY"
    XYZ = "XYZ"
    Y = "Y"
    YCBCR12 = "YCBCR12"
    YCBCR16 = "YCBCR16"
    YCBCR20 = "YCBCR20"
    YCBCR24 = "YCBCR24"
    YES = "YES"
    # YES = "Yes"
    YT = "YT"
    YUV420B10 = "YUV420B10"
    YUV420B8 = "YUV420B8"
    YUV420C10 = "YUV420C10"
    YUV420C8 = "YUV420C8"
    YUV420L8 = "YUV420L8"
    YUV422B10 = "YUV422B10"
    YUV422B8 = "YUV422B8"
    ZERO = "ZERO"


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class MSO70KDXCommands:
    """The MSO70KDX commands.

    This provides access to all the commands for the MSO70KDX device. See the documentation of each
    property for more usage information.

    Properties:
        - ``.acquire``: The ``ACQuire`` command tree.
        - ``.alias``: The ``ALIas`` command.
        - ``.allev``: The ``ALLEv`` command.
        - ``.allocate``: The ``ALLOcate`` command tree.
        - ``.application``: The ``APPLication`` command tree.
        - ``.autoset``: The ``AUTOSet`` command.
        - ``.auxin``: The ``AUXIn`` command tree.
        - ``.auxout``: The ``AUXout`` command.
        - ``.bell``: The ``BELl`` command.
        - ``.bus``: The ``BUS`` command tree.
        - ``.busy``: The ``BUSY`` command.
        - ``.cal``: The ``*CAL`` command.
        - ``.calibrate``: The ``CALibrate`` command.
        - ``.ch``: The ``CH<x>`` command.
        - ``.clear``: The ``CLEAR`` command.
        - ``.cls``: The ``*CLS`` command.
        - ``.cmdbatch``: The ``CMDBatch`` command.
        - ``.counter``: The ``COUnter`` command tree.
        - ``.cq``: The ``CQ<x>`` command tree.
        - ``.cursor``: The ``CURSor`` command.
        - ``.curve``: The ``CURVe`` command.
        - ``.curvenext``: The ``CURVENext`` command.
        - ``.curvestream``: The ``CURVEStream`` command.
        - ``.custom``: The ``CUSTOM`` command tree.
        - ``.d``: The ``D<x>`` command tree.
        - ``.data``: The ``DATa`` command.
        - ``.date``: The ``DATE`` command.
        - ``.ddt``: The ``*DDT`` command.
        - ``.delete``: The ``DELEte`` command tree.
        - ``.dese``: The ``DESE`` command.
        - ``.diag``: The ``DIAg`` command tree.
        - ``.display``: The ``DISplay`` command.
        - ``.dpojet``: The ``DPOJET`` command tree.
        - ``.email``: The ``EMail`` command.
        - ``.errordetector``: The ``ERRORDetector`` command tree.
        - ``.ese``: The ``*ESE`` command.
        - ``.esr``: The ``*ESR`` command.
        - ``.event``: The ``EVENT`` command.
        - ``.evmsg``: The ``EVMsg`` command.
        - ``.evqty``: The ``EVQty`` command.
        - ``.export``: The ``EXPort`` command.
        - ``.factory``: The ``FACtory`` command.
        - ``.fastacq``: The ``FASTAcq`` command.
        - ``.filesystem``: The ``FILESystem`` command.
        - ``.gpibusb``: The ``GPIBUsb`` command tree.
        - ``.hardcopy``: The ``HARDCopy`` command.
        - ``.hdr``: The ``HDR`` command.
        - ``.header``: The ``HEADer`` command.
        - ``.histogram``: The ``HIStogram`` command.
        - ``.horizontal``: The ``HORizontal`` command.
        - ``.id``: The ``ID`` command.
        - ``.idn``: The ``*IDN`` command.
        - ``.limit``: The ``LIMit`` command.
        - ``.linktraining``: The ``LINKTRaining`` command tree.
        - ``.lock``: The ``LOCk`` command.
        - ``.lrn``: The ``*LRN`` command.
        - ``.mark``: The ``MARK`` command.
        - ``.mask``: The ``MASK`` command.
        - ``.math``: The ``MATH<x>`` command.
        - ``.matharbflt``: The ``MATHArbflt<x>`` command tree.
        - ``.mathvar``: The ``MATHVAR`` command.
        - ``.mch``: The ``MCH<x>`` command tree.
        - ``.measurement``: The ``MEASUrement`` command.
        - ``.multiscope``: The ``MULTiscope`` command tree.
        - ``.newpass``: The ``NEWpass`` command.
        - ``.opc``: The ``*OPC`` command.
        - ``.opcextended``: The ``OPCEXtended`` command.
        - ``.opt``: The ``*OPT`` command.
        - ``.password``: The ``PASSWord`` command.
        - ``.pcenable``: The ``PCENable`` command.
        - ``.psc``: The ``*PSC`` command.
        - ``.pud``: The ``*PUD`` command.
        - ``.rcl``: The ``*RCL`` command.
        - ``.recall``: The ``RECAll`` command tree.
        - ``.ref``: The ``REF<x>`` command tree.
        - ``.rem``: The ``REM`` command.
        - ``.rosc``: The ``ROSc`` command tree.
        - ``.rst``: The ``*RST`` command.
        - ``.sav``: The ``*SAV`` command.
        - ``.save``: The ``SAVe`` command tree.
        - ``.saveon``: The ``SAVEON`` command.
        - ``.sds``: The ``*SDS`` command.
        - ``.search``: The ``SEARCH`` command tree.
        - ``.select``: The ``SELect`` command.
        - ``.set``: The ``SET`` command.
        - ``.setup``: The ``SETUp`` command tree.
        - ``.sre``: The ``*SRE`` command.
        - ``.stb``: The ``*STB`` command.
        - ``.system``: The ``SYSTem`` command tree.
        - ``.teklink``: The ``TEKLink`` command tree.
        - ``.teksecure``: The ``TEKSecure`` command.
        - ``.test``: The ``TEST`` command.
        - ``.time``: The ``TIME`` command.
        - ``.trg``: The ``*TRG`` command.
        - ``.trig``: The ``TRIG`` command tree.
        - ``.trigger``: The ``TRIGger`` command.
        - ``.tst``: The ``*TST`` command.
        - ``.unlock``: The ``UNLock`` command.
        - ``.usbtmc``: The ``USBTMC`` command tree.
        - ``.verbose``: The ``VERBose`` command.
        - ``.visual``: The ``VISual`` command.
        - ``.wai``: The ``*WAI`` command.
        - ``.wavfrm``: The ``WAVFrm`` command.
        - ``.wavfrmstream``: The ``WAVFRMStream`` command.
        - ``.wfminpre``: The ``WFMInpre`` command.
        - ``.wfmoutpre``: The ``WFMOutpre`` command.
        - ``.wfmpre``: The ``WFMPre`` command tree.
        - ``.zoom``: The ``ZOOm`` command.
    """

    # pylint: disable=too-many-statements
    def __init__(self, device: Optional[PIControl] = None) -> None:  # noqa: PLR0915
        self._acquire = Acquire(device)
        self._alias = Alias(device)
        self._allev = Allev(device)
        self._allocate = Allocate(device)
        self._application = Application(device)
        self._autoset = Autoset(device)
        self._auxin = Auxin(device)
        self._auxout = Auxout(device)
        self._bell = Bell(device)
        self._bus = Bus(device)
        self._busy = Busy(device)
        self._cal = Cal(device)
        self._calibrate = Calibrate(device)
        self._ch: Dict[int, Channel] = DefaultDictPassKeyToFactory(
            lambda x: Channel(device, f"CH{x}")
        )
        self._clear = Clear(device)
        self._cls = Cls(device)
        self._cmdbatch = Cmdbatch(device)
        self._counter = Counter(device)
        self._cq: Dict[int, CqItem] = DefaultDictPassKeyToFactory(
            lambda x: CqItem(device, f"CQ{x}")
        )
        self._cursor = Cursor(device)
        self._curve = Curve(device)
        self._curvenext = Curvenext(device)
        self._curvestream = Curvestream(device)
        self._custom = Custom(device)
        self._d: Dict[int, DigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: DigitalBit(device, f"D{x}")
        )
        self._data = Data(device)
        self._date = Date(device)
        self._ddt = Ddt(device)
        self._delete = Delete(device)
        self._dese = Dese(device)
        self._diag = Diag(device)
        self._display = Display(device)
        self._dpojet = Dpojet(device)
        self._email = Email(device)
        self._errordetector = Errordetector(device)
        self._ese = Ese(device)
        self._esr = Esr(device)
        self._event = Event(device)
        self._evmsg = Evmsg(device)
        self._evqty = Evqty(device)
        self._export = Export(device)
        self._factory = Factory(device)
        self._fastacq = Fastacq(device)
        self._filesystem = Filesystem(device)
        self._gpibusb = Gpibusb(device)
        self._hardcopy = Hardcopy(device)
        self._hdr = Hdr(device)
        self._header = Header(device)
        self._histogram = Histogram(device)
        self._horizontal = Horizontal(device)
        self._id = Id(device)
        self._idn = Idn(device)
        self._limit = Limit(device)
        self._linktraining = Linktraining(device)
        self._lock = Lock(device)
        self._lrn = Lrn(device)
        self._mark = Mark(device)
        self._mask = Mask(device)
        self._math: Dict[int, MathItem] = DefaultDictPassKeyToFactory(
            lambda x: MathItem(device, f"MATH{x}")
        )
        self._matharbflt: Dict[int, MatharbfltItem] = DefaultDictPassKeyToFactory(
            lambda x: MatharbfltItem(device, f"MATHArbflt{x}")
        )
        self._mathvar = Mathvar(device)
        self._mch: Dict[int, MchItem] = DefaultDictPassKeyToFactory(
            lambda x: MchItem(device, f"MCH{x}")
        )
        self._measurement = Measurement(device)
        self._multiscope = Multiscope(device)
        self._newpass = Newpass(device)
        self._opc = Opc(device)
        self._opcextended = Opcextended(device)
        self._opt = Opt(device)
        self._password = Password(device)
        self._pcenable = Pcenable(device)
        self._psc = Psc(device)
        self._pud = Pud(device)
        self._rcl = Rcl(device)
        self._recall = Recall(device)
        self._ref: Dict[int, RefItem] = DefaultDictPassKeyToFactory(
            lambda x: RefItem(device, f"REF{x}")
        )
        self._rem = Rem(device)
        self._rosc = Rosc(device)
        self._rst = Rst(device)
        self._sav = Sav(device)
        self._save = Save(device)
        self._saveon = Saveon(device)
        self._sds = Sds(device)
        self._search = Search(device)
        self._select = Select(device)
        self._set = Set(device)
        self._setup = Setup(device)
        self._sre = Sre(device)
        self._stb = Stb(device)
        self._system = System(device)
        self._teklink = Teklink(device)
        self._teksecure = Teksecure(device)
        self._test = Test(device)
        self._time = Time(device)
        self._trg = Trg(device)
        self._trig = Trig(device)
        self._trigger = Trigger(device)
        self._tst = Tst(device)
        self._unlock = Unlock(device)
        self._usbtmc = Usbtmc(device)
        self._verbose = Verbose(device)
        self._visual = Visual(device)
        self._wai = Wai(device)
        self._wavfrm = Wavfrm(device)
        self._wavfrmstream = Wavfrmstream(device)
        self._wfminpre = Wfminpre(device)
        self._wfmoutpre = Wfmoutpre(device)
        self._wfmpre = Wfmpre(device)
        self._zoom = Zoom(device)

    @property
    def acquire(self) -> Acquire:
        """Return the ``ACQuire`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enhancedenob``: The ``ACQuire:ENHANCEDEnob`` command.
            - ``.interpeightbit``: The ``ACQuire:INTERPEightbit`` command.
            - ``.magnivu``: The ``ACQuire:MAGnivu`` command.
            - ``.mode``: The ``ACQuire:MODe`` command.
            - ``.numacq``: The ``ACQuire:NUMACq`` command.
            - ``.numavg``: The ``ACQuire:NUMAVg`` command.
            - ``.numenv``: The ``ACQuire:NUMEnv`` command.
            - ``.numframesacquired``: The ``ACQuire:NUMFRAMESACQuired`` command.
            - ``.numsamples``: The ``ACQuire:NUMSAMples`` command.
            - ``.samplingmode``: The ``ACQuire:SAMPlingmode`` command.
            - ``.state``: The ``ACQuire:STATE`` command.
            - ``.stopafter``: The ``ACQuire:STOPAfter`` command.
            - ``.syncsamples``: The ``ACQuire:SYNcsamples`` command.
        """
        return self._acquire

    @property
    def alias(self) -> Alias:
        """Return the ``ALIas`` command.

        Description:
            - This command sets or queries the state of alias functionality, and it is identical to
              the ``ALIAS:STATE`` command.

        Usage:
            - Using the ``.query()`` method will send the ``ALIas?`` query.
            - Using the ``.verify(value)`` method will send the ``ALIas?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ALIas value`` command.

        SCPI Syntax:
            ```
            - ALIas {ON|OFF|<NR1>}
            - ALIas?
            ```

        Info:
            - ``OFF`` turns Alias expansion off.
            - ``ON`` turns Alias expansion on. When a defined alias is received, the specified
              command sequence is substituted for the alias and executed.
            - ``<NR1>`` = 0 disables Alias mode; any other value enables Alias mode.

        Sub-properties:
            - ``.catalog``: The ``ALIas:CATalog`` command.
            - ``.define``: The ``ALIas:DEFine`` command.
            - ``.delete``: The ``ALIas:DELEte`` command.
            - ``.state``: The ``ALIas:STATE`` command.
        """
        return self._alias

    @property
    def allev(self) -> Allev:
        """Return the ``ALLEv`` command.

        Description:
            - This query-only command prompts the instrument to return all events and their messages
              (delimited by commas), and removes the returned events from the Event Queue. Use the
              ``*ESR?`` query to enable the events to be returned. This command is similar to
              repeatedly sending ``*EVMsg?`` queries to the instrument.

        Usage:
            - Using the ``.query()`` method will send the ``ALLEv?`` query.
            - Using the ``.verify(value)`` method will send the ``ALLEv?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ALLEv?
            ```
        """
        return self._allev

    @property
    def allocate(self) -> Allocate:
        """Return the ``ALLOcate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ALLOcate?`` query.
            - Using the ``.verify(value)`` method will send the ``ALLOcate?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.waveform``: The ``ALLOcate:WAVEform`` command tree.
        """
        return self._allocate

    @property
    def application(self) -> Application:
        """Return the ``APPLication`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``APPLication?`` query.
            - Using the ``.verify(value)`` method will send the ``APPLication?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.activate``: The ``APPLication:ACTivate`` command.
            - ``.scopeapp``: The ``APPLication:SCOPEAPP`` command tree.
        """
        return self._application

    @property
    def autoset(self) -> Autoset:
        """Return the ``AUTOSet`` command.

        Description:
            - This command (no query format) sets the vertical, horizontal, and trigger controls of
              the instrument to automatically acquire and display the selected waveform. (To autoset
              a video waveform, the video trigger must be set to video standard, not custom. Video
              arguments require video hardware.) This is equivalent to pressing the front panel
              AUTOSET button. For a detailed description of autoset functionality, see Autoset in
              the index of the online help for your instrument.

        Usage:
            - Using the ``.write(value)`` method will send the ``AUTOSet value`` command.

        SCPI Syntax:
            ```
            - AUTOSet {EXECute|UNDo|VFields|VIDeo|VLines}
            ```

        Info:
            - ``EXECute`` runs the autoset routine; this is equivalent to pressing the front panel
              AUTOSET button. If the display is set to a PAL, MV, or IRE graticule, this argument
              forces the graticule display to full mode (frame, grid, and cross hair).
            - ``UNDo`` returns the instrument to the setting prior to executing an autoset.
            - ``VFields`` autosets the displayed waveform.
            - ``VIDeo`` autosets the displayed waveform.
            - ``VLines`` autosets the displayed waveform.

        Sub-properties:
            - ``.overlay``: The ``AUTOSet:OVErlay`` command.
            - ``.percent``: The ``AUTOSet:PERcent`` command.
        """
        return self._autoset

    @property
    def auxin(self) -> Auxin:
        """Return the ``AUXIn`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXIn?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXIn?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bandwidth``: The ``AUXIn:BANdwidth`` command.
            - ``.coupling``: The ``AUXIn:COUPling`` command.
            - ``.offset``: The ``AUXIn:OFFSet`` command.
            - ``.probefunc``: The ``AUXIn:PROBEFunc`` command tree.
            - ``.probe``: The ``AUXIn:PRObe`` command tree.
            - ``.vterm``: The ``AUXIn:VTERm`` command tree.
        """
        return self._auxin

    @property
    def auxout(self) -> Auxout:
        """Return the ``AUXout`` command.

        Description:
            - This query-only command returns the auxiliary output setup and is equivalent to
              selecting External Signals. From the Utilities menu, and then viewing the current
              settings for the AUX OUT Configuration.

        Usage:
            - Using the ``.query()`` method will send the ``AUXout?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXout?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXout?
            ```

        Sub-properties:
            - ``.edge``: The ``AUXout:EDGE`` command.
            - ``.source``: The ``AUXout:SOUrce`` command.
        """
        return self._auxout

    @property
    def bell(self) -> Bell:
        """Return the ``BELl`` command.

        Description:
            - This command was previously used to beep an audio indicator and is provided for
              backward compatibility.

        Usage:
            - Using the ``.write()`` method will send the ``BELl`` command.

        SCPI Syntax:
            ```
            - BELl
            ```
        """
        return self._bell

    @property
    def bus(self) -> Bus:
        """Return the ``BUS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.b1``: The ``BUS:B1<x>`` command tree.
            - ``.b``: The ``BUS:B<x>`` command tree.
            - ``.ch``: The ``BUS:CH<x>`` command tree.
            - ``.math``: The ``BUS:MATH<x>`` command tree.
            - ``.ref``: The ``BUS:REF<x>`` command tree.
        """
        return self._bus

    @property
    def busy(self) -> Busy:
        """Return the ``BUSY`` command.

        Description:
            - This query-only command returns the status of the instrument. This command allows you
              to synchronize the operation of the instrument with your application program.

        Usage:
            - Using the ``.query()`` method will send the ``BUSY?`` query.
            - Using the ``.verify(value)`` method will send the ``BUSY?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - BUSY?
            ```
        """
        return self._busy

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
    def calibrate(self) -> Calibrate:
        """Return the ``CALibrate`` command.

        Description:
            - This query returns the status of signal path calibration.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate?
            ```

        Sub-properties:
            - ``.calprobe``: The ``CALibrate:CALProbe`` command tree.
            - ``.internal``: The ``CALibrate:INTERNal`` command.
            - ``.probestate``: The ``CALibrate:PRObestate`` command tree.
            - ``.results``: The ``CALibrate:RESults`` command.
        """
        return self._calibrate

    @property
    def ch(self) -> Dict[int, Channel]:
        """Return the ``CH<x>`` command.

        Description:
            - This query-only command returns the vertical parameters for the specified channel. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>?
            ```

        Sub-properties:
            - ``.atiactive``: The ``CH<x>:ATIACTive`` command.
            - ``.available``: The ``CH<x>:AVAILable`` command.
            - ``.bandwidth``: The ``CH<x>:BANdwidth`` command.
            - ``.coupling``: The ``CH<x>:COUPling`` command.
            - ``.deskew``: The ``CH<x>:DESKew`` command.
            - ``.fastacqcapable``: The ``CH<x>:FASTAcqcapable`` command.
            - ``.fastframecapable``: The ``CH<x>:FASTFRamecapable`` command.
            - ``.icapture``: The ``CH<x>:ICAPture`` command tree.
            - ``.invert``: The ``CH<x>:INVert`` command.
            - ``.label``: The ``CH<x>:LABel`` command tree.
            - ``.offset``: The ``CH<x>:OFFSet`` command.
            - ``.opti``: The ``CH<x>:OPTI`` command tree.
            - ``.optical``: The ``CH<x>:OPTIcal`` command tree.
            - ``.position``: The ``CH<x>:POSition`` command.
            - ``.probecontrol``: The ``CH<x>:PROBECOntrol`` command.
            - ``.probecal``: The ``CH<x>:PROBECal`` command.
            - ``.probefunc``: The ``CH<x>:PROBEFunc`` command tree.
            - ``.probe``: The ``CH<x>:PRObe`` command.
            - ``.scale``: The ``CH<x>:SCAle`` command.
            - ``.termination``: The ``CH<x>:TERmination`` command.
            - ``.threshold``: The ``CH<x>:THRESHold`` command.
            - ``.vterm``: The ``CH<x>:VTERm`` command tree.
        """
        return self._ch

    @property
    def clear(self) -> Clear:
        """Return the ``CLEAR`` command.

        Description:
            - This command clears acquisitions, measurements, and waveforms.

        Usage:
            - Using the ``.write(value)`` method will send the ``CLEAR value`` command.

        SCPI Syntax:
            ```
            - CLEAR {ALL}
            ```
        """
        return self._clear

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
    def cmdbatch(self) -> Cmdbatch:
        """Return the ``CMDBatch`` command.

        Description:
            - This command sets or queries the state of command batching. By batching commands,
              database transactions can be optimized, increasing command throughput. Also, batching
              allows for ALL commands in an individual batch to be order independent and accomplish
              the same result as if the commands were coupled. The Batch state is persistent and
              will be saved across power cycles, but will not be saved and recalled as part of a
              setup. In a setup scenario, the factory initial value is enabled.

        Usage:
            - Using the ``.query()`` method will send the ``CMDBatch?`` query.
            - Using the ``.verify(value)`` method will send the ``CMDBatch?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CMDBatch value`` command.

        SCPI Syntax:
            ```
            - CMDBatch {<NR1>OFF|ON}
            - CMDBatch?
            ```

        Info:
            - ``<NR1>`` = 0 turns command batching off; any other value turns command batching on.
            - ``OFF`` turns command batching off.
            - ``ON`` turns command batching on.
        """
        return self._cmdbatch

    @property
    def counter(self) -> Counter:
        """Return the ``COUnter`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``COUnter?`` query.
            - Using the ``.verify(value)`` method will send the ``COUnter?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.results``: The ``COUnter:RESULTs`` command.
        """
        return self._counter

    @property
    def cq(self) -> Dict[int, CqItem]:
        """Return the ``CQ<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CQ<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CQ<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.threshold``: The ``CQ<x>:THRESHold`` command.
        """
        return self._cq

    @property
    def cursor(self) -> Cursor:
        """Return the ``CURSor`` command.

        Description:
            - Returns all of the current cursor settings.

        Usage:
            - Using the ``.query()`` method will send the ``CURSor?`` query.
            - Using the ``.verify(value)`` method will send the ``CURSor?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURSor?
            ```

        Sub-properties:
            - ``.function``: The ``CURSor:FUNCtion`` command.
            - ``.hbars``: The ``CURSor:HBArs`` command.
            - ``.linestyle``: The ``CURSor:LINESTyle`` command.
            - ``.mode``: The ``CURSor:MODe`` command.
            - ``.screen``: The ``CURSor:SCREEN`` command tree.
            - ``.source1``: The ``CURSor:SOUrce1`` command.
            - ``.state``: The ``CURSor:STATE`` command.
            - ``.vbars``: The ``CURSor:VBArs`` command.
            - ``.waveform``: The ``CURSor:WAVEform`` command.
            - ``.xy``: The ``CURSor:XY`` command.
        """
        return self._cursor

    @property
    def curve(self) -> Curve:
        """Return the ``CURVe`` command.

        Description:
            - The ``CURVe`` command transfers the waveform data points the oscilloscope's internal
              reference memory location (REF1-4), which is specified by the to ``DATa:DESTination``
              command. The ``CURVe?`` query transfers data the oscilloscope; the source waveform is
              specified by the from ``DATa:SOUrce`` command. The first and last data points are
              specified by the ``DATa:STARt`` and ``DATa:STOP`` commands. Associated with each
              waveform transferred using the ``CURVe`` command or query is a waveform preamble that
              provides the data format, scale and associated information needed to interpret the
              waveform data points. The preamble information for waveforms sent the oscilloscope is
              specified using the to WFMInpre commands. The preamble information for waveforms
              transferred the oscilloscope is specified or queried using the from WFMOutpre
              commands. If the waveform is not displayed, the query form generates an error. The
              ``CURVe`` command and ``CURVe?`` query transfer waveform data in ASCII or binary
              format. ASCII data is sent as a comma-separated list of decimal values. Binary data is
              sent with the IEEE488.2 binary block header immediately followed by the binary data.
              The IEEE488.2 binary block header is defined as follows: #N<N-digits> where: N is a
              single decimal or hexadecimal digit indicating the number of digits to follow.
              <N-digits> are the decimal digits representing the number of bytes in the data that
              immediately follows this binary block header. The Waveform Transfer command group text
              contains more comprehensive information.

        Usage:
            - Using the ``.query()`` method will send the ``CURVe?`` query.
            - Using the ``.verify(value)`` method will send the ``CURVe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURVe value`` command.

        SCPI Syntax:
            ```
            - CURVe {<Block>|<asc curve>}
            - CURVe?
            ```

        Info:
            - ``<Block>`` is the waveform data in binary format. The waveform is formatted as
              follows.
            - ``<asc curve>`` is the waveform data in ASCII format. The format for ASCII data is
              <NR1>[,<NR1>..], where each <NR1> represents a data point. For RF frequency domain
              waveforms, the data is transmitted as 4-byte floating point values (NR2 or NR3).
        """
        return self._curve

    @property
    def curvenext(self) -> Curvenext:
        """Return the ``CURVENext`` command.

        Description:
            - This query-only command returns unique waveform data from the instrument. This query
              performs just like CURVE?, except multiple uses guarantee that the waveform returned
              is always a new acquisition since the previous CURVENEXT. Note that if the instrument
              is acquiring waveform records at a slow rate (high resolution mode), you must
              configure the controller for long timeout thresholds. Data will not be transferred
              until a new waveform is acquired since the previous ``:CURVENext?`` response.

        Usage:
            - Using the ``.query()`` method will send the ``CURVENext?`` query.
            - Using the ``.verify(value)`` method will send the ``CURVENext?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURVENext?
            ```
        """
        return self._curvenext

    @property
    def curvestream(self) -> Curvestream:
        """Return the ``CURVEStream`` command.

        Description:
            - This query continuously transfers waveform data from the instrument as it is acquired.
              This command puts the instrument into a talk-only mode, allowing the controller to
              receive waveform records as fast as (and as soon as) they are acquired. Use the
              ``DATA:SOURCE`` command to specify the waveform sources. The command does the same
              thing as the CURVE command. Control of the instrument through the user interface or
              other external client is not possible while in streaming mode. The GPIB controller
              must take the instrument out of this continuous talking mode to terminate the query
              and allow other input sources to resume communication with the instrument. The
              following options are available to transition out of streaming curve mode: send a
              device clear over the bus or send another query to the instrument (a MEPE Query
              Interrupted error will occur, but the instrument will be placed back into its normal
              talk/listen mode). Turning the waveform screen display mode off
              (``:DISPLAY:WAVEFORM OFF``) will increase waveform throughput during streaming mode.
              While in streaming mode, two extreme conditions can occur. If the waveform records are
              being acquired slowly (high resolution), configure the controller for long time-out
              thresholds, as the data is not sent out until each complete record is acquired. If the
              waveform records are being acquired rapidly (low resolution), and the controller is
              not reading the data off the bus fast enough, the trigger rate is slowed to allow each
              waveform to be sent sequentially.

        Usage:
            - Using the ``.query()`` method will send the ``CURVEStream?`` query.
            - Using the ``.verify(value)`` method will send the ``CURVEStream?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CURVEStream value`` command.

        SCPI Syntax:
            ```
            - CURVEStream {<Block>|<asc curve>}
            - CURVEStream?
            ```
        """
        return self._curvestream

    @property
    def custom(self) -> Custom:
        """Return the ``CUSTOM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CUSTOM?`` query.
            - Using the ``.verify(value)`` method will send the ``CUSTOM?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.gate``: The ``CUSTOM:GATE<x>`` command tree.
            - ``.select``: The ``CUSTOM:SELECT`` command tree.
        """
        return self._custom

    @property
    def d(self) -> Dict[int, DigitalBit]:
        """Return the ``D<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``D<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.label``: The ``D<x>:LABEL`` command.
            - ``.position``: The ``D<x>:POSition`` command.
            - ``.probe``: The ``D<x>:PROBE`` command tree.
            - ``.threshold``: The ``D<x>:THRESHold`` command.
        """
        return self._d

    @property
    def data(self) -> Data:
        """Return the ``DATa`` command.

        Description:
            - This command sets or queries the format and location of the waveform data that is
              transferred with the CURVE command.

        Usage:
            - Using the ``.query()`` method will send the ``DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa value`` command.

        SCPI Syntax:
            ```
            - DATa {INIT|SNAp}
            - DATa?
            ```

        Info:
            - ``INIT`` initializes the waveform data parameters to their factory defaults except for
              ``DATa:STOP``, which isset to the current acquisition record length.
            - ``SNAp`` Sets ``DATa:STARt`` and ``DATa:STOP`` to match the current waveform cursor
              positions of WAVEVIEW1 CURSOR1 if these waveform cursors are currently on. If these
              waveform cursors are not on when the ``DATa SNAp`` command is sent, it is silently
              ignored and ``DATa:STARt`` and ``:STOP`` remain unchanged.

        Sub-properties:
            - ``.destination``: The ``DATa:DESTination`` command.
            - ``.encdg``: The ``DATa:ENCdg`` command.
            - ``.framestart``: The ``DATa:FRAMESTARt`` command.
            - ``.framestop``: The ``DATa:FRAMESTOP`` command.
            - ``.source``: The ``DATa:SOUrce`` command.
            - ``.start``: The ``DATa:STARt`` command.
            - ``.stop``: The ``DATa:STOP`` command.
            - ``.syncsources``: The ``DATa:SYNCSOUrces`` command.
        """
        return self._data

    @property
    def date(self) -> Date:
        """Return the ``DATE`` command.

        Description:
            - This command specifies the date the oscilloscope displays.

        Usage:
            - Using the ``.query()`` method will send the ``DATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATE value`` command.

        SCPI Syntax:
            ```
            - DATE <QString>
            - DATE?
            ```

        Info:
            - ``<QString>`` is a date in the form 'yyyy-mm-dd' where yyyy refers to a four-digit
              year number, mm refers to a two-digit month number from 01 to 12, and dd refers to a
              two-digit day number in the month.
        """
        return self._date

    @property
    def ddt(self) -> Ddt:
        """Return the ``*DDT`` command.

        Description:
            - This command allows you to specify a command or a list of commands that are executed
              when the instrument receives a TRG command. Define Device Trigger ( ``*DDT`` ) is a
              special alias that the ``*TRG`` command uses.

        Usage:
            - Using the ``.query()`` method will send the ``*DDT?`` query.
            - Using the ``.verify(value)`` method will send the ``*DDT?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``*DDT value`` command.

        SCPI Syntax:
            ```
            - *DDT {<Block>|<QString>}
            - *DDT?
            ```

        Info:
            - ``<Block>`` is a complete sequence of program messages. The messages can contain only
              valid commands that must be separated by semicolons and must follow all rules for
              concatenating commands. The sequence must be less than or equal to 80 characters. The
              format of this argument is always returned as a query.
            - ``<QString>`` is a complete sequence of program messages. The messages can contain
              only valid commands that must be separated by semicolons and must follow all rules for
              concatenating commands. The sequence must be less than or equal to 80 characters.
        """
        return self._ddt

    @property
    def delete(self) -> Delete:
        """Return the ``DELEte`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DELEte?`` query.
            - Using the ``.verify(value)`` method will send the ``DELEte?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.setup``: The ``DELEte:SETUp`` command.
            - ``.waveform``: The ``DELEte:WAVEform`` command.
        """
        return self._delete

    @property
    def dese(self) -> Dese:
        """Return the ``DESE`` command.

        Description:
            - This command sets and queries the bits in the Device Event Status Enable Register
              (DESER). The DESER is the mask that determines whether events are reported to the
              Standard Event Status Register (SESR), and entered into the Event Queue. For a more
              detailed discussion of the use of these registers, see Registers.

        Usage:
            - Using the ``.query()`` method will send the ``DESE?`` query.
            - Using the ``.verify(value)`` method will send the ``DESE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DESE value`` command.

        SCPI Syntax:
            ```
            - DESE <NR1>
            - DESE?
            ```

        Info:
            - ``<NR1>`` The binary bits of the DESER are set according to this value, which ranges
              from 1 through 255. For example, ``DESE 209`` sets the DESER to the binary value
              11010001 (that is, the most significant bit in the register is set to 1, the next most
              significant bit to 1, the next bit to 0, etc.).
        """
        return self._dese

    @property
    def diag(self) -> Diag:
        """Return the ``DIAg`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIAg?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAg?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.control``: The ``DIAg:CONTROL`` command tree.
            - ``.execute``: The ``DIAg:EXECUTE`` command.
            - ``.failures``: The ``DIAg:FAILURES`` command tree.
            - ``.item``: The ``DIAg:ITEM`` command.
            - ``.level``: The ``DIAg:LEVEL`` command.
            - ``.loops``: The ``DIAg:LOOPS`` command.
            - ``.name``: The ``DIAg:NAMe`` command.
            - ``.numitems``: The ``DIAg:NUMITEMS`` command.
            - ``.results``: The ``DIAg:RESults`` command.
            - ``.select``: The ``DIAg:SELect`` command tree.
            - ``.state``: The ``DIAg:STATE`` command.
            - ``.stop``: The ``DIAg:STOP`` command.
        """
        return self._diag

    @property
    def display(self) -> Display:
        """Return the ``DISplay`` command.

        Description:
            - This query-only command returns the current Display settings.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay?
            ```

        Sub-properties:
            - ``.clock``: The ``DISplay:CLOCk`` command.
            - ``.color``: The ``DISplay:COLOr`` command.
            - ``.data``: The ``DISplay:DATa`` command.
            - ``.deskew``: The ``DISplay:DESKew`` command.
            - ``.digital``: The ``DISplay:DIGital`` command tree.
            - ``.dpojetplot``: The ``DISplay:DPOJETPlot`` command.
            - ``.filter``: The ``DISplay:FILTer`` command.
            - ``.format``: The ``DISplay:FORMat`` command.
            - ``.graticule``: The ``DISplay:GRAticule`` command.
            - ``.intensity``: The ``DISplay:INTENSITy`` command.
            - ``.persistence``: The ``DISplay:PERSistence`` command.
            - ``.screentext``: The ``DISplay:SCREENTExt`` command.
            - ``.showremote``: The ``DISplay:SHOWREmote`` command.
            - ``.style``: The ``DISplay:STYle`` command.
            - ``.trigbar``: The ``DISplay:TRIGBar`` command.
            - ``.trigt``: The ``DISplay:TRIGT`` command.
            - ``.varpersist``: The ``DISplay:VARpersist`` command.
            - ``.waveform``: The ``DISplay:WAVEform`` command.
        """
        return self._display

    @property
    def dpojet(self) -> Dpojet:
        """Return the ``DPOJET`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DPOJET?`` query.
            - Using the ``.verify(value)`` method will send the ``DPOJET?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.activate``: The ``DPOJET:ACTIVATE`` command.
            - ``.addmeas``: The ``DPOJET:ADDMeas`` command.
            - ``.addplot``: The ``DPOJET:ADDPlot`` command.
            - ``.analysismethod``: The ``DPOJET:ANALYSISMETHOD`` command.
            - ``.applyall``: The ``DPOJET:APPLYAll`` command.
            - ``.bitratestate``: The ``DPOJET:BITRatestate`` command.
            - ``.clearallmeas``: The ``DPOJET:CLEARALLMeas`` command.
            - ``.clearallplots``: The ``DPOJET:CLEARALLPlots`` command.
            - ``.dataratelimits``: The ``DPOJET:DATAratelimits`` command.
            - ``.deskew``: The ``DPOJET:DESKEW`` command.
            - ``.diracmodel``: The ``DPOJET:DIRacmodel`` command.
            - ``.export``: The ``DPOJET:EXPORT`` command.
            - ``.exportraw``: The ``DPOJET:EXPORTRaw`` command.
            - ``.gating``: The ``DPOJET:GATING`` command.
            - ``.haltfreerunonlimfail``: The ``DPOJET:HALTFreerunonlimfail`` command.
            - ``.highperfrendering``: The ``DPOJET:HIGHPerfrendering`` command.
            - ``.interp``: The ``DPOJET:INTERp`` command.
            - ``.jittermode``: The ``DPOJET:JITtermode`` command.
            - ``.jittermodel``: The ``DPOJET:JITtermodel`` command.
            - ``.lasterror``: The ``DPOJET:LASTError`` command.
            - ``.limitrise``: The ``DPOJET:LIMITRise`` command.
            - ``.limits``: The ``DPOJET:LIMits`` command tree.
            - ``.lockrj``: The ``DPOJET:LOCKRJ`` command.
            - ``.lockrjvalue``: The ``DPOJET:LOCKRJValue`` command.
            - ``.logging``: The ``DPOJET:LOGging`` command tree.
            - ``.meas``: The ``DPOJET:MEAS<x>`` command tree.
            - ``.minbujui``: The ``DPOJET:MINBUJUI`` command.
            - ``.noiseenabled``: The ``DPOJET:NOISEENABLED`` command.
            - ``.nummeas``: The ``DPOJET:NUMMeas`` command.
            - ``.numplot``: The ``DPOJET:NUMPlot`` command.
            - ``.opticalunittype``: The ``DPOJET:OPTICALUNITType`` command.
            - ``.plot``: The ``DPOJET:PLOT<x>`` command tree.
            - ``.population``: The ``DPOJET:POPULATION`` command tree.
            - ``.qualify``: The ``DPOJET:QUALify`` command tree.
            - ``.reflevel``: The ``DPOJET:REFLevel`` command tree.
            - ``.reflevels``: The ``DPOJET:REFLevels`` command tree.
            - ``.report``: The ``DPOJET:REPORT`` command.
            - ``.results``: The ``DPOJET:RESULts`` command tree.
            - ``.save``: The ``DPOJET:SAVE`` command.
            - ``.saveallplots``: The ``DPOJET:SAVEALLPLOTS`` command.
            - ``.setimagetpath``: The ``DPOJET:SETIMAGETPath`` command.
            - ``.setloggingpath``: The ``DPOJET:SETLOGGINGPath`` command.
            - ``.setreportpath``: The ``DPOJET:SETREPORTPath`` command.
            - ``.showmeaswarning``: The ``DPOJET:SHOWMEASWARNing`` command.
            - ``.snc``: The ``DPOJET:SNC`` command tree.
            - ``.sourceautoset``: The ``DPOJET:SOURCEAutoset`` command.
            - ``.state``: The ``DPOJET:STATE`` command.
            - ``.tdcompensation``: The ``DPOJET:TDCOMPensation`` command.
            - ``.unittype``: The ``DPOJET:UNITType`` command.
            - ``.vertunittype``: The ``DPOJET:VERTUNITType`` command.
            - ``.version``: The ``DPOJET:VERsion`` command.
        """
        return self._dpojet

    @property
    def email(self) -> Email:
        """Return the ``EMail`` command.

        Description:
            - This command (no query form) sends a test e-mail message or sets the current e-mail
              sent count to zero.

        Usage:
            - Using the ``.write(value)`` method will send the ``EMail value`` command.

        SCPI Syntax:
            ```
            - EMail {TESt|RESET}
            ```

        Info:
            - ``TESt`` argument sends a test e-mail message.
            - ``RESET`` argument sets the e-mail sent count to zero.

        Sub-properties:
            - ``.attempts``: The ``EMail:ATTempts`` command.
            - ``.authlogin``: The ``EMail:AUTHLogin`` command.
            - ``.authpassword``: The ``EMail:AUTHPassword`` command.
            - ``.count``: The ``EMail:COUNt`` command.
            - ``.from``: The ``EMail:FROm`` command.
            - ``.hostwanted``: The ``EMail:HOSTwanted`` command.
            - ``.image``: The ``EMail:IMAGe`` command.
            - ``.limit``: The ``EMail:LIMit`` command.
            - ``.mask``: The ``EMail:MASK`` command.
            - ``.maxsize``: The ``EMail:MAXSize`` command.
            - ``.measurement``: The ``EMail:MEASUrement`` command.
            - ``.numemails``: The ``EMail:NUMEMails`` command.
            - ``.smtpport``: The ``EMail:SMTPPort`` command.
            - ``.smtpserver``: The ``EMail:SMTPServer`` command.
            - ``.status``: The ``EMail:STATUS`` command.
            - ``.timeout``: The ``EMail:TIMEOut`` command.
            - ``.to``: The ``EMail:TO`` command.
            - ``.trigger``: The ``EMail:TRIGger`` command.
            - ``.waveform``: The ``EMail:WAVEform`` command.
        """
        return self._email

    @property
    def errordetector(self) -> Errordetector:
        """Return the ``ERRORDetector`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.alert``: The ``ERRORDetector:ALERT`` command.
            - ``.aligncharacter``: The ``ERRORDetector:ALIGNCHARacter`` command.
            - ``.alignprimitive``: The ``ERRORDetector:ALIGNPRIMitive`` command.
            - ``.bit``: The ``ERRORDetector:BIT`` command tree.
            - ``.bitrate``: The ``ERRORDetector:BITRate`` command.
            - ``.channel``: The ``ERRORDetector:CHANnel`` command.
            - ``.character``: The ``ERRORDetector:CHARacter`` command.
            - ``.duration``: The ``ERRORDetector:DURATION`` command tree.
            - ``.errorlimit``: The ``ERRORDetector:ERRORLIMIT`` command.
            - ``.file``: The ``ERRORDetector:FILE`` command tree.
            - ``.fontsize``: The ``ERRORDetector:FONTSIze`` command.
            - ``.frame``: The ``ERRORDetector:FRAme`` command.
            - ``.maxaligns``: The ``ERRORDetector:MAXALIGNS`` command.
            - ``.patternname``: The ``ERRORDetector:PATTERNNAME`` command.
            - ``.preset``: The ``ERRORDetector:PREset`` command.
            - ``.saveimage``: The ``ERRORDetector:SAVEIMAGE`` command.
            - ``.savewfm``: The ``ERRORDetector:SAVEWFM`` command.
            - ``.scrambled``: The ``ERRORDetector:SCRAMBLED`` command.
            - ``.sendemail``: The ``ERRORDetector:SENDEMAIL`` command.
            - ``.signaltype``: The ``ERRORDetector:SIGnaltype`` command.
            - ``.skipsetprimitive``: The ``ERRORDetector:SKIPSETPRIMitive`` command tree.
            - ``.ssc``: The ``ERRORDetector:SSC`` command.
            - ``.standard``: The ``ERRORDetector:STANdard`` command.
            - ``.state``: The ``ERRORDetector:STATE`` command.
            - ``.status``: The ``ERRORDetector:STATus`` command.
            - ``.stopwhen``: The ``ERRORDetector:STOPWHEN`` command.
            - ``.symbol``: The ``ERRORDetector:SYMBOL`` command.
            - ``.timeformat``: The ``ERRORDetector:TIMEformat`` command.
            - ``.type``: The ``ERRORDetector:TYPe`` command.
        """
        return self._errordetector

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
        """Return the ``EVENT`` command.

        Description:
            - This query-only command returns an event code from the Event Queue that provides
              information about the results of the last ESR read. ``EVENT?`` also removes the
              returned value from the Event Queue.

        Usage:
            - Using the ``.query()`` method will send the ``EVENT?`` query.
            - Using the ``.verify(value)`` method will send the ``EVENT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - EVENT?
            ```
        """
        return self._event

    @property
    def evmsg(self) -> Evmsg:
        """Return the ``EVMsg`` command.

        Description:
            - This query-only command removes a single event code from the Event Queue that is
              associated with the results of the last ESR read and returns the event code with an
              explanatory message. For more information, see Event Handling.

        Usage:
            - Using the ``.query()`` method will send the ``EVMsg?`` query.
            - Using the ``.verify(value)`` method will send the ``EVMsg?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - EVMsg?
            ```
        """
        return self._evmsg

    @property
    def evqty(self) -> Evqty:
        """Return the ``EVQty`` command.

        Description:
            - This query-only command returns the number of events that are enabled in the queue.
              This is useful when using the ALLEV query, since it lets you know exactly how many
              events will be returned.

        Usage:
            - Using the ``.query()`` method will send the ``EVQty?`` query.
            - Using the ``.verify(value)`` method will send the ``EVQty?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - EVQty?
            ```
        """
        return self._evqty

    @property
    def export(self) -> Export:
        """Return the ``EXPort`` command.

        Description:
            - This command sends a copy of the waveform to the file path specified by
              ``EXPORT:FILENAME``. The ``EXPort`` query returns image format and file information.

        Usage:
            - Using the ``.query()`` method will send the ``EXPort?`` query.
            - Using the ``.verify(value)`` method will send the ``EXPort?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``EXPort value`` command.

        SCPI Syntax:
            ```
            - EXPort STARt
            - EXPort?
            ```

        Info:
            - ``STARt`` initiates the export.

        Sub-properties:
            - ``.filename``: The ``EXPort:FILEName`` command.
            - ``.format``: The ``EXPort:FORMat`` command.
            - ``.palette``: The ``EXPort:PALEtte`` command.
            - ``.readouts``: The ``EXPort:READOuts`` command.
            - ``.view``: The ``EXPort:VIEW`` command.
        """
        return self._export

    @property
    def factory(self) -> Factory:
        """Return the ``FACtory`` command.

        Description:
            - This command (no query form) resets the instrument to its factory default settings.
              This command is equivalent to pressing the DEFAULT SETUP button located on the
              instrument front panel or selecting Default Setup from the File menu. This command
              Performs the following in addition to what is done for the ``*RST`` command: Clears
              any pending OPC operations. Resets the following IEEE488.2 registers: ``*ESE 0``
              (Event Status Enable Register) ``*SRE 0`` (Service Request Enable Register) DESE 255
              (Device Event Status Enable Register) ``*PSC 1`` (Power-on Status Clear Flag) Deletes
              all defined aliases. Enables command headers (``:HEADer 1``).

        Usage:
            - Using the ``.write()`` method will send the ``FACtory`` command.

        SCPI Syntax:
            ```
            - FACtory
            ```
        """
        return self._factory

    @property
    def fastacq(self) -> Fastacq:
        """Return the ``FASTAcq`` command.

        Description:
            - This query-only command returns the state of Fast Acquisitions. This command is
              equivalent to pressing the FASTACQ button on the front panel.

        Usage:
            - Using the ``.query()`` method will send the ``FASTAcq?`` query.
            - Using the ``.verify(value)`` method will send the ``FASTAcq?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FASTAcq?
            ```

        Sub-properties:
            - ``.hiacqrate``: The ``FASTAcq:HIACQRATE`` command.
            - ``.state``: The ``FASTAcq:STATE`` command.
        """
        return self._fastacq

    @property
    def filesystem(self) -> Filesystem:
        """Return the ``FILESystem`` command.

        Description:
            - This query-only command returns the directory listing of the current working
              directory. This query is the same as the ``FILESystem:DIR?`` query.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FILESystem?
            ```

        Sub-properties:
            - ``.copy``: The ``FILESystem:COPy`` command.
            - ``.cwd``: The ``FILESystem:CWD`` command.
            - ``.delete``: The ``FILESystem:DELEte`` command.
            - ``.dir``: The ``FILESystem:DIR`` command.
            - ``.mkdir``: The ``FILESystem:MKDir`` command.
            - ``.print``: The ``FILESystem:PRInt`` command.
            - ``.readfile``: The ``FILESystem:READFile`` command.
            - ``.rename``: The ``FILESystem:REName`` command.
            - ``.rmdir``: The ``FILESystem:RMDir`` command.
            - ``.writefile``: The ``FILESystem:WRITEFile`` command.
        """
        return self._filesystem

    @property
    def gpibusb(self) -> Gpibusb:
        """Return the ``GPIBUsb`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``GPIBUsb?`` query.
            - Using the ``.verify(value)`` method will send the ``GPIBUsb?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``GPIBUsb:ADDress`` command.
            - ``.hwversion``: The ``GPIBUsb:HWVersion`` command.
            - ``.id``: The ``GPIBUsb:ID`` command.
        """
        return self._gpibusb

    @property
    def hardcopy(self) -> Hardcopy:
        """Return the ``HARDCopy`` command.

        Description:
            - This command sends a copy of the screen display to the port specified by
              ``HARDCopy:PORT``. This command is equivalent to pressing the PRINT button on the
              front panel. When printing to a file, the file format can be BMP, JPG, PNG, PCX or
              TIFF. The format of the saved screen capture is set by the ``EXPORT:FORMAT`` command.
              The file format setting is persistent, and will not be affected by a default setup or
              ``*RST`` command sent to the instrument. The ``HARDCopy`` query returns the port and
              file path.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HARDCopy value`` command.

        SCPI Syntax:
            ```
            - HARDCopy STARt
            - HARDCopy?
            ```

        Info:
            - ``STARt`` initiates a screen copy to a file or the default system printer, as
              specified by the ``:HARDCopy:PORT`` selection. The default system printer is set
              within the Windows operating system. If you need information about how to set the
              default system printer, refer to Microsoft Windows online help.

        Sub-properties:
            - ``.filename``: The ``HARDCopy:FILEName`` command.
            - ``.layout``: The ``HARDCopy:LAYout`` command.
            - ``.palette``: The ``HARDCopy:PALEtte`` command.
            - ``.port``: The ``HARDCopy:PORT`` command.
            - ``.readouts``: The ``HARDCopy:READOuts`` command.
            - ``.view``: The ``HARDCopy:VIEW`` command.
        """
        return self._hardcopy

    @property
    def hdr(self) -> Hdr:
        """Return the ``HDR`` command.

        Description:
            - This command is identical to the HEADer query and is included for backward
              compatibility purposes.

        Usage:
            - Using the ``.query()`` method will send the ``HDR?`` query.
            - Using the ``.verify(value)`` method will send the ``HDR?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HDR value`` command.

        SCPI Syntax:
            ```
            - HDR {ON|OFF|<NR1>}
            - HDR?
            ```

        Info:
            - ``<NR1>`` = 0 sets the Response Header Enable State to false; any other value sets
              this state to true, which causes the instrument to send headers on query responses.
            - ``OFF`` sets the Response Header Enable State to false. This causes the instrument to
              omit headers on query responses, so that only the argument is returned.
            - ``ON`` sets the Response Header Enable State to true. This causes the instrument to
              include headers on applicable query responses. You can then use the query response as
              a command.
        """
        return self._hdr

    @property
    def header(self) -> Header:
        """Return the ``HEADer`` command.

        Description:
            - This command sets or queries the Response Header Enable State that causes the
              instrument to either include or omit headers on query responses. Whether the long or
              short form of header keywords and enumerations are returned is dependent upon the
              state of ``:VERBose``.

        Usage:
            - Using the ``.query()`` method will send the ``HEADer?`` query.
            - Using the ``.verify(value)`` method will send the ``HEADer?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HEADer value`` command.

        SCPI Syntax:
            ```
            - HEADer {ON|OFF|<NR1>}
            - HEADer?
            ```

        Info:
            - ``<NR1>`` = 0 sets the Response Header Enable State to false; any other value sets
              this state to true.
            - ``OFF`` sets the Response Header Enable State to false. This causes the instrument to
              omit headers on query responses, so that only the argument is returned.
            - ``ON`` sets the Response Header Enable State to true. This causes the instrument to
              include headers on applicable query responses. You can then use the query response as
              a command.
        """
        return self._header

    @property
    def histogram(self) -> Histogram:
        """Return the ``HIStogram`` command.

        Description:
            - This query-only query returns all histogram parameters; it queries the state of all
              histogram parameters that the user can set. This command is equivalent to selecting
              Waveform Histograms from the Measure menu.

        Usage:
            - Using the ``.query()`` method will send the ``HIStogram?`` query.
            - Using the ``.verify(value)`` method will send the ``HIStogram?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HIStogram?
            ```

        Sub-properties:
            - ``.box``: The ``HIStogram:BOX`` command.
            - ``.boxpcnt``: The ``HIStogram:BOXPcnt`` command.
            - ``.count``: The ``HIStogram:COUNt`` command.
            - ``.data``: The ``HIStogram:DATa`` command.
            - ``.display``: The ``HIStogram:DISplay`` command.
            - ``.function``: The ``HIStogram:FUNCtion`` command.
            - ``.mode``: The ``HIStogram:MODe`` command.
            - ``.size``: The ``HIStogram:SIZe`` command.
            - ``.source``: The ``HIStogram:SOUrce`` command.
            - ``.state``: The ``HIStogram:STATE`` command.
        """
        return self._histogram

    @property
    def horizontal(self) -> Horizontal:
        """Return the ``HORizontal`` command.

        Description:
            - Queries the current horizontal settings.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal?
            ```

        Sub-properties:
            - ``.acqduration``: The ``HORizontal:ACQDURATION`` command.
            - ``.acqlength``: The ``HORizontal:ACQLENGTH`` command.
            - ``.digital``: The ``HORizontal:DIGital`` command tree.
            - ``.divisions``: The ``HORizontal:DIVisions`` command.
            - ``.fastframe``: The ``HORizontal:FASTframe`` command.
            - ``.main``: The ``HORizontal:MAIn`` command.
            - ``.mode``: The ``HORizontal:MODE`` command.
            - ``.position``: The ``HORizontal:POSition`` command.
            - ``.roll``: The ``HORizontal:ROLL`` command.
            - ``.timestamp``: The ``HORizontal:TIMEStamp`` command tree.
        """
        return self._horizontal

    @property
    def id(self) -> Id:
        """Return the ``ID`` command.

        Description:
            - This query-only command returns identifying information about the instrument and
              related firmware similar to that returned by the ``*IDN?`` IEEE488.2 common query but
              does not include the instrument serial number.

        Usage:
            - Using the ``.query()`` method will send the ``ID?`` query.
            - Using the ``.verify(value)`` method will send the ``ID?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ID?
            ```
        """
        return self._id

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
    def limit(self) -> Limit:
        """Return the ``LIMit`` command.

        Description:
            - This query-only command returns all settings for the Limit commands.

        Usage:
            - Using the ``.query()`` method will send the ``LIMit?`` query.
            - Using the ``.verify(value)`` method will send the ``LIMit?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - LIMit?
            ```

        Sub-properties:
            - ``.beep``: The ``LIMit:BEEP`` command.
            - ``.compare``: The ``LIMit:COMpare`` command.
            - ``.email``: The ``LIMit:EMail`` command.
            - ``.hardcopy``: The ``LIMit:HARDCopy`` command.
            - ``.highlighthits``: The ``LIMit:HIGHLIGHTHits`` command.
            - ``.lock``: The ``LIMit:LOCk`` command.
            - ``.log``: The ``LIMit:LOG`` command.
            - ``.savewfm``: The ``LIMit:SAVEWFM`` command.
            - ``.srq``: The ``LIMit:SRQ`` command.
            - ``.state``: The ``LIMit:STATE`` command.
            - ``.status``: The ``LIMit:STATus`` command.
            - ``.stoponviolation``: The ``LIMit:STOPOnviolation`` command.
            - ``.template``: The ``LIMit:TEMPlate`` command tree.
        """
        return self._limit

    @property
    def linktraining(self) -> Linktraining:
        """Return the ``LINKTRaining`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``LINKTRaining?`` query.
            - Using the ``.verify(value)`` method will send the ``LINKTRaining?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.acqtime``: The ``LINKTRaining:ACQTime`` command.
            - ``.armscope``: The ``LINKTRaining:ARMscope`` command.
            - ``.decode``: The ``LINKTRaining:DECOde`` command.
            - ``.equalizationch``: The ``LINKTRaining:EQUalizationCH<x>`` command.
            - ``.lane``: The ``LINKTRaining:LANE`` command.
            - ``.mark``: The ``LINKTRaining:MARK`` command.
            - ``.setup``: The ``LINKTRaining:SETUP`` command.
        """
        return self._linktraining

    @property
    def lock(self) -> Lock:
        """Return the ``LOCk`` command.

        Description:
            - This command enables or disables the touch screen and all front panel buttons and
              knobs. There is no front panel equivalent. When the front panel is locked, the front
              panel commands will not work and will not generate error events. You can work around a
              locked front panel, by using the appropriate programmatic interface commands, instead
              of the front-panel commands. For example, to set the trigger level to 50%, you could
              use ``TRIGger:A SETLevel``. To force a trigger, you could use TRIGger FORCe.

        Usage:
            - Using the ``.query()`` method will send the ``LOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``LOCk?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LOCk value`` command.

        SCPI Syntax:
            ```
            - LOCk {ALL|NONe}
            - LOCk?
            ```

        Info:
            - ``ALL`` disables all front panel controls and the touch screen.
            - ``NONe`` enables all front panel controls and the touch screen. The UNLock ALL command
              only unlocks the front panel controls.
            - ``NONe`` command has no effect. For more information, see the ANSI/IEEE Std 488.1-1987
              Standard Digital Interface for Programmable Instrumentation, section 2.8.3 on RL State
              Descriptions.
        """
        return self._lock

    @property
    def lrn(self) -> Lrn:
        """Return the ``*LRN`` command.

        Description:
            - This query-only command returns the commands that list the instrument settings,
              allowing you to record or 'learn' the current instrument settings. You can use these
              commands to return the instrument to the state it was in when you made the ``*LRN?``
              query. This command is identical to the SET command.

        Usage:
            - Using the ``.query()`` method will send the ``*LRN?`` query.
            - Using the ``.verify(value)`` method will send the ``*LRN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - *LRN?
            ```
        """
        return self._lrn

    @property
    def mark(self) -> Mark:
        """Return the ``MARK`` command.

        Description:
            - Moves to the next or previous reference mark on the waveform. Returns the current mark
              position.

        Usage:
            - Using the ``.query()`` method will send the ``MARK?`` query.
            - Using the ``.verify(value)`` method will send the ``MARK?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MARK value`` command.

        SCPI Syntax:
            ```
            - MARK {NEXT|PREVious}
            - MARK?
            ```

        Info:
            - ``NEXT`` moves to the next reference mark on the right.
            - ``PREVious`` moves to the next reference mark on the left.

        Sub-properties:
            - ``.create``: The ``MARK:CREATE`` command.
            - ``.delete``: The ``MARK:DELEte`` command.
            - ``.free``: The ``MARK:FREE`` command.
            - ``.selected``: The ``MARK:SELECTED`` command tree.
            - ``.total``: The ``MARK:TOTal`` command.
        """
        return self._mark

    @property
    def mask(self) -> Mask:
        """Return the ``MASK`` command.

        Description:
            - This query-only command returns the states of all settable mask parameters.

        Usage:
            - Using the ``.query()`` method will send the ``MASK?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK?
            ```

        Sub-properties:
            - ``.autoadjust``: The ``MASK:AUTOAdjust`` command.
            - ``.autoset``: The ``MASK:AUTOSet`` command tree.
            - ``.copy``: The ``MASK:COPy`` command tree.
            - ``.count``: The ``MASK:COUNt`` command.
            - ``.display``: The ``MASK:DISplay`` command.
            - ``.filter``: The ``MASK:FILTer`` command.
            - ``.highlighthits``: The ``MASK:HIGHLIGHTHits`` command.
            - ``.invert``: The ``MASK:INVert`` command.
            - ``.lock``: The ``MASK:LOCk`` command.
            - ``.margin``: The ``MASK:MARgin`` command tree.
            - ``.maskpre``: The ``MASK:MASKPRE`` command tree.
            - ``.polarity``: The ``MASK:POLarity`` command.
            - ``.seg``: The ``MASK:SEG<m>`` command.
            - ``.source``: The ``MASK:SOUrce`` command.
            - ``.standard``: The ``MASK:STANdard`` command.
            - ``.stoponviolation``: The ``MASK:STOPOnviolation`` command.
            - ``.test``: The ``MASK:TESt`` command tree.
            - ``.user``: The ``MASK:USER`` command tree.
        """
        return self._mask

    @property
    def math(self) -> Dict[int, MathItem]:
        """Return the ``MATH<x>`` command.

        Description:
            - This query-only command returns the definition for the math waveform specified by <x>,
              which ranges from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATH<x>?
            ```

        Sub-properties:
            - ``.define``: The ``MATH<x>:DEFine`` command.
            - ``.filter``: The ``MATH<x>:FILTer`` command tree.
            - ``.label``: The ``MATH<x>:LABel`` command tree.
            - ``.numavg``: The ``MATH<x>:NUMAVg`` command.
            - ``.spectral``: The ``MATH<x>:SPECTral`` command.
            - ``.threshold``: The ``MATH<x>:THRESHold`` command.
            - ``.unitstring``: The ``MATH<x>:UNITString`` command.
            - ``.vertical``: The ``MATH<x>:VERTical`` command tree.
        """
        return self._math

    @property
    def matharbflt(self) -> Dict[int, MatharbfltItem]:
        """Return the ``MATHArbflt<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATHArbflt<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MATHArbflt<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.filepath``: The ``MATHArbflt<x>:FILepath`` command.
            - ``.readfile``: The ``MATHArbflt<x>:READFile`` command.
        """
        return self._matharbflt

    @property
    def mathvar(self) -> Mathvar:
        """Return the ``MATHVAR`` command.

        Description:
            - Queries both numerical values you can use within math expressions.

        Usage:
            - Using the ``.query()`` method will send the ``MATHVAR?`` query.
            - Using the ``.verify(value)`` method will send the ``MATHVAR?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATHVAR?
            ```

        Sub-properties:
            - ``.var``: The ``MATHVAR:VAR<x>`` command.
        """
        return self._mathvar

    @property
    def mch(self) -> Dict[int, MchItem]:
        """Return the ``MCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MCH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.minamplitude``: The ``MCH<x>:MINAMPLitude`` command.
            - ``.maxamplitude``: The ``MCH<x>:MAXAMPLitude`` command.
        """
        return self._mch

    @property
    def measurement(self) -> Measurement:
        """Return the ``MEASUrement`` command.

        Description:
            - This query-only command returns all measurement parameters.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement?
            ```

        Sub-properties:
            - ``.annotation``: The ``MEASUrement:ANNOTation`` command tree.
            - ``.dpojetstatistics``: The ``MEASUrement:DPOJETSTATistics`` command.
            - ``.gating``: The ``MEASUrement:GATing`` command.
            - ``.immed``: The ``MEASUrement:IMMed`` command.
            - ``.meas``: The ``MEASUrement:MEAS<x>`` command.
            - ``.method``: The ``MEASUrement:METHod`` command.
            - ``.noise``: The ``MEASUrement:NOISe`` command.
            - ``.reflevel``: The ``MEASUrement:REFLevel`` command.
            - ``.source1``: The ``MEASUrement:SOUrce1`` command tree.
            - ``.statistics``: The ``MEASUrement:STATIstics`` command tree.
        """
        return self._measurement

    @property
    def multiscope(self) -> Multiscope:
        """Return the ``MULTiscope`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MULTiscope?`` query.
            - Using the ``.verify(value)`` method will send the ``MULTiscope?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.config``: The ``MULTiscope:CONFig`` command.
            - ``.exit``: The ``MULTiscope:EXIT`` command.
            - ``.restart``: The ``MULTiscope:RESTART`` command.
            - ``.status``: The ``MULTiscope:STATUS`` command.
        """
        return self._multiscope

    @property
    def newpass(self) -> Newpass:
        """Return the ``NEWpass`` command.

        Description:
            - This command (no query form) changes the password that enables access to password
              protected data. The PASSWord command must be successfully executed before using this
              command or an execution error will be generated.

        Usage:
            - Using the ``.write(value)`` method will send the ``NEWpass value`` command.

        SCPI Syntax:
            ```
            - NEWpass <QString>
            ```

        Info:
            - ``<QString>`` is the new password, which can contain up to 10 characters.
        """
        return self._newpass

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
    def opcextended(self) -> Opcextended:
        """Return the ``OPCEXtended`` command.

        Description:
            - This command sets or queries the behavior of OPC commands and queries. When enabled,
              operations referenced in the ``*OPC`` command description notify when their overlapped
              functionality has completed. When disabled, the operations notify as they have in the
              past (only once updated in the instrument state database). Command synchronization
              Operation PI sequence Single sequence with ttOff ``:ACQUIRE:STOPAFTER SEQUENCE``
              ``:ACQUIRE:STATE 1``;``*OPC?``;``:WFMOUTPRE:XZERO?`` Single sequence with Measurement
              Annotation ``:ACQUIRE:STOPAFTER SEQUENCE``;``:MEASUREMENT:MEAS1:STATE 1``;TYPE PK2PK
              ``:ACQUIRE:STATE 1``;``*OPC?``;``:MEASUREMENT:ANNOTATION:X1?`` Single sequence with
              Cursors ``:ACQUIRE:STOPAFTER SEQUENCE``;``:CURSOR:FUNCTION WAVEFORM``;SOURCE CH1;STATE
              1 ``:ACQUIRE:STATE 1``;``*OPC?`` Single sequence with Math
              ``:ACQUIRE:STOPAFTER SEQUENCE``;``:MATH1:DEFINE`` 'Ch1``*Ch2``';``:SELECT:MATH1 1``
              ``:ACQUIRE:STATE 1``;``*OPC?`` Default setup followed by Save Waveform
              ``*RST``;``*OPC?`` ``:SAVE:WAVEFORM`` CH1,REF1;``*WAI`` ``:SELECT:REF1 1`` Math On
              during Acq Run mode ``:HORIZONTAL:MODE MANUAL``;RECORDLENGTH 2500000 ``:MATH1:DEFINE``
              'CH1``*CH1``';``:SELECT:MATH1 1`` ``:DATA:ENCDG ASCII``;SOURCE REF1;START 1;STOP 10
              ``:SELECT:MATH1 0`` {Wait a couple sec..longer in release mode?}
              ``:SELECT:MATH1 1``;``*WAI``;``:CURVE?`` Save Math to Ref
              ``:HORIZONTAL:MODE MANUAL``;RECORDLENGTH 2500000 ``:MATH1:DEFINE``
              'CH1``*CH1``';``:SELECT:MATH1 1``;``*WAI``; ``:SAVE:WAVEFORM``
              MATH1,REF1;``:SELECT:REF1 1`` ``:DATA:ENCDG ASCII``;SOURCE REF1;START 1;STOP 10 CURVE?
              Trigger state ``:ACQUIRE:STOPAFTER SEQUENCE``
              ``:ACQUIRE:STATE 1``;``*OPC?``;``:TRIGGER:STATE?`` Single sequence with Measurement
              ``:ACQUIRE:STOPAFTER SEQUENCE``;``:MEASUREMENT:MEAS1:STATE 1``;TYPE AMPLITUDE
              ``:ACQUIRE:STATE 1``;``*OPC?``;``:MEASUREMENT:MEAS1:VALUE?`` Single sequence with
              Measurement on Math
              ``:ACQUIRE:STOPAFTER SEQUENCE``;``:HORIZONTAL:MODE MANUAL``;RECORDLENGTH 2500000
              ``:MATH1:DEFINE`` 'CH1``*CH1``';``:SELECT:MATH1 1``
              ``:MEASUREMENT:MEAS1:STATE 1``;TYPE AMPLITUDE;SOURCE MATH1
              ``:ACQUIRE:STATE 1``;``*OPC?``;``:MEASUREMENT:MEAS1:VALUE?`` Acq Count
              ``*RST``;``*WAI``;``:ACQUIRE:NUMACQ?`` Acq state after single sequence
              ``:ACQUIRE:STOPAFTER SEQUENCE``;STATE 1;``*WAI``;``:ACQUIRE:STATE?``

        Usage:
            - Using the ``.query()`` method will send the ``OPCEXtended?`` query.
            - Using the ``.verify(value)`` method will send the ``OPCEXtended?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OPCEXtended value`` command.

        SCPI Syntax:
            ```
            - OPCEXtended {ON|OFF|<NR1>}
            - OPCEXtended?
            ```

        Info:
            - ``ON`` turns on extended OPC behavior.
            - ``OFF`` turns off extended OPC behavior.
            - ``<NR1>`` = 0 turns off extended OPC behavior; any other value turns on extended OPC
              behavior.
        """
        return self._opcextended

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
    def password(self) -> Password:
        """Return the ``PASSWord`` command.

        Description:
            - This command (no query form) enables the ``*PUD`` and NEWpass set commands. Sending
              ``PASSWord`` without any arguments disables these same commands. Once the password is
              successfully entered, the ``*PUD`` and NEWpass commands are enabled until the
              instrument is powered off, or until the FACtory command, the ``PASSWord`` command with
              no arguments, or the ``*RST`` command is issued. To change the password, you must
              first enter the valid password with the ``PASSWord`` command and then change to your
              new password with the NEWpass command. Remember that the password is case sensitive.

        Usage:
            - Using the ``.write(value)`` method will send the ``PASSWord value`` command.

        SCPI Syntax:
            ```
            - PASSWord <QString>
            ```

        Info:
            - ``<QString>`` is the password, which can contain up to 10 characters. The factory
              default password is 'XYZZY' and is always valid.
        """
        return self._password

    @property
    def pcenable(self) -> Pcenable:
        """Return the ``PCENable`` command.

        Description:
            - Sets or queries the enable state of the User Preference Probe compensation.

        Usage:
            - Using the ``.query()`` method will send the ``PCENable?`` query.
            - Using the ``.verify(value)`` method will send the ``PCENable?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PCENable value`` command.

        SCPI Syntax:
            ```
            - PCENable OFF | ON
            - PCENable?
            ```
        """
        return self._pcenable

    @property
    def psc(self) -> Psc:
        """Return the ``*PSC`` command.

        Description:
            - This command sets and queries the power-on status flag that controls the automatic
              power-on handling of the DESER, SRER, and ESER registers. When ``*PSC`` is true, the
              DESER register is set to 255 and the SRER and ESER registers are set to 0 at power-on.
              When ``*PSC`` is false, the current values in the DESER, SRER, and ESER registers are
              preserved in nonvolatile memory when power is shut off and are restored at power-on.

        Usage:
            - Using the ``.query()`` method will send the ``*PSC?`` query.
            - Using the ``.verify(value)`` method will send the ``*PSC?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``*PSC value`` command.

        SCPI Syntax:
            ```
            - *PSC {ON|OFF|<NR1>}
            - *PSC?
            ```

        Info:
            - ``<NR1>`` = 0 sets the power-on status clear flag to false, disables the power-on
              clear and allows the instrument to possibly assert SRQ after power-on; any other value
              sets the power-on status clear flag to true, enabling the power-on status clear and
              prevents any SRQ assertion after power on.
            - ``OFF`` sets the power-on status clear flag to false, disables the power-on clear and
              allows the instrument to possibly assert SRQ after power-on.
            - ``ON`` sets the power-on status clear flag to true, enabling the power-on status clear
              and prevents any SRQ assertion after power on.
        """
        return self._psc

    @property
    def pud(self) -> Pud:
        """Return the ``*PUD`` command.

        Description:
            - This command sets or queries a string of Protected User Data. This data is protected
              by the PASSWord command. You can modify it only by first entering the correct
              password. This password is not necessary to query the data.

        Usage:
            - Using the ``.query()`` method will send the ``*PUD?`` query.
            - Using the ``.verify(value)`` method will send the ``*PUD?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``*PUD value`` command.

        SCPI Syntax:
            ```
            - *PUD {<Block>|<QString>}
            - *PUD?
            ```

        Info:
            - ``<Block>`` is a block containing up to 100 characters.
            - ``<QString>`` is a string containing up to 100 characters.
        """
        return self._pud

    @property
    def rcl(self) -> Rcl:
        """Return the ``*RCL`` command.

        Description:
            - This command restores the state of the oscilloscope from a copy of the settings stored
              in memory (The settings are stored using the ``*SAV`` command).

        Usage:
            - Using the ``.write(value)`` method will send the ``*RCL value`` command.

        SCPI Syntax:
            ```
            - *RCL <NR1>
            ```

        Info:
            - ``<NR1>`` is a value in the range from 1 to 10, which specifies a saved setup storage
              location.
        """
        return self._rcl

    @property
    def recall(self) -> Recall:
        """Return the ``RECAll`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RECAll?`` query.
            - Using the ``.verify(value)`` method will send the ``RECAll?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mask``: The ``RECAll:MASK`` command.
            - ``.setup``: The ``RECAll:SETUp`` command.
            - ``.waveform``: The ``RECAll:WAVEform`` command.
        """
        return self._recall

    @property
    def ref(self) -> Dict[int, RefItem]:
        """Return the ``REF<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.horizontal``: The ``REF<x>:HORizontal`` command tree.
            - ``.label``: The ``REF<x>:LABel`` command.
            - ``.threshold``: The ``REF<x>:THRESHold`` command.
            - ``.vertical``: The ``REF<x>:VERTical`` command tree.
        """
        return self._ref

    @property
    def rem(self) -> Rem:
        """Return the ``REM`` command.

        Description:
            - This command (no query form) embeds a comment within programs as a means of internally
              documenting the programs. This is how to embed comments in a .set file. The instrument
              ignores these embedded comment lines.

        Usage:
            - Using the ``.write(value)`` method will send the ``REM value`` command.

        SCPI Syntax:
            ```
            - REM <QString>
            ```

        Info:
            - ``<QString>`` is a string that can contain a maximum of 80 characters.
        """
        return self._rem

    @property
    def rosc(self) -> Rosc:
        """Return the ``ROSc`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ROSc?`` query.
            - Using the ``.verify(value)`` method will send the ``ROSc?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.out``: The ``ROSc:OUT`` command tree.
            - ``.source``: The ``ROSc:SOUrce`` command.
            - ``.state``: The ``ROSc:STATE`` command.
            - ``.tracking``: The ``ROSc:TRACking`` command.
        """
        return self._rosc

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
            - Stores the state of the oscilloscope to a specified memory location. You can use the
              ``*RCL`` command to restore the oscilloscope to this saved state at a later time.

        Usage:
            - Using the ``.write(value)`` method will send the ``*SAV value`` command.

        SCPI Syntax:
            ```
            - *SAV <NR1>
            ```

        Info:
            - ``<NR1>`` specifies a location in which to save the state of the oscilloscope.
              Location values range from 1 through 10. Using an out-of-range location value causes
              an execution error. Any settings that have been stored previously at this location
              will be overwritten.
        """
        return self._sav

    @property
    def save(self) -> Save:
        """Return the ``SAVe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.eventtable``: The ``SAVe:EVENTtable`` command tree.
            - ``.marks``: The ``SAVe:MARKS`` command.
            - ``.mask``: The ``SAVe:MASK`` command.
            - ``.setup``: The ``SAVe:SETUp`` command.
            - ``.waveform``: The ``SAVe:WAVEform`` command.
        """
        return self._save

    @property
    def saveon(self) -> Saveon:
        """Return the ``SAVEON`` command.

        Description:
            - Sets the auto-increment file count to 0. Once the number of saved files has reached
              the limit that you set (using the ``SAVEON:NUMevents`` command), no files will be
              saved until you reset the count.

        Usage:
            - Using the ``.write(value)`` method will send the ``SAVEON value`` command.

        SCPI Syntax:
            ```
            - SAVEON {RESET}
            ```

        Info:
            - ``RESET`` sets the file count to 0.

        Sub-properties:
            - ``.count``: The ``SAVEON:COUNt`` command.
            - ``.file``: The ``SAVEON:FILE`` command tree.
            - ``.image``: The ``SAVEON:IMAGe`` command.
            - ``.limit``: The ``SAVEON:LIMit`` command.
            - ``.mask``: The ``SAVEON:MASK`` command.
            - ``.measurement``: The ``SAVEON:MEASUrement`` command.
            - ``.numevents``: The ``SAVEON:NUMEvents`` command.
            - ``.setup``: The ``SAVEON:SETUP`` command.
            - ``.trigger``: The ``SAVEON:TRIGger`` command.
            - ``.waveform``: The ``SAVEON:WAVEform`` command.
        """
        return self._saveon

    @property
    def sds(self) -> Sds:
        """Return the ``*SDS`` command.

        Description:
            - This command (no query form) changes the specified setup to reference the factory
              setup instead of the specific user setup slot. The content of the setup slot is
              unchanged, but the data will no longer be accessible to you. This command is
              equivalent to selecting Delete from the File menu, and then choosing the specified
              setup.

        Usage:
            - Using the ``.write(value)`` method will send the ``*SDS value`` command.

        SCPI Syntax:
            ```
            - *SDS <NR1>
            ```

        Info:
            - ``<NR1>`` specifies a user setup location to delete. Setup storage location values
              range from 1 through 10; using an out-of-range value causes an error.
        """
        return self._sds

    @property
    def search(self) -> Search:
        """Return the ``SEARCH`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.markallevents``: The ``SEARCH:MARKALLevents`` command.
            - ``.search``: The ``SEARCH:SEARCH<x>`` command.
            - ``.stop``: The ``SEARCH:STOP`` command.
        """
        return self._search

    @property
    def select(self) -> Select:
        """Return the ``SELect`` command.

        Description:
            - Queries which waveforms are displayed.

        Usage:
            - Using the ``.query()`` method will send the ``SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SELect?
            ```

        Sub-properties:
            - ``.b``: The ``SELect:B<x>`` command.
            - ``.ch``: The ``SELect:CH<x>`` command.
            - ``.control``: The ``SELect:CONTROl`` command.
            - ``.d``: The ``SELect:D<x>`` command.
            - ``.dall``: The ``SELect:DALL`` command.
            - ``.digtraces``: The ``SELect:DIGTraces`` command tree.
            - ``.math``: The ``SELect:MATH<x>`` command.
            - ``.ref``: The ``SELect:REF<x>`` command.
        """
        return self._select

    @property
    def set_(self) -> Set:
        """Return the ``SET`` command.

        Description:
            - This query-only command returns the commands that list the instrument settings, except
              for configuration information for the calibration values. You can use these commands
              to return the instrument to the state it was in when you made the ``SET?`` query. The
              ``SET?`` query always returns command headers, regardless of the setting of the HEADER
              command. This is because the returned commands are intended to be sent back to the
              instrument as a command string. The VERBOSE command can still be used to specify
              whether the returned headers should be abbreviated or full-length. This command is
              identical to the LRN command.

        Usage:
            - Using the ``.query()`` method will send the ``SET?`` query.
            - Using the ``.verify(value)`` method will send the ``SET?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SET?
            ```
        """
        return self._set

    @property
    def setup(self) -> Setup:
        """Return the ``SETUp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SETUp?`` query.
            - Using the ``.verify(value)`` method will send the ``SETUp?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.name``: The ``SETUp:NAMe`` command.
        """
        return self._setup

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
            - ``.setup``: The ``SYSTem:SETup`` command.
        """
        return self._system

    @property
    def teklink(self) -> Teklink:
        """Return the ``TEKLink`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TEKLink?`` query.
            - Using the ``.verify(value)`` method will send the ``TEKLink?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.connection``: The ``TEKLink:CONNection`` command.
            - ``.refclk``: The ``TEKLink:REFClk`` command.
        """
        return self._teklink

    @property
    def teksecure(self) -> Teksecure:
        """Return the ``TEKSecure`` command.

        Description:
            - This command initializes, for the current user, both waveform and setup memories,
              overwriting any previously stored data. Equivalent to invoking Teksecure from the
              Utility menu. This is a time-consuming operation (3 to 5 minutes) and the instrument
              is inoperable until the TekSecure operation is complete.

        Usage:
            - Using the ``.write()`` method will send the ``TEKSecure`` command.

        SCPI Syntax:
            ```
            - TEKSecure
            ```
        """
        return self._teksecure

    @property
    def test(self) -> Test:
        """Return the ``TEST`` command.

        Description:
            - This command provides the ability to select and execute an item at any level of the
              test hierarchy (Test, Area or Subsystem). The query returns the last command sent.
              This command is equivalent to selecting Instrument Diagnostics from the Utilities
              menu, choosing a test and then pressing Run.

        Usage:
            - Using the ``.query()`` method will send the ``TEST?`` query.
            - Using the ``.verify(value)`` method will send the ``TEST?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TEST value`` command.

        SCPI Syntax:
            ```
            - TEST <QString>
            - TEST?
            ```

        Info:
            - ``<QString>`` sets the test ID, which ranges from 0 through 3 characters. If no test
              ID is specified, all available diagnostics are executed.

        Sub-properties:
            - ``.results``: The ``TEST:RESults`` command.
            - ``.stop``: The ``TEST:STOP`` command.
        """
        return self._test

    @property
    def time(self) -> Time:
        """Return the ``TIME`` command.

        Description:
            - This command sets or queries the time that the instrument displays. This command is
              equivalent to selecting Set Time & Date from the Utilities menu and then setting the
              fields in the Time group box.

        Usage:
            - Using the ``.query()`` method will send the ``TIME?`` query.
            - Using the ``.verify(value)`` method will send the ``TIME?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TIME value`` command.

        SCPI Syntax:
            ```
            - TIME <QString>
            - TIME?
            ```

        Info:
            - ``<QString>`` is a time in the form '``hh:mm:ss``' where hh refers to a two-digit hour
              number, mm refers to a two-digit minute number from 01 to 60, and ss refers to a
              two-digit second number from 01 to 60.
        """
        return self._time

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
    def trig(self) -> Trig:
        """Return the ``TRIG`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIG?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIG?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.a``: The ``TRIG:A`` command tree.
        """
        return self._trig

    @property
    def trigger(self) -> Trigger:
        """Return the ``TRIGger`` command.

        Description:
            - This command forces a trigger event to occur. The query returns the current trigger
              parameters for the instrument.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger value`` command.

        SCPI Syntax:
            ```
            - TRIGger FORCe
            - TRIGger?
            ```

        Info:
            - ``FORCe`` creates a trigger event. If ``TRIGger:STATE`` is set to READy, the
              acquisition will complete. Otherwise, this command will be ignored. This is equivalent
              to pressing the Force button on the front panel.

        Sub-properties:
            - ``.a``: The ``TRIGger:A`` command.
            - ``.auxlevel``: The ``TRIGger:AUXLevel`` command.
            - ``.b``: The ``TRIGger:B`` command.
            - ``.enhanced``: The ``TRIGger:ENHanced`` command.
            - ``.equation``: The ``TRIGger:EQUation<x>`` command.
            - ``.lvlsrcpreference``: The ``TRIGger:LVLSrcpreference`` command.
            - ``.main``: The ``TRIGger:MAIn`` command tree.
            - ``.multiscope``: The ``TRIGger:MULTiscope`` command.
            - ``.qualification``: The ``TRIGger:QUALification`` command tree.
            - ``.sensitivity``: The ``TRIGger:SENSITivity`` command.
            - ``.showequation``: The ``TRIGger:SHOWEQuation`` command.
            - ``.state``: The ``TRIGger:STATE`` command.
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
    def unlock(self) -> Unlock:
        """Return the ``UNLock`` command.

        Description:
            - This command (no query form) unlocks the front panel controls only. To unlock the
              front panel controls and the touch screen use the LOCk NONe command. The command
              ``TOUCHSCReen:STATE ON`` enables the touch screen only.

        Usage:
            - Using the ``.write(value)`` method will send the ``UNLock value`` command.

        SCPI Syntax:
            ```
            - UNLock ALL
            ```

        Info:
            - ``ALL`` specifies that all front panel buttons and knobs are unlocked.
        """
        return self._unlock

    @property
    def usbtmc(self) -> Usbtmc:
        """Return the ``USBTMC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``USBTMC?`` query.
            - Using the ``.verify(value)`` method will send the ``USBTMC?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.productid``: The ``USBTMC:PRODUCTID`` command tree.
            - ``.serialnumber``: The ``USBTMC:SERIALnumber`` command.
            - ``.vendorid``: The ``USBTMC:VENDORID`` command tree.
        """
        return self._usbtmc

    @property
    def verbose(self) -> Verbose:
        """Return the ``VERBose`` command.

        Description:
            - This command sets or queries the Verbose state that controls the length of keywords on
              query responses. Keywords can be both headers and arguments.

        Usage:
            - Using the ``.write(value)`` method will send the ``VERBose value`` command.

        SCPI Syntax:
            ```
            - VERBose {ON|OFF|<NR1>}
            ```

        Info:
            - ``<NR1>`` = 0 disables Verbose, any other value enables Verbose.
            - ``OFF`` sets the Verbose state to false, which returns minimum-length keywords for
              applicable setting queries.
            - ``ON`` sets the Verbose state to true, which returns full-length keywords for
              applicable setting queries.
        """
        return self._verbose

    @property
    def visual(self) -> Visual:
        """Return the ``VISual`` command.

        Description:
            - This query-only command returns the settings for each visual trigger area.

        Usage:
            - Using the ``.query()`` method will send the ``VISual?`` query.
            - Using the ``.verify(value)`` method will send the ``VISual?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - VISual?
            ```

        Sub-properties:
            - ``.area``: The ``VISual:AREA<x>`` command.
            - ``.areacolor``: The ``VISual:AREACOLOr`` command.
            - ``.aspectratio``: The ``VISual:ASPECTratio`` command.
            - ``.deletearea``: The ``VISual:DELETEAREA`` command.
            - ``.enable``: The ``VISual:ENAble`` command.
            - ``.file``: The ``VISual:FILE`` command tree.
        """
        return self._visual

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
    def wavfrm(self) -> Wavfrm:
        """Return the ``WAVFrm`` command.

        Description:
            - This query-only command provides the Tektronix standard waveform query which returns
              the waveform preamble followed by the waveform data for the source specified by
              ``:DATa:SOUrce`` using the ``:DATa`` settings for encoding, width, and so forth.

        Usage:
            - Using the ``.query()`` method will send the ``WAVFrm?`` query.
            - Using the ``.verify(value)`` method will send the ``WAVFrm?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WAVFrm?
            ```
        """
        return self._wavfrm

    @property
    def wavfrmstream(self) -> Wavfrmstream:
        """Return the ``WAVFRMStream`` command.

        Description:
            - This query only command returns WFMQUTPRE? and CURVESTREAM? data for the waveforms
              specified by the DATASOURCE command. This command is similar to sending both
              WFMOUTPRE? and CURVESTREAM?, with the additional provision that each CURVESTREAM
              response to WAVFRMS? has a WFMOUTPRE response prepended to it. This helps guarantee a
              continuous synchronized preamble and curve.

        Usage:
            - Using the ``.query()`` method will send the ``WAVFRMStream?`` query.
            - Using the ``.verify(value)`` method will send the ``WAVFRMStream?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WAVFRMStream?
            ```
        """
        return self._wavfrmstream

    @property
    def wfminpre(self) -> Wfminpre:
        """Return the ``WFMInpre`` command.

        Description:
            - Returns the waveform formatting and scaling specifications to be applied to the next
              incoming CURVe command data.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMInpre?
            ```

        Sub-properties:
            - ``.bit_nr``: The ``WFMInpre:BIT_Nr`` command.
            - ``.bn_fmt``: The ``WFMInpre:BN_Fmt`` command.
            - ``.byt_nr``: The ``WFMInpre:BYT_Nr`` command.
            - ``.byt_or``: The ``WFMInpre:BYT_Or`` command.
            - ``.encdg``: The ``WFMInpre:ENCdg`` command.
            - ``.nr_fr``: The ``WFMInpre:NR_FR`` command.
            - ``.nr_pt``: The ``WFMInpre:NR_Pt`` command.
            - ``.pt_fmt``: The ``WFMInpre:PT_Fmt`` command.
            - ``.pt_off``: The ``WFMInpre:PT_Off`` command.
            - ``.wfid``: The ``WFMInpre:WFId`` command.
            - ``.xincr``: The ``WFMInpre:XINcr`` command.
            - ``.xunit``: The ``WFMInpre:XUNit`` command.
            - ``.xzero``: The ``WFMInpre:XZEro`` command.
            - ``.ymult``: The ``WFMInpre:YMUlt`` command.
            - ``.yoff``: The ``WFMInpre:YOFf`` command.
            - ``.yunit``: The ``WFMInpre:YUNit`` command.
            - ``.yzero``: The ``WFMInpre:YZEro`` command.
        """
        return self._wfminpre

    @property
    def wfmoutpre(self) -> Wfmoutpre:
        """Return the ``WFMOutpre`` command.

        Description:
            - This query-only command queries the waveform formatting data for the waveform
              specified by the ``DATA:SOURCE`` command. The preamble components are considered to be
              of two types; formatting and interpretation. The formatting components are: ENCdg,
              ``BN_Fmt``, ``BYT_Or``, ``BYT_Nr``, ``BIT_Nr``. The interpretation components are
              derived from the ``DATa:SOUrce`` specified waveform.

        Usage:
            - Using the ``.query()`` method will send the ``WFMOutpre?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMOutpre?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMOutpre?
            ```

        Sub-properties:
            - ``.bit_nr``: The ``WFMOutpre:BIT_Nr`` command.
            - ``.bn_fmt``: The ``WFMOutpre:BN_Fmt`` command.
            - ``.byt_nr``: The ``WFMOutpre:BYT_Nr`` command.
            - ``.byt_or``: The ``WFMOutpre:BYT_Or`` command.
            - ``.encdg``: The ``WFMOutpre:ENCdg`` command.
            - ``.nr_fr``: The ``WFMOutpre:NR_FR`` command.
            - ``.nr_pt``: The ``WFMOutpre:NR_Pt`` command.
            - ``.pt_fmt``: The ``WFMOutpre:PT_Fmt`` command.
            - ``.pt_order``: The ``WFMOutpre:PT_ORder`` command.
            - ``.pt_off``: The ``WFMOutpre:PT_Off`` command.
            - ``.wfid``: The ``WFMOutpre:WFId`` command.
            - ``.xincr``: The ``WFMOutpre:XINcr`` command.
            - ``.xunit``: The ``WFMOutpre:XUNit`` command.
            - ``.xzero``: The ``WFMOutpre:XZEro`` command.
            - ``.ymult``: The ``WFMOutpre:YMUlt`` command.
            - ``.yoff``: The ``WFMOutpre:YOFf`` command.
            - ``.yunit``: The ``WFMOutpre:YUNit`` command.
            - ``.yzero``: The ``WFMOutpre:YZEro`` command.
        """
        return self._wfmoutpre

    @property
    def wfmpre(self) -> Wfmpre:
        """Return the ``WFMPre`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WFMPre?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMPre?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.nr_fr``: The ``WFMPre:NR_FR`` command.
        """
        return self._wfmpre

    @property
    def zoom(self) -> Zoom:
        """Return the ``ZOOm`` command.

        Description:
            - This command resets the zoom transforms to default values for all traces or live
              traces. The ``ZOOm`` query returns the current vertical and horizontal positioning and
              scaling of the display.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ZOOm value`` command.

        SCPI Syntax:
            ```
            - ZOOm {RESET|RESETLive}
            - ZOOm?
            ```

        Info:
            - ``RESET`` resets the zoom transforms to default values for all traces.
            - ``RESETLive`` resets the zoom transforms to default values for live traces.

        Sub-properties:
            - ``.graticule``: The ``ZOOm:GRAticule`` command tree.
            - ``.horizontal``: The ``ZOOm:HORizontal`` command tree.
            - ``.math``: The ``ZOOm:MATH<x>`` command tree.
            - ``.mode``: The ``ZOOm:MODe`` command.
            - ``.ref``: The ``ZOOm:REF<x>`` command tree.
            - ``.scroll``: The ``ZOOm:SCROLL`` command tree.
            - ``.state``: The ``ZOOm:STATE`` command.
            - ``.vertical``: The ``ZOOm:VERTical`` command tree.
            - ``.zoom1``: The ``ZOOm:ZOOM1`` command.
        """
        return self._zoom


class MSO70KDXMixin:
    """A mixin that provides access to the MSO70KDX commands and constants.

    Properties:
        - ``.command_argument_constants``: The MSO70KDX command argument constants.
        - ``.commands``: The MSO70KDX commands.
    """

    @cached_property
    def command_argument_constants(self) -> MSO70KDXCommandConstants:  # pylint: disable=no-self-use
        """Return the MSO70KDX command argument constants.

        This provides access to all the string constants which can be used as arguments for MSO70KDX
        commands.
        """
        return MSO70KDXCommandConstants()

    @cached_property
    def commands(self) -> MSO70KDXCommands:
        """Return the MSO70KDX commands.

        This provides access to all the commands for the MSO70KDX device. See the documentation of
        each sub-property for more usage information.

        Sub-properties:
            - ``.acquire``: The ``ACQuire`` command tree.
            - ``.alias``: The ``ALIas`` command.
            - ``.allev``: The ``ALLEv`` command.
            - ``.allocate``: The ``ALLOcate`` command tree.
            - ``.application``: The ``APPLication`` command tree.
            - ``.autoset``: The ``AUTOSet`` command.
            - ``.auxin``: The ``AUXIn`` command tree.
            - ``.auxout``: The ``AUXout`` command.
            - ``.bell``: The ``BELl`` command.
            - ``.bus``: The ``BUS`` command tree.
            - ``.busy``: The ``BUSY`` command.
            - ``.cal``: The ``*CAL`` command.
            - ``.calibrate``: The ``CALibrate`` command.
            - ``.ch``: The ``CH<x>`` command.
            - ``.clear``: The ``CLEAR`` command.
            - ``.cls``: The ``*CLS`` command.
            - ``.cmdbatch``: The ``CMDBatch`` command.
            - ``.counter``: The ``COUnter`` command tree.
            - ``.cq``: The ``CQ<x>`` command tree.
            - ``.cursor``: The ``CURSor`` command.
            - ``.curve``: The ``CURVe`` command.
            - ``.curvenext``: The ``CURVENext`` command.
            - ``.curvestream``: The ``CURVEStream`` command.
            - ``.custom``: The ``CUSTOM`` command tree.
            - ``.d``: The ``D<x>`` command tree.
            - ``.data``: The ``DATa`` command.
            - ``.date``: The ``DATE`` command.
            - ``.ddt``: The ``*DDT`` command.
            - ``.delete``: The ``DELEte`` command tree.
            - ``.dese``: The ``DESE`` command.
            - ``.diag``: The ``DIAg`` command tree.
            - ``.display``: The ``DISplay`` command.
            - ``.dpojet``: The ``DPOJET`` command tree.
            - ``.email``: The ``EMail`` command.
            - ``.errordetector``: The ``ERRORDetector`` command tree.
            - ``.ese``: The ``*ESE`` command.
            - ``.esr``: The ``*ESR`` command.
            - ``.event``: The ``EVENT`` command.
            - ``.evmsg``: The ``EVMsg`` command.
            - ``.evqty``: The ``EVQty`` command.
            - ``.export``: The ``EXPort`` command.
            - ``.factory``: The ``FACtory`` command.
            - ``.fastacq``: The ``FASTAcq`` command.
            - ``.filesystem``: The ``FILESystem`` command.
            - ``.gpibusb``: The ``GPIBUsb`` command tree.
            - ``.hardcopy``: The ``HARDCopy`` command.
            - ``.hdr``: The ``HDR`` command.
            - ``.header``: The ``HEADer`` command.
            - ``.histogram``: The ``HIStogram`` command.
            - ``.horizontal``: The ``HORizontal`` command.
            - ``.id``: The ``ID`` command.
            - ``.idn``: The ``*IDN`` command.
            - ``.limit``: The ``LIMit`` command.
            - ``.linktraining``: The ``LINKTRaining`` command tree.
            - ``.lock``: The ``LOCk`` command.
            - ``.lrn``: The ``*LRN`` command.
            - ``.mark``: The ``MARK`` command.
            - ``.mask``: The ``MASK`` command.
            - ``.math``: The ``MATH<x>`` command.
            - ``.matharbflt``: The ``MATHArbflt<x>`` command tree.
            - ``.mathvar``: The ``MATHVAR`` command.
            - ``.mch``: The ``MCH<x>`` command tree.
            - ``.measurement``: The ``MEASUrement`` command.
            - ``.multiscope``: The ``MULTiscope`` command tree.
            - ``.newpass``: The ``NEWpass`` command.
            - ``.opc``: The ``*OPC`` command.
            - ``.opcextended``: The ``OPCEXtended`` command.
            - ``.opt``: The ``*OPT`` command.
            - ``.password``: The ``PASSWord`` command.
            - ``.pcenable``: The ``PCENable`` command.
            - ``.psc``: The ``*PSC`` command.
            - ``.pud``: The ``*PUD`` command.
            - ``.rcl``: The ``*RCL`` command.
            - ``.recall``: The ``RECAll`` command tree.
            - ``.ref``: The ``REF<x>`` command tree.
            - ``.rem``: The ``REM`` command.
            - ``.rosc``: The ``ROSc`` command tree.
            - ``.rst``: The ``*RST`` command.
            - ``.sav``: The ``*SAV`` command.
            - ``.save``: The ``SAVe`` command tree.
            - ``.saveon``: The ``SAVEON`` command.
            - ``.sds``: The ``*SDS`` command.
            - ``.search``: The ``SEARCH`` command tree.
            - ``.select``: The ``SELect`` command.
            - ``.set``: The ``SET`` command.
            - ``.setup``: The ``SETUp`` command tree.
            - ``.sre``: The ``*SRE`` command.
            - ``.stb``: The ``*STB`` command.
            - ``.system``: The ``SYSTem`` command tree.
            - ``.teklink``: The ``TEKLink`` command tree.
            - ``.teksecure``: The ``TEKSecure`` command.
            - ``.test``: The ``TEST`` command.
            - ``.time``: The ``TIME`` command.
            - ``.trg``: The ``*TRG`` command.
            - ``.trig``: The ``TRIG`` command tree.
            - ``.trigger``: The ``TRIGger`` command.
            - ``.tst``: The ``*TST`` command.
            - ``.unlock``: The ``UNLock`` command.
            - ``.usbtmc``: The ``USBTMC`` command tree.
            - ``.verbose``: The ``VERBose`` command.
            - ``.visual``: The ``VISual`` command.
            - ``.wai``: The ``*WAI`` command.
            - ``.wavfrm``: The ``WAVFrm`` command.
            - ``.wavfrmstream``: The ``WAVFRMStream`` command.
            - ``.wfminpre``: The ``WFMInpre`` command.
            - ``.wfmoutpre``: The ``WFMOutpre`` command.
            - ``.wfmpre``: The ``WFMPre`` command tree.
            - ``.zoom``: The ``ZOOm`` command.
        """
        device = self if isinstance(self, PIControl) else None
        return MSO70KDXCommands(device)
