# pylint: disable=line-too-long
"""The data commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DATa {INIT|SNAp}
    - DATa:DESTination REF<x>
    - DATa:DESTination?
    - DATa:ENCdg {ASCIi|FAStest|RIBinary|RPBinary|SRIbinary|SRPbinary|FPbinary|SFPbinary}
    - DATa:ENCdg?
    - DATa:SOUrce {CH<x>|MATH|REF<x>|D<x>|DIGital|RF_AMPlitude|RF_FREQuency|RF_PHASe|RF_NORMal|RF_AVErage|RF_MAXHold|RF_MINHold}
    - DATa:SOUrce?
    - DATa:STARt <NR1>
    - DATa:STARt?
    - DATa:STOP <NR1>
    - DATa:STOP?
    - DATa:WIDth <NR1>
    - DATa:WIDth?
    - DATa?
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DataWidth(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:WIDth`` command.

    Description:
        - This command specifies the width, in bytes per point, for waveform data transferred from
          the instrument via the CURVe? query. (This command is synonymous with
          ``WFMOutpre:BYT_Nr``.)

    Usage:
        - Using the ``.query()`` method will send the ``DATa:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:WIDth?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:WIDth value`` command.

    SCPI Syntax:
        ```
        - DATa:WIDth <NR1>
        - DATa:WIDth?
        ```

    Info:
        - ``<NR1>`` is an integer that indicates the number of bytes per point for the outgoing
          waveform data when queried using the CURVe? command.
    """


class DataStop(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:STOP`` command.

    Description:
        - This command sets or queries the last data point that will be transferred when using the
          CURVE? query. When using the CURVE command, ``DATa:STOP`` is ignored. This command allows
          for the transfer of partial waveforms to the controller. If <NR1> is greater than the
          record length, then data will be transferred up to the record length. If both
          ``DATa:STARt`` and ``DATa:STOP`` are greater than the record length, the last data point
          in the record is returned. ``DATa:STARt`` and ``DATa:STOP`` are order independent. When
          ``DATa:STOP`` is less than ``DATa:STARt``, the values will be swapped internally for the
          CURVE? query. If you always want to transfer complete waveforms, set ``DATa:STARt`` to 1
          and ``DATa:STOP`` to the maximum record length, or larger. Changes to the record length
          value are not automatically reflected in the ``DATa:STOP`` value. As record length is
          varied, the ``DATa:STOP`` value must be explicitly changed to ensure the entire record is
          transmitted. In other words, curve results will not automatically and correctly reflect
          increases in record length if the distance from ``DATa:STARt`` to ``DATa:STOP`` stays
          smaller than the increased record length.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:STOP?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:STOP?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:STOP value`` command.

    SCPI Syntax:
        ```
        - DATa:STOP <NR1>
        - DATa:STOP?
        ```

    Info:
        - ``<NR1>`` is the last data point that will be transferred, which ranges from 1 to the
          record length.
    """


class DataStart(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:STARt`` command.

    Description:
        - This command sets or queries the starting data point for waveform transfer. This command
          allows for the transfer of partial waveforms to and from the instrument. Data will be
          transferred from <NR1> to ``DATa:STOP`` or the record length, whichever is less. If <NR1>
          is greater than the record length, the last data point in the record is transferred.
          ``DATa:STARt`` and ``DATa:STOP`` are order independent. When ``DATa:STOP`` is greater than
          ``DATa:STARt``, the values will be swapped internally for the CURVE? query.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:STARt?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:STARt?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:STARt value`` command.

    SCPI Syntax:
        ```
        - DATa:STARt <NR1>
        - DATa:STARt?
        ```

    Info:
        - ``<NR1>`` is the first data point that will be transferred, which ranges from 1 to the
          record length.
    """


class DataSource(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:SOUrce`` command.

    Description:
        - This command specifies the source waveform to be transferred from the oscilloscope using
          the CURVe? query. The valid waveform sources are CH1-CH4, MATH, REF1-REF4, D0-D15,
          DIGital, ``RF_AMPlitude``, ``RF_FREQuency``, ``RF_PHASe``, ``RF_NORMal``, ``RF_AVErage``,
          ``RF_MAXHold``, and ``RF_MINHold``. Setting ``DATa:SOUrce`` automatically constrains the
          following to valid values for the specified source waveform: ``WFMOutpre:BYT_Nr``,
          ``WFMOutpre:BIT_Nr`` and ``WFMOutpre:BN_Fmt``.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:SOUrce value`` command.

    SCPI Syntax:
        ```
        - DATa:SOUrce {CH<x>|MATH|REF<x>|D<x>|DIGital|RF_AMPlitude|RF_FREQuency|RF_PHASe|RF_NORMal|RF_AVErage|RF_MAXHold|RF_MINHold}
        - DATa:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies which analog channel waveform data will be transferred from the
          oscilloscope to the controller, channels 1 through 4.
        - ``MATH`` specifies that the Math waveform data will be transferred from the oscilloscope
          to the controller.
        - ``REF<x>`` specifies which Reference waveform data will be transferred from the
          oscilloscope to the controller.
        - ``D<x>`` specifies which digital channel waveform data will be transferred from the
          oscilloscope to the controller. (Requires installation of option 3-MSO.).
        - ``DIGital`` specifies that the Digital Collection waveform data will be transferred from
          the oscilloscope to the controller. (Requires installation of option 3-MSO.).
        - ``RF_NORMal`` specify that the RF data will be transferred from the oscilloscope to the
          controller.
        - ``RF_AVErage`` specify that the RF data will be transferred from the oscilloscope to the
          controller.
        - ``RF_MAXHold`` specify that the RF data will be transferred from the oscilloscope to the
          controller.
        - ``RF_MINHold`` specify that the RF data will be transferred from the oscilloscope to the
          controller.
    """  # noqa: E501


class DataEncdg(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:ENCdg`` command.

    Description:
        - This command specifies the encoding format for outgoing waveform data. This command is
          equivalent to setting ``WFMOUTPRE:ENCDG``, ``WFMOUTPRE:BN_FMT``, and ``WFMOUTPRE:BYT_OR``.
          Setting the ``DATa:ENGdg`` value causes the corresponding WFMOutpre values to be updated.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:ENCdg?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:ENCdg?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:ENCdg value`` command.

    SCPI Syntax:
        ```
        - DATa:ENCdg {ASCIi|FAStest|RIBinary|RPBinary|SRIbinary|SRPbinary|FPbinary|SFPbinary}
        - DATa:ENCdg?
        ```

    Info:
        - ``ASCIi`` specifies to use ASCII encoding for the waveform data queried using the CURVe?
          query. Data values are returned as signed decimal integers for analog channel and RF time
          domain data, 4-byte floating point values for RF frequency domain data, or hexadecimal
          values for Digital Collection data with 4 or 8 bytes per point. The maximum number of
          ASCII data points that can be queried using the CURVe? query is 1 million points. If more
          than 1 million points are desired, you must use one of the binary encodings. If ASCII is
          the value, then ``BN_Fmt`` and ``BYT_Or`` are ignored.
        - ``FAStest`` specifies the encoding which results in the fastest waveform data transfer
          rate. This sets the following: ``WFMOutpre:ENCdg BINary``, ``WFMOutpre:BIN_Fmt RI`` and
          ``WFMOutpre:BYT_Or MSB``.
        - ``RIBinary`` specifies the signed integer data point format, with the most significant
          byte transferred first.
        - ``DATa:WIDTH`` is set to 1, the range is from -128 through 127. When ``DATa:WIDTH`` is 2,
          the range is from -32,768 through 32,768. Center screen is 0 (zero). The upper limit is
          the top of the screen and the lower limit is the bottom of the screen. The default
          encoding is RIBINARY. This sets the following: ``WFMOutpre:ENCdg BINary``,
          ``WFMOutpre:BN_Fmt RI`` and ``WFMOutpre:BYT_Or MSB``.
        - ``RPBinary`` specifies the positive integer data-point representation, with the most
          significant byte transferred first.
        - ``BYT_Nr`` is 1, the range of data values is 0 through 255. When ``BYT_Nr`` is 2, the
          range of data values is 0 to 65,535. The center of the screen is 127 for 1-byte data and
          is 32768 for 2-byte data. The upper limit is the top of the screen and the lower limit is
          the bottom of the screen. This sets the following:
          ``:WFMOutpre:ENCdg BINary``,``:WFMOutpre:BN_Fmt RP`` and ``WFMOutpre:BYT_Or MSB``.
        - ``SRIbinary`` specifies the signed integer format. It is the same as RIBinary except that
          the byte order is swapped, meaning that the least significant byte is transferred first.
          This sets the following: ``WFMOutpre:ENCdg BINary``, ``WFMOutpre:BIN_Fmt RI`` and
          ``WFMOutpre:BYT_Or LSB``.
        - ``SRPbinary`` specifies the positive integer format. It is the same as RPBinary except
          that the byte order is swapped, meaning that the least significant byte is transferred
          first. This sets the following: ``WFMOutpre:ENCdg BINary``, ``WFMOutpre:BN_Fmt RP`` and
          ``WFMOutpre:BYT_Or LSB``.
        - ``FPbinary`` specifies floating point binary. It automatically forces ``DATa:WIDTH`` to 4
          and ``BYT_OR`` to MSB (most significant byte transmitted first).
        - ``SFPbinary`` specifies floating point binary. It automatically forces ``DATa:WIDTH`` to 4
          and ``BYT_OR`` to LSB (least significant byte transmitted first).
    """


class DataDestination(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:DESTination`` command.

    Description:
        - This command specifies the reference memory location (REF1-4) for storing waveform data
          transferred into the oscilloscope using the CURVE command.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:DESTination?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:DESTination?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:DESTination value`` command.

    SCPI Syntax:
        ```
        - DATa:DESTination REF<x>
        - DATa:DESTination?
        ```

    Info:
        - ``REF<x>`` is the reference location where the waveform will be stored.
    """


class Data(SCPICmdWrite, SCPICmdRead):
    """The ``DATa`` command.

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
          waveform cursors are not on when the ``DATa SNAp`` command is sent, it is silently ignored
          and ``DATa:STARt`` and ``:STOP`` remain unchanged.

    Properties:
        - ``.destination``: The ``DATa:DESTination`` command.
        - ``.encdg``: The ``DATa:ENCdg`` command.
        - ``.source``: The ``DATa:SOUrce`` command.
        - ``.start``: The ``DATa:STARt`` command.
        - ``.stop``: The ``DATa:STOP`` command.
        - ``.width``: The ``DATa:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DATa") -> None:
        super().__init__(device, cmd_syntax)
        self._destination = DataDestination(device, f"{self._cmd_syntax}:DESTination")
        self._encdg = DataEncdg(device, f"{self._cmd_syntax}:ENCdg")
        self._source = DataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._start = DataStart(device, f"{self._cmd_syntax}:STARt")
        self._stop = DataStop(device, f"{self._cmd_syntax}:STOP")
        self._width = DataWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def destination(self) -> DataDestination:
        """Return the ``DATa:DESTination`` command.

        Description:
            - This command specifies the reference memory location (REF1-4) for storing waveform
              data transferred into the oscilloscope using the CURVE command.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:DESTination?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:DESTination?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:DESTination value`` command.

        SCPI Syntax:
            ```
            - DATa:DESTination REF<x>
            - DATa:DESTination?
            ```

        Info:
            - ``REF<x>`` is the reference location where the waveform will be stored.
        """
        return self._destination

    @property
    def encdg(self) -> DataEncdg:
        """Return the ``DATa:ENCdg`` command.

        Description:
            - This command specifies the encoding format for outgoing waveform data. This command is
              equivalent to setting ``WFMOUTPRE:ENCDG``, ``WFMOUTPRE:BN_FMT``, and
              ``WFMOUTPRE:BYT_OR``. Setting the ``DATa:ENGdg`` value causes the corresponding
              WFMOutpre values to be updated.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:ENCdg?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:ENCdg?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:ENCdg value`` command.

        SCPI Syntax:
            ```
            - DATa:ENCdg {ASCIi|FAStest|RIBinary|RPBinary|SRIbinary|SRPbinary|FPbinary|SFPbinary}
            - DATa:ENCdg?
            ```

        Info:
            - ``ASCIi`` specifies to use ASCII encoding for the waveform data queried using the
              CURVe? query. Data values are returned as signed decimal integers for analog channel
              and RF time domain data, 4-byte floating point values for RF frequency domain data, or
              hexadecimal values for Digital Collection data with 4 or 8 bytes per point. The
              maximum number of ASCII data points that can be queried using the CURVe? query is 1
              million points. If more than 1 million points are desired, you must use one of the
              binary encodings. If ASCII is the value, then ``BN_Fmt`` and ``BYT_Or`` are ignored.
            - ``FAStest`` specifies the encoding which results in the fastest waveform data transfer
              rate. This sets the following: ``WFMOutpre:ENCdg BINary``, ``WFMOutpre:BIN_Fmt RI``
              and ``WFMOutpre:BYT_Or MSB``.
            - ``RIBinary`` specifies the signed integer data point format, with the most significant
              byte transferred first.
            - ``DATa:WIDTH`` is set to 1, the range is from -128 through 127. When ``DATa:WIDTH`` is
              2, the range is from -32,768 through 32,768. Center screen is 0 (zero). The upper
              limit is the top of the screen and the lower limit is the bottom of the screen. The
              default encoding is RIBINARY. This sets the following: ``WFMOutpre:ENCdg BINary``,
              ``WFMOutpre:BN_Fmt RI`` and ``WFMOutpre:BYT_Or MSB``.
            - ``RPBinary`` specifies the positive integer data-point representation, with the most
              significant byte transferred first.
            - ``BYT_Nr`` is 1, the range of data values is 0 through 255. When ``BYT_Nr`` is 2, the
              range of data values is 0 to 65,535. The center of the screen is 127 for 1-byte data
              and is 32768 for 2-byte data. The upper limit is the top of the screen and the lower
              limit is the bottom of the screen. This sets the following:
              ``:WFMOutpre:ENCdg BINary``,``:WFMOutpre:BN_Fmt RP`` and ``WFMOutpre:BYT_Or MSB``.
            - ``SRIbinary`` specifies the signed integer format. It is the same as RIBinary except
              that the byte order is swapped, meaning that the least significant byte is transferred
              first. This sets the following: ``WFMOutpre:ENCdg BINary``, ``WFMOutpre:BIN_Fmt RI``
              and ``WFMOutpre:BYT_Or LSB``.
            - ``SRPbinary`` specifies the positive integer format. It is the same as RPBinary except
              that the byte order is swapped, meaning that the least significant byte is transferred
              first. This sets the following: ``WFMOutpre:ENCdg BINary``, ``WFMOutpre:BN_Fmt RP``
              and ``WFMOutpre:BYT_Or LSB``.
            - ``FPbinary`` specifies floating point binary. It automatically forces ``DATa:WIDTH``
              to 4 and ``BYT_OR`` to MSB (most significant byte transmitted first).
            - ``SFPbinary`` specifies floating point binary. It automatically forces ``DATa:WIDTH``
              to 4 and ``BYT_OR`` to LSB (least significant byte transmitted first).
        """
        return self._encdg

    @property
    def source(self) -> DataSource:
        """Return the ``DATa:SOUrce`` command.

        Description:
            - This command specifies the source waveform to be transferred from the oscilloscope
              using the CURVe? query. The valid waveform sources are CH1-CH4, MATH, REF1-REF4,
              D0-D15, DIGital, ``RF_AMPlitude``, ``RF_FREQuency``, ``RF_PHASe``, ``RF_NORMal``,
              ``RF_AVErage``, ``RF_MAXHold``, and ``RF_MINHold``. Setting ``DATa:SOUrce``
              automatically constrains the following to valid values for the specified source
              waveform: ``WFMOutpre:BYT_Nr``, ``WFMOutpre:BIT_Nr`` and ``WFMOutpre:BN_Fmt``.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:SOUrce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:SOUrce value`` command.

        SCPI Syntax:
            ```
            - DATa:SOUrce {CH<x>|MATH|REF<x>|D<x>|DIGital|RF_AMPlitude|RF_FREQuency|RF_PHASe|RF_NORMal|RF_AVErage|RF_MAXHold|RF_MINHold}
            - DATa:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies which analog channel waveform data will be transferred from the
              oscilloscope to the controller, channels 1 through 4.
            - ``MATH`` specifies that the Math waveform data will be transferred from the
              oscilloscope to the controller.
            - ``REF<x>`` specifies which Reference waveform data will be transferred from the
              oscilloscope to the controller.
            - ``D<x>`` specifies which digital channel waveform data will be transferred from the
              oscilloscope to the controller. (Requires installation of option 3-MSO.).
            - ``DIGital`` specifies that the Digital Collection waveform data will be transferred
              from the oscilloscope to the controller. (Requires installation of option 3-MSO.).
            - ``RF_NORMal`` specify that the RF data will be transferred from the oscilloscope to
              the controller.
            - ``RF_AVErage`` specify that the RF data will be transferred from the oscilloscope to
              the controller.
            - ``RF_MAXHold`` specify that the RF data will be transferred from the oscilloscope to
              the controller.
            - ``RF_MINHold`` specify that the RF data will be transferred from the oscilloscope to
              the controller.
        """  # noqa: E501
        return self._source

    @property
    def start(self) -> DataStart:
        """Return the ``DATa:STARt`` command.

        Description:
            - This command sets or queries the starting data point for waveform transfer. This
              command allows for the transfer of partial waveforms to and from the instrument. Data
              will be transferred from <NR1> to ``DATa:STOP`` or the record length, whichever is
              less. If <NR1> is greater than the record length, the last data point in the record is
              transferred. ``DATa:STARt`` and ``DATa:STOP`` are order independent. When
              ``DATa:STOP`` is greater than ``DATa:STARt``, the values will be swapped internally
              for the CURVE? query.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:STARt?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:STARt?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:STARt value`` command.

        SCPI Syntax:
            ```
            - DATa:STARt <NR1>
            - DATa:STARt?
            ```

        Info:
            - ``<NR1>`` is the first data point that will be transferred, which ranges from 1 to the
              record length.
        """
        return self._start

    @property
    def stop(self) -> DataStop:
        """Return the ``DATa:STOP`` command.

        Description:
            - This command sets or queries the last data point that will be transferred when using
              the CURVE? query. When using the CURVE command, ``DATa:STOP`` is ignored. This command
              allows for the transfer of partial waveforms to the controller. If <NR1> is greater
              than the record length, then data will be transferred up to the record length. If both
              ``DATa:STARt`` and ``DATa:STOP`` are greater than the record length, the last data
              point in the record is returned. ``DATa:STARt`` and ``DATa:STOP`` are order
              independent. When ``DATa:STOP`` is less than ``DATa:STARt``, the values will be
              swapped internally for the CURVE? query. If you always want to transfer complete
              waveforms, set ``DATa:STARt`` to 1 and ``DATa:STOP`` to the maximum record length, or
              larger. Changes to the record length value are not automatically reflected in the
              ``DATa:STOP`` value. As record length is varied, the ``DATa:STOP`` value must be
              explicitly changed to ensure the entire record is transmitted. In other words, curve
              results will not automatically and correctly reflect increases in record length if the
              distance from ``DATa:STARt`` to ``DATa:STOP`` stays smaller than the increased record
              length.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:STOP?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:STOP?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:STOP value`` command.

        SCPI Syntax:
            ```
            - DATa:STOP <NR1>
            - DATa:STOP?
            ```

        Info:
            - ``<NR1>`` is the last data point that will be transferred, which ranges from 1 to the
              record length.
        """
        return self._stop

    @property
    def width(self) -> DataWidth:
        """Return the ``DATa:WIDth`` command.

        Description:
            - This command specifies the width, in bytes per point, for waveform data transferred
              from the instrument via the CURVe? query. (This command is synonymous with
              ``WFMOutpre:BYT_Nr``.)

        Usage:
            - Using the ``.query()`` method will send the ``DATa:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:WIDth?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:WIDth value`` command.

        SCPI Syntax:
            ```
            - DATa:WIDth <NR1>
            - DATa:WIDth?
            ```

        Info:
            - ``<NR1>`` is an integer that indicates the number of bytes per point for the outgoing
              waveform data when queried using the CURVe? command.
        """
        return self._width
