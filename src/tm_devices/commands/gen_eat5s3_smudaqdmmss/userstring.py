# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The userstring commands module.

These commands are used in the following models:
DAQ6510, DMM6500, DMM7510, SMU2450, SMU2460, SMU2461, SMU2470, SMU2601B, SMU2602B, SMU2604B,
SMU2606B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B, SMU2651A, SMU2657A, SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - userstring.add()
    - userstring.delete()
    - userstring.get()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Userstring(BaseTSPCmd):
    """The ``userstring`` command tree.

    Properties and methods:
        - ``.add()``: The ``userstring.add()`` function.
        - ``.delete()``: The ``userstring.delete()`` function.
        - ``.get()``: The ``userstring.get()`` function.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "userstring"
    ) -> None:
        super().__init__(device, cmd_syntax)

    def add(self, name: str, value: str) -> None:
        """Run the ``userstring.add()`` function.

        Description:
            - This function adds a user-defined string to nonvolatile memory.

        TSP Syntax:
            ```
            - userstring.add()
            ```

        Args:
            name: The name of the string; the key of the key-value pair.
            value: The string to associate with name; the value of the key-value pair.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.add("{name}", "{value}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.add()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def delete(self, name: str) -> None:
        """Run the ``userstring.delete()`` function.

        Description:
            - This function deletes a user-defined string from nonvolatile memory.

        TSP Syntax:
            ```
            - userstring.delete()
            ```

        Args:
            name: The name (key) of the key-value pair of the user-defined string to delete.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.delete("{name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.delete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def get(self, name: str) -> str:
        """Run the ``userstring.get()`` function.

        Description:
            - This function retrieves a user-defined string from nonvolatile memory.

        TSP Syntax:
            ```
            - userstring.get()
            ```

        Args:
            name: The name (key) of the user-defined string.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.get("{name}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.get()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
