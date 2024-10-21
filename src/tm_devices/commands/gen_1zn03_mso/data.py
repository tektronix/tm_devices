"""The data commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DATa {INIT|SNAp}
    - DATa:ENCdg {ASCIi|RIBinary|RPBinary|FPBinary|SRIbinary|SRPbinary|SFPbinary}
    - DATa:ENCdg?
    - DATa:MODe {VECtor|PIXmap}
    - DATa:MODe?
    - DATa:RESample <NR1>
    - DATa:RESample?
    - DATa:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
    - DATa:SOUrce:AVAILable?
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


class DataSourceAvailable(SCPICmdRead):
    """The ``DATa:SOUrce:AVAILable`` command.

    Description:
        - This query returns a list of enumerations representing the source waveforms that are
          currently available for ``:CURVe?`` queries. This means that the waveforms have been
          acquired. If there are none, NONE is returned.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:SOUrce:AVAILable?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:SOUrce:AVAILable?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DATa:SOUrce:AVAILable?
        ```
    """


class DataSource(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:SOUrce`` command.

    Description:
        - This command sets or queries the location of waveform data that is transferred from the
          instrument by the CURVE query.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:SOUrce value`` command.

    SCPI Syntax:
        ```
        - DATa:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
        - DATa:SOUrce?
        ```

    Info:
        - ``CH<x>`` selects the specified analog channel as the source.
        - ``DCH<x>_D<x>`` specifies the digital channel as the source. The supported digital channel
          value is 1. The supported digital bit values are 0 to 15 and ALL (all digital bits).
        - ``MATH<x>`` selects the specified reference waveform as the source. The reference number
          is specified by x, which ranges from 1 through 4.
        - ``REF<x>`` selects the specified reference waveform as the source. The reference number is
          specified by x, which ranges from 1 through 8.

    Properties:
        - ``.available``: The ``DATa:SOUrce:AVAILable`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._available = DataSourceAvailable(device, f"{self._cmd_syntax}:AVAILable")

    @property
    def available(self) -> DataSourceAvailable:
        """Return the ``DATa:SOUrce:AVAILable`` command.

        Description:
            - This query returns a list of enumerations representing the source waveforms that are
              currently available for ``:CURVe?`` queries. This means that the waveforms have been
              acquired. If there are none, NONE is returned.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:SOUrce:AVAILable?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:SOUrce:AVAILable?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DATa:SOUrce:AVAILable?
            ```
        """
        return self._available


class DataResample(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:RESample`` command.

    Description:
        - This command sets or queries the resampling of outgoing waveform data. This command is
          equivalent to setting ``WFMOutpre:RESample``. Setting the ``DATa:RESample`` value causes
          the corresponding WFMOutpre value to be updated and vice versa.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:RESample?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:RESample?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:RESample value`` command.

    SCPI Syntax:
        ```
        - DATa:RESample <NR1>
        - DATa:RESample?
        ```

    Info:
        - ``<NR1>`` is the resampling rate. The default value is 1, which means every sample is
          returned. A value of 2 returns every other sample, while a value of 3 returns every third
          sample, and so on.
    """


class DataMode(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:MODe`` command.

    Description:
        - This command sets or queries the mode for waveform data sent to returned by CURVe?. When
          FastAcq mode is ON, and the value is PIXmap, it returns Fast Acquisition pixmap data or
          the vector data is returned. When the data mode is set as VECtor then you get the waveform
          sampled data. The Data width is reset to 1 or 2 instead of 4.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:MODe value`` command.

    SCPI Syntax:
        ```
        - DATa:MODe {VECtor|PIXmap}
        - DATa:MODe?
        ```

    Info:
        - ``VECtor`` sets the mode for waveform data to vector.
        - ``PIXmap`` sets the mode for waveform data to pixmap.
    """


class DataEncdg(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:ENCdg`` command.

    Description:
        - This command sets or queries the format of outgoing waveform data. This command is
          equivalent to setting ``WFMOUTPRE:ENCDG``, ``WFMOUTPRE:BN_FMT``, and ``WFMOUTPRE:BYT_OR``.
          Setting the ``DATa:ENGdg`` value causes the corresponding WFMOutpre values to be updated
          and vice versa.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:ENCdg?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:ENCdg?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:ENCdg value`` command.

    SCPI Syntax:
        ```
        - DATa:ENCdg {ASCIi|RIBinary|RPBinary|FPBinary|SRIbinary|SRPbinary|SFPbinary}
        - DATa:ENCdg?
        ```

    Info:
        - ``ASCIi`` specifies the ASCII representation of signed INT, FLOAT. If ASCII is the value,
          then ``:BN_Fmt`` and ``:BYT_Or`` are ignored. The following are the DATa and WFMOutpre
          parameter settings (separated by semicolons): ``:ENCdg`` = ASC ; ``:BN_Fmt`` = N/A ;
          ``:BYT_Or`` = N/A ; ``:BYT_NR`` = 1,2,4.
        - ``RIBinary`` specifies the positive integer data-point representation, with the most
          significant byte transferred first. When ``:BYT_Nr`` is 1, the range from 0 through 255.
          When ``:BYT_Nr`` is 2,the range is from 0 to 65,535. When ``:BYT_Nr`` is 4, then the
          waveform being queried would return Fast Acquisition Pixmap data (if fast acq is turned on
          and data mode is set to pixmap). The following are the DATa and WFMOutpre parameter
          settings (separated by semicolons): ``:ENCdg`` = BIN ; ``:BN_Fmt`` = RI ; ``:BYT_Or`` =
          MSB ; ``:BYT_NR`` = 1,2.
        - ``RPBinary`` specifies the positive integer data-point representation, with the most
          significant byte transferred first. When ``:BYT_Nr`` is 1, the range from 0 through 255.
          When ``:BYT_Nr`` is 2, the range is from 0 to 65,535. The following are the DATa and
          WFMOutpre parameter settings (separated by semicolons): ``:ENCdg`` = ASC ; ``:BN_Fmt`` =
          RP ; ``:BYT_Or`` = MSB ; ``:BYT_NR`` = 1,2.
        - ``FPBinary`` specifies the floating point (width = 4) data. The range is from -3.4 × 1038
          to 3.4 × 1038. The center of the screen is 0. The upper limit is the top of the screen and
          the lower limit is the bottom of the screen. The FPBinary argument is only applicable to
          math waveforms or ref waveforms saved from math waveforms. The following are the DATa and
          WFMOutpre parameter settings (separated by semicolons): ``:ENCdg`` = BIN ; ``:BN_Fmt`` =
          FP ; ``:BYT_Or`` = MSB ; ``:BYT_NR`` = 4.
        - ``SRIbinary`` is the same as RIBinary except that the byte order is swapped, meaning that
          the least significant byte is transferred first. This format is useful when transferring
          data to IBM compatible PCs. The following are the DATa and WFMOutpre parameter settings
          (separated by semicolons): ``:ENCdg`` = BIN ; ``:BN_Fmt`` = RI ; ``:BYT_Or`` = LSB ;
          ``:BYT_NR`` = 1,2.
        - ``SRPbinary`` is the same as RPBinary except that the byte order is swapped, meaning that
          the least significant byte is transferred first. This format is useful when transferring
          data to PCs. The following are the DATa and WFMOutpre parameter settings (separated by
          semicolons): ``:ENCdg`` = BIN ; ``:BN_Fmt`` = RP ; ``:BYT_Or`` = LSB ; ``:BYT_NR`` = 1,2.
        - ``SFPbinary`` specifies floating point data in IBM PC format. The SFPbinary argument only
          works on math waveforms or ref waveforms saved from math waveforms. The following are the
          DATa and WFMOutpre parameter settings (separated by semicolons): ``:ENCdg`` = BIN ;
          ``:BN_Fmt`` = FP ; ``:BYT_Or`` = LSB ; ``:BYT_NR`` = 4.
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
        - ``.encdg``: The ``DATa:ENCdg`` command.
        - ``.mode``: The ``DATa:MODe`` command.
        - ``.resample``: The ``DATa:RESample`` command.
        - ``.source``: The ``DATa:SOUrce`` command.
        - ``.start``: The ``DATa:STARt`` command.
        - ``.stop``: The ``DATa:STOP`` command.
        - ``.width``: The ``DATa:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DATa") -> None:
        super().__init__(device, cmd_syntax)
        self._encdg = DataEncdg(device, f"{self._cmd_syntax}:ENCdg")
        self._mode = DataMode(device, f"{self._cmd_syntax}:MODe")
        self._resample = DataResample(device, f"{self._cmd_syntax}:RESample")
        self._source = DataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._start = DataStart(device, f"{self._cmd_syntax}:STARt")
        self._stop = DataStop(device, f"{self._cmd_syntax}:STOP")
        self._width = DataWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def encdg(self) -> DataEncdg:
        """Return the ``DATa:ENCdg`` command.

        Description:
            - This command sets or queries the format of outgoing waveform data. This command is
              equivalent to setting ``WFMOUTPRE:ENCDG``, ``WFMOUTPRE:BN_FMT``, and
              ``WFMOUTPRE:BYT_OR``. Setting the ``DATa:ENGdg`` value causes the corresponding
              WFMOutpre values to be updated and vice versa.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:ENCdg?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:ENCdg?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:ENCdg value`` command.

        SCPI Syntax:
            ```
            - DATa:ENCdg {ASCIi|RIBinary|RPBinary|FPBinary|SRIbinary|SRPbinary|SFPbinary}
            - DATa:ENCdg?
            ```

        Info:
            - ``ASCIi`` specifies the ASCII representation of signed INT, FLOAT. If ASCII is the
              value, then ``:BN_Fmt`` and ``:BYT_Or`` are ignored. The following are the DATa and
              WFMOutpre parameter settings (separated by semicolons): ``:ENCdg`` = ASC ; ``:BN_Fmt``
              = N/A ; ``:BYT_Or`` = N/A ; ``:BYT_NR`` = 1,2,4.
            - ``RIBinary`` specifies the positive integer data-point representation, with the most
              significant byte transferred first. When ``:BYT_Nr`` is 1, the range from 0 through
              255. When ``:BYT_Nr`` is 2,the range is from 0 to 65,535. When ``:BYT_Nr`` is 4, then
              the waveform being queried would return Fast Acquisition Pixmap data (if fast acq is
              turned on and data mode is set to pixmap). The following are the DATa and WFMOutpre
              parameter settings (separated by semicolons): ``:ENCdg`` = BIN ; ``:BN_Fmt`` = RI ;
              ``:BYT_Or`` = MSB ; ``:BYT_NR`` = 1,2.
            - ``RPBinary`` specifies the positive integer data-point representation, with the most
              significant byte transferred first. When ``:BYT_Nr`` is 1, the range from 0 through
              255. When ``:BYT_Nr`` is 2, the range is from 0 to 65,535. The following are the DATa
              and WFMOutpre parameter settings (separated by semicolons): ``:ENCdg`` = ASC ;
              ``:BN_Fmt`` = RP ; ``:BYT_Or`` = MSB ; ``:BYT_NR`` = 1,2.
            - ``FPBinary`` specifies the floating point (width = 4) data. The range is from -3.4 ×
              1038 to 3.4 × 1038. The center of the screen is 0. The upper limit is the top of the
              screen and the lower limit is the bottom of the screen. The FPBinary argument is only
              applicable to math waveforms or ref waveforms saved from math waveforms. The following
              are the DATa and WFMOutpre parameter settings (separated by semicolons): ``:ENCdg`` =
              BIN ; ``:BN_Fmt`` = FP ; ``:BYT_Or`` = MSB ; ``:BYT_NR`` = 4.
            - ``SRIbinary`` is the same as RIBinary except that the byte order is swapped, meaning
              that the least significant byte is transferred first. This format is useful when
              transferring data to IBM compatible PCs. The following are the DATa and WFMOutpre
              parameter settings (separated by semicolons): ``:ENCdg`` = BIN ; ``:BN_Fmt`` = RI ;
              ``:BYT_Or`` = LSB ; ``:BYT_NR`` = 1,2.
            - ``SRPbinary`` is the same as RPBinary except that the byte order is swapped, meaning
              that the least significant byte is transferred first. This format is useful when
              transferring data to PCs. The following are the DATa and WFMOutpre parameter settings
              (separated by semicolons): ``:ENCdg`` = BIN ; ``:BN_Fmt`` = RP ; ``:BYT_Or`` = LSB ;
              ``:BYT_NR`` = 1,2.
            - ``SFPbinary`` specifies floating point data in IBM PC format. The SFPbinary argument
              only works on math waveforms or ref waveforms saved from math waveforms. The following
              are the DATa and WFMOutpre parameter settings (separated by semicolons): ``:ENCdg`` =
              BIN ; ``:BN_Fmt`` = FP ; ``:BYT_Or`` = LSB ; ``:BYT_NR`` = 4.
        """
        return self._encdg

    @property
    def mode(self) -> DataMode:
        """Return the ``DATa:MODe`` command.

        Description:
            - This command sets or queries the mode for waveform data sent to returned by CURVe?.
              When FastAcq mode is ON, and the value is PIXmap, it returns Fast Acquisition pixmap
              data or the vector data is returned. When the data mode is set as VECtor then you get
              the waveform sampled data. The Data width is reset to 1 or 2 instead of 4.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:MODe value`` command.

        SCPI Syntax:
            ```
            - DATa:MODe {VECtor|PIXmap}
            - DATa:MODe?
            ```

        Info:
            - ``VECtor`` sets the mode for waveform data to vector.
            - ``PIXmap`` sets the mode for waveform data to pixmap.
        """
        return self._mode

    @property
    def resample(self) -> DataResample:
        """Return the ``DATa:RESample`` command.

        Description:
            - This command sets or queries the resampling of outgoing waveform data. This command is
              equivalent to setting ``WFMOutpre:RESample``. Setting the ``DATa:RESample`` value
              causes the corresponding WFMOutpre value to be updated and vice versa.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:RESample?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:RESample?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:RESample value`` command.

        SCPI Syntax:
            ```
            - DATa:RESample <NR1>
            - DATa:RESample?
            ```

        Info:
            - ``<NR1>`` is the resampling rate. The default value is 1, which means every sample is
              returned. A value of 2 returns every other sample, while a value of 3 returns every
              third sample, and so on.
        """
        return self._resample

    @property
    def source(self) -> DataSource:
        """Return the ``DATa:SOUrce`` command.

        Description:
            - This command sets or queries the location of waveform data that is transferred from
              the instrument by the CURVE query.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:SOUrce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:SOUrce value`` command.

        SCPI Syntax:
            ```
            - DATa:SOUrce {CH<x>|DCH<x>_D<x>|MATH<x>|REF<x>}
            - DATa:SOUrce?
            ```

        Info:
            - ``CH<x>`` selects the specified analog channel as the source.
            - ``DCH<x>_D<x>`` specifies the digital channel as the source. The supported digital
              channel value is 1. The supported digital bit values are 0 to 15 and ALL (all digital
              bits).
            - ``MATH<x>`` selects the specified reference waveform as the source. The reference
              number is specified by x, which ranges from 1 through 4.
            - ``REF<x>`` selects the specified reference waveform as the source. The reference
              number is specified by x, which ranges from 1 through 8.

        Sub-properties:
            - ``.available``: The ``DATa:SOUrce:AVAILable`` command.
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
