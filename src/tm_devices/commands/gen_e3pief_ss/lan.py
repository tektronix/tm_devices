# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The lan commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - lan.applysettings()
    - lan.config.dns.address[N]
    - lan.config.dns.domain
    - lan.config.dns.dynamic
    - lan.config.dns.hostname
    - lan.config.dns.verify
    - lan.config.gateway
    - lan.config.ipaddress
    - lan.config.method
    - lan.config.subnetmask
    - lan.lxidomain
    - lan.nagle
    - lan.reset()
    - lan.restoredefaults()
    - lan.status.dns.address[N]
    - lan.status.dns.name
    - lan.status.duplex
    - lan.status.gateway
    - lan.status.ipaddress
    - lan.status.macaddress
    - lan.status.port.dst
    - lan.status.port.rawsocket
    - lan.status.port.telnet
    - lan.status.port.vxi11
    - lan.status.speed
    - lan.status.subnetmask
    - lan.trigger[N].assert()
    - lan.trigger[N].clear()
    - lan.trigger[N].connect()
    - lan.trigger[N].connected
    - lan.trigger[N].disconnect()
    - lan.trigger[N].ipaddress
    - lan.trigger[N].mode
    - lan.trigger[N].overrun
    - lan.trigger[N].protocol
    - lan.trigger[N].pseudostate
    - lan.trigger[N].stimulus
    - lan.trigger[N].wait()
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from ..helpers import (
    BaseTSPCmd,
    DefaultDictDeviceCommunication,
    DefaultDictPassKeyToFactory,
    NoDeviceProvidedError,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class LanTriggerItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``lan.trigger[N]`` command tree.

    Info:
        - ``N``, the LAN event number (1 to 8).

    Constants:
        - ``.EVENT_ID``: The event identifier used to route the LAN trigger to other subsystems
          (using stimulus properties).

    Properties and methods:
        - ``.assert()``: The ``lan.trigger[N].assert()`` function.
        - ``.clear()``: The ``lan.trigger[N].clear()`` function.
        - ``.connect()``: The ``lan.trigger[N].connect()`` function.
        - ``.connected``: The ``lan.trigger[N].connected`` attribute.
        - ``.disconnect()``: The ``lan.trigger[N].disconnect()`` function.
        - ``.ipaddress``: The ``lan.trigger[N].ipaddress`` attribute.
        - ``.mode``: The ``lan.trigger[N].mode`` attribute.
        - ``.overrun``: The ``lan.trigger[N].overrun`` attribute.
        - ``.protocol``: The ``lan.trigger[N].protocol`` attribute.
        - ``.pseudostate``: The ``lan.trigger[N].pseudostate`` attribute.
        - ``.stimulus``: The ``lan.trigger[N].stimulus`` attribute.
        - ``.wait()``: The ``lan.trigger[N].wait()`` function.
    """

    EVENT_ID = "lan.trigger[N].EVENT_ID"
    """str: The event identifier used to route the LAN trigger to other subsystems (using stimulus properties)."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.EVENT_ID = self.EVENT_ID.replace(
            "[N]", f"[{self._cmd_syntax.rsplit('[', maxsplit=1)[-1].split(']', maxsplit=1)[0]}]"
        )

    @property
    def connected(self) -> str:
        """Access the ``lan.trigger[N].connected`` attribute.

        Description:
            - This attribute stores the LAN event connection state.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].connected)`` query.

        TSP Syntax:
            ```
            - print(lan.trigger[N].connected)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".connected"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.connected)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.connected`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ipaddress(self) -> str:
        """Access the ``lan.trigger[N].ipaddress`` attribute.

        Description:
            - This attribute specifies the address (in dotted-decimal format) of UDP or TCP
              listeners.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].ipaddress)`` query.
            - Setting this property to a value will send the ``lan.trigger[N].ipaddress = value``
              command.

        TSP Syntax:
            ```
            - lan.trigger[N].ipaddress = value
            - print(lan.trigger[N].ipaddress)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ipaddress"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ipaddress)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ipaddress`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ipaddress.setter
    def ipaddress(self, value: Union[str, float]) -> None:
        """Access the ``lan.trigger[N].ipaddress`` attribute.

        Description:
            - This attribute specifies the address (in dotted-decimal format) of UDP or TCP
              listeners.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].ipaddress)`` query.
            - Setting this property to a value will send the ``lan.trigger[N].ipaddress = value``
              command.

        TSP Syntax:
            ```
            - lan.trigger[N].ipaddress = value
            - print(lan.trigger[N].ipaddress)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ipaddress", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ipaddress = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ipaddress`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def mode(self) -> str:
        """Access the ``lan.trigger[N].mode`` attribute.

        Description:
            - This attribute sets the trigger operation and detection mode of the specified LAN
              event.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].mode)`` query.
            - Setting this property to a value will send the ``lan.trigger[N].mode = value``
              command.

        TSP Syntax:
            ```
            - lan.trigger[N].mode = value
            - print(lan.trigger[N].mode)
            ```

        Info:
            - ``N``, a number representing the LAN event number (1 to 8).

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
        """Access the ``lan.trigger[N].mode`` attribute.

        Description:
            - This attribute sets the trigger operation and detection mode of the specified LAN
              event.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].mode)`` query.
            - Setting this property to a value will send the ``lan.trigger[N].mode = value``
              command.

        TSP Syntax:
            ```
            - lan.trigger[N].mode = value
            - print(lan.trigger[N].mode)
            ```

        Info:
            - ``N``, a number representing the LAN event number (1 to 8).

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
    def overrun(self) -> str:
        """Access the ``lan.trigger[N].overrun`` attribute.

        Description:
            - This attribute contains the overrun status of the LAN event detector.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].overrun)`` query.

        TSP Syntax:
            ```
            - print(lan.trigger[N].overrun)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".overrun"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.overrun)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.overrun`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def protocol(self) -> str:
        """Access the ``lan.trigger[N].protocol`` attribute.

        Description:
            - This attribute sets the LAN protocol to use for sending trigger messages.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].protocol)`` query.
            - Setting this property to a value will send the ``lan.trigger[N].protocol = value``
              command.

        TSP Syntax:
            ```
            - lan.trigger[N].protocol = value
            - print(lan.trigger[N].protocol)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".protocol"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.protocol)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.protocol`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @protocol.setter
    def protocol(self, value: Union[str, float]) -> None:
        """Access the ``lan.trigger[N].protocol`` attribute.

        Description:
            - This attribute sets the LAN protocol to use for sending trigger messages.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].protocol)`` query.
            - Setting this property to a value will send the ``lan.trigger[N].protocol = value``
              command.

        TSP Syntax:
            ```
            - lan.trigger[N].protocol = value
            - print(lan.trigger[N].protocol)
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".protocol", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.protocol = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.protocol`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def pseudostate(self) -> str:
        """Access the ``lan.trigger[N].pseudostate`` attribute.

        Description:
            - This attribute sets the simulated line state for the LAN trigger.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].pseudostate)`` query.
            - Setting this property to a value will send the ``lan.trigger[N].pseudostate = value``
              command.

        TSP Syntax:
            ```
            - lan.trigger[N].pseudostate = value
            - print(lan.trigger[N].pseudostate)
            ```

        Info:
            - ``N``, a number representing the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".pseudostate"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.pseudostate)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.pseudostate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @pseudostate.setter
    def pseudostate(self, value: Union[str, float]) -> None:
        """Access the ``lan.trigger[N].pseudostate`` attribute.

        Description:
            - This attribute sets the simulated line state for the LAN trigger.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].pseudostate)`` query.
            - Setting this property to a value will send the ``lan.trigger[N].pseudostate = value``
              command.

        TSP Syntax:
            ```
            - lan.trigger[N].pseudostate = value
            - print(lan.trigger[N].pseudostate)
            ```

        Info:
            - ``N``, a number representing the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".pseudostate", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.pseudostate = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.pseudostate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def stimulus(self) -> str:
        """Access the ``lan.trigger[N].stimulus`` attribute.

        Description:
            - This attribute specifies events that cause this trigger to assert.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].stimulus)`` query.
            - Setting this property to a value will send the ``lan.trigger[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - lan.trigger[N].stimulus = value
            - print(lan.trigger[N].stimulus)
            ```

        Info:
            - ``N``, a number specifying the trigger packet over the LAN for which to set or query
              the trigger source (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".stimulus"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.stimulus)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @stimulus.setter
    def stimulus(self, value: Union[str, float]) -> None:
        """Access the ``lan.trigger[N].stimulus`` attribute.

        Description:
            - This attribute specifies events that cause this trigger to assert.

        Usage:
            - Accessing this property will send the ``print(lan.trigger[N].stimulus)`` query.
            - Setting this property to a value will send the ``lan.trigger[N].stimulus = value``
              command.

        TSP Syntax:
            ```
            - lan.trigger[N].stimulus = value
            - print(lan.trigger[N].stimulus)
            ```

        Info:
            - ``N``, a number specifying the trigger packet over the LAN for which to set or query
              the trigger source (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".stimulus", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.stimulus = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.stimulus`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def assert_(self) -> None:
        """Run the ``lan.trigger[N].assert()`` function.

        Description:
            - This function simulates the occurrence of the trigger and generates the corresponding
              event ID.

        TSP Syntax:
            ```
            - lan.trigger[N].assert()
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.assert()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.assert()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def clear(self) -> None:
        """Run the ``lan.trigger[N].clear()`` function.

        Description:
            - This function clears the event detector for a LAN trigger.

        TSP Syntax:
            ```
            - lan.trigger[N].clear()
            ```

        Info:
            - ``N``, the LAN event number (1 to 8) to clear.

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

    def connect(self) -> None:
        """Run the ``lan.trigger[N].connect()`` function.

        Description:
            - This function prepares the event generator for outgoing trigger events.

        TSP Syntax:
            ```
            - lan.trigger[N].connect()
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.connect()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.connect()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def disconnect(self) -> None:
        """Run the ``lan.trigger[N].disconnect()`` function.

        Description:
            - This function disconnects the LAN trigger.

        TSP Syntax:
            ```
            - lan.trigger[N].disconnect()
            ```

        Info:
            - ``N``, the LAN event number (1 to 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.disconnect()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.disconnect()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def wait(self, timeout: float) -> str:
        """Run the ``lan.trigger[N].wait()`` function.

        Description:
            - This function waits for an input trigger.

        TSP Syntax:
            ```
            - lan.trigger[N].wait()
            ```

        Args:
            timeout: Maximum amount of time in seconds to wait for the trigger event.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.wait({timeout}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.wait()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class LanStatusPort(BaseTSPCmd):
    """The ``lan.status.port`` command tree.

    Info:
        - ``port``, the dead socket termination socket port number.

    Properties and methods:
        - ``.dst``: The ``lan.status.port.dst`` attribute.
        - ``.rawsocket``: The ``lan.status.port.rawsocket`` attribute.
        - ``.telnet``: The ``lan.status.port.telnet`` attribute.
        - ``.vxi11``: The ``lan.status.port.vxi11`` attribute.
    """

    @property
    def dst(self) -> str:
        """Access the ``lan.status.port.dst`` attribute.

        Description:
            - This attribute contains the LAN dead socket termination port number.

        Usage:
            - Accessing this property will send the ``print(lan.status.port.dst)`` query.

        TSP Syntax:
            ```
            - print(lan.status.port.dst)
            ```

        Info:
            - ``port``, the dead socket termination socket port number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".dst"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.dst)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.dst`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rawsocket(self) -> str:
        """Access the ``lan.status.port.rawsocket`` attribute.

        Description:
            - This attribute contains the LAN raw socket connection port number.

        Usage:
            - Accessing this property will send the ``print(lan.status.port.rawsocket)`` query.

        TSP Syntax:
            ```
            - print(lan.status.port.rawsocket)
            ```

        Info:
            - ``port``, the raw socket port number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rawsocket"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rawsocket)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rawsocket`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def telnet(self) -> str:
        """Access the ``lan.status.port.telnet`` attribute.

        Description:
            - This attribute contains the LAN Telnet connection port number.

        Usage:
            - Accessing this property will send the ``print(lan.status.port.telnet)`` query.

        TSP Syntax:
            ```
            - print(lan.status.port.telnet)
            ```

        Info:
            - ``port``, the telnet port number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".telnet"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.telnet)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.telnet`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def vxi11(self) -> str:
        """Access the ``lan.status.port.vxi11`` attribute.

        Description:
            - This attribute contains the LAN VXI-11 connection port number.

        Usage:
            - Accessing this property will send the ``print(lan.status.port.vxi11)`` query.

        TSP Syntax:
            ```
            - print(lan.status.port.vxi11)
            ```

        Info:
            - ``port``, the lAN VXI-11 port number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".vxi11"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.vxi11)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.vxi11`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class LanStatusDns(BaseTSPCmd):
    """The ``lan.status.dns`` command tree.

    Properties and methods:
        - ``.address``: The ``lan.status.dns.address[N]`` attribute.
        - ``.name``: The ``lan.status.dns.name`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.address[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.address[{{key}}])",
            device=self._device,
        )

    @property
    def address(self) -> Dict[int, Union[str, float]]:
        """Access the ``lan.status.dns.address[N]`` attribute.

        Description:
            - This attribute contains the DNS server IP addresses.

        Usage:
            - Accessing an item from this property will send the
              ``print(lan.status.dns.address[N])`` query.

        TSP Syntax:
            ```
            - print(lan.status.dns.address[N])
            ```

        Info:
            - ``N``, the entry index (1, 2, or 3).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._address

    @property
    def name(self) -> str:
        """Access the ``lan.status.dns.name`` attribute.

        Description:
            - This attribute contains the present DNS fully qualified host name.

        Usage:
            - Accessing this property will send the ``print(lan.status.dns.name)`` query.

        TSP Syntax:
            ```
            - print(lan.status.dns.name)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".name"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.name)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.name`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class LanStatus(BaseTSPCmd):
    """The ``lan.status`` command tree.

    Properties and methods:
        - ``.dns``: The ``lan.status.dns`` command tree.
        - ``.duplex``: The ``lan.status.duplex`` attribute.
        - ``.gateway``: The ``lan.status.gateway`` attribute.
        - ``.ipaddress``: The ``lan.status.ipaddress`` attribute.
        - ``.macaddress``: The ``lan.status.macaddress`` attribute.
        - ``.port``: The ``lan.status.port`` command tree.
        - ``.speed``: The ``lan.status.speed`` attribute.
        - ``.subnetmask``: The ``lan.status.subnetmask`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dns = LanStatusDns(device, f"{self._cmd_syntax}.dns")
        self._port = LanStatusPort(device, f"{self._cmd_syntax}.port")

    @property
    def dns(self) -> LanStatusDns:
        """Return the ``lan.status.dns`` command tree.

        Sub-properties and sub-methods:
            - ``.address``: The ``lan.status.dns.address[N]`` attribute.
            - ``.name``: The ``lan.status.dns.name`` attribute.
        """
        return self._dns

    @property
    def duplex(self) -> str:
        """Access the ``lan.status.duplex`` attribute.

        Description:
            - This attribute contains the duplex mode presently in use by the LAN interface.

        Usage:
            - Accessing this property will send the ``print(lan.status.duplex)`` query.

        TSP Syntax:
            ```
            - print(lan.status.duplex)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".duplex"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.duplex)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.duplex`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def gateway(self) -> str:
        """Access the ``lan.status.gateway`` attribute.

        Description:
            - This attribute contains the gateway address presently in use by the LAN interface.

        Usage:
            - Accessing this property will send the ``print(lan.status.gateway)`` query.

        TSP Syntax:
            ```
            - print(lan.status.gateway)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".gateway"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.gateway)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.gateway`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ipaddress(self) -> str:
        """Access the ``lan.status.ipaddress`` attribute.

        Description:
            - This attribute contains the LAN IP address presently in use by the LAN interface.

        Usage:
            - Accessing this property will send the ``print(lan.status.ipaddress)`` query.

        TSP Syntax:
            ```
            - print(lan.status.ipaddress)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ipaddress"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ipaddress)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ipaddress`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def macaddress(self) -> str:
        """Access the ``lan.status.macaddress`` attribute.

        Description:
            - This attribute contains the LAN MAC address.

        Usage:
            - Accessing this property will send the ``print(lan.status.macaddress)`` query.

        TSP Syntax:
            ```
            - print(lan.status.macaddress)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".macaddress"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.macaddress)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.macaddress`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def port(self) -> LanStatusPort:
        """Return the ``lan.status.port`` command tree.

        Info:
            - ``port``, the dead socket termination socket port number.

        Sub-properties and sub-methods:
            - ``.dst``: The ``lan.status.port.dst`` attribute.
            - ``.rawsocket``: The ``lan.status.port.rawsocket`` attribute.
            - ``.telnet``: The ``lan.status.port.telnet`` attribute.
            - ``.vxi11``: The ``lan.status.port.vxi11`` attribute.
        """
        return self._port

    @property
    def speed(self) -> str:
        """Access the ``lan.status.speed`` attribute.

        Description:
            - This attribute contains the LAN speed.

        Usage:
            - Accessing this property will send the ``print(lan.status.speed)`` query.

        TSP Syntax:
            ```
            - print(lan.status.speed)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".speed"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.speed)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.speed`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def subnetmask(self) -> str:
        """Access the ``lan.status.subnetmask`` attribute.

        Description:
            - This attribute contains the LAN subnet mask that is presently in use by the LAN
              interface.

        Usage:
            - Accessing this property will send the ``print(lan.status.subnetmask)`` query.

        TSP Syntax:
            ```
            - print(lan.status.subnetmask)
            ```

        Info:
            - ``mask``, a string specifying the subnet mask in dotted decimal notation.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".subnetmask"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.subnetmask)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.subnetmask`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class LanConfigDns(BaseTSPCmd):
    """The ``lan.config.dns`` command tree.

    Properties and methods:
        - ``.address``: The ``lan.config.dns.address[N]`` attribute.
        - ``.domain``: The ``lan.config.dns.domain`` attribute.
        - ``.dynamic``: The ``lan.config.dns.dynamic`` attribute.
        - ``.hostname``: The ``lan.config.dns.hostname`` attribute.
        - ``.verify``: The ``lan.config.dns.verify`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.address[{{key}}]",
            write_syntax=f"{self._cmd_syntax}.address[{{key}}] = ",
            query_syntax=f"print({self._cmd_syntax}.address[{{key}}])",
            device=self._device,
        )

    @property
    def address(self) -> Dict[int, Union[str, float]]:
        """Access the ``lan.config.dns.address[N]`` attribute.

        Description:
            - Configures DNS server IP addresses.

        Usage:
            - Accessing an item from this property will send the
              ``print(lan.config.dns.address[N])`` query.
            - Setting an item from this property to a value will send the
              ``lan.config.dns.address[N] = value`` command.

        TSP Syntax:
            ```
            - lan.config.dns.address[N] = value
            - print(lan.config.dns.address[N])
            ```

        Info:
            - ``N``, the entry index (1 or 2).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._address

    @property
    def domain(self) -> str:
        """Access the ``lan.config.dns.domain`` attribute.

        Description:
            - Configures the dynamic DNS domain.

        Usage:
            - Accessing this property will send the ``print(lan.config.dns.domain)`` query.
            - Setting this property to a value will send the ``lan.config.dns.domain = value``
              command.

        TSP Syntax:
            ```
            - lan.config.dns.domain = value
            - print(lan.config.dns.domain)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".domain"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.domain)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.domain`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @domain.setter
    def domain(self, value: Union[str, float]) -> None:
        """Access the ``lan.config.dns.domain`` attribute.

        Description:
            - Configures the dynamic DNS domain.

        Usage:
            - Accessing this property will send the ``print(lan.config.dns.domain)`` query.
            - Setting this property to a value will send the ``lan.config.dns.domain = value``
              command.

        TSP Syntax:
            ```
            - lan.config.dns.domain = value
            - print(lan.config.dns.domain)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".domain", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.domain = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.domain`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def dynamic(self) -> str:
        """Access the ``lan.config.dns.dynamic`` attribute.

        Description:
            - Enables or disables the dynamic DNS registration.

        Usage:
            - Accessing this property will send the ``print(lan.config.dns.dynamic)`` query.
            - Setting this property to a value will send the ``lan.config.dns.dynamic = value``
              command.

        TSP Syntax:
            ```
            - lan.config.dns.dynamic = value
            - print(lan.config.dns.dynamic)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".dynamic"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.dynamic)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.dynamic`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @dynamic.setter
    def dynamic(self, value: Union[str, float]) -> None:
        """Access the ``lan.config.dns.dynamic`` attribute.

        Description:
            - Enables or disables the dynamic DNS registration.

        Usage:
            - Accessing this property will send the ``print(lan.config.dns.dynamic)`` query.
            - Setting this property to a value will send the ``lan.config.dns.dynamic = value``
              command.

        TSP Syntax:
            ```
            - lan.config.dns.dynamic = value
            - print(lan.config.dns.dynamic)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".dynamic", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.dynamic = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.dynamic`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def hostname(self) -> str:
        """Access the ``lan.config.dns.hostname`` attribute.

        Description:
            - This attribute defines the dynamic DNS host name.

        Usage:
            - Accessing this property will send the ``print(lan.config.dns.hostname)`` query.
            - Setting this property to a value will send the ``lan.config.dns.hostname = value``
              command.

        TSP Syntax:
            ```
            - lan.config.dns.hostname = value
            - print(lan.config.dns.hostname)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".hostname"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.hostname)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.hostname`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @hostname.setter
    def hostname(self, value: Union[str, float]) -> None:
        """Access the ``lan.config.dns.hostname`` attribute.

        Description:
            - This attribute defines the dynamic DNS host name.

        Usage:
            - Accessing this property will send the ``print(lan.config.dns.hostname)`` query.
            - Setting this property to a value will send the ``lan.config.dns.hostname = value``
              command.

        TSP Syntax:
            ```
            - lan.config.dns.hostname = value
            - print(lan.config.dns.hostname)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".hostname", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.hostname = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.hostname`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def verify(self) -> str:
        """Access the ``lan.config.dns.verify`` attribute.

        Description:
            - This attribute defines the DNS host name verification state.

        Usage:
            - Accessing this property will send the ``print(lan.config.dns.verify)`` query.
            - Setting this property to a value will send the ``lan.config.dns.verify = value``
              command.

        TSP Syntax:
            ```
            - lan.config.dns.verify = value
            - print(lan.config.dns.verify)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".verify"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.verify)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.verify`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @verify.setter
    def verify(self, value: Union[str, float]) -> None:
        """Access the ``lan.config.dns.verify`` attribute.

        Description:
            - This attribute defines the DNS host name verification state.

        Usage:
            - Accessing this property will send the ``print(lan.config.dns.verify)`` query.
            - Setting this property to a value will send the ``lan.config.dns.verify = value``
              command.

        TSP Syntax:
            ```
            - lan.config.dns.verify = value
            - print(lan.config.dns.verify)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".verify", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.verify = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.verify`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class LanConfig(BaseTSPCmd):
    """The ``lan.config`` command tree.

    Properties and methods:
        - ``.dns``: The ``lan.config.dns`` command tree.
        - ``.gateway``: The ``lan.config.gateway`` attribute.
        - ``.ipaddress``: The ``lan.config.ipaddress`` attribute.
        - ``.method``: The ``lan.config.method`` attribute.
        - ``.subnetmask``: The ``lan.config.subnetmask`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dns = LanConfigDns(device, f"{self._cmd_syntax}.dns")

    @property
    def dns(self) -> LanConfigDns:
        """Return the ``lan.config.dns`` command tree.

        Sub-properties and sub-methods:
            - ``.address``: The ``lan.config.dns.address[N]`` attribute.
            - ``.domain``: The ``lan.config.dns.domain`` attribute.
            - ``.dynamic``: The ``lan.config.dns.dynamic`` attribute.
            - ``.hostname``: The ``lan.config.dns.hostname`` attribute.
            - ``.verify``: The ``lan.config.dns.verify`` attribute.
        """
        return self._dns

    @property
    def gateway(self) -> str:
        """Access the ``lan.config.gateway`` attribute.

        Description:
            - This attribute contains the LAN default gateway address.

        Usage:
            - Accessing this property will send the ``print(lan.config.gateway)`` query.
            - Setting this property to a value will send the ``lan.config.gateway = value`` command.

        TSP Syntax:
            ```
            - lan.config.gateway = value
            - print(lan.config.gateway)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".gateway"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.gateway)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.gateway`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @gateway.setter
    def gateway(self, value: Union[str, float]) -> None:
        """Access the ``lan.config.gateway`` attribute.

        Description:
            - This attribute contains the LAN default gateway address.

        Usage:
            - Accessing this property will send the ``print(lan.config.gateway)`` query.
            - Setting this property to a value will send the ``lan.config.gateway = value`` command.

        TSP Syntax:
            ```
            - lan.config.gateway = value
            - print(lan.config.gateway)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".gateway", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.gateway = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.gateway`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ipaddress(self) -> str:
        """Access the ``lan.config.ipaddress`` attribute.

        Description:
            - This command specifies the LAN IP address.

        Usage:
            - Accessing this property will send the ``print(lan.config.ipaddress)`` query.
            - Setting this property to a value will send the ``lan.config.ipaddress = value``
              command.

        TSP Syntax:
            ```
            - lan.config.ipaddress = value
            - print(lan.config.ipaddress)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ipaddress"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ipaddress)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ipaddress`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ipaddress.setter
    def ipaddress(self, value: Union[str, float]) -> None:
        """Access the ``lan.config.ipaddress`` attribute.

        Description:
            - This command specifies the LAN IP address.

        Usage:
            - Accessing this property will send the ``print(lan.config.ipaddress)`` query.
            - Setting this property to a value will send the ``lan.config.ipaddress = value``
              command.

        TSP Syntax:
            ```
            - lan.config.ipaddress = value
            - print(lan.config.ipaddress)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ipaddress", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ipaddress = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ipaddress`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def method(self) -> str:
        """Access the ``lan.config.method`` attribute.

        Description:
            - This attribute contains the LAN settings configuration method.

        Usage:
            - Accessing this property will send the ``print(lan.config.method)`` query.
            - Setting this property to a value will send the ``lan.config.method = value`` command.

        TSP Syntax:
            ```
            - lan.config.method = value
            - print(lan.config.method)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".method"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.method)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.method`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @method.setter
    def method(self, value: Union[str, float]) -> None:
        """Access the ``lan.config.method`` attribute.

        Description:
            - This attribute contains the LAN settings configuration method.

        Usage:
            - Accessing this property will send the ``print(lan.config.method)`` query.
            - Setting this property to a value will send the ``lan.config.method = value`` command.

        TSP Syntax:
            ```
            - lan.config.method = value
            - print(lan.config.method)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".method", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.method = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.method`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def subnetmask(self) -> str:
        """Access the ``lan.config.subnetmask`` attribute.

        Description:
            - This attribute contains the LAN subnet mask.

        Usage:
            - Accessing this property will send the ``print(lan.config.subnetmask)`` query.
            - Setting this property to a value will send the ``lan.config.subnetmask = value``
              command.

        TSP Syntax:
            ```
            - lan.config.subnetmask = value
            - print(lan.config.subnetmask)
            ```

        Info:
            - ``mask``, the string that specifies the LAN subnet mask value in dotted decimal
              notation.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".subnetmask"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.subnetmask)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.subnetmask`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @subnetmask.setter
    def subnetmask(self, value: Union[str, float]) -> None:
        """Access the ``lan.config.subnetmask`` attribute.

        Description:
            - This attribute contains the LAN subnet mask.

        Usage:
            - Accessing this property will send the ``print(lan.config.subnetmask)`` query.
            - Setting this property to a value will send the ``lan.config.subnetmask = value``
              command.

        TSP Syntax:
            ```
            - lan.config.subnetmask = value
            - print(lan.config.subnetmask)
            ```

        Info:
            - ``mask``, the string that specifies the LAN subnet mask value in dotted decimal
              notation.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".subnetmask", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.subnetmask = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.subnetmask`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Lan(BaseTSPCmd):
    """The ``lan`` command tree.

    Properties and methods:
        - ``.applysettings()``: The ``lan.applysettings()`` function.
        - ``.config``: The ``lan.config`` command tree.
        - ``.lxidomain``: The ``lan.lxidomain`` attribute.
        - ``.nagle``: The ``lan.nagle`` attribute.
        - ``.reset()``: The ``lan.reset()`` function.
        - ``.restoredefaults()``: The ``lan.restoredefaults()`` function.
        - ``.status``: The ``lan.status`` command tree.
        - ``.trigger``: The ``lan.trigger[N]`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "lan") -> None:
        super().__init__(device, cmd_syntax)
        self._config = LanConfig(device, f"{self._cmd_syntax}.config")
        self._status = LanStatus(device, f"{self._cmd_syntax}.status")
        self._trigger: Dict[int, LanTriggerItem] = DefaultDictPassKeyToFactory(
            lambda x: LanTriggerItem(device, f"{self._cmd_syntax}.trigger[{x}]")
        )

    @property
    def config(self) -> LanConfig:
        """Return the ``lan.config`` command tree.

        Sub-properties and sub-methods:
            - ``.dns``: The ``lan.config.dns`` command tree.
            - ``.gateway``: The ``lan.config.gateway`` attribute.
            - ``.ipaddress``: The ``lan.config.ipaddress`` attribute.
            - ``.method``: The ``lan.config.method`` attribute.
            - ``.subnetmask``: The ``lan.config.subnetmask`` attribute.
        """
        return self._config

    @property
    def lxidomain(self) -> str:
        """Access the ``lan.lxidomain`` attribute.

        Description:
            - This attribute contains the LXI domain.

        Usage:
            - Accessing this property will send the ``print(lan.lxidomain)`` query.
            - Setting this property to a value will send the ``lan.lxidomain = value`` command.

        TSP Syntax:
            ```
            - lan.lxidomain = value
            - print(lan.lxidomain)
            ```

        Info:
            - ``domain``, the LXI domain number (0 to 255).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".lxidomain"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.lxidomain)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lxidomain`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @lxidomain.setter
    def lxidomain(self, value: Union[str, float]) -> None:
        """Access the ``lan.lxidomain`` attribute.

        Description:
            - This attribute contains the LXI domain.

        Usage:
            - Accessing this property will send the ``print(lan.lxidomain)`` query.
            - Setting this property to a value will send the ``lan.lxidomain = value`` command.

        TSP Syntax:
            ```
            - lan.lxidomain = value
            - print(lan.lxidomain)
            ```

        Info:
            - ``domain``, the LXI domain number (0 to 255).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".lxidomain", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.lxidomain = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.lxidomain`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def nagle(self) -> str:
        """Access the ``lan.nagle`` attribute.

        Description:
            - This attribute controls the state of the LAN Nagle algorithm.

        Usage:
            - Accessing this property will send the ``print(lan.nagle)`` query.
            - Setting this property to a value will send the ``lan.nagle = value`` command.

        TSP Syntax:
            ```
            - lan.nagle = value
            - print(lan.nagle)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".nagle"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.nagle)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.nagle`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @nagle.setter
    def nagle(self, value: Union[str, float]) -> None:
        """Access the ``lan.nagle`` attribute.

        Description:
            - This attribute controls the state of the LAN Nagle algorithm.

        Usage:
            - Accessing this property will send the ``print(lan.nagle)`` query.
            - Setting this property to a value will send the ``lan.nagle = value`` command.

        TSP Syntax:
            ```
            - lan.nagle = value
            - print(lan.nagle)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".nagle", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.nagle = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.nagle`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def status(self) -> LanStatus:
        """Return the ``lan.status`` command tree.

        Sub-properties and sub-methods:
            - ``.dns``: The ``lan.status.dns`` command tree.
            - ``.duplex``: The ``lan.status.duplex`` attribute.
            - ``.gateway``: The ``lan.status.gateway`` attribute.
            - ``.ipaddress``: The ``lan.status.ipaddress`` attribute.
            - ``.macaddress``: The ``lan.status.macaddress`` attribute.
            - ``.port``: The ``lan.status.port`` command tree.
            - ``.speed``: The ``lan.status.speed`` attribute.
            - ``.subnetmask``: The ``lan.status.subnetmask`` attribute.
        """
        return self._status

    @property
    def trigger(self) -> Dict[int, LanTriggerItem]:
        """Return the ``lan.trigger[N]`` command tree.

        Info:
            - ``N``, the LAN event number (1 to 8).

        Constants:
            - ``.EVENT_ID``: The event identifier used to route the LAN trigger to other subsystems
              (using stimulus properties).

        Sub-properties and sub-methods:
            - ``.assert()``: The ``lan.trigger[N].assert()`` function.
            - ``.clear()``: The ``lan.trigger[N].clear()`` function.
            - ``.connect()``: The ``lan.trigger[N].connect()`` function.
            - ``.connected``: The ``lan.trigger[N].connected`` attribute.
            - ``.disconnect()``: The ``lan.trigger[N].disconnect()`` function.
            - ``.ipaddress``: The ``lan.trigger[N].ipaddress`` attribute.
            - ``.mode``: The ``lan.trigger[N].mode`` attribute.
            - ``.overrun``: The ``lan.trigger[N].overrun`` attribute.
            - ``.protocol``: The ``lan.trigger[N].protocol`` attribute.
            - ``.pseudostate``: The ``lan.trigger[N].pseudostate`` attribute.
            - ``.stimulus``: The ``lan.trigger[N].stimulus`` attribute.
            - ``.wait()``: The ``lan.trigger[N].wait()`` function.
        """
        return self._trigger

    def applysettings(self) -> None:
        """Run the ``lan.applysettings()`` function.

        Description:
            - This function re-initializes the LAN interface with new settings.

        TSP Syntax:
            ```
            - lan.applysettings()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.applysettings()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.applysettings()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def reset(self) -> None:
        """Run the ``lan.reset()`` function.

        Description:
            - This function resets the LAN interface.

        TSP Syntax:
            ```
            - lan.reset()
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

    def restoredefaults(self) -> None:
        """Run the ``lan.restoredefaults()`` function.

        Description:
            - This function resets LAN settings to default values.

        TSP Syntax:
            ```
            - lan.restoredefaults()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.restoredefaults()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.restoredefaults()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
