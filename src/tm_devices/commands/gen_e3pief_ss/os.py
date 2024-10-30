# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The os commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - os.time()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Os(BaseTSPCmd):
    """The ``os`` command tree.

    Properties and methods:
        - ``.time()``: The ``os.time()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "os") -> None:
        super().__init__(device, cmd_syntax)

    def time(self, timespec: Optional[str] = None) -> str:
        """Run the ``os.time()`` function.

        Description:
            - This function generates a time value in UTC time.

        TSP Syntax:
            ```
            - os.time()
            ```

        Args:
            timespec (optional): The date and time (year, month, day, hour, and minute).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (timespec,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.time({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.time()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
