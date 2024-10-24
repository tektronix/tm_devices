# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The digio commands module.

These commands are used in the following models:
DAQ6510, SMU2450, SMU2460, SMU2461, SMU2470

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - digio.line[N].mode
    - digio.line[N].reset()
    - digio.line[N].state
    - digio.readport()
    - digio.writeport()
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from ..helpers import (
    BaseTSPCmd,
    DefaultDictPassKeyToFactory,
    NoDeviceProvidedError,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class DigioLineItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``digio.line[N]`` command tree.

    Info:
        - ``N``, the digital I/O line: 1 to 6.

    Properties and methods:
        - ``.mode``: The ``digio.line[N].mode`` attribute.
        - ``.reset()``: The ``digio.line[N].reset()`` function.
        - ``.state``: The ``digio.line[N].state`` attribute.
    """

    @property
    def mode(self) -> str:
        """Access the ``digio.line[N].mode`` attribute.

        Description:
            - This attribute sets the mode of the digital I/O line to be a digital line, trigger
              line, or synchronous line and sets the line to be input, output, or open-drain.

        Usage:
            - Accessing this property will send the ``print(digio.line[N].mode)`` query.
            - Setting this property to a value will send the ``digio.line[N].mode = value`` command.

        TSP Syntax:
            ```
            - digio.line[N].mode = value
            - print(digio.line[N].mode)
            ```

        Info:
            - ``N``, the digital I/O line: 1 to 6.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".mode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.mode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @mode.setter
    def mode(self, value: Union[str, float]) -> None:
        """Access the ``digio.line[N].mode`` attribute.

        Description:
            - This attribute sets the mode of the digital I/O line to be a digital line, trigger
              line, or synchronous line and sets the line to be input, output, or open-drain.

        Usage:
            - Accessing this property will send the ``print(digio.line[N].mode)`` query.
            - Setting this property to a value will send the ``digio.line[N].mode = value`` command.

        TSP Syntax:
            ```
            - digio.line[N].mode = value
            - print(digio.line[N].mode)
            ```

        Info:
            - ``N``, the digital I/O line: 1 to 6.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".mode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.mode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def state(self) -> str:
        """Access the ``digio.line[N].state`` attribute.

        Description:
            - This function sets a digital I/O line high or low when the line is set for digital
              control and returns the state on the digital I/O lines.

        Usage:
            - Accessing this property will send the ``print(digio.line[N].state)`` query.
            - Setting this property to a value will send the ``digio.line[N].state = value``
              command.

        TSP Syntax:
            ```
            - digio.line[N].state = value
            - print(digio.line[N].state)
            ```

        Info:
            - ``N``, the digital I/O line: 1 to 6.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".state"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.state)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.state`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @state.setter
    def state(self, value: Union[str, float]) -> None:
        """Access the ``digio.line[N].state`` attribute.

        Description:
            - This function sets a digital I/O line high or low when the line is set for digital
              control and returns the state on the digital I/O lines.

        Usage:
            - Accessing this property will send the ``print(digio.line[N].state)`` query.
            - Setting this property to a value will send the ``digio.line[N].state = value``
              command.

        TSP Syntax:
            ```
            - digio.line[N].state = value
            - print(digio.line[N].state)
            ```

        Info:
            - ``N``, the digital I/O line: 1 to 6.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".state", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.state = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.state`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def reset(self) -> None:
        """Run the ``digio.line[N].reset()`` function.

        Description:
            - This function resets digital I/O line values to their factory defaults.

        TSP Syntax:
            ```
            - digio.line[N].reset()
            ```

        Info:
            - ``N``, the digital I/O line: 1 to 6.

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


class Digio(BaseTSPCmd):
    """The ``digio`` command tree.

    Constants:
        - ``.MODE_DIGITAL_IN``: Set the digital I/O mode to digital control, input.
        - ``.MODE_DIGITAL_OPEN_DRAIN``: Set the digital I/O mode to digital control, open-drain.
        - ``.MODE_DIGITAL_OUT``: Set the digital I/O mode to digital control, output.
        - ``.MODE_SYNCHRONOUS_ACCEPTOR``: Set the digital I/O mode to synchronous acceptor.
        - ``.MODE_SYNCHRONOUS_MASTER``: Set the digital I/O mode to synchronous master.
        - ``.MODE_TRIGGER_IN``: Set the digital I/O mode to trigger control, input.
        - ``.MODE_TRIGGER_OPEN_DRAIN``: Set the digital I/O mode to trigger control, open-drain.
        - ``.MODE_TRIGGER_OUT``: Set the digital I/O mode to trigger control, output.
        - ``.STATE_HIGH``: Set the line high.
        - ``.STATE_LOW``: Set the line low.

    Properties and methods:
        - ``.line``: The ``digio.line[N]`` command tree.
        - ``.readport()``: The ``digio.readport()`` function.
        - ``.writeport()``: The ``digio.writeport()`` function.
    """

    MODE_DIGITAL_IN = "digio.MODE_DIGITAL_IN"
    """str: Set the digital I/O mode to digital control, input."""
    MODE_DIGITAL_OPEN_DRAIN = "digio.MODE_DIGITAL_OPEN_DRAIN"
    """str: Set the digital I/O mode to digital control, open-drain."""
    MODE_DIGITAL_OUT = "digio.MODE_DIGITAL_OUT"
    """str: Set the digital I/O mode to digital control, output."""
    MODE_SYNCHRONOUS_ACCEPTOR = "digio.MODE_SYNCHRONOUS_ACCEPTOR"
    """str: Set the digital I/O mode to synchronous acceptor."""
    MODE_SYNCHRONOUS_MASTER = "digio.MODE_SYNCHRONOUS_MASTER"
    """str: Set the digital I/O mode to synchronous master."""
    MODE_TRIGGER_IN = "digio.MODE_TRIGGER_IN"
    """str: Set the digital I/O mode to trigger control, input."""
    MODE_TRIGGER_OPEN_DRAIN = "digio.MODE_TRIGGER_OPEN_DRAIN"
    """str: Set the digital I/O mode to trigger control, open-drain."""
    MODE_TRIGGER_OUT = "digio.MODE_TRIGGER_OUT"
    """str: Set the digital I/O mode to trigger control, output."""
    STATE_HIGH = "digio.STATE_HIGH"
    """str: Set the line high."""
    STATE_LOW = "digio.STATE_LOW"
    """str: Set the line low."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "digio") -> None:
        super().__init__(device, cmd_syntax)
        self._line: Dict[int, DigioLineItem] = DefaultDictPassKeyToFactory(
            lambda x: DigioLineItem(device, f"{self._cmd_syntax}.line[{x}]")
        )

    @property
    def line(self) -> Dict[int, DigioLineItem]:
        """Return the ``digio.line[N]`` command tree.

        Info:
            - ``N``, the digital I/O line: 1 to 6.

        Sub-properties and sub-methods:
            - ``.mode``: The ``digio.line[N].mode`` attribute.
            - ``.reset()``: The ``digio.line[N].reset()`` function.
            - ``.state``: The ``digio.line[N].state`` attribute.
        """
        return self._line

    def readport(self) -> str:
        """Run the ``digio.readport()`` function.

        Description:
            - This function reads the digital I/O port.

        TSP Syntax:
            ```
            - digio.readport()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.readport())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.readport()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def writeport(self, data: int) -> None:
        """Run the ``digio.writeport()`` function.

        Description:
            - This function writes to all digital I/O lines.

        TSP Syntax:
            ```
            - digio.writeport()
            ```

        Args:
            data: The value to write to the port (0 to 63).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.writeport({data})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.writeport()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
