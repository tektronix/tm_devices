"""The peakstable commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - PEAKSTABle:ADDNew <QString>
    - PEAKSTABle:DELete <QString>
    - PEAKSTABle:LIST?
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


class PeakstableList(SCPICmdRead):
    """The ``PEAKSTABle:LIST`` command.

    Description:
        - This command deletes the specified peak markers table.

    Usage:
        - Using the ``.query()`` method will send the ``PEAKSTABle:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``PEAKSTABle:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - PEAKSTABle:LIST?
        ```
    """


class PeakstableDelete(SCPICmdWrite):
    """The ``PEAKSTABle:DELete`` command.

    Description:
        - This command deletes the specified peak markers table.

    Usage:
        - Using the ``.write(value)`` method will send the ``PEAKSTABle:DELete value`` command.

    SCPI Syntax:
        ```
        - PEAKSTABle:DELete <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string that is the name of the peak markers table to delete. The
          argument is of the form 'TABLE<NR1>', where <NR1> ≥ 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class PeakstableAddnew(SCPICmdWrite):
    """The ``PEAKSTABle:ADDNew`` command.

    Description:
        - This command adds the specified peak markers table.

    Usage:
        - Using the ``.write(value)`` method will send the ``PEAKSTABle:ADDNew value`` command.

    SCPI Syntax:
        ```
        - PEAKSTABle:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string that is the name of the new peak markers table. The
          argument is of the form 'TABLE<NR1>', where <NR1> ≥ 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Peakstable(SCPICmdRead):
    """The ``PEAKSTABle`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PEAKSTABle?`` query.
        - Using the ``.verify(value)`` method will send the ``PEAKSTABle?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``PEAKSTABle:ADDNew`` command.
        - ``.delete``: The ``PEAKSTABle:DELete`` command.
        - ``.list``: The ``PEAKSTABle:LIST`` command.
        - ``.table``: The ``PEAKSTABle:TABle<x>`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "PEAKSTABle"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = PeakstableAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = PeakstableDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = PeakstableList(device, f"{self._cmd_syntax}:LIST")
        self._table: Dict[int, PeakstableTableItem] = DefaultDictPassKeyToFactory(
            lambda x: PeakstableTableItem(device, f"{self._cmd_syntax}:TABle{x}")
        )

    @property
    def addnew(self) -> PeakstableAddnew:
        """Return the ``PEAKSTABle:ADDNew`` command.

        Description:
            - This command adds the specified peak markers table.

        Usage:
            - Using the ``.write(value)`` method will send the ``PEAKSTABle:ADDNew value`` command.

        SCPI Syntax:
            ```
            - PEAKSTABle:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string that is the name of the new peak markers table. The
              argument is of the form 'TABLE<NR1>', where <NR1> ≥ 1.
        """
        return self._addnew

    @property
    def delete(self) -> PeakstableDelete:
        """Return the ``PEAKSTABle:DELete`` command.

        Description:
            - This command deletes the specified peak markers table.

        Usage:
            - Using the ``.write(value)`` method will send the ``PEAKSTABle:DELete value`` command.

        SCPI Syntax:
            ```
            - PEAKSTABle:DELete <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string that is the name of the peak markers table to delete.
              The argument is of the form 'TABLE<NR1>', where <NR1> ≥ 1.
        """
        return self._delete

    @property
    def list(self) -> PeakstableList:
        """Return the ``PEAKSTABle:LIST`` command.

        Description:
            - This command deletes the specified peak markers table.

        Usage:
            - Using the ``.query()`` method will send the ``PEAKSTABle:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``PEAKSTABle:LIST?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - PEAKSTABle:LIST?
            ```
        """
        return self._list

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
