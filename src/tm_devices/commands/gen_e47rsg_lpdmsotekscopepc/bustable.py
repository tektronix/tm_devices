"""The bustable commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - BUSTABle:ADDNew <QString>
    - BUSTABle:DELete <QString>
    - BUSTABle:LIST?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class BustableList(SCPICmdRead):
    """The ``BUSTABle:LIST`` command.

    Description:
        - This query lists all currently defined bus tables.

    Usage:
        - Using the ``.query()`` method will send the ``BUSTABle:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``BUSTABle:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - BUSTABle:LIST?
        ```
    """


class BustableDelete(SCPICmdWrite):
    """The ``BUSTABle:DELete`` command.

    Description:
        - Deletes the specified bus table. Argument is of the form 'TABLE<NR1>', where <NR1> is ≥1).

    Usage:
        - Using the ``.write(value)`` method will send the ``BUSTABle:DELete value`` command.

    SCPI Syntax:
        ```
        - BUSTABle:DELete <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string that is the name of the bus table to delete.
    """

    _WRAP_ARG_WITH_QUOTES = True


class BustableAddnew(SCPICmdWrite):
    """The ``BUSTABle:ADDNew`` command.

    Description:
        - Adds the specified bus table. Argument is of the form 'TABLE<NR1>', where <NR1> is ≥1).

    Usage:
        - Using the ``.write(value)`` method will send the ``BUSTABle:ADDNew value`` command.

    SCPI Syntax:
        ```
        - BUSTABle:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string that is the name of the new bus table.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Bustable(SCPICmdRead):
    """The ``BUSTABle`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BUSTABle?`` query.
        - Using the ``.verify(value)`` method will send the ``BUSTABle?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``BUSTABle:ADDNew`` command.
        - ``.delete``: The ``BUSTABle:DELete`` command.
        - ``.list``: The ``BUSTABle:LIST`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "BUSTABle") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = BustableAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = BustableDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = BustableList(device, f"{self._cmd_syntax}:LIST")

    @property
    def addnew(self) -> BustableAddnew:
        """Return the ``BUSTABle:ADDNew`` command.

        Description:
            - Adds the specified bus table. Argument is of the form 'TABLE<NR1>', where <NR1> is
              ≥1).

        Usage:
            - Using the ``.write(value)`` method will send the ``BUSTABle:ADDNew value`` command.

        SCPI Syntax:
            ```
            - BUSTABle:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string that is the name of the new bus table.
        """
        return self._addnew

    @property
    def delete(self) -> BustableDelete:
        """Return the ``BUSTABle:DELete`` command.

        Description:
            - Deletes the specified bus table. Argument is of the form 'TABLE<NR1>', where <NR1> is
              ≥1).

        Usage:
            - Using the ``.write(value)`` method will send the ``BUSTABle:DELete value`` command.

        SCPI Syntax:
            ```
            - BUSTABle:DELete <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string that is the name of the bus table to delete.
        """
        return self._delete

    @property
    def list(self) -> BustableList:
        """Return the ``BUSTABle:LIST`` command.

        Description:
            - This query lists all currently defined bus tables.

        Usage:
            - Using the ``.query()`` method will send the ``BUSTABle:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``BUSTABle:LIST?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - BUSTABle:LIST?
            ```
        """
        return self._list
