"""The mainwindow commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MAINWindow:BADGe:BRINgtoview <Qstring>
    - MAINWindow:FONTSize <NR1>
    - MAINWindow:RRBDisplaystate {1|ON|0|OFF}
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MainwindowRrbdisplaystate(SCPICmdWrite):
    """The ``MAINWindow:RRBDisplaystate`` command.

    Description:
        - Sets the display state of the Results readout bar to ON (displayed) or OFF (not
          displayed).

    Usage:
        - Using the ``.write(value)`` method will send the ``MAINWindow:RRBDisplaystate value``
          command.

    SCPI Syntax:
        ```
        - MAINWindow:RRBDisplaystate {1|ON|0|OFF}
        ```

    Info:
        - ``1`` or ON enables Autoset to change vertical settings.
        - ``0`` or OFF disables Autoset from changing vertical settings.
    """


class MainwindowFontsize(SCPICmdWrite):
    """The ``MAINWindow:FONTSize`` command.

    Description:
        - Sets the font size for UI text elements. Font size range is 12 to 20 points.

    Usage:
        - Using the ``.write(value)`` method will send the ``MAINWindow:FONTSize value`` command.

    SCPI Syntax:
        ```
        - MAINWindow:FONTSize <NR1>
        ```

    Info:
        - ``<NR1>`` specifies the font size.
    """


class MainwindowBadgeBringtoview(SCPICmdWrite):
    """The ``MAINWindow:BADGe:BRINgtoview`` command.

    Description:
        - This command is used to automatically scroll the specified badge to make it visible. The
          input to the command is the badge title name.

    Usage:
        - Using the ``.write(value)`` method will send the ``MAINWindow:BADGe:BRINgtoview value``
          command.

    SCPI Syntax:
        ```
        - MAINWindow:BADGe:BRINgtoview <Qstring>
        ```

    Info:
        - ``<Qstring>`` specifies a badge title name to make the badge visible.
    """


class MainwindowBadge(SCPICmdRead):
    """The ``MAINWindow:BADGe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MAINWindow:BADGe?`` query.
        - Using the ``.verify(value)`` method will send the ``MAINWindow:BADGe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bringtoview``: The ``MAINWindow:BADGe:BRINgtoview`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bringtoview = MainwindowBadgeBringtoview(device, f"{self._cmd_syntax}:BRINgtoview")

    @property
    def bringtoview(self) -> MainwindowBadgeBringtoview:
        """Return the ``MAINWindow:BADGe:BRINgtoview`` command.

        Description:
            - This command is used to automatically scroll the specified badge to make it visible.
              The input to the command is the badge title name.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``MAINWindow:BADGe:BRINgtoview value`` command.

        SCPI Syntax:
            ```
            - MAINWindow:BADGe:BRINgtoview <Qstring>
            ```

        Info:
            - ``<Qstring>`` specifies a badge title name to make the badge visible.
        """
        return self._bringtoview


class Mainwindow(SCPICmdRead):
    """The ``MAINWindow`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MAINWindow?`` query.
        - Using the ``.verify(value)`` method will send the ``MAINWindow?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.badge``: The ``MAINWindow:BADGe`` command tree.
        - ``.fontsize``: The ``MAINWindow:FONTSize`` command.
        - ``.rrbdisplaystate``: The ``MAINWindow:RRBDisplaystate`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "MAINWindow"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._badge = MainwindowBadge(device, f"{self._cmd_syntax}:BADGe")
        self._fontsize = MainwindowFontsize(device, f"{self._cmd_syntax}:FONTSize")
        self._rrbdisplaystate = MainwindowRrbdisplaystate(
            device, f"{self._cmd_syntax}:RRBDisplaystate"
        )

    @property
    def badge(self) -> MainwindowBadge:
        """Return the ``MAINWindow:BADGe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MAINWindow:BADGe?`` query.
            - Using the ``.verify(value)`` method will send the ``MAINWindow:BADGe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bringtoview``: The ``MAINWindow:BADGe:BRINgtoview`` command.
        """
        return self._badge

    @property
    def fontsize(self) -> MainwindowFontsize:
        """Return the ``MAINWindow:FONTSize`` command.

        Description:
            - Sets the font size for UI text elements. Font size range is 12 to 20 points.

        Usage:
            - Using the ``.write(value)`` method will send the ``MAINWindow:FONTSize value``
              command.

        SCPI Syntax:
            ```
            - MAINWindow:FONTSize <NR1>
            ```

        Info:
            - ``<NR1>`` specifies the font size.
        """
        return self._fontsize

    @property
    def rrbdisplaystate(self) -> MainwindowRrbdisplaystate:
        """Return the ``MAINWindow:RRBDisplaystate`` command.

        Description:
            - Sets the display state of the Results readout bar to ON (displayed) or OFF (not
              displayed).

        Usage:
            - Using the ``.write(value)`` method will send the ``MAINWindow:RRBDisplaystate value``
              command.

        SCPI Syntax:
            ```
            - MAINWindow:RRBDisplaystate {1|ON|0|OFF}
            ```

        Info:
            - ``1`` or ON enables Autoset to change vertical settings.
            - ``0`` or OFF disables Autoset from changing vertical settings.
        """
        return self._rrbdisplaystate
