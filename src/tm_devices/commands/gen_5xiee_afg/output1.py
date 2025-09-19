"""The output1 commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - OUTPut1:IMPedance {<ohms>|INFinity|MINimum|MAXimum}
    - OUTPut1:IMPedance?
    - OUTPut1:POLarity {NORMal|INVerted}
    - OUTPut1:POLarity?
    - OUTPut1:STATe {ON|OFF|<NR1>}
    - OUTPut1:STATe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Output1State(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut1:STATe`` command.

    Description:
        - This command sets or query whether to enable the arbitrary function generator output for
          the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut1:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut1:STATe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut1:STATe value`` command.

    SCPI Syntax:
        ```
        - OUTPut1:STATe {ON|OFF|<NR1>}
        - OUTPut1:STATe?
        ```
    """


class Output1Polarity(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut1:POLarity`` command.

    Description:
        - This command inverts a specified output waveform relative to the offset level. The query
          command returns the polarity for the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut1:POLarity?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut1:POLarity?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut1:POLarity value`` command.

    SCPI Syntax:
        ```
        - OUTPut1:POLarity {NORMal|INVerted}
        - OUTPut1:POLarity?
        ```
    """


class Output1Impedance(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut1:IMPedance`` command.

    Description:
        - The ``OUTPut:IMPedance`` command sets the output load impedance for the specified channel.
          The specified value is used for amplitude, offset, and high/low level settings. You can
          set the impedance to any value from 1 Ω to 10 kΩ with a resolution of 1 Ω or 3 digits. The
          default value is 50 Ω . The ``OUTPut:IMPedance?`` command returns the current load
          impedance setting in ohms. If the load impedance is set to INFinity, the query command
          returns '9.9E+37'.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut1:IMPedance?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut1:IMPedance?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut1:IMPedance value`` command.

    SCPI Syntax:
        ```
        - OUTPut1:IMPedance {<ohms>|INFinity|MINimum|MAXimum}
        - OUTPut1:IMPedance?
        ```
    """


class Output1(SCPICmdRead):
    """The ``OUTPut1`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut1?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut1?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.impedance``: The ``OUTPut1:IMPedance`` command.
        - ``.polarity``: The ``OUTPut1:POLarity`` command.
        - ``.state``: The ``OUTPut1:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "OUTPut1") -> None:
        super().__init__(device, cmd_syntax)
        self._impedance = Output1Impedance(device, f"{self._cmd_syntax}:IMPedance")
        self._polarity = Output1Polarity(device, f"{self._cmd_syntax}:POLarity")
        self._state = Output1State(device, f"{self._cmd_syntax}:STATe")

    @property
    def impedance(self) -> Output1Impedance:
        """Return the ``OUTPut1:IMPedance`` command.

        Description:
            - The ``OUTPut:IMPedance`` command sets the output load impedance for the specified
              channel. The specified value is used for amplitude, offset, and high/low level
              settings. You can set the impedance to any value from 1 Ω to 10 kΩ with a resolution
              of 1 Ω or 3 digits. The default value is 50 Ω . The ``OUTPut:IMPedance?`` command
              returns the current load impedance setting in ohms. If the load impedance is set to
              INFinity, the query command returns '9.9E+37'.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut1:IMPedance?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut1:IMPedance?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut1:IMPedance value`` command.

        SCPI Syntax:
            ```
            - OUTPut1:IMPedance {<ohms>|INFinity|MINimum|MAXimum}
            - OUTPut1:IMPedance?
            ```
        """
        return self._impedance

    @property
    def polarity(self) -> Output1Polarity:
        """Return the ``OUTPut1:POLarity`` command.

        Description:
            - This command inverts a specified output waveform relative to the offset level. The
              query command returns the polarity for the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut1:POLarity?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut1:POLarity?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut1:POLarity value`` command.

        SCPI Syntax:
            ```
            - OUTPut1:POLarity {NORMal|INVerted}
            - OUTPut1:POLarity?
            ```
        """
        return self._polarity

    @property
    def state(self) -> Output1State:
        """Return the ``OUTPut1:STATe`` command.

        Description:
            - This command sets or query whether to enable the arbitrary function generator output
              for the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut1:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut1:STATe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut1:STATe value`` command.

        SCPI Syntax:
            ```
            - OUTPut1:STATe {ON|OFF|<NR1>}
            - OUTPut1:STATe?
            ```
        """
        return self._state
