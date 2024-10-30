"""The cq commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CQ<x>:THRESHold <NR3>
    - CQ<x>:THRESHold?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CqItemThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``CQ<x>:THRESHold`` command.

    Description:
        - This command sets or queries the comparable threshold for converting the clock/qualifier
          signal to its digital form, where x is zero.

    Usage:
        - Using the ``.query()`` method will send the ``CQ<x>:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``CQ<x>:THRESHold?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CQ<x>:THRESHold value`` command.

    SCPI Syntax:
        ```
        - CQ<x>:THRESHold <NR3>
        - CQ<x>:THRESHold?
        ```

    Info:
        - ``<NR3>`` specifies the channel/qualifier threshold in volts.
    """


class CqItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CQ<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CQ<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CQ<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.threshold``: The ``CQ<x>:THRESHold`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CQ<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = CqItemThreshold(device, f"{self._cmd_syntax}:THRESHold")

    @property
    def threshold(self) -> CqItemThreshold:
        """Return the ``CQ<x>:THRESHold`` command.

        Description:
            - This command sets or queries the comparable threshold for converting the
              clock/qualifier signal to its digital form, where x is zero.

        Usage:
            - Using the ``.query()`` method will send the ``CQ<x>:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``CQ<x>:THRESHold?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CQ<x>:THRESHold value`` command.

        SCPI Syntax:
            ```
            - CQ<x>:THRESHold <NR3>
            - CQ<x>:THRESHold?
            ```

        Info:
            - ``<NR3>`` specifies the channel/qualifier threshold in volts.
        """
        return self._threshold
