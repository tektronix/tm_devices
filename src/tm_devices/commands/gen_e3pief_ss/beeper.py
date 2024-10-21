# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The beeper commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - beeper.beep()
    - beeper.enable
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Beeper(BaseTSPCmd):
    """The ``beeper`` command tree.

    Properties and methods:
        - ``.beep()``: The ``beeper.beep()`` function.
        - ``.enable``: The ``beeper.enable`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "beeper") -> None:
        super().__init__(device, cmd_syntax)

    @property
    def enable(self) -> str:
        """Access the ``beeper.enable`` attribute.

        Description:
            - This command allows you to turn the beeper on or off.

        Usage:
            - Accessing this property will send the ``print(beeper.enable)`` query.
            - Setting this property to a value will send the ``beeper.enable = value`` command.

        TSP Syntax:
            ```
            - beeper.enable = value
            - print(beeper.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``beeper.enable`` attribute.

        Description:
            - This command allows you to turn the beeper on or off.

        Usage:
            - Accessing this property will send the ``print(beeper.enable)`` query.
            - Setting this property to a value will send the ``beeper.enable = value`` command.

        TSP Syntax:
            ```
            - beeper.enable = value
            - print(beeper.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def beep(self, duration: float, frequency: float) -> None:
        """Run the ``beeper.beep()`` function.

        Description:
            - This function generates an audible tone.

        TSP Syntax:
            ```
            - beeper.beep()
            ```

        Args:
            duration: The amount of time to play the tone (0.001 s to 100 s).
            frequency: The frequency of the beep (20 Hz to 8000 Hz).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.beep({duration}, {frequency})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.beep()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
