"""The header commands module.

These commands are used in the following models:
MDO3

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HEADer {ON|OFF|<NR1>}
    - HEADer?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Header(SCPICmdWrite, SCPICmdRead):
    """The ``HEADer`` command.

    Description:
        - This command specifies the Response Header Enable State that causes the oscilloscope to
          either include or omit headers on query responses.

    Usage:
        - Using the ``.query()`` method will send the ``HEADer?`` query.
        - Using the ``.verify(value)`` method will send the ``HEADer?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HEADer value`` command.

    SCPI Syntax:
        ```
        - HEADer {ON|OFF|<NR1>}
        - HEADer?
        ```

    Info:
        - ``OFF`` sets the Response Header Enable State to false. This causes the oscilloscope to
          omit headers on query responses, so that only the argument is returned.
        - ``ON`` sets the Response Header Enable State to true. This causes the oscilloscope to
          include headers on applicable query responses. You can then use the query response as a
          command.
        - ``<NR1>`` = 0 sets the Response Header Enable State to false; any other value sets this
          state to true.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "HEADer") -> None:
        super().__init__(device, cmd_syntax)
