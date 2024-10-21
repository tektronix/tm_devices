"""The channelmapping commands module.

These commands are used in the following models:
DPO70KSX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CHANNELMAPping?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Channelmapping(SCPICmdRead):
    """The ``CHANNELMAPping`` command.

    Description:
        - This query returns a list of all channel mappings (such as, CH1.B2,CH2.A2,CH3.C2,CH4.D2).
          DPO70000SX Series only.

    Usage:
        - Using the ``.query()`` method will send the ``CHANNELMAPping?`` query.
        - Using the ``.verify(value)`` method will send the ``CHANNELMAPping?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CHANNELMAPping?
        ```
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "CHANNELMAPping"
    ) -> None:
        super().__init__(device, cmd_syntax)
