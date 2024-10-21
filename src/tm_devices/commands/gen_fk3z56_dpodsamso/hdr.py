"""The hdr commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HDR {ON|OFF|<NR1>}
    - HDR?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Hdr(SCPICmdWrite, SCPICmdRead):
    """The ``HDR`` command.

    Description:
        - This command is identical to the HEADer query and is included for backward compatibility
          purposes.

    Usage:
        - Using the ``.query()`` method will send the ``HDR?`` query.
        - Using the ``.verify(value)`` method will send the ``HDR?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HDR value`` command.

    SCPI Syntax:
        ```
        - HDR {ON|OFF|<NR1>}
        - HDR?
        ```

    Info:
        - ``<NR1>`` = 0 sets the Response Header Enable State to false; any other value sets this
          state to true, which causes the instrument to send headers on query responses.
        - ``OFF`` sets the Response Header Enable State to false. This causes the instrument to omit
          headers on query responses, so that only the argument is returned.
        - ``ON`` sets the Response Header Enable State to true. This causes the instrument to
          include headers on applicable query responses. You can then use the query response as a
          command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "HDR") -> None:
        super().__init__(device, cmd_syntax)
