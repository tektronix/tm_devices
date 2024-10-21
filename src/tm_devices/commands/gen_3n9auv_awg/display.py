"""The display commands module.

These commands are used in the following models:
AWG5200, AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DISPlay:PLOT:STATe {0|1|OFF|ON}
    - DISPlay:PLOT:STATe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DisplayPlotState(SCPICmdWrite, SCPICmdRead):
    """The ``DISPlay:PLOT:STATe`` command.

    Description:
        - This command minimizes or restores the plot's display area on the Home screen's channel
          window of the AWG. This command only minimizes or restores the display area; it does not
          close the window. Plots in the Function generator window are not affected.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:PLOT:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:PLOT:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISPlay:PLOT:STATe value`` command.

    SCPI Syntax:
        ```
        - DISPlay:PLOT:STATe {0|1|OFF|ON}
        - DISPlay:PLOT:STATe?
        ```

    Info:
        - ``*RST`` sets this to 1.
    """


class DisplayPlot(SCPICmdRead):
    """The ``DISPlay:PLOT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:PLOT?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:PLOT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DISPlay:PLOT:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayPlotState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> DisplayPlotState:
        """Return the ``DISPlay:PLOT:STATe`` command.

        Description:
            - This command minimizes or restores the plot's display area on the Home screen's
              channel window of the AWG. This command only minimizes or restores the display area;
              it does not close the window. Plots in the Function generator window are not affected.

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:PLOT:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:PLOT:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISPlay:PLOT:STATe value`` command.

        SCPI Syntax:
            ```
            - DISPlay:PLOT:STATe {0|1|OFF|ON}
            - DISPlay:PLOT:STATe?
            ```

        Info:
            - ``*RST`` sets this to 1.
        """
        return self._state


class Display(SCPICmdRead):
    """The ``DISPlay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.plot``: The ``DISPlay:PLOT`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DISPlay") -> None:
        super().__init__(device, cmd_syntax)
        self._plot = DisplayPlot(device, f"{self._cmd_syntax}:PLOT")

    @property
    def plot(self) -> DisplayPlot:
        """Return the ``DISPlay:PLOT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:PLOT?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:PLOT?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DISPlay:PLOT:STATe`` command.
        """
        return self._plot
