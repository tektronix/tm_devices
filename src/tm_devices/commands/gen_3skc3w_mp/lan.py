# pyright: reportConstantRedefinition=none
"""The lan commands module.

These commands are used in the following models:
MP5103

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - lan.applysettings()
    - lan.autoconnect
    - lan.config.dns.address[N]
    - lan.config.dns.domain
    - lan.config.dns.dynamic
    - lan.config.dns.hostname
    - lan.config.dns.verify
    - lan.config.gateway
    - lan.config.ipaddress
    - lan.config.method
    - lan.config.subnetmask
    - lan.enable
    - lan.hislip.access
    - lan.identify
    - lan.ipconfig()
    - lan.linktimeout
    - lan.nagle
    - lan.rawsocket.access
    - lan.reset()
    - lan.restoredefaults()
    - lan.status.dns.address[N]
    - lan.status.dns.name
    - lan.status.gateway
    - lan.status.ipaddress
    - lan.status.macaddress
    - lan.status.port.dst
    - lan.status.port.hislip
    - lan.status.port.rawsocket
    - lan.status.port.telnet
    - lan.status.speed
    - lan.status.subnetmask
    - lan.telnet.access
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, DefaultDictDeviceCommunication, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class LanTelnet(BaseTSPCmd):
    """The ``lan.telnet`` command tree.

    Properties and methods:
        - ``.access``: The ``lan.telnet.access`` attribute.
    """

    @property
    def access(self) -> str:
        """Access the ``lan.telnet.access`` attribute.

        Description:
            - This command is used to enable or disable mainframe telnet port communications

        Usage:
            - Accessing this property will send the ``print(lan.telnet.access)`` query.
            - Setting this property to a value will send the ``lan.telnet.access = value`` command.

        TSP Syntax:
            ```
            - lan.telnet.access = value
            - print(lan.telnet.access)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".access"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.access)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.access`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @access.setter
    def access(self, value: Union[str, float]) -> None:
        """Access the ``lan.telnet.access`` attribute.

        Description:
            - This command is used to enable or disable mainframe telnet port communications

        Usage:
            - Accessing this property will send the ``print(lan.telnet.access)`` query.
            - Setting this property to a value will send the ``lan.telnet.access = value`` command.

        TSP Syntax:
            ```
            - lan.telnet.access = value
            - print(lan.telnet.access)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".access", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.access = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.access`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class LanStatusPort(BaseTSPCmd):
    """The ``lan.status.port`` command tree.

    Info:
        - ``port``, the dST port number.

    Properties and methods:
        - ``.dst``: The ``lan.status.port.dst`` attribute.
        - ``.hislip``: The ``lan.status.port.hislip`` attribute.
        - ``.rawsocket``: The ``lan.status.port.rawsocket`` attribute.
        - ``.telnet``: The ``lan.status.port.telnet`` attribute.
    """

    @property
    def dst(self) -> str:
        """Access the ``lan.status.port.dst`` attribute.

        Description:
            - This attribute contains the LAN dead socket termination (DST) port number.

        Usage:
            - Accessing this property will send the ``print(lan.status.port.dst)`` query.

        TSP Syntax:
            ```
            - print(lan.status.port.dst)
            ```

        Info:
            - ``port``, the dST port number.

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
    def hislip(self) -> str:
        """Access the ``lan.status.port.hislip`` attribute.

        Description:
            - This attribute contains the HiSLIP connection port number.

        Usage:
            - Accessing this property will send the ``print(lan.status.port.hislip)`` query.

        TSP Syntax:
            ```
            - print(lan.status.port.hislip)
            ```

        Info:
            - ``port``, the hiSLIP port number, 4880.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".hislip"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.hislip)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.hislip`` attribute."  # noqa: E501
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
            - ``port``, the raw socket port number, 5025.

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
            - This attribute contains the LAN telnet connection port number.

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
            - ``N``, the entry index: 1, 2, or 3.

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
            - ``port``, the dST port number.

        Sub-properties and sub-methods:
            - ``.dst``: The ``lan.status.port.dst`` attribute.
            - ``.hislip``: The ``lan.status.port.hislip`` attribute.
            - ``.rawsocket``: The ``lan.status.port.rawsocket`` attribute.
            - ``.telnet``: The ``lan.status.port.telnet`` attribute.
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


class LanRawsocket(BaseTSPCmd):
    """The ``lan.rawsocket`` command tree.

    Properties and methods:
        - ``.access``: The ``lan.rawsocket.access`` attribute.
    """

    @property
    def access(self) -> str:
        """Access the ``lan.rawsocket.access`` attribute.

        Description:
            - This command is used to enable or disable mainframe raw socket port communications

        Usage:
            - Accessing this property will send the ``print(lan.rawsocket.access)`` query.
            - Setting this property to a value will send the ``lan.rawsocket.access = value``
              command.

        TSP Syntax:
            ```
            - lan.rawsocket.access = value
            - print(lan.rawsocket.access)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".access"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.access)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.access`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @access.setter
    def access(self, value: Union[str, float]) -> None:
        """Access the ``lan.rawsocket.access`` attribute.

        Description:
            - This command is used to enable or disable mainframe raw socket port communications

        Usage:
            - Accessing this property will send the ``print(lan.rawsocket.access)`` query.
            - Setting this property to a value will send the ``lan.rawsocket.access = value``
              command.

        TSP Syntax:
            ```
            - lan.rawsocket.access = value
            - print(lan.rawsocket.access)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".access", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.access = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.access`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class LanHislip(BaseTSPCmd):
    """The ``lan.hislip`` command tree.

    Properties and methods:
        - ``.access``: The ``lan.hislip.access`` attribute.
    """

    @property
    def access(self) -> str:
        """Access the ``lan.hislip.access`` attribute.

        Description:
            - This command is used to enable or disable mainframe HiSLIP port communications.

        Usage:
            - Accessing this property will send the ``print(lan.hislip.access)`` query.
            - Setting this property to a value will send the ``lan.hislip.access = value`` command.

        TSP Syntax:
            ```
            - lan.hislip.access = value
            - print(lan.hislip.access)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".access"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.access)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.access`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @access.setter
    def access(self, value: Union[str, float]) -> None:
        """Access the ``lan.hislip.access`` attribute.

        Description:
            - This command is used to enable or disable mainframe HiSLIP port communications.

        Usage:
            - Accessing this property will send the ``print(lan.hislip.access)`` query.
            - Setting this property to a value will send the ``lan.hislip.access = value`` command.

        TSP Syntax:
            ```
            - lan.hislip.access = value
            - print(lan.hislip.access)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".access", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.access = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.access`` attribute."  # noqa: E501
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
            - This command configures the DNS server IP addresses.

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
            - ``N``, the entry index: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._address

    @property
    def domain(self) -> str:
        """Access the ``lan.config.dns.domain`` attribute.

        Description:
            - This attribute configures the dynamic DNS domain.

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
            - This attribute configures the dynamic DNS domain.

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
        - ``.autoconnect``: The ``lan.autoconnect`` attribute.
        - ``.config``: The ``lan.config`` command tree.
        - ``.enable``: The ``lan.enable`` attribute.
        - ``.hislip``: The ``lan.hislip`` command tree.
        - ``.identify``: The ``lan.identify`` attribute.
        - ``.ipconfig()``: The ``lan.ipconfig()`` function.
        - ``.linktimeout``: The ``lan.linktimeout`` attribute.
        - ``.nagle``: The ``lan.nagle`` attribute.
        - ``.rawsocket``: The ``lan.rawsocket`` command tree.
        - ``.reset()``: The ``lan.reset()`` function.
        - ``.restoredefaults()``: The ``lan.restoredefaults()`` function.
        - ``.status``: The ``lan.status`` command tree.
        - ``.telnet``: The ``lan.telnet`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "lan") -> None:
        super().__init__(device, cmd_syntax)
        self._config = LanConfig(device, f"{self._cmd_syntax}.config")
        self._hislip = LanHislip(device, f"{self._cmd_syntax}.hislip")
        self._rawsocket = LanRawsocket(device, f"{self._cmd_syntax}.rawsocket")
        self._status = LanStatus(device, f"{self._cmd_syntax}.status")
        self._telnet = LanTelnet(device, f"{self._cmd_syntax}.telnet")

    @property
    def autoconnect(self) -> str:
        """Access the ``lan.autoconnect`` attribute.

        Description:
            - This attribute is used to enable or disable link monitoring.

        Usage:
            - Accessing this property will send the ``print(lan.autoconnect)`` query.
            - Setting this property to a value will send the ``lan.autoconnect = value`` command.

        TSP Syntax:
            ```
            - lan.autoconnect = value
            - print(lan.autoconnect)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autoconnect"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autoconnect)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autoconnect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autoconnect.setter
    def autoconnect(self, value: Union[str, float]) -> None:
        """Access the ``lan.autoconnect`` attribute.

        Description:
            - This attribute is used to enable or disable link monitoring.

        Usage:
            - Accessing this property will send the ``print(lan.autoconnect)`` query.
            - Setting this property to a value will send the ``lan.autoconnect = value`` command.

        TSP Syntax:
            ```
            - lan.autoconnect = value
            - print(lan.autoconnect)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autoconnect", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autoconnect = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autoconnect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

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
    def enable(self) -> str:
        """Access the ``lan.enable`` attribute.

        Description:
            - This attribute controls whether or not any communications using the LAN connector are
              enabled.

        Usage:
            - Accessing this property will send the ``print(lan.enable)`` query.
            - Setting this property to a value will send the ``lan.enable = value`` command.

        TSP Syntax:
            ```
            - lan.enable = value
            - print(lan.enable)
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
        """Access the ``lan.enable`` attribute.

        Description:
            - This attribute controls whether or not any communications using the LAN connector are
              enabled.

        Usage:
            - Accessing this property will send the ``print(lan.enable)`` query.
            - Setting this property to a value will send the ``lan.enable = value`` command.

        TSP Syntax:
            ```
            - lan.enable = value
            - print(lan.enable)
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
    def hislip(self) -> LanHislip:
        """Return the ``lan.hislip`` command tree.

        Sub-properties and sub-methods:
            - ``.access``: The ``lan.hislip.access`` attribute.
        """
        return self._hislip

    @property
    def identify(self) -> str:
        """Access the ``lan.identify`` attribute.

        Description:
            - This attribute controls the LXI LAN identify state.

        Usage:
            - Accessing this property will send the ``print(lan.identify)`` query.
            - Setting this property to a value will send the ``lan.identify = value`` command.

        TSP Syntax:
            ```
            - lan.identify = value
            - print(lan.identify)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".identify"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.identify)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.identify`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @identify.setter
    def identify(self, value: Union[str, float]) -> None:
        """Access the ``lan.identify`` attribute.

        Description:
            - This attribute controls the LXI LAN identify state.

        Usage:
            - Accessing this property will send the ``print(lan.identify)`` query.
            - Setting this property to a value will send the ``lan.identify = value`` command.

        TSP Syntax:
            ```
            - lan.identify = value
            - print(lan.identify)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".identify", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.identify = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.identify`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def linktimeout(self) -> str:
        """Access the ``lan.linktimeout`` attribute.

        Description:
            - This attribute contains the LAN link timeout period.

        Usage:
            - Accessing this property will send the ``print(lan.linktimeout)`` query.
            - Setting this property to a value will send the ``lan.linktimeout = value`` command.

        TSP Syntax:
            ```
            - lan.linktimeout = value
            - print(lan.linktimeout)
            ```

        Info:
            - ``timeout``, the LAN link monitor time-out period (in seconds).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".linktimeout"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.linktimeout)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.linktimeout`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @linktimeout.setter
    def linktimeout(self, value: Union[str, float]) -> None:
        """Access the ``lan.linktimeout`` attribute.

        Description:
            - This attribute contains the LAN link timeout period.

        Usage:
            - Accessing this property will send the ``print(lan.linktimeout)`` query.
            - Setting this property to a value will send the ``lan.linktimeout = value`` command.

        TSP Syntax:
            ```
            - lan.linktimeout = value
            - print(lan.linktimeout)
            ```

        Info:
            - ``timeout``, the LAN link monitor time-out period (in seconds).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".linktimeout", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.linktimeout = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.linktimeout`` attribute."  # noqa: E501
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
    def rawsocket(self) -> LanRawsocket:
        """Return the ``lan.rawsocket`` command tree.

        Sub-properties and sub-methods:
            - ``.access``: The ``lan.rawsocket.access`` attribute.
        """
        return self._rawsocket

    @property
    def status(self) -> LanStatus:
        """Return the ``lan.status`` command tree.

        Sub-properties and sub-methods:
            - ``.dns``: The ``lan.status.dns`` command tree.
            - ``.gateway``: The ``lan.status.gateway`` attribute.
            - ``.ipaddress``: The ``lan.status.ipaddress`` attribute.
            - ``.macaddress``: The ``lan.status.macaddress`` attribute.
            - ``.port``: The ``lan.status.port`` command tree.
            - ``.speed``: The ``lan.status.speed`` attribute.
            - ``.subnetmask``: The ``lan.status.subnetmask`` attribute.
        """
        return self._status

    @property
    def telnet(self) -> LanTelnet:
        """Return the ``lan.telnet`` command tree.

        Sub-properties and sub-methods:
            - ``.access``: The ``lan.telnet.access`` attribute.
        """
        return self._telnet

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

    def ipconfig(
        self,
        method: Optional[str] = None,
        ip_v4_address: Optional[str] = None,
        subnet_mask: Optional[str] = None,
        gateway: Optional[str] = None,
    ) -> str:
        """Run the ``lan.ipconfig()`` function.

        Description:
            - This function specifies the LAN configuration for the instrument.

        TSP Syntax:
            ```
            - lan.ipconfig()
            ```

        Args:
            method (optional): The method for configuring LAN settings; it can be one of the
                following values.
            ip_v4_address (optional): LAN IP address; must be a string specifying the IP address in
                dotted decimal notation.
            subnet_mask (optional): The LAN subnet mask; must be a string in dotted decimal
                notation.
            gateway (optional): The LAN default gateway; must be a string in dotted decimal
                notation.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    method,
                    f'"{ip_v4_address}"' if ip_v4_address is not None else None,
                    f'"{subnet_mask}"' if subnet_mask is not None else None,
                    f'"{gateway}"' if gateway is not None else None,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ipconfig({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.ipconfig()`` function."  # noqa: E501
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
