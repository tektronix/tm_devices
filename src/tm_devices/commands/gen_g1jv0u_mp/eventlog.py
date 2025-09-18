# pyright: reportConstantRedefinition=none
"""The eventlog commands module.

These commands are used in the following models:
MP5103

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - eventlog.clear()
    - eventlog.count
    - eventlog.next()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Eventlog(BaseTSPCmd):
    """The ``eventlog`` command tree.

    Properties and methods:
        - ``.clear()``: The ``eventlog.clear()`` function.
        - ``.count``: The ``eventlog.count`` attribute.
        - ``.next()``: The ``eventlog.next()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "eventlog") -> None:
        super().__init__(device, cmd_syntax)

    @property
    def count(self) -> str:
        """Access the ``eventlog.count`` attribute.

        Description:
            - This attribute stores the number of events in the event log.

        Usage:
            - Accessing this property will send the ``print(eventlog.count)`` query.

        TSP Syntax:
            ```
            - print(eventlog.count)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".count"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.count)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def clear(self) -> None:
        """Run the ``eventlog.clear()`` function.

        Description:
            - This function clears the event log.

        TSP Syntax:
            ```
            - eventlog.clear()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.clear()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.clear()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def next(self, event_type: Optional[str] = None) -> str:
        """Run the ``eventlog.next()`` function.

        Description:
            - This function reads and returns the oldest unread event message from the event log,
              which is then removed from the event log.

        TSP Syntax:
            ```
            - eventlog.next()
            ```

        Args:
            event_type (optional): Limits the return to specific event log types.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (event_type,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.next({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.next()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
