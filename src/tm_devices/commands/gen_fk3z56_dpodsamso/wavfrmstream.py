"""The wavfrmstream commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - WAVFRMStream?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Wavfrmstream(SCPICmdRead):
    """The ``WAVFRMStream`` command.

    Description:
        - This query only command returns WFMQUTPRE? and CURVESTREAM? data for the waveforms
          specified by the DATASOURCE command. This command is similar to sending both WFMOUTPRE?
          and CURVESTREAM?, with the additional provision that each CURVESTREAM response to WAVFRMS?
          has a WFMOUTPRE response prepended to it. This helps guarantee a continuous synchronized
          preamble and curve.

    Usage:
        - Using the ``.query()`` method will send the ``WAVFRMStream?`` query.
        - Using the ``.verify(value)`` method will send the ``WAVFRMStream?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WAVFRMStream?
        ```
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "WAVFRMStream"
    ) -> None:
        super().__init__(device, cmd_syntax)
