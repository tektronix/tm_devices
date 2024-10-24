"""The password commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4B, MSO4K,
MSO4KB, MSO5, MSO5B, MSO5K, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - PASSWord <QString>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Password(SCPICmdWrite):
    """The ``PASSWord`` command.

    Description:
        - This command (no query form) enables the ``*PUD`` and NEWpass set commands. Sending
          ``PASSWord`` without any arguments disables these same commands. Once the password is
          successfully entered, the ``*PUD`` and NEWpass commands are enabled until the instrument
          is powered off, or until the FACtory command, the ``PASSWord`` command with no arguments,
          or the ``*RST`` command is issued. To change the password, you must first enter the valid
          password with the ``PASSWord`` command and then change to your new password with the
          NEWpass command. Remember that the password is case sensitive.

    Usage:
        - Using the ``.write(value)`` method will send the ``PASSWord value`` command.

    SCPI Syntax:
        ```
        - PASSWord <QString>
        ```

    Info:
        - ``<QString>`` is the password, which can contain up to 10 characters. The factory default
          password is 'XYZZY' and is always valid.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "PASSWord") -> None:
        super().__init__(device, cmd_syntax)
