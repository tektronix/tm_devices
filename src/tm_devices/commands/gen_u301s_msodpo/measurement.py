# pylint: disable=line-too-long
"""The measurement commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MEASUrement:CLEARSNapshot
    - MEASUrement:GATing {OFF|SCREen|CURSor}
    - MEASUrement:GATing?
    - MEASUrement:IMMed:DELay:DIRection {BACKWards|FORWards}
    - MEASUrement:IMMed:DELay:DIRection?
    - MEASUrement:IMMed:DELay:EDGE<x> {FALL|RISe}
    - MEASUrement:IMMed:DELay:EDGE<x>?
    - MEASUrement:IMMed:DELay?
    - MEASUrement:IMMed:SOUrce1 {CH<x>|MATH<y>|REF<x>}
    - MEASUrement:IMMed:SOUrce1?
    - MEASUrement:IMMed:SOUrce2 {CH<x>|MATH<y>|REF<x>}
    - MEASUrement:IMMed:SOUrce2?
    - MEASUrement:IMMed:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|LOW|MAXimum|MEAN|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PEDGECount|PDUty|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS}
    - MEASUrement:IMMed:TYPe?
    - MEASUrement:IMMed:UNIts?
    - MEASUrement:IMMed:VALue?
    - MEASUrement:IMMed?
    - MEASUrement:INDICators:HORZ<x>?
    - MEASUrement:INDICators:NUMHORZ?
    - MEASUrement:INDICators:NUMVERT?
    - MEASUrement:INDICators:STATE {OFF|MEAS<x>}
    - MEASUrement:INDICators:STATE?
    - MEASUrement:INDICators:VERT<x>?
    - MEASUrement:INDICators?
    - MEASUrement:MEAS<x>:COUNt?
    - MEASUrement:MEAS<x>:DELay:DIRection {BACKWards|FORWards}
    - MEASUrement:MEAS<x>:DELay:DIRection?
    - MEASUrement:MEAS<x>:DELay:EDGE<x> {FALL|RISe}
    - MEASUrement:MEAS<x>:DELay:EDGE<x>?
    - MEASUrement:MEAS<x>:DELay?
    - MEASUrement:MEAS<x>:MAXimum?
    - MEASUrement:MEAS<x>:MEAN?
    - MEASUrement:MEAS<x>:MINImum?
    - MEASUrement:MEAS<x>:SOURCE2 {CH<x>|MATH<y>|REF<x>}
    - MEASUrement:MEAS<x>:SOURCE2?
    - MEASUrement:MEAS<x>:SOURCE[1] {CH<x>|MATH<y>|REF<x>}
    - MEASUrement:MEAS<x>:SOURCE[1]?
    - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|MATH|}
    - MEASUrement:MEAS<x>:SOUrce1?
    - MEASUrement:MEAS<x>:STATE {ON|OFF|<NR1>}
    - MEASUrement:MEAS<x>:STATE?
    - MEASUrement:MEAS<x>:STDdev?
    - MEASUrement:MEAS<x>:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|LOW|MAXimum|MEAN|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PDUty|PEDGECount|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS}
    - MEASUrement:MEAS<x>:TYPe?
    - MEASUrement:MEAS<x>:UNIts?
    - MEASUrement:MEAS<x>:VALue?
    - MEASUrement:MEAS<x>?
    - MEASUrement:METHod {Auto|HIStogram|MINMax}
    - MEASUrement:METHod?
    - MEASUrement:REFLevel:ABSolute:HIGH <NR3>
    - MEASUrement:REFLevel:ABSolute:HIGH?
    - MEASUrement:REFLevel:ABSolute:LOW <NR3>
    - MEASUrement:REFLevel:ABSolute:LOW?
    - MEASUrement:REFLevel:ABSolute:MID [1] <NR3>[1]?
    - MEASUrement:REFLevel:ABSolute:MID2 <NR3>
    - MEASUrement:REFLevel:ABSolute:MID2?
    - MEASUrement:REFLevel:ABSolute:MID<x> <NR3>
    - MEASUrement:REFLevel:ABSolute:MID<x>?
    - MEASUrement:REFLevel:ABSolute:MID?
    - MEASUrement:REFLevel:METHod {ABSolute|PERCent}
    - MEASUrement:REFLevel:METHod?
    - MEASUrement:REFLevel:PERCent:HIGH <NR3>
    - MEASUrement:REFLevel:PERCent:HIGH?
    - MEASUrement:REFLevel:PERCent:LOW <NR3>
    - MEASUrement:REFLevel:PERCent:LOW?
    - MEASUrement:REFLevel:PERCent:MID [1] <NR3>[1]?
    - MEASUrement:REFLevel:PERCent:MID2 <NR3>
    - MEASUrement:REFLevel:PERCent:MID2?
    - MEASUrement:REFLevel:PERCent:MID<x> <NR3>
    - MEASUrement:REFLevel:PERCent:MID<x>?
    - MEASUrement:REFLevel:PERCent:MID?
    - MEASUrement:REFLevel?
    - MEASUrement:SNAPShot
    - MEASUrement:STATIstics RESET
    - MEASUrement:STATIstics:MODE {OFF|ON}
    - MEASUrement:STATIstics:MODE?
    - MEASUrement:STATIstics:WEIghting <NR1>
    - MEASUrement:STATIstics:WEIghting?
    - MEASUrement:STATIstics?
    - MEASUrement?
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


class MeasurementStatisticsWeighting(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:STATIstics:WEIghting`` command.

    Description:
        - This command specifies the time constant for mean and standard deviation statistical
          accumulations.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:STATIstics:WEIghting?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics:WEIghting?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:STATIstics:WEIghting value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:STATIstics:WEIghting <NR1>
        - MEASUrement:STATIstics:WEIghting?
        ```

    Info:
        - ``<NR1>`` is the number of samples used for the mean and standard deviation statistical
          accumulations.
    """


class MeasurementStatisticsMode(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:STATIstics:MODE`` command.

    Description:
        - Controls the operation and display of management statistics.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:STATIstics:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics:MODE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:STATIstics:MODE value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:STATIstics:MODE {OFF|ON}
        - MEASUrement:STATIstics:MODE?
        ```

    Info:
        - ``OFF`` turns all measurements off. This is the default value.
        - ``ON`` turns on statistics and displays all statistics for each measurement.
    """


class MeasurementStatistics(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:STATIstics`` command.

    Description:
        - Clears all of the statistics accumulated for all periodic measurements (MEAS1 through
          MEAS4). The query form returns statistic settings.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:STATIstics?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:STATIstics value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:STATIstics RESET
        - MEASUrement:STATIstics?
        ```

    Info:
        - ``RESET`` clears the measurements.

    Properties:
        - ``.mode``: The ``MEASUrement:STATIstics:MODE`` command.
        - ``.weighting``: The ``MEASUrement:STATIstics:WEIghting`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = MeasurementStatisticsMode(device, f"{self._cmd_syntax}:MODE")
        self._weighting = MeasurementStatisticsWeighting(device, f"{self._cmd_syntax}:WEIghting")

    @property
    def mode(self) -> MeasurementStatisticsMode:
        """Return the ``MEASUrement:STATIstics:MODE`` command.

        Description:
            - Controls the operation and display of management statistics.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:STATIstics:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics:MODE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:STATIstics:MODE value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:STATIstics:MODE {OFF|ON}
            - MEASUrement:STATIstics:MODE?
            ```

        Info:
            - ``OFF`` turns all measurements off. This is the default value.
            - ``ON`` turns on statistics and displays all statistics for each measurement.
        """
        return self._mode

    @property
    def weighting(self) -> MeasurementStatisticsWeighting:
        """Return the ``MEASUrement:STATIstics:WEIghting`` command.

        Description:
            - This command specifies the time constant for mean and standard deviation statistical
              accumulations.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:STATIstics:WEIghting?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:STATIstics:WEIghting?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:STATIstics:WEIghting value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:STATIstics:WEIghting <NR1>
            - MEASUrement:STATIstics:WEIghting?
            ```

        Info:
            - ``<NR1>`` is the number of samples used for the mean and standard deviation
              statistical accumulations.
        """
        return self._weighting


class MeasurementSnapshot(SCPICmdWriteNoArguments):
    """The ``MEASUrement:SNAPShot`` command.

    Description:
        - Displays the measurement snapshot list on the oscilloscope screen. The list contains the
          immediate values for all available measurements of the active signal. You can query each
          individual measurement separately.

    Usage:
        - Using the ``.write()`` method will send the ``MEASUrement:SNAPShot`` command.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot
        ```
    """


class MeasurementReflevelPercentMidItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevel:PERCent:MID<x>`` command.

    Description:
        - This command specifies the percent (where 100% is equal to HIGH) that is used to calculate
          a mid reference level. There are two mid reference levels; thus, MID<x> can be either MID1
          or MID2. This command applies when the command ``MEASUREMENT:REFLEVEL:METHOD`` has been
          set to Percent. This command is equivalent to setting the Reference Levels in the MEASURE
          menu on the oscilloscope front panel.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent:MID<x>?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:PERCent:MID<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevel:PERCent:MID<x> value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel:PERCent:MID<x> <NR3>
        - MEASUrement:REFLevel:PERCent:MID<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the mid reference level, ranging from
          0 to 100%. The default mid reference level is 50%.
    """


class MeasurementReflevelPercentMid2(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevel:PERCent:MID2`` command.

    Description:
        - Sets or returns the percent (where 100% is equal to HIGH) that is used to calculate the
          mid reference level for the second waveform specified when ``MEASUREMENT:REFLEVEL:METHOD``
          is set to Percent. This command affects the results of delay measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent:MID2?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:PERCent:MID2?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevel:PERCent:MID2 value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel:PERCent:MID2 <NR3>
        - MEASUrement:REFLevel:PERCent:MID2?
        ```

    Info:
        - ``<NR3>`` is the mid reference level, ranging from 0 to 100%. The default mid reference
          level is 50%.
    """


class MeasurementReflevelPercentMid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevel:PERCent:MID`` command.

    Description:
        - [1] Sets or returns the percent (where 100% is equal to HIGH) that is used to calculate
          the mid reference level when ``MEASUrement:REFLevel:METHod`` is set to Percent. This
          command affects the results of period, frequency, delay, and all cyclic measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent:MID?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:PERCent:MID?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevel:PERCent:MID value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel:PERCent:MID [1] <NR3>[1]?
        - MEASUrement:REFLevel:PERCent:MID?
        ```

    Info:
        - ``<NR3>`` is the mid reference level, ranging from 0 to 100%. The default mid reference
          level is 50%.
    """


class MeasurementReflevelPercentLow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevel:PERCent:LOW`` command.

    Description:
        - This command specifies the percent (where 100% is equal to HIGH) used to calculate the low
          reference level when ``MEASUREMENT:REFLEVEL:METHOD`` is set to Percent. This command
          affects the results of rise and fall measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent:LOW?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:PERCent:LOW?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevel:PERCent:LOW value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel:PERCent:LOW <NR3>
        - MEASUrement:REFLevel:PERCent:LOW?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the low reference level, ranging from
          0 to 100%. The default low reference level is 10%.
    """


class MeasurementReflevelPercentHigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevel:PERCent:HIGH`` command.

    Description:
        - This command specifies the percent (where 100% is equal to HIGH) used to calculate the
          high reference level when ``MEASUREMENT:REFLEVEL:METHOD`` is set to Percent. This command
          affects the results of rise and fall measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:PERCent:HIGH?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevel:PERCent:HIGH value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel:PERCent:HIGH <NR3>
        - MEASUrement:REFLevel:PERCent:HIGH?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the high reference level, ranging from
          0 to 100%. The default high reference level is 90%.
    """


class MeasurementReflevelPercent(SCPICmdRead):
    """The ``MEASUrement:REFLevel:PERCent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:PERCent?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.high``: The ``MEASUrement:REFLevel:PERCent:HIGH`` command.
        - ``.low``: The ``MEASUrement:REFLevel:PERCent:LOW`` command.
        - ``.mid``: The ``MEASUrement:REFLevel:PERCent:MID`` command.
        - ``.mid2``: The ``MEASUrement:REFLevel:PERCent:MID2`` command.
        - ``.midx``: The ``MEASUrement:REFLevel:PERCent:MID<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = MeasurementReflevelPercentHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = MeasurementReflevelPercentLow(device, f"{self._cmd_syntax}:LOW")
        self._mid = MeasurementReflevelPercentMid(device, f"{self._cmd_syntax}:MID")
        self._mid2 = MeasurementReflevelPercentMid2(device, f"{self._cmd_syntax}:MID2")
        self._midx: Dict[int, MeasurementReflevelPercentMidItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementReflevelPercentMidItem(device, f"{self._cmd_syntax}:MID{x}")
        )

    @property
    def high(self) -> MeasurementReflevelPercentHigh:
        """Return the ``MEASUrement:REFLevel:PERCent:HIGH`` command.

        Description:
            - This command specifies the percent (where 100% is equal to HIGH) used to calculate the
              high reference level when ``MEASUREMENT:REFLEVEL:METHOD`` is set to Percent. This
              command affects the results of rise and fall measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent:HIGH?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevel:PERCent:HIGH?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevel:PERCent:HIGH value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel:PERCent:HIGH <NR3>
            - MEASUrement:REFLevel:PERCent:HIGH?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the high reference level, ranging
              from 0 to 100%. The default high reference level is 90%.
        """
        return self._high

    @property
    def low(self) -> MeasurementReflevelPercentLow:
        """Return the ``MEASUrement:REFLevel:PERCent:LOW`` command.

        Description:
            - This command specifies the percent (where 100% is equal to HIGH) used to calculate the
              low reference level when ``MEASUREMENT:REFLEVEL:METHOD`` is set to Percent. This
              command affects the results of rise and fall measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent:LOW?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevel:PERCent:LOW?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevel:PERCent:LOW value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel:PERCent:LOW <NR3>
            - MEASUrement:REFLevel:PERCent:LOW?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the low reference level, ranging
              from 0 to 100%. The default low reference level is 10%.
        """
        return self._low

    @property
    def mid(self) -> MeasurementReflevelPercentMid:
        """Return the ``MEASUrement:REFLevel:PERCent:MID`` command.

        Description:
            - [1] Sets or returns the percent (where 100% is equal to HIGH) that is used to
              calculate the mid reference level when ``MEASUrement:REFLevel:METHod`` is set to
              Percent. This command affects the results of period, frequency, delay, and all cyclic
              measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent:MID?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevel:PERCent:MID?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevel:PERCent:MID value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel:PERCent:MID [1] <NR3>[1]?
            - MEASUrement:REFLevel:PERCent:MID?
            ```

        Info:
            - ``<NR3>`` is the mid reference level, ranging from 0 to 100%. The default mid
              reference level is 50%.
        """
        return self._mid

    @property
    def mid2(self) -> MeasurementReflevelPercentMid2:
        """Return the ``MEASUrement:REFLevel:PERCent:MID2`` command.

        Description:
            - Sets or returns the percent (where 100% is equal to HIGH) that is used to calculate
              the mid reference level for the second waveform specified when
              ``MEASUREMENT:REFLEVEL:METHOD`` is set to Percent. This command affects the results of
              delay measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent:MID2?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevel:PERCent:MID2?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevel:PERCent:MID2 value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel:PERCent:MID2 <NR3>
            - MEASUrement:REFLevel:PERCent:MID2?
            ```

        Info:
            - ``<NR3>`` is the mid reference level, ranging from 0 to 100%. The default mid
              reference level is 50%.
        """
        return self._mid2

    @property
    def midx(self) -> Dict[int, MeasurementReflevelPercentMidItem]:
        """Return the ``MEASUrement:REFLevel:PERCent:MID<x>`` command.

        Description:
            - This command specifies the percent (where 100% is equal to HIGH) that is used to
              calculate a mid reference level. There are two mid reference levels; thus, MID<x> can
              be either MID1 or MID2. This command applies when the command
              ``MEASUREMENT:REFLEVEL:METHOD`` has been set to Percent. This command is equivalent to
              setting the Reference Levels in the MEASURE menu on the oscilloscope front panel.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent:MID<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevel:PERCent:MID<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevel:PERCent:MID<x> value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel:PERCent:MID<x> <NR3>
            - MEASUrement:REFLevel:PERCent:MID<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the mid reference level, ranging
              from 0 to 100%. The default mid reference level is 50%.
        """
        return self._midx


class MeasurementReflevelMethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevel:METHod`` command.

    Description:
        - Specifies or returns the reference level units used for measurement calculations.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:METHod?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:METHod?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:REFLevel:METHod value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel:METHod {ABSolute|PERCent}
        - MEASUrement:REFLevel:METHod?
        ```

    Info:
        - ``ABSolute`` specifies that the reference levels are set explicitly using the
          ``MEASUrement:REFLevel:ABSolute`` commands. This method is useful when precise values are
          required (for example, when designing to published interface specifications, such as
          RS-232-C).
        - ``PERCent`` specifies that the reference levels are calculated as a percent relative to
          HIGH and LOW. The percentages are defined using the ``MEASUrement:REFLevel:PERCent``
          commands.
    """


class MeasurementReflevelAbsoluteMidItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevel:ABSolute:MID<x>`` command.

    Description:
        - This command specifies an absolute mid reference level (the 50% reference level) for the
          'to' waveform when taking a delay measurement, in volts. There are two absolute mid
          reference levels; thus MID<x> can either be MID1 or MID2. This command applies when
          ``MEASUREMENT:REFLEVEL:METHOD`` has been set to Absolute. This command is equivalent to
          setting the Reference Levels in the MEASURE menu on the oscilloscope front panel.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute:MID<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:REFLevel:ABSolute:MID<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevel:ABSolute:MID<x> value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel:ABSolute:MID<x> <NR3>
        - MEASUrement:REFLevel:ABSolute:MID<x>?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the mid reference level in volts.
    """


class MeasurementReflevelAbsoluteMid2(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevel:ABSolute:MID2`` command.

    Description:
        - Sets or returns the mid reference level for the 'to' waveform when taking a delay
          measurement, and is the 50% reference level when ``MEASUREMENT:REFLEVEL:METHOD`` is set to
          Absolute. This command affects the results of delay measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute:MID2?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:ABSolute:MID2?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevel:ABSolute:MID2 value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel:ABSolute:MID2 <NR3>
        - MEASUrement:REFLevel:ABSolute:MID2?
        ```

    Info:
        - ``<NR3>`` is the mid reference level, in volts. The default is 0.0 V.
    """


class MeasurementReflevelAbsoluteMid(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevel:ABSolute:MID`` command.

    Description:
        - [1] Sets or returns the mid reference level, and is the 50% reference level when
          ``MEASUREMENT:REFLEVEL:METHOD`` is set to Absolute. This command affects the results of
          period, frequency, delay, and all cyclic measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute:MID?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:ABSolute:MID?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevel:ABSolute:MID value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel:ABSolute:MID [1] <NR3>[1]?
        - MEASUrement:REFLevel:ABSolute:MID?
        ```

    Info:
        - ``<NR3>`` is the mid reference level, in volts. The default is 0.0 V.
    """


class MeasurementReflevelAbsoluteLow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevel:ABSolute:LOW`` command.

    Description:
        - This command specifies the low reference level, and is the lower reference level when
          ``MEASUREMENT:REFLEVEL:METHOD`` is set to Absolute.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute:LOW?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:ABSolute:LOW?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevel:ABSolute:LOW value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel:ABSolute:LOW <NR3>
        - MEASUrement:REFLevel:ABSolute:LOW?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the low reference level, in volts. The
          default is 0.0 V.
    """


class MeasurementReflevelAbsoluteHigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:REFLevel:ABSolute:HIGH`` command.

    Description:
        - This command specifies the high reference level, and is the upper reference level when
          ``MEASUREMENT:REFLEVEL:METHOD`` is set to Absolute. This command affects the results of
          rise and fall measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:ABSolute:HIGH?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:REFLevel:ABSolute:HIGH value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel:ABSolute:HIGH <NR3>
        - MEASUrement:REFLevel:ABSolute:HIGH?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the high reference level, in volts.
          The default is 0.0 V.
    """


class MeasurementReflevelAbsolute(SCPICmdRead):
    """The ``MEASUrement:REFLevel:ABSolute`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:ABSolute?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.high``: The ``MEASUrement:REFLevel:ABSolute:HIGH`` command.
        - ``.low``: The ``MEASUrement:REFLevel:ABSolute:LOW`` command.
        - ``.mid``: The ``MEASUrement:REFLevel:ABSolute:MID`` command.
        - ``.mid2``: The ``MEASUrement:REFLevel:ABSolute:MID2`` command.
        - ``.midx``: The ``MEASUrement:REFLevel:ABSolute:MID<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = MeasurementReflevelAbsoluteHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = MeasurementReflevelAbsoluteLow(device, f"{self._cmd_syntax}:LOW")
        self._mid = MeasurementReflevelAbsoluteMid(device, f"{self._cmd_syntax}:MID")
        self._mid2 = MeasurementReflevelAbsoluteMid2(device, f"{self._cmd_syntax}:MID2")
        self._midx: Dict[int, MeasurementReflevelAbsoluteMidItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementReflevelAbsoluteMidItem(device, f"{self._cmd_syntax}:MID{x}")
        )

    @property
    def high(self) -> MeasurementReflevelAbsoluteHigh:
        """Return the ``MEASUrement:REFLevel:ABSolute:HIGH`` command.

        Description:
            - This command specifies the high reference level, and is the upper reference level when
              ``MEASUREMENT:REFLEVEL:METHOD`` is set to Absolute. This command affects the results
              of rise and fall measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute:HIGH?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevel:ABSolute:HIGH?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevel:ABSolute:HIGH value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel:ABSolute:HIGH <NR3>
            - MEASUrement:REFLevel:ABSolute:HIGH?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the high reference level, in
              volts. The default is 0.0 V.
        """
        return self._high

    @property
    def low(self) -> MeasurementReflevelAbsoluteLow:
        """Return the ``MEASUrement:REFLevel:ABSolute:LOW`` command.

        Description:
            - This command specifies the low reference level, and is the lower reference level when
              ``MEASUREMENT:REFLEVEL:METHOD`` is set to Absolute.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute:LOW?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevel:ABSolute:LOW?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevel:ABSolute:LOW value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel:ABSolute:LOW <NR3>
            - MEASUrement:REFLevel:ABSolute:LOW?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the low reference level, in volts.
              The default is 0.0 V.
        """
        return self._low

    @property
    def mid(self) -> MeasurementReflevelAbsoluteMid:
        """Return the ``MEASUrement:REFLevel:ABSolute:MID`` command.

        Description:
            - [1] Sets or returns the mid reference level, and is the 50% reference level when
              ``MEASUREMENT:REFLEVEL:METHOD`` is set to Absolute. This command affects the results
              of period, frequency, delay, and all cyclic measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute:MID?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevel:ABSolute:MID?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevel:ABSolute:MID value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel:ABSolute:MID [1] <NR3>[1]?
            - MEASUrement:REFLevel:ABSolute:MID?
            ```

        Info:
            - ``<NR3>`` is the mid reference level, in volts. The default is 0.0 V.
        """
        return self._mid

    @property
    def mid2(self) -> MeasurementReflevelAbsoluteMid2:
        """Return the ``MEASUrement:REFLevel:ABSolute:MID2`` command.

        Description:
            - Sets or returns the mid reference level for the 'to' waveform when taking a delay
              measurement, and is the 50% reference level when ``MEASUREMENT:REFLEVEL:METHOD`` is
              set to Absolute. This command affects the results of delay measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute:MID2?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevel:ABSolute:MID2?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevel:ABSolute:MID2 value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel:ABSolute:MID2 <NR3>
            - MEASUrement:REFLevel:ABSolute:MID2?
            ```

        Info:
            - ``<NR3>`` is the mid reference level, in volts. The default is 0.0 V.
        """
        return self._mid2

    @property
    def midx(self) -> Dict[int, MeasurementReflevelAbsoluteMidItem]:
        """Return the ``MEASUrement:REFLevel:ABSolute:MID<x>`` command.

        Description:
            - This command specifies an absolute mid reference level (the 50% reference level) for
              the 'to' waveform when taking a delay measurement, in volts. There are two absolute
              mid reference levels; thus MID<x> can either be MID1 or MID2. This command applies
              when ``MEASUREMENT:REFLEVEL:METHOD`` has been set to Absolute. This command is
              equivalent to setting the Reference Levels in the MEASURE menu on the oscilloscope
              front panel.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute:MID<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:REFLevel:ABSolute:MID<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:REFLevel:ABSolute:MID<x> value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel:ABSolute:MID<x> <NR3>
            - MEASUrement:REFLevel:ABSolute:MID<x>?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the mid reference level in volts.
        """
        return self._midx


class MeasurementReflevel(SCPICmdRead):
    """The ``MEASUrement:REFLevel`` command.

    Description:
        - Returns the current reference level parameters.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:REFLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:REFLevel?
        ```

    Properties:
        - ``.absolute``: The ``MEASUrement:REFLevel:ABSolute`` command tree.
        - ``.method``: The ``MEASUrement:REFLevel:METHod`` command.
        - ``.percent``: The ``MEASUrement:REFLevel:PERCent`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = MeasurementReflevelAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._method = MeasurementReflevelMethod(device, f"{self._cmd_syntax}:METHod")
        self._percent = MeasurementReflevelPercent(device, f"{self._cmd_syntax}:PERCent")

    @property
    def absolute(self) -> MeasurementReflevelAbsolute:
        """Return the ``MEASUrement:REFLevel:ABSolute`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:ABSolute?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:ABSolute?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``MEASUrement:REFLevel:ABSolute:HIGH`` command.
            - ``.low``: The ``MEASUrement:REFLevel:ABSolute:LOW`` command.
            - ``.mid``: The ``MEASUrement:REFLevel:ABSolute:MID`` command.
            - ``.mid2``: The ``MEASUrement:REFLevel:ABSolute:MID2`` command.
            - ``.midx``: The ``MEASUrement:REFLevel:ABSolute:MID<x>`` command.
        """
        return self._absolute

    @property
    def method(self) -> MeasurementReflevelMethod:
        """Return the ``MEASUrement:REFLevel:METHod`` command.

        Description:
            - Specifies or returns the reference level units used for measurement calculations.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:METHod?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:METHod?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:REFLevel:METHod value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel:METHod {ABSolute|PERCent}
            - MEASUrement:REFLevel:METHod?
            ```

        Info:
            - ``ABSolute`` specifies that the reference levels are set explicitly using the
              ``MEASUrement:REFLevel:ABSolute`` commands. This method is useful when precise values
              are required (for example, when designing to published interface specifications, such
              as RS-232-C).
            - ``PERCent`` specifies that the reference levels are calculated as a percent relative
              to HIGH and LOW. The percentages are defined using the
              ``MEASUrement:REFLevel:PERCent`` commands.
        """
        return self._method

    @property
    def percent(self) -> MeasurementReflevelPercent:
        """Return the ``MEASUrement:REFLevel:PERCent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel:PERCent?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel:PERCent?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``MEASUrement:REFLevel:PERCent:HIGH`` command.
            - ``.low``: The ``MEASUrement:REFLevel:PERCent:LOW`` command.
            - ``.mid``: The ``MEASUrement:REFLevel:PERCent:MID`` command.
            - ``.mid2``: The ``MEASUrement:REFLevel:PERCent:MID2`` command.
            - ``.midx``: The ``MEASUrement:REFLevel:PERCent:MID<x>`` command.
        """
        return self._percent


class MeasurementMethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:METHod`` command.

    Description:
        - This command specifies the method used to calculate the 0% and 100% reference level.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:METHod?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:METHod?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:METHod value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:METHod {Auto|HIStogram|MINMax}
        - MEASUrement:METHod?
        ```

    Info:
        - ``Auto`` selects the best method for each data set.
        - ``HIStogram`` sets the high and low waveform levels statistically using a histogram
          algorithm.
        - ``MINMax`` uses the highest and lowest values of the waveform record. This selection is
          best for examining waveforms with no large, flat portions of a common value, such as sine
          waves and triangle waves.
    """


class MeasurementMeasItemValue(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:VALue`` command.

    Description:
        - Returns a calculate value for the measurement specified by <x>, which ranges from 1
          through 4.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:VALue?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:VALue?
        ```
    """


class MeasurementMeasItemUnits(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:UNIts`` command.

    Description:
        - Returns the units associated with the specified measurement. The measurement slots are
          specified by <x>, which ranges from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:UNIts?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:UNIts?
        ```
    """


class MeasurementMeasItemType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:TYPe`` command.

    Description:
        - Sets or returns the measurement type defined for the specified measurement slot. The
          measurement slot is specified by <x>, which ranges from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|LOW|MAXimum|MEAN|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PDUty|PEDGECount|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS}
        - MEASUrement:MEAS<x>:TYPe?
        ```

    Info:
        - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it measures
          the high value less the low value measured over the entire waveform or gated region. This
          measurement is available only on DPO models.
        - ``Amplitude = High - Low``
        - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
          region and is measured in volt-seconds. The area measured above the ground is positive,
          while the area below ground is negative. This measurement is available only on DPO models.
        - ``BURst`` measures the duration of a burst. The measurement is made over the entire
          waveform or gated region.
        - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures, in
          volt-seconds, the area over the first cycle in the waveform or the first cycle in the
          gated region. The area measured above the common reference point is positive, while the
          area below the common reference point is negative. This measurement is available only on
          DPO models.
        - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the waveform
          or the first cycle in the gated region. This measurement is available only on DPO models.
        - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle in
          the waveform or the first cycle in the gated region. This measurement is available only on
          DPO models.
        - ``DELay`` measures the time between the middle reference (default = 50%) amplitude point
          of the source waveform and the destination waveform. This measurement is available only on
          DPO models.
        - ``FALL`` measures the time taken for the falling edge of the first pulse in the waveform
          or gated region to fall from a high reference value (default is 90%) to a low reference
          value (default is 10%). This measurement is available only on DPO models.
        - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is the
          reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per second.
        - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a waveform.
          This measurement is available only on DPO models.
        - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a waveform.
          This measurement is available only on DPO models.
        - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
          found. It is measured over the entire waveform or gated region. This measurement is
          available only on DPO models.
        - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or gated
          region. This measurement is available only on DPO models.
        - ``MINImum`` finds the minimum amplitude. This value is typically the most negative peak
          voltage. It is measured over the entire waveform or gated region. This measurement is
          available only on DPO models.
        - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
          period, expressed as a percentage. The duty cycle is measured on the first cycle in the
          waveform or gated region.
        - ``Negative Duty Cycle = ((Negative Width) / Period) × 100%``
        - ``NEDGECount`` is the count of negative edges.
        - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
          waveform or gated region. This measurement is available only on DPO models.
        - ``Negative Overshoot = ((Low - Minimum) / Amplitude) × 100%)``
        - ``NPULSECount`` is the count of negative pulses.
        - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
          reference (default = 50%) amplitude points of a negative pulse. The measurement is made on
          the first pulse in the waveform or gated region.
        - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
          period, expressed as a percentage. It is measured on the first cycle in the waveform or
          gated region.
        - ``Positive Duty Cycle = ((Positive Width) / Period) × 100%``
        - ``PEDGECount`` is the count of positive edges.
        - ``PERIod`` is the time required to complete the first cycle in a waveform or gated region.
          Period is the reciprocal of frequency and is measured in seconds.
        - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
          reference waveform) between two waveforms. The measurement is made between the middle
          reference points of the two waveforms and is expressed in degrees, where 360° represents
          one waveform cycle.
        - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
          amplitude in the entire waveform or gated region. This measurement is available only on
          DPO models.
        - ``POVershoot`` is the positive overshoot value over the entire waveform or gated region.
          This measurement is available only on DPO models.
        - ``Positive Overshoot = ((Maximum - High) / Amplitude) ×100%``
        - ``PPULSECount`` is the count of positive pulses.
        - ``PWIdth`` (positive width) is the distance (time) between the middle reference (default =
          50%) amplitude points of a positive pulse. The measurement is made on the first pulse in
          the waveform or gated region.
        - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the time
          it takes for the leading edge of the first pulse encountered to rise from a low reference
          value (default is 10%) to a high reference value (default is 90%). This measurement is
          available only on DPO models.
        - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
          waveform or gated region. This measurement is available only on DPO models.
    """  # noqa: E501


class MeasurementMeasItemStddev(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:STDdev`` command.

    Description:
        - Returns the standard deviation of values accumulated for this measurement since the last
          statistical reset. Measurements are specified by <x>, the measurement slots, from 1
          through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:STDdev?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:STDdev?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:STDdev?
        ```
    """


class MeasurementMeasItemState(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:STATE`` command.

    Description:
        - This command specifies whether the specified measurement slot is computed and displayed.
          The measurement slot is specified by <x>, which ranges from 1 through 8. For a measurement
          to display, you must have selected a source waveform and defined the measurement you want
          to take and display. You select the measurement using the ``MEASUREMENT:MEASX:SOURCEX``
          command. You define the measurement type using the ``MEASUREMENT:MEASX:TYPE`` command.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:STATE value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:STATE {ON|OFF|<NR1>}
        - MEASUrement:MEAS<x>:STATE?
        ```

    Info:
        - ``OFF`` disables calculation and display of the specified measurement slot.
        - ``ON`` enables calculation and display of the specified measurement slot.
        - ``<NR1>`` = 0 disables calculation and display of the specified measurement slot; any
          other value enables calculation and display of the specified measurement slot.
    """


class MeasurementMeasItemSource1(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:SOUrce1`` command.

    Description:
        - For SOURce1: Sets or returns the source for all single channel measurements. For delay or
          phase measurements, sets or returns the waveform to measure 'from'. For SOUrce2: Sets or
          returns the waveform to measure 'to' when taking a delay measurement or phase measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1 value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|MATH|}
        - MEASUrement:MEAS<x>:SOUrce1?
        ```

    Info:
        - ``CH<x>`` is an input channel waveform, where x is the channel number.
        - ``MATH`` is the math waveform.
        - ``REF<x>`` is a reference waveform, where x is the reference channel number.
    """


class MeasurementMeasItemSourceItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:SOURCE[1]`` command.

    Description:
        - Sets or returns the source for all single source measurements and specifies the source to
          measure 'from' when taking a delay measurement or phase measurement. Measurements are
          specified by <x>, which ranges from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOURCE[1]?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOURCE[1]?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SOURCE[1] value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:SOURCE[1] {CH<x>|MATH<y>|REF<x>}
        - MEASUrement:MEAS<x>:SOURCE[1]?
        ```

    Info:
        - ``CH<x>`` is an input channel waveform, where x is the channel number.
        - ``MATH<y>`` is a math waveform, where y is 1.
        - ``REF<x>`` is a reference waveform, where x is the reference channel number.
    """


class MeasurementMeasItemSource2(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:SOURCE2`` command.

    Description:
        - Sets or returns the reference source to measure 'to' when taking a delay measurement or
          phase measurement. Measurements are specified by <x>, which ranges from 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOURCE2?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOURCE2?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SOURCE2 value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:SOURCE2 {CH<x>|MATH<y>|REF<x>}
        - MEASUrement:MEAS<x>:SOURCE2?
        ```

    Info:
        - ``CH<x>`` is an input channel waveform, where x is the channel number.
        - ``MATH<y>`` is the math waveform, which is always 1.
        - ``REF<x>`` is a reference waveform, where x is the reference channel number.
    """


class MeasurementMeasItemMinimum(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:MINImum`` command.

    Description:
        - Returns the minimum value for this measurement since the last statistical reset.
          Measurements are specified by <x>, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:MINImum?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:MINImum?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:MINImum?
        ```
    """


class MeasurementMeasItemMean(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:MEAN`` command.

    Description:
        - Returns the mean value accumulated for this measurement since the last statistical reset.
          Measurements are specified by x, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:MEAN?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:MEAN?
        ```
    """


class MeasurementMeasItemMaximum(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:MAXimum`` command.

    Description:
        - Returns the maximum value found for this measurement since the last statistical reset.
          Measurements are specified by x, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:MAXimum?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:MAXimum?
        ```
    """


class MeasurementMeasItemDelayEdgeItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:DELay:EDGE<x>`` command.

    Description:
        - This command specifies the slope of the edge used for the delay 'from' or 'to' waveform
          when taking an immediate delay measurement. The waveform is specified by
          ``MEASUREMENT:MEASX:SOURCEX``.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay:EDGE<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:DELay:EDGE<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:DELay:EDGE<x> value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:DELay:EDGE<x> {FALL|RISe}
        - MEASUrement:MEAS<x>:DELay:EDGE<x>?
        ```

    Info:
        - ``<x>`` specifies which waveform to use, where <x> = 1 is the 'from' waveform, and <x> = 2
          is the 'to' waveform.
        - ``FALL`` specifies the falling edge.
        - ``RISe`` specifies the rising edge.
    """


class MeasurementMeasItemDelayDirection(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:DELay:DIRection`` command.

    Description:
        - This command specifies the starting point and direction that determines the delay 'to'
          edge when taking a delay measurement. Use the ``MEASUREMENT:MEASX:SOURCEX`` command to
          specify the waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay:DIRection?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:DELay:DIRection?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:DELay:DIRection value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:DELay:DIRection {BACKWards|FORWards}
        - MEASUrement:MEAS<x>:DELay:DIRection?
        ```

    Info:
        - ``BACKWards`` means the search starts at the end of the waveform and looks for the last
          rising or falling edge in the waveform. Use the ``MEASUREMENT:MEASX:DELAY:EDGEX`` command
          to specify the slope of the edge.
        - ``FORWards`` means the search starts at the beginning of the waveform and looks for the
          first rising or falling edge in the waveform. Use the ``MEASUREMENT:MEASX:DELAY:EDGEX``
          command to specify the slope of the edge.
    """


class MeasurementMeasItemDelay(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:DELay`` command.

    Description:
        - Returns the delay measurement parameters for the measurement specified by <x>, which
          ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:DELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:DELay?
        ```

    Properties:
        - ``.direction``: The ``MEASUrement:MEAS<x>:DELay:DIRection`` command.
        - ``.edge``: The ``MEASUrement:MEAS<x>:DELay:EDGE<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = MeasurementMeasItemDelayDirection(device, f"{self._cmd_syntax}:DIRection")
        self._edge: Dict[int, MeasurementMeasItemDelayEdgeItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementMeasItemDelayEdgeItem(device, f"{self._cmd_syntax}:EDGE{x}")
        )

    @property
    def direction(self) -> MeasurementMeasItemDelayDirection:
        """Return the ``MEASUrement:MEAS<x>:DELay:DIRection`` command.

        Description:
            - This command specifies the starting point and direction that determines the delay 'to'
              edge when taking a delay measurement. Use the ``MEASUREMENT:MEASX:SOURCEX`` command to
              specify the waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay:DIRection?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:DELay:DIRection?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:DELay:DIRection value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:DELay:DIRection {BACKWards|FORWards}
            - MEASUrement:MEAS<x>:DELay:DIRection?
            ```

        Info:
            - ``BACKWards`` means the search starts at the end of the waveform and looks for the
              last rising or falling edge in the waveform. Use the ``MEASUREMENT:MEASX:DELAY:EDGEX``
              command to specify the slope of the edge.
            - ``FORWards`` means the search starts at the beginning of the waveform and looks for
              the first rising or falling edge in the waveform. Use the
              ``MEASUREMENT:MEASX:DELAY:EDGEX`` command to specify the slope of the edge.
        """
        return self._direction

    @property
    def edge(self) -> Dict[int, MeasurementMeasItemDelayEdgeItem]:
        """Return the ``MEASUrement:MEAS<x>:DELay:EDGE<x>`` command.

        Description:
            - This command specifies the slope of the edge used for the delay 'from' or 'to'
              waveform when taking an immediate delay measurement. The waveform is specified by
              ``MEASUREMENT:MEASX:SOURCEX``.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay:EDGE<x>?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:DELay:EDGE<x>?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:DELay:EDGE<x> value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:DELay:EDGE<x> {FALL|RISe}
            - MEASUrement:MEAS<x>:DELay:EDGE<x>?
            ```

        Info:
            - ``<x>`` specifies which waveform to use, where <x> = 1 is the 'from' waveform, and <x>
              = 2 is the 'to' waveform.
            - ``FALL`` specifies the falling edge.
            - ``RISe`` specifies the rising edge.
        """
        return self._edge


class MeasurementMeasItemCount(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:COUNt`` command.

    Description:
        - Returns the number of values accumulated for this measurement since the last statistical
          reset. Values may be ignored if they generated an error. Measurements are specified by x,
          which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:COUNt?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:COUNt?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class MeasurementMeasItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>`` command.

    Description:
        - Returns all measurement parameters for the specified active measurement <x>.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>?
        ```

    Properties:
        - ``.count``: The ``MEASUrement:MEAS<x>:COUNt`` command.
        - ``.delay``: The ``MEASUrement:MEAS<x>:DELay`` command.
        - ``.maximum``: The ``MEASUrement:MEAS<x>:MAXimum`` command.
        - ``.mean``: The ``MEASUrement:MEAS<x>:MEAN`` command.
        - ``.minimum``: The ``MEASUrement:MEAS<x>:MINImum`` command.
        - ``.source2``: The ``MEASUrement:MEAS<x>:SOURCE2`` command.
        - ``.source``: The ``MEASUrement:MEAS<x>:SOURCE[1]`` command.
        - ``.source1``: The ``MEASUrement:MEAS<x>:SOUrce1`` command.
        - ``.state``: The ``MEASUrement:MEAS<x>:STATE`` command.
        - ``.stddev``: The ``MEASUrement:MEAS<x>:STDdev`` command.
        - ``.type``: The ``MEASUrement:MEAS<x>:TYPe`` command.
        - ``.units``: The ``MEASUrement:MEAS<x>:UNIts`` command.
        - ``.value``: The ``MEASUrement:MEAS<x>:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = MeasurementMeasItemCount(device, f"{self._cmd_syntax}:COUNt")
        self._delay = MeasurementMeasItemDelay(device, f"{self._cmd_syntax}:DELay")
        self._maximum = MeasurementMeasItemMaximum(device, f"{self._cmd_syntax}:MAXimum")
        self._mean = MeasurementMeasItemMean(device, f"{self._cmd_syntax}:MEAN")
        self._minimum = MeasurementMeasItemMinimum(device, f"{self._cmd_syntax}:MINImum")
        self._source2 = MeasurementMeasItemSource2(device, f"{self._cmd_syntax}:SOURCE2")
        self._source: Dict[int, MeasurementMeasItemSourceItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementMeasItemSourceItem(device, f"{self._cmd_syntax}:SOURCE{x}")
        )
        self._source1 = MeasurementMeasItemSource1(device, f"{self._cmd_syntax}:SOUrce1")
        self._state = MeasurementMeasItemState(device, f"{self._cmd_syntax}:STATE")
        self._stddev = MeasurementMeasItemStddev(device, f"{self._cmd_syntax}:STDdev")
        self._type = MeasurementMeasItemType(device, f"{self._cmd_syntax}:TYPe")
        self._units = MeasurementMeasItemUnits(device, f"{self._cmd_syntax}:UNIts")
        self._value = MeasurementMeasItemValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def count(self) -> MeasurementMeasItemCount:
        """Return the ``MEASUrement:MEAS<x>:COUNt`` command.

        Description:
            - Returns the number of values accumulated for this measurement since the last
              statistical reset. Values may be ignored if they generated an error. Measurements are
              specified by x, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:COUNt?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:COUNt?
            ```
        """
        return self._count

    @property
    def delay(self) -> MeasurementMeasItemDelay:
        """Return the ``MEASUrement:MEAS<x>:DELay`` command.

        Description:
            - Returns the delay measurement parameters for the measurement specified by <x>, which
              ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:DELay?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:DELay?
            ```

        Sub-properties:
            - ``.direction``: The ``MEASUrement:MEAS<x>:DELay:DIRection`` command.
            - ``.edge``: The ``MEASUrement:MEAS<x>:DELay:EDGE<x>`` command.
        """
        return self._delay

    @property
    def maximum(self) -> MeasurementMeasItemMaximum:
        """Return the ``MEASUrement:MEAS<x>:MAXimum`` command.

        Description:
            - Returns the maximum value found for this measurement since the last statistical reset.
              Measurements are specified by x, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:MAXimum?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:MAXimum?
            ```
        """
        return self._maximum

    @property
    def mean(self) -> MeasurementMeasItemMean:
        """Return the ``MEASUrement:MEAS<x>:MEAN`` command.

        Description:
            - Returns the mean value accumulated for this measurement since the last statistical
              reset. Measurements are specified by x, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:MEAN?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:MEAN?
            ```
        """
        return self._mean

    @property
    def minimum(self) -> MeasurementMeasItemMinimum:
        """Return the ``MEASUrement:MEAS<x>:MINImum`` command.

        Description:
            - Returns the minimum value for this measurement since the last statistical reset.
              Measurements are specified by <x>, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:MINImum?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:MINImum?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:MINImum?
            ```
        """
        return self._minimum

    @property
    def source2(self) -> MeasurementMeasItemSource2:
        """Return the ``MEASUrement:MEAS<x>:SOURCE2`` command.

        Description:
            - Sets or returns the reference source to measure 'to' when taking a delay measurement
              or phase measurement. Measurements are specified by <x>, which ranges from 1 through
              4.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOURCE2?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOURCE2?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SOURCE2 value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:SOURCE2 {CH<x>|MATH<y>|REF<x>}
            - MEASUrement:MEAS<x>:SOURCE2?
            ```

        Info:
            - ``CH<x>`` is an input channel waveform, where x is the channel number.
            - ``MATH<y>`` is the math waveform, which is always 1.
            - ``REF<x>`` is a reference waveform, where x is the reference channel number.
        """
        return self._source2

    @property
    def source(self) -> Dict[int, MeasurementMeasItemSourceItem]:
        """Return the ``MEASUrement:MEAS<x>:SOURCE[1]`` command.

        Description:
            - Sets or returns the source for all single source measurements and specifies the source
              to measure 'from' when taking a delay measurement or phase measurement. Measurements
              are specified by <x>, which ranges from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOURCE[1]?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOURCE[1]?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:SOURCE[1] value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:SOURCE[1] {CH<x>|MATH<y>|REF<x>}
            - MEASUrement:MEAS<x>:SOURCE[1]?
            ```

        Info:
            - ``CH<x>`` is an input channel waveform, where x is the channel number.
            - ``MATH<y>`` is a math waveform, where y is 1.
            - ``REF<x>`` is a reference waveform, where x is the reference channel number.
        """
        return self._source

    @property
    def source1(self) -> MeasurementMeasItemSource1:
        """Return the ``MEASUrement:MEAS<x>:SOUrce1`` command.

        Description:
            - For SOURce1: Sets or returns the source for all single channel measurements. For delay
              or phase measurements, sets or returns the waveform to measure 'from'. For SOUrce2:
              Sets or returns the waveform to measure 'to' when taking a delay measurement or phase
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|MATH|}
            - MEASUrement:MEAS<x>:SOUrce1?
            ```

        Info:
            - ``CH<x>`` is an input channel waveform, where x is the channel number.
            - ``MATH`` is the math waveform.
            - ``REF<x>`` is a reference waveform, where x is the reference channel number.
        """
        return self._source1

    @property
    def state(self) -> MeasurementMeasItemState:
        """Return the ``MEASUrement:MEAS<x>:STATE`` command.

        Description:
            - This command specifies whether the specified measurement slot is computed and
              displayed. The measurement slot is specified by <x>, which ranges from 1 through 8.
              For a measurement to display, you must have selected a source waveform and defined the
              measurement you want to take and display. You select the measurement using the
              ``MEASUREMENT:MEASX:SOURCEX`` command. You define the measurement type using the
              ``MEASUREMENT:MEASX:TYPE`` command.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:STATE value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:STATE {ON|OFF|<NR1>}
            - MEASUrement:MEAS<x>:STATE?
            ```

        Info:
            - ``OFF`` disables calculation and display of the specified measurement slot.
            - ``ON`` enables calculation and display of the specified measurement slot.
            - ``<NR1>`` = 0 disables calculation and display of the specified measurement slot; any
              other value enables calculation and display of the specified measurement slot.
        """
        return self._state

    @property
    def stddev(self) -> MeasurementMeasItemStddev:
        """Return the ``MEASUrement:MEAS<x>:STDdev`` command.

        Description:
            - Returns the standard deviation of values accumulated for this measurement since the
              last statistical reset. Measurements are specified by <x>, the measurement slots, from
              1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:STDdev?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:STDdev?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:STDdev?
            ```
        """
        return self._stddev

    @property
    def type(self) -> MeasurementMeasItemType:
        """Return the ``MEASUrement:MEAS<x>:TYPe`` command.

        Description:
            - Sets or returns the measurement type defined for the specified measurement slot. The
              measurement slot is specified by <x>, which ranges from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|LOW|MAXimum|MEAN|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PDUty|PEDGECount|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS}
            - MEASUrement:MEAS<x>:TYPe?
            ```

        Info:
            - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it
              measures the high value less the low value measured over the entire waveform or gated
              region. This measurement is available only on DPO models.
            - ``Amplitude = High - Low``
            - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
              region and is measured in volt-seconds. The area measured above the ground is
              positive, while the area below ground is negative. This measurement is available only
              on DPO models.
            - ``BURst`` measures the duration of a burst. The measurement is made over the entire
              waveform or gated region.
            - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures, in
              volt-seconds, the area over the first cycle in the waveform or the first cycle in the
              gated region. The area measured above the common reference point is positive, while
              the area below the common reference point is negative. This measurement is available
              only on DPO models.
            - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the
              waveform or the first cycle in the gated region. This measurement is available only on
              DPO models.
            - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle
              in the waveform or the first cycle in the gated region. This measurement is available
              only on DPO models.
            - ``DELay`` measures the time between the middle reference (default = 50%) amplitude
              point of the source waveform and the destination waveform. This measurement is
              available only on DPO models.
            - ``FALL`` measures the time taken for the falling edge of the first pulse in the
              waveform or gated region to fall from a high reference value (default is 90%) to a low
              reference value (default is 10%). This measurement is available only on DPO models.
            - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is
              the reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per
              second.
            - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a
              waveform. This measurement is available only on DPO models.
            - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a
              waveform. This measurement is available only on DPO models.
            - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
              found. It is measured over the entire waveform or gated region. This measurement is
              available only on DPO models.
            - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or
              gated region. This measurement is available only on DPO models.
            - ``MINImum`` finds the minimum amplitude. This value is typically the most negative
              peak voltage. It is measured over the entire waveform or gated region. This
              measurement is available only on DPO models.
            - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
              period, expressed as a percentage. The duty cycle is measured on the first cycle in
              the waveform or gated region.
            - ``Negative Duty Cycle = ((Negative Width) / Period) × 100%``
            - ``NEDGECount`` is the count of negative edges.
            - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
              waveform or gated region. This measurement is available only on DPO models.
            - ``Negative Overshoot = ((Low - Minimum) / Amplitude) × 100%)``
            - ``NPULSECount`` is the count of negative pulses.
            - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
              reference (default = 50%) amplitude points of a negative pulse. The measurement is
              made on the first pulse in the waveform or gated region.
            - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
              period, expressed as a percentage. It is measured on the first cycle in the waveform
              or gated region.
            - ``Positive Duty Cycle = ((Positive Width) / Period) × 100%``
            - ``PEDGECount`` is the count of positive edges.
            - ``PERIod`` is the time required to complete the first cycle in a waveform or gated
              region. Period is the reciprocal of frequency and is measured in seconds.
            - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
              reference waveform) between two waveforms. The measurement is made between the middle
              reference points of the two waveforms and is expressed in degrees, where 360°
              represents one waveform cycle.
            - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
              amplitude in the entire waveform or gated region. This measurement is available only
              on DPO models.
            - ``POVershoot`` is the positive overshoot value over the entire waveform or gated
              region. This measurement is available only on DPO models.
            - ``Positive Overshoot = ((Maximum - High) / Amplitude) ×100%``
            - ``PPULSECount`` is the count of positive pulses.
            - ``PWIdth`` (positive width) is the distance (time) between the middle reference
              (default = 50%) amplitude points of a positive pulse. The measurement is made on the
              first pulse in the waveform or gated region.
            - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the
              time it takes for the leading edge of the first pulse encountered to rise from a low
              reference value (default is 10%) to a high reference value (default is 90%). This
              measurement is available only on DPO models.
            - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
              waveform or gated region. This measurement is available only on DPO models.
        """  # noqa: E501
        return self._type

    @property
    def units(self) -> MeasurementMeasItemUnits:
        """Return the ``MEASUrement:MEAS<x>:UNIts`` command.

        Description:
            - Returns the units associated with the specified measurement. The measurement slots are
              specified by <x>, which ranges from 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:UNIts?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:UNIts?
            ```
        """
        return self._units

    @property
    def value(self) -> MeasurementMeasItemValue:
        """Return the ``MEASUrement:MEAS<x>:VALue`` command.

        Description:
            - Returns a calculate value for the measurement specified by <x>, which ranges from 1
              through 4.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:VALue?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:VALue?
            ```
        """
        return self._value


class MeasurementIndicatorsVertItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MEASUrement:INDICators:VERT<x>`` command.

    Description:
        - Returns the value of the specified vertical measurement indicator <x> from the trigger
          point, where <x> can be 1 through 8. A negative value means that the indicator is
          positioned earlier in the waveform record than the trigger point.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:INDICators:VERT<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators:VERT<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:INDICators:VERT<x>?
        ```
    """


class MeasurementIndicatorsState(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:INDICators:STATE`` command.

    Description:
        - This command specifies the state of visible measurement indicators.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:INDICators:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:INDICators:STATE value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:INDICators:STATE {OFF|MEAS<x>}
        - MEASUrement:INDICators:STATE?
        ```

    Info:
        - ``OFF`` turns the visible measurement indicators off.
        - ``MEAS<x>`` displays the visible measurement indicators for measurement <x>, where <x> can
          be 1 through 8.
    """


class MeasurementIndicatorsNumvert(SCPICmdRead):
    """The ``MEASUrement:INDICators:NUMVERT`` command.

    Description:
        - Returns the number of vertical measurement indicators currently being displayed.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:INDICators:NUMVERT?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators:NUMVERT?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:INDICators:NUMVERT?
        ```
    """


class MeasurementIndicatorsNumhorz(SCPICmdRead):
    """The ``MEASUrement:INDICators:NUMHORZ`` command.

    Description:
        - Returns the number of horizontal measurement indicators currently being displayed.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:INDICators:NUMHORZ?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators:NUMHORZ?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:INDICators:NUMHORZ?
        ```
    """


class MeasurementIndicatorsHorzItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MEASUrement:INDICators:HORZ<x>`` command.

    Description:
        - Returns the position of the specified horizontal measurement indicator <x>, where <x> can
          be 1, 2, 3, or 4.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:INDICators:HORZ<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators:HORZ<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:INDICators:HORZ<x>?
        ```
    """


class MeasurementIndicators(SCPICmdRead):
    """The ``MEASUrement:INDICators`` command.

    Description:
        - Returns all measurement indicator parameters.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:INDICators?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:INDICators?
        ```

    Properties:
        - ``.horz``: The ``MEASUrement:INDICators:HORZ<x>`` command.
        - ``.numhorz``: The ``MEASUrement:INDICators:NUMHORZ`` command.
        - ``.numvert``: The ``MEASUrement:INDICators:NUMVERT`` command.
        - ``.state``: The ``MEASUrement:INDICators:STATE`` command.
        - ``.vert``: The ``MEASUrement:INDICators:VERT<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._horz: Dict[int, MeasurementIndicatorsHorzItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementIndicatorsHorzItem(device, f"{self._cmd_syntax}:HORZ{x}")
        )
        self._numhorz = MeasurementIndicatorsNumhorz(device, f"{self._cmd_syntax}:NUMHORZ")
        self._numvert = MeasurementIndicatorsNumvert(device, f"{self._cmd_syntax}:NUMVERT")
        self._state = MeasurementIndicatorsState(device, f"{self._cmd_syntax}:STATE")
        self._vert: Dict[int, MeasurementIndicatorsVertItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementIndicatorsVertItem(device, f"{self._cmd_syntax}:VERT{x}")
        )

    @property
    def horz(self) -> Dict[int, MeasurementIndicatorsHorzItem]:
        """Return the ``MEASUrement:INDICators:HORZ<x>`` command.

        Description:
            - Returns the position of the specified horizontal measurement indicator <x>, where <x>
              can be 1, 2, 3, or 4.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:INDICators:HORZ<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators:HORZ<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:INDICators:HORZ<x>?
            ```
        """
        return self._horz

    @property
    def numhorz(self) -> MeasurementIndicatorsNumhorz:
        """Return the ``MEASUrement:INDICators:NUMHORZ`` command.

        Description:
            - Returns the number of horizontal measurement indicators currently being displayed.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:INDICators:NUMHORZ?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators:NUMHORZ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:INDICators:NUMHORZ?
            ```
        """
        return self._numhorz

    @property
    def numvert(self) -> MeasurementIndicatorsNumvert:
        """Return the ``MEASUrement:INDICators:NUMVERT`` command.

        Description:
            - Returns the number of vertical measurement indicators currently being displayed.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:INDICators:NUMVERT?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators:NUMVERT?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:INDICators:NUMVERT?
            ```
        """
        return self._numvert

    @property
    def state(self) -> MeasurementIndicatorsState:
        """Return the ``MEASUrement:INDICators:STATE`` command.

        Description:
            - This command specifies the state of visible measurement indicators.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:INDICators:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:INDICators:STATE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:INDICators:STATE {OFF|MEAS<x>}
            - MEASUrement:INDICators:STATE?
            ```

        Info:
            - ``OFF`` turns the visible measurement indicators off.
            - ``MEAS<x>`` displays the visible measurement indicators for measurement <x>, where <x>
              can be 1 through 8.
        """
        return self._state

    @property
    def vert(self) -> Dict[int, MeasurementIndicatorsVertItem]:
        """Return the ``MEASUrement:INDICators:VERT<x>`` command.

        Description:
            - Returns the value of the specified vertical measurement indicator <x> from the trigger
              point, where <x> can be 1 through 8. A negative value means that the indicator is
              positioned earlier in the waveform record than the trigger point.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:INDICators:VERT<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators:VERT<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:INDICators:VERT<x>?
            ```
        """
        return self._vert


class MeasurementImmedValue(SCPICmdRead):
    """The ``MEASUrement:IMMed:VALue`` command.

    Description:
        - Returns the value of the measurement specified by the ``MEASUREMENT:IMMED:TYPE`` command.
          The measurement is immediately taken on the source(s) specified by a
          ``MEASUREMENT:IMMED:SOURCEX`` command.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:VALue?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:VALue?
        ```
    """


class MeasurementImmedUnits(SCPICmdRead):
    """The ``MEASUrement:IMMed:UNIts`` command.

    Description:
        - Returns a string containing the units of the immediate measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:UNIts?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:UNIts?
        ```
    """


class MeasurementImmedType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:TYPe`` command.

    Description:
        - Sets or returns the immediate measurement type.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:TYPe value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|LOW|MAXimum|MEAN|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PEDGECount|PDUty|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS}
        - MEASUrement:IMMed:TYPe?
        ```

    Info:
        - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it measures
          the high value less the low value measured over the entire waveform or gated region. This
          measurement is available only on DPO models.
        - ``Amplitude = High - Low``
        - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
          region and is measured in volt-seconds. The area measured above the ground is positive,
          while the area below ground is negative. This measurement is available only on DPO models.
        - ``BURst`` measures the duration of a burst. The measurement is made over the entire
          waveform or gated region.
        - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures, in
          volt-seconds, the area over the first cycle in the waveform or the first cycle in the
          gated region. The area measured above the common reference point is positive, while the
          area below the common reference point is negative. This measurement is available on DPO
          and MSO models.
        - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the waveform
          or the first cycle in the gated region. This measurement is available only on DPO and MSO
          models.
        - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle in
          the waveform or the first cycle in the gated region. This measurement is available only on
          DPO and MSO models.
        - ``DELay`` measures the time between the middle reference (default = 50%) amplitude point
          of the source waveform and the destination waveform.
        - ``FALL`` measures the time taken for the falling edge of the first pulse in the waveform
          or gated region to fall from a high reference value (default is 90%) to a low reference
          value (default is 10%). This measurement is available only on DPO models.
        - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is the
          reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per second.
        - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a waveform.
          This measurement is available only on DPO models.
        - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a waveform.
          This measurement is available only on DPO models.
        - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
          found. It is measured over the entire waveform or gated region. This measurement is
          available only on DPO models.
        - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or gated
          region. This measurement is available only on DPO models.
        - ``MINImum`` finds the minimum amplitude. This value is typically the most negative peak
          voltage. It is measured over the entire waveform or gated region. This measurement is
          available only on DPO models.
        - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
          period, expressed as a percentage. The duty cycle is measured on the first cycle in the
          waveform or gated region.
        - ``Negative Duty Cycle = ((Negative Width) / Period) × 100%``
        - ``NEDGECount`` is the count of falling edges.
        - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
          waveform or gated region. This measurement is available only on DPO models.
        - ``Negative Overshoot = ((Low - Minimum) / Amplitude) × 100%)``
        - ``NPULSECount`` is the count of negative pulses.
        - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
          reference (default = 50%) amplitude points of a negative pulse. The measurement is made on
          the first pulse in the waveform or gated region.
        - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
          period, expressed as a percentage. It is measured on the first cycle in the waveform or
          gated region.
        - ``Positive Duty Cycle = ((Positive Width / Period) × 100%``
        - ``PEDGECount`` is the count of rising edges.
        - ``PERIod`` is the time required to complete the first cycle in a waveform or gated region.
          Period is the reciprocal of frequency and is measured in seconds.
        - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
          reference waveform) between two waveforms. The measurement is made between the middle
          reference points of the two waveforms and is expressed in degrees, where 360° represents
          one waveform cycle.
        - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
          amplitude in the entire waveform or gated region. This measurement is available only on
          DPO models.
        - ``POVershoot`` is the positive overshoot value over the entire waveform or gated region.
          This measurement is available only on DPO models.
        - ``Positive Overshoot = ((Maximum - High) / Amplitude) ×100%``
        - ``PPULSECount`` is the count of positive pulses.
        - ``PWIdth`` (positive width) is the distance (time) between the middle reference (default =
          50%) amplitude points of a positive pulse. The measurement is made on the first pulse in
          the waveform or gated region.
        - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the time
          it takes for the leading edge of the first pulse encountered to rise from a low reference
          value (default is 10%) to a high reference value (default is 90%). This measurement is
          available only on DPO models.
        - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
          waveform or gated region. This measurement is available only on DPO models.
    """  # noqa: E501


class MeasurementImmedSource2(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:SOUrce2`` command.

    Description:
        - Sets or returns the source to measure 'to' for phase or delay immediate measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:SOUrce2?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:SOUrce2?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:SOUrce2 value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:SOUrce2 {CH<x>|MATH<y>|REF<x>}
        - MEASUrement:IMMed:SOUrce2?
        ```

    Info:
        - ``CH<x>`` is an input channel waveform, where x is the channel number.
        - ``MATH<y>`` is a math waveform. The y variable can be expressed as an integer of 1.
        - ``REF<X>`` is a reference waveform, where x is the reference channel number.
    """


class MeasurementImmedSource1(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:SOUrce1`` command.

    Description:
        - Sets or returns the source for all single source immediate measurements and specifies the
          source to measure 'from' when taking an immediate delay measurement or phase measurement.
          Digital channels (D<x>) are available as a measurement source for time, edge and pulse
          measurements such as Period, Frequency, Pos Width, Neg Width, Pos Duty Cycle, Neg Duty
          Cycle, Pos/Neg Edges and Pos/Neg Pulses, Delay and Phase.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:SOUrce1 value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:SOUrce1 {CH<x>|MATH<y>|REF<x>}
        - MEASUrement:IMMed:SOUrce1?
        ```

    Info:
        - ``CH<x>`` is an input channel waveform. The x variable can be expressed as an integer,
          where x is the channel number.
        - ``MATH<y>`` is a math waveform. The y variable can be expressed as an integer of 1.
        - ``REF<X>`` is a reference waveform. The x variable can be expressed as an integer, where x
          is the reference channel number.
    """


class MeasurementImmedDelayEdgeItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:DELay:EDGE<x>`` command.

    Description:
        - This command specifies the slope of the edge the oscilloscope uses for the delay 'from' or
          'to' waveform when taking an immediate delay measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:DELay:EDGE<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:DELay:EDGE<x>?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:DELay:EDGE<x> value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:DELay:EDGE<x> {FALL|RISe}
        - MEASUrement:IMMed:DELay:EDGE<x>?
        ```

    Info:
        - ``<x>`` specifies which waveform to use, where <x> = 1 is the 'from' waveform, and <x> = 2
          is the 'to' waveform.
        - ``FALL`` specifies the falling edge.
        - ``RISe`` specifies the rising edge.
    """


class MeasurementImmedDelayDirection(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:DELay:DIRection`` command.

    Description:
        - This command specifies the starting point and direction that determines the delay 'to'
          edge when taking an immediate delay measurement.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:DELay:DIRection?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:DELay:DIRection?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:IMMed:DELay:DIRection value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:DELay:DIRection {BACKWards|FORWards}
        - MEASUrement:IMMed:DELay:DIRection?
        ```

    Info:
        - ``BACKWards`` starts the search at the end of the waveform and looks for the last rising
          or falling edge in the waveform.
        - ``FORWards`` starts the search at the beginning of the waveform and looks for the first
          rising or falling edge in the waveform.
    """


class MeasurementImmedDelay(SCPICmdRead):
    """The ``MEASUrement:IMMed:DELay`` command.

    Description:
        - Returns information about the immediate delay measurement. This command is equivalent to
          viewing the delay measurement settings on the measurement readout.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:DELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:DELay?
        ```

    Properties:
        - ``.direction``: The ``MEASUrement:IMMed:DELay:DIRection`` command.
        - ``.edge``: The ``MEASUrement:IMMed:DELay:EDGE<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = MeasurementImmedDelayDirection(device, f"{self._cmd_syntax}:DIRection")
        self._edge: Dict[int, MeasurementImmedDelayEdgeItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementImmedDelayEdgeItem(device, f"{self._cmd_syntax}:EDGE{x}")
        )

    @property
    def direction(self) -> MeasurementImmedDelayDirection:
        """Return the ``MEASUrement:IMMed:DELay:DIRection`` command.

        Description:
            - This command specifies the starting point and direction that determines the delay 'to'
              edge when taking an immediate delay measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:DELay:DIRection?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:DELay:DIRection?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:DELay:DIRection value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:DELay:DIRection {BACKWards|FORWards}
            - MEASUrement:IMMed:DELay:DIRection?
            ```

        Info:
            - ``BACKWards`` starts the search at the end of the waveform and looks for the last
              rising or falling edge in the waveform.
            - ``FORWards`` starts the search at the beginning of the waveform and looks for the
              first rising or falling edge in the waveform.
        """
        return self._direction

    @property
    def edge(self) -> Dict[int, MeasurementImmedDelayEdgeItem]:
        """Return the ``MEASUrement:IMMed:DELay:EDGE<x>`` command.

        Description:
            - This command specifies the slope of the edge the oscilloscope uses for the delay
              'from' or 'to' waveform when taking an immediate delay measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:DELay:EDGE<x>?``
              query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:DELay:EDGE<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:DELay:EDGE<x> value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:DELay:EDGE<x> {FALL|RISe}
            - MEASUrement:IMMed:DELay:EDGE<x>?
            ```

        Info:
            - ``<x>`` specifies which waveform to use, where <x> = 1 is the 'from' waveform, and <x>
              = 2 is the 'to' waveform.
            - ``FALL`` specifies the falling edge.
            - ``RISe`` specifies the rising edge.
        """
        return self._edge


class MeasurementImmed(SCPICmdRead):
    """The ``MEASUrement:IMMed`` command.

    Description:
        - Returns all immediate measurement setup parameters.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed?
        ```

    Properties:
        - ``.delay``: The ``MEASUrement:IMMed:DELay`` command.
        - ``.source1``: The ``MEASUrement:IMMed:SOUrce1`` command.
        - ``.source2``: The ``MEASUrement:IMMed:SOUrce2`` command.
        - ``.type``: The ``MEASUrement:IMMed:TYPe`` command.
        - ``.units``: The ``MEASUrement:IMMed:UNIts`` command.
        - ``.value``: The ``MEASUrement:IMMed:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delay = MeasurementImmedDelay(device, f"{self._cmd_syntax}:DELay")
        self._source2 = MeasurementImmedSource2(device, f"{self._cmd_syntax}:SOUrce2")
        self._source1 = MeasurementImmedSource1(device, f"{self._cmd_syntax}:SOUrce1")
        self._type = MeasurementImmedType(device, f"{self._cmd_syntax}:TYPe")
        self._units = MeasurementImmedUnits(device, f"{self._cmd_syntax}:UNIts")
        self._value = MeasurementImmedValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def delay(self) -> MeasurementImmedDelay:
        """Return the ``MEASUrement:IMMed:DELay`` command.

        Description:
            - Returns information about the immediate delay measurement. This command is equivalent
              to viewing the delay measurement settings on the measurement readout.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:DELay?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:DELay?
            ```

        Sub-properties:
            - ``.direction``: The ``MEASUrement:IMMed:DELay:DIRection`` command.
            - ``.edge``: The ``MEASUrement:IMMed:DELay:EDGE<x>`` command.
        """
        return self._delay

    @property
    def source2(self) -> MeasurementImmedSource2:
        """Return the ``MEASUrement:IMMed:SOUrce2`` command.

        Description:
            - Sets or returns the source to measure 'to' for phase or delay immediate measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:SOUrce2?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:SOUrce2?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:SOUrce2 value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:SOUrce2 {CH<x>|MATH<y>|REF<x>}
            - MEASUrement:IMMed:SOUrce2?
            ```

        Info:
            - ``CH<x>`` is an input channel waveform, where x is the channel number.
            - ``MATH<y>`` is a math waveform. The y variable can be expressed as an integer of 1.
            - ``REF<X>`` is a reference waveform, where x is the reference channel number.
        """
        return self._source2

    @property
    def source1(self) -> MeasurementImmedSource1:
        """Return the ``MEASUrement:IMMed:SOUrce1`` command.

        Description:
            - Sets or returns the source for all single source immediate measurements and specifies
              the source to measure 'from' when taking an immediate delay measurement or phase
              measurement. Digital channels (D<x>) are available as a measurement source for time,
              edge and pulse measurements such as Period, Frequency, Pos Width, Neg Width, Pos Duty
              Cycle, Neg Duty Cycle, Pos/Neg Edges and Pos/Neg Pulses, Delay and Phase.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:SOUrce1 {CH<x>|MATH<y>|REF<x>}
            - MEASUrement:IMMed:SOUrce1?
            ```

        Info:
            - ``CH<x>`` is an input channel waveform. The x variable can be expressed as an integer,
              where x is the channel number.
            - ``MATH<y>`` is a math waveform. The y variable can be expressed as an integer of 1.
            - ``REF<X>`` is a reference waveform. The x variable can be expressed as an integer,
              where x is the reference channel number.
        """
        return self._source1

    @property
    def type(self) -> MeasurementImmedType:
        """Return the ``MEASUrement:IMMed:TYPe`` command.

        Description:
            - Sets or returns the immediate measurement type.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:TYPe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|LOW|MAXimum|MEAN|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PEDGECount|PDUty|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS}
            - MEASUrement:IMMed:TYPe?
            ```

        Info:
            - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it
              measures the high value less the low value measured over the entire waveform or gated
              region. This measurement is available only on DPO models.
            - ``Amplitude = High - Low``
            - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
              region and is measured in volt-seconds. The area measured above the ground is
              positive, while the area below ground is negative. This measurement is available only
              on DPO models.
            - ``BURst`` measures the duration of a burst. The measurement is made over the entire
              waveform or gated region.
            - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures, in
              volt-seconds, the area over the first cycle in the waveform or the first cycle in the
              gated region. The area measured above the common reference point is positive, while
              the area below the common reference point is negative. This measurement is available
              on DPO and MSO models.
            - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the
              waveform or the first cycle in the gated region. This measurement is available only on
              DPO and MSO models.
            - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle
              in the waveform or the first cycle in the gated region. This measurement is available
              only on DPO and MSO models.
            - ``DELay`` measures the time between the middle reference (default = 50%) amplitude
              point of the source waveform and the destination waveform.
            - ``FALL`` measures the time taken for the falling edge of the first pulse in the
              waveform or gated region to fall from a high reference value (default is 90%) to a low
              reference value (default is 10%). This measurement is available only on DPO models.
            - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is
              the reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per
              second.
            - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a
              waveform. This measurement is available only on DPO models.
            - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a
              waveform. This measurement is available only on DPO models.
            - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
              found. It is measured over the entire waveform or gated region. This measurement is
              available only on DPO models.
            - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or
              gated region. This measurement is available only on DPO models.
            - ``MINImum`` finds the minimum amplitude. This value is typically the most negative
              peak voltage. It is measured over the entire waveform or gated region. This
              measurement is available only on DPO models.
            - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
              period, expressed as a percentage. The duty cycle is measured on the first cycle in
              the waveform or gated region.
            - ``Negative Duty Cycle = ((Negative Width) / Period) × 100%``
            - ``NEDGECount`` is the count of falling edges.
            - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
              waveform or gated region. This measurement is available only on DPO models.
            - ``Negative Overshoot = ((Low - Minimum) / Amplitude) × 100%)``
            - ``NPULSECount`` is the count of negative pulses.
            - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
              reference (default = 50%) amplitude points of a negative pulse. The measurement is
              made on the first pulse in the waveform or gated region.
            - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
              period, expressed as a percentage. It is measured on the first cycle in the waveform
              or gated region.
            - ``Positive Duty Cycle = ((Positive Width / Period) × 100%``
            - ``PEDGECount`` is the count of rising edges.
            - ``PERIod`` is the time required to complete the first cycle in a waveform or gated
              region. Period is the reciprocal of frequency and is measured in seconds.
            - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
              reference waveform) between two waveforms. The measurement is made between the middle
              reference points of the two waveforms and is expressed in degrees, where 360°
              represents one waveform cycle.
            - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
              amplitude in the entire waveform or gated region. This measurement is available only
              on DPO models.
            - ``POVershoot`` is the positive overshoot value over the entire waveform or gated
              region. This measurement is available only on DPO models.
            - ``Positive Overshoot = ((Maximum - High) / Amplitude) ×100%``
            - ``PPULSECount`` is the count of positive pulses.
            - ``PWIdth`` (positive width) is the distance (time) between the middle reference
              (default = 50%) amplitude points of a positive pulse. The measurement is made on the
              first pulse in the waveform or gated region.
            - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the
              time it takes for the leading edge of the first pulse encountered to rise from a low
              reference value (default is 10%) to a high reference value (default is 90%). This
              measurement is available only on DPO models.
            - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
              waveform or gated region. This measurement is available only on DPO models.
        """  # noqa: E501
        return self._type

    @property
    def units(self) -> MeasurementImmedUnits:
        """Return the ``MEASUrement:IMMed:UNIts`` command.

        Description:
            - Returns a string containing the units of the immediate measurement.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:UNIts?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:UNIts?
            ```
        """
        return self._units

    @property
    def value(self) -> MeasurementImmedValue:
        """Return the ``MEASUrement:IMMed:VALue`` command.

        Description:
            - Returns the value of the measurement specified by the ``MEASUREMENT:IMMED:TYPE``
              command. The measurement is immediately taken on the source(s) specified by a
              ``MEASUREMENT:IMMED:SOURCEX`` command.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:VALue?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:VALue?
            ```
        """
        return self._value


class MeasurementGating(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:GATing`` command.

    Description:
        - Specifies or returns the measurement gating setting.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:GATing?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:GATing value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:GATing {OFF|SCREen|CURSor}
        - MEASUrement:GATing?
        ```

    Info:
        - ``OFF`` turns off measurement gating (full record).
        - ``SCREen`` turns on gating, using the left and right edges of the screen.
        - ``CURSor`` limits measurements to the portion of the waveform between the vertical bar
          cursors, even if they are off screen.
    """


class MeasurementClearsnapshot(SCPICmdWriteNoArguments):
    """The ``MEASUrement:CLEARSNapshot`` command.

    Description:
        - Removes the measurement snapshot display.

    Usage:
        - Using the ``.write()`` method will send the ``MEASUrement:CLEARSNapshot`` command.

    SCPI Syntax:
        ```
        - MEASUrement:CLEARSNapshot
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Measurement(SCPICmdRead):
    """The ``MEASUrement`` command.

    Description:
        - This query-only command returns all measurement parameters.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement?
        ```

    Properties:
        - ``.clearsnapshot``: The ``MEASUrement:CLEARSNapshot`` command.
        - ``.gating``: The ``MEASUrement:GATing`` command.
        - ``.immed``: The ``MEASUrement:IMMed`` command.
        - ``.indicators``: The ``MEASUrement:INDICators`` command.
        - ``.meas``: The ``MEASUrement:MEAS<x>`` command.
        - ``.method``: The ``MEASUrement:METHod`` command.
        - ``.reflevel``: The ``MEASUrement:REFLevel`` command.
        - ``.snapshot``: The ``MEASUrement:SNAPShot`` command.
        - ``.statistics``: The ``MEASUrement:STATIstics`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "MEASUrement"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._clearsnapshot = MeasurementClearsnapshot(device, f"{self._cmd_syntax}:CLEARSNapshot")
        self._gating = MeasurementGating(device, f"{self._cmd_syntax}:GATing")
        self._immed = MeasurementImmed(device, f"{self._cmd_syntax}:IMMed")
        self._indicators = MeasurementIndicators(device, f"{self._cmd_syntax}:INDICators")
        self._meas: Dict[int, MeasurementMeasItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementMeasItem(device, f"{self._cmd_syntax}:MEAS{x}")
        )
        self._method = MeasurementMethod(device, f"{self._cmd_syntax}:METHod")
        self._reflevel = MeasurementReflevel(device, f"{self._cmd_syntax}:REFLevel")
        self._snapshot = MeasurementSnapshot(device, f"{self._cmd_syntax}:SNAPShot")
        self._statistics = MeasurementStatistics(device, f"{self._cmd_syntax}:STATIstics")

    @property
    def clearsnapshot(self) -> MeasurementClearsnapshot:
        """Return the ``MEASUrement:CLEARSNapshot`` command.

        Description:
            - Removes the measurement snapshot display.

        Usage:
            - Using the ``.write()`` method will send the ``MEASUrement:CLEARSNapshot`` command.

        SCPI Syntax:
            ```
            - MEASUrement:CLEARSNapshot
            ```
        """
        return self._clearsnapshot

    @property
    def gating(self) -> MeasurementGating:
        """Return the ``MEASUrement:GATing`` command.

        Description:
            - Specifies or returns the measurement gating setting.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:GATing?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:GATing value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:GATing {OFF|SCREen|CURSor}
            - MEASUrement:GATing?
            ```

        Info:
            - ``OFF`` turns off measurement gating (full record).
            - ``SCREen`` turns on gating, using the left and right edges of the screen.
            - ``CURSor`` limits measurements to the portion of the waveform between the vertical bar
              cursors, even if they are off screen.
        """
        return self._gating

    @property
    def immed(self) -> MeasurementImmed:
        """Return the ``MEASUrement:IMMed`` command.

        Description:
            - Returns all immediate measurement setup parameters.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed?
            ```

        Sub-properties:
            - ``.delay``: The ``MEASUrement:IMMed:DELay`` command.
            - ``.source1``: The ``MEASUrement:IMMed:SOUrce1`` command.
            - ``.source2``: The ``MEASUrement:IMMed:SOUrce2`` command.
            - ``.type``: The ``MEASUrement:IMMed:TYPe`` command.
            - ``.units``: The ``MEASUrement:IMMed:UNIts`` command.
            - ``.value``: The ``MEASUrement:IMMed:VALue`` command.
        """
        return self._immed

    @property
    def indicators(self) -> MeasurementIndicators:
        """Return the ``MEASUrement:INDICators`` command.

        Description:
            - Returns all measurement indicator parameters.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:INDICators?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:INDICators?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:INDICators?
            ```

        Sub-properties:
            - ``.horz``: The ``MEASUrement:INDICators:HORZ<x>`` command.
            - ``.numhorz``: The ``MEASUrement:INDICators:NUMHORZ`` command.
            - ``.numvert``: The ``MEASUrement:INDICators:NUMVERT`` command.
            - ``.state``: The ``MEASUrement:INDICators:STATE`` command.
            - ``.vert``: The ``MEASUrement:INDICators:VERT<x>`` command.
        """
        return self._indicators

    @property
    def meas(self) -> Dict[int, MeasurementMeasItem]:
        """Return the ``MEASUrement:MEAS<x>`` command.

        Description:
            - Returns all measurement parameters for the specified active measurement <x>.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>?
            ```

        Sub-properties:
            - ``.count``: The ``MEASUrement:MEAS<x>:COUNt`` command.
            - ``.delay``: The ``MEASUrement:MEAS<x>:DELay`` command.
            - ``.maximum``: The ``MEASUrement:MEAS<x>:MAXimum`` command.
            - ``.mean``: The ``MEASUrement:MEAS<x>:MEAN`` command.
            - ``.minimum``: The ``MEASUrement:MEAS<x>:MINImum`` command.
            - ``.source2``: The ``MEASUrement:MEAS<x>:SOURCE2`` command.
            - ``.source``: The ``MEASUrement:MEAS<x>:SOURCE[1]`` command.
            - ``.source1``: The ``MEASUrement:MEAS<x>:SOUrce1`` command.
            - ``.state``: The ``MEASUrement:MEAS<x>:STATE`` command.
            - ``.stddev``: The ``MEASUrement:MEAS<x>:STDdev`` command.
            - ``.type``: The ``MEASUrement:MEAS<x>:TYPe`` command.
            - ``.units``: The ``MEASUrement:MEAS<x>:UNIts`` command.
            - ``.value``: The ``MEASUrement:MEAS<x>:VALue`` command.
        """
        return self._meas

    @property
    def method(self) -> MeasurementMethod:
        """Return the ``MEASUrement:METHod`` command.

        Description:
            - This command specifies the method used to calculate the 0% and 100% reference level.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:METHod?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:METHod?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:METHod value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:METHod {Auto|HIStogram|MINMax}
            - MEASUrement:METHod?
            ```

        Info:
            - ``Auto`` selects the best method for each data set.
            - ``HIStogram`` sets the high and low waveform levels statistically using a histogram
              algorithm.
            - ``MINMax`` uses the highest and lowest values of the waveform record. This selection
              is best for examining waveforms with no large, flat portions of a common value, such
              as sine waves and triangle waves.
        """
        return self._method

    @property
    def reflevel(self) -> MeasurementReflevel:
        """Return the ``MEASUrement:REFLevel`` command.

        Description:
            - Returns the current reference level parameters.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:REFLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:REFLevel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:REFLevel?
            ```

        Sub-properties:
            - ``.absolute``: The ``MEASUrement:REFLevel:ABSolute`` command tree.
            - ``.method``: The ``MEASUrement:REFLevel:METHod`` command.
            - ``.percent``: The ``MEASUrement:REFLevel:PERCent`` command tree.
        """
        return self._reflevel

    @property
    def snapshot(self) -> MeasurementSnapshot:
        """Return the ``MEASUrement:SNAPShot`` command.

        Description:
            - Displays the measurement snapshot list on the oscilloscope screen. The list contains
              the immediate values for all available measurements of the active signal. You can
              query each individual measurement separately.

        Usage:
            - Using the ``.write()`` method will send the ``MEASUrement:SNAPShot`` command.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot
            ```
        """
        return self._snapshot

    @property
    def statistics(self) -> MeasurementStatistics:
        """Return the ``MEASUrement:STATIstics`` command.

        Description:
            - Clears all of the statistics accumulated for all periodic measurements (MEAS1 through
              MEAS4). The query form returns statistic settings.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:STATIstics?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:STATIstics value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:STATIstics RESET
            - MEASUrement:STATIstics?
            ```

        Info:
            - ``RESET`` clears the measurements.

        Sub-properties:
            - ``.mode``: The ``MEASUrement:STATIstics:MODE`` command.
            - ``.weighting``: The ``MEASUrement:STATIstics:WEIghting`` command.
        """
        return self._statistics
