"""The hsinterface commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HSInterface:PORT <NR1>
    - HSInterface:PORT?
    - HSInterface:STATe {0|1}
    - HSInterface:STATe?
    - HSInterface:TIMeout <NR1>
    - HSInterface:TIMeout?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class HsinterfaceTimeout(SCPICmdWrite, SCPICmdRead):
    """The ``HSInterface:TIMeout`` command.

    Description:
        - This command sets or queries the timeout for the high speed interface. If a client is
          waiting for data and no new data is acquired within the specified timeout, the high speed
          interface will disconnect the client.

    Usage:
        - Using the ``.query()`` method will send the ``HSInterface:TIMeout?`` query.
        - Using the ``.verify(value)`` method will send the ``HSInterface:TIMeout?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HSInterface:TIMeout value`` command.

    SCPI Syntax:
        ```
        - HSInterface:TIMeout <NR1>
        - HSInterface:TIMeout?
        ```

    Info:
        - ``<NR1>`` is the amount of time in seconds. The default value is 20 seconds.
    """


class HsinterfaceState(SCPICmdWrite, SCPICmdRead):
    """The ``HSInterface:STATe`` command.

    Description:
        - This command enables or disables the high speed interface.

    Usage:
        - Using the ``.query()`` method will send the ``HSInterface:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``HSInterface:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HSInterface:STATe value`` command.

    SCPI Syntax:
        ```
        - HSInterface:STATe {0|1}
        - HSInterface:STATe?
        ```

    Info:
        - ``0`` disables high speed interface. This is the default value.
        - ``1`` enables high speed interface.
    """


class HsinterfacePort(SCPICmdWrite, SCPICmdRead):
    """The ``HSInterface:PORT`` command.

    Description:
        - This command sets or queries the port that the high speed interface listens on.

    Usage:
        - Using the ``.query()`` method will send the ``HSInterface:PORT?`` query.
        - Using the ``.verify(value)`` method will send the ``HSInterface:PORT?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HSInterface:PORT value`` command.

    SCPI Syntax:
        ```
        - HSInterface:PORT <NR1>
        - HSInterface:PORT?
        ```

    Info:
        - ``<NR1>`` is the port number that the high speed interface listens. The default value is
          5000.
    """


class Hsinterface(SCPICmdRead):
    """The ``HSInterface`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HSInterface?`` query.
        - Using the ``.verify(value)`` method will send the ``HSInterface?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.port``: The ``HSInterface:PORT`` command.
        - ``.state``: The ``HSInterface:STATe`` command.
        - ``.timeout``: The ``HSInterface:TIMeout`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "HSInterface"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._port = HsinterfacePort(device, f"{self._cmd_syntax}:PORT")
        self._state = HsinterfaceState(device, f"{self._cmd_syntax}:STATe")
        self._timeout = HsinterfaceTimeout(device, f"{self._cmd_syntax}:TIMeout")

    @property
    def port(self) -> HsinterfacePort:
        """Return the ``HSInterface:PORT`` command.

        Description:
            - This command sets or queries the port that the high speed interface listens on.

        Usage:
            - Using the ``.query()`` method will send the ``HSInterface:PORT?`` query.
            - Using the ``.verify(value)`` method will send the ``HSInterface:PORT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HSInterface:PORT value`` command.

        SCPI Syntax:
            ```
            - HSInterface:PORT <NR1>
            - HSInterface:PORT?
            ```

        Info:
            - ``<NR1>`` is the port number that the high speed interface listens. The default value
              is 5000.
        """
        return self._port

    @property
    def state(self) -> HsinterfaceState:
        """Return the ``HSInterface:STATe`` command.

        Description:
            - This command enables or disables the high speed interface.

        Usage:
            - Using the ``.query()`` method will send the ``HSInterface:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``HSInterface:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HSInterface:STATe value`` command.

        SCPI Syntax:
            ```
            - HSInterface:STATe {0|1}
            - HSInterface:STATe?
            ```

        Info:
            - ``0`` disables high speed interface. This is the default value.
            - ``1`` enables high speed interface.
        """
        return self._state

    @property
    def timeout(self) -> HsinterfaceTimeout:
        """Return the ``HSInterface:TIMeout`` command.

        Description:
            - This command sets or queries the timeout for the high speed interface. If a client is
              waiting for data and no new data is acquired within the specified timeout, the high
              speed interface will disconnect the client.

        Usage:
            - Using the ``.query()`` method will send the ``HSInterface:TIMeout?`` query.
            - Using the ``.verify(value)`` method will send the ``HSInterface:TIMeout?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HSInterface:TIMeout value``
              command.

        SCPI Syntax:
            ```
            - HSInterface:TIMeout <NR1>
            - HSInterface:TIMeout?
            ```

        Info:
            - ``<NR1>`` is the amount of time in seconds. The default value is 20 seconds.
        """
        return self._timeout
