# pylint: disable=line-too-long
"""The math commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MATH<x>:DEFine <QString>
    - MATH<x>:DEFine?
    - MATH<x>:FILTer:MODe {CENTered|SHIFted}
    - MATH<x>:FILTer:MODe?
    - MATH<x>:FILTer:RISetime <NR3>
    - MATH<x>:FILTer:RISetime?
    - MATH<x>:LABel:NAMe <QString>
    - MATH<x>:LABel:NAMe?
    - MATH<x>:LABel:XPOS <NR1>
    - MATH<x>:LABel:XPOS?
    - MATH<x>:LABel:YPOS <NR1>
    - MATH<x>:LABel:YPOS?
    - MATH<x>:NUMAVg <NR1>
    - MATH<x>:NUMAVg?
    - MATH<x>:SPECTral:CENTER <NR3>
    - MATH<x>:SPECTral:CENTER?
    - MATH<x>:SPECTral:GATEPOS <NR3>
    - MATH<x>:SPECTral:GATEPOS?
    - MATH<x>:SPECTral:GATEWIDTH <NR3>
    - MATH<x>:SPECTral:GATEWIDTH?
    - MATH<x>:SPECTral:LOCk {ON|OFF|<NR1>}
    - MATH<x>:SPECTral:LOCk?
    - MATH<x>:SPECTral:MAG {LINEAr|DB|DBM}
    - MATH<x>:SPECTral:MAG?
    - MATH<x>:SPECTral:PHASE {DEGrees|RADians|GROUPDelay}
    - MATH<x>:SPECTral:PHASE?
    - MATH<x>:SPECTral:REFLEVELOffset {DBM|<NR3>}
    - MATH<x>:SPECTral:REFLEVELOffset?
    - MATH<x>:SPECTral:REFLevel <NR3>
    - MATH<x>:SPECTral:REFLevel?
    - MATH<x>:SPECTral:RESBw <NR3>
    - MATH<x>:SPECTral:RESBw?
    - MATH<x>:SPECTral:SPAN {<NR3>|FULl}
    - MATH<x>:SPECTral:SPAN?
    - MATH<x>:SPECTral:SUPPress <NR3>
    - MATH<x>:SPECTral:SUPPress?
    - MATH<x>:SPECTral:UNWRap {ON|OFF|<NR1>}
    - MATH<x>:SPECTral:UNWRap?
    - MATH<x>:SPECTral:WINdow {RECTANGular|HAMMing|HANNing|KAISERBessel|BLACKMANHarris|FLATTOP2|GAUSSian|TEKEXPonential}
    - MATH<x>:SPECTral:WINdow?
    - MATH<x>:SPECTral?
    - MATH<x>:THRESHold <NR3>
    - MATH<x>:THRESHold?
    - MATH<x>:UNITString <QString>
    - MATH<x>:UNITString?
    - MATH<x>:VERTical:AUTOSCale {ON|OFF|<NR1>}
    - MATH<x>:VERTical:AUTOSCale?
    - MATH<x>:VERTical:POSition <NR3>
    - MATH<x>:VERTical:POSition?
    - MATH<x>:VERTical:SCAle <NR3>
    - MATH<x>:VERTical:SCAle?
    - MATH<x>?
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MathItemVerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:VERTical:SCAle`` command.

    Description:
        - This command sets or queries the vertical scale of the specified math waveform. The Math
          waveform is specified by x, which ranges from 1 through 4. This command is equivalent to
          selecting Position/Scale from the Math menu and then entering a Vert Scale value or
          adjusting the front panel Vertical SCALE knob. Each waveform has its own vertical scale
          parameter. For a signal with constant amplitude, increasing the scale causes the waveform
          to be displayed smaller. Decreasing the scale causes the waveform to be displayed larger.
          Scale affects all waveforms. For reference and math waveforms, the scale setting controls
          the display only, graphically scaling these waveforms and having no affect on the
          acquisition hardware. Be aware that autoscaling occurs when a math waveform is first
          defined and enabled, or when a math string changes. After the math waveform is computed
          for the first time, the instrument determines the min + max of that waveform data. Then,
          the instrument sets the math position so that (min + max)/2 is in the center of the
          screen. In addition, the instrument sets the math scale so that the range of the min and
          max covers 6 divisions. This autoscaling process can take up to 1/2 second to complete and
          will override any vertical scale or position commands for that math waveform received
          during this time. You should insert an appropriate pause in your program after defining
          and enabling a math waveform before changing its position or scale.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:VERTical:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:VERTical:SCAle value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:VERTical:SCAle <NR3>
        - MATH<x>:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is the scale in volts, amps or watts per division. The range is from 100.0E-36
          through 100.0E+36.
    """


class MathItemVerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:VERTical:POSition`` command.

    Description:
        - This command sets or queries the vertical position of the specified Math waveform. The
          Math waveform is specified by x, which ranges from 1 through 4. The position value is
          usually applied to the signal before it is digitized. The highest three units/div scale
          ranges of a given math are implemented by changing the way the acquired data is displayed.
          When the instrument is operating in any of these highest three scale ranges, the position
          control operates only on the signal after it is digitized. Note that if a signal that
          exceeds the range of the digitizer in one of these three scale ranges is repositioned, the
          displayed waveform will contain clipped values on-screen. This command is equivalent to
          selecting Position/Scale from the Math menu and then entering a Vert Pos value or
          adjusting the front panel Vertical POSITION knob. Increasing the position value of a
          waveform causes the waveform to move up, and decreasing the position value causes the
          waveform to move down. Position adjusts only the display position of a waveform, whether a
          channel, math, or reference waveform. The position value determines the vertical graticule
          coordinate at which input signal values, equal to the present offset setting for that
          reference, are displayed. For example, if the position for Math 3 is set to 2.0 and the
          offset is set to 3.0, then the input signals equal to 3.0 are displayed 2.0 divisions
          above the center of the screen. Be aware that autoscaling occurs when a math waveform is
          first defined and enabled, or when a math string changes. After the math waveform is
          computed for the first time, the instrument determines the min + max of that waveform
          data. Then, the instrument sets the math position so that (min + max)/2 is in the center
          of the screen. In addition, the instrument sets the math scale so that the range of the
          min and max cover 6 divisions. This autoscaling process can take up to 1/2 second to
          complete and will override any vertical scale or position commands for that math waveform
          received during this time. You should insert an appropriate pause in your program after
          defining and enabling a math waveform before changing its position or scale.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:VERTical:POSition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:VERTical:POSition value``
          command.

    SCPI Syntax:
        ```
        - MATH<x>:VERTical:POSition <NR3>
        - MATH<x>:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is the desired position control in divisions from the center graticule.
    """


class MathItemVerticalAutoscale(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:VERTical:AUTOSCale`` command.

    Description:
        - This command sets or queries auto-scaling of the specified math waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:VERTical:AUTOSCale?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:VERTical:AUTOSCale?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:VERTical:AUTOSCale value``
          command.

    SCPI Syntax:
        ```
        - MATH<x>:VERTical:AUTOSCale {ON|OFF|<NR1>}
        - MATH<x>:VERTical:AUTOSCale?
        ```

    Info:
        - ``ON, 1`` - enables auto-scaling of new math waveforms. (This is the default).
        - ``OFF, 2`` - math waveforms will not be scaled after activation, and will use the current
          ``:MATH<x>:VERTical:SCAle`` and ``:MATH<x>:VERTical:POSition`` values.
    """


class MathItemVertical(SCPICmdRead):
    """The ``MATH<x>:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:VERTical?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.autoscale``: The ``MATH<x>:VERTical:AUTOSCale`` command.
        - ``.position``: The ``MATH<x>:VERTical:POSition`` command.
        - ``.scale``: The ``MATH<x>:VERTical:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autoscale = MathItemVerticalAutoscale(device, f"{self._cmd_syntax}:AUTOSCale")
        self._position = MathItemVerticalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = MathItemVerticalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def autoscale(self) -> MathItemVerticalAutoscale:
        """Return the ``MATH<x>:VERTical:AUTOSCale`` command.

        Description:
            - This command sets or queries auto-scaling of the specified math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:VERTical:AUTOSCale?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:VERTical:AUTOSCale?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:VERTical:AUTOSCale value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:VERTical:AUTOSCale {ON|OFF|<NR1>}
            - MATH<x>:VERTical:AUTOSCale?
            ```

        Info:
            - ``ON, 1`` - enables auto-scaling of new math waveforms. (This is the default).
            - ``OFF, 2`` - math waveforms will not be scaled after activation, and will use the
              current ``:MATH<x>:VERTical:SCAle`` and ``:MATH<x>:VERTical:POSition`` values.
        """
        return self._autoscale

    @property
    def position(self) -> MathItemVerticalPosition:
        """Return the ``MATH<x>:VERTical:POSition`` command.

        Description:
            - This command sets or queries the vertical position of the specified Math waveform. The
              Math waveform is specified by x, which ranges from 1 through 4. The position value is
              usually applied to the signal before it is digitized. The highest three units/div
              scale ranges of a given math are implemented by changing the way the acquired data is
              displayed. When the instrument is operating in any of these highest three scale
              ranges, the position control operates only on the signal after it is digitized. Note
              that if a signal that exceeds the range of the digitizer in one of these three scale
              ranges is repositioned, the displayed waveform will contain clipped values on-screen.
              This command is equivalent to selecting Position/Scale from the Math menu and then
              entering a Vert Pos value or adjusting the front panel Vertical POSITION knob.
              Increasing the position value of a waveform causes the waveform to move up, and
              decreasing the position value causes the waveform to move down. Position adjusts only
              the display position of a waveform, whether a channel, math, or reference waveform.
              The position value determines the vertical graticule coordinate at which input signal
              values, equal to the present offset setting for that reference, are displayed. For
              example, if the position for Math 3 is set to 2.0 and the offset is set to 3.0, then
              the input signals equal to 3.0 are displayed 2.0 divisions above the center of the
              screen. Be aware that autoscaling occurs when a math waveform is first defined and
              enabled, or when a math string changes. After the math waveform is computed for the
              first time, the instrument determines the min + max of that waveform data. Then, the
              instrument sets the math position so that (min + max)/2 is in the center of the
              screen. In addition, the instrument sets the math scale so that the range of the min
              and max cover 6 divisions. This autoscaling process can take up to 1/2 second to
              complete and will override any vertical scale or position commands for that math
              waveform received during this time. You should insert an appropriate pause in your
              program after defining and enabling a math waveform before changing its position or
              scale.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:VERTical:POSition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:VERTical:POSition value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:VERTical:POSition <NR3>
            - MATH<x>:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is the desired position control in divisions from the center graticule.
        """
        return self._position

    @property
    def scale(self) -> MathItemVerticalScale:
        """Return the ``MATH<x>:VERTical:SCAle`` command.

        Description:
            - This command sets or queries the vertical scale of the specified math waveform. The
              Math waveform is specified by x, which ranges from 1 through 4. This command is
              equivalent to selecting Position/Scale from the Math menu and then entering a Vert
              Scale value or adjusting the front panel Vertical SCALE knob. Each waveform has its
              own vertical scale parameter. For a signal with constant amplitude, increasing the
              scale causes the waveform to be displayed smaller. Decreasing the scale causes the
              waveform to be displayed larger. Scale affects all waveforms. For reference and math
              waveforms, the scale setting controls the display only, graphically scaling these
              waveforms and having no affect on the acquisition hardware. Be aware that autoscaling
              occurs when a math waveform is first defined and enabled, or when a math string
              changes. After the math waveform is computed for the first time, the instrument
              determines the min + max of that waveform data. Then, the instrument sets the math
              position so that (min + max)/2 is in the center of the screen. In addition, the
              instrument sets the math scale so that the range of the min and max covers 6
              divisions. This autoscaling process can take up to 1/2 second to complete and will
              override any vertical scale or position commands for that math waveform received
              during this time. You should insert an appropriate pause in your program after
              defining and enabling a math waveform before changing its position or scale.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:VERTical:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:VERTical:SCAle?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:VERTical:SCAle value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:VERTical:SCAle <NR3>
            - MATH<x>:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is the scale in volts, amps or watts per division. The range is from
              100.0E-36 through 100.0E+36.
        """
        return self._scale


class MathItemUnitstring(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:UNITString`` command.

    Description:
        - This command sets or queries the string to use for units for the math waveform specified
          by x, which can be 1 through 4. This command will override the default unit string with
          the one that you specify.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:UNITString?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:UNITString?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:UNITString value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:UNITString <QString>
        - MATH<x>:UNITString?
        ```

    Info:
        - ``<QString>`` quoted string argument is the units to be used for the specified math
          waveform.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathItemThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:THRESHold`` command.

    Description:
        - This command sets or queries the threshold for the math waveform specified by x, which can
          be 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:THRESHold?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:THRESHold?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:THRESHold value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:THRESHold <NR3>
        - MATH<x>:THRESHold?
        ```

    Info:
        - ``<NR3>`` specifies the math threshold in volts.
    """


class MathItemSpectralWindow(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:WINdow`` command.

    Description:
        - This command sets or returns the window function used to multiply the spectral analyzer
          input data for the specified math waveform. The Math waveform is specified by x, which
          ranges from 1 through 4. A spectral window determines what the filter shape of the
          spectral analyzer will be in the frequency domain. It can be described by a mathematical
          function that is multiplied point-by-point times the input data to the spectral analyzer.
          This command is equal to selecting Spectral Setup from the Math menu, and choosing from
          the Window Type drop-down list. Following is a list of arguments that specify the window
          function used to multiply the spectral analyzer input data. The windows are listed in the
          order of their ability to resolve frequencies (resolution bandwidth). For additional
          information about spectral windows, see Selecting a Spectral Window in the online help for
          this instrument.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:WINdow?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:WINdow?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:WINdow value``
          command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:WINdow {RECTANGular|HAMMing|HANNing|KAISERBessel|BLACKMANHarris|FLATTOP2|GAUSSian|TEKEXPonential}
        - MATH<x>:SPECTral:WINdow?
        ```

    Info:
        - ``RECTANGular`` window function is equivalent to multiplying all gate data by one.
        - ``HAMMing`` window function is based on a cosine series.
        - ``HANNing`` window function is based on a cosine series.
        - ``KAISERBessel`` window function is based on a cosine series.
        - ``BLACKMANHarris`` window function is based on a cosine series.
        - ``FLATTOP2`` window function is a cosine series window with a flattened frequency response
          lobe.
        - ``GAUSSian`` window function has the best localization characteristics in the joint
          time/frequency plane.
        - ``TEKEXPonential`` window has an exponential nonsymmetrical shape in the time domain and a
          triangular shape in the frequency domain.
    """  # noqa: E501


class MathItemSpectralUnwrap(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:UNWRap`` command.

    Description:
        - This command sets or returns whether phase unwrap of the spectral analyzer output data is
          enabled for the specified math waveform. The Math waveform is specified by x, which ranges
          from 1 through 4. This command is equal to selecting Spectral Setup from the Math menu,
          choosing the Phase tab and then clicking the Unwrap button. This command affects only
          Spectral Phase waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:UNWRap?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:UNWRap?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:UNWRap value``
          command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:UNWRap {ON|OFF|<NR1>}
        - MATH<x>:SPECTral:UNWRap?
        ```

    Info:
        - ``ON`` enables phase unwrap.
        - ``OFF`` disables phase wrap.
        - ``<NR1>`` = 0 disables phase wrap; any other value enables phase wrap.
    """


class MathItemSpectralSuppress(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:SUPPress`` command.

    Description:
        - This command sets or returns the phase suppression threshold for the specified math
          waveform. The Math waveform is specified by x, which ranges from 1 through 4. This command
          is equal to selecting Spectral Setup from the Math menu, choosing the Phase tab and then
          entering a value in the Suppression Threshold box. This command affects only Spectral
          Phase waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:SUPPress?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:SUPPress?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:SUPPress value``
          command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:SUPPress <NR3>
        - MATH<x>:SPECTral:SUPPress?
        ```

    Info:
        - ``<NR3>`` is the magnitude level that data with magnitude values below this value are
          displayed as zero phase.
    """


class MathItemSpectralSpan(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:SPAN`` command.

    Description:
        - This command sets the ceiling of the frequency span to a value that is closest to the
          specified value. The query form of this command returns the current span value for
          specified math waveform. The Math waveform is specified by x, which ranges from 1 through
          4. This command is equal to selecting Spectral Setup from the Math menu and then entering
          a value in the Freq Span box.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:SPAN?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:SPAN?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:SPAN value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:SPAN {<NR3>|FULl}
        - MATH<x>:SPECTral:SPAN?
        ```

    Info:
        - ``<NR3>`` specifies the frequency span of the output data vector from the spectral
          analyzer.
        - ``FULL`` sets the top of the span to 1/2 the sample rate and sets the center frequency to
          1/2 the span.
    """


class MathItemSpectralResbw(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:RESBw`` command.

    Description:
        - This command sets or returns the resolution bandwidth of the spectral analyzer for the
          specified math waveform. The Math waveform is specified by x, which ranges from 1 through
          4. This command is equivalent to selecting Spectral Setup from the Math menu and then
          entering a value in the Res BW box.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:RESBw?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:RESBw?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:RESBw value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:RESBw <NR3>
        - MATH<x>:SPECTral:RESBw?
        ```

    Info:
        - ``<NR3>`` is the desired resolution bandwidth value. Units are represented in Hertz.
    """


class MathItemSpectralReflevel(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:REFLevel`` command.

    Description:
        - This command specifies the vertical position of the specified spectral math waveform on
          the display screen. The numerical value represents the position at the top of the display
          graticule. The Math waveform is specified by x, which ranges from 1 through 4. This
          command is equal to selecting Spectral Setup from the Math menu, choosing the Mag tab and
          then entering a value in the Reference Level box.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:REFLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:REFLevel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:REFLevel value``
          command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:REFLevel <NR3>
        - MATH<x>:SPECTral:REFLevel?
        ```

    Info:
        - ``<NR3>`` is the value that represents the top of the display screen graticule. The range
          depends on the units and both the ``MATH<x>:VERTical:SCAle`` and
          ``MATH<x>:VERTical:POSition`` settings.
    """


class MathItemSpectralRefleveloffset(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:REFLEVELOffset`` command.

    Description:
        - This command sets or returns the spectral level offset used for calculating the dB value
          for the specified math waveform. The Math waveform is specified by x, which ranges from 1
          through 4. Changing the reference level offset causes the spectral waveform to move
          vertically, with respect to zero dB. This command is equal to selecting Spectral Setup
          from the Math menu, choosing the Mag tab and then entering a value in the Reference Level
          Offset box.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:REFLEVELOffset?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:REFLEVELOffset?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:REFLEVELOffset value``
          command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:REFLEVELOffset {DBM|<NR3>}
        - MATH<x>:SPECTral:REFLEVELOffset?
        ```

    Info:
        - ``DBM`` specifies the reference level used for calculation to be equivalent to 1 mW into
          50 Ω (Zero dB will occur at this level).
        - ``<NR3>`` specifies the reference level used for calculation of the decibel value when the
          output units are Log.
    """


class MathItemSpectralPhase(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:PHASE`` command.

    Description:
        - This command sets or returns the units of a SpectralPhase function in the specified math
          definition string. The Math waveform is specified by x, which ranges from 1 through 4.
          This command is equal to selecting Spectral Phase from the Math menu, selecting the
          Advanced button, selecting the Vert Axis tab, and then clicking the desired Scale button.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:PHASE?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:PHASE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:PHASE value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:PHASE {DEGrees|RADians|GROUPDelay}
        - MATH<x>:SPECTral:PHASE?
        ```

    Info:
        - ``DEGREES`` sets the SpectralPhase units to degrees.
        - ``RADIANS`` sets the SpectralPhase units to radians.
        - ``GROUPDELAY`` sets the SpectralPhase units to groupdelay, which computes the derivative
          of unwrapped phase spectrum. Units are expressed in seconds.
    """


class MathItemSpectralMag(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:MAG`` command.

    Description:
        - This command sets or returns the units of the SpectralMag function in the specified math
          definition string. The Math waveform is specified by x, which ranges from 1 through 4.
          This command is equivalent to selecting Spectral Mag from the Math menu and then entering
          the units that you want in the Scale box, or selecting Basic from the Math menu and then
          clicking the desired Scale button.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:MAG?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:MAG?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:MAG value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:MAG {LINEAr|DB|DBM}
        - MATH<x>:SPECTral:MAG?
        ```

    Info:
        - ``LINEAR`` sets the SpectralMag units to linear.
        - ``DB`` sets the SpectralMag units to decibels.
        - ``DBM`` sets the SpectralMag units to decibels. It also sets the Ref Level Offset to a
          value that is the equivalent of 1 mW into 50 Ω.
    """


class MathItemSpectralLock(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:LOCk`` command.

    Description:
        - This command locks menus for two or more math waveforms together as a group. The query
          form of this command returns an ON (1) or OFF (0), indicating whether spectral locking is
          turned on. This command is equal to selecting Spectral Setup from the Math menu, choosing
          the Control tab and then clicking the Time/Track Frequency Domain Controls button
          associated with the math waveforms that you want to lock. Math<x> Lock Combinations Math1
          Math2 Math3 Locked Math Waveforms Off None Off On Math3 and Math4 locked Off On Off Math2
          and Math3 locked Off On Math2, Math3, and Math4 locked On Off Math1 and Math2 locked On
          Off On Math1 and Math2 locked, Math3 and Math4 locked On Off Math1, Math2, and Math3
          locked On Math1, Math2, Math3, and Math4 locked

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:LOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:LOCk?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:LOCk value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:LOCk {ON|OFF|<NR1>}
        - MATH<x>:SPECTral:LOCk?
        ```

    Info:
        - ``ON`` turns on the parameter lock for the specified math waveform.
        - ``OFF`` turns off the parameter lock for the specified math waveform.
        - ``<NR1>`` = 0 disables the parameter lock for the specified math waveform; any other value
          enables the parameter lock.
    """


class MathItemSpectralGatewidth(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:GATEWIDTH`` command.

    Description:
        - This command sets or returns the gate width input in seconds, to the spectral analyzer for
          the specified math waveform. The math waveform is specified by x, which ranges from 1
          through 4. This command is equivalent to selecting Spectral Setup from the Math menu and
          entering a duration value in the Gate Dur box.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:GATEWIDTH?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:GATEWIDTH?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:GATEWIDTH value``
          command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:GATEWIDTH <NR3>
        - MATH<x>:SPECTral:GATEWIDTH?
        ```

    Info:
        - ``<NR3>`` is the time across the 10-division screen in seconds.
    """


class MathItemSpectralGatepos(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:GATEPOS`` command.

    Description:
        - This command sets or returns the position of the center of the gate, which is used as the
          data input to the spectral analyzer for the specified math waveform. The math waveform is
          specified by x, which ranges from 1 through 4. This command is equivalent to selecting
          Spectral Setup from the Math menu and then entering a Gate Pos value.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:GATEPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:GATEPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:GATEPOS value``
          command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:GATEPOS <NR3>
        - MATH<x>:SPECTral:GATEPOS?
        ```

    Info:
        - ``<NR3>`` is the gate position. Units are represented in seconds, with respect to trigger
          position.
    """


class MathItemSpectralCenter(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:SPECTral:CENTER`` command.

    Description:
        - This command specifies or returns the center frequency of the spectral analyzer output
          data span for the specified math waveform. The Math waveform is specified by x, which
          ranges from 1 through 4. This command is equivalent to selecting Spectral Setup from the
          Math menu and then entering a Center Freq value.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:CENTER?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:CENTER?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:CENTER value``
          command.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral:CENTER <NR3>
        - MATH<x>:SPECTral:CENTER?
        ```

    Info:
        - ``<NR3>`` is the desired frequency of the spectral analyzer output data span in hertz.
    """


#  pylint: disable=too-many-instance-attributes
class MathItemSpectral(SCPICmdRead):
    """The ``MATH<x>:SPECTral`` command.

    Description:
        - This query-only command returns the current spectral setups for the specified math
          waveform. The Math waveform is specified by x, which ranges from 1 through 4. This command
          is equivalent to selecting Spectral Setup from the Math menu and viewing the current
          spectral setup values.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:SPECTral?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATH<x>:SPECTral?
        ```

    Properties:
        - ``.center``: The ``MATH<x>:SPECTral:CENTER`` command.
        - ``.gatepos``: The ``MATH<x>:SPECTral:GATEPOS`` command.
        - ``.gatewidth``: The ``MATH<x>:SPECTral:GATEWIDTH`` command.
        - ``.lock``: The ``MATH<x>:SPECTral:LOCk`` command.
        - ``.mag``: The ``MATH<x>:SPECTral:MAG`` command.
        - ``.phase``: The ``MATH<x>:SPECTral:PHASE`` command.
        - ``.refleveloffset``: The ``MATH<x>:SPECTral:REFLEVELOffset`` command.
        - ``.reflevel``: The ``MATH<x>:SPECTral:REFLevel`` command.
        - ``.resbw``: The ``MATH<x>:SPECTral:RESBw`` command.
        - ``.span``: The ``MATH<x>:SPECTral:SPAN`` command.
        - ``.suppress``: The ``MATH<x>:SPECTral:SUPPress`` command.
        - ``.unwrap``: The ``MATH<x>:SPECTral:UNWRap`` command.
        - ``.window``: The ``MATH<x>:SPECTral:WINdow`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._center = MathItemSpectralCenter(device, f"{self._cmd_syntax}:CENTER")
        self._gatepos = MathItemSpectralGatepos(device, f"{self._cmd_syntax}:GATEPOS")
        self._gatewidth = MathItemSpectralGatewidth(device, f"{self._cmd_syntax}:GATEWIDTH")
        self._lock = MathItemSpectralLock(device, f"{self._cmd_syntax}:LOCk")
        self._mag = MathItemSpectralMag(device, f"{self._cmd_syntax}:MAG")
        self._phase = MathItemSpectralPhase(device, f"{self._cmd_syntax}:PHASE")
        self._refleveloffset = MathItemSpectralRefleveloffset(
            device, f"{self._cmd_syntax}:REFLEVELOffset"
        )
        self._reflevel = MathItemSpectralReflevel(device, f"{self._cmd_syntax}:REFLevel")
        self._resbw = MathItemSpectralResbw(device, f"{self._cmd_syntax}:RESBw")
        self._span = MathItemSpectralSpan(device, f"{self._cmd_syntax}:SPAN")
        self._suppress = MathItemSpectralSuppress(device, f"{self._cmd_syntax}:SUPPress")
        self._unwrap = MathItemSpectralUnwrap(device, f"{self._cmd_syntax}:UNWRap")
        self._window = MathItemSpectralWindow(device, f"{self._cmd_syntax}:WINdow")

    @property
    def center(self) -> MathItemSpectralCenter:
        """Return the ``MATH<x>:SPECTral:CENTER`` command.

        Description:
            - This command specifies or returns the center frequency of the spectral analyzer output
              data span for the specified math waveform. The Math waveform is specified by x, which
              ranges from 1 through 4. This command is equivalent to selecting Spectral Setup from
              the Math menu and then entering a Center Freq value.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:CENTER?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:CENTER?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:CENTER value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:CENTER <NR3>
            - MATH<x>:SPECTral:CENTER?
            ```

        Info:
            - ``<NR3>`` is the desired frequency of the spectral analyzer output data span in hertz.
        """
        return self._center

    @property
    def gatepos(self) -> MathItemSpectralGatepos:
        """Return the ``MATH<x>:SPECTral:GATEPOS`` command.

        Description:
            - This command sets or returns the position of the center of the gate, which is used as
              the data input to the spectral analyzer for the specified math waveform. The math
              waveform is specified by x, which ranges from 1 through 4. This command is equivalent
              to selecting Spectral Setup from the Math menu and then entering a Gate Pos value.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:GATEPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:GATEPOS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:GATEPOS value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:GATEPOS <NR3>
            - MATH<x>:SPECTral:GATEPOS?
            ```

        Info:
            - ``<NR3>`` is the gate position. Units are represented in seconds, with respect to
              trigger position.
        """
        return self._gatepos

    @property
    def gatewidth(self) -> MathItemSpectralGatewidth:
        """Return the ``MATH<x>:SPECTral:GATEWIDTH`` command.

        Description:
            - This command sets or returns the gate width input in seconds, to the spectral analyzer
              for the specified math waveform. The math waveform is specified by x, which ranges
              from 1 through 4. This command is equivalent to selecting Spectral Setup from the Math
              menu and entering a duration value in the Gate Dur box.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:GATEWIDTH?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:GATEWIDTH?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:GATEWIDTH value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:GATEWIDTH <NR3>
            - MATH<x>:SPECTral:GATEWIDTH?
            ```

        Info:
            - ``<NR3>`` is the time across the 10-division screen in seconds.
        """
        return self._gatewidth

    @property
    def lock(self) -> MathItemSpectralLock:
        """Return the ``MATH<x>:SPECTral:LOCk`` command.

        Description:
            - This command locks menus for two or more math waveforms together as a group. The query
              form of this command returns an ON (1) or OFF (0), indicating whether spectral locking
              is turned on. This command is equal to selecting Spectral Setup from the Math menu,
              choosing the Control tab and then clicking the Time/Track Frequency Domain Controls
              button associated with the math waveforms that you want to lock. Math<x> Lock
              Combinations Math1 Math2 Math3 Locked Math Waveforms Off None Off On Math3 and Math4
              locked Off On Off Math2 and Math3 locked Off On Math2, Math3, and Math4 locked On Off
              Math1 and Math2 locked On Off On Math1 and Math2 locked, Math3 and Math4 locked On Off
              Math1, Math2, and Math3 locked On Math1, Math2, Math3, and Math4 locked

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:LOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:LOCk?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:LOCk value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:LOCk {ON|OFF|<NR1>}
            - MATH<x>:SPECTral:LOCk?
            ```

        Info:
            - ``ON`` turns on the parameter lock for the specified math waveform.
            - ``OFF`` turns off the parameter lock for the specified math waveform.
            - ``<NR1>`` = 0 disables the parameter lock for the specified math waveform; any other
              value enables the parameter lock.
        """
        return self._lock

    @property
    def mag(self) -> MathItemSpectralMag:
        """Return the ``MATH<x>:SPECTral:MAG`` command.

        Description:
            - This command sets or returns the units of the SpectralMag function in the specified
              math definition string. The Math waveform is specified by x, which ranges from 1
              through 4. This command is equivalent to selecting Spectral Mag from the Math menu and
              then entering the units that you want in the Scale box, or selecting Basic from the
              Math menu and then clicking the desired Scale button.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:MAG?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:MAG?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:MAG value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:MAG {LINEAr|DB|DBM}
            - MATH<x>:SPECTral:MAG?
            ```

        Info:
            - ``LINEAR`` sets the SpectralMag units to linear.
            - ``DB`` sets the SpectralMag units to decibels.
            - ``DBM`` sets the SpectralMag units to decibels. It also sets the Ref Level Offset to a
              value that is the equivalent of 1 mW into 50 Ω.
        """
        return self._mag

    @property
    def phase(self) -> MathItemSpectralPhase:
        """Return the ``MATH<x>:SPECTral:PHASE`` command.

        Description:
            - This command sets or returns the units of a SpectralPhase function in the specified
              math definition string. The Math waveform is specified by x, which ranges from 1
              through 4. This command is equal to selecting Spectral Phase from the Math menu,
              selecting the Advanced button, selecting the Vert Axis tab, and then clicking the
              desired Scale button.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:PHASE?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:PHASE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:PHASE value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:PHASE {DEGrees|RADians|GROUPDelay}
            - MATH<x>:SPECTral:PHASE?
            ```

        Info:
            - ``DEGREES`` sets the SpectralPhase units to degrees.
            - ``RADIANS`` sets the SpectralPhase units to radians.
            - ``GROUPDELAY`` sets the SpectralPhase units to groupdelay, which computes the
              derivative of unwrapped phase spectrum. Units are expressed in seconds.
        """
        return self._phase

    @property
    def refleveloffset(self) -> MathItemSpectralRefleveloffset:
        """Return the ``MATH<x>:SPECTral:REFLEVELOffset`` command.

        Description:
            - This command sets or returns the spectral level offset used for calculating the dB
              value for the specified math waveform. The Math waveform is specified by x, which
              ranges from 1 through 4. Changing the reference level offset causes the spectral
              waveform to move vertically, with respect to zero dB. This command is equal to
              selecting Spectral Setup from the Math menu, choosing the Mag tab and then entering a
              value in the Reference Level Offset box.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:REFLEVELOffset?``
              query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:REFLEVELOffset?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH<x>:SPECTral:REFLEVELOffset value`` command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:REFLEVELOffset {DBM|<NR3>}
            - MATH<x>:SPECTral:REFLEVELOffset?
            ```

        Info:
            - ``DBM`` specifies the reference level used for calculation to be equivalent to 1 mW
              into 50 Ω (Zero dB will occur at this level).
            - ``<NR3>`` specifies the reference level used for calculation of the decibel value when
              the output units are Log.
        """
        return self._refleveloffset

    @property
    def reflevel(self) -> MathItemSpectralReflevel:
        """Return the ``MATH<x>:SPECTral:REFLevel`` command.

        Description:
            - This command specifies the vertical position of the specified spectral math waveform
              on the display screen. The numerical value represents the position at the top of the
              display graticule. The Math waveform is specified by x, which ranges from 1 through 4.
              This command is equal to selecting Spectral Setup from the Math menu, choosing the Mag
              tab and then entering a value in the Reference Level box.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:REFLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:REFLevel?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:REFLevel value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:REFLevel <NR3>
            - MATH<x>:SPECTral:REFLevel?
            ```

        Info:
            - ``<NR3>`` is the value that represents the top of the display screen graticule. The
              range depends on the units and both the ``MATH<x>:VERTical:SCAle`` and
              ``MATH<x>:VERTical:POSition`` settings.
        """
        return self._reflevel

    @property
    def resbw(self) -> MathItemSpectralResbw:
        """Return the ``MATH<x>:SPECTral:RESBw`` command.

        Description:
            - This command sets or returns the resolution bandwidth of the spectral analyzer for the
              specified math waveform. The Math waveform is specified by x, which ranges from 1
              through 4. This command is equivalent to selecting Spectral Setup from the Math menu
              and then entering a value in the Res BW box.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:RESBw?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:RESBw?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:RESBw value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:RESBw <NR3>
            - MATH<x>:SPECTral:RESBw?
            ```

        Info:
            - ``<NR3>`` is the desired resolution bandwidth value. Units are represented in Hertz.
        """
        return self._resbw

    @property
    def span(self) -> MathItemSpectralSpan:
        """Return the ``MATH<x>:SPECTral:SPAN`` command.

        Description:
            - This command sets the ceiling of the frequency span to a value that is closest to the
              specified value. The query form of this command returns the current span value for
              specified math waveform. The Math waveform is specified by x, which ranges from 1
              through 4. This command is equal to selecting Spectral Setup from the Math menu and
              then entering a value in the Freq Span box.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:SPAN?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:SPAN?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:SPAN value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:SPAN {<NR3>|FULl}
            - MATH<x>:SPECTral:SPAN?
            ```

        Info:
            - ``<NR3>`` specifies the frequency span of the output data vector from the spectral
              analyzer.
            - ``FULL`` sets the top of the span to 1/2 the sample rate and sets the center frequency
              to 1/2 the span.
        """
        return self._span

    @property
    def suppress(self) -> MathItemSpectralSuppress:
        """Return the ``MATH<x>:SPECTral:SUPPress`` command.

        Description:
            - This command sets or returns the phase suppression threshold for the specified math
              waveform. The Math waveform is specified by x, which ranges from 1 through 4. This
              command is equal to selecting Spectral Setup from the Math menu, choosing the Phase
              tab and then entering a value in the Suppression Threshold box. This command affects
              only Spectral Phase waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:SUPPress?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:SUPPress?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:SUPPress value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:SUPPress <NR3>
            - MATH<x>:SPECTral:SUPPress?
            ```

        Info:
            - ``<NR3>`` is the magnitude level that data with magnitude values below this value are
              displayed as zero phase.
        """
        return self._suppress

    @property
    def unwrap(self) -> MathItemSpectralUnwrap:
        """Return the ``MATH<x>:SPECTral:UNWRap`` command.

        Description:
            - This command sets or returns whether phase unwrap of the spectral analyzer output data
              is enabled for the specified math waveform. The Math waveform is specified by x, which
              ranges from 1 through 4. This command is equal to selecting Spectral Setup from the
              Math menu, choosing the Phase tab and then clicking the Unwrap button. This command
              affects only Spectral Phase waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:UNWRap?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:UNWRap?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:UNWRap value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:UNWRap {ON|OFF|<NR1>}
            - MATH<x>:SPECTral:UNWRap?
            ```

        Info:
            - ``ON`` enables phase unwrap.
            - ``OFF`` disables phase wrap.
            - ``<NR1>`` = 0 disables phase wrap; any other value enables phase wrap.
        """
        return self._unwrap

    @property
    def window(self) -> MathItemSpectralWindow:
        """Return the ``MATH<x>:SPECTral:WINdow`` command.

        Description:
            - This command sets or returns the window function used to multiply the spectral
              analyzer input data for the specified math waveform. The Math waveform is specified by
              x, which ranges from 1 through 4. A spectral window determines what the filter shape
              of the spectral analyzer will be in the frequency domain. It can be described by a
              mathematical function that is multiplied point-by-point times the input data to the
              spectral analyzer. This command is equal to selecting Spectral Setup from the Math
              menu, and choosing from the Window Type drop-down list. Following is a list of
              arguments that specify the window function used to multiply the spectral analyzer
              input data. The windows are listed in the order of their ability to resolve
              frequencies (resolution bandwidth). For additional information about spectral windows,
              see Selecting a Spectral Window in the online help for this instrument.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral:WINdow?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral:WINdow?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:SPECTral:WINdow value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral:WINdow {RECTANGular|HAMMing|HANNing|KAISERBessel|BLACKMANHarris|FLATTOP2|GAUSSian|TEKEXPonential}
            - MATH<x>:SPECTral:WINdow?
            ```

        Info:
            - ``RECTANGular`` window function is equivalent to multiplying all gate data by one.
            - ``HAMMing`` window function is based on a cosine series.
            - ``HANNing`` window function is based on a cosine series.
            - ``KAISERBessel`` window function is based on a cosine series.
            - ``BLACKMANHarris`` window function is based on a cosine series.
            - ``FLATTOP2`` window function is a cosine series window with a flattened frequency
              response lobe.
            - ``GAUSSian`` window function has the best localization characteristics in the joint
              time/frequency plane.
            - ``TEKEXPonential`` window has an exponential nonsymmetrical shape in the time domain
              and a triangular shape in the frequency domain.
        """  # noqa: E501
        return self._window


class MathItemNumavg(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:NUMAVg`` command.

    Description:
        - This command sets or returns the acquisition number at which the averaging algorithm will
          begin exponential averaging. Prior to that acquisition number, the algorithm uses stable
          averaging. This has no effect unless the AVG() function is used in the specified math
          expression. If so, it affects all AVG() functions in this math expression. The Math
          waveform is specified by x, which ranges from 1 through 4. This command is equivalent to
          selecting Set Math Averages from the Math menu and then entering an averaging value for
          the math waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:NUMAVg?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:NUMAVg?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:NUMAVg value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:NUMAVg <NR1>
        - MATH<x>:NUMAVg?
        ```

    Info:
        - ``<NR1>`` specifies the number of acquisitions over which exponential averaging is
          performed.
    """


class MathItemLabelYpos(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:LABel:YPOS`` command.

    Description:
        - This command sets or queries the Y screen offset at which the label attached to a math
          waveform is displayed, relative to the waveform handle. The Math waveform is specified by
          x, which ranges from 1 through 4. This command is equivalent to selecting Math Label from
          the Math menu and entering a value in the Y Position box.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:LABel:YPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:LABel:YPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:LABel:YPOS value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:LABel:YPOS <NR1>
        - MATH<x>:LABel:YPOS?
        ```

    Info:
        - ``<NR1>`` is the location (in divisions) where the label for the selected math waveform is
          displayed, relative to the waveform handle. Arguments should rang from 10 to -10.
    """


class MathItemLabelXpos(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:LABel:XPOS`` command.

    Description:
        - This command sets or queries the X screen offset at which the label attached to a math
          waveform is displayed, relative to the left edge of the screen. Channels are specified by
          x, which ranges from 1 through 4. This command is equivalent to selecting Math Label from
          the Math menu and entering a value in the X Position box.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:LABel:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:LABel:XPOS?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:LABel:XPOS value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:LABel:XPOS <NR1>
        - MATH<x>:LABel:XPOS?
        ```

    Info:
        - ``<NR1>`` is the location (in divisions) where the label for the selected math waveform is
          displayed, relative to the left edge of the screen. Arguments should be integers ranging
          from 0 to 10.
    """


class MathItemLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:LABel:NAMe`` command.

    Description:
        - This command sets or returns the label string, which is used for annotating the math
          waveform on the screen. The math waveform to which the label is attached is specified by
          x, which ranges in value from 1 through 4. This command is equivalent to selecting Math
          Setup from the Math menu and entering a label in the Label box.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:LABel:NAMe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:LABel:NAMe value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:LABel:NAMe <QString>
        - MATH<x>:LABel:NAMe?
        ```

    Info:
        - ``<QString>`` specifies the label to annotate the math waveform.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathItemLabel(SCPICmdRead):
    """The ``MATH<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.name``: The ``MATH<x>:LABel:NAMe`` command.
        - ``.xpos``: The ``MATH<x>:LABel:XPOS`` command.
        - ``.ypos``: The ``MATH<x>:LABel:YPOS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._name = MathItemLabelName(device, f"{self._cmd_syntax}:NAMe")
        self._xpos = MathItemLabelXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = MathItemLabelYpos(device, f"{self._cmd_syntax}:YPOS")

    @property
    def name(self) -> MathItemLabelName:
        """Return the ``MATH<x>:LABel:NAMe`` command.

        Description:
            - This command sets or returns the label string, which is used for annotating the math
              waveform on the screen. The math waveform to which the label is attached is specified
              by x, which ranges in value from 1 through 4. This command is equivalent to selecting
              Math Setup from the Math menu and entering a label in the Label box.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:LABel:NAMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:LABel:NAMe value`` command.

        SCPI Syntax:
            ```
            - MATH<x>:LABel:NAMe <QString>
            - MATH<x>:LABel:NAMe?
            ```

        Info:
            - ``<QString>`` specifies the label to annotate the math waveform.
        """
        return self._name

    @property
    def xpos(self) -> MathItemLabelXpos:
        """Return the ``MATH<x>:LABel:XPOS`` command.

        Description:
            - This command sets or queries the X screen offset at which the label attached to a math
              waveform is displayed, relative to the left edge of the screen. Channels are specified
              by x, which ranges from 1 through 4. This command is equivalent to selecting Math
              Label from the Math menu and entering a value in the X Position box.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:LABel:XPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:LABel:XPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:LABel:XPOS value`` command.

        SCPI Syntax:
            ```
            - MATH<x>:LABel:XPOS <NR1>
            - MATH<x>:LABel:XPOS?
            ```

        Info:
            - ``<NR1>`` is the location (in divisions) where the label for the selected math
              waveform is displayed, relative to the left edge of the screen. Arguments should be
              integers ranging from 0 to 10.
        """
        return self._xpos

    @property
    def ypos(self) -> MathItemLabelYpos:
        """Return the ``MATH<x>:LABel:YPOS`` command.

        Description:
            - This command sets or queries the Y screen offset at which the label attached to a math
              waveform is displayed, relative to the waveform handle. The Math waveform is specified
              by x, which ranges from 1 through 4. This command is equivalent to selecting Math
              Label from the Math menu and entering a value in the Y Position box.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:LABel:YPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:LABel:YPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:LABel:YPOS value`` command.

        SCPI Syntax:
            ```
            - MATH<x>:LABel:YPOS <NR1>
            - MATH<x>:LABel:YPOS?
            ```

        Info:
            - ``<NR1>`` is the location (in divisions) where the label for the selected math
              waveform is displayed, relative to the waveform handle. Arguments should rang from 10
              to -10.
        """
        return self._ypos


class MathItemFilterRisetime(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:FILTer:RISetime`` command.

    Description:
        - This command or query sets or returns the filter rise time parameter.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:FILTer:RISetime?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:FILTer:RISetime?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:FILTer:RISetime value``
          command.

    SCPI Syntax:
        ```
        - MATH<x>:FILTer:RISetime <NR3>
        - MATH<x>:FILTer:RISetime?
        ```

    Info:
        - ``<NR3>`` sets how the filter affects a signal. The bandwidth of the filter is
          approximately 0.35 / (filter rise time). For a square wave input, the measurement system
          rise time of Math(x) = filter (chx) is very close to the filter rise time of Math(x).
    """


class MathItemFilterMode(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:FILTer:MODe`` command.

    Description:
        - This command or query sets or returns the filter rise time parameter.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:FILTer:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:FILTer:MODe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:FILTer:MODe value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:FILTer:MODe {CENTered|SHIFted}
        - MATH<x>:FILTer:MODe?
        ```

    Info:
        - ``CENTERED`` sets the value at any point to the average of that point in the source
          waveform and N points on either side of that point.
        - ``SHIFTED`` sets the value at any point to the average of that point in the source
          waveform and 2N points before that in the source waveform. This shifts a rising edge to
          the right side of the screen. Shifted mode is sometimes called a causal filter since the
          value at any point is not caused by points after it in time.
    """


class MathItemFilter(SCPICmdRead):
    """The ``MATH<x>:FILTer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:FILTer?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:FILTer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``MATH<x>:FILTer:MODe`` command.
        - ``.risetime``: The ``MATH<x>:FILTer:RISetime`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = MathItemFilterMode(device, f"{self._cmd_syntax}:MODe")
        self._risetime = MathItemFilterRisetime(device, f"{self._cmd_syntax}:RISetime")

    @property
    def mode(self) -> MathItemFilterMode:
        """Return the ``MATH<x>:FILTer:MODe`` command.

        Description:
            - This command or query sets or returns the filter rise time parameter.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:FILTer:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:FILTer:MODe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:FILTer:MODe value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:FILTer:MODe {CENTered|SHIFted}
            - MATH<x>:FILTer:MODe?
            ```

        Info:
            - ``CENTERED`` sets the value at any point to the average of that point in the source
              waveform and N points on either side of that point.
            - ``SHIFTED`` sets the value at any point to the average of that point in the source
              waveform and 2N points before that in the source waveform. This shifts a rising edge
              to the right side of the screen. Shifted mode is sometimes called a causal filter
              since the value at any point is not caused by points after it in time.
        """
        return self._mode

    @property
    def risetime(self) -> MathItemFilterRisetime:
        """Return the ``MATH<x>:FILTer:RISetime`` command.

        Description:
            - This command or query sets or returns the filter rise time parameter.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:FILTer:RISetime?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:FILTer:RISetime?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:FILTer:RISetime value``
              command.

        SCPI Syntax:
            ```
            - MATH<x>:FILTer:RISetime <NR3>
            - MATH<x>:FILTer:RISetime?
            ```

        Info:
            - ``<NR3>`` sets how the filter affects a signal. The bandwidth of the filter is
              approximately 0.35 / (filter rise time). For a square wave input, the measurement
              system rise time of Math(x) = filter (chx) is very close to the filter rise time of
              Math(x).
        """
        return self._risetime


class MathItemDefine(SCPICmdWrite, SCPICmdRead):
    """The ``MATH<x>:DEFine`` command.

    Description:
        - This command allows you to define new waveforms using mathematical expressions. Sending
          this command is equivalent to selecting Math Setup from the Math menu, selecting a math
          waveform (Math 1 through Math 4), and then entering a math expression in the Math<x> box.
          The query form of this command returns the math definition for the specified math
          waveform. You can specify a math expression from waveforms, measurements and scalar
          sources, functions, operands, and numerical constants. You can define and display up to
          four math waveforms simultaneously. Math expressions can be simple, such as Ch1, which
          specifies that a waveform should show the signal source of Channel 1 with no mathematical
          computation. Math expressions can also be complex, consisting of 100 plus characters and
          comprising many sources (including other math waveforms), functions, and operands. As an
          example, you can enter the expression Log(Ch1+Ch2), which specifies that the signals from
          channels 1 and 2 are to be algebraically added, and the base 10 log of the sum is to be
          shown as the final math waveform. For more information about constructing mathematical
          expressions, see Creating and Using Math Waveforms in the user online help for this
          instrument.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>:DEFine?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>:DEFine?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH<x>:DEFine value`` command.

    SCPI Syntax:
        ```
        - MATH<x>:DEFine <QString>
        - MATH<x>:DEFine?
        ```

    Info:
        - ``<QString>`` quoted string argument is the mathematical expression that defines the
          waveform.
    """

    _WRAP_ARG_WITH_QUOTES = True


#  pylint: disable=too-many-instance-attributes
class MathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MATH<x>`` command.

    Description:
        - This query-only command returns the definition for the math waveform specified by <x>,
          which ranges from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATH<x>?
        ```

    Properties:
        - ``.define``: The ``MATH<x>:DEFine`` command.
        - ``.filter``: The ``MATH<x>:FILTer`` command tree.
        - ``.label``: The ``MATH<x>:LABel`` command tree.
        - ``.numavg``: The ``MATH<x>:NUMAVg`` command.
        - ``.spectral``: The ``MATH<x>:SPECTral`` command.
        - ``.threshold``: The ``MATH<x>:THRESHold`` command.
        - ``.unitstring``: The ``MATH<x>:UNITString`` command.
        - ``.vertical``: The ``MATH<x>:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MATH<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._define = MathItemDefine(device, f"{self._cmd_syntax}:DEFine")
        self._filter = MathItemFilter(device, f"{self._cmd_syntax}:FILTer")
        self._label = MathItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._numavg = MathItemNumavg(device, f"{self._cmd_syntax}:NUMAVg")
        self._spectral = MathItemSpectral(device, f"{self._cmd_syntax}:SPECTral")
        self._threshold = MathItemThreshold(device, f"{self._cmd_syntax}:THRESHold")
        self._unitstring = MathItemUnitstring(device, f"{self._cmd_syntax}:UNITString")
        self._vertical = MathItemVertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def define(self) -> MathItemDefine:
        """Return the ``MATH<x>:DEFine`` command.

        Description:
            - This command allows you to define new waveforms using mathematical expressions.
              Sending this command is equivalent to selecting Math Setup from the Math menu,
              selecting a math waveform (Math 1 through Math 4), and then entering a math expression
              in the Math<x> box. The query form of this command returns the math definition for the
              specified math waveform. You can specify a math expression from waveforms,
              measurements and scalar sources, functions, operands, and numerical constants. You can
              define and display up to four math waveforms simultaneously. Math expressions can be
              simple, such as Ch1, which specifies that a waveform should show the signal source of
              Channel 1 with no mathematical computation. Math expressions can also be complex,
              consisting of 100 plus characters and comprising many sources (including other math
              waveforms), functions, and operands. As an example, you can enter the expression
              Log(Ch1+Ch2), which specifies that the signals from channels 1 and 2 are to be
              algebraically added, and the base 10 log of the sum is to be shown as the final math
              waveform. For more information about constructing mathematical expressions, see
              Creating and Using Math Waveforms in the user online help for this instrument.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:DEFine?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:DEFine?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:DEFine value`` command.

        SCPI Syntax:
            ```
            - MATH<x>:DEFine <QString>
            - MATH<x>:DEFine?
            ```

        Info:
            - ``<QString>`` quoted string argument is the mathematical expression that defines the
              waveform.
        """
        return self._define

    @property
    def filter(self) -> MathItemFilter:
        """Return the ``MATH<x>:FILTer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:FILTer?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:FILTer?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``MATH<x>:FILTer:MODe`` command.
            - ``.risetime``: The ``MATH<x>:FILTer:RISetime`` command.
        """
        return self._filter

    @property
    def label(self) -> MathItemLabel:
        """Return the ``MATH<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:LABel?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.name``: The ``MATH<x>:LABel:NAMe`` command.
            - ``.xpos``: The ``MATH<x>:LABel:XPOS`` command.
            - ``.ypos``: The ``MATH<x>:LABel:YPOS`` command.
        """
        return self._label

    @property
    def numavg(self) -> MathItemNumavg:
        """Return the ``MATH<x>:NUMAVg`` command.

        Description:
            - This command sets or returns the acquisition number at which the averaging algorithm
              will begin exponential averaging. Prior to that acquisition number, the algorithm uses
              stable averaging. This has no effect unless the AVG() function is used in the
              specified math expression. If so, it affects all AVG() functions in this math
              expression. The Math waveform is specified by x, which ranges from 1 through 4. This
              command is equivalent to selecting Set Math Averages from the Math menu and then
              entering an averaging value for the math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:NUMAVg?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:NUMAVg?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:NUMAVg value`` command.

        SCPI Syntax:
            ```
            - MATH<x>:NUMAVg <NR1>
            - MATH<x>:NUMAVg?
            ```

        Info:
            - ``<NR1>`` specifies the number of acquisitions over which exponential averaging is
              performed.
        """
        return self._numavg

    @property
    def spectral(self) -> MathItemSpectral:
        """Return the ``MATH<x>:SPECTral`` command.

        Description:
            - This query-only command returns the current spectral setups for the specified math
              waveform. The Math waveform is specified by x, which ranges from 1 through 4. This
              command is equivalent to selecting Spectral Setup from the Math menu and viewing the
              current spectral setup values.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:SPECTral?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:SPECTral?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATH<x>:SPECTral?
            ```

        Sub-properties:
            - ``.center``: The ``MATH<x>:SPECTral:CENTER`` command.
            - ``.gatepos``: The ``MATH<x>:SPECTral:GATEPOS`` command.
            - ``.gatewidth``: The ``MATH<x>:SPECTral:GATEWIDTH`` command.
            - ``.lock``: The ``MATH<x>:SPECTral:LOCk`` command.
            - ``.mag``: The ``MATH<x>:SPECTral:MAG`` command.
            - ``.phase``: The ``MATH<x>:SPECTral:PHASE`` command.
            - ``.refleveloffset``: The ``MATH<x>:SPECTral:REFLEVELOffset`` command.
            - ``.reflevel``: The ``MATH<x>:SPECTral:REFLevel`` command.
            - ``.resbw``: The ``MATH<x>:SPECTral:RESBw`` command.
            - ``.span``: The ``MATH<x>:SPECTral:SPAN`` command.
            - ``.suppress``: The ``MATH<x>:SPECTral:SUPPress`` command.
            - ``.unwrap``: The ``MATH<x>:SPECTral:UNWRap`` command.
            - ``.window``: The ``MATH<x>:SPECTral:WINdow`` command.
        """
        return self._spectral

    @property
    def threshold(self) -> MathItemThreshold:
        """Return the ``MATH<x>:THRESHold`` command.

        Description:
            - This command sets or queries the threshold for the math waveform specified by x, which
              can be 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:THRESHold?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:THRESHold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:THRESHold value`` command.

        SCPI Syntax:
            ```
            - MATH<x>:THRESHold <NR3>
            - MATH<x>:THRESHold?
            ```

        Info:
            - ``<NR3>`` specifies the math threshold in volts.
        """
        return self._threshold

    @property
    def unitstring(self) -> MathItemUnitstring:
        """Return the ``MATH<x>:UNITString`` command.

        Description:
            - This command sets or queries the string to use for units for the math waveform
              specified by x, which can be 1 through 4. This command will override the default unit
              string with the one that you specify.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:UNITString?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:UNITString?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH<x>:UNITString value`` command.

        SCPI Syntax:
            ```
            - MATH<x>:UNITString <QString>
            - MATH<x>:UNITString?
            ```

        Info:
            - ``<QString>`` quoted string argument is the units to be used for the specified math
              waveform.
        """
        return self._unitstring

    @property
    def vertical(self) -> MathItemVertical:
        """Return the ``MATH<x>:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH<x>:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH<x>:VERTical?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.autoscale``: The ``MATH<x>:VERTical:AUTOSCale`` command.
            - ``.position``: The ``MATH<x>:VERTical:POSition`` command.
            - ``.scale``: The ``MATH<x>:VERTical:SCAle`` command.
        """
        return self._vertical
