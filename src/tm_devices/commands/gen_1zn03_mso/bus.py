# pylint: disable=line-too-long
"""The bus commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - BUS:ADDNew <QString>
    - BUS:B<x>:CAN:BITRate {RATE10K|RATE100K|RATE1M|RATE125K|RATE153K|RATE20K|RATE25K|RATE250K|RATE31K|RATE33K|RATE400K|RATE50K|RATE500K|RATE62K|RATE68K|RATE800K|RATE83K|RATE92K|CUSTom}
    - BUS:B<x>:CAN:BITRate:VALue <NR3>
    - BUS:B<x>:CAN:BITRate:VALue?
    - BUS:B<x>:CAN:BITRate?
    - BUS:B<x>:CAN:FD:BITRate {RATE1M|RATE2M|RATE3M|RATE4M|RATE5M|RATE6M|RATE7M|RATE8M|RATE9M|RATE10M|RATE11M|RATE12M|RATE13M|RATE14M|RATE15M|RATE16M|CUSTom}
    - BUS:B<x>:CAN:FD:BITRate:CUSTom <NR1>
    - BUS:B<x>:CAN:FD:BITRate:CUSTom?
    - BUS:B<x>:CAN:FD:BITRate?
    - BUS:B<x>:CAN:SAMPLEpoint <NR1>
    - BUS:B<x>:CAN:SAMPLEpoint?
    - BUS:B<x>:CAN:SIGNal {DIFFerential|CANH|CANL|RX|TX}
    - BUS:B<x>:CAN:SIGNal?
    - BUS:B<x>:CAN:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:CAN:SOUrce?
    - BUS:B<x>:CAN:STANDard {CAN2X|FDISO|FDNONISO}
    - BUS:B<x>:CAN:STANDard?
    - BUS:B<x>:CAN:THReshold <NR3>
    - BUS:B<x>:CAN:THReshold?
    - BUS:B<x>:DISplay:FORMat {HEX|BINARY|MIXEDASCII|MIXEDHEX|ASCII|DECIMAL|MIXED}
    - BUS:B<x>:DISplay:FORMat?
    - BUS:B<x>:DISplay:LAYout {BUS|BUSANDWAVEFORM}
    - BUS:B<x>:DISplay:LAYout?
    - BUS:B<x>:I2C:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:I2C:CLOCk:SOUrce?
    - BUS:B<x>:I2C:CLOCk:THReshold <NR3>
    - BUS:B<x>:I2C:CLOCk:THReshold?
    - BUS:B<x>:I2C:DATa:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:I2C:DATa:SOUrce?
    - BUS:B<x>:I2C:DATa:THReshold <NR3>
    - BUS:B<x>:I2C:DATa:THReshold?
    - BUS:B<x>:I2C:RWINADDR {0|1}
    - BUS:B<x>:I2C:RWINADDR?
    - BUS:B<x>:LABel:COLor <QString>
    - BUS:B<x>:LABel:COLor?
    - BUS:B<x>:LABel:FONT:BOLD {ON|OFF|1|0}
    - BUS:B<x>:LABel:FONT:BOLD?
    - BUS:B<x>:LABel:FONT:ITALic {ON|OFF|1|0}
    - BUS:B<x>:LABel:FONT:ITALic?
    - BUS:B<x>:LABel:FONT:SIZE <NR1>
    - BUS:B<x>:LABel:FONT:SIZE?
    - BUS:B<x>:LABel:FONT:TYPE <QString>
    - BUS:B<x>:LABel:FONT:TYPE?
    - BUS:B<x>:LABel:FONT:UNDERline {ON|OFF|1|0}
    - BUS:B<x>:LABel:FONT:UNDERline?
    - BUS:B<x>:LABel:XPOS <NR3>
    - BUS:B<x>:LABel:XPOS?
    - BUS:B<x>:LABel:YPOS <NR3>
    - BUS:B<x>:LABel:YPOS?
    - BUS:B<x>:LABel:name <QString>
    - BUS:B<x>:LABel:name?
    - BUS:B<x>:LIN:BITRate {RATE10K|RATE1K|RATE19K|RATE2K|RATE4K|RATE9K|CUSTom}
    - BUS:B<x>:LIN:BITRate:CUSTom <NR1>
    - BUS:B<x>:LIN:BITRate:CUSTom?
    - BUS:B<x>:LIN:BITRate?
    - BUS:B<x>:LIN:IDFORmat {NOPARity|PARity}
    - BUS:B<x>:LIN:IDFORmat?
    - BUS:B<x>:LIN:POLarity {INVerted|NORmal}
    - BUS:B<x>:LIN:POLarity?
    - BUS:B<x>:LIN:SAMPLEpoint <NR1>
    - BUS:B<x>:LIN:SAMPLEpoint?
    - BUS:B<x>:LIN:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:LIN:SOUrce:THReshold <NR3>
    - BUS:B<x>:LIN:SOUrce:THReshold?
    - BUS:B<x>:LIN:SOUrce?
    - BUS:B<x>:LIN:STANDard {MIXed|V1X|V2X}
    - BUS:B<x>:LIN:STANDard?
    - BUS:B<x>:PARallel:ALLTHResholds <NR3>
    - BUS:B<x>:PARallel:ALLTHResholds:APPly
    - BUS:B<x>:PARallel:ALLTHResholds?
    - BUS:B<x>:PARallel:BIT<x>SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
    - BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold <NR3>
    - BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold?
    - BUS:B<x>:PARallel:BIT<x>SOUrce?
    - BUS:B<x>:PARallel:CLOCk:EDGE {FALLING|RISING|EITHER}
    - BUS:B<x>:PARallel:CLOCk:EDGE?
    - BUS:B<x>:PARallel:CLOCk:ISCLOCKED {ON|OFF|<NR1>}
    - BUS:B<x>:PARallel:CLOCk:ISCLOCKED?
    - BUS:B<x>:PARallel:CLOCkSOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
    - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold <NR3>
    - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?
    - BUS:B<x>:PARallel:CLOCkSOUrce?
    - BUS:B<x>:RS232C:BITRate {CUSTOM|RATE300|RATE1K|RATE2K|RATE9K|RATE19K|RATE38K|RATE115K|RATE921K}
    - BUS:B<x>:RS232C:BITRate:CUSTom <NR1>
    - BUS:B<x>:RS232C:BITRate:CUSTom?
    - BUS:B<x>:RS232C:BITRate?
    - BUS:B<x>:RS232C:DATABits {<NR1>}
    - BUS:B<x>:RS232C:DATABits?
    - BUS:B<x>:RS232C:DELIMiter {NULl|CR|LF|SPace|XFF}
    - BUS:B<x>:RS232C:DELIMiter?
    - BUS:B<x>:RS232C:DISplaymode {FRame|PACKET}
    - BUS:B<x>:RS232C:DISplaymode?
    - BUS:B<x>:RS232C:PARity {NONe|EVEN|ODD}
    - BUS:B<x>:RS232C:PARity?
    - BUS:B<x>:RS232C:POLarity {NORmal|INVERTed}
    - BUS:B<x>:RS232C:POLarity?
    - BUS:B<x>:RS232C:SOUrce {CH<x>|DCH<x>_D<x>|REF<x>|MATH<x>|REF<x>_D<x>}
    - BUS:B<x>:RS232C:SOUrce:THReshold <NR3>
    - BUS:B<x>:RS232C:SOUrce:THReshold?
    - BUS:B<x>:RS232C:SOUrce?
    - BUS:B<x>:SENT:CHANWidth {TWELVEtwelve|FOURTEENten|SIXTEENeight}
    - BUS:B<x>:SENT:CHANWidth?
    - BUS:B<x>:SENT:NIBBLECount {THREE|FOUR|SIX}
    - BUS:B<x>:SENT:NIBBLECount?
    - BUS:B<x>:SENT:NUMCHANnel {ONE|TWO}
    - BUS:B<x>:SENT:NUMCHANnel?
    - BUS:B<x>:SENT:PAUSEPULSe {NO|YES}
    - BUS:B<x>:SENT:PAUSEPULSe?
    - BUS:B<x>:SENT:POLARITY {INVerted|NORmal}
    - BUS:B<x>:SENT:POLARITY?
    - BUS:B<x>:SENT:SLOW {NOne|ENHANCED4|ENHANCED8|SHOrt}
    - BUS:B<x>:SENT:SLOW?
    - BUS:B<x>:SENT:SOUrce {CH<x>|DCH<x>_D<x>|Math<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:SENT:SOUrce?
    - BUS:B<x>:SENT:THRESHold <NR3>
    - BUS:B<x>:SENT:THRESHold?
    - BUS:B<x>:SENT:TICKTIME <NR3>
    - BUS:B<x>:SENT:TICKTIME?
    - BUS:B<x>:SENT:TICKTOLerance <NR3>
    - BUS:B<x>:SENT:TICKTOLerance?
    - BUS:B<x>:SPI:BITOrder {LSB|MSB}
    - BUS:B<x>:SPI:BITOrder?
    - BUS:B<x>:SPI:CLOCk:POLarity {FALL|RISE}
    - BUS:B<x>:SPI:CLOCk:POLarity?
    - BUS:B<x>:SPI:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:SPI:CLOCk:SOUrce?
    - BUS:B<x>:SPI:CLOCk:THReshold <NR3>
    - BUS:B<x>:SPI:CLOCk:THReshold?
    - BUS:B<x>:SPI:DATa:POLarity {HIGH|LOW}
    - BUS:B<x>:SPI:DATa:POLarity?
    - BUS:B<x>:SPI:DATa:SIZe <NR1>
    - BUS:B<x>:SPI:DATa:SIZe?
    - BUS:B<x>:SPI:DATa:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:SPI:DATa:SOUrce?
    - BUS:B<x>:SPI:DATa:THReshold <NR3>
    - BUS:B<x>:SPI:DATa:THReshold?
    - BUS:B<x>:SPI:FRAMING {IDLE|SS}
    - BUS:B<x>:SPI:FRAMING?
    - BUS:B<x>:SPI:IDLETime <NR3>
    - BUS:B<x>:SPI:IDLETime?
    - BUS:B<x>:SPI:MISo:DATa:POLarity {HIGH|LOW}
    - BUS:B<x>:SPI:MISo:DATa:POLarity?
    - BUS:B<x>:SPI:MISo:INPut {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SPI:MISo:INPut?
    - BUS:B<x>:SPI:MISo:THReshold <NR3>
    - BUS:B<x>:SPI:MISo:THReshold?
    - BUS:B<x>:SPI:MOSi:DATa:POLarity {HIGH|LOW}
    - BUS:B<x>:SPI:MOSi:DATa:POLarity?
    - BUS:B<x>:SPI:MOSi:INPut {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
    - BUS:B<x>:SPI:MOSi:INPut?
    - BUS:B<x>:SPI:MOSi:THReshold <NR3>
    - BUS:B<x>:SPI:MOSi:THReshold?
    - BUS:B<x>:SPI:NUMBer:INputs {ONE|TWO}
    - BUS:B<x>:SPI:NUMBer:INputs?
    - BUS:B<x>:SPI:SELect:POLarity {LOW|HIGH}
    - BUS:B<x>:SPI:SELect:POLarity?
    - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
    - BUS:B<x>:SPI:SELect:SOUrce?
    - BUS:B<x>:SPI:SELect:THReshold <NR3>
    - BUS:B<x>:SPI:SELect:THReshold?
    - BUS:B<x>:TYPe {CAN|I2C|LIN|PARallel|RS232C|SENT|SPI}
    - BUS:B<x>:TYPe?
    - BUS:DELete <QString>
    - BUS:LIST?
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


class BusList(SCPICmdRead):
    """The ``BUS:LIST`` command.

    Description:
        - This query returns a comma separated list of all currently defined buses.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - BUS:LIST?
        ```
    """


class BusDelete(SCPICmdWrite):
    """The ``BUS:DELete`` command.

    Description:
        - This command deletes the specified bus.

    Usage:
        - Using the ``.write(value)`` method will send the ``BUS:DELete value`` command.

    SCPI Syntax:
        ```
        - BUS:DELete <QString>
        ```

    Info:
        - ``<QString>`` specifies the bus to delete and is of the form 'B<NR1>', where <NR1> is ≥1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class BusBItemType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:TYPe`` command.

    Description:
        - This command sets or queries the bus type or standard for the specified bus. The bus is
          specified by x. Arguments for a bus type are only available then the required serial bus
          option is installed.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:TYPe {CAN|I2C|LIN|PARallel|RS232C|SENT|SPI}
        - BUS:B<x>:TYPe?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``CAN`` specifies a Controller Area Network bus.
        - ``I2C`` specifies the Inter-IC bus.
        - ``LIN`` specifies a Local Interconnect Network bus.
        - ``PARallel`` specifies a parallel bus.
        - ``RS232C`` specifies the RS-232 Serial bus.
        - ``SENT`` specifies the Single Edge Nibble Transmission (SENT) automotive serial bus.
        - ``SPI`` specifies the Serial Peripheral Interface bus.
    """


class BusBItemSpiSelectThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect:THReshold`` command.

    Description:
        - This command sets or queries the SPI Select (SS) source threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SELect:THReshold <NR3>
        - BUS:B<x>:SPI:SELect:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SPI Select (SS) source threshold for the specified bus.
    """


class BusBItemSpiSelectSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect:SOUrce`` command.

    Description:
        - This command sets or queries the SPI Slave Select (SS) source for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:SPI:SELect:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``CH<x>`` designates an analog channel as the bus SPI Slave Select source.
        - ``DCH<x>_D<x>`` designates a digital channel as the bus SPI Slave Select source. The
          supported digital channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` designates a math waveform as the Slave Select source.
        - ``REF<x>`` designates a reference waveform as the Slave Select source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified SPI bus.
    """


class BusBItemSpiSelectPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect:POLarity`` command.

    Description:
        - This command sets or queries the SPI Slave Select (SS) polarity for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SELect:POLarity {LOW|HIGH}
        - BUS:B<x>:SPI:SELect:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``LOW`` sets an active low polarity.
        - ``HIGH`` sets an active high polarity.
    """


class BusBItemSpiSelect(SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:SELect:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:SELect:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SPI:SELect:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiSelectPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiSelectSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSpiSelectThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def polarity(self) -> BusBItemSpiSelectPolarity:
        """Return the ``BUS:B<x>:SPI:SELect:POLarity`` command.

        Description:
            - This command sets or queries the SPI Slave Select (SS) polarity for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:SELect:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SELect:POLarity {LOW|HIGH}
            - BUS:B<x>:SPI:SELect:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``LOW`` sets an active low polarity.
            - ``HIGH`` sets an active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiSelectSource:
        """Return the ``BUS:B<x>:SPI:SELect:SOUrce`` command.

        Description:
            - This command sets or queries the SPI Slave Select (SS) source for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:SPI:SELect:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``CH<x>`` designates an analog channel as the bus SPI Slave Select source.
            - ``DCH<x>_D<x>`` designates a digital channel as the bus SPI Slave Select source. The
              supported digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``MATH<x>`` designates a math waveform as the Slave Select source.
            - ``REF<x>`` designates a reference waveform as the Slave Select source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified SPI bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSpiSelectThreshold:
        """Return the ``BUS:B<x>:SPI:SELect:THReshold`` command.

        Description:
            - This command sets or queries the SPI Select (SS) source threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:SELect:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SELect:THReshold <NR3>
            - BUS:B<x>:SPI:SELect:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SPI Select (SS) source threshold for the specified bus.
        """
        return self._threshold


class BusBItemSpiNumberInputs(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:NUMBer:INputs`` command.

    Description:
        - This command sets or queries the number of inputs for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:NUMBer:INputs {ONE|TWO}
        - BUS:B<x>:SPI:NUMBer:INputs?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``ONE`` sets the Data Inputs as one.
        - ``TWO`` sets the Data Inputs as two.
    """


class BusBItemSpiNumber(SCPICmdRead):
    """The ``BUS:B<x>:SPI:NUMBer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:NUMBer?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:NUMBer?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.inputs``: The ``BUS:B<x>:SPI:NUMBer:INputs`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._inputs = BusBItemSpiNumberInputs(device, f"{self._cmd_syntax}:INputs")

    @property
    def inputs(self) -> BusBItemSpiNumberInputs:
        """Return the ``BUS:B<x>:SPI:NUMBer:INputs`` command.

        Description:
            - This command sets or queries the number of inputs for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:NUMBer:INputs value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:NUMBer:INputs {ONE|TWO}
            - BUS:B<x>:SPI:NUMBer:INputs?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``ONE`` sets the Data Inputs as one.
            - ``TWO`` sets the Data Inputs as two.
        """
        return self._inputs


class BusBItemSpiMosiThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MOSi:THReshold`` command.

    Description:
        - This command sets or queries the SPI MOSI source thresold for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MOSi:THReshold <NR3>
        - BUS:B<x>:SPI:MOSi:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SPI MOSI Data source threshold for the specified bus.
    """


class BusBItemSpiMosiInput(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MOSi:INPut`` command.

    Description:
        - This command sets or queries the SPI MOSI source for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:INPut?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:INPut?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MOSi:INPut value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MOSi:INPut {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SPI:MOSi:INPut?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``CH<x>`` designates an analog channel as the source.
        - ``DCH<x>_D<x>`` designates the channel bit of separate digital channel as the source. The
          supported digital channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` designates a math waveform as the source.
        - ``REF<x>`` designates a reference waveform as the source.
    """


class BusBItemSpiMosiDataPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MOSi:DATa:POLarity`` command.

    Description:
        - This command sets or queries the SPI MOSI source polarity for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:DATa:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:DATa:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MOSi:DATa:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MOSi:DATa:POLarity {HIGH|LOW}
        - BUS:B<x>:SPI:MOSi:DATa:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``HIGH`` sets the polarity to high.
        - ``LOW`` sets the polarity to low.
    """


class BusBItemSpiMosiData(SCPICmdRead):
    """The ``BUS:B<x>:SPI:MOSi:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:DATa?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:MOSi:DATa:POLarity`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiMosiDataPolarity(device, f"{self._cmd_syntax}:POLarity")

    @property
    def polarity(self) -> BusBItemSpiMosiDataPolarity:
        """Return the ``BUS:B<x>:SPI:MOSi:DATa:POLarity`` command.

        Description:
            - This command sets or queries the SPI MOSI source polarity for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:DATa:POLarity?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:DATa:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:MOSi:DATa:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MOSi:DATa:POLarity {HIGH|LOW}
            - BUS:B<x>:SPI:MOSi:DATa:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``HIGH`` sets the polarity to high.
            - ``LOW`` sets the polarity to low.
        """
        return self._polarity


class BusBItemSpiMosi(SCPICmdRead):
    """The ``BUS:B<x>:SPI:MOSi`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.data``: The ``BUS:B<x>:SPI:MOSi:DATa`` command tree.
        - ``.input``: The ``BUS:B<x>:SPI:MOSi:INPut`` command.
        - ``.threshold``: The ``BUS:B<x>:SPI:MOSi:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = BusBItemSpiMosiData(device, f"{self._cmd_syntax}:DATa")
        self._input = BusBItemSpiMosiInput(device, f"{self._cmd_syntax}:INPut")
        self._threshold = BusBItemSpiMosiThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def data(self) -> BusBItemSpiMosiData:
        """Return the ``BUS:B<x>:SPI:MOSi:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:DATa?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:MOSi:DATa:POLarity`` command.
        """
        return self._data

    @property
    def input(self) -> BusBItemSpiMosiInput:
        """Return the ``BUS:B<x>:SPI:MOSi:INPut`` command.

        Description:
            - This command sets or queries the SPI MOSI source for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:INPut?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:INPut?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MOSi:INPut value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MOSi:INPut {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SPI:MOSi:INPut?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``CH<x>`` designates an analog channel as the source.
            - ``DCH<x>_D<x>`` designates the channel bit of separate digital channel as the source.
              The supported digital channel value is 1. The supported digital bit values are 0 to
              15.
            - ``MATH<x>`` designates a math waveform as the source.
            - ``REF<x>`` designates a reference waveform as the source.
        """
        return self._input

    @property
    def threshold(self) -> BusBItemSpiMosiThreshold:
        """Return the ``BUS:B<x>:SPI:MOSi:THReshold`` command.

        Description:
            - This command sets or queries the SPI MOSI source thresold for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MOSi:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MOSi:THReshold <NR3>
            - BUS:B<x>:SPI:MOSi:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SPI MOSI Data source threshold for the specified bus.
        """
        return self._threshold


class BusBItemSpiMisoThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MISo:THReshold`` command.

    Description:
        - This command sets or queries the SPI MISo Data source threshold for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MISo:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MISo:THReshold <NR3>
        - BUS:B<x>:SPI:MISo:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SPI MISo Data source threshold for the specified bus.
    """


class BusBItemSpiMisoInput(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MISo:INPut`` command.

    Description:
        - This command sets or queries the SPI MISo source for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:INPut?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:INPut?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MISo:INPut value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MISo:INPut {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
        - BUS:B<x>:SPI:MISo:INPut?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``CH<x>`` designates an analog channel as the source.
        - ``DCH<x>_D<x>`` specifies the channel bit of separate digital channel as the source. The
          supported digital channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` designates a math waveform as the source.
        - ``REF<x>`` designates a reference waveform as the source.
    """


class BusBItemSpiMisoDataPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:MISo:DATa:POLarity`` command.

    Description:
        - This command sets or queries the SPI MISo Data source polarity for the specified bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:DATa:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:DATa:POLarity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MISo:DATa:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:MISo:DATa:POLarity {HIGH|LOW}
        - BUS:B<x>:SPI:MISo:DATa:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``HIGH`` sets the polarity to high.
        - ``LOW`` sets the polarity to low.
    """


class BusBItemSpiMisoData(SCPICmdRead):
    """The ``BUS:B<x>:SPI:MISo:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:DATa?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:MISo:DATa:POLarity`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiMisoDataPolarity(device, f"{self._cmd_syntax}:POLarity")

    @property
    def polarity(self) -> BusBItemSpiMisoDataPolarity:
        """Return the ``BUS:B<x>:SPI:MISo:DATa:POLarity`` command.

        Description:
            - This command sets or queries the SPI MISo Data source polarity for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:DATa:POLarity?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:DATa:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:MISo:DATa:POLarity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MISo:DATa:POLarity {HIGH|LOW}
            - BUS:B<x>:SPI:MISo:DATa:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``HIGH`` sets the polarity to high.
            - ``LOW`` sets the polarity to low.
        """
        return self._polarity


class BusBItemSpiMiso(SCPICmdRead):
    """The ``BUS:B<x>:SPI:MISo`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.data``: The ``BUS:B<x>:SPI:MISo:DATa`` command tree.
        - ``.input``: The ``BUS:B<x>:SPI:MISo:INPut`` command.
        - ``.threshold``: The ``BUS:B<x>:SPI:MISo:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = BusBItemSpiMisoData(device, f"{self._cmd_syntax}:DATa")
        self._input = BusBItemSpiMisoInput(device, f"{self._cmd_syntax}:INPut")
        self._threshold = BusBItemSpiMisoThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def data(self) -> BusBItemSpiMisoData:
        """Return the ``BUS:B<x>:SPI:MISo:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:DATa?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:MISo:DATa:POLarity`` command.
        """
        return self._data

    @property
    def input(self) -> BusBItemSpiMisoInput:
        """Return the ``BUS:B<x>:SPI:MISo:INPut`` command.

        Description:
            - This command sets or queries the SPI MISo source for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:INPut?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:INPut?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MISo:INPut value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MISo:INPut {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
            - BUS:B<x>:SPI:MISo:INPut?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``CH<x>`` designates an analog channel as the source.
            - ``DCH<x>_D<x>`` specifies the channel bit of separate digital channel as the source.
              The supported digital channel value is 1. The supported digital bit values are 0 to
              15.
            - ``MATH<x>`` designates a math waveform as the source.
            - ``REF<x>`` designates a reference waveform as the source.
        """
        return self._input

    @property
    def threshold(self) -> BusBItemSpiMisoThreshold:
        """Return the ``BUS:B<x>:SPI:MISo:THReshold`` command.

        Description:
            - This command sets or queries the SPI MISo Data source threshold for the specified bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:MISo:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:MISo:THReshold <NR3>
            - BUS:B<x>:SPI:MISo:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SPI MISo Data source threshold for the specified bus.
        """
        return self._threshold


class BusBItemSpiIdletime(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:IDLETime`` command.

    Description:
        - This command sets or queries the SPI idle time for the specified bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:IDLETime value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:IDLETime <NR3>
        - BUS:B<x>:SPI:IDLETime?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` specifies the SPI idle time.
    """


class BusBItemSpiFraming(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:FRAMING`` command.

    Description:
        - This command sets or queries the SPI framing setting for the specified bus. The bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:FRAMING value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:FRAMING {IDLE|SS}
        - BUS:B<x>:SPI:FRAMING?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``IDLE`` specifies IDLE SPI framing.
        - ``SS`` specifies SS SPI framing.
    """


class BusBItemSpiDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:THReshold`` command.

    Description:
        - This command sets or queries the SPI Data (Data) source threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:THReshold <NR3>
        - BUS:B<x>:SPI:DATa:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SPI Data (SDA) source threshold for the specified bus.
    """


class BusBItemSpiDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:SOUrce`` command.

    Description:
        - This command sets or queries the SPI Data (Data) source for the bus number specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:SPI:DATa:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``CH<x>`` designates an analog channel as the data source for the specified SPI bus.
        - ``DCH<x>_D<x>`` specifies the digital channel as the bus SPI clock source. The supported
          digital channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` designates a math waveform as the data source.
        - ``REF<x>`` designates a reference waveform as the data source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform for the
          specified SPI bus.
    """


class BusBItemSpiDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:SIZe`` command.

    Description:
        - This command sets or queries the number of bits per word for the specified SPI bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:SIZe <NR1>
        - BUS:B<x>:SPI:DATa:SIZe?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR1>`` is the data size for the specified bus. The minimum value is 2 and maximum is
          32.
    """


class BusBItemSpiDataPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa:POLarity`` command.

    Description:
        - This command sets or queries the SPI Data (Data) source polarity for the bus number
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATa:POLarity {HIGH|LOW}
        - BUS:B<x>:SPI:DATa:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``HIGH`` sets the SPI data polarity to active high.
        - ``LOW`` sets the SPI data polarity to active low.
    """


class BusBItemSpiData(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:DATa:POLarity`` command.
        - ``.size``: The ``BUS:B<x>:SPI:DATa:SIZe`` command.
        - ``.source``: The ``BUS:B<x>:SPI:DATa:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SPI:DATa:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiDataPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._size = BusBItemSpiDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._source = BusBItemSpiDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSpiDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def polarity(self) -> BusBItemSpiDataPolarity:
        """Return the ``BUS:B<x>:SPI:DATa:POLarity`` command.

        Description:
            - This command sets or queries the SPI Data (Data) source polarity for the bus number
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:POLarity {HIGH|LOW}
            - BUS:B<x>:SPI:DATa:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``HIGH`` sets the SPI data polarity to active high.
            - ``LOW`` sets the SPI data polarity to active low.
        """
        return self._polarity

    @property
    def size(self) -> BusBItemSpiDataSize:
        """Return the ``BUS:B<x>:SPI:DATa:SIZe`` command.

        Description:
            - This command sets or queries the number of bits per word for the specified SPI bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SIZe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:SIZe <NR1>
            - BUS:B<x>:SPI:DATa:SIZe?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR1>`` is the data size for the specified bus. The minimum value is 2 and maximum
              is 32.
        """
        return self._size

    @property
    def source(self) -> BusBItemSpiDataSource:
        """Return the ``BUS:B<x>:SPI:DATa:SOUrce`` command.

        Description:
            - This command sets or queries the SPI Data (Data) source for the bus number specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:SPI:DATa:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``CH<x>`` designates an analog channel as the data source for the specified SPI bus.
            - ``DCH<x>_D<x>`` specifies the digital channel as the bus SPI clock source. The
              supported digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``MATH<x>`` designates a math waveform as the data source.
            - ``REF<x>`` designates a reference waveform as the data source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform for
              the specified SPI bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSpiDataThreshold:
        """Return the ``BUS:B<x>:SPI:DATa:THReshold`` command.

        Description:
            - This command sets or queries the SPI Data (Data) source threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATa:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATa:THReshold <NR3>
            - BUS:B<x>:SPI:DATa:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SPI Data (SDA) source threshold for the specified bus.
        """
        return self._threshold


class BusBItemSpiClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the SPI Clock (SCLK) source threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:CLOCk:THReshold <NR3>
        - BUS:B<x>:SPI:CLOCk:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SPI Clock (SCLK) source threshold for the specified bus.
    """


class BusBItemSpiClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the SPI clock (SCLK) source for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:SPI:CLOCk:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``CH<x>`` designates an analog channel as the bus SPI clock source.
        - ``DCH<x>_D<x>`` specifies the digital channel as the bus SPI clock source. The supported
          digital channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` designates a math waveform as the clock source.
        - ``REF<x>`` designates a reference waveform as the clock source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified SPI bus.
    """


class BusBItemSpiClockPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk:POLarity`` command.

    Description:
        - This command sets or queries the SPI clock (SCLK) source polarity for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:CLOCk:POLarity {FALL|RISE}
        - BUS:B<x>:SPI:CLOCk:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``FALL`` sets the clock to the falling edge of the signal.
        - ``RISE`` sets the clock to the rising edge of the signal.
    """


class BusBItemSpiClock(SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:CLOCk:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SPI:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiClockPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemSpiClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSpiClockThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def polarity(self) -> BusBItemSpiClockPolarity:
        """Return the ``BUS:B<x>:SPI:CLOCk:POLarity`` command.

        Description:
            - This command sets or queries the SPI clock (SCLK) source polarity for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:CLOCk:POLarity {FALL|RISE}
            - BUS:B<x>:SPI:CLOCk:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``FALL`` sets the clock to the falling edge of the signal.
            - ``RISE`` sets the clock to the rising edge of the signal.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiClockSource:
        """Return the ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the SPI clock (SCLK) source for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:SPI:CLOCk:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``CH<x>`` designates an analog channel as the bus SPI clock source.
            - ``DCH<x>_D<x>`` specifies the digital channel as the bus SPI clock source. The
              supported digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``MATH<x>`` designates a math waveform as the clock source.
            - ``REF<x>`` designates a reference waveform as the clock source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified SPI bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSpiClockThreshold:
        """Return the ``BUS:B<x>:SPI:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the SPI Clock (SCLK) source threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:CLOCk:THReshold <NR3>
            - BUS:B<x>:SPI:CLOCk:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SPI Clock (SCLK) source threshold for the specified bus.
        """
        return self._threshold


class BusBItemSpiBitorder(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:BITOrder`` command.

    Description:
        - This command sets or queries the SPI bit order for the specified bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:BITOrder?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:BITOrder?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:BITOrder value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:BITOrder {LSB|MSB}
        - BUS:B<x>:SPI:BITOrder?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``LSB`` specifies that each bit becomes the recovered value's new LSB, after shifting
          previously recovered bits one place to the left. The decoding happens right to left.
        - ``MSB`` specifies that each successive bit from the bus's data line becomes the new MSB of
          the recovered value, shifting any previously recovered bits one place to the right. The
          decoding happens left to right.
    """


#  pylint: disable=too-many-instance-attributes
class BusBItemSpi(SCPICmdRead):
    """The ``BUS:B<x>:SPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.bitorder``: The ``BUS:B<x>:SPI:BITOrder`` command.
        - ``.clock``: The ``BUS:B<x>:SPI:CLOCk`` command tree.
        - ``.data``: The ``BUS:B<x>:SPI:DATa`` command tree.
        - ``.framing``: The ``BUS:B<x>:SPI:FRAMING`` command.
        - ``.idletime``: The ``BUS:B<x>:SPI:IDLETime`` command.
        - ``.miso``: The ``BUS:B<x>:SPI:MISo`` command tree.
        - ``.mosi``: The ``BUS:B<x>:SPI:MOSi`` command tree.
        - ``.number``: The ``BUS:B<x>:SPI:NUMBer`` command tree.
        - ``.select``: The ``BUS:B<x>:SPI:SELect`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitorder = BusBItemSpiBitorder(device, f"{self._cmd_syntax}:BITOrder")
        self._clock = BusBItemSpiClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = BusBItemSpiData(device, f"{self._cmd_syntax}:DATa")
        self._framing = BusBItemSpiFraming(device, f"{self._cmd_syntax}:FRAMING")
        self._idletime = BusBItemSpiIdletime(device, f"{self._cmd_syntax}:IDLETime")
        self._miso = BusBItemSpiMiso(device, f"{self._cmd_syntax}:MISo")
        self._mosi = BusBItemSpiMosi(device, f"{self._cmd_syntax}:MOSi")
        self._number = BusBItemSpiNumber(device, f"{self._cmd_syntax}:NUMBer")
        self._select = BusBItemSpiSelect(device, f"{self._cmd_syntax}:SELect")

    @property
    def bitorder(self) -> BusBItemSpiBitorder:
        """Return the ``BUS:B<x>:SPI:BITOrder`` command.

        Description:
            - This command sets or queries the SPI bit order for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:BITOrder?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:BITOrder?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:BITOrder value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:BITOrder {LSB|MSB}
            - BUS:B<x>:SPI:BITOrder?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``LSB`` specifies that each bit becomes the recovered value's new LSB, after shifting
              previously recovered bits one place to the left. The decoding happens right to left.
            - ``MSB`` specifies that each successive bit from the bus's data line becomes the new
              MSB of the recovered value, shifting any previously recovered bits one place to the
              right. The decoding happens left to right.
        """
        return self._bitorder

    @property
    def clock(self) -> BusBItemSpiClock:
        """Return the ``BUS:B<x>:SPI:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:CLOCk:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SPI:CLOCk:THReshold`` command.
        """
        return self._clock

    @property
    def data(self) -> BusBItemSpiData:
        """Return the ``BUS:B<x>:SPI:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:DATa:POLarity`` command.
            - ``.size``: The ``BUS:B<x>:SPI:DATa:SIZe`` command.
            - ``.source``: The ``BUS:B<x>:SPI:DATa:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SPI:DATa:THReshold`` command.
        """
        return self._data

    @property
    def framing(self) -> BusBItemSpiFraming:
        """Return the ``BUS:B<x>:SPI:FRAMING`` command.

        Description:
            - This command sets or queries the SPI framing setting for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:FRAMING value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:FRAMING {IDLE|SS}
            - BUS:B<x>:SPI:FRAMING?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``IDLE`` specifies IDLE SPI framing.
            - ``SS`` specifies SS SPI framing.
        """
        return self._framing

    @property
    def idletime(self) -> BusBItemSpiIdletime:
        """Return the ``BUS:B<x>:SPI:IDLETime`` command.

        Description:
            - This command sets or queries the SPI idle time for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:IDLETime?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:IDLETime value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:IDLETime <NR3>
            - BUS:B<x>:SPI:IDLETime?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` specifies the SPI idle time.
        """
        return self._idletime

    @property
    def miso(self) -> BusBItemSpiMiso:
        """Return the ``BUS:B<x>:SPI:MISo`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MISo?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MISo?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.data``: The ``BUS:B<x>:SPI:MISo:DATa`` command tree.
            - ``.input``: The ``BUS:B<x>:SPI:MISo:INPut`` command.
            - ``.threshold``: The ``BUS:B<x>:SPI:MISo:THReshold`` command.
        """
        return self._miso

    @property
    def mosi(self) -> BusBItemSpiMosi:
        """Return the ``BUS:B<x>:SPI:MOSi`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:MOSi?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:MOSi?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.data``: The ``BUS:B<x>:SPI:MOSi:DATa`` command tree.
            - ``.input``: The ``BUS:B<x>:SPI:MOSi:INPut`` command.
            - ``.threshold``: The ``BUS:B<x>:SPI:MOSi:THReshold`` command.
        """
        return self._mosi

    @property
    def number(self) -> BusBItemSpiNumber:
        """Return the ``BUS:B<x>:SPI:NUMBer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:NUMBer?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:NUMBer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.inputs``: The ``BUS:B<x>:SPI:NUMBer:INputs`` command.
        """
        return self._number

    @property
    def select(self) -> BusBItemSpiSelect:
        """Return the ``BUS:B<x>:SPI:SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:SELect:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:SELect:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SPI:SELect:THReshold`` command.
        """
        return self._select


class BusBItemSentTicktolerance(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:TICKTOLerance`` command.

    Description:
        - This command sets or queries the SENT bus Tick Tolerance percent parameter for the
          specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:TICKTOLerance?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:TICKTOLerance?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:TICKTOLerance value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:TICKTOLerance <NR3>
        - BUS:B<x>:SENT:TICKTOLerance?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the tick tolerance percentage.
    """


class BusBItemSentTicktime(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:TICKTIME`` command.

    Description:
        - This command sets or queries the SENT bus Clock Tick parameter for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:TICKTIME?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:TICKTIME?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:TICKTIME value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:TICKTIME <NR3>
        - BUS:B<x>:SENT:TICKTIME?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` is the SENT clock tick time, in seconds.
    """


class BusBItemSentThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:THRESHold`` command.

    Description:
        - This command sets or queries the SENT DATA source threshold for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:THRESHold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:THRESHold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:THRESHold <NR3>
        - BUS:B<x>:SENT:THRESHold?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``<NR3>`` sets the data source threshold value in volts.
    """


class BusBItemSentSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:SOUrce`` command.

    Description:
        - This command sets or queries the SENT DATA source for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:SOUrce {CH<x>|DCH<x>_D<x>|Math<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:SENT:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``CH<x>`` specifies an analog channel as the clock source waveform for the audio bus.
        - ``DCH<x>_D<x>`` specifies the channel bit of a separate digital channel as the clock
          source waveform for the audio bus. The supported digital channel value is 1. The supported
          digital bit values are 0 to 15.
        - ``Math<x>`` specifies a math waveform as the clock source waveform for the audio bus.
        - ``REF<x>`` specifies a reference waveform as the clock source waveform for the audio bus.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified audio bus.
    """


class BusBItemSentSlow(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:SLOW`` command.

    Description:
        - This command sets or queries the SENT slow channel configuration for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:SLOW?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:SLOW?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:SLOW value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:SLOW {NOne|ENHANCED4|ENHANCED8|SHOrt}
        - BUS:B<x>:SENT:SLOW?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``NOne`` specifies no slow channel configured.
        - ``ENHANCED4`` specifies Enhanced 4 slow channel configuration.
        - ``ENHANCED8`` specifies Enhanced 8 slow channel configuration.
        - ``SHOrt`` specifies short slow channel configuration.
    """


class BusBItemSentPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:POLARITY`` command.

    Description:
        - This command sets or queries SENT Idle State signal polarity for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:POLARITY?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:POLARITY?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:POLARITY value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:POLARITY {INVerted|NORmal}
        - BUS:B<x>:SENT:POLARITY?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``INVerted`` specifies inverted polarity.
        - ``NORmal`` specifies normal polarity.
    """


class BusBItemSentPausepulse(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:PAUSEPULSe`` command.

    Description:
        - This command sets or queries SENT pause pulse for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:PAUSEPULSe {NO|YES}
        - BUS:B<x>:SENT:PAUSEPULSe?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``NO`` specifies no pause pulse.
        - ``YES`` specifies a pause pulse is used.
    """


class BusBItemSentNumchannel(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:NUMCHANnel`` command.

    Description:
        - This command sets or queries SENT fast data channels for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:NUMCHANnel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:NUMCHANnel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:NUMCHANnel value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:NUMCHANnel {ONE|TWO}
        - BUS:B<x>:SENT:NUMCHANnel?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``ONE`` specifies a SENT bus with one fast channel.
        - ``TWO`` specifies a SENT bus with two fast channels.
    """


class BusBItemSentNibblecount(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:NIBBLECount`` command.

    Description:
        - This command sets or queries SENT data nibbles for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:NIBBLECount?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:NIBBLECount?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:NIBBLECount value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:NIBBLECount {THREE|FOUR|SIX}
        - BUS:B<x>:SENT:NIBBLECount?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``THREE`` specifies regular data with 3 nibbles.
        - ``FOUR`` specifies regular data with 4nibbles.
        - ``SIX`` specifies regular data with 6nibbles.
    """


class BusBItemSentChanwidth(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SENT:CHANWidth`` command.

    Description:
        - This command sets or queries SENT fast channel bit widths for the specified bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:CHANWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:CHANWidth?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:CHANWidth value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SENT:CHANWidth {TWELVEtwelve|FOURTEENten|SIXTEENeight}
        - BUS:B<x>:SENT:CHANWidth?
        ```

    Info:
        - ``B<x>`` is the number of the bus waveform.
        - ``TWELVEtwelve`` sets both Fast Channel 1 and Fast Channel 2 to12 bits wide.
        - ``FOURTEENten`` sets Fast Channel 1 to 14 bits and Fast Channel 2 to 10 bits.
        - ``SIXTEENeight`` sets Fast Channel 1 to 16 bits and Fast Channel 2 to eight bits.
    """


#  pylint: disable=too-many-instance-attributes
class BusBItemSent(SCPICmdRead):
    """The ``BUS:B<x>:SENT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SENT?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus waveform.

    Properties:
        - ``.chanwidth``: The ``BUS:B<x>:SENT:CHANWidth`` command.
        - ``.nibblecount``: The ``BUS:B<x>:SENT:NIBBLECount`` command.
        - ``.numchannel``: The ``BUS:B<x>:SENT:NUMCHANnel`` command.
        - ``.pausepulse``: The ``BUS:B<x>:SENT:PAUSEPULSe`` command.
        - ``.polarity``: The ``BUS:B<x>:SENT:POLARITY`` command.
        - ``.slow``: The ``BUS:B<x>:SENT:SLOW`` command.
        - ``.source``: The ``BUS:B<x>:SENT:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:SENT:THRESHold`` command.
        - ``.ticktime``: The ``BUS:B<x>:SENT:TICKTIME`` command.
        - ``.ticktolerance``: The ``BUS:B<x>:SENT:TICKTOLerance`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._chanwidth = BusBItemSentChanwidth(device, f"{self._cmd_syntax}:CHANWidth")
        self._nibblecount = BusBItemSentNibblecount(device, f"{self._cmd_syntax}:NIBBLECount")
        self._numchannel = BusBItemSentNumchannel(device, f"{self._cmd_syntax}:NUMCHANnel")
        self._pausepulse = BusBItemSentPausepulse(device, f"{self._cmd_syntax}:PAUSEPULSe")
        self._polarity = BusBItemSentPolarity(device, f"{self._cmd_syntax}:POLARITY")
        self._slow = BusBItemSentSlow(device, f"{self._cmd_syntax}:SLOW")
        self._source = BusBItemSentSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemSentThreshold(device, f"{self._cmd_syntax}:THRESHold")
        self._ticktime = BusBItemSentTicktime(device, f"{self._cmd_syntax}:TICKTIME")
        self._ticktolerance = BusBItemSentTicktolerance(device, f"{self._cmd_syntax}:TICKTOLerance")

    @property
    def chanwidth(self) -> BusBItemSentChanwidth:
        """Return the ``BUS:B<x>:SENT:CHANWidth`` command.

        Description:
            - This command sets or queries SENT fast channel bit widths for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:CHANWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:CHANWidth?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:CHANWidth value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:CHANWidth {TWELVEtwelve|FOURTEENten|SIXTEENeight}
            - BUS:B<x>:SENT:CHANWidth?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``TWELVEtwelve`` sets both Fast Channel 1 and Fast Channel 2 to12 bits wide.
            - ``FOURTEENten`` sets Fast Channel 1 to 14 bits and Fast Channel 2 to 10 bits.
            - ``SIXTEENeight`` sets Fast Channel 1 to 16 bits and Fast Channel 2 to eight bits.
        """
        return self._chanwidth

    @property
    def nibblecount(self) -> BusBItemSentNibblecount:
        """Return the ``BUS:B<x>:SENT:NIBBLECount`` command.

        Description:
            - This command sets or queries SENT data nibbles for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:NIBBLECount?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:NIBBLECount?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:NIBBLECount value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:NIBBLECount {THREE|FOUR|SIX}
            - BUS:B<x>:SENT:NIBBLECount?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``THREE`` specifies regular data with 3 nibbles.
            - ``FOUR`` specifies regular data with 4nibbles.
            - ``SIX`` specifies regular data with 6nibbles.
        """
        return self._nibblecount

    @property
    def numchannel(self) -> BusBItemSentNumchannel:
        """Return the ``BUS:B<x>:SENT:NUMCHANnel`` command.

        Description:
            - This command sets or queries SENT fast data channels for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:NUMCHANnel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:NUMCHANnel?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:NUMCHANnel value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:NUMCHANnel {ONE|TWO}
            - BUS:B<x>:SENT:NUMCHANnel?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``ONE`` specifies a SENT bus with one fast channel.
            - ``TWO`` specifies a SENT bus with two fast channels.
        """
        return self._numchannel

    @property
    def pausepulse(self) -> BusBItemSentPausepulse:
        """Return the ``BUS:B<x>:SENT:PAUSEPULSe`` command.

        Description:
            - This command sets or queries SENT pause pulse for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:PAUSEPULSe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:PAUSEPULSe {NO|YES}
            - BUS:B<x>:SENT:PAUSEPULSe?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``NO`` specifies no pause pulse.
            - ``YES`` specifies a pause pulse is used.
        """
        return self._pausepulse

    @property
    def polarity(self) -> BusBItemSentPolarity:
        """Return the ``BUS:B<x>:SENT:POLARITY`` command.

        Description:
            - This command sets or queries SENT Idle State signal polarity for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:POLARITY?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:POLARITY?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:POLARITY value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:POLARITY {INVerted|NORmal}
            - BUS:B<x>:SENT:POLARITY?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``INVerted`` specifies inverted polarity.
            - ``NORmal`` specifies normal polarity.
        """
        return self._polarity

    @property
    def slow(self) -> BusBItemSentSlow:
        """Return the ``BUS:B<x>:SENT:SLOW`` command.

        Description:
            - This command sets or queries the SENT slow channel configuration for the specified
              bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:SLOW?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:SLOW?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:SLOW value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:SLOW {NOne|ENHANCED4|ENHANCED8|SHOrt}
            - BUS:B<x>:SENT:SLOW?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``NOne`` specifies no slow channel configured.
            - ``ENHANCED4`` specifies Enhanced 4 slow channel configuration.
            - ``ENHANCED8`` specifies Enhanced 8 slow channel configuration.
            - ``SHOrt`` specifies short slow channel configuration.
        """
        return self._slow

    @property
    def source(self) -> BusBItemSentSource:
        """Return the ``BUS:B<x>:SENT:SOUrce`` command.

        Description:
            - This command sets or queries the SENT DATA source for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:SOUrce {CH<x>|DCH<x>_D<x>|Math<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:SENT:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``CH<x>`` specifies an analog channel as the clock source waveform for the audio bus.
            - ``DCH<x>_D<x>`` specifies the channel bit of a separate digital channel as the clock
              source waveform for the audio bus. The supported digital channel value is 1. The
              supported digital bit values are 0 to 15.
            - ``Math<x>`` specifies a math waveform as the clock source waveform for the audio bus.
            - ``REF<x>`` specifies a reference waveform as the clock source waveform for the audio
              bus.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified audio bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemSentThreshold:
        """Return the ``BUS:B<x>:SENT:THRESHold`` command.

        Description:
            - This command sets or queries the SENT DATA source threshold for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:THRESHold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:THRESHold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:THRESHold <NR3>
            - BUS:B<x>:SENT:THRESHold?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` sets the data source threshold value in volts.
        """
        return self._threshold

    @property
    def ticktime(self) -> BusBItemSentTicktime:
        """Return the ``BUS:B<x>:SENT:TICKTIME`` command.

        Description:
            - This command sets or queries the SENT bus Clock Tick parameter for the specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:TICKTIME?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:TICKTIME?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:TICKTIME value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:TICKTIME <NR3>
            - BUS:B<x>:SENT:TICKTIME?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the SENT clock tick time, in seconds.
        """
        return self._ticktime

    @property
    def ticktolerance(self) -> BusBItemSentTicktolerance:
        """Return the ``BUS:B<x>:SENT:TICKTOLerance`` command.

        Description:
            - This command sets or queries the SENT bus Tick Tolerance percent parameter for the
              specified bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT:TICKTOLerance?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT:TICKTOLerance?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SENT:TICKTOLerance value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SENT:TICKTOLerance <NR3>
            - BUS:B<x>:SENT:TICKTOLerance?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``<NR3>`` is the tick tolerance percentage.
        """
        return self._ticktolerance


class BusBItemRs232cSourceThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:SOUrce:THReshold`` command.

    Description:
        - This command sets or queries the RS-232C source threshold for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:SOUrce:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce:THReshold?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:RS232C:SOUrce:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:SOUrce:THReshold <NR3>
        - BUS:B<x>:RS232C:SOUrce:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the RS-232C source threshold for the specified bus.
    """


class BusBItemRs232cSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:SOUrce`` command.

    Description:
        - This command sets or queries the RS-232C source for the bus, where the bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:SOUrce {CH<x>|DCH<x>_D<x>|REF<x>|MATH<x>|REF<x>_D<x>}
        - BUS:B<x>:RS232C:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``CH<x>`` specifies an analog channel to use as the RS-232C source.
        - ``DCH<x>_D<x>`` specifies a digital channel of a specified digital channel to use for the
          RS-232C source. The supported digital channel value is 1. The supported digital bit values
          are 0 to 15.
        - ``MATH<x>`` specifies a math channel to use for the RS-232C source.
        - ``REF<x>`` specifies a reference channel to use for the RS-232C source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the source waveform for the
          specified RS-232C bus.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:RS232C:SOUrce:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemRs232cSourceThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def threshold(self) -> BusBItemRs232cSourceThreshold:
        """Return the ``BUS:B<x>:RS232C:SOUrce:THReshold`` command.

        Description:
            - This command sets or queries the RS-232C source threshold for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:SOUrce:THReshold?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:RS232C:SOUrce:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:RS232C:SOUrce:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:SOUrce:THReshold <NR3>
            - BUS:B<x>:RS232C:SOUrce:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the RS-232C source threshold for the specified bus.
        """
        return self._threshold


class BusBItemRs232cPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:POLarity`` command.

    Description:
        - This command sets or queries the RS-232C source polarity for bus <x>, where the bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:POLarity {NORmal|INVERTed}
        - BUS:B<x>:RS232C:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NORmal`` sets the RS-232C bus polarity to positive.
        - ``INVERTed`` sets the RS-232C bus polarity to negative.
    """


class BusBItemRs232cParity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:PARity`` command.

    Description:
        - This command sets or queries the RS-232C parity for bus <x>, where the bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:PARity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:PARity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:PARity value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:PARity {NONe|EVEN|ODD}
        - BUS:B<x>:RS232C:PARity?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NONe`` specifies no parity.
        - ``EVEN`` specifies even parity.
        - ``ODD`` specifies odd parity.
    """


class BusBItemRs232cDisplaymode(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:DISplaymode`` command.

    Description:
        - This command sets or queries the RS-232C display mode for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DISplaymode {FRame|PACKET}
        - BUS:B<x>:RS232C:DISplaymode?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``FRame`` displays each frame as a single entity.
        - ``PACKET`` displays a group of frames terminated with a single frame defined by the
          ``BUS:B<x>:RS232C:DELImiter`` command.
    """


class BusBItemRs232cDelimiter(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:DELIMiter`` command.

    Description:
        - This command sets or queries the RS-232C string delimiter on bus <x>, where the bus number
          is specified by x. This command only applies when Packet view is turned On.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DELIMiter {NULl|CR|LF|SPace|XFF}
        - BUS:B<x>:RS232C:DELIMiter?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NULl`` specifies NULL (0x00 ) delimiting value for a packet.
        - ``CR`` specifies CR (0x0D) delimiting value for a packet.
        - ``LF`` specifies LF (0x0A) delimiting value for a packet.
        - ``XFF`` specifies XFF (0xFF) delimiting value for a packet.
        - ``SPace`` specifies SPace delimiting value for a packet.
    """


class BusBItemRs232cDatabits(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:DATABits`` command.

    Description:
        - This command sets or queries the RS-232C data width for bus<x>, where the bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DATABits value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DATABits {<NR1>}
        - BUS:B<x>:RS232C:DATABits?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` specifies the number of bits in the RS-232C data frame.
    """


class BusBItemRs232cBitrateCustom(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:BITRate:CUSTom`` command.

    Description:
        - This command sets or queries the RS-232C custom bit rate for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate:CUSTom?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate:CUSTom?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate:CUSTom value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:BITRate:CUSTom <NR1>
        - BUS:B<x>:RS232C:BITRate:CUSTom?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the custom bit rate.
    """


class BusBItemRs232cBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:BITRate`` command.

    Description:
        - This command sets or queries the RS-232C bit rate for bus<x>, where the bus number is
          specified by x. If you select Custom, use ``BUS:BX:RS232C:BITRATE:CUSTOM`` to set the bit
          rate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:BITRate {CUSTOM|RATE300|RATE1K|RATE2K|RATE9K|RATE19K|RATE38K|RATE115K|RATE921K}
        - BUS:B<x>:RS232C:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.custom``: The ``BUS:B<x>:RS232C:BITRate:CUSTom`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custom = BusBItemRs232cBitrateCustom(device, f"{self._cmd_syntax}:CUSTom")

    @property
    def custom(self) -> BusBItemRs232cBitrateCustom:
        """Return the ``BUS:B<x>:RS232C:BITRate:CUSTom`` command.

        Description:
            - This command sets or queries the RS-232C custom bit rate for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate:CUSTom?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate:CUSTom?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:RS232C:BITRate:CUSTom value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:BITRate:CUSTom <NR1>
            - BUS:B<x>:RS232C:BITRate:CUSTom?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the custom bit rate.
        """
        return self._custom


class BusBItemRs232c(SCPICmdRead):
    """The ``BUS:B<x>:RS232C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:RS232C:BITRate`` command.
        - ``.databits``: The ``BUS:B<x>:RS232C:DATABits`` command.
        - ``.delimiter``: The ``BUS:B<x>:RS232C:DELIMiter`` command.
        - ``.displaymode``: The ``BUS:B<x>:RS232C:DISplaymode`` command.
        - ``.parity``: The ``BUS:B<x>:RS232C:PARity`` command.
        - ``.polarity``: The ``BUS:B<x>:RS232C:POLarity`` command.
        - ``.source``: The ``BUS:B<x>:RS232C:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemRs232cBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._databits = BusBItemRs232cDatabits(device, f"{self._cmd_syntax}:DATABits")
        self._delimiter = BusBItemRs232cDelimiter(device, f"{self._cmd_syntax}:DELIMiter")
        self._displaymode = BusBItemRs232cDisplaymode(device, f"{self._cmd_syntax}:DISplaymode")
        self._parity = BusBItemRs232cParity(device, f"{self._cmd_syntax}:PARity")
        self._polarity = BusBItemRs232cPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._source = BusBItemRs232cSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemRs232cBitrate:
        """Return the ``BUS:B<x>:RS232C:BITRate`` command.

        Description:
            - This command sets or queries the RS-232C bit rate for bus<x>, where the bus number is
              specified by x. If you select Custom, use ``BUS:BX:RS232C:BITRATE:CUSTOM`` to set the
              bit rate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:BITRate {CUSTOM|RATE300|RATE1K|RATE2K|RATE9K|RATE19K|RATE38K|RATE115K|RATE921K}
            - BUS:B<x>:RS232C:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.custom``: The ``BUS:B<x>:RS232C:BITRate:CUSTom`` command.
        """  # noqa: E501
        return self._bitrate

    @property
    def databits(self) -> BusBItemRs232cDatabits:
        """Return the ``BUS:B<x>:RS232C:DATABits`` command.

        Description:
            - This command sets or queries the RS-232C data width for bus<x>, where the bus number
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DATABits?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DATABits value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DATABits {<NR1>}
            - BUS:B<x>:RS232C:DATABits?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` specifies the number of bits in the RS-232C data frame.
        """
        return self._databits

    @property
    def delimiter(self) -> BusBItemRs232cDelimiter:
        """Return the ``BUS:B<x>:RS232C:DELIMiter`` command.

        Description:
            - This command sets or queries the RS-232C string delimiter on bus <x>, where the bus
              number is specified by x. This command only applies when Packet view is turned On.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DELIMiter {NULl|CR|LF|SPace|XFF}
            - BUS:B<x>:RS232C:DELIMiter?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NULl`` specifies NULL (0x00 ) delimiting value for a packet.
            - ``CR`` specifies CR (0x0D) delimiting value for a packet.
            - ``LF`` specifies LF (0x0A) delimiting value for a packet.
            - ``XFF`` specifies XFF (0xFF) delimiting value for a packet.
            - ``SPace`` specifies SPace delimiting value for a packet.
        """
        return self._delimiter

    @property
    def displaymode(self) -> BusBItemRs232cDisplaymode:
        """Return the ``BUS:B<x>:RS232C:DISplaymode`` command.

        Description:
            - This command sets or queries the RS-232C display mode for the specified bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DISplaymode {FRame|PACKET}
            - BUS:B<x>:RS232C:DISplaymode?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``FRame`` displays each frame as a single entity.
            - ``PACKET`` displays a group of frames terminated with a single frame defined by the
              ``BUS:B<x>:RS232C:DELImiter`` command.
        """
        return self._displaymode

    @property
    def parity(self) -> BusBItemRs232cParity:
        """Return the ``BUS:B<x>:RS232C:PARity`` command.

        Description:
            - This command sets or queries the RS-232C parity for bus <x>, where the bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:PARity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:PARity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:PARity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:PARity {NONe|EVEN|ODD}
            - BUS:B<x>:RS232C:PARity?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NONe`` specifies no parity.
            - ``EVEN`` specifies even parity.
            - ``ODD`` specifies odd parity.
        """
        return self._parity

    @property
    def polarity(self) -> BusBItemRs232cPolarity:
        """Return the ``BUS:B<x>:RS232C:POLarity`` command.

        Description:
            - This command sets or queries the RS-232C source polarity for bus <x>, where the bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:POLarity {NORmal|INVERTed}
            - BUS:B<x>:RS232C:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NORmal`` sets the RS-232C bus polarity to positive.
            - ``INVERTed`` sets the RS-232C bus polarity to negative.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemRs232cSource:
        """Return the ``BUS:B<x>:RS232C:SOUrce`` command.

        Description:
            - This command sets or queries the RS-232C source for the bus, where the bus number is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:SOUrce {CH<x>|DCH<x>_D<x>|REF<x>|MATH<x>|REF<x>_D<x>}
            - BUS:B<x>:RS232C:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``CH<x>`` specifies an analog channel to use as the RS-232C source.
            - ``DCH<x>_D<x>`` specifies a digital channel of a specified digital channel to use for
              the RS-232C source. The supported digital channel value is 1. The supported digital
              bit values are 0 to 15.
            - ``MATH<x>`` specifies a math channel to use for the RS-232C source.
            - ``REF<x>`` specifies a reference channel to use for the RS-232C source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the source waveform for the
              specified RS-232C bus.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:RS232C:SOUrce:THReshold`` command.
        """
        return self._source


class BusBItemParallelClocksourceThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold`` command.

    Description:
        - This command sets or queries the clock source threshold for the parallel bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold <NR3>
        - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?
        ```

    Info:
        - ``<NR3>`` is the clock bit source threshold for the parallel bus.
    """


class BusBItemParallelClocksource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCkSOUrce`` command.

    Description:
        - This command sets or queries the Parallel clock bit source for the specified bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCkSOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
        - BUS:B<x>:PARallel:CLOCkSOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``CH<x>`` specifies an analog FlexChannel to use as the bus clock source.
        - ``DCH<x>_D<x>`` specifies a digital channel on a specified digital channel to use as the
          bus clock source. The supported digital channel value is 1. The supported digital bit
          values are 0 to 15.
        - ``MATH<x>`` specifies the math channel to use as the bus clock source.
        - ``REF<x>`` specifies the reference channel to use as the bus clock source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified parallel bus.
        - ``NONE`` specifies the reference channel to use as the bus clock source.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemParallelClocksourceThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def threshold(self) -> BusBItemParallelClocksourceThreshold:
        """Return the ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold`` command.

        Description:
            - This command sets or queries the clock source threshold for the parallel bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold <NR3>
            - BUS:B<x>:PARallel:CLOCkSOUrce:THReshold?
            ```

        Info:
            - ``<NR3>`` is the clock bit source threshold for the parallel bus.
        """
        return self._threshold


class BusBItemParallelClockIsclocked(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED`` command.

    Description:
        - This command determines whether the bus operates in a clocked or asynchronous fashion. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCk:ISCLOCKED {ON|OFF|<NR1>}
        - BUS:B<x>:PARallel:CLOCk:ISCLOCKED?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``OFF`` argument specifies an asynchronous bus.
        - ``ON`` argument specifies a clocked bus.
        - ``<NR1>`` = 0 specifies an asynchronous bus; any other value specifies a clocked bus.
    """


class BusBItemParallelClockEdge(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.

    Description:
        - This command sets or queries the clock edge for the parallel bus. The bus is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCk:EDGE {FALLING|RISING|EITHER}
        - BUS:B<x>:PARallel:CLOCk:EDGE?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``FALLING`` decodes on the falling edge of the clocked parallel bus signal.
        - ``RISING`` decodes on the rising edge of the clocked parallel bus signal.
        - ``EITHER`` decodes on the rising or falling edge of the clocked parallel bus signal.
    """


class BusBItemParallelClock(SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.edge``: The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.
        - ``.isclocked``: The ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = BusBItemParallelClockEdge(device, f"{self._cmd_syntax}:EDGE")
        self._isclocked = BusBItemParallelClockIsclocked(device, f"{self._cmd_syntax}:ISCLOCKED")

    @property
    def edge(self) -> BusBItemParallelClockEdge:
        """Return the ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.

        Description:
            - This command sets or queries the clock edge for the parallel bus. The bus is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk:EDGE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:EDGE value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCk:EDGE {FALLING|RISING|EITHER}
            - BUS:B<x>:PARallel:CLOCk:EDGE?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``FALLING`` decodes on the falling edge of the clocked parallel bus signal.
            - ``RISING`` decodes on the rising edge of the clocked parallel bus signal.
            - ``EITHER`` decodes on the rising or falling edge of the clocked parallel bus signal.
        """
        return self._edge

    @property
    def isclocked(self) -> BusBItemParallelClockIsclocked:
        """Return the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED`` command.

        Description:
            - This command determines whether the bus operates in a clocked or asynchronous fashion.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCk:ISCLOCKED {ON|OFF|<NR1>}
            - BUS:B<x>:PARallel:CLOCk:ISCLOCKED?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``OFF`` argument specifies an asynchronous bus.
            - ``ON`` argument specifies a clocked bus.
            - ``<NR1>`` = 0 specifies an asynchronous bus; any other value specifies a clocked bus.
        """
        return self._isclocked


class BusBItemParallelBitsourceItemThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold`` command.

    Description:
        - This command sets or queries the specified bit source threshold for the specified parallel
          bus. The bus is specified by x. The bit is specified by x and is an integer in the range
          of 1 to 64.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold <NR3>
        - BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``BIT<x>`` is the number of the bit source.
        - ``<NR3>`` is the specified bit source threshold for the specified parallel bus.
    """


class BusBItemParallelBitsourceItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:BIT<x>SOUrce`` command.

    Description:
        - This command sets or queries the specified bit source for specified parallel bus. The bus
          is specified by x. The bit is specified by x and is an integer in the range of 1 to 64.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:BIT<x>SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:BIT<x>SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
        - BUS:B<x>:PARallel:BIT<x>SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``BIT<x>`` is the number of the bit source.
        - ``CH<x>`` is the specified bit source.
        - ``DCH<x>_D<x>`` specifies a digital channel to use as the source. The supported digital
          channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` is the specified bit source.
        - ``REF<x>`` is the specified bit source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the bit<x> source waveform for
          the specified parallel bus.
        - ``NONE`` disables the bit source.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemParallelBitsourceItemThreshold(
            device, f"{self._cmd_syntax}:THReshold"
        )

    @property
    def threshold(self) -> BusBItemParallelBitsourceItemThreshold:
        """Return the ``BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold`` command.

        Description:
            - This command sets or queries the specified bit source threshold for the specified
              parallel bus. The bus is specified by x. The bit is specified by x and is an integer
              in the range of 1 to 64.

        Usage:
            - Using the ``.query()`` method will send the
              ``BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold <NR3>
            - BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``BIT<x>`` is the number of the bit source.
            - ``<NR3>`` is the specified bit source threshold for the specified parallel bus.
        """
        return self._threshold


class BusBItemParallelAllthresholdsApply(SCPICmdWriteNoArguments):
    """The ``BUS:B<x>:PARallel:ALLTHResholds:APPly`` command.

    Description:
        - This command sets all of the data source thresholds to the value set by
          ``BUS:BX:PARALLEL:ALLTHRESHOLDS`` for the parallel bus. The bus is specified by x.

    Usage:
        - Using the ``.write()`` method will send the ``BUS:B<x>:PARallel:ALLTHResholds:APPly``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:ALLTHResholds:APPly
        ```

    Info:
        - ``B<x>`` is the Bus number.
    """


class BusBItemParallelAllthresholds(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:ALLTHResholds`` command.

    Description:
        - This command sets or queries a threshold value for sources for the parallel bus. Use the
          ``BUS:BX:PARALLEL:ALLTHRESHOLDS:APPLY`` command to set the thresholds to this value. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:ALLTHResholds?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:ALLTHResholds?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:ALLTHResholds value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:ALLTHResholds <NR3>
        - BUS:B<x>:PARallel:ALLTHResholds?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the source threshold.

    Properties:
        - ``.apply``: The ``BUS:B<x>:PARallel:ALLTHResholds:APPly`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._apply = BusBItemParallelAllthresholdsApply(device, f"{self._cmd_syntax}:APPly")

    @property
    def apply(self) -> BusBItemParallelAllthresholdsApply:
        """Return the ``BUS:B<x>:PARallel:ALLTHResholds:APPly`` command.

        Description:
            - This command sets all of the data source thresholds to the value set by
              ``BUS:BX:PARALLEL:ALLTHRESHOLDS`` for the parallel bus. The bus is specified by x.

        Usage:
            - Using the ``.write()`` method will send the ``BUS:B<x>:PARallel:ALLTHResholds:APPly``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:ALLTHResholds:APPly
            ```

        Info:
            - ``B<x>`` is the Bus number.
        """
        return self._apply


class BusBItemParallel(SCPICmdRead):
    """The ``BUS:B<x>:PARallel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.allthresholds``: The ``BUS:B<x>:PARallel:ALLTHResholds`` command.
        - ``.bitsource``: The ``BUS:B<x>:PARallel:BIT<x>SOUrce`` command.
        - ``.clock``: The ``BUS:B<x>:PARallel:CLOCk`` command tree.
        - ``.clocksource``: The ``BUS:B<x>:PARallel:CLOCkSOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._allthresholds = BusBItemParallelAllthresholds(
            device, f"{self._cmd_syntax}:ALLTHResholds"
        )
        self._bitsource: Dict[int, BusBItemParallelBitsourceItem] = DefaultDictPassKeyToFactory(
            lambda x: BusBItemParallelBitsourceItem(device, f"{self._cmd_syntax}:BIT{x}SOUrce")
        )
        self._clock = BusBItemParallelClock(device, f"{self._cmd_syntax}:CLOCk")
        self._clocksource = BusBItemParallelClocksource(device, f"{self._cmd_syntax}:CLOCkSOUrce")

    @property
    def allthresholds(self) -> BusBItemParallelAllthresholds:
        """Return the ``BUS:B<x>:PARallel:ALLTHResholds`` command.

        Description:
            - This command sets or queries a threshold value for sources for the parallel bus. Use
              the ``BUS:BX:PARALLEL:ALLTHRESHOLDS:APPLY`` command to set the thresholds to this
              value. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:ALLTHResholds?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:ALLTHResholds?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:ALLTHResholds value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:ALLTHResholds <NR3>
            - BUS:B<x>:PARallel:ALLTHResholds?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the source threshold.

        Sub-properties:
            - ``.apply``: The ``BUS:B<x>:PARallel:ALLTHResholds:APPly`` command.
        """
        return self._allthresholds

    @property
    def bitsource(self) -> Dict[int, BusBItemParallelBitsourceItem]:
        """Return the ``BUS:B<x>:PARallel:BIT<x>SOUrce`` command.

        Description:
            - This command sets or queries the specified bit source for specified parallel bus. The
              bus is specified by x. The bit is specified by x and is an integer in the range of 1
              to 64.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:BIT<x>SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:BIT<x>SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:BIT<x>SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
            - BUS:B<x>:PARallel:BIT<x>SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``BIT<x>`` is the number of the bit source.
            - ``CH<x>`` is the specified bit source.
            - ``DCH<x>_D<x>`` specifies a digital channel to use as the source. The supported
              digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``MATH<x>`` is the specified bit source.
            - ``REF<x>`` is the specified bit source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the bit<x> source waveform
              for the specified parallel bus.
            - ``NONE`` disables the bit source.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:PARallel:BIT<x>SOUrce:THReshold`` command.
        """
        return self._bitsource

    @property
    def clock(self) -> BusBItemParallelClock:
        """Return the ``BUS:B<x>:PARallel:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCk?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.edge``: The ``BUS:B<x>:PARallel:CLOCk:EDGE`` command.
            - ``.isclocked``: The ``BUS:B<x>:PARallel:CLOCk:ISCLOCKED`` command.
        """
        return self._clock

    @property
    def clocksource(self) -> BusBItemParallelClocksource:
        """Return the ``BUS:B<x>:PARallel:CLOCkSOUrce`` command.

        Description:
            - This command sets or queries the Parallel clock bit source for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCkSOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCkSOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCkSOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>|NONE}
            - BUS:B<x>:PARallel:CLOCkSOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``CH<x>`` specifies an analog FlexChannel to use as the bus clock source.
            - ``DCH<x>_D<x>`` specifies a digital channel on a specified digital channel to use as
              the bus clock source. The supported digital channel value is 1. The supported digital
              bit values are 0 to 15.
            - ``MATH<x>`` specifies the math channel to use as the bus clock source.
            - ``REF<x>`` specifies the reference channel to use as the bus clock source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified parallel bus.
            - ``NONE`` specifies the reference channel to use as the bus clock source.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:PARallel:CLOCkSOUrce:THReshold`` command.
        """
        return self._clocksource


class BusBItemLinStandard(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:STANDard`` command.

    Description:
        - This command sets or queries the LIN bus standard for the specified bus. The bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:STANDard?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:STANDard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:STANDard value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:STANDard {MIXed|V1X|V2X}
        - BUS:B<x>:LIN:STANDard?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``MIXed`` specifies both versions 1.x and 2.x of the LIN standard.
        - ``V1X`` specifies version 1.x of the LIN standard.
        - ``V2X`` specifies version 2.x of the LIN standard.
    """


class BusBItemLinSourceThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:SOUrce:THReshold`` command.

    Description:
        - This command sets or queries the LIN source threshold for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:SOUrce:THReshold <NR3>
        - BUS:B<x>:LIN:SOUrce:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` the LIN source threshold for the specified bus.
    """


class BusBItemLinSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:SOUrce`` command.

    Description:
        - This command sets or queries the LIN data source for the specified bus. The bus number is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:LIN:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``CH<x>`` specifies an analog channel to use as the LIN data source.
        - ``DCH<x>_D<x>`` specifies a digital channel to use as the LIN data source. The supported
          digital channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` specifies a math waveform to use as the LIN data source.
        - ``REF<x>`` specifies a reference waveform to use as the LIN data source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform.

    Properties:
        - ``.threshold``: The ``BUS:B<x>:LIN:SOUrce:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = BusBItemLinSourceThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def threshold(self) -> BusBItemLinSourceThreshold:
        """Return the ``BUS:B<x>:LIN:SOUrce:THReshold`` command.

        Description:
            - This command sets or queries the LIN source threshold for the specified bus. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:LIN:SOUrce:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:SOUrce:THReshold <NR3>
            - BUS:B<x>:LIN:SOUrce:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` the LIN source threshold for the specified bus.
        """
        return self._threshold


class BusBItemLinSamplepoint(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:SAMPLEpoint`` command.

    Description:
        - Specifies the LIN sample point, for the specified LIN bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:SAMPLEpoint <NR1>
        - BUS:B<x>:LIN:SAMPLEpoint?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is a percentage that represents the point at which to sample during each bit
          period.
    """


class BusBItemLinPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:POLarity`` command.

    Description:
        - This command sets or queries the LIN source polarity for the specified bus. The bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:POLarity value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:POLarity {INVerted|NORmal}
        - BUS:B<x>:LIN:POLarity?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
    """


class BusBItemLinIdformat(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:IDFORmat`` command.

    Description:
        - This command sets or queries LIN bus identifier format for the specified bus. The bus
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:IDFORmat?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:IDFORmat?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:IDFORmat value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:IDFORmat {NOPARity|PARity}
        - BUS:B<x>:LIN:IDFORmat?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``NOPARity`` specifies an id format that includes parity.
        - ``PARity`` specifies an id format that separates parity.
    """


class BusBItemLinBitrateCustom(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:BITRate:CUSTom`` command.

    Description:
        - This command sets or queries LIN custom bit rate for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:BITRate:CUSTom <NR1>
        - BUS:B<x>:LIN:BITRate:CUSTom?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the LIN custom bit rate for the specified bus.
    """


class BusBItemLinBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:BITRate`` command.

    Description:
        - This command sets or queries the LIN bus bit rate. The bus number is specified by x. If
          you select Custom, use ``BUS:BX:LIN:BITRATE:CUSTOM`` to set the bit rate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:BITRate {RATE10K|RATE1K|RATE19K|RATE2K|RATE4K|RATE9K|CUSTom}
        - BUS:B<x>:LIN:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.custom``: The ``BUS:B<x>:LIN:BITRate:CUSTom`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custom = BusBItemLinBitrateCustom(device, f"{self._cmd_syntax}:CUSTom")

    @property
    def custom(self) -> BusBItemLinBitrateCustom:
        """Return the ``BUS:B<x>:LIN:BITRate:CUSTom`` command.

        Description:
            - This command sets or queries LIN custom bit rate for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate:CUSTom value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:BITRate:CUSTom <NR1>
            - BUS:B<x>:LIN:BITRate:CUSTom?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the LIN custom bit rate for the specified bus.
        """
        return self._custom


class BusBItemLin(SCPICmdRead):
    """The ``BUS:B<x>:LIN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:LIN:BITRate`` command.
        - ``.idformat``: The ``BUS:B<x>:LIN:IDFORmat`` command.
        - ``.polarity``: The ``BUS:B<x>:LIN:POLarity`` command.
        - ``.samplepoint``: The ``BUS:B<x>:LIN:SAMPLEpoint`` command.
        - ``.source``: The ``BUS:B<x>:LIN:SOUrce`` command.
        - ``.standard``: The ``BUS:B<x>:LIN:STANDard`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemLinBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._idformat = BusBItemLinIdformat(device, f"{self._cmd_syntax}:IDFORmat")
        self._polarity = BusBItemLinPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._samplepoint = BusBItemLinSamplepoint(device, f"{self._cmd_syntax}:SAMPLEpoint")
        self._source = BusBItemLinSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = BusBItemLinStandard(device, f"{self._cmd_syntax}:STANDard")

    @property
    def bitrate(self) -> BusBItemLinBitrate:
        """Return the ``BUS:B<x>:LIN:BITRate`` command.

        Description:
            - This command sets or queries the LIN bus bit rate. The bus number is specified by x.
              If you select Custom, use ``BUS:BX:LIN:BITRATE:CUSTOM`` to set the bit rate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:BITRate {RATE10K|RATE1K|RATE19K|RATE2K|RATE4K|RATE9K|CUSTom}
            - BUS:B<x>:LIN:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.custom``: The ``BUS:B<x>:LIN:BITRate:CUSTom`` command.
        """
        return self._bitrate

    @property
    def idformat(self) -> BusBItemLinIdformat:
        """Return the ``BUS:B<x>:LIN:IDFORmat`` command.

        Description:
            - This command sets or queries LIN bus identifier format for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:IDFORmat?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:IDFORmat?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:IDFORmat value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:IDFORmat {NOPARity|PARity}
            - BUS:B<x>:LIN:IDFORmat?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``NOPARity`` specifies an id format that includes parity.
            - ``PARity`` specifies an id format that separates parity.
        """
        return self._idformat

    @property
    def polarity(self) -> BusBItemLinPolarity:
        """Return the ``BUS:B<x>:LIN:POLarity`` command.

        Description:
            - This command sets or queries the LIN source polarity for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:POLarity?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:POLarity {INVerted|NORmal}
            - BUS:B<x>:LIN:POLarity?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
        """
        return self._polarity

    @property
    def samplepoint(self) -> BusBItemLinSamplepoint:
        """Return the ``BUS:B<x>:LIN:SAMPLEpoint`` command.

        Description:
            - Specifies the LIN sample point, for the specified LIN bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SAMPLEpoint value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:SAMPLEpoint <NR1>
            - BUS:B<x>:LIN:SAMPLEpoint?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is a percentage that represents the point at which to sample during each bit
              period.
        """
        return self._samplepoint

    @property
    def source(self) -> BusBItemLinSource:
        """Return the ``BUS:B<x>:LIN:SOUrce`` command.

        Description:
            - This command sets or queries the LIN data source for the specified bus. The bus number
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:LIN:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``CH<x>`` specifies an analog channel to use as the LIN data source.
            - ``DCH<x>_D<x>`` specifies a digital channel to use as the LIN data source. The
              supported digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``MATH<x>`` specifies a math waveform to use as the LIN data source.
            - ``REF<x>`` specifies a reference waveform to use as the LIN data source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform.

        Sub-properties:
            - ``.threshold``: The ``BUS:B<x>:LIN:SOUrce:THReshold`` command.
        """
        return self._source

    @property
    def standard(self) -> BusBItemLinStandard:
        """Return the ``BUS:B<x>:LIN:STANDard`` command.

        Description:
            - This command sets or queries the LIN bus standard for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:STANDard?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:STANDard?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:STANDard value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:STANDard {MIXed|V1X|V2X}
            - BUS:B<x>:LIN:STANDard?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``MIXed`` specifies both versions 1.x and 2.x of the LIN standard.
            - ``V1X`` specifies version 1.x of the LIN standard.
            - ``V2X`` specifies version 2.x of the LIN standard.
        """
        return self._standard


class BusBItemLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:name`` command.

    Description:
        - This command sets or queries the label for the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:name?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:name?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:name value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:name <QString>
        - BUS:B<x>:LABel:name?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<QString>`` is an alphanumeric string of text enclosed in quotes. The text string is
          limited to 30 characters. It contains the text label information for the bus.
    """

    _WRAP_ARG_WITH_QUOTES = True


class BusBItemLabelYpos(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:YPOS`` command.

    Description:
        - This command sets or queries the y-position of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:YPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:YPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:YPOS value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:YPOS <NR3>
        - BUS:B<x>:LABel:YPOS?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the y-position, in pixels relative to the baseline of the waveform, of the
          specified bus label.
    """


class BusBItemLabelXpos(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:XPOS`` command.

    Description:
        - This command sets or queries the x-position of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:XPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:XPOS value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:XPOS <NR3>
        - BUS:B<x>:LABel:XPOS?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the x-position, in pixels relative to the left edge of the screen of the
          specified bus label.
    """


class BusBItemLabelFontUnderline(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT:UNDERline`` command.

    Description:
        - This command sets or queries the underline state of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:UNDERline?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:UNDERline?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:UNDERline value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:FONT:UNDERline {ON|OFF|1|0}
        - BUS:B<x>:LABel:FONT:UNDERline?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``ON`` displays the label in underlined font.
        - ``OFF`` does not display the label in underlined font.
        - ``1`` displays the label in underlined font.
        - ``0`` does not display the label in underlined font.
    """


class BusBItemLabelFontType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT:TYPE`` command.

    Description:
        - This command sets or queries the font type of the specified bus label, such as Arial or
          Times New Roman. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:TYPE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:TYPE value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:FONT:TYPE <QString>
        - BUS:B<x>:LABel:FONT:TYPE?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<QString>`` is the specified font type. Available fonts include: DejaVu Sans, DejaVu
          Sans Mono, DejaVu Serif, Frutiger LT Std, Monospace, Sans Serif, Serif, Ubuntu, Ubuntu
          Condensed, and Ubuntu Mono.
    """

    _WRAP_ARG_WITH_QUOTES = True


class BusBItemLabelFontSize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT:SIZE`` command.

    Description:
        - This command sets or queries the font size of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:SIZE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:SIZE value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:FONT:SIZE <NR1>
        - BUS:B<x>:LABel:FONT:SIZE?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the font size.
    """


class BusBItemLabelFontItalic(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT:ITALic`` command.

    Description:
        - This command sets or queries the italic state of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:ITALic?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:ITALic?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:ITALic value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:FONT:ITALic {ON|OFF|1|0}
        - BUS:B<x>:LABel:FONT:ITALic?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``ON`` displays the label in italic font.
        - ``OFF`` does not display the label in italic font.
        - ``1`` displays the label in italic font.
        - ``0`` does not display the label in italic font.
    """


class BusBItemLabelFontBold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the specified bus label. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:BOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:BOLD?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:BOLD value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:FONT:BOLD {ON|OFF|1|0}
        - BUS:B<x>:LABel:FONT:BOLD?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``ON`` displays the label in bold font.
        - ``OFF`` does not display the label in bold font.
        - ``1`` displays the label in bold font.
        - ``0`` does not display the label in bold font.
    """


class BusBItemLabelFont(SCPICmdRead):
    """The ``BUS:B<x>:LABel:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bold``: The ``BUS:B<x>:LABel:FONT:BOLD`` command.
        - ``.italic``: The ``BUS:B<x>:LABel:FONT:ITALic`` command.
        - ``.size``: The ``BUS:B<x>:LABel:FONT:SIZE`` command.
        - ``.type``: The ``BUS:B<x>:LABel:FONT:TYPE`` command.
        - ``.underline``: The ``BUS:B<x>:LABel:FONT:UNDERline`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = BusBItemLabelFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = BusBItemLabelFontItalic(device, f"{self._cmd_syntax}:ITALic")
        self._size = BusBItemLabelFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = BusBItemLabelFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = BusBItemLabelFontUnderline(device, f"{self._cmd_syntax}:UNDERline")

    @property
    def bold(self) -> BusBItemLabelFontBold:
        """Return the ``BUS:B<x>:LABel:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:BOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:BOLD?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:BOLD value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:FONT:BOLD {ON|OFF|1|0}
            - BUS:B<x>:LABel:FONT:BOLD?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``ON`` displays the label in bold font.
            - ``OFF`` does not display the label in bold font.
            - ``1`` displays the label in bold font.
            - ``0`` does not display the label in bold font.
        """
        return self._bold

    @property
    def italic(self) -> BusBItemLabelFontItalic:
        """Return the ``BUS:B<x>:LABel:FONT:ITALic`` command.

        Description:
            - This command sets or queries the italic state of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:ITALic?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:ITALic?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:ITALic value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:FONT:ITALic {ON|OFF|1|0}
            - BUS:B<x>:LABel:FONT:ITALic?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``ON`` displays the label in italic font.
            - ``OFF`` does not display the label in italic font.
            - ``1`` displays the label in italic font.
            - ``0`` does not display the label in italic font.
        """
        return self._italic

    @property
    def size(self) -> BusBItemLabelFontSize:
        """Return the ``BUS:B<x>:LABel:FONT:SIZE`` command.

        Description:
            - This command sets or queries the font size of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:SIZE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:SIZE value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:FONT:SIZE <NR1>
            - BUS:B<x>:LABel:FONT:SIZE?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the font size.
        """
        return self._size

    @property
    def type(self) -> BusBItemLabelFontType:
        """Return the ``BUS:B<x>:LABel:FONT:TYPE`` command.

        Description:
            - This command sets or queries the font type of the specified bus label, such as Arial
              or Times New Roman. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:TYPE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:FONT:TYPE value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:FONT:TYPE <QString>
            - BUS:B<x>:LABel:FONT:TYPE?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<QString>`` is the specified font type. Available fonts include: DejaVu Sans, DejaVu
              Sans Mono, DejaVu Serif, Frutiger LT Std, Monospace, Sans Serif, Serif, Ubuntu, Ubuntu
              Condensed, and Ubuntu Mono.
        """
        return self._type

    @property
    def underline(self) -> BusBItemLabelFontUnderline:
        """Return the ``BUS:B<x>:LABel:FONT:UNDERline`` command.

        Description:
            - This command sets or queries the underline state of the specified bus label. The bus
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT:UNDERline?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT:UNDERline?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:LABel:FONT:UNDERline value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:FONT:UNDERline {ON|OFF|1|0}
            - BUS:B<x>:LABel:FONT:UNDERline?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``ON`` displays the label in underlined font.
            - ``OFF`` does not display the label in underlined font.
            - ``1`` displays the label in underlined font.
            - ``0`` does not display the label in underlined font.
        """
        return self._underline


class BusBItemLabelColor(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel:COLor`` command.

    Description:
        - This command sets or queries the color of the specified bus label. The bus is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:COLor?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:COLor?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:COLor value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel:COLor <QString>
        - BUS:B<x>:LABel:COLor?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<QString>`` is the bus label color. To return the color to the default color, send an
          empty string as in this example: ``:BUS:B1:LABEL:COLOR`` ''.
    """

    _WRAP_ARG_WITH_QUOTES = True


class BusBItemLabel(SCPICmdRead):
    """The ``BUS:B<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.color``: The ``BUS:B<x>:LABel:COLor`` command.
        - ``.font``: The ``BUS:B<x>:LABel:FONT`` command tree.
        - ``.xpos``: The ``BUS:B<x>:LABel:XPOS`` command.
        - ``.ypos``: The ``BUS:B<x>:LABel:YPOS`` command.
        - ``.name``: The ``BUS:B<x>:LABel:name`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._color = BusBItemLabelColor(device, f"{self._cmd_syntax}:COLor")
        self._font = BusBItemLabelFont(device, f"{self._cmd_syntax}:FONT")
        self._xpos = BusBItemLabelXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = BusBItemLabelYpos(device, f"{self._cmd_syntax}:YPOS")
        self._name = BusBItemLabelName(device, f"{self._cmd_syntax}:name")

    @property
    def color(self) -> BusBItemLabelColor:
        """Return the ``BUS:B<x>:LABel:COLor`` command.

        Description:
            - This command sets or queries the color of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:COLor?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:COLor?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:COLor value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:COLor <QString>
            - BUS:B<x>:LABel:COLor?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<QString>`` is the bus label color. To return the color to the default color, send
              an empty string as in this example: ``:BUS:B1:LABEL:COLOR`` ''.
        """
        return self._color

    @property
    def font(self) -> BusBItemLabelFont:
        """Return the ``BUS:B<x>:LABel:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:FONT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bold``: The ``BUS:B<x>:LABel:FONT:BOLD`` command.
            - ``.italic``: The ``BUS:B<x>:LABel:FONT:ITALic`` command.
            - ``.size``: The ``BUS:B<x>:LABel:FONT:SIZE`` command.
            - ``.type``: The ``BUS:B<x>:LABel:FONT:TYPE`` command.
            - ``.underline``: The ``BUS:B<x>:LABel:FONT:UNDERline`` command.
        """
        return self._font

    @property
    def xpos(self) -> BusBItemLabelXpos:
        """Return the ``BUS:B<x>:LABel:XPOS`` command.

        Description:
            - This command sets or queries the x-position of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:XPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:XPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:XPOS value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:XPOS <NR3>
            - BUS:B<x>:LABel:XPOS?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the x-position, in pixels relative to the left edge of the screen of the
              specified bus label.
        """
        return self._xpos

    @property
    def ypos(self) -> BusBItemLabelYpos:
        """Return the ``BUS:B<x>:LABel:YPOS`` command.

        Description:
            - This command sets or queries the y-position of the specified bus label. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:YPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:YPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:YPOS value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:YPOS <NR3>
            - BUS:B<x>:LABel:YPOS?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the y-position, in pixels relative to the baseline of the waveform, of
              the specified bus label.
        """
        return self._ypos

    @property
    def name(self) -> BusBItemLabelName:
        """Return the ``BUS:B<x>:LABel:name`` command.

        Description:
            - This command sets or queries the label for the specified bus. The bus is specified by
              x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel:name?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel:name?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel:name value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel:name <QString>
            - BUS:B<x>:LABel:name?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<QString>`` is an alphanumeric string of text enclosed in quotes. The text string is
              limited to 30 characters. It contains the text label information for the bus.
        """
        return self._name


class BusBItemI2cRwinaddr(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:RWINADDR`` command.

    Description:
        - This command sets or queries the manner in which seven-bit I2C addresses are represented
          in the busform display of the specified bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:RWINADDR {0|1}
        - BUS:B<x>:I2C:RWINADDR?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``0`` displays seven-bit slave addresses as integers in the range of 0 to 127, with the
          state of the R/W* bit from the LSB of the slave address byte. For example, the slave
          address byte of 0b10100101 is displayed as the value 0x52 R.
        - ``1`` displays the entire slave address byte as a number, with the R/W* signal as its LSB
          (bit 0) and the slave address in bits 7..1. For example, the slave address byte of
          0b10100101 is displayed as the value 0xA5 R.
    """


class BusBItemI2cDataThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:DATa:THReshold`` command.

    Description:
        - This command sets or queries the I2C Data (SDA) source threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:DATa:THReshold <NR3>
        - BUS:B<x>:I2C:DATa:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the I2C Data (SDA) source threshold for the specified bus.
    """


class BusBItemI2cDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:DATa:SOUrce`` command.

    Description:
        - This command sets or queries the I2C data (SDA) source for the specified I2C bus. The bus
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:DATa:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:I2C:DATa:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``CH<x>`` specifies an analog channel to use as the I2C SDA source.
        - ``DCH<x>_D<x>`` specifies a digital channel to use as the I2C SDA source. The supported
          digital channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` specifies a math waveform to use as the I2C SDA source.
        - ``REF<x>`` specifies a reference waveform to use as the I2C SDA source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform for the
          specified I2C bus.
    """


class BusBItemI2cData(SCPICmdRead):
    """The ``BUS:B<x>:I2C:DATa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:DATa:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:I2C:DATa:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cDataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemI2cDataThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemI2cDataSource:
        """Return the ``BUS:B<x>:I2C:DATa:SOUrce`` command.

        Description:
            - This command sets or queries the I2C data (SDA) source for the specified I2C bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:DATa:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:I2C:DATa:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``CH<x>`` specifies an analog channel to use as the I2C SDA source.
            - ``DCH<x>_D<x>`` specifies a digital channel to use as the I2C SDA source. The
              supported digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``MATH<x>`` specifies a math waveform to use as the I2C SDA source.
            - ``REF<x>`` specifies a reference waveform to use as the I2C SDA source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the data source waveform for
              the specified I2C bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemI2cDataThreshold:
        """Return the ``BUS:B<x>:I2C:DATa:THReshold`` command.

        Description:
            - This command sets or queries the I2C Data (SDA) source threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATa:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:DATa:THReshold <NR3>
            - BUS:B<x>:I2C:DATa:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the I2C Data (SDA) source threshold for the specified bus.
        """
        return self._threshold


class BusBItemI2cClockThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:CLOCk:THReshold`` command.

    Description:
        - This command sets or queries the I2C Clock (SCLK) source threshold for the specified bus.
          The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:THReshold?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:THReshold value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:CLOCk:THReshold <NR3>
        - BUS:B<x>:I2C:CLOCk:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the I2C Clock (SCLK) source threshold for the specified bus.
    """


class BusBItemI2cClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.

    Description:
        - This command sets or queries the I2C clock (SCLK) source for the specified bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:I2C:CLOCk:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``CH<x>`` specifies an analog channel to use as the I2C SCLK source.
        - ``DCH<x>_D<x>`` specifies a digital channel to use as the I2C SCLK source. The supported
          digital channel value is 1. The supported digital bit values are 0 to 15.
        - ``MATH<x>`` specifies a math waveform to use as the I2C SCLK source.
        - ``REF<x>`` specifies a reference waveform to use as the I2C SCLK source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform for
          the specified I2C bus.
    """


class BusBItemI2cClock(SCPICmdRead):
    """The ``BUS:B<x>:I2C:CLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.
        - ``.threshold``: The ``BUS:B<x>:I2C:CLOCk:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cClockSource(device, f"{self._cmd_syntax}:SOUrce")
        self._threshold = BusBItemI2cClockThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def source(self) -> BusBItemI2cClockSource:
        """Return the ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.

        Description:
            - This command sets or queries the I2C clock (SCLK) source for the specified bus. The
              bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:CLOCk:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:I2C:CLOCk:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``CH<x>`` specifies an analog channel to use as the I2C SCLK source.
            - ``DCH<x>_D<x>`` specifies a digital channel to use as the I2C SCLK source. The
              supported digital channel value is 1. The supported digital bit values are 0 to 15.
            - ``MATH<x>`` specifies a math waveform to use as the I2C SCLK source.
            - ``REF<x>`` specifies a reference waveform to use as the I2C SCLK source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the clock source waveform
              for the specified I2C bus.
        """
        return self._source

    @property
    def threshold(self) -> BusBItemI2cClockThreshold:
        """Return the ``BUS:B<x>:I2C:CLOCk:THReshold`` command.

        Description:
            - This command sets or queries the I2C Clock (SCLK) source threshold for the specified
              bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk:THReshold?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:I2C:CLOCk:THReshold value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:CLOCk:THReshold <NR3>
            - BUS:B<x>:I2C:CLOCk:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the I2C Clock (SCLK) source threshold for the specified bus.
        """
        return self._threshold


class BusBItemI2c(SCPICmdRead):
    """The ``BUS:B<x>:I2C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.clock``: The ``BUS:B<x>:I2C:CLOCk`` command tree.
        - ``.data``: The ``BUS:B<x>:I2C:DATa`` command tree.
        - ``.rwinaddr``: The ``BUS:B<x>:I2C:RWINADDR`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clock = BusBItemI2cClock(device, f"{self._cmd_syntax}:CLOCk")
        self._data = BusBItemI2cData(device, f"{self._cmd_syntax}:DATa")
        self._rwinaddr = BusBItemI2cRwinaddr(device, f"{self._cmd_syntax}:RWINADDR")

    @property
    def clock(self) -> BusBItemI2cClock:
        """Return the ``BUS:B<x>:I2C:CLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I2C:CLOCk:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:I2C:CLOCk:THReshold`` command.
        """
        return self._clock

    @property
    def data(self) -> BusBItemI2cData:
        """Return the ``BUS:B<x>:I2C:DATa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATa?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I2C:DATa:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:I2C:DATa:THReshold`` command.
        """
        return self._data

    @property
    def rwinaddr(self) -> BusBItemI2cRwinaddr:
        """Return the ``BUS:B<x>:I2C:RWINADDR`` command.

        Description:
            - This command sets or queries the manner in which seven-bit I2C addresses are
              represented in the busform display of the specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:RWINADDR value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:RWINADDR {0|1}
            - BUS:B<x>:I2C:RWINADDR?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``0`` displays seven-bit slave addresses as integers in the range of 0 to 127, with
              the state of the R/W* bit from the LSB of the slave address byte. For example, the
              slave address byte of 0b10100101 is displayed as the value 0x52 R.
            - ``1`` displays the entire slave address byte as a number, with the R/W* signal as its
              LSB (bit 0) and the slave address in bits 7..1. For example, the slave address byte of
              0b10100101 is displayed as the value 0xA5 R.
        """
        return self._rwinaddr


class BusBItemDisplayLayout(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DISplay:LAYout`` command.

    Description:
        - This command sets or queries what to display for the specified bus. The bus is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:LAYout?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:LAYout?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:LAYout value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DISplay:LAYout {BUS|BUSANDWAVEFORM}
        - BUS:B<x>:DISplay:LAYout?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``BUS`` specifies displaying the bus form only.
        - ``BUSANDWAVEFORM`` specifies displaying the bus form and the constituent source
          waveform(s). This argument is not available for some bus types and some bus
          configurations.
    """


class BusBItemDisplayFormat(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DISplay:FORMat`` command.

    Description:
        - This command sets or queries how the data is represented in the bus form for the specified
          bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:FORMat value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DISplay:FORMat {HEX|BINARY|MIXEDASCII|MIXEDHEX|ASCII|DECIMAL|MIXED}
        - BUS:B<x>:DISplay:FORMat?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``HEX`` specifies hexadecimal format.
        - ``BINARY`` specifies binary format.
        - ``MIXEDASCII`` specifies mixed ASCII format.
        - ``MIXEDHEX`` specifies mixed hexadecimal format.
        - ``ASCII`` specifies ASCII format.
        - ``DECIMAL`` specifies decimal format.
        - ``MIXED`` specifies mixed format.
    """


class BusBItemDisplay(SCPICmdRead):
    """The ``BUS:B<x>:DISplay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.format``: The ``BUS:B<x>:DISplay:FORMat`` command.
        - ``.layout``: The ``BUS:B<x>:DISplay:LAYout`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._format = BusBItemDisplayFormat(device, f"{self._cmd_syntax}:FORMat")
        self._layout = BusBItemDisplayLayout(device, f"{self._cmd_syntax}:LAYout")

    @property
    def format(self) -> BusBItemDisplayFormat:
        """Return the ``BUS:B<x>:DISplay:FORMat`` command.

        Description:
            - This command sets or queries how the data is represented in the bus form for the
              specified bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:FORMat?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:FORMat value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DISplay:FORMat {HEX|BINARY|MIXEDASCII|MIXEDHEX|ASCII|DECIMAL|MIXED}
            - BUS:B<x>:DISplay:FORMat?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``HEX`` specifies hexadecimal format.
            - ``BINARY`` specifies binary format.
            - ``MIXEDASCII`` specifies mixed ASCII format.
            - ``MIXEDHEX`` specifies mixed hexadecimal format.
            - ``ASCII`` specifies ASCII format.
            - ``DECIMAL`` specifies decimal format.
            - ``MIXED`` specifies mixed format.
        """
        return self._format

    @property
    def layout(self) -> BusBItemDisplayLayout:
        """Return the ``BUS:B<x>:DISplay:LAYout`` command.

        Description:
            - This command sets or queries what to display for the specified bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:LAYout?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:LAYout?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:LAYout value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DISplay:LAYout {BUS|BUSANDWAVEFORM}
            - BUS:B<x>:DISplay:LAYout?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``BUS`` specifies displaying the bus form only.
            - ``BUSANDWAVEFORM`` specifies displaying the bus form and the constituent source
              waveform(s). This argument is not available for some bus types and some bus
              configurations.
        """
        return self._layout


class BusBItemCanThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:THReshold`` command.

    Description:
        - This command sets or queries the source channel threshold for the specified CAN bus. The
          bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:THReshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:THReshold value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:THReshold <NR3>
        - BUS:B<x>:CAN:THReshold?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` is the source channel threshold for the specified CAN bus.
    """


class BusBItemCanStandard(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:STANDard`` command.

    Description:
        - This command sets or queries which CAN standard specification to analyze the specified CAN
          bus with. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:STANDard?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:STANDard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:STANDard value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:STANDard {CAN2X|FDISO|FDNONISO}
        - BUS:B<x>:CAN:STANDard?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``CAN2X`` sets the CAN bus standard to CAN 2.0.
        - ``FDISO`` sets the CAN bus standard to ISO CAN FD (11898-``1:2015``).
        - ``FDNONISO`` sets the CAN bus standard to non-ISO CAN FD (``Bosch:2012``).
    """


class BusBItemCanSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:SOUrce`` command.

    Description:
        - This command sets or queries the CAN source channel for the specified CAN bus. The bus
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
        - BUS:B<x>:CAN:SOUrce?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``CH<x>`` specifies an analog channel to use as the source.
        - ``DCH<x>_D<x>`` specifies a digital channel to use as the source. The supported digital
          channel value is 1. The supported digital bits values are 0 to 15.
        - ``MATH<x>`` specifies a math waveform to use as the source.
        - ``REF<x>`` specifies a reference waveform to use as the source.
        - ``REF<x>_D<x>`` specifies a digital reference waveform as the source.
    """


class BusBItemCanSignal(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:SIGNal`` command.

    Description:
        - This command sets or queries the signal type for the specified CAN bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SIGNal?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SIGNal?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SIGNal value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:SIGNal {DIFFerential|CANH|CANL|RX|TX}
        - BUS:B<x>:CAN:SIGNal?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
    """


class BusBItemCanSamplepoint(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:SAMPLEpoint`` command.

    Description:
        - This command sets or queries the sample point for the specified CAN bus. The bus is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:SAMPLEpoint <NR1>
        - BUS:B<x>:CAN:SAMPLEpoint?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the sample point, in percent, for the specified CAN bus.
    """


class BusBItemCanFdBitrateCustom(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` command.

    Description:
        - This command sets or queries the custom bit rate for the increased data phase of CAN FD
          packets on the specified CAN bus. The bus is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:BITRate:CUSTom?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate:CUSTom?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate:CUSTom value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:FD:BITRate:CUSTom <NR1>
        - BUS:B<x>:CAN:FD:BITRate:CUSTom?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR1>`` is the custom FD bit rate for the specified bus.
    """


class BusBItemCanFdBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:FD:BITRate`` command.

    Description:
        - This command sets or queries the increased data phase bit rate used by CAN FD packets on
          the specified CAN bus. The bus is specified by x. If you select Custom, use
          ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` to set the bit rate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:FD:BITRate {RATE1M|RATE2M|RATE3M|RATE4M|RATE5M|RATE6M|RATE7M|RATE8M|RATE9M|RATE10M|RATE11M|RATE12M|RATE13M|RATE14M|RATE15M|RATE16M|CUSTom}
        - BUS:B<x>:CAN:FD:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.custom``: The ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custom = BusBItemCanFdBitrateCustom(device, f"{self._cmd_syntax}:CUSTom")

    @property
    def custom(self) -> BusBItemCanFdBitrateCustom:
        """Return the ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` command.

        Description:
            - This command sets or queries the custom bit rate for the increased data phase of CAN
              FD packets on the specified CAN bus. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:BITRate:CUSTom?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate:CUSTom?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:CAN:FD:BITRate:CUSTom value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:FD:BITRate:CUSTom <NR1>
            - BUS:B<x>:CAN:FD:BITRate:CUSTom?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the custom FD bit rate for the specified bus.
        """
        return self._custom


class BusBItemCanFd(SCPICmdRead):
    """The ``BUS:B<x>:CAN:FD`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:CAN:FD:BITRate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemCanFdBitrate(device, f"{self._cmd_syntax}:BITRate")

    @property
    def bitrate(self) -> BusBItemCanFdBitrate:
        """Return the ``BUS:B<x>:CAN:FD:BITRate`` command.

        Description:
            - This command sets or queries the increased data phase bit rate used by CAN FD packets
              on the specified CAN bus. The bus is specified by x. If you select Custom, use
              ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` to set the bit rate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:FD:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:FD:BITRate {RATE1M|RATE2M|RATE3M|RATE4M|RATE5M|RATE6M|RATE7M|RATE8M|RATE9M|RATE10M|RATE11M|RATE12M|RATE13M|RATE14M|RATE15M|RATE16M|CUSTom}
            - BUS:B<x>:CAN:FD:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.custom``: The ``BUS:B<x>:CAN:FD:BITRate:CUSTom`` command.
        """  # noqa: E501
        return self._bitrate


class BusBItemCanBitrateValue(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:BITRate:VALue`` command.

    Description:
        - This command sets or queries CAN bit rate when Custom is selected by
          ``BUS:BX:CAN:BITRATE``. The bus number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:BITRate:VALue <NR3>
        - BUS:B<x>:CAN:BITRate:VALue?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``<NR3>`` specifies the CAN bit rate.
    """


class BusBItemCanBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:BITRate`` command.

    Description:
        - This command sets or queries the CAN bit rate. The bus number is specified by x. If you
          select Custom, use ``BUS:BX:CAN:BITRATE:VALUE`` to set the bit rate.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:BITRate {RATE10K|RATE100K|RATE1M|RATE125K|RATE153K|RATE20K|RATE25K|RATE250K|RATE31K|RATE33K|RATE400K|RATE50K|RATE500K|RATE62K|RATE68K|RATE800K|RATE83K|RATE92K|CUSTom}
        - BUS:B<x>:CAN:BITRate?
        ```

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.value``: The ``BUS:B<x>:CAN:BITRate:VALue`` command.
    """  # noqa: E501

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = BusBItemCanBitrateValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def value(self) -> BusBItemCanBitrateValue:
        """Return the ``BUS:B<x>:CAN:BITRate:VALue`` command.

        Description:
            - This command sets or queries CAN bit rate when Custom is selected by
              ``BUS:BX:CAN:BITRATE``. The bus number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate:VALue value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:BITRate:VALue <NR3>
            - BUS:B<x>:CAN:BITRate:VALue?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` specifies the CAN bit rate.
        """
        return self._value


class BusBItemCan(SCPICmdRead):
    """The ``BUS:B<x>:CAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:CAN:BITRate`` command.
        - ``.fd``: The ``BUS:B<x>:CAN:FD`` command tree.
        - ``.samplepoint``: The ``BUS:B<x>:CAN:SAMPLEpoint`` command.
        - ``.signal``: The ``BUS:B<x>:CAN:SIGNal`` command.
        - ``.source``: The ``BUS:B<x>:CAN:SOUrce`` command.
        - ``.standard``: The ``BUS:B<x>:CAN:STANDard`` command.
        - ``.threshold``: The ``BUS:B<x>:CAN:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemCanBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._fd = BusBItemCanFd(device, f"{self._cmd_syntax}:FD")
        self._samplepoint = BusBItemCanSamplepoint(device, f"{self._cmd_syntax}:SAMPLEpoint")
        self._signal = BusBItemCanSignal(device, f"{self._cmd_syntax}:SIGNal")
        self._source = BusBItemCanSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = BusBItemCanStandard(device, f"{self._cmd_syntax}:STANDard")
        self._threshold = BusBItemCanThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def bitrate(self) -> BusBItemCanBitrate:
        """Return the ``BUS:B<x>:CAN:BITRate`` command.

        Description:
            - This command sets or queries the CAN bit rate. The bus number is specified by x. If
              you select Custom, use ``BUS:BX:CAN:BITRATE:VALUE`` to set the bit rate.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:BITRate {RATE10K|RATE100K|RATE1M|RATE125K|RATE153K|RATE20K|RATE25K|RATE250K|RATE31K|RATE33K|RATE400K|RATE50K|RATE500K|RATE62K|RATE68K|RATE800K|RATE83K|RATE92K|CUSTom}
            - BUS:B<x>:CAN:BITRate?
            ```

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.value``: The ``BUS:B<x>:CAN:BITRate:VALue`` command.
        """  # noqa: E501
        return self._bitrate

    @property
    def fd(self) -> BusBItemCanFd:
        """Return the ``BUS:B<x>:CAN:FD`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:FD?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:FD?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:CAN:FD:BITRate`` command.
        """
        return self._fd

    @property
    def samplepoint(self) -> BusBItemCanSamplepoint:
        """Return the ``BUS:B<x>:CAN:SAMPLEpoint`` command.

        Description:
            - This command sets or queries the sample point for the specified CAN bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SAMPLEpoint value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:SAMPLEpoint <NR1>
            - BUS:B<x>:CAN:SAMPLEpoint?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR1>`` is the sample point, in percent, for the specified CAN bus.
        """
        return self._samplepoint

    @property
    def signal(self) -> BusBItemCanSignal:
        """Return the ``BUS:B<x>:CAN:SIGNal`` command.

        Description:
            - This command sets or queries the signal type for the specified CAN bus. The bus is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SIGNal?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SIGNal?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SIGNal value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:SIGNal {DIFFerential|CANH|CANL|RX|TX}
            - BUS:B<x>:CAN:SIGNal?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
        """
        return self._signal

    @property
    def source(self) -> BusBItemCanSource:
        """Return the ``BUS:B<x>:CAN:SOUrce`` command.

        Description:
            - This command sets or queries the CAN source channel for the specified CAN bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>|REF<x>_D<x>}
            - BUS:B<x>:CAN:SOUrce?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``CH<x>`` specifies an analog channel to use as the source.
            - ``DCH<x>_D<x>`` specifies a digital channel to use as the source. The supported
              digital channel value is 1. The supported digital bits values are 0 to 15.
            - ``MATH<x>`` specifies a math waveform to use as the source.
            - ``REF<x>`` specifies a reference waveform to use as the source.
            - ``REF<x>_D<x>`` specifies a digital reference waveform as the source.
        """
        return self._source

    @property
    def standard(self) -> BusBItemCanStandard:
        """Return the ``BUS:B<x>:CAN:STANDard`` command.

        Description:
            - This command sets or queries which CAN standard specification to analyze the specified
              CAN bus with. The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:STANDard?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:STANDard?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:STANDard value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:STANDard {CAN2X|FDISO|FDNONISO}
            - BUS:B<x>:CAN:STANDard?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``CAN2X`` sets the CAN bus standard to CAN 2.0.
            - ``FDISO`` sets the CAN bus standard to ISO CAN FD (11898-``1:2015``).
            - ``FDNONISO`` sets the CAN bus standard to non-ISO CAN FD (``Bosch:2012``).
        """
        return self._standard

    @property
    def threshold(self) -> BusBItemCanThreshold:
        """Return the ``BUS:B<x>:CAN:THReshold`` command.

        Description:
            - This command sets or queries the source channel threshold for the specified CAN bus.
              The bus is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:THReshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:THReshold value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:THReshold <NR3>
            - BUS:B<x>:CAN:THReshold?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``<NR3>`` is the source channel threshold for the specified CAN bus.
        """
        return self._threshold


#  pylint: disable=too-many-instance-attributes
class BusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``B<x>`` is the number of the bus.

    Properties:
        - ``.can``: The ``BUS:B<x>:CAN`` command tree.
        - ``.display``: The ``BUS:B<x>:DISplay`` command tree.
        - ``.i2c``: The ``BUS:B<x>:I2C`` command tree.
        - ``.label``: The ``BUS:B<x>:LABel`` command tree.
        - ``.lin``: The ``BUS:B<x>:LIN`` command tree.
        - ``.parallel``: The ``BUS:B<x>:PARallel`` command tree.
        - ``.rs232c``: The ``BUS:B<x>:RS232C`` command tree.
        - ``.sent``: The ``BUS:B<x>:SENT`` command tree.
        - ``.spi``: The ``BUS:B<x>:SPI`` command tree.
        - ``.type``: The ``BUS:B<x>:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._can = BusBItemCan(device, f"{self._cmd_syntax}:CAN")
        self._display = BusBItemDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._i2c = BusBItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._label = BusBItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._lin = BusBItemLin(device, f"{self._cmd_syntax}:LIN")
        self._parallel = BusBItemParallel(device, f"{self._cmd_syntax}:PARallel")
        self._rs232c = BusBItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._sent = BusBItemSent(device, f"{self._cmd_syntax}:SENT")
        self._spi = BusBItemSpi(device, f"{self._cmd_syntax}:SPI")
        self._type = BusBItemType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def can(self) -> BusBItemCan:
        """Return the ``BUS:B<x>:CAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:CAN:BITRate`` command.
            - ``.fd``: The ``BUS:B<x>:CAN:FD`` command tree.
            - ``.samplepoint``: The ``BUS:B<x>:CAN:SAMPLEpoint`` command.
            - ``.signal``: The ``BUS:B<x>:CAN:SIGNal`` command.
            - ``.source``: The ``BUS:B<x>:CAN:SOUrce`` command.
            - ``.standard``: The ``BUS:B<x>:CAN:STANDard`` command.
            - ``.threshold``: The ``BUS:B<x>:CAN:THReshold`` command.
        """
        return self._can

    @property
    def display(self) -> BusBItemDisplay:
        """Return the ``BUS:B<x>:DISplay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.format``: The ``BUS:B<x>:DISplay:FORMat`` command.
            - ``.layout``: The ``BUS:B<x>:DISplay:LAYout`` command.
        """
        return self._display

    @property
    def i2c(self) -> BusBItemI2c:
        """Return the ``BUS:B<x>:I2C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.clock``: The ``BUS:B<x>:I2C:CLOCk`` command tree.
            - ``.data``: The ``BUS:B<x>:I2C:DATa`` command tree.
            - ``.rwinaddr``: The ``BUS:B<x>:I2C:RWINADDR`` command.
        """
        return self._i2c

    @property
    def label(self) -> BusBItemLabel:
        """Return the ``BUS:B<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.color``: The ``BUS:B<x>:LABel:COLor`` command.
            - ``.font``: The ``BUS:B<x>:LABel:FONT`` command tree.
            - ``.xpos``: The ``BUS:B<x>:LABel:XPOS`` command.
            - ``.ypos``: The ``BUS:B<x>:LABel:YPOS`` command.
            - ``.name``: The ``BUS:B<x>:LABel:name`` command.
        """
        return self._label

    @property
    def lin(self) -> BusBItemLin:
        """Return the ``BUS:B<x>:LIN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:LIN:BITRate`` command.
            - ``.idformat``: The ``BUS:B<x>:LIN:IDFORmat`` command.
            - ``.polarity``: The ``BUS:B<x>:LIN:POLarity`` command.
            - ``.samplepoint``: The ``BUS:B<x>:LIN:SAMPLEpoint`` command.
            - ``.source``: The ``BUS:B<x>:LIN:SOUrce`` command.
            - ``.standard``: The ``BUS:B<x>:LIN:STANDard`` command.
        """
        return self._lin

    @property
    def parallel(self) -> BusBItemParallel:
        """Return the ``BUS:B<x>:PARallel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.allthresholds``: The ``BUS:B<x>:PARallel:ALLTHResholds`` command.
            - ``.bitsource``: The ``BUS:B<x>:PARallel:BIT<x>SOUrce`` command.
            - ``.clock``: The ``BUS:B<x>:PARallel:CLOCk`` command tree.
            - ``.clocksource``: The ``BUS:B<x>:PARallel:CLOCkSOUrce`` command.
        """
        return self._parallel

    @property
    def rs232c(self) -> BusBItemRs232c:
        """Return the ``BUS:B<x>:RS232C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:RS232C:BITRate`` command.
            - ``.databits``: The ``BUS:B<x>:RS232C:DATABits`` command.
            - ``.delimiter``: The ``BUS:B<x>:RS232C:DELIMiter`` command.
            - ``.displaymode``: The ``BUS:B<x>:RS232C:DISplaymode`` command.
            - ``.parity``: The ``BUS:B<x>:RS232C:PARity`` command.
            - ``.polarity``: The ``BUS:B<x>:RS232C:POLarity`` command.
            - ``.source``: The ``BUS:B<x>:RS232C:SOUrce`` command.
        """
        return self._rs232c

    @property
    def sent(self) -> BusBItemSent:
        """Return the ``BUS:B<x>:SENT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SENT?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SENT?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.chanwidth``: The ``BUS:B<x>:SENT:CHANWidth`` command.
            - ``.nibblecount``: The ``BUS:B<x>:SENT:NIBBLECount`` command.
            - ``.numchannel``: The ``BUS:B<x>:SENT:NUMCHANnel`` command.
            - ``.pausepulse``: The ``BUS:B<x>:SENT:PAUSEPULSe`` command.
            - ``.polarity``: The ``BUS:B<x>:SENT:POLARITY`` command.
            - ``.slow``: The ``BUS:B<x>:SENT:SLOW`` command.
            - ``.source``: The ``BUS:B<x>:SENT:SOUrce`` command.
            - ``.threshold``: The ``BUS:B<x>:SENT:THRESHold`` command.
            - ``.ticktime``: The ``BUS:B<x>:SENT:TICKTIME`` command.
            - ``.ticktolerance``: The ``BUS:B<x>:SENT:TICKTOLerance`` command.
        """
        return self._sent

    @property
    def spi(self) -> BusBItemSpi:
        """Return the ``BUS:B<x>:SPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus waveform.

        Sub-properties:
            - ``.bitorder``: The ``BUS:B<x>:SPI:BITOrder`` command.
            - ``.clock``: The ``BUS:B<x>:SPI:CLOCk`` command tree.
            - ``.data``: The ``BUS:B<x>:SPI:DATa`` command tree.
            - ``.framing``: The ``BUS:B<x>:SPI:FRAMING`` command.
            - ``.idletime``: The ``BUS:B<x>:SPI:IDLETime`` command.
            - ``.miso``: The ``BUS:B<x>:SPI:MISo`` command tree.
            - ``.mosi``: The ``BUS:B<x>:SPI:MOSi`` command tree.
            - ``.number``: The ``BUS:B<x>:SPI:NUMBer`` command tree.
            - ``.select``: The ``BUS:B<x>:SPI:SELect`` command tree.
        """
        return self._spi

    @property
    def type(self) -> BusBItemType:
        """Return the ``BUS:B<x>:TYPe`` command.

        Description:
            - This command sets or queries the bus type or standard for the specified bus. The bus
              is specified by x. Arguments for a bus type are only available then the required
              serial bus option is installed.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:TYPe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:TYPe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:TYPe {CAN|I2C|LIN|PARallel|RS232C|SENT|SPI}
            - BUS:B<x>:TYPe?
            ```

        Info:
            - ``B<x>`` is the number of the bus waveform.
            - ``CAN`` specifies a Controller Area Network bus.
            - ``I2C`` specifies the Inter-IC bus.
            - ``LIN`` specifies a Local Interconnect Network bus.
            - ``PARallel`` specifies a parallel bus.
            - ``RS232C`` specifies the RS-232 Serial bus.
            - ``SENT`` specifies the Single Edge Nibble Transmission (SENT) automotive serial bus.
            - ``SPI`` specifies the Serial Peripheral Interface bus.
        """
        return self._type


class BusAddnew(SCPICmdWrite):
    """The ``BUS:ADDNew`` command.

    Description:
        - This command adds the specified bus. This command creates/adds the bus but does not
          display it (turn it on). In order to enable bus decoding and see the bus display on
          screen, send the ``DISPLAY:WAVEVIEWX:BUS:BX:STATE ON`` command.

    Usage:
        - Using the ``.write(value)`` method will send the ``BUS:ADDNew value`` command.

    SCPI Syntax:
        ```
        - BUS:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string of the form 'B<NR1>' where NR1 is ≥1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Bus(SCPICmdRead):
    """The ``BUS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``BUS:ADDNew`` command.
        - ``.b``: The ``BUS:B<x>`` command tree.
        - ``.delete``: The ``BUS:DELete`` command.
        - ``.list``: The ``BUS:LIST`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "BUS") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = BusAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._b: Dict[int, BusBItem] = DefaultDictPassKeyToFactory(
            lambda x: BusBItem(device, f"{self._cmd_syntax}:B{x}")
        )
        self._delete = BusDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = BusList(device, f"{self._cmd_syntax}:LIST")

    @property
    def addnew(self) -> BusAddnew:
        """Return the ``BUS:ADDNew`` command.

        Description:
            - This command adds the specified bus. This command creates/adds the bus but does not
              display it (turn it on). In order to enable bus decoding and see the bus display on
              screen, send the ``DISPLAY:WAVEVIEWX:BUS:BX:STATE ON`` command.

        Usage:
            - Using the ``.write(value)`` method will send the ``BUS:ADDNew value`` command.

        SCPI Syntax:
            ```
            - BUS:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string of the form 'B<NR1>' where NR1 is ≥1.
        """
        return self._addnew

    @property
    def b(self) -> Dict[int, BusBItem]:
        """Return the ``BUS:B<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``B<x>`` is the number of the bus.

        Sub-properties:
            - ``.can``: The ``BUS:B<x>:CAN`` command tree.
            - ``.display``: The ``BUS:B<x>:DISplay`` command tree.
            - ``.i2c``: The ``BUS:B<x>:I2C`` command tree.
            - ``.label``: The ``BUS:B<x>:LABel`` command tree.
            - ``.lin``: The ``BUS:B<x>:LIN`` command tree.
            - ``.parallel``: The ``BUS:B<x>:PARallel`` command tree.
            - ``.rs232c``: The ``BUS:B<x>:RS232C`` command tree.
            - ``.sent``: The ``BUS:B<x>:SENT`` command tree.
            - ``.spi``: The ``BUS:B<x>:SPI`` command tree.
            - ``.type``: The ``BUS:B<x>:TYPe`` command.
        """
        return self._b

    @property
    def delete(self) -> BusDelete:
        """Return the ``BUS:DELete`` command.

        Description:
            - This command deletes the specified bus.

        Usage:
            - Using the ``.write(value)`` method will send the ``BUS:DELete value`` command.

        SCPI Syntax:
            ```
            - BUS:DELete <QString>
            ```

        Info:
            - ``<QString>`` specifies the bus to delete and is of the form 'B<NR1>', where <NR1> is
              ≥1.
        """
        return self._delete

    @property
    def list(self) -> BusList:
        """Return the ``BUS:LIST`` command.

        Description:
            - This query returns a comma separated list of all currently defined buses.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:LIST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - BUS:LIST?
            ```
        """
        return self._list
