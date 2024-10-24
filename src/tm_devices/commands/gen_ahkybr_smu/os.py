# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The os commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2604B, SMU2606B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B,
SMU2651A, SMU2657A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - os.remove()
    - os.rename()
    - os.time()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Os(BaseTSPCmd):
    """The ``os`` command tree.

    Properties and methods:
        - ``.remove()``: The ``os.remove()`` function.
        - ``.rename()``: The ``os.rename()`` function.
        - ``.time()``: The ``os.time()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "os") -> None:
        super().__init__(device, cmd_syntax)

    def remove(self, filename: str) -> str:
        """Run the ``os.remove()`` function.

        Description:
            - This function deletes the file or directory with a given name.

        TSP Syntax:
            ```
            - os.remove()
            ```

        Args:
            filename: A string representing the name of the file or directory to delete.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.remove("{filename}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.remove()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def rename(self, oldname: str, newname: str) -> str:
        """Run the ``os.rename()`` function.

        Description:
            - This function renames an existing file or directory.

        TSP Syntax:
            ```
            - os.rename()
            ```

        Args:
            oldname: String representing the name of the file or directory to rename.
            newname: String representing the new name of the file or directory.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.rename("{oldname}", "{newname}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.rename()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def time(self, timespec: Optional[str] = None) -> str:
        """Run the ``os.time()`` function.

        Description:
            - This function generates a time value in UTC time.

        TSP Syntax:
            ```
            - os.time()
            ```

        Args:
            timespec (optional): The date and time (year, month, day, hour, and minute).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (timespec,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.time({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.time()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
