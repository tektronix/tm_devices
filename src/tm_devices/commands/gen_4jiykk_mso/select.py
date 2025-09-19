"""The select commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SELect:CH<x> {ON|OFF|1|0}
    - SELect:CH<x>?
    - SELect:DCH<x>:DAll {ON|OFF|<NR1>}
    - SELect:DCH<x>:DAll?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedChannel,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SelectDchItemDall(SCPICmdWrite, SCPICmdRead):
    """The ``SELect:DCH<x>:DAll`` command.

    Description:
        - This command turns on or off all constituent digital channels.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:DCH<x>:DAll?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:DCH<x>:DAll?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:DCH<x>:DAll value`` command.

    SCPI Syntax:
        ```
        - SELect:DCH<x>:DAll {ON|OFF|<NR1>}
        - SELect:DCH<x>:DAll?
        ```

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``<NR1>`` = 0 disables the specified digital channel; any other value turns the on the
          digital channel.
        - ``OFF`` turns off the specified digital channel.
        - ``ON`` turns on the specified digital channel.
    """


class SelectDchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SELect:DCH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:DCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:DCH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.

    Properties:
        - ``.dall``: The ``SELect:DCH<x>:DAll`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dall = SelectDchItemDall(device, f"{self._cmd_syntax}:DAll")

    @property
    def dall(self) -> SelectDchItemDall:
        """Return the ``SELect:DCH<x>:DAll`` command.

        Description:
            - This command turns on or off all constituent digital channels.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:DCH<x>:DAll?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:DCH<x>:DAll?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:DCH<x>:DAll value`` command.

        SCPI Syntax:
            ```
            - SELect:DCH<x>:DAll {ON|OFF|<NR1>}
            - SELect:DCH<x>:DAll?
            ```

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``<NR1>`` = 0 disables the specified digital channel; any other value turns the on the
              digital channel.
            - ``OFF`` turns off the specified digital channel.
            - ``ON`` turns on the specified digital channel.
        """
        return self._dall


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
        - ``.dch``: The ``SELect:DCH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SELect") -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SelectChannel] = DefaultDictPassKeyToFactory(
            lambda x: SelectChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._dch: Dict[int, SelectDchItem] = DefaultDictPassKeyToFactory(
            lambda x: SelectDchItem(device, f"{self._cmd_syntax}:DCH{x}")
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

    @property
    def dch(self) -> Dict[int, SelectDchItem]:
        """Return the ``SELect:DCH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:DCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:DCH<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.

        Sub-properties:
            - ``.dall``: The ``SELect:DCH<x>:DAll`` command.
        """
        return self._dch
