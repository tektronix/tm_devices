"""The curvestream commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CURVEStream?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Curvestream(SCPICmdRead):
    """The ``CURVEStream`` command.

    Description:
        - This query-only command continuously transfers waveform data from the instrument as it is
          acquired. This command puts the instrument into a streaming data mode, allowing the
          controller to receive waveform records as fast as they are acquired. Use the
          ``DATA:SOURCE`` command to specify the waveform sources. The command supports all the same
          data formatting options as the CURVE command. Control of the instrument through the user
          interface or other external clients is not allowed while in streaming data mode. The GPIB
          controller must take the instrument out of this streaming data mode to terminate the query
          and allow other input sources to resume communication with the instrument. The following
          options are available to transition out of streaming data mode: Send a device clear over
          the bus Send another command or query to the instrument Turning the waveform screen
          display mode off ( ``:DISplay:WAVEform OFF`` ) may increase waveform throughput during
          streaming mode. Using a data encoding of SRIbinary ( ``DATa:ENCdg SRIbinary`` ) may also
          increase the waveform throughput since that is the raw native data format of the
          oscilloscope. While in streaming data mode, two extreme conditions can occur. If the
          waveform records are being acquired slowly (high resolution), configure the controller for
          a long time-out threshold, as the data is not sent out until each complete record is
          acquired. If the waveform records are being acquired rapidly (low resolution), and the
          controller is not reading the data off the bus fast enough, the trigger rate is slowed to
          allow each waveform to be sent sequentially.

    Usage:
        - Using the ``.query()`` method will send the ``CURVEStream?`` query.
        - Using the ``.verify(value)`` method will send the ``CURVEStream?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURVEStream?
        ```
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "CURVEStream"
    ) -> None:
        super().__init__(device, cmd_syntax)
