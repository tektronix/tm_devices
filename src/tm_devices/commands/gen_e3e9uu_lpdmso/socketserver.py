"""The socketserver commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SOCKETServer:ENAble {0|1|OFF|ON}
    - SOCKETServer:ENAble?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SocketserverEnable(SCPICmdWrite, SCPICmdRead):
    """The ``SOCKETServer:ENAble`` command.

    Description:
        - This command enables or disables the socket server which supports a telnet or other TCPIP
          socket connection to send commands and queries to the instrument. The default state is
          enabled.

    Usage:
        - Using the ``.query()`` method will send the ``SOCKETServer:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``SOCKETServer:ENAble?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SOCKETServer:ENAble value`` command.

    SCPI Syntax:
        ```
        - SOCKETServer:ENAble {0|1|OFF|ON}
        - SOCKETServer:ENAble?
        ```

    Info:
        - ``1`` enables the socket server. If the state is 0 (disabled) and this command is sent to
          enable the socket server when the port is in use by another service, then the error event
          code 221 (Settings conflict) is posted to the event queue and the socket server remains
          disabled. In this case, select a different port number and attempt to enable the socket
          server again.
        - ``0`` disables the socket server.
        - ``ON`` enables the socket server.
        - ``OFF`` disables the socket server.
    """


class Socketserver(SCPICmdRead):
    """The ``SOCKETServer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOCKETServer?`` query.
        - Using the ``.verify(value)`` method will send the ``SOCKETServer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``SOCKETServer:ENAble`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "SOCKETServer"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = SocketserverEnable(device, f"{self._cmd_syntax}:ENAble")

    @property
    def enable(self) -> SocketserverEnable:
        """Return the ``SOCKETServer:ENAble`` command.

        Description:
            - This command enables or disables the socket server which supports a telnet or other
              TCPIP socket connection to send commands and queries to the instrument. The default
              state is enabled.

        Usage:
            - Using the ``.query()`` method will send the ``SOCKETServer:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``SOCKETServer:ENAble?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SOCKETServer:ENAble value``
              command.

        SCPI Syntax:
            ```
            - SOCKETServer:ENAble {0|1|OFF|ON}
            - SOCKETServer:ENAble?
            ```

        Info:
            - ``1`` enables the socket server. If the state is 0 (disabled) and this command is sent
              to enable the socket server when the port is in use by another service, then the error
              event code 221 (Settings conflict) is posted to the event queue and the socket server
              remains disabled. In this case, select a different port number and attempt to enable
              the socket server again.
            - ``0`` disables the socket server.
            - ``ON`` enables the socket server.
            - ``OFF`` disables the socket server.
        """
        return self._enable
