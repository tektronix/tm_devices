"""The rrb commands module.

These commands are used in the following models:
MDO3

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - RRB:STATE {ON|OFF|<NR1>}
    - RRB:STATE?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class RrbState(SCPICmdWrite, SCPICmdRead):
    """The ``RRB:STATE`` command.

    Description:
        - This command returns or sets the state of the Results Readout bar (RRB). Visible if set to
          1. Hidden when set to 0.

    Usage:
        - Using the ``.query()`` method will send the ``RRB:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``RRB:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``RRB:STATE value`` command.

    SCPI Syntax:
        ```
        - RRB:STATE {ON|OFF|<NR1>}
        - RRB:STATE?
        ```

    Info:
        - ``OFF or <NR1> = 0`` sets the state of the right results readout bar to off.
        - ``ON or <NR1> ≠ 0`` sets the state of the right results readout bar to on.
    """


class Rrb(SCPICmdRead):
    """The ``RRB`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``RRB?`` query.
        - Using the ``.verify(value)`` method will send the ``RRB?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``RRB:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "RRB") -> None:
        super().__init__(device, cmd_syntax)
        self._state = RrbState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> RrbState:
        """Return the ``RRB:STATE`` command.

        Description:
            - This command returns or sets the state of the Results Readout bar (RRB). Visible if
              set to 1. Hidden when set to 0.

        Usage:
            - Using the ``.query()`` method will send the ``RRB:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``RRB:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``RRB:STATE value`` command.

        SCPI Syntax:
            ```
            - RRB:STATE {ON|OFF|<NR1>}
            - RRB:STATE?
            ```

        Info:
            - ``OFF or <NR1> = 0`` sets the state of the right results readout bar to off.
            - ``ON or <NR1> ≠ 0`` sets the state of the right results readout bar to on.
        """
        return self._state
