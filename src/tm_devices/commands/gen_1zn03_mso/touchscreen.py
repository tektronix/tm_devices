"""The touchscreen commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TOUCHSCReen:STATe {0|1|OFF|ON}
    - TOUCHSCReen:STATe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class TouchscreenState(SCPICmdWrite, SCPICmdRead):
    """The ``TOUCHSCReen:STATe`` command.

    Description:
        - This sets or queries the enabled state of the touch screen only. This command is
          equivalent to pushing the Touch Off button on the front panel. To completely disable front
          panel operation, use the command LOCK ALL. To re-enable the front panel, send the command
          LOCK NONE.

    Usage:
        - Using the ``.query()`` method will send the ``TOUCHSCReen:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``TOUCHSCReen:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TOUCHSCReen:STATe value`` command.

    SCPI Syntax:
        ```
        - TOUCHSCReen:STATe {0|1|OFF|ON}
        - TOUCHSCReen:STATe?
        ```

    Info:
        - ``0`` disables the touch screen.
        - ``ON`` enables the touch screen.
        - ``OFF`` disables the touch screen.
    """


class Touchscreen(SCPICmdRead):
    """The ``TOUCHSCReen`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TOUCHSCReen?`` query.
        - Using the ``.verify(value)`` method will send the ``TOUCHSCReen?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``TOUCHSCReen:STATe`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "TOUCHSCReen"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._state = TouchscreenState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> TouchscreenState:
        """Return the ``TOUCHSCReen:STATe`` command.

        Description:
            - This sets or queries the enabled state of the touch screen only. This command is
              equivalent to pushing the Touch Off button on the front panel. To completely disable
              front panel operation, use the command LOCK ALL. To re-enable the front panel, send
              the command LOCK NONE.

        Usage:
            - Using the ``.query()`` method will send the ``TOUCHSCReen:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``TOUCHSCReen:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TOUCHSCReen:STATe value`` command.

        SCPI Syntax:
            ```
            - TOUCHSCReen:STATe {0|1|OFF|ON}
            - TOUCHSCReen:STATe?
            ```

        Info:
            - ``0`` disables the touch screen.
            - ``ON`` enables the touch screen.
            - ``OFF`` disables the touch screen.
        """
        return self._state
