"""The data commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DATa {INIT|SNAp}
    - DATa:COMPosition {COMPOSITE_YT|COMPOSITE_ENV|SINGULAR_YT}
    - DATa:COMPosition:AVAILable?
    - DATa:COMPosition?
    - DATa:DESTination REF<x>
    - DATa:DESTination?
    - DATa:ENCdg {ASCIi|FAStest|RIBinary|RPBinary|SRIbinary|SRPbinary}
    - DATa:ENCdg?
    - DATa:RESOlution {FULL|REDUced}
    - DATa:RESOlution?
    - DATa:SOUrce {CH<x>|MATH|REF<x>|D<x>}
    - DATa:SOUrce?
    - DATa:STARt <NR1>
    - DATa:STARt?
    - DATa:STOP <NR1>
    - DATa:STOP?
    - DATa:WIDth <NR1>
    - DATa:WIDth?
    - DATa?
    ```
"""

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
        - Sets or returns the location of the waveform data transferred from the oscilloscope by the
          CURVE? query.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:SOUrce value`` command.

    SCPI Syntax:
        ```
        - DATa:SOUrce {CH<x>|MATH|REF<x>|D<x>}
        - DATa:SOUrce?
        ```

    Info:
        - ``CH<x>`` specifies which analog channel data will be transferred from the oscilloscope to
          the controller, channels 1 through 4. x has a minimum of 1 and a maximum of 4.
        - ``MATH`` specifies that the Math waveform data will be transferred from the oscilloscope
          to the controller.
        - ``REF<x>`` specifies which Reference waveform data will be transferred from the
          oscilloscope to the controller, waveforms, 1 through 4. x has a minimum of 1 and a maximum
          of 2.
        - ``D<x>`` specifies that the returned waveform data is packaged as 4 bytes per sample,
          representing the states of all digital channels (D0-D15) and the logic states of the
          analog channels (Ch1-Ch4). When the ``:DATA:SOURCE`` is set to DIGITAL, the
          ``:DATA:WIDTH`` is automatically set to 4. x has a minimum of 0 and a maximum of 15.
    """


class DataResolution(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:RESOlution`` command.

    Description:
        - Sets or returns whether the CURVE? query returns full resolution records (acquired data)
          or reduced resolution records (filtered/displayed data).

    Usage:
        - Using the ``.query()`` method will send the ``DATa:RESOlution?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:RESOlution?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:RESOlution value`` command.

    SCPI Syntax:
        ```
        - DATa:RESOlution {FULL|REDUced}
        - DATa:RESOlution?
        ```

    Info:
        - ``FULL`` sets the instrument to return the full undecimated record acquired by the
          instrument. The full resolution records are not subject to the effects of FilterVu. Full
          resolution record lengths are 100,000, 125,000, 1,000,000 or 1,250,000 points.
        - ``REDUced`` sets the instrument to return short waveforms that are decimated from the full
          acquisition record. Reduced records are subject to the low pass filtering effects of
          FilterVu settings. Reduced record lengths range from 800 to 6250 points, depending on the
          acquisition settings.
    """


class DataEncdg(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:ENCdg`` command.

    Description:
        - Sets or returns the format of outgoing waveform data. This command is equivalent to
          setting ``WFMOUTPRE:ENCDG``, ``WFMOUTPRE:BN_FMT``, ``andWFMINPRE:FILTERFREQ``. Setting the
          ``DATa:ENGdg`` value causes the corresponding WFMOutpre values to be updated and
          conversely.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:ENCdg?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:ENCdg?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:ENCdg value`` command.

    SCPI Syntax:
        ```
        - DATa:ENCdg {ASCIi|FAStest|RIBinary|RPBinary|SRIbinary|SRPbinary}
        - DATa:ENCdg?
        ```

    Info:
        - ``ASCIi`` specifies the ASCII representation for waveform data points. If ASCII is the
          value, then ``:BN_Fmt`` and ``:BYT_Or`` are ignored.
        - ``FAStest`` specifies that the data be sent in the fastest possible manner consistent with
          maintaining accuracy and is interpreted with respect to the waveform specified by
          ``DATA:SOURCE``.
        - ``RIBinary`` specifies signed integer data point representation with the most significant
          byte transferred first.
        - ``RPBinary`` specifies the positive integer data-point representation, with the most
          significant byte transferred first.
        - ``SRIbinary`` is the same as RIBinary except that the byte order is swapped, meaning that
          the least significant byte is transferred first. This format is useful when transferring
          data to IBM compatible PCs.
        - ``SRPbinary`` is the same as RPBinary except that the byte order is swapped, meaning that
          the least significant byte is transferred first. This format is useful when transferring
          data to PCs.
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


class DataCompositionAvailable(SCPICmdRead):
    """The ``DATa:COMPosition:AVAILable`` command.

    Description:
        - Lists the waveform data types that are available for return from the instrument under the
          current instrument settings.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:COMPosition:AVAILable?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:COMPosition:AVAILable?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DATa:COMPosition:AVAILable?
        ```
    """


class DataComposition(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:COMPosition`` command.

    Description:
        - Sets or returns the type of data that the CURVE? query returns.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:COMPosition?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:COMPosition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:COMPosition value`` command.

    SCPI Syntax:
        ```
        - DATa:COMPosition {COMPOSITE_YT|COMPOSITE_ENV|SINGULAR_YT}
        - DATa:COMPosition?
        ```

    Info:
        - ``COMPOSITE_YT`` is of native width 8-bits and is written as 8-bit data in ISF files and
          REF waveforms. The data can be queried as 1- or 2-byte data in CURVE? queries by setting
          the data width to 1 or 2.
        - ``COMPOSITE_ENV`` is min/max pair data. Its native width is 8-bits and is written as 8-bit
          data in ISF files and REF waveforms. The data can be queried as 1- or 2- byte data in
          CURVE? queries by setting the data width to 1 or 2.
        - ``SINGULAR_YT`` is 16-bit data which originates as averaged acquired data or math data. It
          is written to ISF files and REF waveforms as 16-bit data. The data can be queried as 1- or
          2- byte data in CURVE? queries by setting the data width to 1 or 2.

    Properties:
        - ``.available``: The ``DATa:COMPosition:AVAILable`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._available = DataCompositionAvailable(device, f"{self._cmd_syntax}:AVAILable")

    @property
    def available(self) -> DataCompositionAvailable:
        """Return the ``DATa:COMPosition:AVAILable`` command.

        Description:
            - Lists the waveform data types that are available for return from the instrument under
              the current instrument settings.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:COMPosition:AVAILable?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:COMPosition:AVAILable?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DATa:COMPosition:AVAILable?
            ```
        """
        return self._available


#  pylint: disable=too-many-instance-attributes
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
        - ``.composition``: The ``DATa:COMPosition`` command.
        - ``.destination``: The ``DATa:DESTination`` command.
        - ``.encdg``: The ``DATa:ENCdg`` command.
        - ``.resolution``: The ``DATa:RESOlution`` command.
        - ``.source``: The ``DATa:SOUrce`` command.
        - ``.start``: The ``DATa:STARt`` command.
        - ``.stop``: The ``DATa:STOP`` command.
        - ``.width``: The ``DATa:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DATa") -> None:
        super().__init__(device, cmd_syntax)
        self._composition = DataComposition(device, f"{self._cmd_syntax}:COMPosition")
        self._destination = DataDestination(device, f"{self._cmd_syntax}:DESTination")
        self._encdg = DataEncdg(device, f"{self._cmd_syntax}:ENCdg")
        self._resolution = DataResolution(device, f"{self._cmd_syntax}:RESOlution")
        self._source = DataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._start = DataStart(device, f"{self._cmd_syntax}:STARt")
        self._stop = DataStop(device, f"{self._cmd_syntax}:STOP")
        self._width = DataWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def composition(self) -> DataComposition:
        """Return the ``DATa:COMPosition`` command.

        Description:
            - Sets or returns the type of data that the CURVE? query returns.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:COMPosition?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:COMPosition?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:COMPosition value`` command.

        SCPI Syntax:
            ```
            - DATa:COMPosition {COMPOSITE_YT|COMPOSITE_ENV|SINGULAR_YT}
            - DATa:COMPosition?
            ```

        Info:
            - ``COMPOSITE_YT`` is of native width 8-bits and is written as 8-bit data in ISF files
              and REF waveforms. The data can be queried as 1- or 2-byte data in CURVE? queries by
              setting the data width to 1 or 2.
            - ``COMPOSITE_ENV`` is min/max pair data. Its native width is 8-bits and is written as
              8-bit data in ISF files and REF waveforms. The data can be queried as 1- or 2- byte
              data in CURVE? queries by setting the data width to 1 or 2.
            - ``SINGULAR_YT`` is 16-bit data which originates as averaged acquired data or math
              data. It is written to ISF files and REF waveforms as 16-bit data. The data can be
              queried as 1- or 2- byte data in CURVE? queries by setting the data width to 1 or 2.

        Sub-properties:
            - ``.available``: The ``DATa:COMPosition:AVAILable`` command.
        """
        return self._composition

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
            - Sets or returns the format of outgoing waveform data. This command is equivalent to
              setting ``WFMOUTPRE:ENCDG``, ``WFMOUTPRE:BN_FMT``, ``andWFMINPRE:FILTERFREQ``. Setting
              the ``DATa:ENGdg`` value causes the corresponding WFMOutpre values to be updated and
              conversely.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:ENCdg?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:ENCdg?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:ENCdg value`` command.

        SCPI Syntax:
            ```
            - DATa:ENCdg {ASCIi|FAStest|RIBinary|RPBinary|SRIbinary|SRPbinary}
            - DATa:ENCdg?
            ```

        Info:
            - ``ASCIi`` specifies the ASCII representation for waveform data points. If ASCII is the
              value, then ``:BN_Fmt`` and ``:BYT_Or`` are ignored.
            - ``FAStest`` specifies that the data be sent in the fastest possible manner consistent
              with maintaining accuracy and is interpreted with respect to the waveform specified by
              ``DATA:SOURCE``.
            - ``RIBinary`` specifies signed integer data point representation with the most
              significant byte transferred first.
            - ``RPBinary`` specifies the positive integer data-point representation, with the most
              significant byte transferred first.
            - ``SRIbinary`` is the same as RIBinary except that the byte order is swapped, meaning
              that the least significant byte is transferred first. This format is useful when
              transferring data to IBM compatible PCs.
            - ``SRPbinary`` is the same as RPBinary except that the byte order is swapped, meaning
              that the least significant byte is transferred first. This format is useful when
              transferring data to PCs.
        """
        return self._encdg

    @property
    def resolution(self) -> DataResolution:
        """Return the ``DATa:RESOlution`` command.

        Description:
            - Sets or returns whether the CURVE? query returns full resolution records (acquired
              data) or reduced resolution records (filtered/displayed data).

        Usage:
            - Using the ``.query()`` method will send the ``DATa:RESOlution?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:RESOlution?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:RESOlution value`` command.

        SCPI Syntax:
            ```
            - DATa:RESOlution {FULL|REDUced}
            - DATa:RESOlution?
            ```

        Info:
            - ``FULL`` sets the instrument to return the full undecimated record acquired by the
              instrument. The full resolution records are not subject to the effects of FilterVu.
              Full resolution record lengths are 100,000, 125,000, 1,000,000 or 1,250,000 points.
            - ``REDUced`` sets the instrument to return short waveforms that are decimated from the
              full acquisition record. Reduced records are subject to the low pass filtering effects
              of FilterVu settings. Reduced record lengths range from 800 to 6250 points, depending
              on the acquisition settings.
        """
        return self._resolution

    @property
    def source(self) -> DataSource:
        """Return the ``DATa:SOUrce`` command.

        Description:
            - Sets or returns the location of the waveform data transferred from the oscilloscope by
              the CURVE? query.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:SOUrce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:SOUrce value`` command.

        SCPI Syntax:
            ```
            - DATa:SOUrce {CH<x>|MATH|REF<x>|D<x>}
            - DATa:SOUrce?
            ```

        Info:
            - ``CH<x>`` specifies which analog channel data will be transferred from the
              oscilloscope to the controller, channels 1 through 4. x has a minimum of 1 and a
              maximum of 4.
            - ``MATH`` specifies that the Math waveform data will be transferred from the
              oscilloscope to the controller.
            - ``REF<x>`` specifies which Reference waveform data will be transferred from the
              oscilloscope to the controller, waveforms, 1 through 4. x has a minimum of 1 and a
              maximum of 2.
            - ``D<x>`` specifies that the returned waveform data is packaged as 4 bytes per sample,
              representing the states of all digital channels (D0-D15) and the logic states of the
              analog channels (Ch1-Ch4). When the ``:DATA:SOURCE`` is set to DIGITAL, the
              ``:DATA:WIDTH`` is automatically set to 4. x has a minimum of 0 and a maximum of 15.
        """
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
