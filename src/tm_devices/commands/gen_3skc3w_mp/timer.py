# pyright: reportConstantRedefinition=none
"""The timer commands module.

These commands are used in the following models:
MP5103

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - timer.cleartime()
    - timer.measure.t()
    - timer.readtime()
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
        - ``.cleartime()``: The ``timer.cleartime()`` function.
        - ``.measure``: The ``timer.measure`` command tree.
        - ``.readtime()``: The ``timer.readtime()`` function.
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

    def cleartime(self) -> str:
        """Run the ``timer.cleartime()`` function.

        Description:
            - This function resets the timer to zero (0) seconds.

        TSP Syntax:
            ```
            - timer.cleartime()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.cleartime())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.cleartime()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def readtime(self) -> str:
        """Run the ``timer.readtime()`` function.

        Description:
            - This function measures the elapsed time since the timer was last reset.

        TSP Syntax:
            ```
            - timer.readtime()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.readtime())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.readtime()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
