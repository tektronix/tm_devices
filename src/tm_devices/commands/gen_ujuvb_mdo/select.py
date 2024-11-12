# pylint: disable=line-too-long
"""The select commands module.

These commands are used in the following models:
MDO3

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SELect:B<x> {OFF|ON|0|1}
    - SELect:B<x>?
    - SELect:BUS<x> {OFF|ON|0|1}
    - SELect:BUS<x>?
    - SELect:CH<x> {ON|OFF|1|0}
    - SELect:CH<x>?
    - SELect:CONTROl {CH<x>|MATH|REF<x>|BUS<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe|RF_NORMal|RF_AVErage|RF_MAXHold|RF_MINHold}
    - SELect:CONTROl?
    - SELect:D<x> {ON|OFF|<NR1>}
    - SELect:D<x>?
    - SELect:DAll {ON|OFF|0|1}
    - SELect:MATH {ON|OFF|<NR1>}
    - SELect:MATH1 {ON|OFF|<NR1>}
    - SELect:MATH1?
    - SELect:MATH?
    - SELect:REF<x> {ON|OFF|<NR1>}
    - SELect:REF<x>?
    - SELect:RF_AVErage {OFF|ON|0|1}
    - SELect:RF_AVErage?
    - SELect:RF_MAXHold {OFF|ON|0|1}
    - SELect:RF_MAXHold?
    - SELect:RF_MINHold {OFF|ON|0|1}
    - SELect:RF_MINHold?
    - SELect:RF_NORMal {OFF|ON|0|1}
    - SELect:RF_NORMal?
    - SELect?
    ```
"""  # noqa: E501

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


class SelectRfNormal(SCPICmdWrite, SCPICmdRead):
    """The ``SELect:RF_NORMal`` command.

    Description:
        - This command switches the frequency domain Normal trace display on or off in the frequency
          domain graticule.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:RF_NORMal?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:RF_NORMal?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:RF_NORMal value`` command.

    SCPI Syntax:
        ```
        - SELect:RF_NORMal {OFF|ON|0|1}
        - SELect:RF_NORMal?
        ```

    Info:
        - ``OFF`` or 0 turns the frequency domain Normal trace display off.
        - ``ON`` or 1 turns it on.
    """


class SelectRfMinhold(SCPICmdWrite, SCPICmdRead):
    """The ``SELect:RF_MINHold`` command.

    Description:
        - This command switches the frequency domain Min Hold trace display on or off in the
          frequency domain graticule.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:RF_MINHold?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:RF_MINHold?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:RF_MINHold value`` command.

    SCPI Syntax:
        ```
        - SELect:RF_MINHold {OFF|ON|0|1}
        - SELect:RF_MINHold?
        ```

    Info:
        - ``OFF`` or 0 turns the frequency domain Min Hold display off.
        - ``ON`` or 1 turns it on.
    """


class SelectRfMaxhold(SCPICmdWrite, SCPICmdRead):
    """The ``SELect:RF_MAXHold`` command.

    Description:
        - This command switches the frequency domain Max Hold trace display on or off in the
          frequency domain graticule.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:RF_MAXHold?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:RF_MAXHold?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:RF_MAXHold value`` command.

    SCPI Syntax:
        ```
        - SELect:RF_MAXHold {OFF|ON|0|1}
        - SELect:RF_MAXHold?
        ```

    Info:
        - ``OFF`` or 0 turns the frequency domain Max Hold trace display off.
        - ``ON`` or 1 turns it on.
    """


class SelectRfAverage(SCPICmdWrite, SCPICmdRead):
    """The ``SELect:RF_AVErage`` command.

    Description:
        - This command switches the RF Average trace display on or off in the frequency domain
          graticule.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:RF_AVErage?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:RF_AVErage?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:RF_AVErage value`` command.

    SCPI Syntax:
        ```
        - SELect:RF_AVErage {OFF|ON|0|1}
        - SELect:RF_AVErage?
        ```

    Info:
        - ``OFF`` or 0 turns the RF Average trace display off.
        - ``ON`` or 1 turns it on.
    """


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


class SelectMath(SCPICmdWrite, SCPICmdRead):
    """The ``SELect:MATH`` command.

    Description:
        - Turns on and off the display of the math waveform. The query returns whether the math
          waveform is on or off but does not indicate whether it is the selected waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:MATH?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:MATH?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:MATH value`` command.

    SCPI Syntax:
        ```
        - SELect:MATH {ON|OFF|<NR1>}
        - SELect:MATH?
        ```

    Info:
        - ``ON`` turns on the display of the specified waveform. This waveform also becomes the
          selected waveform.
        - ``OFF`` turns off the display of the specified waveform.
        - ``<NR1>`` = 0 turns off the display of the specified waveform; any other value turns on
          the display of the specified waveform.
    """


class SelectDall(SCPICmdWrite):
    """The ``SELect:DAll`` command.

    Description:
        - This command turns on or off all digital channels (D0 - D15).

    Usage:
        - Using the ``.write(value)`` method will send the ``SELect:DAll value`` command.

    SCPI Syntax:
        ```
        - SELect:DAll {ON|OFF|0|1}
        ```
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
        - This command selects a waveform to be used with channel-related commands such as the
          cursor commands. In addition to selecting the waveform, it turns on the display of the
          waveform, if it wasn't on already.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:CONTROl?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:CONTROl?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:CONTROl value`` command.

    SCPI Syntax:
        ```
        - SELect:CONTROl {CH<x>|MATH|REF<x>|BUS<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe|RF_NORMal|RF_AVErage|RF_MAXHold|RF_MINHold}
        - SELect:CONTROl?
        ```

    Info:
        - ``CH<x>`` specifies a channel waveform as the waveform affected by the front-panel
          controls.
        - ``MATH`` specifies the math waveform as the waveform that is affected by the front-panel
          controls.
        - ``BUS<x>`` specifies a bus waveform as the waveform affected by the front-panel controls.
        - ``D<x>`` specifies a digital waveform as the waveform affected by the front-panel
          controls. (Requires option 3-MSO.).
        - ``RF_NORMal`` specify an RF trace as the waveform affected by the front-panel controls.
        - ``RF_AVErage`` specify an RF trace as the waveform affected by the front-panel controls.
        - ``RF_MAXHold`` specify an RF trace as the waveform affected by the front-panel controls.
        - ``RF_MINHold`` specify an RF trace as the waveform affected by the front-panel controls.
    """  # noqa: E501


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


class SelectBusItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``SELect:BUS<x>`` command.

    Description:
        - This command turns on and off the display of the waveform for <x>, where x is the bus
          number 1-2. The query returns whether the channel is on or off but does not indicate
          whether it is the specified waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:BUS<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:BUS<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:BUS<x> value`` command.

    SCPI Syntax:
        ```
        - SELect:BUS<x> {OFF|ON|0|1}
        - SELect:BUS<x>?
        ```

    Info:
        - ``ON`` or 1 turns the specified waveform display on.
        - ``OFF`` or 0 turns the specified waveform display off.
    """


class SelectBItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``SELect:B<x>`` command.

    Description:
        - This command turns on and off the display of the waveform for <x>, where x is the bus
          number 1-2. The query returns whether the channel is on or off but does not indicate
          whether it is the specified waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:B<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:B<x> value`` command.

    SCPI Syntax:
        ```
        - SELect:B<x> {OFF|ON|0|1}
        - SELect:B<x>?
        ```

    Info:
        - ``ON`` or 1 turns the specified waveform display on.
        - ``OFF`` or 0 turns the specified waveform display off.
    """


#  pylint: disable=too-many-instance-attributes
class Select(SCPICmdRead):
    """The ``SELect`` command.

    Description:
        - Queries which waveforms are displayed.

    Usage:
        - Using the ``.query()`` method will send the ``SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SELect?
        ```

    Properties:
        - ``.ch``: The ``SELect:CH<x>`` command.
        - ``.control``: The ``SELect:CONTROl`` command.
        - ``.d``: The ``SELect:D<x>`` command.
        - ``.dall``: The ``SELect:DAll`` command.
        - ``.ref``: The ``SELect:REF<x>`` command.
        - ``.rf_average``: The ``SELect:RF_AVErage`` command.
        - ``.rf_maxhold``: The ``SELect:RF_MAXHold`` command.
        - ``.rf_minhold``: The ``SELect:RF_MINHold`` command.
        - ``.rf_normal``: The ``SELect:RF_NORMal`` command.
        - ``.bus``: The ``SELect:BUS<x>`` command.
        - ``.b``: The ``SELect:B<x>`` command.
        - ``.math``: The ``SELect:MATH`` command.
        - ``.math1``: The ``SELect:MATH1`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SELect") -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SelectChannel] = DefaultDictPassKeyToFactory(
            lambda x: SelectChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._control = SelectControl(device, f"{self._cmd_syntax}:CONTROl")
        self._d: Dict[int, SelectDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: SelectDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )
        self._dall = SelectDall(device, f"{self._cmd_syntax}:DAll")
        self._ref: Dict[int, SelectRefItem] = DefaultDictPassKeyToFactory(
            lambda x: SelectRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )
        self._rf_average = SelectRfAverage(device, f"{self._cmd_syntax}:RF_AVErage")
        self._rf_maxhold = SelectRfMaxhold(device, f"{self._cmd_syntax}:RF_MAXHold")
        self._rf_minhold = SelectRfMinhold(device, f"{self._cmd_syntax}:RF_MINHold")
        self._rf_normal = SelectRfNormal(device, f"{self._cmd_syntax}:RF_NORMal")
        self._bus: Dict[int, SelectBusItem] = DefaultDictPassKeyToFactory(
            lambda x: SelectBusItem(device, f"{self._cmd_syntax}:BUS{x}")
        )
        self._b: Dict[int, SelectBItem] = DefaultDictPassKeyToFactory(
            lambda x: SelectBItem(device, f"{self._cmd_syntax}:B{x}")
        )
        self._math = SelectMath(device, f"{self._cmd_syntax}:MATH")
        self._math1 = SelectMath1(device, f"{self._cmd_syntax}:MATH1")

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
    def control(self) -> SelectControl:
        """Return the ``SELect:CONTROl`` command.

        Description:
            - This command selects a waveform to be used with channel-related commands such as the
              cursor commands. In addition to selecting the waveform, it turns on the display of the
              waveform, if it wasn't on already.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:CONTROl?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:CONTROl?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:CONTROl value`` command.

        SCPI Syntax:
            ```
            - SELect:CONTROl {CH<x>|MATH|REF<x>|BUS<x>|D<x>|RF_AMPlitude|RF_FREQuency|RF_PHASe|RF_NORMal|RF_AVErage|RF_MAXHold|RF_MINHold}
            - SELect:CONTROl?
            ```

        Info:
            - ``CH<x>`` specifies a channel waveform as the waveform affected by the front-panel
              controls.
            - ``MATH`` specifies the math waveform as the waveform that is affected by the
              front-panel controls.
            - ``BUS<x>`` specifies a bus waveform as the waveform affected by the front-panel
              controls.
            - ``D<x>`` specifies a digital waveform as the waveform affected by the front-panel
              controls. (Requires option 3-MSO.).
            - ``RF_NORMal`` specify an RF trace as the waveform affected by the front-panel
              controls.
            - ``RF_AVErage`` specify an RF trace as the waveform affected by the front-panel
              controls.
            - ``RF_MAXHold`` specify an RF trace as the waveform affected by the front-panel
              controls.
            - ``RF_MINHold`` specify an RF trace as the waveform affected by the front-panel
              controls.
        """  # noqa: E501
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
    def dall(self) -> SelectDall:
        """Return the ``SELect:DAll`` command.

        Description:
            - This command turns on or off all digital channels (D0 - D15).

        Usage:
            - Using the ``.write(value)`` method will send the ``SELect:DAll value`` command.

        SCPI Syntax:
            ```
            - SELect:DAll {ON|OFF|0|1}
            ```
        """
        return self._dall

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

    @property
    def rf_average(self) -> SelectRfAverage:
        """Return the ``SELect:RF_AVErage`` command.

        Description:
            - This command switches the RF Average trace display on or off in the frequency domain
              graticule.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:RF_AVErage?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:RF_AVErage?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:RF_AVErage value`` command.

        SCPI Syntax:
            ```
            - SELect:RF_AVErage {OFF|ON|0|1}
            - SELect:RF_AVErage?
            ```

        Info:
            - ``OFF`` or 0 turns the RF Average trace display off.
            - ``ON`` or 1 turns it on.
        """
        return self._rf_average

    @property
    def rf_maxhold(self) -> SelectRfMaxhold:
        """Return the ``SELect:RF_MAXHold`` command.

        Description:
            - This command switches the frequency domain Max Hold trace display on or off in the
              frequency domain graticule.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:RF_MAXHold?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:RF_MAXHold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:RF_MAXHold value`` command.

        SCPI Syntax:
            ```
            - SELect:RF_MAXHold {OFF|ON|0|1}
            - SELect:RF_MAXHold?
            ```

        Info:
            - ``OFF`` or 0 turns the frequency domain Max Hold trace display off.
            - ``ON`` or 1 turns it on.
        """
        return self._rf_maxhold

    @property
    def rf_minhold(self) -> SelectRfMinhold:
        """Return the ``SELect:RF_MINHold`` command.

        Description:
            - This command switches the frequency domain Min Hold trace display on or off in the
              frequency domain graticule.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:RF_MINHold?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:RF_MINHold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:RF_MINHold value`` command.

        SCPI Syntax:
            ```
            - SELect:RF_MINHold {OFF|ON|0|1}
            - SELect:RF_MINHold?
            ```

        Info:
            - ``OFF`` or 0 turns the frequency domain Min Hold display off.
            - ``ON`` or 1 turns it on.
        """
        return self._rf_minhold

    @property
    def rf_normal(self) -> SelectRfNormal:
        """Return the ``SELect:RF_NORMal`` command.

        Description:
            - This command switches the frequency domain Normal trace display on or off in the
              frequency domain graticule.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:RF_NORMal?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:RF_NORMal?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:RF_NORMal value`` command.

        SCPI Syntax:
            ```
            - SELect:RF_NORMal {OFF|ON|0|1}
            - SELect:RF_NORMal?
            ```

        Info:
            - ``OFF`` or 0 turns the frequency domain Normal trace display off.
            - ``ON`` or 1 turns it on.
        """
        return self._rf_normal

    @property
    def bus(self) -> Dict[int, SelectBusItem]:
        """Return the ``SELect:BUS<x>`` command.

        Description:
            - This command turns on and off the display of the waveform for <x>, where x is the bus
              number 1-2. The query returns whether the channel is on or off but does not indicate
              whether it is the specified waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:BUS<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:BUS<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:BUS<x> value`` command.

        SCPI Syntax:
            ```
            - SELect:BUS<x> {OFF|ON|0|1}
            - SELect:BUS<x>?
            ```

        Info:
            - ``ON`` or 1 turns the specified waveform display on.
            - ``OFF`` or 0 turns the specified waveform display off.
        """
        return self._bus

    @property
    def b(self) -> Dict[int, SelectBItem]:
        """Return the ``SELect:B<x>`` command.

        Description:
            - This command turns on and off the display of the waveform for <x>, where x is the bus
              number 1-2. The query returns whether the channel is on or off but does not indicate
              whether it is the specified waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:B<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:B<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:B<x> value`` command.

        SCPI Syntax:
            ```
            - SELect:B<x> {OFF|ON|0|1}
            - SELect:B<x>?
            ```

        Info:
            - ``ON`` or 1 turns the specified waveform display on.
            - ``OFF`` or 0 turns the specified waveform display off.
        """
        return self._b

    @property
    def math(self) -> SelectMath:
        """Return the ``SELect:MATH`` command.

        Description:
            - Turns on and off the display of the math waveform. The query returns whether the math
              waveform is on or off but does not indicate whether it is the selected waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:MATH?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:MATH?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:MATH value`` command.

        SCPI Syntax:
            ```
            - SELect:MATH {ON|OFF|<NR1>}
            - SELect:MATH?
            ```

        Info:
            - ``ON`` turns on the display of the specified waveform. This waveform also becomes the
              selected waveform.
            - ``OFF`` turns off the display of the specified waveform.
            - ``<NR1>`` = 0 turns off the display of the specified waveform; any other value turns
              on the display of the specified waveform.
        """
        return self._math

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
