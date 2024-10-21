# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The timer commands module.

These commands are used in the following models:
DAQ6510, DMM6500, DMM7510, SMU2450, SMU2460, SMU2461, SMU2470

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - timer.cleartime()
    - timer.gettime()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Timer(BaseTSPCmd):
    """The ``timer`` command tree.

    Properties and methods:
        - ``.cleartime()``: The ``timer.cleartime()`` function.
        - ``.gettime()``: The ``timer.gettime()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "timer") -> None:
        super().__init__(device, cmd_syntax)

    def cleartime(self) -> None:
        """Run the ``timer.cleartime()`` function.

        Description:
            - This function resets the timer to zero (0) seconds.

        TSP Syntax:
            ```
            - timer.cleartime()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.cleartime()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.cleartime()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def gettime(self) -> str:
        """Run the ``timer.gettime()`` function.

        Description:
            - This function measures the elapsed time since the timer was last cleared.

        TSP Syntax:
            ```
            - timer.gettime()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.gettime())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.gettime()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
