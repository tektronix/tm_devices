"""The customtable commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CUSTOMTABle:ADDNew <Qstring>
    - CUSTOMTABle:DELete <Qstring>
    - CUSTOMTABle:LIST? <Qstring>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CustomtableList(SCPICmdReadWithArguments):
    """The ``CUSTOMTABle:LIST`` command.

    Description:
        - This command queries the list of custom result tables has been added.

    Usage:
        - Using the ``.query(argument)`` method will send the ``CUSTOMTABle:LIST? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``CUSTOMTABle:LIST? argument``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CUSTOMTABle:LIST? <Qstring>
        ```

    Info:
        - ``<Qstring>`` specifies the custom results table name.
    """


class CustomtableDelete(SCPICmdWrite):
    """The ``CUSTOMTABle:DELete`` command.

    Description:
        - This command deletes the custom result(s) table that was added.

    Usage:
        - Using the ``.write(value)`` method will send the ``CUSTOMTABle:DELete value`` command.

    SCPI Syntax:
        ```
        - CUSTOMTABle:DELete <Qstring>
        ```

    Info:
        - ``<Qstring>`` specifies the custom results table name.
    """


class CustomtableAddnew(SCPICmdWrite):
    """The ``CUSTOMTABle:ADDNew`` command.

    Description:
        - This command adds new custom results table.

    Usage:
        - Using the ``.write(value)`` method will send the ``CUSTOMTABle:ADDNew value`` command.

    SCPI Syntax:
        ```
        - CUSTOMTABle:ADDNew <Qstring>
        ```

    Info:
        - ``<Qstring>`` specifies the custom results table name.
    """


class Customtable(SCPICmdRead):
    """The ``CUSTOMTABle`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CUSTOMTABle?`` query.
        - Using the ``.verify(value)`` method will send the ``CUSTOMTABle?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``CUSTOMTABle:ADDNew`` command.
        - ``.delete``: The ``CUSTOMTABle:DELete`` command.
        - ``.list``: The ``CUSTOMTABle:LIST`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "CUSTOMTABle"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = CustomtableAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = CustomtableDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = CustomtableList(device, f"{self._cmd_syntax}:LIST")

    @property
    def addnew(self) -> CustomtableAddnew:
        """Return the ``CUSTOMTABle:ADDNew`` command.

        Description:
            - This command adds new custom results table.

        Usage:
            - Using the ``.write(value)`` method will send the ``CUSTOMTABle:ADDNew value`` command.

        SCPI Syntax:
            ```
            - CUSTOMTABle:ADDNew <Qstring>
            ```

        Info:
            - ``<Qstring>`` specifies the custom results table name.
        """
        return self._addnew

    @property
    def delete(self) -> CustomtableDelete:
        """Return the ``CUSTOMTABle:DELete`` command.

        Description:
            - This command deletes the custom result(s) table that was added.

        Usage:
            - Using the ``.write(value)`` method will send the ``CUSTOMTABle:DELete value`` command.

        SCPI Syntax:
            ```
            - CUSTOMTABle:DELete <Qstring>
            ```

        Info:
            - ``<Qstring>`` specifies the custom results table name.
        """
        return self._delete

    @property
    def list(self) -> CustomtableList:
        """Return the ``CUSTOMTABle:LIST`` command.

        Description:
            - This command queries the list of custom result tables has been added.

        Usage:
            - Using the ``.query(argument)`` method will send the ``CUSTOMTABle:LIST? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CUSTOMTABle:LIST? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.

        SCPI Syntax:
            ```
            - CUSTOMTABle:LIST? <Qstring>
            ```

        Info:
            - ``<Qstring>`` specifies the custom results table name.
        """
        return self._list
