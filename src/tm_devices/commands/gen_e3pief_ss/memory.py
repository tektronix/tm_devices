# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The memory commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - memory.available()
    - memory.used()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Memory(BaseTSPCmd):
    """The ``memory`` command tree.

    Properties and methods:
        - ``.available()``: The ``memory.available()`` function.
        - ``.used()``: The ``memory.used()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "memory") -> None:
        super().__init__(device, cmd_syntax)

    def available(self) -> str:
        """Run the ``memory.available()`` function.

        Description:
            - This function reads and returns the amount of memory that is available in the
              instrument overall for storing user scripts and channel patterns and for user-defined
              DMM configurations.

        TSP Syntax:
            ```
            - memory.available()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.available())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.available()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def used(self) -> str:
        """Run the ``memory.used()`` function.

        Description:
            - This function reports the amount of memory used in the instrument overall and for user
              scripts, storing channel patterns, and storing user DMM configurations.

        TSP Syntax:
            ```
            - memory.used()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.used())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.used()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
