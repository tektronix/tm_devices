"""The data commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DATa {INIT|SNAp}
    - DATa:DESTination REF<x>
    - DATa:DESTination?
    - DATa:ENCdg {ASCIi|FAStest|RIBinary|RPBinary|FPBinary|SRIbinary|SRPbinary|SFPbinary}
    - DATa:ENCdg?
    - DATa:FRAMESTARt <NR1>
    - DATa:FRAMESTARt?
    - DATa:FRAMESTOP <NR1>
    - DATa:FRAMESTOP?
    - DATa:SOUrce <wfm>[<,><wfm>]
    - DATa:SOUrce?
    - DATa:STARt <NR1>
    - DATa:STARt?
    - DATa:STOP <NR1>
    - DATa:STOP?
    - DATa:SYNCSOUrces {ON|OFF|<NR1>}
    - DATa:SYNCSOUrces?
    - DATa?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DataSyncsources(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:SYNCSOUrces`` command.

    Description:
        - This command sets or queries if the data sync sources are on or off.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:SYNCSOUrces?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:SYNCSOUrces?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:SYNCSOUrces value`` command.

    SCPI Syntax:
        ```
        - DATa:SYNCSOUrces {ON|OFF|<NR1>}
        - DATa:SYNCSOUrces?
        ```

    Info:
        - ``NR1`` = 0 specifies that the data sync sources are not available; any other value
          specifies that the data sync sources are available.
        - ``OFF`` specifies that the data sync sources are not available.
        - ``ON`` specifies that the data sync sources are available.
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
        - This command sets or queries the location of waveform data that is transferred from the
          instrument by the CURVE Query.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:SOUrce value`` command.

    SCPI Syntax:
        ```
        - DATa:SOUrce <wfm>[<,><wfm>]
        - DATa:SOUrce?
        ```

    Info:
        - ``<wfm>`` is the location of the waveform data that will be transferred from the
          instrument to the controller. It can consist of CH<x>, MATH<x>, REF<x>, DIGITALALL. Note
          that digital data is transferred as 16-bit data, with the least-significant bit
          representing D0, and the most-significant bit representing D15.
        - ``<wfm>`` can consist of the following.
        - ``CH<x>`` selects the specified analog channel as the source.
        - ``MATH<x>`` selects the specified reference waveform as the source. The reference number
          is specified by x, which ranges from 1 through 4.
        - ``REF<x>`` selects the specified reference waveform as the source. The reference number is
          specified by x, which ranges from 1 through 8.
        - ``CH<x>_D<x>`` selects the specified digital channel.
        - ``CH<x>_DAll`` selects the specified channel group of digital channels.
        - ``DIGITALALL`` selects digital waveforms as the source. The Digital data is transferred as
          16-bit data, with the least-significant bit representing D0, and the most-significant bit
          representing D15. The LSB always contains D0-D7 and MSB always contains D8-D15 data.
        - ``CH<x>_SV_NORMal`` , ``CH<x>_SV_AVErage``, ``CH<x>_SV_MAX_Hold``, ``CH<x>_SV_MIN_Hold``
          selects the specified Spectrum View waveform.
        - ``CH<x>_MAG_VS_TIME`` , ``CH<x>_FREQ_VS_TIME``, ``CH<x>_PHASE_VS_TIME`` selects the
          specified RF vs. Time waveform.
        - ``CH<x>_SV_BASEBAND_IQ`` selects the specified RF baseband IQ data.
    """


class DataFramestop(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:FRAMESTOP`` command.

    Description:
        - This command sets or queries the ending data frame for waveform transfers. This command
          allows for transferring a subset of frames of a FastFrame waveform from the instrument
          (CURVe? query). Any value set by this command is ignored when transferring waveform data
          to the instrument (CURVe command).

    Usage:
        - Using the ``.query()`` method will send the ``DATa:FRAMESTOP?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:FRAMESTOP?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:FRAMESTOP value`` command.

    SCPI Syntax:
        ```
        - DATa:FRAMESTOP <NR1>
        - DATa:FRAMESTOP?
        ```

    Info:
        - ``<NR1>`` is the last data frame that is transferred, which ranges from 1 to the number of
          acquired frames. If <NR1> is greater than the number of acquired frames, then you will
          receive up to the number of acquired frames. If both.
        - ``DATA:FRAMESTART`` and ``DATA:FRAMESTOP`` are order independent. The smaller number is
          used as in CURVE and ``SAVE:WAVEFORM`` queries.
        - ``DATA:FRAMESTART`` to 1 and ``DATA:FRAMESTOP`` to the maximum number of acquired frames,
          or larger.
    """


class DataFramestart(SCPICmdWrite, SCPICmdRead):
    """The ``DATa:FRAMESTARt`` command.

    Description:
        - This command sets or queries the starting acquisition for waveform transfer using the
          CURVE? query. This is only relevant when History or FastFrame acquisition modes are
          enabled.

    Usage:
        - Using the ``.query()`` method will send the ``DATa:FRAMESTARt?`` query.
        - Using the ``.verify(value)`` method will send the ``DATa:FRAMESTARt?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATa:FRAMESTARt value`` command.

    SCPI Syntax:
        ```
        - DATa:FRAMESTARt <NR1>
        - DATa:FRAMESTARt?
        ```

    Info:
        - ``<NR1>`` is the first acquisition that will be transferred, which ranges from 1 to the
          number of History or FastFrame acquisitions. Results are transferred from acquisition
          <NR1> to ``DATa:FRAMESTOP`` or the total number of acquisitions, whichever is less. If
          <NR1> is greater than the number of acquisitions, then only the last acquisition is
          transferred. If ``DATa:FRAMESTARt`` is greater than ``DATa:FRAMESTOP``, then only a single
          acquisition at <NR1> is transferred.
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
        - DATa:ENCdg {ASCIi|FAStest|RIBinary|RPBinary|FPBinary|SRIbinary|SRPbinary|SFPbinary}
        - DATa:ENCdg?
        ```

    Info:
        - ``ASCIi`` specifies the ASCII representation of signed INT, FLOAT. If ASCII is the value,
          then ``:BN_Fmt`` and ``:BYT_Or`` are ignored.
        - ``FAStest`` specifies that the data be sent in the fastest possible manner consistent with
          maintaining accuracy and is interpreted with respect to the first waveform specified in
          the ``DATA:SOUrce`` list.
        - ``RIBinary`` specifies signed integer data point representation with the most significant
          byte transferred first.
        - ``RPBinary`` specifies the positive integer data-point representation, with the most
          significant byte transferred first.
        - ``FPBinary`` specifies the floating point (width = 4) data.
        - ``38`` to 3.4 × 1038. The center of the screen is 0. The upper limit is the top of the
          screen and the lower limit is the bottom of the screen.
        - ``FPBinary`` argument is only applicable to math waveforms or ref waveforms saved from
          math waveforms.
        - ``SRIbinary`` is the same as RIBinary except that the byte order is swapped, meaning that
          the least significant byte is transferred first. This format is useful when transferring
          data to IBM compatible PCs.
        - ``SRPbinary`` is the same as RPBinary except that the byte order is swapped, meaning that
          the least significant byte is transferred first. This format is useful when transferring
          data to PCs.
        - ``SFPbinary`` specifies floating point data in IBM PC format. The SFPbinary argument only
          works on math waveforms or ref waveforms saved from math waveforms.
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
        - ``.destination``: The ``DATa:DESTination`` command.
        - ``.encdg``: The ``DATa:ENCdg`` command.
        - ``.framestart``: The ``DATa:FRAMESTARt`` command.
        - ``.framestop``: The ``DATa:FRAMESTOP`` command.
        - ``.source``: The ``DATa:SOUrce`` command.
        - ``.start``: The ``DATa:STARt`` command.
        - ``.stop``: The ``DATa:STOP`` command.
        - ``.syncsources``: The ``DATa:SYNCSOUrces`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DATa") -> None:
        super().__init__(device, cmd_syntax)
        self._destination = DataDestination(device, f"{self._cmd_syntax}:DESTination")
        self._encdg = DataEncdg(device, f"{self._cmd_syntax}:ENCdg")
        self._framestart = DataFramestart(device, f"{self._cmd_syntax}:FRAMESTARt")
        self._framestop = DataFramestop(device, f"{self._cmd_syntax}:FRAMESTOP")
        self._source = DataSource(device, f"{self._cmd_syntax}:SOUrce")
        self._start = DataStart(device, f"{self._cmd_syntax}:STARt")
        self._stop = DataStop(device, f"{self._cmd_syntax}:STOP")
        self._syncsources = DataSyncsources(device, f"{self._cmd_syntax}:SYNCSOUrces")

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
            - DATa:ENCdg {ASCIi|FAStest|RIBinary|RPBinary|FPBinary|SRIbinary|SRPbinary|SFPbinary}
            - DATa:ENCdg?
            ```

        Info:
            - ``ASCIi`` specifies the ASCII representation of signed INT, FLOAT. If ASCII is the
              value, then ``:BN_Fmt`` and ``:BYT_Or`` are ignored.
            - ``FAStest`` specifies that the data be sent in the fastest possible manner consistent
              with maintaining accuracy and is interpreted with respect to the first waveform
              specified in the ``DATA:SOUrce`` list.
            - ``RIBinary`` specifies signed integer data point representation with the most
              significant byte transferred first.
            - ``RPBinary`` specifies the positive integer data-point representation, with the most
              significant byte transferred first.
            - ``FPBinary`` specifies the floating point (width = 4) data.
            - ``38`` to 3.4 × 1038. The center of the screen is 0. The upper limit is the top of the
              screen and the lower limit is the bottom of the screen.
            - ``FPBinary`` argument is only applicable to math waveforms or ref waveforms saved from
              math waveforms.
            - ``SRIbinary`` is the same as RIBinary except that the byte order is swapped, meaning
              that the least significant byte is transferred first. This format is useful when
              transferring data to IBM compatible PCs.
            - ``SRPbinary`` is the same as RPBinary except that the byte order is swapped, meaning
              that the least significant byte is transferred first. This format is useful when
              transferring data to PCs.
            - ``SFPbinary`` specifies floating point data in IBM PC format. The SFPbinary argument
              only works on math waveforms or ref waveforms saved from math waveforms.
        """
        return self._encdg

    @property
    def framestart(self) -> DataFramestart:
        """Return the ``DATa:FRAMESTARt`` command.

        Description:
            - This command sets or queries the starting acquisition for waveform transfer using the
              CURVE? query. This is only relevant when History or FastFrame acquisition modes are
              enabled.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:FRAMESTARt?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:FRAMESTARt?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:FRAMESTARt value`` command.

        SCPI Syntax:
            ```
            - DATa:FRAMESTARt <NR1>
            - DATa:FRAMESTARt?
            ```

        Info:
            - ``<NR1>`` is the first acquisition that will be transferred, which ranges from 1 to
              the number of History or FastFrame acquisitions. Results are transferred from
              acquisition <NR1> to ``DATa:FRAMESTOP`` or the total number of acquisitions, whichever
              is less. If <NR1> is greater than the number of acquisitions, then only the last
              acquisition is transferred. If ``DATa:FRAMESTARt`` is greater than ``DATa:FRAMESTOP``,
              then only a single acquisition at <NR1> is transferred.
        """
        return self._framestart

    @property
    def framestop(self) -> DataFramestop:
        """Return the ``DATa:FRAMESTOP`` command.

        Description:
            - This command sets or queries the ending data frame for waveform transfers. This
              command allows for transferring a subset of frames of a FastFrame waveform from the
              instrument (CURVe? query). Any value set by this command is ignored when transferring
              waveform data to the instrument (CURVe command).

        Usage:
            - Using the ``.query()`` method will send the ``DATa:FRAMESTOP?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:FRAMESTOP?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:FRAMESTOP value`` command.

        SCPI Syntax:
            ```
            - DATa:FRAMESTOP <NR1>
            - DATa:FRAMESTOP?
            ```

        Info:
            - ``<NR1>`` is the last data frame that is transferred, which ranges from 1 to the
              number of acquired frames. If <NR1> is greater than the number of acquired frames,
              then you will receive up to the number of acquired frames. If both.
            - ``DATA:FRAMESTART`` and ``DATA:FRAMESTOP`` are order independent. The smaller number
              is used as in CURVE and ``SAVE:WAVEFORM`` queries.
            - ``DATA:FRAMESTART`` to 1 and ``DATA:FRAMESTOP`` to the maximum number of acquired
              frames, or larger.
        """
        return self._framestop

    @property
    def source(self) -> DataSource:
        """Return the ``DATa:SOUrce`` command.

        Description:
            - This command sets or queries the location of waveform data that is transferred from
              the instrument by the CURVE Query.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:SOUrce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:SOUrce value`` command.

        SCPI Syntax:
            ```
            - DATa:SOUrce <wfm>[<,><wfm>]
            - DATa:SOUrce?
            ```

        Info:
            - ``<wfm>`` is the location of the waveform data that will be transferred from the
              instrument to the controller. It can consist of CH<x>, MATH<x>, REF<x>, DIGITALALL.
              Note that digital data is transferred as 16-bit data, with the least-significant bit
              representing D0, and the most-significant bit representing D15.
            - ``<wfm>`` can consist of the following.
            - ``CH<x>`` selects the specified analog channel as the source.
            - ``MATH<x>`` selects the specified reference waveform as the source. The reference
              number is specified by x, which ranges from 1 through 4.
            - ``REF<x>`` selects the specified reference waveform as the source. The reference
              number is specified by x, which ranges from 1 through 8.
            - ``CH<x>_D<x>`` selects the specified digital channel.
            - ``CH<x>_DAll`` selects the specified channel group of digital channels.
            - ``DIGITALALL`` selects digital waveforms as the source. The Digital data is
              transferred as 16-bit data, with the least-significant bit representing D0, and the
              most-significant bit representing D15. The LSB always contains D0-D7 and MSB always
              contains D8-D15 data.
            - ``CH<x>_SV_NORMal`` , ``CH<x>_SV_AVErage``, ``CH<x>_SV_MAX_Hold``,
              ``CH<x>_SV_MIN_Hold`` selects the specified Spectrum View waveform.
            - ``CH<x>_MAG_VS_TIME`` , ``CH<x>_FREQ_VS_TIME``, ``CH<x>_PHASE_VS_TIME`` selects the
              specified RF vs. Time waveform.
            - ``CH<x>_SV_BASEBAND_IQ`` selects the specified RF baseband IQ data.
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
    def syncsources(self) -> DataSyncsources:
        """Return the ``DATa:SYNCSOUrces`` command.

        Description:
            - This command sets or queries if the data sync sources are on or off.

        Usage:
            - Using the ``.query()`` method will send the ``DATa:SYNCSOUrces?`` query.
            - Using the ``.verify(value)`` method will send the ``DATa:SYNCSOUrces?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DATa:SYNCSOUrces value`` command.

        SCPI Syntax:
            ```
            - DATa:SYNCSOUrces {ON|OFF|<NR1>}
            - DATa:SYNCSOUrces?
            ```

        Info:
            - ``NR1`` = 0 specifies that the data sync sources are not available; any other value
              specifies that the data sync sources are available.
            - ``OFF`` specifies that the data sync sources are not available.
            - ``ON`` specifies that the data sync sources are available.
        """
        return self._syncsources
