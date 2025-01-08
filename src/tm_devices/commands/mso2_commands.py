"""The MSO2 commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_1lwj1r_msomdodpo.rosc import Rosc
from .gen_1zn03_mso.acquire import Acquire
from .gen_1zn03_mso.actonevent import Actonevent
from .gen_1zn03_mso.auxout import Auxout
from .gen_1zn03_mso.battery import Battery
from .gen_1zn03_mso.bus import Bus
from .gen_1zn03_mso.callouts import Callouts
from .gen_1zn03_mso.ch import Channel
from .gen_1zn03_mso.data import Data
from .gen_1zn03_mso.dch import DchItem
from .gen_1zn03_mso.diag import Diag
from .gen_1zn03_mso.display import Display
from .gen_1zn03_mso.fpanel import Fpanel
from .gen_1zn03_mso.horizontal import Horizontal
from .gen_1zn03_mso.mask import Mask
from .gen_1zn03_mso.math import Math
from .gen_1zn03_mso.measurement import Measurement
from .gen_1zn03_mso.pg import Pg
from .gen_1zn03_mso.plot import Plot
from .gen_1zn03_mso.power import Power
from .gen_1zn03_mso.ref import Ref
from .gen_1zn03_mso.save import Save
from .gen_1zn03_mso.saveon import Saveon
from .gen_1zn03_mso.saveonevent import Saveonevent
from .gen_1zn03_mso.search import Search
from .gen_1zn03_mso.select import Select
from .gen_1zn03_mso.touchscreen import Touchscreen
from .gen_1zn03_mso.trigger import Trigger
from .gen_1zn03_mso.vxi import Vxi
from .gen_c69az_msotekscopepc.lic import Lic
from .gen_c69az_msotekscopepc.license import License
from .gen_e3h2zs_lpdmso.afg import Afg
from .gen_e3h2zs_lpdmso.autoset import Autoset
from .gen_e3h2zs_lpdmso.calibrate import Calibrate
from .gen_e3h2zs_lpdmso.connected import Connected
from .gen_e3h2zs_lpdmso.ethernet import Ethernet
from .gen_e3h2zs_lpdmso.usbdevice import Usbdevice
from .gen_e4de2d_lpdmsomdo.clear import Clear
from .gen_e6bmgw_lpdmsotekscopepcdpomdo.totaluptime import Totaluptime
from .gen_e6wozn_lpdmsotekscopepcmdodpo.pause import Pause
from .gen_e47rsg_lpdmsotekscopepc.autosavepitimeout import Autosavepitimeout
from .gen_e47rsg_lpdmsotekscopepc.autosaveuitimeout import Autosaveuitimeout
from .gen_e47rsg_lpdmsotekscopepc.bustable import Bustable
from .gen_e47rsg_lpdmsotekscopepc.configuration import Configuration
from .gen_e47rsg_lpdmsotekscopepc.curve import Curve
from .gen_e47rsg_lpdmsotekscopepc.curvestream import Curvestream
from .gen_e47rsg_lpdmsotekscopepc.customtable import Customtable
from .gen_e47rsg_lpdmsotekscopepc.date import Date
from .gen_e47rsg_lpdmsotekscopepc.filesystem import Filesystem
from .gen_e47rsg_lpdmsotekscopepc.mainwindow import Mainwindow
from .gen_e47rsg_lpdmsotekscopepc.meastable import Meastable
from .gen_e47rsg_lpdmsotekscopepc.recall import Recall
from .gen_e47rsg_lpdmsotekscopepc.socketserver import Socketserver
from .gen_e47rsg_lpdmsotekscopepc.time import Time
from .gen_e47rsg_lpdmsotekscopepc.undo import Undo
from .gen_e47rsg_lpdmsotekscopepc.vertical import Vertical
from .gen_e47rsg_lpdmsotekscopepc.wfmoutpre import Wfmoutpre
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
class MSO2CommandConstants:
    """The MSO2 command argument constants.

    This provides access to all the string constants which can be used as arguments for MSO2
    commands.
    """

    ABORT = "ABORT"  # ABOrt
    ABSOLUTE = "ABSOLUTE"  # ABSolute
    AC = "AC"
    ACKMISS = "ACKMISS"
    ACRMS = "ACRMS"
    ADD = "ADD"
    ADDR10 = "ADDR10"
    ADDR7 = "ADDR7"
    ADDRANDDATA = "ADDRANDDATA"
    ADDRESS = "ADDRESS"  # ADDRess
    ADVANCED = "ADVANCED"  # ADVanced
    ALL = "ALL"
    AND = "AND"
    ANYERROR = "ANYERROR"  # ANYERRor
    AREA = "AREA"
    ARROW = "ARROW"
    ASCII = "ASCII"
    # ASCII = "ASCIi"
    # ASCII = "ASCii"
    ATRIGGER = "ATRIGGER"  # ATRIGger
    AUTO = "AUTO"
    AUTOMATIC = "AUTOMATIC"  # AUTOmatic
    AUTOSET = "AUTOSET"  # AUTOset
    AVERAGE = "AVERAGE"  # AVErage
    BACKWARD = "BACKWARD"  # BACKWard
    BADGE = "BADGE"
    BASE = "BASE"
    BASIC = "BASIC"  # BASic
    BINARY = "BINARY"
    # BINARY = "BINary"
    BITSTUFFING = "BITSTUFFING"  # BITSTUFFing
    BLACKMANHARRIS = "BLACKMANHARRIS"  # BLACKMANHarris
    BMP = "BMP"
    BOOKMARK = "BOOKMARK"
    BOTH = "BOTH"
    BURST = "BURST"  # BURSt
    BURSTWIDTH = "BURSTWIDTH"
    BUS = "BUS"
    # BUS = "Bus"
    BUSANDWAVEFORM = "BUSANDWAVEFORM"
    CAN = "CAN"
    CAN2X = "CAN2X"
    CHECKSUM = "CHECKSUM"  # CHecksum
    CLEAR = "CLEAR"
    CLOCK = "CLOCK"
    CONSTANT = "CONSTANT"  # CONSTant
    CONTINUOUS = "CONTINUOUS"  # CONTinuous
    CR = "CR"
    CRC = "CRC"
    CUSTOM = "CUSTOM"  # CUSTom
    DATA = "DATA"
    # DATA = "DATa"
    DATARATE = "DATARATE"
    DBM = "DBM"
    DC = "DC"
    DCREJECT = "DCREJECT"  # DCREJect
    DDR = "DDR"
    DECIMAL = "DECIMAL"
    DEFAULTSETUP = "DEFAULTSETUP"  # DEFaultsetup
    DISABLED = "DISABLED"  # DISabled
    DIVIDE = "DIVIDE"  # DIVide
    DONTINCLUDE = "DONTINCLUDE"  # DONTInclude
    DOTS = "DOTS"  # DOTs
    EDGE = "EDGE"
    EITHER = "EITHER"
    # EITHER = "EITher"
    ENVELOPE = "ENVELOPE"  # ENVelope
    EOF = "EOF"
    EOP = "EOP"  # EOp
    EQUAL = "EQUAL"  # EQUal
    # EQUAL = "EQual"
    EQUALS = "EQUALS"  # Equals
    ERROR = "ERROR"  # ERRor
    EXECUTE = "EXECUTE"  # EXECute
    EXTENDED = "EXTENDED"
    # EXTENDED = "EXTENDed"
    # EXTENDED = "EXTended"
    EYEHISTOGRAM = "EYEHISTOGRAM"  # EYEhistogram
    FACTORY = "FACTORY"  # FACtory
    FALL = "FALL"
    FALLING = "FALLING"
    # FALLING = "FALling"
    FALLSLEWRATE = "FALLSLEWRATE"
    FALLTIME = "FALLTIME"
    FALSE = "FALSE"  # FALSe
    FAST = "FAST"
    FCDATA = "FCDATA"  # FCData
    FCDFIRST = "FCDFIRST"  # FCDFirst
    FCDTWO = "FCDTWO"  # FCDTwo
    FDBITS = "FDBITS"
    FDISO = "FDISO"
    FDNONISO = "FDNONISO"
    FFT = "FFT"
    FIFTY = "FIFTY"  # FIFTy
    # FIFTY = "FIFty"
    FILE = "FILE"
    FIRST = "FIRST"
    FIXED = "FIXED"
    FLATTOP2 = "FLATTOP2"
    FORCE = "FORCE"  # FORCe
    FORCETRIG = "FORCETRIG"  # FORCetrig
    FORMERROR = "FORMERROR"  # FORMERRor
    FORWARD = "FORWARD"  # FORWard
    FOUR = "FOUR"
    FOURTEENTEN = "FOURTEENTEN"  # FOURTEENten
    FP = "FP"
    FPBINARY = "FPBINARY"  # FPBinary
    FRAME = "FRAME"  # FRame
    FRAMELENGTH = "FRAMELENGTH"  # FRAMELENgth
    FRAMETYPE = "FRAMETYPE"  # FRAMEtype
    FULLSCREEN = "FULLSCREEN"  # FULLScreen
    GAUSSIAN = "GAUSSIAN"  # GAUSSian
    GLOBAL = "GLOBAL"  # GLOBal
    GPKNOB1 = "GPKNOB1"
    GPKNOB2 = "GPKNOB2"
    GRATICULE = "GRATICULE"
    GREATERTHAN = "GREATERTHAN"  # GREATERthan
    H = "H"
    HAMMING = "HAMMING"  # HAMMing
    HANNING = "HANNING"  # HANNing
    HBARS = "HBARS"  # HBArs
    HEX = "HEX"
    HFREJ = "HFREJ"  # HFRej
    HIGH = "HIGH"
    HIGHTIME = "HIGHTIME"
    HIGHZ = "HIGHZ"
    HIGH_Z = "HIGH_Z"
    HIRES = "HIRES"  # HIRes
    HOLD = "HOLD"
    HORIZONTAL = "HORIZONTAL"  # HORizontal
    HORIZONTALSCALE = "HORIZONTALSCALE"  # HORIZontalscale
    HORZPOS = "HORZPOS"
    I2C = "I2C"
    IDANDDATA = "IDANDDATA"
    IDENTIFIER = "IDENTIFIER"  # IDentifier
    IDLE = "IDLE"
    INCLUDE = "INCLUDE"  # INCLude
    INDEPENDENT = "INDEPENDENT"
    INFINITE = "INFINITE"  # INFInite
    INFPERSIST = "INFPERSIST"  # INFPersist
    INIT = "INIT"
    INRANGE = "INRANGE"  # INRange
    # INRANGE = "INrange"
    INSIDERANGE = "INSIDERANGE"  # INSIDErange
    INVERTED = "INVERTED"  # INVERTed
    # INVERTED = "INVErted"
    # INVERTED = "INVerted"
    JPG = "JPG"
    KAISERBESSEL = "KAISERBESSEL"  # KAISERBessel
    L = "L"
    LATCH = "LATCH"  # LATCh
    LESSEQUAL = "LESSEQUAL"  # LESSEQual
    LESSTHAN = "LESSTHAN"  # LESSthan
    LF = "LF"
    LFREJ = "LFREJ"  # LFRej
    LIN = "LIN"
    LINEAR = "LINEAR"
    # LINEAR = "LINEAr"
    # LINEAR = "LINear"
    LOG = "LOG"
    LOGIC = "LOGIC"  # LOGIc
    LOW = "LOW"
    LOWTIME = "LOWTIME"
    LSB = "LSB"
    MANUAL = "MANUAL"  # MANual
    MATH = "MATH"  # MATh
    MEAN = "MEAN"
    MEANHISTOGRAM = "MEANHISTOGRAM"  # MEANhistogram
    MEDIUM = "MEDIUM"  # MEDium
    MID = "MID"
    MINMAX = "MINMAX"  # MINMax
    MISO = "MISO"  # MISo
    MISODATA = "MISODATA"  # MISOdata
    MIXED = "MIXED"
    # MIXED = "MIXed"
    MIXEDASCII = "MIXEDASCII"
    MIXEDHEX = "MIXEDHEX"
    MODEHISTOGRAM = "MODEHISTOGRAM"  # MODEhistogram
    MOREEQUA = "MOREEQUA"  # MOREEQua
    MOREEQUAL = "MOREEQUAL"  # MOREEQual
    MORETHAN = "MORETHAN"  # MOREthan
    MOSI = "MOSI"  # MOSi
    MOSIDATA = "MOSIDATA"  # MOSIdata
    MOVEABLE = "MOVEABLE"
    MSB = "MSB"
    MULTIPLY = "MULTIPLY"  # MULTiply
    NAND = "NAND"  # NANd
    NDUTY = "NDUTY"  # NDUty
    NEGATIVE = "NEGATIVE"  # NEGative
    NO = "NO"
    NOCARE = "NOCARE"
    NOISEREJ = "NOISEREJ"  # NOISErej
    NOMINAL = "NOMINAL"  # NOMinal
    NOPARITY = "NOPARITY"  # NOPARity
    NOR = "NOR"
    NORMAL = "NORMAL"  # NORMal
    # NORMAL = "NORmal"
    NOTE = "NOTE"
    NOTEQUAL = "NOTEQUAL"  # NOTEQual
    NOTEQUALS = "NOTEQUALS"  # NOTEQuals
    NPERIOD = "NPERIOD"
    NULL = "NULL"  # NULl
    NUMACQS = "NUMACQS"  # NUMACQs
    OCCURS = "OCCURS"
    OFF = "OFF"
    ON = "ON"
    ONE = "ONE"
    OPPOSITEAS = "OPPOSITEAS"  # OPPositeas
    OR = "OR"
    OUTRANGE = "OUTRANGE"  # OUTRange
    # OUTRANGE = "OUTrange"
    OUTSIDE = "OUTSIDE"  # OUTside
    OUTSIDERANGE = "OUTSIDERANGE"  # OUTSIDErange
    OVERLAY = "OVERLAY"  # OVErlay
    OVERLOAD = "OVERLOAD"  # OVERLoad
    PACKET = "PACKET"
    PARALLEL = "PARALLEL"  # PARallel
    PARITY = "PARITY"  # PARity
    PARITYERROR = "PARITYERROR"  # PARItyerror
    PAUSE = "PAUSE"
    PDUTY = "PDUTY"
    PEAKDETECT = "PEAKDETECT"  # PEAKdetect
    PERCENT = "PERCENT"  # PERCent
    PERIOD = "PERIOD"
    PERSOURCE = "PERSOURCE"  # PERSource
    PHASE = "PHASE"
    PIXMAP = "PIXMAP"  # PIXmap
    PK2PK = "PK2PK"  # PK2Pk
    PNG = "PNG"
    POSITIVE = "POSITIVE"  # POSitive
    POST = "POST"
    POVERSHOOT = "POVERSHOOT"
    PROFILE = "PROFILE"  # PROFile
    PULSEWIDTH = "PULSEWIDTH"  # PULSEWidth
    PWIDTH = "PWIDTH"
    READ = "READ"
    RECORDLENGTH = "RECORDLENGTH"  # RECORDLength
    RECTANGLE = "RECTANGLE"
    RECTANGULAR = "RECTANGULAR"  # RECTANGular
    REF = "REF"
    REMOTE = "REMOTE"  # REMote
    REPEATSTART = "REPEATSTART"  # REPEATstart
    RESOLUTION = "RESOLUTION"  # RESOlution
    RFVSTIME = "RFVSTIME"  # RFvsTime
    RI = "RI"
    RIBINARY = "RIBINARY"  # RIBinary
    RISE = "RISE"
    # RISE = "RISe"
    RISESLEWRATE = "RISESLEWRATE"
    RISETIME = "RISETIME"
    RISING = "RISING"
    # RISING = "RISing"
    RMS = "RMS"
    RP = "RP"
    RPBINARY = "RPBINARY"  # RPBinary
    RS232C = "RS232C"
    RUNSTOP = "RUNSTOP"  # RUNSTop
    RUNT = "RUNT"
    # RUNT = "RUNt"
    RXDATA = "RXDATA"  # RXData
    SAME = "SAME"
    SAMEAS = "SAMEAS"  # SAMEas
    SAMPLE = "SAMPLE"  # SAMple
    SCREEN = "SCREEN"
    SDATA = "SDATA"  # SDATa
    SEARCH1 = "SEARCH1"
    SEARCHTOTRIGGER = "SEARCHTOTRIGGER"  # SEARCHtotrigger
    SEGMENTS = "SEGMENTS"  # SEGments
    SENT = "SENT"
    SEQUENCE = "SEQUENCE"  # SEQuence
    SERVICE = "SERVICE"
    SETHOLD = "SETHOLD"  # SETHold
    SETLEVEL = "SETLEVEL"  # SETLevel
    SETTO50 = "SETTO50"
    SETUP = "SETUP"
    SFPBINARY = "SFPBINARY"  # SFPbinary
    SINC = "SINC"
    SINGLESEQ = "SINGLESEQ"  # SINGleseq
    SINX = "SINX"
    SIX = "SIX"
    SIXTEENEIGHT = "SIXTEENEIGHT"  # SIXTEENeight
    SKEW = "SKEW"
    SLEEP = "SLEEP"
    SLOW = "SLOW"
    SNAP = "SNAP"  # SNAp
    SOF = "SOF"
    SPACE = "SPACE"  # SPace
    SPECTRAL = "SPECTRAL"  # SPECtral
    SPI = "SPI"
    SPLIT = "SPLIT"
    SRIBINARY = "SRIBINARY"  # SRIbinary
    SRPBINARY = "SRPBINARY"  # SRPbinary
    SS = "SS"
    STACKED = "STACKED"  # STAcked
    STANDARD = "STANDARD"  # STandard
    START = "START"
    # START = "STARt"
    STARTOFFRAME = "STARTOFFRAME"  # STARTofframe
    STAYSHIGH = "STAYSHIGH"  # STAYSHigh
    STAYSLOW = "STAYSLOW"  # STAYSLow
    STOP = "STOP"
    SUBTRACT = "SUBTRACT"  # SUBtract
    SYNC = "SYNC"
    SYNCFIELD = "SYNCFIELD"  # SYNCfield
    TEKEXPONENTIAL = "TEKEXPONENTIAL"  # TEKEXPonential
    TEMPERATURE = "TEMPERATURE"  # TEMPerature
    TENNINETY = "TENNINETY"  # TENNinety
    THREE = "THREE"
    TIMEOUT = "TIMEOUT"  # TIMEOut
    TIMEOUTSIDELEVEL = "TIMEOUTSIDELEVEL"
    TIMETOMAX = "TIMETOMAX"
    TIMETOMIN = "TIMETOMIN"
    TOGGLE = "TOGGLE"
    TOLERANCES = "TOLERANCES"  # TOLerances
    TOP = "TOP"
    TOUCHSCREEN = "TOUCHSCREEN"  # TOUCHSCReen
    TRACK = "TRACK"
    TRANSITION = "TRANSITION"  # TRANsition
    TRIGGERTOSEARCH = "TRIGGERTOSEARCH"  # TRIGgertosearch
    TRIGMODE = "TRIGMODE"  # TRIGMode
    TRUE = "TRUE"  # TRUe
    TWELVETWELVE = "TWELVETWELVE"  # TWELVEtwelve
    TWENTYEIGHTY = "TWENTYEIGHTY"  # TWENtyeighty
    TWO = "TWO"
    TXDATA = "TXDATA"  # TXData
    UNEQUAL = "UNEQUAL"  # UNEQual
    UNIQUE = "UNIQUE"  # UNIQue
    USBTMC = "USBTMC"  # USBTmc
    USER = "USER"
    V1X = "V1X"
    V2X = "V2X"
    VBARS = "VBARS"  # VBArs
    VECTOR = "VECTOR"  # VECtor
    VECTORS = "VECTORS"  # VECtors
    VERTICAL = "VERTICAL"  # VERTical
    VERTPOS = "VERTPOS"
    VERTSCALE = "VERTSCALE"
    VISIBILITY = "VISIBILITY"  # VISIBility
    WAKEUP = "WAKEUP"  # WAKEup
    WAVEFORM = "WAVEFORM"
    # WAVEFORM = "WAVEform"
    WIDTH = "WIDTH"  # WIDth
    WITHIN = "WITHIN"  # WIThin
    WRITE = "WRITE"
    X = "X"
    XFF = "XFF"
    YES = "YES"
    ZERO = "ZERO"  # ZERo


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class MSO2Commands:
    """The MSO2 commands.

    This provides access to all the commands for the MSO2 device. See the documentation of each
    property for more usage information.

    Properties:
        - ``.acquire``: The ``ACQuire`` command.
        - ``.actonevent``: The ``ACTONEVent`` command tree.
        - ``.afg``: The ``AFG`` command tree.
        - ``.alias``: The ``ALIas`` command.
        - ``.allev``: The ``ALLEv`` command.
        - ``.autosavepitimeout``: The ``AUTOSAVEPITIMEOUT`` command.
        - ``.autosaveuitimeout``: The ``AUTOSAVEUITIMEOUT`` command.
        - ``.autoset``: The ``AUTOSet`` command.
        - ``.auxout``: The ``AUXout`` command tree.
        - ``.battery``: The ``BATTery`` command tree.
        - ``.bus``: The ``BUS`` command tree.
        - ``.bustable``: The ``BUSTABle`` command tree.
        - ``.busy``: The ``BUSY`` command.
        - ``.cal``: The ``*CAL`` command.
        - ``.calibrate``: The ``CALibrate`` command.
        - ``.callouts``: The ``CALLOUTS`` command tree.
        - ``.ch``: The ``CH<x>`` command.
        - ``.clear``: The ``CLEAR`` command.
        - ``.cls``: The ``*CLS`` command.
        - ``.configuration``: The ``CONFIGuration`` command tree.
        - ``.connected``: The ``CONNected`` command tree.
        - ``.curve``: The ``CURVe`` command.
        - ``.curvestream``: The ``CURVEStream`` command.
        - ``.customtable``: The ``CUSTOMTABle`` command tree.
        - ``.data``: The ``DATa`` command.
        - ``.date``: The ``DATE`` command.
        - ``.dch``: The ``DCH<x>`` command tree.
        - ``.ddt``: The ``*DDT`` command.
        - ``.dese``: The ``DESE`` command.
        - ``.diag``: The ``DIAg`` command tree.
        - ``.display``: The ``DISplay`` command.
        - ``.ese``: The ``*ESE`` command.
        - ``.esr``: The ``*ESR`` command.
        - ``.ethernet``: The ``ETHERnet`` command tree.
        - ``.event``: The ``EVENT`` command.
        - ``.evmsg``: The ``EVMsg`` command.
        - ``.evqty``: The ``EVQty`` command.
        - ``.factory``: The ``FACtory`` command.
        - ``.filesystem``: The ``FILESystem`` command.
        - ``.fpanel``: The ``FPAnel`` command tree.
        - ``.header``: The ``HEADer`` command.
        - ``.horizontal``: The ``HORizontal`` command.
        - ``.id``: The ``ID`` command.
        - ``.idn``: The ``*IDN`` command.
        - ``.lic``: The ``LIC`` command tree.
        - ``.license``: The ``LICense`` command.
        - ``.lock``: The ``LOCk`` command.
        - ``.lrn``: The ``*LRN`` command.
        - ``.mainwindow``: The ``MAINWindow`` command tree.
        - ``.mask``: The ``MASK`` command tree.
        - ``.math``: The ``MATH`` command tree.
        - ``.meastable``: The ``MEASTABle`` command tree.
        - ``.measurement``: The ``MEASUrement`` command.
        - ``.newpass``: The ``NEWpass`` command.
        - ``.opc``: The ``*OPC`` command.
        - ``.opt``: The ``*OPT`` command.
        - ``.password``: The ``PASSWord`` command.
        - ``.pause``: The ``PAUSe`` command.
        - ``.pg``: The ``PG`` command tree.
        - ``.plot``: The ``PLOT`` command tree.
        - ``.power``: The ``POWer`` command tree.
        - ``.psc``: The ``*PSC`` command.
        - ``.pud``: The ``*PUD`` command.
        - ``.recall``: The ``RECAll`` command tree.
        - ``.ref``: The ``REF`` command tree.
        - ``.rem``: The ``REM`` command.
        - ``.rosc``: The ``ROSc`` command tree.
        - ``.rst``: The ``*RST`` command.
        - ``.save``: The ``SAVe`` command tree.
        - ``.saveon``: The ``SAVEON`` command tree.
        - ``.saveonevent``: The ``SAVEONEVent`` command tree.
        - ``.search``: The ``SEARCH`` command tree.
        - ``.select``: The ``SELect`` command tree.
        - ``.set``: The ``SET`` command.
        - ``.socketserver``: The ``SOCKETServer`` command tree.
        - ``.sre``: The ``*SRE`` command.
        - ``.stb``: The ``*STB`` command.
        - ``.teksecure``: The ``TEKSecure`` command.
        - ``.time``: The ``TIMe`` command.
        - ``.totaluptime``: The ``TOTaluptime`` command.
        - ``.touchscreen``: The ``TOUCHSCReen`` command tree.
        - ``.trg``: The ``*TRG`` command.
        - ``.trigger``: The ``TRIGger`` command.
        - ``.tst``: The ``*TST`` command.
        - ``.undo``: The ``UNDO`` command.
        - ``.unlock``: The ``UNLock`` command.
        - ``.usbdevice``: The ``USBDevice`` command tree.
        - ``.verbose``: The ``VERBose`` command.
        - ``.vertical``: The ``VERTical`` command tree.
        - ``.vxi``: The ``VXI`` command tree.
        - ``.wai``: The ``*WAI`` command.
        - ``.wavfrm``: The ``WAVFrm`` command.
        - ``.wfmoutpre``: The ``WFMOutpre`` command.
    """

    # pylint: disable=too-many-statements
    def __init__(self, device: Optional[PIControl] = None) -> None:  # noqa: PLR0915
        self._acquire = Acquire(device)
        self._actonevent = Actonevent(device)
        self._afg = Afg(device)
        self._alias = Alias(device)
        self._allev = Allev(device)
        self._autosavepitimeout = Autosavepitimeout(device)
        self._autosaveuitimeout = Autosaveuitimeout(device)
        self._autoset = Autoset(device)
        self._auxout = Auxout(device)
        self._battery = Battery(device)
        self._bus = Bus(device)
        self._bustable = Bustable(device)
        self._busy = Busy(device)
        self._cal = Cal(device)
        self._calibrate = Calibrate(device)
        self._callouts = Callouts(device)
        self._ch: Dict[int, Channel] = DefaultDictPassKeyToFactory(
            lambda x: Channel(device, f"CH{x}")
        )
        self._clear = Clear(device)
        self._cls = Cls(device)
        self._configuration = Configuration(device)
        self._connected = Connected(device)
        self._curve = Curve(device)
        self._curvestream = Curvestream(device)
        self._customtable = Customtable(device)
        self._data = Data(device)
        self._date = Date(device)
        self._dch: Dict[int, DchItem] = DefaultDictPassKeyToFactory(
            lambda x: DchItem(device, f"DCH{x}")
        )
        self._ddt = Ddt(device)
        self._dese = Dese(device)
        self._diag = Diag(device)
        self._display = Display(device)
        self._ese = Ese(device)
        self._esr = Esr(device)
        self._ethernet = Ethernet(device)
        self._event = Event(device)
        self._evmsg = Evmsg(device)
        self._evqty = Evqty(device)
        self._factory = Factory(device)
        self._filesystem = Filesystem(device)
        self._fpanel = Fpanel(device)
        self._header = Header(device)
        self._horizontal = Horizontal(device)
        self._id = Id(device)
        self._idn = Idn(device)
        self._lic = Lic(device)
        self._license = License(device)
        self._lock = Lock(device)
        self._lrn = Lrn(device)
        self._mainwindow = Mainwindow(device)
        self._mask = Mask(device)
        self._math = Math(device)
        self._meastable = Meastable(device)
        self._measurement = Measurement(device)
        self._newpass = Newpass(device)
        self._opc = Opc(device)
        self._opt = Opt(device)
        self._password = Password(device)
        self._pause = Pause(device)
        self._pg = Pg(device)
        self._plot = Plot(device)
        self._power = Power(device)
        self._psc = Psc(device)
        self._pud = Pud(device)
        self._recall = Recall(device)
        self._ref = Ref(device)
        self._rem = Rem(device)
        self._rosc = Rosc(device)
        self._rst = Rst(device)
        self._save = Save(device)
        self._saveon = Saveon(device)
        self._saveonevent = Saveonevent(device)
        self._search = Search(device)
        self._select = Select(device)
        self._set = Set(device)
        self._socketserver = Socketserver(device)
        self._sre = Sre(device)
        self._stb = Stb(device)
        self._teksecure = Teksecure(device)
        self._time = Time(device)
        self._totaluptime = Totaluptime(device)
        self._touchscreen = Touchscreen(device)
        self._trg = Trg(device)
        self._trigger = Trigger(device)
        self._tst = Tst(device)
        self._undo = Undo(device)
        self._unlock = Unlock(device)
        self._usbdevice = Usbdevice(device)
        self._verbose = Verbose(device)
        self._vertical = Vertical(device)
        self._vxi = Vxi(device)
        self._wai = Wai(device)
        self._wavfrm = Wavfrm(device)
        self._wfmoutpre = Wfmoutpre(device)

    @property
    def acquire(self) -> Acquire:
        """Return the ``ACQuire`` command.

        Description:
            - Queries the current acquisition state.

        Usage:
            - Using the ``.query()`` method will send the ``ACQuire?`` query.
            - Using the ``.verify(value)`` method will send the ``ACQuire?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ACQuire?
            ```

        Sub-properties:
            - ``.fastacq``: The ``ACQuire:FASTAcq`` command tree.
            - ``.maxsamplerate``: The ``ACQuire:MAXSamplerate`` command.
            - ``.mode``: The ``ACQuire:MODe`` command.
            - ``.numacq``: The ``ACQuire:NUMACq`` command.
            - ``.numavg``: The ``ACQuire:NUMAVg`` command.
            - ``.sequence``: The ``ACQuire:SEQuence`` command tree.
            - ``.state``: The ``ACQuire:STATE`` command.
            - ``.stopafter``: The ``ACQuire:STOPAfter`` command.
        """
        return self._acquire

    @property
    def actonevent(self) -> Actonevent:
        """Return the ``ACTONEVent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``ACTONEVent:ENable`` command.
            - ``.limitcount``: The ``ACTONEVent:LIMITCount`` command.
            - ``.limit``: The ``ACTONEVent:LIMit`` command.
            - ``.maskfail``: The ``ACTONEVent:MASKFail`` command tree.
            - ``.maskhit``: The ``ACTONEVent:MASKHit`` command tree.
            - ``.maskpass``: The ``ACTONEVent:MASKPass`` command tree.
            - ``.measurement``: The ``ACTONEVent:MEASUrement`` command tree.
            - ``.search``: The ``ACTONEVent:SEARCH`` command tree.
            - ``.trigger``: The ``ACTONEVent:TRIGger`` command tree.
        """
        return self._actonevent

    @property
    def afg(self) -> Afg:
        """Return the ``AFG`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFG?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``AFG:AMPLitude`` command.
            - ``.arbitrary``: The ``AFG:ARBitrary`` command tree.
            - ``.burst``: The ``AFG:BURSt`` command tree.
            - ``.frequency``: The ``AFG:FREQuency`` command.
            - ``.function``: The ``AFG:FUNCtion`` command.
            - ``.highlevel``: The ``AFG:HIGHLevel`` command.
            - ``.lowlevel``: The ``AFG:LOWLevel`` command.
            - ``.noiseadd``: The ``AFG:NOISEAdd`` command tree.
            - ``.offset``: The ``AFG:OFFSet`` command.
            - ``.output``: The ``AFG:OUTPut`` command tree.
            - ``.period``: The ``AFG:PERIod`` command.
            - ``.pulse``: The ``AFG:PULse`` command tree.
            - ``.ramp``: The ``AFG:RAMP`` command tree.
            - ``.square``: The ``AFG:SQUare`` command tree.
        """
        return self._afg

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
    def autosavepitimeout(self) -> Autosavepitimeout:
        """Return the ``AUTOSAVEPITIMEOUT`` command.

        Description:
            - This command sets or queries the idle time from the programmable interface before
              auto-save occurs.

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSAVEPITIMEOUT?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSAVEPITIMEOUT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUTOSAVEPITIMEOUT value`` command.

        SCPI Syntax:
            ```
            - AUTOSAVEPITIMEOUT <NR1>
            - AUTOSAVEPITIMEOUT?
            ```

        Info:
            - ``<NR1>``
        """
        return self._autosavepitimeout

    @property
    def autosaveuitimeout(self) -> Autosaveuitimeout:
        """Return the ``AUTOSAVEUITIMEOUT`` command.

        Description:
            - This command sets or queries the idle time from the user interface before auto-save
              occurs.

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSAVEUITIMEOUT?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSAVEUITIMEOUT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUTOSAVEUITIMEOUT value`` command.

        SCPI Syntax:
            ```
            - AUTOSAVEUITIMEOUT <NR1>
            - AUTOSAVEUITIMEOUT?
            ```

        Info:
            - ``<NR1>``
        """
        return self._autosaveuitimeout

    @property
    def autoset(self) -> Autoset:
        """Return the ``AUTOSet`` command.

        Description:
            - This command (no query format) sets the vertical, horizontal, and trigger controls of
              the instrument to automatically acquire and display the selected waveform.

        Usage:
            - Using the ``.write(value)`` method will send the ``AUTOSet value`` command.

        SCPI Syntax:
            ```
            - AUTOSet EXECute
            ```

        Info:
            - ``EXECute`` autosets the displayed waveform; this is equivalent to pressing the front
              panel Autoset button.

        Sub-properties:
            - ``.acquisition``: The ``AUTOSet:ACQuisition`` command tree.
            - ``.enable``: The ``AUTOSet:ENAble`` command.
            - ``.horizontal``: The ``AUTOSet:HORizontal`` command tree.
            - ``.trigger``: The ``AUTOSet:TRIGger`` command tree.
            - ``.vertical``: The ``AUTOSet:VERTical`` command tree.
        """
        return self._autoset

    @property
    def auxout(self) -> Auxout:
        """Return the ``AUXout`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AUXout?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXout?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``AUXout:EDGE`` command.
            - ``.source``: The ``AUXout:SOUrce`` command.
        """
        return self._auxout

    @property
    def battery(self) -> Battery:
        """Return the ``BATTery`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BATTery?`` query.
            - Using the ``.verify(value)`` method will send the ``BATTery?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.acpower``: The ``BATTery:ACPOWer`` command.
            - ``.slot``: The ``BATTery:SLOT<1,2>`` command tree.
        """
        return self._battery

    @property
    def bus(self) -> Bus:
        """Return the ``BUS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.addnew``: The ``BUS:ADDNew`` command.
            - ``.b``: The ``BUS:B<x>`` command tree.
            - ``.delete``: The ``BUS:DELete`` command.
            - ``.list``: The ``BUS:LIST`` command.
        """
        return self._bus

    @property
    def bustable(self) -> Bustable:
        """Return the ``BUSTABle`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUSTABle?`` query.
            - Using the ``.verify(value)`` method will send the ``BUSTABle?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.addnew``: The ``BUSTABle:ADDNew`` command.
            - ``.delete``: The ``BUSTABle:DELete`` command.
            - ``.list``: The ``BUSTABle:LIST`` command.
        """
        return self._bustable

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
            - ``.internal``: The ``CALibrate:INTERNal`` command.
            - ``.pwrupstatus``: The ``CALibrate:PWRUpstatus`` command.
        """
        return self._calibrate

    @property
    def callouts(self) -> Callouts:
        """Return the ``CALLOUTS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS?`` query.
            - Using the ``.verify(value)`` method will send the ``CALLOUTS?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.addnew``: The ``CALLOUTS:ADDNew`` command.
            - ``.callout``: The ``CALLOUTS:CALLOUT<x>`` command tree.
            - ``.delete``: The ``CALLOUTS:DELete`` command.
        """
        return self._callouts

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
            - ``.bandwidth``: The ``CH<x>:BANdwidth`` command.
            - ``.clipping``: The ``CH<x>:CLIPping`` command.
            - ``.coupling``: The ``CH<x>:COUPling`` command.
            - ``.deskew``: The ``CH<x>:DESKew`` command.
            - ``.ditherrange``: The ``CH<x>:DITHERrange`` command.
            - ``.invert``: The ``CH<x>:INVert`` command.
            - ``.label``: The ``CH<x>:LABel`` command tree.
            - ``.offset``: The ``CH<x>:OFFSet`` command.
            - ``.position``: The ``CH<x>:POSition`` command.
            - ``.probefunc``: The ``CH<x>:PROBEFunc`` command tree.
            - ``.scaleratio``: The ``CH<x>:SCALERATio`` command.
            - ``.scale``: The ``CH<x>:SCAle`` command.
            - ``.termination``: The ``CH<x>:TERmination`` command.
            - ``.vterm``: The ``CH<x>:VTERm`` command tree.
        """
        return self._ch

    @property
    def clear(self) -> Clear:
        """Return the ``CLEAR`` command.

        Description:
            - This command clears acquisitions, measurements, and waveforms.

        Usage:
            - Using the ``.write()`` method will send the ``CLEAR`` command.

        SCPI Syntax:
            ```
            - CLEAR
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
    def configuration(self) -> Configuration:
        """Return the ``CONFIGuration`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.analog``: The ``CONFIGuration:ANALOg`` command tree.
        """
        return self._configuration

    @property
    def connected(self) -> Connected:
        """Return the ``CONNected`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONNected?`` query.
            - Using the ``.verify(value)`` method will send the ``CONNected?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.requested``: The ``CONNected:REQUested`` command tree.
            - ``.status``: The ``CONNected:STATus`` command.
            - ``.usage``: The ``CONNected:USAGe`` command tree.
        """
        return self._connected

    @property
    def curve(self) -> Curve:
        """Return the ``CURVe`` command.

        Description:
            - This command transfers waveform data from the instrument. Each waveform that is
              transferred has an associated waveform preamble that contains information such as data
              format and scale. The ``CURVe?`` query transfers data from the instrument. The data
              source is specified by the ``DATA:SOURCE`` command. The first and last data points are
              specified by the ``DATA:START`` and ``DATA:STOP`` commands. For digital sources,
              ``CH<x>_D<x>`` or CH<x> _DALL, when the ``:DATa:WIDth`` is 1, the returned data is
              state only. When the ``:DATa:WIDth`` is 2, the returned data is transition data with 2
              bits per digital channel representing the transition information as follows: 0 0 low 0
              1 high 1 1 multiple transitions in interval ending with high 1 0 multiple transitions
              in interval ending with low For individual digital channels (such as ``CH<x>_D<x>`` ),
              ``:DATa:WIDth 2`` provides the 2-bit transition data with the upper 14 bits zero.
              ``:DATa:WIDth 1`` provides only the state in the LSB with the upper 7 bits all zero.
              For ``CH<x>_DAll`` sources, ``:DATa:WIDth 2`` provides the 2-bit transition data for
              each of the 8 constituent channels with the D7 bit represented in the 2 most
              significant bits, D6 in the next 2, and so on. ``:DATa:WIDth 1`` provides the states
              of each of the 8 constituent channels with D7 represented in the most significant bit
              and D0 in the least significant bit. Depending on the sample rate, multi-transition
              data may not be available and ``:CURVe?`` queries for digital channels with
              ``:DATa:WIDth 2`` may result in a warning event 'Execution warning: Multi-transition
              data not available'. In this case, the transition data returned will be 0 0 or 0 1.
              For MATH sources, only 8-byte double precision floating point data is returned in
              ``:CURVe?`` queries. A Fast Acquisition waveform Pixmap data is a 500 (vertical) by
              1000 (horizontal) point bitmap. Each point represents display intensity for that
              screen location. 500 (vertical) which is the row count in the bitmap, might vary based
              on how many channels enabled from same FastAcq group. To query and get the Fast Acq
              Pixel Map data, the following command set should be sent: ``ACQuire:FASTAcq:STATE ON``
              ``DATA:MODe PIXmap`` When the FastAcq is on, Curve? on Ch<x> will return pixmap data
              (if ``DATA:MODe`` is PIXmap). The number of rows in the pixmap will vary based on how
              many ch<x> sources are turned on and how they are grouped in acquisition HW. The
              grouping can vary from model to model. The number of columns in pixmap data is fixed
              to 1000. For example, on a MSO58 instrument, Ch1 to Ch4 is 'group1' and Ch5 to Ch8 is
              'group2'. If Ch1 is turned on (in group1) then Ch1 rows will be 500. If Ch2 and Ch3
              are turned on (in group1) then Ch2 and Ch3 rows will be 250 each. When all Ch1/2/3/4
              are turned on (in group1) then 125 rows per channel. If Ch1 (in group1) and Ch8 (in
              group2) are turned on then 500 rows will be returned for each channel. To calculate
              the number of rows, you can use- (number of bytes from curve header/``BYT_NR``)/1000.

        Usage:
            - Using the ``.query()`` method will send the ``CURVe?`` query.
            - Using the ``.verify(value)`` method will send the ``CURVe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURVe?
            ```
        """
        return self._curve

    @property
    def curvestream(self) -> Curvestream:
        """Return the ``CURVEStream`` command.

        Description:
            - This query-only command continuously transfers waveform data from the instrument as it
              is acquired. This command puts the instrument into a streaming data mode, allowing the
              controller to receive waveform records as fast as they are acquired. Use the
              ``DATA:SOURCE`` command to specify the waveform sources. The command supports all the
              same data formatting options as the CURVE command. Control of the instrument through
              the user interface or other external clients is not allowed while in streaming data
              mode. The GPIB controller must take the instrument out of this streaming data mode to
              terminate the query and allow other input sources to resume communication with the
              instrument. The following options are available to transition out of streaming data
              mode: Send a device clear over the bus Send another command or query to the instrument
              Turning the waveform screen display mode off ( ``:DISplay:WAVEform OFF`` ) may
              increase waveform throughput during streaming mode. Using a data encoding of SRIbinary
              ( ``DATa:ENCdg SRIbinary`` ) may also increase the waveform throughput since that is
              the raw native data format of the oscilloscope. While in streaming data mode, two
              extreme conditions can occur. If the waveform records are being acquired slowly (high
              resolution), configure the controller for a long time-out threshold, as the data is
              not sent out until each complete record is acquired. If the waveform records are being
              acquired rapidly (low resolution), and the controller is not reading the data off the
              bus fast enough, the trigger rate is slowed to allow each waveform to be sent
              sequentially.

        Usage:
            - Using the ``.query()`` method will send the ``CURVEStream?`` query.
            - Using the ``.verify(value)`` method will send the ``CURVEStream?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CURVEStream?
            ```
        """
        return self._curvestream

    @property
    def customtable(self) -> Customtable:
        """Return the ``CUSTOMTABle`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CUSTOMTABle?`` query.
            - Using the ``.verify(value)`` method will send the ``CUSTOMTABle?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.addnew``: The ``CUSTOMTABle:ADDNew`` command.
            - ``.delete``: The ``CUSTOMTABle:DELete`` command.
            - ``.list``: The ``CUSTOMTABle:LIST`` command.
        """
        return self._customtable

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
            - ``.encdg``: The ``DATa:ENCdg`` command.
            - ``.mode``: The ``DATa:MODe`` command.
            - ``.resample``: The ``DATa:RESample`` command.
            - ``.source``: The ``DATa:SOUrce`` command.
            - ``.start``: The ``DATa:STARt`` command.
            - ``.stop``: The ``DATa:STOP`` command.
            - ``.width``: The ``DATa:WIDth`` command.
        """
        return self._data

    @property
    def date(self) -> Date:
        """Return the ``DATE`` command.

        Description:
            - This command queries the date that the instrument displays.

        Usage:
            - Using the ``.query()`` method will send the ``DATE?`` query.
            - Using the ``.verify(value)`` method will send the ``DATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DATE?
            ```
        """
        return self._date

    @property
    def dch(self) -> Dict[int, DchItem]:
        """Return the ``DCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DCH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.

        Sub-properties:
            - ``.d``: The ``DCH<x>_D<x>`` command tree.
        """
        return self._dch

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
            - ``.loop``: The ``DIAg:LOOP`` command tree.
            - ``.mode``: The ``DIAg:MODe`` command.
            - ``.result``: The ``DIAg:RESUlt`` command.
            - ``.select``: The ``DIAg:SELect`` command.
            - ``.state``: The ``DIAg:STATE`` command.
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
            - ``.colors``: The ``DISplay:COLors`` command.
            - ``.global``: The ``DISplay:GLObal`` command tree.
            - ``.intensity``: The ``DISplay:INTENSITy`` command.
            - ``.mathfftview1``: The ``DISplay:MATHFFTView1`` command tree.
            - ``.persistence``: The ``DISplay:PERSistence`` command.
            - ``.plotview1``: The ``DISplay:PLOTView1`` command tree.
            - ``.reffftview``: The ``DISplay:REFFFTView<x>`` command tree.
            - ``.select``: The ``DISplay:SELect`` command tree.
            - ``.varpersist``: The ``DISplay:VARpersist`` command.
            - ``.waveview``: The ``DISplay:WAVEView`` command tree.
            - ``.waveview1``: The ``DISplay:WAVEView1`` command tree.
            - ``.waveform``: The ``DISplay:WAVEform`` command.
            - ``.ch``: The ``DISplay:CH<x>`` command tree.
            - ``.math``: The ``DISplay:Math<x>`` command tree.
            - ``.ref``: The ``DISplay:REF<x>`` command tree.
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
    def ethernet(self) -> Ethernet:
        """Return the ``ETHERnet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dhcpbootp``: The ``ETHERnet:DHCPbootp`` command.
            - ``.dns``: The ``ETHERnet:DNS`` command tree.
            - ``.domainname``: The ``ETHERnet:DOMAINname`` command.
            - ``.enet``: The ``ETHERnet:ENET`` command tree.
            - ``.gateway``: The ``ETHERnet:GATEWay`` command tree.
            - ``.ipaddress``: The ``ETHERnet:IPADDress`` command.
            - ``.lxi``: The ``ETHERnet:LXI`` command tree.
            - ``.name``: The ``ETHERnet:NAME`` command.
            - ``.networkconfig``: The ``ETHERnet:NETWORKCONFig`` command.
            - ``.ping``: The ``ETHERnet:PING`` command.
            - ``.subnetmask``: The ``ETHERnet:SUBNETMask`` command.
        """
        return self._ethernet

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
            - ``.homedir``: The ``FILESystem:HOMEDir`` command.
            - ``.ldir``: The ``FILESystem:LDIR`` command.
            - ``.mkdir``: The ``FILESystem:MKDir`` command.
            - ``.mount``: The ``FILESystem:MOUNT`` command tree.
            - ``.readfile``: The ``FILESystem:READFile`` command.
            - ``.rename``: The ``FILESystem:REName`` command.
            - ``.rmdir``: The ``FILESystem:RMDir`` command.
            - ``.tekdrive``: The ``FILESystem:TEKDrive`` command tree.
            - ``.unmount``: The ``FILESystem:UNMOUNT`` command tree.
            - ``.writefile``: The ``FILESystem:WRITEFile`` command.
        """
        return self._filesystem

    @property
    def fpanel(self) -> Fpanel:
        """Return the ``FPAnel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``FPAnel?`` query.
            - Using the ``.verify(value)`` method will send the ``FPAnel?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.press``: The ``FPAnel:PRESS`` command.
            - ``.turn``: The ``FPAnel:TURN`` command.
        """
        return self._fpanel

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
            - ``.delay``: The ``HORizontal:DELay`` command tree.
            - ``.divisions``: The ``HORizontal:DIVisions`` command.
            - ``.main``: The ``HORizontal:MAIn`` command tree.
            - ``.mode``: The ``HORizontal:MODE`` command.
            - ``.position``: The ``HORizontal:POSition`` command.
            - ``.previewstate``: The ``HORizontal:PREViewstate`` command.
            - ``.recordlength``: The ``HORizontal:RECOrdlength`` command.
            - ``.samplerate``: The ``HORizontal:SAMPLERate`` command.
            - ``.scale``: The ``HORizontal:SCAle`` command.
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
    def lic(self) -> Lic:
        """Return the ``LIC`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``LIC?`` query.
            - Using the ``.verify(value)`` method will send the ``LIC?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.uninstall``: The ``LIC:UNINSTALL`` command.
        """
        return self._lic

    @property
    def license(self) -> License:
        """Return the ``LICense`` command.

        Description:
            - This query-only command returns all license parameters.

        Usage:
            - Using the ``.query()`` method will send the ``LICense?`` query.
            - Using the ``.verify(value)`` method will send the ``LICense?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - LICense?
            ```

        Sub-properties:
            - ``.appid``: The ``LICense:APPID`` command.
            - ``.count``: The ``LICense:COUNt`` command.
            - ``.error``: The ``LICense:ERRor`` command.
            - ``.gmt``: The ``LICense:GMT`` command.
            - ``.hid``: The ``LICense:HID`` command.
            - ``.install``: The ``LICense:INSTall`` command.
            - ``.item``: The ``LICense:ITEM`` command.
            - ``.list``: The ``LICense:LIST`` command.
            - ``.validate``: The ``LICense:VALidate`` command.
        """
        return self._license

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
    def mainwindow(self) -> Mainwindow:
        """Return the ``MAINWindow`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MAINWindow?`` query.
            - Using the ``.verify(value)`` method will send the ``MAINWindow?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.badge``: The ``MAINWindow:BADGe`` command tree.
            - ``.fontsize``: The ``MAINWindow:FONTSize`` command.
            - ``.rrbdisplaystate``: The ``MAINWindow:RRBDisplaystate`` command.
        """
        return self._mainwindow

    @property
    def mask(self) -> Mask:
        """Return the ``MASK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delete``: The ``MASK:DELete`` command.
            - ``.mask``: The ``MASK:MASK<x>`` command tree.
            - ``.test``: The ``MASK:TESt`` command tree.
        """
        return self._mask

    @property
    def math(self) -> Math:
        """Return the ``MATH`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.addnew``: The ``MATH:ADDNew`` command.
            - ``.delete``: The ``MATH:DELete`` command.
            - ``.list``: The ``MATH:LIST`` command.
            - ``.math``: The ``MATH:MATH<x>`` command tree.
        """
        return self._math

    @property
    def meastable(self) -> Meastable:
        """Return the ``MEASTABle`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASTABle?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASTABle?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.addnew``: The ``MEASTABle:ADDNew`` command.
            - ``.delete``: The ``MEASTABle:DELETE`` command.
        """
        return self._meastable

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
            - ``.addmeas``: The ``MEASUrement:ADDMEAS`` command.
            - ``.addnew``: The ``MEASUrement:ADDNew`` command.
            - ``.annotate``: The ``MEASUrement:ANNOTate`` command.
            - ``.ch``: The ``MEASUrement:CH<x>`` command tree.
            - ``.deleteall``: The ``MEASUrement:DELETEALL`` command.
            - ``.delete``: The ``MEASUrement:DELete`` command.
            - ``.edge``: The ``MEASUrement:EDGE<x>`` command.
            - ``.gating``: The ``MEASUrement:GATing`` command.
            - ``.interp``: The ``MEASUrement:INTERp`` command.
            - ``.list``: The ``MEASUrement:LIST`` command.
            - ``.math``: The ``MEASUrement:MATH<x>`` command tree.
            - ``.meas``: The ``MEASUrement:MEAS<x>`` command tree.
            - ``.ref``: The ``MEASUrement:REF<x>`` command tree.
            - ``.reflevels``: The ``MEASUrement:REFLevels`` command tree.
            - ``.statistics``: The ``MEASUrement:STATIstics`` command tree.
        """
        return self._measurement

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
    def pause(self) -> Pause:
        """Return the ``PAUSe`` command.

        Description:
            - This command causes the interface to pause the specified number of seconds before
              processing any other commands.

        Usage:
            - Using the ``.write(value)`` method will send the ``PAUSe value`` command.

        SCPI Syntax:
            ```
            - PAUSe <NR3>
            ```

        Info:
            - ``<NR3>`` is the specified number of seconds the interface is to pause before
              processing any other commands. The pause time is specified as a floating point value
              in seconds and must be > 0.0 and ≥1800.0.
        """
        return self._pause

    @property
    def pg(self) -> Pg:
        """Return the ``PG`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PG?`` query.
            - Using the ``.verify(value)`` method will send the ``PG?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``PG:AMPlitude`` command.
            - ``.bit``: The ``PG:BIT`` command tree.
            - ``.bitrate``: The ``PG:BITRate`` command.
            - ``.burst``: The ``PG:BURSt`` command tree.
            - ``.file``: The ``PG:FILE`` command tree.
            - ``.output``: The ``PG:OUTPut`` command tree.
            - ``.patterndefinition``: The ``PG:PATTERNdefinition`` command.
        """
        return self._pg

    @property
    def plot(self) -> Plot:
        """Return the ``PLOT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.addnew``: The ``PLOT:ADDNew`` command.
            - ``.delete``: The ``PLOT:DELete`` command.
            - ``.list``: The ``PLOT:LIST`` command.
            - ``.plot``: The ``PLOT:PLOT<x>`` command tree.
        """
        return self._plot

    @property
    def power(self) -> Power:
        """Return the ``POWer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.addnew``: The ``POWer:ADDNew`` command.
            - ``.delete``: The ``POWer:DELete`` command.
            - ``.power``: The ``POWer:POWer<x>`` command tree.
        """
        return self._power

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
    def recall(self) -> Recall:
        """Return the ``RECAll`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``RECAll?`` query.
            - Using the ``.verify(value)`` method will send the ``RECAll?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mask``: The ``RECAll:MASK`` command.
            - ``.session``: The ``RECAll:SESsion`` command.
            - ``.setup``: The ``RECAll:SETUp`` command.
            - ``.waveform``: The ``RECAll:WAVEform`` command.
        """
        return self._recall

    @property
    def ref(self) -> Ref:
        """Return the ``REF`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REF?`` query.
            - Using the ``.verify(value)`` method will send the ``REF?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.addnew``: The ``REF:ADDNew`` command.
            - ``.delete``: The ``REF:DELete`` command.
            - ``.list``: The ``REF:LIST`` command.
            - ``.ref``: The ``REF:REF<x>`` command tree.
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
            - ``.source``: The ``ROSc:SOUrce`` command.
            - ``.state``: The ``ROSc:STATE`` command.
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
    def save(self) -> Save:
        """Return the ``SAVe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVe?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.eventtable``: The ``SAVe:EVENTtable`` command tree.
            - ``.image``: The ``SAVe:IMAGe`` command.
            - ``.plotdata``: The ``SAVe:PLOTData`` command.
            - ``.report``: The ``SAVe:REPOrt`` command.
            - ``.session``: The ``SAVe:SESsion`` command.
            - ``.setup``: The ``SAVe:SETUp`` command.
            - ``.waveform``: The ``SAVe:WAVEform`` command.
        """
        return self._save

    @property
    def saveon(self) -> Saveon:
        """Return the ``SAVEON`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEON?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEON?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.file``: The ``SAVEON:FILE`` command tree.
            - ``.image``: The ``SAVEON:IMAGe`` command.
            - ``.trigger``: The ``SAVEON:TRIGger`` command.
            - ``.waveform``: The ``SAVEON:WAVEform`` command.
        """
        return self._saveon

    @property
    def saveonevent(self) -> Saveonevent:
        """Return the ``SAVEONEVent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SAVEONEVent?`` query.
            - Using the ``.verify(value)`` method will send the ``SAVEONEVent?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.filedest``: The ``SAVEONEVent:FILEDest`` command.
            - ``.filename``: The ``SAVEONEVent:FILEName`` command.
            - ``.image``: The ``SAVEONEVent:IMAGe`` command tree.
            - ``.waveform``: The ``SAVEONEVent:WAVEform`` command tree.
        """
        return self._saveonevent

    @property
    def search(self) -> Search:
        """Return the ``SEARCH`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.addnew``: The ``SEARCH:ADDNew`` command.
            - ``.deleteall``: The ``SEARCH:DELETEALL`` command.
            - ``.delete``: The ``SEARCH:DELete`` command.
            - ``.list``: The ``SEARCH:LIST`` command.
            - ``.search``: The ``SEARCH:SEARCH<x>`` command tree.
            - ``.selected``: The ``SEARCH:SELected`` command.
        """
        return self._search

    @property
    def select(self) -> Select:
        """Return the ``SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``SELect:CH<x>`` command.
            - ``.dch``: The ``SELect:DCH<x>`` command tree.
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
    def socketserver(self) -> Socketserver:
        """Return the ``SOCKETServer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOCKETServer?`` query.
            - Using the ``.verify(value)`` method will send the ``SOCKETServer?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``SOCKETServer:ENAble`` command.
            - ``.port``: The ``SOCKETServer:PORT`` command.
            - ``.protocol``: The ``SOCKETServer:PROTOCol`` command.
        """
        return self._socketserver

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
    def time(self) -> Time:
        """Return the ``TIMe`` command.

        Description:
            - This command sets the time in the form ``hh:mm:ss`` where hh refers to a two-digit
              hour number, mm refers to a two-digit minute number from 01 to 60, and ss refers to a
              two-digit second number from 01 to 60.

        Usage:
            - Using the ``.query()`` method will send the ``TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``TIMe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TIMe value`` command.

        SCPI Syntax:
            ```
            - TIMe <QString>
            - TIMe?
            ```

        Info:
            - ``<QString>`` is a quoted string representing the desired time.

        Sub-properties:
            - ``.zone``: The ``TIMe:ZONe`` command.
        """
        return self._time

    @property
    def totaluptime(self) -> Totaluptime:
        """Return the ``TOTaluptime`` command.

        Description:
            - Total number of hours the instrument has been turned on since the NV memory was last
              programmed, usually during the initial manufacturing process.

        Usage:
            - Using the ``.query()`` method will send the ``TOTaluptime?`` query.
            - Using the ``.verify(value)`` method will send the ``TOTaluptime?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TOTaluptime?
            ```
        """
        return self._totaluptime

    @property
    def touchscreen(self) -> Touchscreen:
        """Return the ``TOUCHSCReen`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TOUCHSCReen?`` query.
            - Using the ``.verify(value)`` method will send the ``TOUCHSCReen?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``TOUCHSCReen:STATe`` command.
        """
        return self._touchscreen

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
            - ``.hysteresis``: The ``TRIGger:HYSTeresis`` command tree.
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
    def undo(self) -> Undo:
        """Return the ``UNDO`` command.

        Description:
            - Reverts the instrument settings to a state before the previous command or user
              interface action.

        Usage:
            - Using the ``.write()`` method will send the ``UNDO`` command.

        SCPI Syntax:
            ```
            - UNDO
            ```
        """
        return self._undo

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
    def usbdevice(self) -> Usbdevice:
        """Return the ``USBDevice`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``USBDevice?`` query.
            - Using the ``.verify(value)`` method will send the ``USBDevice?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.configure``: The ``USBDevice:CONFigure`` command.
        """
        return self._usbdevice

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
    def vertical(self) -> Vertical:
        """Return the ``VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``VERTical?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.deskew``: The ``VERTical:DESKew`` command tree.
        """
        return self._vertical

    @property
    def vxi(self) -> Vxi:
        """Return the ``VXI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``VXI?`` query.
            - Using the ``.verify(value)`` method will send the ``VXI?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``VXI:ENAble`` command.
            - ``.port``: The ``VXI:PORT`` command tree.
        """
        return self._vxi

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
            - ``.asc_fmt``: The ``WFMOutpre:ASC_Fmt`` command.
            - ``.bit_nr``: The ``WFMOutpre:BIT_Nr`` command.
            - ``.bn_fmt``: The ``WFMOutpre:BN_Fmt`` command.
            - ``.byt_nr``: The ``WFMOutpre:BYT_Nr`` command.
            - ``.byt_or``: The ``WFMOutpre:BYT_Or`` command.
            - ``.centerfrequency``: The ``WFMOutpre:CENTERFREQuency`` command.
            - ``.domain``: The ``WFMOutpre:DOMain`` command.
            - ``.encdg``: The ``WFMOutpre:ENCdg`` command.
            - ``.nr_pt``: The ``WFMOutpre:NR_Pt`` command.
            - ``.pt_fmt``: The ``WFMOutpre:PT_Fmt`` command.
            - ``.pt_order``: The ``WFMOutpre:PT_ORder`` command.
            - ``.pt_off``: The ``WFMOutpre:PT_Off`` command.
            - ``.resample``: The ``WFMOutpre:RESample`` command.
            - ``.span``: The ``WFMOutpre:SPAN`` command.
            - ``.wfid``: The ``WFMOutpre:WFId`` command.
            - ``.wfmtype``: The ``WFMOutpre:WFMTYPe`` command.
            - ``.xincr``: The ``WFMOutpre:XINcr`` command.
            - ``.xunit``: The ``WFMOutpre:XUNit`` command.
            - ``.xzero``: The ``WFMOutpre:XZEro`` command.
            - ``.ymult``: The ``WFMOutpre:YMUlt`` command.
            - ``.yoff``: The ``WFMOutpre:YOFf`` command.
            - ``.yunit``: The ``WFMOutpre:YUNit`` command.
            - ``.yzero``: The ``WFMOutpre:YZEro`` command.
        """
        return self._wfmoutpre


class MSO2Mixin:
    """A mixin that provides access to the MSO2 commands and constants.

    Properties:
        - ``.command_argument_constants``: The MSO2 command argument constants.
        - ``.commands``: The MSO2 commands.
    """

    @cached_property
    def command_argument_constants(self) -> MSO2CommandConstants:  # pylint: disable=no-self-use
        """Return the MSO2 command argument constants.

        This provides access to all the string constants which can be used as arguments for MSO2
        commands.
        """
        return MSO2CommandConstants()

    @cached_property
    def commands(self) -> MSO2Commands:
        """Return the MSO2 commands.

        This provides access to all the commands for the MSO2 device. See the documentation of each
        sub-property for more usage information.

        Sub-properties:
            - ``.acquire``: The ``ACQuire`` command.
            - ``.actonevent``: The ``ACTONEVent`` command tree.
            - ``.afg``: The ``AFG`` command tree.
            - ``.alias``: The ``ALIas`` command.
            - ``.allev``: The ``ALLEv`` command.
            - ``.autosavepitimeout``: The ``AUTOSAVEPITIMEOUT`` command.
            - ``.autosaveuitimeout``: The ``AUTOSAVEUITIMEOUT`` command.
            - ``.autoset``: The ``AUTOSet`` command.
            - ``.auxout``: The ``AUXout`` command tree.
            - ``.battery``: The ``BATTery`` command tree.
            - ``.bus``: The ``BUS`` command tree.
            - ``.bustable``: The ``BUSTABle`` command tree.
            - ``.busy``: The ``BUSY`` command.
            - ``.cal``: The ``*CAL`` command.
            - ``.calibrate``: The ``CALibrate`` command.
            - ``.callouts``: The ``CALLOUTS`` command tree.
            - ``.ch``: The ``CH<x>`` command.
            - ``.clear``: The ``CLEAR`` command.
            - ``.cls``: The ``*CLS`` command.
            - ``.configuration``: The ``CONFIGuration`` command tree.
            - ``.connected``: The ``CONNected`` command tree.
            - ``.curve``: The ``CURVe`` command.
            - ``.curvestream``: The ``CURVEStream`` command.
            - ``.customtable``: The ``CUSTOMTABle`` command tree.
            - ``.data``: The ``DATa`` command.
            - ``.date``: The ``DATE`` command.
            - ``.dch``: The ``DCH<x>`` command tree.
            - ``.ddt``: The ``*DDT`` command.
            - ``.dese``: The ``DESE`` command.
            - ``.diag``: The ``DIAg`` command tree.
            - ``.display``: The ``DISplay`` command.
            - ``.ese``: The ``*ESE`` command.
            - ``.esr``: The ``*ESR`` command.
            - ``.ethernet``: The ``ETHERnet`` command tree.
            - ``.event``: The ``EVENT`` command.
            - ``.evmsg``: The ``EVMsg`` command.
            - ``.evqty``: The ``EVQty`` command.
            - ``.factory``: The ``FACtory`` command.
            - ``.filesystem``: The ``FILESystem`` command.
            - ``.fpanel``: The ``FPAnel`` command tree.
            - ``.header``: The ``HEADer`` command.
            - ``.horizontal``: The ``HORizontal`` command.
            - ``.id``: The ``ID`` command.
            - ``.idn``: The ``*IDN`` command.
            - ``.lic``: The ``LIC`` command tree.
            - ``.license``: The ``LICense`` command.
            - ``.lock``: The ``LOCk`` command.
            - ``.lrn``: The ``*LRN`` command.
            - ``.mainwindow``: The ``MAINWindow`` command tree.
            - ``.mask``: The ``MASK`` command tree.
            - ``.math``: The ``MATH`` command tree.
            - ``.meastable``: The ``MEASTABle`` command tree.
            - ``.measurement``: The ``MEASUrement`` command.
            - ``.newpass``: The ``NEWpass`` command.
            - ``.opc``: The ``*OPC`` command.
            - ``.opt``: The ``*OPT`` command.
            - ``.password``: The ``PASSWord`` command.
            - ``.pause``: The ``PAUSe`` command.
            - ``.pg``: The ``PG`` command tree.
            - ``.plot``: The ``PLOT`` command tree.
            - ``.power``: The ``POWer`` command tree.
            - ``.psc``: The ``*PSC`` command.
            - ``.pud``: The ``*PUD`` command.
            - ``.recall``: The ``RECAll`` command tree.
            - ``.ref``: The ``REF`` command tree.
            - ``.rem``: The ``REM`` command.
            - ``.rosc``: The ``ROSc`` command tree.
            - ``.rst``: The ``*RST`` command.
            - ``.save``: The ``SAVe`` command tree.
            - ``.saveon``: The ``SAVEON`` command tree.
            - ``.saveonevent``: The ``SAVEONEVent`` command tree.
            - ``.search``: The ``SEARCH`` command tree.
            - ``.select``: The ``SELect`` command tree.
            - ``.set``: The ``SET`` command.
            - ``.socketserver``: The ``SOCKETServer`` command tree.
            - ``.sre``: The ``*SRE`` command.
            - ``.stb``: The ``*STB`` command.
            - ``.teksecure``: The ``TEKSecure`` command.
            - ``.time``: The ``TIMe`` command.
            - ``.totaluptime``: The ``TOTaluptime`` command.
            - ``.touchscreen``: The ``TOUCHSCReen`` command tree.
            - ``.trg``: The ``*TRG`` command.
            - ``.trigger``: The ``TRIGger`` command.
            - ``.tst``: The ``*TST`` command.
            - ``.undo``: The ``UNDO`` command.
            - ``.unlock``: The ``UNLock`` command.
            - ``.usbdevice``: The ``USBDevice`` command tree.
            - ``.verbose``: The ``VERBose`` command.
            - ``.vertical``: The ``VERTical`` command tree.
            - ``.vxi``: The ``VXI`` command tree.
            - ``.wai``: The ``*WAI`` command.
            - ``.wavfrm``: The ``WAVFrm`` command.
            - ``.wfmoutpre``: The ``WFMOutpre`` command.
        """
        device = self if isinstance(self, PIControl) else None
        return MSO2Commands(device)
