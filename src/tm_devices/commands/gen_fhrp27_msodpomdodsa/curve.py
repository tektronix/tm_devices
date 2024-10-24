"""The curve commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CURVe {<Block>|<asc curve>}
    - CURVe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Curve(SCPICmdWrite, SCPICmdRead):
    """The ``CURVe`` command.

    Description:
        - The ``CURVe`` command transfers the waveform data points the oscilloscope's internal
          reference memory location (REF1-4), which is specified by the to ``DATa:DESTination``
          command. The ``CURVe?`` query transfers data the oscilloscope; the source waveform is
          specified by the from ``DATa:SOUrce`` command. The first and last data points are
          specified by the ``DATa:STARt`` and ``DATa:STOP`` commands. Associated with each waveform
          transferred using the ``CURVe`` command or query is a waveform preamble that provides the
          data format, scale and associated information needed to interpret the waveform data
          points. The preamble information for waveforms sent the oscilloscope is specified using
          the to WFMInpre commands. The preamble information for waveforms transferred the
          oscilloscope is specified or queried using the from WFMOutpre commands. If the waveform is
          not displayed, the query form generates an error. The ``CURVe`` command and ``CURVe?``
          query transfer waveform data in ASCII or binary format. ASCII data is sent as a
          comma-separated list of decimal values. Binary data is sent with the IEEE488.2 binary
          block header immediately followed by the binary data. The IEEE488.2 binary block header is
          defined as follows: #N<N-digits> where: N is a single decimal or hexadecimal digit
          indicating the number of digits to follow. <N-digits> are the decimal digits representing
          the number of bytes in the data that immediately follows this binary block header. The
          Waveform Transfer command group text contains more comprehensive information.

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
        - ``<Block>`` is the waveform data in binary format. The waveform is formatted as follows.
        - ``<asc curve>`` is the waveform data in ASCII format. The format for ASCII data is
          <NR1>[,<NR1>..], where each <NR1> represents a data point. For RF frequency domain
          waveforms, the data is transmitted as 4-byte floating point values (NR2 or NR3).
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CURVe") -> None:
        super().__init__(device, cmd_syntax)
