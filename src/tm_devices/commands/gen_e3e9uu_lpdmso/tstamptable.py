"""The tstamptable commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TSTamptable:ADDNew <Qstring>
    - TSTamptable:DELETE <Qstring>
    - TSTamptable:LIST?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class TstamptableList(SCPICmdRead):
    """The ``TSTamptable:LIST`` command.

    Description:
        - This command queries the list of History time stamp results tables has been added.

    Usage:
        - Using the ``.query()`` method will send the ``TSTamptable:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``TSTamptable:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TSTamptable:LIST?
        ```
    """


class TstamptableDelete(SCPICmdWrite):
    """The ``TSTamptable:DELETE`` command.

    Description:
        - This command deletes the requested History time stamp results table.

    Usage:
        - Using the ``.write(value)`` method will send the ``TSTamptable:DELETE value`` command.

    SCPI Syntax:
        ```
        - TSTamptable:DELETE <Qstring>
        ```

    Info:
        - ``<Qstring>`` specifies the History time stamp results table name.
    """


class TstamptableAddnew(SCPICmdWrite):
    """The ``TSTamptable:ADDNew`` command.

    Description:
        - This command adds a new History time stamp results table to the scope application.

    Usage:
        - Using the ``.write(value)`` method will send the ``TSTamptable:ADDNew value`` command.

    SCPI Syntax:
        ```
        - TSTamptable:ADDNew <Qstring>
        ```

    Info:
        - ``<Qstring>`` specifies the History time stamp results table name.
    """


class Tstamptable(SCPICmdRead):
    """The ``TSTamptable`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TSTamptable?`` query.
        - Using the ``.verify(value)`` method will send the ``TSTamptable?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``TSTamptable:ADDNew`` command.
        - ``.delete``: The ``TSTamptable:DELETE`` command.
        - ``.list``: The ``TSTamptable:LIST`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "TSTamptable"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = TstamptableAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = TstamptableDelete(device, f"{self._cmd_syntax}:DELETE")
        self._list = TstamptableList(device, f"{self._cmd_syntax}:LIST")

    @property
    def addnew(self) -> TstamptableAddnew:
        """Return the ``TSTamptable:ADDNew`` command.

        Description:
            - This command adds a new History time stamp results table to the scope application.

        Usage:
            - Using the ``.write(value)`` method will send the ``TSTamptable:ADDNew value`` command.

        SCPI Syntax:
            ```
            - TSTamptable:ADDNew <Qstring>
            ```

        Info:
            - ``<Qstring>`` specifies the History time stamp results table name.
        """
        return self._addnew

    @property
    def delete(self) -> TstamptableDelete:
        """Return the ``TSTamptable:DELETE`` command.

        Description:
            - This command deletes the requested History time stamp results table.

        Usage:
            - Using the ``.write(value)`` method will send the ``TSTamptable:DELETE value`` command.

        SCPI Syntax:
            ```
            - TSTamptable:DELETE <Qstring>
            ```

        Info:
            - ``<Qstring>`` specifies the History time stamp results table name.
        """
        return self._delete

    @property
    def list(self) -> TstamptableList:
        """Return the ``TSTamptable:LIST`` command.

        Description:
            - This command queries the list of History time stamp results tables has been added.

        Usage:
            - Using the ``.query()`` method will send the ``TSTamptable:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``TSTamptable:LIST?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TSTamptable:LIST?
            ```
        """
        return self._list
