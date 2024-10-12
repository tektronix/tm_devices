"""The save_and_recall commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *RCL <NR1>
    - *SAV <NR1>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Sav(SCPICmdWrite):
    """The ``*SAV`` command.

    Description:
        - Stores the state of the oscilloscope to a specified memory location. You can use the
          ``*RCL`` command to restore the oscilloscope to this saved state at a later time.

    Usage:
        - Using the ``.write(value)`` method will send the ``*SAV value`` command.

    SCPI Syntax:
        ```
        - *SAV <NR1>
        ```

    Info:
        - ``<NR1>`` specifies a location in which to save the state of the oscilloscope. Location
          values range from 1 through 10. Using an out-of-range location value causes an execution
          error. Any settings that have been stored previously at this location will be overwritten.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*SAV") -> None:
        super().__init__(device, cmd_syntax)


class Rcl(SCPICmdWrite):
    """The ``*RCL`` command.

    Description:
        - This command restores the state of the oscilloscope from a copy of the settings stored in
          memory (The settings are stored using the ``*SAV`` command).

    Usage:
        - Using the ``.write(value)`` method will send the ``*RCL value`` command.

    SCPI Syntax:
        ```
        - *RCL <NR1>
        ```

    Info:
        - ``<NR1>`` is a value in the range from 1 to 10, which specifies a saved setup storage
          location.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*RCL") -> None:
        super().__init__(device, cmd_syntax)
