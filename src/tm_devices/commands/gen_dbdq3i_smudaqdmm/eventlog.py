# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The eventlog commands module.

These commands are used in the following models:
DAQ6510, DMM6500, DMM7510, SMU2450, SMU2460, SMU2461, SMU2470

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - eventlog.clear()
    - eventlog.getcount()
    - eventlog.next()
    - eventlog.post()
    - eventlog.save()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Eventlog(BaseTSPCmd):
    """The ``eventlog`` command tree.

    Constants:
        - ``.SEV_ALL``: Returns the total number of unread events in the event log.
        - ``.SEV_ERROR``: Returns the number of error events in the event log.
        - ``.SEV_INFO``: Returns the number of information messages in the event log.
        - ``.SEV_WARN``: Returns the number of warnings in the event log.

    Properties and methods:
        - ``.clear()``: The ``eventlog.clear()`` function.
        - ``.getcount()``: The ``eventlog.getcount()`` function.
        - ``.next()``: The ``eventlog.next()`` function.
        - ``.post()``: The ``eventlog.post()`` function.
        - ``.save()``: The ``eventlog.save()`` function.
    """

    SEV_ALL = "eventlog.SEV_ALL"
    """str: Returns the total number of unread events in the event log."""
    SEV_ERROR = "eventlog.SEV_ERROR"
    """str: Returns the number of error events in the event log."""
    SEV_INFO = "eventlog.SEV_INFO"
    """str: Returns the number of information messages in the event log."""
    SEV_WARN = "eventlog.SEV_WARN"
    """str: Returns the number of warnings in the event log."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "eventlog") -> None:
        super().__init__(device, cmd_syntax)

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

    def getcount(self, event_type: Optional[str] = None) -> str:
        """Run the ``eventlog.getcount()`` function.

        Description:
            - This function returns the number of unread events in the event log.

        TSP Syntax:
            ```
            - eventlog.getcount()
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
                f"print({self._cmd_syntax}.getcount({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getcount()`` function."  # noqa: E501
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

    def post(self, message: str, event_type: Optional[str] = None) -> None:
        """Run the ``eventlog.post()`` function.

        Description:
            - This function allows you to post your own text to the event log.

        TSP Syntax:
            ```
            - eventlog.post()
            ```

        Args:
            message: String that contains the message.
            event_type (optional): The type of event; if no event is defined, defaults to
                eventlog.SEV_INFO.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{message}"',
                    event_type,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.post({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.post()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def save(self, filename: str, event_type: Optional[str] = None) -> None:
        """Run the ``eventlog.save()`` function.

        Description:
            - This function saves the event log to a file on a USB flash drive.

        TSP Syntax:
            ```
            - eventlog.save()
            ```

        Args:
            filename: A string that represents the name of the file to be saved.
            event_type (optional): Limits the return to specific event log types; set a cumulative
                integer value that represents the event log types to.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{filename}"',
                    event_type,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.save({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.save()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
