"""The d commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - D<x>
    - D<x>:LABel <Qstring>
    - D<x>:LABel?
    - D<x>:POSition <NR3>
    - D<x>:POSition?
    - D<x>:THReshold {ECL|TTL|<NR3>}
    - D<x>:THReshold?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments, ValidatedDigitalBit

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DigitalBitThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``D<x>:THReshold`` command.

    Description:
        - This command specifies the logical threshold for the digital channel <x>, where x is the
          digital channel number D0 - D15.

    Usage:
        - Using the ``.query()`` method will send the ``D<x>:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``D<x>:THReshold?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``D<x>:THReshold value`` command.

    SCPI Syntax:
        ```
        - D<x>:THReshold {ECL|TTL|<NR3>}
        - D<x>:THReshold?
        ```

    Info:
        - ``ECL`` sets the digital threshold for channel <x> to a preset ECL high level of -1.3V.
        - ``TTL`` sets the digital threshold for channel <x> to a preset TTL high level of 1.4V.
        - ``<NR3>`` is a floating point number that specifies the digital threshold for channel <x>,
          in volts.
    """


class DigitalBitPosition(SCPICmdWrite, SCPICmdRead):
    """The ``D<x>:POSition`` command.

    Description:
        - This command specifies the vertical position for digital channel <x>, where x is the
          channel number.

    Usage:
        - Using the ``.query()`` method will send the ``D<x>:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``D<x>:POSition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``D<x>:POSition value`` command.

    SCPI Syntax:
        ```
        - D<x>:POSition <NR3>
        - D<x>:POSition?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the position of the digital channel,
          in slot units. Use the oscilloscope front-panel controls to place the channel; then query
          the channel to obtain an exact value for the position.
    """


class DigitalBitLabel(SCPICmdWrite, SCPICmdRead):
    """The ``D<x>:LABel`` command.

    Description:
        - This command specifies the waveform label for digital channel <x>, where x is the channel
          number.

    Usage:
        - Using the ``.query()`` method will send the ``D<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``D<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``D<x>:LABel value`` command.

    SCPI Syntax:
        ```
        - D<x>:LABel <Qstring>
        - D<x>:LABel?
        ```

    Info:
        - ``<Qstring>`` is an alphanumeric string of text, enclosed in quotes, that contains the
          text label information for the digital channel <x> waveform. The text string is limited to
          30 characters.
    """


class DigitalBit(ValidatedDigitalBit, SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``D<x>`` command.

    Description:
        - This command specifies parameters for digital channel <x>, where x is the channel number.

    Usage:
        - Using the ``.write()`` method will send the ``D<x>`` command.

    SCPI Syntax:
        ```
        - D<x>
        ```

    Properties:
        - ``.label``: The ``D<x>:LABel`` command.
        - ``.position``: The ``D<x>:POSition`` command.
        - ``.threshold``: The ``D<x>:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "D<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._label = DigitalBitLabel(device, f"{self._cmd_syntax}:LABel")
        self._position = DigitalBitPosition(device, f"{self._cmd_syntax}:POSition")
        self._threshold = DigitalBitThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def label(self) -> DigitalBitLabel:
        """Return the ``D<x>:LABel`` command.

        Description:
            - This command specifies the waveform label for digital channel <x>, where x is the
              channel number.

        Usage:
            - Using the ``.query()`` method will send the ``D<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``D<x>:LABel?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``D<x>:LABel value`` command.

        SCPI Syntax:
            ```
            - D<x>:LABel <Qstring>
            - D<x>:LABel?
            ```

        Info:
            - ``<Qstring>`` is an alphanumeric string of text, enclosed in quotes, that contains the
              text label information for the digital channel <x> waveform. The text string is
              limited to 30 characters.
        """
        return self._label

    @property
    def position(self) -> DigitalBitPosition:
        """Return the ``D<x>:POSition`` command.

        Description:
            - This command specifies the vertical position for digital channel <x>, where x is the
              channel number.

        Usage:
            - Using the ``.query()`` method will send the ``D<x>:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``D<x>:POSition?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``D<x>:POSition value`` command.

        SCPI Syntax:
            ```
            - D<x>:POSition <NR3>
            - D<x>:POSition?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the position of the digital
              channel, in slot units. Use the oscilloscope front-panel controls to place the
              channel; then query the channel to obtain an exact value for the position.
        """
        return self._position

    @property
    def threshold(self) -> DigitalBitThreshold:
        """Return the ``D<x>:THReshold`` command.

        Description:
            - This command specifies the logical threshold for the digital channel <x>, where x is
              the digital channel number D0 - D15.

        Usage:
            - Using the ``.query()`` method will send the ``D<x>:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``D<x>:THReshold?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``D<x>:THReshold value`` command.

        SCPI Syntax:
            ```
            - D<x>:THReshold {ECL|TTL|<NR3>}
            - D<x>:THReshold?
            ```

        Info:
            - ``ECL`` sets the digital threshold for channel <x> to a preset ECL high level of
              -1.3V.
            - ``TTL`` sets the digital threshold for channel <x> to a preset TTL high level of 1.4V.
            - ``<NR3>`` is a floating point number that specifies the digital threshold for channel
              <x>, in volts.
        """
        return self._threshold
