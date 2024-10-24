# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The eventlog commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - eventlog.all()
    - eventlog.clear()
    - eventlog.count
    - eventlog.enable
    - eventlog.next()
    - eventlog.overwritemethod
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Eventlog(BaseTSPCmd):
    """The ``eventlog`` command tree.

    Properties and methods:
        - ``.all()``: The ``eventlog.all()`` function.
        - ``.clear()``: The ``eventlog.clear()`` function.
        - ``.count``: The ``eventlog.count`` attribute.
        - ``.enable``: The ``eventlog.enable`` attribute.
        - ``.next()``: The ``eventlog.next()`` function.
        - ``.overwritemethod``: The ``eventlog.overwritemethod`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "eventlog") -> None:
        super().__init__(device, cmd_syntax)

    @property
    def count(self) -> str:
        """Access the ``eventlog.count`` attribute.

        Description:
            - This attribute returns the number of unread events in the event log.

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

    @property
    def enable(self) -> str:
        """Access the ``eventlog.enable`` attribute.

        Description:
            - This attribute enables or disables the event log.

        Usage:
            - Accessing this property will send the ``print(eventlog.enable)`` query.
            - Setting this property to a value will send the ``eventlog.enable = value`` command.

        TSP Syntax:
            ```
            - eventlog.enable = value
            - print(eventlog.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``eventlog.enable`` attribute.

        Description:
            - This attribute enables or disables the event log.

        Usage:
            - Accessing this property will send the ``print(eventlog.enable)`` query.
            - Setting this property to a value will send the ``eventlog.enable = value`` command.

        TSP Syntax:
            ```
            - eventlog.enable = value
            - print(eventlog.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def overwritemethod(self) -> str:
        """Access the ``eventlog.overwritemethod`` attribute.

        Description:
            - This attribute controls how the event log processes events if the event log is full.

        Usage:
            - Accessing this property will send the ``print(eventlog.overwritemethod)`` query.
            - Setting this property to a value will send the ``eventlog.overwritemethod = value``
              command.

        TSP Syntax:
            ```
            - eventlog.overwritemethod = value
            - print(eventlog.overwritemethod)
            ```

        Info:
            - ``method``, the set to one of the following values:

                * 0 or eventlog.DISCARD_NEWEST: New entries are not logged
                * 1 or eventlog.DISCARD_OLDEST: Old entries are deleted as new events are logged.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".overwritemethod"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.overwritemethod)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.overwritemethod`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @overwritemethod.setter
    def overwritemethod(self, value: Union[str, float]) -> None:
        """Access the ``eventlog.overwritemethod`` attribute.

        Description:
            - This attribute controls how the event log processes events if the event log is full.

        Usage:
            - Accessing this property will send the ``print(eventlog.overwritemethod)`` query.
            - Setting this property to a value will send the ``eventlog.overwritemethod = value``
              command.

        TSP Syntax:
            ```
            - eventlog.overwritemethod = value
            - print(eventlog.overwritemethod)
            ```

        Info:
            - ``method``, the set to one of the following values:

                * 0 or eventlog.DISCARD_NEWEST: New entries are not logged
                * 1 or eventlog.DISCARD_OLDEST: Old entries are deleted as new events are logged.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".overwritemethod", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.overwritemethod = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.overwritemethod`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def all(self) -> str:
        """Run the ``eventlog.all()`` function.

        Description:
            - This function returns all entries from the event log as a single string and removes
              them from the event log.

        TSP Syntax:
            ```
            - eventlog.all()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.all())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.all()`` function."  # noqa: E501
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
            - This function returns the oldest unread event message from the event log.

        TSP Syntax:
            ```
            - eventlog.next()
            ```

        Args:
            event_type (optional): Limits the return to specific event log types; set a cumulative
                integer value that represents the event log types to.

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
