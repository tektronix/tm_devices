"""The status_and_error commands module.

These commands are used in the following models:
AWG5200, AWG5K, AWG5KC, AWG70KA, AWG70KB, AWG7K, AWG7KC, DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K,
DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MDO3, MDO3K, MDO4K,
MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4K, MSO4KB, MSO5K, MSO5KB, MSO70KC, MSO70KDX, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *ESE <NR1>
    - *ESE?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Ese(SCPICmdWrite, SCPICmdRead):
    """The ``*ESE`` command.

    Description:
        - This command sets and queries the bits in the Event Status Enable Register (ESER). The
          ESER prevents events from being reported to the Status Byte Register (STB). For a more
          detailed discussion of the use of these registers, see Registers.

    Usage:
        - Using the ``.query()`` method will send the ``*ESE?`` query.
        - Using the ``.verify(value)`` method will send the ``*ESE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*ESE value`` command.

    SCPI Syntax:
        ```
        - *ESE <NR1>
        - *ESE?
        ```

    Info:
        - ``<NR1>`` specifies the binary bits of the ESER according to this value, which ranges from
          0 through 255.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*ESE") -> None:
        super().__init__(device, cmd_syntax)
