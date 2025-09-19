# pylint: disable=line-too-long
"""The errordetector commands module.

These commands are used in the following models:
DPO70KSX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ERRORDetector:ALERT {ON|OFF|<NR1>}
    - ERRORDetector:ALERT?
    - ERRORDetector:ALIGNCHARacter:MINus?
    - ERRORDetector:ALIGNCHARacter:PLUS?
    - ERRORDetector:ALIGNCHARacter:SYMBOL <QString>
    - ERRORDetector:ALIGNCHARacter:SYMBOL?
    - ERRORDetector:ALIGNCHARacter?
    - ERRORDetector:ALIGNPRIMitive:MINUS?
    - ERRORDetector:ALIGNPRIMitive:MINus<x>?
    - ERRORDetector:ALIGNPRIMitive:PLUS<x>?
    - ERRORDetector:ALIGNPRIMitive:PLUS?
    - ERRORDetector:ALIGNPRIMitive:STATE {ON|OFF|<NR1>}
    - ERRORDetector:ALIGNPRIMitive:STATE?
    - ERRORDetector:ALIGNPRIMitive:SYMBOL<x> <QString>
    - ERRORDetector:ALIGNPRIMitive:SYMBOL<x>?
    - ERRORDetector:ALIGNPRIMitive:SYMBOLS
    - ERRORDetector:ALIGNPRIMitive:SYMBOLS?
    - ERRORDetector:ALIGNPRIMitive?
    - ERRORDetector:BIT:LENgth <NR1>
    - ERRORDetector:BIT:LENgth?
    - ERRORDetector:BIT:PATTERNFilename <fileName>
    - ERRORDetector:BIT:PATTERNFilename?
    - ERRORDetector:BIT:SYNCPATtern:BITString <QString>
    - ERRORDetector:BIT:SYNCPATtern:BITString?
    - ERRORDetector:BIT:SYNCPATtern:DISParity<x> {RDPLUS|RDMINUS}
    - ERRORDetector:BIT:SYNCPATtern:DISParity<x>?
    - ERRORDetector:BIT:SYNCPATtern:MINus<x>?
    - ERRORDetector:BIT:SYNCPATtern:PLUS<x>?
    - ERRORDetector:BIT:SYNCPATtern?
    - ERRORDetector:BIT:TEST <LEARN | START | STOP | CLEAR | SYNC>DPO70000SX<START | STOP | CLEAR>
    - ERRORDetector:BIT:TEST:COUNt?
    - ERRORDetector:BIT:TEST:DURATION?
    - ERRORDetector:BIT:TEST:MAXALIGNS?
    - ERRORDetector:BIT:TEST:RATE?
    - ERRORDetector:BIT:TEST:RESults?
    - ERRORDetector:BIT:TEST:SECOnds?
    - ERRORDetector:BIT:TEST:STATUS:LOCK?
    - ERRORDetector:BIT:TEST:STATUS:MAX_AP?
    - ERRORDetector:BIT:TEST:STATUS:SIGNAL?
    - ERRORDetector:BIT:TEST:STATUS:START?
    - ERRORDetector:BIT:TEST:STATUS:SYNC?
    - ERRORDetector:BIT:TEST:STATUS?
    - ERRORDetector:BIT:TEST:TIME:DAYS?
    - ERRORDetector:BIT:TEST:TIME:HOURS?
    - ERRORDetector:BIT:TEST:TIME:MINUTES?
    - ERRORDetector:BIT:TEST:TIME:SECOnds?
    - ERRORDetector:BIT:TEST:TIME?
    - ERRORDetector:BITRate {RATEcustom:CUSTOM|RATE312000000:RATE312|RATE1250000000:RATE1250|RATE1500000000:RATE1500|RATE2125000000:RATE2125|RATE2500000000:RATE2500|RATE3000000000:RATE3000|RATE3125000000:RATE3125|RATE4250000000:RATE4250|RATE5000000000:RATE5000|RATE6000000000:RATE6000|RATE6250000000:RATE6250}DPO70000SX{RATE3200|RATE3600|RATE4000|RATE4400|RATE4800|RATE5200|RATE5600|RATE6000|RATE6400|CUSTOM}
    - ERRORDetector:BITRate:VALue <NR3>
    - ERRORDetector:BITRate:VALue?
    - ERRORDetector:BITRate?
    - ERRORDetector:CHANnel {CH1|CH2|CH3|CH4}
    - ERRORDetector:CHANnel?
    - ERRORDetector:DURATION:COUNt <NR1>
    - ERRORDetector:DURATION:COUNt?
    - ERRORDetector:DURATION:SECOnds <NR1>
    - ERRORDetector:DURATION:SECOnds?
    - ERRORDetector:DURATION:TIME <NR1>
    - ERRORDetector:DURATION:TIME:DAYS <NR1>
    - ERRORDetector:DURATION:TIME:DAYS?
    - ERRORDetector:DURATION:TIME:HOURS <NR1>
    - ERRORDetector:DURATION:TIME:HOURS?
    - ERRORDetector:DURATION:TIME:MINUTES <NR1>
    - ERRORDetector:DURATION:TIME:MINUTES?
    - ERRORDetector:DURATION:TIME:SECOnds <NR1>
    - ERRORDetector:DURATION:TIME:SECOnds?
    - ERRORDetector:DURATION:TIME?
    - ERRORDetector:ERRORLIMIT <NR1>
    - ERRORDetector:ERRORLIMIT?
    - ERRORDetector:FILE:RECAll <fileName>
    - ERRORDetector:FILE:SAVe <fileName>
    - ERRORDetector:FONTSIze {DEFAULT|LARGE|XLARGE}
    - ERRORDetector:FONTSIze?
    - ERRORDetector:FRAme:EOF <Qstring>
    - ERRORDetector:FRAme:EOF?
    - ERRORDetector:FRAme:INITIALCRCVALue <NR1>
    - ERRORDetector:FRAme:INITIALCRCVALue?
    - ERRORDetector:FRAme:SOF <Qstring>
    - ERRORDetector:FRAme:SOF?
    - ERRORDetector:FRAme:TEST <START|STOP|CLEAR|SYNC>
    - ERRORDetector:FRAme:TEST:BADCHARS?
    - ERRORDetector:FRAme:TEST:COUNt?
    - ERRORDetector:FRAme:TEST:DISParity?
    - ERRORDetector:FRAme:TEST:DURATION?
    - ERRORDetector:FRAme:TEST:MAXALIGNS?
    - ERRORDetector:FRAme:TEST:RATE?
    - ERRORDetector:FRAme:TEST:RESults?
    - ERRORDetector:FRAme:TEST:SECOnds?
    - ERRORDetector:FRAme:TEST:STATUS:LOCK?
    - ERRORDetector:FRAme:TEST:STATUS:MAX_AP?
    - ERRORDetector:FRAme:TEST:STATUS:SIGNAL?
    - ERRORDetector:FRAme:TEST:STATUS:START?
    - ERRORDetector:FRAme:TEST:STATUS?
    - ERRORDetector:FRAme:TEST:TIME:DAYS?
    - ERRORDetector:FRAme:TEST:TIME:HOURS?
    - ERRORDetector:FRAme:TEST:TIME:MINUTES?
    - ERRORDetector:FRAme:TEST:TIME:SECOnds?
    - ERRORDetector:FRAme:TEST:TIME?
    - ERRORDetector:FRAme:TEST?
    - ERRORDetector:FRAme?
    - ERRORDetector:MAXALIGNS <NR1>
    - ERRORDetector:MAXALIGNS?
    - ERRORDetector:PATTERNNAME <Qstring>
    - ERRORDetector:PATTERNNAME?
    - ERRORDetector:PREset {SATA1_CJTPAT_BIT|SATA2_CJTPAT_BIT|SATA3_CJTPAT_BIT|SATA3_FRAME|SATA3_CHAR|SATA3_HFTP_BIT|SATA3_LBP_BIT|SATA3_LFTP_BIT|SATA3_MFTP_BIT|USB3_SYMBOL|USB3_CHAR|PCIE1_COMP_BIT|PCIE2_COMP_BIT|ANY_CJTPAT_BIT|ANY_CJTPAT_CHAR|CUSTOM}DPO70000SX{CUSTOM_SETUP|PRBS7_BIT_ERROR|PRBS9_BIT_ERROR|PRBS11_BIT_ERROR|PRBS16_BIT_ERROR|PRBS23_BIT_ERROR}
    - ERRORDetector:PREset:APPLY
    - ERRORDetector:SAVEIMAGE {OFF|ON}
    - ERRORDetector:SAVEIMAGE?
    - ERRORDetector:SAVEWFM {OFF|ON}
    - ERRORDetector:SAVEWFM?
    - ERRORDetector:SCRAMBLED {ON|OFF}
    - ERRORDetector:SCRAMBLED?
    - ERRORDetector:SENDEMAIL {OFF|ON}
    - ERRORDetector:SENDEMAIL?
    - ERRORDetector:SIGnaltype {ANY8B10B|CUSTOM|PCIEGEN<x>|PRBS11|PRBS16|PRBS23|PRBS7|PRBS9|SATAGEN<x>|USB3}
    - ERRORDetector:SIGnaltype?
    - ERRORDetector:SSC {ON|OFF}
    - ERRORDetector:SSC?
    - ERRORDetector:STANdard <LIST>
    - ERRORDetector:STANdard?
    - ERRORDetector:STATE {ON|OFF|<NR1>}
    - ERRORDetector:STATE?
    - ERRORDetector:STATus?
    - ERRORDetector:STOPWHEN <MANUAL | COUNT | TIME | ERROR>DPO70000SX<MANUAL>
    - ERRORDetector:STOPWHEN?
    - ERRORDetector:SYMBOL:TEST <START|STOP|CLEAR>
    - ERRORDetector:SYMBOL:TEST:BADCHARS?
    - ERRORDetector:SYMBOL:TEST:BITCOUNT?
    - ERRORDetector:SYMBOL:TEST:BITDURATION?
    - ERRORDetector:SYMBOL:TEST:BITRate?
    - ERRORDetector:SYMBOL:TEST:COUNt?
    - ERRORDetector:SYMBOL:TEST:DISParity?
    - ERRORDetector:SYMBOL:TEST:DURATION?
    - ERRORDetector:SYMBOL:TEST:MAXALIGNS?
    - ERRORDetector:SYMBOL:TEST:RATE?
    - ERRORDetector:SYMBOL:TEST:RESults?
    - ERRORDetector:SYMBOL:TEST:SECOnds?
    - ERRORDetector:SYMBOL:TEST:STATUS:LOCK?
    - ERRORDetector:SYMBOL:TEST:STATUS:MAX_AP?
    - ERRORDetector:SYMBOL:TEST:STATUS:SIGNAL?
    - ERRORDetector:SYMBOL:TEST:STATUS:START?
    - ERRORDetector:SYMBOL:TEST:STATUS?
    - ERRORDetector:SYMBOL:TEST:TIME:DAYS?
    - ERRORDetector:SYMBOL:TEST:TIME:HOURS?
    - ERRORDetector:SYMBOL:TEST:TIME:MINUTES?
    - ERRORDetector:SYMBOL:TEST:TIME:SECOnds?
    - ERRORDetector:SYMBOL:TEST:TIME?
    - ERRORDetector:SYMBOL:TEST?
    - ERRORDetector:SYMBOL?
    - ERRORDetector:TIMEformat {DDHHMMSS|SECONDS}
    - ERRORDetector:TIMEformat?
    - ERRORDetector:TYPe {BIT|FRAME|SYMBOL|CHARACTER|PRBS7|PRBS9}
    - ERRORDetector:TYPe?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ErrordetectorType(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:TYPe`` command.

    Description:
        - This command sets or queries the error detector type.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:TYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:TYPe value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:TYPe {BIT|FRAME|SYMBOL|CHARACTER|PRBS7|PRBS9}
        - ERRORDetector:TYPe?
        ```

    Info:
        - ``BIT`` sets the error detector type to bit.
        - ``FRAME`` sets the error detector type to frame.
        - ``SYMBOL`` sets the error detector type to symbol.
        - ``CHARACTER`` sets the error detector type to character.
        - ``PRBS7`` sets the error detector type to PRBS7.
        - ``PRBS9`` sets the error detector type to PRBS9.
    """


class ErrordetectorTimeformat(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:TIMEformat`` command.

    Description:
        - This command sets or queries error detector Elapsed Time Format as DDHHMMSS or Seconds.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:TIMEformat?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:TIMEformat?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:TIMEformat value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:TIMEformat {DDHHMMSS|SECONDS}
        - ERRORDetector:TIMEformat?
        ```
    """


class ErrordetectorSymbolTestTimeSeconds(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:TIME:SECOnds`` command.

    Description:
        - This command queries the elapsed time seconds component for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:TIME:SECOnds?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:SYMBOL:TEST:TIME:SECOnds?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:TIME:SECOnds?
        ```
    """


class ErrordetectorSymbolTestTimeMinutes(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:TIME:MINUTES`` command.

    Description:
        - This command queries the elapsed time minutes component for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:TIME:MINUTES?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:SYMBOL:TEST:TIME:MINUTES?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:TIME:MINUTES?
        ```
    """


class ErrordetectorSymbolTestTimeHours(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:TIME:HOURS`` command.

    Description:
        - This command queries the elapsed time hours component for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:TIME:HOURS?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:SYMBOL:TEST:TIME:HOURS?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:TIME:HOURS?
        ```
    """


class ErrordetectorSymbolTestTimeDays(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:TIME:DAYS`` command.

    Description:
        - This command queries the elapsed time days component for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:TIME:DAYS?``
          query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:TIME:DAYS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:TIME:DAYS?
        ```
    """


class ErrordetectorSymbolTestTime(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:TIME`` command.

    Description:
        - This command queries the elapsed time (in days, hours, minutes, and seconds) for symbol
          error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:TIME?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:TIME?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:TIME?
        ```

    Properties:
        - ``.days``: The ``ERRORDetector:SYMBOL:TEST:TIME:DAYS`` command.
        - ``.hours``: The ``ERRORDetector:SYMBOL:TEST:TIME:HOURS`` command.
        - ``.minutes``: The ``ERRORDetector:SYMBOL:TEST:TIME:MINUTES`` command.
        - ``.seconds``: The ``ERRORDetector:SYMBOL:TEST:TIME:SECOnds`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._days = ErrordetectorSymbolTestTimeDays(device, f"{self._cmd_syntax}:DAYS")
        self._hours = ErrordetectorSymbolTestTimeHours(device, f"{self._cmd_syntax}:HOURS")
        self._minutes = ErrordetectorSymbolTestTimeMinutes(device, f"{self._cmd_syntax}:MINUTES")
        self._seconds = ErrordetectorSymbolTestTimeSeconds(device, f"{self._cmd_syntax}:SECOnds")

    @property
    def days(self) -> ErrordetectorSymbolTestTimeDays:
        """Return the ``ERRORDetector:SYMBOL:TEST:TIME:DAYS`` command.

        Description:
            - This command queries the elapsed time days component for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:TIME:DAYS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:TIME:DAYS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:TIME:DAYS?
            ```
        """
        return self._days

    @property
    def hours(self) -> ErrordetectorSymbolTestTimeHours:
        """Return the ``ERRORDetector:SYMBOL:TEST:TIME:HOURS`` command.

        Description:
            - This command queries the elapsed time hours component for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:TIME:HOURS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:TIME:HOURS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:TIME:HOURS?
            ```
        """
        return self._hours

    @property
    def minutes(self) -> ErrordetectorSymbolTestTimeMinutes:
        """Return the ``ERRORDetector:SYMBOL:TEST:TIME:MINUTES`` command.

        Description:
            - This command queries the elapsed time minutes component for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the
              ``ERRORDetector:SYMBOL:TEST:TIME:MINUTES?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:TIME:MINUTES?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:TIME:MINUTES?
            ```
        """
        return self._minutes

    @property
    def seconds(self) -> ErrordetectorSymbolTestTimeSeconds:
        """Return the ``ERRORDetector:SYMBOL:TEST:TIME:SECOnds`` command.

        Description:
            - This command queries the elapsed time seconds component for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the
              ``ERRORDetector:SYMBOL:TEST:TIME:SECOnds?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:TIME:SECOnds?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:TIME:SECOnds?
            ```
        """
        return self._seconds


class ErrordetectorSymbolTestStatusStart(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:STATUS:START`` command.

    Description:
        - This command queries the START status for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:STATUS:START?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:SYMBOL:TEST:STATUS:START?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:STATUS:START?
        ```
    """


class ErrordetectorSymbolTestStatusSignal(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:STATUS:SIGNAL`` command.

    Description:
        - This command queries the SIGNAL status for the symbol error test.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:STATUS:SIGNAL?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:SYMBOL:TEST:STATUS:SIGNAL?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:STATUS:SIGNAL?
        ```
    """


class ErrordetectorSymbolTestStatusMaxAp(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:STATUS:MAX_AP`` command.

    Description:
        - This command queries the ``MAX_AP`` status for the symbol error test.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:STATUS:MAX_AP?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:SYMBOL:TEST:STATUS:MAX_AP?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:STATUS:MAX_AP?
        ```
    """


class ErrordetectorSymbolTestStatusLock(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:STATUS:LOCK`` command.

    Description:
        - This command queries the LOCK status for the symbol error test.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:STATUS:LOCK?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:SYMBOL:TEST:STATUS:LOCK?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:STATUS:LOCK?
        ```
    """


class ErrordetectorSymbolTestStatus(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:STATUS`` command.

    Description:
        - This command queries all of the status for the symbol error test.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:STATUS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:STATUS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:STATUS?
        ```

    Properties:
        - ``.lock``: The ``ERRORDetector:SYMBOL:TEST:STATUS:LOCK`` command.
        - ``.max_ap``: The ``ERRORDetector:SYMBOL:TEST:STATUS:MAX_AP`` command.
        - ``.signal``: The ``ERRORDetector:SYMBOL:TEST:STATUS:SIGNAL`` command.
        - ``.start``: The ``ERRORDetector:SYMBOL:TEST:STATUS:START`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lock = ErrordetectorSymbolTestStatusLock(device, f"{self._cmd_syntax}:LOCK")
        self._max_ap = ErrordetectorSymbolTestStatusMaxAp(device, f"{self._cmd_syntax}:MAX_AP")
        self._signal = ErrordetectorSymbolTestStatusSignal(device, f"{self._cmd_syntax}:SIGNAL")
        self._start = ErrordetectorSymbolTestStatusStart(device, f"{self._cmd_syntax}:START")

    @property
    def lock(self) -> ErrordetectorSymbolTestStatusLock:
        """Return the ``ERRORDetector:SYMBOL:TEST:STATUS:LOCK`` command.

        Description:
            - This command queries the LOCK status for the symbol error test.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:STATUS:LOCK?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:STATUS:LOCK?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:STATUS:LOCK?
            ```
        """
        return self._lock

    @property
    def max_ap(self) -> ErrordetectorSymbolTestStatusMaxAp:
        """Return the ``ERRORDetector:SYMBOL:TEST:STATUS:MAX_AP`` command.

        Description:
            - This command queries the ``MAX_AP`` status for the symbol error test.

        Usage:
            - Using the ``.query()`` method will send the
              ``ERRORDetector:SYMBOL:TEST:STATUS:MAX_AP?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:STATUS:MAX_AP?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:STATUS:MAX_AP?
            ```
        """
        return self._max_ap

    @property
    def signal(self) -> ErrordetectorSymbolTestStatusSignal:
        """Return the ``ERRORDetector:SYMBOL:TEST:STATUS:SIGNAL`` command.

        Description:
            - This command queries the SIGNAL status for the symbol error test.

        Usage:
            - Using the ``.query()`` method will send the
              ``ERRORDetector:SYMBOL:TEST:STATUS:SIGNAL?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:STATUS:SIGNAL?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:STATUS:SIGNAL?
            ```
        """
        return self._signal

    @property
    def start(self) -> ErrordetectorSymbolTestStatusStart:
        """Return the ``ERRORDetector:SYMBOL:TEST:STATUS:START`` command.

        Description:
            - This command queries the START status for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the
              ``ERRORDetector:SYMBOL:TEST:STATUS:START?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:STATUS:START?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:STATUS:START?
            ```
        """
        return self._start


class ErrordetectorSymbolTestSeconds(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:SECOnds`` command.

    Description:
        - This command queries the elapsed duration time (in seconds) for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:SECOnds?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:SECOnds?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:SECOnds?
        ```
    """


class ErrordetectorSymbolTestResults(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:RESults`` command.

    Description:
        - This command queries all of the results for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:RESults?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:RESults?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:RESults?
        ```
    """


class ErrordetectorSymbolTestRate(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:RATE`` command.

    Description:
        - This command queries the calculated symbol error rate for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:RATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:RATE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:RATE?
        ```
    """


class ErrordetectorSymbolTestMaxaligns(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:MAXALIGNS`` command.

    Description:
        - This command queries the maximum consecutive skip order sets encountered for symbol error
          testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:MAXALIGNS?``
          query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:MAXALIGNS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:MAXALIGNS?
        ```
    """


class ErrordetectorSymbolTestDuration(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:DURATION`` command.

    Description:
        - This command queries the elapsed duration (in units of symbols) for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:DURATION?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:DURATION?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:DURATION?
        ```
    """


class ErrordetectorSymbolTestDisparity(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:DISParity`` command.

    Description:
        - This command queries the disparity error count for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:DISParity?``
          query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:DISParity?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:DISParity?
        ```
    """


class ErrordetectorSymbolTestCount(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:COUNt`` command.

    Description:
        - This command queries the symbol error count for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:COUNt?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:COUNt?
        ```
    """


class ErrordetectorSymbolTestBitrate(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:BITRate`` command.

    Description:
        - This command queries the calculated bit error rate for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:BITRate?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:BITRate?
        ```
    """


class ErrordetectorSymbolTestBitduration(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:BITDURATION`` command.

    Description:
        - This command queries the elapsed duration in units of bits tested for symbol error
          testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:BITDURATION?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:SYMBOL:TEST:BITDURATION?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:BITDURATION?
        ```
    """


class ErrordetectorSymbolTestBitcount(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:BITCOUNT`` command.

    Description:
        - This command queries the bit error count (number of bad bits) for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:BITCOUNT?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:BITCOUNT?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:BITCOUNT?
        ```
    """


class ErrordetectorSymbolTestBadchars(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST:BADCHARS`` command.

    Description:
        - This command queries the illegal character count for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:BADCHARS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:BADCHARS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST:BADCHARS?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class ErrordetectorSymbolTest(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:SYMBOL:TEST`` command.

    Description:
        - This command initiates and terminates symbol error testing for the arguments START and
          STOP. Zeroes the symbol error results for the argument CLEAR. Re-synchronizes the
          recovered clock for the argument SYNC. This command also queries all of the symbol test
          settings and results for symbol error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:SYMBOL:TEST value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL:TEST <START|STOP|CLEAR>
        - ERRORDetector:SYMBOL:TEST?
        ```

    Info:
        - ``START`` initiates symbol and bit error testing.
        - ``STOP`` terminates symbol and bit error testing.
        - ``CLEAR`` zeroes the symbol and bit error counts, duration, bit error rate, and symbol
          error rate.
        - ``SYNC`` re-synchronizes the recovered clock.

    Properties:
        - ``.badchars``: The ``ERRORDetector:SYMBOL:TEST:BADCHARS`` command.
        - ``.bitcount``: The ``ERRORDetector:SYMBOL:TEST:BITCOUNT`` command.
        - ``.bitduration``: The ``ERRORDetector:SYMBOL:TEST:BITDURATION`` command.
        - ``.bitrate``: The ``ERRORDetector:SYMBOL:TEST:BITRate`` command.
        - ``.count``: The ``ERRORDetector:SYMBOL:TEST:COUNt`` command.
        - ``.disparity``: The ``ERRORDetector:SYMBOL:TEST:DISParity`` command.
        - ``.duration``: The ``ERRORDetector:SYMBOL:TEST:DURATION`` command.
        - ``.maxaligns``: The ``ERRORDetector:SYMBOL:TEST:MAXALIGNS`` command.
        - ``.rate``: The ``ERRORDetector:SYMBOL:TEST:RATE`` command.
        - ``.results``: The ``ERRORDetector:SYMBOL:TEST:RESults`` command.
        - ``.seconds``: The ``ERRORDetector:SYMBOL:TEST:SECOnds`` command.
        - ``.status``: The ``ERRORDetector:SYMBOL:TEST:STATUS`` command.
        - ``.time``: The ``ERRORDetector:SYMBOL:TEST:TIME`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._badchars = ErrordetectorSymbolTestBadchars(device, f"{self._cmd_syntax}:BADCHARS")
        self._bitcount = ErrordetectorSymbolTestBitcount(device, f"{self._cmd_syntax}:BITCOUNT")
        self._bitduration = ErrordetectorSymbolTestBitduration(
            device, f"{self._cmd_syntax}:BITDURATION"
        )
        self._bitrate = ErrordetectorSymbolTestBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._count = ErrordetectorSymbolTestCount(device, f"{self._cmd_syntax}:COUNt")
        self._disparity = ErrordetectorSymbolTestDisparity(device, f"{self._cmd_syntax}:DISParity")
        self._duration = ErrordetectorSymbolTestDuration(device, f"{self._cmd_syntax}:DURATION")
        self._maxaligns = ErrordetectorSymbolTestMaxaligns(device, f"{self._cmd_syntax}:MAXALIGNS")
        self._rate = ErrordetectorSymbolTestRate(device, f"{self._cmd_syntax}:RATE")
        self._results = ErrordetectorSymbolTestResults(device, f"{self._cmd_syntax}:RESults")
        self._seconds = ErrordetectorSymbolTestSeconds(device, f"{self._cmd_syntax}:SECOnds")
        self._status = ErrordetectorSymbolTestStatus(device, f"{self._cmd_syntax}:STATUS")
        self._time = ErrordetectorSymbolTestTime(device, f"{self._cmd_syntax}:TIME")

    @property
    def badchars(self) -> ErrordetectorSymbolTestBadchars:
        """Return the ``ERRORDetector:SYMBOL:TEST:BADCHARS`` command.

        Description:
            - This command queries the illegal character count for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:BADCHARS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:BADCHARS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:BADCHARS?
            ```
        """
        return self._badchars

    @property
    def bitcount(self) -> ErrordetectorSymbolTestBitcount:
        """Return the ``ERRORDetector:SYMBOL:TEST:BITCOUNT`` command.

        Description:
            - This command queries the bit error count (number of bad bits) for symbol error
              testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:BITCOUNT?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:BITCOUNT?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:BITCOUNT?
            ```
        """
        return self._bitcount

    @property
    def bitduration(self) -> ErrordetectorSymbolTestBitduration:
        """Return the ``ERRORDetector:SYMBOL:TEST:BITDURATION`` command.

        Description:
            - This command queries the elapsed duration in units of bits tested for symbol error
              testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:BITDURATION?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:BITDURATION?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:BITDURATION?
            ```
        """
        return self._bitduration

    @property
    def bitrate(self) -> ErrordetectorSymbolTestBitrate:
        """Return the ``ERRORDetector:SYMBOL:TEST:BITRate`` command.

        Description:
            - This command queries the calculated bit error rate for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:BITRate?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:BITRate?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:BITRate?
            ```
        """
        return self._bitrate

    @property
    def count(self) -> ErrordetectorSymbolTestCount:
        """Return the ``ERRORDetector:SYMBOL:TEST:COUNt`` command.

        Description:
            - This command queries the symbol error count for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:COUNt?``
              query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:COUNt?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:COUNt?
            ```
        """
        return self._count

    @property
    def disparity(self) -> ErrordetectorSymbolTestDisparity:
        """Return the ``ERRORDetector:SYMBOL:TEST:DISParity`` command.

        Description:
            - This command queries the disparity error count for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:DISParity?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:DISParity?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:DISParity?
            ```
        """
        return self._disparity

    @property
    def duration(self) -> ErrordetectorSymbolTestDuration:
        """Return the ``ERRORDetector:SYMBOL:TEST:DURATION`` command.

        Description:
            - This command queries the elapsed duration (in units of symbols) for symbol error
              testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:DURATION?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:DURATION?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:DURATION?
            ```
        """
        return self._duration

    @property
    def maxaligns(self) -> ErrordetectorSymbolTestMaxaligns:
        """Return the ``ERRORDetector:SYMBOL:TEST:MAXALIGNS`` command.

        Description:
            - This command queries the maximum consecutive skip order sets encountered for symbol
              error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:MAXALIGNS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:MAXALIGNS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:MAXALIGNS?
            ```
        """
        return self._maxaligns

    @property
    def rate(self) -> ErrordetectorSymbolTestRate:
        """Return the ``ERRORDetector:SYMBOL:TEST:RATE`` command.

        Description:
            - This command queries the calculated symbol error rate for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:RATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:RATE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:RATE?
            ```
        """
        return self._rate

    @property
    def results(self) -> ErrordetectorSymbolTestResults:
        """Return the ``ERRORDetector:SYMBOL:TEST:RESults`` command.

        Description:
            - This command queries all of the results for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:RESults?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:RESults?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:RESults?
            ```
        """
        return self._results

    @property
    def seconds(self) -> ErrordetectorSymbolTestSeconds:
        """Return the ``ERRORDetector:SYMBOL:TEST:SECOnds`` command.

        Description:
            - This command queries the elapsed duration time (in seconds) for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:SECOnds?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:SECOnds?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:SECOnds?
            ```
        """
        return self._seconds

    @property
    def status(self) -> ErrordetectorSymbolTestStatus:
        """Return the ``ERRORDetector:SYMBOL:TEST:STATUS`` command.

        Description:
            - This command queries all of the status for the symbol error test.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:STATUS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:SYMBOL:TEST:STATUS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:STATUS?
            ```

        Sub-properties:
            - ``.lock``: The ``ERRORDetector:SYMBOL:TEST:STATUS:LOCK`` command.
            - ``.max_ap``: The ``ERRORDetector:SYMBOL:TEST:STATUS:MAX_AP`` command.
            - ``.signal``: The ``ERRORDetector:SYMBOL:TEST:STATUS:SIGNAL`` command.
            - ``.start``: The ``ERRORDetector:SYMBOL:TEST:STATUS:START`` command.
        """
        return self._status

    @property
    def time(self) -> ErrordetectorSymbolTestTime:
        """Return the ``ERRORDetector:SYMBOL:TEST:TIME`` command.

        Description:
            - This command queries the elapsed time (in days, hours, minutes, and seconds) for
              symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST:TIME?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST:TIME?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST:TIME?
            ```

        Sub-properties:
            - ``.days``: The ``ERRORDetector:SYMBOL:TEST:TIME:DAYS`` command.
            - ``.hours``: The ``ERRORDetector:SYMBOL:TEST:TIME:HOURS`` command.
            - ``.minutes``: The ``ERRORDetector:SYMBOL:TEST:TIME:MINUTES`` command.
            - ``.seconds``: The ``ERRORDetector:SYMBOL:TEST:TIME:SECOnds`` command.
        """
        return self._time


class ErrordetectorSymbol(SCPICmdRead):
    """The ``ERRORDetector:SYMBOL`` command.

    Description:
        - This command queries all symbol error settings, status, and results.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:SYMBOL?
        ```

    Properties:
        - ``.test``: The ``ERRORDetector:SYMBOL:TEST`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._test = ErrordetectorSymbolTest(device, f"{self._cmd_syntax}:TEST")

    @property
    def test(self) -> ErrordetectorSymbolTest:
        """Return the ``ERRORDetector:SYMBOL:TEST`` command.

        Description:
            - This command initiates and terminates symbol error testing for the arguments START and
              STOP. Zeroes the symbol error results for the argument CLEAR. Re-synchronizes the
              recovered clock for the argument SYNC. This command also queries all of the symbol
              test settings and results for symbol error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL:TEST?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL:TEST?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:SYMBOL:TEST value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL:TEST <START|STOP|CLEAR>
            - ERRORDetector:SYMBOL:TEST?
            ```

        Info:
            - ``START`` initiates symbol and bit error testing.
            - ``STOP`` terminates symbol and bit error testing.
            - ``CLEAR`` zeroes the symbol and bit error counts, duration, bit error rate, and symbol
              error rate.
            - ``SYNC`` re-synchronizes the recovered clock.

        Sub-properties:
            - ``.badchars``: The ``ERRORDetector:SYMBOL:TEST:BADCHARS`` command.
            - ``.bitcount``: The ``ERRORDetector:SYMBOL:TEST:BITCOUNT`` command.
            - ``.bitduration``: The ``ERRORDetector:SYMBOL:TEST:BITDURATION`` command.
            - ``.bitrate``: The ``ERRORDetector:SYMBOL:TEST:BITRate`` command.
            - ``.count``: The ``ERRORDetector:SYMBOL:TEST:COUNt`` command.
            - ``.disparity``: The ``ERRORDetector:SYMBOL:TEST:DISParity`` command.
            - ``.duration``: The ``ERRORDetector:SYMBOL:TEST:DURATION`` command.
            - ``.maxaligns``: The ``ERRORDetector:SYMBOL:TEST:MAXALIGNS`` command.
            - ``.rate``: The ``ERRORDetector:SYMBOL:TEST:RATE`` command.
            - ``.results``: The ``ERRORDetector:SYMBOL:TEST:RESults`` command.
            - ``.seconds``: The ``ERRORDetector:SYMBOL:TEST:SECOnds`` command.
            - ``.status``: The ``ERRORDetector:SYMBOL:TEST:STATUS`` command.
            - ``.time``: The ``ERRORDetector:SYMBOL:TEST:TIME`` command.
        """
        return self._test


class ErrordetectorStopwhen(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:STOPWHEN`` command.

    Description:
        - This command sets or queries the stopping condition. The test can be stopped when the
          count, time, or number of errors elapses. If the STOPWHEN value is MANUAL, the test runs
          until a TEST STOP command is received.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:STOPWHEN?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:STOPWHEN?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:STOPWHEN value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:STOPWHEN <MANUAL | COUNT | TIME | ERROR>DPO70000SX<MANUAL>
        - ERRORDetector:STOPWHEN?
        ```

    Info:
        - ``MANUAL`` indicates that the test must be stopped by issuing a TEST STOP command. This is
          the default.
        - ``COUNT`` stops the test when ``DURATION:COUNT`` comparisons are made. The comparisons can
          be bit, frame, symbol, or character as appropriate for the ``TEST:TYPE``.
        - ``TIME`` stops the test when ``DURATION:TIME`` elapses.
        - ``ERROR`` stops the test when the number of errors ≥ ERRORLIMIT.
    """


class ErrordetectorStatus(SCPICmdRead):
    """The ``ERRORDetector:STATus`` command.

    Description:
        - Queries only the 'most significant' or 'summary' status of the error detector. All of the
          status flags for each test type may be obtained from the
          ``ERRORdetector:<TESTTYPE>:TEST:STATUS`` commands. LOCK refers to the recovered clock.
          Signal refers to the cable carrying the signal to the scope. SYNC refers to bit error
          tests that require a sync pattern. STOPPED/COUNTING refer to whether the error detector is
          testing for errors. ``MAX_AP`` refers to whether the error detector has detected the
          maximum consecutive Align (or SkipSets) Primitives as specified in the ERRORDetector:
          <TESTTYPE>MAXALIGNS command

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:STATus?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:STATus?
        ```
    """


class ErrordetectorState(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:STATE`` command.

    Description:
        - This command sets or queries the status of the error option. STATE must be ON to use the
          error detector feature.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:STATE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:STATE value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:STATE {ON|OFF|<NR1>}
        - ERRORDetector:STATE?
        ```

    Info:
        - ``ON`` enables the software error detector feature.
        - ``OFF`` disables the software error detector feature. This is the default.
        - ``<NR1>`` = 0 disables the error detector; any other value enables the error detector.
    """


class ErrordetectorStandard(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:STANdard`` command.

    Description:
        - This command sets or queries the standard selection for error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:STANdard?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:STANdard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:STANdard value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:STANdard <LIST>
        - ERRORDetector:STANdard?
        ```

    Info:
        - ``<LIST>`` is the supported standard.
    """


class ErrordetectorSsc(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:SSC`` command.

    Description:
        - This command sets or queries the status of the spread spectrum clock tracking option.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SSC?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SSC?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:SSC value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:SSC {ON|OFF}
        - ERRORDetector:SSC?
        ```

    Info:
        - ``ON`` enables spread spectrum clock tracking. For error detector, the spread spectrum
          clock tracking should always be turned on.
        - ``OFF`` disables spread spectrum clock tracking. For serial trigger, the spread spectrum
          clock tracking is turned off.
    """


class ErrordetectorSignaltype(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:SIGnaltype`` command.

    Description:
        - This command sets or queries error detector Signal Type control. Setting the signal type
          establishes the bit rate appropriate for the standard, as well as establishing the testing
          algorithm. Custom bit rates may be used as well. See the ``ERRORDetector:BITRATE`` and
          ``ERRORDetector:BITRATE:VALue`` commands.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SIGnaltype?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SIGnaltype?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:SIGnaltype value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:SIGnaltype {ANY8B10B|CUSTOM|PCIEGEN<x>|PRBS11|PRBS16|PRBS23|PRBS7|PRBS9|SATAGEN<x>|USB3}
        - ERRORDetector:SIGnaltype?
        ```

    Info:
        - ``The DPO70000SX only supports PRBS7, PRBS9, PRBS11, PRBS16, PRBS23, and CUSTOM.``
    """  # noqa: E501


class ErrordetectorSendemail(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:SENDEMAIL`` command.

    Description:
        - This command sets or queries error detector Send Email control. When set to ON, a email
          will be sent to the recipient, defined elsewhere in the PI, when the error detector
          detects an error (because detecting an error triggers the instrument). The default number
          of emails sent is 1, so that you do not overflow your inbox. If you also set the SaveImage
          or SaveWfm parameters to ON, the email will contain these items. Send Email is an
          alternate way of setting the E-mail on Trigger actions defined elsewhere in the PI.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SENDEMAIL?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SENDEMAIL?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:SENDEMAIL value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:SENDEMAIL {OFF|ON}
        - ERRORDetector:SENDEMAIL?
        ```

    Info:
        - ``OFF`` disables the send email feature.
        - ``ON`` enables the send email feature.
    """


class ErrordetectorScrambled(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:SCRAMBLED`` command.

    Description:
        - This command sets or queries the status of the error detection data scrambling option.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SCRAMBLED?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SCRAMBLED?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:SCRAMBLED value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:SCRAMBLED {ON|OFF}
        - ERRORDetector:SCRAMBLED?
        ```

    Info:
        - ``ON`` enables the error detection data scrambling option. This is the default option.
        - ``OFF`` disables the error detection data scrambling option.
    """


class ErrordetectorSavewfm(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:SAVEWFM`` command.

    Description:
        - This command sets or queries error detector Save Waveform (WFM) control. When set to ON, a
          waveform object will be made when the error detector detects an error (because detecting
          an error triggers the instrument). The waveforms are saved in the
          C:Users<yourName>TektronixTekScopeSaveOnTrigger directory. A default limit of 10 screen
          shots prevents overflowing your disk drive should the error detector sense massive errors,
          such as when you disconnect the signal. If you also set the SendEmail parameter to ON, the
          saved waveform (wfm object) is emailed to the recipient (set elsewhere in the trigger PI)
          as an attachedment. SaveImage is an alternate way of setting the Save on Trigger actions
          defined elsewhere in the PI.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SAVEWFM?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SAVEWFM?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:SAVEWFM value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:SAVEWFM {OFF|ON}
        - ERRORDetector:SAVEWFM?
        ```

    Info:
        - ``OFF`` turns off the error detector save waveform feature.
        - ``ON`` turns on the error detector save waveform feature.
    """


class ErrordetectorSaveimage(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:SAVEIMAGE`` command.

    Description:
        - Sets or queries error detector Save Image control. When set to ON, a screen shot will be
          made when the error detector detects an error (because detecting an error triggers the
          scope). The images are saved in the C:Users<yourName> TektronixTekScopeSaveOnTrigger
          directory. A default limit of 10 screen shots prevents overflowing your disk drive should
          the error detector sense massive errors, such as when you disconnect the signal. If you
          also set the SendEmail parameter to ON, the saved image (screen shot) will be emailed to
          the recipient (set elsewhere in the trigger PI). SaveImage is an alternate way of setting
          the Save on Trigger actions defined elsewhere in the PI.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:SAVEIMAGE?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:SAVEIMAGE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:SAVEIMAGE value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:SAVEIMAGE {OFF|ON}
        - ERRORDetector:SAVEIMAGE?
        ```
    """


class ErrordetectorPresetApply(SCPICmdWriteNoArguments):
    """The ``ERRORDetector:PREset:APPLY`` command.

    Description:
        - This command causes selected preset setup to be applied. Until this command is received by
          the instrument, the selected preset has not been applied. This mimics the user interface
          operation, which allows window shopping various preset setups, without actually applying
          them to the instrument setup.

    Usage:
        - Using the ``.write()`` method will send the ``ERRORDetector:PREset:APPLY`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:PREset:APPLY
        ```
    """


class ErrordetectorPreset(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:PREset`` command.

    Description:
        - This command sets or queries error detector font preset selection. A number of preset
          setups are selected by this parameter to cover the more common cases. The preset names
          attempt to indicate the standard, signal pattern, and test type employed. The bit rate
          appropriate for the standard is used. The text files containing the preset setups are
          located in the C:UsersPublicTektronixTekScopeErrorDetector directory in Windows. You may
          select CUSTOM as a preset value, and save or recall your own custom setups. You may want
          to recall one of the standard preset setups, modify some of the parameters, and then save
          it as a custom setup for recall at a later time. This same behavior is supported on the
          error detector User Interface. he ``SATA3_FRAME`` preset expects the SATA3 Compliance
          Pattern. ``USB3_SYMBOL`` preset expects the USB3 standard ``CP0_SKP`` signal. You can set
          a PATTERNNAME for each setup.

    Usage:
        - Using the ``.write(value)`` method will send the ``ERRORDetector:PREset value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:PREset {SATA1_CJTPAT_BIT|SATA2_CJTPAT_BIT|SATA3_CJTPAT_BIT|SATA3_FRAME|SATA3_CHAR|SATA3_HFTP_BIT|SATA3_LBP_BIT|SATA3_LFTP_BIT|SATA3_MFTP_BIT|USB3_SYMBOL|USB3_CHAR|PCIE1_COMP_BIT|PCIE2_COMP_BIT|ANY_CJTPAT_BIT|ANY_CJTPAT_CHAR|CUSTOM}DPO70000SX{CUSTOM_SETUP|PRBS7_BIT_ERROR|PRBS9_BIT_ERROR|PRBS11_BIT_ERROR|PRBS16_BIT_ERROR|PRBS23_BIT_ERROR}
        ```

    Properties:
        - ``.apply``: The ``ERRORDetector:PREset:APPLY`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._apply = ErrordetectorPresetApply(device, f"{self._cmd_syntax}:APPLY")

    @property
    def apply(self) -> ErrordetectorPresetApply:
        """Return the ``ERRORDetector:PREset:APPLY`` command.

        Description:
            - This command causes selected preset setup to be applied. Until this command is
              received by the instrument, the selected preset has not been applied. This mimics the
              user interface operation, which allows window shopping various preset setups, without
              actually applying them to the instrument setup.

        Usage:
            - Using the ``.write()`` method will send the ``ERRORDetector:PREset:APPLY`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:PREset:APPLY
            ```
        """
        return self._apply


class ErrordetectorPatternname(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:PATTERNNAME`` command.

    Description:
        - This command sets or queries the pattern name stored in the setup file. Setting this name
          has no functional effect on the instrument, but it is a convenient reminder to users as to
          which setup is in effect.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:PATTERNNAME?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:PATTERNNAME?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:PATTERNNAME value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:PATTERNNAME <Qstring>
        - ERRORDetector:PATTERNNAME?
        ```

    Info:
        - ``<Qstring>`` is a quoted string representing a pattern name.
    """


class ErrordetectorMaxaligns(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:MAXALIGNS`` command.

    Description:
        - This command sets or queries the maximum consecutive align primitives before a
          ``MAX_AP_FAIL`` error is reported.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:MAXALIGNS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:MAXALIGNS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:MAXALIGNS value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:MAXALIGNS <NR1>
        - ERRORDetector:MAXALIGNS?
        ```

    Info:
        - ``<NR1>`` is a integer. The limit values are 0 to 63 and the default is 8.
    """


class ErrordetectorFrameTestTimeSeconds(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:TIME:SECOnds`` command.

    Description:
        - This command queries the elapsed time seconds component for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:TIME:SECOnds?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:FRAme:TEST:TIME:SECOnds?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:TIME:SECOnds?
        ```
    """


class ErrordetectorFrameTestTimeMinutes(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:TIME:MINUTES`` command.

    Description:
        - This command queries the elapsed time minutes component for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:TIME:MINUTES?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:FRAme:TEST:TIME:MINUTES?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:TIME:MINUTES?
        ```
    """


class ErrordetectorFrameTestTimeHours(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:TIME:HOURS`` command.

    Description:
        - This command queries the elapsed time hours component for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:TIME:HOURS?``
          query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:TIME:HOURS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:TIME:HOURS?
        ```
    """


class ErrordetectorFrameTestTimeDays(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:TIME:DAYS`` command.

    Description:
        - This command queries the elapsed time days component for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:TIME:DAYS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:TIME:DAYS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:TIME:DAYS?
        ```
    """


class ErrordetectorFrameTestTime(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:TIME`` command.

    Description:
        - This command queries the elapsed time (in days, hours, minutes, and seconds) for frame
          error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:TIME?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:TIME?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:TIME?
        ```

    Properties:
        - ``.days``: The ``ERRORDetector:FRAme:TEST:TIME:DAYS`` command.
        - ``.hours``: The ``ERRORDetector:FRAme:TEST:TIME:HOURS`` command.
        - ``.minutes``: The ``ERRORDetector:FRAme:TEST:TIME:MINUTES`` command.
        - ``.seconds``: The ``ERRORDetector:FRAme:TEST:TIME:SECOnds`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._days = ErrordetectorFrameTestTimeDays(device, f"{self._cmd_syntax}:DAYS")
        self._hours = ErrordetectorFrameTestTimeHours(device, f"{self._cmd_syntax}:HOURS")
        self._minutes = ErrordetectorFrameTestTimeMinutes(device, f"{self._cmd_syntax}:MINUTES")
        self._seconds = ErrordetectorFrameTestTimeSeconds(device, f"{self._cmd_syntax}:SECOnds")

    @property
    def days(self) -> ErrordetectorFrameTestTimeDays:
        """Return the ``ERRORDetector:FRAme:TEST:TIME:DAYS`` command.

        Description:
            - This command queries the elapsed time days component for frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:TIME:DAYS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:TIME:DAYS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:TIME:DAYS?
            ```
        """
        return self._days

    @property
    def hours(self) -> ErrordetectorFrameTestTimeHours:
        """Return the ``ERRORDetector:FRAme:TEST:TIME:HOURS`` command.

        Description:
            - This command queries the elapsed time hours component for frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:TIME:HOURS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:TIME:HOURS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:TIME:HOURS?
            ```
        """
        return self._hours

    @property
    def minutes(self) -> ErrordetectorFrameTestTimeMinutes:
        """Return the ``ERRORDetector:FRAme:TEST:TIME:MINUTES`` command.

        Description:
            - This command queries the elapsed time minutes component for frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:TIME:MINUTES?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:TIME:MINUTES?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:TIME:MINUTES?
            ```
        """
        return self._minutes

    @property
    def seconds(self) -> ErrordetectorFrameTestTimeSeconds:
        """Return the ``ERRORDetector:FRAme:TEST:TIME:SECOnds`` command.

        Description:
            - This command queries the elapsed time seconds component for frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:TIME:SECOnds?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:TIME:SECOnds?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:TIME:SECOnds?
            ```
        """
        return self._seconds


class ErrordetectorFrameTestStatusStart(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:STATUS:START`` command.

    Description:
        - This command returns the START status for frame error tests.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:STATUS:START?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:FRAme:TEST:STATUS:START?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:STATUS:START?
        ```
    """


class ErrordetectorFrameTestStatusSignal(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:STATUS:SIGNAL`` command.

    Description:
        - This command queries the SIGNAL status for the frame error test.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:STATUS:SIGNAL?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:FRAme:TEST:STATUS:SIGNAL?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:STATUS:SIGNAL?
        ```
    """


class ErrordetectorFrameTestStatusMaxAp(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:STATUS:MAX_AP`` command.

    Description:
        - This command queries the ``MAX_AP`` status for the frame error test.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:STATUS:MAX_AP?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:FRAme:TEST:STATUS:MAX_AP?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:STATUS:MAX_AP?
        ```
    """


class ErrordetectorFrameTestStatusLock(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:STATUS:LOCK`` command.

    Description:
        - This command queries the LOCK status for the frame error test.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:STATUS:LOCK?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:FRAme:TEST:STATUS:LOCK?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:STATUS:LOCK?
        ```
    """


class ErrordetectorFrameTestStatus(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:STATUS`` command.

    Description:
        - This command queries all of the status for frame error status.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:STATUS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:STATUS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:STATUS?
        ```

    Properties:
        - ``.lock``: The ``ERRORDetector:FRAme:TEST:STATUS:LOCK`` command.
        - ``.max_ap``: The ``ERRORDetector:FRAme:TEST:STATUS:MAX_AP`` command.
        - ``.signal``: The ``ERRORDetector:FRAme:TEST:STATUS:SIGNAL`` command.
        - ``.start``: The ``ERRORDetector:FRAme:TEST:STATUS:START`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lock = ErrordetectorFrameTestStatusLock(device, f"{self._cmd_syntax}:LOCK")
        self._max_ap = ErrordetectorFrameTestStatusMaxAp(device, f"{self._cmd_syntax}:MAX_AP")
        self._signal = ErrordetectorFrameTestStatusSignal(device, f"{self._cmd_syntax}:SIGNAL")
        self._start = ErrordetectorFrameTestStatusStart(device, f"{self._cmd_syntax}:START")

    @property
    def lock(self) -> ErrordetectorFrameTestStatusLock:
        """Return the ``ERRORDetector:FRAme:TEST:STATUS:LOCK`` command.

        Description:
            - This command queries the LOCK status for the frame error test.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:STATUS:LOCK?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:STATUS:LOCK?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:STATUS:LOCK?
            ```
        """
        return self._lock

    @property
    def max_ap(self) -> ErrordetectorFrameTestStatusMaxAp:
        """Return the ``ERRORDetector:FRAme:TEST:STATUS:MAX_AP`` command.

        Description:
            - This command queries the ``MAX_AP`` status for the frame error test.

        Usage:
            - Using the ``.query()`` method will send the
              ``ERRORDetector:FRAme:TEST:STATUS:MAX_AP?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:STATUS:MAX_AP?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:STATUS:MAX_AP?
            ```
        """
        return self._max_ap

    @property
    def signal(self) -> ErrordetectorFrameTestStatusSignal:
        """Return the ``ERRORDetector:FRAme:TEST:STATUS:SIGNAL`` command.

        Description:
            - This command queries the SIGNAL status for the frame error test.

        Usage:
            - Using the ``.query()`` method will send the
              ``ERRORDetector:FRAme:TEST:STATUS:SIGNAL?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:STATUS:SIGNAL?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:STATUS:SIGNAL?
            ```
        """
        return self._signal

    @property
    def start(self) -> ErrordetectorFrameTestStatusStart:
        """Return the ``ERRORDetector:FRAme:TEST:STATUS:START`` command.

        Description:
            - This command returns the START status for frame error tests.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:STATUS:START?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:STATUS:START?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:STATUS:START?
            ```
        """
        return self._start


class ErrordetectorFrameTestSeconds(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:SECOnds`` command.

    Description:
        - This command queries the result of elapsed duration in seconds for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:SECOnds?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:SECOnds?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:SECOnds?
        ```
    """


class ErrordetectorFrameTestResults(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:RESults`` command.

    Description:
        - This command queries all the results for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:RESults?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:RESults?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:RESults?
        ```
    """


class ErrordetectorFrameTestRate(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:RATE`` command.

    Description:
        - This command queries the calculated frame error rate.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:RATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:RATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:RATE?
        ```
    """


class ErrordetectorFrameTestMaxaligns(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:MAXALIGNS`` command.

    Description:
        - This command queries the result of the maximum consecutive aligns encountered for frame
          error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:MAXALIGNS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:MAXALIGNS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:MAXALIGNS?
        ```
    """


class ErrordetectorFrameTestDuration(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:DURATION`` command.

    Description:
        - This command queries the elapsed duration in number of frames.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:DURATION?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:DURATION?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:DURATION?
        ```
    """


class ErrordetectorFrameTestDisparity(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:DISParity`` command.

    Description:
        - This command queries the disparity error count for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:DISParity?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:DISParity?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:DISParity?
        ```
    """


class ErrordetectorFrameTestCount(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:COUNt`` command.

    Description:
        - This command queries the test error count for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:COUNt?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:COUNt?
        ```
    """


class ErrordetectorFrameTestBadchars(SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST:BADCHARS`` command.

    Description:
        - This command queries the illegal character count for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:BADCHARS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:BADCHARS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST:BADCHARS?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class ErrordetectorFrameTest(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:FRAme:TEST`` command.

    Description:
        - This command and query initiates and terminates frame error testing for the arguments
          START and STOP. Zeroes the frame error results for the argument CLEAR. Re-synchronizes the
          recovered clock for the argument SYNC.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:FRAme:TEST value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:TEST <START|STOP|CLEAR|SYNC>
        - ERRORDetector:FRAme:TEST?
        ```

    Info:
        - ``START`` initiates the frame error test counting of errors and duration.
        - ``STOP`` terminates the frame error test counting of frame errors and duration.
        - ``CLEAR`` zeroes the frame error test count, duration, and rate.
        - ``SYNC`` re-synchronizes the recovered clock.

    Properties:
        - ``.badchars``: The ``ERRORDetector:FRAme:TEST:BADCHARS`` command.
        - ``.count``: The ``ERRORDetector:FRAme:TEST:COUNt`` command.
        - ``.disparity``: The ``ERRORDetector:FRAme:TEST:DISParity`` command.
        - ``.duration``: The ``ERRORDetector:FRAme:TEST:DURATION`` command.
        - ``.maxaligns``: The ``ERRORDetector:FRAme:TEST:MAXALIGNS`` command.
        - ``.rate``: The ``ERRORDetector:FRAme:TEST:RATE`` command.
        - ``.results``: The ``ERRORDetector:FRAme:TEST:RESults`` command.
        - ``.seconds``: The ``ERRORDetector:FRAme:TEST:SECOnds`` command.
        - ``.status``: The ``ERRORDetector:FRAme:TEST:STATUS`` command.
        - ``.time``: The ``ERRORDetector:FRAme:TEST:TIME`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._badchars = ErrordetectorFrameTestBadchars(device, f"{self._cmd_syntax}:BADCHARS")
        self._count = ErrordetectorFrameTestCount(device, f"{self._cmd_syntax}:COUNt")
        self._disparity = ErrordetectorFrameTestDisparity(device, f"{self._cmd_syntax}:DISParity")
        self._duration = ErrordetectorFrameTestDuration(device, f"{self._cmd_syntax}:DURATION")
        self._maxaligns = ErrordetectorFrameTestMaxaligns(device, f"{self._cmd_syntax}:MAXALIGNS")
        self._rate = ErrordetectorFrameTestRate(device, f"{self._cmd_syntax}:RATE")
        self._results = ErrordetectorFrameTestResults(device, f"{self._cmd_syntax}:RESults")
        self._seconds = ErrordetectorFrameTestSeconds(device, f"{self._cmd_syntax}:SECOnds")
        self._status = ErrordetectorFrameTestStatus(device, f"{self._cmd_syntax}:STATUS")
        self._time = ErrordetectorFrameTestTime(device, f"{self._cmd_syntax}:TIME")

    @property
    def badchars(self) -> ErrordetectorFrameTestBadchars:
        """Return the ``ERRORDetector:FRAme:TEST:BADCHARS`` command.

        Description:
            - This command queries the illegal character count for frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:BADCHARS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:BADCHARS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:BADCHARS?
            ```
        """
        return self._badchars

    @property
    def count(self) -> ErrordetectorFrameTestCount:
        """Return the ``ERRORDetector:FRAme:TEST:COUNt`` command.

        Description:
            - This command queries the test error count for frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:COUNt?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:COUNt?
            ```
        """
        return self._count

    @property
    def disparity(self) -> ErrordetectorFrameTestDisparity:
        """Return the ``ERRORDetector:FRAme:TEST:DISParity`` command.

        Description:
            - This command queries the disparity error count for frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:DISParity?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:DISParity?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:DISParity?
            ```
        """
        return self._disparity

    @property
    def duration(self) -> ErrordetectorFrameTestDuration:
        """Return the ``ERRORDetector:FRAme:TEST:DURATION`` command.

        Description:
            - This command queries the elapsed duration in number of frames.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:DURATION?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:DURATION?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:DURATION?
            ```
        """
        return self._duration

    @property
    def maxaligns(self) -> ErrordetectorFrameTestMaxaligns:
        """Return the ``ERRORDetector:FRAme:TEST:MAXALIGNS`` command.

        Description:
            - This command queries the result of the maximum consecutive aligns encountered for
              frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:MAXALIGNS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:MAXALIGNS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:MAXALIGNS?
            ```
        """
        return self._maxaligns

    @property
    def rate(self) -> ErrordetectorFrameTestRate:
        """Return the ``ERRORDetector:FRAme:TEST:RATE`` command.

        Description:
            - This command queries the calculated frame error rate.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:RATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:RATE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:RATE?
            ```
        """
        return self._rate

    @property
    def results(self) -> ErrordetectorFrameTestResults:
        """Return the ``ERRORDetector:FRAme:TEST:RESults`` command.

        Description:
            - This command queries all the results for frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:RESults?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:RESults?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:RESults?
            ```
        """
        return self._results

    @property
    def seconds(self) -> ErrordetectorFrameTestSeconds:
        """Return the ``ERRORDetector:FRAme:TEST:SECOnds`` command.

        Description:
            - This command queries the result of elapsed duration in seconds for frame error
              testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:SECOnds?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:TEST:SECOnds?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:SECOnds?
            ```
        """
        return self._seconds

    @property
    def status(self) -> ErrordetectorFrameTestStatus:
        """Return the ``ERRORDetector:FRAme:TEST:STATUS`` command.

        Description:
            - This command queries all of the status for frame error status.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:STATUS?``
              query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:STATUS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:STATUS?
            ```

        Sub-properties:
            - ``.lock``: The ``ERRORDetector:FRAme:TEST:STATUS:LOCK`` command.
            - ``.max_ap``: The ``ERRORDetector:FRAme:TEST:STATUS:MAX_AP`` command.
            - ``.signal``: The ``ERRORDetector:FRAme:TEST:STATUS:SIGNAL`` command.
            - ``.start``: The ``ERRORDetector:FRAme:TEST:STATUS:START`` command.
        """
        return self._status

    @property
    def time(self) -> ErrordetectorFrameTestTime:
        """Return the ``ERRORDetector:FRAme:TEST:TIME`` command.

        Description:
            - This command queries the elapsed time (in days, hours, minutes, and seconds) for frame
              error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST:TIME?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST:TIME?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST:TIME?
            ```

        Sub-properties:
            - ``.days``: The ``ERRORDetector:FRAme:TEST:TIME:DAYS`` command.
            - ``.hours``: The ``ERRORDetector:FRAme:TEST:TIME:HOURS`` command.
            - ``.minutes``: The ``ERRORDetector:FRAme:TEST:TIME:MINUTES`` command.
            - ``.seconds``: The ``ERRORDetector:FRAme:TEST:TIME:SECOnds`` command.
        """
        return self._time


class ErrordetectorFrameSof(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:FRAme:SOF`` command.

    Description:
        - This command sets or queries the Start of Frame for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:SOF?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:SOF?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:FRAme:SOF value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:SOF <Qstring>
        - ERRORDetector:FRAme:SOF?
        ```

    Info:
        - ``<Qstring>`` is a quoted string representing a 32-bit pattern.
    """


class ErrordetectorFrameInitialcrcvalue(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:FRAme:INITIALCRCVALue`` command.

    Description:
        - This command sets or queries the initial CRC value for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:INITIALCRCVALue?``
          query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:INITIALCRCVALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ERRORDetector:FRAme:INITIALCRCVALue value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:INITIALCRCVALue <NR1>
        - ERRORDetector:FRAme:INITIALCRCVALue?
        ```

    Info:
        - ``<NR1>`` is a value defined by the selected standard.
    """


class ErrordetectorFrameEof(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:FRAme:EOF`` command.

    Description:
        - This command sets or queries the End of Frame for frame error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:EOF?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:EOF?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:FRAme:EOF value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme:EOF <Qstring>
        - ERRORDetector:FRAme:EOF?
        ```

    Info:
        - ``<Qstring>`` is a quoted string representing a 32-bit pattern.
    """


class ErrordetectorFrame(SCPICmdRead):
    """The ``ERRORDetector:FRAme`` command.

    Description:
        - This command queries all frame error settings, status, and results.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FRAme?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:FRAme?
        ```

    Properties:
        - ``.eof``: The ``ERRORDetector:FRAme:EOF`` command.
        - ``.initialcrcvalue``: The ``ERRORDetector:FRAme:INITIALCRCVALue`` command.
        - ``.sof``: The ``ERRORDetector:FRAme:SOF`` command.
        - ``.test``: The ``ERRORDetector:FRAme:TEST`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._eof = ErrordetectorFrameEof(device, f"{self._cmd_syntax}:EOF")
        self._initialcrcvalue = ErrordetectorFrameInitialcrcvalue(
            device, f"{self._cmd_syntax}:INITIALCRCVALue"
        )
        self._sof = ErrordetectorFrameSof(device, f"{self._cmd_syntax}:SOF")
        self._test = ErrordetectorFrameTest(device, f"{self._cmd_syntax}:TEST")

    @property
    def eof(self) -> ErrordetectorFrameEof:
        """Return the ``ERRORDetector:FRAme:EOF`` command.

        Description:
            - This command sets or queries the End of Frame for frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:EOF?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:EOF?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:FRAme:EOF value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:EOF <Qstring>
            - ERRORDetector:FRAme:EOF?
            ```

        Info:
            - ``<Qstring>`` is a quoted string representing a 32-bit pattern.
        """
        return self._eof

    @property
    def initialcrcvalue(self) -> ErrordetectorFrameInitialcrcvalue:
        """Return the ``ERRORDetector:FRAme:INITIALCRCVALue`` command.

        Description:
            - This command sets or queries the initial CRC value for frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:INITIALCRCVALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:FRAme:INITIALCRCVALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:FRAme:INITIALCRCVALue value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:INITIALCRCVALue <NR1>
            - ERRORDetector:FRAme:INITIALCRCVALue?
            ```

        Info:
            - ``<NR1>`` is a value defined by the selected standard.
        """
        return self._initialcrcvalue

    @property
    def sof(self) -> ErrordetectorFrameSof:
        """Return the ``ERRORDetector:FRAme:SOF`` command.

        Description:
            - This command sets or queries the Start of Frame for frame error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:SOF?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:SOF?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:FRAme:SOF value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:SOF <Qstring>
            - ERRORDetector:FRAme:SOF?
            ```

        Info:
            - ``<Qstring>`` is a quoted string representing a 32-bit pattern.
        """
        return self._sof

    @property
    def test(self) -> ErrordetectorFrameTest:
        """Return the ``ERRORDetector:FRAme:TEST`` command.

        Description:
            - This command and query initiates and terminates frame error testing for the arguments
              START and STOP. Zeroes the frame error results for the argument CLEAR. Re-synchronizes
              the recovered clock for the argument SYNC.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme:TEST?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme:TEST?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:FRAme:TEST value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme:TEST <START|STOP|CLEAR|SYNC>
            - ERRORDetector:FRAme:TEST?
            ```

        Info:
            - ``START`` initiates the frame error test counting of errors and duration.
            - ``STOP`` terminates the frame error test counting of frame errors and duration.
            - ``CLEAR`` zeroes the frame error test count, duration, and rate.
            - ``SYNC`` re-synchronizes the recovered clock.

        Sub-properties:
            - ``.badchars``: The ``ERRORDetector:FRAme:TEST:BADCHARS`` command.
            - ``.count``: The ``ERRORDetector:FRAme:TEST:COUNt`` command.
            - ``.disparity``: The ``ERRORDetector:FRAme:TEST:DISParity`` command.
            - ``.duration``: The ``ERRORDetector:FRAme:TEST:DURATION`` command.
            - ``.maxaligns``: The ``ERRORDetector:FRAme:TEST:MAXALIGNS`` command.
            - ``.rate``: The ``ERRORDetector:FRAme:TEST:RATE`` command.
            - ``.results``: The ``ERRORDetector:FRAme:TEST:RESults`` command.
            - ``.seconds``: The ``ERRORDetector:FRAme:TEST:SECOnds`` command.
            - ``.status``: The ``ERRORDetector:FRAme:TEST:STATUS`` command.
            - ``.time``: The ``ERRORDetector:FRAme:TEST:TIME`` command.
        """
        return self._test


class ErrordetectorFontsize(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:FONTSIze`` command.

    Description:
        - Sets or queries error detector font size selection. Currently, the font size only applied
          the error detector UI control window.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FONTSIze?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FONTSIze?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:FONTSIze value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:FONTSIze {DEFAULT|LARGE|XLARGE}
        - ERRORDetector:FONTSIze?
        ```

    Info:
        - ``DEFAULT`` sets the font size to the default size.
        - ``LARGE`` sets the font size to large.
        - ``XLARGE`` sets the font size to extra large.
    """


class ErrordetectorFileSave(SCPICmdWrite):
    """The ``ERRORDetector:FILE:SAVe`` command.

    Description:
        - This command initiates a file save of error detector parameters to a text file. Argument
          is the file name. The setup files are supplied with the instrument. You can also save your
          own setup files. For example, the setup for the USB ``CP0_SKP`` signal test pattern is
          supplied in 'C:UsersPublicTektronixTekScopeErrorDetector
          ``UsbCP0_SKPsymbolErrorSetup``.txt'.

    Usage:
        - Using the ``.write(value)`` method will send the ``ERRORDetector:FILE:SAVe value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:FILE:SAVe <fileName>
        ```

    Info:
        - ``<fileName>`` is the file name and file location. The default location is
          'C:UsersPublicTektronixTekScopeErrorDetector' and the setup file is in TXT format.
    """


class ErrordetectorFileRecall(SCPICmdWrite):
    """The ``ERRORDetector:FILE:RECAll`` command.

    Description:
        - This command initiates a file recall of error detector parameters from a text file.
          Argument is the file name. The setup files are supplied with the instrument. You can also
          create your own setup files. The setup for the USB ``CP0_SKP`` signal test pattern is
          supplied in 'C:UsersPublicTektronixTekScopeErrorDetector
          ``UsbCP0_SKPsymbolErrorSetup``.txt'.

    Usage:
        - Using the ``.write(value)`` method will send the ``ERRORDetector:FILE:RECAll value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:FILE:RECAll <fileName>
        ```

    Info:
        - ``<fileName>`` is the file name and file location. The default location is
          'C:UsersPublicTektronixTekScopeErrorDetector' and the setup file is in TXT format.
    """


class ErrordetectorFile(SCPICmdRead):
    """The ``ERRORDetector:FILE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:FILE?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:FILE?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.recall``: The ``ERRORDetector:FILE:RECAll`` command.
        - ``.save``: The ``ERRORDetector:FILE:SAVe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._recall = ErrordetectorFileRecall(device, f"{self._cmd_syntax}:RECAll")
        self._save = ErrordetectorFileSave(device, f"{self._cmd_syntax}:SAVe")

    @property
    def recall(self) -> ErrordetectorFileRecall:
        """Return the ``ERRORDetector:FILE:RECAll`` command.

        Description:
            - This command initiates a file recall of error detector parameters from a text file.
              Argument is the file name. The setup files are supplied with the instrument. You can
              also create your own setup files. The setup for the USB ``CP0_SKP`` signal test
              pattern is supplied in 'C:UsersPublicTektronixTekScopeErrorDetector
              ``UsbCP0_SKPsymbolErrorSetup``.txt'.

        Usage:
            - Using the ``.write(value)`` method will send the ``ERRORDetector:FILE:RECAll value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:FILE:RECAll <fileName>
            ```

        Info:
            - ``<fileName>`` is the file name and file location. The default location is
              'C:UsersPublicTektronixTekScopeErrorDetector' and the setup file is in TXT format.
        """
        return self._recall

    @property
    def save(self) -> ErrordetectorFileSave:
        """Return the ``ERRORDetector:FILE:SAVe`` command.

        Description:
            - This command initiates a file save of error detector parameters to a text file.
              Argument is the file name. The setup files are supplied with the instrument. You can
              also save your own setup files. For example, the setup for the USB ``CP0_SKP`` signal
              test pattern is supplied in 'C:UsersPublicTektronixTekScopeErrorDetector
              ``UsbCP0_SKPsymbolErrorSetup``.txt'.

        Usage:
            - Using the ``.write(value)`` method will send the ``ERRORDetector:FILE:SAVe value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:FILE:SAVe <fileName>
            ```

        Info:
            - ``<fileName>`` is the file name and file location. The default location is
              'C:UsersPublicTektronixTekScopeErrorDetector' and the setup file is in TXT format.
        """
        return self._save


class ErrordetectorErrorlimit(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:ERRORLIMIT`` command.

    Description:
        - This command sets or queries the error limit value to use when STOPWHEN is ERROR.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ERRORLIMIT?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:ERRORLIMIT?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:ERRORLIMIT value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:ERRORLIMIT <NR1>
        - ERRORDetector:ERRORLIMIT?
        ```

    Info:
        - ``<NR1>`` is the maximum number of errors.
    """


class ErrordetectorDurationTimeSeconds(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:DURATION:TIME:SECOnds`` command.

    Description:
        - This command sets or queries the test duration time seconds component for error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:TIME:SECOnds?``
          query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION:TIME:SECOnds?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ERRORDetector:DURATION:TIME:SECOnds value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:DURATION:TIME:SECOnds <NR1>
        - ERRORDetector:DURATION:TIME:SECOnds?
        ```

    Info:
        - ``<NR1>`` is a number for the test duration time seconds component.
    """


class ErrordetectorDurationTimeMinutes(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:DURATION:TIME:MINUTES`` command.

    Description:
        - This command sets or queries the test duration time minutes component for error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:TIME:MINUTES?``
          query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION:TIME:MINUTES?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ERRORDetector:DURATION:TIME:MINUTES value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:DURATION:TIME:MINUTES <NR1>
        - ERRORDetector:DURATION:TIME:MINUTES?
        ```

    Info:
        - ``<NR1>`` is a number for the test duration time minutes component.
    """


class ErrordetectorDurationTimeHours(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:DURATION:TIME:HOURS`` command.

    Description:
        - This command sets or queries the test duration time hours component.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:TIME:HOURS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION:TIME:HOURS?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ERRORDetector:DURATION:TIME:HOURS value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:DURATION:TIME:HOURS <NR1>
        - ERRORDetector:DURATION:TIME:HOURS?
        ```

    Info:
        - ``<NR1>`` is a number for the test duration time hours component.
    """


class ErrordetectorDurationTimeDays(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:DURATION:TIME:DAYS`` command.

    Description:
        - This command sets or queries the test duration time days component.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:TIME:DAYS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION:TIME:DAYS?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ERRORDetector:DURATION:TIME:DAYS value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:DURATION:TIME:DAYS <NR1>
        - ERRORDetector:DURATION:TIME:DAYS?
        ```

    Info:
        - ``<NR1>`` is a number for the test duration time days component.
    """


class ErrordetectorDurationTime(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:DURATION:TIME`` command.

    Description:
        - This command sets or queries the test duration time in days, hours, minutes, and seconds.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:TIME?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION:TIME?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:DURATION:TIME value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:DURATION:TIME <NR1>
        - ERRORDetector:DURATION:TIME?
        ```

    Info:
        - ``<NR1>`` is the test duration time in days, hours, minutes, and seconds. It is in the
          format <DD, HH, MM, SS>.

    Properties:
        - ``.days``: The ``ERRORDetector:DURATION:TIME:DAYS`` command.
        - ``.hours``: The ``ERRORDetector:DURATION:TIME:HOURS`` command.
        - ``.minutes``: The ``ERRORDetector:DURATION:TIME:MINUTES`` command.
        - ``.seconds``: The ``ERRORDetector:DURATION:TIME:SECOnds`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._days = ErrordetectorDurationTimeDays(device, f"{self._cmd_syntax}:DAYS")
        self._hours = ErrordetectorDurationTimeHours(device, f"{self._cmd_syntax}:HOURS")
        self._minutes = ErrordetectorDurationTimeMinutes(device, f"{self._cmd_syntax}:MINUTES")
        self._seconds = ErrordetectorDurationTimeSeconds(device, f"{self._cmd_syntax}:SECOnds")

    @property
    def days(self) -> ErrordetectorDurationTimeDays:
        """Return the ``ERRORDetector:DURATION:TIME:DAYS`` command.

        Description:
            - This command sets or queries the test duration time days component.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:TIME:DAYS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:DURATION:TIME:DAYS?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:DURATION:TIME:DAYS value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:DURATION:TIME:DAYS <NR1>
            - ERRORDetector:DURATION:TIME:DAYS?
            ```

        Info:
            - ``<NR1>`` is a number for the test duration time days component.
        """
        return self._days

    @property
    def hours(self) -> ErrordetectorDurationTimeHours:
        """Return the ``ERRORDetector:DURATION:TIME:HOURS`` command.

        Description:
            - This command sets or queries the test duration time hours component.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:TIME:HOURS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:DURATION:TIME:HOURS?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:DURATION:TIME:HOURS value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:DURATION:TIME:HOURS <NR1>
            - ERRORDetector:DURATION:TIME:HOURS?
            ```

        Info:
            - ``<NR1>`` is a number for the test duration time hours component.
        """
        return self._hours

    @property
    def minutes(self) -> ErrordetectorDurationTimeMinutes:
        """Return the ``ERRORDetector:DURATION:TIME:MINUTES`` command.

        Description:
            - This command sets or queries the test duration time minutes component for error
              testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:TIME:MINUTES?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:DURATION:TIME:MINUTES?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:DURATION:TIME:MINUTES value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:DURATION:TIME:MINUTES <NR1>
            - ERRORDetector:DURATION:TIME:MINUTES?
            ```

        Info:
            - ``<NR1>`` is a number for the test duration time minutes component.
        """
        return self._minutes

    @property
    def seconds(self) -> ErrordetectorDurationTimeSeconds:
        """Return the ``ERRORDetector:DURATION:TIME:SECOnds`` command.

        Description:
            - This command sets or queries the test duration time seconds component for error
              testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:TIME:SECOnds?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:DURATION:TIME:SECOnds?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:DURATION:TIME:SECOnds value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:DURATION:TIME:SECOnds <NR1>
            - ERRORDetector:DURATION:TIME:SECOnds?
            ```

        Info:
            - ``<NR1>`` is a number for the test duration time seconds component.
        """
        return self._seconds


class ErrordetectorDurationSeconds(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:DURATION:SECOnds`` command.

    Description:
        - This command sets or queries the test duration in seconds.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:SECOnds?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION:SECOnds?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:DURATION:SECOnds value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:DURATION:SECOnds <NR1>
        - ERRORDetector:DURATION:SECOnds?
        ```

    Info:
        - ``<NR1>`` is the test duration in seconds.
    """


class ErrordetectorDurationCount(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:DURATION:COUNt`` command.

    Description:
        - This command sets or queries the test duration count as the number of bits, frames,
          symbols, or characters to be tested for error testing. (Frame, symbol, and character
          testing not available on the DPO70000SX instruments.)

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION:COUNt?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:DURATION:COUNt value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:DURATION:COUNt <NR1>
        - ERRORDetector:DURATION:COUNt?
        ```

    Info:
        - ``<NR1>`` indicates the number of bits, frame, symbols, or characters to be tested for the
          test duration count. (Frame, symbol, and character testing not available on the DPO70000SX
          instruments.).
    """


class ErrordetectorDuration(SCPICmdRead):
    """The ``ERRORDetector:DURATION`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:DURATION?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.count``: The ``ERRORDetector:DURATION:COUNt`` command.
        - ``.seconds``: The ``ERRORDetector:DURATION:SECOnds`` command.
        - ``.time``: The ``ERRORDetector:DURATION:TIME`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = ErrordetectorDurationCount(device, f"{self._cmd_syntax}:COUNt")
        self._seconds = ErrordetectorDurationSeconds(device, f"{self._cmd_syntax}:SECOnds")
        self._time = ErrordetectorDurationTime(device, f"{self._cmd_syntax}:TIME")

    @property
    def count(self) -> ErrordetectorDurationCount:
        """Return the ``ERRORDetector:DURATION:COUNt`` command.

        Description:
            - This command sets or queries the test duration count as the number of bits, frames,
              symbols, or characters to be tested for error testing. (Frame, symbol, and character
              testing not available on the DPO70000SX instruments.)

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION:COUNt?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:DURATION:COUNt value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:DURATION:COUNt <NR1>
            - ERRORDetector:DURATION:COUNt?
            ```

        Info:
            - ``<NR1>`` indicates the number of bits, frame, symbols, or characters to be tested for
              the test duration count. (Frame, symbol, and character testing not available on the
              DPO70000SX instruments.).
        """
        return self._count

    @property
    def seconds(self) -> ErrordetectorDurationSeconds:
        """Return the ``ERRORDetector:DURATION:SECOnds`` command.

        Description:
            - This command sets or queries the test duration in seconds.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:SECOnds?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION:SECOnds?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:DURATION:SECOnds value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:DURATION:SECOnds <NR1>
            - ERRORDetector:DURATION:SECOnds?
            ```

        Info:
            - ``<NR1>`` is the test duration in seconds.
        """
        return self._seconds

    @property
    def time(self) -> ErrordetectorDurationTime:
        """Return the ``ERRORDetector:DURATION:TIME`` command.

        Description:
            - This command sets or queries the test duration time in days, hours, minutes, and
              seconds.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:DURATION:TIME?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION:TIME?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:DURATION:TIME value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:DURATION:TIME <NR1>
            - ERRORDetector:DURATION:TIME?
            ```

        Info:
            - ``<NR1>`` is the test duration time in days, hours, minutes, and seconds. It is in the
              format <DD, HH, MM, SS>.

        Sub-properties:
            - ``.days``: The ``ERRORDetector:DURATION:TIME:DAYS`` command.
            - ``.hours``: The ``ERRORDetector:DURATION:TIME:HOURS`` command.
            - ``.minutes``: The ``ERRORDetector:DURATION:TIME:MINUTES`` command.
            - ``.seconds``: The ``ERRORDetector:DURATION:TIME:SECOnds`` command.
        """
        return self._time


class ErrordetectorChannel(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:CHANnel`` command.

    Description:
        - Sets or queries error detector channel selection.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:CHANnel?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:CHANnel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:CHANnel value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:CHANnel {CH1|CH2|CH3|CH4}
        - ERRORDetector:CHANnel?
        ```

    Info:
        - ``CHx`` is the error detector channel selection.
    """


class ErrordetectorBitrateValue(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:BITRate:VALue`` command.

    Description:
        - This command sets or queries error detector custom bitrate value for error detection. To
          set the custom value, you must also set ``ERRORDetector:BITTRATE`` to CUSTOM. The bitrate
          range is nominally 1.25 Gb/s to 6.25 Gb/s. Special coding also allows the custom bitrate
          to range from 200 Mb/s to 350 Mb/s for PRBS7 and PRBS9 only.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BITRate:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BITRate:VALue?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:BITRate:VALue value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:BITRate:VALue <NR3>
        - ERRORDetector:BITRate:VALue?
        ```

    Info:
        - ``<NR3>`` is the custom bit rate value.
    """


class ErrordetectorBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:BITRate`` command.

    Description:
        - This command sets or queries error detector bitrate enumeration for error detection. There
          are two bitrate enumerations for each standard: 1) The standard bitrate, for example
          RATE6000 (meaning 6.0Gb/s, for SATA Gen3); and 2) Custom. When Custom is selected the
          ``ERRORDetector:BITRATE:VALUE`` must also be set to the specific desired bitrate. For
          example, 6.1 Gb/s.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:BITRate value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:BITRate {RATEcustom:CUSTOM|RATE312000000:RATE312|RATE1250000000:RATE1250|RATE1500000000:RATE1500|RATE2125000000:RATE2125|RATE2500000000:RATE2500|RATE3000000000:RATE3000|RATE3125000000:RATE3125|RATE4250000000:RATE4250|RATE5000000000:RATE5000|RATE6000000000:RATE6000|RATE6250000000:RATE6250}DPO70000SX{RATE3200|RATE3600|RATE4000|RATE4400|RATE4800|RATE5200|RATE5600|RATE6000|RATE6400|CUSTOM}
        - ERRORDetector:BITRate?
        ```

    Info:
        - ``RATE3200..to..RATE6400`` sets the error detector bit rate to the specified value.
          RATE3200 indicates a bitrate of 3.2 Gb/s, etc.
        - ``:ERRORDETECTOR:BITRATE:VALUE`` command.

    Properties:
        - ``.value``: The ``ERRORDetector:BITRate:VALue`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = ErrordetectorBitrateValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> ErrordetectorBitrateValue:
        """Return the ``ERRORDetector:BITRate:VALue`` command.

        Description:
            - This command sets or queries error detector custom bitrate value for error detection.
              To set the custom value, you must also set ``ERRORDetector:BITTRATE`` to CUSTOM. The
              bitrate range is nominally 1.25 Gb/s to 6.25 Gb/s. Special coding also allows the
              custom bitrate to range from 200 Mb/s to 350 Mb/s for PRBS7 and PRBS9 only.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BITRate:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BITRate:VALue?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:BITRate:VALue value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:BITRate:VALue <NR3>
            - ERRORDetector:BITRate:VALue?
            ```

        Info:
            - ``<NR3>`` is the custom bit rate value.
        """
        return self._value


class ErrordetectorBitTestTimeSeconds(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:TIME:SECOnds`` command.

    Description:
        - This command queries the elapsed time seconds component for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:TIME:SECOnds?``
          query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:TIME:SECOnds?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:TIME:SECOnds?
        ```
    """


class ErrordetectorBitTestTimeMinutes(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:TIME:MINUTES`` command.

    Description:
        - This command queries the elapsed time minutes component for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:TIME:MINUTES?``
          query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:TIME:MINUTES?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:TIME:MINUTES?
        ```
    """


class ErrordetectorBitTestTimeHours(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:TIME:HOURS`` command.

    Description:
        - This command queries the elapsed time hours component for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:TIME:HOURS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:TIME:HOURS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:TIME:HOURS?
        ```
    """


class ErrordetectorBitTestTimeDays(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:TIME:DAYS`` command.

    Description:
        - This command queries the elapsed time days component for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:TIME:DAYS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:TIME:DAYS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:TIME:DAYS?
        ```
    """


class ErrordetectorBitTestTime(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:TIME`` command.

    Description:
        - This command queries the elapsed time (in days, hours, minutes, and seconds) for bit error
          testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:TIME?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:TIME?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:TIME?
        ```

    Properties:
        - ``.days``: The ``ERRORDetector:BIT:TEST:TIME:DAYS`` command.
        - ``.hours``: The ``ERRORDetector:BIT:TEST:TIME:HOURS`` command.
        - ``.minutes``: The ``ERRORDetector:BIT:TEST:TIME:MINUTES`` command.
        - ``.seconds``: The ``ERRORDetector:BIT:TEST:TIME:SECOnds`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._days = ErrordetectorBitTestTimeDays(device, f"{self._cmd_syntax}:DAYS")
        self._hours = ErrordetectorBitTestTimeHours(device, f"{self._cmd_syntax}:HOURS")
        self._minutes = ErrordetectorBitTestTimeMinutes(device, f"{self._cmd_syntax}:MINUTES")
        self._seconds = ErrordetectorBitTestTimeSeconds(device, f"{self._cmd_syntax}:SECOnds")

    @property
    def days(self) -> ErrordetectorBitTestTimeDays:
        """Return the ``ERRORDetector:BIT:TEST:TIME:DAYS`` command.

        Description:
            - This command queries the elapsed time days component for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:TIME:DAYS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:TEST:TIME:DAYS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:TIME:DAYS?
            ```
        """
        return self._days

    @property
    def hours(self) -> ErrordetectorBitTestTimeHours:
        """Return the ``ERRORDetector:BIT:TEST:TIME:HOURS`` command.

        Description:
            - This command queries the elapsed time hours component for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:TIME:HOURS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:TEST:TIME:HOURS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:TIME:HOURS?
            ```
        """
        return self._hours

    @property
    def minutes(self) -> ErrordetectorBitTestTimeMinutes:
        """Return the ``ERRORDetector:BIT:TEST:TIME:MINUTES`` command.

        Description:
            - This command queries the elapsed time minutes component for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:TIME:MINUTES?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:TEST:TIME:MINUTES?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:TIME:MINUTES?
            ```
        """
        return self._minutes

    @property
    def seconds(self) -> ErrordetectorBitTestTimeSeconds:
        """Return the ``ERRORDetector:BIT:TEST:TIME:SECOnds`` command.

        Description:
            - This command queries the elapsed time seconds component for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:TIME:SECOnds?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:TEST:TIME:SECOnds?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:TIME:SECOnds?
            ```
        """
        return self._seconds


class ErrordetectorBitTestStatusSync(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:STATUS:SYNC`` command.

    Description:
        - This command queries the SYNC status for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS:SYNC?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:STATUS:SYNC?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:STATUS:SYNC?
        ```
    """


class ErrordetectorBitTestStatusStart(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:STATUS:START`` command.

    Description:
        - This command queries the START status for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS:START?``
          query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:STATUS:START?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:STATUS:START?
        ```
    """


class ErrordetectorBitTestStatusSignal(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:STATUS:SIGNAL`` command.

    Description:
        - This command queries the SIGNAL status for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS:SIGNAL?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:BIT:TEST:STATUS:SIGNAL?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:STATUS:SIGNAL?
        ```
    """


class ErrordetectorBitTestStatusMaxAp(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:STATUS:MAX_AP`` command.

    Description:
        - This command queries the ``MAX_AP`` status for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS:MAX_AP?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:BIT:TEST:STATUS:MAX_AP?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:STATUS:MAX_AP?
        ```
    """


class ErrordetectorBitTestStatusLock(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:STATUS:LOCK`` command.

    Description:
        - This command queries the LOCK status for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS:LOCK?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:STATUS:LOCK?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:STATUS:LOCK?
        ```
    """


class ErrordetectorBitTestStatus(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:STATUS`` command.

    Description:
        - This command queries all of the bit error test status bits.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:STATUS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:STATUS?
        ```

    Properties:
        - ``.lock``: The ``ERRORDetector:BIT:TEST:STATUS:LOCK`` command.
        - ``.max_ap``: The ``ERRORDetector:BIT:TEST:STATUS:MAX_AP`` command.
        - ``.signal``: The ``ERRORDetector:BIT:TEST:STATUS:SIGNAL`` command.
        - ``.start``: The ``ERRORDetector:BIT:TEST:STATUS:START`` command.
        - ``.sync``: The ``ERRORDetector:BIT:TEST:STATUS:SYNC`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lock = ErrordetectorBitTestStatusLock(device, f"{self._cmd_syntax}:LOCK")
        self._max_ap = ErrordetectorBitTestStatusMaxAp(device, f"{self._cmd_syntax}:MAX_AP")
        self._signal = ErrordetectorBitTestStatusSignal(device, f"{self._cmd_syntax}:SIGNAL")
        self._start = ErrordetectorBitTestStatusStart(device, f"{self._cmd_syntax}:START")
        self._sync = ErrordetectorBitTestStatusSync(device, f"{self._cmd_syntax}:SYNC")

    @property
    def lock(self) -> ErrordetectorBitTestStatusLock:
        """Return the ``ERRORDetector:BIT:TEST:STATUS:LOCK`` command.

        Description:
            - This command queries the LOCK status for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS:LOCK?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:TEST:STATUS:LOCK?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:STATUS:LOCK?
            ```
        """
        return self._lock

    @property
    def max_ap(self) -> ErrordetectorBitTestStatusMaxAp:
        """Return the ``ERRORDetector:BIT:TEST:STATUS:MAX_AP`` command.

        Description:
            - This command queries the ``MAX_AP`` status for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS:MAX_AP?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:TEST:STATUS:MAX_AP?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:STATUS:MAX_AP?
            ```
        """
        return self._max_ap

    @property
    def signal(self) -> ErrordetectorBitTestStatusSignal:
        """Return the ``ERRORDetector:BIT:TEST:STATUS:SIGNAL`` command.

        Description:
            - This command queries the SIGNAL status for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS:SIGNAL?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:TEST:STATUS:SIGNAL?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:STATUS:SIGNAL?
            ```
        """
        return self._signal

    @property
    def start(self) -> ErrordetectorBitTestStatusStart:
        """Return the ``ERRORDetector:BIT:TEST:STATUS:START`` command.

        Description:
            - This command queries the START status for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS:START?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:TEST:STATUS:START?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:STATUS:START?
            ```
        """
        return self._start

    @property
    def sync(self) -> ErrordetectorBitTestStatusSync:
        """Return the ``ERRORDetector:BIT:TEST:STATUS:SYNC`` command.

        Description:
            - This command queries the SYNC status for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS:SYNC?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:TEST:STATUS:SYNC?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:STATUS:SYNC?
            ```
        """
        return self._sync


class ErrordetectorBitTestSeconds(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:SECOnds`` command.

    Description:
        - This command queries the elapsed time in seconds for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:SECOnds?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:SECOnds?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:SECOnds?
        ```
    """


class ErrordetectorBitTestResults(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:RESults`` command.

    Description:
        - This command queries all of the results for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:RESults?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:RESults?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:RESults?
        ```
    """


class ErrordetectorBitTestRate(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:RATE`` command.

    Description:
        - This command queries the calculated bit error rate for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:RATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:RATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:RATE?
        ```
    """


class ErrordetectorBitTestMaxaligns(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:MAXALIGNS`` command.

    Description:
        - This command queries the maximum consecutive SATA align primitives or USB skip order sets
          for bit error testing. The maximum number of align primitives is a design parameter of the
          bus standard.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:MAXALIGNS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:MAXALIGNS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:MAXALIGNS?
        ```
    """


class ErrordetectorBitTestDuration(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:DURATION`` command.

    Description:
        - This command queries the elapsed duration (in units of bits) tested for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:DURATION?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:DURATION?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:DURATION?
        ```
    """


class ErrordetectorBitTestCount(SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST:COUNt`` command.

    Description:
        - This command queries the bit error count for bit error testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:COUNt?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST:COUNt?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class ErrordetectorBitTest(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:BIT:TEST`` command.

    Description:
        - This command initiates and terminates bit error testing for the arguments START and STOP.
          It zeroes bit error test results for the argument CLEAR. It also copies the test pattern
          from the signal to memory for the argument LEARN. It re-synchronizes the recovered clock
          for argument SYNC.

    Usage:
        - Using the ``.write(value)`` method will send the ``ERRORDetector:BIT:TEST value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:TEST <LEARN | START | STOP | CLEAR | SYNC>DPO70000SX<START | STOP | CLEAR>
        ```

    Info:
        - ``LEARN`` copies the test pattern from the signal to the hardware template memory.
        - ``START`` initiates bit error counting of bit errors and duration.
        - ``STOP`` terminates bit error counting of bit errors and duration.
        - ``CLEAR`` zeroes the bit error count, duration, and bit error rate.
        - ``SYNC`` resynchronizes the recovered clock.

    Properties:
        - ``.count``: The ``ERRORDetector:BIT:TEST:COUNt`` command.
        - ``.duration``: The ``ERRORDetector:BIT:TEST:DURATION`` command.
        - ``.maxaligns``: The ``ERRORDetector:BIT:TEST:MAXALIGNS`` command.
        - ``.rate``: The ``ERRORDetector:BIT:TEST:RATE`` command.
        - ``.results``: The ``ERRORDetector:BIT:TEST:RESults`` command.
        - ``.seconds``: The ``ERRORDetector:BIT:TEST:SECOnds`` command.
        - ``.status``: The ``ERRORDetector:BIT:TEST:STATUS`` command.
        - ``.time``: The ``ERRORDetector:BIT:TEST:TIME`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = ErrordetectorBitTestCount(device, f"{self._cmd_syntax}:COUNt")
        self._duration = ErrordetectorBitTestDuration(device, f"{self._cmd_syntax}:DURATION")
        self._maxaligns = ErrordetectorBitTestMaxaligns(device, f"{self._cmd_syntax}:MAXALIGNS")
        self._rate = ErrordetectorBitTestRate(device, f"{self._cmd_syntax}:RATE")
        self._results = ErrordetectorBitTestResults(device, f"{self._cmd_syntax}:RESults")
        self._seconds = ErrordetectorBitTestSeconds(device, f"{self._cmd_syntax}:SECOnds")
        self._status = ErrordetectorBitTestStatus(device, f"{self._cmd_syntax}:STATUS")
        self._time = ErrordetectorBitTestTime(device, f"{self._cmd_syntax}:TIME")

    @property
    def count(self) -> ErrordetectorBitTestCount:
        """Return the ``ERRORDetector:BIT:TEST:COUNt`` command.

        Description:
            - This command queries the bit error count for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:COUNt?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:COUNt?
            ```
        """
        return self._count

    @property
    def duration(self) -> ErrordetectorBitTestDuration:
        """Return the ``ERRORDetector:BIT:TEST:DURATION`` command.

        Description:
            - This command queries the elapsed duration (in units of bits) tested for bit error
              testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:DURATION?``
              query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:DURATION?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:DURATION?
            ```
        """
        return self._duration

    @property
    def maxaligns(self) -> ErrordetectorBitTestMaxaligns:
        """Return the ``ERRORDetector:BIT:TEST:MAXALIGNS`` command.

        Description:
            - This command queries the maximum consecutive SATA align primitives or USB skip order
              sets for bit error testing. The maximum number of align primitives is a design
              parameter of the bus standard.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:MAXALIGNS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:TEST:MAXALIGNS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:MAXALIGNS?
            ```
        """
        return self._maxaligns

    @property
    def rate(self) -> ErrordetectorBitTestRate:
        """Return the ``ERRORDetector:BIT:TEST:RATE`` command.

        Description:
            - This command queries the calculated bit error rate for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:RATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:RATE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:RATE?
            ```
        """
        return self._rate

    @property
    def results(self) -> ErrordetectorBitTestResults:
        """Return the ``ERRORDetector:BIT:TEST:RESults`` command.

        Description:
            - This command queries all of the results for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:RESults?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:RESults?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:RESults?
            ```
        """
        return self._results

    @property
    def seconds(self) -> ErrordetectorBitTestSeconds:
        """Return the ``ERRORDetector:BIT:TEST:SECOnds`` command.

        Description:
            - This command queries the elapsed time in seconds for bit error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:SECOnds?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:SECOnds?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:SECOnds?
            ```
        """
        return self._seconds

    @property
    def status(self) -> ErrordetectorBitTestStatus:
        """Return the ``ERRORDetector:BIT:TEST:STATUS`` command.

        Description:
            - This command queries all of the bit error test status bits.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:STATUS?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:STATUS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:STATUS?
            ```

        Sub-properties:
            - ``.lock``: The ``ERRORDetector:BIT:TEST:STATUS:LOCK`` command.
            - ``.max_ap``: The ``ERRORDetector:BIT:TEST:STATUS:MAX_AP`` command.
            - ``.signal``: The ``ERRORDetector:BIT:TEST:STATUS:SIGNAL`` command.
            - ``.start``: The ``ERRORDetector:BIT:TEST:STATUS:START`` command.
            - ``.sync``: The ``ERRORDetector:BIT:TEST:STATUS:SYNC`` command.
        """
        return self._status

    @property
    def time(self) -> ErrordetectorBitTestTime:
        """Return the ``ERRORDetector:BIT:TEST:TIME`` command.

        Description:
            - This command queries the elapsed time (in days, hours, minutes, and seconds) for bit
              error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:TEST:TIME?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:TEST:TIME?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST:TIME?
            ```

        Sub-properties:
            - ``.days``: The ``ERRORDetector:BIT:TEST:TIME:DAYS`` command.
            - ``.hours``: The ``ERRORDetector:BIT:TEST:TIME:HOURS`` command.
            - ``.minutes``: The ``ERRORDetector:BIT:TEST:TIME:MINUTES`` command.
            - ``.seconds``: The ``ERRORDetector:BIT:TEST:TIME:SECOnds`` command.
        """
        return self._time


class ErrordetectorBitSyncpatternPlusItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``ERRORDetector:BIT:SYNCPATtern:PLUS<x>`` command.

    Description:
        - This command queries the four RD+ bit string sync pattern elements.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:SYNCPATtern:PLUS<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:BIT:SYNCPATtern:PLUS<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:SYNCPATtern:PLUS<x>?
        ```
    """


class ErrordetectorBitSyncpatternMinusItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``ERRORDetector:BIT:SYNCPATtern:MINus<x>`` command.

    Description:
        - This command queries the four RD- bit string sync pattern elements.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:SYNCPATtern:MINus<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:BIT:SYNCPATtern:MINus<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:SYNCPATtern:MINus<x>?
        ```
    """


class ErrordetectorBitSyncpatternDisparityItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``ERRORDetector:BIT:SYNCPATtern:DISParity<x>`` command.

    Description:
        - Sets or queries the four sync pattern Disparity elements, when the ``SYNCpat:ADVanced`` is
          ON. When Advanced is off, the DISParity alternates based on the DISParity of the first
          element.

    Usage:
        - Using the ``.query()`` method will send the
          ``ERRORDetector:BIT:SYNCPATtern:DISParity<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:BIT:SYNCPATtern:DISParity<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ERRORDetector:BIT:SYNCPATtern:DISParity<x> value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:SYNCPATtern:DISParity<x> {RDPLUS|RDMINUS}
        - ERRORDetector:BIT:SYNCPATtern:DISParity<x>?
        ```

    Info:
        - ``RDPLUS`` sets the sync pattern disparity element to RDPLUS.
        - ``RDMINUS`` sets the sync pattern disparity element to RDMINUS.
    """


class ErrordetectorBitSyncpatternBitstring(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:BIT:SYNCPATtern:BITString`` command.

    Description:
        - This command queries the 10-, 20-, 30-, or 40-bit sync pattern in bit string form.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:SYNCPATtern:BITString?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:BIT:SYNCPATtern:BITString?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ERRORDetector:BIT:SYNCPATtern:BITString value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:SYNCPATtern:BITString <QString>
        - ERRORDetector:BIT:SYNCPATtern:BITString?
        ```

    Info:
        - ``<QString>`` is the bit string.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ErrordetectorBitSyncpattern(SCPICmdRead):
    """The ``ERRORDetector:BIT:SYNCPATtern`` command.

    Description:
        - This command queries all of the sync pattern forms and associated settings for non-USB bit
          error testing. The SYNCPATtern consists of one to four symbolic 10-bit 8B10B characters
          and their matching RD+ and RD- bit string equivalents. It is required for all non-USB bit
          error testing. This sequence of 8B10B characters must actually occur and be unique in the
          signal test pattern sent to the oscilloscope for error detection to work correctly. The
          SyncPattern has a symbolic form ('K28.5'), an RD+ and RD- bit string form ('0011111010'),
          and an as-used bit string form. The actual form used depends on the
          ``SyncPattern:Disparity`` and ``SyncPattern:Advanced`` settings. When Advanced is Off, the
          disparity setting determines the disparity of the first (leftmost) syncpattern element,
          and the others alternate disparity. When Advanced is On, the Disparity is set for each
          SyncPattern element.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:SYNCPATtern?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:SYNCPATtern?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:SYNCPATtern?
        ```

    Properties:
        - ``.bitstring``: The ``ERRORDetector:BIT:SYNCPATtern:BITString`` command.
        - ``.disparity``: The ``ERRORDetector:BIT:SYNCPATtern:DISParity<x>`` command.
        - ``.minus``: The ``ERRORDetector:BIT:SYNCPATtern:MINus<x>`` command.
        - ``.plus``: The ``ERRORDetector:BIT:SYNCPATtern:PLUS<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitstring = ErrordetectorBitSyncpatternBitstring(
            device, f"{self._cmd_syntax}:BITString"
        )
        self._disparity: Dict[int, ErrordetectorBitSyncpatternDisparityItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: ErrordetectorBitSyncpatternDisparityItem(
                    device, f"{self._cmd_syntax}:DISParity{x}"
                )
            )
        )
        self._minus: Dict[int, ErrordetectorBitSyncpatternMinusItem] = DefaultDictPassKeyToFactory(
            lambda x: ErrordetectorBitSyncpatternMinusItem(device, f"{self._cmd_syntax}:MINus{x}")
        )
        self._plus: Dict[int, ErrordetectorBitSyncpatternPlusItem] = DefaultDictPassKeyToFactory(
            lambda x: ErrordetectorBitSyncpatternPlusItem(device, f"{self._cmd_syntax}:PLUS{x}")
        )

    @property
    def bitstring(self) -> ErrordetectorBitSyncpatternBitstring:
        """Return the ``ERRORDetector:BIT:SYNCPATtern:BITString`` command.

        Description:
            - This command queries the 10-, 20-, 30-, or 40-bit sync pattern in bit string form.

        Usage:
            - Using the ``.query()`` method will send the
              ``ERRORDetector:BIT:SYNCPATtern:BITString?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:SYNCPATtern:BITString?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:BIT:SYNCPATtern:BITString value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:SYNCPATtern:BITString <QString>
            - ERRORDetector:BIT:SYNCPATtern:BITString?
            ```

        Info:
            - ``<QString>`` is the bit string.
        """
        return self._bitstring

    @property
    def disparity(self) -> Dict[int, ErrordetectorBitSyncpatternDisparityItem]:
        """Return the ``ERRORDetector:BIT:SYNCPATtern:DISParity<x>`` command.

        Description:
            - Sets or queries the four sync pattern Disparity elements, when the
              ``SYNCpat:ADVanced`` is ON. When Advanced is off, the DISParity alternates based on
              the DISParity of the first element.

        Usage:
            - Using the ``.query()`` method will send the
              ``ERRORDetector:BIT:SYNCPATtern:DISParity<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:SYNCPATtern:DISParity<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:BIT:SYNCPATtern:DISParity<x> value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:SYNCPATtern:DISParity<x> {RDPLUS|RDMINUS}
            - ERRORDetector:BIT:SYNCPATtern:DISParity<x>?
            ```

        Info:
            - ``RDPLUS`` sets the sync pattern disparity element to RDPLUS.
            - ``RDMINUS`` sets the sync pattern disparity element to RDMINUS.
        """
        return self._disparity

    @property
    def minus(self) -> Dict[int, ErrordetectorBitSyncpatternMinusItem]:
        """Return the ``ERRORDetector:BIT:SYNCPATtern:MINus<x>`` command.

        Description:
            - This command queries the four RD- bit string sync pattern elements.

        Usage:
            - Using the ``.query()`` method will send the
              ``ERRORDetector:BIT:SYNCPATtern:MINus<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:SYNCPATtern:MINus<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:SYNCPATtern:MINus<x>?
            ```
        """
        return self._minus

    @property
    def plus(self) -> Dict[int, ErrordetectorBitSyncpatternPlusItem]:
        """Return the ``ERRORDetector:BIT:SYNCPATtern:PLUS<x>`` command.

        Description:
            - This command queries the four RD+ bit string sync pattern elements.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:SYNCPATtern:PLUS<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:SYNCPATtern:PLUS<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:SYNCPATtern:PLUS<x>?
            ```
        """
        return self._plus


class ErrordetectorBitPatternfilename(SCPICmdWrite, SCPICmdRead):
    r"""The ``ERRORDetector:BIT:PATTERNFilename`` command.

    Description:
        - This command sets or queries the drive:pathfilename.txt of a custom signal pattern file
          for the DPO70000SX instruments. The files contain 1 and 0 characters describing a custom
          signal pattern to be matched by the error detector. This file is only needed when the
          preset value is ``CUSTOM_SETUP``. Similar files are included on the oscilloscope for
          PRBS7, PRBS9, PRBS11, and PRBS16, and are located in the
          C:UsersPublicTektronixTekScopeErrorDetector directory. These files must be text type
          (\*.txt). You can examine these PRBS pattern files to help you develop any custom patterns
          you need. These text files can also be used to generate AWG signals (using Serial Express,
          for example). The files must be a multiple of 80 bits. If the length is not 80 bits, then
          the oscilloscope multiplies the length until it is a multiple of 80 bits, subject to the
          1.3 Mbit maximum length limit.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:PATTERNFilename?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:PATTERNFilename?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ERRORDetector:BIT:PATTERNFilename value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:PATTERNFilename <fileName>
        - ERRORDetector:BIT:PATTERNFilename?
        ```

    Info:
        - ``<fileName>`` is the ﬁle name and ﬁle location. The default location is
          C:UsersPublicTektronixTekScopeErrorDetector and the pattern ﬁle is in .txt format. The
          files contain long lists of 0's and 1's.
    """


class ErrordetectorBitLength(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:BIT:LENgth`` command.

    Description:
        - This command sets or queries the signal test pattern length in bits for non-USB bit error
          testing.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT:LENgth?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:LENgth?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:BIT:LENgth value``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:BIT:LENgth <NR1>
        - ERRORDetector:BIT:LENgth?
        ```

    Info:
        - ``<NR1>`` indicates the bit length of the signal test pattern.
    """


class ErrordetectorBit(SCPICmdRead):
    """The ``ERRORDetector:BIT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:BIT?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.length``: The ``ERRORDetector:BIT:LENgth`` command.
        - ``.patternfilename``: The ``ERRORDetector:BIT:PATTERNFilename`` command.
        - ``.syncpattern``: The ``ERRORDetector:BIT:SYNCPATtern`` command.
        - ``.test``: The ``ERRORDetector:BIT:TEST`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._length = ErrordetectorBitLength(device, f"{self._cmd_syntax}:LENgth")
        self._patternfilename = ErrordetectorBitPatternfilename(
            device, f"{self._cmd_syntax}:PATTERNFilename"
        )
        self._syncpattern = ErrordetectorBitSyncpattern(device, f"{self._cmd_syntax}:SYNCPATtern")
        self._test = ErrordetectorBitTest(device, f"{self._cmd_syntax}:TEST")

    @property
    def length(self) -> ErrordetectorBitLength:
        """Return the ``ERRORDetector:BIT:LENgth`` command.

        Description:
            - This command sets or queries the signal test pattern length in bits for non-USB bit
              error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:LENgth?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:LENgth?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:BIT:LENgth value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:LENgth <NR1>
            - ERRORDetector:BIT:LENgth?
            ```

        Info:
            - ``<NR1>`` indicates the bit length of the signal test pattern.
        """
        return self._length

    @property
    def patternfilename(self) -> ErrordetectorBitPatternfilename:
        r"""Return the ``ERRORDetector:BIT:PATTERNFilename`` command.

        Description:
            - This command sets or queries the drive:pathfilename.txt of a custom signal pattern
              file for the DPO70000SX instruments. The files contain 1 and 0 characters describing a
              custom signal pattern to be matched by the error detector. This file is only needed
              when the preset value is ``CUSTOM_SETUP``. Similar files are included on the
              oscilloscope for PRBS7, PRBS9, PRBS11, and PRBS16, and are located in the
              C:UsersPublicTektronixTekScopeErrorDetector directory. These files must be text type
              (\*.txt). You can examine these PRBS pattern files to help you develop any custom
              patterns you need. These text files can also be used to generate AWG signals (using
              Serial Express, for example). The files must be a multiple of 80 bits. If the length
              is not 80 bits, then the oscilloscope multiplies the length until it is a multiple of
              80 bits, subject to the 1.3 Mbit maximum length limit.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:PATTERNFilename?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:BIT:PATTERNFilename?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:BIT:PATTERNFilename value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:PATTERNFilename <fileName>
            - ERRORDetector:BIT:PATTERNFilename?
            ```

        Info:
            - ``<fileName>`` is the ﬁle name and ﬁle location. The default location is
              C:UsersPublicTektronixTekScopeErrorDetector and the pattern ﬁle is in .txt format. The
              files contain long lists of 0's and 1's.
        """
        return self._patternfilename

    @property
    def syncpattern(self) -> ErrordetectorBitSyncpattern:
        """Return the ``ERRORDetector:BIT:SYNCPATtern`` command.

        Description:
            - This command queries all of the sync pattern forms and associated settings for non-USB
              bit error testing. The SYNCPATtern consists of one to four symbolic 10-bit 8B10B
              characters and their matching RD+ and RD- bit string equivalents. It is required for
              all non-USB bit error testing. This sequence of 8B10B characters must actually occur
              and be unique in the signal test pattern sent to the oscilloscope for error detection
              to work correctly. The SyncPattern has a symbolic form ('K28.5'), an RD+ and RD- bit
              string form ('0011111010'), and an as-used bit string form. The actual form used
              depends on the ``SyncPattern:Disparity`` and ``SyncPattern:Advanced`` settings. When
              Advanced is Off, the disparity setting determines the disparity of the first
              (leftmost) syncpattern element, and the others alternate disparity. When Advanced is
              On, the Disparity is set for each SyncPattern element.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT:SYNCPATtern?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT:SYNCPATtern?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:SYNCPATtern?
            ```

        Sub-properties:
            - ``.bitstring``: The ``ERRORDetector:BIT:SYNCPATtern:BITString`` command.
            - ``.disparity``: The ``ERRORDetector:BIT:SYNCPATtern:DISParity<x>`` command.
            - ``.minus``: The ``ERRORDetector:BIT:SYNCPATtern:MINus<x>`` command.
            - ``.plus``: The ``ERRORDetector:BIT:SYNCPATtern:PLUS<x>`` command.
        """
        return self._syncpattern

    @property
    def test(self) -> ErrordetectorBitTest:
        """Return the ``ERRORDetector:BIT:TEST`` command.

        Description:
            - This command initiates and terminates bit error testing for the arguments START and
              STOP. It zeroes bit error test results for the argument CLEAR. It also copies the test
              pattern from the signal to memory for the argument LEARN. It re-synchronizes the
              recovered clock for argument SYNC.

        Usage:
            - Using the ``.write(value)`` method will send the ``ERRORDetector:BIT:TEST value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:BIT:TEST <LEARN | START | STOP | CLEAR | SYNC>DPO70000SX<START | STOP | CLEAR>
            ```

        Info:
            - ``LEARN`` copies the test pattern from the signal to the hardware template memory.
            - ``START`` initiates bit error counting of bit errors and duration.
            - ``STOP`` terminates bit error counting of bit errors and duration.
            - ``CLEAR`` zeroes the bit error count, duration, and bit error rate.
            - ``SYNC`` resynchronizes the recovered clock.

        Sub-properties:
            - ``.count``: The ``ERRORDetector:BIT:TEST:COUNt`` command.
            - ``.duration``: The ``ERRORDetector:BIT:TEST:DURATION`` command.
            - ``.maxaligns``: The ``ERRORDetector:BIT:TEST:MAXALIGNS`` command.
            - ``.rate``: The ``ERRORDetector:BIT:TEST:RATE`` command.
            - ``.results``: The ``ERRORDetector:BIT:TEST:RESults`` command.
            - ``.seconds``: The ``ERRORDetector:BIT:TEST:SECOnds`` command.
            - ``.status``: The ``ERRORDetector:BIT:TEST:STATUS`` command.
            - ``.time``: The ``ERRORDetector:BIT:TEST:TIME`` command.
        """  # noqa: E501
        return self._test


class ErrordetectorAlignprimitiveSymbols(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``ERRORDetector:ALIGNPRIMitive:SYMBOLS`` command.

    Description:
        - Sets or queries the four align primitive symbols. You can set one or more symbols with the
          command, but they must be done in order. The query returns all four symbols.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:SYMBOLS?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:ALIGNPRIMitive:SYMBOLS?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``ERRORDetector:ALIGNPRIMitive:SYMBOLS``
          command.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNPRIMitive:SYMBOLS
        - ERRORDetector:ALIGNPRIMitive:SYMBOLS?
        ```

    Info:
        - ``<Qstring>`` is a quoted string representing one of the four align primitive symbols,
          such as 'K28.5'. You can set one or more of the symbols with a single command, but the
          symbols must be set in order.
    """


class ErrordetectorAlignprimitiveSymbolItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:ALIGNPRIMitive:SYMBOL<x>`` command.

    Description:
        - Sets or queries the align primitive symbol. The individual symbolic array elements may be
          accessed through SYMbol1, SYMBol2, etc.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:SYMBOL<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:ALIGNPRIMitive:SYMBOL<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ERRORDetector:ALIGNPRIMitive:SYMBOL<x> value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNPRIMitive:SYMBOL<x> <QString>
        - ERRORDetector:ALIGNPRIMitive:SYMBOL<x>?
        ```

    Info:
        - ``<QString>`` is a quoted string representing the symbolic align primitive symbols such as
          K28.5.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ErrordetectorAlignprimitiveState(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:ALIGNPRIMitive:STATE`` command.

    Description:
        - This command sets or queries the status of the RD- align primitive option.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALIGNPRIMitive:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ERRORDetector:ALIGNPRIMitive:STATE value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNPRIMitive:STATE {ON|OFF|<NR1>}
        - ERRORDetector:ALIGNPRIMitive:STATE?
        ```

    Info:
        - ``ON`` enables the align primitive option.
        - ``OFF`` disables the align primitive option.
        - ``<NR1>`` = 0 disables the align primitive option; any other value enables the option.
    """


class ErrordetectorAlignprimitivePlusItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``ERRORDetector:ALIGNPRIMitive:PLUS<x>`` command.

    Description:
        - This command queries the align primitive plus value.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:PLUS<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:ALIGNPRIMitive:PLUS<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNPRIMitive:PLUS<x>?
        ```
    """


class ErrordetectorAlignprimitivePlus(SCPICmdRead):
    """The ``ERRORDetector:ALIGNPRIMitive:PLUS`` command.

    Description:
        - This command queries the four RD+ align primitive bit string values.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:PLUS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALIGNPRIMitive:PLUS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNPRIMitive:PLUS?
        ```
    """


class ErrordetectorAlignprimitiveMinusItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``ERRORDetector:ALIGNPRIMitive:MINus<x>`` command.

    Description:
        - This command queries the RD- align primitive bit string values.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:MINus<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ERRORDetector:ALIGNPRIMitive:MINus<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNPRIMitive:MINus<x>?
        ```
    """


class ErrordetectorAlignprimitiveMinus(SCPICmdRead):
    """The ``ERRORDetector:ALIGNPRIMitive:MINUS`` command.

    Description:
        - This command queries the RD- align primitive bit string values.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:MINUS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALIGNPRIMitive:MINUS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNPRIMitive:MINUS?
        ```
    """


class ErrordetectorAlignprimitive(SCPICmdRead):
    """The ``ERRORDetector:ALIGNPRIMitive`` command.

    Description:
        - This command queries all of the align primitive values, including its state (ON=1/OFF=0),
          the length four array of symbolic character values, and the RD+ and RD- .length four
          arrays of bit string values.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALIGNPRIMitive?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNPRIMitive?
        ```

    Properties:
        - ``.minus``: The ``ERRORDetector:ALIGNPRIMitive:MINUS`` command.
        - ``.minusx``: The ``ERRORDetector:ALIGNPRIMitive:MINus<x>`` command.
        - ``.plus``: The ``ERRORDetector:ALIGNPRIMitive:PLUS`` command.
        - ``.plusx``: The ``ERRORDetector:ALIGNPRIMitive:PLUS<x>`` command.
        - ``.state``: The ``ERRORDetector:ALIGNPRIMitive:STATE`` command.
        - ``.symbol``: The ``ERRORDetector:ALIGNPRIMitive:SYMBOL<x>`` command.
        - ``.symbols``: The ``ERRORDetector:ALIGNPRIMitive:SYMBOLS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._minus = ErrordetectorAlignprimitiveMinus(device, f"{self._cmd_syntax}:MINUS")
        self._minusx: Dict[int, ErrordetectorAlignprimitiveMinusItem] = DefaultDictPassKeyToFactory(
            lambda x: ErrordetectorAlignprimitiveMinusItem(device, f"{self._cmd_syntax}:MINus{x}")
        )
        self._plus = ErrordetectorAlignprimitivePlus(device, f"{self._cmd_syntax}:PLUS")
        self._plusx: Dict[int, ErrordetectorAlignprimitivePlusItem] = DefaultDictPassKeyToFactory(
            lambda x: ErrordetectorAlignprimitivePlusItem(device, f"{self._cmd_syntax}:PLUS{x}")
        )
        self._state = ErrordetectorAlignprimitiveState(device, f"{self._cmd_syntax}:STATE")
        self._symbol: Dict[int, ErrordetectorAlignprimitiveSymbolItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: ErrordetectorAlignprimitiveSymbolItem(
                    device, f"{self._cmd_syntax}:SYMBOL{x}"
                )
            )
        )
        self._symbols = ErrordetectorAlignprimitiveSymbols(device, f"{self._cmd_syntax}:SYMBOLS")

    @property
    def minus(self) -> ErrordetectorAlignprimitiveMinus:
        """Return the ``ERRORDetector:ALIGNPRIMitive:MINUS`` command.

        Description:
            - This command queries the RD- align primitive bit string values.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:MINUS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:ALIGNPRIMitive:MINUS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNPRIMitive:MINUS?
            ```
        """
        return self._minus

    @property
    def minusx(self) -> Dict[int, ErrordetectorAlignprimitiveMinusItem]:
        """Return the ``ERRORDetector:ALIGNPRIMitive:MINus<x>`` command.

        Description:
            - This command queries the RD- align primitive bit string values.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:MINus<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:ALIGNPRIMitive:MINus<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNPRIMitive:MINus<x>?
            ```
        """
        return self._minusx

    @property
    def plus(self) -> ErrordetectorAlignprimitivePlus:
        """Return the ``ERRORDetector:ALIGNPRIMitive:PLUS`` command.

        Description:
            - This command queries the four RD+ align primitive bit string values.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:PLUS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:ALIGNPRIMitive:PLUS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNPRIMitive:PLUS?
            ```
        """
        return self._plus

    @property
    def plusx(self) -> Dict[int, ErrordetectorAlignprimitivePlusItem]:
        """Return the ``ERRORDetector:ALIGNPRIMitive:PLUS<x>`` command.

        Description:
            - This command queries the align primitive plus value.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:PLUS<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:ALIGNPRIMitive:PLUS<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNPRIMitive:PLUS<x>?
            ```
        """
        return self._plusx

    @property
    def state(self) -> ErrordetectorAlignprimitiveState:
        """Return the ``ERRORDetector:ALIGNPRIMitive:STATE`` command.

        Description:
            - This command sets or queries the status of the RD- align primitive option.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:ALIGNPRIMitive:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:ALIGNPRIMitive:STATE value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNPRIMitive:STATE {ON|OFF|<NR1>}
            - ERRORDetector:ALIGNPRIMitive:STATE?
            ```

        Info:
            - ``ON`` enables the align primitive option.
            - ``OFF`` disables the align primitive option.
            - ``<NR1>`` = 0 disables the align primitive option; any other value enables the option.
        """
        return self._state

    @property
    def symbol(self) -> Dict[int, ErrordetectorAlignprimitiveSymbolItem]:
        """Return the ``ERRORDetector:ALIGNPRIMitive:SYMBOL<x>`` command.

        Description:
            - Sets or queries the align primitive symbol. The individual symbolic array elements may
              be accessed through SYMbol1, SYMBol2, etc.

        Usage:
            - Using the ``.query()`` method will send the
              ``ERRORDetector:ALIGNPRIMitive:SYMBOL<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:ALIGNPRIMitive:SYMBOL<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:ALIGNPRIMitive:SYMBOL<x> value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNPRIMitive:SYMBOL<x> <QString>
            - ERRORDetector:ALIGNPRIMitive:SYMBOL<x>?
            ```

        Info:
            - ``<QString>`` is a quoted string representing the symbolic align primitive symbols
              such as K28.5.
        """
        return self._symbol

    @property
    def symbols(self) -> ErrordetectorAlignprimitiveSymbols:
        """Return the ``ERRORDetector:ALIGNPRIMitive:SYMBOLS`` command.

        Description:
            - Sets or queries the four align primitive symbols. You can set one or more symbols with
              the command, but they must be done in order. The query returns all four symbols.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive:SYMBOLS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:ALIGNPRIMitive:SYMBOLS?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``ERRORDetector:ALIGNPRIMitive:SYMBOLS``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNPRIMitive:SYMBOLS
            - ERRORDetector:ALIGNPRIMitive:SYMBOLS?
            ```

        Info:
            - ``<Qstring>`` is a quoted string representing one of the four align primitive symbols,
              such as 'K28.5'. You can set one or more of the symbols with a single command, but the
              symbols must be set in order.
        """
        return self._symbols


class ErrordetectorAligncharacterSymbol(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:ALIGNCHARacter:SYMBOL`` command.

    Description:
        - This command sets or queries the symbolic align character value. Reception of the align
          character by the instrument aligns the receiver to the 10-bit character boundary.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNCHARacter:SYMBOL?``
          query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALIGNCHARacter:SYMBOL?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ERRORDetector:ALIGNCHARacter:SYMBOL value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNCHARacter:SYMBOL <QString>
        - ERRORDetector:ALIGNCHARacter:SYMBOL?
        ```

    Info:
        - ``<QString>`` is a quoted string representing a symbolic character, e.g., 'K28.5'.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ErrordetectorAligncharacterPlus(SCPICmdRead):
    """The ``ERRORDetector:ALIGNCHARacter:PLUS`` command.

    Description:
        - This command queries the RD+ align character bit string value. Reception of the align
          character by the instrument aligns the receiver to the 10-bit character boundary.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNCHARacter:PLUS?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALIGNCHARacter:PLUS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNCHARacter:PLUS?
        ```
    """


class ErrordetectorAligncharacterMinus(SCPICmdRead):
    """The ``ERRORDetector:ALIGNCHARacter:MINus`` command.

    Description:
        - This command queries the RD- align character bit string value. Reception of this character
          by the instrument causes the receiver to align to the 10-bit character boundary.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNCHARacter:MINus?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALIGNCHARacter:MINus?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNCHARacter:MINus?
        ```
    """


class ErrordetectorAligncharacter(SCPICmdRead):
    """The ``ERRORDetector:ALIGNCHARacter`` command.

    Description:
        - This command queries all of the align character values. Align characters must be defined
          for all test types, and those characters must appear in the signal test pattern. The Align
          character may be in symbolic or bit string form

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNCHARacter?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALIGNCHARacter?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ERRORDetector:ALIGNCHARacter?
        ```

    Properties:
        - ``.minus``: The ``ERRORDetector:ALIGNCHARacter:MINus`` command.
        - ``.plus``: The ``ERRORDetector:ALIGNCHARacter:PLUS`` command.
        - ``.symbol``: The ``ERRORDetector:ALIGNCHARacter:SYMBOL`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._minus = ErrordetectorAligncharacterMinus(device, f"{self._cmd_syntax}:MINus")
        self._plus = ErrordetectorAligncharacterPlus(device, f"{self._cmd_syntax}:PLUS")
        self._symbol = ErrordetectorAligncharacterSymbol(device, f"{self._cmd_syntax}:SYMBOL")

    @property
    def minus(self) -> ErrordetectorAligncharacterMinus:
        """Return the ``ERRORDetector:ALIGNCHARacter:MINus`` command.

        Description:
            - This command queries the RD- align character bit string value. Reception of this
              character by the instrument causes the receiver to align to the 10-bit character
              boundary.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNCHARacter:MINus?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:ALIGNCHARacter:MINus?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNCHARacter:MINus?
            ```
        """
        return self._minus

    @property
    def plus(self) -> ErrordetectorAligncharacterPlus:
        """Return the ``ERRORDetector:ALIGNCHARacter:PLUS`` command.

        Description:
            - This command queries the RD+ align character bit string value. Reception of the align
              character by the instrument aligns the receiver to the 10-bit character boundary.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNCHARacter:PLUS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:ALIGNCHARacter:PLUS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNCHARacter:PLUS?
            ```
        """
        return self._plus

    @property
    def symbol(self) -> ErrordetectorAligncharacterSymbol:
        """Return the ``ERRORDetector:ALIGNCHARacter:SYMBOL`` command.

        Description:
            - This command sets or queries the symbolic align character value. Reception of the
              align character by the instrument aligns the receiver to the 10-bit character
              boundary.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNCHARacter:SYMBOL?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ERRORDetector:ALIGNCHARacter:SYMBOL?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ERRORDetector:ALIGNCHARacter:SYMBOL value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNCHARacter:SYMBOL <QString>
            - ERRORDetector:ALIGNCHARacter:SYMBOL?
            ```

        Info:
            - ``<QString>`` is a quoted string representing a symbolic character, e.g., 'K28.5'.
        """
        return self._symbol


class ErrordetectorAlert(SCPICmdWrite, SCPICmdRead):
    """The ``ERRORDetector:ALERT`` command.

    Description:
        - This command sets or queries the error detector alert.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector:ALERT?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALERT?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ERRORDetector:ALERT value`` command.

    SCPI Syntax:
        ```
        - ERRORDetector:ALERT {ON|OFF|<NR1>}
        - ERRORDetector:ALERT?
        ```

    Info:
        - ``ON`` turns on the error detector alert.
        - ``OFF`` turns off the error detector alert.
        - ``<NR1>`` = 0 disables the alert; any other value enables the alert.
    """


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class Errordetector(SCPICmdRead):
    """The ``ERRORDetector`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ERRORDetector?`` query.
        - Using the ``.verify(value)`` method will send the ``ERRORDetector?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.alert``: The ``ERRORDetector:ALERT`` command.
        - ``.aligncharacter``: The ``ERRORDetector:ALIGNCHARacter`` command.
        - ``.alignprimitive``: The ``ERRORDetector:ALIGNPRIMitive`` command.
        - ``.bit``: The ``ERRORDetector:BIT`` command tree.
        - ``.bitrate``: The ``ERRORDetector:BITRate`` command.
        - ``.channel``: The ``ERRORDetector:CHANnel`` command.
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
        - ``.ssc``: The ``ERRORDetector:SSC`` command.
        - ``.standard``: The ``ERRORDetector:STANdard`` command.
        - ``.state``: The ``ERRORDetector:STATE`` command.
        - ``.status``: The ``ERRORDetector:STATus`` command.
        - ``.stopwhen``: The ``ERRORDetector:STOPWHEN`` command.
        - ``.symbol``: The ``ERRORDetector:SYMBOL`` command.
        - ``.timeformat``: The ``ERRORDetector:TIMEformat`` command.
        - ``.type``: The ``ERRORDetector:TYPe`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "ERRORDetector"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._alert = ErrordetectorAlert(device, f"{self._cmd_syntax}:ALERT")
        self._aligncharacter = ErrordetectorAligncharacter(
            device, f"{self._cmd_syntax}:ALIGNCHARacter"
        )
        self._alignprimitive = ErrordetectorAlignprimitive(
            device, f"{self._cmd_syntax}:ALIGNPRIMitive"
        )
        self._bit = ErrordetectorBit(device, f"{self._cmd_syntax}:BIT")
        self._bitrate = ErrordetectorBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._channel = ErrordetectorChannel(device, f"{self._cmd_syntax}:CHANnel")
        self._duration = ErrordetectorDuration(device, f"{self._cmd_syntax}:DURATION")
        self._errorlimit = ErrordetectorErrorlimit(device, f"{self._cmd_syntax}:ERRORLIMIT")
        self._file = ErrordetectorFile(device, f"{self._cmd_syntax}:FILE")
        self._fontsize = ErrordetectorFontsize(device, f"{self._cmd_syntax}:FONTSIze")
        self._frame = ErrordetectorFrame(device, f"{self._cmd_syntax}:FRAme")
        self._maxaligns = ErrordetectorMaxaligns(device, f"{self._cmd_syntax}:MAXALIGNS")
        self._patternname = ErrordetectorPatternname(device, f"{self._cmd_syntax}:PATTERNNAME")
        self._preset = ErrordetectorPreset(device, f"{self._cmd_syntax}:PREset")
        self._saveimage = ErrordetectorSaveimage(device, f"{self._cmd_syntax}:SAVEIMAGE")
        self._savewfm = ErrordetectorSavewfm(device, f"{self._cmd_syntax}:SAVEWFM")
        self._scrambled = ErrordetectorScrambled(device, f"{self._cmd_syntax}:SCRAMBLED")
        self._sendemail = ErrordetectorSendemail(device, f"{self._cmd_syntax}:SENDEMAIL")
        self._signaltype = ErrordetectorSignaltype(device, f"{self._cmd_syntax}:SIGnaltype")
        self._ssc = ErrordetectorSsc(device, f"{self._cmd_syntax}:SSC")
        self._standard = ErrordetectorStandard(device, f"{self._cmd_syntax}:STANdard")
        self._state = ErrordetectorState(device, f"{self._cmd_syntax}:STATE")
        self._status = ErrordetectorStatus(device, f"{self._cmd_syntax}:STATus")
        self._stopwhen = ErrordetectorStopwhen(device, f"{self._cmd_syntax}:STOPWHEN")
        self._symbol = ErrordetectorSymbol(device, f"{self._cmd_syntax}:SYMBOL")
        self._timeformat = ErrordetectorTimeformat(device, f"{self._cmd_syntax}:TIMEformat")
        self._type = ErrordetectorType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def alert(self) -> ErrordetectorAlert:
        """Return the ``ERRORDetector:ALERT`` command.

        Description:
            - This command sets or queries the error detector alert.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALERT?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALERT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:ALERT value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:ALERT {ON|OFF|<NR1>}
            - ERRORDetector:ALERT?
            ```

        Info:
            - ``ON`` turns on the error detector alert.
            - ``OFF`` turns off the error detector alert.
            - ``<NR1>`` = 0 disables the alert; any other value enables the alert.
        """
        return self._alert

    @property
    def aligncharacter(self) -> ErrordetectorAligncharacter:
        """Return the ``ERRORDetector:ALIGNCHARacter`` command.

        Description:
            - This command queries all of the align character values. Align characters must be
              defined for all test types, and those characters must appear in the signal test
              pattern. The Align character may be in symbolic or bit string form

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNCHARacter?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALIGNCHARacter?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNCHARacter?
            ```

        Sub-properties:
            - ``.minus``: The ``ERRORDetector:ALIGNCHARacter:MINus`` command.
            - ``.plus``: The ``ERRORDetector:ALIGNCHARacter:PLUS`` command.
            - ``.symbol``: The ``ERRORDetector:ALIGNCHARacter:SYMBOL`` command.
        """
        return self._aligncharacter

    @property
    def alignprimitive(self) -> ErrordetectorAlignprimitive:
        """Return the ``ERRORDetector:ALIGNPRIMitive`` command.

        Description:
            - This command queries all of the align primitive values, including its state
              (ON=1/OFF=0), the length four array of symbolic character values, and the RD+ and RD-
              .length four arrays of bit string values.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ALIGNPRIMitive?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:ALIGNPRIMitive?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:ALIGNPRIMitive?
            ```

        Sub-properties:
            - ``.minus``: The ``ERRORDetector:ALIGNPRIMitive:MINUS`` command.
            - ``.minusx``: The ``ERRORDetector:ALIGNPRIMitive:MINus<x>`` command.
            - ``.plus``: The ``ERRORDetector:ALIGNPRIMitive:PLUS`` command.
            - ``.plusx``: The ``ERRORDetector:ALIGNPRIMitive:PLUS<x>`` command.
            - ``.state``: The ``ERRORDetector:ALIGNPRIMitive:STATE`` command.
            - ``.symbol``: The ``ERRORDetector:ALIGNPRIMitive:SYMBOL<x>`` command.
            - ``.symbols``: The ``ERRORDetector:ALIGNPRIMitive:SYMBOLS`` command.
        """
        return self._alignprimitive

    @property
    def bit(self) -> ErrordetectorBit:
        """Return the ``ERRORDetector:BIT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BIT?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BIT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.length``: The ``ERRORDetector:BIT:LENgth`` command.
            - ``.patternfilename``: The ``ERRORDetector:BIT:PATTERNFilename`` command.
            - ``.syncpattern``: The ``ERRORDetector:BIT:SYNCPATtern`` command.
            - ``.test``: The ``ERRORDetector:BIT:TEST`` command.
        """
        return self._bit

    @property
    def bitrate(self) -> ErrordetectorBitrate:
        """Return the ``ERRORDetector:BITRate`` command.

        Description:
            - This command sets or queries error detector bitrate enumeration for error detection.
              There are two bitrate enumerations for each standard: 1) The standard bitrate, for
              example RATE6000 (meaning 6.0Gb/s, for SATA Gen3); and 2) Custom. When Custom is
              selected the ``ERRORDetector:BITRATE:VALUE`` must also be set to the specific desired
              bitrate. For example, 6.1 Gb/s.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:BITRate value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:BITRate {RATEcustom:CUSTOM|RATE312000000:RATE312|RATE1250000000:RATE1250|RATE1500000000:RATE1500|RATE2125000000:RATE2125|RATE2500000000:RATE2500|RATE3000000000:RATE3000|RATE3125000000:RATE3125|RATE4250000000:RATE4250|RATE5000000000:RATE5000|RATE6000000000:RATE6000|RATE6250000000:RATE6250}DPO70000SX{RATE3200|RATE3600|RATE4000|RATE4400|RATE4800|RATE5200|RATE5600|RATE6000|RATE6400|CUSTOM}
            - ERRORDetector:BITRate?
            ```

        Info:
            - ``RATE3200..to..RATE6400`` sets the error detector bit rate to the specified value.
              RATE3200 indicates a bitrate of 3.2 Gb/s, etc.
            - ``:ERRORDETECTOR:BITRATE:VALUE`` command.

        Sub-properties:
            - ``.value``: The ``ERRORDetector:BITRate:VALue`` command.
        """  # noqa: E501
        return self._bitrate

    @property
    def channel(self) -> ErrordetectorChannel:
        """Return the ``ERRORDetector:CHANnel`` command.

        Description:
            - Sets or queries error detector channel selection.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:CHANnel?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:CHANnel?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:CHANnel value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:CHANnel {CH1|CH2|CH3|CH4}
            - ERRORDetector:CHANnel?
            ```

        Info:
            - ``CHx`` is the error detector channel selection.
        """
        return self._channel

    @property
    def duration(self) -> ErrordetectorDuration:
        """Return the ``ERRORDetector:DURATION`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:DURATION?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:DURATION?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.count``: The ``ERRORDetector:DURATION:COUNt`` command.
            - ``.seconds``: The ``ERRORDetector:DURATION:SECOnds`` command.
            - ``.time``: The ``ERRORDetector:DURATION:TIME`` command.
        """
        return self._duration

    @property
    def errorlimit(self) -> ErrordetectorErrorlimit:
        """Return the ``ERRORDetector:ERRORLIMIT`` command.

        Description:
            - This command sets or queries the error limit value to use when STOPWHEN is ERROR.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:ERRORLIMIT?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:ERRORLIMIT?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:ERRORLIMIT value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:ERRORLIMIT <NR1>
            - ERRORDetector:ERRORLIMIT?
            ```

        Info:
            - ``<NR1>`` is the maximum number of errors.
        """
        return self._errorlimit

    @property
    def file(self) -> ErrordetectorFile:
        """Return the ``ERRORDetector:FILE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FILE?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:FILE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.recall``: The ``ERRORDetector:FILE:RECAll`` command.
            - ``.save``: The ``ERRORDetector:FILE:SAVe`` command.
        """
        return self._file

    @property
    def fontsize(self) -> ErrordetectorFontsize:
        """Return the ``ERRORDetector:FONTSIze`` command.

        Description:
            - Sets or queries error detector font size selection. Currently, the font size only
              applied the error detector UI control window.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FONTSIze?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:FONTSIze?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:FONTSIze value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:FONTSIze {DEFAULT|LARGE|XLARGE}
            - ERRORDetector:FONTSIze?
            ```

        Info:
            - ``DEFAULT`` sets the font size to the default size.
            - ``LARGE`` sets the font size to large.
            - ``XLARGE`` sets the font size to extra large.
        """
        return self._fontsize

    @property
    def frame(self) -> ErrordetectorFrame:
        """Return the ``ERRORDetector:FRAme`` command.

        Description:
            - This command queries all frame error settings, status, and results.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:FRAme?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:FRAme?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:FRAme?
            ```

        Sub-properties:
            - ``.eof``: The ``ERRORDetector:FRAme:EOF`` command.
            - ``.initialcrcvalue``: The ``ERRORDetector:FRAme:INITIALCRCVALue`` command.
            - ``.sof``: The ``ERRORDetector:FRAme:SOF`` command.
            - ``.test``: The ``ERRORDetector:FRAme:TEST`` command.
        """
        return self._frame

    @property
    def maxaligns(self) -> ErrordetectorMaxaligns:
        """Return the ``ERRORDetector:MAXALIGNS`` command.

        Description:
            - This command sets or queries the maximum consecutive align primitives before a
              ``MAX_AP_FAIL`` error is reported.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:MAXALIGNS?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:MAXALIGNS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:MAXALIGNS value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:MAXALIGNS <NR1>
            - ERRORDetector:MAXALIGNS?
            ```

        Info:
            - ``<NR1>`` is a integer. The limit values are 0 to 63 and the default is 8.
        """
        return self._maxaligns

    @property
    def patternname(self) -> ErrordetectorPatternname:
        """Return the ``ERRORDetector:PATTERNNAME`` command.

        Description:
            - This command sets or queries the pattern name stored in the setup file. Setting this
              name has no functional effect on the instrument, but it is a convenient reminder to
              users as to which setup is in effect.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:PATTERNNAME?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:PATTERNNAME?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:PATTERNNAME value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:PATTERNNAME <Qstring>
            - ERRORDetector:PATTERNNAME?
            ```

        Info:
            - ``<Qstring>`` is a quoted string representing a pattern name.
        """
        return self._patternname

    @property
    def preset(self) -> ErrordetectorPreset:
        """Return the ``ERRORDetector:PREset`` command.

        Description:
            - This command sets or queries error detector font preset selection. A number of preset
              setups are selected by this parameter to cover the more common cases. The preset names
              attempt to indicate the standard, signal pattern, and test type employed. The bit rate
              appropriate for the standard is used. The text files containing the preset setups are
              located in the C:UsersPublicTektronixTekScopeErrorDetector directory in Windows. You
              may select CUSTOM as a preset value, and save or recall your own custom setups. You
              may want to recall one of the standard preset setups, modify some of the parameters,
              and then save it as a custom setup for recall at a later time. This same behavior is
              supported on the error detector User Interface. he ``SATA3_FRAME`` preset expects the
              SATA3 Compliance Pattern. ``USB3_SYMBOL`` preset expects the USB3 standard ``CP0_SKP``
              signal. You can set a PATTERNNAME for each setup.

        Usage:
            - Using the ``.write(value)`` method will send the ``ERRORDetector:PREset value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:PREset {SATA1_CJTPAT_BIT|SATA2_CJTPAT_BIT|SATA3_CJTPAT_BIT|SATA3_FRAME|SATA3_CHAR|SATA3_HFTP_BIT|SATA3_LBP_BIT|SATA3_LFTP_BIT|SATA3_MFTP_BIT|USB3_SYMBOL|USB3_CHAR|PCIE1_COMP_BIT|PCIE2_COMP_BIT|ANY_CJTPAT_BIT|ANY_CJTPAT_CHAR|CUSTOM}DPO70000SX{CUSTOM_SETUP|PRBS7_BIT_ERROR|PRBS9_BIT_ERROR|PRBS11_BIT_ERROR|PRBS16_BIT_ERROR|PRBS23_BIT_ERROR}
            ```

        Sub-properties:
            - ``.apply``: The ``ERRORDetector:PREset:APPLY`` command.
        """  # noqa: E501
        return self._preset

    @property
    def saveimage(self) -> ErrordetectorSaveimage:
        """Return the ``ERRORDetector:SAVEIMAGE`` command.

        Description:
            - Sets or queries error detector Save Image control. When set to ON, a screen shot will
              be made when the error detector detects an error (because detecting an error triggers
              the scope). The images are saved in the C:Users<yourName>
              TektronixTekScopeSaveOnTrigger directory. A default limit of 10 screen shots prevents
              overflowing your disk drive should the error detector sense massive errors, such as
              when you disconnect the signal. If you also set the SendEmail parameter to ON, the
              saved image (screen shot) will be emailed to the recipient (set elsewhere in the
              trigger PI). SaveImage is an alternate way of setting the Save on Trigger actions
              defined elsewhere in the PI.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SAVEIMAGE?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:SAVEIMAGE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:SAVEIMAGE value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:SAVEIMAGE {OFF|ON}
            - ERRORDetector:SAVEIMAGE?
            ```
        """
        return self._saveimage

    @property
    def savewfm(self) -> ErrordetectorSavewfm:
        """Return the ``ERRORDetector:SAVEWFM`` command.

        Description:
            - This command sets or queries error detector Save Waveform (WFM) control. When set to
              ON, a waveform object will be made when the error detector detects an error (because
              detecting an error triggers the instrument). The waveforms are saved in the
              C:Users<yourName>TektronixTekScopeSaveOnTrigger directory. A default limit of 10
              screen shots prevents overflowing your disk drive should the error detector sense
              massive errors, such as when you disconnect the signal. If you also set the SendEmail
              parameter to ON, the saved waveform (wfm object) is emailed to the recipient (set
              elsewhere in the trigger PI) as an attachedment. SaveImage is an alternate way of
              setting the Save on Trigger actions defined elsewhere in the PI.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SAVEWFM?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:SAVEWFM?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:SAVEWFM value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:SAVEWFM {OFF|ON}
            - ERRORDetector:SAVEWFM?
            ```

        Info:
            - ``OFF`` turns off the error detector save waveform feature.
            - ``ON`` turns on the error detector save waveform feature.
        """
        return self._savewfm

    @property
    def scrambled(self) -> ErrordetectorScrambled:
        """Return the ``ERRORDetector:SCRAMBLED`` command.

        Description:
            - This command sets or queries the status of the error detection data scrambling option.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SCRAMBLED?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:SCRAMBLED?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:SCRAMBLED value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:SCRAMBLED {ON|OFF}
            - ERRORDetector:SCRAMBLED?
            ```

        Info:
            - ``ON`` enables the error detection data scrambling option. This is the default option.
            - ``OFF`` disables the error detection data scrambling option.
        """
        return self._scrambled

    @property
    def sendemail(self) -> ErrordetectorSendemail:
        """Return the ``ERRORDetector:SENDEMAIL`` command.

        Description:
            - This command sets or queries error detector Send Email control. When set to ON, a
              email will be sent to the recipient, defined elsewhere in the PI, when the error
              detector detects an error (because detecting an error triggers the instrument). The
              default number of emails sent is 1, so that you do not overflow your inbox. If you
              also set the SaveImage or SaveWfm parameters to ON, the email will contain these
              items. Send Email is an alternate way of setting the E-mail on Trigger actions defined
              elsewhere in the PI.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SENDEMAIL?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:SENDEMAIL?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:SENDEMAIL value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:SENDEMAIL {OFF|ON}
            - ERRORDetector:SENDEMAIL?
            ```

        Info:
            - ``OFF`` disables the send email feature.
            - ``ON`` enables the send email feature.
        """
        return self._sendemail

    @property
    def signaltype(self) -> ErrordetectorSignaltype:
        """Return the ``ERRORDetector:SIGnaltype`` command.

        Description:
            - This command sets or queries error detector Signal Type control. Setting the signal
              type establishes the bit rate appropriate for the standard, as well as establishing
              the testing algorithm. Custom bit rates may be used as well. See the
              ``ERRORDetector:BITRATE`` and ``ERRORDetector:BITRATE:VALue`` commands.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SIGnaltype?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:SIGnaltype?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:SIGnaltype value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:SIGnaltype {ANY8B10B|CUSTOM|PCIEGEN<x>|PRBS11|PRBS16|PRBS23|PRBS7|PRBS9|SATAGEN<x>|USB3}
            - ERRORDetector:SIGnaltype?
            ```

        Info:
            - ``The DPO70000SX only supports PRBS7, PRBS9, PRBS11, PRBS16, PRBS23, and CUSTOM.``
        """  # noqa: E501
        return self._signaltype

    @property
    def ssc(self) -> ErrordetectorSsc:
        """Return the ``ERRORDetector:SSC`` command.

        Description:
            - This command sets or queries the status of the spread spectrum clock tracking option.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SSC?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:SSC?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:SSC value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:SSC {ON|OFF}
            - ERRORDetector:SSC?
            ```

        Info:
            - ``ON`` enables spread spectrum clock tracking. For error detector, the spread spectrum
              clock tracking should always be turned on.
            - ``OFF`` disables spread spectrum clock tracking. For serial trigger, the spread
              spectrum clock tracking is turned off.
        """
        return self._ssc

    @property
    def standard(self) -> ErrordetectorStandard:
        """Return the ``ERRORDetector:STANdard`` command.

        Description:
            - This command sets or queries the standard selection for error testing.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:STANdard?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:STANdard?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:STANdard value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:STANdard <LIST>
            - ERRORDetector:STANdard?
            ```

        Info:
            - ``<LIST>`` is the supported standard.
        """
        return self._standard

    @property
    def state(self) -> ErrordetectorState:
        """Return the ``ERRORDetector:STATE`` command.

        Description:
            - This command sets or queries the status of the error option. STATE must be ON to use
              the error detector feature.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:STATE value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:STATE {ON|OFF|<NR1>}
            - ERRORDetector:STATE?
            ```

        Info:
            - ``ON`` enables the software error detector feature.
            - ``OFF`` disables the software error detector feature. This is the default.
            - ``<NR1>`` = 0 disables the error detector; any other value enables the error detector.
        """
        return self._state

    @property
    def status(self) -> ErrordetectorStatus:
        """Return the ``ERRORDetector:STATus`` command.

        Description:
            - Queries only the 'most significant' or 'summary' status of the error detector. All of
              the status flags for each test type may be obtained from the
              ``ERRORdetector:<TESTTYPE>:TEST:STATUS`` commands. LOCK refers to the recovered clock.
              Signal refers to the cable carrying the signal to the scope. SYNC refers to bit error
              tests that require a sync pattern. STOPPED/COUNTING refer to whether the error
              detector is testing for errors. ``MAX_AP`` refers to whether the error detector has
              detected the maximum consecutive Align (or SkipSets) Primitives as specified in the
              ERRORDetector: <TESTTYPE>MAXALIGNS command

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:STATus?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:STATus?
            ```
        """
        return self._status

    @property
    def stopwhen(self) -> ErrordetectorStopwhen:
        """Return the ``ERRORDetector:STOPWHEN`` command.

        Description:
            - This command sets or queries the stopping condition. The test can be stopped when the
              count, time, or number of errors elapses. If the STOPWHEN value is MANUAL, the test
              runs until a TEST STOP command is received.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:STOPWHEN?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:STOPWHEN?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:STOPWHEN value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:STOPWHEN <MANUAL | COUNT | TIME | ERROR>DPO70000SX<MANUAL>
            - ERRORDetector:STOPWHEN?
            ```

        Info:
            - ``MANUAL`` indicates that the test must be stopped by issuing a TEST STOP command.
              This is the default.
            - ``COUNT`` stops the test when ``DURATION:COUNT`` comparisons are made. The comparisons
              can be bit, frame, symbol, or character as appropriate for the ``TEST:TYPE``.
            - ``TIME`` stops the test when ``DURATION:TIME`` elapses.
            - ``ERROR`` stops the test when the number of errors ≥ ERRORLIMIT.
        """
        return self._stopwhen

    @property
    def symbol(self) -> ErrordetectorSymbol:
        """Return the ``ERRORDetector:SYMBOL`` command.

        Description:
            - This command queries all symbol error settings, status, and results.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:SYMBOL?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:SYMBOL?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ERRORDetector:SYMBOL?
            ```

        Sub-properties:
            - ``.test``: The ``ERRORDetector:SYMBOL:TEST`` command.
        """
        return self._symbol

    @property
    def timeformat(self) -> ErrordetectorTimeformat:
        """Return the ``ERRORDetector:TIMEformat`` command.

        Description:
            - This command sets or queries error detector Elapsed Time Format as DDHHMMSS or
              Seconds.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:TIMEformat?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:TIMEformat?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:TIMEformat value``
              command.

        SCPI Syntax:
            ```
            - ERRORDetector:TIMEformat {DDHHMMSS|SECONDS}
            - ERRORDetector:TIMEformat?
            ```
        """
        return self._timeformat

    @property
    def type(self) -> ErrordetectorType:
        """Return the ``ERRORDetector:TYPe`` command.

        Description:
            - This command sets or queries the error detector type.

        Usage:
            - Using the ``.query()`` method will send the ``ERRORDetector:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``ERRORDetector:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ERRORDetector:TYPe value`` command.

        SCPI Syntax:
            ```
            - ERRORDetector:TYPe {BIT|FRAME|SYMBOL|CHARACTER|PRBS7|PRBS9}
            - ERRORDetector:TYPe?
            ```

        Info:
            - ``BIT`` sets the error detector type to bit.
            - ``FRAME`` sets the error detector type to frame.
            - ``SYMBOL`` sets the error detector type to symbol.
            - ``CHARACTER`` sets the error detector type to character.
            - ``PRBS7`` sets the error detector type to PRBS7.
            - ``PRBS9`` sets the error detector type to PRBS9.
        """
        return self._type
