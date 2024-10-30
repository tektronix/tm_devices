# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The errorqueue commands module.

These commands are used in the following models:
SMU2601B_Pulse

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - errorqueue.next()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Errorqueue(BaseTSPCmd):
    """The ``errorqueue`` command tree.

    Properties and methods:
        - ``.next()``: The ``errorqueue.next()`` function.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "errorqueue"
    ) -> None:
        super().__init__(device, cmd_syntax)

    def next(self) -> str:
        """Run the ``errorqueue.next()`` function.

        Description:
            - This function reads the oldest entry from the error queue and removes it from the
              queue.

        TSP Syntax:
            ```
            - errorqueue.next()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.next())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.next()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
