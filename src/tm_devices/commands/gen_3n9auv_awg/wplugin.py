"""The wplugin commands module.

These commands are used in the following models:
AWG5200, AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - WPLugin:ACTive <plugin_name>
    - WPLugin:ACTive?
    - WPLugin:PLUGins?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class WpluginPlugins(SCPICmdRead):
    """The ``WPLugin:PLUGins`` command.

    Description:
        - This command returns all the available waveform creation plug-ins installed. The response
          returns a comma separated string with all the plug-in names.

    Usage:
        - Using the ``.query()`` method will send the ``WPLugin:PLUGins?`` query.
        - Using the ``.verify(value)`` method will send the ``WPLugin:PLUGins?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WPLugin:PLUGins?
        ```
    """


class WpluginActive(SCPICmdWrite, SCPICmdRead):
    """The ``WPLugin:ACTive`` command.

    Description:
        - This command sets or returns the active waveform creation plug-in.

    Usage:
        - Using the ``.query()`` method will send the ``WPLugin:ACTive?`` query.
        - Using the ``.verify(value)`` method will send the ``WPLugin:ACTive?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WPLugin:ACTive value`` command.

    SCPI Syntax:
        ```
        - WPLugin:ACTive <plugin_name>
        - WPLugin:ACTive?
        ```
    """


class Wplugin(SCPICmdRead):
    """The ``WPLugin`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WPLugin?`` query.
        - Using the ``.verify(value)`` method will send the ``WPLugin?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.active``: The ``WPLugin:ACTive`` command.
        - ``.plugins``: The ``WPLugin:PLUGins`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "WPLugin") -> None:
        super().__init__(device, cmd_syntax)
        self._active = WpluginActive(device, f"{self._cmd_syntax}:ACTive")
        self._plugins = WpluginPlugins(device, f"{self._cmd_syntax}:PLUGins")

    @property
    def active(self) -> WpluginActive:
        """Return the ``WPLugin:ACTive`` command.

        Description:
            - This command sets or returns the active waveform creation plug-in.

        Usage:
            - Using the ``.query()`` method will send the ``WPLugin:ACTive?`` query.
            - Using the ``.verify(value)`` method will send the ``WPLugin:ACTive?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WPLugin:ACTive value`` command.

        SCPI Syntax:
            ```
            - WPLugin:ACTive <plugin_name>
            - WPLugin:ACTive?
            ```
        """
        return self._active

    @property
    def plugins(self) -> WpluginPlugins:
        """Return the ``WPLugin:PLUGins`` command.

        Description:
            - This command returns all the available waveform creation plug-ins installed. The
              response returns a comma separated string with all the plug-in names.

        Usage:
            - Using the ``.query()`` method will send the ``WPLugin:PLUGins?`` query.
            - Using the ``.verify(value)`` method will send the ``WPLugin:PLUGins?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WPLugin:PLUGins?
            ```
        """
        return self._plugins
