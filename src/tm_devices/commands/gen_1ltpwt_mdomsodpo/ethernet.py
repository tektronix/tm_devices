"""The ethernet commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

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
    - ETHERnet:LXI:LAN:PASSWord:ENABle {0|1|ON|OFF}
    - ETHERnet:LXI:LAN:PASSWord:ENABle?
    - ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle {0|1|ON|OFF}
    - ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle?
    - ETHERnet:LXI:LAN:RESET
    - ETHERnet:LXI:LAN:SERVICENAMe QString
    - ETHERnet:LXI:LAN:SERVICENAMe?
    - ETHERnet:LXI:LAN:STATus?
    - ETHERnet:NAME <QString>
    - ETHERnet:NAME?
    - ETHERnet:NETWORKCONFig {AUTOmatic|MANual}
    - ETHERnet:NETWORKCONFig?
    - ETHERnet:PASSWord <new>
    - ETHERnet:PASSWord?
    - ETHERnet:PING EXECute
    - ETHERnet:PING:STATus?
    - ETHERnet:SUBNETMask <QString>
    - ETHERnet:SUBNETMask?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

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
    """The ``ETHERnet:PING:STATus`` command.

    Description:
        - Returns the results of sending the ``ETHERNET:PING`` command to ping the gateway IP
          address.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:PING:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:PING:STATus?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ETHERnet:PING:STATus?
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
        - ``.status``: The ``ETHERnet:PING:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._status = EthernetPingStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def status(self) -> EthernetPingStatus:
        """Return the ``ETHERnet:PING:STATus`` command.

        Description:
            - Returns the results of sending the ``ETHERNET:PING`` command to ping the gateway IP
              address.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:PING:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:PING:STATus?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ETHERnet:PING:STATus?
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


class EthernetNetworkconfig(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:NETWORKCONFig`` command.

    Description:
        - This command specifies the Ethernet network configuration setting.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:NETWORKCONFig?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:NETWORKCONFig?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ETHERnet:NETWORKCONFig value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:NETWORKCONFig {AUTOmatic|MANual}
        - ETHERnet:NETWORKCONFig?
        ```

    Info:
        - ``AUTOmatic`` specifies that the instrument's IP address, subnet mask and gateway settings
          will be received from a DHCP server on the local network.
        - ``MANual`` specifies that the Ethernet settings will be configured manually, using
          ``ETHERNET:IPADDRESS``, ``ETHERNET:SUBNETMASK``, and ``ETHERNET:GATEWAY:IPADDRESS``.
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


class EthernetLxiLanStatus(SCPICmdRead):
    """The ``ETHERnet:LXI:LAN:STATus`` command.

    Description:
        - This query returns the LXI network status: one of OK, FAULT, or IDENTIFY. IDENTIFY
          indicates that the device identify mode is enabled.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:LXI:LAN:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:LXI:LAN:STATus?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ETHERnet:LXI:LAN:STATus?
        ```
    """


class EthernetLxiLanServicename(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:LXI:LAN:SERVICENAMe`` command.

    Description:
        - This command specifies the mDNS service name used for the LXI interface.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:LXI:LAN:SERVICENAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:LXI:LAN:SERVICENAMe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ETHERnet:LXI:LAN:SERVICENAMe value``
          command.

    SCPI Syntax:
        ```
        - ETHERnet:LXI:LAN:SERVICENAMe QString
        - ETHERnet:LXI:LAN:SERVICENAMe?
        ```
    """


class EthernetLxiLanReset(SCPICmdWriteNoArguments):
    """The ``ETHERnet:LXI:LAN:RESET`` command.

    Description:
        - This command resets the LXI local area network.

    Usage:
        - Using the ``.write()`` method will send the ``ETHERnet:LXI:LAN:RESET`` command.

    SCPI Syntax:
        ```
        - ETHERnet:LXI:LAN:RESET
        ```
    """


class EthernetLxiLanPasswordEscopeenable(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle`` command.

    Description:
        - This command controls whether to use the LXI password for e``*Scope`` (effectively equal
          to enabling password protection for e``*Scope``). With e``*Scope``, you can access any
          Internet-connected 3 Series Mixed Domain Oscilloscope from a web browser.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle {0|1|ON|OFF}
        - ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle?
        ```

    Info:
        - ``0, OFF`` turns off the LXI password feature for e``*Scope``. This is the default.
        - ``1, ON`` turns on the LXI password feature for e``*Scope``.
    """


class EthernetLxiLanPasswordEnable(SCPICmdWrite, SCPICmdRead):
    """The ``ETHERnet:LXI:LAN:PASSWord:ENABle`` command.

    Description:
        - This command controls whether LXI (LAN eXtensions for Instrumentation) is password
          protected.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:LXI:LAN:PASSWord:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:LXI:LAN:PASSWord:ENABle?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ETHERnet:LXI:LAN:PASSWord:ENABle value`` command.

    SCPI Syntax:
        ```
        - ETHERnet:LXI:LAN:PASSWord:ENABle {0|1|ON|OFF}
        - ETHERnet:LXI:LAN:PASSWord:ENABle?
        ```

    Info:
        - ``0, OFF`` - turns off the LXI password feature. This is the default.
        - ``1, ON`` - turns on the LXI password feature.
    """


class EthernetLxiLanPassword(SCPICmdRead):
    """The ``ETHERnet:LXI:LAN:PASSWord`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:LXI:LAN:PASSWord?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:LXI:LAN:PASSWord?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``ETHERnet:LXI:LAN:PASSWord:ENABle`` command.
        - ``.escopeenable``: The ``ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = EthernetLxiLanPasswordEnable(device, f"{self._cmd_syntax}:ENABle")
        self._escopeenable = EthernetLxiLanPasswordEscopeenable(
            device, f"{self._cmd_syntax}:ESCOPEENABle"
        )

    @property
    def enable(self) -> EthernetLxiLanPasswordEnable:
        """Return the ``ETHERnet:LXI:LAN:PASSWord:ENABle`` command.

        Description:
            - This command controls whether LXI (LAN eXtensions for Instrumentation) is password
              protected.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:LXI:LAN:PASSWord:ENABle?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ETHERnet:LXI:LAN:PASSWord:ENABle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ETHERnet:LXI:LAN:PASSWord:ENABle value`` command.

        SCPI Syntax:
            ```
            - ETHERnet:LXI:LAN:PASSWord:ENABle {0|1|ON|OFF}
            - ETHERnet:LXI:LAN:PASSWord:ENABle?
            ```

        Info:
            - ``0, OFF`` - turns off the LXI password feature. This is the default.
            - ``1, ON`` - turns on the LXI password feature.
        """
        return self._enable

    @property
    def escopeenable(self) -> EthernetLxiLanPasswordEscopeenable:
        """Return the ``ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle`` command.

        Description:
            - This command controls whether to use the LXI password for e``*Scope`` (effectively
              equal to enabling password protection for e``*Scope``). With e``*Scope``, you can
              access any Internet-connected 3 Series Mixed Domain Oscilloscope from a web browser.

        Usage:
            - Using the ``.query()`` method will send the
              ``ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle value`` command.

        SCPI Syntax:
            ```
            - ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle {0|1|ON|OFF}
            - ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle?
            ```

        Info:
            - ``0, OFF`` turns off the LXI password feature for e``*Scope``. This is the default.
            - ``1, ON`` turns on the LXI password feature for e``*Scope``.
        """
        return self._escopeenable


class EthernetLxiLan(SCPICmdRead):
    """The ``ETHERnet:LXI:LAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:LXI:LAN?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:LXI:LAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.password``: The ``ETHERnet:LXI:LAN:PASSWord`` command tree.
        - ``.reset``: The ``ETHERnet:LXI:LAN:RESET`` command.
        - ``.servicename``: The ``ETHERnet:LXI:LAN:SERVICENAMe`` command.
        - ``.status``: The ``ETHERnet:LXI:LAN:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._password = EthernetLxiLanPassword(device, f"{self._cmd_syntax}:PASSWord")
        self._reset = EthernetLxiLanReset(device, f"{self._cmd_syntax}:RESET")
        self._servicename = EthernetLxiLanServicename(device, f"{self._cmd_syntax}:SERVICENAMe")
        self._status = EthernetLxiLanStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def password(self) -> EthernetLxiLanPassword:
        """Return the ``ETHERnet:LXI:LAN:PASSWord`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:LXI:LAN:PASSWord?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:LXI:LAN:PASSWord?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``ETHERnet:LXI:LAN:PASSWord:ENABle`` command.
            - ``.escopeenable``: The ``ETHERnet:LXI:LAN:PASSWord:ESCOPEENABle`` command.
        """
        return self._password

    @property
    def reset(self) -> EthernetLxiLanReset:
        """Return the ``ETHERnet:LXI:LAN:RESET`` command.

        Description:
            - This command resets the LXI local area network.

        Usage:
            - Using the ``.write()`` method will send the ``ETHERnet:LXI:LAN:RESET`` command.

        SCPI Syntax:
            ```
            - ETHERnet:LXI:LAN:RESET
            ```
        """
        return self._reset

    @property
    def servicename(self) -> EthernetLxiLanServicename:
        """Return the ``ETHERnet:LXI:LAN:SERVICENAMe`` command.

        Description:
            - This command specifies the mDNS service name used for the LXI interface.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:LXI:LAN:SERVICENAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:LXI:LAN:SERVICENAMe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ETHERnet:LXI:LAN:SERVICENAMe value`` command.

        SCPI Syntax:
            ```
            - ETHERnet:LXI:LAN:SERVICENAMe QString
            - ETHERnet:LXI:LAN:SERVICENAMe?
            ```
        """
        return self._servicename

    @property
    def status(self) -> EthernetLxiLanStatus:
        """Return the ``ETHERnet:LXI:LAN:STATus`` command.

        Description:
            - This query returns the LXI network status: one of OK, FAULT, or IDENTIFY. IDENTIFY
              indicates that the device identify mode is enabled.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:LXI:LAN:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:LXI:LAN:STATus?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ETHERnet:LXI:LAN:STATus?
            ```
        """
        return self._status


class EthernetLxi(SCPICmdRead):
    """The ``ETHERnet:LXI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ETHERnet:LXI?`` query.
        - Using the ``.verify(value)`` method will send the ``ETHERnet:LXI?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.lan``: The ``ETHERnet:LXI:LAN`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lan = EthernetLxiLan(device, f"{self._cmd_syntax}:LAN")

    @property
    def lan(self) -> EthernetLxiLan:
        """Return the ``ETHERnet:LXI:LAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:LXI:LAN?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:LXI:LAN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.password``: The ``ETHERnet:LXI:LAN:PASSWord`` command tree.
            - ``.reset``: The ``ETHERnet:LXI:LAN:RESET`` command.
            - ``.servicename``: The ``ETHERnet:LXI:LAN:SERVICENAMe`` command.
            - ``.status``: The ``ETHERnet:LXI:LAN:STATus`` command.
        """
        return self._lan


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
        - ``.lxi``: The ``ETHERnet:LXI`` command tree.
        - ``.name``: The ``ETHERnet:NAME`` command.
        - ``.networkconfig``: The ``ETHERnet:NETWORKCONFig`` command.
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
        self._lxi = EthernetLxi(device, f"{self._cmd_syntax}:LXI")
        self._name = EthernetName(device, f"{self._cmd_syntax}:NAME")
        self._networkconfig = EthernetNetworkconfig(device, f"{self._cmd_syntax}:NETWORKCONFig")
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
    def lxi(self) -> EthernetLxi:
        """Return the ``ETHERnet:LXI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:LXI?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:LXI?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.lan``: The ``ETHERnet:LXI:LAN`` command tree.
        """
        return self._lxi

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
    def networkconfig(self) -> EthernetNetworkconfig:
        """Return the ``ETHERnet:NETWORKCONFig`` command.

        Description:
            - This command specifies the Ethernet network configuration setting.

        Usage:
            - Using the ``.query()`` method will send the ``ETHERnet:NETWORKCONFig?`` query.
            - Using the ``.verify(value)`` method will send the ``ETHERnet:NETWORKCONFig?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ETHERnet:NETWORKCONFig value``
              command.

        SCPI Syntax:
            ```
            - ETHERnet:NETWORKCONFig {AUTOmatic|MANual}
            - ETHERnet:NETWORKCONFig?
            ```

        Info:
            - ``AUTOmatic`` specifies that the instrument's IP address, subnet mask and gateway
              settings will be received from a DHCP server on the local network.
            - ``MANual`` specifies that the Ethernet settings will be configured manually, using
              ``ETHERNET:IPADDRESS``, ``ETHERNET:SUBNETMASK``, and ``ETHERNET:GATEWAY:IPADDRESS``.
        """
        return self._networkconfig

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
            - ``.status``: The ``ETHERnet:PING:STATus`` command.
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
