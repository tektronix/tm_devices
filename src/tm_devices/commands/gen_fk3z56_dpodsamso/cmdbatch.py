"""The cmdbatch commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CMDBatch {<NR1>OFF|ON}
    - CMDBatch?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Cmdbatch(SCPICmdWrite, SCPICmdRead):
    """The ``CMDBatch`` command.

    Description:
        - This command sets or queries the state of command batching. By batching commands, database
          transactions can be optimized, increasing command throughput. Also, batching allows for
          ALL commands in an individual batch to be order independent and accomplish the same result
          as if the commands were coupled. The Batch state is persistent and will be saved across
          power cycles, but will not be saved and recalled as part of a setup. In a setup scenario,
          the factory initial value is enabled.

    Usage:
        - Using the ``.query()`` method will send the ``CMDBatch?`` query.
        - Using the ``.verify(value)`` method will send the ``CMDBatch?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CMDBatch value`` command.

    SCPI Syntax:
        ```
        - CMDBatch {<NR1>OFF|ON}
        - CMDBatch?
        ```

    Info:
        - ``<NR1>`` = 0 turns command batching off; any other value turns command batching on.
        - ``OFF`` turns command batching off.
        - ``ON`` turns command batching on.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CMDBatch") -> None:
        super().__init__(device, cmd_syntax)
