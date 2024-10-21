"""The lock commands module.

These commands are used in the following models:
MDO3

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - LOCk:ALL
    - LOCk:FPanel {LOCKed|UNLOCKed}
    - LOCk:FPanel?
    - LOCk:MOUse {LOCKed|UNLOCKed}
    - LOCk:MOUse?
    - LOCk:NONe
    - LOCk:TOUCHscreen {LOCKed|UNLOCKed}
    - LOCk:TOUCHscreen?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class LockTouchscreen(SCPICmdWrite, SCPICmdRead):
    """The ``LOCk:TOUCHscreen`` command.

    Description:
        - This command enables or disables the touchscreen.

    Usage:
        - Using the ``.query()`` method will send the ``LOCk:TOUCHscreen?`` query.
        - Using the ``.verify(value)`` method will send the ``LOCk:TOUCHscreen?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LOCk:TOUCHscreen value`` command.

    SCPI Syntax:
        ```
        - LOCk:TOUCHscreen {LOCKed|UNLOCKed}
        - LOCk:TOUCHscreen?
        ```

    Info:
        - ``LOCKed`` disables the touchscreen.
        - ``UNLOCKed`` enables the touchscreen.
    """


class LockNone(SCPICmdWriteNoArguments):
    """The ``LOCk:NONe`` command.

    Description:
        - This command enables the front panel, mouse, and touchscreen.

    Usage:
        - Using the ``.write()`` method will send the ``LOCk:NONe`` command.

    SCPI Syntax:
        ```
        - LOCk:NONe
        ```
    """


class LockMouse(SCPICmdWrite, SCPICmdRead):
    """The ``LOCk:MOUse`` command.

    Description:
        - This command enables or disables the mouse.

    Usage:
        - Using the ``.query()`` method will send the ``LOCk:MOUse?`` query.
        - Using the ``.verify(value)`` method will send the ``LOCk:MOUse?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LOCk:MOUse value`` command.

    SCPI Syntax:
        ```
        - LOCk:MOUse {LOCKed|UNLOCKed}
        - LOCk:MOUse?
        ```

    Info:
        - ``LOCKed`` disables the mouse.
        - ``UNLOCKed`` enables the mouse.
    """


class LockFpanel(SCPICmdWrite, SCPICmdRead):
    """The ``LOCk:FPanel`` command.

    Description:
        - This command enables or disables the front panel buttons and knobs.

    Usage:
        - Using the ``.query()`` method will send the ``LOCk:FPanel?`` query.
        - Using the ``.verify(value)`` method will send the ``LOCk:FPanel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``LOCk:FPanel value`` command.

    SCPI Syntax:
        ```
        - LOCk:FPanel {LOCKed|UNLOCKed}
        - LOCk:FPanel?
        ```

    Info:
        - ``LOCKed`` disables the front panel.
        - ``UNLOCKed`` enables the front panel.
    """


class LockAll(SCPICmdWriteNoArguments):
    """The ``LOCk:ALL`` command.

    Description:
        - This command disables the front panel, mouse, and touchscreen.

    Usage:
        - Using the ``.write()`` method will send the ``LOCk:ALL`` command.

    SCPI Syntax:
        ```
        - LOCk:ALL
        ```
    """


class Lock(SCPICmdRead):
    """The ``LOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``LOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``LOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.all``: The ``LOCk:ALL`` command.
        - ``.fpanel``: The ``LOCk:FPanel`` command.
        - ``.mouse``: The ``LOCk:MOUse`` command.
        - ``.none``: The ``LOCk:NONe`` command.
        - ``.touchscreen``: The ``LOCk:TOUCHscreen`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "LOCk") -> None:
        super().__init__(device, cmd_syntax)
        self._all = LockAll(device, f"{self._cmd_syntax}:ALL")
        self._fpanel = LockFpanel(device, f"{self._cmd_syntax}:FPanel")
        self._mouse = LockMouse(device, f"{self._cmd_syntax}:MOUse")
        self._none = LockNone(device, f"{self._cmd_syntax}:NONe")
        self._touchscreen = LockTouchscreen(device, f"{self._cmd_syntax}:TOUCHscreen")

    @property
    def all(self) -> LockAll:
        """Return the ``LOCk:ALL`` command.

        Description:
            - This command disables the front panel, mouse, and touchscreen.

        Usage:
            - Using the ``.write()`` method will send the ``LOCk:ALL`` command.

        SCPI Syntax:
            ```
            - LOCk:ALL
            ```
        """
        return self._all

    @property
    def fpanel(self) -> LockFpanel:
        """Return the ``LOCk:FPanel`` command.

        Description:
            - This command enables or disables the front panel buttons and knobs.

        Usage:
            - Using the ``.query()`` method will send the ``LOCk:FPanel?`` query.
            - Using the ``.verify(value)`` method will send the ``LOCk:FPanel?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LOCk:FPanel value`` command.

        SCPI Syntax:
            ```
            - LOCk:FPanel {LOCKed|UNLOCKed}
            - LOCk:FPanel?
            ```

        Info:
            - ``LOCKed`` disables the front panel.
            - ``UNLOCKed`` enables the front panel.
        """
        return self._fpanel

    @property
    def mouse(self) -> LockMouse:
        """Return the ``LOCk:MOUse`` command.

        Description:
            - This command enables or disables the mouse.

        Usage:
            - Using the ``.query()`` method will send the ``LOCk:MOUse?`` query.
            - Using the ``.verify(value)`` method will send the ``LOCk:MOUse?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LOCk:MOUse value`` command.

        SCPI Syntax:
            ```
            - LOCk:MOUse {LOCKed|UNLOCKed}
            - LOCk:MOUse?
            ```

        Info:
            - ``LOCKed`` disables the mouse.
            - ``UNLOCKed`` enables the mouse.
        """
        return self._mouse

    @property
    def none(self) -> LockNone:
        """Return the ``LOCk:NONe`` command.

        Description:
            - This command enables the front panel, mouse, and touchscreen.

        Usage:
            - Using the ``.write()`` method will send the ``LOCk:NONe`` command.

        SCPI Syntax:
            ```
            - LOCk:NONe
            ```
        """
        return self._none

    @property
    def touchscreen(self) -> LockTouchscreen:
        """Return the ``LOCk:TOUCHscreen`` command.

        Description:
            - This command enables or disables the touchscreen.

        Usage:
            - Using the ``.query()`` method will send the ``LOCk:TOUCHscreen?`` query.
            - Using the ``.verify(value)`` method will send the ``LOCk:TOUCHscreen?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``LOCk:TOUCHscreen value`` command.

        SCPI Syntax:
            ```
            - LOCk:TOUCHscreen {LOCKed|UNLOCKed}
            - LOCk:TOUCHscreen?
            ```

        Info:
            - ``LOCKed`` disables the touchscreen.
            - ``UNLOCKed`` enables the touchscreen.
        """
        return self._touchscreen
