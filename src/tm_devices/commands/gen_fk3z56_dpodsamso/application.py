"""The application commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - APPLication:ACTivate <string>
    - APPLication:SCOPEAPP:WINDOW {FULLSCREEN|MINIMIZED}
    - APPLication:SCOPEAPP:WINDOW?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ApplicationScopeappWindow(SCPICmdWrite, SCPICmdRead):
    """The ``APPLication:SCOPEAPP:WINDOW`` command.

    Description:
        - Sets or queries whether the oscilloscope application is minimized or displayed full
          screen.

    Usage:
        - Using the ``.query()`` method will send the ``APPLication:SCOPEAPP:WINDOW?`` query.
        - Using the ``.verify(value)`` method will send the ``APPLication:SCOPEAPP:WINDOW?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``APPLication:SCOPEAPP:WINDOW value``
          command.

    SCPI Syntax:
        ```
        - APPLication:SCOPEAPP:WINDOW {FULLSCREEN|MINIMIZED}
        - APPLication:SCOPEAPP:WINDOW?
        ```

    Info:
        - ``FULLSCREEN`` sets the oscilloscope display to fill the oscilloscope screen.
        - ``MINIMIZED`` minimizes the oscilloscope display to an icon at the bottom of the screen.
    """


class ApplicationScopeapp(SCPICmdRead):
    """The ``APPLication:SCOPEAPP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``APPLication:SCOPEAPP?`` query.
        - Using the ``.verify(value)`` method will send the ``APPLication:SCOPEAPP?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.window``: The ``APPLication:SCOPEAPP:WINDOW`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._window = ApplicationScopeappWindow(device, f"{self._cmd_syntax}:WINDOW")

    @property
    def window(self) -> ApplicationScopeappWindow:
        """Return the ``APPLication:SCOPEAPP:WINDOW`` command.

        Description:
            - Sets or queries whether the oscilloscope application is minimized or displayed full
              screen.

        Usage:
            - Using the ``.query()`` method will send the ``APPLication:SCOPEAPP:WINDOW?`` query.
            - Using the ``.verify(value)`` method will send the ``APPLication:SCOPEAPP:WINDOW?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``APPLication:SCOPEAPP:WINDOW value``
              command.

        SCPI Syntax:
            ```
            - APPLication:SCOPEAPP:WINDOW {FULLSCREEN|MINIMIZED}
            - APPLication:SCOPEAPP:WINDOW?
            ```

        Info:
            - ``FULLSCREEN`` sets the oscilloscope display to fill the oscilloscope screen.
            - ``MINIMIZED`` minimizes the oscilloscope display to an icon at the bottom of the
              screen.
        """
        return self._window


class ApplicationActivate(SCPICmdWrite):
    """The ``APPLication:ACTivate`` command.

    Description:
        - For legacy Java based applications, starts the application specified in the string. The
          available applications depend on the oscilloscope model and installed options. (DPOJET and
          DPOJET-based applications do not require this command and are started automatically by
          sending them any command, such as DPOJET: VERsion? )

    Usage:
        - Using the ``.write(value)`` method will send the ``APPLication:ACTivate value`` command.

    SCPI Syntax:
        ```
        - APPLication:ACTivate <string>
        ```

    Info:
        - ``<string>`` is the name of the application that you want to start. Enter the application
          name exactly as it appears in the oscilloscope Analyze menu.
    """


class Application(SCPICmdRead):
    """The ``APPLication`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``APPLication?`` query.
        - Using the ``.verify(value)`` method will send the ``APPLication?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.activate``: The ``APPLication:ACTivate`` command.
        - ``.scopeapp``: The ``APPLication:SCOPEAPP`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "APPLication"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._activate = ApplicationActivate(device, f"{self._cmd_syntax}:ACTivate")
        self._scopeapp = ApplicationScopeapp(device, f"{self._cmd_syntax}:SCOPEAPP")

    @property
    def activate(self) -> ApplicationActivate:
        """Return the ``APPLication:ACTivate`` command.

        Description:
            - For legacy Java based applications, starts the application specified in the string.
              The available applications depend on the oscilloscope model and installed options.
              (DPOJET and DPOJET-based applications do not require this command and are started
              automatically by sending them any command, such as DPOJET: VERsion? )

        Usage:
            - Using the ``.write(value)`` method will send the ``APPLication:ACTivate value``
              command.

        SCPI Syntax:
            ```
            - APPLication:ACTivate <string>
            ```

        Info:
            - ``<string>`` is the name of the application that you want to start. Enter the
              application name exactly as it appears in the oscilloscope Analyze menu.
        """
        return self._activate

    @property
    def scopeapp(self) -> ApplicationScopeapp:
        """Return the ``APPLication:SCOPEAPP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``APPLication:SCOPEAPP?`` query.
            - Using the ``.verify(value)`` method will send the ``APPLication:SCOPEAPP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.window``: The ``APPLication:SCOPEAPP:WINDOW`` command.
        """
        return self._scopeapp
