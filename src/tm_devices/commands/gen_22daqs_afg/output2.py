"""The output2 commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - OUTPut2:IMPedance {<ohms>|INFinity|MINimum|MAXimum}
    - OUTPut2:IMPedance?
    - OUTPut2:POLarity {NORMal|INVerted}
    - OUTPut2:POLarity?
    - OUTPut2:STATe {ON|OFF|<NR1>}
    - OUTPut2:STATe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Output2State(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut2:STATe`` command.

    Description:
        - This command sets or query whether to enable the arbitrary function generator output for
          the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut2:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut2:STATe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut2:STATe value`` command.

    SCPI Syntax:
        ```
        - OUTPut2:STATe {ON|OFF|<NR1>}
        - OUTPut2:STATe?
        ```
    """


class Output2Polarity(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut2:POLarity`` command.

    Description:
        - This command inverts a specified output waveform relative to the offset level. The query
          command returns the polarity for the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut2:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut2:POLarity?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut2:POLarity value`` command.

    SCPI Syntax:
        ```
        - OUTPut2:POLarity {NORMal|INVerted}
        - OUTPut2:POLarity?
        ```
    """


class Output2Impedance(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut2:IMPedance`` command.

    Description:
        - The ``OUTPut:IMPedance`` command sets the output load impedance for the specified channel.
          The specified value is used for amplitude, offset, and high/low level settings. You can
          set the impedance to any value from 1 Ω to 10 kΩ with a resolution of 1 Ω or 3 digits. The
          default value is 50 Ω . The ``OUTPut:IMPedance?`` command returns the current load
          impedance setting in ohms. If the load impedance is set to INFinity, the query command
          returns '9.9E+37'.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut2:IMPedance?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut2:IMPedance?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut2:IMPedance value`` command.

    SCPI Syntax:
        ```
        - OUTPut2:IMPedance {<ohms>|INFinity|MINimum|MAXimum}
        - OUTPut2:IMPedance?
        ```
    """


class Output2(SCPICmdRead):
    """The ``OUTPut2`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut2?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut2?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.impedance``: The ``OUTPut2:IMPedance`` command.
        - ``.polarity``: The ``OUTPut2:POLarity`` command.
        - ``.state``: The ``OUTPut2:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "OUTPut2") -> None:
        super().__init__(device, cmd_syntax)
        self._impedance = Output2Impedance(device, f"{self._cmd_syntax}:IMPedance")
        self._polarity = Output2Polarity(device, f"{self._cmd_syntax}:POLarity")
        self._state = Output2State(device, f"{self._cmd_syntax}:STATe")

    @property
    def impedance(self) -> Output2Impedance:
        """Return the ``OUTPut2:IMPedance`` command.

        Description:
            - The ``OUTPut:IMPedance`` command sets the output load impedance for the specified
              channel. The specified value is used for amplitude, offset, and high/low level
              settings. You can set the impedance to any value from 1 Ω to 10 kΩ with a resolution
              of 1 Ω or 3 digits. The default value is 50 Ω . The ``OUTPut:IMPedance?`` command
              returns the current load impedance setting in ohms. If the load impedance is set to
              INFinity, the query command returns '9.9E+37'.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut2:IMPedance?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut2:IMPedance?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut2:IMPedance value`` command.

        SCPI Syntax:
            ```
            - OUTPut2:IMPedance {<ohms>|INFinity|MINimum|MAXimum}
            - OUTPut2:IMPedance?
            ```
        """
        return self._impedance

    @property
    def polarity(self) -> Output2Polarity:
        """Return the ``OUTPut2:POLarity`` command.

        Description:
            - This command inverts a specified output waveform relative to the offset level. The
              query command returns the polarity for the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut2:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut2:POLarity?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut2:POLarity value`` command.

        SCPI Syntax:
            ```
            - OUTPut2:POLarity {NORMal|INVerted}
            - OUTPut2:POLarity?
            ```
        """
        return self._polarity

    @property
    def state(self) -> Output2State:
        """Return the ``OUTPut2:STATe`` command.

        Description:
            - This command sets or query whether to enable the arbitrary function generator output
              for the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut2:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut2:STATe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut2:STATe value`` command.

        SCPI Syntax:
            ```
            - OUTPut2:STATe {ON|OFF|<NR1>}
            - OUTPut2:STATe?
            ```
        """
        return self._state
