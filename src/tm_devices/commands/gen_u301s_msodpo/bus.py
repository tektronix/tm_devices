"""The bus commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - BUS
    - BUS:B<x>:CAN:BITRate <NR1>
    - BUS:B<x>:CAN:BITRate?
    - BUS:B<x>:CAN:PRObe {CANH|CANL|RX|TX|DIFFerential}
    - BUS:B<x>:CAN:PRObe?
    - BUS:B<x>:CAN:SAMPLEpoint <NR1>
    - BUS:B<x>:CAN:SAMPLEpoint?
    - BUS:B<x>:CAN:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:CAN:SOUrce?
    - BUS:B<x>:DISplay:FORMAt {BINary|HEXadecimal|ASCII|MIXed}
    - BUS:B<x>:DISplay:FORMAt?
    - BUS:B<x>:DISplay:TYPe {BUS|BOTh}
    - BUS:B<x>:DISplay:TYPe?
    - BUS:B<x>:FLEXray:BITRate <NR1>
    - BUS:B<x>:FLEXray:BITRate?
    - BUS:B<x>:FLEXray:CHannel {A|B}
    - BUS:B<x>:FLEXray:CHannel?
    - BUS:B<x>:FLEXray:SIGnal {BDIFFBP|BM|TXRX}
    - BUS:B<x>:FLEXray:SIGnal?
    - BUS:B<x>:FLEXray:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:FLEXray:SOUrce?
    - BUS:B<x>:I2C:ADDRess:RWINClude {ON|OFF|<NR1>}
    - BUS:B<x>:I2C:ADDRess:RWINClude?
    - BUS:B<x>:I2C:CLOCK:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:I2C:CLOCK:SOUrce?
    - BUS:B<x>:I2C:DATA:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:I2C:DATA:SOUrce?
    - BUS:B<x>:I2C:SCLK:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:I2C:SCLK:SOUrce?
    - BUS:B<x>:I2C:SDATA:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:I2C:SDATA:SOUrce?
    - BUS:B<x>:LABel <Qstring>
    - BUS:B<x>:LABel?
    - BUS:B<x>:LIN:BITRate <NR1>
    - BUS:B<x>:LIN:BITRate?
    - BUS:B<x>:LIN:IDFORmat {NOPARity|PARity}
    - BUS:B<x>:LIN:IDFORmat?
    - BUS:B<x>:LIN:POLARity {NORMal|INVerted}
    - BUS:B<x>:LIN:POLARity?
    - BUS:B<x>:LIN:SAMPLEpoint <NR1>
    - BUS:B<x>:LIN:SAMPLEpoint?
    - BUS:B<x>:LIN:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:LIN:SOUrce?
    - BUS:B<x>:LIN:STANDard {V1X|V2X|MIXed}
    - BUS:B<x>:LIN:STANDard?
    - BUS:B<x>:PARallel:BIT<x>:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:PARallel:BIT<x>:SOUrce?
    - BUS:B<x>:PARallel:CLOCK:EDGE {EITher|RISing|FALling}
    - BUS:B<x>:PARallel:CLOCK:EDGE?
    - BUS:B<x>:PARallel:CLOCK:ISCLOCKed {YES|NO}
    - BUS:B<x>:PARallel:CLOCK:ISCLOCKed?
    - BUS:B<x>:PARallel:CLOCK:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:PARallel:CLOCK:SOUrce?
    - BUS:B<x>:PARallel:WIDth <NR1>
    - BUS:B<x>:PARallel:WIDth?
    - BUS:B<x>:POSition <NR3>
    - BUS:B<x>:POSition?
    - BUS:B<x>:RS232C:BITRate <NR1>
    - BUS:B<x>:RS232C:BITRate?
    - BUS:B<x>:RS232C:DATABits {7|8|9}
    - BUS:B<x>:RS232C:DATABits?
    - BUS:B<x>:RS232C:DELIMiter {NULl|LF|CR|SPace|XFF}
    - BUS:B<x>:RS232C:DELIMiter?
    - BUS:B<x>:RS232C:DISplaymode {FRAme|PACKET}
    - BUS:B<x>:RS232C:DISplaymode?
    - BUS:B<x>:RS232C:PARity {NONe|EVEN|ODD}
    - BUS:B<x>:RS232C:PARity?
    - BUS:B<x>:RS232C:POLarity {NORMal|INVERTed}
    - BUS:B<x>:RS232C:POLarity?
    - BUS:B<x>:RS232C:RX:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:RS232C:RX:SOUrce?
    - BUS:B<x>:RS232C:TX:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:RS232C:TX:SOUrce?
    - BUS:B<x>:SPI:BITOrder {LSB|MSB}
    - BUS:B<x>:SPI:BITOrder?
    - BUS:B<x>:SPI:CLOCK:POLARity {FALL|RISe}
    - BUS:B<x>:SPI:CLOCK:POLARity?
    - BUS:B<x>:SPI:CLOCK:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:CLOCK:SOUrce?
    - BUS:B<x>:SPI:DATA:IN:POLARity {LOW|HIGH}
    - BUS:B<x>:SPI:DATA:IN:POLARity?
    - BUS:B<x>:SPI:DATA:IN:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:DATA:IN:SOUrce?
    - BUS:B<x>:SPI:DATA:MISO:POLARity {LOW|HIGH}
    - BUS:B<x>:SPI:DATA:MISO:POLARity?
    - BUS:B<x>:SPI:DATA:MISO:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:DATA:MISO:SOUrce?
    - BUS:B<x>:SPI:DATA:MOSI:POLARity {LOW|HIGH}
    - BUS:B<x>:SPI:DATA:MOSI:POLARity?
    - BUS:B<x>:SPI:DATA:MOSI:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:DATA:MOSI:SOUrce?
    - BUS:B<x>:SPI:DATA:OUT:POLARity {LOW|HIGH}
    - BUS:B<x>:SPI:DATA:OUT:POLARity?
    - BUS:B<x>:SPI:DATA:OUT:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:DATA:OUT:SOUrce?
    - BUS:B<x>:SPI:DATA:SIZe <NR1>
    - BUS:B<x>:SPI:DATA:SIZe?
    - BUS:B<x>:SPI:FRAMING {SS|IDLEtime}
    - BUS:B<x>:SPI:FRAMING?
    - BUS:B<x>:SPI:IDLETime <NR3>
    - BUS:B<x>:SPI:IDLETime?
    - BUS:B<x>:SPI:SCLK:POLARity {FALL|RISe}
    - BUS:B<x>:SPI:SCLK:POLARity?
    - BUS:B<x>:SPI:SCLK:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:SCLK:SOUrce?
    - BUS:B<x>:SPI:SELect:POLARity {LOW|HIGH}
    - BUS:B<x>:SPI:SELect:POLARity?
    - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:SELect:SOUrce?
    - BUS:B<x>:SPI:SS:POLARity {LOW|HIGH}
    - BUS:B<x>:SPI:SS:POLARity?
    - BUS:B<x>:SPI:SS:SOUrce {CH<x>|D<x>}
    - BUS:B<x>:SPI:SS:SOUrce?
    - BUS:B<x>:STATE {ON|OFF|<NR1>}
    - BUS:B<x>:STATE?
    - BUS:B<x>:TYPE {I2C|SPI|CAN|RS232C|PARallel|LIN}
    - BUS:LOWerthreshold:CH<x> {<NR3>|ECL|TTL}
    - BUS:LOWerthreshold:CH<x>?
    - BUS:THReshold:CH<x> {ECL|TTL|<NR3>}
    - BUS:THReshold:CH<x>?
    - BUS:THReshold:D<x> {<NR3>|ECL|TTL}
    - BUS:THReshold:D<x>?
    - BUS:UPPerthreshold:CH<x> {<NR3>|ECL|TTL}
    - BUS:UPPerthreshold:CH<x>?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedChannel,
    ValidatedDigitalBit,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class BusUpperthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:UPPerthreshold:CH<x>`` command.

    Description:
        - Sets the upper threshold for each analog channel (1-4). This applies to all search and
          trigger types that use the channel.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:UPPerthreshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:UPPerthreshold:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - BUS:UPPerthreshold:CH<x> {<NR3>|ECL|TTL}
        - BUS:UPPerthreshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold, in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class BusUpperthreshold(SCPICmdRead):
    """The ``BUS:UPPerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:UPPerthreshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``BUS:UPPerthreshold:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, BusUpperthresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: BusUpperthresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, BusUpperthresholdChannel]:
        """Return the ``BUS:UPPerthreshold:CH<x>`` command.

        Description:
            - Sets the upper threshold for each analog channel (1-4). This applies to all search and
              trigger types that use the channel.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:UPPerthreshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold:CH<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:UPPerthreshold:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - BUS:UPPerthreshold:CH<x> {<NR3>|ECL|TTL}
            - BUS:UPPerthreshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold, in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._ch


class BusThresholdDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:THReshold:D<x>`` command.

    Description:
        - This command specifies the threshold for digital channel <x>, where x is the digital
          channel number (0-15). This will apply to all Search and Trigger Types that use the
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:THReshold:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:THReshold:D<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:THReshold:D<x> value`` command.

    SCPI Syntax:
        ```
        - BUS:THReshold:D<x> {<NR3>|ECL|TTL}
        - BUS:THReshold:D<x>?
        ```

    Info:
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
        - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
    """


class BusThresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:THReshold:CH<x>`` command.

    Description:
        - This command specifies the threshold for analog channel <x>, where x is the channel number
          (1-4). This setting applies to all trigger types that use the channel.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:THReshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:THReshold:CH<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:THReshold:CH<x> value`` command.

    SCPI Syntax:
        ```
        - BUS:THReshold:CH<x> {ECL|TTL|<NR3>}
        - BUS:THReshold:CH<x>?
        ```

    Info:
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a TTL preset high level of 1.4V.
        - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
    """


class BusThreshold(SCPICmdRead):
    """The ``BUS:THReshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:THReshold?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``BUS:THReshold:CH<x>`` command.
        - ``.d``: The ``BUS:THReshold:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, BusThresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: BusThresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._d: Dict[int, BusThresholdDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: BusThresholdDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def ch(self) -> Dict[int, BusThresholdChannel]:
        """Return the ``BUS:THReshold:CH<x>`` command.

        Description:
            - This command specifies the threshold for analog channel <x>, where x is the channel
              number (1-4). This setting applies to all trigger types that use the channel.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:THReshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:THReshold:CH<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:THReshold:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - BUS:THReshold:CH<x> {ECL|TTL|<NR3>}
            - BUS:THReshold:CH<x>?
            ```

        Info:
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a TTL preset high level of 1.4V.
            - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
        """
        return self._ch

    @property
    def d(self) -> Dict[int, BusThresholdDigitalBit]:
        """Return the ``BUS:THReshold:D<x>`` command.

        Description:
            - This command specifies the threshold for digital channel <x>, where x is the digital
              channel number (0-15). This will apply to all Search and Trigger Types that use the
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:THReshold:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:THReshold:D<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:THReshold:D<x> value`` command.

        SCPI Syntax:
            ```
            - BUS:THReshold:D<x> {<NR3>|ECL|TTL}
            - BUS:THReshold:D<x>?
            ```

        Info:
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
            - ``<NR3>`` is a floating point number that specifies the threshold level, in volts.
        """
        return self._d


class BusLowerthresholdChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``BUS:LOWerthreshold:CH<x>`` command.

    Description:
        - This command sets the lower threshold for each channel. This applies to all search and
          trigger types that use the channel.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:LOWerthreshold:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:LOWerthreshold:CH<x> value``
          command.

    SCPI Syntax:
        ```
        - BUS:LOWerthreshold:CH<x> {<NR3>|ECL|TTL}
        - BUS:LOWerthreshold:CH<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the threshold, in volts.
        - ``ECL`` specifies a preset ECL high level of -1.3V.
        - ``TTL`` specifies a preset TTL high level of 1.4V.
    """


class BusLowerthreshold(SCPICmdRead):
    """The ``BUS:LOWerthreshold`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:LOWerthreshold?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``BUS:LOWerthreshold:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, BusLowerthresholdChannel] = DefaultDictPassKeyToFactory(
            lambda x: BusLowerthresholdChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, BusLowerthresholdChannel]:
        """Return the ``BUS:LOWerthreshold:CH<x>`` command.

        Description:
            - This command sets the lower threshold for each channel. This applies to all search and
              trigger types that use the channel.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:LOWerthreshold:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold:CH<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:LOWerthreshold:CH<x> value``
              command.

        SCPI Syntax:
            ```
            - BUS:LOWerthreshold:CH<x> {<NR3>|ECL|TTL}
            - BUS:LOWerthreshold:CH<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the threshold, in volts.
            - ``ECL`` specifies a preset ECL high level of -1.3V.
            - ``TTL`` specifies a preset TTL high level of 1.4V.
        """
        return self._ch


class BusBItemType(SCPICmdWrite):
    """The ``BUS:B<x>:TYPE`` command.

    Description:
        - Sets or returns the bus type for <x>, where x is the bus number.

    Usage:
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:TYPE value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:TYPE {I2C|SPI|CAN|RS232C|PARallel|LIN}
        ```

    Info:
        - ``I2C`` specifies the Inter-IC bus.
        - ``SPI`` specifies the Serial Peripheral Interface bus (not available on two-channel
          models).
        - ``CAN`` specifies the Controller Area Network bus.
        - ``RS232C`` specifies the RS232C bus.
        - ``PARallel`` specifies the parallel bus.
        - ``LIN`` specifies the LIN bus.
    """


class BusBItemState(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:STATE`` command.

    Description:
        - This command specifies the on/off state of the bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:STATE value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:STATE {ON|OFF|<NR1>}
        - BUS:B<x>:STATE?
        ```

    Info:
        - ``ON`` or <NR1> ≠ 0 turns on the bus.
        - ``OFF`` or <NR1> = 0 turns off the bus.
    """


class BusBItemSpiSsSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SS:SOUrce`` command.

    Description:
        - This command specifies the source waveform for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SS:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SS:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:SS:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform.
        - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
    """


class BusBItemSpiSsPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SS:POLARity`` command.

    Description:
        - Sets or returns the SPI SS polarity for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS:POLARity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS:POLARity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SS:POLARity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SS:POLARity {LOW|HIGH}
        - BUS:B<x>:SPI:SS:POLARity?
        ```

    Info:
        - ``LOW`` specifies an active low polarity.
        - ``HIGH`` specifies an active high polarity.
    """


class BusBItemSpiSs(SCPICmdRead):
    """The ``BUS:B<x>:SPI:SS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:SS:POLARity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:SS:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiSsPolarity(device, f"{self._cmd_syntax}:POLARity")
        self._source = BusBItemSpiSsSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiSsPolarity:
        """Return the ``BUS:B<x>:SPI:SS:POLARity`` command.

        Description:
            - Sets or returns the SPI SS polarity for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS:POLARity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS:POLARity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SS:POLARity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SS:POLARity {LOW|HIGH}
            - BUS:B<x>:SPI:SS:POLARity?
            ```

        Info:
            - ``LOW`` specifies an active low polarity.
            - ``HIGH`` specifies an active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiSsSource:
        """Return the ``BUS:B<x>:SPI:SS:SOUrce`` command.

        Description:
            - This command specifies the source waveform for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SS:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SS:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:SS:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform.
            - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
        """
        return self._source


class BusBItemSpiSelectSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect:SOUrce`` command.

    Description:
        - This command specifies the source waveform for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:SELect:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform.
        - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
    """


class BusBItemSpiSelectPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect:POLARity`` command.

    Description:
        - Sets or returns the SPI SS polarity for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:POLARity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:POLARity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:POLARity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SELect:POLARity {LOW|HIGH}
        - BUS:B<x>:SPI:SELect:POLARity?
        ```

    Info:
        - ``LOW`` specifies an active low polarity.
        - ``HIGH`` specifies an active high polarity.
    """


class BusBItemSpiSelect(SCPICmdRead):
    """The ``BUS:B<x>:SPI:SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:SELect:POLARity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:SELect:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiSelectPolarity(device, f"{self._cmd_syntax}:POLARity")
        self._source = BusBItemSpiSelectSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiSelectPolarity:
        """Return the ``BUS:B<x>:SPI:SELect:POLARity`` command.

        Description:
            - Sets or returns the SPI SS polarity for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:POLARity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:POLARity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:SELect:POLARity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SELect:POLARity {LOW|HIGH}
            - BUS:B<x>:SPI:SELect:POLARity?
            ```

        Info:
            - ``LOW`` specifies an active low polarity.
            - ``HIGH`` specifies an active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiSelectSource:
        """Return the ``BUS:B<x>:SPI:SELect:SOUrce`` command.

        Description:
            - This command specifies the source waveform for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SELect:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SELect:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:SELect:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform.
            - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
        """
        return self._source


class BusBItemSpiSclkSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SCLK:SOUrce`` command.

    Description:
        - Sets or returns the SPI SCLK source for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLK:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLK:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SCLK:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SCLK:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:SCLK:SOUrce?
        ```

    Info:
        - ``CH<x>`` is the channel to use as the SPI SCLK source. x has a minimum of 1 and a maximum
          of 4.
        - ``D<x>`` is the digital channel to use as the SPI SCLK source. x has a minimum of 0 and a
          maximum of 15.
    """


class BusBItemSpiSclkPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:SCLK:POLARity`` command.

    Description:
        - Sets or returns the SPI SCLK polarity for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLK:POLARity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLK:POLARity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SCLK:POLARity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:SCLK:POLARity {FALL|RISe}
        - BUS:B<x>:SPI:SCLK:POLARity?
        ```

    Info:
        - ``FALL`` specifies the falling edge.
        - ``RISe`` specifies the rising edge.
    """


class BusBItemSpiSclk(SCPICmdRead):
    """The ``BUS:B<x>:SPI:SCLK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLK?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLK?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:SCLK:POLARity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:SCLK:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiSclkPolarity(device, f"{self._cmd_syntax}:POLARity")
        self._source = BusBItemSpiSclkSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiSclkPolarity:
        """Return the ``BUS:B<x>:SPI:SCLK:POLARity`` command.

        Description:
            - Sets or returns the SPI SCLK polarity for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLK:POLARity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLK:POLARity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SCLK:POLARity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SCLK:POLARity {FALL|RISe}
            - BUS:B<x>:SPI:SCLK:POLARity?
            ```

        Info:
            - ``FALL`` specifies the falling edge.
            - ``RISe`` specifies the rising edge.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiSclkSource:
        """Return the ``BUS:B<x>:SPI:SCLK:SOUrce`` command.

        Description:
            - Sets or returns the SPI SCLK source for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLK:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLK:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:SCLK:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:SCLK:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:SCLK:SOUrce?
            ```

        Info:
            - ``CH<x>`` is the channel to use as the SPI SCLK source. x has a minimum of 1 and a
              maximum of 4.
            - ``D<x>`` is the digital channel to use as the SPI SCLK source. x has a minimum of 0
              and a maximum of 15.
        """
        return self._source


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
        - This command specifies the type of framing to use for the SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:FRAMING value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:FRAMING {SS|IDLEtime}
        - BUS:B<x>:SPI:FRAMING?
        ```
    """


class BusBItemSpiDataSize(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:SIZe`` command.

    Description:
        - Sets or returns the number of bits per word for the specified SPI bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:SIZe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATA:SIZe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATA:SIZe <NR1>
        - BUS:B<x>:SPI:DATA:SIZe?
        ```

    Info:
        - ``<NR1>`` specifies the number of bits per word.
    """


class BusBItemSpiDataOutSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:OUT:SOUrce`` command.

    Description:
        - Sets or returns the SPI MOSI source for bus <x, where x is the bus number>.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:OUT:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:OUT:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATA:OUT:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATA:OUT:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:DATA:OUT:SOUrce?
        ```

    Info:
        - ``CH<x>`` is the channel to use as the SPI MISO source. x has a minimum of 1 and a maximum
          of 4.
        - ``D<x>`` is the digital channel to use as the SPI MISO source. x has a minimum of 0 and a
          maximum of 15.
    """


class BusBItemSpiDataOutPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:OUT:POLARity`` command.

    Description:
        - Sets or returns the SPI MOSI polarity for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:OUT:POLARity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:OUT:POLARity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATA:OUT:POLARity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATA:OUT:POLARity {LOW|HIGH}
        - BUS:B<x>:SPI:DATA:OUT:POLARity?
        ```

    Info:
        - ``LOW`` specifies the active low polarity.
        - ``HIGH`` specifies the active high polarity.
    """


class BusBItemSpiDataOut(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:OUT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:OUT?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:OUT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:DATA:OUT:POLARity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:DATA:OUT:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiDataOutPolarity(device, f"{self._cmd_syntax}:POLARity")
        self._source = BusBItemSpiDataOutSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiDataOutPolarity:
        """Return the ``BUS:B<x>:SPI:DATA:OUT:POLARity`` command.

        Description:
            - Sets or returns the SPI MOSI polarity for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:OUT:POLARity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:OUT:POLARity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATA:OUT:POLARity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATA:OUT:POLARity {LOW|HIGH}
            - BUS:B<x>:SPI:DATA:OUT:POLARity?
            ```

        Info:
            - ``LOW`` specifies the active low polarity.
            - ``HIGH`` specifies the active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiDataOutSource:
        """Return the ``BUS:B<x>:SPI:DATA:OUT:SOUrce`` command.

        Description:
            - Sets or returns the SPI MOSI source for bus <x, where x is the bus number>.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:OUT:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:OUT:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATA:OUT:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATA:OUT:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:DATA:OUT:SOUrce?
            ```

        Info:
            - ``CH<x>`` is the channel to use as the SPI MISO source. x has a minimum of 1 and a
              maximum of 4.
            - ``D<x>`` is the digital channel to use as the SPI MISO source. x has a minimum of 0
              and a maximum of 15.
        """
        return self._source


class BusBItemSpiDataMosiSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:MOSI:SOUrce`` command.

    Description:
        - Sets or returns the SPI MOSI source for bus <x, where x is the bus number>.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MOSI:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MOSI:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATA:MOSI:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATA:MOSI:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:DATA:MOSI:SOUrce?
        ```

    Info:
        - ``CH<x>`` is the channel to use as the SPI MISO source. x has a minimum of 1 and a maximum
          of 4.
        - ``D<x>`` is the digital channel to use as the SPI MISO source. x has a minimum of 0 and a
          maximum of 15.
    """


class BusBItemSpiDataMosiPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:MOSI:POLARity`` command.

    Description:
        - Sets or returns the SPI MOSI polarity for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MOSI:POLARity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MOSI:POLARity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATA:MOSI:POLARity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATA:MOSI:POLARity {LOW|HIGH}
        - BUS:B<x>:SPI:DATA:MOSI:POLARity?
        ```

    Info:
        - ``LOW`` specifies the active low polarity.
        - ``HIGH`` specifies the active high polarity.
    """


class BusBItemSpiDataMosi(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:MOSI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MOSI?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MOSI?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:DATA:MOSI:POLARity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:DATA:MOSI:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiDataMosiPolarity(device, f"{self._cmd_syntax}:POLARity")
        self._source = BusBItemSpiDataMosiSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiDataMosiPolarity:
        """Return the ``BUS:B<x>:SPI:DATA:MOSI:POLARity`` command.

        Description:
            - Sets or returns the SPI MOSI polarity for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MOSI:POLARity?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MOSI:POLARity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATA:MOSI:POLARity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATA:MOSI:POLARity {LOW|HIGH}
            - BUS:B<x>:SPI:DATA:MOSI:POLARity?
            ```

        Info:
            - ``LOW`` specifies the active low polarity.
            - ``HIGH`` specifies the active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiDataMosiSource:
        """Return the ``BUS:B<x>:SPI:DATA:MOSI:SOUrce`` command.

        Description:
            - Sets or returns the SPI MOSI source for bus <x, where x is the bus number>.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MOSI:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MOSI:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATA:MOSI:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATA:MOSI:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:DATA:MOSI:SOUrce?
            ```

        Info:
            - ``CH<x>`` is the channel to use as the SPI MISO source. x has a minimum of 1 and a
              maximum of 4.
            - ``D<x>`` is the digital channel to use as the SPI MISO source. x has a minimum of 0
              and a maximum of 15.
        """
        return self._source


class BusBItemSpiDataMisoSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:MISO:SOUrce`` command.

    Description:
        - Sets or returns the SPI MISO source for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MISO:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MISO:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATA:MISO:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATA:MISO:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:DATA:MISO:SOUrce?
        ```

    Info:
        - ``CH<x>`` is the channel to use as the SPI MISO source. x has a minimum of 1 and a maximum
          of 4.
        - ``D<x>`` is the digital channel to use as the SPI MISO source. x has a minimum of 0 and a
          maximum of 15.
    """


class BusBItemSpiDataMisoPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:MISO:POLARity`` command.

    Description:
        - Sets or returns the SPI MISO polarity for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MISO:POLARity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MISO:POLARity?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATA:MISO:POLARity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATA:MISO:POLARity {LOW|HIGH}
        - BUS:B<x>:SPI:DATA:MISO:POLARity?
        ```

    Info:
        - ``LOW`` specifies an active low polarity.
        - ``HIGH`` specifies an active high polarity.
    """


class BusBItemSpiDataMiso(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:MISO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MISO?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MISO?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:DATA:MISO:POLARity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:DATA:MISO:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiDataMisoPolarity(device, f"{self._cmd_syntax}:POLARity")
        self._source = BusBItemSpiDataMisoSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiDataMisoPolarity:
        """Return the ``BUS:B<x>:SPI:DATA:MISO:POLARity`` command.

        Description:
            - Sets or returns the SPI MISO polarity for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MISO:POLARity?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MISO:POLARity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATA:MISO:POLARity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATA:MISO:POLARity {LOW|HIGH}
            - BUS:B<x>:SPI:DATA:MISO:POLARity?
            ```

        Info:
            - ``LOW`` specifies an active low polarity.
            - ``HIGH`` specifies an active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiDataMisoSource:
        """Return the ``BUS:B<x>:SPI:DATA:MISO:SOUrce`` command.

        Description:
            - Sets or returns the SPI MISO source for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MISO:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MISO:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATA:MISO:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATA:MISO:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:DATA:MISO:SOUrce?
            ```

        Info:
            - ``CH<x>`` is the channel to use as the SPI MISO source. x has a minimum of 1 and a
              maximum of 4.
            - ``D<x>`` is the digital channel to use as the SPI MISO source. x has a minimum of 0
              and a maximum of 15.
        """
        return self._source


class BusBItemSpiDataInSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:IN:SOUrce`` command.

    Description:
        - Sets or returns the SPI MISO source for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:IN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:IN:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATA:IN:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATA:IN:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:DATA:IN:SOUrce?
        ```

    Info:
        - ``CH<x>`` is the channel to use as the SPI MISO source. x has a minimum of 1 and a maximum
          of 4.
        - ``D<x>`` is the digital channel to use as the SPI MISO source. x has a minimum of 0 and a
          maximum of 15.
    """


class BusBItemSpiDataInPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:IN:POLARity`` command.

    Description:
        - Sets or returns the SPI MISO polarity for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:IN:POLARity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:IN:POLARity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATA:IN:POLARity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:DATA:IN:POLARity {LOW|HIGH}
        - BUS:B<x>:SPI:DATA:IN:POLARity?
        ```

    Info:
        - ``LOW`` specifies an active low polarity.
        - ``HIGH`` specifies an active high polarity.
    """


class BusBItemSpiDataIn(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA:IN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:IN?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:IN?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:DATA:IN:POLARity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:DATA:IN:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiDataInPolarity(device, f"{self._cmd_syntax}:POLARity")
        self._source = BusBItemSpiDataInSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiDataInPolarity:
        """Return the ``BUS:B<x>:SPI:DATA:IN:POLARity`` command.

        Description:
            - Sets or returns the SPI MISO polarity for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:IN:POLARity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:IN:POLARity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:SPI:DATA:IN:POLARity value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATA:IN:POLARity {LOW|HIGH}
            - BUS:B<x>:SPI:DATA:IN:POLARity?
            ```

        Info:
            - ``LOW`` specifies an active low polarity.
            - ``HIGH`` specifies an active high polarity.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiDataInSource:
        """Return the ``BUS:B<x>:SPI:DATA:IN:SOUrce`` command.

        Description:
            - Sets or returns the SPI MISO source for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:IN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:IN:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATA:IN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATA:IN:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:DATA:IN:SOUrce?
            ```

        Info:
            - ``CH<x>`` is the channel to use as the SPI MISO source. x has a minimum of 1 and a
              maximum of 4.
            - ``D<x>`` is the digital channel to use as the SPI MISO source. x has a minimum of 0
              and a maximum of 15.
        """
        return self._source


class BusBItemSpiData(SCPICmdRead):
    """The ``BUS:B<x>:SPI:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.size``: The ``BUS:B<x>:SPI:DATA:SIZe`` command.
        - ``.in``: The ``BUS:B<x>:SPI:DATA:IN`` command tree.
        - ``.miso``: The ``BUS:B<x>:SPI:DATA:MISO`` command tree.
        - ``.out``: The ``BUS:B<x>:SPI:DATA:OUT`` command tree.
        - ``.mosi``: The ``BUS:B<x>:SPI:DATA:MOSI`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._size = BusBItemSpiDataSize(device, f"{self._cmd_syntax}:SIZe")
        self._in = BusBItemSpiDataIn(device, f"{self._cmd_syntax}:IN")
        self._miso = BusBItemSpiDataMiso(device, f"{self._cmd_syntax}:MISO")
        self._out = BusBItemSpiDataOut(device, f"{self._cmd_syntax}:OUT")
        self._mosi = BusBItemSpiDataMosi(device, f"{self._cmd_syntax}:MOSI")

    @property
    def size(self) -> BusBItemSpiDataSize:
        """Return the ``BUS:B<x>:SPI:DATA:SIZe`` command.

        Description:
            - Sets or returns the number of bits per word for the specified SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:SIZe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:DATA:SIZe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:DATA:SIZe <NR1>
            - BUS:B<x>:SPI:DATA:SIZe?
            ```

        Info:
            - ``<NR1>`` specifies the number of bits per word.
        """
        return self._size

    @property
    def in_(self) -> BusBItemSpiDataIn:
        """Return the ``BUS:B<x>:SPI:DATA:IN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:IN?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:IN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:DATA:IN:POLARity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:DATA:IN:SOUrce`` command.
        """
        return self._in

    @property
    def miso(self) -> BusBItemSpiDataMiso:
        """Return the ``BUS:B<x>:SPI:DATA:MISO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MISO?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MISO?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:DATA:MISO:POLARity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:DATA:MISO:SOUrce`` command.
        """
        return self._miso

    @property
    def out(self) -> BusBItemSpiDataOut:
        """Return the ``BUS:B<x>:SPI:DATA:OUT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:OUT?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:OUT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:DATA:OUT:POLARity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:DATA:OUT:SOUrce`` command.
        """
        return self._out

    @property
    def mosi(self) -> BusBItemSpiDataMosi:
        """Return the ``BUS:B<x>:SPI:DATA:MOSI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA:MOSI?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA:MOSI?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:DATA:MOSI:POLARity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:DATA:MOSI:SOUrce`` command.
        """
        return self._mosi


class BusBItemSpiClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCK:SOUrce`` command.

    Description:
        - Sets or returns the SPI SCLK source for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCK:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCK:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCK:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:CLOCK:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:SPI:CLOCK:SOUrce?
        ```

    Info:
        - ``CH<x>`` is the channel to use as the SPI SCLK source. x has a minimum of 1 and a maximum
          of 4.
        - ``D<x>`` is the digital channel to use as the SPI SCLK source. x has a minimum of 0 and a
          maximum of 15.
    """


class BusBItemSpiClockPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCK:POLARity`` command.

    Description:
        - Sets or returns the SPI SCLK polarity for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCK:POLARity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCK:POLARity?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCK:POLARity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:SPI:CLOCK:POLARity {FALL|RISe}
        - BUS:B<x>:SPI:CLOCK:POLARity?
        ```

    Info:
        - ``FALL`` specifies the falling edge.
        - ``RISe`` specifies the rising edge.
    """


class BusBItemSpiClock(SCPICmdRead):
    """The ``BUS:B<x>:SPI:CLOCK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCK?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCK?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.polarity``: The ``BUS:B<x>:SPI:CLOCK:POLARity`` command.
        - ``.source``: The ``BUS:B<x>:SPI:CLOCK:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._polarity = BusBItemSpiClockPolarity(device, f"{self._cmd_syntax}:POLARity")
        self._source = BusBItemSpiClockSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def polarity(self) -> BusBItemSpiClockPolarity:
        """Return the ``BUS:B<x>:SPI:CLOCK:POLARity`` command.

        Description:
            - Sets or returns the SPI SCLK polarity for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCK:POLARity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCK:POLARity?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCK:POLARity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:CLOCK:POLARity {FALL|RISe}
            - BUS:B<x>:SPI:CLOCK:POLARity?
            ```

        Info:
            - ``FALL`` specifies the falling edge.
            - ``RISe`` specifies the rising edge.
        """
        return self._polarity

    @property
    def source(self) -> BusBItemSpiClockSource:
        """Return the ``BUS:B<x>:SPI:CLOCK:SOUrce`` command.

        Description:
            - Sets or returns the SPI SCLK source for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCK:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCK:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:CLOCK:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:CLOCK:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:SPI:CLOCK:SOUrce?
            ```

        Info:
            - ``CH<x>`` is the channel to use as the SPI SCLK source. x has a minimum of 1 and a
              maximum of 4.
            - ``D<x>`` is the digital channel to use as the SPI SCLK source. x has a minimum of 0
              and a maximum of 15.
        """
        return self._source


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
        - ``.data``: The ``BUS:B<x>:SPI:DATA`` command tree.
        - ``.framing``: The ``BUS:B<x>:SPI:FRAMING`` command.
        - ``.idletime``: The ``BUS:B<x>:SPI:IDLETime`` command.
        - ``.clock``: The ``BUS:B<x>:SPI:CLOCK`` command tree.
        - ``.sclk``: The ``BUS:B<x>:SPI:SCLK`` command tree.
        - ``.select``: The ``BUS:B<x>:SPI:SELect`` command tree.
        - ``.ss``: The ``BUS:B<x>:SPI:SS`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitorder = BusBItemSpiBitorder(device, f"{self._cmd_syntax}:BITOrder")
        self._data = BusBItemSpiData(device, f"{self._cmd_syntax}:DATA")
        self._framing = BusBItemSpiFraming(device, f"{self._cmd_syntax}:FRAMING")
        self._idletime = BusBItemSpiIdletime(device, f"{self._cmd_syntax}:IDLETime")
        self._clock = BusBItemSpiClock(device, f"{self._cmd_syntax}:CLOCK")
        self._sclk = BusBItemSpiSclk(device, f"{self._cmd_syntax}:SCLK")
        self._select = BusBItemSpiSelect(device, f"{self._cmd_syntax}:SELect")
        self._ss = BusBItemSpiSs(device, f"{self._cmd_syntax}:SS")

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
    def data(self) -> BusBItemSpiData:
        """Return the ``BUS:B<x>:SPI:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.size``: The ``BUS:B<x>:SPI:DATA:SIZe`` command.
            - ``.in``: The ``BUS:B<x>:SPI:DATA:IN`` command tree.
            - ``.miso``: The ``BUS:B<x>:SPI:DATA:MISO`` command tree.
            - ``.out``: The ``BUS:B<x>:SPI:DATA:OUT`` command tree.
            - ``.mosi``: The ``BUS:B<x>:SPI:DATA:MOSI`` command tree.
        """
        return self._data

    @property
    def framing(self) -> BusBItemSpiFraming:
        """Return the ``BUS:B<x>:SPI:FRAMING`` command.

        Description:
            - This command specifies the type of framing to use for the SPI bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:FRAMING?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:SPI:FRAMING value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:SPI:FRAMING {SS|IDLEtime}
            - BUS:B<x>:SPI:FRAMING?
            ```
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
    def clock(self) -> BusBItemSpiClock:
        """Return the ``BUS:B<x>:SPI:CLOCK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:CLOCK?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:CLOCK?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:CLOCK:POLARity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:CLOCK:SOUrce`` command.
        """
        return self._clock

    @property
    def sclk(self) -> BusBItemSpiSclk:
        """Return the ``BUS:B<x>:SPI:SCLK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SCLK?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SCLK?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:SCLK:POLARity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:SCLK:SOUrce`` command.
        """
        return self._sclk

    @property
    def select(self) -> BusBItemSpiSelect:
        """Return the ``BUS:B<x>:SPI:SELect`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SELect?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SELect?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:SELect:POLARity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:SELect:SOUrce`` command.
        """
        return self._select

    @property
    def ss(self) -> BusBItemSpiSs:
        """Return the ``BUS:B<x>:SPI:SS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:SPI:SS?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:SPI:SS?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.polarity``: The ``BUS:B<x>:SPI:SS:POLARity`` command.
            - ``.source``: The ``BUS:B<x>:SPI:SS:SOUrce`` command.
        """
        return self._ss


class BusBItemRs232cTxSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:TX:SOUrce`` command.

    Description:
        - Sets or returns the RS232 TX Source for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:TX:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:RS232C:TX:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the channel to use as the RS232 TX source. x has a minimum of 1 and a
          maximum of 4.
        - ``D<x>`` specifies the digital channel to use as the RS232 TX source. x has a minimum of 0
          and a maximum of 15.
    """


class BusBItemRs232cTx(SCPICmdRead):
    """The ``BUS:B<x>:RS232C:TX`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:TX?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:TX?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:RS232C:TX:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemRs232cTxSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemRs232cTxSource:
        """Return the ``BUS:B<x>:RS232C:TX:SOUrce`` command.

        Description:
            - Sets or returns the RS232 TX Source for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:TX:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:TX:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:RS232C:TX:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the channel to use as the RS232 TX source. x has a minimum of 1
              and a maximum of 4.
            - ``D<x>`` specifies the digital channel to use as the RS232 TX source. x has a minimum
              of 0 and a maximum of 15.
        """
        return self._source


class BusBItemRs232cRxSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:RX:SOUrce`` command.

    Description:
        - Sets or returns the RS232 RX source for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:RX:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:RS232C:RX:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the channel to use for the RS232 RX source. x has a minimum of 1 and a
          maximum of 4.
        - ``D<x>`` specifies the digital channel to use for the RS232 RX source. x has a minimum of
          0 and a maximum of 15.
    """


class BusBItemRs232cRx(SCPICmdRead):
    """The ``BUS:B<x>:RS232C:RX`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:RX?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:RX?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:RS232C:RX:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemRs232cRxSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemRs232cRxSource:
        """Return the ``BUS:B<x>:RS232C:RX:SOUrce`` command.

        Description:
            - Sets or returns the RS232 RX source for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:RX:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:RX:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:RS232C:RX:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the channel to use for the RS232 RX source. x has a minimum of 1
              and a maximum of 4.
            - ``D<x>`` specifies the digital channel to use for the RS232 RX source. x has a minimum
              of 0 and a maximum of 15.
        """
        return self._source


class BusBItemRs232cPolarity(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:POLarity`` command.

    Description:
        - This command specifies the polarity for the RS-232C bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:POLarity value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:POLarity {NORMal|INVERTed}
        - BUS:B<x>:RS232C:POLarity?
        ```

    Info:
        - ``NORMal`` sets the polarity to positive.
        - ``INVERTed`` sets the polarity to negative.
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
        - This command specifies the display mode for the RS-232 bus (frame or packet).

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DISplaymode {FRAme|PACKET}
        - BUS:B<x>:RS232C:DISplaymode?
        ```

    Info:
        - ``FRAme`` displays each frame as a single entity.
        - ``PACKET`` displays a group of frames terminated with a single frame defined by the
          ``BUS:B<x>:RS232C:DELImiter`` command or the front panel.
    """


class BusBItemRs232cDelimiter(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:DELIMiter`` command.

    Description:
        - This command specifies the delimiting value for a packet on the RS-232 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:DELIMiter {NULl|LF|CR|SPace|XFF}
        - BUS:B<x>:RS232C:DELIMiter?
        ```

    Info:
        - ``NULl`` specifies 0x00.
        - ``LF`` specifies 0x0A.
        - ``CR`` specifies 0x0D.
        - ``XFF`` specifies 0xFF.
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
        - BUS:B<x>:RS232C:DATABits {7|8|9}
        - BUS:B<x>:RS232C:DATABits?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``7`` specifies the number of bits as 7 in the RS-232C data frame.
        - ``8`` specifies the number of bits as 8 in the RS-232C data frame.
        - ``9`` specifies the number of bits as 9 in the RS-232C data frame.
    """


class BusBItemRs232cBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:RS232C:BITRate`` command.

    Description:
        - This command specifies the bit rate for the RS-232 bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:RS232C:BITRate <NR1>
        - BUS:B<x>:RS232C:BITRate?
        ```

    Info:
        - ``<NR1>`` is the bit rate in bits-per-second. You can enter any positive integer, and the
          instrument will coerce the value to the closest supported bit rate.
    """


#  pylint: disable=too-many-instance-attributes
class BusBItemRs232c(SCPICmdRead):
    """The ``BUS:B<x>:RS232C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:RS232C:BITRate`` command.
        - ``.databits``: The ``BUS:B<x>:RS232C:DATABits`` command.
        - ``.delimiter``: The ``BUS:B<x>:RS232C:DELIMiter`` command.
        - ``.displaymode``: The ``BUS:B<x>:RS232C:DISplaymode`` command.
        - ``.parity``: The ``BUS:B<x>:RS232C:PARity`` command.
        - ``.polarity``: The ``BUS:B<x>:RS232C:POLarity`` command.
        - ``.rx``: The ``BUS:B<x>:RS232C:RX`` command tree.
        - ``.tx``: The ``BUS:B<x>:RS232C:TX`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemRs232cBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._databits = BusBItemRs232cDatabits(device, f"{self._cmd_syntax}:DATABits")
        self._delimiter = BusBItemRs232cDelimiter(device, f"{self._cmd_syntax}:DELIMiter")
        self._displaymode = BusBItemRs232cDisplaymode(device, f"{self._cmd_syntax}:DISplaymode")
        self._parity = BusBItemRs232cParity(device, f"{self._cmd_syntax}:PARity")
        self._polarity = BusBItemRs232cPolarity(device, f"{self._cmd_syntax}:POLarity")
        self._rx = BusBItemRs232cRx(device, f"{self._cmd_syntax}:RX")
        self._tx = BusBItemRs232cTx(device, f"{self._cmd_syntax}:TX")

    @property
    def bitrate(self) -> BusBItemRs232cBitrate:
        """Return the ``BUS:B<x>:RS232C:BITRate`` command.

        Description:
            - This command specifies the bit rate for the RS-232 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:BITRate <NR1>
            - BUS:B<x>:RS232C:BITRate?
            ```

        Info:
            - ``<NR1>`` is the bit rate in bits-per-second. You can enter any positive integer, and
              the instrument will coerce the value to the closest supported bit rate.
        """
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
            - BUS:B<x>:RS232C:DATABits {7|8|9}
            - BUS:B<x>:RS232C:DATABits?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``7`` specifies the number of bits as 7 in the RS-232C data frame.
            - ``8`` specifies the number of bits as 8 in the RS-232C data frame.
            - ``9`` specifies the number of bits as 9 in the RS-232C data frame.
        """
        return self._databits

    @property
    def delimiter(self) -> BusBItemRs232cDelimiter:
        """Return the ``BUS:B<x>:RS232C:DELIMiter`` command.

        Description:
            - This command specifies the delimiting value for a packet on the RS-232 bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DELIMiter value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DELIMiter {NULl|LF|CR|SPace|XFF}
            - BUS:B<x>:RS232C:DELIMiter?
            ```

        Info:
            - ``NULl`` specifies 0x00.
            - ``LF`` specifies 0x0A.
            - ``CR`` specifies 0x0D.
            - ``XFF`` specifies 0xFF.
        """
        return self._delimiter

    @property
    def displaymode(self) -> BusBItemRs232cDisplaymode:
        """Return the ``BUS:B<x>:RS232C:DISplaymode`` command.

        Description:
            - This command specifies the display mode for the RS-232 bus (frame or packet).

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:DISplaymode?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:DISplaymode value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:DISplaymode {FRAme|PACKET}
            - BUS:B<x>:RS232C:DISplaymode?
            ```

        Info:
            - ``FRAme`` displays each frame as a single entity.
            - ``PACKET`` displays a group of frames terminated with a single frame defined by the
              ``BUS:B<x>:RS232C:DELImiter`` command or the front panel.
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
            - This command specifies the polarity for the RS-232C bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:POLarity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:RS232C:POLarity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:RS232C:POLarity {NORMal|INVERTed}
            - BUS:B<x>:RS232C:POLarity?
            ```

        Info:
            - ``NORMal`` sets the polarity to positive.
            - ``INVERTed`` sets the polarity to negative.
        """
        return self._polarity

    @property
    def rx(self) -> BusBItemRs232cRx:
        """Return the ``BUS:B<x>:RS232C:RX`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:RX?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:RX?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:RS232C:RX:SOUrce`` command.
        """
        return self._rx

    @property
    def tx(self) -> BusBItemRs232cTx:
        """Return the ``BUS:B<x>:RS232C:TX`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C:TX?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C:TX?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:RS232C:TX:SOUrce`` command.
        """
        return self._tx


class BusBItemPosition(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:POSition`` command.

    Description:
        - This command specifies the position of the bus waveform on the display.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:POSition?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:POSition value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:POSition <NR3>
        - BUS:B<x>:POSition?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the position of the bus <x> waveform
          on the display.
    """


class BusBItemParallelWidth(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:WIDth`` command.

    Description:
        - This command specifies the number of bits to use for the width of the parallel bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:WIDth?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:WIDth value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:WIDth <NR1>
        - BUS:B<x>:PARallel:WIDth?
        ```

    Info:
        - ``<NR1>`` is the number of bits.
    """


class BusBItemParallelClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCK:SOUrce`` command.

    Description:
        - Sets or returns the parallel bus source <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCK:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCK:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:CLOCK:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCK:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:PARallel:CLOCK:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the channel to use as the parallel bit source. x has a minimum of 1
          and a maximum of 4.
        - ``D<x>`` specifies the digital channel to use as the parallel bit source. x has a minimum
          of 0 and a maximum of 15.
    """


class BusBItemParallelClockIsclocked(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCK:ISCLOCKed`` command.

    Description:
        - Sets or returns the parallel bus clock function for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCK:ISCLOCKed?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCK:ISCLOCKed?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``BUS:B<x>:PARallel:CLOCK:ISCLOCKed value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCK:ISCLOCKed {YES|NO}
        - BUS:B<x>:PARallel:CLOCK:ISCLOCKed?
        ```

    Info:
        - ``YES`` specifies that the parallel bus is clocked.
        - ``NO`` specifies that the parallel bus is not clocked.
    """


class BusBItemParallelClockEdge(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCK:EDGE`` command.

    Description:
        - Sets or returns the parallel clock edge for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCK:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCK:EDGE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:CLOCK:EDGE value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:CLOCK:EDGE {EITher|RISing|FALling}
        - BUS:B<x>:PARallel:CLOCK:EDGE?
        ```

    Info:
        - ``EIther`` specifies either rising or falling edge as the clock edge.
        - ``RISing`` specifies the rising edge as the clock edge.
        - ``FALling`` specifies the falling edge as the clock edge.
    """


class BusBItemParallelClock(SCPICmdRead):
    """The ``BUS:B<x>:PARallel:CLOCK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCK?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCK?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``BUS:B<x>:PARallel:CLOCK:EDGE`` command.
        - ``.isclocked``: The ``BUS:B<x>:PARallel:CLOCK:ISCLOCKed`` command.
        - ``.source``: The ``BUS:B<x>:PARallel:CLOCK:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = BusBItemParallelClockEdge(device, f"{self._cmd_syntax}:EDGE")
        self._isclocked = BusBItemParallelClockIsclocked(device, f"{self._cmd_syntax}:ISCLOCKed")
        self._source = BusBItemParallelClockSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def edge(self) -> BusBItemParallelClockEdge:
        """Return the ``BUS:B<x>:PARallel:CLOCK:EDGE`` command.

        Description:
            - Sets or returns the parallel clock edge for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCK:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCK:EDGE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCK:EDGE value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCK:EDGE {EITher|RISing|FALling}
            - BUS:B<x>:PARallel:CLOCK:EDGE?
            ```

        Info:
            - ``EIther`` specifies either rising or falling edge as the clock edge.
            - ``RISing`` specifies the rising edge as the clock edge.
            - ``FALling`` specifies the falling edge as the clock edge.
        """
        return self._edge

    @property
    def isclocked(self) -> BusBItemParallelClockIsclocked:
        """Return the ``BUS:B<x>:PARallel:CLOCK:ISCLOCKed`` command.

        Description:
            - Sets or returns the parallel bus clock function for bus <x>, where x is the bus
              number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCK:ISCLOCKed?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCK:ISCLOCKed?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCK:ISCLOCKed value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCK:ISCLOCKed {YES|NO}
            - BUS:B<x>:PARallel:CLOCK:ISCLOCKed?
            ```

        Info:
            - ``YES`` specifies that the parallel bus is clocked.
            - ``NO`` specifies that the parallel bus is not clocked.
        """
        return self._isclocked

    @property
    def source(self) -> BusBItemParallelClockSource:
        """Return the ``BUS:B<x>:PARallel:CLOCK:SOUrce`` command.

        Description:
            - Sets or returns the parallel bus source <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCK:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCK:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:CLOCK:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:CLOCK:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:PARallel:CLOCK:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the channel to use as the parallel bit source. x has a minimum of
              1 and a maximum of 4.
            - ``D<x>`` specifies the digital channel to use as the parallel bit source. x has a
              minimum of 0 and a maximum of 15.
        """
        return self._source


class BusBItemParallelBitItemSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:BIT<x>:SOUrce`` command.

    Description:
        - Specifies the bit source waveform for the parallel bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:BIT<x>:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:PARallel:BIT<x>:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:PARallel:BIT<x>:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the bit source waveform.
        - ``D<x>`` specifies a digital channel as the bit source waveform. (Requires option 3-MSO.).
    """


class BusBItemParallelBitItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:B<x>:PARallel:BIT<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:BIT<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:PARallel:BIT<x>:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemParallelBitItemSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemParallelBitItemSource:
        """Return the ``BUS:B<x>:PARallel:BIT<x>:SOUrce`` command.

        Description:
            - Specifies the bit source waveform for the parallel bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:BIT<x>:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:PARallel:BIT<x>:SOUrce value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:BIT<x>:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:PARallel:BIT<x>:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the bit source waveform.
            - ``D<x>`` specifies a digital channel as the bit source waveform. (Requires option
              3-MSO.).
        """
        return self._source


class BusBItemParallel(SCPICmdRead):
    """The ``BUS:B<x>:PARallel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bit``: The ``BUS:B<x>:PARallel:BIT<x>`` command tree.
        - ``.clock``: The ``BUS:B<x>:PARallel:CLOCK`` command tree.
        - ``.width``: The ``BUS:B<x>:PARallel:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bit: Dict[int, BusBItemParallelBitItem] = DefaultDictPassKeyToFactory(
            lambda x: BusBItemParallelBitItem(device, f"{self._cmd_syntax}:BIT{x}")
        )
        self._clock = BusBItemParallelClock(device, f"{self._cmd_syntax}:CLOCK")
        self._width = BusBItemParallelWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def bit(self) -> Dict[int, BusBItemParallelBitItem]:
        """Return the ``BUS:B<x>:PARallel:BIT<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:BIT<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:BIT<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:PARallel:BIT<x>:SOUrce`` command.
        """
        return self._bit

    @property
    def clock(self) -> BusBItemParallelClock:
        """Return the ``BUS:B<x>:PARallel:CLOCK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:CLOCK?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:CLOCK?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.edge``: The ``BUS:B<x>:PARallel:CLOCK:EDGE`` command.
            - ``.isclocked``: The ``BUS:B<x>:PARallel:CLOCK:ISCLOCKed`` command.
            - ``.source``: The ``BUS:B<x>:PARallel:CLOCK:SOUrce`` command.
        """
        return self._clock

    @property
    def width(self) -> BusBItemParallelWidth:
        """Return the ``BUS:B<x>:PARallel:WIDth`` command.

        Description:
            - This command specifies the number of bits to use for the width of the parallel bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:PARallel:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:PARallel:WIDth?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:PARallel:WIDth value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:PARallel:WIDth <NR1>
            - BUS:B<x>:PARallel:WIDth?
            ```

        Info:
            - ``<NR1>`` is the number of bits.
        """
        return self._width


class BusBItemLinStandard(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:STANDard`` command.

    Description:
        - Specifies the LIN bus standard to use.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:STANDard?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:STANDard?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:STANDard value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:STANDard {V1X|V2X|MIXed}
        - BUS:B<x>:LIN:STANDard?
        ```

    Info:
        - ``V1X`` sets the LIN bus standard to V1X.
        - ``V2X`` sets the LIN bus standard to V2X.
        - ``MIXed`` sets the LIN bus standard to MIXED.
    """


class BusBItemLinSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:SOUrce`` command.

    Description:
        - Specifies the source waveform for the LIN bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:LIN:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform.
        - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
    """


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
    """The ``BUS:B<x>:LIN:POLARity`` command.

    Description:
        - Sets or returns the LIN polarity.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:POLARity?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:POLARity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:POLARity value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:POLARity {NORMal|INVerted}
        - BUS:B<x>:LIN:POLARity?
        ```

    Info:
        - ``NORMal`` specifies normal LIN polarity.
        - ``INVerted`` specifies inverted LIN polarity.
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


class BusBItemLinBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LIN:BITRate`` command.

    Description:
        - Specifies the bit rate for the LIN bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LIN:BITRate <NR1>
        - BUS:B<x>:LIN:BITRate?
        ```

    Info:
        - ``<NR1>`` is the LIN bus bit rate. You can enter any positive integer, and the instrument
          will coerce the value to the closest supported bit rate.
    """


class BusBItemLin(SCPICmdRead):
    """The ``BUS:B<x>:LIN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LIN?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:LIN:BITRate`` command.
        - ``.idformat``: The ``BUS:B<x>:LIN:IDFORmat`` command.
        - ``.polarity``: The ``BUS:B<x>:LIN:POLARity`` command.
        - ``.samplepoint``: The ``BUS:B<x>:LIN:SAMPLEpoint`` command.
        - ``.source``: The ``BUS:B<x>:LIN:SOUrce`` command.
        - ``.standard``: The ``BUS:B<x>:LIN:STANDard`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemLinBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._idformat = BusBItemLinIdformat(device, f"{self._cmd_syntax}:IDFORmat")
        self._polarity = BusBItemLinPolarity(device, f"{self._cmd_syntax}:POLARity")
        self._samplepoint = BusBItemLinSamplepoint(device, f"{self._cmd_syntax}:SAMPLEpoint")
        self._source = BusBItemLinSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = BusBItemLinStandard(device, f"{self._cmd_syntax}:STANDard")

    @property
    def bitrate(self) -> BusBItemLinBitrate:
        """Return the ``BUS:B<x>:LIN:BITRate`` command.

        Description:
            - Specifies the bit rate for the LIN bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:BITRate <NR1>
            - BUS:B<x>:LIN:BITRate?
            ```

        Info:
            - ``<NR1>`` is the LIN bus bit rate. You can enter any positive integer, and the
              instrument will coerce the value to the closest supported bit rate.
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
        """Return the ``BUS:B<x>:LIN:POLARity`` command.

        Description:
            - Sets or returns the LIN polarity.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:POLARity?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:POLARity?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:POLARity value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:POLARity {NORMal|INVerted}
            - BUS:B<x>:LIN:POLARity?
            ```

        Info:
            - ``NORMal`` specifies normal LIN polarity.
            - ``INVerted`` specifies inverted LIN polarity.
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
            - Specifies the source waveform for the LIN bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:LIN:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform.
            - ``D<x>`` specifies a digital channel as the source waveform. (Requires option 3-MSO.).
        """
        return self._source

    @property
    def standard(self) -> BusBItemLinStandard:
        """Return the ``BUS:B<x>:LIN:STANDard`` command.

        Description:
            - Specifies the LIN bus standard to use.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN:STANDard?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN:STANDard?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LIN:STANDard value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LIN:STANDard {V1X|V2X|MIXed}
            - BUS:B<x>:LIN:STANDard?
            ```

        Info:
            - ``V1X`` sets the LIN bus standard to V1X.
            - ``V2X`` sets the LIN bus standard to V2X.
            - ``MIXed`` sets the LIN bus standard to MIXED.
        """
        return self._standard


class BusBItemLabel(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:LABel`` command.

    Description:
        - Specifies the waveform label for the bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:LABel <Qstring>
        - BUS:B<x>:LABel?
        ```

    Info:
        - ``<Qstring>`` is an alphanumeric string of text, enclosed in quotes, that contains the
          text label information for bus <x>. The text string is limited to 30 characters.
    """


class BusBItemI2cSdataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:SDATA:SOUrce`` command.

    Description:
        - Sets or returns the I2C SDATA source for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SDATA:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SDATA:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:SDATA:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:SDATA:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:I2C:SDATA:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the analog channel to use as the I2C SDATA source. x has a minimum of
          1 and a maximum of 4.
        - ``D<x>`` specifies the digital channel to use as the I2C SDATA source. x has a minimum of
          0 and a maximum of 15.
    """


class BusBItemI2cSdata(SCPICmdRead):
    """The ``BUS:B<x>:I2C:SDATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SDATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SDATA?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:SDATA:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cSdataSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemI2cSdataSource:
        """Return the ``BUS:B<x>:I2C:SDATA:SOUrce`` command.

        Description:
            - Sets or returns the I2C SDATA source for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SDATA:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SDATA:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:SDATA:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:SDATA:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:I2C:SDATA:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the analog channel to use as the I2C SDATA source. x has a minimum
              of 1 and a maximum of 4.
            - ``D<x>`` specifies the digital channel to use as the I2C SDATA source. x has a minimum
              of 0 and a maximum of 15.
        """
        return self._source


class BusBItemI2cSclkSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:SCLK:SOUrce`` command.

    Description:
        - Sets or returns the I2C SCLK source for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SCLK:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SCLK:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:SCLK:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:SCLK:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:I2C:SCLK:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the analog channel to use as the I2C SCLK source. x has a minimum of 1
          and a maximum of 4.
        - ``D<x>`` specifies the digital channel to use as the I2C SCLK source. x has a minimum of 0
          and a maximum of 15.
    """


class BusBItemI2cSclk(SCPICmdRead):
    """The ``BUS:B<x>:I2C:SCLK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SCLK?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SCLK?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:SCLK:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cSclkSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemI2cSclkSource:
        """Return the ``BUS:B<x>:I2C:SCLK:SOUrce`` command.

        Description:
            - Sets or returns the I2C SCLK source for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SCLK:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SCLK:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:SCLK:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:SCLK:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:I2C:SCLK:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the analog channel to use as the I2C SCLK source. x has a minimum
              of 1 and a maximum of 4.
            - ``D<x>`` specifies the digital channel to use as the I2C SCLK source. x has a minimum
              of 0 and a maximum of 15.
        """
        return self._source


class BusBItemI2cDataSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:DATA:SOUrce`` command.

    Description:
        - Sets or returns the I2C SDATA source for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATA:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATA:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATA:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:DATA:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:I2C:DATA:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the analog channel to use as the I2C SDATA source. x has a minimum of
          1 and a maximum of 4.
        - ``D<x>`` specifies the digital channel to use as the I2C SDATA source. x has a minimum of
          0 and a maximum of 15.
    """


class BusBItemI2cData(SCPICmdRead):
    """The ``BUS:B<x>:I2C:DATA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATA?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:DATA:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cDataSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemI2cDataSource:
        """Return the ``BUS:B<x>:I2C:DATA:SOUrce`` command.

        Description:
            - Sets or returns the I2C SDATA source for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATA:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATA:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:DATA:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:DATA:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:I2C:DATA:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the analog channel to use as the I2C SDATA source. x has a minimum
              of 1 and a maximum of 4.
            - ``D<x>`` specifies the digital channel to use as the I2C SDATA source. x has a minimum
              of 0 and a maximum of 15.
        """
        return self._source


class BusBItemI2cClockSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:CLOCK:SOUrce`` command.

    Description:
        - Sets or returns the I2C SCLK source for bus <x>, where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCK:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCK:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCK:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:CLOCK:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:I2C:CLOCK:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies the analog channel to use as the I2C SCLK source. x has a minimum of 1
          and a maximum of 4.
        - ``D<x>`` specifies the digital channel to use as the I2C SCLK source. x has a minimum of 0
          and a maximum of 15.
    """


class BusBItemI2cClock(SCPICmdRead):
    """The ``BUS:B<x>:I2C:CLOCK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCK?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCK?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``BUS:B<x>:I2C:CLOCK:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = BusBItemI2cClockSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> BusBItemI2cClockSource:
        """Return the ``BUS:B<x>:I2C:CLOCK:SOUrce`` command.

        Description:
            - Sets or returns the I2C SCLK source for bus <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCK:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCK:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:CLOCK:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:CLOCK:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:I2C:CLOCK:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies the analog channel to use as the I2C SCLK source. x has a minimum
              of 1 and a maximum of 4.
            - ``D<x>`` specifies the digital channel to use as the I2C SCLK source. x has a minimum
              of 0 and a maximum of 15.
        """
        return self._source


class BusBItemI2cAddressRwinclude(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:I2C:ADDRess:RWINClude`` command.

    Description:
        - Sets and returns whether the read/write bit is included in the address.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:ADDRess:RWINClude?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:ADDRess:RWINClude?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:I2C:ADDRess:RWINClude value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:I2C:ADDRess:RWINClude {ON|OFF|<NR1>}
        - BUS:B<x>:I2C:ADDRess:RWINClude?
        ```

    Info:
        - ``<NR1>`` = 0 does not include the read/write bit in the address; any other value includes
          the read/write bit in the address.
    """


class BusBItemI2cAddress(SCPICmdRead):
    """The ``BUS:B<x>:I2C:ADDRess`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:ADDRess?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:ADDRess?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.rwinclude``: The ``BUS:B<x>:I2C:ADDRess:RWINClude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rwinclude = BusBItemI2cAddressRwinclude(device, f"{self._cmd_syntax}:RWINClude")

    @property
    def rwinclude(self) -> BusBItemI2cAddressRwinclude:
        """Return the ``BUS:B<x>:I2C:ADDRess:RWINClude`` command.

        Description:
            - Sets and returns whether the read/write bit is included in the address.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:ADDRess:RWINClude?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:ADDRess:RWINClude?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``BUS:B<x>:I2C:ADDRess:RWINClude value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:I2C:ADDRess:RWINClude {ON|OFF|<NR1>}
            - BUS:B<x>:I2C:ADDRess:RWINClude?
            ```

        Info:
            - ``<NR1>`` = 0 does not include the read/write bit in the address; any other value
              includes the read/write bit in the address.
        """
        return self._rwinclude


class BusBItemI2c(SCPICmdRead):
    """The ``BUS:B<x>:I2C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:I2C?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``BUS:B<x>:I2C:ADDRess`` command tree.
        - ``.clock``: The ``BUS:B<x>:I2C:CLOCK`` command tree.
        - ``.sclk``: The ``BUS:B<x>:I2C:SCLK`` command tree.
        - ``.data``: The ``BUS:B<x>:I2C:DATA`` command tree.
        - ``.sdata``: The ``BUS:B<x>:I2C:SDATA`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = BusBItemI2cAddress(device, f"{self._cmd_syntax}:ADDRess")
        self._clock = BusBItemI2cClock(device, f"{self._cmd_syntax}:CLOCK")
        self._sclk = BusBItemI2cSclk(device, f"{self._cmd_syntax}:SCLK")
        self._data = BusBItemI2cData(device, f"{self._cmd_syntax}:DATA")
        self._sdata = BusBItemI2cSdata(device, f"{self._cmd_syntax}:SDATA")

    @property
    def address(self) -> BusBItemI2cAddress:
        """Return the ``BUS:B<x>:I2C:ADDRess`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:ADDRess?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:ADDRess?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.rwinclude``: The ``BUS:B<x>:I2C:ADDRess:RWINClude`` command.
        """
        return self._address

    @property
    def clock(self) -> BusBItemI2cClock:
        """Return the ``BUS:B<x>:I2C:CLOCK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:CLOCK?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:CLOCK?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I2C:CLOCK:SOUrce`` command.
        """
        return self._clock

    @property
    def sclk(self) -> BusBItemI2cSclk:
        """Return the ``BUS:B<x>:I2C:SCLK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SCLK?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SCLK?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I2C:SCLK:SOUrce`` command.
        """
        return self._sclk

    @property
    def data(self) -> BusBItemI2cData:
        """Return the ``BUS:B<x>:I2C:DATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:DATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I2C:DATA:SOUrce`` command.
        """
        return self._data

    @property
    def sdata(self) -> BusBItemI2cSdata:
        """Return the ``BUS:B<x>:I2C:SDATA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C:SDATA?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C:SDATA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``BUS:B<x>:I2C:SDATA:SOUrce`` command.
        """
        return self._sdata


class BusBItemFlexraySource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:SOUrce`` command.

    Description:
        - Specifies the FlexRay bus source waveform.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:FLEXray:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the source waveform.
    """


class BusBItemFlexraySignal(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:SIGnal`` command.

    Description:
        - This command sets or queries the FlexRay signal type for the specified bus. The bus number
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SIGnal?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SIGnal?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:SIGnal value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:SIGnal {BDIFFBP|BM|TXRX}
        - BUS:B<x>:FLEXray:SIGnal?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``BDIFFBP`` sets the FlexRay signal type to BDIFFBP.
        - ``BM`` sets the FlexRay signal type to BM.
        - ``TXRX`` sets the FlexRay signal type to TXRX.
    """


class BusBItemFlexrayChannel(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:CHannel`` command.

    Description:
        - This command sets or queries the FlexRay channel type for the specified bus. The bus
          number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:CHannel?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:CHannel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:CHannel value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:CHannel {A|B}
        - BUS:B<x>:FLEXray:CHannel?
        ```

    Info:
        - ``B<x>`` is the number of the bus.
        - ``A`` specifies the A channel.
        - ``B`` specifies the B channel.
    """


class BusBItemFlexrayBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:FLEXray:BITRate`` command.

    Description:
        - Specifies the bit rate for the FlexRay bus signal. The maximum bitrate is 100 Mbps.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:FLEXray:BITRate <NR1>
        - BUS:B<x>:FLEXray:BITRate?
        ```

    Info:
        - ``<NR1>`` specifies the FlexRay bus bit rate. You can enter any positive integer, and the
          instrument will coerce the value to the closest supported bit rate.
    """


class BusBItemFlexray(SCPICmdRead):
    """The ``BUS:B<x>:FLEXray`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:FLEXray:BITRate`` command.
        - ``.channel``: The ``BUS:B<x>:FLEXray:CHannel`` command.
        - ``.signal``: The ``BUS:B<x>:FLEXray:SIGnal`` command.
        - ``.source``: The ``BUS:B<x>:FLEXray:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemFlexrayBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._channel = BusBItemFlexrayChannel(device, f"{self._cmd_syntax}:CHannel")
        self._signal = BusBItemFlexraySignal(device, f"{self._cmd_syntax}:SIGnal")
        self._source = BusBItemFlexraySource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemFlexrayBitrate:
        """Return the ``BUS:B<x>:FLEXray:BITRate`` command.

        Description:
            - Specifies the bit rate for the FlexRay bus signal. The maximum bitrate is 100 Mbps.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:BITRate <NR1>
            - BUS:B<x>:FLEXray:BITRate?
            ```

        Info:
            - ``<NR1>`` specifies the FlexRay bus bit rate. You can enter any positive integer, and
              the instrument will coerce the value to the closest supported bit rate.
        """
        return self._bitrate

    @property
    def channel(self) -> BusBItemFlexrayChannel:
        """Return the ``BUS:B<x>:FLEXray:CHannel`` command.

        Description:
            - This command sets or queries the FlexRay channel type for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:CHannel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:CHannel?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:CHannel value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:CHannel {A|B}
            - BUS:B<x>:FLEXray:CHannel?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``A`` specifies the A channel.
            - ``B`` specifies the B channel.
        """
        return self._channel

    @property
    def signal(self) -> BusBItemFlexraySignal:
        """Return the ``BUS:B<x>:FLEXray:SIGnal`` command.

        Description:
            - This command sets or queries the FlexRay signal type for the specified bus. The bus
              number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SIGnal?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SIGnal?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:SIGnal value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:SIGnal {BDIFFBP|BM|TXRX}
            - BUS:B<x>:FLEXray:SIGnal?
            ```

        Info:
            - ``B<x>`` is the number of the bus.
            - ``BDIFFBP`` sets the FlexRay signal type to BDIFFBP.
            - ``BM`` sets the FlexRay signal type to BM.
            - ``TXRX`` sets the FlexRay signal type to TXRX.
        """
        return self._signal

    @property
    def source(self) -> BusBItemFlexraySource:
        """Return the ``BUS:B<x>:FLEXray:SOUrce`` command.

        Description:
            - Specifies the FlexRay bus source waveform.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:FLEXray:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:FLEXray:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:FLEXray:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the source waveform.
        """
        return self._source


class BusBItemDisplayType(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DISplay:TYPe`` command.

    Description:
        - Specifies the display type for bus. You can set up the bus to display the protocol
          information, the logic waveforms that comprise the bus, or both.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:TYPe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DISplay:TYPe {BUS|BOTh}
        - BUS:B<x>:DISplay:TYPe?
        ```

    Info:
        - ``BUS`` displays the bus waveforms only.
        - ``BOTh`` displays both the bus and logic waveforms.
    """


class BusBItemDisplayFormat(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:DISplay:FORMAt`` command.

    Description:
        - Sets or returns the display format for the numerical information in the bus waveform <x>,
          where x is the bus number.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:FORMAt?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:FORMAt?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:FORMAt value``
          command.

    SCPI Syntax:
        ```
        - BUS:B<x>:DISplay:FORMAt {BINary|HEXadecimal|ASCII|MIXed}
        - BUS:B<x>:DISplay:FORMAt?
        ```

    Info:
        - ``BINary`` specifies a binary data display.
        - ``HEXadecimal`` specifies a hexadecimal data display.
        - ``ASCII`` specifies an ASCII format for RS232 only.
        - ``MIXed`` specifies a mixed format for LIN only.
    """


class BusBItemDisplay(SCPICmdRead):
    """The ``BUS:B<x>:DISplay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.format``: The ``BUS:B<x>:DISplay:FORMAt`` command.
        - ``.type``: The ``BUS:B<x>:DISplay:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._format = BusBItemDisplayFormat(device, f"{self._cmd_syntax}:FORMAt")
        self._type = BusBItemDisplayType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def format(self) -> BusBItemDisplayFormat:
        """Return the ``BUS:B<x>:DISplay:FORMAt`` command.

        Description:
            - Sets or returns the display format for the numerical information in the bus waveform
              <x>, where x is the bus number.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:FORMAt?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:FORMAt?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:FORMAt value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DISplay:FORMAt {BINary|HEXadecimal|ASCII|MIXed}
            - BUS:B<x>:DISplay:FORMAt?
            ```

        Info:
            - ``BINary`` specifies a binary data display.
            - ``HEXadecimal`` specifies a hexadecimal data display.
            - ``ASCII`` specifies an ASCII format for RS232 only.
            - ``MIXed`` specifies a mixed format for LIN only.
        """
        return self._format

    @property
    def type(self) -> BusBItemDisplayType:
        """Return the ``BUS:B<x>:DISplay:TYPe`` command.

        Description:
            - Specifies the display type for bus. You can set up the bus to display the protocol
              information, the logic waveforms that comprise the bus, or both.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:DISplay:TYPe value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:DISplay:TYPe {BUS|BOTh}
            - BUS:B<x>:DISplay:TYPe?
            ```

        Info:
            - ``BUS`` displays the bus waveforms only.
            - ``BOTh`` displays both the bus and logic waveforms.
        """
        return self._type


class BusBItemCanSource(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:SOUrce`` command.

    Description:
        - Specifies the CAN bus data source.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SOUrce value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:SOUrce {CH<x>|D<x>}
        - BUS:B<x>:CAN:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies an analog channel as the data source waveform.
        - ``D<x>`` specifies a digital channel as the data source waveform. (Requires installation
          of option 3-MSO.).
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


class BusBItemCanProbe(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:PRObe`` command.

    Description:
        - Specifies the probing method for the CAN bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:PRObe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:PRObe value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:PRObe {CANH|CANL|RX|TX|DIFFerential}
        - BUS:B<x>:CAN:PRObe?
        ```

    Info:
        - ``CANH`` specifies the single-ended CANH signal, as specified by the CAN standard.
        - ``CANL`` specifies the single-ended CANL signal, as specified by the CAN standard.
        - ``RX`` specifies the receive signal on the bus side of the CAN transceiver.
        - ``TX`` specifies the transmit signal.
        - ``DIFFerential`` specifies the differential CAN signal.
    """


class BusBItemCanBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``BUS:B<x>:CAN:BITRate`` command.

    Description:
        - Specifies the bit rate for the CAN bus.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate value`` command.

    SCPI Syntax:
        ```
        - BUS:B<x>:CAN:BITRate <NR1>
        - BUS:B<x>:CAN:BITRate?
        ```

    Info:
        - ``<NR1>`` is the bit rate. The instrument supports bit rates at 10 bps intervals. You can
          enter any positive integer, and the instrument will coerce the value to the closest
          supported bit rate.
    """


class BusBItemCan(SCPICmdRead):
    """The ``BUS:B<x>:CAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>:CAN?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bitrate``: The ``BUS:B<x>:CAN:BITRate`` command.
        - ``.probe``: The ``BUS:B<x>:CAN:PRObe`` command.
        - ``.samplepoint``: The ``BUS:B<x>:CAN:SAMPLEpoint`` command.
        - ``.source``: The ``BUS:B<x>:CAN:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bitrate = BusBItemCanBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._probe = BusBItemCanProbe(device, f"{self._cmd_syntax}:PRObe")
        self._samplepoint = BusBItemCanSamplepoint(device, f"{self._cmd_syntax}:SAMPLEpoint")
        self._source = BusBItemCanSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def bitrate(self) -> BusBItemCanBitrate:
        """Return the ``BUS:B<x>:CAN:BITRate`` command.

        Description:
            - Specifies the bit rate for the CAN bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:BITRate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:BITRate value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:BITRate <NR1>
            - BUS:B<x>:CAN:BITRate?
            ```

        Info:
            - ``<NR1>`` is the bit rate. The instrument supports bit rates at 10 bps intervals. You
              can enter any positive integer, and the instrument will coerce the value to the
              closest supported bit rate.
        """
        return self._bitrate

    @property
    def probe(self) -> BusBItemCanProbe:
        """Return the ``BUS:B<x>:CAN:PRObe`` command.

        Description:
            - Specifies the probing method for the CAN bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:PRObe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:PRObe value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:PRObe {CANH|CANL|RX|TX|DIFFerential}
            - BUS:B<x>:CAN:PRObe?
            ```

        Info:
            - ``CANH`` specifies the single-ended CANH signal, as specified by the CAN standard.
            - ``CANL`` specifies the single-ended CANL signal, as specified by the CAN standard.
            - ``RX`` specifies the receive signal on the bus side of the CAN transceiver.
            - ``TX`` specifies the transmit signal.
            - ``DIFFerential`` specifies the differential CAN signal.
        """
        return self._probe

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
    def source(self) -> BusBItemCanSource:
        """Return the ``BUS:B<x>:CAN:SOUrce`` command.

        Description:
            - Specifies the CAN bus data source.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:CAN:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - BUS:B<x>:CAN:SOUrce {CH<x>|D<x>}
            - BUS:B<x>:CAN:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies an analog channel as the data source waveform.
            - ``D<x>`` specifies a digital channel as the data source waveform. (Requires
              installation of option 3-MSO.).
        """
        return self._source


#  pylint: disable=too-many-instance-attributes
class BusBItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``BUS:B<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUS:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``BUS:B<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.can``: The ``BUS:B<x>:CAN`` command tree.
        - ``.display``: The ``BUS:B<x>:DISplay`` command tree.
        - ``.flexray``: The ``BUS:B<x>:FLEXray`` command tree.
        - ``.i2c``: The ``BUS:B<x>:I2C`` command tree.
        - ``.label``: The ``BUS:B<x>:LABel`` command.
        - ``.lin``: The ``BUS:B<x>:LIN`` command tree.
        - ``.parallel``: The ``BUS:B<x>:PARallel`` command tree.
        - ``.position``: The ``BUS:B<x>:POSition`` command.
        - ``.rs232c``: The ``BUS:B<x>:RS232C`` command tree.
        - ``.spi``: The ``BUS:B<x>:SPI`` command tree.
        - ``.state``: The ``BUS:B<x>:STATE`` command.
        - ``.type``: The ``BUS:B<x>:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._can = BusBItemCan(device, f"{self._cmd_syntax}:CAN")
        self._display = BusBItemDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._flexray = BusBItemFlexray(device, f"{self._cmd_syntax}:FLEXray")
        self._i2c = BusBItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._label = BusBItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._lin = BusBItemLin(device, f"{self._cmd_syntax}:LIN")
        self._parallel = BusBItemParallel(device, f"{self._cmd_syntax}:PARallel")
        self._position = BusBItemPosition(device, f"{self._cmd_syntax}:POSition")
        self._rs232c = BusBItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._spi = BusBItemSpi(device, f"{self._cmd_syntax}:SPI")
        self._state = BusBItemState(device, f"{self._cmd_syntax}:STATE")
        self._type = BusBItemType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def can(self) -> BusBItemCan:
        """Return the ``BUS:B<x>:CAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:CAN?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:CAN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:CAN:BITRate`` command.
            - ``.probe``: The ``BUS:B<x>:CAN:PRObe`` command.
            - ``.samplepoint``: The ``BUS:B<x>:CAN:SAMPLEpoint`` command.
            - ``.source``: The ``BUS:B<x>:CAN:SOUrce`` command.
        """
        return self._can

    @property
    def display(self) -> BusBItemDisplay:
        """Return the ``BUS:B<x>:DISplay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:DISplay?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.format``: The ``BUS:B<x>:DISplay:FORMAt`` command.
            - ``.type``: The ``BUS:B<x>:DISplay:TYPe`` command.
        """
        return self._display

    @property
    def flexray(self) -> BusBItemFlexray:
        """Return the ``BUS:B<x>:FLEXray`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:FLEXray?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:FLEXray?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:FLEXray:BITRate`` command.
            - ``.channel``: The ``BUS:B<x>:FLEXray:CHannel`` command.
            - ``.signal``: The ``BUS:B<x>:FLEXray:SIGnal`` command.
            - ``.source``: The ``BUS:B<x>:FLEXray:SOUrce`` command.
        """
        return self._flexray

    @property
    def i2c(self) -> BusBItemI2c:
        """Return the ``BUS:B<x>:I2C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:I2C?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:I2C?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``BUS:B<x>:I2C:ADDRess`` command tree.
            - ``.clock``: The ``BUS:B<x>:I2C:CLOCK`` command tree.
            - ``.sclk``: The ``BUS:B<x>:I2C:SCLK`` command tree.
            - ``.data``: The ``BUS:B<x>:I2C:DATA`` command tree.
            - ``.sdata``: The ``BUS:B<x>:I2C:SDATA`` command tree.
        """
        return self._i2c

    @property
    def label(self) -> BusBItemLabel:
        """Return the ``BUS:B<x>:LABel`` command.

        Description:
            - Specifies the waveform label for the bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LABel?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:LABel value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:LABel <Qstring>
            - BUS:B<x>:LABel?
            ```

        Info:
            - ``<Qstring>`` is an alphanumeric string of text, enclosed in quotes, that contains the
              text label information for bus <x>. The text string is limited to 30 characters.
        """
        return self._label

    @property
    def lin(self) -> BusBItemLin:
        """Return the ``BUS:B<x>:LIN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:LIN?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:LIN?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:LIN:BITRate`` command.
            - ``.idformat``: The ``BUS:B<x>:LIN:IDFORmat`` command.
            - ``.polarity``: The ``BUS:B<x>:LIN:POLARity`` command.
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

        Sub-properties:
            - ``.bit``: The ``BUS:B<x>:PARallel:BIT<x>`` command tree.
            - ``.clock``: The ``BUS:B<x>:PARallel:CLOCK`` command tree.
            - ``.width``: The ``BUS:B<x>:PARallel:WIDth`` command.
        """
        return self._parallel

    @property
    def position(self) -> BusBItemPosition:
        """Return the ``BUS:B<x>:POSition`` command.

        Description:
            - This command specifies the position of the bus waveform on the display.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:POSition?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:POSition value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:POSition <NR3>
            - BUS:B<x>:POSition?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the position of the bus <x>
              waveform on the display.
        """
        return self._position

    @property
    def rs232c(self) -> BusBItemRs232c:
        """Return the ``BUS:B<x>:RS232C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:RS232C?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:RS232C?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bitrate``: The ``BUS:B<x>:RS232C:BITRate`` command.
            - ``.databits``: The ``BUS:B<x>:RS232C:DATABits`` command.
            - ``.delimiter``: The ``BUS:B<x>:RS232C:DELIMiter`` command.
            - ``.displaymode``: The ``BUS:B<x>:RS232C:DISplaymode`` command.
            - ``.parity``: The ``BUS:B<x>:RS232C:PARity`` command.
            - ``.polarity``: The ``BUS:B<x>:RS232C:POLarity`` command.
            - ``.rx``: The ``BUS:B<x>:RS232C:RX`` command tree.
            - ``.tx``: The ``BUS:B<x>:RS232C:TX`` command tree.
        """
        return self._rs232c

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
            - ``.data``: The ``BUS:B<x>:SPI:DATA`` command tree.
            - ``.framing``: The ``BUS:B<x>:SPI:FRAMING`` command.
            - ``.idletime``: The ``BUS:B<x>:SPI:IDLETime`` command.
            - ``.clock``: The ``BUS:B<x>:SPI:CLOCK`` command tree.
            - ``.sclk``: The ``BUS:B<x>:SPI:SCLK`` command tree.
            - ``.select``: The ``BUS:B<x>:SPI:SELect`` command tree.
            - ``.ss``: The ``BUS:B<x>:SPI:SS`` command tree.
        """
        return self._spi

    @property
    def state(self) -> BusBItemState:
        """Return the ``BUS:B<x>:STATE`` command.

        Description:
            - This command specifies the on/off state of the bus.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:STATE {ON|OFF|<NR1>}
            - BUS:B<x>:STATE?
            ```

        Info:
            - ``ON`` or <NR1> ≠ 0 turns on the bus.
            - ``OFF`` or <NR1> = 0 turns off the bus.
        """
        return self._state

    @property
    def type(self) -> BusBItemType:
        """Return the ``BUS:B<x>:TYPE`` command.

        Description:
            - Sets or returns the bus type for <x>, where x is the bus number.

        Usage:
            - Using the ``.write(value)`` method will send the ``BUS:B<x>:TYPE value`` command.

        SCPI Syntax:
            ```
            - BUS:B<x>:TYPE {I2C|SPI|CAN|RS232C|PARallel|LIN}
            ```

        Info:
            - ``I2C`` specifies the Inter-IC bus.
            - ``SPI`` specifies the Serial Peripheral Interface bus (not available on two-channel
              models).
            - ``CAN`` specifies the Controller Area Network bus.
            - ``RS232C`` specifies the RS232C bus.
            - ``PARallel`` specifies the parallel bus.
            - ``LIN`` specifies the LIN bus.
        """
        return self._type


class Bus(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``BUS`` command.

    Description:
        - Sets or returns the parameters for each bus. These parameters affect either the Serial
          Trigger Setup or the Bus Display.

    Usage:
        - Using the ``.write()`` method will send the ``BUS`` command.

    SCPI Syntax:
        ```
        - BUS
        ```

    Properties:
        - ``.b``: The ``BUS:B<x>`` command tree.
        - ``.lowerthreshold``: The ``BUS:LOWerthreshold`` command tree.
        - ``.threshold``: The ``BUS:THReshold`` command tree.
        - ``.upperthreshold``: The ``BUS:UPPerthreshold`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "BUS") -> None:
        super().__init__(device, cmd_syntax)
        self._b: Dict[int, BusBItem] = DefaultDictPassKeyToFactory(
            lambda x: BusBItem(device, f"{self._cmd_syntax}:B{x}")
        )
        self._lowerthreshold = BusLowerthreshold(device, f"{self._cmd_syntax}:LOWerthreshold")
        self._threshold = BusThreshold(device, f"{self._cmd_syntax}:THReshold")
        self._upperthreshold = BusUpperthreshold(device, f"{self._cmd_syntax}:UPPerthreshold")

    @property
    def b(self) -> Dict[int, BusBItem]:
        """Return the ``BUS:B<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:B<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:B<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.can``: The ``BUS:B<x>:CAN`` command tree.
            - ``.display``: The ``BUS:B<x>:DISplay`` command tree.
            - ``.flexray``: The ``BUS:B<x>:FLEXray`` command tree.
            - ``.i2c``: The ``BUS:B<x>:I2C`` command tree.
            - ``.label``: The ``BUS:B<x>:LABel`` command.
            - ``.lin``: The ``BUS:B<x>:LIN`` command tree.
            - ``.parallel``: The ``BUS:B<x>:PARallel`` command tree.
            - ``.position``: The ``BUS:B<x>:POSition`` command.
            - ``.rs232c``: The ``BUS:B<x>:RS232C`` command tree.
            - ``.spi``: The ``BUS:B<x>:SPI`` command tree.
            - ``.state``: The ``BUS:B<x>:STATE`` command.
            - ``.type``: The ``BUS:B<x>:TYPE`` command.
        """
        return self._b

    @property
    def lowerthreshold(self) -> BusLowerthreshold:
        """Return the ``BUS:LOWerthreshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:LOWerthreshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:LOWerthreshold?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``BUS:LOWerthreshold:CH<x>`` command.
        """
        return self._lowerthreshold

    @property
    def threshold(self) -> BusThreshold:
        """Return the ``BUS:THReshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:THReshold?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``BUS:THReshold:CH<x>`` command.
            - ``.d``: The ``BUS:THReshold:D<x>`` command.
        """
        return self._threshold

    @property
    def upperthreshold(self) -> BusUpperthreshold:
        """Return the ``BUS:UPPerthreshold`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``BUS:UPPerthreshold?`` query.
            - Using the ``.verify(value)`` method will send the ``BUS:UPPerthreshold?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``BUS:UPPerthreshold:CH<x>`` command.
        """
        return self._upperthreshold
