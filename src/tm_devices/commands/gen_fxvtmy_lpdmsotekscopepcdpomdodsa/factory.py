"""The factory commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4B, MSO4K,
MSO4KB, MSO5, MSO5B, MSO5K, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX, TekScopePC

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
          Resets the following IEEE488.2 registers: ``*ESE 0`` (Event Status Enable Register)
          ``*SRE 0`` (Service Request Enable Register) DESE 255 (Device Event Status Enable
          Register) ``*PSC 1`` (Power-on Status Clear Flag) Deletes all defined aliases. Enables
          command headers (``:HEADer 1``).

    Usage:
        - Using the ``.write()`` method will send the ``FACtory`` command.

    SCPI Syntax:
        ```
        - FACtory
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "FACtory") -> None:
        super().__init__(device, cmd_syntax)
