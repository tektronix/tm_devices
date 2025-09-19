# pylint: disable=line-too-long
"""The plot commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - PLOT:ADDNew <QString>
    - PLOT:DELete <QString>
    - PLOT:LIST?
    - PLOT:PLOT<x>:BATHtub:BER <NR1>
    - PLOT:PLOT<x>:BATHtub:BER?
    - PLOT:PLOT<x>:BATHtub:XAXISUnits {UNITIntervals|SECOnds}
    - PLOT:PLOT<x>:BATHtub:XAXISUnits?
    - PLOT:PLOT<x>:BITType {ALLBits|TRANSition|NONTRANsition}
    - PLOT:PLOT<x>:BITType?
    - PLOT:PLOT<x>:EXPORTRaw?
    - PLOT:PLOT<x>:EXTENDuis <NR1>
    - PLOT:PLOT<x>:EXTENDuis?
    - PLOT:PLOT<x>:EYERender {FAst|COMPlete}
    - PLOT:PLOT<x>:EYERender?
    - PLOT:PLOT<x>:IMDA:MEAS {VRMS|IRMS|PHASE|FREQuency|TRPWR|REPWR|APPPWR|TRPWRSUM|REPWRSUM|APPPWRSUM|DCPWR|INPWR|OUTPWR|EFFiciency|TOTALEFFiciency|INPWRSUM|OUTPWRSUM}
    - PLOT:PLOT<x>:IMDA:MEAS?
    - PLOT:PLOT<x>:IMDAPLOTDisplay {ALL|ONEPAIRVI|ONEPAIRV|ONEPAIRI|PHASEONE|PHASETWO|PHASETHREE|ABC|DQ0}
    - PLOT:PLOT<x>:IMDAPLOTDisplay?
    - PLOT:PLOT<x>:LABel:COLor <QString>
    - PLOT:PLOT<x>:LABel:COLor?
    - PLOT:PLOT<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
    - PLOT:PLOT<x>:LABel:FONT:BOLD?
    - PLOT:PLOT<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
    - PLOT:PLOT<x>:LABel:FONT:ITALic?
    - PLOT:PLOT<x>:LABel:FONT:SIZE <NR1>
    - PLOT:PLOT<x>:LABel:FONT:SIZE?
    - PLOT:PLOT<x>:LABel:FONT:TYPE <QString>
    - PLOT:PLOT<x>:LABel:FONT:TYPE?
    - PLOT:PLOT<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
    - PLOT:PLOT<x>:LABel:FONT:UNDERline?
    - PLOT:PLOT<x>:LABel:NAMe <QString>
    - PLOT:PLOT<x>:LABel:NAMe?
    - PLOT:PLOT<x>:LABel:XPOS <NR3>
    - PLOT:PLOT<x>:LABel:XPOS?
    - PLOT:PLOT<x>:LABel:YPOS <NR3>
    - PLOT:PLOT<x>:LABel:YPOS?
    - PLOT:PLOT<x>:MASK?
    - PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit {ON|OFF}
    - PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit?
    - PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM <NR3>
    - PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM?
    - PLOT:PLOT<x>:MASKOffset:PERCENTui:TO <NR3>
    - PLOT:PLOT<x>:MASKOffset:PERCENTui:TO?
    - PLOT:PLOT<x>:NUMBins {TWENtyfive|FIFTY|HUNdred|TWOFifty|FIVEHundred|TWOThousand|MAXimum}
    - PLOT:PLOT<x>:NUMBins?
    - PLOT:PLOT<x>:PTYPe {RMS|MAGNITUDE}
    - PLOT:PLOT<x>:PTYPe?
    - PLOT:PLOT<x>:RAILNUM RAIL<x>
    - PLOT:PLOT<x>:RAILNUM?
    - PLOT:PLOT<x>:SOUrce1 MEAS<x>
    - PLOT:PLOT<x>:SOUrce1?
    - PLOT:PLOT<x>:SPECtrum:BASE <NR1>
    - PLOT:PLOT<x>:SPECtrum:BASE?
    - PLOT:PLOT<x>:SPECtrum:DYNRange <NR3>
    - PLOT:PLOT<x>:SPECtrum:DYNRange?
    - PLOT:PLOT<x>:TYPe {NONE|BATHTUB|EYEDIAGRAM|HARMONICS|HISTOGRAM|IMDATIMETREND|IMDAACQTREND|INDUCTANCE|IVSINTEGRALV|MAGPROPERTY|PHASENOISE|PHASOR|SOA|SPECTRUM|SSCPROFILE|SWL|TIEHISTOGRAM|TIETIMETREND|TIESPECTRUM|TIMETREND|XY|XYZ}
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class PlotPlotItemType(SCPICmdWrite):
    """The ``PLOT:PLOT<x>:TYPe`` command.

    Description:
        - This command sets or returns the current plot type of the specified plot.

    Usage:
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:TYPe value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:TYPe {NONE|BATHTUB|EYEDIAGRAM|HARMONICS|HISTOGRAM|IMDATIMETREND|IMDAACQTREND|INDUCTANCE|IVSINTEGRALV|MAGPROPERTY|PHASENOISE|PHASOR|SOA|SPECTRUM|SSCPROFILE|SWL|TIEHISTOGRAM|TIETIMETREND|TIESPECTRUM|TIMETREND|XY|XYZ}
        ```

    Info:
        - ``<x>`` is the plot number. This is the equivalent of the number shown on a plot heading
          in the UI.
        - ``NONE`` does not create a plot.
        - ``BATHTUB`` creates a bathtub plot.
        - ``EYEDIAGRAM`` creates an eye diagram. This plot type is not available on a 4 Series MSO
          instrument.
        - ``HARMONICS`` creates a harmonics bar graph.
        - ``HISTOGRAM`` creates a histogram plot.
        - ``IMDATIMETREND`` creates a IMDA time trend plot. This plot type requires option IMDA.
        - ``IMDAACQTREND`` creates a IMDA acq trend plot. This plot type requires option IMDA.
        - ``INDUCTANCE`` creates a inductance plot.
        - ``IVSINTEGRALV`` creates a I vs. ∫V plot.
        - ``PHASENOISE`` creates a phase noise plot.
        - ``PHASOR`` creates the Phasor Diagram. This plot type requires option 5-DPM on MSO58/56
          series instruments.
        - ``MAGPROPERTY`` creates a BH curve.
        - ``SOA`` creates an SOA plot.
        - ``SPECTRUM`` creates a spectrum plot.
        - ``SSCPROFILE`` creates a SSC profile plot.
        - ``SWL`` creates a Switching Loss plot.
        - ``TIEHISTOGRAM`` creates a TIE histogram plot.
        - ``TIESPECTRUM`` creates a TIE spectrum plot.
        - ``TIETIMETREND`` creates a TIE time trend plot.
        - ``TIMETREND`` creates a time trend plot.
        - ``XY`` creates a XY plot.
        - ``XYZ`` creates a XYZ plot.
    """  # noqa: E501


class PlotPlotItemSpectrumDynrange(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:SPECtrum:DYNRange`` command.

    Description:
        - This command sets or queries the dynamic range value.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:SPECtrum:DYNRange?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:SPECtrum:DYNRange?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:SPECtrum:DYNRange value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:SPECtrum:DYNRange <NR3>
        - PLOT:PLOT<x>:SPECtrum:DYNRange?
        ```

    Info:
        - ``<NR3>`` is the dynamic range value.
    """


class PlotPlotItemSpectrumBase(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:SPECtrum:BASE`` command.

    Description:
        - This command sets or queries the spectrum base. Undefined for non-spectrum plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:SPECtrum:BASE?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:SPECtrum:BASE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:SPECtrum:BASE value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:SPECtrum:BASE <NR1>
        - PLOT:PLOT<x>:SPECtrum:BASE?
        ```

    Info:
        - ``<NR1>`` is the spectrum base.
    """


class PlotPlotItemSpectrum(SCPICmdRead):
    """The ``PLOT:PLOT<x>:SPECtrum`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:SPECtrum?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:SPECtrum?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.base``: The ``PLOT:PLOT<x>:SPECtrum:BASE`` command.
        - ``.dynrange``: The ``PLOT:PLOT<x>:SPECtrum:DYNRange`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._base = PlotPlotItemSpectrumBase(device, f"{self._cmd_syntax}:BASE")
        self._dynrange = PlotPlotItemSpectrumDynrange(device, f"{self._cmd_syntax}:DYNRange")

    @property
    def base(self) -> PlotPlotItemSpectrumBase:
        """Return the ``PLOT:PLOT<x>:SPECtrum:BASE`` command.

        Description:
            - This command sets or queries the spectrum base. Undefined for non-spectrum plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:SPECtrum:BASE?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:SPECtrum:BASE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:SPECtrum:BASE value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:SPECtrum:BASE <NR1>
            - PLOT:PLOT<x>:SPECtrum:BASE?
            ```

        Info:
            - ``<NR1>`` is the spectrum base.
        """
        return self._base

    @property
    def dynrange(self) -> PlotPlotItemSpectrumDynrange:
        """Return the ``PLOT:PLOT<x>:SPECtrum:DYNRange`` command.

        Description:
            - This command sets or queries the dynamic range value.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:SPECtrum:DYNRange?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:SPECtrum:DYNRange?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PLOT:PLOT<x>:SPECtrum:DYNRange value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:SPECtrum:DYNRange <NR3>
            - PLOT:PLOT<x>:SPECtrum:DYNRange?
            ```

        Info:
            - ``<NR3>`` is the dynamic range value.
        """
        return self._dynrange


class PlotPlotItemSource1(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:SOUrce1`` command.

    Description:
        - This command sets or queries the plot source.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:SOUrce1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:SOUrce1 value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:SOUrce1 MEAS<x>
        - PLOT:PLOT<x>:SOUrce1?
        ```

    Info:
        - ``MEAS<x>`` is the specified measurement source for the specified plot.
    """


class PlotPlotItemRailnum(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:RAILNUM`` command.

    Description:
        - Sets the DPM histogram source.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:RAILNUM?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:RAILNUM?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:RAILNUM value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:RAILNUM RAIL<x>
        - PLOT:PLOT<x>:RAILNUM?
        ```

    Info:
        - ``PLOT<x>`` is the plot number.
        - ``Rail<x>`` is the rail number. x has a minimum of 1 and a maximum of 7.
    """


class PlotPlotItemPtype(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:PTYPe`` command.

    Description:
        - This command sets or returns the phasor type of the phasor diagram plot.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:PTYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:PTYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:PTYPe value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:PTYPe {RMS|MAGNITUDE}
        - PLOT:PLOT<x>:PTYPe?
        ```

    Info:
        - ``PLOT<x>`` is the plot number.
        - ``RMS`` sets the phasor type to RMS.
        - ``MAGNITUDE`` sets the phasor type to MAGNITUDE.
    """


class PlotPlotItemNumbins(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:NUMBins`` command.

    Description:
        - This command sets or queries the current histogram resolution.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:NUMBins?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:NUMBins?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:NUMBins value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:NUMBins {TWENtyfive|FIFTY|HUNdred|TWOFifty|FIVEHundred|TWOThousand|MAXimum}
        - PLOT:PLOT<x>:NUMBins?
        ```

    Info:
        - ``TWENtyfive`` sets the number of bins to 25.
        - ``FIFTY`` sets the number of bins to 50.
        - ``HUNdred`` sets the number of bins to 100.
        - ``TWOFifty`` sets the number of bins to 250.
        - ``FIVEHundred`` sets the number of bins to 500.
        - ``TWOThousand`` sets the number of bins to 2000.
        - ``MAXimum`` sets the number of bins to the maximum value.
    """


class PlotPlotItemMaskoffsetPercentuiTo(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:MASKOffset:PERCENTui:TO`` command.

    Description:
        - This command sets or queries the allowed range for the mask to move in the right
          direction. Only applies to eye diagram plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:MASKOffset:PERCENTui:TO?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``PLOT:PLOT<x>:MASKOffset:PERCENTui:TO?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``PLOT:PLOT<x>:MASKOffset:PERCENTui:TO value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:MASKOffset:PERCENTui:TO <NR3>
        - PLOT:PLOT<x>:MASKOffset:PERCENTui:TO?
        ```

    Info:
        - ``PLOT<x>`` is the plot number.
        - ``<NR3>`` is the allowed range in percentage for the mask to move in the right direction.
    """


class PlotPlotItemMaskoffsetPercentuiFrom(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM`` command.

    Description:
        - This command sets or queries the allowed range for the mask to move in the left direction.
          Only applies to eye diagram plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM <NR3>
        - PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM?
        ```

    Info:
        - ``PLOT<x>`` is the plot number.
        - ``<NR3>`` is the allowed range in percentage for the mask to move in the left direction.
    """


class PlotPlotItemMaskoffsetPercentui(SCPICmdRead):
    """The ``PLOT:PLOT<x>:MASKOffset:PERCENTui`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:MASKOffset:PERCENTui?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:MASKOffset:PERCENTui?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``PLOT<x>`` is the plot number.

    Properties:
        - ``.from``: The ``PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM`` command.
        - ``.to``: The ``PLOT:PLOT<x>:MASKOffset:PERCENTui:TO`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._from = PlotPlotItemMaskoffsetPercentuiFrom(device, f"{self._cmd_syntax}:FROM")
        self._to = PlotPlotItemMaskoffsetPercentuiTo(device, f"{self._cmd_syntax}:TO")

    @property
    def from_(self) -> PlotPlotItemMaskoffsetPercentuiFrom:
        """Return the ``PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM`` command.

        Description:
            - This command sets or queries the allowed range for the mask to move in the left
              direction. Only applies to eye diagram plots.

        Usage:
            - Using the ``.query()`` method will send the
              ``PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM?`` query.
            - Using the ``.verify(value)`` method will send the
              ``PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM <NR3>
            - PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM?
            ```

        Info:
            - ``PLOT<x>`` is the plot number.
            - ``<NR3>`` is the allowed range in percentage for the mask to move in the left
              direction.
        """
        return self._from

    @property
    def to(self) -> PlotPlotItemMaskoffsetPercentuiTo:
        """Return the ``PLOT:PLOT<x>:MASKOffset:PERCENTui:TO`` command.

        Description:
            - This command sets or queries the allowed range for the mask to move in the right
              direction. Only applies to eye diagram plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:MASKOffset:PERCENTui:TO?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``PLOT:PLOT<x>:MASKOffset:PERCENTui:TO?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PLOT:PLOT<x>:MASKOffset:PERCENTui:TO value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:MASKOffset:PERCENTui:TO <NR3>
            - PLOT:PLOT<x>:MASKOffset:PERCENTui:TO?
            ```

        Info:
            - ``PLOT<x>`` is the plot number.
            - ``<NR3>`` is the allowed range in percentage for the mask to move in the right
              direction.
        """
        return self._to


class PlotPlotItemMaskoffsetHorizontalAutofit(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit`` command.

    Description:
        - This command enables or disables eye mask autofit in the specified plot.

    Usage:
        - Using the ``.query()`` method will send the
          ``PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit?`` query.
        - Using the ``.verify(value)`` method will send the
          ``PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit {ON|OFF}
        - PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit?
        ```

    Info:
        - ``PLOT<x>`` is the plot number.
        - ``ON`` enables eye mask autofit.
        - ``OFF`` disables eye mask autofit.
    """


class PlotPlotItemMaskoffsetHorizontal(SCPICmdRead):
    """The ``PLOT:PLOT<x>:MASKOffset:HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:MASKOffset:HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:MASKOffset:HORizontal?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``PLOT<x>`` is the plot number.

    Properties:
        - ``.autofit``: The ``PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autofit = PlotPlotItemMaskoffsetHorizontalAutofit(
            device, f"{self._cmd_syntax}:AUTOfit"
        )

    @property
    def autofit(self) -> PlotPlotItemMaskoffsetHorizontalAutofit:
        """Return the ``PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit`` command.

        Description:
            - This command enables or disables eye mask autofit in the specified plot.

        Usage:
            - Using the ``.query()`` method will send the
              ``PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit?`` query.
            - Using the ``.verify(value)`` method will send the
              ``PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit {ON|OFF}
            - PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit?
            ```

        Info:
            - ``PLOT<x>`` is the plot number.
            - ``ON`` enables eye mask autofit.
            - ``OFF`` disables eye mask autofit.
        """
        return self._autofit


class PlotPlotItemMaskoffset(SCPICmdRead):
    """The ``PLOT:PLOT<x>:MASKOffset`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:MASKOffset?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:MASKOffset?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``PLOT<x>`` is the plot number.

    Properties:
        - ``.horizontal``: The ``PLOT:PLOT<x>:MASKOffset:HORizontal`` command tree.
        - ``.percentui``: The ``PLOT:PLOT<x>:MASKOffset:PERCENTui`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horizontal = PlotPlotItemMaskoffsetHorizontal(
            device, f"{self._cmd_syntax}:HORizontal"
        )
        self._percentui = PlotPlotItemMaskoffsetPercentui(device, f"{self._cmd_syntax}:PERCENTui")

    @property
    def horizontal(self) -> PlotPlotItemMaskoffsetHorizontal:
        """Return the ``PLOT:PLOT<x>:MASKOffset:HORizontal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:MASKOffset:HORizontal?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``PLOT:PLOT<x>:MASKOffset:HORizontal?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``PLOT<x>`` is the plot number.

        Sub-properties:
            - ``.autofit``: The ``PLOT:PLOT<x>:MASKOffset:HORizontal:AUTOfit`` command.
        """
        return self._horizontal

    @property
    def percentui(self) -> PlotPlotItemMaskoffsetPercentui:
        """Return the ``PLOT:PLOT<x>:MASKOffset:PERCENTui`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:MASKOffset:PERCENTui?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``PLOT:PLOT<x>:MASKOffset:PERCENTui?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``PLOT<x>`` is the plot number.

        Sub-properties:
            - ``.from``: The ``PLOT:PLOT<x>:MASKOffset:PERCENTui:FROM`` command.
            - ``.to``: The ``PLOT:PLOT<x>:MASKOffset:PERCENTui:TO`` command.
        """
        return self._percentui


class PlotPlotItemMask(SCPICmdRead):
    """The ``PLOT:PLOT<x>:MASK`` command.

    Description:
        - This command returns the name of the mask test associated with the specified eye diagram
          plot.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:MASK?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:MASK?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:MASK?
        ```

    Info:
        - ``PLOT<x>`` is the plot number.
    """


class PlotPlotItemLabelYpos(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:LABel:YPOS`` command.

    Description:
        - This command sets or queries the y-position of the specified trend label. This
          command/query only applies to Time Trend plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:YPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:YPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:YPOS value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:LABel:YPOS <NR3>
        - PLOT:PLOT<x>:LABel:YPOS?
        ```

    Info:
        - ``<NR3>`` is the x-position, in pixels relative to the baseline of the waveform, of the
          label.
    """


class PlotPlotItemLabelXpos(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:LABel:XPOS`` command.

    Description:
        - This command sets or queries the x-position of the specified trend label. This
          command/query only applies to Time Trend plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:XPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:XPOS value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:LABel:XPOS <NR3>
        - PLOT:PLOT<x>:LABel:XPOS?
        ```

    Info:
        - ``<NR3>`` is the y-position, in pixels relative to the left edge of the display, of the
          label.
    """


class PlotPlotItemLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:LABel:NAMe`` command.

    Description:
        - This command sets or queries the specified trend's label. This command/query only applies
          to Time Trend plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:NAMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:NAMe value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:LABel:NAMe <QString>
        - PLOT:PLOT<x>:LABel:NAMe?
        ```

    Info:
        - ``<QString>`` is the label.
    """

    _WRAP_ARG_WITH_QUOTES = True


class PlotPlotItemLabelFontUnderline(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:LABel:FONT:UNDERline`` command.

    Description:
        - This command sets or queries the underline state of the specified trend label. This
          command/query only applies to Time Trend plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT:UNDERline?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:UNDERline?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``PLOT:PLOT<x>:LABel:FONT:UNDERline value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
        - PLOT:PLOT<x>:LABel:FONT:UNDERline?
        ```

    Info:
        - ``<NR1>`` = 0 disables underline font; any other value turns this feature on.
        - ``OFF`` disables underline font.
        - ``ON`` enables underline font.
    """


class PlotPlotItemLabelFontType(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:LABel:FONT:TYPE`` command.

    Description:
        - This command sets or queries the font type of the specified trend label, such as Arial or
          Times New Roman. This command/query only applies to Time Trend plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:TYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:TYPE value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:LABel:FONT:TYPE <QString>
        - PLOT:PLOT<x>:LABel:FONT:TYPE?
        ```

    Info:
        - ``<QString>`` is the font type: Times New Roman, Arial, Frutiger LT Std 55 Roman, DejaVu
          Sans, DejaVu Sans Mono, Frutiger LT Std, Monospace, Sans Serif, Serif, Ubuntu, Ubuntu
          Condensed, and Ubuntu Mono.
    """

    _WRAP_ARG_WITH_QUOTES = True


class PlotPlotItemLabelFontSize(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:LABel:FONT:SIZE`` command.

    Description:
        - This command sets or queries the font size of the specified trend label. This
          command/query only applies to Time Trend plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:SIZE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:SIZE value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:LABel:FONT:SIZE <NR1>
        - PLOT:PLOT<x>:LABel:FONT:SIZE?
        ```

    Info:
        - ``<NR1>`` is the font size.
    """


class PlotPlotItemLabelFontItalic(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:LABel:FONT:ITALic`` command.

    Description:
        - This command sets or queries the italic state of the specified trend label. This
          command/query only applies to Time Trend plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT:ITALic?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:ITALic?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:ITALic value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
        - PLOT:PLOT<x>:LABel:FONT:ITALic?
        ```

    Info:
        - ``<NR1>`` = 0 disables italic font; any other value turns this feature on.
        - ``OFF`` disables italic font.
        - ``ON`` enables italic font.
    """


class PlotPlotItemLabelFontBold(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:LABel:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the specified trend label. This
          command/query only applies to Time Trend plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT:BOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:BOLD?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:BOLD value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
        - PLOT:PLOT<x>:LABel:FONT:BOLD?
        ```

    Info:
        - ``<NR1>`` = 0 disables bold font; any other value turns this feature on.
        - ``OFF`` disables bold font.
        - ``ON`` enables bold font.
    """


class PlotPlotItemLabelFont(SCPICmdRead):
    """The ``PLOT:PLOT<x>:LABel:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bold``: The ``PLOT:PLOT<x>:LABel:FONT:BOLD`` command.
        - ``.italic``: The ``PLOT:PLOT<x>:LABel:FONT:ITALic`` command.
        - ``.size``: The ``PLOT:PLOT<x>:LABel:FONT:SIZE`` command.
        - ``.type``: The ``PLOT:PLOT<x>:LABel:FONT:TYPE`` command.
        - ``.underline``: The ``PLOT:PLOT<x>:LABel:FONT:UNDERline`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = PlotPlotItemLabelFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = PlotPlotItemLabelFontItalic(device, f"{self._cmd_syntax}:ITALic")
        self._size = PlotPlotItemLabelFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = PlotPlotItemLabelFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = PlotPlotItemLabelFontUnderline(device, f"{self._cmd_syntax}:UNDERline")

    @property
    def bold(self) -> PlotPlotItemLabelFontBold:
        """Return the ``PLOT:PLOT<x>:LABel:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the specified trend label. This
              command/query only applies to Time Trend plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT:BOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:BOLD?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PLOT:PLOT<x>:LABel:FONT:BOLD value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
            - PLOT:PLOT<x>:LABel:FONT:BOLD?
            ```

        Info:
            - ``<NR1>`` = 0 disables bold font; any other value turns this feature on.
            - ``OFF`` disables bold font.
            - ``ON`` enables bold font.
        """
        return self._bold

    @property
    def italic(self) -> PlotPlotItemLabelFontItalic:
        """Return the ``PLOT:PLOT<x>:LABel:FONT:ITALic`` command.

        Description:
            - This command sets or queries the italic state of the specified trend label. This
              command/query only applies to Time Trend plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT:ITALic?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:ITALic?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PLOT:PLOT<x>:LABel:FONT:ITALic value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
            - PLOT:PLOT<x>:LABel:FONT:ITALic?
            ```

        Info:
            - ``<NR1>`` = 0 disables italic font; any other value turns this feature on.
            - ``OFF`` disables italic font.
            - ``ON`` enables italic font.
        """
        return self._italic

    @property
    def size(self) -> PlotPlotItemLabelFontSize:
        """Return the ``PLOT:PLOT<x>:LABel:FONT:SIZE`` command.

        Description:
            - This command sets or queries the font size of the specified trend label. This
              command/query only applies to Time Trend plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:SIZE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PLOT:PLOT<x>:LABel:FONT:SIZE value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:LABel:FONT:SIZE <NR1>
            - PLOT:PLOT<x>:LABel:FONT:SIZE?
            ```

        Info:
            - ``<NR1>`` is the font size.
        """
        return self._size

    @property
    def type(self) -> PlotPlotItemLabelFontType:
        """Return the ``PLOT:PLOT<x>:LABel:FONT:TYPE`` command.

        Description:
            - This command sets or queries the font type of the specified trend label, such as Arial
              or Times New Roman. This command/query only applies to Time Trend plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PLOT:PLOT<x>:LABel:FONT:TYPE value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:LABel:FONT:TYPE <QString>
            - PLOT:PLOT<x>:LABel:FONT:TYPE?
            ```

        Info:
            - ``<QString>`` is the font type: Times New Roman, Arial, Frutiger LT Std 55 Roman,
              DejaVu Sans, DejaVu Sans Mono, Frutiger LT Std, Monospace, Sans Serif, Serif, Ubuntu,
              Ubuntu Condensed, and Ubuntu Mono.
        """
        return self._type

    @property
    def underline(self) -> PlotPlotItemLabelFontUnderline:
        """Return the ``PLOT:PLOT<x>:LABel:FONT:UNDERline`` command.

        Description:
            - This command sets or queries the underline state of the specified trend label. This
              command/query only applies to Time Trend plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT:UNDERline?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``PLOT:PLOT<x>:LABel:FONT:UNDERline?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PLOT:PLOT<x>:LABel:FONT:UNDERline value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
            - PLOT:PLOT<x>:LABel:FONT:UNDERline?
            ```

        Info:
            - ``<NR1>`` = 0 disables underline font; any other value turns this feature on.
            - ``OFF`` disables underline font.
            - ``ON`` enables underline font.
        """
        return self._underline


class PlotPlotItemLabelColor(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:LABel:COLor`` command.

    Description:
        - This command sets or queries the color of the specified trend label. This command/query
          only applies to Time Trend plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:COLor?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:COLor?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:COLor value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:LABel:COLor <QString>
        - PLOT:PLOT<x>:LABel:COLor?
        ```

    Info:
        - ``<QString>`` is the label color. The default color is specified by a quoted empty string,
          and is the only available color.
    """

    _WRAP_ARG_WITH_QUOTES = True


class PlotPlotItemLabel(SCPICmdRead):
    """The ``PLOT:PLOT<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.color``: The ``PLOT:PLOT<x>:LABel:COLor`` command.
        - ``.font``: The ``PLOT:PLOT<x>:LABel:FONT`` command tree.
        - ``.name``: The ``PLOT:PLOT<x>:LABel:NAMe`` command.
        - ``.xpos``: The ``PLOT:PLOT<x>:LABel:XPOS`` command.
        - ``.ypos``: The ``PLOT:PLOT<x>:LABel:YPOS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._color = PlotPlotItemLabelColor(device, f"{self._cmd_syntax}:COLor")
        self._font = PlotPlotItemLabelFont(device, f"{self._cmd_syntax}:FONT")
        self._name = PlotPlotItemLabelName(device, f"{self._cmd_syntax}:NAMe")
        self._xpos = PlotPlotItemLabelXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = PlotPlotItemLabelYpos(device, f"{self._cmd_syntax}:YPOS")

    @property
    def color(self) -> PlotPlotItemLabelColor:
        """Return the ``PLOT:PLOT<x>:LABel:COLor`` command.

        Description:
            - This command sets or queries the color of the specified trend label. This
              command/query only applies to Time Trend plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:COLor?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:COLor?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:COLor value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:LABel:COLor <QString>
            - PLOT:PLOT<x>:LABel:COLor?
            ```

        Info:
            - ``<QString>`` is the label color. The default color is specified by a quoted empty
              string, and is the only available color.
        """
        return self._color

    @property
    def font(self) -> PlotPlotItemLabelFont:
        """Return the ``PLOT:PLOT<x>:LABel:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:FONT?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bold``: The ``PLOT:PLOT<x>:LABel:FONT:BOLD`` command.
            - ``.italic``: The ``PLOT:PLOT<x>:LABel:FONT:ITALic`` command.
            - ``.size``: The ``PLOT:PLOT<x>:LABel:FONT:SIZE`` command.
            - ``.type``: The ``PLOT:PLOT<x>:LABel:FONT:TYPE`` command.
            - ``.underline``: The ``PLOT:PLOT<x>:LABel:FONT:UNDERline`` command.
        """
        return self._font

    @property
    def name(self) -> PlotPlotItemLabelName:
        """Return the ``PLOT:PLOT<x>:LABel:NAMe`` command.

        Description:
            - This command sets or queries the specified trend's label. This command/query only
              applies to Time Trend plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:NAMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:NAMe value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:LABel:NAMe <QString>
            - PLOT:PLOT<x>:LABel:NAMe?
            ```

        Info:
            - ``<QString>`` is the label.
        """
        return self._name

    @property
    def xpos(self) -> PlotPlotItemLabelXpos:
        """Return the ``PLOT:PLOT<x>:LABel:XPOS`` command.

        Description:
            - This command sets or queries the x-position of the specified trend label. This
              command/query only applies to Time Trend plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:XPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:XPOS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:XPOS value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:LABel:XPOS <NR3>
            - PLOT:PLOT<x>:LABel:XPOS?
            ```

        Info:
            - ``<NR3>`` is the y-position, in pixels relative to the left edge of the display, of
              the label.
        """
        return self._xpos

    @property
    def ypos(self) -> PlotPlotItemLabelYpos:
        """Return the ``PLOT:PLOT<x>:LABel:YPOS`` command.

        Description:
            - This command sets or queries the y-position of the specified trend label. This
              command/query only applies to Time Trend plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel:YPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel:YPOS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:LABel:YPOS value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:LABel:YPOS <NR3>
            - PLOT:PLOT<x>:LABel:YPOS?
            ```

        Info:
            - ``<NR3>`` is the x-position, in pixels relative to the baseline of the waveform, of
              the label.
        """
        return self._ypos


class PlotPlotItemImdaplotdisplay(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:IMDAPLOTDisplay`` command.

    Description:
        - This command sets or returns the IMDA time trend and acq trend plot display configuration.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:IMDAPLOTDisplay?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:IMDAPLOTDisplay?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:IMDAPLOTDisplay value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:IMDAPLOTDisplay {ALL|ONEPAIRVI|ONEPAIRV|ONEPAIRI|PHASEONE|PHASETWO|PHASETHREE|ABC|DQ0}
        - PLOT:PLOT<x>:IMDAPLOTDisplay?
        ```

    Info:
        - ``PLOT<x>`` is the plot number.
        - ``ALL`` sets the IMDA time trend and acq trend plot display configuration to ALL.
        - ``ONEPAIRVI`` sets the IMDA time trend and acq trend plot display configuration to
          ONEPAIRVI.
        - ``ONEPAIRV`` sets the IMDA time trend and acq trend plot display configuration to
          ONEPAIRV.
        - ``ONEPAIRI`` sets the IMDA time trend and acq trend plot display configuration to
          ONEPAIRI.
        - ``PHASEONE`` sets the IMDA time trend and acq trend plot display configuration to
          PHASEONE.
        - ``PHASETWO`` sets the IMDA time trend and acq trend plot display configuration to
          PHASETWO.
        - ``PHASETHREE`` sets the IMDA time trend and acq trend plot display configuration to
          PHASETHREE.
        - ``ABC`` sets the IMDA time trend plot display to ABC.
        - ``DQ0`` sets the IMDA time trend plot display to DQ0.
    """  # noqa: E501


class PlotPlotItemImdaMeas(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:IMDA:MEAS`` command.

    Description:
        - This command sets or returns the measurement selection of trend plot and acq trend plot.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:IMDA:MEAS?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:IMDA:MEAS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:IMDA:MEAS value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:IMDA:MEAS {VRMS|IRMS|PHASE|FREQuency|TRPWR|REPWR|APPPWR|TRPWRSUM|REPWRSUM|APPPWRSUM|DCPWR|INPWR|OUTPWR|EFFiciency|TOTALEFFiciency|INPWRSUM|OUTPWRSUM}
        - PLOT:PLOT<x>:IMDA:MEAS?
        ```

    Info:
        - ``PLOT<x>`` is the plot number.
        - ``VRMS`` sets the IMDA measurement selection to VRMS.
        - ``IRMS`` sets the IMDA measurement selection to IRMS.
        - ``PHASE`` sets the IMDA measurement selection to PHASE.
        - ``FREQuency`` sets the IMDA measurement selection to FREQuency.
        - ``TRPWR`` sets the IMDA measurement selection to TRPWR.
        - ``REPWR`` sets the IMDA measurement selection to REPWR.
        - ``APPPWR`` sets the IMDA measurement selection to APPPWR.
        - ``TRPWRSUM`` sets the IMDA measurement selection to TRPWRSUM.
        - ``REPWRSUM`` sets the IMDA measurement selection to REPWRSUM.
        - ``APPPWRSUM`` sets the IMDA measurement selection to APPPWRSUM.
        - ``DCPWR`` sets the IMDA measurement selection to DCPWR. This selection is applicable only
          for acq trend plots.
        - ``INPWR`` sets the IMDA measurement selection to INPWR. This selection is applicable only
          for acq trend plots.
        - ``OUTPWR`` sets the IMDA measurement selection to OUTPWR. This selection is applicable
          only for acq trend plots.
        - ``EFFiciency`` sets the IMDA measurement selection to EFFiciency.
        - ``TOTALEFFiciency`` sets the IMDA measurement selection to TOTALEFFiciency. This selection
          is applicable only for acq trend plots.
        - ``INPWRSUM`` sets the IMDA measurement selection to INPWRSUM. This selection is applicable
          only for acq trend plots.
        - ``OUTPWRSUM`` sets the IMDA measurement selection to OUTPWRSUM. This selection is
          applicable only for acq trend plots.
    """  # noqa: E501


class PlotPlotItemImda(SCPICmdRead):
    """The ``PLOT:PLOT<x>:IMDA`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:IMDA?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:IMDA?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``PLOT<x>`` is the plot number.

    Properties:
        - ``.meas``: The ``PLOT:PLOT<x>:IMDA:MEAS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._meas = PlotPlotItemImdaMeas(device, f"{self._cmd_syntax}:MEAS")

    @property
    def meas(self) -> PlotPlotItemImdaMeas:
        """Return the ``PLOT:PLOT<x>:IMDA:MEAS`` command.

        Description:
            - This command sets or returns the measurement selection of trend plot and acq trend
              plot.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:IMDA:MEAS?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:IMDA:MEAS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:IMDA:MEAS value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:IMDA:MEAS {VRMS|IRMS|PHASE|FREQuency|TRPWR|REPWR|APPPWR|TRPWRSUM|REPWRSUM|APPPWRSUM|DCPWR|INPWR|OUTPWR|EFFiciency|TOTALEFFiciency|INPWRSUM|OUTPWRSUM}
            - PLOT:PLOT<x>:IMDA:MEAS?
            ```

        Info:
            - ``PLOT<x>`` is the plot number.
            - ``VRMS`` sets the IMDA measurement selection to VRMS.
            - ``IRMS`` sets the IMDA measurement selection to IRMS.
            - ``PHASE`` sets the IMDA measurement selection to PHASE.
            - ``FREQuency`` sets the IMDA measurement selection to FREQuency.
            - ``TRPWR`` sets the IMDA measurement selection to TRPWR.
            - ``REPWR`` sets the IMDA measurement selection to REPWR.
            - ``APPPWR`` sets the IMDA measurement selection to APPPWR.
            - ``TRPWRSUM`` sets the IMDA measurement selection to TRPWRSUM.
            - ``REPWRSUM`` sets the IMDA measurement selection to REPWRSUM.
            - ``APPPWRSUM`` sets the IMDA measurement selection to APPPWRSUM.
            - ``DCPWR`` sets the IMDA measurement selection to DCPWR. This selection is applicable
              only for acq trend plots.
            - ``INPWR`` sets the IMDA measurement selection to INPWR. This selection is applicable
              only for acq trend plots.
            - ``OUTPWR`` sets the IMDA measurement selection to OUTPWR. This selection is applicable
              only for acq trend plots.
            - ``EFFiciency`` sets the IMDA measurement selection to EFFiciency.
            - ``TOTALEFFiciency`` sets the IMDA measurement selection to TOTALEFFiciency. This
              selection is applicable only for acq trend plots.
            - ``INPWRSUM`` sets the IMDA measurement selection to INPWRSUM. This selection is
              applicable only for acq trend plots.
            - ``OUTPWRSUM`` sets the IMDA measurement selection to OUTPWRSUM. This selection is
              applicable only for acq trend plots.
        """  # noqa: E501
        return self._meas


class PlotPlotItemEyerender(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:EYERender`` command.

    Description:
        - This command sets or queries the eye rendering method for the specified plot.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:EYERender?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:EYERender?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:EYERender value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:EYERender {FAst|COMPlete}
        - PLOT:PLOT<x>:EYERender?
        ```

    Info:
        - ``PLOT<x>`` is the plot number.
        - ``FAst`` sets the eye rendering method to fast.
        - ``COMPlete`` sets the eye rendering method to complete.
    """


class PlotPlotItemExtenduis(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:EXTENDuis`` command.

    Description:
        - This command sets or queries number of UIs surrounding the eye boundary UIs that are used
          for fast eye rendering.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:EXTENDuis?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:EXTENDuis?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:EXTENDuis value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:EXTENDuis <NR1>
        - PLOT:PLOT<x>:EXTENDuis?
        ```

    Info:
        - ``PLOT<x>`` is the plot number.
        - ``<NR1>`` is the number of surrounding UIs.
    """


class PlotPlotItemExportraw(SCPICmdRead):
    """The ``PLOT:PLOT<x>:EXPORTRaw`` command.

    Description:
        - This command returns a binary stream of double values containing the x,y and hits value.
          Use this command along with ``MEASUREMENT:ADDMEAS TIE``, ``PLOT:PLOT1:TYPE EYEDIAGRAM``,
          ``DISplay:SELect:VIEW`` plotview1 to export the eye diagram plot data.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:EXPORTRaw?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:EXPORTRaw?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:EXPORTRaw?
        ```
    """


class PlotPlotItemBittype(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:BITType`` command.

    Description:
        - This command sets or queries the bit type to display for the specified eye diagram plot.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:BITType?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:BITType?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:BITType value`` command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:BITType {ALLBits|TRANSition|NONTRANsition}
        - PLOT:PLOT<x>:BITType?
        ```

    Info:
        - ``PLOT<x>`` is the plot number.
        - ``ALLBits`` sets the eye diagram plot to show both transition and nontransition bits.
        - ``TRANSition`` sets the eye diagram plot to show only bits where a logic level transition
          occurs.
        - ``NONTRANsition`` sets the eye diagram plot to show only bits where no logic level
          transition occurs.
    """


class PlotPlotItemBathtubXaxisunits(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:BATHtub:XAXISUnits`` command.

    Description:
        - This command sets or queries the X-Axis unit, either unit intervals or seconds.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:BATHtub:XAXISUnits?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:BATHtub:XAXISUnits?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:BATHtub:XAXISUnits value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:BATHtub:XAXISUnits {UNITIntervals|SECOnds}
        - PLOT:PLOT<x>:BATHtub:XAXISUnits?
        ```

    Info:
        - ``UNITIntervals`` specifies units as unit intervals.
        - ``SECOnds`` specifies units as seconds.
    """


class PlotPlotItemBathtubBer(SCPICmdWrite, SCPICmdRead):
    """The ``PLOT:PLOT<x>:BATHtub:BER`` command.

    Description:
        - This command sets or queries the bathtub BER value.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:BATHtub:BER?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:BATHtub:BER?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:BATHtub:BER value``
          command.

    SCPI Syntax:
        ```
        - PLOT:PLOT<x>:BATHtub:BER <NR1>
        - PLOT:PLOT<x>:BATHtub:BER?
        ```

    Info:
        - ``<NR1>`` is the bathtub BER value.
    """


class PlotPlotItemBathtub(SCPICmdRead):
    """The ``PLOT:PLOT<x>:BATHtub`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:BATHtub?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:BATHtub?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ber``: The ``PLOT:PLOT<x>:BATHtub:BER`` command.
        - ``.xaxisunits``: The ``PLOT:PLOT<x>:BATHtub:XAXISUnits`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ber = PlotPlotItemBathtubBer(device, f"{self._cmd_syntax}:BER")
        self._xaxisunits = PlotPlotItemBathtubXaxisunits(device, f"{self._cmd_syntax}:XAXISUnits")

    @property
    def ber(self) -> PlotPlotItemBathtubBer:
        """Return the ``PLOT:PLOT<x>:BATHtub:BER`` command.

        Description:
            - This command sets or queries the bathtub BER value.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:BATHtub:BER?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:BATHtub:BER?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:BATHtub:BER value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:BATHtub:BER <NR1>
            - PLOT:PLOT<x>:BATHtub:BER?
            ```

        Info:
            - ``<NR1>`` is the bathtub BER value.
        """
        return self._ber

    @property
    def xaxisunits(self) -> PlotPlotItemBathtubXaxisunits:
        """Return the ``PLOT:PLOT<x>:BATHtub:XAXISUnits`` command.

        Description:
            - This command sets or queries the X-Axis unit, either unit intervals or seconds.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:BATHtub:XAXISUnits?``
              query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:BATHtub:XAXISUnits?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PLOT:PLOT<x>:BATHtub:XAXISUnits value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:BATHtub:XAXISUnits {UNITIntervals|SECOnds}
            - PLOT:PLOT<x>:BATHtub:XAXISUnits?
            ```

        Info:
            - ``UNITIntervals`` specifies units as unit intervals.
            - ``SECOnds`` specifies units as seconds.
        """
        return self._xaxisunits


#  pylint: disable=too-many-instance-attributes
class PlotPlotItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``PLOT:PLOT<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:PLOT<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bathtub``: The ``PLOT:PLOT<x>:BATHtub`` command tree.
        - ``.bittype``: The ``PLOT:PLOT<x>:BITType`` command.
        - ``.exportraw``: The ``PLOT:PLOT<x>:EXPORTRaw`` command.
        - ``.extenduis``: The ``PLOT:PLOT<x>:EXTENDuis`` command.
        - ``.eyerender``: The ``PLOT:PLOT<x>:EYERender`` command.
        - ``.imda``: The ``PLOT:PLOT<x>:IMDA`` command tree.
        - ``.imdaplotdisplay``: The ``PLOT:PLOT<x>:IMDAPLOTDisplay`` command.
        - ``.label``: The ``PLOT:PLOT<x>:LABel`` command tree.
        - ``.mask``: The ``PLOT:PLOT<x>:MASK`` command.
        - ``.maskoffset``: The ``PLOT:PLOT<x>:MASKOffset`` command tree.
        - ``.numbins``: The ``PLOT:PLOT<x>:NUMBins`` command.
        - ``.ptype``: The ``PLOT:PLOT<x>:PTYPe`` command.
        - ``.railnum``: The ``PLOT:PLOT<x>:RAILNUM`` command.
        - ``.source1``: The ``PLOT:PLOT<x>:SOUrce1`` command.
        - ``.spectrum``: The ``PLOT:PLOT<x>:SPECtrum`` command tree.
        - ``.type``: The ``PLOT:PLOT<x>:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bathtub = PlotPlotItemBathtub(device, f"{self._cmd_syntax}:BATHtub")
        self._bittype = PlotPlotItemBittype(device, f"{self._cmd_syntax}:BITType")
        self._exportraw = PlotPlotItemExportraw(device, f"{self._cmd_syntax}:EXPORTRaw")
        self._extenduis = PlotPlotItemExtenduis(device, f"{self._cmd_syntax}:EXTENDuis")
        self._eyerender = PlotPlotItemEyerender(device, f"{self._cmd_syntax}:EYERender")
        self._imda = PlotPlotItemImda(device, f"{self._cmd_syntax}:IMDA")
        self._imdaplotdisplay = PlotPlotItemImdaplotdisplay(
            device, f"{self._cmd_syntax}:IMDAPLOTDisplay"
        )
        self._label = PlotPlotItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._mask = PlotPlotItemMask(device, f"{self._cmd_syntax}:MASK")
        self._maskoffset = PlotPlotItemMaskoffset(device, f"{self._cmd_syntax}:MASKOffset")
        self._numbins = PlotPlotItemNumbins(device, f"{self._cmd_syntax}:NUMBins")
        self._ptype = PlotPlotItemPtype(device, f"{self._cmd_syntax}:PTYPe")
        self._railnum = PlotPlotItemRailnum(device, f"{self._cmd_syntax}:RAILNUM")
        self._source1 = PlotPlotItemSource1(device, f"{self._cmd_syntax}:SOUrce1")
        self._spectrum = PlotPlotItemSpectrum(device, f"{self._cmd_syntax}:SPECtrum")
        self._type = PlotPlotItemType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def bathtub(self) -> PlotPlotItemBathtub:
        """Return the ``PLOT:PLOT<x>:BATHtub`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:BATHtub?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:BATHtub?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ber``: The ``PLOT:PLOT<x>:BATHtub:BER`` command.
            - ``.xaxisunits``: The ``PLOT:PLOT<x>:BATHtub:XAXISUnits`` command.
        """
        return self._bathtub

    @property
    def bittype(self) -> PlotPlotItemBittype:
        """Return the ``PLOT:PLOT<x>:BITType`` command.

        Description:
            - This command sets or queries the bit type to display for the specified eye diagram
              plot.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:BITType?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:BITType?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:BITType value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:BITType {ALLBits|TRANSition|NONTRANsition}
            - PLOT:PLOT<x>:BITType?
            ```

        Info:
            - ``PLOT<x>`` is the plot number.
            - ``ALLBits`` sets the eye diagram plot to show both transition and nontransition bits.
            - ``TRANSition`` sets the eye diagram plot to show only bits where a logic level
              transition occurs.
            - ``NONTRANsition`` sets the eye diagram plot to show only bits where no logic level
              transition occurs.
        """
        return self._bittype

    @property
    def exportraw(self) -> PlotPlotItemExportraw:
        """Return the ``PLOT:PLOT<x>:EXPORTRaw`` command.

        Description:
            - This command returns a binary stream of double values containing the x,y and hits
              value. Use this command along with ``MEASUREMENT:ADDMEAS TIE``,
              ``PLOT:PLOT1:TYPE EYEDIAGRAM``, ``DISplay:SELect:VIEW`` plotview1 to export the eye
              diagram plot data.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:EXPORTRaw?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:EXPORTRaw?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:EXPORTRaw?
            ```
        """
        return self._exportraw

    @property
    def extenduis(self) -> PlotPlotItemExtenduis:
        """Return the ``PLOT:PLOT<x>:EXTENDuis`` command.

        Description:
            - This command sets or queries number of UIs surrounding the eye boundary UIs that are
              used for fast eye rendering.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:EXTENDuis?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:EXTENDuis?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:EXTENDuis value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:EXTENDuis <NR1>
            - PLOT:PLOT<x>:EXTENDuis?
            ```

        Info:
            - ``PLOT<x>`` is the plot number.
            - ``<NR1>`` is the number of surrounding UIs.
        """
        return self._extenduis

    @property
    def eyerender(self) -> PlotPlotItemEyerender:
        """Return the ``PLOT:PLOT<x>:EYERender`` command.

        Description:
            - This command sets or queries the eye rendering method for the specified plot.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:EYERender?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:EYERender?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:EYERender value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:EYERender {FAst|COMPlete}
            - PLOT:PLOT<x>:EYERender?
            ```

        Info:
            - ``PLOT<x>`` is the plot number.
            - ``FAst`` sets the eye rendering method to fast.
            - ``COMPlete`` sets the eye rendering method to complete.
        """
        return self._eyerender

    @property
    def imda(self) -> PlotPlotItemImda:
        """Return the ``PLOT:PLOT<x>:IMDA`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:IMDA?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:IMDA?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``PLOT<x>`` is the plot number.

        Sub-properties:
            - ``.meas``: The ``PLOT:PLOT<x>:IMDA:MEAS`` command.
        """
        return self._imda

    @property
    def imdaplotdisplay(self) -> PlotPlotItemImdaplotdisplay:
        """Return the ``PLOT:PLOT<x>:IMDAPLOTDisplay`` command.

        Description:
            - This command sets or returns the IMDA time trend and acq trend plot display
              configuration.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:IMDAPLOTDisplay?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:IMDAPLOTDisplay?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``PLOT:PLOT<x>:IMDAPLOTDisplay value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:IMDAPLOTDisplay {ALL|ONEPAIRVI|ONEPAIRV|ONEPAIRI|PHASEONE|PHASETWO|PHASETHREE|ABC|DQ0}
            - PLOT:PLOT<x>:IMDAPLOTDisplay?
            ```

        Info:
            - ``PLOT<x>`` is the plot number.
            - ``ALL`` sets the IMDA time trend and acq trend plot display configuration to ALL.
            - ``ONEPAIRVI`` sets the IMDA time trend and acq trend plot display configuration to
              ONEPAIRVI.
            - ``ONEPAIRV`` sets the IMDA time trend and acq trend plot display configuration to
              ONEPAIRV.
            - ``ONEPAIRI`` sets the IMDA time trend and acq trend plot display configuration to
              ONEPAIRI.
            - ``PHASEONE`` sets the IMDA time trend and acq trend plot display configuration to
              PHASEONE.
            - ``PHASETWO`` sets the IMDA time trend and acq trend plot display configuration to
              PHASETWO.
            - ``PHASETHREE`` sets the IMDA time trend and acq trend plot display configuration to
              PHASETHREE.
            - ``ABC`` sets the IMDA time trend plot display to ABC.
            - ``DQ0`` sets the IMDA time trend plot display to DQ0.
        """  # noqa: E501
        return self._imdaplotdisplay

    @property
    def label(self) -> PlotPlotItemLabel:
        """Return the ``PLOT:PLOT<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.color``: The ``PLOT:PLOT<x>:LABel:COLor`` command.
            - ``.font``: The ``PLOT:PLOT<x>:LABel:FONT`` command tree.
            - ``.name``: The ``PLOT:PLOT<x>:LABel:NAMe`` command.
            - ``.xpos``: The ``PLOT:PLOT<x>:LABel:XPOS`` command.
            - ``.ypos``: The ``PLOT:PLOT<x>:LABel:YPOS`` command.
        """
        return self._label

    @property
    def mask(self) -> PlotPlotItemMask:
        """Return the ``PLOT:PLOT<x>:MASK`` command.

        Description:
            - This command returns the name of the mask test associated with the specified eye
              diagram plot.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:MASK?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:MASK?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:MASK?
            ```

        Info:
            - ``PLOT<x>`` is the plot number.
        """
        return self._mask

    @property
    def maskoffset(self) -> PlotPlotItemMaskoffset:
        """Return the ``PLOT:PLOT<x>:MASKOffset`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:MASKOffset?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:MASKOffset?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``PLOT<x>`` is the plot number.

        Sub-properties:
            - ``.horizontal``: The ``PLOT:PLOT<x>:MASKOffset:HORizontal`` command tree.
            - ``.percentui``: The ``PLOT:PLOT<x>:MASKOffset:PERCENTui`` command tree.
        """
        return self._maskoffset

    @property
    def numbins(self) -> PlotPlotItemNumbins:
        """Return the ``PLOT:PLOT<x>:NUMBins`` command.

        Description:
            - This command sets or queries the current histogram resolution.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:NUMBins?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:NUMBins?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:NUMBins value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:NUMBins {TWENtyfive|FIFTY|HUNdred|TWOFifty|FIVEHundred|TWOThousand|MAXimum}
            - PLOT:PLOT<x>:NUMBins?
            ```

        Info:
            - ``TWENtyfive`` sets the number of bins to 25.
            - ``FIFTY`` sets the number of bins to 50.
            - ``HUNdred`` sets the number of bins to 100.
            - ``TWOFifty`` sets the number of bins to 250.
            - ``FIVEHundred`` sets the number of bins to 500.
            - ``TWOThousand`` sets the number of bins to 2000.
            - ``MAXimum`` sets the number of bins to the maximum value.
        """  # noqa: E501
        return self._numbins

    @property
    def ptype(self) -> PlotPlotItemPtype:
        """Return the ``PLOT:PLOT<x>:PTYPe`` command.

        Description:
            - This command sets or returns the phasor type of the phasor diagram plot.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:PTYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:PTYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:PTYPe value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:PTYPe {RMS|MAGNITUDE}
            - PLOT:PLOT<x>:PTYPe?
            ```

        Info:
            - ``PLOT<x>`` is the plot number.
            - ``RMS`` sets the phasor type to RMS.
            - ``MAGNITUDE`` sets the phasor type to MAGNITUDE.
        """
        return self._ptype

    @property
    def railnum(self) -> PlotPlotItemRailnum:
        """Return the ``PLOT:PLOT<x>:RAILNUM`` command.

        Description:
            - Sets the DPM histogram source.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:RAILNUM?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:RAILNUM?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:RAILNUM value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:RAILNUM RAIL<x>
            - PLOT:PLOT<x>:RAILNUM?
            ```

        Info:
            - ``PLOT<x>`` is the plot number.
            - ``Rail<x>`` is the rail number. x has a minimum of 1 and a maximum of 7.
        """
        return self._railnum

    @property
    def source1(self) -> PlotPlotItemSource1:
        """Return the ``PLOT:PLOT<x>:SOUrce1`` command.

        Description:
            - This command sets or queries the plot source.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:SOUrce1?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:SOUrce1 MEAS<x>
            - PLOT:PLOT<x>:SOUrce1?
            ```

        Info:
            - ``MEAS<x>`` is the specified measurement source for the specified plot.
        """
        return self._source1

    @property
    def spectrum(self) -> PlotPlotItemSpectrum:
        """Return the ``PLOT:PLOT<x>:SPECtrum`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>:SPECtrum?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>:SPECtrum?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.base``: The ``PLOT:PLOT<x>:SPECtrum:BASE`` command.
            - ``.dynrange``: The ``PLOT:PLOT<x>:SPECtrum:DYNRange`` command.
        """
        return self._spectrum

    @property
    def type(self) -> PlotPlotItemType:
        """Return the ``PLOT:PLOT<x>:TYPe`` command.

        Description:
            - This command sets or returns the current plot type of the specified plot.

        Usage:
            - Using the ``.write(value)`` method will send the ``PLOT:PLOT<x>:TYPe value`` command.

        SCPI Syntax:
            ```
            - PLOT:PLOT<x>:TYPe {NONE|BATHTUB|EYEDIAGRAM|HARMONICS|HISTOGRAM|IMDATIMETREND|IMDAACQTREND|INDUCTANCE|IVSINTEGRALV|MAGPROPERTY|PHASENOISE|PHASOR|SOA|SPECTRUM|SSCPROFILE|SWL|TIEHISTOGRAM|TIETIMETREND|TIESPECTRUM|TIMETREND|XY|XYZ}
            ```

        Info:
            - ``<x>`` is the plot number. This is the equivalent of the number shown on a plot
              heading in the UI.
            - ``NONE`` does not create a plot.
            - ``BATHTUB`` creates a bathtub plot.
            - ``EYEDIAGRAM`` creates an eye diagram. This plot type is not available on a 4 Series
              MSO instrument.
            - ``HARMONICS`` creates a harmonics bar graph.
            - ``HISTOGRAM`` creates a histogram plot.
            - ``IMDATIMETREND`` creates a IMDA time trend plot. This plot type requires option IMDA.
            - ``IMDAACQTREND`` creates a IMDA acq trend plot. This plot type requires option IMDA.
            - ``INDUCTANCE`` creates a inductance plot.
            - ``IVSINTEGRALV`` creates a I vs. ∫V plot.
            - ``PHASENOISE`` creates a phase noise plot.
            - ``PHASOR`` creates the Phasor Diagram. This plot type requires option 5-DPM on
              MSO58/56 series instruments.
            - ``MAGPROPERTY`` creates a BH curve.
            - ``SOA`` creates an SOA plot.
            - ``SPECTRUM`` creates a spectrum plot.
            - ``SSCPROFILE`` creates a SSC profile plot.
            - ``SWL`` creates a Switching Loss plot.
            - ``TIEHISTOGRAM`` creates a TIE histogram plot.
            - ``TIESPECTRUM`` creates a TIE spectrum plot.
            - ``TIETIMETREND`` creates a TIE time trend plot.
            - ``TIMETREND`` creates a time trend plot.
            - ``XY`` creates a XY plot.
            - ``XYZ`` creates a XYZ plot.
        """  # noqa: E501
        return self._type


class PlotList(SCPICmdRead):
    """The ``PLOT:LIST`` command.

    Description:
        - This command lists all currently defined plots.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - PLOT:LIST?
        ```
    """


class PlotDelete(SCPICmdWrite):
    """The ``PLOT:DELete`` command.

    Description:
        - This command deletes the specified plot.

    Usage:
        - Using the ``.write(value)`` method will send the ``PLOT:DELete value`` command.

    SCPI Syntax:
        ```
        - PLOT:DELete <QString>
        ```

    Info:
        - ``<QString>`` is the specified plot. Argument is of the form 'PLOT<NR1>, where <NR1> is ≥
          1).
    """

    _WRAP_ARG_WITH_QUOTES = True


class PlotAddnew(SCPICmdWrite):
    """The ``PLOT:ADDNew`` command.

    Description:
        - This command adds the specified plot.

    Usage:
        - Using the ``.write(value)`` method will send the ``PLOT:ADDNew value`` command.

    SCPI Syntax:
        ```
        - PLOT:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` is the specified plot. The argument is of the form 'PLOT<NR1>', where <NR1>
          ≥ 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Plot(SCPICmdRead):
    """The ``PLOT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``PLOT?`` query.
        - Using the ``.verify(value)`` method will send the ``PLOT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``PLOT:ADDNew`` command.
        - ``.delete``: The ``PLOT:DELete`` command.
        - ``.list``: The ``PLOT:LIST`` command.
        - ``.plot``: The ``PLOT:PLOT<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "PLOT") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = PlotAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = PlotDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = PlotList(device, f"{self._cmd_syntax}:LIST")
        self._plot: Dict[int, PlotPlotItem] = DefaultDictPassKeyToFactory(
            lambda x: PlotPlotItem(device, f"{self._cmd_syntax}:PLOT{x}")
        )

    @property
    def addnew(self) -> PlotAddnew:
        """Return the ``PLOT:ADDNew`` command.

        Description:
            - This command adds the specified plot.

        Usage:
            - Using the ``.write(value)`` method will send the ``PLOT:ADDNew value`` command.

        SCPI Syntax:
            ```
            - PLOT:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` is the specified plot. The argument is of the form 'PLOT<NR1>', where
              <NR1> ≥ 1.
        """
        return self._addnew

    @property
    def delete(self) -> PlotDelete:
        """Return the ``PLOT:DELete`` command.

        Description:
            - This command deletes the specified plot.

        Usage:
            - Using the ``.write(value)`` method will send the ``PLOT:DELete value`` command.

        SCPI Syntax:
            ```
            - PLOT:DELete <QString>
            ```

        Info:
            - ``<QString>`` is the specified plot. Argument is of the form 'PLOT<NR1>, where <NR1>
              is ≥ 1).
        """
        return self._delete

    @property
    def list(self) -> PlotList:
        """Return the ``PLOT:LIST`` command.

        Description:
            - This command lists all currently defined plots.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:LIST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - PLOT:LIST?
            ```
        """
        return self._list

    @property
    def plot(self) -> Dict[int, PlotPlotItem]:
        """Return the ``PLOT:PLOT<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``PLOT:PLOT<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``PLOT:PLOT<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bathtub``: The ``PLOT:PLOT<x>:BATHtub`` command tree.
            - ``.bittype``: The ``PLOT:PLOT<x>:BITType`` command.
            - ``.exportraw``: The ``PLOT:PLOT<x>:EXPORTRaw`` command.
            - ``.extenduis``: The ``PLOT:PLOT<x>:EXTENDuis`` command.
            - ``.eyerender``: The ``PLOT:PLOT<x>:EYERender`` command.
            - ``.imda``: The ``PLOT:PLOT<x>:IMDA`` command tree.
            - ``.imdaplotdisplay``: The ``PLOT:PLOT<x>:IMDAPLOTDisplay`` command.
            - ``.label``: The ``PLOT:PLOT<x>:LABel`` command tree.
            - ``.mask``: The ``PLOT:PLOT<x>:MASK`` command.
            - ``.maskoffset``: The ``PLOT:PLOT<x>:MASKOffset`` command tree.
            - ``.numbins``: The ``PLOT:PLOT<x>:NUMBins`` command.
            - ``.ptype``: The ``PLOT:PLOT<x>:PTYPe`` command.
            - ``.railnum``: The ``PLOT:PLOT<x>:RAILNUM`` command.
            - ``.source1``: The ``PLOT:PLOT<x>:SOUrce1`` command.
            - ``.spectrum``: The ``PLOT:PLOT<x>:SPECtrum`` command tree.
            - ``.type``: The ``PLOT:PLOT<x>:TYPe`` command.
        """
        return self._plot
