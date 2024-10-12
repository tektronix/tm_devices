# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The errorqueue commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2604B, SMU2606B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B,
SMU2651A, SMU2657A, SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - errorqueue.clear()
    - errorqueue.count
    - errorqueue.next()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Errorqueue(BaseTSPCmd):
    """The ``errorqueue`` command tree.

    Properties and methods:
        - ``.clear()``: The ``errorqueue.clear()`` function.
        - ``.count``: The ``errorqueue.count`` attribute.
        - ``.next()``: The ``errorqueue.next()`` function.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "errorqueue"
    ) -> None:
        super().__init__(device, cmd_syntax)

    @property
    def count(self) -> str:
        """Access the ``errorqueue.count`` attribute.

        Description:
            - This attribute gets the number of entries in the error queue.

        Usage:
            - Accessing this property will send the ``print(errorqueue.count)`` query.

        TSP Syntax:
            ```
            - print(errorqueue.count)
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

    def clear(self) -> None:
        """Run the ``errorqueue.clear()`` function.

        Description:
            - This function clears all entries out of the error queue.

        TSP Syntax:
            ```
            - errorqueue.clear()
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

    def next(self) -> str:
        """Run the ``errorqueue.next()`` function.

        Description:
            - This function reads the oldest entry from the error queue and removes it from the
              queue.

        TSP Syntax:
            ```
            - errorqueue.next()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.next())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.next()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
