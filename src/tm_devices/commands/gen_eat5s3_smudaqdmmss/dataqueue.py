# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The dataqueue commands module.

These commands are used in the following models:
DAQ6510, DMM6500, DMM7510, SMU2450, SMU2460, SMU2461, SMU2470, SMU2601B, SMU2602B, SMU2604B,
SMU2606B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B, SMU2651A, SMU2657A, SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - dataqueue.add()
    - dataqueue.clear()
    - dataqueue.count
    - dataqueue.next()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Dataqueue(BaseTSPCmd):
    """The ``dataqueue`` command tree.

    Constants:
        - ``.CAPACITY``: The maximum number of entries that you can store in the data queue.

    Properties and methods:
        - ``.add()``: The ``dataqueue.add()`` function.
        - ``.clear()``: The ``dataqueue.clear()`` function.
        - ``.count``: The ``dataqueue.count`` attribute.
        - ``.next()``: The ``dataqueue.next()`` function.
    """

    CAPACITY = "dataqueue.CAPACITY"
    """str: The maximum number of entries that you can store in the data queue."""

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "dataqueue"
    ) -> None:
        super().__init__(device, cmd_syntax)

    @property
    def count(self) -> str:
        """Access the ``dataqueue.count`` attribute.

        Description:
            - This attribute contains the number of items in the data queue.

        Usage:
            - Accessing this property will send the ``print(dataqueue.count)`` query.

        TSP Syntax:
            ```
            - print(dataqueue.count)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".count"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.count)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def add(self, value: str, timeout: Optional[float] = None) -> str:
        """Run the ``dataqueue.add()`` function.

        Description:
            - This function adds an entry to the data queue.

        TSP Syntax:
            ```
            - dataqueue.add()
            ```

        Args:
            value: The data item to add; value can be of any type.
            timeout (optional): The maximum number of seconds to wait for space in the data queue.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    value,
                    timeout,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.add({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.add()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def clear(self) -> None:
        """Run the ``dataqueue.clear()`` function.

        Description:
            - This function clears the data queue.

        TSP Syntax:
            ```
            - dataqueue.clear()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.clear()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.clear()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def next(self, timeout: Optional[float] = None) -> str:
        """Run the ``dataqueue.next()`` function.

        Description:
            - This function removes the next entry from the data queue.

        TSP Syntax:
            ```
            - dataqueue.next()
            ```

        Args:
            timeout (optional): The number of seconds to wait for data in the queue.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (timeout,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.next({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.next()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
