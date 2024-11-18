"""The math1 commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MATH1:DEFine <QString>
    - MATH1:DEFine?
    - MATH1:HORizontal:POSition <NR3>
    - MATH1:HORizontal:POSition?
    - MATH1:HORizontal:SCAle <NR3>
    - MATH1:HORizontal:SCAle?
    - MATH1:HORizontal:UNIts?
    - MATH1:LABel <QString>
    - MATH1:LABel?
    - MATH1:SPECTral:GATing:INDICators {ON|OFF|<NR1>}
    - MATH1:SPECTral:GATing:INDICators:END?
    - MATH1:SPECTral:GATing:INDICators:STARt?
    - MATH1:SPECTral:GATing:INDICators?
    - MATH1:SPECTral:MAG {LINEAr|DB}
    - MATH1:SPECTral:MAG?
    - MATH1:SPECTral:NYQUISTFreq?
    - MATH1:SPECTral:WINdow {RECTangular|HAMming|HANning|BLAckmanharris}
    - MATH1:SPECTral:WINdow?
    - MATH1:TYPe {DUAL|FFT}
    - MATH1:TYPe?
    - MATH1:VERTical:POSition <NR3>
    - MATH1:VERTical:POSition?
    - MATH1:VERTical:SCAle <NR3>
    - MATH1:VERTical:SCAle?
    - MATH1:VERTical:UNIts?
    - MATH1?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Math1VerticalUnits(SCPICmdRead):
    """The ``MATH1:VERTical:UNIts`` command.

    Description:
        - Returns the math waveform vertical measurement unit value.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:VERTical:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:VERTical:UNIts?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATH1:VERTical:UNIts?
        ```
    """


class Math1VerticalScale(SCPICmdWrite, SCPICmdRead):
    """The ``MATH1:VERTical:SCAle`` command.

    Description:
        - This command specifies the vertical scale of the currently selected math type. This
          setting controls the display only, graphically scaling these waveforms and having no
          affect on the acquisition hardware. For a signal with constant amplitude, increasing the
          scale causes the waveform to be displayed smaller. Decreasing the scale causes the
          waveform to be displayed larger.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:VERTical:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:VERTical:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH1:VERTical:SCAle value`` command.

    SCPI Syntax:
        ```
        - MATH1:VERTical:SCAle <NR3>
        - MATH1:VERTical:SCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the scale-per-division in the current
          math vertical units. The range is from 1.0E-12 through 500.0E+12.
    """


class Math1VerticalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``MATH1:VERTical:POSition`` command.

    Description:
        - This command specifies the vertical position of the currently selected math type.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:VERTical:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:VERTical:POSition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH1:VERTical:POSition value``
          command.

    SCPI Syntax:
        ```
        - MATH1:VERTical:POSition <NR3>
        - MATH1:VERTical:POSition?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the desired position in divisions from
          the center graticule.
    """


class Math1Vertical(SCPICmdRead):
    """The ``MATH1:VERTical`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:VERTical?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:VERTical?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``MATH1:VERTical:POSition`` command.
        - ``.scale``: The ``MATH1:VERTical:SCAle`` command.
        - ``.units``: The ``MATH1:VERTical:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = Math1VerticalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = Math1VerticalScale(device, f"{self._cmd_syntax}:SCAle")
        self._units = Math1VerticalUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def position(self) -> Math1VerticalPosition:
        """Return the ``MATH1:VERTical:POSition`` command.

        Description:
            - This command specifies the vertical position of the currently selected math type.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:VERTical:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:VERTical:POSition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH1:VERTical:POSition value``
              command.

        SCPI Syntax:
            ```
            - MATH1:VERTical:POSition <NR3>
            - MATH1:VERTical:POSition?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the desired position in divisions
              from the center graticule.
        """
        return self._position

    @property
    def scale(self) -> Math1VerticalScale:
        """Return the ``MATH1:VERTical:SCAle`` command.

        Description:
            - This command specifies the vertical scale of the currently selected math type. This
              setting controls the display only, graphically scaling these waveforms and having no
              affect on the acquisition hardware. For a signal with constant amplitude, increasing
              the scale causes the waveform to be displayed smaller. Decreasing the scale causes the
              waveform to be displayed larger.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:VERTical:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:VERTical:SCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH1:VERTical:SCAle value``
              command.

        SCPI Syntax:
            ```
            - MATH1:VERTical:SCAle <NR3>
            - MATH1:VERTical:SCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the scale-per-division in the
              current math vertical units. The range is from 1.0E-12 through 500.0E+12.
        """
        return self._scale

    @property
    def units(self) -> Math1VerticalUnits:
        """Return the ``MATH1:VERTical:UNIts`` command.

        Description:
            - Returns the math waveform vertical measurement unit value.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:VERTical:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:VERTical:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATH1:VERTical:UNIts?
            ```
        """
        return self._units


class Math1Type(SCPICmdWrite, SCPICmdRead):
    """The ``MATH1:TYPe`` command.

    Description:
        - This command specifies the math waveform type - either dual or FFT. This command is
          typically used along with ``1:DEFine``, which specifies the current mathematical
          expression as a text string which defines the waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH1:TYPe value`` command.

    SCPI Syntax:
        ```
        - MATH1:TYPe {DUAL|FFT}
        - MATH1:TYPe?
        ```

    Info:
        - ``DUAL`` sets the math waveform mode to dual waveform math.
        - ``FFT`` sets the math waveform mode to FFT math.
    """


class Math1SpectralWindow(SCPICmdWrite, SCPICmdRead):
    """The ``MATH1:SPECTral:WINdow`` command.

    Description:
        - This command specifies the window function for the spectral analyzer input data for the
          specified math waveform. A spectral window determines what the filter shape of the
          spectral analyzer will be in the frequency domain. It can be described by a mathematical
          function that is multiplied point-by-point times the input data to the spectral analyzer.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:SPECTral:WINdow?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:SPECTral:WINdow?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH1:SPECTral:WINdow value`` command.

    SCPI Syntax:
        ```
        - MATH1:SPECTral:WINdow {RECTangular|HAMming|HANning|BLAckmanharris}
        - MATH1:SPECTral:WINdow?
        ```

    Info:
        - ``RECTangular`` window function is equivalent to multiplying all gate data by one.
        - ``HAMming`` window function is based on a cosine series.
        - ``HANning`` window function is based on a cosine series.
        - ``BLAckmanharris`` window function is based on a cosine series.
    """


class Math1SpectralNyquistfreq(SCPICmdRead):
    """The ``MATH1:SPECTral:NYQUISTFreq`` command.

    Description:
        - Returns the Nyquist frequency of the FFT math waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:SPECTral:NYQUISTFreq?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:SPECTral:NYQUISTFreq?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATH1:SPECTral:NYQUISTFreq?
        ```
    """


class Math1SpectralMag(SCPICmdWrite, SCPICmdRead):
    """The ``MATH1:SPECTral:MAG`` command.

    Description:
        - This command specifies the units of the Spectral Magnification function in the math
          string.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:SPECTral:MAG?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:SPECTral:MAG?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH1:SPECTral:MAG value`` command.

    SCPI Syntax:
        ```
        - MATH1:SPECTral:MAG {LINEAr|DB}
        - MATH1:SPECTral:MAG?
        ```

    Info:
        - ``LINEAR`` sets the SpectralMag units to linear.
        - ``DB`` sets the SpectralMag units to decibels.
    """


class Math1SpectralGatingIndicatorsStart(SCPICmdRead):
    """The ``MATH1:SPECTral:GATing:INDICators:STARt`` command.

    Description:
        - Returns the starting point in the source waveform record used for computing the FFT math
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:SPECTral:GATing:INDICators:STARt?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH1:SPECTral:GATing:INDICators:STARt?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATH1:SPECTral:GATing:INDICators:STARt?
        ```
    """


class Math1SpectralGatingIndicatorsEnd(SCPICmdRead):
    """The ``MATH1:SPECTral:GATing:INDICators:END`` command.

    Description:
        - Returns the ending point in the source waveform record used for computing the FFT

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:SPECTral:GATing:INDICators:END?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH1:SPECTral:GATing:INDICators:END?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATH1:SPECTral:GATing:INDICators:END?
        ```
    """


class Math1SpectralGatingIndicators(SCPICmdWrite, SCPICmdRead):
    """The ``MATH1:SPECTral:GATing:INDICators`` command.

    Description:
        - Enables or disables the display of indicators that show the portion of the source waveform
          record used to compute the math FFT waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:SPECTral:GATing:INDICators?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:SPECTral:GATing:INDICators?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH1:SPECTral:GATing:INDICators value`` command.

    SCPI Syntax:
        ```
        - MATH1:SPECTral:GATing:INDICators {ON|OFF|<NR1>}
        - MATH1:SPECTral:GATing:INDICators?
        ```

    Info:
        - ``OFF`` turns off the display of indicators.
        - ``ON`` turns on the display of indicators.
        - ``<NR1>`` = 0 turns off the display of indicators. Any other value turns on the display of
          indicators.

    Properties:
        - ``.end``: The ``MATH1:SPECTral:GATing:INDICators:END`` command.
        - ``.start``: The ``MATH1:SPECTral:GATing:INDICators:STARt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._end = Math1SpectralGatingIndicatorsEnd(device, f"{self._cmd_syntax}:END")
        self._start = Math1SpectralGatingIndicatorsStart(device, f"{self._cmd_syntax}:STARt")

    @property
    def end(self) -> Math1SpectralGatingIndicatorsEnd:
        """Return the ``MATH1:SPECTral:GATing:INDICators:END`` command.

        Description:
            - Returns the ending point in the source waveform record used for computing the FFT

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:SPECTral:GATing:INDICators:END?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH1:SPECTral:GATing:INDICators:END?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATH1:SPECTral:GATing:INDICators:END?
            ```
        """
        return self._end

    @property
    def start(self) -> Math1SpectralGatingIndicatorsStart:
        """Return the ``MATH1:SPECTral:GATing:INDICators:STARt`` command.

        Description:
            - Returns the starting point in the source waveform record used for computing the FFT
              math waveform.

        Usage:
            - Using the ``.query()`` method will send the
              ``MATH1:SPECTral:GATing:INDICators:STARt?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MATH1:SPECTral:GATing:INDICators:STARt?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATH1:SPECTral:GATing:INDICators:STARt?
            ```
        """
        return self._start


class Math1SpectralGating(SCPICmdRead):
    """The ``MATH1:SPECTral:GATing`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:SPECTral:GATing?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:SPECTral:GATing?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.indicators``: The ``MATH1:SPECTral:GATing:INDICators`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._indicators = Math1SpectralGatingIndicators(device, f"{self._cmd_syntax}:INDICators")

    @property
    def indicators(self) -> Math1SpectralGatingIndicators:
        """Return the ``MATH1:SPECTral:GATing:INDICators`` command.

        Description:
            - Enables or disables the display of indicators that show the portion of the source
              waveform record used to compute the math FFT waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:SPECTral:GATing:INDICators?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH1:SPECTral:GATing:INDICators?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH1:SPECTral:GATing:INDICators value`` command.

        SCPI Syntax:
            ```
            - MATH1:SPECTral:GATing:INDICators {ON|OFF|<NR1>}
            - MATH1:SPECTral:GATing:INDICators?
            ```

        Info:
            - ``OFF`` turns off the display of indicators.
            - ``ON`` turns on the display of indicators.
            - ``<NR1>`` = 0 turns off the display of indicators. Any other value turns on the
              display of indicators.

        Sub-properties:
            - ``.end``: The ``MATH1:SPECTral:GATing:INDICators:END`` command.
            - ``.start``: The ``MATH1:SPECTral:GATing:INDICators:STARt`` command.
        """
        return self._indicators


class Math1Spectral(SCPICmdRead):
    """The ``MATH1:SPECTral`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:SPECTral?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:SPECTral?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.gating``: The ``MATH1:SPECTral:GATing`` command tree.
        - ``.mag``: The ``MATH1:SPECTral:MAG`` command.
        - ``.nyquistfreq``: The ``MATH1:SPECTral:NYQUISTFreq`` command.
        - ``.window``: The ``MATH1:SPECTral:WINdow`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._gating = Math1SpectralGating(device, f"{self._cmd_syntax}:GATing")
        self._mag = Math1SpectralMag(device, f"{self._cmd_syntax}:MAG")
        self._nyquistfreq = Math1SpectralNyquistfreq(device, f"{self._cmd_syntax}:NYQUISTFreq")
        self._window = Math1SpectralWindow(device, f"{self._cmd_syntax}:WINdow")

    @property
    def gating(self) -> Math1SpectralGating:
        """Return the ``MATH1:SPECTral:GATing`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:SPECTral:GATing?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:SPECTral:GATing?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.indicators``: The ``MATH1:SPECTral:GATing:INDICators`` command.
        """
        return self._gating

    @property
    def mag(self) -> Math1SpectralMag:
        """Return the ``MATH1:SPECTral:MAG`` command.

        Description:
            - This command specifies the units of the Spectral Magnification function in the math
              string.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:SPECTral:MAG?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:SPECTral:MAG?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH1:SPECTral:MAG value`` command.

        SCPI Syntax:
            ```
            - MATH1:SPECTral:MAG {LINEAr|DB}
            - MATH1:SPECTral:MAG?
            ```

        Info:
            - ``LINEAR`` sets the SpectralMag units to linear.
            - ``DB`` sets the SpectralMag units to decibels.
        """
        return self._mag

    @property
    def nyquistfreq(self) -> Math1SpectralNyquistfreq:
        """Return the ``MATH1:SPECTral:NYQUISTFreq`` command.

        Description:
            - Returns the Nyquist frequency of the FFT math waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:SPECTral:NYQUISTFreq?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:SPECTral:NYQUISTFreq?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATH1:SPECTral:NYQUISTFreq?
            ```
        """
        return self._nyquistfreq

    @property
    def window(self) -> Math1SpectralWindow:
        """Return the ``MATH1:SPECTral:WINdow`` command.

        Description:
            - This command specifies the window function for the spectral analyzer input data for
              the specified math waveform. A spectral window determines what the filter shape of the
              spectral analyzer will be in the frequency domain. It can be described by a
              mathematical function that is multiplied point-by-point times the input data to the
              spectral analyzer.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:SPECTral:WINdow?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:SPECTral:WINdow?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH1:SPECTral:WINdow value``
              command.

        SCPI Syntax:
            ```
            - MATH1:SPECTral:WINdow {RECTangular|HAMming|HANning|BLAckmanharris}
            - MATH1:SPECTral:WINdow?
            ```

        Info:
            - ``RECTangular`` window function is equivalent to multiplying all gate data by one.
            - ``HAMming`` window function is based on a cosine series.
            - ``HANning`` window function is based on a cosine series.
            - ``BLAckmanharris`` window function is based on a cosine series.
        """
        return self._window


class Math1Label(SCPICmdWrite, SCPICmdRead):
    """The ``MATH1:LABel`` command.

    Description:
        - Sets or queries the waveform label for the math waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH1:LABel value`` command.

    SCPI Syntax:
        ```
        - MATH1:LABel <QString>
        - MATH1:LABel?
        ```

    Info:
        - ``<QString>`` is the quoted string used as the label for the math waveform.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Math1HorizontalUnits(SCPICmdRead):
    """The ``MATH1:HORizontal:UNIts`` command.

    Description:
        - Returns the math waveform horizontal measurement unit value.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:HORizontal:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:HORizontal:UNIts?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATH1:HORizontal:UNIts?
        ```
    """


class Math1HorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``MATH1:HORizontal:SCAle`` command.

    Description:
        - This command specifies the math horizontal display scale for FFT or for dual math
          waveforms that have source waveforms that are reference waveforms. The horizontal scale of
          a dual math waveform with a channel source waveform is set through the command.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:HORizontal:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:HORizontal:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH1:HORizontal:SCAle value`` command.

    SCPI Syntax:
        ```
        - MATH1:HORizontal:SCAle <NR3>
        - MATH1:HORizontal:SCAle?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the math horizontal scale, in seconds.
    """


class Math1HorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``MATH1:HORizontal:POSition`` command.

    Description:
        - This command specifies the math horizontal display position for FFT or (non-live) math
          reference waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:HORizontal:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:HORizontal:POSition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH1:HORizontal:POSition value``
          command.

    SCPI Syntax:
        ```
        - MATH1:HORizontal:POSition <NR3>
        - MATH1:HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the % of the math waveform that
          precedes center screen. It can vary from 0.0 to 100.0.
    """


class Math1Horizontal(SCPICmdRead):
    """The ``MATH1:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:HORizontal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``MATH1:HORizontal:POSition`` command.
        - ``.scale``: The ``MATH1:HORizontal:SCAle`` command.
        - ``.units``: The ``MATH1:HORizontal:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = Math1HorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = Math1HorizontalScale(device, f"{self._cmd_syntax}:SCAle")
        self._units = Math1HorizontalUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def position(self) -> Math1HorizontalPosition:
        """Return the ``MATH1:HORizontal:POSition`` command.

        Description:
            - This command specifies the math horizontal display position for FFT or (non-live) math
              reference waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:HORizontal:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:HORizontal:POSition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH1:HORizontal:POSition value``
              command.

        SCPI Syntax:
            ```
            - MATH1:HORizontal:POSition <NR3>
            - MATH1:HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the % of the math waveform that
              precedes center screen. It can vary from 0.0 to 100.0.
        """
        return self._position

    @property
    def scale(self) -> Math1HorizontalScale:
        """Return the ``MATH1:HORizontal:SCAle`` command.

        Description:
            - This command specifies the math horizontal display scale for FFT or for dual math
              waveforms that have source waveforms that are reference waveforms. The horizontal
              scale of a dual math waveform with a channel source waveform is set through the
              command.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:HORizontal:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:HORizontal:SCAle?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH1:HORizontal:SCAle value``
              command.

        SCPI Syntax:
            ```
            - MATH1:HORizontal:SCAle <NR3>
            - MATH1:HORizontal:SCAle?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the math horizontal scale, in
              seconds.
        """
        return self._scale

    @property
    def units(self) -> Math1HorizontalUnits:
        """Return the ``MATH1:HORizontal:UNIts`` command.

        Description:
            - Returns the math waveform horizontal measurement unit value.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:HORizontal:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:HORizontal:UNIts?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATH1:HORizontal:UNIts?
            ```
        """
        return self._units


class Math1Define(SCPICmdWrite, SCPICmdRead):
    r"""The ``MATH1:DEFine`` command.

    Description:
        - This command specifies the current math function as a text string. You must also specify
          the type (dual waveform, FFT, advanced math, or spectrum math) using ``MATH1:TYPE Dual``
          math expressions are strings of the form <wfm> <operation> <wfm>, where the <wfm>s are any
          combination of live analog or reference waveforms in the time domain display, the
          <operation> is any of +, -, \* or /, and the type has been set to DUAL. FFT math
          expressions are strings of the form FFT(<wfm>), where <wfm> is any live analog or
          reference waveforms in the time domain display, and the type has been set to FFT. Advanced
          math expressions extend beyond dual math expressions, incorporating combinations of
          advanced math functions, measurements, and operators. Spectrum math (MDO models)
          expressions are strings of the form <wfm><operation><wfm>, where the waveforms are any
          combination of live RF or reference traces in the frequency domain display, the
          <operation> is either + or -, and type has been set to SPECTRUM.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1:DEFine?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1:DEFine?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH1:DEFine value`` command.

    SCPI Syntax:
        ```
        - MATH1:DEFine <QString>
        - MATH1:DEFine?
        ```

    Info:
        - ``<QString>`` quoted string argument is the mathematical expression that defines the
          waveform.
        - ``:MATH:DEFINE 'FFT(CH1)'``
        - ``Automatic measurements of waveforms``
        - ``:MATH:DEFINE 'AMPlitude(CH1)'``
        - ``:MATH:DEFINE 'AREA(CH1)'``
        - ``:MATH:DEFINE 'BURST(CH1)'``
        - ``:MATH:DEFINE 'CAREA(CH1)'``
        - ``:MATH:DEFINE 'CMEAN(CH1)'``
        - ``:MATH:DEFINE 'CRMS(CH1)'``
        - ``:MATH:DEFINE 'DELAY(CH1,CH2)'``
        - ``:MATH:DEFINE 'FALL(CH1)'``
        - ``:MATH:DEFINE 'FREQUENCY(CH1)'``
        - ``:MATH:DEFINE 'HIGH(CH1)*CH2'``
        - ``:MATH:DEFINE 'LOW(CH1)'``
        - ``:MATH:DEFINE 'MAXIMUM(CH1)'``
        - ``:MATH:DEFINE 'MEAN(CH1)'``
        - ``:MATH:DEFINE 'MINIMUM(CH1)'``
        - ``:MATH:DEFINE 'NDUTY(CH1)'``
        - ``:MATH:DEFINE 'NOVERSHOOT(CH1)'``
        - ``:MATH:DEFINE 'NWIDTH(CH1)'``
        - ``:MATH:DEFINE 'PDUTY(CH1)'``
        - ``:MATH:DEFINE 'PERIOD(CH1)'``
        - ``:MATH:DEFINE 'PHASE(CH1,CH2)'``
        - ``:MATH:DEFINE 'PK2PK(CH1)'``
        - ``:MATH:DEFINE 'POVERSHOOT(CH1)'``
        - ``:MATH:DEFINE 'PWIDTH(CH1)'``
        - ``:MATH:DEFINE 'RISE(CH1)'``
        - ``:MATH:DEFINE 'RMS(CH1)'``
        - ``:MATH:DEFINE 'SINE(CH1)'``
        - ``Trigonometric operations on expressions``
        - ``:MATH:DEFINE 'ABS(CH2-CH1)'``
        - ``:MATH:DEFINE 'COSine(CH1)'``
        - ``:MATH:DEFINE 'CH1 * DEG(VAR1)'``
        - ``:MATH:DEFINE 'DIFF(CH1)'``
        - ``:MATH:DEFINE 'DIFF(ABS(CH1))'``
        - ``:MATH:DEFINE 'EXP(DIFF(CH1))'``
        - ``:MATH:DEFINE 'FFT(CH1)'``
        - ``:MATH:DEFINE 'FFT(CH1+CH2)'``
        - ``:MATH:DEFINE 'FFT(CH1+ INT(CH2))'``
        - ``:MATH:DEFINE 'CH1 + FFT(CH2)'`` Not acceptable.
        - ``:MATH:DEFINE 'INTG(CH1)'``
        - ``:MATH:DEFINE 'INTG(CH1+CH2)'``
        - ``:MATH:DEFINE 'LOG(CH1)'``
        - ``:MATH:DEFINE 'RAD(PHASE(CH1,CH2))'``
        - ``:MATH:DEFINE 'SQRT(SINE(CH1))'``
        - ``:MATH:DEFINE 'SINE(CH1+CH2)'``
        - ``:MATH:DEFINE 'TAN(CH1)'``
        - ``:MATH:DEFINE 'TRE(PERIOD(CH1))'``
        - ``User-defined variables``
        - ``:MATH:DEFINE 'VAR1+CH1'``
        - ``Relational and logical operators``
        - ``:MATH:DEFINE '(CH1 < CH2)'``
        - ``:MATH:DEFINE '(CH1 > CH2)'``
        - ``:MATH:DEFINE '(CH1 <= CH2)'``
        - ``:MATH:DEFINE '(CH1 >= CH2)'``
        - ``:MATH:DEFINE '(CH1 != CH2)'``
        - ``:MATH:DEFINE 'CH1==CH2'``
        - ``:MATH:DEFINE '(CH1 != CH2)``
        - ``(CH3 == CH4)'``
        - ``:MATH:DEFINE '(CH1 != CH2) && (CH3 == CH4)'``
        - ``:MATH:DEFINE '(CH2-CH1) * !(CH1 >= CH2)'``
    """

    _WRAP_ARG_WITH_QUOTES = True


class Math1(SCPICmdRead):
    """The ``MATH1`` command.

    Description:
        - Returns the definition of the math waveform. The returned data depends on the setting of
          the ``MATH1:TYPE`` command.

    Usage:
        - Using the ``.query()`` method will send the ``MATH1?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH1?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATH1?
        ```

    Properties:
        - ``.define``: The ``MATH1:DEFine`` command.
        - ``.horizontal``: The ``MATH1:HORizontal`` command tree.
        - ``.label``: The ``MATH1:LABel`` command.
        - ``.spectral``: The ``MATH1:SPECTral`` command tree.
        - ``.type``: The ``MATH1:TYPe`` command.
        - ``.vertical``: The ``MATH1:VERTical`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MATH1") -> None:
        super().__init__(device, cmd_syntax)
        self._define = Math1Define(device, f"{self._cmd_syntax}:DEFine")
        self._horizontal = Math1Horizontal(device, f"{self._cmd_syntax}:HORizontal")
        self._label = Math1Label(device, f"{self._cmd_syntax}:LABel")
        self._spectral = Math1Spectral(device, f"{self._cmd_syntax}:SPECTral")
        self._type = Math1Type(device, f"{self._cmd_syntax}:TYPe")
        self._vertical = Math1Vertical(device, f"{self._cmd_syntax}:VERTical")

    @property
    def define(self) -> Math1Define:
        r"""Return the ``MATH1:DEFine`` command.

        Description:
            - This command specifies the current math function as a text string. You must also
              specify the type (dual waveform, FFT, advanced math, or spectrum math) using
              ``MATH1:TYPE Dual`` math expressions are strings of the form <wfm> <operation> <wfm>,
              where the <wfm>s are any combination of live analog or reference waveforms in the time
              domain display, the <operation> is any of +, -, \* or /, and the type has been set to
              DUAL. FFT math expressions are strings of the form FFT(<wfm>), where <wfm> is any live
              analog or reference waveforms in the time domain display, and the type has been set to
              FFT. Advanced math expressions extend beyond dual math expressions, incorporating
              combinations of advanced math functions, measurements, and operators. Spectrum math
              (MDO models) expressions are strings of the form <wfm><operation><wfm>, where the
              waveforms are any combination of live RF or reference traces in the frequency domain
              display, the <operation> is either + or -, and type has been set to SPECTRUM.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:DEFine?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:DEFine?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH1:DEFine value`` command.

        SCPI Syntax:
            ```
            - MATH1:DEFine <QString>
            - MATH1:DEFine?
            ```

        Info:
            - ``<QString>`` quoted string argument is the mathematical expression that defines the
              waveform.
            - ``:MATH:DEFINE 'FFT(CH1)'``
            - ``Automatic measurements of waveforms``
            - ``:MATH:DEFINE 'AMPlitude(CH1)'``
            - ``:MATH:DEFINE 'AREA(CH1)'``
            - ``:MATH:DEFINE 'BURST(CH1)'``
            - ``:MATH:DEFINE 'CAREA(CH1)'``
            - ``:MATH:DEFINE 'CMEAN(CH1)'``
            - ``:MATH:DEFINE 'CRMS(CH1)'``
            - ``:MATH:DEFINE 'DELAY(CH1,CH2)'``
            - ``:MATH:DEFINE 'FALL(CH1)'``
            - ``:MATH:DEFINE 'FREQUENCY(CH1)'``
            - ``:MATH:DEFINE 'HIGH(CH1)*CH2'``
            - ``:MATH:DEFINE 'LOW(CH1)'``
            - ``:MATH:DEFINE 'MAXIMUM(CH1)'``
            - ``:MATH:DEFINE 'MEAN(CH1)'``
            - ``:MATH:DEFINE 'MINIMUM(CH1)'``
            - ``:MATH:DEFINE 'NDUTY(CH1)'``
            - ``:MATH:DEFINE 'NOVERSHOOT(CH1)'``
            - ``:MATH:DEFINE 'NWIDTH(CH1)'``
            - ``:MATH:DEFINE 'PDUTY(CH1)'``
            - ``:MATH:DEFINE 'PERIOD(CH1)'``
            - ``:MATH:DEFINE 'PHASE(CH1,CH2)'``
            - ``:MATH:DEFINE 'PK2PK(CH1)'``
            - ``:MATH:DEFINE 'POVERSHOOT(CH1)'``
            - ``:MATH:DEFINE 'PWIDTH(CH1)'``
            - ``:MATH:DEFINE 'RISE(CH1)'``
            - ``:MATH:DEFINE 'RMS(CH1)'``
            - ``:MATH:DEFINE 'SINE(CH1)'``
            - ``Trigonometric operations on expressions``
            - ``:MATH:DEFINE 'ABS(CH2-CH1)'``
            - ``:MATH:DEFINE 'COSine(CH1)'``
            - ``:MATH:DEFINE 'CH1 * DEG(VAR1)'``
            - ``:MATH:DEFINE 'DIFF(CH1)'``
            - ``:MATH:DEFINE 'DIFF(ABS(CH1))'``
            - ``:MATH:DEFINE 'EXP(DIFF(CH1))'``
            - ``:MATH:DEFINE 'FFT(CH1)'``
            - ``:MATH:DEFINE 'FFT(CH1+CH2)'``
            - ``:MATH:DEFINE 'FFT(CH1+ INT(CH2))'``
            - ``:MATH:DEFINE 'CH1 + FFT(CH2)'`` Not acceptable.
            - ``:MATH:DEFINE 'INTG(CH1)'``
            - ``:MATH:DEFINE 'INTG(CH1+CH2)'``
            - ``:MATH:DEFINE 'LOG(CH1)'``
            - ``:MATH:DEFINE 'RAD(PHASE(CH1,CH2))'``
            - ``:MATH:DEFINE 'SQRT(SINE(CH1))'``
            - ``:MATH:DEFINE 'SINE(CH1+CH2)'``
            - ``:MATH:DEFINE 'TAN(CH1)'``
            - ``:MATH:DEFINE 'TRE(PERIOD(CH1))'``
            - ``User-defined variables``
            - ``:MATH:DEFINE 'VAR1+CH1'``
            - ``Relational and logical operators``
            - ``:MATH:DEFINE '(CH1 < CH2)'``
            - ``:MATH:DEFINE '(CH1 > CH2)'``
            - ``:MATH:DEFINE '(CH1 <= CH2)'``
            - ``:MATH:DEFINE '(CH1 >= CH2)'``
            - ``:MATH:DEFINE '(CH1 != CH2)'``
            - ``:MATH:DEFINE 'CH1==CH2'``
            - ``:MATH:DEFINE '(CH1 != CH2)``
            - ``(CH3 == CH4)'``
            - ``:MATH:DEFINE '(CH1 != CH2) && (CH3 == CH4)'``
            - ``:MATH:DEFINE '(CH2-CH1) * !(CH1 >= CH2)'``
        """
        return self._define

    @property
    def horizontal(self) -> Math1Horizontal:
        """Return the ``MATH1:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:HORizontal?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:HORizontal?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``MATH1:HORizontal:POSition`` command.
            - ``.scale``: The ``MATH1:HORizontal:SCAle`` command.
            - ``.units``: The ``MATH1:HORizontal:UNIts`` command.
        """
        return self._horizontal

    @property
    def label(self) -> Math1Label:
        """Return the ``MATH1:LABel`` command.

        Description:
            - Sets or queries the waveform label for the math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:LABel?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH1:LABel value`` command.

        SCPI Syntax:
            ```
            - MATH1:LABel <QString>
            - MATH1:LABel?
            ```

        Info:
            - ``<QString>`` is the quoted string used as the label for the math waveform.
        """
        return self._label

    @property
    def spectral(self) -> Math1Spectral:
        """Return the ``MATH1:SPECTral`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:SPECTral?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:SPECTral?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.gating``: The ``MATH1:SPECTral:GATing`` command tree.
            - ``.mag``: The ``MATH1:SPECTral:MAG`` command.
            - ``.nyquistfreq``: The ``MATH1:SPECTral:NYQUISTFreq`` command.
            - ``.window``: The ``MATH1:SPECTral:WINdow`` command.
        """
        return self._spectral

    @property
    def type(self) -> Math1Type:
        """Return the ``MATH1:TYPe`` command.

        Description:
            - This command specifies the math waveform type - either dual or FFT. This command is
              typically used along with ``1:DEFine``, which specifies the current mathematical
              expression as a text string which defines the waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:TYPe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH1:TYPe value`` command.

        SCPI Syntax:
            ```
            - MATH1:TYPe {DUAL|FFT}
            - MATH1:TYPe?
            ```

        Info:
            - ``DUAL`` sets the math waveform mode to dual waveform math.
            - ``FFT`` sets the math waveform mode to FFT math.
        """
        return self._type

    @property
    def vertical(self) -> Math1Vertical:
        """Return the ``MATH1:VERTical`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH1:VERTical?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH1:VERTical?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``MATH1:VERTical:POSition`` command.
            - ``.scale``: The ``MATH1:VERTical:SCAle`` command.
            - ``.units``: The ``MATH1:VERTical:UNIts`` command.
        """
        return self._vertical
