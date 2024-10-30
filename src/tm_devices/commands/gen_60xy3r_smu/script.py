# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The script commands module.

These commands are used in the following models:
SMU2450

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - script.delete()
    - script.load()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Script(BaseTSPCmd):
    """The ``script`` command tree.

    Properties and methods:
        - ``.delete()``: The ``script.delete()`` function.
        - ``.load()``: The ``script.load()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "script") -> None:
        super().__init__(device, cmd_syntax)

    def delete(self, script_name: str) -> None:
        """Run the ``script.delete()`` function.

        Description:
            - This function deletes a script from the run-time memory and nonvolatile memory.

        TSP Syntax:
            ```
            - script.delete()
            ```

        Args:
            script_name: A string that represents the name of the script.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.delete("{script_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.delete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def load(self, file: str) -> str:
        """Run the ``script.load()`` function.

        Description:
            - This function creates a script from a specified file.

        TSP Syntax:
            ```
            - script.load()
            ```

        Args:
            file: A string that contains the path and file name of the script file to load; if
                scriptVar is not defined, this name is used as the global variable name for this
                script.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.load("{file}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.load()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
