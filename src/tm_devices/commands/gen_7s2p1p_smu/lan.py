# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The lan commands module.

These commands are used in the following models:
SMU2601B_Pulse

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - lan.config.dns.hostname
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


# pylint: disable=too-few-public-methods
class LanTriggerItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``lan.trigger[N]`` command tree.

    Constants:
        - ``.EVENT_ID``: Selects the event that causes a trigger to be asserted on the digital
          output line as the appropriate LXI trigger packet received on LAN trigger object N.
    """

    EVENT_ID = "lan.trigger[N].EVENT_ID"
    """str: Selects the event that causes a trigger to be asserted on the digital output line as the appropriate LXI trigger packet received on LAN trigger object N."""  # noqa: E501

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        # pylint: disable=invalid-name
        self.EVENT_ID = self.EVENT_ID.replace(
            "[N]", f"[{self._cmd_syntax.rsplit('[', maxsplit=1)[-1].split(']', maxsplit=1)[0]}]"
        )


class LanConfigDns(BaseTSPCmd):
    """The ``lan.config.dns`` command tree.

    Properties and methods:
        - ``.hostname``: The ``lan.config.dns.hostname`` attribute.
    """

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


class LanConfig(BaseTSPCmd):
    """The ``lan.config`` command tree.

    Properties and methods:
        - ``.dns``: The ``lan.config.dns`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dns = LanConfigDns(device, f"{self._cmd_syntax}.dns")

    @property
    def dns(self) -> LanConfigDns:
        """Return the ``lan.config.dns`` command tree.

        Sub-properties and sub-methods:
            - ``.hostname``: The ``lan.config.dns.hostname`` attribute.
        """
        return self._dns


class Lan(BaseTSPCmd):
    """The ``lan`` command tree.

    Constants:
        - ``.AUTO``: Selects automatic sequencing of configuration.
        - ``.DISABLE``: Disables automatic link reconnection and monitoring.
        - ``.ENABLE``: Enables automatic link reconnection and monitoring.
        - ``.FULL``: Full-duplex operation.
        - ``.HALF``: Half-duplex operation.
        - ``.MANUAL``: Use only manually specified configuration settings.
        - ``.MULTICAST``: Sets the LAN protocol to use for sending trigger messages to multicast.
        - ``.TCP``: Use TCP protocol.
        - ``.TRIG_EITHER``: Sets the trigger operation and detection mode of the specified LAN event
          to rising or falling edge (positive or negative state).
        - ``.TRIG_FALLING``: Sets the trigger operation and detection mode of the specified LAN
          event to falling edge (negative state).
        - ``.TRIG_RISING``: Sets the trigger operation and detection mode of the specified LAN event
          to rising edge (positive state).
        - ``.TRIG_RISINGA``: Sets the trigger operation and detection mode of the specified LAN
          event to rising edge (positive state).
        - ``.TRIG_RISINGM``: Sets the trigger operation and detection mode of the specified LAN
          event to rising edge (positive state).
        - ``.TRIG_SYNCHRONOUS``: Use for compatibility with older instruments; sets the trigger
          operation and detection mode of the specified LAN event to falling edge (negative state).
        - ``.TRIG_SYNCHRONOUSA``: Sets the trigger operation and detection mode of the specified LAN
          event to falling edge (negative state).
        - ``.TRIG_SYNCHRONOUSM``: Sets the trigger operation and detection mode of the specified LAN
          event to rising edge (positive state).
        - ``.UDP``: Use UDP protocol.

    Properties and methods:
        - ``.config``: The ``lan.config`` command tree.
        - ``.trigger``: The ``lan.trigger[N]`` command tree.
    """

    AUTO = "lan.AUTO"
    """str: Selects automatic sequencing of configuration."""
    DISABLE = "lan.DISABLE"
    """str: Disables automatic link reconnection and monitoring."""
    ENABLE = "lan.ENABLE"
    """str: Enables automatic link reconnection and monitoring."""
    FULL = "lan.FULL"
    """str: Full-duplex operation."""
    HALF = "lan.HALF"
    """str: Half-duplex operation."""
    MANUAL = "lan.MANUAL"
    """str: Use only manually specified configuration settings."""
    MULTICAST = "lan.MULTICAST"
    """str: Sets the LAN protocol to use for sending trigger messages to multicast."""
    TCP = "lan.TCP"
    """str: Use TCP protocol."""
    TRIG_EITHER = "lan.TRIG_EITHER"
    """str: Sets the trigger operation and detection mode of the specified LAN event to rising or falling edge (positive or negative state)."""  # noqa: E501
    TRIG_FALLING = "lan.TRIG_FALLING"
    """str: Sets the trigger operation and detection mode of the specified LAN event to falling edge (negative state)."""  # noqa: E501
    TRIG_RISING = "lan.TRIG_RISING"
    """str: Sets the trigger operation and detection mode of the specified LAN event to rising edge (positive state)."""  # noqa: E501
    TRIG_RISINGA = "lan.TRIG_RISINGA"
    """str: Sets the trigger operation and detection mode of the specified LAN event to rising edge (positive state)."""  # noqa: E501
    TRIG_RISINGM = "lan.TRIG_RISINGM"
    """str: Sets the trigger operation and detection mode of the specified LAN event to rising edge (positive state)."""  # noqa: E501
    TRIG_SYNCHRONOUS = "lan.TRIG_SYNCHRONOUS"
    """str: Use for compatibility with older instruments; sets the trigger operation and detection mode of the specified LAN event to falling edge (negative state)."""  # noqa: E501
    TRIG_SYNCHRONOUSA = "lan.TRIG_SYNCHRONOUSA"
    """str: Sets the trigger operation and detection mode of the specified LAN event to falling edge (negative state)."""  # noqa: E501
    TRIG_SYNCHRONOUSM = "lan.TRIG_SYNCHRONOUSM"
    """str: Sets the trigger operation and detection mode of the specified LAN event to rising edge (positive state)."""  # noqa: E501
    UDP = "lan.UDP"
    """str: Use UDP protocol."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "lan") -> None:
        super().__init__(device, cmd_syntax)
        self._config = LanConfig(device, f"{self._cmd_syntax}.config")
        self._trigger: Dict[int, LanTriggerItem] = DefaultDictPassKeyToFactory(
            lambda x: LanTriggerItem(device, f"{self._cmd_syntax}.trigger[{x}]")
        )

    @property
    def config(self) -> LanConfig:
        """Return the ``lan.config`` command tree.

        Sub-properties and sub-methods:
            - ``.dns``: The ``lan.config.dns`` command tree.
        """
        return self._config

    @property
    def trigger(self) -> Dict[int, LanTriggerItem]:
        """Return the ``lan.trigger[N]`` command tree.

        Constants:
            - ``.EVENT_ID``: Selects the event that causes a trigger to be asserted on the digital
              output line as the appropriate LXI trigger packet received on LAN trigger object N.
        """
        return self._trigger
