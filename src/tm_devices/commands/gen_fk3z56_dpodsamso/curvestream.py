"""The curvestream commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CURVEStream {<Block>|<asc curve>}
    - CURVEStream?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Curvestream(SCPICmdWrite, SCPICmdRead):
    """The ``CURVEStream`` command.

    Description:
        - This query continuously transfers waveform data from the instrument as it is acquired.
          This command puts the instrument into a talk-only mode, allowing the controller to receive
          waveform records as fast as (and as soon as) they are acquired. Use the ``DATA:SOURCE``
          command to specify the waveform sources. The command does the same thing as the CURVE
          command. Control of the instrument through the user interface or other external client is
          not possible while in streaming mode. The GPIB controller must take the instrument out of
          this continuous talking mode to terminate the query and allow other input sources to
          resume communication with the instrument. The following options are available to
          transition out of streaming curve mode: send a device clear over the bus or send another
          query to the instrument (a MEPE Query Interrupted error will occur, but the instrument
          will be placed back into its normal talk/listen mode). Turning the waveform screen display
          mode off (``:DISPLAY:WAVEFORM OFF``) will increase waveform throughput during streaming
          mode. While in streaming mode, two extreme conditions can occur. If the waveform records
          are being acquired slowly (high resolution), configure the controller for long time-out
          thresholds, as the data is not sent out until each complete record is acquired. If the
          waveform records are being acquired rapidly (low resolution), and the controller is not
          reading the data off the bus fast enough, the trigger rate is slowed to allow each
          waveform to be sent sequentially.

    Usage:
        - Using the ``.query()`` method will send the ``CURVEStream?`` query.
        - Using the ``.verify(value)`` method will send the ``CURVEStream?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CURVEStream value`` command.

    SCPI Syntax:
        ```
        - CURVEStream {<Block>|<asc curve>}
        - CURVEStream?
        ```
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "CURVEStream"
    ) -> None:
        super().__init__(device, cmd_syntax)
