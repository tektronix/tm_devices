"""The select commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SELect {ON|OFF}
    - SELect:BUS<x> {ON|OFF|<NR1>}
    - SELect:BUS<x>?
    - SELect:CH<x> {ON|OFF|<NR1>}
    - SELect:CH<x>?
    - SELect:CONTROl {CH<x>|MATH|BUS<x>}
    - SELect:CONTROl?
    - SELect:D<x> {ON|OFF|<NR1>}
    - SELect:D<x>?
    - SELect:MATH1 {ON|OFF|<NR1>}
    - SELect:MATH1?
    - SELect:REF<x> {ON|OFF|<NR1>}
    - SELect:REF<x>?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedChannel,
    ValidatedDigitalBit,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SelectRefItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``SELect:REF<x>`` command.

    Description:
        - Turns on and off the display of the reference waveform <x>. The <x > variable represents
          the reference channel number, which can be 1-4. The query returns whether the channel is
          on or off.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:REF<x> value`` command.

    SCPI Syntax:
        ```
        - SELect:REF<x> {ON|OFF|<NR1>}
        - SELect:REF<x>?
        ```

    Info:
        - ``ON`` turns on the display of the specified waveform. This waveform also becomes the
          selected waveform.
        - ``OFF`` turns off the display of the specified waveform.
        - ``<NR1>`` = 0 turns off the display of the specified waveform; any other value turns on
          the display of the specified waveform.
    """


class SelectMath1(SCPICmdWrite, SCPICmdRead):
    """The ``SELect:MATH1`` command.

    Description:
        - Turns on and off the display of the math waveform. The query returns whether the math
          waveform is on or off but does not indicate whether it is the selected waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:MATH1?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:MATH1?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:MATH1 value`` command.

    SCPI Syntax:
        ```
        - SELect:MATH1 {ON|OFF|<NR1>}
        - SELect:MATH1?
        ```

    Info:
        - ``ON`` turns on the display of the specified waveform. This waveform also becomes the
          selected waveform.
        - ``OFF`` turns off the display of the specified waveform.
        - ``<NR1>`` = 0 turns off the display of the specified waveform; any other value turns on
          the display of the specified waveform.
    """


class SelectDigitalBit(ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead):
    """The ``SELect:D<x>`` command.

    Description:
        - Turns on the display of the digital channel <x> and resets the acquisition. <x > is the
          channel number, which can be 0-15. The query returns whether the channel is on or off but
          does not indicate whether it is the selected waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:D<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:D<x> value`` command.

    SCPI Syntax:
        ```
        - SELect:D<x> {ON|OFF|<NR1>}
        - SELect:D<x>?
        ```

    Info:
        - ``ON`` turns on the display of the specified waveform. This waveform also becomes the
          selected waveform.
        - ``OFF`` turns off the display of the specified waveform.
        - ``<NR1>`` = 0 turns off the display of the specified waveform; any other value turns on
          the display of the specified waveform.
    """


class SelectControl(SCPICmdWrite, SCPICmdRead):
    """The ``SELect:CONTROl`` command.

    Description:
        - Sets or returns the waveform that is the recipient of future channel-related commands, for
          example, the cursor commands. The command form also performs the equivalent of a
          ``SELECT:CHX ON`` command, as well as the Math, Reference, and Bus variations of that
          command.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:CONTROl?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:CONTROl?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:CONTROl value`` command.

    SCPI Syntax:
        ```
        - SELect:CONTROl {CH<x>|MATH|BUS<x>}
        - SELect:CONTROl?
        ```

    Info:
        - ``CH<x>`` specifies a channel waveform as the waveform affected by the front-panel
          controls. <x> is the channel number.
        - ``MATH`` specifies the math waveform as the waveform that is affected by the front-panel
          controls.
        - ``BUS<x>`` specifies a bus waveform as the waveform affected by the front-panel controls.
          <x> specifies the bus number.
    """


class SelectChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``SELect:CH<x>`` command.

    Description:
        - This command sets or queries the displayed state of the specified channel waveform. The x
          can be channel 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:CH<x> value`` command.

    SCPI Syntax:
        ```
        - SELect:CH<x> {ON|OFF|<NR1>}
        - SELect:CH<x>?
        ```

    Info:
        - ``<NR1> = 0`` turns off the display of the specified channel waveform; any other value
          turns on the display of the specified waveform.
        - ``OFF`` turns off the display of the indicated channel waveform.
        - ``ON`` displays the indicated channel waveform.
    """


class SelectBusItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``SELect:BUS<x>`` command.

    Description:
        - This command turns on and off the display of the waveform for <x>, where x is the bus
          number. The query returns whether the channel is on or off but does not indicate whether
          it is the selected waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:BUS<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:BUS<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:BUS<x> value`` command.

    SCPI Syntax:
        ```
        - SELect:BUS<x> {ON|OFF|<NR1>}
        - SELect:BUS<x>?
        ```
    """


class Select(SCPICmdWrite, SCPICmdRead):
    """The ``SELect`` command.

    Description:
        - Sets or returns the selected waveform display (controlled by the front-panel) on or off.

    Usage:
        - Using the ``.write(value)`` method will send the ``SELect value`` command.

    SCPI Syntax:
        ```
        - SELect {ON|OFF}
        ```

    Info:
        - ``ON`` turns the selected waveform display on.
        - ``OFF`` turns the selected waveform display off.

    Properties:
        - ``.bus``: The ``SELect:BUS<x>`` command.
        - ``.ch``: The ``SELect:CH<x>`` command.
        - ``.control``: The ``SELect:CONTROl`` command.
        - ``.d``: The ``SELect:D<x>`` command.
        - ``.math1``: The ``SELect:MATH1`` command.
        - ``.ref``: The ``SELect:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SELect") -> None:
        super().__init__(device, cmd_syntax)
        self._bus: Dict[int, SelectBusItem] = DefaultDictPassKeyToFactory(
            lambda x: SelectBusItem(device, f"{self._cmd_syntax}:BUS{x}")
        )
        self._ch: Dict[int, SelectChannel] = DefaultDictPassKeyToFactory(
            lambda x: SelectChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._control = SelectControl(device, f"{self._cmd_syntax}:CONTROl")
        self._d: Dict[int, SelectDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: SelectDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )
        self._math1 = SelectMath1(device, f"{self._cmd_syntax}:MATH1")
        self._ref: Dict[int, SelectRefItem] = DefaultDictPassKeyToFactory(
            lambda x: SelectRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def bus(self) -> Dict[int, SelectBusItem]:
        """Return the ``SELect:BUS<x>`` command.

        Description:
            - This command turns on and off the display of the waveform for <x>, where x is the bus
              number. The query returns whether the channel is on or off but does not indicate
              whether it is the selected waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:BUS<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:BUS<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:BUS<x> value`` command.

        SCPI Syntax:
            ```
            - SELect:BUS<x> {ON|OFF|<NR1>}
            - SELect:BUS<x>?
            ```
        """
        return self._bus

    @property
    def ch(self) -> Dict[int, SelectChannel]:
        """Return the ``SELect:CH<x>`` command.

        Description:
            - This command sets or queries the displayed state of the specified channel waveform.
              The x can be channel 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:CH<x> value`` command.

        SCPI Syntax:
            ```
            - SELect:CH<x> {ON|OFF|<NR1>}
            - SELect:CH<x>?
            ```

        Info:
            - ``<NR1> = 0`` turns off the display of the specified channel waveform; any other value
              turns on the display of the specified waveform.
            - ``OFF`` turns off the display of the indicated channel waveform.
            - ``ON`` displays the indicated channel waveform.
        """
        return self._ch

    @property
    def control(self) -> SelectControl:
        """Return the ``SELect:CONTROl`` command.

        Description:
            - Sets or returns the waveform that is the recipient of future channel-related commands,
              for example, the cursor commands. The command form also performs the equivalent of a
              ``SELECT:CHX ON`` command, as well as the Math, Reference, and Bus variations of that
              command.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:CONTROl?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:CONTROl?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:CONTROl value`` command.

        SCPI Syntax:
            ```
            - SELect:CONTROl {CH<x>|MATH|BUS<x>}
            - SELect:CONTROl?
            ```

        Info:
            - ``CH<x>`` specifies a channel waveform as the waveform affected by the front-panel
              controls. <x> is the channel number.
            - ``MATH`` specifies the math waveform as the waveform that is affected by the
              front-panel controls.
            - ``BUS<x>`` specifies a bus waveform as the waveform affected by the front-panel
              controls. <x> specifies the bus number.
        """
        return self._control

    @property
    def d(self) -> Dict[int, SelectDigitalBit]:
        """Return the ``SELect:D<x>`` command.

        Description:
            - Turns on the display of the digital channel <x> and resets the acquisition. <x > is
              the channel number, which can be 0-15. The query returns whether the channel is on or
              off but does not indicate whether it is the selected waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:D<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:D<x> value`` command.

        SCPI Syntax:
            ```
            - SELect:D<x> {ON|OFF|<NR1>}
            - SELect:D<x>?
            ```

        Info:
            - ``ON`` turns on the display of the specified waveform. This waveform also becomes the
              selected waveform.
            - ``OFF`` turns off the display of the specified waveform.
            - ``<NR1>`` = 0 turns off the display of the specified waveform; any other value turns
              on the display of the specified waveform.
        """
        return self._d

    @property
    def math1(self) -> SelectMath1:
        """Return the ``SELect:MATH1`` command.

        Description:
            - Turns on and off the display of the math waveform. The query returns whether the math
              waveform is on or off but does not indicate whether it is the selected waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:MATH1?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:MATH1?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:MATH1 value`` command.

        SCPI Syntax:
            ```
            - SELect:MATH1 {ON|OFF|<NR1>}
            - SELect:MATH1?
            ```

        Info:
            - ``ON`` turns on the display of the specified waveform. This waveform also becomes the
              selected waveform.
            - ``OFF`` turns off the display of the specified waveform.
            - ``<NR1>`` = 0 turns off the display of the specified waveform; any other value turns
              on the display of the specified waveform.
        """
        return self._math1

    @property
    def ref(self) -> Dict[int, SelectRefItem]:
        """Return the ``SELect:REF<x>`` command.

        Description:
            - Turns on and off the display of the reference waveform <x>. The <x > variable
              represents the reference channel number, which can be 1-4. The query returns whether
              the channel is on or off.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:REF<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:REF<x> value`` command.

        SCPI Syntax:
            ```
            - SELect:REF<x> {ON|OFF|<NR1>}
            - SELect:REF<x>?
            ```

        Info:
            - ``ON`` turns on the display of the specified waveform. This waveform also becomes the
              selected waveform.
            - ``OFF`` turns off the display of the specified waveform.
            - ``<NR1>`` = 0 turns off the display of the specified waveform; any other value turns
              on the display of the specified waveform.
        """
        return self._ref
