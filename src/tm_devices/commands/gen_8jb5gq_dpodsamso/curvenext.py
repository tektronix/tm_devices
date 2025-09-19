"""The curvenext commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CURVENext?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Curvenext(SCPICmdRead):
    """The ``CURVENext`` command.

    Description:
        - This query-only command returns unique waveform data from the instrument. This query
          performs just like CURVE?, except multiple uses guarantee that the waveform returned is
          always a new acquisition since the previous CURVENEXT. Note that if the instrument is
          acquiring waveform records at a slow rate (high resolution mode), you must configure the
          controller for long timeout thresholds. Data will not be transferred until a new waveform
          is acquired since the previous ``:CURVENext?`` response.

    Usage:
        - Using the ``.query()`` method will send the ``CURVENext?`` query.
        - Using the ``.verify(value)`` method will send the ``CURVENext?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURVENext?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CURVENext") -> None:
        super().__init__(device, cmd_syntax)
