# pyright: reportConstantRedefinition=none
"""The firmware commands module.

These commands are used in the following models:
MPSU50_2ST, MSMU60_2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - firmware.update()
    - firmware.verify()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Firmware(BaseTSPCmd):
    """The ``firmware`` command tree.

    Properties and methods:
        - ``.update()``: The ``firmware.update()`` function.
        - ``.verify()``: The ``firmware.verify()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "firmware") -> None:
        super().__init__(device, cmd_syntax)

    def update(self) -> None:
        """Run the ``firmware.update()`` function.

        Description:
            - This function flashes a firmware image of a module installed in a slot after the image
              has been downloaded to the mainframe.

        TSP Syntax:
            ```
            - firmware.update()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.update()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.update()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def verify(self) -> str:
        """Run the ``firmware.verify()`` function.

        Description:
            - This function verifys that an image downloaded to the mainframe is the exact firmware
              flashed onto a module.

        TSP Syntax:
            ```
            - firmware.verify()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.verify())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.verify()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
