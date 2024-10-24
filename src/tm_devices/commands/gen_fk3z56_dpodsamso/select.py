"""The select commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SELect:B<x> {0|1|OFF|ON}
    - SELect:B<x>?
    - SELect:CH<x> {ON|OFF|<NR1>}
    - SELect:CH<x>?
    - SELect:CONTROl {CH<x>|MATH<x>|REF<x>}
    - SELect:CONTROl?
    - SELect:D<x> {ON|OFF|<NR1>}
    - SELect:D<x>?
    - SELect:DALL <NR1>
    - SELect:DIGTraces:COMbination <nr1>
    - SELect:DIGTraces:LISt <Dx>
    - SELect:DIGTraces:LISt?
    - SELect:MATH<x> {ON|OFF|<NR1>}
    - SELect:MATH<x>?
    - SELect:REF<x> {ON|OFF|<NR1>}
    - SELect:REF<x>?
    - SELect?
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
        - This command turns on the display of a specified waveform and also resets the acquisition.
          The query returns whether the channel is on or off but does not indicate whether it is the
          selected waveform. WFM can be a channel, math, or reference waveform.

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


class SelectMathItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``SELect:MATH<x>`` command.

    Description:
        - This command turns on the display of a specified waveform and also resets the acquisition.
          The query returns whether the channel is on or off but does not indicate whether it is the
          selected waveform. WFM can be a channel, math, or reference waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:MATH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:MATH<x> value`` command.

    SCPI Syntax:
        ```
        - SELect:MATH<x> {ON|OFF|<NR1>}
        - SELect:MATH<x>?
        ```

    Info:
        - ``ON`` turns on the display of the specified waveform. This waveform also becomes the
          selected waveform.
        - ``OFF`` turns off the display of the specified waveform.
        - ``<NR1>`` = 0 turns off the display of the specified waveform; any other value turns on
          the display of the specified waveform.
    """


class SelectDigtracesList(SCPICmdWrite, SCPICmdRead):
    """The ``SELect:DIGTraces:LISt`` command.

    Description:
        - This command turns on the specified digital channels or returns the list of digital
          channels that are on.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:DIGTraces:LISt?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:DIGTraces:LISt?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:DIGTraces:LISt value`` command.

    SCPI Syntax:
        ```
        - SELect:DIGTraces:LISt <Dx>
        - SELect:DIGTraces:LISt?
        ```
    """


class SelectDigtracesCombination(SCPICmdWrite):
    """The ``SELect:DIGTraces:COMbination`` command.

    Description:
        - This command turns on the digital channels that have binary digits as 1. The binary digits
          are obtained from the set decimal value.

    Usage:
        - Using the ``.write(value)`` method will send the ``SELect:DIGTraces:COMbination value``
          command.

    SCPI Syntax:
        ```
        - SELect:DIGTraces:COMbination <nr1>
        ```

    Info:
        - ``nr1`` is a decimal integer.
    """


class SelectDigtraces(SCPICmdRead):
    """The ``SELect:DIGTraces`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:DIGTraces?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:DIGTraces?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.combination``: The ``SELect:DIGTraces:COMbination`` command.
        - ``.list``: The ``SELect:DIGTraces:LISt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._combination = SelectDigtracesCombination(device, f"{self._cmd_syntax}:COMbination")
        self._list = SelectDigtracesList(device, f"{self._cmd_syntax}:LISt")

    @property
    def combination(self) -> SelectDigtracesCombination:
        """Return the ``SELect:DIGTraces:COMbination`` command.

        Description:
            - This command turns on the digital channels that have binary digits as 1. The binary
              digits are obtained from the set decimal value.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``SELect:DIGTraces:COMbination value`` command.

        SCPI Syntax:
            ```
            - SELect:DIGTraces:COMbination <nr1>
            ```

        Info:
            - ``nr1`` is a decimal integer.
        """
        return self._combination

    @property
    def list(self) -> SelectDigtracesList:
        """Return the ``SELect:DIGTraces:LISt`` command.

        Description:
            - This command turns on the specified digital channels or returns the list of digital
              channels that are on.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:DIGTraces:LISt?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:DIGTraces:LISt?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:DIGTraces:LISt value``
              command.

        SCPI Syntax:
            ```
            - SELect:DIGTraces:LISt <Dx>
            - SELect:DIGTraces:LISt?
            ```
        """
        return self._list


class SelectDall(SCPICmdWrite):
    """The ``SELect:DALL`` command.

    Description:
        - This command sets the displayed state of all the digital inputs.

    Usage:
        - Using the ``.write(value)`` method will send the ``SELect:DALL value`` command.

    SCPI Syntax:
        ```
        - SELect:DALL <NR1>
        ```

    Info:
        - ``<NR1> = 0`` turns off the display of all the digital inputs; any other value turns on
          the display of all the digital inputs.
        - ``OFF`` turns off the display of all the digital inputs.
        - ``ON`` displays all the digital inputs.
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
        - <wfm> This command sets or queries the waveform that is selected as the implied recipient
          of channel-related commands that support legacy-style programs. The command form also
          performs the equivalent of a ``SELECT:WFM ON`` command. This command is equivalent to
          selecting Measurement Setup from the Measure menu and either viewing or setting the Source
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:CONTROl?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:CONTROl?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:CONTROl value`` command.

    SCPI Syntax:
        ```
        - SELect:CONTROl {CH<x>|MATH<x>|REF<x>}
        - SELect:CONTROl?
        ```

    Info:
        - ``CH<x>`` selects the specified channel waveform as the waveform that is affected by the
          front panel controls. The x variable can be expressed as an integer ranging from 1 through
          4.
        - ``MATH<x>`` selects the specified math waveform as the waveform that is affected by the
          front panel controls. The x variable can be expressed as an integer ranging from 1 through
          4.
        - ``REF<x>`` selects the specified reference waveform as the waveform that is affected by
          the front panel controls. The x variable can be expressed as an integer ranging from 1
          through 4.
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


class SelectBItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``SELect:B<x>`` command.

    Description:
        - This command sets or queries the display state for the bus specified by x. The value of x
          can range from 1 through 16.

    Usage:
        - Using the ``.query()`` method will send the ``SELect:B<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:B<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:B<x> value`` command.

    SCPI Syntax:
        ```
        - SELect:B<x> {0|1|OFF|ON}
        - SELect:B<x>?
        ```

    Info:
        - ``0`` turns off the display of the specified bus; any other value turns on the display of
          the specified bus.
        - ``1`` turns on the display of the specified bus.
        - ``OFF`` turns off the display of the indicated bus.
        - ``ON`` turns on the display of the indicated bus.
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
        - ``.b``: The ``SELect:B<x>`` command.
        - ``.ch``: The ``SELect:CH<x>`` command.
        - ``.control``: The ``SELect:CONTROl`` command.
        - ``.d``: The ``SELect:D<x>`` command.
        - ``.dall``: The ``SELect:DALL`` command.
        - ``.digtraces``: The ``SELect:DIGTraces`` command tree.
        - ``.math``: The ``SELect:MATH<x>`` command.
        - ``.ref``: The ``SELect:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SELect") -> None:
        super().__init__(device, cmd_syntax)
        self._b: Dict[int, SelectBItem] = DefaultDictPassKeyToFactory(
            lambda x: SelectBItem(device, f"{self._cmd_syntax}:B{x}")
        )
        self._control = SelectControl(device, f"{self._cmd_syntax}:CONTROl")
        self._dall = SelectDall(device, f"{self._cmd_syntax}:DALL")
        self._digtraces = SelectDigtraces(device, f"{self._cmd_syntax}:DIGTraces")
        self._ch: Dict[int, SelectChannel] = DefaultDictPassKeyToFactory(
            lambda x: SelectChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._math: Dict[int, SelectMathItem] = DefaultDictPassKeyToFactory(
            lambda x: SelectMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )
        self._ref: Dict[int, SelectRefItem] = DefaultDictPassKeyToFactory(
            lambda x: SelectRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )
        self._d: Dict[int, SelectDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: SelectDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def b(self) -> Dict[int, SelectBItem]:
        """Return the ``SELect:B<x>`` command.

        Description:
            - This command sets or queries the display state for the bus specified by x. The value
              of x can range from 1 through 16.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:B<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:B<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:B<x> value`` command.

        SCPI Syntax:
            ```
            - SELect:B<x> {0|1|OFF|ON}
            - SELect:B<x>?
            ```

        Info:
            - ``0`` turns off the display of the specified bus; any other value turns on the display
              of the specified bus.
            - ``1`` turns on the display of the specified bus.
            - ``OFF`` turns off the display of the indicated bus.
            - ``ON`` turns on the display of the indicated bus.
        """
        return self._b

    @property
    def control(self) -> SelectControl:
        """Return the ``SELect:CONTROl`` command.

        Description:
            - <wfm> This command sets or queries the waveform that is selected as the implied
              recipient of channel-related commands that support legacy-style programs. The command
              form also performs the equivalent of a ``SELECT:WFM ON`` command. This command is
              equivalent to selecting Measurement Setup from the Measure menu and either viewing or
              setting the Source waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:CONTROl?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:CONTROl?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:CONTROl value`` command.

        SCPI Syntax:
            ```
            - SELect:CONTROl {CH<x>|MATH<x>|REF<x>}
            - SELect:CONTROl?
            ```

        Info:
            - ``CH<x>`` selects the specified channel waveform as the waveform that is affected by
              the front panel controls. The x variable can be expressed as an integer ranging from 1
              through 4.
            - ``MATH<x>`` selects the specified math waveform as the waveform that is affected by
              the front panel controls. The x variable can be expressed as an integer ranging from 1
              through 4.
            - ``REF<x>`` selects the specified reference waveform as the waveform that is affected
              by the front panel controls. The x variable can be expressed as an integer ranging
              from 1 through 4.
        """
        return self._control

    @property
    def dall(self) -> SelectDall:
        """Return the ``SELect:DALL`` command.

        Description:
            - This command sets the displayed state of all the digital inputs.

        Usage:
            - Using the ``.write(value)`` method will send the ``SELect:DALL value`` command.

        SCPI Syntax:
            ```
            - SELect:DALL <NR1>
            ```

        Info:
            - ``<NR1> = 0`` turns off the display of all the digital inputs; any other value turns
              on the display of all the digital inputs.
            - ``OFF`` turns off the display of all the digital inputs.
            - ``ON`` displays all the digital inputs.
        """
        return self._dall

    @property
    def digtraces(self) -> SelectDigtraces:
        """Return the ``SELect:DIGTraces`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:DIGTraces?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:DIGTraces?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.combination``: The ``SELect:DIGTraces:COMbination`` command.
            - ``.list``: The ``SELect:DIGTraces:LISt`` command.
        """
        return self._digtraces

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
    def math(self) -> Dict[int, SelectMathItem]:
        """Return the ``SELect:MATH<x>`` command.

        Description:
            - This command turns on the display of a specified waveform and also resets the
              acquisition. The query returns whether the channel is on or off but does not indicate
              whether it is the selected waveform. WFM can be a channel, math, or reference
              waveform.

        Usage:
            - Using the ``.query()`` method will send the ``SELect:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:MATH<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:MATH<x> value`` command.

        SCPI Syntax:
            ```
            - SELect:MATH<x> {ON|OFF|<NR1>}
            - SELect:MATH<x>?
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
    def ref(self) -> Dict[int, SelectRefItem]:
        """Return the ``SELect:REF<x>`` command.

        Description:
            - This command turns on the display of a specified waveform and also resets the
              acquisition. The query returns whether the channel is on or off but does not indicate
              whether it is the selected waveform. WFM can be a channel, math, or reference
              waveform.

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
