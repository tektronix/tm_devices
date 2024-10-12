"""The active commands module.

These commands are used in the following models:
AWG5200, AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ACTive:MODE {NORMal|CALibration|DIAGnostic}
    - ACTive:MODE?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ActiveMode(SCPICmdWrite, SCPICmdRead):
    """The ``ACTive:MODE`` command.

    Description:
        - This command enables and disables access to diagnostics or calibration. When the active
          mode is DIAGnostic or CALibration, all other non-diagnostic and non-calibration commands
          are ignored and no action occurs. If a test or procedure is in progress, errors are not
          returned; they are added to the system error queue, which can be accessed with
          ``SYSTEM:ERROR:NEXT``. For example: -200, '[D|C] are still running;' -300,'Device-specific
          error; Diagnostics tests still in progress - ``act:mode`` diag' -300,'Device-specific
          error; Calibration procedures still in progress - ``act:mode`` cal' To avoid this error,
          use the command ``DIAGNOSTIC:STOP:STATE`` or ``CALIBRATION:STOP:STATE`` to test for this
          condition. This command blocks when changing any state. Changing the state to NORMal
          causes a hardware initialization process and any related system settings are restored. If
          any diagnostic tests are in progress, then the request to change the active mode fails and
          the mode will not change. When changing the active mode, it's recommended to follow the
          action with an operation complete command (``*OPC``) to ensure the command has finished
          before other commands are processed.

    Usage:
        - Using the ``.query()`` method will send the ``ACTive:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTive:MODE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTive:MODE value`` command.

    SCPI Syntax:
        ```
        - ACTive:MODE {NORMal|CALibration|DIAGnostic}
        - ACTive:MODE?
        ```

    Info:
        - ``NORMal`` disables any active state for either calibration or diagnostics. When entering
          the active state of normal, the hardware is set to a default state and the previous system
          state is restored and waveform playout is set to off.
        - ``CALibration`` enables the active state for the calibration. Entering the active state of
          calibration turns waveform playout off.
        - ``DIAGnostic`` enables the active state for the diagnostics. Entering the active state of
          diagnostics turns waveform playout off.
        - ``*RST`` sets this to NORM.
    """


class Active(SCPICmdRead):
    """The ``ACTive`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTive?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTive?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``ACTive:MODE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ACTive") -> None:
        super().__init__(device, cmd_syntax)
        self._mode = ActiveMode(device, f"{self._cmd_syntax}:MODE")

    @property
    def mode(self) -> ActiveMode:
        """Return the ``ACTive:MODE`` command.

        Description:
            - This command enables and disables access to diagnostics or calibration. When the
              active mode is DIAGnostic or CALibration, all other non-diagnostic and non-calibration
              commands are ignored and no action occurs. If a test or procedure is in progress,
              errors are not returned; they are added to the system error queue, which can be
              accessed with ``SYSTEM:ERROR:NEXT``. For example: -200, '[D|C] are still running;'
              -300,'Device-specific error; Diagnostics tests still in progress - ``act:mode`` diag'
              -300,'Device-specific error; Calibration procedures still in progress - ``act:mode``
              cal' To avoid this error, use the command ``DIAGNOSTIC:STOP:STATE`` or
              ``CALIBRATION:STOP:STATE`` to test for this condition. This command blocks when
              changing any state. Changing the state to NORMal causes a hardware initialization
              process and any related system settings are restored. If any diagnostic tests are in
              progress, then the request to change the active mode fails and the mode will not
              change. When changing the active mode, it's recommended to follow the action with an
              operation complete command (``*OPC``) to ensure the command has finished before other
              commands are processed.

        Usage:
            - Using the ``.query()`` method will send the ``ACTive:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTive:MODE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACTive:MODE value`` command.

        SCPI Syntax:
            ```
            - ACTive:MODE {NORMal|CALibration|DIAGnostic}
            - ACTive:MODE?
            ```

        Info:
            - ``NORMal`` disables any active state for either calibration or diagnostics. When
              entering the active state of normal, the hardware is set to a default state and the
              previous system state is restored and waveform playout is set to off.
            - ``CALibration`` enables the active state for the calibration. Entering the active
              state of calibration turns waveform playout off.
            - ``DIAGnostic`` enables the active state for the diagnostics. Entering the active state
              of diagnostics turns waveform playout off.
            - ``*RST`` sets this to NORM.
        """
        return self._mode
