"""The miscellaneous commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4B, MSO4K,
MSO4KB, MSO5, MSO5B, MSO5K, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *DDT {<Block>|<QString>}
    - *DDT?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Ddt(SCPICmdWrite, SCPICmdRead):
    """The ``*DDT`` command.

    Description:
        - This command allows you to specify a command or a list of commands that are executed when
          the instrument receives a TRG command. Define Device Trigger ( ``*DDT`` ) is a special
          alias that the ``*TRG`` command uses.

    Usage:
        - Using the ``.query()`` method will send the ``*DDT?`` query.
        - Using the ``.verify(value)`` method will send the ``*DDT?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*DDT value`` command.

    SCPI Syntax:
        ```
        - *DDT {<Block>|<QString>}
        - *DDT?
        ```

    Info:
        - ``<Block>`` is a complete sequence of program messages. The messages can contain only
          valid commands that must be separated by semicolons and must follow all rules for
          concatenating commands. The sequence must be less than or equal to 80 characters. The
          format of this argument is always returned as a query.
        - ``<QString>`` is a complete sequence of program messages. The messages can contain only
          valid commands that must be separated by semicolons and must follow all rules for
          concatenating commands. The sequence must be less than or equal to 80 characters.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*DDT") -> None:
        super().__init__(device, cmd_syntax)
