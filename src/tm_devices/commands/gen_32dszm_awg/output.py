"""The output commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - OUTPut[n]:FILTer:LPASs:FREQuency {<NR3>|INFinity}
    - OUTPut[n]:FILTer:LPASs:FREQuency?
    - OUTPut[n]:STATe <output_state>
    - OUTPut[n]:STATe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class OutputItemState(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:STATe`` command.

    Description:
        - This command and query sets or returns the output state of the arbitrary waveform
          generator. Setting the output state of a channel to ON will switch on its analog output
          signal and marker.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:STATe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``OUTPut[n]:STATe value`` command.

    SCPI Syntax:
        ```
        - OUTPut[n]:STATe <output_state>
        - OUTPut[n]:STATe?
        ```

    Info:
        - ``<output_state>`` ::=<Boolean>.
        - ``0`` sets the channel output to False (OFF).
        - ``1`` sets the channel output to True (ON).
    """


class OutputItemFilterLpassFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``OUTPut[n]:FILTer:LPASs:FREQuency`` command.

    Description:
        - This command and query sets or returns the low-pass filter frequency of the filter.
          INFinity is same as Through (no filter). This command is not available on instruments with
          option 02 or option 06.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer:LPASs:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:FILTer:LPASs:FREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``OUTPut[n]:FILTer:LPASs:FREQuency value`` command.

    SCPI Syntax:
        ```
        - OUTPut[n]:FILTer:LPASs:FREQuency {<NR3>|INFinity}
        - OUTPut[n]:FILTer:LPASs:FREQuency?
        ```

    Info:
        - ``<NR3>``
    """


class OutputItemFilterLpass(SCPICmdRead):
    """The ``OUTPut[n]:FILTer:LPASs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer:LPASs?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:FILTer:LPASs?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``OUTPut[n]:FILTer:LPASs:FREQuency`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = OutputItemFilterLpassFrequency(device, f"{self._cmd_syntax}:FREQuency")

    @property
    def frequency(self) -> OutputItemFilterLpassFrequency:
        """Return the ``OUTPut[n]:FILTer:LPASs:FREQuency`` command.

        Description:
            - This command and query sets or returns the low-pass filter frequency of the filter.
              INFinity is same as Through (no filter). This command is not available on instruments
              with option 02 or option 06.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer:LPASs:FREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``OUTPut[n]:FILTer:LPASs:FREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``OUTPut[n]:FILTer:LPASs:FREQuency value`` command.

        SCPI Syntax:
            ```
            - OUTPut[n]:FILTer:LPASs:FREQuency {<NR3>|INFinity}
            - OUTPut[n]:FILTer:LPASs:FREQuency?
            ```

        Info:
            - ``<NR3>``
        """
        return self._frequency


class OutputItemFilter(SCPICmdRead):
    """The ``OUTPut[n]:FILTer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]:FILTer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.lpass``: The ``OUTPut[n]:FILTer:LPASs`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._lpass = OutputItemFilterLpass(device, f"{self._cmd_syntax}:LPASs")

    @property
    def lpass(self) -> OutputItemFilterLpass:
        """Return the ``OUTPut[n]:FILTer:LPASs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer:LPASs?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:FILTer:LPASs?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``OUTPut[n]:FILTer:LPASs:FREQuency`` command.
        """
        return self._lpass


class OutputItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``OUTPut[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``OUTPut[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``OUTPut[n]?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.filter``: The ``OUTPut[n]:FILTer`` command tree.
        - ``.state``: The ``OUTPut[n]:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "OUTPut[n]") -> None:
        super().__init__(device, cmd_syntax)
        self._filter = OutputItemFilter(device, f"{self._cmd_syntax}:FILTer")
        self._state = OutputItemState(device, f"{self._cmd_syntax}:STATe")

    @property
    def filter(self) -> OutputItemFilter:
        """Return the ``OUTPut[n]:FILTer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:FILTer?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:FILTer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.lpass``: The ``OUTPut[n]:FILTer:LPASs`` command tree.
        """
        return self._filter

    @property
    def state(self) -> OutputItemState:
        """Return the ``OUTPut[n]:STATe`` command.

        Description:
            - This command and query sets or returns the output state of the arbitrary waveform
              generator. Setting the output state of a channel to ON will switch on its analog
              output signal and marker.

        Usage:
            - Using the ``.query()`` method will send the ``OUTPut[n]:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``OUTPut[n]:STATe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``OUTPut[n]:STATe value`` command.

        SCPI Syntax:
            ```
            - OUTPut[n]:STATe <output_state>
            - OUTPut[n]:STATe?
            ```

        Info:
            - ``<output_state>`` ::=<Boolean>.
            - ``0`` sets the channel output to False (OFF).
            - ``1`` sets the channel output to True (ON).
        """
        return self._state
