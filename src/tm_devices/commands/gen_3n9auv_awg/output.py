"""The output commands module.

These commands are used in the following models:
AWG5200, AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - OUTPut:OFF {0|1|OFF|ON}
    - OUTPut:OFF?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class OutputOff(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut:OFF`` command.

    Description:
        - This command sets or returns the state (enabled or disabled) of the 'All Outputs Off'
          control. Enabling All Output Off causes each channel's output and markers to go to an
          ungrounded (or open) state. Disabling the control causes each channel to go to its
          currently defined state. A channel's defined state can be changed while the All Outputs
          Off is in effect, but the actual output remains open until the All Outputs Off is
          disabled.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut:OFF?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut:OFF?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut:OFF value`` command.

    SCPI Syntax:
        ```
        - OUTPut:OFF {0|1|OFF|ON}
        - OUTPut:OFF?
        ```

    Info:
        - ``0`` or OFF disables the All Output Off function, allowing the channel and marker outputs
          to go to their defined state.1 or ON enables the All Output Off function, disabling all
          channel outputs and marker outputs.
        - ``*RST`` sets all channels to 0.
    """


class Output(SCPICmdRead):
    """The ``OUTPut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.off``: The ``OUTPut:OFF`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "OUTPut") -> None:
        super().__init__(device, cmd_syntax)
        self._off = OutputOff(device, f"{self._cmd_syntax}:OFF")

    @property
    def off(self) -> OutputOff:
        """Return the ``OUTPut:OFF`` command.

        Description:
            - This command sets or returns the state (enabled or disabled) of the 'All Outputs Off'
              control. Enabling All Output Off causes each channel's output and markers to go to an
              ungrounded (or open) state. Disabling the control causes each channel to go to its
              currently defined state. A channel's defined state can be changed while the All
              Outputs Off is in effect, but the actual output remains open until the All Outputs Off
              is disabled.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut:OFF?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut:OFF?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut:OFF value`` command.

        SCPI Syntax:
            ```
            - OUTPut:OFF {0|1|OFF|ON}
            - OUTPut:OFF?
            ```

        Info:
            - ``0`` or OFF disables the All Output Off function, allowing the channel and marker
              outputs to go to their defined state.1 or ON enables the All Output Off function,
              disabling all channel outputs and marker outputs.
            - ``*RST`` sets all channels to 0.
        """
        return self._off
