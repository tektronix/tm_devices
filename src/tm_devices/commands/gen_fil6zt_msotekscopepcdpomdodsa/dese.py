"""The dese commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4K, MSO4KB, MSO5K,
MSO5KB, MSO70KC, MSO70KDX, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DESE <NR1>
    - DESE?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Dese(SCPICmdWrite, SCPICmdRead):
    """The ``DESE`` command.

    Description:
        - This command sets and queries the bits in the Device Event Status Enable Register (DESER).
          The DESER is the mask that determines whether events are reported to the Standard Event
          Status Register (SESR), and entered into the Event Queue. For a more detailed discussion
          of the use of these registers, see Registers.

    Usage:
        - Using the ``.query()`` method will send the ``DESE?`` query.
        - Using the ``.verify(value)`` method will send the ``DESE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DESE value`` command.

    SCPI Syntax:
        ```
        - DESE <NR1>
        - DESE?
        ```

    Info:
        - ``<NR1>`` The binary bits of the DESER are set according to this value, which ranges from
          1 through 255. For example, ``DESE 209`` sets the DESER to the binary value 11010001 (that
          is, the most significant bit in the register is set to 1, the next most significant bit to
          1, the next bit to 0, etc.).
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DESE") -> None:
        super().__init__(device, cmd_syntax)
