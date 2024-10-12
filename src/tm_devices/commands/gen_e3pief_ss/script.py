# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The script commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - script.anonymous
    - script.delete()
    - script.load()
    - script.new()
    - script.newautorun()
    - script.restore()
    - script.run()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Script(BaseTSPCmd):
    """The ``script`` command tree.

    Properties and methods:
        - ``.anonymous``: The ``script.anonymous`` attribute.
        - ``.delete()``: The ``script.delete()`` function.
        - ``.load()``: The ``script.load()`` function.
        - ``.new()``: The ``script.new()`` function.
        - ``.newautorun()``: The ``script.newautorun()`` function.
        - ``.restore()``: The ``script.restore()`` function.
        - ``.run()``: The ``script.run()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "script") -> None:
        super().__init__(device, cmd_syntax)

    @property
    def anonymous(self) -> str:
        """Access the ``script.anonymous`` attribute.

        Description:
            - This is a reference to the anonymous script.

        Usage:
            - Accessing this property will send the ``print(script.anonymous)`` query.

        TSP Syntax:
            ```
            - print(script.anonymous)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".anonymous"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.anonymous)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.anonymous`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def delete(self, script_name: str) -> None:
        """Run the ``script.delete()`` function.

        Description:
            - This function deletes a script from the runtime memory and nonvolatile memory.

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

    def new(self, code: str, name: Optional[str] = None) -> str:
        """Run the ``script.new()`` function.

        Description:
            - This function creates a script.

        TSP Syntax:
            ```
            - script.new()
            ```

        Args:
            code: A string containing the body of the script.
            name (optional): The name of the script.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{code}"',
                    f'"{name}"' if name is not None else None,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.new({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.new()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def newautorun(self, code: str, name: Optional[str] = None) -> str:
        """Run the ``script.newautorun()`` function.

        Description:
            - This function creates a script and enables autorun.

        TSP Syntax:
            ```
            - script.newautorun()
            ```

        Args:
            code: A string that contains the body of the script.
            name (optional): The name of the script.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{code}"',
                    f'"{name}"' if name is not None else None,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.newautorun({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.newautorun()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def restore(self, name: str) -> None:
        """Run the ``script.restore()`` function.

        Description:
            - This function restores a script that was removed from the runtime environment.

        TSP Syntax:
            ```
            - script.restore()
            ```

        Args:
            name: The name of the script to be restored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.restore({name})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.restore()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def run(self) -> None:
        """Run the ``script.run()`` function.

        Description:
            - This function runs the anonymous script.

        TSP Syntax:
            ```
            - script.run()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.run()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.run()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
