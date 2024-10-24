# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The upgrade commands module.

These commands are used in the following models:
SMU2470

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - upgrade.previous()
    - upgrade.unit()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Upgrade(BaseTSPCmd):
    """The ``upgrade`` command tree.

    Properties and methods:
        - ``.previous()``: The ``upgrade.previous()`` function.
        - ``.unit()``: The ``upgrade.unit()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "upgrade") -> None:
        super().__init__(device, cmd_syntax)

    def previous(self) -> str:
        """Run the ``upgrade.previous()`` function.

        Description:
            - This function returns to a previous version of the 2470 firmware.

        TSP Syntax:
            ```
            - upgrade.previous()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.previous())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.previous()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def unit(self) -> None:
        """Run the ``upgrade.unit()`` function.

        Description:
            - This function upgrades the 2470 firmware.

        TSP Syntax:
            ```
            - upgrade.unit()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.unit()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.unit()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
