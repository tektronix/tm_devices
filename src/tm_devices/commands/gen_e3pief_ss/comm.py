# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The comm commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - comm.gpib.enable
    - comm.lan.enable
    - comm.lan.rawsockets.enable
    - comm.lan.telnet.enable
    - comm.lan.vxi11.enable
    - comm.lan.web.enable
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class CommLanWeb(BaseTSPCmd):
    """The ``comm.lan.web`` command tree.

    Properties and methods:
        - ``.enable``: The ``comm.lan.web.enable`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``comm.lan.web.enable`` attribute.

        Description:
            - This attribute describes whether or not communication using the web interface is
              enabled.

        Usage:
            - Accessing this property will send the ``print(comm.lan.web.enable)`` query.
            - Setting this property to a value will send the ``comm.lan.web.enable = value``
              command.

        TSP Syntax:
            ```
            - comm.lan.web.enable = value
            - print(comm.lan.web.enable)
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
        """Access the ``comm.lan.web.enable`` attribute.

        Description:
            - This attribute describes whether or not communication using the web interface is
              enabled.

        Usage:
            - Accessing this property will send the ``print(comm.lan.web.enable)`` query.
            - Setting this property to a value will send the ``comm.lan.web.enable = value``
              command.

        TSP Syntax:
            ```
            - comm.lan.web.enable = value
            - print(comm.lan.web.enable)
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


class CommLanVxi11(BaseTSPCmd):
    """The ``comm.lan.vxi11`` command tree.

    Properties and methods:
        - ``.enable``: The ``comm.lan.vxi11.enable`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``comm.lan.vxi11.enable`` attribute.

        Description:
            - This attribute describes whether or not communication using a VXI-11 connection is
              enabled.

        Usage:
            - Accessing this property will send the ``print(comm.lan.vxi11.enable)`` query.
            - Setting this property to a value will send the ``comm.lan.vxi11.enable = value``
              command.

        TSP Syntax:
            ```
            - comm.lan.vxi11.enable = value
            - print(comm.lan.vxi11.enable)
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
        """Access the ``comm.lan.vxi11.enable`` attribute.

        Description:
            - This attribute describes whether or not communication using a VXI-11 connection is
              enabled.

        Usage:
            - Accessing this property will send the ``print(comm.lan.vxi11.enable)`` query.
            - Setting this property to a value will send the ``comm.lan.vxi11.enable = value``
              command.

        TSP Syntax:
            ```
            - comm.lan.vxi11.enable = value
            - print(comm.lan.vxi11.enable)
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


class CommLanTelnet(BaseTSPCmd):
    """The ``comm.lan.telnet`` command tree.

    Properties and methods:
        - ``.enable``: The ``comm.lan.telnet.enable`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``comm.lan.telnet.enable`` attribute.

        Description:
            - This attribute describes whether or not communication using Telnet is enabled.

        Usage:
            - Accessing this property will send the ``print(comm.lan.telnet.enable)`` query.
            - Setting this property to a value will send the ``comm.lan.telnet.enable = value``
              command.

        TSP Syntax:
            ```
            - comm.lan.telnet.enable = value
            - print(comm.lan.telnet.enable)
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
        """Access the ``comm.lan.telnet.enable`` attribute.

        Description:
            - This attribute describes whether or not communication using Telnet is enabled.

        Usage:
            - Accessing this property will send the ``print(comm.lan.telnet.enable)`` query.
            - Setting this property to a value will send the ``comm.lan.telnet.enable = value``
              command.

        TSP Syntax:
            ```
            - comm.lan.telnet.enable = value
            - print(comm.lan.telnet.enable)
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


class CommLanRawsockets(BaseTSPCmd):
    """The ``comm.lan.rawsockets`` command tree.

    Properties and methods:
        - ``.enable``: The ``comm.lan.rawsockets.enable`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``comm.lan.rawsockets.enable`` attribute.

        Description:
            - This attribute describes whether or not communication using raw socket is enabled.

        Usage:
            - Accessing this property will send the ``print(comm.lan.rawsockets.enable)`` query.
            - Setting this property to a value will send the ``comm.lan.rawsockets.enable = value``
              command.

        TSP Syntax:
            ```
            - comm.lan.rawsockets.enable = value
            - print(comm.lan.rawsockets.enable)
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
        """Access the ``comm.lan.rawsockets.enable`` attribute.

        Description:
            - This attribute describes whether or not communication using raw socket is enabled.

        Usage:
            - Accessing this property will send the ``print(comm.lan.rawsockets.enable)`` query.
            - Setting this property to a value will send the ``comm.lan.rawsockets.enable = value``
              command.

        TSP Syntax:
            ```
            - comm.lan.rawsockets.enable = value
            - print(comm.lan.rawsockets.enable)
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


class CommLan(BaseTSPCmd):
    """The ``comm.lan`` command tree.

    Properties and methods:
        - ``.enable``: The ``comm.lan.enable`` attribute.
        - ``.rawsockets``: The ``comm.lan.rawsockets`` command tree.
        - ``.telnet``: The ``comm.lan.telnet`` command tree.
        - ``.vxi11``: The ``comm.lan.vxi11`` command tree.
        - ``.web``: The ``comm.lan.web`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rawsockets = CommLanRawsockets(device, f"{self._cmd_syntax}.rawsockets")
        self._telnet = CommLanTelnet(device, f"{self._cmd_syntax}.telnet")
        self._vxi11 = CommLanVxi11(device, f"{self._cmd_syntax}.vxi11")
        self._web = CommLanWeb(device, f"{self._cmd_syntax}.web")

    @property
    def enable(self) -> str:
        """Access the ``comm.lan.enable`` attribute.

        Description:
            - This attribute controls whether or not any communication using the LAN connection is
              enabled.

        Usage:
            - Accessing this property will send the ``print(comm.lan.enable)`` query.
            - Setting this property to a value will send the ``comm.lan.enable = value`` command.

        TSP Syntax:
            ```
            - comm.lan.enable = value
            - print(comm.lan.enable)
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
        """Access the ``comm.lan.enable`` attribute.

        Description:
            - This attribute controls whether or not any communication using the LAN connection is
              enabled.

        Usage:
            - Accessing this property will send the ``print(comm.lan.enable)`` query.
            - Setting this property to a value will send the ``comm.lan.enable = value`` command.

        TSP Syntax:
            ```
            - comm.lan.enable = value
            - print(comm.lan.enable)
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
    def rawsockets(self) -> CommLanRawsockets:
        """Return the ``comm.lan.rawsockets`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``comm.lan.rawsockets.enable`` attribute.
        """
        return self._rawsockets

    @property
    def telnet(self) -> CommLanTelnet:
        """Return the ``comm.lan.telnet`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``comm.lan.telnet.enable`` attribute.
        """
        return self._telnet

    @property
    def vxi11(self) -> CommLanVxi11:
        """Return the ``comm.lan.vxi11`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``comm.lan.vxi11.enable`` attribute.
        """
        return self._vxi11

    @property
    def web(self) -> CommLanWeb:
        """Return the ``comm.lan.web`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``comm.lan.web.enable`` attribute.
        """
        return self._web


class CommGpib(BaseTSPCmd):
    """The ``comm.gpib`` command tree.

    Properties and methods:
        - ``.enable``: The ``comm.gpib.enable`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``comm.gpib.enable`` attribute.

        Description:
            - This attribute describes whether or not communication using the GPIB connection is
              enabled.

        Usage:
            - Accessing this property will send the ``print(comm.gpib.enable)`` query.
            - Setting this property to a value will send the ``comm.gpib.enable = value`` command.

        TSP Syntax:
            ```
            - comm.gpib.enable = value
            - print(comm.gpib.enable)
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
        """Access the ``comm.gpib.enable`` attribute.

        Description:
            - This attribute describes whether or not communication using the GPIB connection is
              enabled.

        Usage:
            - Accessing this property will send the ``print(comm.gpib.enable)`` query.
            - Setting this property to a value will send the ``comm.gpib.enable = value`` command.

        TSP Syntax:
            ```
            - comm.gpib.enable = value
            - print(comm.gpib.enable)
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


class Comm(BaseTSPCmd):
    """The ``comm`` command tree.

    Properties and methods:
        - ``.gpib``: The ``comm.gpib`` command tree.
        - ``.lan``: The ``comm.lan`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "comm") -> None:
        super().__init__(device, cmd_syntax)
        self._gpib = CommGpib(device, f"{self._cmd_syntax}.gpib")
        self._lan = CommLan(device, f"{self._cmd_syntax}.lan")

    @property
    def gpib(self) -> CommGpib:
        """Return the ``comm.gpib`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``comm.gpib.enable`` attribute.
        """
        return self._gpib

    @property
    def lan(self) -> CommLan:
        """Return the ``comm.lan`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``comm.lan.enable`` attribute.
            - ``.rawsockets``: The ``comm.lan.rawsockets`` command tree.
            - ``.telnet``: The ``comm.lan.telnet`` command tree.
            - ``.vxi11``: The ``comm.lan.vxi11`` command tree.
            - ``.web``: The ``comm.lan.web`` command tree.
        """
        return self._lan
