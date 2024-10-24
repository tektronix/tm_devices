"""The miscellaneous commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC, AWG5200, AWG5K, AWG5KC, AWG70KA, AWG70KB, AWG7K, AWG7KC, DPO2K, DPO2KB,
DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD,
LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4B, MSO4K, MSO4KB, MSO5,
MSO5B, MSO5K, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *TRG
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Trg(SCPICmdWriteNoArguments):
    """The ``*TRG`` command.

    Description:
        - Performs a group execute trigger on commands defined by ``*DDT``.

    Usage:
        - Using the ``.write()`` method will send the ``*TRG`` command.

    SCPI Syntax:
        ```
        - *TRG
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*TRG") -> None:
        super().__init__(device, cmd_syntax)
