"""The miscellaneous commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

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
          the instrument receives a ``*TRG`` command. Define Device Trigger (``*DDT``) is a special
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
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*DDT") -> None:
        super().__init__(device, cmd_syntax)
