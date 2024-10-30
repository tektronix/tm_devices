"""The meastable commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MEASTABle:ADDNew <QString>
    - MEASTABle:DELETE <QString>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MeastableDelete(SCPICmdWrite):
    """The ``MEASTABle:DELETE`` command.

    Description:
        - This command removes the requested measurement results view table from the scope
          application.

    Usage:
        - Using the ``.write(value)`` method will send the ``MEASTABle:DELETE value`` command.

    SCPI Syntax:
        ```
        - MEASTABle:DELETE <QString>
        ```

    Info:
        - ``<QString>`` specifies a measurement results view table to remove.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MeastableAddnew(SCPICmdWrite):
    """The ``MEASTABle:ADDNew`` command.

    Description:
        - This command adds a new measurement results view table to the scope application. The
          results view table can be named through the argument sent to the command.

    Usage:
        - Using the ``.write(value)`` method will send the ``MEASTABle:ADDNew value`` command.

    SCPI Syntax:
        ```
        - MEASTABle:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` specifies a new measurement results view table to the scope application.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Meastable(SCPICmdRead):
    """The ``MEASTABle`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASTABle?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASTABle?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``MEASTABle:ADDNew`` command.
        - ``.delete``: The ``MEASTABle:DELETE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MEASTABle") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = MeastableAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = MeastableDelete(device, f"{self._cmd_syntax}:DELETE")

    @property
    def addnew(self) -> MeastableAddnew:
        """Return the ``MEASTABle:ADDNew`` command.

        Description:
            - This command adds a new measurement results view table to the scope application. The
              results view table can be named through the argument sent to the command.

        Usage:
            - Using the ``.write(value)`` method will send the ``MEASTABle:ADDNew value`` command.

        SCPI Syntax:
            ```
            - MEASTABle:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` specifies a new measurement results view table to the scope application.
        """
        return self._addnew

    @property
    def delete(self) -> MeastableDelete:
        """Return the ``MEASTABle:DELETE`` command.

        Description:
            - This command removes the requested measurement results view table from the scope
              application.

        Usage:
            - Using the ``.write(value)`` method will send the ``MEASTABle:DELETE value`` command.

        SCPI Syntax:
            ```
            - MEASTABle:DELETE <QString>
            ```

        Info:
            - ``<QString>`` specifies a measurement results view table to remove.
        """
        return self._delete
