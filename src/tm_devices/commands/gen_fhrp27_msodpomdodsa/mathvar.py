"""The mathvar commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MATHVAR:VAR<x> <NR3>
    - MATHVAR:VAR<x>?
    - MATHVAR?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MathvarVarItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    r"""The ``MATHVAR:VAR<x>`` command.

    Description:
        - This command specifies one of two different numerical values you can use within math
          expressions. These values can range from -10.0e-18 to 1.0e+15; the default values are 0.0.
          <x> specifies the location, 1 or 2, in which you can store values. Stored math variables
          can be referenced within math expressions as VAR1 and VAR2. For example, the following
          command defines MATH1 as the product of Channel 1 and math variable 1: ``MATH1:DEFINE``
          'CH1 \* VAR1'.

    Usage:
        - Using the ``.query()`` method will send the ``MATHVAR:VAR<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MATHVAR:VAR<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATHVAR:VAR<x> value`` command.

    SCPI Syntax:
        ```
        - MATHVAR:VAR<x> <NR3>
        - MATHVAR:VAR<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the numerical value to be stored in
          location x <1 through 2>.
    """


class Mathvar(SCPICmdRead):
    """The ``MATHVAR`` command.

    Description:
        - Queries both numerical values you can use within math expressions.

    Usage:
        - Using the ``.query()`` method will send the ``MATHVAR?`` query.
        - Using the ``.verify(value)`` method will send the ``MATHVAR?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATHVAR?
        ```

    Properties:
        - ``.var``: The ``MATHVAR:VAR<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MATHVAR") -> None:
        super().__init__(device, cmd_syntax)
        self._var: Dict[int, MathvarVarItem] = DefaultDictPassKeyToFactory(
            lambda x: MathvarVarItem(device, f"{self._cmd_syntax}:VAR{x}")
        )

    @property
    def var(self) -> Dict[int, MathvarVarItem]:
        r"""Return the ``MATHVAR:VAR<x>`` command.

        Description:
            - This command specifies one of two different numerical values you can use within math
              expressions. These values can range from -10.0e-18 to 1.0e+15; the default values are
              0.0. <x> specifies the location, 1 or 2, in which you can store values. Stored math
              variables can be referenced within math expressions as VAR1 and VAR2. For example, the
              following command defines MATH1 as the product of Channel 1 and math variable 1:
              ``MATH1:DEFINE`` 'CH1 \* VAR1'.

        Usage:
            - Using the ``.query()`` method will send the ``MATHVAR:VAR<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MATHVAR:VAR<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATHVAR:VAR<x> value`` command.

        SCPI Syntax:
            ```
            - MATHVAR:VAR<x> <NR3>
            - MATHVAR:VAR<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the numerical value to be stored
              in location x <1 through 2>.
        """
        return self._var
