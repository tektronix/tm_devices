# pyright: reportConstantRedefinition=none
"""The usbtmc commands module.

These commands are used in the following models:
MP5103

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - usbtmc.access
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Usbtmc(BaseTSPCmd):
    """The ``usbtmc`` command tree.

    Properties and methods:
        - ``.access``: The ``usbtmc.access`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "usbtmc") -> None:
        super().__init__(device, cmd_syntax)

    @property
    def access(self) -> str:
        """Access the ``usbtmc.access`` attribute.

        Description:
            - This command is used to enable or disable the mainframe rear panel USB port access.

        Usage:
            - Accessing this property will send the ``print(usbtmc.access)`` query.
            - Setting this property to a value will send the ``usbtmc.access = value`` command.

        TSP Syntax:
            ```
            - usbtmc.access = value
            - print(usbtmc.access)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".access"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.access)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.access`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @access.setter
    def access(self, value: Union[str, float]) -> None:
        """Access the ``usbtmc.access`` attribute.

        Description:
            - This command is used to enable or disable the mainframe rear panel USB port access.

        Usage:
            - Accessing this property will send the ``print(usbtmc.access)`` query.
            - Setting this property to a value will send the ``usbtmc.access = value`` command.

        TSP Syntax:
            ```
            - usbtmc.access = value
            - print(usbtmc.access)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".access", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.access = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.access`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
