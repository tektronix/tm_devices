"""The source3 commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SOURce3:POWer:LEVel:IMMediate:AMPLitude {<percent>|MINimum|MAXimum}
    - SOURce3:POWer:LEVel:IMMediate:AMPLitude?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Source3PowerLevelImmediateAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce3:POWer:LEVel:IMMediate:AMPLitude`` command.

    Description:
        - This command sets or queries the internal noise level which applies to the output signal
          for the specified channel. The noise level represents the percent against current
          amplitude level. The setting range is 0 to 50%. This command is available when Run Mode is
          set to Continuous, Burst, or Sweep. You can set or query whether to add the internal noise
          to the output signal using the [SOURce[1|2]]``:COMBine:FEED`` command.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce3:POWer:LEVel:IMMediate:AMPLitude?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce3:POWer:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce3:POWer:LEVel:IMMediate:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - SOURce3:POWer:LEVel:IMMediate:AMPLitude {<percent>|MINimum|MAXimum}
        - SOURce3:POWer:LEVel:IMMediate:AMPLitude?
        ```
    """


class Source3PowerLevelImmediate(SCPICmdRead):
    """The ``SOURce3:POWer:LEVel:IMMediate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce3:POWer:LEVel:IMMediate?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce3:POWer:LEVel:IMMediate?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``SOURce3:POWer:LEVel:IMMediate:AMPLitude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = Source3PowerLevelImmediateAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )

    @property
    def amplitude(self) -> Source3PowerLevelImmediateAmplitude:
        """Return the ``SOURce3:POWer:LEVel:IMMediate:AMPLitude`` command.

        Description:
            - This command sets or queries the internal noise level which applies to the output
              signal for the specified channel. The noise level represents the percent against
              current amplitude level. The setting range is 0 to 50%. This command is available when
              Run Mode is set to Continuous, Burst, or Sweep. You can set or query whether to add
              the internal noise to the output signal using the [SOURce[1|2]]``:COMBine:FEED``
              command.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce3:POWer:LEVel:IMMediate:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce3:POWer:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce3:POWer:LEVel:IMMediate:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - SOURce3:POWer:LEVel:IMMediate:AMPLitude {<percent>|MINimum|MAXimum}
            - SOURce3:POWer:LEVel:IMMediate:AMPLitude?
            ```
        """
        return self._amplitude


class Source3PowerLevel(SCPICmdRead):
    """The ``SOURce3:POWer:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce3:POWer:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce3:POWer:LEVel?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``SOURce3:POWer:LEVel:IMMediate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = Source3PowerLevelImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> Source3PowerLevelImmediate:
        """Return the ``SOURce3:POWer:LEVel:IMMediate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce3:POWer:LEVel:IMMediate?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce3:POWer:LEVel:IMMediate?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``SOURce3:POWer:LEVel:IMMediate:AMPLitude`` command.
        """
        return self._immediate


class Source3Power(SCPICmdRead):
    """The ``SOURce3:POWer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce3:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce3:POWer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.level``: The ``SOURce3:POWer:LEVel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._level = Source3PowerLevel(device, f"{self._cmd_syntax}:LEVel")

    @property
    def level(self) -> Source3PowerLevel:
        """Return the ``SOURce3:POWer:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce3:POWer:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce3:POWer:LEVel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``SOURce3:POWer:LEVel:IMMediate`` command tree.
        """
        return self._level


class Source3(SCPICmdRead):
    """The ``SOURce3`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce3?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce3?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.power``: The ``SOURce3:POWer`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SOURce3") -> None:
        super().__init__(device, cmd_syntax)
        self._power = Source3Power(device, f"{self._cmd_syntax}:POWer")

    @property
    def power(self) -> Source3Power:
        """Return the ``SOURce3:POWer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce3:POWer?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce3:POWer?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.level``: The ``SOURce3:POWer:LEVel`` command tree.
        """
        return self._power
