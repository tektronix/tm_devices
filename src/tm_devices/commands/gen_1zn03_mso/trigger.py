# pylint: disable=line-too-long
"""The trigger commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TRIGger FORCe
    - TRIGger:A SETLevel
    - TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATa|IDANDDATA|EOF|ERRor|FDBITS}
    - TRIGger:A:BUS:B<x>:CAN:CONDition?
    - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection {READ|WRITE|NOCARE}
    - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?
    - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet <NR1>
    - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?
    - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual}
    - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
    - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:CAN:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:CAN:DATa:VALue?
    - TRIGger:A:BUS:B<x>:CAN:ERRType {ACKMISS|BITSTUFFing|FORMERRor|ANYERRor}
    - TRIGger:A:BUS:B<x>:CAN:ERRType?
    - TRIGger:A:BUS:B<x>:CAN:FD:BRSBit {ONE|ZERo|NOCARE}
    - TRIGger:A:BUS:B<x>:CAN:FD:BRSBit?
    - TRIGger:A:BUS:B<x>:CAN:FD:ESIBit {ONE|ZERo|NOCARE}
    - TRIGger:A:BUS:B<x>:CAN:FD:ESIBit?
    - TRIGger:A:BUS:B<x>:CAN:FRAMEtype {DATa|REMote|ERRor|OVERLoad}
    - TRIGger:A:BUS:B<x>:CAN:FRAMEtype?
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTended}
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue <QString>
    - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?
    - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe {ADDR7|ADDR10}
    - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?
    - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue <QString>
    - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?
    - TRIGger:A:BUS:B<x>:I2C:CONDition {STARt|STOP|REPEATstart|ACKMISS|ADDRess|DATa|ADDRANDDATA}
    - TRIGger:A:BUS:B<x>:I2C:CONDition?
    - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection {READ|WRITE|NOCARE}
    - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?
    - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:I2C:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:I2C:DATa:VALue?
    - TRIGger:A:BUS:B<x>:LIN:CONDition {SYNCfield|IDentifier|DATa|IDANDDATA|WAKEup|SLEEP|ERRor}
    - TRIGger:A:BUS:B<x>:LIN:CONDition?
    - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?
    - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
    - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:LIN:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:LIN:DATa:VALue?
    - TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum}
    - TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
    - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue <QString>
    - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?
    - TRIGger:A:BUS:B<x>:PARallel:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:PARallel:DATa:VALue?
    - TRIGger:A:BUS:B<x>:RS232C:CONDition {STARt|EOp|DATa|PARItyerror}
    - TRIGger:A:BUS:B<x>:RS232C:CONDition?
    - TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe <NR3>
    - TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:RS232C:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:RS232C:DATa:VALue?
    - TRIGger:A:BUS:B<x>:SENT:CONDition {START|FAST|SLOW|ERRor}
    - TRIGger:A:BUS:B<x>:SENT:CONDition?
    - TRIGger:A:BUS:B<x>:SENT:ERRType CRC
    - TRIGger:A:BUS:B<x>:SENT:ERRType:CRC {FAST|SLOW}
    - TRIGger:A:BUS:B<x>:SENT:ERRType:CRC?
    - TRIGger:A:BUS:B<x>:SENT:ERRType?
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue?
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier?
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue <Qstring>
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue?
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue?
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier?
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue <Qstring>
    - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue?
    - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue?
    - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
    - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier?
    - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue <Qstring>
    - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue?
    - TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue <Qstring>
    - TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue?
    - TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue <Qstring>
    - TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue?
    - TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|Inrange|OUTrange}
    - TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier?
    - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue <QString>
    - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue?
    - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INRange|OUTRange}
    - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier?
    - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue <Qstring>
    - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue?
    - TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue <Qstring>
    - TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue?
    - TRIGger:A:BUS:B<x>:SPI:CONDition {SS|STARTofframe|DATa}
    - TRIGger:A:BUS:B<x>:SPI:CONDition?
    - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe <NR1>
    - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?
    - TRIGger:A:BUS:B<x>:SPI:DATa:VALue <QString>
    - TRIGger:A:BUS:B<x>:SPI:DATa:VALue?
    - TRIGger:A:BUS:SOUrce B<x>
    - TRIGger:A:BUS:SOUrce?
    - TRIGger:A:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
    - TRIGger:A:EDGE:COUPling?
    - TRIGger:A:EDGE:SLOpe {RISe|FALL|EITher}
    - TRIGger:A:EDGE:SLOpe?
    - TRIGger:A:EDGE:SOUrce {CH<x>|DCH<x>_D<x>|INTernal|AUXiliary}
    - TRIGger:A:EDGE:SOUrce?
    - TRIGger:A:HOLDoff:TIMe <NR3>
    - TRIGger:A:HOLDoff:TIMe?
    - TRIGger:A:LEVel:CH<x> <NR3>
    - TRIGger:A:LEVel:CH<x>?
    - TRIGger:A:LOGICPattern:CH<x> {HIGH|LOW|X}
    - TRIGger:A:LOGICPattern:CH<x>?
    - TRIGger:A:LOGICPattern:DCH<x>_D<x> {HIGH|LOW|X}
    - TRIGger:A:LOGICPattern:DCH<x>_D<x>?
    - TRIGger:A:LOGIc:DELTatime <NR3>
    - TRIGger:A:LOGIc:DELTatime?
    - TRIGger:A:LOGIc:FUNCtion {AND|NANd|NOR|OR}
    - TRIGger:A:LOGIc:FUNCtion?
    - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>}
    - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
    - TRIGger:A:LOGIc:POLarity {POSitive|NEGative|EITher}
    - TRIGger:A:LOGIc:POLarity?
    - TRIGger:A:LOGIc:USECLockedge {OFF|ON|0|1|<NR1>}
    - TRIGger:A:LOGIc:USECLockedge?
    - TRIGger:A:LOGIc:WHEn {TRUe|FALSe|MOREThan|LESSThan|EQual|UNEQual}
    - TRIGger:A:LOGIc:WHEn?
    - TRIGger:A:LOWerthreshold:CH<x> <NR3>
    - TRIGger:A:LOWerthreshold:CH<x>?
    - TRIGger:A:MODe {AUTO|NORMal}
    - TRIGger:A:MODe?
    - TRIGger:A:PULSEWidth:HIGHLimit <NR3>
    - TRIGger:A:PULSEWidth:HIGHLimit?
    - TRIGger:A:PULSEWidth:LOWLimit <NR3>
    - TRIGger:A:PULSEWidth:LOWLimit?
    - TRIGger:A:PULSEWidth:POLarity {NEGative|POSitive}
    - TRIGger:A:PULSEWidth:POLarity?
    - TRIGger:A:PULSEWidth:SOUrce {CH<x>|DCH<x>_D<x>}
    - TRIGger:A:PULSEWidth:SOUrce?
    - TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual|WIThin|OUTside}
    - TRIGger:A:PULSEWidth:WHEn?
    - TRIGger:A:RUNT:POLarity {EITher|NEGative|POSitive}
    - TRIGger:A:RUNT:POLarity?
    - TRIGger:A:RUNT:SOUrce {CH<x>}
    - TRIGger:A:RUNT:SOUrce?
    - TRIGger:A:RUNT:WHEn {LESSthan|MOREthan|EQual|UNEQual|OCCURS}
    - TRIGger:A:RUNT:WHEn?
    - TRIGger:A:RUNT:WIDth <NR3>
    - TRIGger:A:RUNT:WIDth?
    - TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x> {INCLude|DONTInclude}
    - TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x>?
    - TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
    - TRIGger:A:SETHold:CLOCk:EDGE?
    - TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>}
    - TRIGger:A:SETHold:CLOCk:SOUrce?
    - TRIGger:A:SETHold:HOLDTime <NR3>
    - TRIGger:A:SETHold:HOLDTime?
    - TRIGger:A:SETHold:SETTime <NR3>
    - TRIGger:A:SETHold:SETTime?
    - TRIGger:A:TIMEOut:POLarity {STAYSHigh|STAYSLow|EITher}
    - TRIGger:A:TIMEOut:POLarity?
    - TRIGger:A:TIMEOut:SOUrce {CH<x>|DCH<x>_D<x>}
    - TRIGger:A:TIMEOut:SOUrce?
    - TRIGger:A:TIMEOut:TIMe <NR3>
    - TRIGger:A:TIMEOut:TIMe?
    - TRIGger:A:TYPe {EDGE|WIDth|RISE|FALL|TIMEOut|RUNt|LOGIc|SETHold|BUS}
    - TRIGger:A:TYPe?
    - TRIGger:A:UPPerthreshold:CH<x> <NR3>
    - TRIGger:A:UPPerthreshold:CH<x>?
    - TRIGger:A?
    - TRIGger:AUXLevel {<NR3>|ECL|TTL}
    - TRIGger:AUXLevel?
    - TRIGger:HYSTeresis:USER:STATe {ON|OFF|1|0}
    - TRIGger:HYSTeresis:USER:STATe?
    - TRIGger:HYSTeresis:USER:VALue <NR1>
    - TRIGger:HYSTeresis:USER:VALue?
    - TRIGger:STATE?
    - TRIGger?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedChannel,
    ValidatedDigitalBit,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class TriggerState(SCPICmdRead):
    """The ``TRIGger:STATE`` command.

    Description:
        - This query-only command returns the current state of the triggering system.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TRIGger:STATE?
        ```
    """


class TriggerHysteresisUserValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:HYSTeresis:USER:VALue`` command.

    Description:
        - This command sets or returns the height of the user-defined trigger hysteresis zone in
          volts.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:HYSTeresis:USER:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:HYSTeresis:USER:VALue?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:HYSTeresis:USER:VALue value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:HYSTeresis:USER:VALue <NR1>
        - TRIGger:HYSTeresis:USER:VALue?
        ```

    Info:
        - ``<NR1>`` sets the height of the hysteresis zone in volts.
    """


class TriggerHysteresisUserState(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:HYSTeresis:USER:STATe`` command.

    Description:
        - This command enables or disables user-defined trigger hysteresis.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:HYSTeresis:USER:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:HYSTeresis:USER:STATe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:HYSTeresis:USER:STATe value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:HYSTeresis:USER:STATe {ON|OFF|1|0}
        - TRIGger:HYSTeresis:USER:STATe?
        ```

    Info:
        - ``ON`` enables user-defined trigger hysteresis.
        - ``OFF`` disables user-defined trigger hysteresis.
        - ``1`` enables user-defined trigger hysteresis.
        - ``0`` disables user-defined trigger hysteresis.
    """


class TriggerHysteresisUser(SCPICmdRead):
    """The ``TRIGger:HYSTeresis:USER`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:HYSTeresis:USER?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:HYSTeresis:USER?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``TRIGger:HYSTeresis:USER:STATe`` command.
        - ``.value``: The ``TRIGger:HYSTeresis:USER:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = TriggerHysteresisUserState(device, f"{self._cmd_syntax}:STATe")
        self._value = TriggerHysteresisUserValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def state(self) -> TriggerHysteresisUserState:
        """Return the ``TRIGger:HYSTeresis:USER:STATe`` command.

        Description:
            - This command enables or disables user-defined trigger hysteresis.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:HYSTeresis:USER:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:HYSTeresis:USER:STATe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:HYSTeresis:USER:STATe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:HYSTeresis:USER:STATe {ON|OFF|1|0}
            - TRIGger:HYSTeresis:USER:STATe?
            ```

        Info:
            - ``ON`` enables user-defined trigger hysteresis.
            - ``OFF`` disables user-defined trigger hysteresis.
            - ``1`` enables user-defined trigger hysteresis.
            - ``0`` disables user-defined trigger hysteresis.
        """
        return self._state

    @property
    def value(self) -> TriggerHysteresisUserValue:
        """Return the ``TRIGger:HYSTeresis:USER:VALue`` command.

        Description:
            - This command sets or returns the height of the user-defined trigger hysteresis zone in
              volts.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:HYSTeresis:USER:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:HYSTeresis:USER:VALue?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:HYSTeresis:USER:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:HYSTeresis:USER:VALue <NR1>
            - TRIGger:HYSTeresis:USER:VALue?
            ```

        Info:
            - ``<NR1>`` sets the height of the hysteresis zone in volts.
        """
        return self._value


class TriggerHysteresis(SCPICmdRead):
    """The ``TRIGger:HYSTeresis`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:HYSTeresis?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:HYSTeresis?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.user``: The ``TRIGger:HYSTeresis:USER`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._user = TriggerHysteresisUser(device, f"{self._cmd_syntax}:USER")

    @property
    def user(self) -> TriggerHysteresisUser:
        """Return the ``TRIGger:HYSTeresis:USER`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:HYSTeresis:USER?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:HYSTeresis:USER?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``TRIGger:HYSTeresis:USER:STATe`` command.
            - ``.value``: The ``TRIGger:HYSTeresis:USER:VALue`` command.
        """
        return self._user


class TriggerAuxlevel(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:AUXLevel`` command.

    Description:
        - For those instruments that have an Auxiliary Input (such as an MSO58LP), this command sets
          or queries the Auxiliary Input voltage level to use for an edge trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:AUXLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:AUXLevel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:AUXLevel value`` command.

    SCPI Syntax:
        ```
        - TRIGger:AUXLevel {<NR3>|ECL|TTL}
        - TRIGger:AUXLevel?
        ```

    Info:
        - ``<NR3>`` is trigger level in Volts.
        - ``ECL`` sets trigger level to -1.3 Volts.
        - ``TTL`` sets trigger level to 1.4 Volts.
    """


class TriggerAUpperthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:UPPerthreshold:CH<x>`` command.

    Description:
        - This command sets or queries the specified channel upper trigger level. The CH<x> range is
          1 to 4 and depends on the number of analog channels on your instrument.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:UPPerthreshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:UPPerthreshold:CH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:UPPerthreshold:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:UPPerthreshold:CH<x> <NR3>
        - TRIGger:A:UPPerthreshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` specifies the trigger level in user units (usually volts).
    """


class TriggerAUpperthreshold(SCPICmdRead):
    """The ``TRIGger:A:UPPerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:UPPerthreshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:UPPerthreshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:A:UPPerthreshold:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerAUpperthresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerAUpperthresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerAUpperthresholdChannel]:
        """Return the ``TRIGger:A:UPPerthreshold:CH<x>`` command.

        Description:
            - This command sets or queries the specified channel upper trigger level. The CH<x>
              range is 1 to 4 and depends on the number of analog channels on your instrument.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:UPPerthreshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:UPPerthreshold:CH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:UPPerthreshold:CH<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:UPPerthreshold:CH<x> <NR3>
            - TRIGger:A:UPPerthreshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` specifies the trigger level in user units (usually volts).
        """
        return self._ch


class TriggerAType(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TYPe`` command.

    Description:
        - This command sets or queries the type of A trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TYPe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:TYPe {EDGE|WIDth|RISE|FALL|TIMEOut|RUNt|LOGIc|SETHold|BUS}
        - TRIGger:A:TYPe?
        ```

    Info:
        - ``EDGE`` is a normal trigger. A trigger event occurs when a signal passes through a
          specified voltage level in a specified direction and is controlled by the
          ``TRIGger:A:EDGE`` commands.
        - ``WIDth`` specifies that the trigger occurs when a pulse with a specified width is found.
        - ``RISE`` specifies that the trigger occurs when a pulse with a specified rise is found.
        - ``FALL`` specifies that the trigger occurs when a pulse with a specified fall is found.
        - ``TIMEOut`` specifies that a trigger occurs when a pulse with the specified timeout is
          found.
        - ``RUNt`` specifies that a trigger occurs when a pulse with the specified parameters is
          found.
        - ``LOGIc`` specifies that a trigger occurs when specified conditions are met and is
          controlled by the ``TRIGger:A:LOGIc`` commands.
        - ``SETHold`` specifies that a trigger occurs when a signal is found that meets the setup
          and hold parameters.
        - ``BUS`` specifies that a trigger occurs when a signal is found that meets the specified
          bus setup parameters.
    """


class TriggerATimeoutTime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TIMEOut:TIMe`` command.

    Description:
        - When triggering using the TIMEOut trigger type, this command specifies the timeout time,
          in seconds. This command is equivalent to selecting Timeout from the Trig menu and setting
          a value for Time Limit. The timeout trigger type is selected using
          ``TRIGGER:A:TYPE TIMEOut``

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:TIMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:TIMe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:TIMEOut:TIMe <NR3>
        - TRIGger:A:TIMEOut:TIMe?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the timeout time, in seconds.
    """


class TriggerATimeoutSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TIMEOut:SOUrce`` command.

    Description:
        - When triggering using the TIMEOut trigger type, this command specifies the source. The
          available sources are live channels and digital channels. The default is channel 1. The
          timeout trigger type is selected using ``TRIGGER:A:TYPE TIMEOut``.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:TIMEOut:SOUrce {CH<x>|DCH<x>_D<x>}
        - TRIGger:A:TIMEOut:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the timeout trigger source.
        - ``DCH<x>_D<x>`` specifies a digital channel as the timeout trigger source. The supported
          digital channel value is 1. The supported digital bit values are 0 to 15.
    """


class TriggerATimeoutPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:TIMEOut:POLarity`` command.

    Description:
        - When triggering using the TIMEOut trigger type, this commands specifies the polarity to be
          used.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:TIMEOut:POLarity {STAYSHigh|STAYSLow|EITher}
        - TRIGger:A:TIMEOut:POLarity?
        ```

    Info:
        - ``STAYSHigh`` . Trigger when the signal stays high during the timeout time specified by
          the command ``TRIGGER:A:TIMEOUT:TIME``.
        - ``STAYSLow`` . Trigger when the signal stays low during the timeout time specified by the
          command ``TRIGGER:A:TIMEOUT:TIME``.
        - ``EITher`` . Trigger when the signal is either high or low during the timeout time
          specified by the command ``TRIGGER:A:TIMEOUT:TIME``.
    """


class TriggerATimeout(SCPICmdRead):
    """The ``TRIGger:A:TIMEOut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``TRIGger:A:TIMEOut:POLarity`` command.
        - ``.source``: The ``TRIGger:A:TIMEOut:SOUrce`` command.
        - ``.time``: The ``TRIGger:A:TIMEOut:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = TriggerATimeoutPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = TriggerATimeoutSource(device, f"{self._cmd_syntax}:SOUrce")
        self._time = TriggerATimeoutTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def polarity(self) -> TriggerATimeoutPolarity:
        """Return the ``TRIGger:A:TIMEOut:POLarity`` command.

        Description:
            - When triggering using the TIMEOut trigger type, this commands specifies the polarity
              to be used.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:POLarity value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:TIMEOut:POLarity {STAYSHigh|STAYSLow|EITher}
            - TRIGger:A:TIMEOut:POLarity?
            ```

        Info:
            - ``STAYSHigh`` . Trigger when the signal stays high during the timeout time specified
              by the command ``TRIGGER:A:TIMEOUT:TIME``.
            - ``STAYSLow`` . Trigger when the signal stays low during the timeout time specified by
              the command ``TRIGGER:A:TIMEOUT:TIME``.
            - ``EITher`` . Trigger when the signal is either high or low during the timeout time
              specified by the command ``TRIGGER:A:TIMEOUT:TIME``.
        """
        return self._polarity

    @property
    def source(self) -> TriggerATimeoutSource:
        """Return the ``TRIGger:A:TIMEOut:SOUrce`` command.

        Description:
            - When triggering using the TIMEOut trigger type, this command specifies the source. The
              available sources are live channels and digital channels. The default is channel 1.
              The timeout trigger type is selected using ``TRIGGER:A:TYPE TIMEOut``.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:TIMEOut:SOUrce {CH<x>|DCH<x>_D<x>}
            - TRIGger:A:TIMEOut:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the timeout trigger source.
            - ``DCH<x>_D<x>`` specifies a digital channel as the timeout trigger source. The
              supported digital channel value is 1. The supported digital bit values are 0 to 15.
        """
        return self._source

    @property
    def time(self) -> TriggerATimeoutTime:
        """Return the ``TRIGger:A:TIMEOut:TIMe`` command.

        Description:
            - When triggering using the TIMEOut trigger type, this command specifies the timeout
              time, in seconds. This command is equivalent to selecting Timeout from the Trig menu
              and setting a value for Time Limit. The timeout trigger type is selected using
              ``TRIGGER:A:TYPE TIMEOut``

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut:TIMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TIMEOut:TIMe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:TIMEOut:TIMe <NR3>
            - TRIGger:A:TIMEOut:TIMe?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the timeout time, in seconds.
        """
        return self._time


class TriggerASetholdSettime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:SETTime`` command.

    Description:
        - This command specifies the setup time for setup and hold violation triggering. This
          command is equivalent to selecting Setup/Hold Setup from the Trig menu and then setting
          the desired Setup Time.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:SETTime?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:SETTime?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:SETTime value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:SETTime <NR3>
        - TRIGger:A:SETHold:SETTime?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the setup time for setup and hold
          violation triggering.
    """


class TriggerASetholdHoldtime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:HOLDTime`` command.

    Description:
        - This command specifies the hold time for setup and hold violation triggering. This command
          is equivalent to selecting Setup/Hold Setup from the Trig menu and then setting the
          desired Hold Time.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:HOLDTime?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:HOLDTime?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:HOLDTime value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:HOLDTime <NR3>
        - TRIGger:A:SETHold:HOLDTime?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the hold time setting, in seconds.
          Positive values for hold time occur after the clock edge. Negative values occur before the
          clock edge.
    """


class TriggerASetholdClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:CLOCk:SOUrce`` command.

    Description:
        - This command specifies the clock source for the setup and hold triggering. You cannot
          specify the same source for both clock and data.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>}
        - TRIGger:A:SETHold:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the analog channel to use as the clock source waveform.
        - ``DCH<x>_D<x>`` specifies the digital channel to use as the clock source waveform. The
          supported digital channel value is 1. The supported digital bit values are 0 to 15.
    """


class TriggerASetholdClockEdge(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHold:CLOCk:EDGE`` command.

    Description:
        - This command specifies the clock edge polarity for setup and hold triggering.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:EDGE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:EDGE value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
        - TRIGger:A:SETHold:CLOCk:EDGE?
        ```

    Info:
        - ``FALL`` specifies polarity as the clock falling edge.
        - ``RISe`` specifies polarity as the clock rising edge.
    """


class TriggerASetholdClock(SCPICmdRead):
    """The ``TRIGger:A:SETHold:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``TRIGger:A:SETHold:CLOCk:EDGE`` command.
        - ``.source``: The ``TRIGger:A:SETHold:CLOCk:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = TriggerASetholdClockEdge(device, f"{self._cmd_syntax}:EDGE")
        self._source = TriggerASetholdClockSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def edge(self) -> TriggerASetholdClockEdge:
        """Return the ``TRIGger:A:SETHold:CLOCk:EDGE`` command.

        Description:
            - This command specifies the clock edge polarity for setup and hold triggering.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:EDGE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHold:CLOCk:EDGE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:CLOCk:EDGE {FALL|RISe}
            - TRIGger:A:SETHold:CLOCk:EDGE?
            ```

        Info:
            - ``FALL`` specifies polarity as the clock falling edge.
            - ``RISe`` specifies polarity as the clock rising edge.
        """
        return self._edge

    @property
    def source(self) -> TriggerASetholdClockSource:
        """Return the ``TRIGger:A:SETHold:CLOCk:SOUrce`` command.

        Description:
            - This command specifies the clock source for the setup and hold triggering. You cannot
              specify the same source for both clock and data.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHold:CLOCk:SOUrce value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>}
            - TRIGger:A:SETHold:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the analog channel to use as the clock source waveform.
            - ``DCH<x>_D<x>`` specifies the digital channel to use as the clock source waveform. The
              supported digital channel value is 1. The supported digital bit values are 0 to 15.
        """
        return self._source


class TriggerASethold(SCPICmdRead):
    """The ``TRIGger:A:SETHold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clock``: The ``TRIGger:A:SETHold:CLOCk`` command tree.
        - ``.holdtime``: The ``TRIGger:A:SETHold:HOLDTime`` command.
        - ``.settime``: The ``TRIGger:A:SETHold:SETTime`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = TriggerASetholdClock(device, f"{self._cmd_syntax}:CLOCk")
        self._holdtime = TriggerASetholdHoldtime(device, f"{self._cmd_syntax}:HOLDTime")
        self._settime = TriggerASetholdSettime(device, f"{self._cmd_syntax}:SETTime")

    @property
    def clock(self) -> TriggerASetholdClock:
        """Return the ``TRIGger:A:SETHold:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:CLOCk?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``TRIGger:A:SETHold:CLOCk:EDGE`` command.
            - ``.source``: The ``TRIGger:A:SETHold:CLOCk:SOUrce`` command.
        """
        return self._clock

    @property
    def holdtime(self) -> TriggerASetholdHoldtime:
        """Return the ``TRIGger:A:SETHold:HOLDTime`` command.

        Description:
            - This command specifies the hold time for setup and hold violation triggering. This
              command is equivalent to selecting Setup/Hold Setup from the Trig menu and then
              setting the desired Hold Time.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:HOLDTime?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:HOLDTime?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:HOLDTime value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:HOLDTime <NR3>
            - TRIGger:A:SETHold:HOLDTime?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the hold time setting, in seconds.
              Positive values for hold time occur after the clock edge. Negative values occur before
              the clock edge.
        """
        return self._holdtime

    @property
    def settime(self) -> TriggerASetholdSettime:
        """Return the ``TRIGger:A:SETHold:SETTime`` command.

        Description:
            - This command specifies the setup time for setup and hold violation triggering. This
              command is equivalent to selecting Setup/Hold Setup from the Trig menu and then
              setting the desired Setup Time.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold:SETTime?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold:SETTime?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:SETHold:SETTime value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHold:SETTime <NR3>
            - TRIGger:A:SETHold:SETTime?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the setup time for setup and hold
              violation triggering.
        """
        return self._settime


class TriggerASetholdlogicvalDchItemDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x>`` command.

    Description:
        - This command sets or queries the conditions used for generating an A logic pattern, with
          respect to the defined input pattern, and identifies the time that the selected pattern
          may be true and still generate the trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x> {INCLude|DONTInclude}
        - TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x>?
        ```

    Info:
        - ``DCH<x>_D<x>`` specifies the digital channel to use as the clock source waveform. The
          supported digital channel value is 1. The supported digital bit values are 0 to 15.
        - ``INCLude`` specifies including the specified digital channel SETHOLD inputs.
        - ``DONTInclude`` specifies not including the specified digital channel SETHOLD inputs.
    """


class TriggerASetholdlogicvalDchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.d``: The ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, TriggerASetholdlogicvalDchItemDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerASetholdlogicvalDchItemDigitalBit(device, f"{self._cmd_syntax}_D{x}")
        )

    @property
    def d(self) -> Dict[int, TriggerASetholdlogicvalDchItemDigitalBit]:
        """Return the ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x>`` command.

        Description:
            - This command sets or queries the conditions used for generating an A logic pattern,
              with respect to the defined input pattern, and identifies the time that the selected
              pattern may be true and still generate the trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x> {INCLude|DONTInclude}
            - TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x>?
            ```

        Info:
            - ``DCH<x>_D<x>`` specifies the digital channel to use as the clock source waveform. The
              supported digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``INCLude`` specifies including the specified digital channel SETHOLD inputs.
            - ``DONTInclude`` specifies not including the specified digital channel SETHOLD inputs.
        """
        return self._d


class TriggerASetholdlogicval(SCPICmdRead):
    """The ``TRIGger:A:SETHOLDLOGICVAL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:SETHOLDLOGICVAL?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHOLDLOGICVAL?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dch``: The ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dch: Dict[int, TriggerASetholdlogicvalDchItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerASetholdlogicvalDchItem(device, f"{self._cmd_syntax}:DCH{x}")
        )

    @property
    def dch(self) -> Dict[int, TriggerASetholdlogicvalDchItem]:
        """Return the ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.d``: The ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>_D<x>`` command.
        """
        return self._dch


class TriggerARuntWidth(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RUNT:WIDth`` command.

    Description:
        - This command specifies the width, in seconds, for a runt trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:WIDth?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:WIDth value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:RUNT:WIDth <NR3>
        - TRIGger:A:RUNT:WIDth?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the minimum width, in seconds.
    """


class TriggerARuntWhen(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RUNT:WHEn`` command.

    Description:
        - This command specifies the type of pulse width the trigger checks for when it detects a
          runt.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:WHEn?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:WHEn value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:RUNT:WHEn {LESSthan|MOREthan|EQual|UNEQual|OCCURS}
        - TRIGger:A:RUNT:WHEn?
        ```

    Info:
        - ``OCCURS`` sets the instrument to trigger if a runt signal of any detectable width occurs.
        - ``LESSthan`` sets the instrument to trigger if the a runt pulse is detected with width
          less than the time set by the ``TRIGGER:A:RUNT:WIDTH`` command.
        - ``MOREthan`` sets the instrument to trigger if the a runt pulse is detected with width
          greater than the time set by the ``TRIGGER:A:RUNT:WIDTH`` command.
        - ``EQual`` sets the instrument to trigger if a runt pulse is detected with width equal to
          the time period specified in ``TRIGGER:A:RUNT:WIDTH`` within a ±5% tolerance.
        - ``UNEQual`` sets the instrument to trigger if a runt pulse is detected with width greater
          than or less than (but not equal to) the time period specified in ``TRIGGER:A:RUNT:WIDTH``
          within a ±5% tolerance.
    """


class TriggerARuntSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RUNT:SOUrce`` command.

    Description:
        - This command specifies the source waveform for the runt trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:RUNT:SOUrce {CH<x>}
        - TRIGger:A:RUNT:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the analog channel number to use as the source waveform for the runt
          trigger. To specify the threshold levels when using CH<x> as the source, use
          ``TRIGGER:A:LOWERTHRESHOLD:CHX`` and ``TRIGGER:A:UPPERTHRESHOLD:CHX``.
    """


class TriggerARuntPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:RUNT:POLarity`` command.

    Description:
        - This command specifies the polarity for the runt trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:RUNT:POLarity {EITher|NEGative|POSitive}
        - TRIGger:A:RUNT:POLarity?
        ```

    Info:
        - ``POSitive`` indicates that the rising edge crosses the low threshold and the falling edge
          recrosses the low threshold without either edge ever crossing the high threshold.
        - ``NEGative`` indicates that the falling edge crosses the high threshold and the rising
          edge recrosses the high threshold without either edge ever crossing the low threshold.
        - ``EITher`` triggers on a runt of either polarity.
    """


class TriggerARunt(SCPICmdRead):
    """The ``TRIGger:A:RUNT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:RUNT?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``TRIGger:A:RUNT:POLarity`` command.
        - ``.source``: The ``TRIGger:A:RUNT:SOUrce`` command.
        - ``.when``: The ``TRIGger:A:RUNT:WHEn`` command.
        - ``.width``: The ``TRIGger:A:RUNT:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = TriggerARuntPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = TriggerARuntSource(device, f"{self._cmd_syntax}:SOUrce")
        self._when = TriggerARuntWhen(device, f"{self._cmd_syntax}:WHEn")
        self._width = TriggerARuntWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def polarity(self) -> TriggerARuntPolarity:
        """Return the ``TRIGger:A:RUNT:POLarity`` command.

        Description:
            - This command specifies the polarity for the runt trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:POLarity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:POLarity value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RUNT:POLarity {EITher|NEGative|POSitive}
            - TRIGger:A:RUNT:POLarity?
            ```

        Info:
            - ``POSitive`` indicates that the rising edge crosses the low threshold and the falling
              edge recrosses the low threshold without either edge ever crossing the high threshold.
            - ``NEGative`` indicates that the falling edge crosses the high threshold and the rising
              edge recrosses the high threshold without either edge ever crossing the low threshold.
            - ``EITher`` triggers on a runt of either polarity.
        """
        return self._polarity

    @property
    def source(self) -> TriggerARuntSource:
        """Return the ``TRIGger:A:RUNT:SOUrce`` command.

        Description:
            - This command specifies the source waveform for the runt trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RUNT:SOUrce {CH<x>}
            - TRIGger:A:RUNT:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the analog channel number to use as the source waveform for the
              runt trigger. To specify the threshold levels when using CH<x> as the source, use
              ``TRIGGER:A:LOWERTHRESHOLD:CHX`` and ``TRIGGER:A:UPPERTHRESHOLD:CHX``.
        """
        return self._source

    @property
    def when(self) -> TriggerARuntWhen:
        """Return the ``TRIGger:A:RUNT:WHEn`` command.

        Description:
            - This command specifies the type of pulse width the trigger checks for when it detects
              a runt.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:WHEn?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:WHEn value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RUNT:WHEn {LESSthan|MOREthan|EQual|UNEQual|OCCURS}
            - TRIGger:A:RUNT:WHEn?
            ```

        Info:
            - ``OCCURS`` sets the instrument to trigger if a runt signal of any detectable width
              occurs.
            - ``LESSthan`` sets the instrument to trigger if the a runt pulse is detected with width
              less than the time set by the ``TRIGGER:A:RUNT:WIDTH`` command.
            - ``MOREthan`` sets the instrument to trigger if the a runt pulse is detected with width
              greater than the time set by the ``TRIGGER:A:RUNT:WIDTH`` command.
            - ``EQual`` sets the instrument to trigger if a runt pulse is detected with width equal
              to the time period specified in ``TRIGGER:A:RUNT:WIDTH`` within a ±5% tolerance.
            - ``UNEQual`` sets the instrument to trigger if a runt pulse is detected with width
              greater than or less than (but not equal to) the time period specified in
              ``TRIGGER:A:RUNT:WIDTH`` within a ±5% tolerance.
        """
        return self._when

    @property
    def width(self) -> TriggerARuntWidth:
        """Return the ``TRIGger:A:RUNT:WIDth`` command.

        Description:
            - This command specifies the width, in seconds, for a runt trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RUNT:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT:WIDth?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:RUNT:WIDth value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:RUNT:WIDth <NR3>
            - TRIGger:A:RUNT:WIDth?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the minimum width, in seconds.
        """
        return self._width


class TriggerAPulsewidthWhen(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:WHEn`` command.

    Description:
        - This command specifies to trigger when a pulse is detected with a width (duration) that is
          less than, greater than, equal to, or unequal to a specified value (set using
          ``TRIGGER:A:PULSEWIDTH:LOWLIMIT``), OR whose width falls outside of or within a specified
          range of two values (set using ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` and
          ``TRIGGER:A:PULSEWIDTH:HIGHLIMIT``).

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual|WIThin|OUTside}
        - TRIGger:A:PULSEWidth:WHEn?
        ```

    Info:
        - ``LESSthan`` causes a trigger when a pulse is detected with a width less than the time set
          by the ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` command.
        - ``MOREthan`` causes a trigger when a pulse is detected with a width greater than the time
          set by the ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` command.
        - ``EQual`` causes a trigger when a pulse is detected with a width equal to the time period
          specified in ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` within a ±5% tolerance.
        - ``UNEQual`` causes a trigger when a pulse is detected with a width greater than or less
          than (but not equal) the time period specified in ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` within
          a ±5% tolerance.
        - ``WIThin`` causes a trigger when a pulse is detected that is within a range set by two
          values.
        - ``OUTside`` causes a trigger when a pulse is detected that is outside of a range set by
          two values.
    """


class TriggerAPulsewidthSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:SOUrce`` command.

    Description:
        - This command specifies the source waveform for a pulse width trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:SOUrce {CH<x>|DCH<x>_D<x>}
        - TRIGger:A:PULSEWidth:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog input channel as the pulse-width trigger source.
        - ``DCH<x>_D<x>`` specifies an digital input channel as the pulse-width trigger source. The
          supported digital channel value is 1. The supported digital bit values are 0 to 15.
    """


class TriggerAPulsewidthPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:POLarity`` command.

    Description:
        - This command specifies the polarity for a pulse width trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:POLarity {NEGative|POSitive}
        - TRIGger:A:PULSEWidth:POLarity?
        ```

    Info:
        - ``NEGative`` specifies a negative pulse.
        - ``POSitive`` specifies a positive pulse.
    """


class TriggerAPulsewidthLowlimit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:LOWLimit`` command.

    Description:
        - This command specifies the lower limit to use, in seconds, when triggering on detection of
          a pulse whose duration is inside or outside a range of two values. (Use
          ``TRIGGER:A:PULSEWIDTH:HIGHLIMIT`` to specify the upper limit of the range.) This command
          also specifies the single limit to use, in seconds, when triggering on detection of a
          pulse whose duration is less than, greater than, equal to, or not equal to this time
          limit.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:LOWLimit?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:LOWLimit?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:LOWLimit value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:LOWLimit <NR3>
        - TRIGger:A:PULSEWidth:LOWLimit?
        ```

    Info:
        - ``<NR3>`` is a floating point number that represents the lower value of the range.
    """


class TriggerAPulsewidthHighlimit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth:HIGHLimit`` command.

    Description:
        - This command specifies the upper limit to use, in seconds, when triggering on detection of
          a pulse whose duration is inside or outside a range of two values. (Use
          ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` to specify the lower value of the range.)

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:HIGHLimit?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:HIGHLimit?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:HIGHLimit value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:PULSEWidth:HIGHLimit <NR3>
        - TRIGger:A:PULSEWidth:HIGHLimit?
        ```

    Info:
        - ``<NR3>`` is a floating point number that represents the higher value of the range.
    """


class TriggerAPulsewidth(SCPICmdRead):
    """The ``TRIGger:A:PULSEWidth`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.highlimit``: The ``TRIGger:A:PULSEWidth:HIGHLimit`` command.
        - ``.lowlimit``: The ``TRIGger:A:PULSEWidth:LOWLimit`` command.
        - ``.polarity``: The ``TRIGger:A:PULSEWidth:POLarity`` command.
        - ``.source``: The ``TRIGger:A:PULSEWidth:SOUrce`` command.
        - ``.when``: The ``TRIGger:A:PULSEWidth:WHEn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._highlimit = TriggerAPulsewidthHighlimit(device, f"{self._cmd_syntax}:HIGHLimit")
        self._lowlimit = TriggerAPulsewidthLowlimit(device, f"{self._cmd_syntax}:LOWLimit")
        self._polarity = TriggerAPulsewidthPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = TriggerAPulsewidthSource(device, f"{self._cmd_syntax}:SOUrce")
        self._when = TriggerAPulsewidthWhen(device, f"{self._cmd_syntax}:WHEn")

    @property
    def highlimit(self) -> TriggerAPulsewidthHighlimit:
        """Return the ``TRIGger:A:PULSEWidth:HIGHLimit`` command.

        Description:
            - This command specifies the upper limit to use, in seconds, when triggering on
              detection of a pulse whose duration is inside or outside a range of two values. (Use
              ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` to specify the lower value of the range.)

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:HIGHLimit?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:HIGHLimit?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:PULSEWidth:HIGHLimit value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:HIGHLimit <NR3>
            - TRIGger:A:PULSEWidth:HIGHLimit?
            ```

        Info:
            - ``<NR3>`` is a floating point number that represents the higher value of the range.
        """
        return self._highlimit

    @property
    def lowlimit(self) -> TriggerAPulsewidthLowlimit:
        """Return the ``TRIGger:A:PULSEWidth:LOWLimit`` command.

        Description:
            - This command specifies the lower limit to use, in seconds, when triggering on
              detection of a pulse whose duration is inside or outside a range of two values. (Use
              ``TRIGGER:A:PULSEWIDTH:HIGHLIMIT`` to specify the upper limit of the range.) This
              command also specifies the single limit to use, in seconds, when triggering on
              detection of a pulse whose duration is less than, greater than, equal to, or not equal
              to this time limit.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:LOWLimit?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:LOWLimit?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:PULSEWidth:LOWLimit value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:LOWLimit <NR3>
            - TRIGger:A:PULSEWidth:LOWLimit?
            ```

        Info:
            - ``<NR3>`` is a floating point number that represents the lower value of the range.
        """
        return self._lowlimit

    @property
    def polarity(self) -> TriggerAPulsewidthPolarity:
        """Return the ``TRIGger:A:PULSEWidth:POLarity`` command.

        Description:
            - This command specifies the polarity for a pulse width trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:PULSEWidth:POLarity value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:POLarity {NEGative|POSitive}
            - TRIGger:A:PULSEWidth:POLarity?
            ```

        Info:
            - ``NEGative`` specifies a negative pulse.
            - ``POSitive`` specifies a positive pulse.
        """
        return self._polarity

    @property
    def source(self) -> TriggerAPulsewidthSource:
        """Return the ``TRIGger:A:PULSEWidth:SOUrce`` command.

        Description:
            - This command specifies the source waveform for a pulse width trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:SOUrce {CH<x>|DCH<x>_D<x>}
            - TRIGger:A:PULSEWidth:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog input channel as the pulse-width trigger source.
            - ``DCH<x>_D<x>`` specifies an digital input channel as the pulse-width trigger source.
              The supported digital channel value is 1. The supported digital bit values are 0 to
              15.
        """
        return self._source

    @property
    def when(self) -> TriggerAPulsewidthWhen:
        """Return the ``TRIGger:A:PULSEWidth:WHEn`` command.

        Description:
            - This command specifies to trigger when a pulse is detected with a width (duration)
              that is less than, greater than, equal to, or unequal to a specified value (set using
              ``TRIGGER:A:PULSEWIDTH:LOWLIMIT``), OR whose width falls outside of or within a
              specified range of two values (set using ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` and
              ``TRIGGER:A:PULSEWIDTH:HIGHLIMIT``).

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:PULSEWidth:WHEn value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:PULSEWidth:WHEn {LESSthan|MOREthan|EQual|UNEQual|WIThin|OUTside}
            - TRIGger:A:PULSEWidth:WHEn?
            ```

        Info:
            - ``LESSthan`` causes a trigger when a pulse is detected with a width less than the time
              set by the ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` command.
            - ``MOREthan`` causes a trigger when a pulse is detected with a width greater than the
              time set by the ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` command.
            - ``EQual`` causes a trigger when a pulse is detected with a width equal to the time
              period specified in ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` within a ±5% tolerance.
            - ``UNEQual`` causes a trigger when a pulse is detected with a width greater than or
              less than (but not equal) the time period specified in
              ``TRIGGER:A:PULSEWIDTH:LOWLIMIT`` within a ±5% tolerance.
            - ``WIThin`` causes a trigger when a pulse is detected that is within a range set by two
              values.
            - ``OUTside`` causes a trigger when a pulse is detected that is outside of a range set
              by two values.
        """
        return self._when


class TriggerAMode(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:MODe`` command.

    Description:
        - This command sets or queries the A trigger mode. This command is equivalent to pushing the
          Mode button on the front panel.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:MODe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:MODe {AUTO|NORMal}
        - TRIGger:A:MODe?
        ```

    Info:
        - ``AUTO`` generates a trigger if one is not detected within a specified time period.
        - ``NORMal`` waits for a valid trigger event.
    """


class TriggerALowerthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOWerthreshold:CH<x>`` command.

    Description:
        - This command sets or queries the A or B lower trigger level threshold for the channel,
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:CH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOWerthreshold:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOWerthreshold:CH<x> <NR3>
        - TRIGger:A:LOWerthreshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` specifies the threshold voltage in user units.
    """


class TriggerALowerthreshold(SCPICmdRead):
    """The ``TRIGger:A:LOWerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:A:LOWerthreshold:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerALowerthresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALowerthresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerALowerthresholdChannel]:
        """Return the ``TRIGger:A:LOWerthreshold:CH<x>`` command.

        Description:
            - This command sets or queries the A or B lower trigger level threshold for the channel,
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold:CH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOWerthreshold:CH<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOWerthreshold:CH<x> <NR3>
            - TRIGger:A:LOWerthreshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` specifies the threshold voltage in user units.
        """
        return self._ch


class TriggerALogicWhen(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:WHEn`` command.

    Description:
        - This command sets or queries the condition for generating an A or B logic trigger with
          respect to the defined input pattern. This command is equivalent to selecting Logic for
          Trigger Type, Use Clock Edge to No, and choosing a trigger condition from the Logic
          Pattern drop-down list.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:WHEn?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:WHEn?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:WHEn value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:WHEn {TRUe|FALSe|MOREThan|LESSThan|EQual|UNEQual}
        - TRIGger:A:LOGIc:WHEn?
        ```

    Info:
        - ``TRUe`` triggers on an input pattern that is true.
        - ``FALSe`` triggers on an input pattern that is false.
        - ``MOREthan`` triggers on an input pattern that is true for a time period greater than a
          user defined Time Limit (DELTatime) value.
        - ``LESSthan`` triggers on an input pattern that is true for a time period less than a user
          defined Time Limit (DELTatime) value.
        - ``EQual`` triggers on an input pattern that is true for a time period equal to a user
          defined Time Limit (DELTatime) value.
        - ``UNEQual`` triggers on an input pattern that is true for a time period not equal to a
          user defined Time Limit (DELTatime) value.
    """


class TriggerALogicUseclockedge(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:USECLockedge`` command.

    Description:
        - This command specifies whether or not Logic trigger type uses clock source.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:USECLockedge?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:USECLockedge?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:USECLockedge value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:USECLockedge {OFF|ON|0|1|<NR1>}
        - TRIGger:A:LOGIc:USECLockedge?
        ```

    Info:
        - ``ON`` specifies that logic trigger type uses clock source.
        - ``1`` specifies that logic trigger type uses clock source.
        - ``OFF`` specifies that logic trigger type does not use clock source.
        - ``0`` specifies that logic trigger type does not use clock source.
        - ``<NR1>`` = 0 specifies that logic trigger type does not use clock source; any other value
          uses clock source.
    """


class TriggerALogicPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:POLarity`` command.

    Description:
        - This command sets or queries the polarity for the clock channel when Use Clock Edge is set
          to Yes for Logic trigger type.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:POLarity value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:POLarity {POSitive|NEGative|EITher}
        - TRIGger:A:LOGIc:POLarity?
        ```

    Info:
        - ``NEGative`` specifies negative polarity.
        - ``POSITIVe`` specifies positive polarity.
        - ``EITher`` specifies either polarity.
    """


class TriggerALogicInputClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.

    Description:
        - This command specifies the channel to use as the clock source for logic trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>}
        - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the clock source. Number of channels depends on
          instrument configuration.
        - ``DCH<x>_D<x>`` specifies a digital channel as the clock source. The supported digital
          channel value is 1. The supported digital bit values are 0 to 15.
    """


class TriggerALogicInputClock(SCPICmdRead):
    """The ``TRIGger:A:LOGIc:INPut:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = TriggerALogicInputClockSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> TriggerALogicInputClockSource:
        """Return the ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.

        Description:
            - This command specifies the channel to use as the clock source for logic trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>}
            - TRIGger:A:LOGIc:INPut:CLOCk:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the clock source. Number of channels depends
              on instrument configuration.
            - ``DCH<x>_D<x>`` specifies a digital channel as the clock source. The supported digital
              channel value is 1. The supported digital bit values are 0 to 15.
        """
        return self._source


class TriggerALogicInput(SCPICmdRead):
    """The ``TRIGger:A:LOGIc:INPut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clock``: The ``TRIGger:A:LOGIc:INPut:CLOCk`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = TriggerALogicInputClock(device, f"{self._cmd_syntax}:CLOCk")

    @property
    def clock(self) -> TriggerALogicInputClock:
        """Return the ``TRIGger:A:LOGIc:INPut:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut:CLOCk?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``TRIGger:A:LOGIc:INPut:CLOCk:SOUrce`` command.
        """
        return self._clock


class TriggerALogicFunction(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:FUNCtion`` command.

    Description:
        - This command sets or queries the logical combination of the input channels for logic
          triggers. This command is equivalent to selecting Logic for the Trigger Type, and setting
          or viewing the Define Logic.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:FUNCtion {AND|NANd|NOR|OR}
        - TRIGger:A:LOGIc:FUNCtion?
        ```

    Info:
        - ``AND`` specifies to trigger if all conditions are true.
        - ``NANd`` specifies to trigger if any of the conditions are false.
        - ``NOR`` specifies to trigger if all conditions are false.
        - ``OR`` specifies to trigger if any of the conditions are true.
    """


class TriggerALogicDeltatime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGIc:DELTatime`` command.

    Description:
        - This command specifies or queries the Logic trigger delta time value. The time value is
          used as part of the Logic trigger condition to determine if the duration of a logic
          pattern meets the specified time constraints.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:DELTatime?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:DELTatime?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:DELTatime value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGIc:DELTatime <NR3>
        - TRIGger:A:LOGIc:DELTatime?
        ```

    Info:
        - ``<NR3>`` the Logic trigger delta time value.
    """


class TriggerALogic(SCPICmdRead):
    """The ``TRIGger:A:LOGIc`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.deltatime``: The ``TRIGger:A:LOGIc:DELTatime`` command.
        - ``.function``: The ``TRIGger:A:LOGIc:FUNCtion`` command.
        - ``.input``: The ``TRIGger:A:LOGIc:INPut`` command tree.
        - ``.polarity``: The ``TRIGger:A:LOGIc:POLarity`` command.
        - ``.useclockedge``: The ``TRIGger:A:LOGIc:USECLockedge`` command.
        - ``.when``: The ``TRIGger:A:LOGIc:WHEn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._deltatime = TriggerALogicDeltatime(device, f"{self._cmd_syntax}:DELTatime")
        self._function = TriggerALogicFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._input = TriggerALogicInput(device, f"{self._cmd_syntax}:INPut")
        self._polarity = TriggerALogicPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._useclockedge = TriggerALogicUseclockedge(device, f"{self._cmd_syntax}:USECLockedge")
        self._when = TriggerALogicWhen(device, f"{self._cmd_syntax}:WHEn")

    @property
    def deltatime(self) -> TriggerALogicDeltatime:
        """Return the ``TRIGger:A:LOGIc:DELTatime`` command.

        Description:
            - This command specifies or queries the Logic trigger delta time value. The time value
              is used as part of the Logic trigger condition to determine if the duration of a logic
              pattern meets the specified time constraints.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:DELTatime?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:DELTatime?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:DELTatime value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:DELTatime <NR3>
            - TRIGger:A:LOGIc:DELTatime?
            ```

        Info:
            - ``<NR3>`` the Logic trigger delta time value.
        """
        return self._deltatime

    @property
    def function(self) -> TriggerALogicFunction:
        """Return the ``TRIGger:A:LOGIc:FUNCtion`` command.

        Description:
            - This command sets or queries the logical combination of the input channels for logic
              triggers. This command is equivalent to selecting Logic for the Trigger Type, and
              setting or viewing the Define Logic.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:FUNCtion value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:FUNCtion {AND|NANd|NOR|OR}
            - TRIGger:A:LOGIc:FUNCtion?
            ```

        Info:
            - ``AND`` specifies to trigger if all conditions are true.
            - ``NANd`` specifies to trigger if any of the conditions are false.
            - ``NOR`` specifies to trigger if all conditions are false.
            - ``OR`` specifies to trigger if any of the conditions are true.
        """
        return self._function

    @property
    def input(self) -> TriggerALogicInput:
        """Return the ``TRIGger:A:LOGIc:INPut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:INPut?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:INPut?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.clock``: The ``TRIGger:A:LOGIc:INPut:CLOCk`` command tree.
        """
        return self._input

    @property
    def polarity(self) -> TriggerALogicPolarity:
        """Return the ``TRIGger:A:LOGIc:POLarity`` command.

        Description:
            - This command sets or queries the polarity for the clock channel when Use Clock Edge is
              set to Yes for Logic trigger type.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:POLarity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:POLarity value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:POLarity {POSitive|NEGative|EITher}
            - TRIGger:A:LOGIc:POLarity?
            ```

        Info:
            - ``NEGative`` specifies negative polarity.
            - ``POSITIVe`` specifies positive polarity.
            - ``EITher`` specifies either polarity.
        """
        return self._polarity

    @property
    def useclockedge(self) -> TriggerALogicUseclockedge:
        """Return the ``TRIGger:A:LOGIc:USECLockedge`` command.

        Description:
            - This command specifies whether or not Logic trigger type uses clock source.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:USECLockedge?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:USECLockedge?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGIc:USECLockedge value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:USECLockedge {OFF|ON|0|1|<NR1>}
            - TRIGger:A:LOGIc:USECLockedge?
            ```

        Info:
            - ``ON`` specifies that logic trigger type uses clock source.
            - ``1`` specifies that logic trigger type uses clock source.
            - ``OFF`` specifies that logic trigger type does not use clock source.
            - ``0`` specifies that logic trigger type does not use clock source.
            - ``<NR1>`` = 0 specifies that logic trigger type does not use clock source; any other
              value uses clock source.
        """
        return self._useclockedge

    @property
    def when(self) -> TriggerALogicWhen:
        """Return the ``TRIGger:A:LOGIc:WHEn`` command.

        Description:
            - This command sets or queries the condition for generating an A or B logic trigger with
              respect to the defined input pattern. This command is equivalent to selecting Logic
              for Trigger Type, Use Clock Edge to No, and choosing a trigger condition from the
              Logic Pattern drop-down list.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc:WHEn?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc:WHEn?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGIc:WHEn value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGIc:WHEn {TRUe|FALSe|MOREThan|LESSThan|EQual|UNEQual}
            - TRIGger:A:LOGIc:WHEn?
            ```

        Info:
            - ``TRUe`` triggers on an input pattern that is true.
            - ``FALSe`` triggers on an input pattern that is false.
            - ``MOREthan`` triggers on an input pattern that is true for a time period greater than
              a user defined Time Limit (DELTatime) value.
            - ``LESSthan`` triggers on an input pattern that is true for a time period less than a
              user defined Time Limit (DELTatime) value.
            - ``EQual`` triggers on an input pattern that is true for a time period equal to a user
              defined Time Limit (DELTatime) value.
            - ``UNEQual`` triggers on an input pattern that is true for a time period not equal to a
              user defined Time Limit (DELTatime) value.
        """
        return self._when


class TriggerALogicpatternDchItemDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGICPattern:DCH<x>_D<x>`` command.

    Description:
        - This command sets or queries the Logic Pattern for the specified digital channel. This
          command is used along with the Define Logic choice (``LOGIc:FUNCtion``) to determine when
          the logic trigger occurs.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGICPattern:DCH<x>_D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGICPattern:DCH<x>_D<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:LOGICPattern:DCH<x>_D<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGICPattern:DCH<x>_D<x> {HIGH|LOW|X}
        - TRIGger:A:LOGICPattern:DCH<x>_D<x>?
        ```

    Info:
        - ``DCH<x>_D<x>`` specifies the digital channel. The supported digital channel value is 1.
          The supported digital bits values are 0 to 15.
        - ``HIGH`` specifies triggering when the pattern is high.
        - ``LOW`` specifies triggering when the pattern is low.
        - ``X`` specifies triggering when the pattern is high or low.
    """


class TriggerALogicpatternDchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``TRIGger:A:LOGICPattern:DCH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGICPattern:DCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGICPattern:DCH<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.d``: The ``TRIGger:A:LOGICPattern:DCH<x>_D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, TriggerALogicpatternDchItemDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALogicpatternDchItemDigitalBit(device, f"{self._cmd_syntax}_D{x}")
        )

    @property
    def d(self) -> Dict[int, TriggerALogicpatternDchItemDigitalBit]:
        """Return the ``TRIGger:A:LOGICPattern:DCH<x>_D<x>`` command.

        Description:
            - This command sets or queries the Logic Pattern for the specified digital channel. This
              command is used along with the Define Logic choice (``LOGIc:FUNCtion``) to determine
              when the logic trigger occurs.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGICPattern:DCH<x>_D<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:LOGICPattern:DCH<x>_D<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGICPattern:DCH<x>_D<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGICPattern:DCH<x>_D<x> {HIGH|LOW|X}
            - TRIGger:A:LOGICPattern:DCH<x>_D<x>?
            ```

        Info:
            - ``DCH<x>_D<x>`` specifies the digital channel. The supported digital channel value is
              1. The supported digital bits values are 0 to 15.
            - ``HIGH`` specifies triggering when the pattern is high.
            - ``LOW`` specifies triggering when the pattern is low.
            - ``X`` specifies triggering when the pattern is high or low.
        """
        return self._d


class TriggerALogicpatternChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LOGICPattern:CH<x>`` command.

    Description:
        - This command sets or queries the Logic Pattern for the specified channel. This command is
          used along with the Define Logic choice (``LOGIc:FUNCtion``) to determine when the logic
          trigger occurs.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGICPattern:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGICPattern:CH<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LOGICPattern:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:LOGICPattern:CH<x> {HIGH|LOW|X}
        - TRIGger:A:LOGICPattern:CH<x>?
        ```

    Info:
        - ``CH<x>`` specifies the channel.
        - ``HIGH`` specifies triggering when the pattern is high.
        - ``LOW`` specifies triggering when the pattern is low.
        - ``X`` specifies triggering when the pattern is high or low.
    """


class TriggerALogicpattern(SCPICmdRead):
    """The ``TRIGger:A:LOGICPattern`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LOGICPattern?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGICPattern?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:A:LOGICPattern:CH<x>`` command.
        - ``.dch``: The ``TRIGger:A:LOGICPattern:DCH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerALogicpatternChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALogicpatternChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._dch: Dict[int, TriggerALogicpatternDchItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALogicpatternDchItem(device, f"{self._cmd_syntax}:DCH{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerALogicpatternChannel]:
        """Return the ``TRIGger:A:LOGICPattern:CH<x>`` command.

        Description:
            - This command sets or queries the Logic Pattern for the specified channel. This command
              is used along with the Define Logic choice (``LOGIc:FUNCtion``) to determine when the
              logic trigger occurs.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGICPattern:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGICPattern:CH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:LOGICPattern:CH<x> value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:LOGICPattern:CH<x> {HIGH|LOW|X}
            - TRIGger:A:LOGICPattern:CH<x>?
            ```

        Info:
            - ``CH<x>`` specifies the channel.
            - ``HIGH`` specifies triggering when the pattern is high.
            - ``LOW`` specifies triggering when the pattern is low.
            - ``X`` specifies triggering when the pattern is high or low.
        """
        return self._ch

    @property
    def dch(self) -> Dict[int, TriggerALogicpatternDchItem]:
        """Return the ``TRIGger:A:LOGICPattern:DCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGICPattern:DCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGICPattern:DCH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.d``: The ``TRIGger:A:LOGICPattern:DCH<x>_D<x>`` command.
        """
        return self._dch


class TriggerALevelChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:LEVel:CH<x>`` command.

    Description:
        - This command sets or queries the CH<x> trigger level for an Edge, Pulse Width, Runt or
          Rise/Fall (Transition and Slew Rate) trigger when triggering on an analog channel
          waveform. Each channel can have an independent trigger level. The <x> is the channel
          number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:CH<x> value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:LEVel:CH<x> <NR3>
        - TRIGger:A:LEVel:CH<x>?
        ```

    Info:
        - ``<NR3>`` specifies the trigger level in user units (usually volts).
    """


class TriggerALevel(SCPICmdRead):
    """The ``TRIGger:A:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``TRIGger:A:LEVel:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, TriggerALevelChannel] = DefaultDictPassKeyToFactory(
            lambda x: TriggerALevelChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, TriggerALevelChannel]:
        """Return the ``TRIGger:A:LEVel:CH<x>`` command.

        Description:
            - This command sets or queries the CH<x> trigger level for an Edge, Pulse Width, Runt or
              Rise/Fall (Transition and Slew Rate) trigger when triggering on an analog channel
              waveform. Each channel can have an independent trigger level. The <x> is the channel
              number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:LEVel:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:LEVel:CH<x> <NR3>
            - TRIGger:A:LEVel:CH<x>?
            ```

        Info:
            - ``<NR3>`` specifies the trigger level in user units (usually volts).
        """
        return self._ch


class TriggerAHoldoffTime(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:HOLDoff:TIMe`` command.

    Description:
        - This command sets or queries the A trigger holdoff time. This command is equivalent to
          selecting Mode & Holdoff from the Trig menu, selecting Time, and then setting the desired
          Holdoff Time.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:HOLDoff:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:HOLDoff:TIMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:HOLDoff:TIMe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:HOLDoff:TIMe <NR3>
        - TRIGger:A:HOLDoff:TIMe?
        ```

    Info:
        - ``<NR3>`` specifies the holdoff time in seconds. The range is from 0 seconds through 10
          seconds.
    """


class TriggerAHoldoff(SCPICmdRead):
    """The ``TRIGger:A:HOLDoff`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:HOLDoff?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:HOLDoff?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.time``: The ``TRIGger:A:HOLDoff:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._time = TriggerAHoldoffTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def time(self) -> TriggerAHoldoffTime:
        """Return the ``TRIGger:A:HOLDoff:TIMe`` command.

        Description:
            - This command sets or queries the A trigger holdoff time. This command is equivalent to
              selecting Mode & Holdoff from the Trig menu, selecting Time, and then setting the
              desired Holdoff Time.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:HOLDoff:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:HOLDoff:TIMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:HOLDoff:TIMe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:HOLDoff:TIMe <NR3>
            - TRIGger:A:HOLDoff:TIMe?
            ```

        Info:
            - ``<NR3>`` specifies the holdoff time in seconds. The range is from 0 seconds through
              10 seconds.
        """
        return self._time


class TriggerAEdgeSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:EDGE:SOUrce`` command.

    Description:
        - This command sets or queries the source for the edge trigger. For instruments that have an
          Auxiliary Input, AUXiliary can be selected as trigger source.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:SOUrce {CH<x>|DCH<x>_D<x>|INTernal|AUXiliary}
        - TRIGger:A:EDGE:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the edge trigger source.
        - ``DCH<x>_D<x>`` specifies a digital channel as the edge trigger source. The supported
          digital channel value is 1. The supported digital bit values are 0 to 15.
        - ``INTernal`` specifies a internal edge trigger source.
        - ``AUXiliary`` specifies the Auxiliary Input.
    """


class TriggerAEdgeSlope(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:EDGE:SLOpe`` command.

    Description:
        - This command sets or queries the slope for the edge trigger. This command is equivalent to
          selecting Edge from the Trigger Type drop-down in the Trigger setup context menu, and then
          choosing the desired Slope. This command is also equivalent to pressing the front-panel
          Slope button.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SLOpe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:SLOpe {RISe|FALL|EITher}
        - TRIGger:A:EDGE:SLOpe?
        ```

    Info:
        - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
        - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
        - ``EITHER`` specifies to trigger on either the rising or falling edge of a signal.
    """


class TriggerAEdgeCoupling(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:EDGE:COUPling`` command.

    Description:
        - This command sets or queries the type of coupling for the edge trigger. This command is
          equivalent to selecting Edge from the Trigger Type drop-down in the Trigger setup context
          menu, and choosing from the Coupling drop-down list.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:COUPling?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:COUPling?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:COUPling value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
        - TRIGger:A:EDGE:COUPling?
        ```

    Info:
        - ``DC`` selects DC trigger coupling, which passes all input signals to the trigger
          circuitry.
        - ``HFRej`` coupling attenuates signals above 50 kHz before passing the signals to the
          trigger circuitry.
        - ``LFRej`` coupling attenuates signals below 80 kHz before passing the signals to the
          trigger circuitry.
        - ``NOISErej`` coupling provides stable triggering by increasing the trigger hysteresis.
          Increased hysteresis reduces the trigger sensitivity to noise but can require greater
          trigger signal amplitude.
    """


class TriggerAEdge(SCPICmdRead):
    """The ``TRIGger:A:EDGE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.coupling``: The ``TRIGger:A:EDGE:COUPling`` command.
        - ``.slope``: The ``TRIGger:A:EDGE:SLOpe`` command.
        - ``.source``: The ``TRIGger:A:EDGE:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._coupling = TriggerAEdgeCoupling(device, f"{self._cmd_syntax}:COUPling")
        self._slope = TriggerAEdgeSlope(device, f"{self._cmd_syntax}:SLOpe")
        self._source = TriggerAEdgeSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def coupling(self) -> TriggerAEdgeCoupling:
        """Return the ``TRIGger:A:EDGE:COUPling`` command.

        Description:
            - This command sets or queries the type of coupling for the edge trigger. This command
              is equivalent to selecting Edge from the Trigger Type drop-down in the Trigger setup
              context menu, and choosing from the Coupling drop-down list.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:COUPling?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:COUPling?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:COUPling value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:COUPling {DC|HFRej|LFRej|NOISErej}
            - TRIGger:A:EDGE:COUPling?
            ```

        Info:
            - ``DC`` selects DC trigger coupling, which passes all input signals to the trigger
              circuitry.
            - ``HFRej`` coupling attenuates signals above 50 kHz before passing the signals to the
              trigger circuitry.
            - ``LFRej`` coupling attenuates signals below 80 kHz before passing the signals to the
              trigger circuitry.
            - ``NOISErej`` coupling provides stable triggering by increasing the trigger hysteresis.
              Increased hysteresis reduces the trigger sensitivity to noise but can require greater
              trigger signal amplitude.
        """
        return self._coupling

    @property
    def slope(self) -> TriggerAEdgeSlope:
        """Return the ``TRIGger:A:EDGE:SLOpe`` command.

        Description:
            - This command sets or queries the slope for the edge trigger. This command is
              equivalent to selecting Edge from the Trigger Type drop-down in the Trigger setup
              context menu, and then choosing the desired Slope. This command is also equivalent to
              pressing the front-panel Slope button.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SLOpe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SLOpe value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:SLOpe {RISe|FALL|EITher}
            - TRIGger:A:EDGE:SLOpe?
            ```

        Info:
            - ``RISe`` specifies to trigger on the rising or positive edge of a signal.
            - ``FALL`` specifies to trigger on the falling or negative edge of a signal.
            - ``EITHER`` specifies to trigger on either the rising or falling edge of a signal.
        """
        return self._slope

    @property
    def source(self) -> TriggerAEdgeSource:
        """Return the ``TRIGger:A:EDGE:SOUrce`` command.

        Description:
            - This command sets or queries the source for the edge trigger. For instruments that
              have an Auxiliary Input, AUXiliary can be selected as trigger source.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:EDGE:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:EDGE:SOUrce {CH<x>|DCH<x>_D<x>|INTernal|AUXiliary}
            - TRIGger:A:EDGE:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the edge trigger source.
            - ``DCH<x>_D<x>`` specifies a digital channel as the edge trigger source. The supported
              digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``INTernal`` specifies a internal edge trigger source.
            - ``AUXiliary`` specifies the Auxiliary Input.
        """
        return self._source


class TriggerABusSource(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:SOUrce`` command.

    Description:
        - This command sets or queries the source bus for a bus trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS:SOUrce value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:SOUrce B<x>
        - TRIGger:A:BUS:SOUrce?
        ```

    Info:
        - ``B<x>`` sets the selected source to the bus.
    """


class TriggerABusBItemSpiDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa:VALue`` command.

    Description:
        - This command specifies the binary data string used for SPI triggering if the trigger
          condition is DATA. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SPI:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:SPI:DATa:VALue?
        ```

    Info:
        - ``<QString>`` specifies the data value in the specified valid format. The valid characters
          are 0, 1, and X for binary format.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemSpiDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string to be used for a SPI trigger if the
          trigger condition is DATa. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data string in bytes.
    """


class TriggerABusBItemSpiData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.size``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = TriggerABusBItemSpiDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemSpiDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def size(self) -> TriggerABusBItemSpiDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string to be used for a SPI trigger if
              the trigger condition is DATa. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:SPI:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data string in bytes.
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemSpiDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa:VALue`` command.

        Description:
            - This command specifies the binary data string used for SPI triggering if the trigger
              condition is DATA. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SPI:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:SPI:DATa:VALue?
            ```

        Info:
            - ``<QString>`` specifies the data value in the specified valid format. The valid
              characters are 0, 1, and X for binary format.
        """
        return self._value


class TriggerABusBItemSpiCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI:CONDition`` command.

    Description:
        - This command specifies the trigger condition for a SPI trigger. B<x> is the specified bus
          number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SPI:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SPI:CONDition {SS|STARTofframe|DATa}
        - TRIGger:A:BUS:B<x>:SPI:CONDition?
        ```

    Info:
        - ``SS`` specifies the Slave Selection condition.
        - ``STARTofframe`` is applicable when ``BUS:B<x>:SPI:FRAMING`` is set to IDLEtime. When the
          trigger condition is set to STARTofframe, the instrument triggers on the first SPI clock
          after an idle time when there are no clocks.
        - ``DATa`` sets the trigger condition to Master-In Slave-Out and Master-Out Slave-In.
    """


class TriggerABusBItemSpi(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:SPI:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemSpiCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemSpiData(device, f"{self._cmd_syntax}:DATa")

    @property
    def condition(self) -> TriggerABusBItemSpiCondition:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:CONDition`` command.

        Description:
            - This command specifies the trigger condition for a SPI trigger. B<x> is the specified
              bus number.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SPI:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SPI:CONDition {SS|STARTofframe|DATa}
            - TRIGger:A:BUS:B<x>:SPI:CONDition?
            ```

        Info:
            - ``SS`` specifies the Slave Selection condition.
            - ``STARTofframe`` is applicable when ``BUS:B<x>:SPI:FRAMING`` is set to IDLEtime. When
              the trigger condition is set to STARTofframe, the instrument triggers on the first SPI
              clock after an idle time when there are no clocks.
            - ``DATa`` sets the trigger condition to Master-In Slave-Out and Master-Out Slave-In.
        """
        return self._condition

    @property
    def data(self) -> TriggerABusBItemSpiData:
        """Return the ``TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SPI:DATa:VALue`` command.
        """
        return self._data


class TriggerABusBItemSentSlowIdentifierValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue`` command.

    Description:
        - This command sets or queries the qualifier to use when triggering on SENT slow packet bus
          data. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue <Qstring>
        - TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue?
        ```

    Info:
        - ``<Qstring>`` is the binary identifier value.
    """


class TriggerABusBItemSentSlowIdentifier(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemSentSlowIdentifierValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemSentSlowIdentifierValue:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue`` command.

        Description:
            - This command sets or queries the qualifier to use when triggering on SENT slow packet
              bus data. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue <Qstring>
            - TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue?
            ```

        Info:
            - ``<Qstring>`` is the binary identifier value.
        """
        return self._value


class TriggerABusBItemSentSlowDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue`` command.

    Description:
        - This command sets or queries the binary slow channel value to use when triggering on a
          SENT bus signal. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue <Qstring>
        - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue?
        ```

    Info:
        - ``<Qstring>`` is the binary slow channel data value.
    """


class TriggerABusBItemSentSlowDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier`` command.

    Description:
        - This command sets or queries the binary identifier value to use when triggering on a SENT
          bus signal. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INRange|OUTRange}
        - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier?
        ```

    Info:
        - ``EQUal`` specifies the qualifier as Equal.
        - ``UNEQual`` specifies the qualifier as Not Equal to.
        - ``LESSthan`` specifies the qualifier as Less Than.
        - ``MOREthan`` specifies the qualifier as More Than.
        - ``LESSEQual`` specifies the qualifier as Less Than or Equal to.
        - ``MOREEQual`` specifies the qualifier as More Than or Equal to.
        - ``INRange`` sets the qualifier to inside a range.
        - ``OUTRange`` sets the qualifier to outside a range.
    """  # noqa: E501


class TriggerABusBItemSentSlowDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue`` command.

    Description:
        - This command sets or queries the high binary Slow channel data value to use when
          triggering on a SENT bus signal. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue?
        ```

    Info:
        - ``<Qstring>`` sets the binary Slow channel data value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemSentSlowData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemSentSlowDataHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._qualifier = TriggerABusBItemSentSlowDataQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = TriggerABusBItemSentSlowDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemSentSlowDataHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue`` command.

        Description:
            - This command sets or queries the high binary Slow channel data value to use when
              triggering on a SENT bus signal. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue?
            ```

        Info:
            - ``<Qstring>`` sets the binary Slow channel data value.
        """
        return self._hivalue

    @property
    def qualifier(self) -> TriggerABusBItemSentSlowDataQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier`` command.

        Description:
            - This command sets or queries the binary identifier value to use when triggering on a
              SENT bus signal. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INRange|OUTRange}
            - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier?
            ```

        Info:
            - ``EQUal`` specifies the qualifier as Equal.
            - ``UNEQual`` specifies the qualifier as Not Equal to.
            - ``LESSthan`` specifies the qualifier as Less Than.
            - ``MOREthan`` specifies the qualifier as More Than.
            - ``LESSEQual`` specifies the qualifier as Less Than or Equal to.
            - ``MOREEQual`` specifies the qualifier as More Than or Equal to.
            - ``INRange`` sets the qualifier to inside a range.
            - ``OUTRange`` sets the qualifier to outside a range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> TriggerABusBItemSentSlowDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue`` command.

        Description:
            - This command sets or queries the binary slow channel value to use when triggering on a
              SENT bus signal. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue <Qstring>
            - TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue?
            ```

        Info:
            - ``<Qstring>`` is the binary slow channel data value.
        """
        return self._value


class TriggerABusBItemSentSlow(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:SLOW`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:SLOW?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:SLOW?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.data``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA`` command tree.
        - ``.identifier``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = TriggerABusBItemSentSlowData(device, f"{self._cmd_syntax}:DATA")
        self._identifier = TriggerABusBItemSentSlowIdentifier(
            device, f"{self._cmd_syntax}:IDentifier"
        )

    @property
    def data(self) -> TriggerABusBItemSentSlowData:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:HIVALue`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:QUALifier`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA:VALue`` command.
        """
        return self._data

    @property
    def identifier(self) -> TriggerABusBItemSentSlowIdentifier:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier:VALue`` command.
        """
        return self._identifier


class TriggerABusBItemSentPauseQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier`` command.

    Description:
        - This command sets or queries the qualifier to be used when triggering on SENT pause
          pulses. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|Inrange|OUTrange}
        - TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier?
        ```

    Info:
        - ``EQUal`` sets the qualifier as Equal.
        - ``INrange`` sets the qualifier to in range.
        - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
        - ``LESSThan`` sets the qualifier as Less Than.
        - ``MOREEQual`` sets the qualifier as More Than or Equal to.
        - ``MOREThan`` sets the qualifier as More Than.
        - ``OUTrange`` sets the qualifier to out of range.
        - ``UNEQual`` sets the qualifier as Unequal.
    """  # noqa: E501


class TriggerABusBItemSentPause(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:PAUSE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:PAUSE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:PAUSE?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._qualifier = TriggerABusBItemSentPauseQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )

    @property
    def qualifier(self) -> TriggerABusBItemSentPauseQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier`` command.

        Description:
            - This command sets or queries the qualifier to be used when triggering on SENT pause
              pulses. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|Inrange|OUTrange}
            - TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier?
            ```

        Info:
            - ``EQUal`` sets the qualifier as Equal.
            - ``INrange`` sets the qualifier to in range.
            - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
            - ``LESSThan`` sets the qualifier as Less Than.
            - ``MOREEQual`` sets the qualifier as More Than or Equal to.
            - ``MOREThan`` sets the qualifier as More Than.
            - ``OUTrange`` sets the qualifier to out of range.
            - ``UNEQual`` sets the qualifier as Unequal.
        """  # noqa: E501
        return self._qualifier


class TriggerABusBItemSentFastStatusValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue`` command.

    Description:
        - This command sets or queries the binary status value to be used when triggering on a SENT
          bus signal. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue <Qstring>
        - TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue?
        ```

    Info:
        - ``<Qstring>`` is the binary status value on which to trigger.
    """


class TriggerABusBItemSentFastStatus(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemSentFastStatusValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemSentFastStatusValue:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue`` command.

        Description:
            - This command sets or queries the binary status value to be used when triggering on a
              SENT bus signal. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue <Qstring>
            - TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue?
            ```

        Info:
            - ``<Qstring>`` is the binary status value on which to trigger.
        """
        return self._value


class TriggerABusBItemSentFastInvertnibbleValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue`` command.

    Description:
        - This command sets or queries the binary fast message inverted nibble value to be used when
          triggering on a SENT bus signal. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue <Qstring>
        - TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue?
        ```

    Info:
        - ``<Qstring>`` is the Fast Channel 1 inverted nibble binary value on which to trigger.
    """


class TriggerABusBItemSentFastInvertnibble(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemSentFastInvertnibbleValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemSentFastInvertnibbleValue:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue`` command.

        Description:
            - This command sets or queries the binary fast message inverted nibble value to be used
              when triggering on a SENT bus signal. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue <Qstring>
            - TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue?
            ```

        Info:
            - ``<Qstring>`` is the Fast Channel 1 inverted nibble binary value on which to trigger.
        """
        return self._value


class TriggerABusBItemSentFastCounterValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue`` command.

    Description:
        - This command sets or queries the binary fast message counter value to be used when
          triggering on a SENT bus signal. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue <Qstring>
        - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue?
        ```

    Info:
        - ``<Qstring>`` is the Fast Channel 1 fast message counter binary value on which to trigger.
    """


class TriggerABusBItemSentFastCounterQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier`` command.

    Description:
        - This command sets or queries the qualifier to be used when triggering on SENT fast packet
          bus data for the secure format counter. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier?
        ```

    Info:
        - ``EQUal`` sets the qualifier as Equal.
        - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
        - ``LESSThan`` sets the qualifier as Less Than.
        - ``MOREEQual`` sets the qualifier as More Than or Equal to.
        - ``MOREThan`` sets the qualifier as More Than.
        - ``UNEQual`` sets the qualifier as Unequal.
        - ``INrange`` sets the qualifier to inside a range.
        - ``OUTrange`` sets the qualifier to outside a range.
    """  # noqa: E501


class TriggerABusBItemSentFastCounterHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue`` command.

    Description:
        - This command sets or queries the high binary fast message counter value to be used when
          triggering on a SENT bus signal. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue?
        ```

    Info:
        - ``<Qstring>`` sets the Fast Channel 1 counter binary value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemSentFastCounter(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemSentFastCounterHivalue(
            device, f"{self._cmd_syntax}:HIVALue"
        )
        self._qualifier = TriggerABusBItemSentFastCounterQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = TriggerABusBItemSentFastCounterValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemSentFastCounterHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue`` command.

        Description:
            - This command sets or queries the high binary fast message counter value to be used
              when triggering on a SENT bus signal. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue?
            ```

        Info:
            - ``<Qstring>`` sets the Fast Channel 1 counter binary value.
        """
        return self._hivalue

    @property
    def qualifier(self) -> TriggerABusBItemSentFastCounterQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier`` command.

        Description:
            - This command sets or queries the qualifier to be used when triggering on SENT fast
              packet bus data for the secure format counter. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier?
            ```

        Info:
            - ``EQUal`` sets the qualifier as Equal.
            - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
            - ``LESSThan`` sets the qualifier as Less Than.
            - ``MOREEQual`` sets the qualifier as More Than or Equal to.
            - ``MOREThan`` sets the qualifier as More Than.
            - ``UNEQual`` sets the qualifier as Unequal.
            - ``INrange`` sets the qualifier to inside a range.
            - ``OUTrange`` sets the qualifier to outside a range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> TriggerABusBItemSentFastCounterValue:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue`` command.

        Description:
            - This command sets or queries the binary fast message counter value to be used when
              triggering on a SENT bus signal. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue <Qstring>
            - TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue?
            ```

        Info:
            - ``<Qstring>`` is the Fast Channel 1 fast message counter binary value on which to
              trigger.
        """
        return self._value


class TriggerABusBItemSentFastChan2bValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue`` command.

    Description:
        - This command sets or queries the binary fast channel 2 value to be used when triggering on
          a SENT bus signal. The trigger condition must be set to FAST. B<x> is the specified bus
          number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue <Qstring>
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue?
        ```

    Info:
        - ``<Qstring>`` is the Fast Channel 2 binary value on which to trigger.
    """


class TriggerABusBItemSentFastChan2bQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier`` command.

    Description:
        - This command sets or queries the qualifier to be used when triggering on SENT fast packet
          bus data for device channel 2. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier?
        ```

    Info:
        - ``EQUal`` sets the qualifier as Equal.
        - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
        - ``LESSThan`` sets the qualifier as Less Than.
        - ``MOREEQual`` sets the qualifier as More Than or Equal to.
        - ``MOREThan`` sets the qualifier as More Than.
        - ``UNEQual`` sets the qualifier as Unequal.
        - ``INrange`` sets the qualifier to inside a range.
        - ``OUTrange`` sets the qualifier to outside a range.
    """  # noqa: E501


class TriggerABusBItemSentFastChan2bHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue`` command.

    Description:
        - This command sets or queries the high binary fast channel 2 value to use when triggering
          on a SENT bus signal. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue?
        ```

    Info:
        - ``<Qstring>`` sets the Fast Channel 2 high binary data value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemSentFastChan2b(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemSentFastChan2bHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._qualifier = TriggerABusBItemSentFastChan2bQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = TriggerABusBItemSentFastChan2bValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemSentFastChan2bHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue`` command.

        Description:
            - This command sets or queries the high binary fast channel 2 value to use when
              triggering on a SENT bus signal. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue?
            ```

        Info:
            - ``<Qstring>`` sets the Fast Channel 2 high binary data value.
        """
        return self._hivalue

    @property
    def qualifier(self) -> TriggerABusBItemSentFastChan2bQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier`` command.

        Description:
            - This command sets or queries the qualifier to be used when triggering on SENT fast
              packet bus data for device channel 2. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier?
            ```

        Info:
            - ``EQUal`` sets the qualifier as Equal.
            - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
            - ``LESSThan`` sets the qualifier as Less Than.
            - ``MOREEQual`` sets the qualifier as More Than or Equal to.
            - ``MOREThan`` sets the qualifier as More Than.
            - ``UNEQual`` sets the qualifier as Unequal.
            - ``INrange`` sets the qualifier to inside a range.
            - ``OUTrange`` sets the qualifier to outside a range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> TriggerABusBItemSentFastChan2bValue:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue`` command.

        Description:
            - This command sets or queries the binary fast channel 2 value to be used when
              triggering on a SENT bus signal. The trigger condition must be set to FAST. B<x> is
              the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue <Qstring>
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue?
            ```

        Info:
            - ``<Qstring>`` is the Fast Channel 2 binary value on which to trigger.
        """
        return self._value


class TriggerABusBItemSentFastChan1aValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue`` command.

    Description:
        - This command sets or queries the binary fast channel 1 value to be used when triggering on
          a SENT bus signal. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue <Qstring>
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue?
        ```

    Info:
        - ``<Qstring>`` is the Fast Channel 1 value on which to trigger.
    """


class TriggerABusBItemSentFastChan1aQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier`` command.

    Description:
        - This command sets or queries the qualifier to be used when triggering on SENT fast packet
          bus data for device channel 1. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier?
        ```

    Info:
        - ``EQUal`` sets the qualifier as Equal.
        - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
        - ``LESSThan`` sets the qualifier as Less Than.
        - ``MOREEQual`` sets the qualifier as More Than or Equal to.
        - ``MOREThan`` sets the qualifier as More Than.
        - ``UNEQual`` sets the qualifier as Unequal.
        - ``INrange`` sets the qualifier to inside a range.
        - ``OUTrange`` sets the qualifier to outside a range.
    """  # noqa: E501


class TriggerABusBItemSentFastChan1aHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue`` command.

    Description:
        - This command sets or queries the high binary fast channel 1 value to use when triggering
          on a SENT bus signal. B<x> is the specified bus number.

    Usage:
        - Using the ``.query()`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue?
        ```

    Info:
        - ``<Qstring>`` sets the Fast Channel 1 binary data high value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemSentFastChan1a(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemSentFastChan1aHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._qualifier = TriggerABusBItemSentFastChan1aQualifier(
            device, f"{self._cmd_syntax}:QUALifier"
        )
        self._value = TriggerABusBItemSentFastChan1aValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemSentFastChan1aHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue`` command.

        Description:
            - This command sets or queries the high binary fast channel 1 value to use when
              triggering on a SENT bus signal. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue?
            ```

        Info:
            - ``<Qstring>`` sets the Fast Channel 1 binary data high value.
        """
        return self._hivalue

    @property
    def qualifier(self) -> TriggerABusBItemSentFastChan1aQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier`` command.

        Description:
            - This command sets or queries the qualifier to be used when triggering on SENT fast
              packet bus data for device channel 1. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier {EQual|UNEQual|LESSthan|MOREthan|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier?
            ```

        Info:
            - ``EQUal`` sets the qualifier as Equal.
            - ``LESSEQual`` sets the qualifier as Less Than or Equal to.
            - ``LESSThan`` sets the qualifier as Less Than.
            - ``MOREEQual`` sets the qualifier as More Than or Equal to.
            - ``MOREThan`` sets the qualifier as More Than.
            - ``UNEQual`` sets the qualifier as Unequal.
            - ``INrange`` sets the qualifier to inside a range.
            - ``OUTrange`` sets the qualifier to outside a range.
        """  # noqa: E501
        return self._qualifier

    @property
    def value(self) -> TriggerABusBItemSentFastChan1aValue:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue`` command.

        Description:
            - This command sets or queries the binary fast channel 1 value to be used when
              triggering on a SENT bus signal. B<x> is the specified bus number.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue <Qstring>
            - TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue?
            ```

        Info:
            - ``<Qstring>`` is the Fast Channel 1 value on which to trigger.
        """
        return self._value


class TriggerABusBItemSentFast(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:FAST`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.chan1a``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A`` command tree.
        - ``.chan2b``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B`` command tree.
        - ``.counter``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer`` command tree.
        - ``.invertnibble``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble`` command tree.
        - ``.status``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._chan1a = TriggerABusBItemSentFastChan1a(device, f"{self._cmd_syntax}:CHAN1A")
        self._chan2b = TriggerABusBItemSentFastChan2b(device, f"{self._cmd_syntax}:CHAN2B")
        self._counter = TriggerABusBItemSentFastCounter(device, f"{self._cmd_syntax}:COUNTer")
        self._invertnibble = TriggerABusBItemSentFastInvertnibble(
            device, f"{self._cmd_syntax}:INVERTNIBble"
        )
        self._status = TriggerABusBItemSentFastStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def chan1a(self) -> TriggerABusBItemSentFastChan1a:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:HIVALue`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:QUALifier`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A:VALue`` command.
        """
        return self._chan1a

    @property
    def chan2b(self) -> TriggerABusBItemSentFastChan2b:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:HIVALue`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:QUALifier`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B:VALue`` command.
        """
        return self._chan2b

    @property
    def counter(self) -> TriggerABusBItemSentFastCounter:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:HIVALue`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:QUALifier`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer:VALue`` command.
        """
        return self._counter

    @property
    def invertnibble(self) -> TriggerABusBItemSentFastInvertnibble:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble:VALue`` command.
        """
        return self._invertnibble

    @property
    def status(self) -> TriggerABusBItemSentFastStatus:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus:VALue`` command.
        """
        return self._status


class TriggerABusBItemSentErrtypeCrc(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:ERRType:CRC`` command.

    Description:
        - This command sets or queries the CRC error type to be used when triggering on SENT data.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:ERRType:CRC?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:ERRType:CRC?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:ERRType:CRC value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:ERRType:CRC {FAST|SLOW}
        - TRIGger:A:BUS:B<x>:SENT:ERRType:CRC?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``FAST`` specifies triggering on CRC errors in only the Fast Channel.
        - ``SLOW`` specifies triggering on CRC errors in only the slow channel.
    """


class TriggerABusBItemSentErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:ERRType`` command.

    Description:
        - This command sets or queries the error type to be used when triggering on SENT data.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:ERRType?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:ERRType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:ERRType value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:ERRType CRC
        - TRIGger:A:BUS:B<x>:SENT:ERRType?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``CRC`` specifies triggering on CRC errors.

    Properties:
        - ``.crc``: The ``TRIGger:A:BUS:B<x>:SENT:ERRType:CRC`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._crc = TriggerABusBItemSentErrtypeCrc(device, f"{self._cmd_syntax}:CRC")

    @property
    def crc(self) -> TriggerABusBItemSentErrtypeCrc:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:ERRType:CRC`` command.

        Description:
            - This command sets or queries the CRC error type to be used when triggering on SENT
              data.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:ERRType:CRC?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:ERRType:CRC?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:ERRType:CRC value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:ERRType:CRC {FAST|SLOW}
            - TRIGger:A:BUS:B<x>:SENT:ERRType:CRC?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``FAST`` specifies triggering on CRC errors in only the Fast Channel.
            - ``SLOW`` specifies triggering on CRC errors in only the slow channel.
        """
        return self._crc


class TriggerABusBItemSentCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT:CONDition`` command.

    Description:
        - This command sets or queries the trigger condition for a SENT bus.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:SENT:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:SENT:CONDition {START|FAST|SLOW|ERRor}
        - TRIGger:A:BUS:B<x>:SENT:CONDition?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``START`` sets triggering on start of packet.
        - ``FAST`` sets triggering on fast channel packets.
        - ``SLOW`` sets triggering on slow channel packets.
        - ``ERRor`` sets triggering on errors.
    """


class TriggerABusBItemSent(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:SENT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:SENT:CONDition`` command.
        - ``.errtype``: The ``TRIGger:A:BUS:B<x>:SENT:ERRType`` command.
        - ``.fast``: The ``TRIGger:A:BUS:B<x>:SENT:FAST`` command tree.
        - ``.pause``: The ``TRIGger:A:BUS:B<x>:SENT:PAUSE`` command tree.
        - ``.slow``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemSentCondition(device, f"{self._cmd_syntax}:CONDition")
        self._errtype = TriggerABusBItemSentErrtype(device, f"{self._cmd_syntax}:ERRType")
        self._fast = TriggerABusBItemSentFast(device, f"{self._cmd_syntax}:FAST")
        self._pause = TriggerABusBItemSentPause(device, f"{self._cmd_syntax}:PAUSE")
        self._slow = TriggerABusBItemSentSlow(device, f"{self._cmd_syntax}:SLOW")

    @property
    def condition(self) -> TriggerABusBItemSentCondition:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:CONDition`` command.

        Description:
            - This command sets or queries the trigger condition for a SENT bus.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:CONDition {START|FAST|SLOW|ERRor}
            - TRIGger:A:BUS:B<x>:SENT:CONDition?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``START`` sets triggering on start of packet.
            - ``FAST`` sets triggering on fast channel packets.
            - ``SLOW`` sets triggering on slow channel packets.
            - ``ERRor`` sets triggering on errors.
        """
        return self._condition

    @property
    def errtype(self) -> TriggerABusBItemSentErrtype:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:ERRType`` command.

        Description:
            - This command sets or queries the error type to be used when triggering on SENT data.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:ERRType?``
              query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:ERRType?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:SENT:ERRType value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:SENT:ERRType CRC
            - TRIGger:A:BUS:B<x>:SENT:ERRType?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``CRC`` specifies triggering on CRC errors.

        Sub-properties:
            - ``.crc``: The ``TRIGger:A:BUS:B<x>:SENT:ERRType:CRC`` command.
        """
        return self._errtype

    @property
    def fast(self) -> TriggerABusBItemSentFast:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:FAST`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:FAST?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.chan1a``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN1A`` command tree.
            - ``.chan2b``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:CHAN2B`` command tree.
            - ``.counter``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:COUNTer`` command tree.
            - ``.invertnibble``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:INVERTNIBble`` command tree.
            - ``.status``: The ``TRIGger:A:BUS:B<x>:SENT:FAST:STATus`` command tree.
        """
        return self._fast

    @property
    def pause(self) -> TriggerABusBItemSentPause:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:PAUSE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:PAUSE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:PAUSE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:SENT:PAUSE:QUALifier`` command.
        """
        return self._pause

    @property
    def slow(self) -> TriggerABusBItemSentSlow:
        """Return the ``TRIGger:A:BUS:B<x>:SENT:SLOW`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT:SLOW?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT:SLOW?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:DATA`` command tree.
            - ``.identifier``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW:IDentifier`` command tree.
        """
        return self._slow


class TriggerABusBItemRs232cDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:DATa:VALue`` command.

    Description:
        - This command sets or queries the data address string used for the RS-232 bus trigger when
          the trigger condition is set to Data. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:DATa:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:DATa:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:RS232C:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:RS232C:DATa:VALue?
        ```

    Info:
        - ``<QString>`` specifies the address value. The argument is a string of 0, 1, or X
          representing a binary number.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemRs232cDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe`` command.

    Description:
        - This command sets or queries the length of the data string in bytes to be used for an
          RS-232C trigger when the trigger condition is Data. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe <NR3>
        - TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe?
        ```

    Info:
        - ``<NR3>`` specifies the data size in bytes.
    """


class TriggerABusBItemRs232cData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:DATa?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.size``: The ``TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:RS232C:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = TriggerABusBItemRs232cDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemRs232cDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def size(self) -> TriggerABusBItemRs232cDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe`` command.

        Description:
            - This command sets or queries the length of the data string in bytes to be used for an
              RS-232C trigger when the trigger condition is Data. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe <NR3>
            - TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe?
            ```

        Info:
            - ``<NR3>`` specifies the data size in bytes.
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemRs232cDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:DATa:VALue`` command.

        Description:
            - This command sets or queries the data address string used for the RS-232 bus trigger
              when the trigger condition is set to Data. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:DATa:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:RS232C:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:RS232C:DATa:VALue?
            ```

        Info:
            - ``<QString>`` specifies the address value. The argument is a string of 0, 1, or X
              representing a binary number.
        """
        return self._value


class TriggerABusBItemRs232cCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.

    Description:
        - This command specifies the condition for an RS-232C trigger, where the bus number is
          specified by< >x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:CONDition?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:RS232C:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:RS232C:CONDition {STARt|EOp|DATa|PARItyerror}
        - TRIGger:A:BUS:B<x>:RS232C:CONDition?
        ```

    Info:
        - ``STARt`` sets the Trigger on condition to Start.
        - ``EOp`` sets the Trigger on condition to End of Packet.
        - ``DATa`` sets the Trigger on condition to Data.
        - ``PARItyerror`` sets the Trigger on condition to Parity Error.
    """


class TriggerABusBItemRs232c(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:RS232C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:RS232C:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemRs232cCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemRs232cData(device, f"{self._cmd_syntax}:DATa")

    @property
    def condition(self) -> TriggerABusBItemRs232cCondition:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.

        Description:
            - This command specifies the condition for an RS-232C trigger, where the bus number is
              specified by< >x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:RS232C:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:RS232C:CONDition {STARt|EOp|DATa|PARItyerror}
            - TRIGger:A:BUS:B<x>:RS232C:CONDition?
            ```

        Info:
            - ``STARt`` sets the Trigger on condition to Start.
            - ``EOp`` sets the Trigger on condition to End of Packet.
            - ``DATa`` sets the Trigger on condition to Data.
            - ``PARItyerror`` sets the Trigger on condition to Parity Error.
        """
        return self._condition

    @property
    def data(self) -> TriggerABusBItemRs232cData:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``TRIGger:A:BUS:B<x>:RS232C:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:RS232C:DATa:VALue`` command.
        """
        return self._data


class TriggerABusBItemParallelDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:PARallel:DATa:VALue`` command.

    Description:
        - This command specifies the binary data string used for a Parallel Bus trigger. The bus
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:PARallel:DATa:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:PARallel:DATa:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:PARallel:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:PARallel:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:PARallel:DATa:VALue?
        ```

    Info:
        - ``<QString>`` is the binary data string used for a Parallel Bus trigger.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemParallelData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:PARallel:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:PARallel:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:PARallel:DATa?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:PARallel:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemParallelDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemParallelDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:PARallel:DATa:VALue`` command.

        Description:
            - This command specifies the binary data string used for a Parallel Bus trigger. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:PARallel:DATa:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:PARallel:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:PARallel:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:PARallel:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:PARallel:DATa:VALue?
            ```

        Info:
            - ``<QString>`` is the binary data string used for a Parallel Bus trigger.
        """
        return self._value


class TriggerABusBItemParallel(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:PARallel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:PARallel?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:PARallel?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.data``: The ``TRIGger:A:BUS:B<x>:PARallel:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = TriggerABusBItemParallelData(device, f"{self._cmd_syntax}:DATa")

    @property
    def data(self) -> TriggerABusBItemParallelData:
        """Return the ``TRIGger:A:BUS:B<x>:PARallel:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:PARallel:DATa?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:PARallel:DATa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:PARallel:DATa:VALue`` command.
        """
        return self._data


class TriggerABusBItemLinIdentifierValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.

    Description:
        - This command specifies the binary address string used for LIN bus trigger if the trigger
          condition is ID or IDANDDATA. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue <QString>
        - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?
        ```

    Info:
        - ``<QString>`` is the binary address string used for LIN trigger if the trigger condition
          is ID or IDANDDATA.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemLinIdentifier(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:IDentifier`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:IDentifier?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:IDentifier?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = TriggerABusBItemLinIdentifierValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> TriggerABusBItemLinIdentifierValue:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.

        Description:
            - This command specifies the binary address string used for LIN bus trigger if the
              trigger condition is ID or IDANDDATA. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue <QString>
            - TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue?
            ```

        Info:
            - ``<QString>`` is the binary address string used for LIN trigger if the trigger
              condition is ID or IDANDDATA.
        """
        return self._value


class TriggerABusBItemLinErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.

    Description:
        - This command specifies the error type be used for LIN trigger. The bus number is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum}
        - TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
        ```

    Info:
        - ``SYNC`` sets the LIN error type to SYNC.
        - ``PARity`` sets the LIN error type to parity.
        - ``CHecksum`` sets the LIN error type to checksum.
    """


class TriggerABusBItemLinDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.

    Description:
        - This command specifies the binary data string to be used for LIN trigger condition if
          trigger condition is ID or IDANDDATA. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:LIN:DATa:VALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the LIN trigger data value.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemLinDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string in bytes to be used for LIN trigger.
          The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the size of the data string in bytes.
    """


class TriggerABusBItemLinDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier`` command.

    Description:
        - This command specifies the LIN data qualifier. This only applies if the trigger condition
          is IDANDDATA or DATA. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
        - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the LIN data qualifier to less than.
        - ``MOREthan`` sets the LIN data qualifier to greater than.
        - ``EQual`` sets the LIN data qualifier to equal.
        - ``UNEQual`` sets the LIN data qualifier to not equal.
        - ``LESSEQual`` sets the LIN data qualifier to less than or equal.
        - ``MOREEQual`` sets the LIN data qualifier to greater than or equal.
        - ``INrange`` sets the LIN data qualifier to in range.
        - ``OUTrange`` sets the LIN data qualifier to out of range.
    """  # noqa: E501


class TriggerABusBItemLinDataHivalue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.

    Description:
        - This command specifies the high data value string used for a LIN bus trigger when the
          trigger condition is DATA or IDANDDATA and the data qualifier is INRANGE or OUTRANGE. The
          bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue <QString>
        - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?
        ```

    Info:
        - ``<QString>`` is a quoted string that is the binary data string used for LIN trigger if
          the trigger condition is ID or IDANDDATA.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemLinData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier`` command.
        - ``.size``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hivalue = TriggerABusBItemLinDataHivalue(device, f"{self._cmd_syntax}:HIVALue")
        self._qualifier = TriggerABusBItemLinDataQualifier(device, f"{self._cmd_syntax}:QUALifier")
        self._size = TriggerABusBItemLinDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemLinDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def hivalue(self) -> TriggerABusBItemLinDataHivalue:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.

        Description:
            - This command specifies the high data value string used for a LIN bus trigger when the
              trigger condition is DATA or IDANDDATA and the data qualifier is INRANGE or OUTRANGE.
              The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue <QString>
            - TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the binary data string used for LIN trigger
              if the trigger condition is ID or IDANDDATA.
        """
        return self._hivalue

    @property
    def qualifier(self) -> TriggerABusBItemLinDataQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier`` command.

        Description:
            - This command specifies the LIN data qualifier. This only applies if the trigger
              condition is IDANDDATA or DATA. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual|INrange|OUTrange}
            - TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the LIN data qualifier to less than.
            - ``MOREthan`` sets the LIN data qualifier to greater than.
            - ``EQual`` sets the LIN data qualifier to equal.
            - ``UNEQual`` sets the LIN data qualifier to not equal.
            - ``LESSEQual`` sets the LIN data qualifier to less than or equal.
            - ``MOREEQual`` sets the LIN data qualifier to greater than or equal.
            - ``INrange`` sets the LIN data qualifier to in range.
            - ``OUTrange`` sets the LIN data qualifier to out of range.
        """  # noqa: E501
        return self._qualifier

    @property
    def size(self) -> TriggerABusBItemLinDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string in bytes to be used for LIN
              trigger. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:LIN:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the size of the data string in bytes.
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemLinDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.

        Description:
            - This command specifies the binary data string to be used for LIN trigger condition if
              trigger condition is ID or IDANDDATA. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:LIN:DATa:VALue?
            ```

        Info:
            - ``<QString>`` is a quoted string that is the LIN trigger data value.
        """
        return self._value


class TriggerABusBItemLinCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN:CONDition`` command.

    Description:
        - This command specifies the trigger condition for LIN. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:LIN:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:LIN:CONDition {SYNCfield|IDentifier|DATa|IDANDDATA|WAKEup|SLEEP|ERRor}
        - TRIGger:A:BUS:B<x>:LIN:CONDition?
        ```

    Info:
        - ``SYNCfield`` sets the LIN trigger condition to sync field.
        - ``IDentifier`` sets the LIN trigger condition to identifier.
        - ``DATa`` sets the LIN trigger condition to data.
        - ``IDANDDATA`` sets the LIN trigger condition to id and data.
        - ``WAKEup`` sets the LIN trigger condition to wake up.
        - ``SLEEP`` sets the LIN trigger condition to sleep.
        - ``ERRor`` sets the LIN trigger condition to error.
    """


class TriggerABusBItemLin(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:LIN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:LIN:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.
        - ``.errtype``: The ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.
        - ``.identifier``: The ``TRIGger:A:BUS:B<x>:LIN:IDentifier`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemLinCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemLinData(device, f"{self._cmd_syntax}:DATa")
        self._errtype = TriggerABusBItemLinErrtype(device, f"{self._cmd_syntax}:ERRTYPE")
        self._identifier = TriggerABusBItemLinIdentifier(device, f"{self._cmd_syntax}:IDentifier")

    @property
    def condition(self) -> TriggerABusBItemLinCondition:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:CONDition`` command.

        Description:
            - This command specifies the trigger condition for LIN. The bus number is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:CONDition {SYNCfield|IDentifier|DATa|IDANDDATA|WAKEup|SLEEP|ERRor}
            - TRIGger:A:BUS:B<x>:LIN:CONDition?
            ```

        Info:
            - ``SYNCfield`` sets the LIN trigger condition to sync field.
            - ``IDentifier`` sets the LIN trigger condition to identifier.
            - ``DATa`` sets the LIN trigger condition to data.
            - ``IDANDDATA`` sets the LIN trigger condition to id and data.
            - ``WAKEup`` sets the LIN trigger condition to wake up.
            - ``SLEEP`` sets the LIN trigger condition to sleep.
            - ``ERRor`` sets the LIN trigger condition to error.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> TriggerABusBItemLinData:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hivalue``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:HIVALue`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:QUALifier`` command.
            - ``.size``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:LIN:DATa:VALue`` command.
        """
        return self._data

    @property
    def errtype(self) -> TriggerABusBItemLinErrtype:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.

        Description:
            - This command specifies the error type be used for LIN trigger. The bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:LIN:ERRTYPE {SYNC|PARity|CHecksum}
            - TRIGger:A:BUS:B<x>:LIN:ERRTYPE?
            ```

        Info:
            - ``SYNC`` sets the LIN error type to SYNC.
            - ``PARity`` sets the LIN error type to parity.
            - ``CHecksum`` sets the LIN error type to checksum.
        """
        return self._errtype

    @property
    def identifier(self) -> TriggerABusBItemLinIdentifier:
        """Return the ``TRIGger:A:BUS:B<x>:LIN:IDentifier`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN:IDentifier?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:LIN:IDentifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``TRIGger:A:BUS:B<x>:LIN:IDentifier:VALue`` command.
        """
        return self._identifier


class TriggerABusBItemI2cDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.

    Description:
        - This command specifies the binary data string used for I2C triggering if the trigger
          condition is DATA or ADDRANDDATA. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:I2C:DATa:VALue?
        ```

    Info:
        - ``<QString>`` is the binary data string, where the number of bits is 8 times the number of
          bytes specified. The only allowed characters in the string are 0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemI2cDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.

    Description:
        - This command specifies the length of the data string in bytes to be used for an I2C
          trigger if the trigger condition is DATA or ADDRANDDATA. Applies to bus <x>, where the bus
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data string in bytes.
    """


class TriggerABusBItemI2cDataDirection(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection`` command.

    Description:
        - This command specifies the I 2 C trigger type to be valid on a Read, Write, or Either
          condition. Read or write is indicated by the R/W bit in the I 2 C protocol. The bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection {READ|WRITE|NOCARE}
        - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?
        ```

    Info:
        - ``READ`` specifies read as the data direction.
        - ``WRITE`` specifies write as the data direction.
        - ``NOCARE`` specifies either as the data direction.
    """


class TriggerABusBItemI2cData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.direction``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection`` command.
        - ``.size``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = TriggerABusBItemI2cDataDirection(device, f"{self._cmd_syntax}:DIRection")
        self._size = TriggerABusBItemI2cDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemI2cDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def direction(self) -> TriggerABusBItemI2cDataDirection:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection`` command.

        Description:
            - This command specifies the I 2 C trigger type to be valid on a Read, Write, or Either
              condition. Read or write is indicated by the R/W bit in the I 2 C protocol. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection {READ|WRITE|NOCARE}
            - TRIGger:A:BUS:B<x>:I2C:DATa:DIRection?
            ```

        Info:
            - ``READ`` specifies read as the data direction.
            - ``WRITE`` specifies write as the data direction.
            - ``NOCARE`` specifies either as the data direction.
        """
        return self._direction

    @property
    def size(self) -> TriggerABusBItemI2cDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.

        Description:
            - This command specifies the length of the data string in bytes to be used for an I2C
              trigger if the trigger condition is DATA or ADDRANDDATA. Applies to bus <x>, where the
              bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:I2C:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data string in bytes.
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemI2cDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.

        Description:
            - This command specifies the binary data string used for I2C triggering if the trigger
              condition is DATA or ADDRANDDATA. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:I2C:DATa:VALue?
            ```

        Info:
            - ``<QString>`` is the binary data string, where the number of bits is 8 times the
              number of bytes specified. The only allowed characters in the string are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemI2cCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:CONDition`` command.

    Description:
        - This command specifies the trigger condition for an I 2 C trigger. The bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:CONDition {STARt|STOP|REPEATstart|ACKMISS|ADDRess|DATa|ADDRANDDATA}
        - TRIGger:A:BUS:B<x>:I2C:CONDition?
        ```

    Info:
        - ``STARt`` specifies a search based on start condition.
        - ``STOP`` specifies a search based on stop condition.
        - ``REPEATstart`` specifies a search based on repeat of start condition.
        - ``ACKMISS`` specifies a search based on missing acknowledgement condition.
        - ``ADDRess`` specifies a search based on address.
        - ``DATa`` specifies a search based on data.
        - ``ADDRANDDATA`` specifies a search based on address and data.
    """


class TriggerABusBItemI2cAddressValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.

    Description:
        - This command specifies the binary address string used for the I 2 C trigger if the trigger
          condition is ADDRESS or ADDRANDDATA. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue <QString>
        - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?
        ```

    Info:
        - ``<QString>`` is up to 7 or 10-bits depending on the address mode that specifies the
          address. The only allowed characters in the QString are 0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemI2cAddressMode(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.

    Description:
        - This command specifies the I 2 C address mode to 7 or 10-bit. The bus number is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?``
          query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe {ADDR7|ADDR10}
        - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?
        ```

    Info:
        - ``ADDR7`` specifies the 7-bit I2C address mode.
        - ``ADDR10`` specifies the 10-bit I2C address mode.
    """


class TriggerABusBItemI2cAddress(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = TriggerABusBItemI2cAddressMode(device, f"{self._cmd_syntax}:MODe")
        self._value = TriggerABusBItemI2cAddressValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def mode(self) -> TriggerABusBItemI2cAddressMode:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.

        Description:
            - This command specifies the I 2 C address mode to 7 or 10-bit. The bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe {ADDR7|ADDR10}
            - TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe?
            ```

        Info:
            - ``ADDR7`` specifies the 7-bit I2C address mode.
            - ``ADDR10`` specifies the 10-bit I2C address mode.
        """
        return self._mode

    @property
    def value(self) -> TriggerABusBItemI2cAddressValue:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.

        Description:
            - This command specifies the binary address string used for the I 2 C trigger if the
              trigger condition is ADDRESS or ADDRANDDATA. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue <QString>
            - TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue?
            ```

        Info:
            - ``<QString>`` is up to 7 or 10-bits depending on the address mode that specifies the
              address. The only allowed characters in the QString are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemI2c(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:I2C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:I2C:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = TriggerABusBItemI2cAddress(device, f"{self._cmd_syntax}:ADDRess")
        self._condition = TriggerABusBItemI2cCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemI2cData(device, f"{self._cmd_syntax}:DATa")

    @property
    def address(self) -> TriggerABusBItemI2cAddress:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:ADDRess?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:MODe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess:VALue`` command.
        """
        return self._address

    @property
    def condition(self) -> TriggerABusBItemI2cCondition:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:CONDition`` command.

        Description:
            - This command specifies the trigger condition for an I 2 C trigger. The bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:I2C:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:I2C:CONDition {STARt|STOP|REPEATstart|ACKMISS|ADDRess|DATa|ADDRANDDATA}
            - TRIGger:A:BUS:B<x>:I2C:CONDition?
            ```

        Info:
            - ``STARt`` specifies a search based on start condition.
            - ``STOP`` specifies a search based on stop condition.
            - ``REPEATstart`` specifies a search based on repeat of start condition.
            - ``ACKMISS`` specifies a search based on missing acknowledgement condition.
            - ``ADDRess`` specifies a search based on address.
            - ``DATa`` specifies a search based on data.
            - ``ADDRANDDATA`` specifies a search based on address and data.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> TriggerABusBItemI2cData:
        """Return the ``TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.direction``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:DIRection`` command.
            - ``.size``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:I2C:DATa:VALue`` command.
        """
        return self._data


class TriggerABusBItemCanIdentifierValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.

    Description:
        - This command sets the binary address value to be used when triggering on a CAN bus signal.
          The trigger condition must be set to IDANDDATA or DATa (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue <QString>
        - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?
        ```

    Info:
        - ``<QString>`` is up to 29 bits specifying the binary identifier value. The only allowed
          characters in the QString are 0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemCanIdentifierMode(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.

    Description:
        - This command sets the addressing mode (standard or extended format) to be used when
          triggering on a CAN bus signal. The trigger condition must be set to IDANDDATA or DATa
          (using ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTended}
        - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
        ```

    Info:
        - ``STandard`` specifies the standard addressing mode.
        - ``EXTended`` specifies the extended addressing mode.
    """


class TriggerABusBItemCanIdentifier(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:IDentifier?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:IDentifier?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = TriggerABusBItemCanIdentifierMode(device, f"{self._cmd_syntax}:MODe")
        self._value = TriggerABusBItemCanIdentifierValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def mode(self) -> TriggerABusBItemCanIdentifierMode:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.

        Description:
            - This command sets the addressing mode (standard or extended format) to be used when
              triggering on a CAN bus signal. The trigger condition must be set to IDANDDATA or DATa
              (using ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe {STandard|EXTended}
            - TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe?
            ```

        Info:
            - ``STandard`` specifies the standard addressing mode.
            - ``EXTended`` specifies the extended addressing mode.
        """
        return self._mode

    @property
    def value(self) -> TriggerABusBItemCanIdentifierValue:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.

        Description:
            - This command sets the binary address value to be used when triggering on a CAN bus
              signal. The trigger condition must be set to IDANDDATA or DATa (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue <QString>
            - TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue?
            ```

        Info:
            - ``<QString>`` is up to 29 bits specifying the binary identifier value. The only
              allowed characters in the QString are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemCanFrametype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.

    Description:
        - This command sets the frame type (data, remote, error or overload) to be used when
          triggering on a CAN bus signal. The trigger condition must be set to FRAMEtype (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number.The bus number is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:FRAMEtype {DATa|REMote|ERRor|OVERLoad}
        - TRIGger:A:BUS:B<x>:CAN:FRAMEtype?
        ```

    Info:
        - ``DATa`` specifies a data frame type.
        - ``REMote`` specifies a remote frame type.
        - ``ERRor`` specifies an error frame type.
        - ``OVERLoad`` specifies an overload frame type.
    """


class TriggerABusBItemCanFdEsibit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBit`` command.

    Description:
        - This command sets or queries the value of the error state indicator bit (ESI bit) for a
          CAN bus to triggering on. The bus number is specified by x. The trigger condition must be
          set to FDBITS, and the CAN standard must be FDISO or FDNONISO.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBit?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBit?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBit value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:FD:ESIBit {ONE|ZERo|NOCARE}
        - TRIGger:A:BUS:B<x>:CAN:FD:ESIBit?
        ```

    Info:
        - ``ONE`` filters CAN FD packets to only match those where the ESI bit has a value of 1
          (recessive).
        - ``ZERo`` filters CAN FD packets to only match those where the ESI bit has a value of 0
          (dominant).
        - ``NOCARE`` disables filtering of CAN FD packets on the ESI bit.
    """


class TriggerABusBItemCanFdBrsbit(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBit`` command.

    Description:
        - This command sets or queries the value of the bit rate switch bit (BRS bit) for a CAN bus
          to triggering on. The bus number is specified by x. The trigger condition must be set to
          FDBITS, and the CAN standard must be FDISO or FDNONISO.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBit?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBit?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBit value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:FD:BRSBit {ONE|ZERo|NOCARE}
        - TRIGger:A:BUS:B<x>:CAN:FD:BRSBit?
        ```

    Info:
        - ``ONE`` filters CAN FD packets to only match those where the BRS bit has a value of 1
          (fast data enabled).
        - ``ZERo`` filters CAN FD packets to only match those where the BRS bit has a value of 0
          (fast data disabled).
        - ``NOCARE`` disables filtering of CAN FD packets on the BRS bit.
    """


class TriggerABusBItemCanFd(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:FD`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.brsbit``: The ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBit`` command.
        - ``.esibit``: The ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBit`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._brsbit = TriggerABusBItemCanFdBrsbit(device, f"{self._cmd_syntax}:BRSBit")
        self._esibit = TriggerABusBItemCanFdEsibit(device, f"{self._cmd_syntax}:ESIBit")

    @property
    def brsbit(self) -> TriggerABusBItemCanFdBrsbit:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBit`` command.

        Description:
            - This command sets or queries the value of the bit rate switch bit (BRS bit) for a CAN
              bus to triggering on. The bus number is specified by x. The trigger condition must be
              set to FDBITS, and the CAN standard must be FDISO or FDNONISO.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBit?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBit?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBit value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:FD:BRSBit {ONE|ZERo|NOCARE}
            - TRIGger:A:BUS:B<x>:CAN:FD:BRSBit?
            ```

        Info:
            - ``ONE`` filters CAN FD packets to only match those where the BRS bit has a value of 1
              (fast data enabled).
            - ``ZERo`` filters CAN FD packets to only match those where the BRS bit has a value of 0
              (fast data disabled).
            - ``NOCARE`` disables filtering of CAN FD packets on the BRS bit.
        """
        return self._brsbit

    @property
    def esibit(self) -> TriggerABusBItemCanFdEsibit:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBit`` command.

        Description:
            - This command sets or queries the value of the error state indicator bit (ESI bit) for
              a CAN bus to triggering on. The bus number is specified by x. The trigger condition
              must be set to FDBITS, and the CAN standard must be FDISO or FDNONISO.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBit?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBit?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBit value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:FD:ESIBit {ONE|ZERo|NOCARE}
            - TRIGger:A:BUS:B<x>:CAN:FD:ESIBit?
            ```

        Info:
            - ``ONE`` filters CAN FD packets to only match those where the ESI bit has a value of 1
              (recessive).
            - ``ZERo`` filters CAN FD packets to only match those where the ESI bit has a value of 0
              (dominant).
            - ``NOCARE`` disables filtering of CAN FD packets on the ESI bit.
        """
        return self._esibit


class TriggerABusBItemCanErrtype(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:ERRType`` command.

    Description:
        - This command sets or queries the type of error condition for a CAN bus to triggering on.
          The bus number is specified by x. The trigger condition must be set to ERRor.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ERRType?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ERRType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ERRType value``
          command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:ERRType {ACKMISS|BITSTUFFing|FORMERRor|ANYERRor}
        - TRIGger:A:BUS:B<x>:CAN:ERRType?
        ```

    Info:
        - ``ACKMISS`` specifies triggering on a missing ACK field.
        - ``BITSTUFFing`` specifies triggering on a bit stuffing error.
        - ``FORMERRor`` specifies triggering on a CAN FD form error. To use this option, the CAN
          standard must be set to FDISO or FDNONISO.
        - ``ANYERRor`` specifies triggering on any error type.
    """


class TriggerABusBItemCanDataValue(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.

    Description:
        - This command sets the binary data value to be used when triggering on a CAN bus signal.
          The trigger condition must be set to IDANDDATA or DATa (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:DATa:VALue <QString>
        - TRIGger:A:BUS:B<x>:CAN:DATa:VALue?
        ```

    Info:
        - ``<QString>`` is the data value in binary format. The only allowed characters in the
          QString are 0, 1, and X.
    """

    _WRAP_ARG_WITH_QUOTES = True


class TriggerABusBItemCanDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.

    Description:
        - This command sets the length of the data string, in bytes, to be used when triggering on a
          CAN bus signal. The trigger condition must be set to IDANDDATA or DATa (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe <NR1>
        - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?
        ```

    Info:
        - ``<NR1>`` is the length of the data string in bytes.
    """


class TriggerABusBItemCanDataQualifier(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.

    Description:
        - This command sets the qualifier (<, >, =, ≠, ≤, ≥) to be used when triggering on a CAN bus
          signal. The trigger condition must be set to IDANDDATA or DATa (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual}
        - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
        ```

    Info:
        - ``LESSthan`` sets the instrument to trigger when the data is less than the qualifier
          value.
        - ``MOREthan`` sets the instrument to trigger when the data is greater than the qualifier
          value.
        - ``EQual`` sets the instrument to trigger when the data is equal to the qualifier value.
        - ``UNEQual`` sets the instrument to trigger when the data is not equal to the qualifier
          value.
        - ``LESSEQual`` sets the instrument to trigger when the data is less than or equal to the
          qualifier value.
        - ``MOREEQual`` sets the instrument to trigger when the data is greater than or equal to the
          qualifier value.
    """  # noqa: E501


class TriggerABusBItemCanDataOffset(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.

    Description:
        - This command sets or queries the data offset value, in bytes, to use when triggering on
          the CAN data field. The bus number is specified by x. The trigger condition must be set to
          DATA or IDANDDATA.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet <NR1>
        - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?
        ```

    Info:
        - ``<NR1>`` is an integer whose minimum and default values are -1 (don't care), and the
          maximum is up to 7 (for CAN 2.0) or up to 63 (for ISO CAN FD and Non-ISO CAN FD).
    """


class TriggerABusBItemCanDataDirection(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection`` command.

    Description:
        - This command sets the data direction (read, write or 'nocare') to be used to search on a
          CAN bus signal. The trigger condition must be set to IDentifier (using
          ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection {READ|WRITE|NOCARE}
        - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?
        ```

    Info:
        - ``READ`` sets the CAN data direction to READ.
        - ``WRITE`` sets the CAN data direction to WRITE.
        - ``NOCARE`` sets the CAN data direction to either.
    """


class TriggerABusBItemCanData(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.direction``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection`` command.
        - ``.offset``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.
        - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.
        - ``.size``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.
        - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = TriggerABusBItemCanDataDirection(device, f"{self._cmd_syntax}:DIRection")
        self._offset = TriggerABusBItemCanDataOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._qualifier = TriggerABusBItemCanDataQualifier(device, f"{self._cmd_syntax}:QUALifier")
        self._size = TriggerABusBItemCanDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._value = TriggerABusBItemCanDataValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def direction(self) -> TriggerABusBItemCanDataDirection:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection`` command.

        Description:
            - This command sets the data direction (read, write or 'nocare') to be used to search on
              a CAN bus signal. The trigger condition must be set to IDentifier (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection {READ|WRITE|NOCARE}
            - TRIGger:A:BUS:B<x>:CAN:DATa:DIRection?
            ```

        Info:
            - ``READ`` sets the CAN data direction to READ.
            - ``WRITE`` sets the CAN data direction to WRITE.
            - ``NOCARE`` sets the CAN data direction to either.
        """
        return self._direction

    @property
    def offset(self) -> TriggerABusBItemCanDataOffset:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.

        Description:
            - This command sets or queries the data offset value, in bytes, to use when triggering
              on the CAN data field. The bus number is specified by x. The trigger condition must be
              set to DATA or IDANDDATA.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet <NR1>
            - TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet?
            ```

        Info:
            - ``<NR1>`` is an integer whose minimum and default values are -1 (don't care), and the
              maximum is up to 7 (for CAN 2.0) or up to 63 (for ISO CAN FD and Non-ISO CAN FD).
        """
        return self._offset

    @property
    def qualifier(self) -> TriggerABusBItemCanDataQualifier:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.

        Description:
            - This command sets the qualifier (<, >, =, ≠, ≤, ≥) to be used when triggering on a CAN
              bus signal. The trigger condition must be set to IDANDDATA or DATa (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier {LESSthan|MOREthan|EQual|UNEQual|LESSEQual|MOREEQual}
            - TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier?
            ```

        Info:
            - ``LESSthan`` sets the instrument to trigger when the data is less than the qualifier
              value.
            - ``MOREthan`` sets the instrument to trigger when the data is greater than the
              qualifier value.
            - ``EQual`` sets the instrument to trigger when the data is equal to the qualifier
              value.
            - ``UNEQual`` sets the instrument to trigger when the data is not equal to the qualifier
              value.
            - ``LESSEQual`` sets the instrument to trigger when the data is less than or equal to
              the qualifier value.
            - ``MOREEQual`` sets the instrument to trigger when the data is greater than or equal to
              the qualifier value.
        """  # noqa: E501
        return self._qualifier

    @property
    def size(self) -> TriggerABusBItemCanDataSize:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.

        Description:
            - This command sets the length of the data string, in bytes, to be used when triggering
              on a CAN bus signal. The trigger condition must be set to IDANDDATA or DATa (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe <NR1>
            - TRIGger:A:BUS:B<x>:CAN:DATa:SIZe?
            ```

        Info:
            - ``<NR1>`` is the length of the data string in bytes.
        """
        return self._size

    @property
    def value(self) -> TriggerABusBItemCanDataValue:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.

        Description:
            - This command sets the binary data value to be used when triggering on a CAN bus
              signal. The trigger condition must be set to IDANDDATA or DATa (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:DATa:VALue <QString>
            - TRIGger:A:BUS:B<x>:CAN:DATa:VALue?
            ```

        Info:
            - ``<QString>`` is the data value in binary format. The only allowed characters in the
              QString are 0, 1, and X.
        """
        return self._value


class TriggerABusBItemCanCondition(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN:CONDition`` command.

    Description:
        - This command sets the condition (start of frame, frame type, identifier, matching data,
          EOF, missing ACK field, bit-stuffing error) to be used when triggering on a CAN bus
          signal. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:CONDition?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:CONDition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``TRIGger:A:BUS:B<x>:CAN:CONDition value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATa|IDANDDATA|EOF|ERRor|FDBITS}
        - TRIGger:A:BUS:B<x>:CAN:CONDition?
        ```

    Info:
        - ``SOF`` enables triggering on the start of frame.
        - ``FDBITS`` enables triggering on the values of the BRS and ESI bits in an FD packet.
        - ``FRAMEtype`` enables triggering on the type of frame.
        - ``IDentifier`` enables triggering on a matching identifier.
        - ``DATa`` enables triggering on matching data.
        - ``IDANDDATA`` enables triggering on a matching identifier and matching data.
        - ``EOF`` enables triggering on the end of frame.
        - ``ERRor`` enables triggering on a specified error condition.
    """  # noqa: E501


class TriggerABusBItemCan(SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>:CAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.condition``: The ``TRIGger:A:BUS:B<x>:CAN:CONDition`` command.
        - ``.data``: The ``TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.
        - ``.errtype``: The ``TRIGger:A:BUS:B<x>:CAN:ERRType`` command.
        - ``.fd``: The ``TRIGger:A:BUS:B<x>:CAN:FD`` command tree.
        - ``.frametype``: The ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.
        - ``.identifier``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._condition = TriggerABusBItemCanCondition(device, f"{self._cmd_syntax}:CONDition")
        self._data = TriggerABusBItemCanData(device, f"{self._cmd_syntax}:DATa")
        self._errtype = TriggerABusBItemCanErrtype(device, f"{self._cmd_syntax}:ERRType")
        self._fd = TriggerABusBItemCanFd(device, f"{self._cmd_syntax}:FD")
        self._frametype = TriggerABusBItemCanFrametype(device, f"{self._cmd_syntax}:FRAMEtype")
        self._identifier = TriggerABusBItemCanIdentifier(device, f"{self._cmd_syntax}:IDentifier")

    @property
    def condition(self) -> TriggerABusBItemCanCondition:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:CONDition`` command.

        Description:
            - This command sets the condition (start of frame, frame type, identifier, matching
              data, EOF, missing ACK field, bit-stuffing error) to be used when triggering on a CAN
              bus signal. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:CONDition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:CONDition?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:CONDition value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:CONDition {SOF|FRAMEtype|IDentifier|DATa|IDANDDATA|EOF|ERRor|FDBITS}
            - TRIGger:A:BUS:B<x>:CAN:CONDition?
            ```

        Info:
            - ``SOF`` enables triggering on the start of frame.
            - ``FDBITS`` enables triggering on the values of the BRS and ESI bits in an FD packet.
            - ``FRAMEtype`` enables triggering on the type of frame.
            - ``IDentifier`` enables triggering on a matching identifier.
            - ``DATa`` enables triggering on matching data.
            - ``IDANDDATA`` enables triggering on a matching identifier and matching data.
            - ``EOF`` enables triggering on the end of frame.
            - ``ERRor`` enables triggering on a specified error condition.
        """  # noqa: E501
        return self._condition

    @property
    def data(self) -> TriggerABusBItemCanData:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.direction``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:DIRection`` command.
            - ``.offset``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:OFFSet`` command.
            - ``.qualifier``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:QUALifier`` command.
            - ``.size``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:SIZe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:DATa:VALue`` command.
        """
        return self._data

    @property
    def errtype(self) -> TriggerABusBItemCanErrtype:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:ERRType`` command.

        Description:
            - This command sets or queries the type of error condition for a CAN bus to triggering
              on. The bus number is specified by x. The trigger condition must be set to ERRor.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ERRType?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:ERRType?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:ERRType value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:ERRType {ACKMISS|BITSTUFFing|FORMERRor|ANYERRor}
            - TRIGger:A:BUS:B<x>:CAN:ERRType?
            ```

        Info:
            - ``ACKMISS`` specifies triggering on a missing ACK field.
            - ``BITSTUFFing`` specifies triggering on a bit stuffing error.
            - ``FORMERRor`` specifies triggering on a CAN FD form error. To use this option, the CAN
              standard must be set to FDISO or FDNONISO.
            - ``ANYERRor`` specifies triggering on any error type.
        """
        return self._errtype

    @property
    def fd(self) -> TriggerABusBItemCanFd:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:FD`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FD?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.brsbit``: The ``TRIGger:A:BUS:B<x>:CAN:FD:BRSBit`` command.
            - ``.esibit``: The ``TRIGger:A:BUS:B<x>:CAN:FD:ESIBit`` command.
        """
        return self._fd

    @property
    def frametype(self) -> TriggerABusBItemCanFrametype:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.

        Description:
            - This command sets the frame type (data, remote, error or overload) to be used when
              triggering on a CAN bus signal. The trigger condition must be set to FRAMEtype (using
              ``TRIGGER:A:BUS:BX:CAN:CONDITION``). B<x> is the bus number.The bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:B<x>:CAN:FRAMEtype {DATa|REMote|ERRor|OVERLoad}
            - TRIGger:A:BUS:B<x>:CAN:FRAMEtype?
            ```

        Info:
            - ``DATa`` specifies a data frame type.
            - ``REMote`` specifies a remote frame type.
            - ``ERRor`` specifies an error frame type.
            - ``OVERLoad`` specifies an overload frame type.
        """
        return self._frametype

    @property
    def identifier(self) -> TriggerABusBItemCanIdentifier:
        """Return the ``TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN:IDentifier?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``TRIGger:A:BUS:B<x>:CAN:IDentifier?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:MODe`` command.
            - ``.value``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier:VALue`` command.
        """
        return self._identifier


class TriggerABusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``TRIGger:A:BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.can``: The ``TRIGger:A:BUS:B<x>:CAN`` command tree.
        - ``.i2c``: The ``TRIGger:A:BUS:B<x>:I2C`` command tree.
        - ``.lin``: The ``TRIGger:A:BUS:B<x>:LIN`` command tree.
        - ``.parallel``: The ``TRIGger:A:BUS:B<x>:PARallel`` command tree.
        - ``.rs232c``: The ``TRIGger:A:BUS:B<x>:RS232C`` command tree.
        - ``.sent``: The ``TRIGger:A:BUS:B<x>:SENT`` command tree.
        - ``.spi``: The ``TRIGger:A:BUS:B<x>:SPI`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._can = TriggerABusBItemCan(device, f"{self._cmd_syntax}:CAN")
        self._i2c = TriggerABusBItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._lin = TriggerABusBItemLin(device, f"{self._cmd_syntax}:LIN")
        self._parallel = TriggerABusBItemParallel(device, f"{self._cmd_syntax}:PARallel")
        self._rs232c = TriggerABusBItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._sent = TriggerABusBItemSent(device, f"{self._cmd_syntax}:SENT")
        self._spi = TriggerABusBItemSpi(device, f"{self._cmd_syntax}:SPI")

    @property
    def can(self) -> TriggerABusBItemCan:
        """Return the ``TRIGger:A:BUS:B<x>:CAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:CAN?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:CAN?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:CAN:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:CAN:DATa`` command tree.
            - ``.errtype``: The ``TRIGger:A:BUS:B<x>:CAN:ERRType`` command.
            - ``.fd``: The ``TRIGger:A:BUS:B<x>:CAN:FD`` command tree.
            - ``.frametype``: The ``TRIGger:A:BUS:B<x>:CAN:FRAMEtype`` command.
            - ``.identifier``: The ``TRIGger:A:BUS:B<x>:CAN:IDentifier`` command tree.
        """
        return self._can

    @property
    def i2c(self) -> TriggerABusBItemI2c:
        """Return the ``TRIGger:A:BUS:B<x>:I2C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:I2C?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:I2C?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``TRIGger:A:BUS:B<x>:I2C:ADDRess`` command tree.
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:I2C:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:I2C:DATa`` command tree.
        """
        return self._i2c

    @property
    def lin(self) -> TriggerABusBItemLin:
        """Return the ``TRIGger:A:BUS:B<x>:LIN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:LIN?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:LIN?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:LIN:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:LIN:DATa`` command tree.
            - ``.errtype``: The ``TRIGger:A:BUS:B<x>:LIN:ERRTYPE`` command.
            - ``.identifier``: The ``TRIGger:A:BUS:B<x>:LIN:IDentifier`` command tree.
        """
        return self._lin

    @property
    def parallel(self) -> TriggerABusBItemParallel:
        """Return the ``TRIGger:A:BUS:B<x>:PARallel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:PARallel?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:PARallel?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``TRIGger:A:BUS:B<x>:PARallel:DATa`` command tree.
        """
        return self._parallel

    @property
    def rs232c(self) -> TriggerABusBItemRs232c:
        """Return the ``TRIGger:A:BUS:B<x>:RS232C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:RS232C?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:RS232C?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:RS232C:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:RS232C:DATa`` command tree.
        """
        return self._rs232c

    @property
    def sent(self) -> TriggerABusBItemSent:
        """Return the ``TRIGger:A:BUS:B<x>:SENT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SENT?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SENT?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:SENT:CONDition`` command.
            - ``.errtype``: The ``TRIGger:A:BUS:B<x>:SENT:ERRType`` command.
            - ``.fast``: The ``TRIGger:A:BUS:B<x>:SENT:FAST`` command tree.
            - ``.pause``: The ``TRIGger:A:BUS:B<x>:SENT:PAUSE`` command tree.
            - ``.slow``: The ``TRIGger:A:BUS:B<x>:SENT:SLOW`` command tree.
        """
        return self._sent

    @property
    def spi(self) -> TriggerABusBItemSpi:
        """Return the ``TRIGger:A:BUS:B<x>:SPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>:SPI?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>:SPI?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.condition``: The ``TRIGger:A:BUS:B<x>:SPI:CONDition`` command.
            - ``.data``: The ``TRIGger:A:BUS:B<x>:SPI:DATa`` command tree.
        """
        return self._spi


class TriggerABus(SCPICmdRead):
    """The ``TRIGger:A:BUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A:BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.b``: The ``TRIGger:A:BUS:B<x>`` command tree.
        - ``.source``: The ``TRIGger:A:BUS:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._b: Dict[int, TriggerABusBItem] = DefaultDictPassKeyToFactory(
            lambda x: TriggerABusBItem(device, f"{self._cmd_syntax}:B{x}")
        )
        self._source = TriggerABusSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def b(self) -> Dict[int, TriggerABusBItem]:
        """Return the ``TRIGger:A:BUS:B<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:B<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:B<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.can``: The ``TRIGger:A:BUS:B<x>:CAN`` command tree.
            - ``.i2c``: The ``TRIGger:A:BUS:B<x>:I2C`` command tree.
            - ``.lin``: The ``TRIGger:A:BUS:B<x>:LIN`` command tree.
            - ``.parallel``: The ``TRIGger:A:BUS:B<x>:PARallel`` command tree.
            - ``.rs232c``: The ``TRIGger:A:BUS:B<x>:RS232C`` command tree.
            - ``.sent``: The ``TRIGger:A:BUS:B<x>:SENT`` command tree.
            - ``.spi``: The ``TRIGger:A:BUS:B<x>:SPI`` command tree.
        """
        return self._b

    @property
    def source(self) -> TriggerABusSource:
        """Return the ``TRIGger:A:BUS:SOUrce`` command.

        Description:
            - This command sets or queries the source bus for a bus trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:BUS:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - TRIGger:A:BUS:SOUrce B<x>
            - TRIGger:A:BUS:SOUrce?
            ```

        Info:
            - ``B<x>`` sets the selected source to the bus.
        """
        return self._source


#  pylint: disable=too-many-instance-attributes
class TriggerA(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger:A`` command.

    Description:
        - This command sets the A trigger level automatically to 50% of the range of the minimum and
          maximum values of the trigger input signal. The query returns current trigger parameters.
          The trigger level is the voltage threshold through which the trigger source signal must
          pass to generate a trigger event. This command is equivalent to pushing the LEVEL knob on
          the front panel.

    Usage:
        - Using the ``.query()`` method will send the ``TRIGger:A?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIGger:A?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIGger:A value`` command.

    SCPI Syntax:
        ```
        - TRIGger:A SETLevel
        - TRIGger:A?
        ```

    Info:
        - ``SETLevel`` sets the trigger level to 50% of the range of the minimum and maximum values
          of the trigger input signal.

    Properties:
        - ``.bus``: The ``TRIGger:A:BUS`` command tree.
        - ``.edge``: The ``TRIGger:A:EDGE`` command tree.
        - ``.holdoff``: The ``TRIGger:A:HOLDoff`` command tree.
        - ``.level``: The ``TRIGger:A:LEVel`` command tree.
        - ``.logicpattern``: The ``TRIGger:A:LOGICPattern`` command tree.
        - ``.logic``: The ``TRIGger:A:LOGIc`` command tree.
        - ``.lowerthreshold``: The ``TRIGger:A:LOWerthreshold`` command tree.
        - ``.mode``: The ``TRIGger:A:MODe`` command.
        - ``.pulsewidth``: The ``TRIGger:A:PULSEWidth`` command tree.
        - ``.runt``: The ``TRIGger:A:RUNT`` command tree.
        - ``.setholdlogicval``: The ``TRIGger:A:SETHOLDLOGICVAL`` command tree.
        - ``.sethold``: The ``TRIGger:A:SETHold`` command tree.
        - ``.timeout``: The ``TRIGger:A:TIMEOut`` command tree.
        - ``.type``: The ``TRIGger:A:TYPe`` command.
        - ``.upperthreshold``: The ``TRIGger:A:UPPerthreshold`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bus = TriggerABus(device, f"{self._cmd_syntax}:BUS")
        self._edge = TriggerAEdge(device, f"{self._cmd_syntax}:EDGE")
        self._holdoff = TriggerAHoldoff(device, f"{self._cmd_syntax}:HOLDoff")
        self._level = TriggerALevel(device, f"{self._cmd_syntax}:LEVel")
        self._logicpattern = TriggerALogicpattern(device, f"{self._cmd_syntax}:LOGICPattern")
        self._logic = TriggerALogic(device, f"{self._cmd_syntax}:LOGIc")
        self._lowerthreshold = TriggerALowerthreshold(device, f"{self._cmd_syntax}:LOWerthreshold")
        self._mode = TriggerAMode(device, f"{self._cmd_syntax}:MODe")
        self._pulsewidth = TriggerAPulsewidth(device, f"{self._cmd_syntax}:PULSEWidth")
        self._runt = TriggerARunt(device, f"{self._cmd_syntax}:RUNT")
        self._setholdlogicval = TriggerASetholdlogicval(
            device, f"{self._cmd_syntax}:SETHOLDLOGICVAL"
        )
        self._sethold = TriggerASethold(device, f"{self._cmd_syntax}:SETHold")
        self._timeout = TriggerATimeout(device, f"{self._cmd_syntax}:TIMEOut")
        self._type = TriggerAType(device, f"{self._cmd_syntax}:TYPe")
        self._upperthreshold = TriggerAUpperthreshold(device, f"{self._cmd_syntax}:UPPerthreshold")

    @property
    def bus(self) -> TriggerABus:
        """Return the ``TRIGger:A:BUS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:BUS?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:BUS?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.b``: The ``TRIGger:A:BUS:B<x>`` command tree.
            - ``.source``: The ``TRIGger:A:BUS:SOUrce`` command.
        """
        return self._bus

    @property
    def edge(self) -> TriggerAEdge:
        """Return the ``TRIGger:A:EDGE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:EDGE?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.coupling``: The ``TRIGger:A:EDGE:COUPling`` command.
            - ``.slope``: The ``TRIGger:A:EDGE:SLOpe`` command.
            - ``.source``: The ``TRIGger:A:EDGE:SOUrce`` command.
        """
        return self._edge

    @property
    def holdoff(self) -> TriggerAHoldoff:
        """Return the ``TRIGger:A:HOLDoff`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:HOLDoff?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:HOLDoff?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.time``: The ``TRIGger:A:HOLDoff:TIMe`` command.
        """
        return self._holdoff

    @property
    def level(self) -> TriggerALevel:
        """Return the ``TRIGger:A:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LEVel?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``TRIGger:A:LEVel:CH<x>`` command.
        """
        return self._level

    @property
    def logicpattern(self) -> TriggerALogicpattern:
        """Return the ``TRIGger:A:LOGICPattern`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGICPattern?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGICPattern?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``TRIGger:A:LOGICPattern:CH<x>`` command.
            - ``.dch``: The ``TRIGger:A:LOGICPattern:DCH<x>`` command tree.
        """
        return self._logicpattern

    @property
    def logic(self) -> TriggerALogic:
        """Return the ``TRIGger:A:LOGIc`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOGIc?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOGIc?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.deltatime``: The ``TRIGger:A:LOGIc:DELTatime`` command.
            - ``.function``: The ``TRIGger:A:LOGIc:FUNCtion`` command.
            - ``.input``: The ``TRIGger:A:LOGIc:INPut`` command tree.
            - ``.polarity``: The ``TRIGger:A:LOGIc:POLarity`` command.
            - ``.useclockedge``: The ``TRIGger:A:LOGIc:USECLockedge`` command.
            - ``.when``: The ``TRIGger:A:LOGIc:WHEn`` command.
        """
        return self._logic

    @property
    def lowerthreshold(self) -> TriggerALowerthreshold:
        """Return the ``TRIGger:A:LOWerthreshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:LOWerthreshold?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:LOWerthreshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``TRIGger:A:LOWerthreshold:CH<x>`` command.
        """
        return self._lowerthreshold

    @property
    def mode(self) -> TriggerAMode:
        """Return the ``TRIGger:A:MODe`` command.

        Description:
            - This command sets or queries the A trigger mode. This command is equivalent to pushing
              the Mode button on the front panel.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:MODe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:MODe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:MODe {AUTO|NORMal}
            - TRIGger:A:MODe?
            ```

        Info:
            - ``AUTO`` generates a trigger if one is not detected within a specified time period.
            - ``NORMal`` waits for a valid trigger event.
        """
        return self._mode

    @property
    def pulsewidth(self) -> TriggerAPulsewidth:
        """Return the ``TRIGger:A:PULSEWidth`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:PULSEWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:PULSEWidth?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.highlimit``: The ``TRIGger:A:PULSEWidth:HIGHLimit`` command.
            - ``.lowlimit``: The ``TRIGger:A:PULSEWidth:LOWLimit`` command.
            - ``.polarity``: The ``TRIGger:A:PULSEWidth:POLarity`` command.
            - ``.source``: The ``TRIGger:A:PULSEWidth:SOUrce`` command.
            - ``.when``: The ``TRIGger:A:PULSEWidth:WHEn`` command.
        """
        return self._pulsewidth

    @property
    def runt(self) -> TriggerARunt:
        """Return the ``TRIGger:A:RUNT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:RUNT?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:RUNT?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``TRIGger:A:RUNT:POLarity`` command.
            - ``.source``: The ``TRIGger:A:RUNT:SOUrce`` command.
            - ``.when``: The ``TRIGger:A:RUNT:WHEn`` command.
            - ``.width``: The ``TRIGger:A:RUNT:WIDth`` command.
        """
        return self._runt

    @property
    def setholdlogicval(self) -> TriggerASetholdlogicval:
        """Return the ``TRIGger:A:SETHOLDLOGICVAL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHOLDLOGICVAL?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHOLDLOGICVAL?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dch``: The ``TRIGger:A:SETHOLDLOGICVAL:DCH<x>`` command tree.
        """
        return self._setholdlogicval

    @property
    def sethold(self) -> TriggerASethold:
        """Return the ``TRIGger:A:SETHold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:SETHold?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:SETHold?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.clock``: The ``TRIGger:A:SETHold:CLOCk`` command tree.
            - ``.holdtime``: The ``TRIGger:A:SETHold:HOLDTime`` command.
            - ``.settime``: The ``TRIGger:A:SETHold:SETTime`` command.
        """
        return self._sethold

    @property
    def timeout(self) -> TriggerATimeout:
        """Return the ``TRIGger:A:TIMEOut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TIMEOut?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TIMEOut?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``TRIGger:A:TIMEOut:POLarity`` command.
            - ``.source``: The ``TRIGger:A:TIMEOut:SOUrce`` command.
            - ``.time``: The ``TRIGger:A:TIMEOut:TIMe`` command.
        """
        return self._timeout

    @property
    def type(self) -> TriggerAType:
        """Return the ``TRIGger:A:TYPe`` command.

        Description:
            - This command sets or queries the type of A trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A:TYPe value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A:TYPe {EDGE|WIDth|RISE|FALL|TIMEOut|RUNt|LOGIc|SETHold|BUS}
            - TRIGger:A:TYPe?
            ```

        Info:
            - ``EDGE`` is a normal trigger. A trigger event occurs when a signal passes through a
              specified voltage level in a specified direction and is controlled by the
              ``TRIGger:A:EDGE`` commands.
            - ``WIDth`` specifies that the trigger occurs when a pulse with a specified width is
              found.
            - ``RISE`` specifies that the trigger occurs when a pulse with a specified rise is
              found.
            - ``FALL`` specifies that the trigger occurs when a pulse with a specified fall is
              found.
            - ``TIMEOut`` specifies that a trigger occurs when a pulse with the specified timeout is
              found.
            - ``RUNt`` specifies that a trigger occurs when a pulse with the specified parameters is
              found.
            - ``LOGIc`` specifies that a trigger occurs when specified conditions are met and is
              controlled by the ``TRIGger:A:LOGIc`` commands.
            - ``SETHold`` specifies that a trigger occurs when a signal is found that meets the
              setup and hold parameters.
            - ``BUS`` specifies that a trigger occurs when a signal is found that meets the
              specified bus setup parameters.
        """
        return self._type

    @property
    def upperthreshold(self) -> TriggerAUpperthreshold:
        """Return the ``TRIGger:A:UPPerthreshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A:UPPerthreshold?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A:UPPerthreshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``TRIGger:A:UPPerthreshold:CH<x>`` command.
        """
        return self._upperthreshold


class Trigger(SCPICmdWrite, SCPICmdRead):
    """The ``TRIGger`` command.

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
        - ``FORCe`` creates a trigger event. If ``TRIGger:STATE`` is set to READy, the acquisition
          will complete. Otherwise, this command will be ignored. This is equivalent to pressing the
          Force button on the front panel.

    Properties:
        - ``.a``: The ``TRIGger:A`` command.
        - ``.auxlevel``: The ``TRIGger:AUXLevel`` command.
        - ``.hysteresis``: The ``TRIGger:HYSTeresis`` command tree.
        - ``.state``: The ``TRIGger:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "TRIGger") -> None:
        super().__init__(device, cmd_syntax)
        self._a = TriggerA(device, f"{self._cmd_syntax}:A")
        self._auxlevel = TriggerAuxlevel(device, f"{self._cmd_syntax}:AUXLevel")
        self._hysteresis = TriggerHysteresis(device, f"{self._cmd_syntax}:HYSTeresis")
        self._state = TriggerState(device, f"{self._cmd_syntax}:STATE")

    @property
    def a(self) -> TriggerA:
        """Return the ``TRIGger:A`` command.

        Description:
            - This command sets the A trigger level automatically to 50% of the range of the minimum
              and maximum values of the trigger input signal. The query returns current trigger
              parameters. The trigger level is the voltage threshold through which the trigger
              source signal must pass to generate a trigger event. This command is equivalent to
              pushing the LEVEL knob on the front panel.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:A?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:A?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:A value`` command.

        SCPI Syntax:
            ```
            - TRIGger:A SETLevel
            - TRIGger:A?
            ```

        Info:
            - ``SETLevel`` sets the trigger level to 50% of the range of the minimum and maximum
              values of the trigger input signal.

        Sub-properties:
            - ``.bus``: The ``TRIGger:A:BUS`` command tree.
            - ``.edge``: The ``TRIGger:A:EDGE`` command tree.
            - ``.holdoff``: The ``TRIGger:A:HOLDoff`` command tree.
            - ``.level``: The ``TRIGger:A:LEVel`` command tree.
            - ``.logicpattern``: The ``TRIGger:A:LOGICPattern`` command tree.
            - ``.logic``: The ``TRIGger:A:LOGIc`` command tree.
            - ``.lowerthreshold``: The ``TRIGger:A:LOWerthreshold`` command tree.
            - ``.mode``: The ``TRIGger:A:MODe`` command.
            - ``.pulsewidth``: The ``TRIGger:A:PULSEWidth`` command tree.
            - ``.runt``: The ``TRIGger:A:RUNT`` command tree.
            - ``.setholdlogicval``: The ``TRIGger:A:SETHOLDLOGICVAL`` command tree.
            - ``.sethold``: The ``TRIGger:A:SETHold`` command tree.
            - ``.timeout``: The ``TRIGger:A:TIMEOut`` command tree.
            - ``.type``: The ``TRIGger:A:TYPe`` command.
            - ``.upperthreshold``: The ``TRIGger:A:UPPerthreshold`` command tree.
        """
        return self._a

    @property
    def auxlevel(self) -> TriggerAuxlevel:
        """Return the ``TRIGger:AUXLevel`` command.

        Description:
            - For those instruments that have an Auxiliary Input (such as an MSO58LP), this command
              sets or queries the Auxiliary Input voltage level to use for an edge trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:AUXLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:AUXLevel?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIGger:AUXLevel value`` command.

        SCPI Syntax:
            ```
            - TRIGger:AUXLevel {<NR3>|ECL|TTL}
            - TRIGger:AUXLevel?
            ```

        Info:
            - ``<NR3>`` is trigger level in Volts.
            - ``ECL`` sets trigger level to -1.3 Volts.
            - ``TTL`` sets trigger level to 1.4 Volts.
        """
        return self._auxlevel

    @property
    def hysteresis(self) -> TriggerHysteresis:
        """Return the ``TRIGger:HYSTeresis`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:HYSTeresis?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:HYSTeresis?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.user``: The ``TRIGger:HYSTeresis:USER`` command tree.
        """
        return self._hysteresis

    @property
    def state(self) -> TriggerState:
        """Return the ``TRIGger:STATE`` command.

        Description:
            - This query-only command returns the current state of the triggering system.

        Usage:
            - Using the ``.query()`` method will send the ``TRIGger:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIGger:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TRIGger:STATE?
            ```
        """
        return self._state
