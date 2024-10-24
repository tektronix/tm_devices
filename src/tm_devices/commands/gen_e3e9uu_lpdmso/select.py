"""The select commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SELect:CH<x> {ON|OFF|1|0}
    - SELect:CH<x>?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import DefaultDictPassKeyToFactory, SCPICmdRead, SCPICmdWrite, ValidatedChannel

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SelectChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SELect:CH<x>`` command.

    Description:
        - Turns the display of the channel <x> waveform on or off, where <x > is the channel number.
          This command also resets the acquisition. The query returns whether the channel is on or
          off but does not indicate whether it is the specified waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SELect:CH<x> {ON|OFF|1|0}
        - SELect:CH<x>?
        ```

    Info:
        - ``ON`` turns on the display of the specified waveform. This waveform also becomes the
          selected waveform.
        - ``OFF`` turns off the display of the specified waveform.
        - ``1`` turns on the display of the specified waveform. This waveform also becomes the
          selected waveform.
        - ``0`` turns off the display of the specified waveform.
    """


class Select(SCPICmdRead):
    """The ``SELect`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``SELect:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SELect") -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SelectChannel] = DefaultDictPassKeyToFactory(
            lambda x: SelectChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, SelectChannel]:
        """Return the ``SELect:CH<x>`` command.

        Description:
            - Turns the display of the channel <x> waveform on or off, where <x > is the channel
              number. This command also resets the acquisition. The query returns whether the
              channel is on or off but does not indicate whether it is the specified waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SELect:CH<x> {ON|OFF|1|0}
            - SELect:CH<x>?
            ```

        Info:
            - ``ON`` turns on the display of the specified waveform. This waveform also becomes the
              selected waveform.
            - ``OFF`` turns off the display of the specified waveform.
            - ``1`` turns on the display of the specified waveform. This waveform also becomes the
              selected waveform.
            - ``0`` turns off the display of the specified waveform.
        """
        return self._ch
