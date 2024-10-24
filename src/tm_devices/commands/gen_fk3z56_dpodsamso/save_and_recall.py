"""The save_and_recall commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *SDS <NR1>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Sds(SCPICmdWrite):
    """The ``*SDS`` command.

    Description:
        - This command (no query form) changes the specified setup to reference the factory setup
          instead of the specific user setup slot. The content of the setup slot is unchanged, but
          the data will no longer be accessible to you. This command is equivalent to selecting
          Delete from the File menu, and then choosing the specified setup.

    Usage:
        - Using the ``.write(value)`` method will send the ``*SDS value`` command.

    SCPI Syntax:
        ```
        - *SDS <NR1>
        ```

    Info:
        - ``<NR1>`` specifies a user setup location to delete. Setup storage location values range
          from 1 through 10; using an out-of-range value causes an error.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*SDS") -> None:
        super().__init__(device, cmd_syntax)
