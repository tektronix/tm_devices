# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The file commands module.

These commands are used in the following models:
DAQ6510, DMM6500, DMM7510, SMU2450, SMU2460, SMU2461, SMU2470

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - file.close()
    - file.flush()
    - file.mkdir()
    - file.open()
    - file.read()
    - file.usbdriveexists()
    - file.write()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class File(BaseTSPCmd):
    """The ``file`` command tree.

    Constants:
        - ``.MODE_APPEND``: Append the file.
        - ``.MODE_READ``: Read the file.
        - ``.MODE_WRITE``: Write to the file.
        - ``.READ_ALL``: Return the whole file, starting at the present position; returns nil if the
          present file position is at the end of the file.
        - ``.READ_LINE``: Return the next line; returns nil if the present file position is at the
          end of the file.
        - ``.READ_NUMBER``: Return a string that represents the number found; returns an event
          string if no number was found; returns nil if the current file position is at the end of
          file.

    Properties and methods:
        - ``.close()``: The ``file.close()`` function.
        - ``.flush()``: The ``file.flush()`` function.
        - ``.mkdir()``: The ``file.mkdir()`` function.
        - ``.open()``: The ``file.open()`` function.
        - ``.read()``: The ``file.read()`` function.
        - ``.usbdriveexists()``: The ``file.usbdriveexists()`` function.
        - ``.write()``: The ``file.write()`` function.
    """

    MODE_APPEND = "file.MODE_APPEND"
    """str: Append the file."""
    MODE_READ = "file.MODE_READ"
    """str: Read the file."""
    MODE_WRITE = "file.MODE_WRITE"
    """str: Write to the file."""
    READ_ALL = "file.READ_ALL"
    """str: Return the whole file, starting at the present position; returns nil if the present file position is at the end of the file."""  # noqa: E501
    READ_LINE = "file.READ_LINE"
    """str: Return the next line; returns nil if the present file position is at the end of the file."""  # noqa: E501
    READ_NUMBER = "file.READ_NUMBER"
    """str: Return a string that represents the number found; returns an event string if no number was found; returns nil if the current file position is at the end of file."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "file") -> None:
        super().__init__(device, cmd_syntax)

    def close(self, file_number: int) -> None:
        """Run the ``file.close()`` function.

        Description:
            - This function closes a file on the USB flash drive.

        TSP Syntax:
            ```
            - file.close()
            ```

        Args:
            file_number: The file number returned from the file.open() function to close.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.close({file_number})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.close()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def flush(self, file_number: int) -> None:
        """Run the ``file.flush()`` function.

        Description:
            - This function writes buffering data to a file on the USB flash drive.

        TSP Syntax:
            ```
            - file.flush()
            ```

        Args:
            file_number: The file number returned from the file.open() function to flush.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.flush({file_number})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.flush()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def mkdir(self, path: str) -> None:
        """Run the ``file.mkdir()`` function.

        Description:
            - This function creates a directory at the specified path on the USB flash drive.

        TSP Syntax:
            ```
            - file.mkdir()
            ```

        Args:
            path: A string that contains the path of the directory.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.mkdir("{path}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.mkdir()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def open(self, file_name: str, access_type: str) -> str:
        """Run the ``file.open()`` function.

        Description:
            - This function opens a file on the USB flash drive for later reference.

        TSP Syntax:
            ```
            - file.open()
            ```

        Args:
            file_name: A string that contains the file name to open, including the full path of
                file.
            access_type: The type of action to do.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.open("{file_name}", {access_type}))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.open()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def read(self, file_number: int, read_action: str) -> str:
        """Run the ``file.read()`` function.

        Description:
            - This function reads data from a file on the USB flash drive.

        TSP Syntax:
            ```
            - file.read()
            ```

        Args:
            file_number: The file number returned from the file.open() function to read.
            read_action: The action.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.read({file_number}, {read_action}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.read()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def usbdriveexists(self) -> str:
        """Run the ``file.usbdriveexists()`` function.

        Description:
            - This function detects if a USB flash drive is inserted into the front-panel USB port.

        TSP Syntax:
            ```
            - file.usbdriveexists()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.usbdriveexists())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.usbdriveexists()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def write(self, file_number: int, string: str) -> None:
        """Run the ``file.write()`` function.

        Description:
            - This function writes data to a file on the USB flash drive.

        TSP Syntax:
            ```
            - file.write()
            ```

        Args:
            file_number: The file number returned from the file.open() function to write.
            string: A string that contains the data to write to the file.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.write({file_number}, "{string}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.write()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
