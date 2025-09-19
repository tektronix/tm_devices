"""The peakstable commands module.

These commands are used in the following models:
DPO7AX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - PEAKSTABle:TABle<x>:FRESolution {AUTO|PRECISE}
    - PEAKSTABle:TABle<x>:FRESolution?
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


class PeakstableTableItemFresolution(SCPICmdWrite, SCPICmdRead):
    """The ``PEAKSTABle:TABle<x>:FRESolution`` command.

    Description:
        - This command sets or queries the Frequency Resolution state for peak markers table.

    Usage:
        - Using the ``.query()`` method will send the ``PEAKSTABle:TABle<x>:FRESolution?`` query.
        - Using the ``.verify(value)`` method will send the ``PEAKSTABle:TABle<x>:FRESolution?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PEAKSTABle:TABle<x>:FRESolution value``
          command.

    SCPI Syntax:
        ```
        - PEAKSTABle:TABle<x>:FRESolution {AUTO|PRECISE}
        - PEAKSTABle:TABle<x>:FRESolution?
        ```

    Info:
        - ``AUTO`` shows the frequency with the same precision as shown in the Spectrum View
          display.
        - ``PRECISE`` shows the frequency down to single Hz resolution.
    """


class PeakstableTableItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``PEAKSTABle:TABle<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PEAKSTABle:TABle<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``PEAKSTABle:TABle<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fresolution``: The ``PEAKSTABle:TABle<x>:FRESolution`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fresolution = PeakstableTableItemFresolution(
            device, f"{self._cmd_syntax}:FRESolution"
        )

    @property
    def fresolution(self) -> PeakstableTableItemFresolution:
        """Return the ``PEAKSTABle:TABle<x>:FRESolution`` command.

        Description:
            - This command sets or queries the Frequency Resolution state for peak markers table.

        Usage:
            - Using the ``.query()`` method will send the ``PEAKSTABle:TABle<x>:FRESolution?``
              query.
            - Using the ``.verify(value)`` method will send the ``PEAKSTABle:TABle<x>:FRESolution?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PEAKSTABle:TABle<x>:FRESolution value`` command.

        SCPI Syntax:
            ```
            - PEAKSTABle:TABle<x>:FRESolution {AUTO|PRECISE}
            - PEAKSTABle:TABle<x>:FRESolution?
            ```

        Info:
            - ``AUTO`` shows the frequency with the same precision as shown in the Spectrum View
              display.
            - ``PRECISE`` shows the frequency down to single Hz resolution.
        """
        return self._fresolution


class Peakstable(SCPICmdRead):
    """The ``PEAKSTABle`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PEAKSTABle?`` query.
        - Using the ``.verify(value)`` method will send the ``PEAKSTABle?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.table``: The ``PEAKSTABle:TABle<x>`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "PEAKSTABle"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._table: Dict[int, PeakstableTableItem] = DefaultDictPassKeyToFactory(
            lambda x: PeakstableTableItem(device, f"{self._cmd_syntax}:TABle{x}")
        )

    @property
    def table(self) -> Dict[int, PeakstableTableItem]:
        """Return the ``PEAKSTABle:TABle<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PEAKSTABle:TABle<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``PEAKSTABle:TABle<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.fresolution``: The ``PEAKSTABle:TABle<x>:FRESolution`` command.
        """
        return self._table
