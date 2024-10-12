"""The horizontal commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HORizontal:ACQDURATION?
    - HORizontal:ACQLENGTH?
    - HORizontal:DIGital:MAGnivu:POSition?
    - HORizontal:DIGital:RECOrdlength:MAGnivu?
    - HORizontal:DIGital:RECOrdlength:MAIn?
    - HORizontal:DIGital:RECOrdlength?
    - HORizontal:DIGital:SAMPLERate:MAGnivu?
    - HORizontal:DIGital:SAMPLERate:MAIn?
    - HORizontal:DIGital:SAMPLERate?
    - HORizontal:DIVisions?
    - HORizontal:FASTframe:COUNt <NR1>
    - HORizontal:FASTframe:COUNt?
    - HORizontal:FASTframe:FRAMELock {ON|OFF|<NR1>}
    - HORizontal:FASTframe:FRAMELock?
    - HORizontal:FASTframe:LENgth <NR1>
    - HORizontal:FASTframe:LENgth?
    - HORizontal:FASTframe:MAXFRames?
    - HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x> <NR1>
    - HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x>?
    - HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x> <NR1>
    - HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x>?
    - HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x> <NR1>
    - HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x>?
    - HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x> <NR1>
    - HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x>?
    - HORizontal:FASTframe:MULtipleframes:MODe {OFF|OVERlay|ONLYOVERlay}
    - HORizontal:FASTframe:MULtipleframes:MODe?
    - HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x> <NR1>
    - HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x>?
    - HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x> <NR1>
    - HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x>?
    - HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x> <NR1>
    - HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x>?
    - HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x> <NR1>
    - HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x>?
    - HORizontal:FASTframe:REF:FRAme <NR1>
    - HORizontal:FASTframe:REF:FRAme?
    - HORizontal:FASTframe:REF:SOUrce <wfm>
    - HORizontal:FASTframe:REF:SOUrce?
    - HORizontal:FASTframe:SELECTED:CH<x> <NRF>
    - HORizontal:FASTframe:SELECTED:CH<x>?
    - HORizontal:FASTframe:SELECTED:MATH<x> <NRF>
    - HORizontal:FASTframe:SELECTED:MATH<x>?
    - HORizontal:FASTframe:SELECTED:REF<x> <NRF>
    - HORizontal:FASTframe:SELECTED:REF<x>?
    - HORizontal:FASTframe:SELECTED:SOUrce <NR1>
    - HORizontal:FASTframe:SELECTED:SOUrce?
    - HORizontal:FASTframe:SEQuence {FIRst|LAST}
    - HORizontal:FASTframe:SEQuence?
    - HORizontal:FASTframe:SINGLEFramemath {ON|OFF|<NR1>}
    - HORizontal:FASTframe:SINGLEFramemath?
    - HORizontal:FASTframe:SIXteenbit {ON|OFF|<NR1>}
    - HORizontal:FASTframe:SIXteenbit?
    - HORizontal:FASTframe:STATE {ON|OFF|<NR1>}
    - HORizontal:FASTframe:STATE?
    - HORizontal:FASTframe:SUMFrame {NONe|AVErage|ENVelope}
    - HORizontal:FASTframe:SUMFrame?
    - HORizontal:FASTframe:TIMEStamp:ALL:CH<x>? <NR1>, <NR1>
    - HORizontal:FASTframe:TIMEStamp:ALL:D<x>? <NR1>, <NR1>
    - HORizontal:FASTframe:TIMEStamp:ALL:MATH<x>? <NR1>, <NR1>
    - HORizontal:FASTframe:TIMEStamp:ALL:REF<x>? <NR1>, <NR1>
    - HORizontal:FASTframe:TIMEStamp:BETWeen:CH<x>? <NR1>, <NR1>
    - HORizontal:FASTframe:TIMEStamp:BETWeen:D<x>? <NR1>, <NR1>
    - HORizontal:FASTframe:TIMEStamp:BETWeen:MATH<x>? <NR1>, <NR1>
    - HORizontal:FASTframe:TIMEStamp:BETWeen:REF<x>? <NR1>, <NR1>
    - HORizontal:FASTframe:TIMEStamp:DELTa:CH<x>?
    - HORizontal:FASTframe:TIMEStamp:DELTa:D<x>?
    - HORizontal:FASTframe:TIMEStamp:DELTa:MATH<x>?
    - HORizontal:FASTframe:TIMEStamp:DELTa:REF<x>?
    - HORizontal:FASTframe:TIMEStamp:FRAMe:CH<x>? <NR1>
    - HORizontal:FASTframe:TIMEStamp:FRAMe:D<x>? <NR1>
    - HORizontal:FASTframe:TIMEStamp:FRAMe:MATH<x>? <NR1>
    - HORizontal:FASTframe:TIMEStamp:FRAMe:REF<x>? <NR1>
    - HORizontal:FASTframe:TIMEStamp:REF?
    - HORizontal:FASTframe:TIMEStamp:SELECTED:CH<x>?
    - HORizontal:FASTframe:TIMEStamp:SELECTED:D<x>?
    - HORizontal:FASTframe:TIMEStamp:SELECTED:MATH<x>?
    - HORizontal:FASTframe:TIMEStamp:SELECTED:REF<x>?
    - HORizontal:FASTframe:TRACk {LIVE|ALL}
    - HORizontal:FASTframe:TRACk?
    - HORizontal:FASTframe:XZEro:ALL:CH<x>? <NR1>,<NR1>
    - HORizontal:FASTframe:XZEro:ALL:REF<x>? <NR1>,<NR1>
    - HORizontal:FASTframe:XZEro:FRAme:CH<x>? <NR1>
    - HORizontal:FASTframe:XZEro:FRAme:REF<x>? <NR1>
    - HORizontal:FASTframe:XZEro:REF?
    - HORizontal:FASTframe:XZEro:SELECTED:CH<x>?
    - HORizontal:FASTframe:XZEro:SELECTED:REF<x>?
    - HORizontal:FASTframe?
    - HORizontal:MAIn:DELay:MODe {ON|OFF|<NR1>}
    - HORizontal:MAIn:DELay:MODe?
    - HORizontal:MAIn:DELay:POSition <NR3>
    - HORizontal:MAIn:DELay:POSition?
    - HORizontal:MAIn:DELay:TIMe <NR3>
    - HORizontal:MAIn:DELay:TIMe?
    - HORizontal:MAIn:INTERPRatio?
    - HORizontal:MAIn:SCAle
    - HORizontal:MAIn:SCAle?
    - HORizontal:MAIn:UNIts <QString>
    - HORizontal:MAIn:UNIts:STRing <QString>
    - HORizontal:MAIn:UNIts:STRing?
    - HORizontal:MAIn:UNIts?
    - HORizontal:MAIn?
    - HORizontal:MODE {AUTO|CONStant|MANual}
    - HORizontal:MODE:AUTO:LIMITrecordlen <NR1>
    - HORizontal:MODE:AUTO:LIMITrecordlen?
    - HORizontal:MODE:RECOrdlength <NR1>
    - HORizontal:MODE:RECOrdlength?
    - HORizontal:MODE:SAMPLERate <NR1>
    - HORizontal:MODE:SAMPLERate?
    - HORizontal:MODE:SCAle <NR1>
    - HORizontal:MODE:SCAle?
    - HORizontal:MODE?
    - HORizontal:POSition <NR3>
    - HORizontal:POSition?
    - HORizontal:ROLL {AUTO|OFF|ON}
    - HORizontal:ROLL?
    - HORizontal:TIMEStamp:CH<x>?
    - HORizontal:TIMEStamp:REF<x>?
    - HORizontal?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdReadWithArguments,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedChannel,
    ValidatedDigitalBit,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class HorizontalTimestampRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``HORizontal:TIMEStamp:REF<x>`` command.

    Description:
        - This query returns the horizontal timebase for the reference waveform. The reference is
          specified by x. The value of x can range from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:TIMEStamp:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:TIMEStamp:REF<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:TIMEStamp:REF<x>?
        ```
    """


class HorizontalTimestampChannel(ValidatedChannel, SCPICmdRead):
    """The ``HORizontal:TIMEStamp:CH<x>`` command.

    Description:
        - This query returns the horizontal timebase for the channel. The channel is specified by x.
          The value of x can range from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:TIMEStamp:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:TIMEStamp:CH<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:TIMEStamp:CH<x>?
        ```
    """


class HorizontalTimestamp(SCPICmdRead):
    """The ``HORizontal:TIMEStamp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:TIMEStamp?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:TIMEStamp?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:TIMEStamp:CH<x>`` command.
        - ``.ref``: The ``HORizontal:TIMEStamp:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalTimestampChannel] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalTimestampChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._ref: Dict[int, HorizontalTimestampRefItem] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalTimestampRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def ch(self) -> Dict[int, HorizontalTimestampChannel]:
        """Return the ``HORizontal:TIMEStamp:CH<x>`` command.

        Description:
            - This query returns the horizontal timebase for the channel. The channel is specified
              by x. The value of x can range from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:TIMEStamp:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:TIMEStamp:CH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:TIMEStamp:CH<x>?
            ```
        """
        return self._ch

    @property
    def ref(self) -> Dict[int, HorizontalTimestampRefItem]:
        """Return the ``HORizontal:TIMEStamp:REF<x>`` command.

        Description:
            - This query returns the horizontal timebase for the reference waveform. The reference
              is specified by x. The value of x can range from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:TIMEStamp:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:TIMEStamp:REF<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:TIMEStamp:REF<x>?
            ```
        """
        return self._ref


class HorizontalRoll(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:ROLL`` command.

    Description:
        - This command sets or queries the Roll Mode status. Use Roll Mode when you want to view
          data at very slow sweep speeds. It is useful for observing data samples on the screen as
          they occur. This command is equivalent to selecting Horizontal/Acquisition Setup from the
          Horiz/Acq menu, selecting the Acquisition tab, and setting the Roll Mode to Auto or Off.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:ROLL?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:ROLL?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:ROLL value`` command.

    SCPI Syntax:
        ```
        - HORizontal:ROLL {AUTO|OFF|ON}
        - HORizontal:ROLL?
        ```

    Info:
        - ``AUTO`` enables Roll Mode, if the time/division is set appropriately.
        - ``OFF`` disables Roll Mode.
        - ``ON`` enables Roll Mode, if the time/division is set appropriately.
    """


class HorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:POSition`` command.

    Description:
        - This command sets or queries the horizontal position as a percent of screen width. When
          Horizontal Delay Mode is turned off, this command is equivalent to adjusting the
          HORIZONTAL POSITION knob on the front panel. When Horizontal Delay Mode is turned on, the
          horizontal position is forced to 50%.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:POSition?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:POSition value`` command.

    SCPI Syntax:
        ```
        - HORizontal:POSition <NR3>
        - HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is from 0 to ≈100 and is the position of the trigger point on the screen (0 =
          left edge, 100 = right edge).
    """


class HorizontalModeScale(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODE:SCAle`` command.

    Description:
        - This command sets or queries the horizontal scale.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODE:SCAle value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MODE:SCAle <NR1>
        - HORizontal:MODE:SCAle?
        ```

    Info:
        - ``<NR1>`` is the horizontal scale in seconds per division.
    """


class HorizontalModeSamplerate(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODE:SAMPLERate`` command.

    Description:
        - This command sets or queries the sample rate.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE:SAMPLERate?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:SAMPLERate?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODE:SAMPLERate value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:MODE:SAMPLERate <NR1>
        - HORizontal:MODE:SAMPLERate?
        ```

    Info:
        - ``<NR1>`` is the sample rate in samples per second.
    """


class HorizontalModeRecordlength(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODE:RECOrdlength`` command.

    Description:
        - This command sets or queries the record length.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE:RECOrdlength?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:RECOrdlength?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODE:RECOrdlength value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:MODE:RECOrdlength <NR1>
        - HORizontal:MODE:RECOrdlength?
        ```

    Info:
        - ``<NR1>`` is the record length in samples. Manual mode lets you change the record length,
          while the record length is read only for Automatic mode.
    """


class HorizontalModeAutoLimitrecordlen(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODE:AUTO:LIMITrecordlen`` command.

    Description:
        - This command sets or queries the record length limit used by the auto horizontal mode.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE:AUTO:LIMITrecordlen?``
          query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:AUTO:LIMITrecordlen?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:MODE:AUTO:LIMITrecordlen value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MODE:AUTO:LIMITrecordlen <NR1>
        - HORizontal:MODE:AUTO:LIMITrecordlen?
        ```

    Info:
        - ``<NR1>`` is the record length limit in samples.
    """


class HorizontalModeAuto(SCPICmdRead):
    """The ``HORizontal:MODE:AUTO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE:AUTO?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:AUTO?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.limitrecordlen``: The ``HORizontal:MODE:AUTO:LIMITrecordlen`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._limitrecordlen = HorizontalModeAutoLimitrecordlen(
            device, f"{self._cmd_syntax}:LIMITrecordlen"
        )

    @property
    def limitrecordlen(self) -> HorizontalModeAutoLimitrecordlen:
        """Return the ``HORizontal:MODE:AUTO:LIMITrecordlen`` command.

        Description:
            - This command sets or queries the record length limit used by the auto horizontal mode.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE:AUTO:LIMITrecordlen?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:MODE:AUTO:LIMITrecordlen?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:MODE:AUTO:LIMITrecordlen value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MODE:AUTO:LIMITrecordlen <NR1>
            - HORizontal:MODE:AUTO:LIMITrecordlen?
            ```

        Info:
            - ``<NR1>`` is the record length limit in samples.
        """
        return self._limitrecordlen


class HorizontalMode(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODE`` command.

    Description:
        - This command set or queries the horizontal mode. Auto mode is the factory default.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODE value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MODE {AUTO|CONStant|MANual}
        - HORizontal:MODE?
        ```

    Info:
        - ``AUTO`` selects the automatic horizontal model. Auto mode attempts to keep record length
          constant as you change the time per division setting. Record length is read only.
        - ``CONSTANT`` selects the constant horizontal model. Constant mode attempts to keep sample
          rate constant as you change the time per division setting. Record length is read only.
        - ``MANUAL`` selects the manual horizontal model. Manual mode lets you change sample mode
          and record length. Time per division or Horizontal scale is read only.

    Properties:
        - ``.auto``: The ``HORizontal:MODE:AUTO`` command tree.
        - ``.recordlength``: The ``HORizontal:MODE:RECOrdlength`` command.
        - ``.samplerate``: The ``HORizontal:MODE:SAMPLERate`` command.
        - ``.scale``: The ``HORizontal:MODE:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._auto = HorizontalModeAuto(device, f"{self._cmd_syntax}:AUTO")
        self._recordlength = HorizontalModeRecordlength(device, f"{self._cmd_syntax}:RECOrdlength")
        self._samplerate = HorizontalModeSamplerate(device, f"{self._cmd_syntax}:SAMPLERate")
        self._scale = HorizontalModeScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def auto(self) -> HorizontalModeAuto:
        """Return the ``HORizontal:MODE:AUTO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE:AUTO?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:AUTO?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.limitrecordlen``: The ``HORizontal:MODE:AUTO:LIMITrecordlen`` command.
        """
        return self._auto

    @property
    def recordlength(self) -> HorizontalModeRecordlength:
        """Return the ``HORizontal:MODE:RECOrdlength`` command.

        Description:
            - This command sets or queries the record length.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE:RECOrdlength?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:RECOrdlength?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:MODE:RECOrdlength value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MODE:RECOrdlength <NR1>
            - HORizontal:MODE:RECOrdlength?
            ```

        Info:
            - ``<NR1>`` is the record length in samples. Manual mode lets you change the record
              length, while the record length is read only for Automatic mode.
        """
        return self._recordlength

    @property
    def samplerate(self) -> HorizontalModeSamplerate:
        """Return the ``HORizontal:MODE:SAMPLERate`` command.

        Description:
            - This command sets or queries the sample rate.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE:SAMPLERate?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:SAMPLERate?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MODE:SAMPLERate value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:MODE:SAMPLERate <NR1>
            - HORizontal:MODE:SAMPLERate?
            ```

        Info:
            - ``<NR1>`` is the sample rate in samples per second.
        """
        return self._samplerate

    @property
    def scale(self) -> HorizontalModeScale:
        """Return the ``HORizontal:MODE:SCAle`` command.

        Description:
            - This command sets or queries the horizontal scale.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:SCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MODE:SCAle value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:MODE:SCAle <NR1>
            - HORizontal:MODE:SCAle?
            ```

        Info:
            - ``<NR1>`` is the horizontal scale in seconds per division.
        """
        return self._scale


class HorizontalMainUnitsString(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MAIn:UNIts:STRing`` command.

    Description:
        - This command sets or queries the units string for the horizontal time base.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:UNIts:STRing?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:UNIts:STRing?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MAIn:UNIts:STRing value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:UNIts:STRing <QString>
        - HORizontal:MAIn:UNIts:STRing?
        ```

    Info:
        - ``<QString>`` is the time base units string.
    """

    _WRAP_ARG_WITH_QUOTES = True


class HorizontalMainUnits(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MAIn:UNIts`` command.

    Description:
        - This command sets or queries the units for the horizontal time base. It is equivalent to
          setting the ``HORizontal:MAIn:UNIts:STRing``.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:UNIts?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MAIn:UNIts value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:UNIts <QString>
        - HORizontal:MAIn:UNIts?
        ```

    Info:
        - ``<QString>`` is the time base units string.

    Properties:
        - ``.string``: The ``HORizontal:MAIn:UNIts:STRing`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._string = HorizontalMainUnitsString(device, f"{self._cmd_syntax}:STRing")

    @property
    def string(self) -> HorizontalMainUnitsString:
        """Return the ``HORizontal:MAIn:UNIts:STRing`` command.

        Description:
            - This command sets or queries the units string for the horizontal time base.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:UNIts:STRing?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:UNIts:STRing?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:MAIn:UNIts:STRing value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:UNIts:STRing <QString>
            - HORizontal:MAIn:UNIts:STRing?
            ```

        Info:
            - ``<QString>`` is the time base units string.
        """
        return self._string


class HorizontalMainScale(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``HORizontal:MAIn:SCAle`` command.

    Description:
        - This c

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``HORizontal:MAIn:SCAle`` command.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:SCAle
        - HORizontal:MAIn:SCAle?
        ```
    """


class HorizontalMainInterpratio(SCPICmdRead):
    """The ``HORizontal:MAIn:INTERPRatio`` command.

    Description:
        - This query-only command returns the Horizontal interpolation ratio.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:INTERPRatio?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:INTERPRatio?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:INTERPRatio?
        ```
    """


class HorizontalMainDelayTime(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MAIn:DELay:TIMe`` command.

    Description:
        - This command sets or queries the time base trigger delay time. This command is equivalent
          to selecting Position/Scale from the Horiz/Acq menu and choosing a value for Horiz Delay.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:DELay:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:DELay:TIMe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MAIn:DELay:TIMe value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:DELay:TIMe <NR3>
        - HORizontal:MAIn:DELay:TIMe?
        ```

    Info:
        - ``<NR3>`` specifies the time base trigger delay time setting, typically represented in
          seconds.
    """


class HorizontalMainDelayPosition(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MAIn:DELay:POSition`` command.

    Description:
        - This command sets or queries the time base position when Horizontal Delay Mode is turned
          on. This command is equivalent to selecting Horizontal/Acquisition Setup from the
          Horiz/Acq menu and then entering a Ref Point value.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:DELay:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:DELay:POSition?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MAIn:DELay:POSition value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:DELay:POSition <NR3>
        - HORizontal:MAIn:DELay:POSition?
        ```

    Info:
        - ``<NR3>`` is from 0 to ≈100 and is the percentage of the waveform that is displayed left
          of the center graticule.
    """


class HorizontalMainDelayMode(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MAIn:DELay:MODe`` command.

    Description:
        - This command sets or queries the time base trigger delay mode. This command is equivalent
          to choosing Delay Mode On from the Horiz/Acq menu.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:DELay:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:DELay:MODe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MAIn:DELay:MODe value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:DELay:MODe {ON|OFF|<NR1>}
        - HORizontal:MAIn:DELay:MODe?
        ```

    Info:
        - ``<NR1>`` = 0 disables the time base trigger delay mode, any other value enables the time
          base trigger delay mode.
        - ``ON`` enables the time base trigger delay mode.
        - ``OFF`` disables the time base trigger delay mode.
    """


class HorizontalMainDelay(SCPICmdRead):
    """The ``HORizontal:MAIn:DELay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:DELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``HORizontal:MAIn:DELay:MODe`` command.
        - ``.position``: The ``HORizontal:MAIn:DELay:POSition`` command.
        - ``.time``: The ``HORizontal:MAIn:DELay:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = HorizontalMainDelayMode(device, f"{self._cmd_syntax}:MODe")
        self._position = HorizontalMainDelayPosition(device, f"{self._cmd_syntax}:POSition")
        self._time = HorizontalMainDelayTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def mode(self) -> HorizontalMainDelayMode:
        """Return the ``HORizontal:MAIn:DELay:MODe`` command.

        Description:
            - This command sets or queries the time base trigger delay mode. This command is
              equivalent to choosing Delay Mode On from the Horiz/Acq menu.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:DELay:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:DELay:MODe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MAIn:DELay:MODe value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:DELay:MODe {ON|OFF|<NR1>}
            - HORizontal:MAIn:DELay:MODe?
            ```

        Info:
            - ``<NR1>`` = 0 disables the time base trigger delay mode, any other value enables the
              time base trigger delay mode.
            - ``ON`` enables the time base trigger delay mode.
            - ``OFF`` disables the time base trigger delay mode.
        """
        return self._mode

    @property
    def position(self) -> HorizontalMainDelayPosition:
        """Return the ``HORizontal:MAIn:DELay:POSition`` command.

        Description:
            - This command sets or queries the time base position when Horizontal Delay Mode is
              turned on. This command is equivalent to selecting Horizontal/Acquisition Setup from
              the Horiz/Acq menu and then entering a Ref Point value.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:DELay:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:DELay:POSition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:MAIn:DELay:POSition value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:DELay:POSition <NR3>
            - HORizontal:MAIn:DELay:POSition?
            ```

        Info:
            - ``<NR3>`` is from 0 to ≈100 and is the percentage of the waveform that is displayed
              left of the center graticule.
        """
        return self._position

    @property
    def time(self) -> HorizontalMainDelayTime:
        """Return the ``HORizontal:MAIn:DELay:TIMe`` command.

        Description:
            - This command sets or queries the time base trigger delay time. This command is
              equivalent to selecting Position/Scale from the Horiz/Acq menu and choosing a value
              for Horiz Delay.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:DELay:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:DELay:TIMe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MAIn:DELay:TIMe value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:DELay:TIMe <NR3>
            - HORizontal:MAIn:DELay:TIMe?
            ```

        Info:
            - ``<NR3>`` specifies the time base trigger delay time setting, typically represented in
              seconds.
        """
        return self._time


class HorizontalMain(SCPICmdRead):
    """The ``HORizontal:MAIn`` command.

    Description:
        - This query-only command returns the time per division of the time base. This command is
          equivalent to selecting Position/Scale from the Horiz/Acq menu.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:MAIn?
        ```

    Properties:
        - ``.interpratio``: The ``HORizontal:MAIn:INTERPRatio`` command.
        - ``.scale``: The ``HORizontal:MAIn:SCAle`` command.
        - ``.units``: The ``HORizontal:MAIn:UNIts`` command.
        - ``.delay``: The ``HORizontal:MAIn:DELay`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._interpratio = HorizontalMainInterpratio(device, f"{self._cmd_syntax}:INTERPRatio")
        self._scale = HorizontalMainScale(device, f"{self._cmd_syntax}:SCAle")
        self._units = HorizontalMainUnits(device, f"{self._cmd_syntax}:UNIts")
        self._delay = HorizontalMainDelay(device, f"{self._cmd_syntax}:DELay")

    @property
    def interpratio(self) -> HorizontalMainInterpratio:
        """Return the ``HORizontal:MAIn:INTERPRatio`` command.

        Description:
            - This query-only command returns the Horizontal interpolation ratio.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:INTERPRatio?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:INTERPRatio?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:INTERPRatio?
            ```
        """
        return self._interpratio

    @property
    def scale(self) -> HorizontalMainScale:
        """Return the ``HORizontal:MAIn:SCAle`` command.

        Description:
            - This c

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:SCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``HORizontal:MAIn:SCAle`` command.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:SCAle
            - HORizontal:MAIn:SCAle?
            ```
        """
        return self._scale

    @property
    def units(self) -> HorizontalMainUnits:
        """Return the ``HORizontal:MAIn:UNIts`` command.

        Description:
            - This command sets or queries the units for the horizontal time base. It is equivalent
              to setting the ``HORizontal:MAIn:UNIts:STRing``.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MAIn:UNIts value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:UNIts <QString>
            - HORizontal:MAIn:UNIts?
            ```

        Info:
            - ``<QString>`` is the time base units string.

        Sub-properties:
            - ``.string``: The ``HORizontal:MAIn:UNIts:STRing`` command.
        """
        return self._units

    @property
    def delay(self) -> HorizontalMainDelay:
        """Return the ``HORizontal:MAIn:DELay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:DELay?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``HORizontal:MAIn:DELay:MODe`` command.
            - ``.position``: The ``HORizontal:MAIn:DELay:POSition`` command.
            - ``.time``: The ``HORizontal:MAIn:DELay:TIMe`` command.
        """
        return self._delay


class HorizontalFastframeXzeroSelectedRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``HORizontal:FASTframe:XZEro:SELECTED:REF<x>`` command.

    Description:
        - This command sets or queries the time from the trigger to the trigger sample on the
          selected reference waveform. REF<x> can be REF1, REF2, REF3, or REF4.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:XZEro:SELECTED:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:XZEro:SELECTED:REF<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:XZEro:SELECTED:REF<x>?
        ```
    """


class HorizontalFastframeXzeroSelectedChannel(ValidatedChannel, SCPICmdRead):
    """The ``HORizontal:FASTframe:XZEro:SELECTED:CH<x>`` command.

    Description:
        - This command sets or queries the time from the trigger to the trigger sample on the
          selected channel. CH<x> can be CH1, CH2, CH3, or CH4.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:SELECTED:CH<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:XZEro:SELECTED:CH<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:XZEro:SELECTED:CH<x>?
        ```
    """


class HorizontalFastframeXzeroSelected(SCPICmdRead):
    """The ``HORizontal:FASTframe:XZEro:SELECTED`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:SELECTED?``
          query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro:SELECTED?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:FASTframe:XZEro:SELECTED:CH<x>`` command.
        - ``.ref``: The ``HORizontal:FASTframe:XZEro:SELECTED:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalFastframeXzeroSelectedChannel] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeXzeroSelectedChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._ref: Dict[int, HorizontalFastframeXzeroSelectedRefItem] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeXzeroSelectedRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def ch(self) -> Dict[int, HorizontalFastframeXzeroSelectedChannel]:
        """Return the ``HORizontal:FASTframe:XZEro:SELECTED:CH<x>`` command.

        Description:
            - This command sets or queries the time from the trigger to the trigger sample on the
              selected channel. CH<x> can be CH1, CH2, CH3, or CH4.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:XZEro:SELECTED:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:XZEro:SELECTED:CH<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:XZEro:SELECTED:CH<x>?
            ```
        """
        return self._ch

    @property
    def ref(self) -> Dict[int, HorizontalFastframeXzeroSelectedRefItem]:
        """Return the ``HORizontal:FASTframe:XZEro:SELECTED:REF<x>`` command.

        Description:
            - This command sets or queries the time from the trigger to the trigger sample on the
              selected reference waveform. REF<x> can be REF1, REF2, REF3, or REF4.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:XZEro:SELECTED:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:XZEro:SELECTED:REF<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:XZEro:SELECTED:REF<x>?
            ```
        """
        return self._ref


class HorizontalFastframeXzeroRef(SCPICmdRead):
    """The ``HORizontal:FASTframe:XZEro:REF`` command.

    Description:
        - This query-only command returns the sub-sample time between the trigger sample (designated
          by ``PT_OFF``) and the occurrence of the actual trigger for the waveform specified by the
          ``DATa:SOUrce`` command for the reference frame. This value is in units of
          ``WFMOutpre:XUNit``.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:REF?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro:REF?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:XZEro:REF?
        ```
    """


class HorizontalFastframeXzeroFrameRefItem(ValidatedDynamicNumberCmd, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:XZEro:FRAme:REF<x>`` command.

    Description:
        - This command queries the time from the trigger to the trigger sample of the specified
          frame on the specified reference.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:XZEro:FRAme:REF<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:XZEro:FRAme:REF<x>? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:XZEro:FRAme:REF<x>? <NR1>
        ```

    Info:
        - ``<NR1>`` specifies a frame on the specified reference.
    """


class HorizontalFastframeXzeroFrameChannel(ValidatedChannel, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:XZEro:FRAme:CH<x>`` command.

    Description:
        - This command queries the time from the trigger to the trigger sample of the specified
          frame on the specified channel.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:XZEro:FRAme:CH<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:XZEro:FRAme:CH<x>? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:XZEro:FRAme:CH<x>? <NR1>
        ```

    Info:
        - ``<NR1>`` specifies a frame on the specified channel.
    """


class HorizontalFastframeXzeroFrame(SCPICmdRead):
    """The ``HORizontal:FASTframe:XZEro:FRAme`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:FRAme?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro:FRAme?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:FASTframe:XZEro:FRAme:CH<x>`` command.
        - ``.ref``: The ``HORizontal:FASTframe:XZEro:FRAme:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalFastframeXzeroFrameChannel] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeXzeroFrameChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._ref: Dict[int, HorizontalFastframeXzeroFrameRefItem] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeXzeroFrameRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def ch(self) -> Dict[int, HorizontalFastframeXzeroFrameChannel]:
        """Return the ``HORizontal:FASTframe:XZEro:FRAme:CH<x>`` command.

        Description:
            - This command queries the time from the trigger to the trigger sample of the specified
              frame on the specified channel.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:XZEro:FRAme:CH<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:XZEro:FRAme:CH<x>? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:XZEro:FRAme:CH<x>? <NR1>
            ```

        Info:
            - ``<NR1>`` specifies a frame on the specified channel.
        """
        return self._ch

    @property
    def ref(self) -> Dict[int, HorizontalFastframeXzeroFrameRefItem]:
        """Return the ``HORizontal:FASTframe:XZEro:FRAme:REF<x>`` command.

        Description:
            - This command queries the time from the trigger to the trigger sample of the specified
              frame on the specified reference.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:XZEro:FRAme:REF<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:XZEro:FRAme:REF<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:XZEro:FRAme:REF<x>? <NR1>
            ```

        Info:
            - ``<NR1>`` specifies a frame on the specified reference.
        """
        return self._ref


class HorizontalFastframeXzeroAllRefItem(ValidatedDynamicNumberCmd, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:XZEro:ALL:REF<x>`` command.

    Description:
        - This command queries the time from the trigger to the trigger sample of the specified
          frames on the specified reference.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:XZEro:ALL:REF<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:XZEro:ALL:REF<x>? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:XZEro:ALL:REF<x>? <NR1>,<NR1>
        ```

    Info:
        - ``<NR1>`` specifies the first and last frame of a range of frames.
    """


class HorizontalFastframeXzeroAllChannel(ValidatedChannel, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:XZEro:ALL:CH<x>`` command.

    Description:
        - This command queries the time from the trigger to the trigger sample of the specified
          frames on the specified channel.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:XZEro:ALL:CH<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:XZEro:ALL:CH<x>? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:XZEro:ALL:CH<x>? <NR1>,<NR1>
        ```

    Info:
        - ``<NR1>`` specifies the first and last frame of a range of frames.
    """


class HorizontalFastframeXzeroAll(SCPICmdRead):
    """The ``HORizontal:FASTframe:XZEro:ALL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:ALL?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro:ALL?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:FASTframe:XZEro:ALL:CH<x>`` command.
        - ``.ref``: The ``HORizontal:FASTframe:XZEro:ALL:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalFastframeXzeroAllChannel] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeXzeroAllChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._ref: Dict[int, HorizontalFastframeXzeroAllRefItem] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeXzeroAllRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def ch(self) -> Dict[int, HorizontalFastframeXzeroAllChannel]:
        """Return the ``HORizontal:FASTframe:XZEro:ALL:CH<x>`` command.

        Description:
            - This command queries the time from the trigger to the trigger sample of the specified
              frames on the specified channel.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:XZEro:ALL:CH<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:XZEro:ALL:CH<x>? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:XZEro:ALL:CH<x>? <NR1>,<NR1>
            ```

        Info:
            - ``<NR1>`` specifies the first and last frame of a range of frames.
        """
        return self._ch

    @property
    def ref(self) -> Dict[int, HorizontalFastframeXzeroAllRefItem]:
        """Return the ``HORizontal:FASTframe:XZEro:ALL:REF<x>`` command.

        Description:
            - This command queries the time from the trigger to the trigger sample of the specified
              frames on the specified reference.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:XZEro:ALL:REF<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:XZEro:ALL:REF<x>? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:XZEro:ALL:REF<x>? <NR1>,<NR1>
            ```

        Info:
            - ``<NR1>`` specifies the first and last frame of a range of frames.
        """
        return self._ref


class HorizontalFastframeXzero(SCPICmdRead):
    """The ``HORizontal:FASTframe:XZEro`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.all``: The ``HORizontal:FASTframe:XZEro:ALL`` command tree.
        - ``.frame``: The ``HORizontal:FASTframe:XZEro:FRAme`` command tree.
        - ``.ref``: The ``HORizontal:FASTframe:XZEro:REF`` command.
        - ``.selected``: The ``HORizontal:FASTframe:XZEro:SELECTED`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._all = HorizontalFastframeXzeroAll(device, f"{self._cmd_syntax}:ALL")
        self._frame = HorizontalFastframeXzeroFrame(device, f"{self._cmd_syntax}:FRAme")
        self._ref = HorizontalFastframeXzeroRef(device, f"{self._cmd_syntax}:REF")
        self._selected = HorizontalFastframeXzeroSelected(device, f"{self._cmd_syntax}:SELECTED")

    @property
    def all(self) -> HorizontalFastframeXzeroAll:
        """Return the ``HORizontal:FASTframe:XZEro:ALL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:ALL?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro:ALL?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:FASTframe:XZEro:ALL:CH<x>`` command.
            - ``.ref``: The ``HORizontal:FASTframe:XZEro:ALL:REF<x>`` command.
        """
        return self._all

    @property
    def frame(self) -> HorizontalFastframeXzeroFrame:
        """Return the ``HORizontal:FASTframe:XZEro:FRAme`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:FRAme?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:XZEro:FRAme?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:FASTframe:XZEro:FRAme:CH<x>`` command.
            - ``.ref``: The ``HORizontal:FASTframe:XZEro:FRAme:REF<x>`` command.
        """
        return self._frame

    @property
    def ref(self) -> HorizontalFastframeXzeroRef:
        """Return the ``HORizontal:FASTframe:XZEro:REF`` command.

        Description:
            - This query-only command returns the sub-sample time between the trigger sample
              (designated by ``PT_OFF``) and the occurrence of the actual trigger for the waveform
              specified by the ``DATa:SOUrce`` command for the reference frame. This value is in
              units of ``WFMOutpre:XUNit``.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:REF?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro:REF?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:XZEro:REF?
            ```
        """
        return self._ref

    @property
    def selected(self) -> HorizontalFastframeXzeroSelected:
        """Return the ``HORizontal:FASTframe:XZEro:SELECTED`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:SELECTED?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:XZEro:SELECTED?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:FASTframe:XZEro:SELECTED:CH<x>`` command.
            - ``.ref``: The ``HORizontal:FASTframe:XZEro:SELECTED:REF<x>`` command.
        """
        return self._selected


class HorizontalFastframeTrack(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:TRACk`` command.

    Description:
        - This command sets up or queries the state of FastFrame tracking feature. This command is
          equivalent to selecting FastFrame Setup from the Horiz/Acq menu and then clicking the
          desired Frame Tracking state. When FastFrame Track is set to 'live', the channel and math
          waveforms are locked together. Adjusting a channel waveform also adjusts a related math
          waveform. All reference waveforms are also locked together but they are separate from
          channel and math waveforms. For example, when you set the Selected Frame Source Ch1 to
          Frame 3, then Selected Frame Ch2, Ch3, Ch4, Math1, Math2, Math3 and Math4 are also set to
          Frame 3. When you set the Selected Frame Source Ref1 to Frame 2, then Selected Frame Ref2,
          Ref3 and Ref4 are also set to Frame 2. If the Frame Tracking is set to Live, changing
          Selected Frame Ch1 will not affect the Selected Frame Ref1 frame of the Reference Frame
          setting. When FastFrame Track is set to 'all', the channel, math and reference waveforms
          are locked together. Adjusting a channel waveform also adjusts the related math and
          reference waveforms. For example, when you set the Selected Frame Source Ch1 to Frame 3,
          then Selected Frame Ch2, Ch3, Ch4, Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3 and Ref4
          are also set to Frame 3.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TRACk?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:TRACk?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:TRACk value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TRACk {LIVE|ALL}
        - HORizontal:FASTframe:TRACk?
        ```

    Info:
        - ``LIVE`` sets FastFrame Track to Live.
        - ``ALL`` sets FastFrame Track to All.
    """


class HorizontalFastframeTimestampSelectedRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:SELECTED:REF<x>`` command.

    Description:
        - This query-only command returns the absolute trigger date and time for the FastFrame
          Selected, within the specified waveform. Valid waveforms include CH<x>, MATH<x> and
          REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The format
          of the output is as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day,
          month, and year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions
          of a second to picoseconds

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:SELECTED:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:SELECTED:REF<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:SELECTED:REF<x>?
        ```
    """


class HorizontalFastframeTimestampSelectedMathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:SELECTED:MATH<x>`` command.

    Description:
        - This query-only command returns the absolute trigger date and time for the FastFrame
          Selected, within the specified waveform. Valid waveforms include CH<x>, MATH<x> and
          REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The format
          of the output is as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day,
          month, and year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions
          of a second to picoseconds

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:SELECTED:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:SELECTED:MATH<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:SELECTED:MATH<x>?
        ```
    """


class HorizontalFastframeTimestampSelectedDigitalBit(ValidatedDigitalBit, SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:SELECTED:D<x>`` command.

    Description:
        - This query-only command returns the absolute trigger date and time for the FastFrame
          Selected, within the specified waveform. Valid waveforms include CH<x>, MATH<x> and
          REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The format
          of the output is as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day,
          month, and year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions
          of a second to picoseconds

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:SELECTED:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:SELECTED:D<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:SELECTED:D<x>?
        ```
    """


class HorizontalFastframeTimestampSelectedChannel(ValidatedChannel, SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:SELECTED:CH<x>`` command.

    Description:
        - This query-only command returns the absolute trigger date and time for the FastFrame
          Selected, within the specified waveform. Valid waveforms include CH<x>, MATH<x> and
          REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The format
          of the output is as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day,
          month, and year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions
          of a second to picoseconds

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:SELECTED:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:SELECTED:CH<x>?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:SELECTED:CH<x>?
        ```
    """


class HorizontalFastframeTimestampSelected(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:SELECTED`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:SELECTED?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:SELECTED?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED:CH<x>`` command.
        - ``.math``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED:MATH<x>`` command.
        - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED:REF<x>`` command.
        - ``.d``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalFastframeTimestampSelectedChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampSelectedChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._math: Dict[int, HorizontalFastframeTimestampSelectedMathItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampSelectedMathItem(
                    device, f"{self._cmd_syntax}:MATH{x}"
                )
            )
        )
        self._ref: Dict[int, HorizontalFastframeTimestampSelectedRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampSelectedRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )
        self._d: Dict[int, HorizontalFastframeTimestampSelectedDigitalBit] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampSelectedDigitalBit(
                    device, f"{self._cmd_syntax}:D{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, HorizontalFastframeTimestampSelectedChannel]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:SELECTED:CH<x>`` command.

        Description:
            - This query-only command returns the absolute trigger date and time for the FastFrame
              Selected, within the specified waveform. Valid waveforms include CH<x>, MATH<x> and
              REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The
              format of the output is as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON
              YYYY is day, month, and year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx
              xxx is fractions of a second to picoseconds

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED:CH<x>?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:SELECTED:CH<x>?
            ```
        """
        return self._ch

    @property
    def math(self) -> Dict[int, HorizontalFastframeTimestampSelectedMathItem]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:SELECTED:MATH<x>`` command.

        Description:
            - This query-only command returns the absolute trigger date and time for the FastFrame
              Selected, within the specified waveform. Valid waveforms include CH<x>, MATH<x> and
              REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The
              format of the output is as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON
              YYYY is day, month, and year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx
              xxx is fractions of a second to picoseconds

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED:MATH<x>?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:SELECTED:MATH<x>?
            ```
        """
        return self._math

    @property
    def ref(self) -> Dict[int, HorizontalFastframeTimestampSelectedRefItem]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:SELECTED:REF<x>`` command.

        Description:
            - This query-only command returns the absolute trigger date and time for the FastFrame
              Selected, within the specified waveform. Valid waveforms include CH<x>, MATH<x> and
              REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The
              format of the output is as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON
              YYYY is day, month, and year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx
              xxx is fractions of a second to picoseconds

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED:REF<x>?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:SELECTED:REF<x>?
            ```
        """
        return self._ref

    @property
    def d(self) -> Dict[int, HorizontalFastframeTimestampSelectedDigitalBit]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:SELECTED:D<x>`` command.

        Description:
            - This query-only command returns the absolute trigger date and time for the FastFrame
              Selected, within the specified waveform. Valid waveforms include CH<x>, MATH<x> and
              REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The
              format of the output is as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON
              YYYY is day, month, and year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx
              xxx is fractions of a second to picoseconds

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED:D<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:SELECTED:D<x>?
            ```
        """
        return self._d


class HorizontalFastframeTimestampRef(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:REF`` command.

    Description:
        - This query-only command returns the absolute trigger date and time for FastFrame
          reference. The format of the output is as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx
          xxx DD MON YYYY is day, month, and year ``HH:MM:SS`` is hours, minutes, and seconds .xxx
          xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:REF?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:TIMEStamp:REF?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:REF?
        ```
    """


class HorizontalFastframeTimestampFrameRefItem(ValidatedDynamicNumberCmd, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:TIMEStamp:FRAMe:REF<x>`` command.

    Description:
        - This query-only command returns the absolute trigger date and time for the specified frame
          and waveform. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be
          expressed as an integer ranging from 1 through 4. The format of the output is as follows:
          DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year ``HH:MM:SS``
          is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:FRAMe:REF<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:FRAMe:REF<x>? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:FRAMe:REF<x>? <NR1>
        ```
    """


class HorizontalFastframeTimestampFrameMathItem(
    ValidatedDynamicNumberCmd, SCPICmdReadWithArguments
):
    """The ``HORizontal:FASTframe:TIMEStamp:FRAMe:MATH<x>`` command.

    Description:
        - This query-only command returns the absolute trigger date and time for the specified frame
          and waveform. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be
          expressed as an integer ranging from 1 through 4. The format of the output is as follows:
          DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year ``HH:MM:SS``
          is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:FRAMe:MATH<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:FRAMe:MATH<x>? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:FRAMe:MATH<x>? <NR1>
        ```
    """


class HorizontalFastframeTimestampFrameDigitalBit(ValidatedDigitalBit, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:TIMEStamp:FRAMe:D<x>`` command.

    Description:
        - This query-only command returns the absolute trigger date and time for the specified frame
          and waveform. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be
          expressed as an integer ranging from 1 through 4. The format of the output is as follows:
          DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year ``HH:MM:SS``
          is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:FRAMe:D<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:FRAMe:D<x>? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:FRAMe:D<x>? <NR1>
        ```
    """


class HorizontalFastframeTimestampFrameChannel(ValidatedChannel, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:TIMEStamp:FRAMe:CH<x>`` command.

    Description:
        - This query-only command returns the absolute trigger date and time for the specified frame
          and waveform. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be
          expressed as an integer ranging from 1 through 4. The format of the output is as follows:
          DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year ``HH:MM:SS``
          is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:FRAMe:CH<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:FRAMe:CH<x>? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:FRAMe:CH<x>? <NR1>
        ```
    """


class HorizontalFastframeTimestampFrame(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:FRAMe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:FRAMe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:FRAMe?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:FASTframe:TIMEStamp:FRAMe:CH<x>`` command.
        - ``.math``: The ``HORizontal:FASTframe:TIMEStamp:FRAMe:MATH<x>`` command.
        - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:FRAMe:REF<x>`` command.
        - ``.d``: The ``HORizontal:FASTframe:TIMEStamp:FRAMe:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalFastframeTimestampFrameChannel] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeTimestampFrameChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._math: Dict[int, HorizontalFastframeTimestampFrameMathItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampFrameMathItem(
                    device, f"{self._cmd_syntax}:MATH{x}"
                )
            )
        )
        self._ref: Dict[int, HorizontalFastframeTimestampFrameRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampFrameRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )
        self._d: Dict[int, HorizontalFastframeTimestampFrameDigitalBit] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampFrameDigitalBit(
                    device, f"{self._cmd_syntax}:D{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, HorizontalFastframeTimestampFrameChannel]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:FRAMe:CH<x>`` command.

        Description:
            - This query-only command returns the absolute trigger date and time for the specified
              frame and waveform. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable
              can be expressed as an integer ranging from 1 through 4. The format of the output is
              as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and
              year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a
              second to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:FRAMe:CH<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:FRAMe:CH<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:FRAMe:CH<x>? <NR1>
            ```
        """
        return self._ch

    @property
    def math(self) -> Dict[int, HorizontalFastframeTimestampFrameMathItem]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:FRAMe:MATH<x>`` command.

        Description:
            - This query-only command returns the absolute trigger date and time for the specified
              frame and waveform. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable
              can be expressed as an integer ranging from 1 through 4. The format of the output is
              as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and
              year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a
              second to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:FRAMe:MATH<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:FRAMe:MATH<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:FRAMe:MATH<x>? <NR1>
            ```
        """
        return self._math

    @property
    def ref(self) -> Dict[int, HorizontalFastframeTimestampFrameRefItem]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:FRAMe:REF<x>`` command.

        Description:
            - This query-only command returns the absolute trigger date and time for the specified
              frame and waveform. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable
              can be expressed as an integer ranging from 1 through 4. The format of the output is
              as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and
              year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a
              second to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:FRAMe:REF<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:FRAMe:REF<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:FRAMe:REF<x>? <NR1>
            ```
        """
        return self._ref

    @property
    def d(self) -> Dict[int, HorizontalFastframeTimestampFrameDigitalBit]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:FRAMe:D<x>`` command.

        Description:
            - This query-only command returns the absolute trigger date and time for the specified
              frame and waveform. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable
              can be expressed as an integer ranging from 1 through 4. The format of the output is
              as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and
              year ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a
              second to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:FRAMe:D<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:FRAMe:D<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:FRAMe:D<x>? <NR1>
            ```
        """
        return self._d


class HorizontalFastframeTimestampDeltaRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:DELTa:REF<x>`` command.

    Description:
        - This query-only command returns the relative time between the triggers of the FastFrame
          Selected and the FastFrame Reference, within the specified waveform. Valid waveforms
          include CH<x>, MATH<x>, and REF<x>. The x variable can be expressed as an integer ranging
          from 1 through 4. The format of the output is as follows: ``HH:MM:SS``.xxx xxx xxx xxx
          ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to
          picoseconds

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:DELTa:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:DELTa:REF<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:DELTa:REF<x>?
        ```
    """


class HorizontalFastframeTimestampDeltaMathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:DELTa:MATH<x>`` command.

    Description:
        - This query-only command returns the relative time between the triggers of the FastFrame
          Selected and the FastFrame Reference, within the specified waveform. Valid waveforms
          include CH<x>, MATH<x>, and REF<x>. The x variable can be expressed as an integer ranging
          from 1 through 4. The format of the output is as follows: ``HH:MM:SS``.xxx xxx xxx xxx
          ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to
          picoseconds

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:DELTa:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:DELTa:MATH<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:DELTa:MATH<x>?
        ```
    """


class HorizontalFastframeTimestampDeltaDigitalBit(ValidatedDigitalBit, SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:DELTa:D<x>`` command.

    Description:
        - This query-only command returns the relative time between the triggers of the FastFrame
          Selected and the FastFrame Reference, within the specified waveform. Valid waveforms
          include CH<x>, MATH<x>, and REF<x>. The x variable can be expressed as an integer ranging
          from 1 through 4. The format of the output is as follows: ``HH:MM:SS``.xxx xxx xxx xxx
          ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to
          picoseconds

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:DELTa:D<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:DELTa:D<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:DELTa:D<x>?
        ```
    """


class HorizontalFastframeTimestampDeltaChannel(ValidatedChannel, SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:DELTa:CH<x>`` command.

    Description:
        - This query-only command returns the relative time between the triggers of the FastFrame
          Selected and the FastFrame Reference, within the specified waveform. Valid waveforms
          include CH<x>, MATH<x>, and REF<x>. The x variable can be expressed as an integer ranging
          from 1 through 4. The format of the output is as follows: ``HH:MM:SS``.xxx xxx xxx xxx
          ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to
          picoseconds

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:DELTa:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:DELTa:CH<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:DELTa:CH<x>?
        ```
    """


class HorizontalFastframeTimestampDelta(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:DELTa`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:DELTa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:DELTa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:FASTframe:TIMEStamp:DELTa:CH<x>`` command.
        - ``.math``: The ``HORizontal:FASTframe:TIMEStamp:DELTa:MATH<x>`` command.
        - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:DELTa:REF<x>`` command.
        - ``.d``: The ``HORizontal:FASTframe:TIMEStamp:DELTa:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalFastframeTimestampDeltaChannel] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeTimestampDeltaChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._math: Dict[int, HorizontalFastframeTimestampDeltaMathItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampDeltaMathItem(
                    device, f"{self._cmd_syntax}:MATH{x}"
                )
            )
        )
        self._ref: Dict[int, HorizontalFastframeTimestampDeltaRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampDeltaRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )
        self._d: Dict[int, HorizontalFastframeTimestampDeltaDigitalBit] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampDeltaDigitalBit(
                    device, f"{self._cmd_syntax}:D{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, HorizontalFastframeTimestampDeltaChannel]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:DELTa:CH<x>`` command.

        Description:
            - This query-only command returns the relative time between the triggers of the
              FastFrame Selected and the FastFrame Reference, within the specified waveform. Valid
              waveforms include CH<x>, MATH<x>, and REF<x>. The x variable can be expressed as an
              integer ranging from 1 through 4. The format of the output is as follows:
              ``HH:MM:SS``.xxx xxx xxx xxx ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx
              xxx is fractions of a second to picoseconds

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:DELTa:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:DELTa:CH<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:DELTa:CH<x>?
            ```
        """
        return self._ch

    @property
    def math(self) -> Dict[int, HorizontalFastframeTimestampDeltaMathItem]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:DELTa:MATH<x>`` command.

        Description:
            - This query-only command returns the relative time between the triggers of the
              FastFrame Selected and the FastFrame Reference, within the specified waveform. Valid
              waveforms include CH<x>, MATH<x>, and REF<x>. The x variable can be expressed as an
              integer ranging from 1 through 4. The format of the output is as follows:
              ``HH:MM:SS``.xxx xxx xxx xxx ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx
              xxx is fractions of a second to picoseconds

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:DELTa:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:DELTa:MATH<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:DELTa:MATH<x>?
            ```
        """
        return self._math

    @property
    def ref(self) -> Dict[int, HorizontalFastframeTimestampDeltaRefItem]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:DELTa:REF<x>`` command.

        Description:
            - This query-only command returns the relative time between the triggers of the
              FastFrame Selected and the FastFrame Reference, within the specified waveform. Valid
              waveforms include CH<x>, MATH<x>, and REF<x>. The x variable can be expressed as an
              integer ranging from 1 through 4. The format of the output is as follows:
              ``HH:MM:SS``.xxx xxx xxx xxx ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx
              xxx is fractions of a second to picoseconds

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:DELTa:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:DELTa:REF<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:DELTa:REF<x>?
            ```
        """
        return self._ref

    @property
    def d(self) -> Dict[int, HorizontalFastframeTimestampDeltaDigitalBit]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:DELTa:D<x>`` command.

        Description:
            - This query-only command returns the relative time between the triggers of the
              FastFrame Selected and the FastFrame Reference, within the specified waveform. Valid
              waveforms include CH<x>, MATH<x>, and REF<x>. The x variable can be expressed as an
              integer ranging from 1 through 4. The format of the output is as follows:
              ``HH:MM:SS``.xxx xxx xxx xxx ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx
              xxx is fractions of a second to picoseconds

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:DELTa:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:DELTa:D<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:DELTa:D<x>?
            ```
        """
        return self._d


class HorizontalFastframeTimestampBetweenRefItem(
    ValidatedDynamicNumberCmd, SCPICmdReadWithArguments
):
    """The ``HORizontal:FASTframe:TIMEStamp:BETWeen:REF<x>`` command.

    Description:
        - This query-only command returns the relative trigger for the delta time between the
          specified frames, within the specified waveform. Valid waveforms include CH<x>, MATH<x>
          and REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The
          format of the delta time output is as follows: ``HH:MM:SS``.xxx xxx xxx xxx ``HH:MM:SS``
          is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:BETWeen:REF<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:BETWeen:REF<x>? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:BETWeen:REF<x>? <NR1>, <NR1>
        ```
    """


class HorizontalFastframeTimestampBetweenMathItem(
    ValidatedDynamicNumberCmd, SCPICmdReadWithArguments
):
    """The ``HORizontal:FASTframe:TIMEStamp:BETWeen:MATH<x>`` command.

    Description:
        - This query-only command returns the relative trigger for the delta time between the
          specified frames, within the specified waveform. Valid waveforms include CH<x>, MATH<x>
          and REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The
          format of the delta time output is as follows: ``HH:MM:SS``.xxx xxx xxx xxx ``HH:MM:SS``
          is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:BETWeen:MATH<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:BETWeen:MATH<x>? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:BETWeen:MATH<x>? <NR1>, <NR1>
        ```
    """


class HorizontalFastframeTimestampBetweenDigitalBit(ValidatedDigitalBit, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:TIMEStamp:BETWeen:D<x>`` command.

    Description:
        - This query-only command returns the relative trigger for the delta time between the
          specified frames, within the specified waveform. Valid waveforms include CH<x>, MATH<x>
          and REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The
          format of the delta time output is as follows: ``HH:MM:SS``.xxx xxx xxx xxx ``HH:MM:SS``
          is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:BETWeen:D<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:BETWeen:D<x>? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:BETWeen:D<x>? <NR1>, <NR1>
        ```
    """


class HorizontalFastframeTimestampBetweenChannel(ValidatedChannel, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:TIMEStamp:BETWeen:CH<x>`` command.

    Description:
        - This query-only command returns the relative trigger for the delta time between the
          specified frames, within the specified waveform. Valid waveforms include CH<x>, MATH<x>
          and REF<x>. The x variable can be expressed as an integer ranging from 1 through 4. The
          format of the delta time output is as follows: ``HH:MM:SS``.xxx xxx xxx xxx ``HH:MM:SS``
          is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:BETWeen:CH<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:BETWeen:CH<x>? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:BETWeen:CH<x>? <NR1>, <NR1>
        ```
    """


class HorizontalFastframeTimestampBetween(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:BETWeen`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:BETWeen?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:BETWeen?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:FASTframe:TIMEStamp:BETWeen:CH<x>`` command.
        - ``.math``: The ``HORizontal:FASTframe:TIMEStamp:BETWeen:MATH<x>`` command.
        - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:BETWeen:REF<x>`` command.
        - ``.d``: The ``HORizontal:FASTframe:TIMEStamp:BETWeen:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalFastframeTimestampBetweenChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampBetweenChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._math: Dict[int, HorizontalFastframeTimestampBetweenMathItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampBetweenMathItem(
                    device, f"{self._cmd_syntax}:MATH{x}"
                )
            )
        )
        self._ref: Dict[int, HorizontalFastframeTimestampBetweenRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampBetweenRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )
        self._d: Dict[int, HorizontalFastframeTimestampBetweenDigitalBit] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampBetweenDigitalBit(
                    device, f"{self._cmd_syntax}:D{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, HorizontalFastframeTimestampBetweenChannel]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:BETWeen:CH<x>`` command.

        Description:
            - This query-only command returns the relative trigger for the delta time between the
              specified frames, within the specified waveform. Valid waveforms include CH<x>,
              MATH<x> and REF<x>. The x variable can be expressed as an integer ranging from 1
              through 4. The format of the delta time output is as follows: ``HH:MM:SS``.xxx xxx xxx
              xxx ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a
              second to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:BETWeen:CH<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:BETWeen:CH<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:BETWeen:CH<x>? <NR1>, <NR1>
            ```
        """
        return self._ch

    @property
    def math(self) -> Dict[int, HorizontalFastframeTimestampBetweenMathItem]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:BETWeen:MATH<x>`` command.

        Description:
            - This query-only command returns the relative trigger for the delta time between the
              specified frames, within the specified waveform. Valid waveforms include CH<x>,
              MATH<x> and REF<x>. The x variable can be expressed as an integer ranging from 1
              through 4. The format of the delta time output is as follows: ``HH:MM:SS``.xxx xxx xxx
              xxx ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a
              second to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:BETWeen:MATH<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:BETWeen:MATH<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:BETWeen:MATH<x>? <NR1>, <NR1>
            ```
        """
        return self._math

    @property
    def ref(self) -> Dict[int, HorizontalFastframeTimestampBetweenRefItem]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:BETWeen:REF<x>`` command.

        Description:
            - This query-only command returns the relative trigger for the delta time between the
              specified frames, within the specified waveform. Valid waveforms include CH<x>,
              MATH<x> and REF<x>. The x variable can be expressed as an integer ranging from 1
              through 4. The format of the delta time output is as follows: ``HH:MM:SS``.xxx xxx xxx
              xxx ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a
              second to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:BETWeen:REF<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:BETWeen:REF<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:BETWeen:REF<x>? <NR1>, <NR1>
            ```
        """
        return self._ref

    @property
    def d(self) -> Dict[int, HorizontalFastframeTimestampBetweenDigitalBit]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:BETWeen:D<x>`` command.

        Description:
            - This query-only command returns the relative trigger for the delta time between the
              specified frames, within the specified waveform. Valid waveforms include CH<x>,
              MATH<x> and REF<x>. The x variable can be expressed as an integer ranging from 1
              through 4. The format of the delta time output is as follows: ``HH:MM:SS``.xxx xxx xxx
              xxx ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a
              second to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:BETWeen:D<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:BETWeen:D<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:BETWeen:D<x>? <NR1>, <NR1>
            ```
        """
        return self._d


class HorizontalFastframeTimestampAllRefItem(ValidatedDynamicNumberCmd, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:TIMEStamp:ALL:REF<x>`` command.

    Description:
        - This query-only command returns the frame number and time stamp for each frame between
          requested frames, inclusive, within the specified waveform. Argument order is unimportant.
          Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be expressed as an
          integer ranging from 1 through 4. The format of the output is as follows: DD MON YYYY
          ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year ``HH:MM:SS`` is hours,
          minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:ALL:REF<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:ALL:REF<x>? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:ALL:REF<x>? <NR1>, <NR1>
        ```
    """


class HorizontalFastframeTimestampAllMathItem(ValidatedDynamicNumberCmd, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:TIMEStamp:ALL:MATH<x>`` command.

    Description:
        - This query-only command returns the frame number and time stamp for each frame between
          requested frames, inclusive, within the specified waveform. Argument order is unimportant.
          Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be expressed as an
          integer ranging from 1 through 4. The format of the output is as follows: DD MON YYYY
          ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year ``HH:MM:SS`` is hours,
          minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:ALL:MATH<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:ALL:MATH<x>? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:ALL:MATH<x>? <NR1>, <NR1>
        ```
    """


class HorizontalFastframeTimestampAllDigitalBit(ValidatedDigitalBit, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:TIMEStamp:ALL:D<x>`` command.

    Description:
        - This query-only command returns the frame number and time stamp for each frame between
          requested frames, inclusive, within the specified waveform. Argument order is unimportant.
          Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be expressed as an
          integer ranging from 1 through 4. The format of the output is as follows: DD MON YYYY
          ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year ``HH:MM:SS`` is hours,
          minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:ALL:D<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:ALL:D<x>? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:ALL:D<x>? <NR1>, <NR1>
        ```
    """


class HorizontalFastframeTimestampAllChannel(ValidatedChannel, SCPICmdReadWithArguments):
    """The ``HORizontal:FASTframe:TIMEStamp:ALL:CH<x>`` command.

    Description:
        - This query-only command returns the frame number and time stamp for each frame between
          requested frames, inclusive, within the specified waveform. Argument order is unimportant.
          Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be expressed as an
          integer ranging from 1 through 4. The format of the output is as follows: DD MON YYYY
          ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year ``HH:MM:SS`` is hours,
          minutes, and seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:ALL:CH<x>? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:ALL:CH<x>? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:ALL:CH<x>? <NR1>, <NR1>
        ```
    """


class HorizontalFastframeTimestampAll(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:ALL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:ALL?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:TIMEStamp:ALL?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:FASTframe:TIMEStamp:ALL:CH<x>`` command.
        - ``.math``: The ``HORizontal:FASTframe:TIMEStamp:ALL:MATH<x>`` command.
        - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:ALL:REF<x>`` command.
        - ``.d``: The ``HORizontal:FASTframe:TIMEStamp:ALL:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalFastframeTimestampAllChannel] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeTimestampAllChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._math: Dict[int, HorizontalFastframeTimestampAllMathItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeTimestampAllMathItem(
                    device, f"{self._cmd_syntax}:MATH{x}"
                )
            )
        )
        self._ref: Dict[int, HorizontalFastframeTimestampAllRefItem] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeTimestampAllRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )
        self._d: Dict[int, HorizontalFastframeTimestampAllDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeTimestampAllDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def ch(self) -> Dict[int, HorizontalFastframeTimestampAllChannel]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:ALL:CH<x>`` command.

        Description:
            - This query-only command returns the frame number and time stamp for each frame between
              requested frames, inclusive, within the specified waveform. Argument order is
              unimportant. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be
              expressed as an integer ranging from 1 through 4. The format of the output is as
              follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year
              ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second
              to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:ALL:CH<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:ALL:CH<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:ALL:CH<x>? <NR1>, <NR1>
            ```
        """
        return self._ch

    @property
    def math(self) -> Dict[int, HorizontalFastframeTimestampAllMathItem]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:ALL:MATH<x>`` command.

        Description:
            - This query-only command returns the frame number and time stamp for each frame between
              requested frames, inclusive, within the specified waveform. Argument order is
              unimportant. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be
              expressed as an integer ranging from 1 through 4. The format of the output is as
              follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year
              ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second
              to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:ALL:MATH<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:ALL:MATH<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:ALL:MATH<x>? <NR1>, <NR1>
            ```
        """
        return self._math

    @property
    def ref(self) -> Dict[int, HorizontalFastframeTimestampAllRefItem]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:ALL:REF<x>`` command.

        Description:
            - This query-only command returns the frame number and time stamp for each frame between
              requested frames, inclusive, within the specified waveform. Argument order is
              unimportant. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be
              expressed as an integer ranging from 1 through 4. The format of the output is as
              follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year
              ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second
              to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:ALL:REF<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:ALL:REF<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:ALL:REF<x>? <NR1>, <NR1>
            ```
        """
        return self._ref

    @property
    def d(self) -> Dict[int, HorizontalFastframeTimestampAllDigitalBit]:
        """Return the ``HORizontal:FASTframe:TIMEStamp:ALL:D<x>`` command.

        Description:
            - This query-only command returns the frame number and time stamp for each frame between
              requested frames, inclusive, within the specified waveform. Argument order is
              unimportant. Valid waveforms include CH<x>, MATH<x> and REF<x>. The x variable can be
              expressed as an integer ranging from 1 through 4. The format of the output is as
              follows: DD MON YYYY ``HH:MM:SS``.xxx xxx xxx xxx DD MON YYYY is day, month, and year
              ``HH:MM:SS`` is hours, minutes, and seconds .xxx xxx xxx xxx is fractions of a second
              to picoseconds

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:ALL:D<x>? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:ALL:D<x>? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:ALL:D<x>? <NR1>, <NR1>
            ```
        """
        return self._d


class HorizontalFastframeTimestamp(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:TIMEStamp?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.all``: The ``HORizontal:FASTframe:TIMEStamp:ALL`` command tree.
        - ``.between``: The ``HORizontal:FASTframe:TIMEStamp:BETWeen`` command tree.
        - ``.delta``: The ``HORizontal:FASTframe:TIMEStamp:DELTa`` command tree.
        - ``.frame``: The ``HORizontal:FASTframe:TIMEStamp:FRAMe`` command tree.
        - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:REF`` command.
        - ``.selected``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._all = HorizontalFastframeTimestampAll(device, f"{self._cmd_syntax}:ALL")
        self._between = HorizontalFastframeTimestampBetween(device, f"{self._cmd_syntax}:BETWeen")
        self._delta = HorizontalFastframeTimestampDelta(device, f"{self._cmd_syntax}:DELTa")
        self._frame = HorizontalFastframeTimestampFrame(device, f"{self._cmd_syntax}:FRAMe")
        self._ref = HorizontalFastframeTimestampRef(device, f"{self._cmd_syntax}:REF")
        self._selected = HorizontalFastframeTimestampSelected(
            device, f"{self._cmd_syntax}:SELECTED"
        )

    @property
    def all(self) -> HorizontalFastframeTimestampAll:
        """Return the ``HORizontal:FASTframe:TIMEStamp:ALL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:ALL?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:ALL?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:FASTframe:TIMEStamp:ALL:CH<x>`` command.
            - ``.math``: The ``HORizontal:FASTframe:TIMEStamp:ALL:MATH<x>`` command.
            - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:ALL:REF<x>`` command.
            - ``.d``: The ``HORizontal:FASTframe:TIMEStamp:ALL:D<x>`` command.
        """
        return self._all

    @property
    def between(self) -> HorizontalFastframeTimestampBetween:
        """Return the ``HORizontal:FASTframe:TIMEStamp:BETWeen`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:BETWeen?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:BETWeen?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:FASTframe:TIMEStamp:BETWeen:CH<x>`` command.
            - ``.math``: The ``HORizontal:FASTframe:TIMEStamp:BETWeen:MATH<x>`` command.
            - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:BETWeen:REF<x>`` command.
            - ``.d``: The ``HORizontal:FASTframe:TIMEStamp:BETWeen:D<x>`` command.
        """
        return self._between

    @property
    def delta(self) -> HorizontalFastframeTimestampDelta:
        """Return the ``HORizontal:FASTframe:TIMEStamp:DELTa`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:DELTa?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:DELTa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:FASTframe:TIMEStamp:DELTa:CH<x>`` command.
            - ``.math``: The ``HORizontal:FASTframe:TIMEStamp:DELTa:MATH<x>`` command.
            - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:DELTa:REF<x>`` command.
            - ``.d``: The ``HORizontal:FASTframe:TIMEStamp:DELTa:D<x>`` command.
        """
        return self._delta

    @property
    def frame(self) -> HorizontalFastframeTimestampFrame:
        """Return the ``HORizontal:FASTframe:TIMEStamp:FRAMe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:FRAMe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:FRAMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:FASTframe:TIMEStamp:FRAMe:CH<x>`` command.
            - ``.math``: The ``HORizontal:FASTframe:TIMEStamp:FRAMe:MATH<x>`` command.
            - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:FRAMe:REF<x>`` command.
            - ``.d``: The ``HORizontal:FASTframe:TIMEStamp:FRAMe:D<x>`` command.
        """
        return self._frame

    @property
    def ref(self) -> HorizontalFastframeTimestampRef:
        """Return the ``HORizontal:FASTframe:TIMEStamp:REF`` command.

        Description:
            - This query-only command returns the absolute trigger date and time for FastFrame
              reference. The format of the output is as follows: DD MON YYYY ``HH:MM:SS``.xxx xxx
              xxx xxx DD MON YYYY is day, month, and year ``HH:MM:SS`` is hours, minutes, and
              seconds .xxx xxx xxx xxx is fractions of a second to picoseconds

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:REF?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:REF?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:REF?
            ```
        """
        return self._ref

    @property
    def selected(self) -> HorizontalFastframeTimestampSelected:
        """Return the ``HORizontal:FASTframe:TIMEStamp:SELECTED`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED:CH<x>`` command.
            - ``.math``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED:MATH<x>`` command.
            - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED:REF<x>`` command.
            - ``.d``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED:D<x>`` command.
        """
        return self._selected


class HorizontalFastframeSumframe(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:SUMFrame`` command.

    Description:
        - This command sets or queries the summary frame mode. When ENVelope is selected, the last
          frame in a FastFrame acquisition is an envelope of all the prior frames in the
          acquisition. When AVErage is selected, the last frame is replaced with a frame that is the
          computed average of all the prior frames in the acquisition. For the summary frame control
          to be active, the number of frames must be two or greater.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SUMFrame?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SUMFrame?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:SUMFrame value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:SUMFrame {NONe|AVErage|ENVelope}
        - HORizontal:FASTframe:SUMFrame?
        ```

    Info:
        - ``NONE`` turns off the summary mode for FastFrame. This is the default setting.
        - ``AVErage`` argument displays the last frame in a FastFrame acquisition as a frame that is
          the computed average of all the prior frames in the acquisition.
        - ``ENVelope`` argument displays the last frame in a FastFrame acquisition as an envelope of
          all the prior frames in the acquisition.
    """


class HorizontalFastframeState(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:STATE`` command.

    Description:
        - This command sets or returns the state of FastFrame. Acquisition modes Envelope and
          Average are not compatible with FastFrame. If FastFrame is on, an attempted set to those
          acquisition modes will fail and revert to Sample mode. If FastFrame is turned on while in
          one of those acquisition modes, the acquisition mode is changed to Sample.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:STATE value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:STATE {ON|OFF|<NR1>}
        - HORizontal:FASTframe:STATE?
        ```

    Info:
        - ``ON`` indicates FastFrame is active.
        - ``OFF`` indicates that FastFrame is off.
        - ``<NR1>`` A 0 turns off FastFrame; any other value activates FastFrame.
    """


class HorizontalFastframeSixteenbit(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:SIXteenbit`` command.

    Description:
        - This command sets or queries FastFrame sixteen bit.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SIXteenbit?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SIXteenbit?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:SIXteenbit value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:SIXteenbit {ON|OFF|<NR1>}
        - HORizontal:FASTframe:SIXteenbit?
        ```

    Info:
        - ``<NR1>`` = 0 disables the function; any other value enables it.
        - ``OFF`` disables the function. When OFF, fastframe data is 8 bit.
        - ``ON`` enables the function. When ON and when the summary frame is average, the data for
          the averaged summary frame is 16 bit.
    """


class HorizontalFastframeSingleframemath(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:SINGLEFramemath`` command.

    Description:
        - This command sets or queries FastFrame single frame math.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SINGLEFramemath?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:SINGLEFramemath?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:SINGLEFramemath value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:SINGLEFramemath {ON|OFF|<NR1>}
        - HORizontal:FASTframe:SINGLEFramemath?
        ```

    Info:
        - ``<NR1>`` = 0 disables the function; any other value enables it.
        - ``OFF`` disables the function.
        - ``ON`` enables the function.
    """


class HorizontalFastframeSequence(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:SEQuence`` command.

    Description:
        - This command sets or queries the FastFrame single-sequence mode stop condition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SEQuence?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:SEQuence value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:SEQuence {FIRst|LAST}
        - HORizontal:FASTframe:SEQuence?
        ```

    Info:
        - ``FIRst`` sets single sequence to stop after n frames.
        - ``LAST`` sets single sequence to stop manually.
    """


class HorizontalFastframeSelectedSource(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:SELECTED:SOUrce`` command.

    Description:
        - This command sets or queries the FastFrame source waveform. This is equivalent to
          selecting FastFrame Setup from the Horiz/Acq menu, and then choosing the waveform source.
          Valid waveforms include CH<x> and MATH<x>. The x variable can be expressed as an integer
          ranging from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED:SOUrce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:SELECTED:SOUrce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:SELECTED:SOUrce value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:SELECTED:SOUrce <NR1>
        - HORizontal:FASTframe:SELECTED:SOUrce?
        ```

    Info:
        - ``<NR1>`` specifies the selected frame number on the specified waveform.
    """


class HorizontalFastframeSelectedRefItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:SELECTED:REF<x>`` command.

    Description:
        - This command sets or queries the FastFrame selected frame number on the specified
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED:REF<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:SELECTED:REF<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:SELECTED:REF<x> value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:SELECTED:REF<x> <NRF>
        - HORizontal:FASTframe:SELECTED:REF<x>?
        ```

    Info:
        - ``<NRF>`` is the selected frame number.
    """


class HorizontalFastframeSelectedMathItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:SELECTED:MATH<x>`` command.

    Description:
        - This command sets or queries the FastFrame selected frame number on the specified
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED:MATH<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:SELECTED:MATH<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:SELECTED:MATH<x> value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:SELECTED:MATH<x> <NRF>
        - HORizontal:FASTframe:SELECTED:MATH<x>?
        ```

    Info:
        - ``<NRF>`` is the selected frame number.
    """


class HorizontalFastframeSelectedChannel(ValidatedChannel, SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:SELECTED:CH<x>`` command.

    Description:
        - This command sets or queries the FastFrame selected frame number on the specified
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED:CH<x>?``
          query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SELECTED:CH<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:SELECTED:CH<x> value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:SELECTED:CH<x> <NRF>
        - HORizontal:FASTframe:SELECTED:CH<x>?
        ```

    Info:
        - ``<NRF>`` is the selected frame number.
    """


class HorizontalFastframeSelected(SCPICmdRead):
    """The ``HORizontal:FASTframe:SELECTED`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SELECTED?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:FASTframe:SELECTED:CH<x>`` command.
        - ``.math``: The ``HORizontal:FASTframe:SELECTED:MATH<x>`` command.
        - ``.ref``: The ``HORizontal:FASTframe:SELECTED:REF<x>`` command.
        - ``.source``: The ``HORizontal:FASTframe:SELECTED:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalFastframeSelectedChannel] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeSelectedChannel(device, f"{self._cmd_syntax}:CH{x}")
        )
        self._math: Dict[int, HorizontalFastframeSelectedMathItem] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeSelectedMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )
        self._ref: Dict[int, HorizontalFastframeSelectedRefItem] = DefaultDictPassKeyToFactory(
            lambda x: HorizontalFastframeSelectedRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )
        self._source = HorizontalFastframeSelectedSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def ch(self) -> Dict[int, HorizontalFastframeSelectedChannel]:
        """Return the ``HORizontal:FASTframe:SELECTED:CH<x>`` command.

        Description:
            - This command sets or queries the FastFrame selected frame number on the specified
              waveform.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED:CH<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:SELECTED:CH<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:SELECTED:CH<x> value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:SELECTED:CH<x> <NRF>
            - HORizontal:FASTframe:SELECTED:CH<x>?
            ```

        Info:
            - ``<NRF>`` is the selected frame number.
        """
        return self._ch

    @property
    def math(self) -> Dict[int, HorizontalFastframeSelectedMathItem]:
        """Return the ``HORizontal:FASTframe:SELECTED:MATH<x>`` command.

        Description:
            - This command sets or queries the FastFrame selected frame number on the specified
              waveform.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED:MATH<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:SELECTED:MATH<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:SELECTED:MATH<x> value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:SELECTED:MATH<x> <NRF>
            - HORizontal:FASTframe:SELECTED:MATH<x>?
            ```

        Info:
            - ``<NRF>`` is the selected frame number.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, HorizontalFastframeSelectedRefItem]:
        """Return the ``HORizontal:FASTframe:SELECTED:REF<x>`` command.

        Description:
            - This command sets or queries the FastFrame selected frame number on the specified
              waveform.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED:REF<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:SELECTED:REF<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:SELECTED:REF<x> value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:SELECTED:REF<x> <NRF>
            - HORizontal:FASTframe:SELECTED:REF<x>?
            ```

        Info:
            - ``<NRF>`` is the selected frame number.
        """
        return self._ref

    @property
    def source(self) -> HorizontalFastframeSelectedSource:
        """Return the ``HORizontal:FASTframe:SELECTED:SOUrce`` command.

        Description:
            - This command sets or queries the FastFrame source waveform. This is equivalent to
              selecting FastFrame Setup from the Horiz/Acq menu, and then choosing the waveform
              source. Valid waveforms include CH<x> and MATH<x>. The x variable can be expressed as
              an integer ranging from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:SELECTED:SOUrce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:SELECTED:SOUrce value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:SELECTED:SOUrce <NR1>
            - HORizontal:FASTframe:SELECTED:SOUrce?
            ```

        Info:
            - ``<NR1>`` specifies the selected frame number on the specified waveform.
        """
        return self._source


class HorizontalFastframeRefSource(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:REF:SOUrce`` command.

    Description:
        - This command sets or queries FastFrame Reference waveform source. This is equivalent to
          selecting FastFrame Setup from the Horiz/Acq menu and choosing the referenc e source.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:REF:SOUrce?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:REF:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:REF:SOUrce <wfm>
        - HORizontal:FASTframe:REF:SOUrce?
        ```

    Info:
        - ``<wfm>`` specifies the FastFrame Reference waveform source. Valid waveforms include CH<x>
          and MATH<x> The x variable can be expressed as an integer ranging from 1 through 4.
    """


class HorizontalFastframeRefFrame(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:REF:FRAme`` command.

    Description:
        - This command sets or returns the reference frame number.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF:FRAme?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:REF:FRAme?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:REF:FRAme value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:REF:FRAme <NR1>
        - HORizontal:FASTframe:REF:FRAme?
        ```

    Info:
        - ``<NR1>`` is the reference frame number.
    """


class HorizontalFastframeRef(SCPICmdRead):
    """The ``HORizontal:FASTframe:REF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:REF?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frame``: The ``HORizontal:FASTframe:REF:FRAme`` command.
        - ``.source``: The ``HORizontal:FASTframe:REF:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frame = HorizontalFastframeRefFrame(device, f"{self._cmd_syntax}:FRAme")
        self._source = HorizontalFastframeRefSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def frame(self) -> HorizontalFastframeRefFrame:
        """Return the ``HORizontal:FASTframe:REF:FRAme`` command.

        Description:
            - This command sets or returns the reference frame number.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF:FRAme?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:REF:FRAme?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:REF:FRAme value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:REF:FRAme <NR1>
            - HORizontal:FASTframe:REF:FRAme?
            ```

        Info:
            - ``<NR1>`` is the reference frame number.
        """
        return self._frame

    @property
    def source(self) -> HorizontalFastframeRefSource:
        """Return the ``HORizontal:FASTframe:REF:SOUrce`` command.

        Description:
            - This command sets or queries FastFrame Reference waveform source. This is equivalent
              to selecting FastFrame Setup from the Horiz/Acq menu and choosing the referenc e
              source.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF:SOUrce?``
              query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:REF:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:REF:SOUrce value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:REF:SOUrce <wfm>
            - HORizontal:FASTframe:REF:SOUrce?
            ```

        Info:
            - ``<wfm>`` specifies the FastFrame Reference waveform source. Valid waveforms include
              CH<x> and MATH<x> The x variable can be expressed as an integer ranging from 1 through
              4.
        """
        return self._source


class HorizontalFastframeMultipleframesNumframesRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x>`` command.

    Description:
        - This command sets or queries the number of frames on the specified waveform for the
          FastFrame multiple frames feature. The multiple frames feature supports displaying
          multiple frames in an overlaid manner. Valid waveforms include CH<x>, MATH<x> and REF<x>.
          The x variable can be expressed as an integer ranging from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x> value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x> <NR1>
        - HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x>?
        ```

    Info:
        - ``<NR1>`` represents the number of frames on the specified waveform.
    """


class HorizontalFastframeMultipleframesNumframesMathItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x>`` command.

    Description:
        - This command sets or queries the number of frames on the specified waveform for the
          FastFrame multiple frames feature. The multiple frames feature supports displaying
          multiple frames in an overlaid manner. Valid waveforms include CH<x>, MATH<x> and REF<x>.
          The x variable can be expressed as an integer ranging from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x> value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x> <NR1>
        - HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x>?
        ```

    Info:
        - ``<NR1>`` represents the number of frames on the specified waveform.
    """


class HorizontalFastframeMultipleframesNumframesDigitalBit(
    ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead
):
    """The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x>`` command.

    Description:
        - This command sets or queries the number of frames on the specified waveform for the
          FastFrame multiple frames feature. The multiple frames feature supports displaying
          multiple frames in an overlaid manner. Valid waveforms include CH<x>, MATH<x> and REF<x>.
          The x variable can be expressed as an integer ranging from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x>?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x> value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x> <NR1>
        - HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x>?
        ```

    Info:
        - ``<NR1>`` represents the number of frames on the specified waveform.
    """


class HorizontalFastframeMultipleframesNumframesChannel(
    ValidatedChannel, SCPICmdWrite, SCPICmdRead
):
    """The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x>`` command.

    Description:
        - This command sets or queries the number of frames on the specified waveform for the
          FastFrame multiple frames feature. The multiple frames feature supports displaying
          multiple frames in an overlaid manner. Valid waveforms include CH<x>, MATH<x> and REF<x>.
          The x variable can be expressed as an integer ranging from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x>?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x> value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x> <NR1>
        - HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x>?
        ```

    Info:
        - ``<NR1>`` represents the number of frames on the specified waveform.
    """


class HorizontalFastframeMultipleframesNumframes(SCPICmdRead):
    """The ``HORizontal:FASTframe:MULtipleframes:NUMFRames`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:NUMFRames?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x>`` command.
        - ``.math``: The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x>`` command.
        - ``.ref``: The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x>`` command.
        - ``.d``: The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalFastframeMultipleframesNumframesChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeMultipleframesNumframesChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._math: Dict[int, HorizontalFastframeMultipleframesNumframesMathItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeMultipleframesNumframesMathItem(
                    device, f"{self._cmd_syntax}:MATH{x}"
                )
            )
        )
        self._ref: Dict[int, HorizontalFastframeMultipleframesNumframesRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeMultipleframesNumframesRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )
        self._d: Dict[int, HorizontalFastframeMultipleframesNumframesDigitalBit] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeMultipleframesNumframesDigitalBit(
                    device, f"{self._cmd_syntax}:D{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, HorizontalFastframeMultipleframesNumframesChannel]:
        """Return the ``HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x>`` command.

        Description:
            - This command sets or queries the number of frames on the specified waveform for the
              FastFrame multiple frames feature. The multiple frames feature supports displaying
              multiple frames in an overlaid manner. Valid waveforms include CH<x>, MATH<x> and
              REF<x>. The x variable can be expressed as an integer ranging from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x> value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x> <NR1>
            - HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x>?
            ```

        Info:
            - ``<NR1>`` represents the number of frames on the specified waveform.
        """
        return self._ch

    @property
    def math(self) -> Dict[int, HorizontalFastframeMultipleframesNumframesMathItem]:
        """Return the ``HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x>`` command.

        Description:
            - This command sets or queries the number of frames on the specified waveform for the
              FastFrame multiple frames feature. The multiple frames feature supports displaying
              multiple frames in an overlaid manner. Valid waveforms include CH<x>, MATH<x> and
              REF<x>. The x variable can be expressed as an integer ranging from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x> value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x> <NR1>
            - HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x>?
            ```

        Info:
            - ``<NR1>`` represents the number of frames on the specified waveform.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, HorizontalFastframeMultipleframesNumframesRefItem]:
        """Return the ``HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x>`` command.

        Description:
            - This command sets or queries the number of frames on the specified waveform for the
              FastFrame multiple frames feature. The multiple frames feature supports displaying
              multiple frames in an overlaid manner. Valid waveforms include CH<x>, MATH<x> and
              REF<x>. The x variable can be expressed as an integer ranging from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x> value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x> <NR1>
            - HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x>?
            ```

        Info:
            - ``<NR1>`` represents the number of frames on the specified waveform.
        """
        return self._ref

    @property
    def d(self) -> Dict[int, HorizontalFastframeMultipleframesNumframesDigitalBit]:
        """Return the ``HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x>`` command.

        Description:
            - This command sets or queries the number of frames on the specified waveform for the
              FastFrame multiple frames feature. The multiple frames feature supports displaying
              multiple frames in an overlaid manner. Valid waveforms include CH<x>, MATH<x> and
              REF<x>. The x variable can be expressed as an integer ranging from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x> value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x> <NR1>
            - HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x>?
            ```

        Info:
            - ``<NR1>`` represents the number of frames on the specified waveform.
        """
        return self._d


class HorizontalFastframeMultipleframesMode(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:MULtipleframes:MODe`` command.

    Description:
        - This command sets or queries the mode for the FastFrame multiple frames feature. This
          feature displays multiple frames in an overlaid manner.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:MULtipleframes:MODe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:MODe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:MODe value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MULtipleframes:MODe {OFF|OVERlay|ONLYOVERlay}
        - HORizontal:FASTframe:MULtipleframes:MODe?
        ```

    Info:
        - ``OFF`` turns off the multiple frames mode.
        - ``OVERlay`` sets the multiple frames mode to overlay.
    """


class HorizontalFastframeMultipleframesFramestartRefItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x>`` command.

    Description:
        - This command sets or queries the start frame number on the specified waveform for the
          FastFrame multiple frames feature. Valid waveforms include CH<x>, MATH<x>, and REF<x>. The
          value of x can be an integer ranging from 1 through 4. The multiple frames feature
          supports displaying multiple frames in an overlaid manner.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x> value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x> <NR1>
        - HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x>?
        ```

    Info:
        - ``<NR1>`` specifies the start frame number on the specified waveform.
    """


class HorizontalFastframeMultipleframesFramestartMathItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x>`` command.

    Description:
        - This command sets or queries the start frame number on the specified waveform for the
          FastFrame multiple frames feature. Valid waveforms include CH<x>, MATH<x>, and REF<x>. The
          value of x can be an integer ranging from 1 through 4. The multiple frames feature
          supports displaying multiple frames in an overlaid manner.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x> value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x> <NR1>
        - HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x>?
        ```

    Info:
        - ``<NR1>`` specifies the start frame number on the specified waveform.
    """


class HorizontalFastframeMultipleframesFramestartDigitalBit(
    ValidatedDigitalBit, SCPICmdWrite, SCPICmdRead
):
    """The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x>`` command.

    Description:
        - This command sets or queries the start frame number on the specified waveform for the
          FastFrame multiple frames feature. Valid waveforms include CH<x>, MATH<x>, and REF<x>. The
          value of x can be an integer ranging from 1 through 4. The multiple frames feature
          supports displaying multiple frames in an overlaid manner.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x>?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x> value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x> <NR1>
        - HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x>?
        ```

    Info:
        - ``<NR1>`` specifies the start frame number on the specified waveform.
    """


class HorizontalFastframeMultipleframesFramestartChannel(
    ValidatedChannel, SCPICmdWrite, SCPICmdRead
):
    """The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x>`` command.

    Description:
        - This command sets or queries the start frame number on the specified waveform for the
          FastFrame multiple frames feature. Valid waveforms include CH<x>, MATH<x>, and REF<x>. The
          value of x can be an integer ranging from 1 through 4. The multiple frames feature
          supports displaying multiple frames in an overlaid manner.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x> value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x> <NR1>
        - HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x>?
        ```

    Info:
        - ``<NR1>`` specifies the start frame number on the specified waveform.
    """


class HorizontalFastframeMultipleframesFramestart(SCPICmdRead):
    """The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:FRAMESTart?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x>`` command.
        - ``.math``: The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x>`` command.
        - ``.ref``: The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x>`` command.
        - ``.d``: The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, HorizontalFastframeMultipleframesFramestartChannel] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeMultipleframesFramestartChannel(
                    device, f"{self._cmd_syntax}:CH{x}"
                )
            )
        )
        self._math: Dict[int, HorizontalFastframeMultipleframesFramestartMathItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeMultipleframesFramestartMathItem(
                    device, f"{self._cmd_syntax}:MATH{x}"
                )
            )
        )
        self._ref: Dict[int, HorizontalFastframeMultipleframesFramestartRefItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeMultipleframesFramestartRefItem(
                    device, f"{self._cmd_syntax}:REF{x}"
                )
            )
        )
        self._d: Dict[int, HorizontalFastframeMultipleframesFramestartDigitalBit] = (
            DefaultDictPassKeyToFactory(
                lambda x: HorizontalFastframeMultipleframesFramestartDigitalBit(
                    device, f"{self._cmd_syntax}:D{x}"
                )
            )
        )

    @property
    def ch(self) -> Dict[int, HorizontalFastframeMultipleframesFramestartChannel]:
        """Return the ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x>`` command.

        Description:
            - This command sets or queries the start frame number on the specified waveform for the
              FastFrame multiple frames feature. Valid waveforms include CH<x>, MATH<x>, and REF<x>.
              The value of x can be an integer ranging from 1 through 4. The multiple frames feature
              supports displaying multiple frames in an overlaid manner.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x> value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x> <NR1>
            - HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x>?
            ```

        Info:
            - ``<NR1>`` specifies the start frame number on the specified waveform.
        """
        return self._ch

    @property
    def math(self) -> Dict[int, HorizontalFastframeMultipleframesFramestartMathItem]:
        """Return the ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x>`` command.

        Description:
            - This command sets or queries the start frame number on the specified waveform for the
              FastFrame multiple frames feature. Valid waveforms include CH<x>, MATH<x>, and REF<x>.
              The value of x can be an integer ranging from 1 through 4. The multiple frames feature
              supports displaying multiple frames in an overlaid manner.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x> value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x> <NR1>
            - HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x>?
            ```

        Info:
            - ``<NR1>`` specifies the start frame number on the specified waveform.
        """
        return self._math

    @property
    def ref(self) -> Dict[int, HorizontalFastframeMultipleframesFramestartRefItem]:
        """Return the ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x>`` command.

        Description:
            - This command sets or queries the start frame number on the specified waveform for the
              FastFrame multiple frames feature. Valid waveforms include CH<x>, MATH<x>, and REF<x>.
              The value of x can be an integer ranging from 1 through 4. The multiple frames feature
              supports displaying multiple frames in an overlaid manner.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x> value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x> <NR1>
            - HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x>?
            ```

        Info:
            - ``<NR1>`` specifies the start frame number on the specified waveform.
        """
        return self._ref

    @property
    def d(self) -> Dict[int, HorizontalFastframeMultipleframesFramestartDigitalBit]:
        """Return the ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x>`` command.

        Description:
            - This command sets or queries the start frame number on the specified waveform for the
              FastFrame multiple frames feature. Valid waveforms include CH<x>, MATH<x>, and REF<x>.
              The value of x can be an integer ranging from 1 through 4. The multiple frames feature
              supports displaying multiple frames in an overlaid manner.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x> value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x> <NR1>
            - HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x>?
            ```

        Info:
            - ``<NR1>`` specifies the start frame number on the specified waveform.
        """
        return self._d


class HorizontalFastframeMultipleframes(SCPICmdRead):
    """The ``HORizontal:FASTframe:MULtipleframes`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:MULtipleframes?``
          query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:MULtipleframes?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.framestart``: The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart`` command tree.
        - ``.mode``: The ``HORizontal:FASTframe:MULtipleframes:MODe`` command.
        - ``.numframes``: The ``HORizontal:FASTframe:MULtipleframes:NUMFRames`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._framestart = HorizontalFastframeMultipleframesFramestart(
            device, f"{self._cmd_syntax}:FRAMESTart"
        )
        self._mode = HorizontalFastframeMultipleframesMode(device, f"{self._cmd_syntax}:MODe")
        self._numframes = HorizontalFastframeMultipleframesNumframes(
            device, f"{self._cmd_syntax}:NUMFRames"
        )

    @property
    def framestart(self) -> HorizontalFastframeMultipleframesFramestart:
        """Return the ``HORizontal:FASTframe:MULtipleframes:FRAMESTart`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:FRAMESTart?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:CH<x>`` command.
            - ``.math``: The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:MATH<x>`` command.
            - ``.ref``: The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:REF<x>`` command.
            - ``.d``: The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart:D<x>`` command.
        """
        return self._framestart

    @property
    def mode(self) -> HorizontalFastframeMultipleframesMode:
        """Return the ``HORizontal:FASTframe:MULtipleframes:MODe`` command.

        Description:
            - This command sets or queries the mode for the FastFrame multiple frames feature. This
              feature displays multiple frames in an overlaid manner.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:MODe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:MODe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:MODe value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MULtipleframes:MODe {OFF|OVERlay|ONLYOVERlay}
            - HORizontal:FASTframe:MULtipleframes:MODe?
            ```

        Info:
            - ``OFF`` turns off the multiple frames mode.
            - ``OVERlay`` sets the multiple frames mode to overlay.
        """
        return self._mode

    @property
    def numframes(self) -> HorizontalFastframeMultipleframesNumframes:
        """Return the ``HORizontal:FASTframe:MULtipleframes:NUMFRames`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:NUMFRames?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:CH<x>`` command.
            - ``.math``: The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:MATH<x>`` command.
            - ``.ref``: The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:REF<x>`` command.
            - ``.d``: The ``HORizontal:FASTframe:MULtipleframes:NUMFRames:D<x>`` command.
        """
        return self._numframes


class HorizontalFastframeMaxframes(SCPICmdRead):
    """The ``HORizontal:FASTframe:MAXFRames`` command.

    Description:
        - This query returns the maximum number of frames.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:MAXFRames?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:MAXFRames?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MAXFRames?
        ```
    """


class HorizontalFastframeLength(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:LENgth`` command.

    Description:
        - This command sets or queries the horizontal record length to the number of sample points
          in each frame. This command is equivalent to selecting FastFrame Setup from the Horiz/Acq
          menu and entering a value in the Rec Length box. FastFrame captures a series of triggered
          acquisitions with minimal intervening time between them.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:LENgth?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:LENgth?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:LENgth value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:LENgth <NR1>
        - HORizontal:FASTframe:LENgth?
        ```

    Info:
        - ``<NR1>`` represents the supported value for horizontal record length in Fast Frame mode.
          In addition, to the allowable record length in normal (single frame) mode, 50 and 250
          point record lengths are permitted in Fast Frame mode.
    """


class HorizontalFastframeFramelock(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:FRAMELock`` command.

    Description:
        - This command sets or queries FastFrame frame lock.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:FRAMELock?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:FRAMELock?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:FRAMELock value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:FRAMELock {ON|OFF|<NR1>}
        - HORizontal:FASTframe:FRAMELock?
        ```

    Info:
        - ``<ON>`` enables frame lock.
        - ``<OFF>`` disables frame lock.
        - ``<NR1>`` = 0 disables frame lock; any other value enables framelock.
    """


class HorizontalFastframeCount(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:COUNt`` command.

    Description:
        - This command sets or returns the number of frames.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:COUNt?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:COUNt value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:COUNt <NR1>
        - HORizontal:FASTframe:COUNt?
        ```

    Info:
        - ``<NR1>`` is the number of frames.
    """


#  pylint: disable=too-many-instance-attributes
class HorizontalFastframe(SCPICmdRead):
    """The ``HORizontal:FASTframe`` command.

    Description:
        - This query returns all information under ``horizontal:fastframe``.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe?
        ```

    Properties:
        - ``.count``: The ``HORizontal:FASTframe:COUNt`` command.
        - ``.framelock``: The ``HORizontal:FASTframe:FRAMELock`` command.
        - ``.length``: The ``HORizontal:FASTframe:LENgth`` command.
        - ``.maxframes``: The ``HORizontal:FASTframe:MAXFRames`` command.
        - ``.multipleframes``: The ``HORizontal:FASTframe:MULtipleframes`` command tree.
        - ``.ref``: The ``HORizontal:FASTframe:REF`` command tree.
        - ``.selected``: The ``HORizontal:FASTframe:SELECTED`` command tree.
        - ``.sequence``: The ``HORizontal:FASTframe:SEQuence`` command.
        - ``.singleframemath``: The ``HORizontal:FASTframe:SINGLEFramemath`` command.
        - ``.sixteenbit``: The ``HORizontal:FASTframe:SIXteenbit`` command.
        - ``.state``: The ``HORizontal:FASTframe:STATE`` command.
        - ``.sumframe``: The ``HORizontal:FASTframe:SUMFrame`` command.
        - ``.timestamp``: The ``HORizontal:FASTframe:TIMEStamp`` command tree.
        - ``.track``: The ``HORizontal:FASTframe:TRACk`` command.
        - ``.xzero``: The ``HORizontal:FASTframe:XZEro`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = HorizontalFastframeCount(device, f"{self._cmd_syntax}:COUNt")
        self._framelock = HorizontalFastframeFramelock(device, f"{self._cmd_syntax}:FRAMELock")
        self._length = HorizontalFastframeLength(device, f"{self._cmd_syntax}:LENgth")
        self._maxframes = HorizontalFastframeMaxframes(device, f"{self._cmd_syntax}:MAXFRames")
        self._multipleframes = HorizontalFastframeMultipleframes(
            device, f"{self._cmd_syntax}:MULtipleframes"
        )
        self._ref = HorizontalFastframeRef(device, f"{self._cmd_syntax}:REF")
        self._selected = HorizontalFastframeSelected(device, f"{self._cmd_syntax}:SELECTED")
        self._sequence = HorizontalFastframeSequence(device, f"{self._cmd_syntax}:SEQuence")
        self._singleframemath = HorizontalFastframeSingleframemath(
            device, f"{self._cmd_syntax}:SINGLEFramemath"
        )
        self._sixteenbit = HorizontalFastframeSixteenbit(device, f"{self._cmd_syntax}:SIXteenbit")
        self._state = HorizontalFastframeState(device, f"{self._cmd_syntax}:STATE")
        self._sumframe = HorizontalFastframeSumframe(device, f"{self._cmd_syntax}:SUMFrame")
        self._timestamp = HorizontalFastframeTimestamp(device, f"{self._cmd_syntax}:TIMEStamp")
        self._track = HorizontalFastframeTrack(device, f"{self._cmd_syntax}:TRACk")
        self._xzero = HorizontalFastframeXzero(device, f"{self._cmd_syntax}:XZEro")

    @property
    def count(self) -> HorizontalFastframeCount:
        """Return the ``HORizontal:FASTframe:COUNt`` command.

        Description:
            - This command sets or returns the number of frames.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:COUNt?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:COUNt value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:COUNt <NR1>
            - HORizontal:FASTframe:COUNt?
            ```

        Info:
            - ``<NR1>`` is the number of frames.
        """
        return self._count

    @property
    def framelock(self) -> HorizontalFastframeFramelock:
        """Return the ``HORizontal:FASTframe:FRAMELock`` command.

        Description:
            - This command sets or queries FastFrame frame lock.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:FRAMELock?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:FRAMELock?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:FRAMELock value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:FRAMELock {ON|OFF|<NR1>}
            - HORizontal:FASTframe:FRAMELock?
            ```

        Info:
            - ``<ON>`` enables frame lock.
            - ``<OFF>`` disables frame lock.
            - ``<NR1>`` = 0 disables frame lock; any other value enables framelock.
        """
        return self._framelock

    @property
    def length(self) -> HorizontalFastframeLength:
        """Return the ``HORizontal:FASTframe:LENgth`` command.

        Description:
            - This command sets or queries the horizontal record length to the number of sample
              points in each frame. This command is equivalent to selecting FastFrame Setup from the
              Horiz/Acq menu and entering a value in the Rec Length box. FastFrame captures a series
              of triggered acquisitions with minimal intervening time between them.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:LENgth?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:LENgth?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:LENgth value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:LENgth <NR1>
            - HORizontal:FASTframe:LENgth?
            ```

        Info:
            - ``<NR1>`` represents the supported value for horizontal record length in Fast Frame
              mode. In addition, to the allowable record length in normal (single frame) mode, 50
              and 250 point record lengths are permitted in Fast Frame mode.
        """
        return self._length

    @property
    def maxframes(self) -> HorizontalFastframeMaxframes:
        """Return the ``HORizontal:FASTframe:MAXFRames`` command.

        Description:
            - This query returns the maximum number of frames.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:MAXFRames?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:MAXFRames?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MAXFRames?
            ```
        """
        return self._maxframes

    @property
    def multipleframes(self) -> HorizontalFastframeMultipleframes:
        """Return the ``HORizontal:FASTframe:MULtipleframes`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:MULtipleframes?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.framestart``: The ``HORizontal:FASTframe:MULtipleframes:FRAMESTart`` command tree.
            - ``.mode``: The ``HORizontal:FASTframe:MULtipleframes:MODe`` command.
            - ``.numframes``: The ``HORizontal:FASTframe:MULtipleframes:NUMFRames`` command tree.
        """
        return self._multipleframes

    @property
    def ref(self) -> HorizontalFastframeRef:
        """Return the ``HORizontal:FASTframe:REF`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:REF?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frame``: The ``HORizontal:FASTframe:REF:FRAme`` command.
            - ``.source``: The ``HORizontal:FASTframe:REF:SOUrce`` command.
        """
        return self._ref

    @property
    def selected(self) -> HorizontalFastframeSelected:
        """Return the ``HORizontal:FASTframe:SELECTED`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SELECTED?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:FASTframe:SELECTED:CH<x>`` command.
            - ``.math``: The ``HORizontal:FASTframe:SELECTED:MATH<x>`` command.
            - ``.ref``: The ``HORizontal:FASTframe:SELECTED:REF<x>`` command.
            - ``.source``: The ``HORizontal:FASTframe:SELECTED:SOUrce`` command.
        """
        return self._selected

    @property
    def sequence(self) -> HorizontalFastframeSequence:
        """Return the ``HORizontal:FASTframe:SEQuence`` command.

        Description:
            - This command sets or queries the FastFrame single-sequence mode stop condition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SEQuence?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SEQuence?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:SEQuence value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:SEQuence {FIRst|LAST}
            - HORizontal:FASTframe:SEQuence?
            ```

        Info:
            - ``FIRst`` sets single sequence to stop after n frames.
            - ``LAST`` sets single sequence to stop manually.
        """
        return self._sequence

    @property
    def singleframemath(self) -> HorizontalFastframeSingleframemath:
        """Return the ``HORizontal:FASTframe:SINGLEFramemath`` command.

        Description:
            - This command sets or queries FastFrame single frame math.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SINGLEFramemath?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:SINGLEFramemath?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:SINGLEFramemath value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:SINGLEFramemath {ON|OFF|<NR1>}
            - HORizontal:FASTframe:SINGLEFramemath?
            ```

        Info:
            - ``<NR1>`` = 0 disables the function; any other value enables it.
            - ``OFF`` disables the function.
            - ``ON`` enables the function.
        """
        return self._singleframemath

    @property
    def sixteenbit(self) -> HorizontalFastframeSixteenbit:
        """Return the ``HORizontal:FASTframe:SIXteenbit`` command.

        Description:
            - This command sets or queries FastFrame sixteen bit.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SIXteenbit?``
              query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SIXteenbit?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:SIXteenbit value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:SIXteenbit {ON|OFF|<NR1>}
            - HORizontal:FASTframe:SIXteenbit?
            ```

        Info:
            - ``<NR1>`` = 0 disables the function; any other value enables it.
            - ``OFF`` disables the function. When OFF, fastframe data is 8 bit.
            - ``ON`` enables the function. When ON and when the summary frame is average, the data
              for the averaged summary frame is 16 bit.
        """
        return self._sixteenbit

    @property
    def state(self) -> HorizontalFastframeState:
        """Return the ``HORizontal:FASTframe:STATE`` command.

        Description:
            - This command sets or returns the state of FastFrame. Acquisition modes Envelope and
              Average are not compatible with FastFrame. If FastFrame is on, an attempted set to
              those acquisition modes will fail and revert to Sample mode. If FastFrame is turned on
              while in one of those acquisition modes, the acquisition mode is changed to Sample.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:STATE value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:STATE {ON|OFF|<NR1>}
            - HORizontal:FASTframe:STATE?
            ```

        Info:
            - ``ON`` indicates FastFrame is active.
            - ``OFF`` indicates that FastFrame is off.
            - ``<NR1>`` A 0 turns off FastFrame; any other value activates FastFrame.
        """
        return self._state

    @property
    def sumframe(self) -> HorizontalFastframeSumframe:
        """Return the ``HORizontal:FASTframe:SUMFrame`` command.

        Description:
            - This command sets or queries the summary frame mode. When ENVelope is selected, the
              last frame in a FastFrame acquisition is an envelope of all the prior frames in the
              acquisition. When AVErage is selected, the last frame is replaced with a frame that is
              the computed average of all the prior frames in the acquisition. For the summary frame
              control to be active, the number of frames must be two or greater.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SUMFrame?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SUMFrame?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:SUMFrame value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:SUMFrame {NONe|AVErage|ENVelope}
            - HORizontal:FASTframe:SUMFrame?
            ```

        Info:
            - ``NONE`` turns off the summary mode for FastFrame. This is the default setting.
            - ``AVErage`` argument displays the last frame in a FastFrame acquisition as a frame
              that is the computed average of all the prior frames in the acquisition.
            - ``ENVelope`` argument displays the last frame in a FastFrame acquisition as an
              envelope of all the prior frames in the acquisition.
        """
        return self._sumframe

    @property
    def timestamp(self) -> HorizontalFastframeTimestamp:
        """Return the ``HORizontal:FASTframe:TIMEStamp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:TIMEStamp?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.all``: The ``HORizontal:FASTframe:TIMEStamp:ALL`` command tree.
            - ``.between``: The ``HORizontal:FASTframe:TIMEStamp:BETWeen`` command tree.
            - ``.delta``: The ``HORizontal:FASTframe:TIMEStamp:DELTa`` command tree.
            - ``.frame``: The ``HORizontal:FASTframe:TIMEStamp:FRAMe`` command tree.
            - ``.ref``: The ``HORizontal:FASTframe:TIMEStamp:REF`` command.
            - ``.selected``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED`` command tree.
        """
        return self._timestamp

    @property
    def track(self) -> HorizontalFastframeTrack:
        """Return the ``HORizontal:FASTframe:TRACk`` command.

        Description:
            - This command sets up or queries the state of FastFrame tracking feature. This command
              is equivalent to selecting FastFrame Setup from the Horiz/Acq menu and then clicking
              the desired Frame Tracking state. When FastFrame Track is set to 'live', the channel
              and math waveforms are locked together. Adjusting a channel waveform also adjusts a
              related math waveform. All reference waveforms are also locked together but they are
              separate from channel and math waveforms. For example, when you set the Selected Frame
              Source Ch1 to Frame 3, then Selected Frame Ch2, Ch3, Ch4, Math1, Math2, Math3 and
              Math4 are also set to Frame 3. When you set the Selected Frame Source Ref1 to Frame 2,
              then Selected Frame Ref2, Ref3 and Ref4 are also set to Frame 2. If the Frame Tracking
              is set to Live, changing Selected Frame Ch1 will not affect the Selected Frame Ref1
              frame of the Reference Frame setting. When FastFrame Track is set to 'all', the
              channel, math and reference waveforms are locked together. Adjusting a channel
              waveform also adjusts the related math and reference waveforms. For example, when you
              set the Selected Frame Source Ch1 to Frame 3, then Selected Frame Ch2, Ch3, Ch4,
              Math1, Math2, Math3, Math4, Ref1, Ref2, Ref3 and Ref4 are also set to Frame 3.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TRACk?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:TRACk?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:TRACk value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TRACk {LIVE|ALL}
            - HORizontal:FASTframe:TRACk?
            ```

        Info:
            - ``LIVE`` sets FastFrame Track to Live.
            - ``ALL`` sets FastFrame Track to All.
        """
        return self._track

    @property
    def xzero(self) -> HorizontalFastframeXzero:
        """Return the ``HORizontal:FASTframe:XZEro`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.all``: The ``HORizontal:FASTframe:XZEro:ALL`` command tree.
            - ``.frame``: The ``HORizontal:FASTframe:XZEro:FRAme`` command tree.
            - ``.ref``: The ``HORizontal:FASTframe:XZEro:REF`` command.
            - ``.selected``: The ``HORizontal:FASTframe:XZEro:SELECTED`` command tree.
        """
        return self._xzero


class HorizontalDivisions(SCPICmdRead):
    """The ``HORizontal:DIVisions`` command.

    Description:
        - This query-only command returns the number of graticule divisions.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIVisions?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIVisions?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIVisions?
        ```
    """


class HorizontalDigitalSamplerateMain(SCPICmdRead):
    """The ``HORizontal:DIGital:SAMPLERate:MAIn`` command.

    Description:
        - Returns the sample rate of the main digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate:MAIn?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:SAMPLERate:MAIn?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:SAMPLERate:MAIn?
        ```
    """


class HorizontalDigitalSamplerateMagnivu(SCPICmdRead):
    """The ``HORizontal:DIGital:SAMPLERate:MAGnivu`` command.

    Description:
        - Returns the sample rate of the MagniVu digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate:MAGnivu?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:DIGital:SAMPLERate:MAGnivu?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:SAMPLERate:MAGnivu?
        ```
    """


class HorizontalDigitalSamplerate(SCPICmdRead):
    """The ``HORizontal:DIGital:SAMPLERate`` command.

    Description:
        - This command queries the sample rate of the digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:SAMPLERate?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:SAMPLERate?
        ```

    Properties:
        - ``.magnivu``: The ``HORizontal:DIGital:SAMPLERate:MAGnivu`` command.
        - ``.main``: The ``HORizontal:DIGital:SAMPLERate:MAIn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._magnivu = HorizontalDigitalSamplerateMagnivu(device, f"{self._cmd_syntax}:MAGnivu")
        self._main = HorizontalDigitalSamplerateMain(device, f"{self._cmd_syntax}:MAIn")

    @property
    def magnivu(self) -> HorizontalDigitalSamplerateMagnivu:
        """Return the ``HORizontal:DIGital:SAMPLERate:MAGnivu`` command.

        Description:
            - Returns the sample rate of the MagniVu digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate:MAGnivu?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:DIGital:SAMPLERate:MAGnivu?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:SAMPLERate:MAGnivu?
            ```
        """
        return self._magnivu

    @property
    def main(self) -> HorizontalDigitalSamplerateMain:
        """Return the ``HORizontal:DIGital:SAMPLERate:MAIn`` command.

        Description:
            - Returns the sample rate of the main digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate:MAIn?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:DIGital:SAMPLERate:MAIn?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:SAMPLERate:MAIn?
            ```
        """
        return self._main


class HorizontalDigitalRecordlengthMain(SCPICmdRead):
    """The ``HORizontal:DIGital:RECOrdlength:MAIn`` command.

    Description:
        - Returns the record length of the main digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength:MAIn?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:DIGital:RECOrdlength:MAIn?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:RECOrdlength:MAIn?
        ```
    """


class HorizontalDigitalRecordlengthMagnivu(SCPICmdRead):
    """The ``HORizontal:DIGital:RECOrdlength:MAGnivu`` command.

    Description:
        - Returns the record length of the MagniVu digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength:MAGnivu?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:DIGital:RECOrdlength:MAGnivu?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:RECOrdlength:MAGnivu?
        ```
    """


class HorizontalDigitalRecordlength(SCPICmdRead):
    """The ``HORizontal:DIGital:RECOrdlength`` command.

    Description:
        - This command queries the record length of the digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:RECOrdlength?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:RECOrdlength?
        ```

    Properties:
        - ``.magnivu``: The ``HORizontal:DIGital:RECOrdlength:MAGnivu`` command.
        - ``.main``: The ``HORizontal:DIGital:RECOrdlength:MAIn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._magnivu = HorizontalDigitalRecordlengthMagnivu(device, f"{self._cmd_syntax}:MAGnivu")
        self._main = HorizontalDigitalRecordlengthMain(device, f"{self._cmd_syntax}:MAIn")

    @property
    def magnivu(self) -> HorizontalDigitalRecordlengthMagnivu:
        """Return the ``HORizontal:DIGital:RECOrdlength:MAGnivu`` command.

        Description:
            - Returns the record length of the MagniVu digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:DIGital:RECOrdlength:MAGnivu?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:DIGital:RECOrdlength:MAGnivu?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:RECOrdlength:MAGnivu?
            ```
        """
        return self._magnivu

    @property
    def main(self) -> HorizontalDigitalRecordlengthMain:
        """Return the ``HORizontal:DIGital:RECOrdlength:MAIn`` command.

        Description:
            - Returns the record length of the main digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength:MAIn?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:DIGital:RECOrdlength:MAIn?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:RECOrdlength:MAIn?
            ```
        """
        return self._main


class HorizontalDigitalMagnivuPosition(SCPICmdRead):
    """The ``HORizontal:DIGital:MAGnivu:POSition`` command.

    Description:
        - This command queries the horizontal position of the trigger in percent, within the MagniVu
          digital acquisition. The MagniVu digital acquisition always includes the trigger. When the
          trigger position is adjusted near the edges of the display, the horizontal position of the
          MagniVu acquisition is adjusted to keep as much of the MagniVu acquisition in the display
          region as possible.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:MAGnivu:POSition?``
          query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:MAGnivu:POSition?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:MAGnivu:POSition?
        ```
    """


class HorizontalDigitalMagnivu(SCPICmdRead):
    """The ``HORizontal:DIGital:MAGnivu`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:MAGnivu?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:MAGnivu?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``HORizontal:DIGital:MAGnivu:POSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = HorizontalDigitalMagnivuPosition(device, f"{self._cmd_syntax}:POSition")

    @property
    def position(self) -> HorizontalDigitalMagnivuPosition:
        """Return the ``HORizontal:DIGital:MAGnivu:POSition`` command.

        Description:
            - This command queries the horizontal position of the trigger in percent, within the
              MagniVu digital acquisition. The MagniVu digital acquisition always includes the
              trigger. When the trigger position is adjusted near the edges of the display, the
              horizontal position of the MagniVu acquisition is adjusted to keep as much of the
              MagniVu acquisition in the display region as possible.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:MAGnivu:POSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:DIGital:MAGnivu:POSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:MAGnivu:POSition?
            ```
        """
        return self._position


class HorizontalDigital(SCPICmdRead):
    """The ``HORizontal:DIGital`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.magnivu``: The ``HORizontal:DIGital:MAGnivu`` command tree.
        - ``.recordlength``: The ``HORizontal:DIGital:RECOrdlength`` command.
        - ``.samplerate``: The ``HORizontal:DIGital:SAMPLERate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._magnivu = HorizontalDigitalMagnivu(device, f"{self._cmd_syntax}:MAGnivu")
        self._recordlength = HorizontalDigitalRecordlength(
            device, f"{self._cmd_syntax}:RECOrdlength"
        )
        self._samplerate = HorizontalDigitalSamplerate(device, f"{self._cmd_syntax}:SAMPLERate")

    @property
    def magnivu(self) -> HorizontalDigitalMagnivu:
        """Return the ``HORizontal:DIGital:MAGnivu`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:MAGnivu?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:MAGnivu?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``HORizontal:DIGital:MAGnivu:POSition`` command.
        """
        return self._magnivu

    @property
    def recordlength(self) -> HorizontalDigitalRecordlength:
        """Return the ``HORizontal:DIGital:RECOrdlength`` command.

        Description:
            - This command queries the record length of the digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength?``
              query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:RECOrdlength?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:RECOrdlength?
            ```

        Sub-properties:
            - ``.magnivu``: The ``HORizontal:DIGital:RECOrdlength:MAGnivu`` command.
            - ``.main``: The ``HORizontal:DIGital:RECOrdlength:MAIn`` command.
        """
        return self._recordlength

    @property
    def samplerate(self) -> HorizontalDigitalSamplerate:
        """Return the ``HORizontal:DIGital:SAMPLERate`` command.

        Description:
            - This command queries the sample rate of the digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:SAMPLERate?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:SAMPLERate?
            ```

        Sub-properties:
            - ``.magnivu``: The ``HORizontal:DIGital:SAMPLERate:MAGnivu`` command.
            - ``.main``: The ``HORizontal:DIGital:SAMPLERate:MAIn`` command.
        """
        return self._samplerate


class HorizontalAcqlength(SCPICmdRead):
    """The ``HORizontal:ACQLENGTH`` command.

    Description:
        - This query returns the record length.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:ACQLENGTH?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:ACQLENGTH?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:ACQLENGTH?
        ```
    """


class HorizontalAcqduration(SCPICmdRead):
    """The ``HORizontal:ACQDURATION`` command.

    Description:
        - This query returns the timebase duration.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:ACQDURATION?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:ACQDURATION?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:ACQDURATION?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Horizontal(SCPICmdRead):
    """The ``HORizontal`` command.

    Description:
        - Queries the current horizontal settings.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal?
        ```

    Properties:
        - ``.acqduration``: The ``HORizontal:ACQDURATION`` command.
        - ``.acqlength``: The ``HORizontal:ACQLENGTH`` command.
        - ``.digital``: The ``HORizontal:DIGital`` command tree.
        - ``.divisions``: The ``HORizontal:DIVisions`` command.
        - ``.fastframe``: The ``HORizontal:FASTframe`` command.
        - ``.main``: The ``HORizontal:MAIn`` command.
        - ``.mode``: The ``HORizontal:MODE`` command.
        - ``.position``: The ``HORizontal:POSition`` command.
        - ``.roll``: The ``HORizontal:ROLL`` command.
        - ``.timestamp``: The ``HORizontal:TIMEStamp`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "HORizontal"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._acqduration = HorizontalAcqduration(device, f"{self._cmd_syntax}:ACQDURATION")
        self._acqlength = HorizontalAcqlength(device, f"{self._cmd_syntax}:ACQLENGTH")
        self._digital = HorizontalDigital(device, f"{self._cmd_syntax}:DIGital")
        self._divisions = HorizontalDivisions(device, f"{self._cmd_syntax}:DIVisions")
        self._fastframe = HorizontalFastframe(device, f"{self._cmd_syntax}:FASTframe")
        self._mode = HorizontalMode(device, f"{self._cmd_syntax}:MODE")
        self._position = HorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._roll = HorizontalRoll(device, f"{self._cmd_syntax}:ROLL")
        self._timestamp = HorizontalTimestamp(device, f"{self._cmd_syntax}:TIMEStamp")
        self._main = HorizontalMain(device, f"{self._cmd_syntax}:MAIn")

    @property
    def acqduration(self) -> HorizontalAcqduration:
        """Return the ``HORizontal:ACQDURATION`` command.

        Description:
            - This query returns the timebase duration.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:ACQDURATION?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:ACQDURATION?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:ACQDURATION?
            ```
        """
        return self._acqduration

    @property
    def acqlength(self) -> HorizontalAcqlength:
        """Return the ``HORizontal:ACQLENGTH`` command.

        Description:
            - This query returns the record length.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:ACQLENGTH?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:ACQLENGTH?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:ACQLENGTH?
            ```
        """
        return self._acqlength

    @property
    def digital(self) -> HorizontalDigital:
        """Return the ``HORizontal:DIGital`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.magnivu``: The ``HORizontal:DIGital:MAGnivu`` command tree.
            - ``.recordlength``: The ``HORizontal:DIGital:RECOrdlength`` command.
            - ``.samplerate``: The ``HORizontal:DIGital:SAMPLERate`` command.
        """
        return self._digital

    @property
    def divisions(self) -> HorizontalDivisions:
        """Return the ``HORizontal:DIVisions`` command.

        Description:
            - This query-only command returns the number of graticule divisions.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIVisions?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DIVisions?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIVisions?
            ```
        """
        return self._divisions

    @property
    def fastframe(self) -> HorizontalFastframe:
        """Return the ``HORizontal:FASTframe`` command.

        Description:
            - This query returns all information under ``horizontal:fastframe``.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe?
            ```

        Sub-properties:
            - ``.count``: The ``HORizontal:FASTframe:COUNt`` command.
            - ``.framelock``: The ``HORizontal:FASTframe:FRAMELock`` command.
            - ``.length``: The ``HORizontal:FASTframe:LENgth`` command.
            - ``.maxframes``: The ``HORizontal:FASTframe:MAXFRames`` command.
            - ``.multipleframes``: The ``HORizontal:FASTframe:MULtipleframes`` command tree.
            - ``.ref``: The ``HORizontal:FASTframe:REF`` command tree.
            - ``.selected``: The ``HORizontal:FASTframe:SELECTED`` command tree.
            - ``.sequence``: The ``HORizontal:FASTframe:SEQuence`` command.
            - ``.singleframemath``: The ``HORizontal:FASTframe:SINGLEFramemath`` command.
            - ``.sixteenbit``: The ``HORizontal:FASTframe:SIXteenbit`` command.
            - ``.state``: The ``HORizontal:FASTframe:STATE`` command.
            - ``.sumframe``: The ``HORizontal:FASTframe:SUMFrame`` command.
            - ``.timestamp``: The ``HORizontal:FASTframe:TIMEStamp`` command tree.
            - ``.track``: The ``HORizontal:FASTframe:TRACk`` command.
            - ``.xzero``: The ``HORizontal:FASTframe:XZEro`` command tree.
        """
        return self._fastframe

    @property
    def mode(self) -> HorizontalMode:
        """Return the ``HORizontal:MODE`` command.

        Description:
            - This command set or queries the horizontal mode. Auto mode is the factory default.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MODE value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MODE {AUTO|CONStant|MANual}
            - HORizontal:MODE?
            ```

        Info:
            - ``AUTO`` selects the automatic horizontal model. Auto mode attempts to keep record
              length constant as you change the time per division setting. Record length is read
              only.
            - ``CONSTANT`` selects the constant horizontal model. Constant mode attempts to keep
              sample rate constant as you change the time per division setting. Record length is
              read only.
            - ``MANUAL`` selects the manual horizontal model. Manual mode lets you change sample
              mode and record length. Time per division or Horizontal scale is read only.

        Sub-properties:
            - ``.auto``: The ``HORizontal:MODE:AUTO`` command tree.
            - ``.recordlength``: The ``HORizontal:MODE:RECOrdlength`` command.
            - ``.samplerate``: The ``HORizontal:MODE:SAMPLERate`` command.
            - ``.scale``: The ``HORizontal:MODE:SCAle`` command.
        """
        return self._mode

    @property
    def position(self) -> HorizontalPosition:
        """Return the ``HORizontal:POSition`` command.

        Description:
            - This command sets or queries the horizontal position as a percent of screen width.
              When Horizontal Delay Mode is turned off, this command is equivalent to adjusting the
              HORIZONTAL POSITION knob on the front panel. When Horizontal Delay Mode is turned on,
              the horizontal position is forced to 50%.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:POSition?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:POSition value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:POSition <NR3>
            - HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is from 0 to ≈100 and is the position of the trigger point on the screen (0
              = left edge, 100 = right edge).
        """
        return self._position

    @property
    def roll(self) -> HorizontalRoll:
        """Return the ``HORizontal:ROLL`` command.

        Description:
            - This command sets or queries the Roll Mode status. Use Roll Mode when you want to view
              data at very slow sweep speeds. It is useful for observing data samples on the screen
              as they occur. This command is equivalent to selecting Horizontal/Acquisition Setup
              from the Horiz/Acq menu, selecting the Acquisition tab, and setting the Roll Mode to
              Auto or Off.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:ROLL?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:ROLL?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:ROLL value`` command.

        SCPI Syntax:
            ```
            - HORizontal:ROLL {AUTO|OFF|ON}
            - HORizontal:ROLL?
            ```

        Info:
            - ``AUTO`` enables Roll Mode, if the time/division is set appropriately.
            - ``OFF`` disables Roll Mode.
            - ``ON`` enables Roll Mode, if the time/division is set appropriately.
        """
        return self._roll

    @property
    def timestamp(self) -> HorizontalTimestamp:
        """Return the ``HORizontal:TIMEStamp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:TIMEStamp?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:TIMEStamp?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``HORizontal:TIMEStamp:CH<x>`` command.
            - ``.ref``: The ``HORizontal:TIMEStamp:REF<x>`` command.
        """
        return self._timestamp

    @property
    def main(self) -> HorizontalMain:
        """Return the ``HORizontal:MAIn`` command.

        Description:
            - This query-only command returns the time per division of the time base. This command
              is equivalent to selecting Position/Scale from the Horiz/Acq menu.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:MAIn?
            ```

        Sub-properties:
            - ``.interpratio``: The ``HORizontal:MAIn:INTERPRatio`` command.
            - ``.scale``: The ``HORizontal:MAIn:SCAle`` command.
            - ``.units``: The ``HORizontal:MAIn:UNIts`` command.
            - ``.delay``: The ``HORizontal:MAIn:DELay`` command tree.
        """
        return self._main
