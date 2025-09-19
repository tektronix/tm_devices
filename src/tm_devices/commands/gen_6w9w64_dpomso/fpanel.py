"""The fpanel commands module.

These commands are used in the following models:
DPO5KB, MSO5KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FPANel:PRESS <menuoff>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class FpanelPress(SCPICmdWrite):
    """The ``FPANel:PRESS`` command.

    Description:
        - This command turns off the displayed menu. It turns off everything except warning
          messages.

    Usage:
        - Using the ``.write(value)`` method will send the ``FPANel:PRESS value`` command.

    SCPI Syntax:
        ```
        - FPANel:PRESS <menuoff>
        ```

    Info:
        - ``menuoff`` turns off the menu.
    """


class Fpanel(SCPICmdRead):
    """The ``FPANel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FPANel?`` query.
        - Using the ``.verify(value)`` method will send the ``FPANel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.press``: The ``FPANel:PRESS`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "FPANel") -> None:
        super().__init__(device, cmd_syntax)
        self._press = FpanelPress(device, f"{self._cmd_syntax}:PRESS")

    @property
    def press(self) -> FpanelPress:
        """Return the ``FPANel:PRESS`` command.

        Description:
            - This command turns off the displayed menu. It turns off everything except warning
              messages.

        Usage:
            - Using the ``.write(value)`` method will send the ``FPANel:PRESS value`` command.

        SCPI Syntax:
            ```
            - FPANel:PRESS <menuoff>
            ```

        Info:
            - ``menuoff`` turns off the menu.
        """
        return self._press
