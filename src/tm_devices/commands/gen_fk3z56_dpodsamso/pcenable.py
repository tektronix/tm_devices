"""The pcenable commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - PCENable OFF | ON
    - PCENable?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Pcenable(SCPICmdWrite, SCPICmdRead):
    """The ``PCENable`` command.

    Description:
        - Sets or queries the enable state of the User Preference Probe compensation.

    Usage:
        - Using the ``.query()`` method will send the ``PCENable?`` query.
        - Using the ``.verify(value)`` method will send the ``PCENable?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PCENable value`` command.

    SCPI Syntax:
        ```
        - PCENable OFF | ON
        - PCENable?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "PCENable") -> None:
        super().__init__(device, cmd_syntax)
