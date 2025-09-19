"""The source4 commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SOURce4:POWer:LEVel:IMMediate:AMPLitude {<percent>|MINimum|MAXimum}
    - SOURce4:POWer:LEVel:IMMediate:AMPLitude?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Source4PowerLevelImmediateAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``SOURce4:POWer:LEVel:IMMediate:AMPLitude`` command.

    Description:
        - This command sets or queries the internal noise level which applies to the output signal
          for the specified channel. The noise level represents the percent against current
          amplitude level. The setting range is 0 to 50%. This command is available when Run Mode is
          set to Continuous, Burst, or Sweep. You can set or query whether to add the internal noise
          to the output signal using the [SOURce[1|2]]``:COMBine:FEED`` command.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce4:POWer:LEVel:IMMediate:AMPLitude?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``SOURce4:POWer:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SOURce4:POWer:LEVel:IMMediate:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - SOURce4:POWer:LEVel:IMMediate:AMPLitude {<percent>|MINimum|MAXimum}
        - SOURce4:POWer:LEVel:IMMediate:AMPLitude?
        ```
    """


class Source4PowerLevelImmediate(SCPICmdRead):
    """The ``SOURce4:POWer:LEVel:IMMediate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce4:POWer:LEVel:IMMediate?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce4:POWer:LEVel:IMMediate?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``SOURce4:POWer:LEVel:IMMediate:AMPLitude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = Source4PowerLevelImmediateAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )

    @property
    def amplitude(self) -> Source4PowerLevelImmediateAmplitude:
        """Return the ``SOURce4:POWer:LEVel:IMMediate:AMPLitude`` command.

        Description:
            - This command sets or queries the internal noise level which applies to the output
              signal for the specified channel. The noise level represents the percent against
              current amplitude level. The setting range is 0 to 50%. This command is available when
              Run Mode is set to Continuous, Burst, or Sweep. You can set or query whether to add
              the internal noise to the output signal using the [SOURce[1|2]]``:COMBine:FEED``
              command.

        Usage:
            - Using the ``.query()`` method will send the
              ``SOURce4:POWer:LEVel:IMMediate:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``SOURce4:POWer:LEVel:IMMediate:AMPLitude?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SOURce4:POWer:LEVel:IMMediate:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - SOURce4:POWer:LEVel:IMMediate:AMPLitude {<percent>|MINimum|MAXimum}
            - SOURce4:POWer:LEVel:IMMediate:AMPLitude?
            ```
        """
        return self._amplitude


class Source4PowerLevel(SCPICmdRead):
    """The ``SOURce4:POWer:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce4:POWer:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce4:POWer:LEVel?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``SOURce4:POWer:LEVel:IMMediate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = Source4PowerLevelImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> Source4PowerLevelImmediate:
        """Return the ``SOURce4:POWer:LEVel:IMMediate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce4:POWer:LEVel:IMMediate?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce4:POWer:LEVel:IMMediate?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``SOURce4:POWer:LEVel:IMMediate:AMPLitude`` command.
        """
        return self._immediate


class Source4Power(SCPICmdRead):
    """The ``SOURce4:POWer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce4:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce4:POWer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.level``: The ``SOURce4:POWer:LEVel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._level = Source4PowerLevel(device, f"{self._cmd_syntax}:LEVel")

    @property
    def level(self) -> Source4PowerLevel:
        """Return the ``SOURce4:POWer:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce4:POWer:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce4:POWer:LEVel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``SOURce4:POWer:LEVel:IMMediate`` command tree.
        """
        return self._level


class Source4(SCPICmdRead):
    """The ``SOURce4`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SOURce4?`` query.
        - Using the ``.verify(value)`` method will send the ``SOURce4?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.power``: The ``SOURce4:POWer`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SOURce4") -> None:
        super().__init__(device, cmd_syntax)
        self._power = Source4Power(device, f"{self._cmd_syntax}:POWer")

    @property
    def power(self) -> Source4Power:
        """Return the ``SOURce4:POWer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SOURce4:POWer?`` query.
            - Using the ``.verify(value)`` method will send the ``SOURce4:POWer?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.level``: The ``SOURce4:POWer:LEVel`` command tree.
        """
        return self._power
