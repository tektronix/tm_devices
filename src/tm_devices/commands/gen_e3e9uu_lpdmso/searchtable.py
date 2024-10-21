"""The searchtable commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SEARCHTABle:ADDNew <qstring>
    - SEARCHTABle:DELete <qstring>
    - SEARCHTABle:list?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SearchtableList(SCPICmdRead):
    """The ``SEARCHTABle:list`` command.

    Description:
        - This command queries all search event table in an Option 5-WIN (Microsoft Windows 10 OS)
          TekExpress compliance testing application.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCHTABle:list?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCHTABle:list?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SEARCHTABle:list?
        ```
    """


class SearchtableDelete(SCPICmdWrite):
    """The ``SEARCHTABle:DELete`` command.

    Description:
        - This command deletes a search event table in an Option 5-WIN (Microsoft Windows 10 OS)
          TekExpress compliance testing application.

    Usage:
        - Using the ``.write(value)`` method will send the ``SEARCHTABle:DELete value`` command.

    SCPI Syntax:
        ```
        - SEARCHTABle:DELete <qstring>
        ```

    Info:
        - ``<qstring>`` contains the name of the search table. 'TABLE' should be the argument prefix
          followed by a non-zero integer.
    """


class SearchtableAddnew(SCPICmdWrite):
    """The ``SEARCHTABle:ADDNew`` command.

    Description:
        - This command adds a new search event table in an Option 5-WIN (Microsoft Windows 10 OS)
          TekExpress compliance testing application.

    Usage:
        - Using the ``.write(value)`` method will send the ``SEARCHTABle:ADDNew value`` command.

    SCPI Syntax:
        ```
        - SEARCHTABle:ADDNew <qstring>
        ```

    Info:
        - ``<qstring>`` contains the name of the search table. 'TABLE' should be the argument prefix
          followed by a non-zero integer.
    """


class Searchtable(SCPICmdRead):
    """The ``SEARCHTABle`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEARCHTABle?`` query.
        - Using the ``.verify(value)`` method will send the ``SEARCHTABle?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``SEARCHTABle:ADDNew`` command.
        - ``.delete``: The ``SEARCHTABle:DELete`` command.
        - ``.list``: The ``SEARCHTABle:list`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "SEARCHTABle"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = SearchtableAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = SearchtableDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = SearchtableList(device, f"{self._cmd_syntax}:list")

    @property
    def addnew(self) -> SearchtableAddnew:
        """Return the ``SEARCHTABle:ADDNew`` command.

        Description:
            - This command adds a new search event table in an Option 5-WIN (Microsoft Windows 10
              OS) TekExpress compliance testing application.

        Usage:
            - Using the ``.write(value)`` method will send the ``SEARCHTABle:ADDNew value`` command.

        SCPI Syntax:
            ```
            - SEARCHTABle:ADDNew <qstring>
            ```

        Info:
            - ``<qstring>`` contains the name of the search table. 'TABLE' should be the argument
              prefix followed by a non-zero integer.
        """
        return self._addnew

    @property
    def delete(self) -> SearchtableDelete:
        """Return the ``SEARCHTABle:DELete`` command.

        Description:
            - This command deletes a search event table in an Option 5-WIN (Microsoft Windows 10 OS)
              TekExpress compliance testing application.

        Usage:
            - Using the ``.write(value)`` method will send the ``SEARCHTABle:DELete value`` command.

        SCPI Syntax:
            ```
            - SEARCHTABle:DELete <qstring>
            ```

        Info:
            - ``<qstring>`` contains the name of the search table. 'TABLE' should be the argument
              prefix followed by a non-zero integer.
        """
        return self._delete

    @property
    def list(self) -> SearchtableList:
        """Return the ``SEARCHTABle:list`` command.

        Description:
            - This command queries all search event table in an Option 5-WIN (Microsoft Windows 10
              OS) TekExpress compliance testing application.

        Usage:
            - Using the ``.query()`` method will send the ``SEARCHTABle:list?`` query.
            - Using the ``.verify(value)`` method will send the ``SEARCHTABle:list?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SEARCHTABle:list?
            ```
        """
        return self._list
