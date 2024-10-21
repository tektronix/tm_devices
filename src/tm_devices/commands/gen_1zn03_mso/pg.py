"""The pg commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - PG:AMPlitude {2.5|3.3|5V}
    - PG:AMPlitude?
    - PG:BIT:ONE {HIGH|LOW|TOGGLE|HIGH_Z}
    - PG:BIT:ONE?
    - PG:BIT:THREE {HIGH|LOW|TOGGLE|HIGH_Z}
    - PG:BIT:THREE?
    - PG:BIT:TWO {HIGH|LOW|TOGGLE|HIGH_Z}
    - PG:BIT:TWO?
    - PG:BIT:ZERO {HIGH|LOW|TOGGLE|HIGH_Z}
    - PG:BIT:ZERO?
    - PG:BITRate <NR3>
    - PG:BITRate?
    - PG:BURSt:CCOUnt <NR1>
    - PG:BURSt:CCOUnt?
    - PG:BURSt:TRIGger
    - PG:FILE:PATTern <QString>
    - PG:FILE:PATTern?
    - PG:OUTPut:MODe {CONTinuous|BURSt|OFF}
    - PG:OUTPut:MODe?
    - PG:PATTERNdefinition {MANual|FILE}
    - PG:PATTERNdefinition?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class PgPatterndefinition(SCPICmdWrite, SCPICmdRead):
    """The ``PG:PATTERNdefinition`` command.

    Description:
        - This command sets or queries the Pattern Generator definition. If set to manual mode, you
          can configure the bit independently. If set to file mode, you can set a data file that
          will be loaded into memory and generated as a sequence.

    Usage:
        - Using the ``.query()`` method will send the ``PG:PATTERNdefinition?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:PATTERNdefinition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PG:PATTERNdefinition value`` command.

    SCPI Syntax:
        ```
        - PG:PATTERNdefinition {MANual|FILE}
        - PG:PATTERNdefinition?
        ```

    Info:
        - ``MANual`` sets the pattern definition source to Manual. This is the default value.
        - ``FILE`` sets the pattern definition source to File.
    """


class PgOutputMode(SCPICmdWrite, SCPICmdRead):
    """The ``PG:OUTPut:MODe`` command.

    Description:
        - This command sets or queries the Pattern Generator output mode.

    Usage:
        - Using the ``.query()`` method will send the ``PG:OUTPut:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:OUTPut:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PG:OUTPut:MODe value`` command.

    SCPI Syntax:
        ```
        - PG:OUTPut:MODe {CONTinuous|BURSt|OFF}
        - PG:OUTPut:MODe?
        ```

    Info:
        - ``CONTinuous`` sets the Pattern Generator output type to continuous.
        - ``BURSt`` sets the Pattern Generator output type to burst.
        - ``OFF`` sets the Pattern Generator output type to off. This is the default value.
    """


class PgOutput(SCPICmdRead):
    """The ``PG:OUTPut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PG:OUTPut?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:OUTPut?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``PG:OUTPut:MODe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = PgOutputMode(device, f"{self._cmd_syntax}:MODe")

    @property
    def mode(self) -> PgOutputMode:
        """Return the ``PG:OUTPut:MODe`` command.

        Description:
            - This command sets or queries the Pattern Generator output mode.

        Usage:
            - Using the ``.query()`` method will send the ``PG:OUTPut:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:OUTPut:MODe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PG:OUTPut:MODe value`` command.

        SCPI Syntax:
            ```
            - PG:OUTPut:MODe {CONTinuous|BURSt|OFF}
            - PG:OUTPut:MODe?
            ```

        Info:
            - ``CONTinuous`` sets the Pattern Generator output type to continuous.
            - ``BURSt`` sets the Pattern Generator output type to burst.
            - ``OFF`` sets the Pattern Generator output type to off. This is the default value.
        """
        return self._mode


class PgFilePattern(SCPICmdWrite, SCPICmdRead):
    """The ``PG:FILE:PATTern`` command.

    Description:
        - This command sets or queries the path of your data file to generate a digital pattern in
          file mode. Only .csv files are supported.

    Usage:
        - Using the ``.query()`` method will send the ``PG:FILE:PATTern?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:FILE:PATTern?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PG:FILE:PATTern value`` command.

    SCPI Syntax:
        ```
        - PG:FILE:PATTern <QString>
        - PG:FILE:PATTern?
        ```

    Info:
        - ``<QString>`` is the file path that specifies the location of the specified instrument
          file.
    """

    _WRAP_ARG_WITH_QUOTES = True


class PgFile(SCPICmdRead):
    """The ``PG:FILE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PG:FILE?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:FILE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.pattern``: The ``PG:FILE:PATTern`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._pattern = PgFilePattern(device, f"{self._cmd_syntax}:PATTern")

    @property
    def pattern(self) -> PgFilePattern:
        """Return the ``PG:FILE:PATTern`` command.

        Description:
            - This command sets or queries the path of your data file to generate a digital pattern
              in file mode. Only .csv files are supported.

        Usage:
            - Using the ``.query()`` method will send the ``PG:FILE:PATTern?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:FILE:PATTern?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PG:FILE:PATTern value`` command.

        SCPI Syntax:
            ```
            - PG:FILE:PATTern <QString>
            - PG:FILE:PATTern?
            ```

        Info:
            - ``<QString>`` is the file path that specifies the location of the specified instrument
              file.
        """
        return self._pattern


class PgBurstTrigger(SCPICmdWriteNoArguments):
    """The ``PG:BURSt:TRIGger`` command.

    Description:
        - This command manually starts the burst pattern. This is only available when output is
          Burst.

    Usage:
        - Using the ``.write()`` method will send the ``PG:BURSt:TRIGger`` command.

    SCPI Syntax:
        ```
        - PG:BURSt:TRIGger
        ```
    """


class PgBurstCcount(SCPICmdWrite, SCPICmdRead):
    """The ``PG:BURSt:CCOUnt`` command.

    Description:
        - This command sets or queries the cycle count for Pattern Generator burst mode. This is
          only available when output is Burst.

    Usage:
        - Using the ``.query()`` method will send the ``PG:BURSt:CCOUnt?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:BURSt:CCOUnt?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PG:BURSt:CCOUnt value`` command.

    SCPI Syntax:
        ```
        - PG:BURSt:CCOUnt <NR1>
        - PG:BURSt:CCOUnt?
        ```

    Info:
        - ``<NR1>`` sets the cycle count for Pattern Generator burst mode. The minimum cycle value
          can be set is 1 and maximum cycles are 2000. The default value is 1.
    """


class PgBurst(SCPICmdRead):
    """The ``PG:BURSt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PG:BURSt?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:BURSt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ccount``: The ``PG:BURSt:CCOUnt`` command.
        - ``.trigger``: The ``PG:BURSt:TRIGger`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ccount = PgBurstCcount(device, f"{self._cmd_syntax}:CCOUnt")
        self._trigger = PgBurstTrigger(device, f"{self._cmd_syntax}:TRIGger")

    @property
    def ccount(self) -> PgBurstCcount:
        """Return the ``PG:BURSt:CCOUnt`` command.

        Description:
            - This command sets or queries the cycle count for Pattern Generator burst mode. This is
              only available when output is Burst.

        Usage:
            - Using the ``.query()`` method will send the ``PG:BURSt:CCOUnt?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:BURSt:CCOUnt?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PG:BURSt:CCOUnt value`` command.

        SCPI Syntax:
            ```
            - PG:BURSt:CCOUnt <NR1>
            - PG:BURSt:CCOUnt?
            ```

        Info:
            - ``<NR1>`` sets the cycle count for Pattern Generator burst mode. The minimum cycle
              value can be set is 1 and maximum cycles are 2000. The default value is 1.
        """
        return self._ccount

    @property
    def trigger(self) -> PgBurstTrigger:
        """Return the ``PG:BURSt:TRIGger`` command.

        Description:
            - This command manually starts the burst pattern. This is only available when output is
              Burst.

        Usage:
            - Using the ``.write()`` method will send the ``PG:BURSt:TRIGger`` command.

        SCPI Syntax:
            ```
            - PG:BURSt:TRIGger
            ```
        """
        return self._trigger


class PgBitrate(SCPICmdWrite, SCPICmdRead):
    """The ``PG:BITRate`` command.

    Description:
        - This command sets or queries the bit rate of data in the Pattern Generator. You can give
          any value, but it will take nearest possible value and generate the pattern.

    Usage:
        - Using the ``.query()`` method will send the ``PG:BITRate?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:BITRate?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PG:BITRate value`` command.

    SCPI Syntax:
        ```
        - PG:BITRate <NR3>
        - PG:BITRate?
        ```

    Info:
        - ``<NR3>`` sets the Pattern Generator bit rate. The minimum bit rate is 1 b/s and maximum
          bit rate is 25 Mb/s. The default value is 125000 b/s.
    """


class PgBitZero(SCPICmdWrite, SCPICmdRead):
    """The ``PG:BIT:ZERO`` command.

    Description:
        - This command sets or queries the output value of Pattern Generator bit 0.

    Usage:
        - Using the ``.query()`` method will send the ``PG:BIT:ZERO?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:BIT:ZERO?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PG:BIT:ZERO value`` command.

    SCPI Syntax:
        ```
        - PG:BIT:ZERO {HIGH|LOW|TOGGLE|HIGH_Z}
        - PG:BIT:ZERO?
        ```

    Info:
        - ``LOW`` sets the Pattern Generator bit value to Low.
        - ``HIGH`` sets the Pattern Generator bit value to High.
        - ``TOGGLE`` sets the Pattern Generator bit value to Toggle.
        - ``HIGH_Z`` sets the Pattern Generator bit value to Hi-Z. Only available for Continuos
          mode.
    """


class PgBitTwo(SCPICmdWrite, SCPICmdRead):
    """The ``PG:BIT:TWO`` command.

    Description:
        - This command sets or queries the output value of Pattern Generator bit 2.

    Usage:
        - Using the ``.query()`` method will send the ``PG:BIT:TWO?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:BIT:TWO?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PG:BIT:TWO value`` command.

    SCPI Syntax:
        ```
        - PG:BIT:TWO {HIGH|LOW|TOGGLE|HIGH_Z}
        - PG:BIT:TWO?
        ```

    Info:
        - ``LOW`` sets the Pattern Generator bit value to Low.
        - ``HIGH`` sets the Pattern Generator bit value to High.
        - ``TOGGLE`` sets the Pattern Generator bit value to Toggle.
        - ``HIGH_Z`` sets the Pattern Generator bit value to Hi-Z. Only available for Continuos
          mode.
    """


class PgBitThree(SCPICmdWrite, SCPICmdRead):
    """The ``PG:BIT:THREE`` command.

    Description:
        - This command sets or queries the output value of Pattern Generator bit 3.

    Usage:
        - Using the ``.query()`` method will send the ``PG:BIT:THREE?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:BIT:THREE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PG:BIT:THREE value`` command.

    SCPI Syntax:
        ```
        - PG:BIT:THREE {HIGH|LOW|TOGGLE|HIGH_Z}
        - PG:BIT:THREE?
        ```

    Info:
        - ``LOW`` sets the Pattern Generator bit value to Low.
        - ``HIGH`` sets the Pattern Generator bit value to High.
        - ``TOGGLE`` sets the Pattern Generator bit value to Toggle.
        - ``HIGH_Z`` sets the Pattern Generator bit value to Hi-Z. Only available for Continuos
          mode.
    """


class PgBitOne(SCPICmdWrite, SCPICmdRead):
    """The ``PG:BIT:ONE`` command.

    Description:
        - This command sets or queries the output value of Pattern Generator bit 1.

    Usage:
        - Using the ``.query()`` method will send the ``PG:BIT:ONE?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:BIT:ONE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PG:BIT:ONE value`` command.

    SCPI Syntax:
        ```
        - PG:BIT:ONE {HIGH|LOW|TOGGLE|HIGH_Z}
        - PG:BIT:ONE?
        ```

    Info:
        - ``LOW`` sets the Pattern Generator bit value to Low.
        - ``HIGH`` sets the Pattern Generator bit value to High.
        - ``TOGGLE`` sets the Pattern Generator bit value to Toggle.
        - ``HIGH_Z`` sets the Pattern Generator bit value to Hi-Z. Only available for Continuos
          mode.
    """


class PgBit(SCPICmdRead):
    """The ``PG:BIT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PG:BIT?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:BIT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.one``: The ``PG:BIT:ONE`` command.
        - ``.three``: The ``PG:BIT:THREE`` command.
        - ``.two``: The ``PG:BIT:TWO`` command.
        - ``.zero``: The ``PG:BIT:ZERO`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._one = PgBitOne(device, f"{self._cmd_syntax}:ONE")
        self._three = PgBitThree(device, f"{self._cmd_syntax}:THREE")
        self._two = PgBitTwo(device, f"{self._cmd_syntax}:TWO")
        self._zero = PgBitZero(device, f"{self._cmd_syntax}:ZERO")

    @property
    def one(self) -> PgBitOne:
        """Return the ``PG:BIT:ONE`` command.

        Description:
            - This command sets or queries the output value of Pattern Generator bit 1.

        Usage:
            - Using the ``.query()`` method will send the ``PG:BIT:ONE?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:BIT:ONE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PG:BIT:ONE value`` command.

        SCPI Syntax:
            ```
            - PG:BIT:ONE {HIGH|LOW|TOGGLE|HIGH_Z}
            - PG:BIT:ONE?
            ```

        Info:
            - ``LOW`` sets the Pattern Generator bit value to Low.
            - ``HIGH`` sets the Pattern Generator bit value to High.
            - ``TOGGLE`` sets the Pattern Generator bit value to Toggle.
            - ``HIGH_Z`` sets the Pattern Generator bit value to Hi-Z. Only available for Continuos
              mode.
        """
        return self._one

    @property
    def three(self) -> PgBitThree:
        """Return the ``PG:BIT:THREE`` command.

        Description:
            - This command sets or queries the output value of Pattern Generator bit 3.

        Usage:
            - Using the ``.query()`` method will send the ``PG:BIT:THREE?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:BIT:THREE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PG:BIT:THREE value`` command.

        SCPI Syntax:
            ```
            - PG:BIT:THREE {HIGH|LOW|TOGGLE|HIGH_Z}
            - PG:BIT:THREE?
            ```

        Info:
            - ``LOW`` sets the Pattern Generator bit value to Low.
            - ``HIGH`` sets the Pattern Generator bit value to High.
            - ``TOGGLE`` sets the Pattern Generator bit value to Toggle.
            - ``HIGH_Z`` sets the Pattern Generator bit value to Hi-Z. Only available for Continuos
              mode.
        """
        return self._three

    @property
    def two(self) -> PgBitTwo:
        """Return the ``PG:BIT:TWO`` command.

        Description:
            - This command sets or queries the output value of Pattern Generator bit 2.

        Usage:
            - Using the ``.query()`` method will send the ``PG:BIT:TWO?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:BIT:TWO?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PG:BIT:TWO value`` command.

        SCPI Syntax:
            ```
            - PG:BIT:TWO {HIGH|LOW|TOGGLE|HIGH_Z}
            - PG:BIT:TWO?
            ```

        Info:
            - ``LOW`` sets the Pattern Generator bit value to Low.
            - ``HIGH`` sets the Pattern Generator bit value to High.
            - ``TOGGLE`` sets the Pattern Generator bit value to Toggle.
            - ``HIGH_Z`` sets the Pattern Generator bit value to Hi-Z. Only available for Continuos
              mode.
        """
        return self._two

    @property
    def zero(self) -> PgBitZero:
        """Return the ``PG:BIT:ZERO`` command.

        Description:
            - This command sets or queries the output value of Pattern Generator bit 0.

        Usage:
            - Using the ``.query()`` method will send the ``PG:BIT:ZERO?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:BIT:ZERO?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PG:BIT:ZERO value`` command.

        SCPI Syntax:
            ```
            - PG:BIT:ZERO {HIGH|LOW|TOGGLE|HIGH_Z}
            - PG:BIT:ZERO?
            ```

        Info:
            - ``LOW`` sets the Pattern Generator bit value to Low.
            - ``HIGH`` sets the Pattern Generator bit value to High.
            - ``TOGGLE`` sets the Pattern Generator bit value to Toggle.
            - ``HIGH_Z`` sets the Pattern Generator bit value to Hi-Z. Only available for Continuos
              mode.
        """
        return self._zero


class PgAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``PG:AMPlitude`` command.

    Description:
        - This command sets or queries the Pattern Generator output voltage. You can give any value,
          but the command will replace it with the nearest valid value (2.5, 3.3 and 5). In burst
          mode, only 5 V is supported.

    Usage:
        - Using the ``.query()`` method will send the ``PG:AMPlitude?`` query.
        - Using the ``.verify(value)`` method will send the ``PG:AMPlitude?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PG:AMPlitude value`` command.

    SCPI Syntax:
        ```
        - PG:AMPlitude {2.5|3.3|5V}
        - PG:AMPlitude?
        ```

    Info:
        - ``2.5`` sets the Pattern Generator amplitude to 2.5 V.
        - ``3.3`` sets the Pattern Generator amplitude to 3.3 V.
        - ``5`` sets the Pattern Generator amplitude to 5 V. This is the default value.
    """


class Pg(SCPICmdRead):
    """The ``PG`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PG?`` query.
        - Using the ``.verify(value)`` method will send the ``PG?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``PG:AMPlitude`` command.
        - ``.bit``: The ``PG:BIT`` command tree.
        - ``.bitrate``: The ``PG:BITRate`` command.
        - ``.burst``: The ``PG:BURSt`` command tree.
        - ``.file``: The ``PG:FILE`` command tree.
        - ``.output``: The ``PG:OUTPut`` command tree.
        - ``.patterndefinition``: The ``PG:PATTERNdefinition`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "PG") -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = PgAmplitude(device, f"{self._cmd_syntax}:AMPlitude")
        self._bit = PgBit(device, f"{self._cmd_syntax}:BIT")
        self._bitrate = PgBitrate(device, f"{self._cmd_syntax}:BITRate")
        self._burst = PgBurst(device, f"{self._cmd_syntax}:BURSt")
        self._file = PgFile(device, f"{self._cmd_syntax}:FILE")
        self._output = PgOutput(device, f"{self._cmd_syntax}:OUTPut")
        self._patterndefinition = PgPatterndefinition(
            device, f"{self._cmd_syntax}:PATTERNdefinition"
        )

    @property
    def amplitude(self) -> PgAmplitude:
        """Return the ``PG:AMPlitude`` command.

        Description:
            - This command sets or queries the Pattern Generator output voltage. You can give any
              value, but the command will replace it with the nearest valid value (2.5, 3.3 and 5).
              In burst mode, only 5 V is supported.

        Usage:
            - Using the ``.query()`` method will send the ``PG:AMPlitude?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:AMPlitude?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PG:AMPlitude value`` command.

        SCPI Syntax:
            ```
            - PG:AMPlitude {2.5|3.3|5V}
            - PG:AMPlitude?
            ```

        Info:
            - ``2.5`` sets the Pattern Generator amplitude to 2.5 V.
            - ``3.3`` sets the Pattern Generator amplitude to 3.3 V.
            - ``5`` sets the Pattern Generator amplitude to 5 V. This is the default value.
        """
        return self._amplitude

    @property
    def bit(self) -> PgBit:
        """Return the ``PG:BIT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PG:BIT?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:BIT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.one``: The ``PG:BIT:ONE`` command.
            - ``.three``: The ``PG:BIT:THREE`` command.
            - ``.two``: The ``PG:BIT:TWO`` command.
            - ``.zero``: The ``PG:BIT:ZERO`` command.
        """
        return self._bit

    @property
    def bitrate(self) -> PgBitrate:
        """Return the ``PG:BITRate`` command.

        Description:
            - This command sets or queries the bit rate of data in the Pattern Generator. You can
              give any value, but it will take nearest possible value and generate the pattern.

        Usage:
            - Using the ``.query()`` method will send the ``PG:BITRate?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:BITRate?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PG:BITRate value`` command.

        SCPI Syntax:
            ```
            - PG:BITRate <NR3>
            - PG:BITRate?
            ```

        Info:
            - ``<NR3>`` sets the Pattern Generator bit rate. The minimum bit rate is 1 b/s and
              maximum bit rate is 25 Mb/s. The default value is 125000 b/s.
        """
        return self._bitrate

    @property
    def burst(self) -> PgBurst:
        """Return the ``PG:BURSt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PG:BURSt?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:BURSt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ccount``: The ``PG:BURSt:CCOUnt`` command.
            - ``.trigger``: The ``PG:BURSt:TRIGger`` command.
        """
        return self._burst

    @property
    def file(self) -> PgFile:
        """Return the ``PG:FILE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PG:FILE?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:FILE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.pattern``: The ``PG:FILE:PATTern`` command.
        """
        return self._file

    @property
    def output(self) -> PgOutput:
        """Return the ``PG:OUTPut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PG:OUTPut?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:OUTPut?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``PG:OUTPut:MODe`` command.
        """
        return self._output

    @property
    def patterndefinition(self) -> PgPatterndefinition:
        """Return the ``PG:PATTERNdefinition`` command.

        Description:
            - This command sets or queries the Pattern Generator definition. If set to manual mode,
              you can configure the bit independently. If set to file mode, you can set a data file
              that will be loaded into memory and generated as a sequence.

        Usage:
            - Using the ``.query()`` method will send the ``PG:PATTERNdefinition?`` query.
            - Using the ``.verify(value)`` method will send the ``PG:PATTERNdefinition?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PG:PATTERNdefinition value``
              command.

        SCPI Syntax:
            ```
            - PG:PATTERNdefinition {MANual|FILE}
            - PG:PATTERNdefinition?
            ```

        Info:
            - ``MANual`` sets the pattern definition source to Manual. This is the default value.
            - ``FILE`` sets the pattern definition source to File.
        """
        return self._patterndefinition
