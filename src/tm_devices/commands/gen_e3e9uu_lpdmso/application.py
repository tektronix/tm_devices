"""The application commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - APPLication:ACTivate <QString>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ApplicationActivate(SCPICmdWrite):
    """The ``APPLication:ACTivate`` command.

    Description:
        - For legacy TekExpress applications. Starts the application specified in the string. The
          available applications depend on the oscilloscope model and installed options.

    Usage:
        - Using the ``.write(value)`` method will send the ``APPLication:ACTivate value`` command.

    SCPI Syntax:
        ```
        - APPLication:ACTivate <QString>
        ```

    Info:
        - ``<QString>`` is the name of the application that you want to start. Enter the application
          name exactly as it appears in the oscilloscope Applications menu.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Application(SCPICmdRead):
    """The ``APPLication`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``APPLication?`` query.
        - Using the ``.verify(value)`` method will send the ``APPLication?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.activate``: The ``APPLication:ACTivate`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "APPLication"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._activate = ApplicationActivate(device, f"{self._cmd_syntax}:ACTivate")

    @property
    def activate(self) -> ApplicationActivate:
        """Return the ``APPLication:ACTivate`` command.

        Description:
            - For legacy TekExpress applications. Starts the application specified in the string.
              The available applications depend on the oscilloscope model and installed options.

        Usage:
            - Using the ``.write(value)`` method will send the ``APPLication:ACTivate value``
              command.

        SCPI Syntax:
            ```
            - APPLication:ACTivate <QString>
            ```

        Info:
            - ``<QString>`` is the name of the application that you want to start. Enter the
              application name exactly as it appears in the oscilloscope Applications menu.
        """
        return self._activate
