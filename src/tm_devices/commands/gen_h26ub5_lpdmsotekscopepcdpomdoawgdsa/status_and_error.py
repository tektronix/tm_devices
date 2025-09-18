"""The status_and_error commands module.

These commands are used in the following models:
AWG5200, AWG5K, AWG5KC, AWG70KA, AWG70KB, AWG7K, AWG7KC, DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K,
DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7AX, DPO7K, DPO7KC, DSA70KC, DSA70KD, LPD6, MDO3,
MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4B, MSO4K, MSO4KB, MSO5, MSO5B, MSO5K,
MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *SRE <NR1>
    - *SRE?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Sre(SCPICmdWrite, SCPICmdRead):
    """The ``*SRE`` command.

    Description:
        - The ``*SRE`` (Service Request Enable) command sets and queries the bits in the Service
          Request Enable Register. For more information, refer to Registers.

    Usage:
        - Using the ``.query()`` method will send the ``*SRE?`` query.
        - Using the ``.verify(value)`` method will send the ``*SRE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*SRE value`` command.

    SCPI Syntax:
        ```
        - *SRE <NR1>
        - *SRE?
        ```

    Info:
        - ``<NR1>`` is a value in the range from 0 through 255. The binary bits of the SRER are set
          according to this value. Using an out-of-range value causes an execution error. The
          power-on default for SRER is 0 if ``*PSC`` is 1. If ``*PSC`` is 0, the SRER maintains the
          previous power cycle value through the current power cycle.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*SRE") -> None:
        super().__init__(device, cmd_syntax)
