"""The status_and_error commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4B, MSO4K,
MSO4KB, MSO5, MSO5B, MSO5K, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *PSC {ON|OFF|<NR1>}
    - *PSC?
    - *PUD {<Block>|<QString>}
    - *PUD?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Pud(SCPICmdWrite, SCPICmdRead):
    """The ``*PUD`` command.

    Description:
        - This command sets or queries a string of Protected User Data. This data is protected by
          the PASSWord command. You can modify it only by first entering the correct password. This
          password is not necessary to query the data.

    Usage:
        - Using the ``.query()`` method will send the ``*PUD?`` query.
        - Using the ``.verify(value)`` method will send the ``*PUD?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*PUD value`` command.

    SCPI Syntax:
        ```
        - *PUD {<Block>|<QString>}
        - *PUD?
        ```

    Info:
        - ``<Block>`` is a block containing up to 100 characters.
        - ``<QString>`` is a string containing up to 100 characters.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*PUD") -> None:
        super().__init__(device, cmd_syntax)


class Psc(SCPICmdWrite, SCPICmdRead):
    """The ``*PSC`` command.

    Description:
        - This command sets and queries the power-on status flag that controls the automatic
          power-on handling of the DESER, SRER, and ESER registers. When ``*PSC`` is true, the DESER
          register is set to 255 and the SRER and ESER registers are set to 0 at power-on. When
          ``*PSC`` is false, the current values in the DESER, SRER, and ESER registers are preserved
          in nonvolatile memory when power is shut off and are restored at power-on.

    Usage:
        - Using the ``.query()`` method will send the ``*PSC?`` query.
        - Using the ``.verify(value)`` method will send the ``*PSC?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*PSC value`` command.

    SCPI Syntax:
        ```
        - *PSC {ON|OFF|<NR1>}
        - *PSC?
        ```

    Info:
        - ``<NR1>`` = 0 sets the power-on status clear flag to false, disables the power-on clear
          and allows the instrument to possibly assert SRQ after power-on; any other value sets the
          power-on status clear flag to true, enabling the power-on status clear and prevents any
          SRQ assertion after power on.
        - ``OFF`` sets the power-on status clear flag to false, disables the power-on clear and
          allows the instrument to possibly assert SRQ after power-on.
        - ``ON`` sets the power-on status clear flag to true, enabling the power-on status clear and
          prevents any SRQ assertion after power on.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*PSC") -> None:
        super().__init__(device, cmd_syntax)
