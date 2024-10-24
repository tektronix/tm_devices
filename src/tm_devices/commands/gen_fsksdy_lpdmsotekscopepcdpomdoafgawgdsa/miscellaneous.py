"""The miscellaneous commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC, AWG5200, AWG5K, AWG5KC, AWG70KA, AWG70KB, AWG7K, AWG7KC, DPO2K, DPO2KB,
DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD,
LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4B, MSO4K, MSO4KB, MSO5,
MSO5B, MSO5K, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *IDN?
    - *TST?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Tst(SCPICmdRead):
    """The ``*TST`` command.

    Description:
        - Tests (self-test) the interface and returns a 0.

    Usage:
        - Using the ``.query()`` method will send the ``*TST?`` query.
        - Using the ``.verify(value)`` method will send the ``*TST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - *TST?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*TST") -> None:
        super().__init__(device, cmd_syntax)


class Idn(SCPICmdRead):
    """The ``*IDN`` command.

    Description:
        - This query-only command returns the instrument identification code.

    Usage:
        - Using the ``.query()`` method will send the ``*IDN?`` query.
        - Using the ``.verify(value)`` method will send the ``*IDN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - *IDN?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*IDN") -> None:
        super().__init__(device, cmd_syntax)
