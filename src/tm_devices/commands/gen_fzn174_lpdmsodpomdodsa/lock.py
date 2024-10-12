"""The lock commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, LPD6, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4B, MSO4K,
MSO4KB, MSO5, MSO5B, MSO5K, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - LOCk {ALL|NONe}
    - LOCk?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Lock(SCPICmdWrite, SCPICmdRead):
    """The ``LOCk`` command.

    Description:
        - This command enables or disables the touch screen and all front panel buttons and knobs.
          There is no front panel equivalent. When the front panel is locked, the front panel
          commands will not work and will not generate error events. You can work around a locked
          front panel, by using the appropriate programmatic interface commands, instead of the
          front-panel commands. For example, to set the trigger level to 50%, you could use
          ``TRIGger:A SETLevel``. To force a trigger, you could use TRIGger FORCe.

    Usage:
        - Using the ``.query()`` method will send the ``LOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``LOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LOCk value`` command.

    SCPI Syntax:
        ```
        - LOCk {ALL|NONe}
        - LOCk?
        ```

    Info:
        - ``ALL`` disables all front panel controls and the touch screen.
        - ``NONe`` enables all front panel controls and the touch screen. The UNLock ALL command
          only unlocks the front panel controls.
        - ``NONe`` command has no effect. For more information, see the ANSI/IEEE Std 488.1-1987
          Standard Digital Interface for Programmable Instrumentation, section 2.8.3 on RL State
          Descriptions.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "LOCk") -> None:
        super().__init__(device, cmd_syntax)
