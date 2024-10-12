# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The tsplink commands module.

These commands are used in the following models:
DAQ6510

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - tsplink.group
    - tsplink.initialize()
    - tsplink.line[N].reset()
    - tsplink.line[N].state
    - tsplink.master
    - tsplink.node
    - tsplink.readport()
    - tsplink.state
    - tsplink.writeport()
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


class TsplinkLineItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``tsplink.line[N]`` command tree.

    Info:
        - ``N``, the trigger line (1 to 3).

    Properties and methods:
        - ``.reset()``: The ``tsplink.line[N].reset()`` function.
        - ``.state``: The ``tsplink.line[N].state`` attribute.
    """

    @property
    def state(self) -> str:
        """Access the ``tsplink.line[N].state`` attribute.

        Description:
            - This attribute reads or writes the digital state of a TSP-Link synchronization line.

        Usage:
            - Accessing this property will send the ``print(tsplink.line[N].state)`` query.
            - Setting this property to a value will send the ``tsplink.line[N].state = value``
              command.

        TSP Syntax:
            ```
            - tsplink.line[N].state = value
            - print(tsplink.line[N].state)
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

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
        """Access the ``tsplink.line[N].state`` attribute.

        Description:
            - This attribute reads or writes the digital state of a TSP-Link synchronization line.

        Usage:
            - Accessing this property will send the ``print(tsplink.line[N].state)`` query.
            - Setting this property to a value will send the ``tsplink.line[N].state = value``
              command.

        TSP Syntax:
            ```
            - tsplink.line[N].state = value
            - print(tsplink.line[N].state)
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

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
        """Run the ``tsplink.line[N].reset()`` function.

        Description:
            - This function resets some of the TSP-Link trigger attributes to their factory
              defaults.

        TSP Syntax:
            ```
            - tsplink.line[N].reset()
            ```

        Info:
            - ``N``, the trigger line (1 to 3).

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


class Tsplink(BaseTSPCmd):
    """The ``tsplink`` command tree.

    Constants:
        - ``.MODE_DIGITAL_OPEN_DRAIN``: TSP-Link digital open drain line.
        - ``.MODE_SYNCHRONOUS_ACCEPTOR``: TSP-Link trigger synchronous acceptor.
        - ``.MODE_SYNCHRONOUS_MASTER``: TSP-Link trigger synchronous master.
        - ``.MODE_TRIGGER_OPEN_DRAIN``: TSP-Link trigger open drain line.
        - ``.STATE_HIGH``: High state of the synchronization line.
        - ``.STATE_LOW``: Low state of the synchronization line.

    Properties and methods:
        - ``.group``: The ``tsplink.group`` attribute.
        - ``.initialize()``: The ``tsplink.initialize()`` function.
        - ``.line``: The ``tsplink.line[N]`` command tree.
        - ``.master``: The ``tsplink.master`` attribute.
        - ``.node``: The ``tsplink.node`` attribute.
        - ``.readport()``: The ``tsplink.readport()`` function.
        - ``.state``: The ``tsplink.state`` attribute.
        - ``.writeport()``: The ``tsplink.writeport()`` function.
    """

    MODE_DIGITAL_OPEN_DRAIN = "tsplink.MODE_DIGITAL_OPEN_DRAIN"
    """str: TSP-Link digital open drain line."""
    MODE_SYNCHRONOUS_ACCEPTOR = "tsplink.MODE_SYNCHRONOUS_ACCEPTOR"
    """str: TSP-Link trigger synchronous acceptor."""
    MODE_SYNCHRONOUS_MASTER = "tsplink.MODE_SYNCHRONOUS_MASTER"
    """str: TSP-Link trigger synchronous master."""
    MODE_TRIGGER_OPEN_DRAIN = "tsplink.MODE_TRIGGER_OPEN_DRAIN"
    """str: TSP-Link trigger open drain line."""
    STATE_HIGH = "tsplink.STATE_HIGH"
    """str: High state of the synchronization line."""
    STATE_LOW = "tsplink.STATE_LOW"
    """str: Low state of the synchronization line."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "tsplink") -> None:
        super().__init__(device, cmd_syntax)
        self._line: Dict[int, TsplinkLineItem] = DefaultDictPassKeyToFactory(
            lambda x: TsplinkLineItem(device, f"{self._cmd_syntax}.line[{x}]")
        )

    @property
    def group(self) -> str:
        """Access the ``tsplink.group`` attribute.

        Description:
            - This attribute contains the group number of a TSP-Link node.

        Usage:
            - Accessing this property will send the ``print(tsplink.group)`` query.
            - Setting this property to a value will send the ``tsplink.group = value`` command.

        TSP Syntax:
            ```
            - tsplink.group = value
            - print(tsplink.group)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".group"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.group)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.group`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @group.setter
    def group(self, value: Union[str, float]) -> None:
        """Access the ``tsplink.group`` attribute.

        Description:
            - This attribute contains the group number of a TSP-Link node.

        Usage:
            - Accessing this property will send the ``print(tsplink.group)`` query.
            - Setting this property to a value will send the ``tsplink.group = value`` command.

        TSP Syntax:
            ```
            - tsplink.group = value
            - print(tsplink.group)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".group", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.group = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.group`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def line(self) -> Dict[int, TsplinkLineItem]:
        """Return the ``tsplink.line[N]`` command tree.

        Info:
            - ``N``, the trigger line (1 to 3).

        Sub-properties and sub-methods:
            - ``.reset()``: The ``tsplink.line[N].reset()`` function.
            - ``.state``: The ``tsplink.line[N].state`` attribute.
        """
        return self._line

    @property
    def master(self) -> str:
        """Access the ``tsplink.master`` attribute.

        Description:
            - This attribute reads the node number assigned to the master node.

        Usage:
            - Accessing this property will send the ``print(tsplink.master)`` query.

        TSP Syntax:
            ```
            - print(tsplink.master)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".master"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.master)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.master`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def node(self) -> str:
        """Access the ``tsplink.node`` attribute.

        Description:
            - This attribute defines the node number.

        Usage:
            - Accessing this property will send the ``print(tsplink.node)`` query.
            - Setting this property to a value will send the ``tsplink.node = value`` command.

        TSP Syntax:
            ```
            - tsplink.node = value
            - print(tsplink.node)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".node"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.node)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.node`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @node.setter
    def node(self, value: Union[str, float]) -> None:
        """Access the ``tsplink.node`` attribute.

        Description:
            - This attribute defines the node number.

        Usage:
            - Accessing this property will send the ``print(tsplink.node)`` query.
            - Setting this property to a value will send the ``tsplink.node = value`` command.

        TSP Syntax:
            ```
            - tsplink.node = value
            - print(tsplink.node)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".node", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.node = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.node`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def state(self) -> str:
        """Access the ``tsplink.state`` attribute.

        Description:
            - This attribute describes the TSP-Link online state.

        Usage:
            - Accessing this property will send the ``print(tsplink.state)`` query.

        TSP Syntax:
            ```
            - print(tsplink.state)
            ```

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

    def initialize(self, expected_nodes: Optional[int] = None) -> str:
        """Run the ``tsplink.initialize()`` function.

        Description:
            - This function initializes all instruments and enclosures in the TSP-Link system.

        TSP Syntax:
            ```
            - tsplink.initialize()
            ```

        Args:
            expected_nodes (optional): The number of nodes expected on the system (1 to 32).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (expected_nodes,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.initialize({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.initialize()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def readport(self) -> str:
        """Run the ``tsplink.readport()`` function.

        Description:
            - This function reads the TSP-Link trigger lines as a digital I/O port.

        TSP Syntax:
            ```
            - tsplink.readport()
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
        """Run the ``tsplink.writeport()`` function.

        Description:
            - This function writes to all TSP-Link synchronization lines as a digital I/O port.

        TSP Syntax:
            ```
            - tsplink.writeport()
            ```

        Args:
            data: Value to write to the port (0 to 7).

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
