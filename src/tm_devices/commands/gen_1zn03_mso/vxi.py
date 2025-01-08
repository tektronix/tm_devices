"""The vxi commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - VXI:ENAble {ON|OFF|1|0}
    - VXI:ENAble?
    - VXI:PORT:HIGH <NR1>
    - VXI:PORT:HIGH?
    - VXI:PORT:LOW <NR1>
    - VXI:PORT:LOW?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class VxiPortLow(SCPICmdWrite, SCPICmdRead):
    """The ``VXI:PORT:LOW`` command.

    Description:
        - This command sets or queries the lower end of the port range for the VXI-11 server.

    Usage:
        - Using the ``.query()`` method will send the ``VXI:PORT:LOW?`` query.
        - Using the ``.verify(value)`` method will send the ``VXI:PORT:LOW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VXI:PORT:LOW value`` command.

    SCPI Syntax:
        ```
        - VXI:PORT:LOW <NR1>
        - VXI:PORT:LOW?
        ```

    Info:
        - ``<NR1>`` is the low end of the TCPIP port range for the VXI-11 server connection. Some
          ports are restricted and cannot be used because they are used by other services. If a
          restricted port falls between the VXI-11 server low port and the VXI-11 server high port,
          then the error code 224 (Illegal parameter value) is posted to the event queue and the
          VXI-11 low port remains unchanged. If the VXI-11 low port number is set to a valid value
          above the VXI-11 high port number, the VXI-11 high port number is set to the value of the
          VXI-11 low port number plus one.
    """


class VxiPortHigh(SCPICmdWrite, SCPICmdRead):
    """The ``VXI:PORT:HIGH`` command.

    Description:
        - This command sets or queries the higher end of the port range for the VXI-11 server.

    Usage:
        - Using the ``.query()`` method will send the ``VXI:PORT:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the ``VXI:PORT:HIGH?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VXI:PORT:HIGH value`` command.

    SCPI Syntax:
        ```
        - VXI:PORT:HIGH <NR1>
        - VXI:PORT:HIGH?
        ```

    Info:
        - ``<NR1>`` is the high end of the TCPIP port range for the VXI-11 server connection. Some
          ports are restricted and cannot be used because they are used by other services. If a
          restricted port falls between the VXI-11 server low port and the VXI-11 server high port,
          then the error code 224 (Illegal parameter value) is posted to the event queue and the
          VXI-11 high port remains unchanged. If the VXI-11 high port number is set to a valid value
          below the VXI-11 low port number, the VXI-11 low port number is set to the value of the
          VXI-11 high port number minus one.
    """


class VxiPort(SCPICmdRead):
    """The ``VXI:PORT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VXI:PORT?`` query.
        - Using the ``.verify(value)`` method will send the ``VXI:PORT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.high``: The ``VXI:PORT:HIGH`` command.
        - ``.low``: The ``VXI:PORT:LOW`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = VxiPortHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = VxiPortLow(device, f"{self._cmd_syntax}:LOW")

    @property
    def high(self) -> VxiPortHigh:
        """Return the ``VXI:PORT:HIGH`` command.

        Description:
            - This command sets or queries the higher end of the port range for the VXI-11 server.

        Usage:
            - Using the ``.query()`` method will send the ``VXI:PORT:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the ``VXI:PORT:HIGH?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VXI:PORT:HIGH value`` command.

        SCPI Syntax:
            ```
            - VXI:PORT:HIGH <NR1>
            - VXI:PORT:HIGH?
            ```

        Info:
            - ``<NR1>`` is the high end of the TCPIP port range for the VXI-11 server connection.
              Some ports are restricted and cannot be used because they are used by other services.
              If a restricted port falls between the VXI-11 server low port and the VXI-11 server
              high port, then the error code 224 (Illegal parameter value) is posted to the event
              queue and the VXI-11 high port remains unchanged. If the VXI-11 high port number is
              set to a valid value below the VXI-11 low port number, the VXI-11 low port number is
              set to the value of the VXI-11 high port number minus one.
        """
        return self._high

    @property
    def low(self) -> VxiPortLow:
        """Return the ``VXI:PORT:LOW`` command.

        Description:
            - This command sets or queries the lower end of the port range for the VXI-11 server.

        Usage:
            - Using the ``.query()`` method will send the ``VXI:PORT:LOW?`` query.
            - Using the ``.verify(value)`` method will send the ``VXI:PORT:LOW?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VXI:PORT:LOW value`` command.

        SCPI Syntax:
            ```
            - VXI:PORT:LOW <NR1>
            - VXI:PORT:LOW?
            ```

        Info:
            - ``<NR1>`` is the low end of the TCPIP port range for the VXI-11 server connection.
              Some ports are restricted and cannot be used because they are used by other services.
              If a restricted port falls between the VXI-11 server low port and the VXI-11 server
              high port, then the error code 224 (Illegal parameter value) is posted to the event
              queue and the VXI-11 low port remains unchanged. If the VXI-11 low port number is set
              to a valid value above the VXI-11 high port number, the VXI-11 high port number is set
              to the value of the VXI-11 low port number plus one.
        """
        return self._low


class VxiEnable(SCPICmdWrite, SCPICmdRead):
    """The ``VXI:ENAble`` command.

    Description:
        - This command sets or queries the state of the VXI-11 server, which is used for command and
          control over an Ethernet connection.

    Usage:
        - Using the ``.query()`` method will send the ``VXI:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``VXI:ENAble?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``VXI:ENAble value`` command.

    SCPI Syntax:
        ```
        - VXI:ENAble {ON|OFF|1|0}
        - VXI:ENAble?
        ```

    Info:
        - ``ON`` enables the VXI-11 server.
        - ``OFF`` disables the VXI-11 server.
        - ``1`` enables the VXI-11 server.
        - ``0`` disables the VXI-11 server.
    """


class Vxi(SCPICmdRead):
    """The ``VXI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``VXI?`` query.
        - Using the ``.verify(value)`` method will send the ``VXI?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``VXI:ENAble`` command.
        - ``.port``: The ``VXI:PORT`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "VXI") -> None:
        super().__init__(device, cmd_syntax)
        self._enable = VxiEnable(device, f"{self._cmd_syntax}:ENAble")
        self._port = VxiPort(device, f"{self._cmd_syntax}:PORT")

    @property
    def enable(self) -> VxiEnable:
        """Return the ``VXI:ENAble`` command.

        Description:
            - This command sets or queries the state of the VXI-11 server, which is used for command
              and control over an Ethernet connection.

        Usage:
            - Using the ``.query()`` method will send the ``VXI:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``VXI:ENAble?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``VXI:ENAble value`` command.

        SCPI Syntax:
            ```
            - VXI:ENAble {ON|OFF|1|0}
            - VXI:ENAble?
            ```

        Info:
            - ``ON`` enables the VXI-11 server.
            - ``OFF`` disables the VXI-11 server.
            - ``1`` enables the VXI-11 server.
            - ``0`` disables the VXI-11 server.
        """
        return self._enable

    @property
    def port(self) -> VxiPort:
        """Return the ``VXI:PORT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``VXI:PORT?`` query.
            - Using the ``.verify(value)`` method will send the ``VXI:PORT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``VXI:PORT:HIGH`` command.
            - ``.low``: The ``VXI:PORT:LOW`` command.
        """
        return self._port
