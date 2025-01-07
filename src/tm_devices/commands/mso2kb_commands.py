# pylint: disable=line-too-long
"""The MSO2KB commands module.

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.
"""

from typing import Dict, Optional

from tm_devices.driver_mixins.device_control.pi_control import PIControl
from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from .gen_1lcv3a_msodpomdo.message import Message
from .gen_1lcv3a_msodpomdo.setup_1 import SetupItem
from .gen_1nmc1o_msodpomdo.clearmenu import Clearmenu
from .gen_1nmc1o_msodpomdo.errlog import Errlog
from .gen_1nmc1o_msodpomdo.language import Language
from .gen_1nmc1o_msodpomdo.usbdevice import Usbdevice
from .gen_1nmc1o_msodpomdo.usbtmc import Usbtmc
from .gen_e6bmgw_lpdmsotekscopepcdpomdo.totaluptime import Totaluptime
from .gen_fhrp27_msodpomdodsa.curve import Curve
from .gen_fhrp27_msodpomdodsa.date import Date
from .gen_fhrp27_msodpomdodsa.mathvar import Mathvar
from .gen_fhrp27_msodpomdodsa.save_and_recall import Rcl, Sav
from .gen_fkjfe8_msodpodsa.time import Time
from .gen_fsksdy_lpdmsotekscopepcdpomdoafgawgdsa.miscellaneous import Idn, Tst
from .gen_fsksdy_lpdmsotekscopepcdpomdoafgawgdsa.status_and_error import (
    Cls,
    Esr,
    Opc,
    Rst,
    Stb,
    Wai,
)
from .gen_ft5uww_lpdmsodpomdoafgawgdsa.calibration import Cal
from .gen_ft5uww_lpdmsodpomdoafgawgdsa.miscellaneous import Trg
from .gen_fu6dog_lpdmsotekscopepcdpomdoawgdsa.status_and_error import Ese, Sre
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
from .gen_u301s_msodpo.acquire import Acquire
from .gen_u301s_msodpo.alias import Alias
from .gen_u301s_msodpo.autoset import Autoset
from .gen_u301s_msodpo.auxin import Auxin
from .gen_u301s_msodpo.bus import Bus
from .gen_u301s_msodpo.calibrate import Calibrate
from .gen_u301s_msodpo.ch import Channel
from .gen_u301s_msodpo.cursor import Cursor
from .gen_u301s_msodpo.d import DigitalBit
from .gen_u301s_msodpo.data import Data
from .gen_u301s_msodpo.diag import Diag
from .gen_u301s_msodpo.display import Display
from .gen_u301s_msodpo.ethernet import Ethernet
from .gen_u301s_msodpo.filesystem import Filesystem
from .gen_u301s_msodpo.filtervu import Filtervu
from .gen_u301s_msodpo.fpanel import Fpanel
from .gen_u301s_msodpo.gpibusb import Gpibusb
from .gen_u301s_msodpo.hardcopy import Hardcopy
from .gen_u301s_msodpo.horizontal import Horizontal
from .gen_u301s_msodpo.mark import Mark
from .gen_u301s_msodpo.math1 import Math1
from .gen_u301s_msodpo.measurement import Measurement
from .gen_u301s_msodpo.pictbridge import Pictbridge
from .gen_u301s_msodpo.recall import Recall
from .gen_u301s_msodpo.ref import RefItem
from .gen_u301s_msodpo.save import Save
from .gen_u301s_msodpo.search import Search
from .gen_u301s_msodpo.select import Select
from .gen_u301s_msodpo.trigger import Trigger
from .gen_u301s_msodpo.wfminpre import Wfminpre
from .gen_u301s_msodpo.wfmoutpre import Wfmoutpre
from .gen_u301s_msodpo.zoom import Zoom
from .helpers import DefaultDictPassKeyToFactory


# pylint: disable=too-few-public-methods
class MSO2KBCommandConstants:
    """The MSO2KB command argument constants.

    This provides access to all the string constants which can be used as arguments for MSO2KB
    commands.
    """

    A = "A"
    A0 = "A0"
    A1 = "A1"
    A2 = "A2"
    A3 = "A3"
    A4 = "A4"
    A5 = "A5"
    A6 = "A6"
    A7 = "A7"
    A8 = "A8"
    A9 = "A9"
    ABORT = "ABORT"  # ABORt
    # ABORT = "ABOrt"
    ABSOLUTE = "ABSOLUTE"  # ABSolute
    AC = "AC"
    ACKMISS = "ACKMISS"
    ACQ = "ACQ"
    ADDR10 = "ADDR10"
    ADDR7 = "ADDR7"
    ADDRANDDATA = "ADDRANDDATA"
    ADDRESS = "ADDRESS"  # ADDRess
    ALL = "ALL"
    ALLFIELDS = "ALLFIELDS"  # ALLFields
    ALLLINES = "ALLLINES"  # ALLLines
    ALWAYS = "ALWAYS"
    AMPLITUDE = "AMPLITUDE"  # AMPlitude
    AND = "AND"
    ANY = "ANY"
    APPKEY = "APPKEY"  # APPKey
    AREA = "AREA"  # AREa
    ASCII = "ASCII"
    # ASCII = "ASCIi"
    # ASCII = "ASCii"
    AUTO = "AUTO"
    # AUTO = "Auto"
    AUX = "AUX"
    AVERAGE = "AVERAGE"  # AVErage
    B = "B"
    B0 = "B0"
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    B4 = "B4"
    B5 = "B5"
    B6 = "B6"
    B7 = "B7"
    B8 = "B8"
    B9 = "B9"
    BACKWARDS = "BACKWARDS"  # BACKWards
    BASE = "BASE"  # BASe
    BDIFFBP = "BDIFFBP"
    BINARY = "BINARY"  # BINary
    BLACKMANHARRIS = "BLACKMANHARRIS"  # BLAckmanharris
    BM = "BM"
    BMP = "BMP"
    BOTH = "BOTH"  # BOTh
    BURST = "BURST"  # BURst
    BUS = "BUS"
    BYPASS = "BYPASS"  # BYPass
    CAN = "CAN"
    CANH = "CANH"
    CANL = "CANL"
    CARD = "CARD"
    CAREA = "CAREA"  # CARea
    CHECKSUM = "CHECKSUM"  # CHecksum
    CM10BY15 = "CM10BY15"
    CM13BY18 = "CM13BY18"
    CM15BY21 = "CM15BY21"
    CM18BY24 = "CM18BY24"
    CM6BY8 = "CM6BY8"
    CM7BY10 = "CM7BY10"
    CM9BY13 = "CM9BY13"
    CMEAN = "CMEAN"  # CMEan
    COLUMN = "COLUMN"
    COMPOSITE_ENV = "COMPOSITE_ENV"
    COMPOSITE_YT = "COMPOSITE_YT"
    CONTINUE = "CONTINUE"  # CONTinue
    CPU = "CPU"
    CR = "CR"
    CRCHEADER = "CRCHEADER"  # CRCHeader
    CRCTRAILER = "CRCTRAILER"  # CRCTrailer
    CRMS = "CRMS"  # CRMs
    CROSSHAIR = "CROSSHAIR"  # CROSSHair
    CURRENT = "CURRENT"  # CURrent
    CURSOR = "CURSOR"  # CURSor
    CYCLECOUNT = "CYCLECOUNT"  # CYCLEcount
    DATA = "DATA"
    DB = "DB"
    DC = "DC"
    DEFLT = "DEFLT"
    DEGREES = "DEGREES"  # DEGrees
    DELAY = "DELAY"  # DELay
    DIFFERENTIAL = "DIFFERENTIAL"  # DIFFerential
    DIGITAL = "DIGITAL"  # DIGItal
    DISABLED = "DISABLED"  # DISabled
    DISPLAY = "DISPLAY"  # DISplay
    DRAFT = "DRAFT"
    DUAL = "DUAL"
    DUMP = "DUMP"  # DUmp
    DYNAMIC = "DYNAMIC"  # DYNAMic
    E = "E"
    ECL = "ECL"
    EDGE = "EDGE"  # EDGe
    EEPROM = "EEPROM"
    EITHER = "EITHER"  # EITher
    ENV = "ENV"
    EOF = "EOF"
    EQUAL = "EQUAL"  # EQUal
    # EQUAL = "EQual"
    ERROR = "ERROR"
    # ERROR = "ERRor"
    EVEN = "EVEN"
    EXECUTE = "EXECUTE"  # EXECute
    EXT = "EXT"
    EXTENDED = "EXTENDED"  # EXTended
    FAIL = "FAIL"
    FALL = "FALL"
    FALLING = "FALLING"  # FALling
    FALSE = "FALSE"  # FALSe
    FASTER = "FASTER"  # FASTer
    FASTEST = "FASTEST"  # FAStest
    FASTPHOTO = "FASTPHOTO"
    FFT = "FFT"
    FINE = "FINE"
    FIVEDIVS = "FIVEDIVS"  # FIVEdivs
    FORCE = "FORCE"  # FORCe
    FORWARDS = "FORWARDS"  # FORWards
    FPANEL = "FPANEL"  # FPAnel
    FRAME = "FRAME"  # FRAme
    FRAMETYPE = "FRAMETYPE"  # FRAMEType
    # FRAMETYPE = "FRAMEtype"
    FRAMETYPEID = "FRAMETYPEID"  # FRAMETypeid
    FREQUENCY = "FREQUENCY"  # FREQuency
    FULL = "FULL"
    # FULL = "FULl"
    GENERALCALL = "GENERALCALL"  # GENeralcall
    GND = "GND"
    GRID = "GRID"  # GRId
    HAGAKIPC = "HAGAKIPC"
    HAGAKIPCARD = "HAGAKIPCARD"
    HALFGRAT = "HALFGRAT"  # HALFgrat
    HAMMING = "HAMMING"  # HAMming
    HANNING = "HANNING"  # HANning
    HBARS = "HBARS"  # HBArs
    HEADER = "HEADER"  # HEADer
    HERTZ = "HERTZ"  # HERtz
    HEXADECIMAL = "HEXADECIMAL"  # HEXadecimal
    HFREJ = "HFREJ"  # HFRej
    HIGH = "HIGH"
    HISTOGRAM = "HISTOGRAM"  # HIStogram
    HSMODE = "HSMODE"  # HSmode
    I2C = "I2C"
    IDANDDATA = "IDANDDATA"
    IDENTIFIER = "IDENTIFIER"  # IDentifier
    IMAGE = "IMAGE"  # IMAGe
    # IMAGE = "IMAge"
    IN11BY17 = "IN11BY17"
    IN2P5BY3P25 = "IN2P5BY3P25"
    IN4BY6 = "IN4BY6"
    IN8BY10 = "IN8BY10"
    INDEPENDENT = "INDEPENDENT"  # INDependent
    INIT = "INIT"
    INRANGE = "INRANGE"  # INrange
    INVERTED = "INVERTED"  # INVERTed
    # INVERTED = "INVerted"
    IO = "IO"
    L = "L"
    L2 = "L2"
    L4 = "L4"
    LANDSCAPE = "LANDSCAPE"  # LANdscape
    LARGE = "LARGE"  # LARge
    LESSEQUAL = "LESSEQUAL"  # LESSEQual
    LESSTHAN = "LESSTHAN"  # LESSThan
    # LESSTHAN = "LESSthan"
    LETTER = "LETTER"
    LF = "LF"
    LFREJ = "LFREJ"  # LFRej
    LIN = "LIN"
    LINE = "LINE"
    LOGIC = "LOGIC"
    # LOGIC = "LOGic"
    LOW = "LOW"
    LSB = "LSB"
    MATH = "MATH"
    MAXIMUM = "MAXIMUM"  # MAXimum
    MEAN = "MEAN"
    MEDIUM = "MEDIUM"  # MEDium
    MINIMUM = "MINIMUM"  # MINImum
    MINMAX = "MINMAX"  # MINMax
    MISO = "MISO"
    MISOMOSI = "MISOMOSI"
    MIXED = "MIXED"  # MIXed
    MM100BY150 = "MM100BY150"
    MM54BY86 = "MM54BY86"
    MOREEQUAL = "MOREEQUAL"  # MOREEQual
    MORETHAN = "MORETHAN"  # MOREThan
    # MORETHAN = "MOREthan"
    MOSI = "MOSI"
    MSB = "MSB"
    NAND = "NAND"  # NANd
    NDUTY = "NDUTY"  # NDUty
    NEDGECOUNT = "NEDGECOUNT"  # NEDGECount
    NEGATIVE = "NEGATIVE"  # NEGative
    NEXT = "NEXT"
    NO = "NO"
    NOCARE = "NOCARE"
    NOISEREJ = "NOISEREJ"  # NOISErej
    NOPARITY = "NOPARITY"  # NOPARity
    NORMAL = "NORMAL"  # NORMal
    NOVERSHOOT = "NOVERSHOOT"  # NOVershoot
    NPULSECOUNT = "NPULSECOUNT"  # NPULSECount
    NRMAL = "NRMAL"
    NTIMES = "NTIMES"
    NTSC = "NTSC"  # NTSc
    NULL = "NULL"
    # NULL = "NULl"
    NULLFRDYNAMIC = "NULLFRDYNAMIC"  # NULLFRDynamic
    NULLFRSTATIC = "NULLFRSTATIC"  # NULLFRStatic
    NUMERIC = "NUMERIC"  # NUMERic
    NWIDTH = "NWIDTH"  # NWIdth
    OCCURS = "OCCURS"
    ODD = "ODD"
    OFF = "OFF"
    ON = "ON"
    ONCE = "ONCE"
    ONFAIL = "ONFAIL"
    OUTRANGE = "OUTRANGE"  # OUTrange
    OVERLOAD = "OVERLOAD"  # OVERLoad
    PACKET = "PACKET"
    PAL = "PAL"
    PARALLEL = "PARALLEL"  # PARallel
    PARITY = "PARITY"  # PARity
    PASS = "PASS"
    PAYLOAD = "PAYLOAD"  # PAYLoad
    PDUTY = "PDUTY"  # PDUty
    PEDGECOUNT = "PEDGECOUNT"  # PEDGECount
    PERCENT = "PERCENT"  # PERCent
    # PERCENT = "PERcent"
    PERIOD = "PERIOD"  # PERIod
    PHASE = "PHASE"  # PHAse
    PHOTO = "PHOTO"
    PK2PK = "PK2PK"  # PK2Pk
    PLAIN = "PLAIN"
    PNG = "PNG"
    PORTRAIT = "PORTRAIT"  # PORTRait
    POSITIVE = "POSITIVE"  # POSitive
    POVERSHOOT = "POVERSHOOT"  # POVershoot
    PPULSECOUNT = "PPULSECOUNT"  # PPULSECount
    PREVIOUS = "PREVIOUS"  # PREVious
    PULSE = "PULSE"  # PULSe
    PWIDTH = "PWIDTH"  # PWIdth
    QUAL = "QUAL"  # QUal
    RATE15 = "RATE15"
    RATE20 = "RATE20"
    RATE25 = "RATE25"
    RATE35 = "RATE35"
    RATE50 = "RATE50"
    READ = "READ"
    RECTANGULAR = "RECTANGULAR"  # RECTangular
    REDUCED = "REDUCED"  # REDUced
    REF = "REF"
    REMOTE = "REMOTE"  # REMote
    REPEATSTART = "REPEATSTART"  # REPEATstart
    RESET = "RESET"
    RI = "RI"
    RIBINARY = "RIBINARY"  # RIBinary
    RISE = "RISE"  # RISe
    RISING = "RISING"  # RISing
    RMS = "RMS"
    ROLL100MM = "ROLL100MM"
    ROLL127MM = "ROLL127MM"
    ROLL210MM = "ROLL210MM"
    ROLL89MM = "ROLL89MM"
    ROM = "ROM"
    RP = "RP"
    RPBINARY = "RPBINARY"  # RPBinary
    RS232C = "RS232C"
    RUNSTOP = "RUNSTOP"  # RUNSTop
    RUNT = "RUNT"  # RUNt
    RX = "RX"
    RXDATA = "RXDATA"
    RXENDPACKET = "RXENDPACKET"  # RXENDPacket
    RXPARITY = "RXPARITY"  # RXPARity
    RXSTART = "RXSTART"  # RXSTArt
    SAMPLE = "SAMPLE"  # SAMple
    SCREEN = "SCREEN"
    # SCREEN = "SCREen"
    SEARCHTOTRIGGER = "SEARCHTOTRIGGER"  # SEARCHtotrigger
    SECAM = "SECAM"
    SECONDS = "SECONDS"  # SEConds
    SEQUENCE = "SEQUENCE"  # SEQuence
    SETHOLD = "SETHOLD"  # SETHold
    SETLEVEL = "SETLEVEL"  # SETLevel
    SETUP = "SETUP"  # SETUp
    SINGULAR_YT = "SINGULAR_YT"
    SLEEP = "SLEEP"
    SLOWER = "SLOWER"  # SLOWer
    SMALL = "SMALL"  # SMAll
    SNAP = "SNAP"  # SNAp
    SOF = "SOF"
    SPI = "SPI"
    SRIBINARY = "SRIBINARY"  # SRIbinary
    SRPBINARY = "SRPBINARY"  # SRPbinary
    SS = "SS"
    STANDARD = "STANDARD"  # STandard
    START = "START"
    # START = "STARt"
    STARTBYTE = "STARTBYTE"  # STARtbyte
    STARTOFFRAME = "STARTOFFRAME"  # STARTofframe
    STARTUP = "STARTUP"  # STARTup
    STARTUPNOSYNC = "STARTUPNOSYNC"  # STARTupnosync
    STATIC = "STATIC"  # STATic
    STOP = "STOP"
    SYNC = "SYNC"
    SYNCFIELD = "SYNCFIELD"  # SYNCField
    SYNCFRAME = "SYNCFRAME"  # SYNCFrame
    TIFF = "TIFF"  # TIFf
    TRACK = "TRACK"  # TRACk
    TRANSITION = "TRANSITION"  # TRAnsition
    TRIGGERTOSEARCH = "TRIGGERTOSEARCH"  # TRIGgertosearch
    TRUE = "TRUE"  # TRUe
    TTL = "TTL"
    TX = "TX"
    TXDATA = "TXDATA"
    TXENDPACKET = "TXENDPACKET"  # TXENDPacket
    TXPARITY = "TXPARITY"  # TXPARity
    TXRX = "TXRX"
    TXSTART = "TXSTART"  # TXSTArt
    UNDO = "UNDO"  # UNDo
    UNEQUAL = "UNEQUAL"  # UNEQual
    USBTMC = "USBTMC"  # USBTmc
    USER = "USER"
    V1X = "V1X"
    V2X = "V2X"
    VBARS = "VBARS"  # VBArs
    VIDEO = "VIDEO"  # VIDeo
    WAKEUP = "WAKEUP"  # WAKEup
    WAVEFORM = "WAVEFORM"  # WAVEform
    WIDTH = "WIDTH"  # WIDth
    WRITE = "WRITE"
    X = "X"
    XFF = "XFF"
    XY = "XY"
    Y = "Y"
    YES = "YES"
    YT = "YT"


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class MSO2KBCommands:
    """The MSO2KB commands.

    This provides access to all the commands for the MSO2KB device. See the documentation of each
    property for more usage information.

    Properties:
        - ``.acquire``: The ``ACQuire`` command.
        - ``.alias``: The ``ALIas`` command.
        - ``.allev``: The ``ALLEv`` command.
        - ``.autoset``: The ``AUTOSet`` command.
        - ``.auxin``: The ``AUXin`` command.
        - ``.bus``: The ``BUS`` command.
        - ``.busy``: The ``BUSY`` command.
        - ``.cal``: The ``*CAL`` command.
        - ``.calibrate``: The ``CALibrate`` command tree.
        - ``.ch``: The ``CH<x>`` command.
        - ``.clearmenu``: The ``CLEARMenu`` command.
        - ``.cls``: The ``*CLS`` command.
        - ``.cursor``: The ``CURSor`` command.
        - ``.curve``: The ``CURVe`` command.
        - ``.d``: The ``D<x>`` command.
        - ``.data``: The ``DATa`` command.
        - ``.date``: The ``DATE`` command.
        - ``.ddt``: The ``*DDT`` command.
        - ``.dese``: The ``DESE`` command.
        - ``.diag``: The ``DIAg`` command tree.
        - ``.display``: The ``DISplay`` command.
        - ``.errlog``: The ``ERRlog`` command.
        - ``.ese``: The ``*ESE`` command.
        - ``.esr``: The ``*ESR`` command.
        - ``.ethernet``: The ``ETHERnet`` command tree.
        - ``.event``: The ``EVENT`` command.
        - ``.evmsg``: The ``EVMsg`` command.
        - ``.evqty``: The ``EVQty`` command.
        - ``.factory``: The ``FACtory`` command.
        - ``.filesystem``: The ``FILESystem`` command.
        - ``.filtervu``: The ``FILTERVu`` command tree.
        - ``.fpanel``: The ``FPAnel`` command tree.
        - ``.gpibusb``: The ``GPIBUsb`` command tree.
        - ``.hardcopy``: The ``HARDCopy`` command.
        - ``.header``: The ``HEADer`` command.
        - ``.horizontal``: The ``HORizontal`` command.
        - ``.id``: The ``ID`` command.
        - ``.idn``: The ``*IDN`` command.
        - ``.language``: The ``LANGuage`` command.
        - ``.lock``: The ``LOCk`` command.
        - ``.lrn``: The ``*LRN`` command.
        - ``.mark``: The ``MARK`` command.
        - ``.math1``: The ``MATH1`` command.
        - ``.mathvar``: The ``MATHVAR`` command.
        - ``.measurement``: The ``MEASUrement`` command.
        - ``.message``: The ``MESSage`` command.
        - ``.newpass``: The ``NEWpass`` command.
        - ``.opc``: The ``*OPC`` command.
        - ``.password``: The ``PASSWord`` command.
        - ``.pictbridge``: The ``PICTBridge`` command tree.
        - ``.psc``: The ``*PSC`` command.
        - ``.pud``: The ``*PUD`` command.
        - ``.rcl``: The ``*RCL`` command.
        - ``.recall``: The ``RECAll`` command tree.
        - ``.ref``: The ``REF<x>`` command.
        - ``.rem``: The ``REM`` command.
        - ``.rst``: The ``*RST`` command.
        - ``.sav``: The ``*SAV`` command.
        - ``.save``: The ``SAVe`` command tree.
        - ``.search``: The ``SEARCH`` command.
        - ``.select``: The ``SELect`` command.
        - ``.set``: The ``SET`` command.
        - ``.setup``: The ``SETUP<x>`` command tree.
        - ``.sre``: The ``*SRE`` command.
        - ``.stb``: The ``*STB`` command.
        - ``.teksecure``: The ``TEKSecure`` command.
        - ``.time``: The ``TIME`` command.
        - ``.totaluptime``: The ``TOTaluptime`` command.
        - ``.trg``: The ``*TRG`` command.
        - ``.trigger``: The ``TRIGger`` command.
        - ``.tst``: The ``*TST`` command.
        - ``.unlock``: The ``UNLock`` command.
        - ``.usbdevice``: The ``USBDevice`` command tree.
        - ``.usbtmc``: The ``USBTMC`` command.
        - ``.verbose``: The ``VERBose`` command.
        - ``.wai``: The ``*WAI`` command.
        - ``.wavfrm``: The ``WAVFrm`` command.
        - ``.wfminpre``: The ``WFMInpre`` command.
        - ``.wfmoutpre``: The ``WFMOutpre`` command.
        - ``.zoom``: The ``ZOOm`` command.
    """

    # pylint: disable=too-many-statements
    def __init__(self, device: Optional[PIControl] = None) -> None:  # noqa: PLR0915
        self._acquire = Acquire(device)
        self._alias = Alias(device)
        self._allev = Allev(device)
        self._autoset = Autoset(device)
        self._auxin = Auxin(device)
        self._bus = Bus(device)
        self._busy = Busy(device)
        self._cal = Cal(device)
        self._calibrate = Calibrate(device)
        self._ch: Dict[int, Channel] = DefaultDictPassKeyToFactory(
            lambda x: Channel(device, f"CH{x}")
        )
        self._clearmenu = Clearmenu(device)
        self._cls = Cls(device)
        self._cursor = Cursor(device)
        self._curve = Curve(device)
        self._d: Dict[int, DigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: DigitalBit(device, f"D{x}")
        )
        self._data = Data(device)
        self._date = Date(device)
        self._ddt = Ddt(device)
        self._dese = Dese(device)
        self._diag = Diag(device)
        self._display = Display(device)
        self._errlog = Errlog(device)
        self._ese = Ese(device)
        self._esr = Esr(device)
        self._ethernet = Ethernet(device)
        self._event = Event(device)
        self._evmsg = Evmsg(device)
        self._evqty = Evqty(device)
        self._factory = Factory(device)
        self._filesystem = Filesystem(device)
        self._filtervu = Filtervu(device)
        self._fpanel = Fpanel(device)
        self._gpibusb = Gpibusb(device)
        self._hardcopy = Hardcopy(device)
        self._header = Header(device)
        self._horizontal = Horizontal(device)
        self._id = Id(device)
        self._idn = Idn(device)
        self._language = Language(device)
        self._lock = Lock(device)
        self._lrn = Lrn(device)
        self._mark = Mark(device)
        self._math1 = Math1(device)
        self._mathvar = Mathvar(device)
        self._measurement = Measurement(device)
        self._message = Message(device)
        self._newpass = Newpass(device)
        self._opc = Opc(device)
        self._password = Password(device)
        self._pictbridge = Pictbridge(device)
        self._psc = Psc(device)
        self._pud = Pud(device)
        self._rcl = Rcl(device)
        self._recall = Recall(device)
        self._ref: Dict[int, RefItem] = DefaultDictPassKeyToFactory(
            lambda x: RefItem(device, f"REF{x}")
        )
        self._rem = Rem(device)
        self._rst = Rst(device)
        self._sav = Sav(device)
        self._save = Save(device)
        self._search = Search(device)
        self._select = Select(device)
        self._set = Set(device)
        self._setup: Dict[int, SetupItem] = DefaultDictPassKeyToFactory(
            lambda x: SetupItem(device, f"SETUP{x}")
        )
        self._sre = Sre(device)
        self._stb = Stb(device)
        self._teksecure = Teksecure(device)
        self._time = Time(device)
        self._totaluptime = Totaluptime(device)
        self._trg = Trg(device)
        self._trigger = Trigger(device)
        self._tst = Tst(device)
        self._unlock = Unlock(device)
        self._usbdevice = Usbdevice(device)
        self._usbtmc = Usbtmc(device)
        self._verbose = Verbose(device)
        self._wai = Wai(device)
        self._wavfrm = Wavfrm(device)
        self._wfminpre = Wfminpre(device)
        self._wfmoutpre = Wfmoutpre(device)
        self._zoom = Zoom(device)

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
            - ``.magnivu``: The ``ACQuire:MAGnivu`` command.
            - ``.maxsamplerate``: The ``ACQuire:MAXSamplerate`` command.
            - ``.mode``: The ``ACQuire:MODe`` command.
            - ``.numacq``: The ``ACQuire:NUMACq`` command.
            - ``.numavg``: The ``ACQuire:NUMAVg`` command.
            - ``.state``: The ``ACQuire:STATE`` command.
            - ``.stopafter``: The ``ACQuire:STOPAfter`` command.
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
    def autoset(self) -> Autoset:
        """Return the ``AUTOSet`` command.

        Description:
            - Sets the vertical, horizontal, and trigger controls of the oscilloscope to
              automatically acquire and display the selected waveform.

        Usage:
            - Using the ``.write(value)`` method will send the ``AUTOSet value`` command.

        SCPI Syntax:
            ```
            - AUTOSet {EXECute|UNDo}
            ```

        Info:
            - ``EXECute`` autosets the displayed waveform.
            - ``UNDo`` restores the oscilloscope settings to those present prior to the autoset
              execution.

        Sub-properties:
            - ``.enable``: The ``AUTOSet:ENAble`` command.
        """
        return self._autoset

    @property
    def auxin(self) -> Auxin:
        """Return the ``AUXin`` command.

        Description:
            - Returns all Aux Input connector parameters.

        Usage:
            - Using the ``.query()`` method will send the ``AUXin?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXin?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AUXin?
            ```

        Sub-properties:
            - ``.probe``: The ``AUXin:PRObe`` command.
        """
        return self._auxin

    @property
    def bus(self) -> Bus:
        """Return the ``BUS`` command.

        Description:
            - Sets or returns the parameters for each bus. These parameters affect either the Serial
              Trigger Setup or the Bus Display.

        Usage:
            - Using the ``.write()`` method will send the ``BUS`` command.

        SCPI Syntax:
            ```
            - BUS
            ```

        Sub-properties:
            - ``.b``: The ``BUS:B<x>`` command tree.
            - ``.lowerthreshold``: The ``BUS:LOWerthreshold`` command tree.
            - ``.threshold``: The ``BUS:THReshold`` command tree.
            - ``.upperthreshold``: The ``BUS:UPPerthreshold`` command tree.
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
        """Return the ``CALibrate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.factory``: The ``CALibrate:FACtory`` command.
            - ``.internal``: The ``CALibrate:INTERNal`` command.
            - ``.powerupstatus``: The ``CALibrate:POWerupstatus`` command.
            - ``.results``: The ``CALibrate:RESults`` command.
            - ``.temperature``: The ``CALibrate:TEMPerature`` command.
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
            - ``.bandwidth``: The ``CH<x>:BANdwidth`` command.
            - ``.coupling``: The ``CH<x>:COUPling`` command.
            - ``.deskew``: The ``CH<x>:DESKew`` command.
            - ``.impedance``: The ``CH<x>:IMPedance`` command.
            - ``.invert``: The ``CH<x>:INVert`` command.
            - ``.label``: The ``CH<x>:LABel`` command.
            - ``.offset``: The ``CH<x>:OFFSet`` command.
            - ``.position``: The ``CH<x>:POSition`` command.
            - ``.probe``: The ``CH<x>:PRObe`` command.
            - ``.scale``: The ``CH<x>:SCAle`` command.
            - ``.termination``: The ``CH<x>:TERmination`` command.
            - ``.volts``: The ``CH<x>:VOLts`` command.
            - ``.yunits``: The ``CH<x>:YUNits`` command.
        """
        return self._ch

    @property
    def clearmenu(self) -> Clearmenu:
        """Return the ``CLEARMenu`` command.

        Description:
            - Clears the current menu from the display. This command is equivalent to pressing the
              front panel Menu off.

        Usage:
            - Using the ``.write()`` method will send the ``CLEARMenu`` command.

        SCPI Syntax:
            ```
            - CLEARMenu
            ```
        """
        return self._clearmenu

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
            - ``.mode``: The ``CURSor:MODe`` command.
            - ``.vbars``: The ``CURSor:VBArs`` command.
            - ``.xy``: The ``CURSor:XY`` command tree.
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
    def d(self) -> Dict[int, DigitalBit]:
        """Return the ``D<x>`` command.

        Description:
            - This command specifies parameters for digital channel <x>, where x is the channel
              number.

        Usage:
            - Using the ``.write()`` method will send the ``D<x>`` command.

        SCPI Syntax:
            ```
            - D<x>
            ```

        Sub-properties:
            - ``.label``: The ``D<x>:LABel`` command.
            - ``.position``: The ``D<x>:POSition`` command.
            - ``.threshold``: The ``D<x>:THREshold`` command.
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
            - ``.composition``: The ``DATa:COMPosition`` command.
            - ``.destination``: The ``DATa:DESTination`` command.
            - ``.encdg``: The ``DATa:ENCdg`` command.
            - ``.resolution``: The ``DATa:RESOlution`` command.
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
            - ``.individual``: The ``DIAg:INDIvidual`` command tree.
            - ``.loop``: The ``DIAg:LOOP`` command tree.
            - ``.result``: The ``DIAg:RESUlt`` command tree.
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
            - ``.clock``: The ``DISplay:CLOCk`` command.
            - ``.digital``: The ``DISplay:DIGital`` command tree.
            - ``.format``: The ``DISplay:FORMat`` command.
            - ``.glitch``: The ``DISplay:GLITch`` command.
            - ``.graticule``: The ``DISplay:GRAticule`` command.
            - ``.intensity``: The ``DISplay:INTENSITy`` command.
            - ``.persistence``: The ``DISplay:PERSistence`` command.
            - ``.style``: The ``DISplay:STYle`` command tree.
        """
        return self._display

    @property
    def errlog(self) -> Errlog:
        """Return the ``ERRlog`` command.

        Description:
            - Clears the oscilloscope error log.

        Usage:
            - Using the ``.write(value)`` method will send the ``ERRlog value`` command.

        SCPI Syntax:
            ```
            - ERRlog {CLEar}
            ```

        Info:
            - ``CLear``

        Sub-properties:
            - ``.first``: The ``ERRlog:FIRst`` command.
            - ``.next``: The ``ERRlog:NEXt`` command.
            - ``.numentries``: The ``ERRlog:NUMENTries`` command.
        """
        return self._errlog

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
            - ``.httpport``: The ``ETHERnet:HTTPPort`` command.
            - ``.ipaddress``: The ``ETHERnet:IPADDress`` command.
            - ``.name``: The ``ETHERnet:NAME`` command.
            - ``.password``: The ``ETHERnet:PASSWord`` command.
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
            - Returns the directory listing of the current working directory and the number of bytes
              of free space available. This query is the same as the ``FILESYSTEM:DIR`` query and
              the ``FILESYSTEM:FREESPACE`` query.

        Usage:
            - Using the ``.query()`` method will send the ``FILESystem?`` query.
            - Using the ``.verify(value)`` method will send the ``FILESystem?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``FILESystem`` command.

        SCPI Syntax:
            ```
            - FILESystem
            - FILESystem?
            ```

        Sub-properties:
            - ``.copy``: The ``FILESystem:COPy`` command.
            - ``.cwd``: The ``FILESystem:CWD`` command.
            - ``.delete``: The ``FILESystem:DELEte`` command.
            - ``.dir``: The ``FILESystem:DIR`` command.
            - ``.format``: The ``FILESystem:FORMat`` command.
            - ``.freespace``: The ``FILESystem:FREESpace`` command.
            - ``.mkdir``: The ``FILESystem:MKDir`` command.
            - ``.readfile``: The ``FILESystem:READFile`` command.
            - ``.rename``: The ``FILESystem:REName`` command.
            - ``.rmdir``: The ``FILESystem:RMDir`` command.
            - ``.writefile``: The ``FILESystem:WRITEFile`` command.
        """
        return self._filesystem

    @property
    def filtervu(self) -> Filtervu:
        """Return the ``FILTERVu`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``FILTERVu?`` query.
            - Using the ``.verify(value)`` method will send the ``FILTERVu?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``FILTERVu:FREQuency`` command.
        """
        return self._filtervu

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
    def gpibusb(self) -> Gpibusb:
        """Return the ``GPIBUsb`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``GPIBUsb?`` query.
            - Using the ``.verify(value)`` method will send the ``GPIBUsb?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.id``: The ``GPIBUsb:ID`` command.
        """
        return self._gpibusb

    @property
    def hardcopy(self) -> Hardcopy:
        """Return the ``HARDCopy`` command.

        Description:
            - Sends a hard copy of the screen display to the currently active printer using the
              current palette and layout settings.

        Usage:
            - Using the ``.query()`` method will send the ``HARDCopy?`` query.
            - Using the ``.verify(value)`` method will send the ``HARDCopy?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HARDCopy value`` command.

        SCPI Syntax:
            ```
            - HARDCopy {START}
            - HARDCopy?
            ```

        Info:
            - ``START`` sends a block of data representing the current screen image to the requested
              port. The data sent is in the image format specified by ``SAVE:IMAGE:FILEFORMAT``, and
              the compression level is controlled by whatever format has been selected (BMP and TIFF
              are uncompressed, while PNG is compressed).

        Sub-properties:
            - ``.activeprinter``: The ``HARDCopy:ACTIVeprinter`` command.
            - ``.inksaver``: The ``HARDCopy:INKSaver`` command.
            - ``.layout``: The ``HARDCopy:LAYout`` command.
            - ``.preview``: The ``HARDCopy:PREVIEW`` command.
            - ``.printer``: The ``HARDCopy:PRINTer`` command tree.
        """
        return self._hardcopy

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
            - ``.acqlength``: The ``HORizontal:ACQLENGTH`` command.
            - ``.delay``: The ``HORizontal:DELay`` command tree.
            - ``.digital``: The ``HORizontal:DIGital`` command tree.
            - ``.main``: The ``HORizontal:MAIn`` command.
            - ``.position``: The ``HORizontal:POSition`` command.
            - ``.previewstate``: The ``HORizontal:PREViewstate`` command.
            - ``.recordlength``: The ``HORizontal:RECOrdlength`` command.
            - ``.resolution``: The ``HORizontal:RESOlution`` command.
            - ``.samplerate``: The ``HORizontal:SAMPLERate`` command.
            - ``.scale``: The ``HORizontal:SCAle`` command.
            - ``.trigger``: The ``HORizontal:TRIGger`` command tree.
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
    def language(self) -> Language:
        """Return the ``LANGuage`` command.

        Description:
            - This command specifies the user interface display language. This command only affects
              the oscilloscope displayed language. Remote commands and their responses are always in
              English.

        Usage:
            - Using the ``.query()`` method will send the ``LANGuage?`` query.
            - Using the ``.verify(value)`` method will send the ``LANGuage?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LANGuage value`` command.

        SCPI Syntax:
            ```
            - LANGuage {ENGLish|FRENch|GERMan|ITALian|SPANish|PORTUguese|JAPAnese|KOREan|RUSSian|SIMPlifiedchinese|TRADitionalchinese}
            - LANGuage?
            ```
        """  # noqa: E501
        return self._language

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
            - ``.selected``: The ``MARK:SELected`` command tree.
            - ``.total``: The ``MARK:TOTal`` command.
        """
        return self._mark

    @property
    def math1(self) -> Math1:
        """Return the ``MATH1`` command.

        Description:
            - Returns the definition of the math waveform. The returned data depends on the setting
              of the ``MATH1:TYPE`` command.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATH1?
            ```

        Sub-properties:
            - ``.define``: The ``MATH1:DEFine`` command.
            - ``.horizontal``: The ``MATH1:HORizontal`` command tree.
            - ``.label``: The ``MATH1:LABel`` command.
            - ``.spectral``: The ``MATH1:SPECTral`` command tree.
            - ``.type``: The ``MATH1:TYPe`` command.
            - ``.vertical``: The ``MATH1:VERTical`` command tree.
        """
        return self._math1

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
            - ``.clearsnapshot``: The ``MEASUrement:CLEARSNapshot`` command.
            - ``.gating``: The ``MEASUrement:GATing`` command.
            - ``.immed``: The ``MEASUrement:IMMed`` command.
            - ``.indicators``: The ``MEASUrement:INDICators`` command.
            - ``.meas``: The ``MEASUrement:MEAS<x>`` command.
            - ``.method``: The ``MEASUrement:METHod`` command.
            - ``.reflevel``: The ``MEASUrement:REFLevel`` command.
            - ``.snapshot``: The ``MEASUrement:SNAPShot`` command.
            - ``.statistics``: The ``MEASUrement:STATIstics`` command.
        """
        return self._measurement

    @property
    def message(self) -> Message:
        """Return the ``MESSage`` command.

        Description:
            - This command sets or queries message box (screen annotation) parameters.

        Usage:
            - Using the ``.query()`` method will send the ``MESSage?`` query.
            - Using the ``.verify(value)`` method will send the ``MESSage?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``MESSage`` command.

        SCPI Syntax:
            ```
            - MESSage
            - MESSage?
            ```

        Sub-properties:
            - ``.box``: The ``MESSage:BOX`` command.
            - ``.clear``: The ``MESSage:CLEAR`` command.
            - ``.show``: The ``MESSage:SHOW`` command.
            - ``.state``: The ``MESSage:STATE`` command.
        """
        return self._message

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
    def pictbridge(self) -> Pictbridge:
        """Return the ``PICTBridge`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PICTBridge?`` query.
            - Using the ``.verify(value)`` method will send the ``PICTBridge?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dateprint``: The ``PICTBridge:DATEPrint`` command.
            - ``.default``: The ``PICTBridge:DEFault`` command.
            - ``.idprint``: The ``PICTBridge:IDPrint`` command.
            - ``.imagesize``: The ``PICTBridge:IMAGESize`` command.
            - ``.papersize``: The ``PICTBridge:PAPERSize`` command.
            - ``.papertype``: The ``PICTBridge:PAPERType`` command.
            - ``.printqual``: The ``PICTBridge:PRINTQual`` command.
        """
        return self._pictbridge

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
            - ``.setup``: The ``RECAll:SETUp`` command.
            - ``.waveform``: The ``RECAll:WAVEform`` command.
        """
        return self._recall

    @property
    def ref(self) -> Dict[int, RefItem]:
        """Return the ``REF<x>`` command.

        Description:
            - This query returns data for the reference waveform specified by <x>.

        Usage:
            - Using the ``.query()`` method will send the ``REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REF<x>?
            ```

        Sub-properties:
            - ``.date``: The ``REF<x>:DATE`` command.
            - ``.horizontal``: The ``REF<x>:HORizontal`` command tree.
            - ``.label``: The ``REF<x>:LABel`` command.
            - ``.position``: The ``REF<x>:POSition`` command.
            - ``.scale``: The ``REF<x>:SCAle`` command.
            - ``.time``: The ``REF<x>:TIMe`` command.
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
            - ``.assign``: The ``SAVe:ASSIgn`` command tree.
            - ``.eventtable``: The ``SAVe:EVENTtable`` command tree.
            - ``.image``: The ``SAVe:IMAGe`` command.
            - ``.setup``: The ``SAVe:SETUp`` command.
            - ``.waveform``: The ``SAVe:WAVEform`` command.
        """
        return self._save

    @property
    def search(self) -> Search:
        """Return the ``SEARCH`` command.

        Description:
            - Returns all search-related settings.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCH?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCH?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SEARCH?
            ```

        Sub-properties:
            - ``.search``: The ``SEARCH:SEARCH<x>`` command tree.
        """
        return self._search

    @property
    def select(self) -> Select:
        """Return the ``SELect`` command.

        Description:
            - Sets or returns the selected waveform display (controlled by the front-panel) on or
              off.

        Usage:
            - Using the ``.write(value)`` method will send the ``SELect value`` command.

        SCPI Syntax:
            ```
            - SELect {ON|OFF}
            ```

        Info:
            - ``ON`` turns the selected waveform display on.
            - ``OFF`` turns the selected waveform display off.

        Sub-properties:
            - ``.bus``: The ``SELect:BUS<x>`` command.
            - ``.ch``: The ``SELect:CH<x>`` command.
            - ``.control``: The ``SELect:CONTROl`` command.
            - ``.d``: The ``SELect:D<x>`` command.
            - ``.math1``: The ``SELect:MATH1`` command.
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
    def setup(self) -> Dict[int, SetupItem]:
        """Return the ``SETUP<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SETUP<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SETUP<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.date``: The ``SETUP<x>:DATE`` command.
            - ``.label``: The ``SETUP<x>:LABEL`` command.
            - ``.time``: The ``SETUP<x>:TIME`` command.
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
            - ``.b``: The ``TRIGger:B`` command tree.
            - ``.external``: The ``TRIGger:EXTernal`` command.
            - ``.frequency``: The ``TRIGger:FREQuency`` command.
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
    def usbtmc(self) -> Usbtmc:
        """Return the ``USBTMC`` command.

        Description:
            - Returns the ``USBTMC`` information used by the USB hosts to determine the instrument
              interfaces.

        Usage:
            - Using the ``.query()`` method will send the ``USBTMC?`` query.
            - Using the ``.verify(value)`` method will send the ``USBTMC?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - USBTMC?
            ```

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
            - ``.composition``: The ``WFMInpre:COMPosition`` command.
            - ``.encdg``: The ``WFMInpre:ENCdg`` command.
            - ``.filterfreq``: The ``WFMInpre:FILTERFreq`` command.
            - ``.nr_pt``: The ``WFMInpre:NR_Pt`` command.
            - ``.pt_fmt``: The ``WFMInpre:PT_Fmt`` command.
            - ``.pt_off``: The ``WFMInpre:PT_Off`` command.
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
            - ``.composition``: The ``WFMOutpre:COMPosition`` command.
            - ``.encdg``: The ``WFMOutpre:ENCdg`` command.
            - ``.filterfreq``: The ``WFMOutpre:FILTERFreq`` command.
            - ``.fractional``: The ``WFMOutpre:FRACTional`` command.
            - ``.nr_pt``: The ``WFMOutpre:NR_Pt`` command.
            - ``.pt_fmt``: The ``WFMOutpre:PT_Fmt`` command.
            - ``.pt_order``: The ``WFMOutpre:PT_ORder`` command.
            - ``.pt_off``: The ``WFMOutpre:PT_Off`` command.
            - ``.recordlength``: The ``WFMOutpre:RECOrdlength`` command.
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
    def zoom(self) -> Zoom:
        """Return the ``ZOOm`` command.

        Description:
            - Returns the current vertical and horizontal positioning and scaling of the display.

        Usage:
            - Using the ``.query()`` method will send the ``ZOOm?`` query.
            - Using the ``.verify(value)`` method will send the ``ZOOm?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ZOOm?
            ```

        Sub-properties:
            - ``.zoom1``: The ``ZOOm:ZOOM1`` command.
            - ``.mode``: The ``ZOOm:MODe`` command.
            - ``.state``: The ``ZOOm:STATE`` command.
        """
        return self._zoom


class MSO2KBMixin:
    """A mixin that provides access to the MSO2KB commands and constants.

    Properties:
        - ``.command_argument_constants``: The MSO2KB command argument constants.
        - ``.commands``: The MSO2KB commands.
    """

    @cached_property
    def command_argument_constants(self) -> MSO2KBCommandConstants:  # pylint: disable=no-self-use
        """Return the MSO2KB command argument constants.

        This provides access to all the string constants which can be used as arguments for MSO2KB
        commands.
        """
        return MSO2KBCommandConstants()

    @cached_property
    def commands(self) -> MSO2KBCommands:
        """Return the MSO2KB commands.

        This provides access to all the commands for the MSO2KB device. See the documentation of
        each sub-property for more usage information.

        Sub-properties:
            - ``.acquire``: The ``ACQuire`` command.
            - ``.alias``: The ``ALIas`` command.
            - ``.allev``: The ``ALLEv`` command.
            - ``.autoset``: The ``AUTOSet`` command.
            - ``.auxin``: The ``AUXin`` command.
            - ``.bus``: The ``BUS`` command.
            - ``.busy``: The ``BUSY`` command.
            - ``.cal``: The ``*CAL`` command.
            - ``.calibrate``: The ``CALibrate`` command tree.
            - ``.ch``: The ``CH<x>`` command.
            - ``.clearmenu``: The ``CLEARMenu`` command.
            - ``.cls``: The ``*CLS`` command.
            - ``.cursor``: The ``CURSor`` command.
            - ``.curve``: The ``CURVe`` command.
            - ``.d``: The ``D<x>`` command.
            - ``.data``: The ``DATa`` command.
            - ``.date``: The ``DATE`` command.
            - ``.ddt``: The ``*DDT`` command.
            - ``.dese``: The ``DESE`` command.
            - ``.diag``: The ``DIAg`` command tree.
            - ``.display``: The ``DISplay`` command.
            - ``.errlog``: The ``ERRlog`` command.
            - ``.ese``: The ``*ESE`` command.
            - ``.esr``: The ``*ESR`` command.
            - ``.ethernet``: The ``ETHERnet`` command tree.
            - ``.event``: The ``EVENT`` command.
            - ``.evmsg``: The ``EVMsg`` command.
            - ``.evqty``: The ``EVQty`` command.
            - ``.factory``: The ``FACtory`` command.
            - ``.filesystem``: The ``FILESystem`` command.
            - ``.filtervu``: The ``FILTERVu`` command tree.
            - ``.fpanel``: The ``FPAnel`` command tree.
            - ``.gpibusb``: The ``GPIBUsb`` command tree.
            - ``.hardcopy``: The ``HARDCopy`` command.
            - ``.header``: The ``HEADer`` command.
            - ``.horizontal``: The ``HORizontal`` command.
            - ``.id``: The ``ID`` command.
            - ``.idn``: The ``*IDN`` command.
            - ``.language``: The ``LANGuage`` command.
            - ``.lock``: The ``LOCk`` command.
            - ``.lrn``: The ``*LRN`` command.
            - ``.mark``: The ``MARK`` command.
            - ``.math1``: The ``MATH1`` command.
            - ``.mathvar``: The ``MATHVAR`` command.
            - ``.measurement``: The ``MEASUrement`` command.
            - ``.message``: The ``MESSage`` command.
            - ``.newpass``: The ``NEWpass`` command.
            - ``.opc``: The ``*OPC`` command.
            - ``.password``: The ``PASSWord`` command.
            - ``.pictbridge``: The ``PICTBridge`` command tree.
            - ``.psc``: The ``*PSC`` command.
            - ``.pud``: The ``*PUD`` command.
            - ``.rcl``: The ``*RCL`` command.
            - ``.recall``: The ``RECAll`` command tree.
            - ``.ref``: The ``REF<x>`` command.
            - ``.rem``: The ``REM`` command.
            - ``.rst``: The ``*RST`` command.
            - ``.sav``: The ``*SAV`` command.
            - ``.save``: The ``SAVe`` command tree.
            - ``.search``: The ``SEARCH`` command.
            - ``.select``: The ``SELect`` command.
            - ``.set``: The ``SET`` command.
            - ``.setup``: The ``SETUP<x>`` command tree.
            - ``.sre``: The ``*SRE`` command.
            - ``.stb``: The ``*STB`` command.
            - ``.teksecure``: The ``TEKSecure`` command.
            - ``.time``: The ``TIME`` command.
            - ``.totaluptime``: The ``TOTaluptime`` command.
            - ``.trg``: The ``*TRG`` command.
            - ``.trigger``: The ``TRIGger`` command.
            - ``.tst``: The ``*TST`` command.
            - ``.unlock``: The ``UNLock`` command.
            - ``.usbdevice``: The ``USBDevice`` command tree.
            - ``.usbtmc``: The ``USBTMC`` command.
            - ``.verbose``: The ``VERBose`` command.
            - ``.wai``: The ``*WAI`` command.
            - ``.wavfrm``: The ``WAVFrm`` command.
            - ``.wfminpre``: The ``WFMInpre`` command.
            - ``.wfmoutpre``: The ``WFMOutpre`` command.
            - ``.zoom``: The ``ZOOm`` command.
        """
        device = self if isinstance(self, PIControl) else None
        return MSO2KBCommands(device)
