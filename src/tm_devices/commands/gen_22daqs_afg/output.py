"""The output commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - OUTPut:TRIGger:MODE {TRIGger|SYNC}
    - OUTPut:TRIGger:MODE?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class OutputTriggerMode(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut:TRIGger:MODE`` command.

    Description:
        - This command sets or queries the mode (trigger or sync) for Trigger Output signal. When
          the burst count is set to Inf-Cycles in burst mode, TRIGger indicates that the infinite
          number of cycles of waveform will be output from the Trigger Output connector. When the
          burst count is set to Inf-Cycles in burst mode, SYNC indicates that one pulse waveform is
          output from the Trigger Output connector when the Inf-Cycles starts. When Run Mode is
          specified other than Burst Inf-Cycles, TRIGger and SYNC have the same effect.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut:TRIGger:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut:TRIGger:MODE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut:TRIGger:MODE value`` command.

    SCPI Syntax:
        ```
        - OUTPut:TRIGger:MODE {TRIGger|SYNC}
        - OUTPut:TRIGger:MODE?
        ```
    """


class OutputTrigger(SCPICmdRead):
    """The ``OUTPut:TRIGger`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut:TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut:TRIGger?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``OUTPut:TRIGger:MODE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = OutputTriggerMode(device, f"{self._cmd_syntax}:MODE")

    @property
    def mode(self) -> OutputTriggerMode:
        """Return the ``OUTPut:TRIGger:MODE`` command.

        Description:
            - This command sets or queries the mode (trigger or sync) for Trigger Output signal.
              When the burst count is set to Inf-Cycles in burst mode, TRIGger indicates that the
              infinite number of cycles of waveform will be output from the Trigger Output
              connector. When the burst count is set to Inf-Cycles in burst mode, SYNC indicates
              that one pulse waveform is output from the Trigger Output connector when the
              Inf-Cycles starts. When Run Mode is specified other than Burst Inf-Cycles, TRIGger and
              SYNC have the same effect.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut:TRIGger:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut:TRIGger:MODE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut:TRIGger:MODE value``
              command.

        SCPI Syntax:
            ```
            - OUTPut:TRIGger:MODE {TRIGger|SYNC}
            - OUTPut:TRIGger:MODE?
            ```
        """
        return self._mode


class Output(SCPICmdRead):
    """The ``OUTPut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.trigger``: The ``OUTPut:TRIGger`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "OUTPut") -> None:
        super().__init__(device, cmd_syntax)
        self._trigger = OutputTrigger(device, f"{self._cmd_syntax}:TRIGger")

    @property
    def trigger(self) -> OutputTrigger:
        """Return the ``OUTPut:TRIGger`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut:TRIGger?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut:TRIGger?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``OUTPut:TRIGger:MODE`` command.
        """
        return self._trigger
