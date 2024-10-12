# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The beeper commands module.

These commands are used in the following models:
DAQ6510, DMM6500, DMM7510, SMU2450, SMU2460, SMU2461, SMU2470

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - beeper.beep()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Beeper(BaseTSPCmd):
    """The ``beeper`` command tree.

    Properties and methods:
        - ``.beep()``: The ``beeper.beep()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "beeper") -> None:
        super().__init__(device, cmd_syntax)

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
