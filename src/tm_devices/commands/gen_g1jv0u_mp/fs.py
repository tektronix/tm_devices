# pyright: reportConstantRedefinition=none
"""The fs commands module.

These commands are used in the following models:
MP5103

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - fs.cwd()
    - fs.is_dir()
    - fs.is_file()
    - fs.mkdir()
    - fs.readdir()
    - fs.rmdir()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Fs(BaseTSPCmd):
    """The ``fs`` command tree.

    Properties and methods:
        - ``.cwd()``: The ``fs.cwd()`` function.
        - ``.is_dir()``: The ``fs.is_dir()`` function.
        - ``.is_file()``: The ``fs.is_file()`` function.
        - ``.mkdir()``: The ``fs.mkdir()`` function.
        - ``.readdir()``: The ``fs.readdir()`` function.
        - ``.rmdir()``: The ``fs.rmdir()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "fs") -> None:
        super().__init__(device, cmd_syntax)

    def cwd(self) -> str:
        """Run the ``fs.cwd()`` function.

        Description:
            - This function returns the absolute path of the current working directory.

        TSP Syntax:
            ```
            - fs.cwd()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.cwd())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.cwd()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def is_dir(self, path: str) -> str:
        """Run the ``fs.is_dir()`` function.

        Description:
            - This function tests whether or not the specified path refers to a directory.

        TSP Syntax:
            ```
            - fs.is_dir()
            ```

        Args:
            path: The path of the file system entry to test.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.is_dir("{path}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.is_dir()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def is_file(self, path: str) -> str:
        """Run the ``fs.is_file()`` function.

        Description:
            - Tests whether the specified path refers to a file (as opposed to a directory).

        TSP Syntax:
            ```
            - fs.is_file()
            ```

        Args:
            path: The path of the file system entry to test.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.is_file("{path}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.is_file()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def mkdir(self, new_path: str) -> str:
        """Run the ``fs.mkdir()`` function.

        Description:
            - This function creates a directory at the specified path.

        TSP Syntax:
            ```
            - fs.mkdir()
            ```

        Args:
            new_path: Location (path) of where to create the new directory.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.mkdir("{new_path}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.mkdir()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def readdir(self, path: str) -> str:
        """Run the ``fs.readdir()`` function.

        Description:
            - This function returns a list of the file system entries in the directory.

        TSP Syntax:
            ```
            - fs.readdir()
            ```

        Args:
            path: The directory path.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.readdir("{path}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.readdir()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def rmdir(self, path: str) -> None:
        """Run the ``fs.rmdir()`` function.

        Description:
            - This function removes a directory from the file system.

        TSP Syntax:
            ```
            - fs.rmdir()
            ```

        Args:
            path: The path of the directory to remove.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.rmdir("{path}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.rmdir()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
