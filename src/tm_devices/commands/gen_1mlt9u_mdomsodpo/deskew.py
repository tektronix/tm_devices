"""The deskew commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DESkew {SETALLtorec}
    - DESkew:DISPlay {OFF|ON|0|1}
    - DESkew:DISPlay?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DeskewDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``DESkew:DISPlay`` command.

    Description:
        - This command specifies the state of the deskew table display.

    Usage:
        - Using the ``.query()`` method will send the ``DESkew:DISPlay?`` query.
        - Using the ``.verify(value)`` method will send the ``DESkew:DISPlay?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DESkew:DISPlay value`` command.

    SCPI Syntax:
        ```
        - DESkew:DISPlay {OFF|ON|0|1}
        - DESkew:DISPlay?
        ```

    Info:
        - ``OFF`` or 0 turns off the deskew table display.
        - ``ON`` or 1 turns on the deskew table display.
    """


class Deskew(SCPICmdWrite, SCPICmdRead):
    """The ``DESkew`` command.

    Description:
        - Causes the deskew values for all channels to be set to the recommended values. Equivalent
          to pressing the 'Set all deskews to recommended values' button in the application UI.

    Usage:
        - Using the ``.write(value)`` method will send the ``DESkew value`` command.

    SCPI Syntax:
        ```
        - DESkew {SETALLtorec}
        ```

    Info:
        - ``<SETALLtorec>`` sets the deskew for all channels to the recommended values.

    Properties:
        - ``.display``: The ``DESkew:DISPlay`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DESkew") -> None:
        super().__init__(device, cmd_syntax)
        self._display = DeskewDisplay(device, f"{self._cmd_syntax}:DISPlay")

    @property
    def display(self) -> DeskewDisplay:
        """Return the ``DESkew:DISPlay`` command.

        Description:
            - This command specifies the state of the deskew table display.

        Usage:
            - Using the ``.query()`` method will send the ``DESkew:DISPlay?`` query.
            - Using the ``.verify(value)`` method will send the ``DESkew:DISPlay?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DESkew:DISPlay value`` command.

        SCPI Syntax:
            ```
            - DESkew:DISPlay {OFF|ON|0|1}
            - DESkew:DISPlay?
            ```

        Info:
            - ``OFF`` or 0 turns off the deskew table display.
            - ``ON`` or 1 turns on the deskew table display.
        """
        return self._display
