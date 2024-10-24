"""The socketserver commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SOCKETServer:ENAble {ON|OFF|<NR1>}
    - SOCKETServer:ENAble?
    - SOCKETServer:PORT <NR1>
    - SOCKETServer:PORT?
    - SOCKETServer:PROTOCol {TERMinal|NONe}
    - SOCKETServer:PROTOCol?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SocketserverProtocol(SCPICmdWrite, SCPICmdRead):
    """The ``SOCKETServer:PROTOCol`` command.

    Description:
        - This command sets or queries the protocol for the socket server.

    Usage:
        - Using the ``.query()`` method will send the ``SOCKETServer:PROTOCol?`` query.
        - Using the ``.verify(value)`` method will send the ``SOCKETServer:PROTOCol?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOCKETServer:PROTOCol value`` command.

    SCPI Syntax:
        ```
        - SOCKETServer:PROTOCol {TERMinal|NONe}
        - SOCKETServer:PROTOCol?
        ```

    Info:
        - ``TERMinal`` specifies terminal protocol for the socket server. When set to TERMinal, a
          session startup message is sent to the socket and a command prompt is provided.
        - ``NONe`` disables the terminal features, allowing the server to be used for raw socket
          transactions, such as with a VISA socket server. The default setting is NONe.
    """


class SocketserverPort(SCPICmdWrite, SCPICmdRead):
    """The ``SOCKETServer:PORT`` command.

    Description:
        - This command sets the TCPIP port for the socket server connection.

    Usage:
        - Using the ``.query()`` method will send the ``SOCKETServer:PORT?`` query.
        - Using the ``.verify(value)`` method will send the ``SOCKETServer:PORT?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOCKETServer:PORT value`` command.

    SCPI Syntax:
        ```
        - SOCKETServer:PORT <NR1>
        - SOCKETServer:PORT?
        ```

    Info:
        - ``<NR1>`` is the TCPIP port for the socket server connection.
    """


class SocketserverEnable(SCPICmdWrite, SCPICmdRead):
    """The ``SOCKETServer:ENAble`` command.

    Description:
        - This command enables or disables the socket server which supports a Telnet or other TCP/IP
          socket connection to send commands and queries to the instrument. The default state is
          enabled.

    Usage:
        - Using the ``.query()`` method will send the ``SOCKETServer:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``SOCKETServer:ENAble?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOCKETServer:ENAble value`` command.

    SCPI Syntax:
        ```
        - SOCKETServer:ENAble {ON|OFF|<NR1>}
        - SOCKETServer:ENAble?
        ```

    Info:
        - ``ON`` enables the socket server.
        - ``OFF`` disables the socket server.
        - ``<NR1> = 0`` disables the socket server; any other value turns it on.
    """


class Socketserver(SCPICmdRead):
    """The ``SOCKETServer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOCKETServer?`` query.
        - Using the ``.verify(value)`` method will send the ``SOCKETServer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``SOCKETServer:ENAble`` command.
        - ``.port``: The ``SOCKETServer:PORT`` command.
        - ``.protocol``: The ``SOCKETServer:PROTOCol`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "SOCKETServer"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = SocketserverEnable(device, f"{self._cmd_syntax}:ENAble")
        self._port = SocketserverPort(device, f"{self._cmd_syntax}:PORT")
        self._protocol = SocketserverProtocol(device, f"{self._cmd_syntax}:PROTOCol")

    @property
    def enable(self) -> SocketserverEnable:
        """Return the ``SOCKETServer:ENAble`` command.

        Description:
            - This command enables or disables the socket server which supports a Telnet or other
              TCP/IP socket connection to send commands and queries to the instrument. The default
              state is enabled.

        Usage:
            - Using the ``.query()`` method will send the ``SOCKETServer:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``SOCKETServer:ENAble?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOCKETServer:ENAble value``
              command.

        SCPI Syntax:
            ```
            - SOCKETServer:ENAble {ON|OFF|<NR1>}
            - SOCKETServer:ENAble?
            ```

        Info:
            - ``ON`` enables the socket server.
            - ``OFF`` disables the socket server.
            - ``<NR1> = 0`` disables the socket server; any other value turns it on.
        """
        return self._enable

    @property
    def port(self) -> SocketserverPort:
        """Return the ``SOCKETServer:PORT`` command.

        Description:
            - This command sets the TCPIP port for the socket server connection.

        Usage:
            - Using the ``.query()`` method will send the ``SOCKETServer:PORT?`` query.
            - Using the ``.verify(value)`` method will send the ``SOCKETServer:PORT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOCKETServer:PORT value`` command.

        SCPI Syntax:
            ```
            - SOCKETServer:PORT <NR1>
            - SOCKETServer:PORT?
            ```

        Info:
            - ``<NR1>`` is the TCPIP port for the socket server connection.
        """
        return self._port

    @property
    def protocol(self) -> SocketserverProtocol:
        """Return the ``SOCKETServer:PROTOCol`` command.

        Description:
            - This command sets or queries the protocol for the socket server.

        Usage:
            - Using the ``.query()`` method will send the ``SOCKETServer:PROTOCol?`` query.
            - Using the ``.verify(value)`` method will send the ``SOCKETServer:PROTOCol?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOCKETServer:PROTOCol value``
              command.

        SCPI Syntax:
            ```
            - SOCKETServer:PROTOCol {TERMinal|NONe}
            - SOCKETServer:PROTOCol?
            ```

        Info:
            - ``TERMinal`` specifies terminal protocol for the socket server. When set to TERMinal,
              a session startup message is sent to the socket and a command prompt is provided.
            - ``NONe`` disables the terminal features, allowing the server to be used for raw socket
              transactions, such as with a VISA socket server. The default setting is NONe.
        """
        return self._protocol
