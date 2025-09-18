"""The dese commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

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
          of the use of these registers, see Registers. Note: Setting the DESER and ESER to the same
          value allows only those codes to be entered into the Event Queue and summarized on the ESB
          bit (bit 5) of the Status Byte Register. Use the ``*ESE`` command to set the ESER.

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
        - ``DESER`` is all bits set if ``*PSC`` is 1. If ``*PSC`` is 0, the DESER maintains the
          previous power cycle value through the current power cycle.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DESE") -> None:
        super().__init__(device, cmd_syntax)
