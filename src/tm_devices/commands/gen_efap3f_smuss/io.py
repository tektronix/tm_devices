# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The io commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2604B, SMU2606B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B,
SMU2651A, SMU2657A, SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - io.close()
    - io.flush()
    - io.input()
    - io.open()
    - io.output()
    - io.read()
    - io.type()
    - io.write()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Io(BaseTSPCmd):
    """The ``io`` command tree.

    Properties and methods:
        - ``.close()``: The ``io.close()`` function.
        - ``.flush()``: The ``io.flush()`` function.
        - ``.input()``: The ``io.input()`` function.
        - ``.open()``: The ``io.open()`` function.
        - ``.output()``: The ``io.output()`` function.
        - ``.read()``: The ``io.read()`` function.
        - ``.type()``: The ``io.type()`` function.
        - ``.write()``: The ``io.write()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "io") -> None:
        super().__init__(device, cmd_syntax)

    def close(self, file: Optional[str] = None) -> None:
        """Run the ``io.close()`` function.

        Description:
            - This function closes a file.

        TSP Syntax:
            ```
            - io.close()
            ```

        Args:
            file (optional): The descriptor of the file to close.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (file,) if x is not None)
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.close({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.close()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def flush(self) -> None:
        """Run the ``io.flush()`` function.

        Description:
            - This function saves buffered data to a file.

        TSP Syntax:
            ```
            - io.flush()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.flush()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.flush()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def input(self, newfile: Optional[str] = None) -> str:
        """Run the ``io.input()`` function.

        Description:
            - This function assigns a previously opened file, or opens a new file, as the default
              input file.

        TSP Syntax:
            ```
            - io.input()
            ```

        Args:
            newfile (optional): A string representing the path of a file to open as the default
                input file, or the file descriptor of an open file to use as the default input file.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x) for x in (f'"{newfile}"' if newfile is not None else None,) if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.input({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.input()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def open(self, path: str, mode: Optional[str] = None) -> str:
        """Run the ``io.open()`` function.

        Description:
            - This function opens a file for later reference.

        TSP Syntax:
            ```
            - io.open()
            ```

        Args:
            path: The path of the file to open.
            mode (optional): A string representing the intended access mode ('r' = read, 'w' =
                write, and 'a' = append).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{path}"',
                    f'"{mode}"' if mode is not None else None,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.open({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.open()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def output(self, newfile: Optional[str] = None) -> str:
        """Run the ``io.output()`` function.

        Description:
            - This function assigns a previously opened file or opens a new file as the default
              output file.

        TSP Syntax:
            ```
            - io.output()
            ```

        Args:
            newfile (optional): A file descriptor to assign (or the path of a file to open) as the
                default output file.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x) for x in (f'"{newfile}"' if newfile is not None else None,) if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.output({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.output()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def read(self, format_: Optional[str] = None) -> str:
        """Run the ``io.read()`` function.

        Description:
            - This function reads data from the default input file.

        TSP Syntax:
            ```
            - io.read()
            ```

        Args:
            format_ (optional): A string or number indicating the type of data to be read.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x) for x in (f'"{format_}"' if format_ is not None else None,) if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.read({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.read()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def type(self, obj: str) -> str:
        """Run the ``io.type()`` function.

        Description:
            - This function checks whether or not a given object is a file handle.

        TSP Syntax:
            ```
            - io.type()
            ```

        Args:
            obj: Object to check.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.type({obj}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.type()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def write(self, data: Optional[str] = None) -> None:
        """Run the ``io.write()`` function.

        Description:
            - This function writes data to the default output file.

        TSP Syntax:
            ```
            - io.write()
            ```

        Args:
            data (optional): The data to be written.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (data,) if x is not None)
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.write({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.write()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
