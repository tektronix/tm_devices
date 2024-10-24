"""The curve commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CURVe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Curve(SCPICmdRead):
    """The ``CURVe`` command.

    Description:
        - This command transfers waveform data from the instrument. Each waveform that is
          transferred has an associated waveform preamble that contains information such as data
          format and scale. The ``CURVe?`` query transfers data from the instrument. The data source
          is specified by the ``DATA:SOURCE`` command. The first and last data points are specified
          by the ``DATA:START`` and ``DATA:STOP`` commands. For digital sources, ``CH<x>_D<x>`` or
          CH<x> _DALL, when the ``:DATa:WIDth`` is 1, the returned data is state only. When the
          ``:DATa:WIDth`` is 2, the returned data is transition data with 2 bits per digital channel
          representing the transition information as follows: 0 0 low 0 1 high 1 1 multiple
          transitions in interval ending with high 1 0 multiple transitions in interval ending with
          low For individual digital channels (such as ``CH<x>_D<x>`` ), ``:DATa:WIDth 2`` provides
          the 2-bit transition data with the upper 14 bits zero. ``:DATa:WIDth 1`` provides only the
          state in the LSB with the upper 7 bits all zero. For ``CH<x>_DAll`` sources,
          ``:DATa:WIDth 2`` provides the 2-bit transition data for each of the 8 constituent
          channels with the D7 bit represented in the 2 most significant bits, D6 in the next 2, and
          so on. ``:DATa:WIDth 1`` provides the states of each of the 8 constituent channels with D7
          represented in the most significant bit and D0 in the least significant bit. Depending on
          the sample rate, multi-transition data may not be available and ``:CURVe?`` queries for
          digital channels with ``:DATa:WIDth 2`` may result in a warning event 'Execution warning:
          Multi-transition data not available'. In this case, the transition data returned will be 0
          0 or 0 1. For MATH sources, only 8-byte double precision floating point data is returned
          in ``:CURVe?`` queries. A Fast Acquisition waveform Pixmap data is a 500 (vertical) by
          1000 (horizontal) point bitmap. Each point represents display intensity for that screen
          location. 500 (vertical) which is the row count in the bitmap, might vary based on how
          many channels enabled from same FastAcq group. To query and get the Fast Acq Pixel Map
          data, the following command set should be sent: ``ACQuire:FASTAcq:STATE ON``
          ``DATA:MODe PIXmap`` When the FastAcq is on, Curve? on Ch<x> will return pixmap data (if
          ``DATA:MODe`` is PIXmap). The number of rows in the pixmap will vary based on how many
          ch<x> sources are turned on and how they are grouped in acquisition HW. The grouping can
          vary from model to model. The number of columns in pixmap data is fixed to 1000. For
          example, on a MSO58 instrument, Ch1 to Ch4 is 'group1' and Ch5 to Ch8 is 'group2'. If Ch1
          is turned on (in group1) then Ch1 rows will be 500. If Ch2 and Ch3 are turned on (in
          group1) then Ch2 and Ch3 rows will be 250 each. When all Ch1/2/3/4 are turned on (in
          group1) then 125 rows per channel. If Ch1 (in group1) and Ch8 (in group2) are turned on
          then 500 rows will be returned for each channel. To calculate the number of rows, you can
          use- (number of bytes from curve header/``BYT_NR``)/1000.

    Usage:
        - Using the ``.query()`` method will send the ``CURVe?`` query.
        - Using the ``.verify(value)`` method will send the ``CURVe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURVe?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CURVe") -> None:
        super().__init__(device, cmd_syntax)
