# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The setup_1 commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - setup.poweron
    - setup.recall()
    - setup.save()
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Setup(BaseTSPCmd):
    """The ``setup`` command tree.

    Properties and methods:
        - ``.poweron``: The ``setup.poweron`` attribute.
        - ``.recall()``: The ``setup.recall()`` function.
        - ``.save()``: The ``setup.save()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "setup") -> None:
        super().__init__(device, cmd_syntax)

    @property
    def poweron(self) -> str:
        """Access the ``setup.poweron`` attribute.

        Description:
            - This attribute specifies which saved setup to recall when the instrument is turned on.

        Usage:
            - Accessing this property will send the ``print(setup.poweron)`` query.
            - Setting this property to a value will send the ``setup.poweron = value`` command.

        TSP Syntax:
            ```
            - setup.poweron = value
            - print(setup.poweron)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".poweron"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.poweron)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.poweron`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @poweron.setter
    def poweron(self, value: Union[str, float]) -> None:
        """Access the ``setup.poweron`` attribute.

        Description:
            - This attribute specifies which saved setup to recall when the instrument is turned on.

        Usage:
            - Accessing this property will send the ``print(setup.poweron)`` query.
            - Setting this property to a value will send the ``setup.poweron = value`` command.

        TSP Syntax:
            ```
            - setup.poweron = value
            - print(setup.poweron)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".poweron", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.poweron = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.poweron`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def recall(self, id_: str) -> None:
        """Run the ``setup.recall()`` function.

        Description:
            - This function recalls settings from a saved setup.

        TSP Syntax:
            ```
            - setup.recall()
            ```

        Args:
            id_: An integer or string that specifies the location of the setup to recall.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.recall({id_})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.recall()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def save(self, id_: Optional[str] = None) -> None:
        """Run the ``setup.save()`` function.

        Description:
            - This function saves the present setup as a user-saved setup.

        TSP Syntax:
            ```
            - setup.save()
            ```

        Args:
            id_ (optional): A string that specifies the path and file name to which to save the user
                setup on a USB flash drive ('/path/filename').

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x) for x in (f'"{id_}"' if id_ is not None else None,) if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.save({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.save()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
