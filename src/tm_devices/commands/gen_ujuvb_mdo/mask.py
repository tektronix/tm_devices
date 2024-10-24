# pylint: disable=line-too-long
"""The mask commands module.

These commands are used in the following models:
MDO3

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MASK:ACTONEVent:ENable {ON|OFF}
    - MASK:ACTONEVent:ENable?
    - MASK:COPy:SOUrce {DS1|DS1A|DS1C|DS2|DS3|DS4NA|DS4XNA|STS1Pulse|STS1Eye|STS3|STSX3|CLOCKCoax|CLOCKSymmetrical|DSOContra|DSODouble|DSOSingle|DSOTiming|G703DS1|DS1Rate|DS2RATECoax|DS2RATESymmetrical|G703DS3|DS3Rate|E1Coax|E1Symmetrical|E<x>|HST<x>|NONe|USER|LIMit}
    - MASK:COPy:SOUrce?
    - MASK:COPy:USER
    - MASK:COUNt RESET
    - MASK:COUNt:FAILURES?
    - MASK:COUNt:HITS?
    - MASK:COUNt:SEG<x>:HITS?
    - MASK:COUNt:TESTS?
    - MASK:COUNt:VIOLATIONS?
    - MASK:COUNt:WAVEFORMS?
    - MASK:CUSTom {INIT|COPYACTive}
    - MASK:DISplay {ON|OFF|1|0}
    - MASK:DISplay?
    - MASK:LOCk {ON|OFF|<NR1>}
    - MASK:LOCk?
    - MASK:MARgin:PERCent <NR3>
    - MASK:MARgin:PERCent?
    - MASK:SOUrce {CH<x>}
    - MASK:SOUrce?
    - MASK:STANdard {DS1|DS1A|DS1C|DS2|DS3|DS4NA|DS4XNA|STS1Pulse|STS1Eye|STS3|STSX3|CLOCKCoax|CLOCKSymmetrical|DSOContra|DSODouble|DSOSingle|DSOTiming|G703DS1|DS1Rate|DS2RATECoax|DS2RATESymmetrical|G703DS3|DS3Rate|E1Coax|E1Symmetrical|E<x>|HST<x>|NONe|USER|LIMit}
    - MASK:STANdard?
    - MASK:STOPOnviolation {ON|OFF|<NR1>}
    - MASK:STOPOnviolation?
    - MASK:TEMPLate:CREATEmask
    - MASK:TEMPLate:SOUrce {CH<x>|REF<x>}
    - MASK:TEMPLate:SOUrce?
    - MASK:TEMPLate:TOLerance:HORizontal <NR3>
    - MASK:TEMPLate:TOLerance:HORizontal?
    - MASK:TEMPLate:TOLerance:VERTical <NR3>
    - MASK:TEMPLate:TOLerance:VERTical?
    - MASK:TESt:AUXout:COMPLetion {ON|OFF|<NR1>}
    - MASK:TESt:AUXout:COMPLetion?
    - MASK:TESt:AUXout:FAILure {ON|OFF|<NR1>}
    - MASK:TESt:AUXout:FAILure?
    - MASK:TESt:COMPLetion:CRITerion {WAVEform|TIMe}
    - MASK:TESt:COMPLetion:CRITerion?
    - MASK:TESt:DELay <NR3>
    - MASK:TESt:DELay?
    - MASK:TESt:HARDCopy {ON|OFF|<NR1>}
    - MASK:TESt:HARDCopy?
    - MASK:TESt:REPeat {ON|OFF|<NR1>}
    - MASK:TESt:REPeat?
    - MASK:TESt:SAVEIMAGE {ON|OFF|<NR1>}
    - MASK:TESt:SAVEIMAGE?
    - MASK:TESt:SAVEWFM {ON|OFF|<NR1>}
    - MASK:TESt:SAVEWFM?
    - MASK:TESt:SRQ:COMPLetion {ON|OFF|<NR1>}
    - MASK:TESt:SRQ:COMPLetion?
    - MASK:TESt:SRQ:FAILure {ON|OFF|<NR1>}
    - MASK:TESt:SRQ:FAILure?
    - MASK:TESt:STATE {ON|OFF|<NR1>}
    - MASK:TESt:STATE?
    - MASK:TESt:STATus?
    - MASK:TESt:STOP:FAILure {|ON|OFF|<NR1>}
    - MASK:TESt:STOP:FAILure?
    - MASK:TESt:THReshold <NR1>
    - MASK:TESt:THReshold?
    - MASK:TESt:TIME {<NR1>|INFInite}
    - MASK:TESt:TIME?
    - MASK:TESt:WAVEform <NR1>
    - MASK:TESt:WAVEform?
    - MASK:USER:AMPLitude <NR3>
    - MASK:USER:AMPLitude?
    - MASK:USER:HSCAle <NR3>
    - MASK:USER:HSCAle?
    - MASK:USER:HTRIGPOS <NR3>
    - MASK:USER:HTRIGPOS?
    - MASK:USER:LABel <QString>
    - MASK:USER:LABel?
    - MASK:USER:MASK<x> DELEte
    - MASK:USER:MASK<x>:NR_Pt?
    - MASK:USER:MASK<x>:POINTS <NR3>
    - MASK:USER:MASK<x>:POINTS?
    - MASK:USER:RECOrdlength <NR1>
    - MASK:USER:RECOrdlength?
    - MASK:USER:SEG<x> DELEte
    - MASK:USER:SEG<x>:NR_Pt?
    - MASK:USER:SEG<x>:POINTS <NR3>
    - MASK:USER:SEG<x>:POINTS?
    - MASK:USER:TRIGTOSAMP <NR3>
    - MASK:USER:TRIGTOSAMP?
    - MASK:USER:VOFFSet <NR3>
    - MASK:USER:VOFFSet?
    - MASK:USER:VPOS <NR3>
    - MASK:USER:VPOS?
    - MASK:USER:VSCAle <NR3>
    - MASK:USER:VSCAle?
    - MASK:USER:WIDth <NR3>
    - MASK:USER:WIDth?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MaskUserWidth(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:WIDth`` command.

    Description:
        - This command specifies the nominal bit width value, in seconds, to be used for a
          user-defined custom mask. This is the time of one bit of data where bit width = 1 / (data
          rate of the signal). A series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:WIDth?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:WIDth value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:WIDth <NR3>
        - MASK:USER:WIDth?
        ```

    Info:
        - ``<NR3>`` is a floating point number that indicates the nominal bit width value in
          seconds.
    """


class MaskUserVscale(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:VSCAle`` command.

    Description:
        - This command specifies the nominal value, in volts per division, to be used to vertically
          scale the input channels for a user-defined custom mask. A series of examples showing how
          to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:VSCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:VSCAle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:VSCAle value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:VSCAle <NR3>
        - MASK:USER:VSCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the nominal vertical scale value for the
          input channels for a user-defined custom mask.
    """


class MaskUserVpos(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:VPOS`` command.

    Description:
        - This command specifies the nominal value, in divisions, to be used to vertically position
          the input channels for a user-defined custom mask. A series of examples showing how to use
          mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:VPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:VPOS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:VPOS value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:VPOS <NR3>
        - MASK:USER:VPOS?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the nominal vertical position value in
          divisions.
    """


class MaskUserVoffset(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:VOFFSet`` command.

    Description:
        - This command specifies the nominal value, in volts, to be used to vertically offset the
          input channels for a user-defined custom mask. A series of examples showing how to use
          mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:VOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:VOFFSet?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:VOFFSet value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:VOFFSet <NR3>
        - MASK:USER:VOFFSet?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the nominal vertical offset value, in
          volts.
    """


class MaskUserTrigtosamp(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:TRIGTOSAMP`` command.

    Description:
        - This command specifies the nominal time, in seconds, from the (leading edge) trigger
          position to the pulse bit sampling position, to be used for testing with a user-defined
          custom mask. A series of examples showing how to use mask commands for typical tasks is
          included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:TRIGTOSAMP?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:TRIGTOSAMP?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:TRIGTOSAMP value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:TRIGTOSAMP <NR3>
        - MASK:USER:TRIGTOSAMP?
        ```

    Info:
        - ``<NR3>`` is a floating point number that sets the time to the pulse bit sampling
          position.
    """


class MaskUserSegItemPoints(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:SEG<x>:POINTS`` command.

    Description:
        - This command specifies the x and y coordinates of the points that make up the segment 1-8.
          The units are normal waveform units. The x-coordinate is specified relative to the
          trigger. The points are specified as a sequence of (x,y) points which traverse the
          boundary of the segment in a counter-clockwise direction. A series of examples showing how
          to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:SEG<x>:POINTS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:SEG<x>:POINTS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:SEG<x>:POINTS value``
          command.

    SCPI Syntax:
        ```
        - MASK:USER:SEG<x>:POINTS <NR3>
        - MASK:USER:SEG<x>:POINTS?
        ```

    Info:
        - ``<NR3>`` is a floating- point number.
    """


class MaskUserSegItemNrPt(SCPICmdRead):
    """The ``MASK:USER:SEG<x>:NR_Pt`` command.

    Description:
        - This query returns the number of points that make up the specified mask segment of a
          user-defined custom mask. There can be up to 8 segments. A series of examples showing how
          to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:SEG<x>:NR_Pt?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:SEG<x>:NR_Pt?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:USER:SEG<x>:NR_Pt?
        ```
    """


class MaskUserSegItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:SEG<x>`` command.

    Description:
        - This command deletes the specified mask segment from the current mask segment. There can
          be up to 8 segments. A series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.write(value)`` method will send the ``MASK:USER:SEG<x> value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:SEG<x> DELEte
        ```

    Properties:
        - ``.nr_pt``: The ``MASK:USER:SEG<x>:NR_Pt`` command.
        - ``.points``: The ``MASK:USER:SEG<x>:POINTS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._nr_pt = MaskUserSegItemNrPt(device, f"{self._cmd_syntax}:NR_Pt")
        self._points = MaskUserSegItemPoints(device, f"{self._cmd_syntax}:POINTS")

    @property
    def nr_pt(self) -> MaskUserSegItemNrPt:
        """Return the ``MASK:USER:SEG<x>:NR_Pt`` command.

        Description:
            - This query returns the number of points that make up the specified mask segment of a
              user-defined custom mask. There can be up to 8 segments. A series of examples showing
              how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:SEG<x>:NR_Pt?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:SEG<x>:NR_Pt?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:USER:SEG<x>:NR_Pt?
            ```
        """
        return self._nr_pt

    @property
    def points(self) -> MaskUserSegItemPoints:
        """Return the ``MASK:USER:SEG<x>:POINTS`` command.

        Description:
            - This command specifies the x and y coordinates of the points that make up the segment
              1-8. The units are normal waveform units. The x-coordinate is specified relative to
              the trigger. The points are specified as a sequence of (x,y) points which traverse the
              boundary of the segment in a counter-clockwise direction. A series of examples showing
              how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:SEG<x>:POINTS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:SEG<x>:POINTS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:SEG<x>:POINTS value``
              command.

        SCPI Syntax:
            ```
            - MASK:USER:SEG<x>:POINTS <NR3>
            - MASK:USER:SEG<x>:POINTS?
            ```

        Info:
            - ``<NR3>`` is a floating- point number.
        """
        return self._points


class MaskUserRecordlength(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:RECOrdlength`` command.

    Description:
        - This command specifies the nominal record length to be used for pulse mask testing with a
          user-defined custom mask. A series of examples showing how to use mask commands for
          typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:RECOrdlength?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:RECOrdlength?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:RECOrdlength value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:RECOrdlength <NR1>
        - MASK:USER:RECOrdlength?
        ```

    Info:
        - ``<NR1>`` is an integer that sets the record length value to be used for pulse mask
          testing of a user-defined custom mask.
    """


class MaskUserMaskItemPoints(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:MASK<x>:POINTS`` command.

    Description:
        - This command specifies the x and y coordinates of the points that make up the segment 1-8.
          The units are normal waveform units. The x-coordinate is specified relative to the
          trigger. The points are specified as a sequence of (x,y) points which traverse the
          boundary of the segment in a counter-clockwise direction. A series of examples showing how
          to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:MASK<x>:POINTS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:MASK<x>:POINTS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:MASK<x>:POINTS value``
          command.

    SCPI Syntax:
        ```
        - MASK:USER:MASK<x>:POINTS <NR3>
        - MASK:USER:MASK<x>:POINTS?
        ```

    Info:
        - ``<NR3>`` is a floating- point number.
    """


class MaskUserMaskItemNrPt(SCPICmdRead):
    """The ``MASK:USER:MASK<x>:NR_Pt`` command.

    Description:
        - This query returns the number of points that make up the specified mask segment of a
          user-defined custom mask. There can be up to 8 segments. A series of examples showing how
          to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:MASK<x>:NR_Pt?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:MASK<x>:NR_Pt?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:USER:MASK<x>:NR_Pt?
        ```
    """


class MaskUserMaskItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:MASK<x>`` command.

    Description:
        - This command deletes the specified mask segment from the current mask segment. There can
          be up to 8 segments. A series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.write(value)`` method will send the ``MASK:USER:MASK<x> value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:MASK<x> DELEte
        ```

    Properties:
        - ``.nr_pt``: The ``MASK:USER:MASK<x>:NR_Pt`` command.
        - ``.points``: The ``MASK:USER:MASK<x>:POINTS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._nr_pt = MaskUserMaskItemNrPt(device, f"{self._cmd_syntax}:NR_Pt")
        self._points = MaskUserMaskItemPoints(device, f"{self._cmd_syntax}:POINTS")

    @property
    def nr_pt(self) -> MaskUserMaskItemNrPt:
        """Return the ``MASK:USER:MASK<x>:NR_Pt`` command.

        Description:
            - This query returns the number of points that make up the specified mask segment of a
              user-defined custom mask. There can be up to 8 segments. A series of examples showing
              how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:MASK<x>:NR_Pt?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:MASK<x>:NR_Pt?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:USER:MASK<x>:NR_Pt?
            ```
        """
        return self._nr_pt

    @property
    def points(self) -> MaskUserMaskItemPoints:
        """Return the ``MASK:USER:MASK<x>:POINTS`` command.

        Description:
            - This command specifies the x and y coordinates of the points that make up the segment
              1-8. The units are normal waveform units. The x-coordinate is specified relative to
              the trigger. The points are specified as a sequence of (x,y) points which traverse the
              boundary of the segment in a counter-clockwise direction. A series of examples showing
              how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:MASK<x>:POINTS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:MASK<x>:POINTS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:MASK<x>:POINTS value``
              command.

        SCPI Syntax:
            ```
            - MASK:USER:MASK<x>:POINTS <NR3>
            - MASK:USER:MASK<x>:POINTS?
            ```

        Info:
            - ``<NR3>`` is a floating- point number.
        """
        return self._points


class MaskUserLabel(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:LABel`` command.

    Description:
        - This command specifies a user-defined label for a custom mask.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:LABel value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:LABel <QString>
        - MASK:USER:LABel?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class MaskUserHtrigpos(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:HTRIGPOS`` command.

    Description:
        - This command specifies the nominal trigger position (pulse leading edge), to be used to
          draw a user-defined custom mask, as a fraction of the display width. A series of examples
          showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:HTRIGPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:HTRIGPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:HTRIGPOS value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:HTRIGPOS <NR3>
        - MASK:USER:HTRIGPOS?
        ```

    Info:
        - ``<NR3>`` is a floating point number in the range of 0.0 to 1.0 that sets the trigger
          points as a fraction of the display width, referenced from the left edge of the graticule.
    """


class MaskUserHscale(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:HSCAle`` command.

    Description:
        - This command specifies the nominal timing resolution, in time/division, to be used to draw
          a user-defined custom mask pulse shape. A series of examples showing how to use mask
          commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:HSCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:HSCAle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:HSCAle value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:HSCAle <NR3>
        - MASK:USER:HSCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point value that specifies the timing resolution used to a draw a
          user-defined custom mask pulse shape.
    """


class MaskUserAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:USER:AMPLitude`` command.

    Description:
        - This command specifies the nominal pulse amplitude, in volts, to be used for a
          user-defined custom mask. A series of examples showing how to use mask commands for
          typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER:AMPLitude?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:USER:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - MASK:USER:AMPLitude <NR3>
        - MASK:USER:AMPLitude?
        ```

    Info:
        - ``<NR3>`` is a floating point number that determines the nominal pulse amplitude, in
          volts, of a user-defined custom mask.
    """


#  pylint: disable=too-many-instance-attributes
class MaskUser(SCPICmdRead):
    """The ``MASK:USER`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:USER?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:USER?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``MASK:USER:AMPLitude`` command.
        - ``.hscale``: The ``MASK:USER:HSCAle`` command.
        - ``.htrigpos``: The ``MASK:USER:HTRIGPOS`` command.
        - ``.label``: The ``MASK:USER:LABel`` command.
        - ``.recordlength``: The ``MASK:USER:RECOrdlength`` command.
        - ``.trigtosamp``: The ``MASK:USER:TRIGTOSAMP`` command.
        - ``.voffset``: The ``MASK:USER:VOFFSet`` command.
        - ``.vpos``: The ``MASK:USER:VPOS`` command.
        - ``.vscale``: The ``MASK:USER:VSCAle`` command.
        - ``.width``: The ``MASK:USER:WIDth`` command.
        - ``.seg``: The ``MASK:USER:SEG<x>`` command.
        - ``.mask``: The ``MASK:USER:MASK<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = MaskUserAmplitude(device, f"{self._cmd_syntax}:AMPLitude")
        self._hscale = MaskUserHscale(device, f"{self._cmd_syntax}:HSCAle")
        self._htrigpos = MaskUserHtrigpos(device, f"{self._cmd_syntax}:HTRIGPOS")
        self._label = MaskUserLabel(device, f"{self._cmd_syntax}:LABel")
        self._recordlength = MaskUserRecordlength(device, f"{self._cmd_syntax}:RECOrdlength")
        self._trigtosamp = MaskUserTrigtosamp(device, f"{self._cmd_syntax}:TRIGTOSAMP")
        self._voffset = MaskUserVoffset(device, f"{self._cmd_syntax}:VOFFSet")
        self._vpos = MaskUserVpos(device, f"{self._cmd_syntax}:VPOS")
        self._vscale = MaskUserVscale(device, f"{self._cmd_syntax}:VSCAle")
        self._width = MaskUserWidth(device, f"{self._cmd_syntax}:WIDth")
        self._seg: Dict[int, MaskUserSegItem] = DefaultDictPassKeyToFactory(
            lambda x: MaskUserSegItem(device, f"{self._cmd_syntax}:SEG{x}")
        )
        self._mask: Dict[int, MaskUserMaskItem] = DefaultDictPassKeyToFactory(
            lambda x: MaskUserMaskItem(device, f"{self._cmd_syntax}:MASK{x}")
        )

    @property
    def amplitude(self) -> MaskUserAmplitude:
        """Return the ``MASK:USER:AMPLitude`` command.

        Description:
            - This command specifies the nominal pulse amplitude, in volts, to be used for a
              user-defined custom mask. A series of examples showing how to use mask commands for
              typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:AMPLitude?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:AMPLitude value``
              command.

        SCPI Syntax:
            ```
            - MASK:USER:AMPLitude <NR3>
            - MASK:USER:AMPLitude?
            ```

        Info:
            - ``<NR3>`` is a floating point number that determines the nominal pulse amplitude, in
              volts, of a user-defined custom mask.
        """
        return self._amplitude

    @property
    def hscale(self) -> MaskUserHscale:
        """Return the ``MASK:USER:HSCAle`` command.

        Description:
            - This command specifies the nominal timing resolution, in time/division, to be used to
              draw a user-defined custom mask pulse shape. A series of examples showing how to use
              mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:HSCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:HSCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:HSCAle value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:HSCAle <NR3>
            - MASK:USER:HSCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point value that specifies the timing resolution used to a
              draw a user-defined custom mask pulse shape.
        """
        return self._hscale

    @property
    def htrigpos(self) -> MaskUserHtrigpos:
        """Return the ``MASK:USER:HTRIGPOS`` command.

        Description:
            - This command specifies the nominal trigger position (pulse leading edge), to be used
              to draw a user-defined custom mask, as a fraction of the display width. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:HTRIGPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:HTRIGPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:HTRIGPOS value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:HTRIGPOS <NR3>
            - MASK:USER:HTRIGPOS?
            ```

        Info:
            - ``<NR3>`` is a floating point number in the range of 0.0 to 1.0 that sets the trigger
              points as a fraction of the display width, referenced from the left edge of the
              graticule.
        """
        return self._htrigpos

    @property
    def label(self) -> MaskUserLabel:
        """Return the ``MASK:USER:LABel`` command.

        Description:
            - This command specifies a user-defined label for a custom mask.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:LABel?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:LABel value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:LABel <QString>
            - MASK:USER:LABel?
            ```
        """
        return self._label

    @property
    def recordlength(self) -> MaskUserRecordlength:
        """Return the ``MASK:USER:RECOrdlength`` command.

        Description:
            - This command specifies the nominal record length to be used for pulse mask testing
              with a user-defined custom mask. A series of examples showing how to use mask commands
              for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:RECOrdlength?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:RECOrdlength?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:RECOrdlength value``
              command.

        SCPI Syntax:
            ```
            - MASK:USER:RECOrdlength <NR1>
            - MASK:USER:RECOrdlength?
            ```

        Info:
            - ``<NR1>`` is an integer that sets the record length value to be used for pulse mask
              testing of a user-defined custom mask.
        """
        return self._recordlength

    @property
    def trigtosamp(self) -> MaskUserTrigtosamp:
        """Return the ``MASK:USER:TRIGTOSAMP`` command.

        Description:
            - This command specifies the nominal time, in seconds, from the (leading edge) trigger
              position to the pulse bit sampling position, to be used for testing with a
              user-defined custom mask. A series of examples showing how to use mask commands for
              typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:TRIGTOSAMP?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:TRIGTOSAMP?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:TRIGTOSAMP value``
              command.

        SCPI Syntax:
            ```
            - MASK:USER:TRIGTOSAMP <NR3>
            - MASK:USER:TRIGTOSAMP?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the time to the pulse bit sampling
              position.
        """
        return self._trigtosamp

    @property
    def voffset(self) -> MaskUserVoffset:
        """Return the ``MASK:USER:VOFFSet`` command.

        Description:
            - This command specifies the nominal value, in volts, to be used to vertically offset
              the input channels for a user-defined custom mask. A series of examples showing how to
              use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:VOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:VOFFSet?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:VOFFSet value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:VOFFSet <NR3>
            - MASK:USER:VOFFSet?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the nominal vertical offset value, in
              volts.
        """
        return self._voffset

    @property
    def vpos(self) -> MaskUserVpos:
        """Return the ``MASK:USER:VPOS`` command.

        Description:
            - This command specifies the nominal value, in divisions, to be used to vertically
              position the input channels for a user-defined custom mask. A series of examples
              showing how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:VPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:VPOS?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:VPOS value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:VPOS <NR3>
            - MASK:USER:VPOS?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the nominal vertical position value in
              divisions.
        """
        return self._vpos

    @property
    def vscale(self) -> MaskUserVscale:
        """Return the ``MASK:USER:VSCAle`` command.

        Description:
            - This command specifies the nominal value, in volts per division, to be used to
              vertically scale the input channels for a user-defined custom mask. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:VSCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:VSCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:VSCAle value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:VSCAle <NR3>
            - MASK:USER:VSCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point number that sets the nominal vertical scale value for
              the input channels for a user-defined custom mask.
        """
        return self._vscale

    @property
    def width(self) -> MaskUserWidth:
        """Return the ``MASK:USER:WIDth`` command.

        Description:
            - This command specifies the nominal bit width value, in seconds, to be used for a
              user-defined custom mask. This is the time of one bit of data where bit width = 1 /
              (data rate of the signal). A series of examples showing how to use mask commands for
              typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER:WIDth?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:USER:WIDth value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:WIDth <NR3>
            - MASK:USER:WIDth?
            ```

        Info:
            - ``<NR3>`` is a floating point number that indicates the nominal bit width value in
              seconds.
        """
        return self._width

    @property
    def seg(self) -> Dict[int, MaskUserSegItem]:
        """Return the ``MASK:USER:SEG<x>`` command.

        Description:
            - This command deletes the specified mask segment from the current mask segment. There
              can be up to 8 segments. A series of examples showing how to use mask commands for
              typical tasks is included in an appendix.

        Usage:
            - Using the ``.write(value)`` method will send the ``MASK:USER:SEG<x> value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:SEG<x> DELEte
            ```

        Sub-properties:
            - ``.nr_pt``: The ``MASK:USER:SEG<x>:NR_Pt`` command.
            - ``.points``: The ``MASK:USER:SEG<x>:POINTS`` command.
        """
        return self._seg

    @property
    def mask(self) -> Dict[int, MaskUserMaskItem]:
        """Return the ``MASK:USER:MASK<x>`` command.

        Description:
            - This command deletes the specified mask segment from the current mask segment. There
              can be up to 8 segments. A series of examples showing how to use mask commands for
              typical tasks is included in an appendix.

        Usage:
            - Using the ``.write(value)`` method will send the ``MASK:USER:MASK<x> value`` command.

        SCPI Syntax:
            ```
            - MASK:USER:MASK<x> DELEte
            ```

        Sub-properties:
            - ``.nr_pt``: The ``MASK:USER:MASK<x>:NR_Pt`` command.
            - ``.points``: The ``MASK:USER:MASK<x>:POINTS`` command.
        """
        return self._mask


class MaskTestWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:WAVEform`` command.

    Description:
        - This command specifies the number of waveforms the instrument should test during a
          pass/fail mask test. A series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:WAVEform?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:WAVEform value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:WAVEform <NR1>
        - MASK:TESt:WAVEform?
        ```

    Info:
        - ``<NR1>`` is an integer that specifies the number of waveforms to test. The maximum
          waveform count that can be specified is 1E09.
    """


class MaskTestTime(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:TIME`` command.

    Description:
        - This command specifies the duration, in seconds, the instrument should run a pass/fail
          mask test. The default is INFINITE. A series of examples showing how to use mask commands
          for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:TIME?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:TIME?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:TIME value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:TIME {<NR1>|INFInite}
        - MASK:TESt:TIME?
        ```

    Info:
        - ``<NR1>`` is an integer that represents the number of seconds to test. The maximum number
          of seconds that can be specified is 172,800.
        - ``INFInite`` indicates that there is no time limit on the test run.
    """


class MaskTestThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:THReshold`` command.

    Description:
        - This command specifies the number of failed tested waveforms needed in a pass/fail mask
          test to cause the test status to change to 'Failing'. A series of examples showing how to
          use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:THReshold?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:THReshold value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:THReshold <NR1>
        - MASK:TESt:THReshold?
        ```

    Info:
        - ``<NR1>`` is an integer that specifies the number of tested waveform violations occurring
          in each mask test that will change the test status to 'Failing'. The maximum number of
          failed tested waveforms that can be specified is 1E09. The default is 1.
    """


class MaskTestStopFailure(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:STOP:FAILure`` command.

    Description:
        - This command causes the instrument to stop acquiring data when a pass/fail mask test
          fails. The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to
          happen. After the event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF
          automatically. A series of examples showing how to use mask commands for typical tasks is
          included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:STOP:FAILure?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:STOP:FAILure?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:STOP:FAILure value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:STOP:FAILure {|ON|OFF|<NR1>}
        - MASK:TESt:STOP:FAILure?
        ```

    Info:
        - ``ON`` turns on this features, so that the instrument stops acquiring data upon failure.
        - ``OFF`` turns off this feature.
        - ``<NR1>`` is an integer. 0 turns off this feature; any other value turns it on.
    """


class MaskTestStop(SCPICmdRead):
    """The ``MASK:TESt:STOP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:STOP?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:STOP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.failure``: The ``MASK:TESt:STOP:FAILure`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._failure = MaskTestStopFailure(device, f"{self._cmd_syntax}:FAILure")

    @property
    def failure(self) -> MaskTestStopFailure:
        """Return the ``MASK:TESt:STOP:FAILure`` command.

        Description:
            - This command causes the instrument to stop acquiring data when a pass/fail mask test
              fails. The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to
              happen. After the event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF
              automatically. A series of examples showing how to use mask commands for typical tasks
              is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:STOP:FAILure?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:STOP:FAILure?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:STOP:FAILure value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:STOP:FAILure {|ON|OFF|<NR1>}
            - MASK:TESt:STOP:FAILure?
            ```

        Info:
            - ``ON`` turns on this features, so that the instrument stops acquiring data upon
              failure.
            - ``OFF`` turns off this feature.
            - ``<NR1>`` is an integer. 0 turns off this feature; any other value turns it on.
        """
        return self._failure


class MaskTestStatus(SCPICmdRead):
    """The ``MASK:TESt:STATus`` command.

    Description:
        - This command indicates the result of a pass/fail mask test. A series of examples showing
          how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:STATus?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:TESt:STATus?
        ```
    """


class MaskTestState(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:STATE`` command.

    Description:
        - This command turns the pass/fail mask test on or off. Most of the other ``MASK:TEST``
          commands need to be executed before this command. A series of examples showing how to use
          mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:STATE value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:STATE {ON|OFF|<NR1>}
        - MASK:TESt:STATE?
        ```

    Info:
        - ``ON`` turns the mask test on.
        - ``OFF`` turns the mask test off.
        - ``<NR1>`` is an integer. 0 turns the mask test off; any other integer turns it on.
    """


class MaskTestSrqFailure(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:SRQ:FAILure`` command.

    Description:
        - This command causes the instrument to send an SRQ command when a pass/fail mask test
          fails. A series of examples showing how to use mask commands for typical tasks is included
          in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SRQ:FAILure?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ:FAILure?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:SRQ:FAILure value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:SRQ:FAILure {ON|OFF|<NR1>}
        - MASK:TESt:SRQ:FAILure?
        ```

    Info:
        - ``ON`` turns on this feature, so that when a mask test fails, the instrument will send an
          SRQ command (if registers are set to send SRQ when OPC is asserted.
        - ``OFF`` turns off this feature.
        - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
    """


class MaskTestSrqCompletion(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:SRQ:COMPLetion`` command.

    Description:
        - This command causes the instrument to send an SRQ command when a pass/fail mask test
          completes. Use the command ``MASK:TEST:COMPLETION:CRITERION`` to specify criterion. The
          ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to happen. After the
          event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF automatically. A series
          of examples showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SRQ:COMPLetion?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ:COMPLetion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:SRQ:COMPLetion value``
          command.

    SCPI Syntax:
        ```
        - MASK:TESt:SRQ:COMPLetion {ON|OFF|<NR1>}
        - MASK:TESt:SRQ:COMPLetion?
        ```

    Info:
        - ``ON`` turns on this feature, so that upon the completion of a mask test, the instrument
          will send an SRQ command (if registers are set to send SRQ when OPC is asserted).
        - ``OFF`` turns off this feature.
        - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
    """


class MaskTestSrq(SCPICmdRead):
    """The ``MASK:TESt:SRQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.completion``: The ``MASK:TESt:SRQ:COMPLetion`` command.
        - ``.failure``: The ``MASK:TESt:SRQ:FAILure`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._completion = MaskTestSrqCompletion(device, f"{self._cmd_syntax}:COMPLetion")
        self._failure = MaskTestSrqFailure(device, f"{self._cmd_syntax}:FAILure")

    @property
    def completion(self) -> MaskTestSrqCompletion:
        """Return the ``MASK:TESt:SRQ:COMPLetion`` command.

        Description:
            - This command causes the instrument to send an SRQ command when a pass/fail mask test
              completes. Use the command ``MASK:TEST:COMPLETION:CRITERION`` to specify criterion.
              The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to happen.
              After the event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF
              automatically. A series of examples showing how to use mask commands for typical tasks
              is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SRQ:COMPLetion?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ:COMPLetion?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:SRQ:COMPLetion value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:SRQ:COMPLetion {ON|OFF|<NR1>}
            - MASK:TESt:SRQ:COMPLetion?
            ```

        Info:
            - ``ON`` turns on this feature, so that upon the completion of a mask test, the
              instrument will send an SRQ command (if registers are set to send SRQ when OPC is
              asserted).
            - ``OFF`` turns off this feature.
            - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
        """
        return self._completion

    @property
    def failure(self) -> MaskTestSrqFailure:
        """Return the ``MASK:TESt:SRQ:FAILure`` command.

        Description:
            - This command causes the instrument to send an SRQ command when a pass/fail mask test
              fails. A series of examples showing how to use mask commands for typical tasks is
              included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SRQ:FAILure?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ:FAILure?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:SRQ:FAILure value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:SRQ:FAILure {ON|OFF|<NR1>}
            - MASK:TESt:SRQ:FAILure?
            ```

        Info:
            - ``ON`` turns on this feature, so that when a mask test fails, the instrument will send
              an SRQ command (if registers are set to send SRQ when OPC is asserted.
            - ``OFF`` turns off this feature.
            - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
        """
        return self._failure


class MaskTestSavewfm(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:SAVEWFM`` command.

    Description:
        - This command copies the waveform data from all active channels to a file on a flash memory
          device such as a USB stick or a network drive. See the command ``FILESYSTEM:MKDIR`` and
          other File System commands for more information on saving to a file. The
          ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to happen. After the
          event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF automatically. A series
          of examples showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SAVEWFM?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAVEWFM?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:SAVEWFM value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:SAVEWFM {ON|OFF|<NR1>}
        - MASK:TESt:SAVEWFM?
        ```

    Info:
        - ``ON`` turns on this feature, so that waveform data from all active channels is copied to
          files upon test failure.
        - ``OFF`` turns off this feature.
        - ``<NR1>`` is an integer. 0 turns off this feature; any other value turns it on.
    """


class MaskTestSaveimage(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:SAVEIMAGE`` command.

    Description:
        - This command causes the instrument to copy the screen image to a file on a USB mass
          storage device or a mounted network drive if a pass/fail mask test fails. See the command
          ``FILESYSTEM:MKDIR`` and other File System commands for more information on saving to a
          file. The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON to save the image on mask
          test failure. After the image is saved the ``MASK:ACTONEVENT:ENABLE`` command will be set
          to OFF automatically. A series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:SAVEIMAGE?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAVEIMAGE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:SAVEIMAGE value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:SAVEIMAGE {ON|OFF|<NR1>}
        - MASK:TESt:SAVEIMAGE?
        ```

    Info:
        - ``ON`` turns on this feature, so that the screen image is copied to a specified file upon
          test failure.
        - ``OFF`` turns off this feature.
        - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
    """


class MaskTestRepeat(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:REPeat`` command.

    Description:
        - This command causes the mask test cycle to continuously repeat upon the completion of the
          previous test cycle. A series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:REPeat?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:REPeat?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:REPeat value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:REPeat {ON|OFF|<NR1>}
        - MASK:TESt:REPeat?
        ```

    Info:
        - ``ON`` turns on this feature, so that the mask test cycle repeats continuously upon the
          completion of the previous test cycle.
        - ``OFF`` turns off this feature.
        - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
    """


class MaskTestHardcopy(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:HARDCopy`` command.

    Description:
        - This command will cause the instrument to generate a screen shot to the default printer as
          soon as a pass/fail mask test fails, using the current instrument hard copy settings. See
          ``HARDCOPY:ACTIVEPRINTER`` and other Hardcopy commands for more information on accessing
          printer settings. A series of examples showing how to use mask commands for typical tasks
          is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:HARDCopy?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:HARDCopy?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:HARDCopy value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:HARDCopy {ON|OFF|<NR1>}
        - MASK:TESt:HARDCopy?
        ```

    Info:
        - ``ON`` turns on this feature, so that the instrument will generate a screen hard copy to
          the default printer upon failure.
        - ``OFF`` turns off this feature.
        - ``<NR1>`` = 0 turns off this feature; any other value turns it on.
    """


class MaskTestDelay(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:DELay`` command.

    Description:
        - This command specifies the amount of time, in seconds, the instrument should wait after
          the start of pass/fail mask testing before it evaluates the waveforms. This command is
          useful if the test system requires some 'settling' time. A series of examples showing how
          to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:DELay?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:DELay value`` command.

    SCPI Syntax:
        ```
        - MASK:TESt:DELay <NR3>
        - MASK:TESt:DELay?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the amount of time in seconds, to
          delay the start of the mask pass/fail test.
    """


class MaskTestCompletionCriterion(SCPICmdWrite, SCPICmdRead):
    r"""The ``MASK:TESt:COMPLetion:CRITerion`` command.

    Description:
        - This command specifies the criterion to be used (either by waveform or by time) for test
          completion during pass/fail mask testing. A series of examples showing how to use mask
          commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:COMPLetion:CRITerion?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:COMPLetion:CRITerion?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:COMPLetion:CRITerion value``
          command.

    SCPI Syntax:
        ```
        - MASK:TESt:COMPLetion:CRITerion {WAVEform|TIMe}
        - MASK:TESt:COMPLetion:CRITerion?
        ```

    Info:
        - ``WAVEform`` specifies that the test is to be considered complete when a specified number
          of waveforms has been tested. (The number of waveforms is specified using
          ``MASK:TEST:WAVEform`` <NR1>) .
        - ``TIMe`` specifies that the test is to be considered complete when a specified amount of
          time has elapsed. (The amount of time is specified using ``MASK:TEST:TIME``
          (<NR1>\|INFInite)).
    """


class MaskTestCompletion(SCPICmdRead):
    """The ``MASK:TESt:COMPLetion`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:COMPLetion?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:COMPLetion?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.criterion``: The ``MASK:TESt:COMPLetion:CRITerion`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._criterion = MaskTestCompletionCriterion(device, f"{self._cmd_syntax}:CRITerion")

    @property
    def criterion(self) -> MaskTestCompletionCriterion:
        r"""Return the ``MASK:TESt:COMPLetion:CRITerion`` command.

        Description:
            - This command specifies the criterion to be used (either by waveform or by time) for
              test completion during pass/fail mask testing. A series of examples showing how to use
              mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:COMPLetion:CRITerion?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:COMPLetion:CRITerion?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MASK:TESt:COMPLetion:CRITerion value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:COMPLetion:CRITerion {WAVEform|TIMe}
            - MASK:TESt:COMPLetion:CRITerion?
            ```

        Info:
            - ``WAVEform`` specifies that the test is to be considered complete when a specified
              number of waveforms has been tested. (The number of waveforms is specified using
              ``MASK:TEST:WAVEform`` <NR1>) .
            - ``TIMe`` specifies that the test is to be considered complete when a specified amount
              of time has elapsed. (The amount of time is specified using ``MASK:TEST:TIME``
              (<NR1>\|INFInite)).
        """
        return self._criterion


class MaskTestAuxoutFailure(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:AUXout:FAILure`` command.

    Description:
        - This command causes the instrument to send a TTL signal to the ``AUX:out`` port whenever a
          pass/fail mask test fails. The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for
          this event to happen. After the event occurs ``MASK:ACTONEVENT:ENABLE`` command will be
          set to OFF automatically. A series of examples showing how to use mask commands for
          typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:AUXout:FAILure?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUXout:FAILure?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:AUXout:FAILure value``
          command.

    SCPI Syntax:
        ```
        - MASK:TESt:AUXout:FAILure {ON|OFF|<NR1>}
        - MASK:TESt:AUXout:FAILure?
        ```

    Info:
        - ``ON`` turns on this feature, so that a signal is sent to the ``AUX:out`` port whenever a
          mask test status changes to 'failing'.
        - ``OFF`` turns off this feature.
        - ``<NR1>= 0`` turns off this feature; any other value turns it on.
    """


class MaskTestAuxoutCompletion(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TESt:AUXout:COMPLetion`` command.

    Description:
        - This command will cause the instrument to send a TTL signal to the ``AUX:out`` port
          whenever a pass/fail mask test completes. The ``MASK:ACTONEVENT:ENABLE`` command should be
          set to ON for this event to happen. After the event occurs ``MASK:ACTONEVENT:ENABLE``
          command will be set to OFF automatically. A series of examples showing how to use mask
          commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:AUXout:COMPLetion?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUXout:COMPLetion?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TESt:AUXout:COMPLetion value``
          command.

    SCPI Syntax:
        ```
        - MASK:TESt:AUXout:COMPLetion {ON|OFF|<NR1>}
        - MASK:TESt:AUXout:COMPLetion?
        ```

    Info:
        - ``ON`` turns on this feature, so that a signal is sent to the ``AUX:out`` port whenever a
          mask test is complete.
        - ``OFF`` turns off this feature.
        - ``<NR1>=0`` turns off this feature; any other value turns it on.
    """


class MaskTestAuxout(SCPICmdRead):
    """The ``MASK:TESt:AUXout`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt:AUXout?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUXout?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.completion``: The ``MASK:TESt:AUXout:COMPLetion`` command.
        - ``.failure``: The ``MASK:TESt:AUXout:FAILure`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._completion = MaskTestAuxoutCompletion(device, f"{self._cmd_syntax}:COMPLetion")
        self._failure = MaskTestAuxoutFailure(device, f"{self._cmd_syntax}:FAILure")

    @property
    def completion(self) -> MaskTestAuxoutCompletion:
        """Return the ``MASK:TESt:AUXout:COMPLetion`` command.

        Description:
            - This command will cause the instrument to send a TTL signal to the ``AUX:out`` port
              whenever a pass/fail mask test completes. The ``MASK:ACTONEVENT:ENABLE`` command
              should be set to ON for this event to happen. After the event occurs
              ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF automatically. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:AUXout:COMPLetion?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUXout:COMPLetion?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:AUXout:COMPLetion value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:AUXout:COMPLetion {ON|OFF|<NR1>}
            - MASK:TESt:AUXout:COMPLetion?
            ```

        Info:
            - ``ON`` turns on this feature, so that a signal is sent to the ``AUX:out`` port
              whenever a mask test is complete.
            - ``OFF`` turns off this feature.
            - ``<NR1>=0`` turns off this feature; any other value turns it on.
        """
        return self._completion

    @property
    def failure(self) -> MaskTestAuxoutFailure:
        """Return the ``MASK:TESt:AUXout:FAILure`` command.

        Description:
            - This command causes the instrument to send a TTL signal to the ``AUX:out`` port
              whenever a pass/fail mask test fails. The ``MASK:ACTONEVENT:ENABLE`` command should be
              set to ON for this event to happen. After the event occurs ``MASK:ACTONEVENT:ENABLE``
              command will be set to OFF automatically. A series of examples showing how to use mask
              commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:AUXout:FAILure?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUXout:FAILure?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:AUXout:FAILure value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:AUXout:FAILure {ON|OFF|<NR1>}
            - MASK:TESt:AUXout:FAILure?
            ```

        Info:
            - ``ON`` turns on this feature, so that a signal is sent to the ``AUX:out`` port
              whenever a mask test status changes to 'failing'.
            - ``OFF`` turns off this feature.
            - ``<NR1>= 0`` turns off this feature; any other value turns it on.
        """
        return self._failure


#  pylint: disable=too-many-instance-attributes
class MaskTest(SCPICmdRead):
    """The ``MASK:TESt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TESt?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TESt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.auxout``: The ``MASK:TESt:AUXout`` command tree.
        - ``.completion``: The ``MASK:TESt:COMPLetion`` command tree.
        - ``.delay``: The ``MASK:TESt:DELay`` command.
        - ``.hardcopy``: The ``MASK:TESt:HARDCopy`` command.
        - ``.repeat``: The ``MASK:TESt:REPeat`` command.
        - ``.saveimage``: The ``MASK:TESt:SAVEIMAGE`` command.
        - ``.savewfm``: The ``MASK:TESt:SAVEWFM`` command.
        - ``.srq``: The ``MASK:TESt:SRQ`` command tree.
        - ``.state``: The ``MASK:TESt:STATE`` command.
        - ``.status``: The ``MASK:TESt:STATus`` command.
        - ``.stop``: The ``MASK:TESt:STOP`` command tree.
        - ``.threshold``: The ``MASK:TESt:THReshold`` command.
        - ``.time``: The ``MASK:TESt:TIME`` command.
        - ``.waveform``: The ``MASK:TESt:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._auxout = MaskTestAuxout(device, f"{self._cmd_syntax}:AUXout")
        self._completion = MaskTestCompletion(device, f"{self._cmd_syntax}:COMPLetion")
        self._delay = MaskTestDelay(device, f"{self._cmd_syntax}:DELay")
        self._hardcopy = MaskTestHardcopy(device, f"{self._cmd_syntax}:HARDCopy")
        self._repeat = MaskTestRepeat(device, f"{self._cmd_syntax}:REPeat")
        self._saveimage = MaskTestSaveimage(device, f"{self._cmd_syntax}:SAVEIMAGE")
        self._savewfm = MaskTestSavewfm(device, f"{self._cmd_syntax}:SAVEWFM")
        self._srq = MaskTestSrq(device, f"{self._cmd_syntax}:SRQ")
        self._state = MaskTestState(device, f"{self._cmd_syntax}:STATE")
        self._status = MaskTestStatus(device, f"{self._cmd_syntax}:STATus")
        self._stop = MaskTestStop(device, f"{self._cmd_syntax}:STOP")
        self._threshold = MaskTestThreshold(device, f"{self._cmd_syntax}:THReshold")
        self._time = MaskTestTime(device, f"{self._cmd_syntax}:TIME")
        self._waveform = MaskTestWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def auxout(self) -> MaskTestAuxout:
        """Return the ``MASK:TESt:AUXout`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:AUXout?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:AUXout?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.completion``: The ``MASK:TESt:AUXout:COMPLetion`` command.
            - ``.failure``: The ``MASK:TESt:AUXout:FAILure`` command.
        """
        return self._auxout

    @property
    def completion(self) -> MaskTestCompletion:
        """Return the ``MASK:TESt:COMPLetion`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:COMPLetion?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:COMPLetion?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.criterion``: The ``MASK:TESt:COMPLetion:CRITerion`` command.
        """
        return self._completion

    @property
    def delay(self) -> MaskTestDelay:
        """Return the ``MASK:TESt:DELay`` command.

        Description:
            - This command specifies the amount of time, in seconds, the instrument should wait
              after the start of pass/fail mask testing before it evaluates the waveforms. This
              command is useful if the test system requires some 'settling' time. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:DELay?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:DELay value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:DELay <NR3>
            - MASK:TESt:DELay?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the amount of time in seconds, to
              delay the start of the mask pass/fail test.
        """
        return self._delay

    @property
    def hardcopy(self) -> MaskTestHardcopy:
        """Return the ``MASK:TESt:HARDCopy`` command.

        Description:
            - This command will cause the instrument to generate a screen shot to the default
              printer as soon as a pass/fail mask test fails, using the current instrument hard copy
              settings. See ``HARDCOPY:ACTIVEPRINTER`` and other Hardcopy commands for more
              information on accessing printer settings. A series of examples showing how to use
              mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:HARDCopy?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:HARDCopy?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:HARDCopy value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:HARDCopy {ON|OFF|<NR1>}
            - MASK:TESt:HARDCopy?
            ```

        Info:
            - ``ON`` turns on this feature, so that the instrument will generate a screen hard copy
              to the default printer upon failure.
            - ``OFF`` turns off this feature.
            - ``<NR1>`` = 0 turns off this feature; any other value turns it on.
        """
        return self._hardcopy

    @property
    def repeat(self) -> MaskTestRepeat:
        """Return the ``MASK:TESt:REPeat`` command.

        Description:
            - This command causes the mask test cycle to continuously repeat upon the completion of
              the previous test cycle. A series of examples showing how to use mask commands for
              typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:REPeat?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:REPeat?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:REPeat value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:REPeat {ON|OFF|<NR1>}
            - MASK:TESt:REPeat?
            ```

        Info:
            - ``ON`` turns on this feature, so that the mask test cycle repeats continuously upon
              the completion of the previous test cycle.
            - ``OFF`` turns off this feature.
            - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
        """
        return self._repeat

    @property
    def saveimage(self) -> MaskTestSaveimage:
        """Return the ``MASK:TESt:SAVEIMAGE`` command.

        Description:
            - This command causes the instrument to copy the screen image to a file on a USB mass
              storage device or a mounted network drive if a pass/fail mask test fails. See the
              command ``FILESYSTEM:MKDIR`` and other File System commands for more information on
              saving to a file. The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON to save
              the image on mask test failure. After the image is saved the
              ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF automatically. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SAVEIMAGE?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAVEIMAGE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:SAVEIMAGE value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:SAVEIMAGE {ON|OFF|<NR1>}
            - MASK:TESt:SAVEIMAGE?
            ```

        Info:
            - ``ON`` turns on this feature, so that the screen image is copied to a specified file
              upon test failure.
            - ``OFF`` turns off this feature.
            - ``<NR1>`` is an integer. 0 turns off this feature; any other integer turns it on.
        """
        return self._saveimage

    @property
    def savewfm(self) -> MaskTestSavewfm:
        """Return the ``MASK:TESt:SAVEWFM`` command.

        Description:
            - This command copies the waveform data from all active channels to a file on a flash
              memory device such as a USB stick or a network drive. See the command
              ``FILESYSTEM:MKDIR`` and other File System commands for more information on saving to
              a file. The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to
              happen. After the event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF
              automatically. A series of examples showing how to use mask commands for typical tasks
              is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SAVEWFM?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SAVEWFM?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:SAVEWFM value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:SAVEWFM {ON|OFF|<NR1>}
            - MASK:TESt:SAVEWFM?
            ```

        Info:
            - ``ON`` turns on this feature, so that waveform data from all active channels is copied
              to files upon test failure.
            - ``OFF`` turns off this feature.
            - ``<NR1>`` is an integer. 0 turns off this feature; any other value turns it on.
        """
        return self._savewfm

    @property
    def srq(self) -> MaskTestSrq:
        """Return the ``MASK:TESt:SRQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:SRQ?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:SRQ?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.completion``: The ``MASK:TESt:SRQ:COMPLetion`` command.
            - ``.failure``: The ``MASK:TESt:SRQ:FAILure`` command.
        """
        return self._srq

    @property
    def state(self) -> MaskTestState:
        """Return the ``MASK:TESt:STATE`` command.

        Description:
            - This command turns the pass/fail mask test on or off. Most of the other ``MASK:TEST``
              commands need to be executed before this command. A series of examples showing how to
              use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:STATE value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:STATE {ON|OFF|<NR1>}
            - MASK:TESt:STATE?
            ```

        Info:
            - ``ON`` turns the mask test on.
            - ``OFF`` turns the mask test off.
            - ``<NR1>`` is an integer. 0 turns the mask test off; any other integer turns it on.
        """
        return self._state

    @property
    def status(self) -> MaskTestStatus:
        """Return the ``MASK:TESt:STATus`` command.

        Description:
            - This command indicates the result of a pass/fail mask test. A series of examples
              showing how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:STATus?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:TESt:STATus?
            ```
        """
        return self._status

    @property
    def stop(self) -> MaskTestStop:
        """Return the ``MASK:TESt:STOP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:STOP?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:STOP?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.failure``: The ``MASK:TESt:STOP:FAILure`` command.
        """
        return self._stop

    @property
    def threshold(self) -> MaskTestThreshold:
        """Return the ``MASK:TESt:THReshold`` command.

        Description:
            - This command specifies the number of failed tested waveforms needed in a pass/fail
              mask test to cause the test status to change to 'Failing'. A series of examples
              showing how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:THReshold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:THReshold value``
              command.

        SCPI Syntax:
            ```
            - MASK:TESt:THReshold <NR1>
            - MASK:TESt:THReshold?
            ```

        Info:
            - ``<NR1>`` is an integer that specifies the number of tested waveform violations
              occurring in each mask test that will change the test status to 'Failing'. The maximum
              number of failed tested waveforms that can be specified is 1E09. The default is 1.
        """
        return self._threshold

    @property
    def time(self) -> MaskTestTime:
        """Return the ``MASK:TESt:TIME`` command.

        Description:
            - This command specifies the duration, in seconds, the instrument should run a pass/fail
              mask test. The default is INFINITE. A series of examples showing how to use mask
              commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:TIME?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:TIME?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:TIME value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:TIME {<NR1>|INFInite}
            - MASK:TESt:TIME?
            ```

        Info:
            - ``<NR1>`` is an integer that represents the number of seconds to test. The maximum
              number of seconds that can be specified is 172,800.
            - ``INFInite`` indicates that there is no time limit on the test run.
        """
        return self._time

    @property
    def waveform(self) -> MaskTestWaveform:
        """Return the ``MASK:TESt:WAVEform`` command.

        Description:
            - This command specifies the number of waveforms the instrument should test during a
              pass/fail mask test. A series of examples showing how to use mask commands for typical
              tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt:WAVEform?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TESt:WAVEform value`` command.

        SCPI Syntax:
            ```
            - MASK:TESt:WAVEform <NR1>
            - MASK:TESt:WAVEform?
            ```

        Info:
            - ``<NR1>`` is an integer that specifies the number of waveforms to test. The maximum
              waveform count that can be specified is 1E09.
        """
        return self._waveform


class MaskTemplateToleranceVertical(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TEMPLate:TOLerance:VERTical`` command.

    Description:
        - This command specifies the vertical limit (tolerance) for a template mask to be used for
          limit testing. This indicates how far vertically from the template source to create the
          mask. A series of examples showing how to use mask commands for typical tasks is included
          in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TEMPLate:TOLerance:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TEMPLate:TOLerance:VERTical?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MASK:TEMPLate:TOLerance:VERTical value`` command.

    SCPI Syntax:
        ```
        - MASK:TEMPLate:TOLerance:VERTical <NR3>
        - MASK:TEMPLate:TOLerance:VERTical?
        ```

    Info:
        - ``<NR3>`` is a floating point value that specifies the vertical limit (tolerence) in
          milli-divisions. Range: 0 to 1000 mDiv, resolution: 1 mDiv, default: 200 mDiv. This value
          cannot be negative.
    """


class MaskTemplateToleranceHorizontal(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TEMPLate:TOLerance:HORizontal`` command.

    Description:
        - This command specifies the horizontal limit (tolerance) for a template mask to be used for
          limit testing. This indicates how far horizontally from the template source to create the
          mask. A series of examples showing how to use mask commands for typical tasks is included
          in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TEMPLate:TOLerance:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TEMPLate:TOLerance:HORizontal?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MASK:TEMPLate:TOLerance:HORizontal value`` command.

    SCPI Syntax:
        ```
        - MASK:TEMPLate:TOLerance:HORizontal <NR3>
        - MASK:TEMPLate:TOLerance:HORizontal?
        ```

    Info:
        - ``<NR3>`` is a floating point value that specifies the horizontal limit (tolerence) in
          milli-divisions. Range: 0 to 500 mDiv, resolution: 1mDiv, default: 200 mDiv. This value
          cannot be negative.
    """


class MaskTemplateTolerance(SCPICmdRead):
    """The ``MASK:TEMPLate:TOLerance`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TEMPLate:TOLerance?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TEMPLate:TOLerance?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.horizontal``: The ``MASK:TEMPLate:TOLerance:HORizontal`` command.
        - ``.vertical``: The ``MASK:TEMPLate:TOLerance:VERTical`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = MaskTemplateToleranceHorizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._vertical = MaskTemplateToleranceVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def horizontal(self) -> MaskTemplateToleranceHorizontal:
        """Return the ``MASK:TEMPLate:TOLerance:HORizontal`` command.

        Description:
            - This command specifies the horizontal limit (tolerance) for a template mask to be used
              for limit testing. This indicates how far horizontally from the template source to
              create the mask. A series of examples showing how to use mask commands for typical
              tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TEMPLate:TOLerance:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MASK:TEMPLate:TOLerance:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MASK:TEMPLate:TOLerance:HORizontal value`` command.

        SCPI Syntax:
            ```
            - MASK:TEMPLate:TOLerance:HORizontal <NR3>
            - MASK:TEMPLate:TOLerance:HORizontal?
            ```

        Info:
            - ``<NR3>`` is a floating point value that specifies the horizontal limit (tolerence) in
              milli-divisions. Range: 0 to 500 mDiv, resolution: 1mDiv, default: 200 mDiv. This
              value cannot be negative.
        """
        return self._horizontal

    @property
    def vertical(self) -> MaskTemplateToleranceVertical:
        """Return the ``MASK:TEMPLate:TOLerance:VERTical`` command.

        Description:
            - This command specifies the vertical limit (tolerance) for a template mask to be used
              for limit testing. This indicates how far vertically from the template source to
              create the mask. A series of examples showing how to use mask commands for typical
              tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TEMPLate:TOLerance:VERTical?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MASK:TEMPLate:TOLerance:VERTical?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MASK:TEMPLate:TOLerance:VERTical value`` command.

        SCPI Syntax:
            ```
            - MASK:TEMPLate:TOLerance:VERTical <NR3>
            - MASK:TEMPLate:TOLerance:VERTical?
            ```

        Info:
            - ``<NR3>`` is a floating point value that specifies the vertical limit (tolerence) in
              milli-divisions. Range: 0 to 1000 mDiv, resolution: 1 mDiv, default: 200 mDiv. This
              value cannot be negative.
        """
        return self._vertical


class MaskTemplateSource(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:TEMPLate:SOUrce`` command.

    Description:
        - This command, typically used for limit mask testing, specifies the source waveform to be
          used to create a template mask. The source can be either one of four channels, or one of
          four saved reference waveforms. See the ``SAVE:WAVEFORM`` commands for more information on
          creating reference waveforms. A series of examples showing how to use mask commands for
          typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TEMPLate:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TEMPLate:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:TEMPLate:SOUrce value`` command.

    SCPI Syntax:
        ```
        - MASK:TEMPLate:SOUrce {CH<x>|REF<x>}
        - MASK:TEMPLate:SOUrce?
        ```
    """


class MaskTemplateCreatemask(SCPICmdWriteNoArguments):
    """The ``MASK:TEMPLate:CREATEmask`` command.

    Description:
        - This command, used for limit mask testing, causes a template mask to be created based on
          the settings of the ``MASK:TEMPLATE:SOURCE``, ``MASK:TEMPLATE:TOLERANCE:HORIZONTAL``, and
          ``MASK:TEMPLATE:TOLERANCE:VERTICAL`` commands. If you do not specify horizontal or
          vertical tolerances, the default tolerance of one minor division will be used. A series of
          examples showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.write()`` method will send the ``MASK:TEMPLate:CREATEmask`` command.

    SCPI Syntax:
        ```
        - MASK:TEMPLate:CREATEmask
        ```
    """


class MaskTemplate(SCPICmdRead):
    """The ``MASK:TEMPLate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:TEMPLate?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:TEMPLate?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.createmask``: The ``MASK:TEMPLate:CREATEmask`` command.
        - ``.source``: The ``MASK:TEMPLate:SOUrce`` command.
        - ``.tolerance``: The ``MASK:TEMPLate:TOLerance`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._createmask = MaskTemplateCreatemask(device, f"{self._cmd_syntax}:CREATEmask")
        self._source = MaskTemplateSource(device, f"{self._cmd_syntax}:SOUrce")
        self._tolerance = MaskTemplateTolerance(device, f"{self._cmd_syntax}:TOLerance")

    @property
    def createmask(self) -> MaskTemplateCreatemask:
        """Return the ``MASK:TEMPLate:CREATEmask`` command.

        Description:
            - This command, used for limit mask testing, causes a template mask to be created based
              on the settings of the ``MASK:TEMPLATE:SOURCE``,
              ``MASK:TEMPLATE:TOLERANCE:HORIZONTAL``, and ``MASK:TEMPLATE:TOLERANCE:VERTICAL``
              commands. If you do not specify horizontal or vertical tolerances, the default
              tolerance of one minor division will be used. A series of examples showing how to use
              mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.write()`` method will send the ``MASK:TEMPLate:CREATEmask`` command.

        SCPI Syntax:
            ```
            - MASK:TEMPLate:CREATEmask
            ```
        """
        return self._createmask

    @property
    def source(self) -> MaskTemplateSource:
        """Return the ``MASK:TEMPLate:SOUrce`` command.

        Description:
            - This command, typically used for limit mask testing, specifies the source waveform to
              be used to create a template mask. The source can be either one of four channels, or
              one of four saved reference waveforms. See the ``SAVE:WAVEFORM`` commands for more
              information on creating reference waveforms. A series of examples showing how to use
              mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TEMPLate:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TEMPLate:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:TEMPLate:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - MASK:TEMPLate:SOUrce {CH<x>|REF<x>}
            - MASK:TEMPLate:SOUrce?
            ```
        """
        return self._source

    @property
    def tolerance(self) -> MaskTemplateTolerance:
        """Return the ``MASK:TEMPLate:TOLerance`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TEMPLate:TOLerance?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TEMPLate:TOLerance?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.horizontal``: The ``MASK:TEMPLate:TOLerance:HORizontal`` command.
            - ``.vertical``: The ``MASK:TEMPLate:TOLerance:VERTical`` command.
        """
        return self._tolerance


class MaskStoponviolation(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:STOPOnviolation`` command.

    Description:
        - This command stops the waveform acquisitions upon the first occurrence of a waveform
          violation. The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event to
          happen. After the event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to OFF
          automatically. You can also specify an action to be performed when acquisitions are
          stopped by using the commands such as ``MASK:TEST:SAVEWFM``, ``MASK:TEST:SAVEIMAGE``,
          ``MASK:TEST:AUXOUT:FAILURE``, ``MASK:TEST:HARDCOPY``, or ``MASK:TEST:SRQ:FAILURE``. A
          series of examples showing how to use mask commands for typical tasks is included in an
          appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:STOPOnviolation?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:STOPOnviolation?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:STOPOnviolation value`` command.

    SCPI Syntax:
        ```
        - MASK:STOPOnviolation {ON|OFF|<NR1>}
        - MASK:STOPOnviolation?
        ```

    Info:
        - ``ON`` stops waveform acquisition on the first occurrence of a mask violation.
        - ``OFF`` turns this feature off.
        - ``<NR1>=0`` turns this feature off ; any other value turns it on.
    """


class MaskStandard(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:STANdard`` command.

    Description:
        - This command replaces the existing mask, if any, with a specified standard mask. There are
          three categories of standard masks: ANSI T1.102, ITU-T, and USB. To ensure that Mask
          commands are enabled, use the command ``APPLICATION:TYPE LIMITMask``. A series of examples
          showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:STANdard?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:STANdard?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:STANdard value`` command.

    SCPI Syntax:
        ```
        - MASK:STANdard {DS1|DS1A|DS1C|DS2|DS3|DS4NA|DS4XNA|STS1Pulse|STS1Eye|STS3|STSX3|CLOCKCoax|CLOCKSymmetrical|DSOContra|DSODouble|DSOSingle|DSOTiming|G703DS1|DS1Rate|DS2RATECoax|DS2RATESymmetrical|G703DS3|DS3Rate|E1Coax|E1Symmetrical|E<x>|HST<x>|NONe|USER|LIMit}
        - MASK:STANdard?
        ```

    Info:
        - ``ANSI T1.102:``
        - ``DS1`` - DS1 1.544 Mb/s.
        - ``DS1A`` - DS1A 2.048 Mb/s.
        - ``DS1C`` - DS1C 3.152 Mb/s.
        - ``DS2`` - DS2 6.312 Mb/s.
        - ``DS3`` - DS3 44.736 Mb/s.
        - ``DS4NA`` - DS4NA 139.26 Mb/s.
        - ``DS4XNA`` - DS4NA Max Output 138.26 Mb/s.
        - ``STS1Pulse`` - STS-1 Pulse 51.84 Mb/s.
        - ``STS1Eye`` - STS-1 Eye 51.84 Mb/s.
        - ``STS3`` - STS-3 155.52 Mb/s.
        - ``STSX3`` - STS-3 Max Output 155.52 Mb/s.
        - ``ITU-T:``
        - ``CLOCKCoax`` - Clock Interface Coaxial Pair 2.048 Mb/s.
        - ``CLOCKSymmetrical`` - Clock Interface Symmetrical Pair 2.048 Mb/s.
        - ``DSOContra`` - DSO Data Contradirectional 64 kb/s.
        - ``DSODouble`` - DSO Double 64 kb/s.
        - ``DSOSingle`` - DSO Single 64 kb/s.
        - ``DSOTiming`` - DSO Timing 64 kb/s.
        - ``G703DS1`` - DS1 G.7031.544 Mb/s.
        - ``DS1Rate`` - DS1 Old Rate 1.544 Mb/s.
        - ``DS2RATECoax`` - DS2 Rate Coaxial Pair 6.312 Mb/s.
        - ``DS2RATESymmetrical`` - DS2 Rate Symmetrical Pair 6.312 Mb/s.
        - ``G703DS3`` - DS3 G.703 44.736 Mb/s.
        - ``DS3Rate`` - DS3 Old Rate 44.736 Mb/s.
        - ``E1Coax`` - E1 Coaxial Pair 2.048 Mb/s.
        - ``E1Symmetrical`` - E1 Symmetric Pair 2.048 Mb/s.
        - ``E2`` - E2 8.448 Mb/s.
        - ``E3`` - E3 34.368 Mb/s.
        - ``USB:``
        - ``HST1`` - ``HS:T1 480`` Mb/s.
        - ``HST2`` - ``HS:T1 480`` Mb/s.
        - ``HST3`` - ``HS:T1 480`` Mb/s.
        - ``HST4`` - ``HS:T1 480`` Mb/s.
        - ``HST5`` - ``HS:T1 480`` Mb/s.
        - ``HST6`` - ``HS:T1 480`` Mb/s.
        - ``LIMit, USER,`` and NONe can be input as well.
    """  # noqa: E501


class MaskSource(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:SOUrce`` command.

    Description:
        - This command specifies the mask source waveform to be used during pass/fail mask testing.
          Must be one of CH1 through CH4. A series of examples showing how to use mask commands for
          typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:SOUrce value`` command.

    SCPI Syntax:
        ```
        - MASK:SOUrce {CH<x>}
        - MASK:SOUrce?
        ```
    """


class MaskMarginPercent(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:MARgin:PERCent`` command.

    Description:
        - Sets or returns the tolerance for the mask test. A positive value expands the mask and a
          negative margin shrinks the mask by the specified percentage. A series of examples showing
          how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MARgin:PERCent?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MARgin:PERCent?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:MARgin:PERCent value`` command.

    SCPI Syntax:
        ```
        - MASK:MARgin:PERCent <NR3>
        - MASK:MARgin:PERCent?
        ```

    Info:
        - ``<NR3>`` is a floating point value that ranges from -50.0 to +50.0. The default is 5.
    """


class MaskMargin(SCPICmdRead):
    """The ``MASK:MARgin`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:MARgin?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:MARgin?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.percent``: The ``MASK:MARgin:PERCent`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._percent = MaskMarginPercent(device, f"{self._cmd_syntax}:PERCent")

    @property
    def percent(self) -> MaskMarginPercent:
        """Return the ``MASK:MARgin:PERCent`` command.

        Description:
            - Sets or returns the tolerance for the mask test. A positive value expands the mask and
              a negative margin shrinks the mask by the specified percentage. A series of examples
              showing how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MARgin:PERCent?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MARgin:PERCent?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:MARgin:PERCent value``
              command.

        SCPI Syntax:
            ```
            - MASK:MARgin:PERCent <NR3>
            - MASK:MARgin:PERCent?
            ```

        Info:
            - ``<NR3>`` is a floating point value that ranges from -50.0 to +50.0. The default is 5.
        """
        return self._percent


class MaskLock(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:LOCk`` command.

    Description:
        - This command locks the mask to the source waveform so that any changes made to the
          horizontal and/or vertical scale settings of the waveform will redraw the mask segments in
          proportion. This feature is useful for expanding the horizontal and/or vertical settings
          in order to zoom in on waveforms and masks, and visually examine violation areas in more
          detail. A series of examples showing how to use mask commands for typical tasks is
          included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:LOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:LOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:LOCk value`` command.

    SCPI Syntax:
        ```
        - MASK:LOCk {ON|OFF|<NR1>}
        - MASK:LOCk?
        ```

    Info:
        - ``ON`` turns on this feature, so that the mask is locked to the waveform.
        - ``OFF`` turns off this feature.
        - ``<NR1> = 0`` turns off this feature. Any other value turns it on.
    """


class MaskDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:DISplay`` command.

    Description:
        - This command controls whether a mask is displayed on the screen. This is useful for
          temporarily turning off masks without deleting them. Turning off the Mask Display when the
          Mask Test is on, turns off the Mask Test. A series of examples showing how to use mask
          commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:DISplay value`` command.

    SCPI Syntax:
        ```
        - MASK:DISplay {ON|OFF|1|0}
        - MASK:DISplay?
        ```

    Info:
        - ``ON`` shows the mask on the display. This is the default value.
        - ``OFF`` removes the mask from the display.
        - ``0`` removes the mask from the display;.
        - ``1`` shows the mask on the display.
    """


class MaskCustom(SCPICmdWrite):
    """The ``MASK:CUSTom`` command.

    Description:
        - This command initializes a custom mask using a default triangle segment 1 mask (
          ``:MASK:CUSTOM INIT`` ), or copies the currently active mask to the user-defined custom
          mask ( ``:MASK:CUSTOM COPYActive`` ). A series of examples showing how to use mask
          commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.write(value)`` method will send the ``MASK:CUSTom value`` command.

    SCPI Syntax:
        ```
        - MASK:CUSTom {INIT|COPYACTive}
        ```

    Info:
        - ``INIT`` sets the user-defined custom mask to its initialized state.
        - ``COPYACTive`` copies the currently active mask to the user-defined custom mask.
    """


class MaskCountWaveforms(SCPICmdRead):
    """The ``MASK:COUNt:WAVEFORMS`` command.

    Description:
        - This query returns the number of waveforms that have been acquired and processed during
          pass/fail mask testing. A series of examples showing how to use mask commands for typical
          tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:WAVEFORMS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:WAVEFORMS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:WAVEFORMS?
        ```
    """


class MaskCountViolations(SCPICmdRead):
    """The ``MASK:COUNt:VIOLATIONS`` command.

    Description:
        - This query returns the number of test violations that have occurred in the current mask
          pass/fail test. A test violation occurs when any part of a waveform falls within any mask
          segment. The default is 0. A series of examples showing how to use mask commands for
          typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:VIOLATIONS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:VIOLATIONS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:VIOLATIONS?
        ```
    """


class MaskCountTests(SCPICmdRead):
    """The ``MASK:COUNt:TESTS`` command.

    Description:
        - This query returns the number of pass/fail mask tests that have occurred. A series of
          examples showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:TESTS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:TESTS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:TESTS?
        ```
    """


class MaskCountSegItemHits(SCPICmdRead):
    """The ``MASK:COUNt:SEG<x>:HITS`` command.

    Description:
        - This query returns the number of hits for the specified mask segment. There are up to 8
          segments. A series of examples showing how to use mask commands for typical tasks is
          included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:SEG<x>:HITS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:SEG<x>:HITS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:SEG<x>:HITS?
        ```
    """


class MaskCountSegItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MASK:COUNt:SEG<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:SEG<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:SEG<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.hits``: The ``MASK:COUNt:SEG<x>:HITS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hits = MaskCountSegItemHits(device, f"{self._cmd_syntax}:HITS")

    @property
    def hits(self) -> MaskCountSegItemHits:
        """Return the ``MASK:COUNt:SEG<x>:HITS`` command.

        Description:
            - This query returns the number of hits for the specified mask segment. There are up to
              8 segments. A series of examples showing how to use mask commands for typical tasks is
              included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:SEG<x>:HITS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:SEG<x>:HITS?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:SEG<x>:HITS?
            ```
        """
        return self._hits


class MaskCountHits(SCPICmdRead):
    """The ``MASK:COUNt:HITS`` command.

    Description:
        - This query returns the sum of all hits in all mask segments. A series of examples showing
          how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:HITS?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:HITS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:HITS?
        ```
    """


class MaskCountFailures(SCPICmdRead):
    """The ``MASK:COUNt:FAILURES`` command.

    Description:
        - This query returns the number of pass/fail mask tests that have failed. A series of
          examples showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COUNt:FAILURES?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COUNt:FAILURES?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MASK:COUNt:FAILURES?
        ```
    """


class MaskCount(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:COUNt`` command.

    Description:
        - This command resets to zero the number of hits and failures for all mask segments. A
          series of examples showing how to use mask commands for typical tasks is included in an
          appendix.

    Usage:
        - Using the ``.write(value)`` method will send the ``MASK:COUNt value`` command.

    SCPI Syntax:
        ```
        - MASK:COUNt RESET
        ```

    Properties:
        - ``.failures``: The ``MASK:COUNt:FAILURES`` command.
        - ``.hits``: The ``MASK:COUNt:HITS`` command.
        - ``.seg``: The ``MASK:COUNt:SEG<x>`` command tree.
        - ``.tests``: The ``MASK:COUNt:TESTS`` command.
        - ``.violations``: The ``MASK:COUNt:VIOLATIONS`` command.
        - ``.waveforms``: The ``MASK:COUNt:WAVEFORMS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._failures = MaskCountFailures(device, f"{self._cmd_syntax}:FAILURES")
        self._hits = MaskCountHits(device, f"{self._cmd_syntax}:HITS")
        self._seg: Dict[int, MaskCountSegItem] = DefaultDictPassKeyToFactory(
            lambda x: MaskCountSegItem(device, f"{self._cmd_syntax}:SEG{x}")
        )
        self._tests = MaskCountTests(device, f"{self._cmd_syntax}:TESTS")
        self._violations = MaskCountViolations(device, f"{self._cmd_syntax}:VIOLATIONS")
        self._waveforms = MaskCountWaveforms(device, f"{self._cmd_syntax}:WAVEFORMS")

    @property
    def failures(self) -> MaskCountFailures:
        """Return the ``MASK:COUNt:FAILURES`` command.

        Description:
            - This query returns the number of pass/fail mask tests that have failed. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:FAILURES?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:FAILURES?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:FAILURES?
            ```
        """
        return self._failures

    @property
    def hits(self) -> MaskCountHits:
        """Return the ``MASK:COUNt:HITS`` command.

        Description:
            - This query returns the sum of all hits in all mask segments. A series of examples
              showing how to use mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:HITS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:HITS?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:HITS?
            ```
        """
        return self._hits

    @property
    def seg(self) -> Dict[int, MaskCountSegItem]:
        """Return the ``MASK:COUNt:SEG<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:SEG<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:SEG<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.hits``: The ``MASK:COUNt:SEG<x>:HITS`` command.
        """
        return self._seg

    @property
    def tests(self) -> MaskCountTests:
        """Return the ``MASK:COUNt:TESTS`` command.

        Description:
            - This query returns the number of pass/fail mask tests that have occurred. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:TESTS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:TESTS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:TESTS?
            ```
        """
        return self._tests

    @property
    def violations(self) -> MaskCountViolations:
        """Return the ``MASK:COUNt:VIOLATIONS`` command.

        Description:
            - This query returns the number of test violations that have occurred in the current
              mask pass/fail test. A test violation occurs when any part of a waveform falls within
              any mask segment. The default is 0. A series of examples showing how to use mask
              commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:VIOLATIONS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:VIOLATIONS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:VIOLATIONS?
            ```
        """
        return self._violations

    @property
    def waveforms(self) -> MaskCountWaveforms:
        """Return the ``MASK:COUNt:WAVEFORMS`` command.

        Description:
            - This query returns the number of waveforms that have been acquired and processed
              during pass/fail mask testing. A series of examples showing how to use mask commands
              for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COUNt:WAVEFORMS?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COUNt:WAVEFORMS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MASK:COUNt:WAVEFORMS?
            ```
        """
        return self._waveforms


class MaskCopyUser(SCPICmdWriteNoArguments):
    """The ``MASK:COPy:USER`` command.

    Description:
        - This creates a user-defined custom mask by making a copy of the source mask that was
          specified prior with the command . The source mask could be a standard, limit or another
          custom mask. A series of examples showing how to use mask commands for typical tasks is
          included in an appendix.

    Usage:
        - Using the ``.write()`` method will send the ``MASK:COPy:USER`` command.

    SCPI Syntax:
        ```
        - MASK:COPy:USER
        ```
    """


class MaskCopySource(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:COPy:SOUrce`` command.

    Description:
        - This command specifies the mask that is to be copied to a user-defined custom mask. The
          specified mask is not copied until after the ``MASK:COPy:USER`` command is executed. Note
          that in addition to a standard mask, LIMit, USER and NONe can also be specified. A series
          of examples showing how to use mask commands for typical tasks is included in an appendix.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COPy:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COPy:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:COPy:SOUrce value`` command.

    SCPI Syntax:
        ```
        - MASK:COPy:SOUrce {DS1|DS1A|DS1C|DS2|DS3|DS4NA|DS4XNA|STS1Pulse|STS1Eye|STS3|STSX3|CLOCKCoax|CLOCKSymmetrical|DSOContra|DSODouble|DSOSingle|DSOTiming|G703DS1|DS1Rate|DS2RATECoax|DS2RATESymmetrical|G703DS3|DS3Rate|E1Coax|E1Symmetrical|E<x>|HST<x>|NONe|USER|LIMit}
        - MASK:COPy:SOUrce?
        ```

    Info:
        - ``ANSI T1.102:``
        - ``DS1`` - DS1 1.544 Mb/s.
        - ``DS1A`` - DS1A 2.048 Mb/s.
        - ``DS1C`` - DS1C 3.152 Mb/s.
        - ``DS2`` - DS2 6.312 Mb/s.
        - ``DS3`` - DS3 44.736 Mb/s.
        - ``DS4NA`` - DS4NA 139.26 Mb/s.
        - ``DS4XNA`` - DS4NA Max Output 138.26 Mb/s.
        - ``STS1Pulse`` - STS-1 Pulse 51.84 Mb/s.
        - ``STS1Eye`` - STS-1 Eye 51.84 Mb/s.
        - ``STS3`` - STS-3 155.52 Mb/s.
        - ``STSX3`` - STS-3 Max Output 155.52 Mb/s.
        - ``ITU-T:``
        - ``CLOCKCoax`` - Clock Interface Coaxial Pair 2.048 Mb/s.
        - ``CLOCKSymmetrical`` - Clock Interface Symmetrical Pair 2.048 Mb/s.
        - ``DSOContra`` - DSO Data Contradirectional 64 kb/s.
        - ``DSODouble`` - DSO Double 64 kb/s.
        - ``DSOSingle`` - DSO Single 64 kb/s.
        - ``DSOTiming`` - DSO Timing 64 kb/s.
        - ``G703DS1`` - DS1 G.7031.544 Mb/s.
        - ``DS1Rate`` - DS1 Old Rate 1.544 Mb/s.
        - ``DS2RATECoax`` - DS2 Rate Coaxial Pair 6.312 Mb/s.
        - ``DS2RATESymmetrical`` - DS2 Rate Symmetrical Pair 6.312 Mb/s.
        - ``G703DS3`` - DS3 G.703 44.736 Mb/s.
        - ``DS3Rate`` - DS3 Old Rate 44.736 Mb/s.
        - ``E1Coax`` - E1 Coaxial Pair 2.048 Mb/s.
        - ``E1Symmetrical`` - E1 Symmetric Pair 2.048 Mb/s.
        - ``E2`` - E2 8.448 Mb/s.
        - ``E3`` - E3 34.368 Mb/s.
        - ``USB:``
        - ``HST1`` - ``HS:T1 480`` Mb/s.
        - ``HST2`` - ``HS:T1 480`` Mb/s.
        - ``HST3`` - ``HS:T1 480`` Mb/s.
        - ``HST4`` - ``HS:T1 480`` Mb/s.
        - ``HST5`` - ``HS:T1 480`` Mb/s.
        - ``HST6`` - ``HS:T1 480`` Mb/s.
        - ``LIMit, USER,`` and NONe can be input as well.
    """  # noqa: E501


class MaskCopy(SCPICmdRead):
    """The ``MASK:COPy`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:COPy?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:COPy?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``MASK:COPy:SOUrce`` command.
        - ``.user``: The ``MASK:COPy:USER`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = MaskCopySource(device, f"{self._cmd_syntax}:SOUrce")
        self._user = MaskCopyUser(device, f"{self._cmd_syntax}:USER")

    @property
    def source(self) -> MaskCopySource:
        """Return the ``MASK:COPy:SOUrce`` command.

        Description:
            - This command specifies the mask that is to be copied to a user-defined custom mask.
              The specified mask is not copied until after the ``MASK:COPy:USER`` command is
              executed. Note that in addition to a standard mask, LIMit, USER and NONe can also be
              specified. A series of examples showing how to use mask commands for typical tasks is
              included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COPy:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COPy:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:COPy:SOUrce value`` command.

        SCPI Syntax:
            ```
            - MASK:COPy:SOUrce {DS1|DS1A|DS1C|DS2|DS3|DS4NA|DS4XNA|STS1Pulse|STS1Eye|STS3|STSX3|CLOCKCoax|CLOCKSymmetrical|DSOContra|DSODouble|DSOSingle|DSOTiming|G703DS1|DS1Rate|DS2RATECoax|DS2RATESymmetrical|G703DS3|DS3Rate|E1Coax|E1Symmetrical|E<x>|HST<x>|NONe|USER|LIMit}
            - MASK:COPy:SOUrce?
            ```

        Info:
            - ``ANSI T1.102:``
            - ``DS1`` - DS1 1.544 Mb/s.
            - ``DS1A`` - DS1A 2.048 Mb/s.
            - ``DS1C`` - DS1C 3.152 Mb/s.
            - ``DS2`` - DS2 6.312 Mb/s.
            - ``DS3`` - DS3 44.736 Mb/s.
            - ``DS4NA`` - DS4NA 139.26 Mb/s.
            - ``DS4XNA`` - DS4NA Max Output 138.26 Mb/s.
            - ``STS1Pulse`` - STS-1 Pulse 51.84 Mb/s.
            - ``STS1Eye`` - STS-1 Eye 51.84 Mb/s.
            - ``STS3`` - STS-3 155.52 Mb/s.
            - ``STSX3`` - STS-3 Max Output 155.52 Mb/s.
            - ``ITU-T:``
            - ``CLOCKCoax`` - Clock Interface Coaxial Pair 2.048 Mb/s.
            - ``CLOCKSymmetrical`` - Clock Interface Symmetrical Pair 2.048 Mb/s.
            - ``DSOContra`` - DSO Data Contradirectional 64 kb/s.
            - ``DSODouble`` - DSO Double 64 kb/s.
            - ``DSOSingle`` - DSO Single 64 kb/s.
            - ``DSOTiming`` - DSO Timing 64 kb/s.
            - ``G703DS1`` - DS1 G.7031.544 Mb/s.
            - ``DS1Rate`` - DS1 Old Rate 1.544 Mb/s.
            - ``DS2RATECoax`` - DS2 Rate Coaxial Pair 6.312 Mb/s.
            - ``DS2RATESymmetrical`` - DS2 Rate Symmetrical Pair 6.312 Mb/s.
            - ``G703DS3`` - DS3 G.703 44.736 Mb/s.
            - ``DS3Rate`` - DS3 Old Rate 44.736 Mb/s.
            - ``E1Coax`` - E1 Coaxial Pair 2.048 Mb/s.
            - ``E1Symmetrical`` - E1 Symmetric Pair 2.048 Mb/s.
            - ``E2`` - E2 8.448 Mb/s.
            - ``E3`` - E3 34.368 Mb/s.
            - ``USB:``
            - ``HST1`` - ``HS:T1 480`` Mb/s.
            - ``HST2`` - ``HS:T1 480`` Mb/s.
            - ``HST3`` - ``HS:T1 480`` Mb/s.
            - ``HST4`` - ``HS:T1 480`` Mb/s.
            - ``HST5`` - ``HS:T1 480`` Mb/s.
            - ``HST6`` - ``HS:T1 480`` Mb/s.
            - ``LIMit, USER,`` and NONe can be input as well.
        """  # noqa: E501
        return self._source

    @property
    def user(self) -> MaskCopyUser:
        """Return the ``MASK:COPy:USER`` command.

        Description:
            - This creates a user-defined custom mask by making a copy of the source mask that was
              specified prior with the command . The source mask could be a standard, limit or
              another custom mask. A series of examples showing how to use mask commands for typical
              tasks is included in an appendix.

        Usage:
            - Using the ``.write()`` method will send the ``MASK:COPy:USER`` command.

        SCPI Syntax:
            ```
            - MASK:COPy:USER
            ```
        """
        return self._user


class MaskActoneventEnable(SCPICmdWrite, SCPICmdRead):
    """The ``MASK:ACTONEVent:ENable`` command.

    Description:
        - This command enables or disables the mask act on event.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:ACTONEVent:ENable?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:ACTONEVent:ENable?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MASK:ACTONEVent:ENable value`` command.

    SCPI Syntax:
        ```
        - MASK:ACTONEVent:ENable {ON|OFF}
        - MASK:ACTONEVent:ENable?
        ```

    Info:
        - ``ON`` enables the mask act on event.
        - ``OFF`` disables the mask act on event.
    """


class MaskActonevent(SCPICmdRead):
    """The ``MASK:ACTONEVent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK:ACTONEVent?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK:ACTONEVent?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``MASK:ACTONEVent:ENable`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = MaskActoneventEnable(device, f"{self._cmd_syntax}:ENable")

    @property
    def enable(self) -> MaskActoneventEnable:
        """Return the ``MASK:ACTONEVent:ENable`` command.

        Description:
            - This command enables or disables the mask act on event.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:ACTONEVent:ENable?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:ACTONEVent:ENable?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:ACTONEVent:ENable value``
              command.

        SCPI Syntax:
            ```
            - MASK:ACTONEVent:ENable {ON|OFF}
            - MASK:ACTONEVent:ENable?
            ```

        Info:
            - ``ON`` enables the mask act on event.
            - ``OFF`` disables the mask act on event.
        """
        return self._enable


#  pylint: disable=too-many-instance-attributes
class Mask(SCPICmdRead):
    """The ``MASK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MASK?`` query.
        - Using the ``.verify(value)`` method will send the ``MASK?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.actonevent``: The ``MASK:ACTONEVent`` command tree.
        - ``.copy``: The ``MASK:COPy`` command tree.
        - ``.count``: The ``MASK:COUNt`` command.
        - ``.custom``: The ``MASK:CUSTom`` command.
        - ``.display``: The ``MASK:DISplay`` command.
        - ``.lock``: The ``MASK:LOCk`` command.
        - ``.margin``: The ``MASK:MARgin`` command tree.
        - ``.source``: The ``MASK:SOUrce`` command.
        - ``.standard``: The ``MASK:STANdard`` command.
        - ``.stoponviolation``: The ``MASK:STOPOnviolation`` command.
        - ``.template``: The ``MASK:TEMPLate`` command tree.
        - ``.test``: The ``MASK:TESt`` command tree.
        - ``.user``: The ``MASK:USER`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MASK") -> None:
        super().__init__(device, cmd_syntax)
        self._actonevent = MaskActonevent(device, f"{self._cmd_syntax}:ACTONEVent")
        self._copy = MaskCopy(device, f"{self._cmd_syntax}:COPy")
        self._count = MaskCount(device, f"{self._cmd_syntax}:COUNt")
        self._custom = MaskCustom(device, f"{self._cmd_syntax}:CUSTom")
        self._display = MaskDisplay(device, f"{self._cmd_syntax}:DISplay")
        self._lock = MaskLock(device, f"{self._cmd_syntax}:LOCk")
        self._margin = MaskMargin(device, f"{self._cmd_syntax}:MARgin")
        self._source = MaskSource(device, f"{self._cmd_syntax}:SOUrce")
        self._standard = MaskStandard(device, f"{self._cmd_syntax}:STANdard")
        self._stoponviolation = MaskStoponviolation(device, f"{self._cmd_syntax}:STOPOnviolation")
        self._template = MaskTemplate(device, f"{self._cmd_syntax}:TEMPLate")
        self._test = MaskTest(device, f"{self._cmd_syntax}:TESt")
        self._user = MaskUser(device, f"{self._cmd_syntax}:USER")

    @property
    def actonevent(self) -> MaskActonevent:
        """Return the ``MASK:ACTONEVent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:ACTONEVent?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:ACTONEVent?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``MASK:ACTONEVent:ENable`` command.
        """
        return self._actonevent

    @property
    def copy(self) -> MaskCopy:
        """Return the ``MASK:COPy`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:COPy?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:COPy?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``MASK:COPy:SOUrce`` command.
            - ``.user``: The ``MASK:COPy:USER`` command.
        """
        return self._copy

    @property
    def count(self) -> MaskCount:
        """Return the ``MASK:COUNt`` command.

        Description:
            - This command resets to zero the number of hits and failures for all mask segments. A
              series of examples showing how to use mask commands for typical tasks is included in
              an appendix.

        Usage:
            - Using the ``.write(value)`` method will send the ``MASK:COUNt value`` command.

        SCPI Syntax:
            ```
            - MASK:COUNt RESET
            ```

        Sub-properties:
            - ``.failures``: The ``MASK:COUNt:FAILURES`` command.
            - ``.hits``: The ``MASK:COUNt:HITS`` command.
            - ``.seg``: The ``MASK:COUNt:SEG<x>`` command tree.
            - ``.tests``: The ``MASK:COUNt:TESTS`` command.
            - ``.violations``: The ``MASK:COUNt:VIOLATIONS`` command.
            - ``.waveforms``: The ``MASK:COUNt:WAVEFORMS`` command.
        """
        return self._count

    @property
    def custom(self) -> MaskCustom:
        """Return the ``MASK:CUSTom`` command.

        Description:
            - This command initializes a custom mask using a default triangle segment 1 mask (
              ``:MASK:CUSTOM INIT`` ), or copies the currently active mask to the user-defined
              custom mask ( ``:MASK:CUSTOM COPYActive`` ). A series of examples showing how to use
              mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.write(value)`` method will send the ``MASK:CUSTom value`` command.

        SCPI Syntax:
            ```
            - MASK:CUSTom {INIT|COPYACTive}
            ```

        Info:
            - ``INIT`` sets the user-defined custom mask to its initialized state.
            - ``COPYACTive`` copies the currently active mask to the user-defined custom mask.
        """
        return self._custom

    @property
    def display(self) -> MaskDisplay:
        """Return the ``MASK:DISplay`` command.

        Description:
            - This command controls whether a mask is displayed on the screen. This is useful for
              temporarily turning off masks without deleting them. Turning off the Mask Display when
              the Mask Test is on, turns off the Mask Test. A series of examples showing how to use
              mask commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:DISplay?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:DISplay?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:DISplay value`` command.

        SCPI Syntax:
            ```
            - MASK:DISplay {ON|OFF|1|0}
            - MASK:DISplay?
            ```

        Info:
            - ``ON`` shows the mask on the display. This is the default value.
            - ``OFF`` removes the mask from the display.
            - ``0`` removes the mask from the display;.
            - ``1`` shows the mask on the display.
        """
        return self._display

    @property
    def lock(self) -> MaskLock:
        """Return the ``MASK:LOCk`` command.

        Description:
            - This command locks the mask to the source waveform so that any changes made to the
              horizontal and/or vertical scale settings of the waveform will redraw the mask
              segments in proportion. This feature is useful for expanding the horizontal and/or
              vertical settings in order to zoom in on waveforms and masks, and visually examine
              violation areas in more detail. A series of examples showing how to use mask commands
              for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:LOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:LOCk?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:LOCk value`` command.

        SCPI Syntax:
            ```
            - MASK:LOCk {ON|OFF|<NR1>}
            - MASK:LOCk?
            ```

        Info:
            - ``ON`` turns on this feature, so that the mask is locked to the waveform.
            - ``OFF`` turns off this feature.
            - ``<NR1> = 0`` turns off this feature. Any other value turns it on.
        """
        return self._lock

    @property
    def margin(self) -> MaskMargin:
        """Return the ``MASK:MARgin`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:MARgin?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:MARgin?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.percent``: The ``MASK:MARgin:PERCent`` command.
        """
        return self._margin

    @property
    def source(self) -> MaskSource:
        """Return the ``MASK:SOUrce`` command.

        Description:
            - This command specifies the mask source waveform to be used during pass/fail mask
              testing. Must be one of CH1 through CH4. A series of examples showing how to use mask
              commands for typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:SOUrce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:SOUrce value`` command.

        SCPI Syntax:
            ```
            - MASK:SOUrce {CH<x>}
            - MASK:SOUrce?
            ```
        """
        return self._source

    @property
    def standard(self) -> MaskStandard:
        """Return the ``MASK:STANdard`` command.

        Description:
            - This command replaces the existing mask, if any, with a specified standard mask. There
              are three categories of standard masks: ANSI T1.102, ITU-T, and USB. To ensure that
              Mask commands are enabled, use the command ``APPLICATION:TYPE LIMITMask``. A series of
              examples showing how to use mask commands for typical tasks is included in an
              appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:STANdard?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:STANdard?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:STANdard value`` command.

        SCPI Syntax:
            ```
            - MASK:STANdard {DS1|DS1A|DS1C|DS2|DS3|DS4NA|DS4XNA|STS1Pulse|STS1Eye|STS3|STSX3|CLOCKCoax|CLOCKSymmetrical|DSOContra|DSODouble|DSOSingle|DSOTiming|G703DS1|DS1Rate|DS2RATECoax|DS2RATESymmetrical|G703DS3|DS3Rate|E1Coax|E1Symmetrical|E<x>|HST<x>|NONe|USER|LIMit}
            - MASK:STANdard?
            ```

        Info:
            - ``ANSI T1.102:``
            - ``DS1`` - DS1 1.544 Mb/s.
            - ``DS1A`` - DS1A 2.048 Mb/s.
            - ``DS1C`` - DS1C 3.152 Mb/s.
            - ``DS2`` - DS2 6.312 Mb/s.
            - ``DS3`` - DS3 44.736 Mb/s.
            - ``DS4NA`` - DS4NA 139.26 Mb/s.
            - ``DS4XNA`` - DS4NA Max Output 138.26 Mb/s.
            - ``STS1Pulse`` - STS-1 Pulse 51.84 Mb/s.
            - ``STS1Eye`` - STS-1 Eye 51.84 Mb/s.
            - ``STS3`` - STS-3 155.52 Mb/s.
            - ``STSX3`` - STS-3 Max Output 155.52 Mb/s.
            - ``ITU-T:``
            - ``CLOCKCoax`` - Clock Interface Coaxial Pair 2.048 Mb/s.
            - ``CLOCKSymmetrical`` - Clock Interface Symmetrical Pair 2.048 Mb/s.
            - ``DSOContra`` - DSO Data Contradirectional 64 kb/s.
            - ``DSODouble`` - DSO Double 64 kb/s.
            - ``DSOSingle`` - DSO Single 64 kb/s.
            - ``DSOTiming`` - DSO Timing 64 kb/s.
            - ``G703DS1`` - DS1 G.7031.544 Mb/s.
            - ``DS1Rate`` - DS1 Old Rate 1.544 Mb/s.
            - ``DS2RATECoax`` - DS2 Rate Coaxial Pair 6.312 Mb/s.
            - ``DS2RATESymmetrical`` - DS2 Rate Symmetrical Pair 6.312 Mb/s.
            - ``G703DS3`` - DS3 G.703 44.736 Mb/s.
            - ``DS3Rate`` - DS3 Old Rate 44.736 Mb/s.
            - ``E1Coax`` - E1 Coaxial Pair 2.048 Mb/s.
            - ``E1Symmetrical`` - E1 Symmetric Pair 2.048 Mb/s.
            - ``E2`` - E2 8.448 Mb/s.
            - ``E3`` - E3 34.368 Mb/s.
            - ``USB:``
            - ``HST1`` - ``HS:T1 480`` Mb/s.
            - ``HST2`` - ``HS:T1 480`` Mb/s.
            - ``HST3`` - ``HS:T1 480`` Mb/s.
            - ``HST4`` - ``HS:T1 480`` Mb/s.
            - ``HST5`` - ``HS:T1 480`` Mb/s.
            - ``HST6`` - ``HS:T1 480`` Mb/s.
            - ``LIMit, USER,`` and NONe can be input as well.
        """  # noqa: E501
        return self._standard

    @property
    def stoponviolation(self) -> MaskStoponviolation:
        """Return the ``MASK:STOPOnviolation`` command.

        Description:
            - This command stops the waveform acquisitions upon the first occurrence of a waveform
              violation. The ``MASK:ACTONEVENT:ENABLE`` command should be set to ON for this event
              to happen. After the event occurs ``MASK:ACTONEVENT:ENABLE`` command will be set to
              OFF automatically. You can also specify an action to be performed when acquisitions
              are stopped by using the commands such as ``MASK:TEST:SAVEWFM``,
              ``MASK:TEST:SAVEIMAGE``, ``MASK:TEST:AUXOUT:FAILURE``, ``MASK:TEST:HARDCOPY``, or
              ``MASK:TEST:SRQ:FAILURE``. A series of examples showing how to use mask commands for
              typical tasks is included in an appendix.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:STOPOnviolation?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:STOPOnviolation?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MASK:STOPOnviolation value``
              command.

        SCPI Syntax:
            ```
            - MASK:STOPOnviolation {ON|OFF|<NR1>}
            - MASK:STOPOnviolation?
            ```

        Info:
            - ``ON`` stops waveform acquisition on the first occurrence of a mask violation.
            - ``OFF`` turns this feature off.
            - ``<NR1>=0`` turns this feature off ; any other value turns it on.
        """
        return self._stoponviolation

    @property
    def template(self) -> MaskTemplate:
        """Return the ``MASK:TEMPLate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TEMPLate?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TEMPLate?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.createmask``: The ``MASK:TEMPLate:CREATEmask`` command.
            - ``.source``: The ``MASK:TEMPLate:SOUrce`` command.
            - ``.tolerance``: The ``MASK:TEMPLate:TOLerance`` command tree.
        """
        return self._template

    @property
    def test(self) -> MaskTest:
        """Return the ``MASK:TESt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:TESt?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:TESt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.auxout``: The ``MASK:TESt:AUXout`` command tree.
            - ``.completion``: The ``MASK:TESt:COMPLetion`` command tree.
            - ``.delay``: The ``MASK:TESt:DELay`` command.
            - ``.hardcopy``: The ``MASK:TESt:HARDCopy`` command.
            - ``.repeat``: The ``MASK:TESt:REPeat`` command.
            - ``.saveimage``: The ``MASK:TESt:SAVEIMAGE`` command.
            - ``.savewfm``: The ``MASK:TESt:SAVEWFM`` command.
            - ``.srq``: The ``MASK:TESt:SRQ`` command tree.
            - ``.state``: The ``MASK:TESt:STATE`` command.
            - ``.status``: The ``MASK:TESt:STATus`` command.
            - ``.stop``: The ``MASK:TESt:STOP`` command tree.
            - ``.threshold``: The ``MASK:TESt:THReshold`` command.
            - ``.time``: The ``MASK:TESt:TIME`` command.
            - ``.waveform``: The ``MASK:TESt:WAVEform`` command.
        """
        return self._test

    @property
    def user(self) -> MaskUser:
        """Return the ``MASK:USER`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MASK:USER?`` query.
            - Using the ``.verify(value)`` method will send the ``MASK:USER?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``MASK:USER:AMPLitude`` command.
            - ``.hscale``: The ``MASK:USER:HSCAle`` command.
            - ``.htrigpos``: The ``MASK:USER:HTRIGPOS`` command.
            - ``.label``: The ``MASK:USER:LABel`` command.
            - ``.recordlength``: The ``MASK:USER:RECOrdlength`` command.
            - ``.trigtosamp``: The ``MASK:USER:TRIGTOSAMP`` command.
            - ``.voffset``: The ``MASK:USER:VOFFSet`` command.
            - ``.vpos``: The ``MASK:USER:VPOS`` command.
            - ``.vscale``: The ``MASK:USER:VSCAle`` command.
            - ``.width``: The ``MASK:USER:WIDth`` command.
            - ``.seg``: The ``MASK:USER:SEG<x>`` command.
            - ``.mask``: The ``MASK:USER:MASK<x>`` command.
        """
        return self._user
