# pyright: reportConstantRedefinition=none
"""The firmware commands module.

These commands are used in the following models:
MP5103

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - firmware.load()
    - firmware.update()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Firmware(BaseTSPCmd):
    """The ``firmware`` command tree.

    Properties and methods:
        - ``.load()``: The ``firmware.load()`` function.
        - ``.update()``: The ``firmware.update()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "firmware") -> None:
        super().__init__(device, cmd_syntax)

    def load(self, filename: str) -> None:
        """Run the ``firmware.load()`` function.

        Description:
            - This function loads a firmware image file from a USB flash drive.

        TSP Syntax:
            ```
            - firmware.load()
            ```

        Args:
            filename: Name of the firmware image file to load.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.load({filename})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.load()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def update(self) -> None:
        """Run the ``firmware.update()`` function.

        Description:
            - This function updates the mainframe with a firmware image.

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
