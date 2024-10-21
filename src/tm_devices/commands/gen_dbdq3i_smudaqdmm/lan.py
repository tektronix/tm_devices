# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The lan commands module.

These commands are used in the following models:
DAQ6510, DMM6500, DMM7510, SMU2450, SMU2460, SMU2461, SMU2470

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - lan.ipconfig()
    - lan.lxidomain
    - lan.macaddress
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Lan(BaseTSPCmd):
    """The ``lan`` command tree.

    Constants:
        - ``.MODE_AUTO``: The instrument automatically assigns LAN settings.
        - ``.MODE_MANUAL``: You specify the LAN settings.
        - ``.OFF``: An open and close on the DST port (5030) closes all open LAN connections.
        - ``.ON``: The DST port needs to be opened, receive the login + <system password>, then
          close the DST port to close all open LAN connections. By turning DST protection ON, you
          are protecting LAN connections from being inadvertently closed by your IT department doing
          a port scan across the corporate network.
        - ``.PROTOCOL_MULTICAST``: Sets the LAN protocol to use for sending trigger messages to
          multicast.
        - ``.PROTOCOL_TCP``: Sets the LAN protocol to use for sending trigger messages to TCP.
        - ``.PROTOCOL_UDP``: Sets the LAN protocol to use for sending trigger messages to UDP.

    Properties and methods:
        - ``.ipconfig()``: The ``lan.ipconfig()`` function.
        - ``.lxidomain``: The ``lan.lxidomain`` attribute.
        - ``.macaddress``: The ``lan.macaddress`` attribute.
    """

    MODE_AUTO = "lan.MODE_AUTO"
    """str: The instrument automatically assigns LAN settings."""
    MODE_MANUAL = "lan.MODE_MANUAL"
    """str: You specify the LAN settings."""
    OFF = "lan.OFF"
    """str: An open and close on the DST port (5030) closes all open LAN connections."""
    ON = "lan.ON"
    """str: The DST port needs to be opened, receive the login + <system password>, then close the DST port to close all open LAN connections.  By turning DST protection ON, you are protecting LAN connections from being inadvertently closed by your IT department doing a port scan across the corporate network."""  # noqa: E501
    PROTOCOL_MULTICAST = "lan.PROTOCOL_MULTICAST"
    """str: Sets the LAN protocol to use for sending trigger messages to multicast."""
    PROTOCOL_TCP = "lan.PROTOCOL_TCP"
    """str: Sets the LAN protocol to use for sending trigger messages to TCP."""
    PROTOCOL_UDP = "lan.PROTOCOL_UDP"
    """str: Sets the LAN protocol to use for sending trigger messages to UDP."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "lan") -> None:
        super().__init__(device, cmd_syntax)

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
    def macaddress(self) -> str:
        """Access the ``lan.macaddress`` attribute.

        Description:
            - This attribute describes the LAN MAC address.

        Usage:
            - Accessing this property will send the ``print(lan.macaddress)`` query.

        TSP Syntax:
            ```
            - print(lan.macaddress)
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
