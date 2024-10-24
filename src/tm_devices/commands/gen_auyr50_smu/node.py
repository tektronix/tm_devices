# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The node commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2604B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - node[N].execute()
    - node[N].getglobal()
    - node[N].setglobal()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class NodeItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``node[N]`` command tree.

    Info:
        - ``N``, the node number of this instrument.

    Properties and methods:
        - ``.execute()``: The ``node[N].execute()`` function.
        - ``.getglobal()``: The ``node[N].getglobal()`` function.
        - ``.setglobal()``: The ``node[N].setglobal()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "node[N]") -> None:
        super().__init__(device, cmd_syntax)

    def execute(self, script_code: str) -> None:
        """Run the ``node[N].execute()`` function.

        Description:
            - This function starts test scripts from a remote node. This command is not available on
              the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - node[N].execute()
            ```

        Args:
            script_code: A string containing the source code.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.execute("{script_code}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.execute()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getglobal(self, name: str) -> str:
        """Run the ``node[N].getglobal()`` function.

        Description:
            - This function returns the value of a global variable. This command is not available on
              the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - node[N].getglobal()
            ```

        Args:
            name: The global variable name.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.getglobal("{name}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getglobal()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setglobal(self, name: str, value: str) -> None:
        """Run the ``node[N].setglobal()`` function.

        Description:
            - This function sets the value of a global variable. This command is not available on
              the 2604B, 2614B, or 2634B.

        TSP Syntax:
            ```
            - node[N].setglobal()
            ```

        Args:
            name: The global variable name to set.
            value: The value to assign to the variable.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.setglobal("{name}", {value})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setglobal()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
