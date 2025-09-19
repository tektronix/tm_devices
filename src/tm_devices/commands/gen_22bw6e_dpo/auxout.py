"""The auxout commands module.

These commands are used in the following models:
DPO7AX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUXout:EDGE {RISing|FALling}
    - AUXout:EDGE?
    - AUXout:LOWLatency {ON|OFF|1|0}
    - AUXout:LOWLatency?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AuxoutLowlatency(SCPICmdWrite, SCPICmdRead):
    """The ``AUXout:LOWLatency`` command.

    Description:
        - When the low latency trigger out setting is enabled, the delay between a trigger occurring
          and a pulse appearing on the auxiliary output BNC connection is reduced.

    Usage:
        - Using the ``.query()`` method will send the ``AUXout:LOWLatency?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXout:LOWLatency?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXout:LOWLatency value`` command.

    SCPI Syntax:
        ```
        - AUXout:LOWLatency {ON|OFF|1|0}
        - AUXout:LOWLatency?
        ```

    Info:
        - ``1 or ON`` enable low latency trigger.
        - ``0 or OFF`` disable low latency trigger.
    """


class AuxoutEdge(SCPICmdWrite, SCPICmdRead):
    """The ``AUXout:EDGE`` command.

    Description:
        - This command sets or queries the direction in which the Auxiliary Output signal will
          transition when a trigger occurs.

    Usage:
        - Using the ``.query()`` method will send the ``AUXout:EDGE?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXout:EDGE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXout:EDGE value`` command.

    SCPI Syntax:
        ```
        - AUXout:EDGE {RISing|FALling}
        - AUXout:EDGE?
        ```

    Info:
        - ``RISing`` sets the polarity to the rising edge.
        - ``FALling`` sets the polarity to the falling edge.
    """


class Auxout(SCPICmdRead):
    """The ``AUXout`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXout?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXout?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.edge``: The ``AUXout:EDGE`` command.
        - ``.lowlatency``: The ``AUXout:LOWLatency`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUXout") -> None:
        super().__init__(device, cmd_syntax)
        self._edge = AuxoutEdge(device, f"{self._cmd_syntax}:EDGE")
        self._lowlatency = AuxoutLowlatency(device, f"{self._cmd_syntax}:LOWLatency")

    @property
    def edge(self) -> AuxoutEdge:
        """Return the ``AUXout:EDGE`` command.

        Description:
            - This command sets or queries the direction in which the Auxiliary Output signal will
              transition when a trigger occurs.

        Usage:
            - Using the ``.query()`` method will send the ``AUXout:EDGE?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXout:EDGE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXout:EDGE value`` command.

        SCPI Syntax:
            ```
            - AUXout:EDGE {RISing|FALling}
            - AUXout:EDGE?
            ```

        Info:
            - ``RISing`` sets the polarity to the rising edge.
            - ``FALling`` sets the polarity to the falling edge.
        """
        return self._edge

    @property
    def lowlatency(self) -> AuxoutLowlatency:
        """Return the ``AUXout:LOWLatency`` command.

        Description:
            - When the low latency trigger out setting is enabled, the delay between a trigger
              occurring and a pulse appearing on the auxiliary output BNC connection is reduced.

        Usage:
            - Using the ``.query()`` method will send the ``AUXout:LOWLatency?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXout:LOWLatency?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXout:LOWLatency value`` command.

        SCPI Syntax:
            ```
            - AUXout:LOWLatency {ON|OFF|1|0}
            - AUXout:LOWLatency?
            ```

        Info:
            - ``1 or ON`` enable low latency trigger.
            - ``0 or OFF`` disable low latency trigger.
        """
        return self._lowlatency
