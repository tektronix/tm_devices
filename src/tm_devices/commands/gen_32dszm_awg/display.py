"""The display commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DISPlay:WINDow1:STATe <display_state>
    - DISPlay:WINDow1:STATe?
    - DISPlay:WINDow2:STATe <display_state>
    - DISPlay:WINDow2:STATe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DisplayWindow2State(SCPICmdWrite, SCPICmdRead):
    """The ``DISPlay:WINDow2:STATe`` command.

    Description:
        - This command minimizes or restores the sequence or waveform window of the arbitrary
          waveform generator. This command only minimizes or restores the display area; it does not
          close the window. There is no maximizing. WINDow1 - Sequence window WINDow2 - Waveform
          window

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:WINDow2:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow2:STATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISPlay:WINDow2:STATe value`` command.

    SCPI Syntax:
        ```
        - DISPlay:WINDow2:STATe <display_state>
        - DISPlay:WINDow2:STATe?
        ```

    Info:
        - ``<display_state>`` ::=<Boolean>.
        - ``0`` indicates False, minimizes the window display.
        - ``1`` indicates True, restores the window display.
    """


class DisplayWindow2(SCPICmdRead):
    """The ``DISPlay:WINDow2`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:WINDow2?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow2?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DISPlay:WINDow2:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayWindow2State(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> DisplayWindow2State:
        """Return the ``DISPlay:WINDow2:STATe`` command.

        Description:
            - This command minimizes or restores the sequence or waveform window of the arbitrary
              waveform generator. This command only minimizes or restores the display area; it does
              not close the window. There is no maximizing. WINDow1 - Sequence window WINDow2 -
              Waveform window

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:WINDow2:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow2:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISPlay:WINDow2:STATe value``
              command.

        SCPI Syntax:
            ```
            - DISPlay:WINDow2:STATe <display_state>
            - DISPlay:WINDow2:STATe?
            ```

        Info:
            - ``<display_state>`` ::=<Boolean>.
            - ``0`` indicates False, minimizes the window display.
            - ``1`` indicates True, restores the window display.
        """
        return self._state


class DisplayWindow1State(SCPICmdWrite, SCPICmdRead):
    """The ``DISPlay:WINDow1:STATe`` command.

    Description:
        - This command minimizes or restores the sequence or waveform window of the arbitrary
          waveform generator. This command only minimizes or restores the display area; it does not
          close the window. There is no maximizing. WINDow1 - Sequence window WINDow2 - Waveform
          window

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:WINDow1:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow1:STATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISPlay:WINDow1:STATe value`` command.

    SCPI Syntax:
        ```
        - DISPlay:WINDow1:STATe <display_state>
        - DISPlay:WINDow1:STATe?
        ```

    Info:
        - ``<display_state>`` ::=<Boolean>.
        - ``0`` indicates False, minimizes the window display.
        - ``1`` indicates True, restores the window display.
    """


class DisplayWindow1(SCPICmdRead):
    """The ``DISPlay:WINDow1`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:WINDow1?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow1?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``DISPlay:WINDow1:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = DisplayWindow1State(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> DisplayWindow1State:
        """Return the ``DISPlay:WINDow1:STATe`` command.

        Description:
            - This command minimizes or restores the sequence or waveform window of the arbitrary
              waveform generator. This command only minimizes or restores the display area; it does
              not close the window. There is no maximizing. WINDow1 - Sequence window WINDow2 -
              Waveform window

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:WINDow1:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow1:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISPlay:WINDow1:STATe value``
              command.

        SCPI Syntax:
            ```
            - DISPlay:WINDow1:STATe <display_state>
            - DISPlay:WINDow1:STATe?
            ```

        Info:
            - ``<display_state>`` ::=<Boolean>.
            - ``0`` indicates False, minimizes the window display.
            - ``1`` indicates True, restores the window display.
        """
        return self._state


class Display(SCPICmdRead):
    """The ``DISPlay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.window1``: The ``DISPlay:WINDow1`` command tree.
        - ``.window2``: The ``DISPlay:WINDow2`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DISPlay") -> None:
        super().__init__(device, cmd_syntax)
        self._window1 = DisplayWindow1(device, f"{self._cmd_syntax}:WINDow1")
        self._window2 = DisplayWindow2(device, f"{self._cmd_syntax}:WINDow2")

    @property
    def window1(self) -> DisplayWindow1:
        """Return the ``DISPlay:WINDow1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:WINDow1?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow1?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DISPlay:WINDow1:STATe`` command.
        """
        return self._window1

    @property
    def window2(self) -> DisplayWindow2:
        """Return the ``DISPlay:WINDow2`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:WINDow2?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow2?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``DISPlay:WINDow2:STATe`` command.
        """
        return self._window2
