"""The teklink commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TEKLink:CONNection?
    - TEKLink:REFClk {ON|OFF|PENDING}
    - TEKLink:REFClk?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class TeklinkRefclk(SCPICmdWrite, SCPICmdRead):
    """The ``TEKLink:REFClk`` command.

    Description:
        - This command sets or queries the current state of the intrument's TekLink Reference
          Output.

    Usage:
        - Using the ``.query()`` method will send the ``TEKLink:REFClk?`` query.
        - Using the ``.verify(value)`` method will send the ``TEKLink:REFClk?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TEKLink:REFClk value`` command.

    SCPI Syntax:
        ```
        - TEKLink:REFClk {ON|OFF|PENDING}
        - TEKLink:REFClk?
        ```

    Info:
        - ``ON`` specifies the on state of the TekLink Reference Output.
        - ``OFF`` specifies the off state of the TekLink Reference Output.
        - ``PENDING`` specifies the pending state of the TekLink Reference Output.
    """


class TeklinkConnection(SCPICmdRead):
    """The ``TEKLink:CONNection`` command.

    Description:
        - This command returns the current TekLink network connection.

    Usage:
        - Using the ``.query()`` method will send the ``TEKLink:CONNection?`` query.
        - Using the ``.verify(value)`` method will send the ``TEKLink:CONNection?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - TEKLink:CONNection?
        ```
    """


class Teklink(SCPICmdRead):
    """The ``TEKLink`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TEKLink?`` query.
        - Using the ``.verify(value)`` method will send the ``TEKLink?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.connection``: The ``TEKLink:CONNection`` command.
        - ``.refclk``: The ``TEKLink:REFClk`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "TEKLink") -> None:
        super().__init__(device, cmd_syntax)
        self._connection = TeklinkConnection(device, f"{self._cmd_syntax}:CONNection")
        self._refclk = TeklinkRefclk(device, f"{self._cmd_syntax}:REFClk")

    @property
    def connection(self) -> TeklinkConnection:
        """Return the ``TEKLink:CONNection`` command.

        Description:
            - This command returns the current TekLink network connection.

        Usage:
            - Using the ``.query()`` method will send the ``TEKLink:CONNection?`` query.
            - Using the ``.verify(value)`` method will send the ``TEKLink:CONNection?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - TEKLink:CONNection?
            ```
        """
        return self._connection

    @property
    def refclk(self) -> TeklinkRefclk:
        """Return the ``TEKLink:REFClk`` command.

        Description:
            - This command sets or queries the current state of the intrument's TekLink Reference
              Output.

        Usage:
            - Using the ``.query()`` method will send the ``TEKLink:REFClk?`` query.
            - Using the ``.verify(value)`` method will send the ``TEKLink:REFClk?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TEKLink:REFClk value`` command.

        SCPI Syntax:
            ```
            - TEKLink:REFClk {ON|OFF|PENDING}
            - TEKLink:REFClk?
            ```

        Info:
            - ``ON`` specifies the on state of the TekLink Reference Output.
            - ``OFF`` specifies the off state of the TekLink Reference Output.
            - ``PENDING`` specifies the pending state of the TekLink Reference Output.
        """
        return self._refclk
