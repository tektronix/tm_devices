"""The riddick_pi_manual commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *LRN?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Lrn(SCPICmdRead):
    """The ``*LRN`` command.

    Description:
        - This query-only command returns the commands that list the instrument settings, allowing
          you to record or “learn” the current instrument settings. You can use these commands to
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
