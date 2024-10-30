"""The display commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DISPlay:BRIGHtness {|MINimum|MAXimum}
    - DISPlay:BRIGHtness?[MINimum|MAXimum]
    - DISPlay:CONTrast {<contrast>|MINimum|MAXimum}
    - DISPlay:CONTrast?
    - DISPlay:SAVer:IMMediate
    - DISPlay:SAVer:STATe {ON|OFF|<NR1>}
    - DISPlay:SAVer:STATe?
    - DISPlay:WINDow:TEXT:CLEar
    - DISPlay:WINDow:TEXT:DATA <string>
    - DISPlay:WINDow:TEXT:DATA?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DisplayWindowTextData(SCPICmdWrite, SCPICmdRead):
    """The ``DISPlay:WINDow:TEXT:DATA`` command.

    Description:
        - The DISPlay[``:WINDow``]``:TEXT``[``:DATA``] command displays a text message on the
          instrument screen. The DISPlay[``:WINDow``]``:TEXT``[``:DATA``]? query returns the text
          string currently displayed on the instrument screen. The displayable characters are ASCII
          codes 32 through 126, and the instrument can display approximately 64 characters.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:WINDow:TEXT:DATA?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow:TEXT:DATA?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISPlay:WINDow:TEXT:DATA value``
          command.

    SCPI Syntax:
        ```
        - DISPlay:WINDow:TEXT:DATA <string>
        - DISPlay:WINDow:TEXT:DATA?
        ```
    """


class DisplayWindowTextClear(SCPICmdWriteNoArguments):
    """The ``DISPlay:WINDow:TEXT:CLEar`` command.

    Description:
        - This command clears the text message from the display screen.

    Usage:
        - Using the ``.write()`` method will send the ``DISPlay:WINDow:TEXT:CLEar`` command.

    SCPI Syntax:
        ```
        - DISPlay:WINDow:TEXT:CLEar
        ```
    """


class DisplayWindowText(SCPICmdRead):
    """The ``DISPlay:WINDow:TEXT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:WINDow:TEXT?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow:TEXT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clear``: The ``DISPlay:WINDow:TEXT:CLEar`` command.
        - ``.data``: The ``DISPlay:WINDow:TEXT:DATA`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clear = DisplayWindowTextClear(device, f"{self._cmd_syntax}:CLEar")
        self._data = DisplayWindowTextData(device, f"{self._cmd_syntax}:DATA")

    @property
    def clear(self) -> DisplayWindowTextClear:
        """Return the ``DISPlay:WINDow:TEXT:CLEar`` command.

        Description:
            - This command clears the text message from the display screen.

        Usage:
            - Using the ``.write()`` method will send the ``DISPlay:WINDow:TEXT:CLEar`` command.

        SCPI Syntax:
            ```
            - DISPlay:WINDow:TEXT:CLEar
            ```
        """
        return self._clear

    @property
    def data(self) -> DisplayWindowTextData:
        """Return the ``DISPlay:WINDow:TEXT:DATA`` command.

        Description:
            - The DISPlay[``:WINDow``]``:TEXT``[``:DATA``] command displays a text message on the
              instrument screen. The DISPlay[``:WINDow``]``:TEXT``[``:DATA``]? query returns the
              text string currently displayed on the instrument screen. The displayable characters
              are ASCII codes 32 through 126, and the instrument can display approximately 64
              characters.

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:WINDow:TEXT:DATA?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow:TEXT:DATA?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISPlay:WINDow:TEXT:DATA value``
              command.

        SCPI Syntax:
            ```
            - DISPlay:WINDow:TEXT:DATA <string>
            - DISPlay:WINDow:TEXT:DATA?
            ```
        """
        return self._data


class DisplayWindow(SCPICmdRead):
    """The ``DISPlay:WINDow`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:WINDow?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.text``: The ``DISPlay:WINDow:TEXT`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._text = DisplayWindowText(device, f"{self._cmd_syntax}:TEXT")

    @property
    def text(self) -> DisplayWindowText:
        """Return the ``DISPlay:WINDow:TEXT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:WINDow:TEXT?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow:TEXT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.clear``: The ``DISPlay:WINDow:TEXT:CLEar`` command.
            - ``.data``: The ``DISPlay:WINDow:TEXT:DATA`` command.
        """
        return self._text


class DisplaySaverState(SCPICmdWrite, SCPICmdRead):
    """The ``DISPlay:SAVer:STATe`` command.

    Description:
        - This command sets or queries the screen saver setting of the LCD display. When enabled,
          the screen saver function starts automatically if no operations are applied to the
          instrument front panel for five minutes.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:SAVer:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:SAVer:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISPlay:SAVer:STATe value`` command.

    SCPI Syntax:
        ```
        - DISPlay:SAVer:STATe {ON|OFF|<NR1>}
        - DISPlay:SAVer:STATe?
        ```
    """


class DisplaySaverImmediate(SCPICmdWriteNoArguments):
    """The ``DISPlay:SAVer:IMMediate`` command.

    Description:
        - This command sets the screen saver state to ON, regardless of the
          ``DISPlay:SAVer``[``:STATe``]? command setting. The screen saver is enabled immediately
          (without waiting for five minutes).

    Usage:
        - Using the ``.write()`` method will send the ``DISPlay:SAVer:IMMediate`` command.

    SCPI Syntax:
        ```
        - DISPlay:SAVer:IMMediate
        ```
    """


class DisplaySaver(SCPICmdRead):
    """The ``DISPlay:SAVer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:SAVer?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:SAVer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``DISPlay:SAVer:IMMediate`` command.
        - ``.state``: The ``DISPlay:SAVer:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = DisplaySaverImmediate(device, f"{self._cmd_syntax}:IMMediate")
        self._state = DisplaySaverState(device, f"{self._cmd_syntax}:STATe")

    @property
    def immediate(self) -> DisplaySaverImmediate:
        """Return the ``DISPlay:SAVer:IMMediate`` command.

        Description:
            - This command sets the screen saver state to ON, regardless of the
              ``DISPlay:SAVer``[``:STATe``]? command setting. The screen saver is enabled
              immediately (without waiting for five minutes).

        Usage:
            - Using the ``.write()`` method will send the ``DISPlay:SAVer:IMMediate`` command.

        SCPI Syntax:
            ```
            - DISPlay:SAVer:IMMediate
            ```
        """
        return self._immediate

    @property
    def state(self) -> DisplaySaverState:
        """Return the ``DISPlay:SAVer:STATe`` command.

        Description:
            - This command sets or queries the screen saver setting of the LCD display. When
              enabled, the screen saver function starts automatically if no operations are applied
              to the instrument front panel for five minutes.

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:SAVer:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:SAVer:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISPlay:SAVer:STATe value``
              command.

        SCPI Syntax:
            ```
            - DISPlay:SAVer:STATe {ON|OFF|<NR1>}
            - DISPlay:SAVer:STATe?
            ```
        """
        return self._state


class DisplayContrast(SCPICmdWrite, SCPICmdRead):
    """The ``DISPlay:CONTrast`` command.

    Description:
        - This command sets or queries the contrast of the LCD display.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay:CONTrast?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay:CONTrast?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISPlay:CONTrast value`` command.

    SCPI Syntax:
        ```
        - DISPlay:CONTrast {<contrast>|MINimum|MAXimum}
        - DISPlay:CONTrast?
        ```
    """


class DisplayBrightness(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``DISPlay:BRIGHtness`` command.

    Description:
        - This command sets or queries the brightness of the LCD display.

    Usage:
        - Using the ``.query(argument)`` method will send the ``DISPlay:BRIGHtness? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``DISPlay:BRIGHtness? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISPlay:BRIGHtness value`` command.

    SCPI Syntax:
        ```
        - DISPlay:BRIGHtness {|MINimum|MAXimum}
        - DISPlay:BRIGHtness?[MINimum|MAXimum]
        ```
    """


class Display(SCPICmdRead):
    """The ``DISPlay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISPlay?`` query.
        - Using the ``.verify(value)`` method will send the ``DISPlay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.brightness``: The ``DISPlay:BRIGHtness`` command.
        - ``.contrast``: The ``DISPlay:CONTrast`` command.
        - ``.saver``: The ``DISPlay:SAVer`` command tree.
        - ``.window``: The ``DISPlay:WINDow`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DISPlay") -> None:
        super().__init__(device, cmd_syntax)
        self._brightness = DisplayBrightness(device, f"{self._cmd_syntax}:BRIGHtness")
        self._contrast = DisplayContrast(device, f"{self._cmd_syntax}:CONTrast")
        self._saver = DisplaySaver(device, f"{self._cmd_syntax}:SAVer")
        self._window = DisplayWindow(device, f"{self._cmd_syntax}:WINDow")

    @property
    def brightness(self) -> DisplayBrightness:
        """Return the ``DISPlay:BRIGHtness`` command.

        Description:
            - This command sets or queries the brightness of the LCD display.

        Usage:
            - Using the ``.query(argument)`` method will send the ``DISPlay:BRIGHtness? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``DISPlay:BRIGHtness? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISPlay:BRIGHtness value`` command.

        SCPI Syntax:
            ```
            - DISPlay:BRIGHtness {|MINimum|MAXimum}
            - DISPlay:BRIGHtness?[MINimum|MAXimum]
            ```
        """
        return self._brightness

    @property
    def contrast(self) -> DisplayContrast:
        """Return the ``DISPlay:CONTrast`` command.

        Description:
            - This command sets or queries the contrast of the LCD display.

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:CONTrast?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:CONTrast?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISPlay:CONTrast value`` command.

        SCPI Syntax:
            ```
            - DISPlay:CONTrast {<contrast>|MINimum|MAXimum}
            - DISPlay:CONTrast?
            ```
        """
        return self._contrast

    @property
    def saver(self) -> DisplaySaver:
        """Return the ``DISPlay:SAVer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:SAVer?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:SAVer?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``DISPlay:SAVer:IMMediate`` command.
            - ``.state``: The ``DISPlay:SAVer:STATe`` command.
        """
        return self._saver

    @property
    def window(self) -> DisplayWindow:
        """Return the ``DISPlay:WINDow`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISPlay:WINDow?`` query.
            - Using the ``.verify(value)`` method will send the ``DISPlay:WINDow?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.text``: The ``DISPlay:WINDow:TEXT`` command tree.
        """
        return self._window
