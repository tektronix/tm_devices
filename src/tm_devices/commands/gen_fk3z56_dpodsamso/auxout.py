"""The auxout commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUXout:EDGE {RISing|FALling}
    - AUXout:EDGE?
    - AUXout:SOUrce {ATRIGger|BTRIGger|DELayed|EVENT|REFOUT}
    - AUXout:SOUrce?
    - AUXout?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AuxoutSource(SCPICmdWrite, SCPICmdRead):
    """The ``AUXout:SOUrce`` command.

    Description:
        - This command sets or queries the trigger source at the BNC connection. This command is
          equivalent to selecting External Signals from the Utilities menu and then selecting the
          desired Configuration setting.

    Usage:
        - Using the ``.query()`` method will send the ``AUXout:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXout:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXout:SOUrce value`` command.

    SCPI Syntax:
        ```
        - AUXout:SOUrce {ATRIGger|BTRIGger|DELayed|EVENT|REFOUT}
        - AUXout:SOUrce?
        ```

    Info:
        - ``ATRIGger`` sets the source at the BNC connector to the main trigger.
        - ``BTRIGger`` sets the source at the BNC connector to the delayed trigger. (7K/70K).
        - ``EVENT`` sets the source at the BNC connector to a specified event. (7K/70K).
        - ``DELayed`` sets the source at the BNC connector to the delayed trigger.
        - ``REFOUT`` sets the source at the BNC connector to the reference output. (5K/7K).
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
    """The ``AUXout`` command.

    Description:
        - This query-only command returns the auxiliary output setup and is equivalent to selecting
          External Signals. From the Utilities menu, and then viewing the current settings for the
          AUX OUT Configuration.

    Usage:
        - Using the ``.query()`` method will send the ``AUXout?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXout?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AUXout?
        ```

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
            - This command sets or queries the trigger source at the BNC connection. This command is
              equivalent to selecting External Signals from the Utilities menu and then selecting
              the desired Configuration setting.

        Usage:
            - Using the ``.query()`` method will send the ``AUXout:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXout:SOUrce?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXout:SOUrce value`` command.

        SCPI Syntax:
            ```
            - AUXout:SOUrce {ATRIGger|BTRIGger|DELayed|EVENT|REFOUT}
            - AUXout:SOUrce?
            ```

        Info:
            - ``ATRIGger`` sets the source at the BNC connector to the main trigger.
            - ``BTRIGger`` sets the source at the BNC connector to the delayed trigger. (7K/70K).
            - ``EVENT`` sets the source at the BNC connector to a specified event. (7K/70K).
            - ``DELayed`` sets the source at the BNC connector to the delayed trigger.
            - ``REFOUT`` sets the source at the BNC connector to the reference output. (5K/7K).
        """
        return self._source
