# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The timer commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2604B, SMU2606B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B,
SMU2651A, SMU2657A, SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - timer.measure.t()
    - timer.reset()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class TimerMeasure(BaseTSPCmd):
    """The ``timer.measure`` command tree.

    Properties and methods:
        - ``.t()``: The ``timer.measure.t()`` function.
    """

    def t(self) -> str:
        """Run the ``timer.measure.t()`` function.

        Description:
            - This function measures the elapsed time since the timer was last reset.

        TSP Syntax:
            ```
            - timer.measure.t()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.t())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.t()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Timer(BaseTSPCmd):
    """The ``timer`` command tree.

    Properties and methods:
        - ``.measure``: The ``timer.measure`` command tree.
        - ``.reset()``: The ``timer.reset()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "timer") -> None:
        super().__init__(device, cmd_syntax)
        self._measure = TimerMeasure(device, f"{self._cmd_syntax}.measure")

    @property
    def measure(self) -> TimerMeasure:
        """Return the ``timer.measure`` command tree.

        Sub-properties and sub-methods:
            - ``.t()``: The ``timer.measure.t()`` function.
        """
        return self._measure

    def reset(self) -> None:
        """Run the ``timer.reset()`` function.

        Description:
            - This function resets the timer to zero (0) seconds.

        TSP Syntax:
            ```
            - timer.reset()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.reset()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.reset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
