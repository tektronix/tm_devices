"""The factory commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FACtory
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Factory(SCPICmdWriteNoArguments):
    """The ``FACtory`` command.

    Description:
        - This command (no query form) resets the instrument to its factory default settings. This
          command is equivalent to pressing the DEFAULT SETUP button located on the instrument front
          panel or selecting Default Setup from the File menu. This command Performs the following
          in addition to what is done for the ``*RST`` command: Clears any pending OPC operations.
          Resets the following IEEE488.2 registers: ``*ESE0`` (Event Status Enable Register)
          ``*SRE 0`` (Service Request Enable Register) DESE255 (Device Event Status Enable Register)
          ``*PSC1`` (Power-on Status Clear Flag) Deletes all defined aliases. Enables command
          headers (``:HEADer 1``).

    Usage:
        - Using the ``.write()`` method will send the ``FACtory`` command.

    SCPI Syntax:
        ```
        - FACtory
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "FACtory") -> None:
        super().__init__(device, cmd_syntax)
