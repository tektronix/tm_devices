"""The header commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, LPD6, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4B, MSO4K,
MSO4KB, MSO5, MSO5B, MSO5K, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX, TekScopePC

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
        - This command sets or queries the Response Header Enable State that causes the instrument
          to either include or omit headers on query responses. Whether the long or short form of
          header keywords and enumerations are returned is dependent upon the state of ``:VERBose``.

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
        - ``<NR1>`` = 0 sets the Response Header Enable State to false; any other value sets this
          state to true.
        - ``OFF`` sets the Response Header Enable State to false. This causes the instrument to omit
          headers on query responses, so that only the argument is returned.
        - ``ON`` sets the Response Header Enable State to true. This causes the instrument to
          include headers on applicable query responses. You can then use the query response as a
          command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "HEADer") -> None:
        super().__init__(device, cmd_syntax)
