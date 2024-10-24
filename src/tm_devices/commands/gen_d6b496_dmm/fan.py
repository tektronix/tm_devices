# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The fan commands module.

These commands are used in the following models:
DMM7510

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - fan.level
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Fan(BaseTSPCmd):
    """The ``fan`` command tree.

    Properties and methods:
        - ``.level``: The ``fan.level`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "fan") -> None:
        super().__init__(device, cmd_syntax)

    @property
    def level(self) -> str:
        """Access the ``fan.level`` attribute.

        Description:
            - This attribute sets the speed of the instrument fan.

        Usage:
            - Accessing this property will send the ``print(fan.level)`` query.
            - Setting this property to a value will send the ``fan.level = value`` command.

        TSP Syntax:
            ```
            - fan.level = value
            - print(fan.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".level"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.level)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @level.setter
    def level(self, value: Union[str, float]) -> None:
        """Access the ``fan.level`` attribute.

        Description:
            - This attribute sets the speed of the instrument fan.

        Usage:
            - Accessing this property will send the ``print(fan.level)`` query.
            - Setting this property to a value will send the ``fan.level = value`` command.

        TSP Syntax:
            ```
            - fan.level = value
            - print(fan.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".level", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.level = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
