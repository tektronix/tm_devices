"""The auxout commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUXout:EDGE {RISing|FALling}
    - AUXout:EDGE?
    - AUXout:SOUrce {ATRIGger|REFOUT|AFG}
    - AUXout:SOUrce?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AuxoutSource(SCPICmdWrite, SCPICmdRead):
    """The ``AUXout:SOUrce`` command.

    Description:
        - This command sets or queries the source at the Auxiliary Output BNC connection.

    Usage:
        - Using the ``.query()`` method will send the ``AUXout:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXout:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXout:SOUrce value`` command.

    SCPI Syntax:
        ```
        - AUXout:SOUrce {ATRIGger|REFOUT|AFG}
        - AUXout:SOUrce?
        ```

    Info:
        - ``ATRIGger`` sets the source at the BNC connector to the main trigger.
        - ``REFOUT`` sets the source at the BNC connector to the reference output.
        - ``AFG`` sets the source at the BNC connector to the AFG output.
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
        - ``.source``: The ``AUXout:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUXout") -> None:
        super().__init__(device, cmd_syntax)
        self._edge = AuxoutEdge(device, f"{self._cmd_syntax}:EDGE")
        self._source = AuxoutSource(device, f"{self._cmd_syntax}:SOUrce")

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
    def source(self) -> AuxoutSource:
        """Return the ``AUXout:SOUrce`` command.

        Description:
            - This command sets or queries the source at the Auxiliary Output BNC connection.

        Usage:
            - Using the ``.query()`` method will send the ``AUXout:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXout:SOUrce?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXout:SOUrce value`` command.

        SCPI Syntax:
            ```
            - AUXout:SOUrce {ATRIGger|REFOUT|AFG}
            - AUXout:SOUrce?
            ```

        Info:
            - ``ATRIGger`` sets the source at the BNC connector to the main trigger.
            - ``REFOUT`` sets the source at the BNC connector to the reference output.
            - ``AFG`` sets the source at the BNC connector to the AFG output.
        """
        return self._source
