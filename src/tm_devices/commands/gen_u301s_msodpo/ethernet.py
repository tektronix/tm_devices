"""The ethernet commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ETHERnet:DHCPbootp {ON|OFF}
    - ETHERnet:DHCPbootp?
    - ETHERnet:DNS:IPADDress <QString>
    - ETHERnet:DNS:IPADDress?
    - ETHERnet:DOMAINname <Qstring>
    - ETHERnet:DOMAINname?
    - ETHERnet:ENET:ADDress?
    - ETHERnet:GATEWay:IPADDress <QString>
    - ETHERnet:GATEWay:IPADDress?
    - ETHERnet:HTTPPort <QString>
    - ETHERnet:HTTPPort?
    - ETHERnet:IPADDress <QString>
    - ETHERnet:IPADDress?
    - ETHERnet:NAME <QString>
    - ETHERnet:NAME?
    - ETHERnet:PASSWord <new>
    - ETHERnet:PASSWord?
    - ETHERnet:PING EXECute
    - ETHERnet:PING:STATUS?
    - ETHERnet:SUBNETMask <QString>
    - ETHERnet:SUBNETMask?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class EthernetSubnetmask(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:SUBNETMask`` command.

    Description:
        - This command sets or queries the instrument subnet mask value.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:SUBNETMask?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:SUBNETMask?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ETHERnet:SUBNETMask value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:SUBNETMask <QString>
        - ETHERnet:SUBNETMask?
        ```

    Info:
        - ``<QString>`` is the subnet mask value, enclosed in quotes.
    """

    _WRAP_ARG_WITH_QUOTES = True


class EthernetPingStatus(SCPICmdRead):
    """The ``ETHERnet:PING:STATUS`` command.

    Description:
        - Returns the results from sending the ``ETHERNET:PING`` command to ping the gateway IP
          address.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:PING:STATUS?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:PING:STATUS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ETHERnet:PING:STATUS?
        ```
    """


class EthernetPing(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:PING`` command.

    Description:
        - Sends a ping packet to the instrument gateway and sets the status accordingly.

    Usage:
        - Using the ``.write(value)`` method will send the ``ETHERnet:PING value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:PING EXECute
        ```

    Properties:
        - ``.status``: The ``ETHERnet:PING:STATUS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = EthernetPingStatus(device, f"{self._cmd_syntax}:STATUS")

    @property
    def status(self) -> EthernetPingStatus:
        """Return the ``ETHERnet:PING:STATUS`` command.

        Description:
            - Returns the results from sending the ``ETHERNET:PING`` command to ping the gateway IP
              address.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:PING:STATUS?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:PING:STATUS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ETHERnet:PING:STATUS?
            ```
        """
        return self._status


class EthernetPassword(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:PASSWord`` command.

    Description:
        - This command specifies the HTTP Ethernet access password. If a password is set, the user
          must enter the password before the user's Web browser can access the oscilloscope.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:PASSWord?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:PASSWord?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ETHERnet:PASSWord value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:PASSWord <new>
        - ETHERnet:PASSWord?
        ```

    Info:
        - ``<new>`` is a new password, enclosed in quotes.
    """


class EthernetName(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:NAME`` command.

    Description:
        - This command sets or queries the instrument Ethernet hostname assigned to the instrument.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:NAME?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:NAME?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ETHERnet:NAME value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:NAME <QString>
        - ETHERnet:NAME?
        ```

    Info:
        - ``<QString>`` is the network name assigned to the instrument, enclosed in quotes.
    """

    _WRAP_ARG_WITH_QUOTES = True


class EthernetIpaddress(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:IPADDress`` command.

    Description:
        - This command sets the IP address assigned to the instrument.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:IPADDress?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:IPADDress?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ETHERnet:IPADDress value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:IPADDress <QString>
        - ETHERnet:IPADDress?
        ```

    Info:
        - ``<QString>`` is a standard IP address value, enclosed in quotes.
    """

    _WRAP_ARG_WITH_QUOTES = True


class EthernetHttpport(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:HTTPPort`` command.

    Description:
        - This command specifies the remote interface HTTP port value.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:HTTPPort?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:HTTPPort?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ETHERnet:HTTPPort value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:HTTPPort <QString>
        - ETHERnet:HTTPPort?
        ```

    Info:
        - ``<QString>`` is an integer port number, enclosed in quotes.
    """

    _WRAP_ARG_WITH_QUOTES = True


class EthernetGatewayIpaddress(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:GATEWay:IPADDress`` command.

    Description:
        - This command specifies the network gateway IP address.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:GATEWay:IPADDress?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:GATEWay:IPADDress?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ETHERnet:GATEWay:IPADDress value``
          command.

    SCPI Syntax:
        ```
        - ETHERnet:GATEWay:IPADDress <QString>
        - ETHERnet:GATEWay:IPADDress?
        ```

    Info:
        - ``<QString>`` is a standard IP address value, enclosed in quotes.
    """

    _WRAP_ARG_WITH_QUOTES = True


class EthernetGateway(SCPICmdRead):
    """The ``ETHERnet:GATEWay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:GATEWay?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:GATEWay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ipaddress``: The ``ETHERnet:GATEWay:IPADDress`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ipaddress = EthernetGatewayIpaddress(device, f"{self._cmd_syntax}:IPADDress")

    @property
    def ipaddress(self) -> EthernetGatewayIpaddress:
        """Return the ``ETHERnet:GATEWay:IPADDress`` command.

        Description:
            - This command specifies the network gateway IP address.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:GATEWay:IPADDress?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:GATEWay:IPADDress?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ETHERnet:GATEWay:IPADDress value``
              command.

        SCPI Syntax:
            ```
            - ETHERnet:GATEWay:IPADDress <QString>
            - ETHERnet:GATEWay:IPADDress?
            ```

        Info:
            - ``<QString>`` is a standard IP address value, enclosed in quotes.
        """
        return self._ipaddress


class EthernetEnetAddress(SCPICmdRead):
    """The ``ETHERnet:ENET:ADDress`` command.

    Description:
        - Returns the Ethernet address (MAC address) value assigned to the instrument. This is
          assigned at the factory and can not be changed.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:ENET:ADDress?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:ENET:ADDress?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ETHERnet:ENET:ADDress?
        ```
    """


class EthernetEnet(SCPICmdRead):
    """The ``ETHERnet:ENET`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:ENET?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:ENET?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.address``: The ``ETHERnet:ENET:ADDress`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._address = EthernetEnetAddress(device, f"{self._cmd_syntax}:ADDress")

    @property
    def address(self) -> EthernetEnetAddress:
        """Return the ``ETHERnet:ENET:ADDress`` command.

        Description:
            - Returns the Ethernet address (MAC address) value assigned to the instrument. This is
              assigned at the factory and can not be changed.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:ENET:ADDress?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:ENET:ADDress?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ETHERnet:ENET:ADDress?
            ```
        """
        return self._address


class EthernetDomainname(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:DOMAINname`` command.

    Description:
        - This command specifies the network domain name.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:DOMAINname?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:DOMAINname?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ETHERnet:DOMAINname value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:DOMAINname <Qstring>
        - ETHERnet:DOMAINname?
        ```

    Info:
        - ``<QString>`` is the network domain name, enclosed in quotes.
    """


class EthernetDnsIpaddress(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:DNS:IPADDress`` command.

    Description:
        - This command specifies the network Domain Name Server (DNS) IP address.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:DNS:IPADDress?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:DNS:IPADDress?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ETHERnet:DNS:IPADDress value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:DNS:IPADDress <QString>
        - ETHERnet:DNS:IPADDress?
        ```

    Info:
        - ``<QString>`` is a standard IP address value, enclosed in quotes.
    """

    _WRAP_ARG_WITH_QUOTES = True


class EthernetDns(SCPICmdRead):
    """The ``ETHERnet:DNS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:DNS?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:DNS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ipaddress``: The ``ETHERnet:DNS:IPADDress`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ipaddress = EthernetDnsIpaddress(device, f"{self._cmd_syntax}:IPADDress")

    @property
    def ipaddress(self) -> EthernetDnsIpaddress:
        """Return the ``ETHERnet:DNS:IPADDress`` command.

        Description:
            - This command specifies the network Domain Name Server (DNS) IP address.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:DNS:IPADDress?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:DNS:IPADDress?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ETHERnet:DNS:IPADDress value``
              command.

        SCPI Syntax:
            ```
            - ETHERnet:DNS:IPADDress <QString>
            - ETHERnet:DNS:IPADDress?
            ```

        Info:
            - ``<QString>`` is a standard IP address value, enclosed in quotes.
        """
        return self._ipaddress


class EthernetDhcpbootp(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:DHCPbootp`` command.

    Description:
        - This command sets the network configuration method to DHCP (that is ON) or static IP
          address (that is OFF).

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:DHCPbootp?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:DHCPbootp?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ETHERnet:DHCPbootp value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:DHCPbootp {ON|OFF}
        - ETHERnet:DHCPbootp?
        ```

    Info:
        - ``ON`` enables the instrument to search the network for a DHCP server in order to
          automatically assign a dynamic IP address to the instrument.
        - ``OFF`` disables the instrument to search the network for a DHCP server.
    """


#  pylint: disable=too-many-instance-attributes
class Ethernet(SCPICmdRead):
    """The ``ETHERnet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dhcpbootp``: The ``ETHERnet:DHCPbootp`` command.
        - ``.dns``: The ``ETHERnet:DNS`` command tree.
        - ``.domainname``: The ``ETHERnet:DOMAINname`` command.
        - ``.enet``: The ``ETHERnet:ENET`` command tree.
        - ``.gateway``: The ``ETHERnet:GATEWay`` command tree.
        - ``.httpport``: The ``ETHERnet:HTTPPort`` command.
        - ``.ipaddress``: The ``ETHERnet:IPADDress`` command.
        - ``.name``: The ``ETHERnet:NAME`` command.
        - ``.password``: The ``ETHERnet:PASSWord`` command.
        - ``.ping``: The ``ETHERnet:PING`` command.
        - ``.subnetmask``: The ``ETHERnet:SUBNETMask`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ETHERnet") -> None:
        super().__init__(device, cmd_syntax)
        self._dhcpbootp = EthernetDhcpbootp(device, f"{self._cmd_syntax}:DHCPbootp")
        self._dns = EthernetDns(device, f"{self._cmd_syntax}:DNS")
        self._domainname = EthernetDomainname(device, f"{self._cmd_syntax}:DOMAINname")
        self._enet = EthernetEnet(device, f"{self._cmd_syntax}:ENET")
        self._gateway = EthernetGateway(device, f"{self._cmd_syntax}:GATEWay")
        self._httpport = EthernetHttpport(device, f"{self._cmd_syntax}:HTTPPort")
        self._ipaddress = EthernetIpaddress(device, f"{self._cmd_syntax}:IPADDress")
        self._name = EthernetName(device, f"{self._cmd_syntax}:NAME")
        self._password = EthernetPassword(device, f"{self._cmd_syntax}:PASSWord")
        self._ping = EthernetPing(device, f"{self._cmd_syntax}:PING")
        self._subnetmask = EthernetSubnetmask(device, f"{self._cmd_syntax}:SUBNETMask")

    @property
    def dhcpbootp(self) -> EthernetDhcpbootp:
        """Return the ``ETHERnet:DHCPbootp`` command.

        Description:
            - This command sets the network configuration method to DHCP (that is ON) or static IP
              address (that is OFF).

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:DHCPbootp?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:DHCPbootp?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ETHERnet:DHCPbootp value`` command.

        SCPI Syntax:
            ```
            - ETHERnet:DHCPbootp {ON|OFF}
            - ETHERnet:DHCPbootp?
            ```

        Info:
            - ``ON`` enables the instrument to search the network for a DHCP server in order to
              automatically assign a dynamic IP address to the instrument.
            - ``OFF`` disables the instrument to search the network for a DHCP server.
        """
        return self._dhcpbootp

    @property
    def dns(self) -> EthernetDns:
        """Return the ``ETHERnet:DNS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:DNS?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:DNS?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ipaddress``: The ``ETHERnet:DNS:IPADDress`` command.
        """
        return self._dns

    @property
    def domainname(self) -> EthernetDomainname:
        """Return the ``ETHERnet:DOMAINname`` command.

        Description:
            - This command specifies the network domain name.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:DOMAINname?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:DOMAINname?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ETHERnet:DOMAINname value``
              command.

        SCPI Syntax:
            ```
            - ETHERnet:DOMAINname <Qstring>
            - ETHERnet:DOMAINname?
            ```

        Info:
            - ``<QString>`` is the network domain name, enclosed in quotes.
        """
        return self._domainname

    @property
    def enet(self) -> EthernetEnet:
        """Return the ``ETHERnet:ENET`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:ENET?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:ENET?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.address``: The ``ETHERnet:ENET:ADDress`` command.
        """
        return self._enet

    @property
    def gateway(self) -> EthernetGateway:
        """Return the ``ETHERnet:GATEWay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:GATEWay?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:GATEWay?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ipaddress``: The ``ETHERnet:GATEWay:IPADDress`` command.
        """
        return self._gateway

    @property
    def httpport(self) -> EthernetHttpport:
        """Return the ``ETHERnet:HTTPPort`` command.

        Description:
            - This command specifies the remote interface HTTP port value.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:HTTPPort?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:HTTPPort?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ETHERnet:HTTPPort value`` command.

        SCPI Syntax:
            ```
            - ETHERnet:HTTPPort <QString>
            - ETHERnet:HTTPPort?
            ```

        Info:
            - ``<QString>`` is an integer port number, enclosed in quotes.
        """
        return self._httpport

    @property
    def ipaddress(self) -> EthernetIpaddress:
        """Return the ``ETHERnet:IPADDress`` command.

        Description:
            - This command sets the IP address assigned to the instrument.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:IPADDress?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:IPADDress?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ETHERnet:IPADDress value`` command.

        SCPI Syntax:
            ```
            - ETHERnet:IPADDress <QString>
            - ETHERnet:IPADDress?
            ```

        Info:
            - ``<QString>`` is a standard IP address value, enclosed in quotes.
        """
        return self._ipaddress

    @property
    def name(self) -> EthernetName:
        """Return the ``ETHERnet:NAME`` command.

        Description:
            - This command sets or queries the instrument Ethernet hostname assigned to the
              instrument.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:NAME?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:NAME?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ETHERnet:NAME value`` command.

        SCPI Syntax:
            ```
            - ETHERnet:NAME <QString>
            - ETHERnet:NAME?
            ```

        Info:
            - ``<QString>`` is the network name assigned to the instrument, enclosed in quotes.
        """
        return self._name

    @property
    def password(self) -> EthernetPassword:
        """Return the ``ETHERnet:PASSWord`` command.

        Description:
            - This command specifies the HTTP Ethernet access password. If a password is set, the
              user must enter the password before the user's Web browser can access the
              oscilloscope.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:PASSWord?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:PASSWord?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ETHERnet:PASSWord value`` command.

        SCPI Syntax:
            ```
            - ETHERnet:PASSWord <new>
            - ETHERnet:PASSWord?
            ```

        Info:
            - ``<new>`` is a new password, enclosed in quotes.
        """
        return self._password

    @property
    def ping(self) -> EthernetPing:
        """Return the ``ETHERnet:PING`` command.

        Description:
            - Sends a ping packet to the instrument gateway and sets the status accordingly.

        Usage:
            - Using the ``.write(value)`` method will send the ``ETHERnet:PING value`` command.

        SCPI Syntax:
            ```
            - ETHERnet:PING EXECute
            ```

        Sub-properties:
            - ``.status``: The ``ETHERnet:PING:STATUS`` command.
        """
        return self._ping

    @property
    def subnetmask(self) -> EthernetSubnetmask:
        """Return the ``ETHERnet:SUBNETMask`` command.

        Description:
            - This command sets or queries the instrument subnet mask value.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:SUBNETMask?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:SUBNETMask?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ETHERnet:SUBNETMask value``
              command.

        SCPI Syntax:
            ```
            - ETHERnet:SUBNETMask <QString>
            - ETHERnet:SUBNETMask?
            ```

        Info:
            - ``<QString>`` is the subnet mask value, enclosed in quotes.
        """
        return self._subnetmask
