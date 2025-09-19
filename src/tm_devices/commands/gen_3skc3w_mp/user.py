# pyright: reportConstantRedefinition=none
"""The user commands module.

These commands are used in the following models:
MP5103

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - user.password.change
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class UserPassword(BaseTSPCmd):
    """The ``user.password`` command tree.

    Properties and methods:
        - ``.change``: The ``user.password.change`` attribute.
    """

    @property
    def change(self) -> str:
        """Access the ``user.password.change`` attribute.

        Description:
            - This attribute is used to add or change the login password.

        Usage:
            - Accessing this property will send the ``print(user.password.change)`` query.
            - Setting this property to a value will send the ``user.password.change = value``
              command.

        TSP Syntax:
            ```
            - user.password.change = value
            - print(user.password.change)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".change"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.change)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.change`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @change.setter
    def change(self, value: Union[str, float]) -> None:
        """Access the ``user.password.change`` attribute.

        Description:
            - This attribute is used to add or change the login password.

        Usage:
            - Accessing this property will send the ``print(user.password.change)`` query.
            - Setting this property to a value will send the ``user.password.change = value``
              command.

        TSP Syntax:
            ```
            - user.password.change = value
            - print(user.password.change)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".change", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.change = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.change`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class User(BaseTSPCmd):
    """The ``user`` command tree.

    Properties and methods:
        - ``.password``: The ``user.password`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "user") -> None:
        super().__init__(device, cmd_syntax)
        self._password = UserPassword(device, f"{self._cmd_syntax}.password")

    @property
    def password(self) -> UserPassword:
        """Return the ``user.password`` command tree.

        Sub-properties and sub-methods:
            - ``.change``: The ``user.password.change`` attribute.
        """
        return self._password
