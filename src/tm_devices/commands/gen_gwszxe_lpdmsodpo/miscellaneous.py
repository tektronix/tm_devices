"""The miscellaneous commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *DDT {<Block>|<QString>}
    - *DDT?
    - *LRN?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Lrn(SCPICmdRead):
    """The ``*LRN`` command.

    Description:
        - This query-only command returns the commands that list the instrument settings, allowing
          you to record or 'learn' the current instrument settings. You can use these commands to
          return the instrument to the state it was in when you made the ``*LRN?`` query. This
          command is identical to the SET? command.

    Usage:
        - Using the ``.query()`` method will send the ``*LRN?`` query.
        - Using the ``.verify(value)`` method will send the ``*LRN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - *LRN?
        ```

    Info:
        - ``<QString>`` is the license nomenclature.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*LRN") -> None:
        super().__init__(device, cmd_syntax)


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

    Info:
        - ``<Block>`` is a complete sequence of program messages. The messages can contain only
          valid commands that must be separated by semicolons and must follow all rules for
          concatenating commands. The sequence must be less than or equal to 80characters. The
          format of this argument is always returned as a query.
        - ``<QString>`` is a complete sequence of program messages. The messages can contain only
          valid commands that must be separated by semicolons and must follow all rules for
          concatenating commands. The sequence must be less than or equal to 80 characters.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*DDT") -> None:
        super().__init__(device, cmd_syntax)
