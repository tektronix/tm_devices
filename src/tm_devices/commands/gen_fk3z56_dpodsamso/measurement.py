# pylint: disable=line-too-long
"""The measurement commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MEASUrement:ANNOTation:IMMEDSTAte {ON|OFF|<NR1>}
    - MEASUrement:ANNOTation:IMMEDSTAte?
    - MEASUrement:ANNOTation:NUMX?
    - MEASUrement:ANNOTation:NUMY?
    - MEASUrement:ANNOTation:STATE {OFF|MEAS<x>}
    - MEASUrement:ANNOTation:STATE?
    - MEASUrement:ANNOTation:TYPe {STANdard|DETAiled}
    - MEASUrement:ANNOTation:TYPe?
    - MEASUrement:ANNOTation:X<x>?
    - MEASUrement:ANNOTation:Y<x>?
    - MEASUrement:DPOJETSTATistics?
    - MEASUrement:GATing {ON|OFF|<NR1>|ZOOM<x>|CURSor}
    - MEASUrement:GATing?
    - MEASUrement:IMMed:DELay:DIREction {BACKWards|FORWards}
    - MEASUrement:IMMed:DELay:DIREction?
    - MEASUrement:IMMed:DELay:EDGE2 {FALL|RISe}
    - MEASUrement:IMMed:DELay:EDGE2?
    - MEASUrement:IMMed:DELay:EDGE<x> {FALL|RISe}
    - MEASUrement:IMMed:DELay:EDGE<x>?
    - MEASUrement:IMMed:DELay?
    - MEASUrement:IMMed:METHod {HIStogram|MINMax|MEAN}
    - MEASUrement:IMMed:METHod?
    - MEASUrement:IMMed:NOISe {HIGH|LOW}
    - MEASUrement:IMMed:NOISe?
    - MEASUrement:IMMed:REFLevel:ABSolute:HIGH <NR3>
    - MEASUrement:IMMed:REFLevel:ABSolute:HIGH?
    - MEASUrement:IMMed:REFLevel:ABSolute:LOW <NR3>
    - MEASUrement:IMMed:REFLevel:ABSolute:LOW?
    - MEASUrement:IMMed:REFLevel:ABSolute:MID<x> <NR3>
    - MEASUrement:IMMed:REFLevel:ABSolute:MID<x>?
    - MEASUrement:IMMed:REFLevel:METHod {ABSolute|PERCent}
    - MEASUrement:IMMed:REFLevel:METHod?
    - MEASUrement:IMMed:REFLevel:PERCent:HIGH <NR1>
    - MEASUrement:IMMed:REFLevel:PERCent:HIGH?
    - MEASUrement:IMMed:REFLevel:PERCent:LOW <NR1>
    - MEASUrement:IMMed:REFLevel:PERCent:LOW?
    - MEASUrement:IMMed:REFLevel:PERCent:MID<x> <NR1>
    - MEASUrement:IMMed:REFLevel:PERCent:MID<x>?
    - MEASUrement:IMMed:REFLevel?
    - MEASUrement:IMMed:SOUrce1 {CH<x>|MATH<y>|REF<x>|HIStogram}
    - MEASUrement:IMMed:SOUrce1:SIGType {PULse|EYE}
    - MEASUrement:IMMed:SOUrce1:SIGType?
    - MEASUrement:IMMed:SOUrce1?
    - MEASUrement:IMMed:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|DISTDUty|EXTINCTDB|EXTINCTPCT|EXTINCTRATIO|EYEHeight|EYEWIdth|FALL|FREQuency|HIGH|HITs|LOW|MAXimum|MEAN|MEDian|MINImum|NCROss|NDUty|NOVershoot|NWIdth|PBASe|PCROss|PCTCROss|PDUty|PEAKHits|PERIod|PHAse|PK2Pk|PKPKJitter|PKPKNoise|POVershoot|PTOP|PWIdth|QFACtor|RISe|RMS|RMSJitter|RMSNoise|SIGMA1|SIGMA2|SIGMA3|SIXSigmajit|SNRatio|STDdev|UNDEFINED|WAVEFORMS}
    - MEASUrement:IMMed:TYPe?
    - MEASUrement:IMMed:UNIts?
    - MEASUrement:IMMed:VALue?
    - MEASUrement:IMMed?
    - MEASUrement:MEAS<x>:COUNt?
    - MEASUrement:MEAS<x>:DELay:DIREction {BACKWards|FORWards}
    - MEASUrement:MEAS<x>:DELay:DIREction?
    - MEASUrement:MEAS<x>:DELay:EDGE<x> {FALL|RISe}
    - MEASUrement:MEAS<x>:DELay:EDGE<x>?
    - MEASUrement:MEAS<x>:DELay?
    - MEASUrement:MEAS<x>:MAXimum?
    - MEASUrement:MEAS<x>:MEAN?
    - MEASUrement:MEAS<x>:METHod {HIStogram|MINMax|MEAN}
    - MEASUrement:MEAS<x>:METHod?
    - MEASUrement:MEAS<x>:MINImum?
    - MEASUrement:MEAS<x>:NOISe {HIGH|LOW}
    - MEASUrement:MEAS<x>:NOISe?
    - MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH <NR3>
    - MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH?
    - MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW <NR3>
    - MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW?
    - MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x> <NR3>
    - MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x>?
    - MEASUrement:MEAS<x>:REFLevel:METHod {ABSolute|PERCent}
    - MEASUrement:MEAS<x>:REFLevel:METHod?
    - MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH <NR3>
    - MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH?
    - MEASUrement:MEAS<x>:REFLevel:PERCent:LOW <NR3>
    - MEASUrement:MEAS<x>:REFLevel:PERCent:LOW?
    - MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x> <NR3>
    - MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x>?
    - MEASUrement:MEAS<x>:REFLevel?
    - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|MATH<y>|REF<x>|HIStogram}
    - MEASUrement:MEAS<x>:SOUrce1:SIGType {PULse|EYE}
    - MEASUrement:MEAS<x>:SOUrce1:SIGType?
    - MEASUrement:MEAS<x>:SOUrce1?
    - MEASUrement:MEAS<x>:STATE {ON|OFF|<NR1>}
    - MEASUrement:MEAS<x>:STATE?
    - MEASUrement:MEAS<x>:STDdev?
    - MEASUrement:MEAS<x>:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|DISTDUty|EXTINCTDB|EXTINCTPCT|EXTINCTRATIO|EYEHeight|EYEWIdth|FALL|FREQuency|HIGH|HITs|LOW|MAXimum|MEAN|MEDian|MINImum|NCROss|NDUty|NOVershoot|NWIdth|PBASe|PCROss|PCTCROss|PDUty|PEAKHits|PERIod|PHAse|PK2Pk|PKPKJitter|PKPKNoise|POVershoot|PTOP|PWIdth|QFACtor|RISe|RMS|RMSJitter|RMSNoise|SIGMA1|SIGMA2|SIGMA3|SIXSigmajit|SNRatio|STDdev|UNDEFINED|WAVEFORMS}
    - MEASUrement:MEAS<x>:TYPe?
    - MEASUrement:MEAS<x>:UNIts?
    - MEASUrement:MEAS<x>:VALue?
    - MEASUrement:MEAS<x>?
    - MEASUrement:METHod {HIStogram|MEAN|MINMax}
    - MEASUrement:METHod?
    - MEASUrement:NOISe {HIGH|LOW}
    - MEASUrement:NOISe?
    - MEASUrement:REFLevel:ABSolute:HIGH <NR3>
    - MEASUrement:REFLevel:ABSolute:HIGH?
    - MEASUrement:REFLevel:ABSolute:LOW <NR3>
    - MEASUrement:REFLevel:ABSolute:LOW?
    - MEASUrement:REFLevel:ABSolute:MID<x> <NR3>
    - MEASUrement:REFLevel:ABSolute:MID<x>?
    - MEASUrement:REFLevel:METHod {ABSolute|PERCent}
    - MEASUrement:REFLevel:METHod?
    - MEASUrement:REFLevel:PERCent:HIGH <NR3>
    - MEASUrement:REFLevel:PERCent:HIGH?
    - MEASUrement:REFLevel:PERCent:LOW <NR3>
    - MEASUrement:REFLevel:PERCent:LOW?
    - MEASUrement:REFLevel:PERCent:MID<x> <NR3>
    - MEASUrement:REFLevel:PERCent:MID<x>?
    - MEASUrement:REFLevel?
    - MEASUrement:SOUrce1:SIGType {PULse|EYE}
    - MEASUrement:SOUrce1:SIGType?
    - MEASUrement:STATIstics:COUNt {RESET}
    - MEASUrement:STATIstics:MODe {OFF|ALL|VALUEMean|MINMax|MEANSTDdev}
    - MEASUrement:STATIstics:MODe?
    - MEASUrement:STATIstics:WEIghting <NR1>
    - MEASUrement:STATIstics:WEIghting?
    - MEASUrement?
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
    """The ``MEASUrement:STATIstics:MODe`` command.

    Description:
        - This command controls the operation and display of measurement statistics. This command is
          equivalent to selecting Measurement Setup from the Measure menu, clicking the Statistics
          button and then choosing the desired Measurement Format.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:STATIstics:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics:MODe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:STATIstics:MODe value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:STATIstics:MODe {OFF|ALL|VALUEMean|MINMax|MEANSTDdev}
        - MEASUrement:STATIstics:MODe?
        ```

    Info:
        - ``OFF`` turns off all measurements. This is the default value.
        - ``ALL`` turns on statistics and displays all statistics for each measurement.
        - ``VALUEMean`` turns on statistics and displays the value and the mean (µ) of each
          measurement.
        - ``MINMax`` turns on statistics and displays the min and max of each measurement.
        - ``MEANSTDdev`` turns on statistics and displays the mean and standard deviation of each
          measurement.
    """


class MeasurementStatisticsCount(SCPICmdWrite):
    """The ``MEASUrement:STATIstics:COUNt`` command.

    Description:
        - This command (no query form) clears existing measurement statistics from memory. This
          command is equivalent to selecting Measurement Setup from the Measure menu, selecting
          Statistics, and clicking the Reset button.

    Usage:
        - Using the ``.write(value)`` method will send the ``MEASUrement:STATIstics:COUNt value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:STATIstics:COUNt {RESET}
        ```

    Info:
        - ``RESET`` clears existing measurement statistics from memory.
    """


class MeasurementStatistics(SCPICmdRead):
    """The ``MEASUrement:STATIstics`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:STATIstics?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.count``: The ``MEASUrement:STATIstics:COUNt`` command.
        - ``.mode``: The ``MEASUrement:STATIstics:MODe`` command.
        - ``.weighting``: The ``MEASUrement:STATIstics:WEIghting`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = MeasurementStatisticsCount(device, f"{self._cmd_syntax}:COUNt")
        self._mode = MeasurementStatisticsMode(device, f"{self._cmd_syntax}:MODe")
        self._weighting = MeasurementStatisticsWeighting(device, f"{self._cmd_syntax}:WEIghting")

    @property
    def count(self) -> MeasurementStatisticsCount:
        """Return the ``MEASUrement:STATIstics:COUNt`` command.

        Description:
            - This command (no query form) clears existing measurement statistics from memory. This
              command is equivalent to selecting Measurement Setup from the Measure menu, selecting
              Statistics, and clicking the Reset button.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:STATIstics:COUNt value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:STATIstics:COUNt {RESET}
            ```

        Info:
            - ``RESET`` clears existing measurement statistics from memory.
        """
        return self._count

    @property
    def mode(self) -> MeasurementStatisticsMode:
        """Return the ``MEASUrement:STATIstics:MODe`` command.

        Description:
            - This command controls the operation and display of measurement statistics. This
              command is equivalent to selecting Measurement Setup from the Measure menu, clicking
              the Statistics button and then choosing the desired Measurement Format.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:STATIstics:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics:MODe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:STATIstics:MODe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:STATIstics:MODe {OFF|ALL|VALUEMean|MINMax|MEANSTDdev}
            - MEASUrement:STATIstics:MODe?
            ```

        Info:
            - ``OFF`` turns off all measurements. This is the default value.
            - ``ALL`` turns on statistics and displays all statistics for each measurement.
            - ``VALUEMean`` turns on statistics and displays the value and the mean (µ) of each
              measurement.
            - ``MINMax`` turns on statistics and displays the min and max of each measurement.
            - ``MEANSTDdev`` turns on statistics and displays the mean and standard deviation of
              each measurement.
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


class MeasurementSource1Sigtype(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:SOUrce1:SIGType`` command.

    Description:
        - This command sets or queries the type of input signal used for measurement SOURCE<x>, 1 or
          2. To ensure accurate measurements, use this command to specify the input-signal type for
          the measurement source.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SOUrce1:SIGType?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SOUrce1:SIGType?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:SOUrce1:SIGType value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:SOUrce1:SIGType {PULse|EYE}
        - MEASUrement:SOUrce1:SIGType?
        ```

    Info:
        - ``PULSE`` is for generic signals that are not associated with synchronous communications
          standards.
        - ``EYE`` is for synchronous-communication signals with NRZ-like characteristics (nonreturn
          to zero).
    """


class MeasurementSource1(SCPICmdRead):
    """The ``MEASUrement:SOUrce1`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SOUrce1?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.sigtype``: The ``MEASUrement:SOUrce1:SIGType`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sigtype = MeasurementSource1Sigtype(device, f"{self._cmd_syntax}:SIGType")

    @property
    def sigtype(self) -> MeasurementSource1Sigtype:
        """Return the ``MEASUrement:SOUrce1:SIGType`` command.

        Description:
            - This command sets or queries the type of input signal used for measurement SOURCE<x>,
              1 or 2. To ensure accurate measurements, use this command to specify the input-signal
              type for the measurement source.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SOUrce1:SIGType?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SOUrce1:SIGType?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:SOUrce1:SIGType value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:SOUrce1:SIGType {PULse|EYE}
            - MEASUrement:SOUrce1:SIGType?
            ```

        Info:
            - ``PULSE`` is for generic signals that are not associated with synchronous
              communications standards.
            - ``EYE`` is for synchronous-communication signals with NRZ-like characteristics
              (nonreturn to zero).
        """
        return self._sigtype


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
        - ``.mid``: The ``MEASUrement:REFLevel:PERCent:MID<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = MeasurementReflevelPercentHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = MeasurementReflevelPercentLow(device, f"{self._cmd_syntax}:LOW")
        self._mid: Dict[int, MeasurementReflevelPercentMidItem] = DefaultDictPassKeyToFactory(
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
    def mid(self) -> Dict[int, MeasurementReflevelPercentMidItem]:
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
        return self._mid


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
        - ``.mid``: The ``MEASUrement:REFLevel:ABSolute:MID<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = MeasurementReflevelAbsoluteHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = MeasurementReflevelAbsoluteLow(device, f"{self._cmd_syntax}:LOW")
        self._mid: Dict[int, MeasurementReflevelAbsoluteMidItem] = DefaultDictPassKeyToFactory(
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
    def mid(self) -> Dict[int, MeasurementReflevelAbsoluteMidItem]:
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
        return self._mid


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
            - ``.mid``: The ``MEASUrement:REFLevel:ABSolute:MID<x>`` command.
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
            - ``.mid``: The ``MEASUrement:REFLevel:PERCent:MID<x>`` command.
        """
        return self._percent


class MeasurementNoise(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:NOISe`` command.

    Description:
        - This command sets or queries whether the noise measurement is made on the high or low
          level of the waveform. Sending this command is equivalent to selecting Ref Levs > Eye >
          Top Level or Base Level in the Comm tab of the Measurement Setup dialog box. The Eye
          section is displayed only if you have an eye-pattern or optical measurement defined.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:NOISe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:NOISe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:NOISe value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:NOISe {HIGH|LOW}
        - MEASUrement:NOISe?
        ```

    Info:
        - ``HIGH`` argument causes the measurement for noise to be taken at the high level of the
          waveform.
        - ``LOW`` argument causes the measurement for noise to be taken at the low level of the
          waveform.
    """


class MeasurementMethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:METHod`` command.

    Description:
        - This command sets or queries the method used to calculate the 0% and 100% reference level.
          This command is equivalent to selecting Reference Levels from the Measure menu and then
          choosing the desired Determine Base, Top From setting.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:METHod?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:METHod?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:METHod value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:METHod {HIStogram|MEAN|MINMax}
        - MEASUrement:METHod?
        ```

    Info:
        - ``HIStogram`` sets the high and low reference levels to the most common values either
          above or below the mid point, depending on whether the high reference point or the low
          reference point is being defined. Because the statistical approach ignores short-term
          aberrations, such as overshoot or ringing, the histogram method is the best setting for
          examining pulses.
        - ``MEAN`` sets the high and low reference levels to the mean values using all values either
          above or below the midpoint, depending on whether it is defining the high or low reference
          level. The selection is best used for examining eye patterns.
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
        - This command sets or queries the measurement type defined for the specified measurement
          slot. The measurement slot is specified by x, which ranges from 1 through 8. This command
          is equivalent to selecting Measurement Setup from the Measure menu and then choosing the
          desired measurement type.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|DISTDUty|EXTINCTDB|EXTINCTPCT|EXTINCTRATIO|EYEHeight|EYEWIdth|FALL|FREQuency|HIGH|HITs|LOW|MAXimum|MEAN|MEDian|MINImum|NCROss|NDUty|NOVershoot|NWIdth|PBASe|PCROss|PCTCROss|PDUty|PEAKHits|PERIod|PHAse|PK2Pk|PKPKJitter|PKPKNoise|POVershoot|PTOP|PWIdth|QFACtor|RISe|RMS|RMSJitter|RMSNoise|SIGMA1|SIGMA2|SIGMA3|SIXSigmajit|SNRatio|STDdev|UNDEFINED|WAVEFORMS}
        - MEASUrement:MEAS<x>:TYPe?
        ```

    Info:
        - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it measures
          the high value less the low value measured over the entire waveform or gated region.
        - ``Amplitude = High - Low``
        - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
          region and is measured in volt-seconds. The area measured above the ground is positive,
          while the area below ground is negative.
        - ``BURst`` measures the duration of a burst. The measurement is made over the entire
          waveform or gated region.
        - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures in
          volt-seconds, the area over the first cycle in the waveform or the first cycle in the
          gated region. The area measured above the common reference point is positive, while the
          area below the common reference point is negative.
        - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the waveform
          or the first cycle in the gated region.
        - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle in
          the waveform or the first cycle in the gated region.
        - ``DELay`` measures the time between the middle reference (default = 50%) amplitude point
          of the source waveform and the destination waveform.
        - ``DISTDUty`` (duty cycle distortion) measures the time between the falling edge and the
          rising edge of the eye pattern at the mid reference level. It is the peak-to-peak time
          variation of the first eye crossing measured at the mid-reference as a percent of the eye
          period.
        - ``EXTINCTDB`` measures the extinction ratio of an optical waveform (eye diagram).
          Extinction Ratio (dB) measures the ratio of the average power levels for the logic High to
          the logic Low of an optical waveform and expresses the result in dB. This measurement only
          works for fast acquisition signals or a reference waveform saved in fast acquisition mode.
        - ``Extinction dB = 10 × (log 10 (High / Low)``
        - ``EXTINCTPCT`` measures the extinction ratio of the selected optical waveform. Extinction
          Ratio (%) measures the ratio of the average power levels for the logic Low (off) to the
          logic (High) (on) of an optical waveform and expresses the result in percent. This
          measurement only works for fast acquisition signals or a reference waveform saved in fast
          acquisition mode.
        - ``Extinction % = 100.0 × (Low / High)``
        - ``EXTINCTRATIO`` measures the extinction ratio of the selected optical waveform.
          Extinction Ratio measures the ratio of the average power levels for the logic High to the
          logic Low of an optical waveform and expresses the result without units. This measurement
          only works for fast acquisition signals or a reference waveform saved in fast acquisition
          mode. Extinction ratios greater than 100 or less than 1 generate errors; low must be
          greater than or equal to 1 µW.
        - ``Extinction Ratio = (High / Low)``
        - ``EYEHeight`` measures the vertical opening of an eye diagram in volts.
        - ``EYEWidth`` measures the width of an eye diagram in seconds.
        - ``FALL`` measures the time taken for the falling edge of the first pulse in the waveform
          or gated region to fall from a high reference value (default is 90%) to a low reference
          value (default is 10%).
        - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is the
          reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per second.
        - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a waveform.
        - ``HITs`` (histogram hits) measures the number of points in or on the histogram box.
        - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a waveform.
        - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
          found. It is measured over the entire waveform or gated region. When histogram is selected
          with the ``MEASUREMENT:METHOD`` command, the maximum measurement measures the voltage of
          the highest nonzero bin in vertical histograms or the time of the right-most bin in
          horizontal histograms.
        - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or gated
          region. When histogram is selected with the ``MEASUREMENT:METHOD`` command, the mean
          measurement measures the average of all acquired points within or on the histogram.
        - ``MEDian`` (histogram measurement) measures the middle point of the histogram box. Half of
          all acquired points within or on the histogram box are less than this value and half are
          greater than this value.
        - ``MINImum`` finds the minimum amplitude. This value is typically the most negative peak
          voltage. It is measured over the entire waveform or gated region. When histogram is
          selected with the ``MEASUREMENT:METHOD`` command, the minimum measurement measures the
          lowest nonzero bin in vertical histograms or the time of the left-most nonzero bin in the
          horizontal histograms.
        - ``NCROss`` (timing measurement) measures the time from the trigger point to the first
          falling edge of the waveform or gated region. The distance (time) is measured at the
          middle reference amplitude point of the signal.
        - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
          period, expressed as a percentage. The duty cycle is measured on the first cycle in the
          waveform or gated region.
        - ``Negative Duty Cycle = (Negative Width) / Period × 100%``
        - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
          waveform or gated region.
        - ``Negative Overshoot = (Low - Minimum) / Amplitude × 100%)``
        - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
          reference (default = 50%) amplitude points of a negative pulse. The measurement is made on
          the first pulse in the waveform or gated region.
        - ``PBASe`` measures the base value used in extinction ratio measurements.
        - ``PCROss`` (timing measurement) measures the time from the trigger point to the first
          positive edge of the waveform or gated region. The distance (time) is measured at the
          middle reference amplitude point of the signal.
        - ``PCTCROss`` measures the location of the eye crossing point expressed as a percentage of
          EYEHeight.
        - ``Crossing percent = 100 ×[(eye-crossing-point - PBASe)/(PTOP - PBASe)]``
        - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
          period, expressed as a percentage. It is measured on the first cycle in the waveform or
          gated region.
        - ``Positive Duty Cycle = (Positive Width)/Period × 100%``
        - ``PEAKHits`` measures the number of points in the largest bin of the histogram.
        - ``PERIod`` is the time required to complete the first cycle in a waveform or gated region.
          Period is the reciprocal of frequency and is measured in seconds.
        - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
          reference waveform) between two waveforms. The measurement is made between the middle
          reference points of the two waveforms and is expressed in degrees, where 360° represents
          one waveform cycle.
        - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
          amplitude in the entire waveform or gated region. When histogram is selected with the
          ``MEASUREMENT:METHOD`` command, the PK2Pk measurement measures the histogram peak to peak
          difference.
        - ``PKPKJitter`` measures the variance (minimum and maximum values) in the time locations of
          the cross point.
        - ``PKPKNoise`` measures the peak-to-peak noise on a waveform at the mid reference level.
        - ``POVershoot``
        - ``Positive Overshoot = (Maximum - High) / Amplitude ×100%``
        - ``PTOT`` measures the top value used in extinction ratio measurements.
        - ``PWIdth`` (positive width) is the distance (time) between the middle reference (default =
          50%) amplitude points of a positive pulse. The measurement is made on the first pulse in
          the waveform or gated region.
        - ``QFACtor`` measures the quality factor. The Q factor is a figure of merit for an eye
          diagram, which indicates the vertical eye opening relative to the noise at the low and
          high logic levels. It is the ratio of the eye size to noise.
        - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the time
          it takes for the leading edge of the first pulse encountered to rise from a low reference
          value (default is 10%) to a high reference value (default is 90%).
        - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
          waveform or gated region.
        - ``RMSJitter`` measures the variance in the time locations of the cross point. The RMS
          jitter is defined as one standard deviation at the cross point.
        - ``RMSNoise`` measures the Root Mean Square noise amplitude on a waveform at the mid
          reference level.
        - ``SIGMA1`` (histogram measurement) measures the percentage of points in the histogram that
          are within one standard deviation of the histogram mean.
        - ``SIGMA2`` (histogram measurement) measures the percentage of points in the histogram that
          are within two standard deviations of the histogram mean.
        - ``SIGMA3`` (histogram measurement) measures the percentage of points in the histogram that
          are within three standard deviations of the histogram mean.
        - ``SIXSigmajit`` (histogram measurement) is six × RMSJitter.
        - ``SNRatio`` measures the signal-to-noise ratio. The signal-to-noise ratio is the amplitude
          of a noise rejection band centered on the mid level.
        - ``STDdev`` measures the standard deviation (Root Mean Square (RMS) deviation) of all
          acquired points within or on the histogram box.
        - ``UNDEFINED`` is the default measurement type, which indicates that no measurement type is
          specified. Once a measurement type is chosen, it can be cleared using this argument.
        - ``WAVEFORMS`` (waveform count) measures the number of waveforms used to calculate the
          histogram.
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


class MeasurementMeasItemSource1Sigtype(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:SOUrce1:SIGType`` command.

    Description:
        - This command sets or queries the type of input signal used for the specified measurement
          slot. MEAS<x> is 1 through 8 for the measurement slot using SOURCE<x>, 1 or 2. To ensure
          accurate measurements, use this command to specify the input-signal type for the
          measurement source.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOUrce1:SIGType?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1:SIGType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:SOUrce1:SIGType value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:SOUrce1:SIGType {PULse|EYE}
        - MEASUrement:MEAS<x>:SOUrce1:SIGType?
        ```

    Info:
        - ``PULSE`` is for generic signals that are not associated with synchronous communications
          standards.
        - ``EYE`` is for synchronous-communication signals with NRZ-like characteristics (nonreturn
          to zero).
    """


class MeasurementMeasItemSource1(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:SOUrce1`` command.

    Description:
        - This command sets or queries the source for all single channel measurements and specifies
          the reference source to measure 'to' when taking a delay measurement or phase measurement.
          Measurements are specified by x, which ranges from 1 through 8. This command is equivalent
          to selecting Measurement Setup from the Measure menu, selecting a measurement type of
          either Phase or Delay, and then choosing the desired measurement source. Tip: Source2
          measurements apply only to phase and delay measurement types, which require both a target
          (Source1) and reference (Source2) source.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1 value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|MATH<y>|REF<x>|HIStogram}
        - MEASUrement:MEAS<x>:SOUrce1?
        ```

    Info:
        - ``CH<x>`` is an input channel waveform. The x variable can be expressed as an integer
          ranging from 1 through 4.
        - ``MATH<y>`` is a math waveform. The y variable can be expressed as an integer ranging from
          1 through 4.
        - ``REF<x>`` is a reference waveform. The x variable can be expressed as an integer ranging
          from 1 through 4.
        - ``HIStogram`` is a histogram. Histogram is valid only for source 1.

    Properties:
        - ``.sigtype``: The ``MEASUrement:MEAS<x>:SOUrce1:SIGType`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sigtype = MeasurementMeasItemSource1Sigtype(device, f"{self._cmd_syntax}:SIGType")

    @property
    def sigtype(self) -> MeasurementMeasItemSource1Sigtype:
        """Return the ``MEASUrement:MEAS<x>:SOUrce1:SIGType`` command.

        Description:
            - This command sets or queries the type of input signal used for the specified
              measurement slot. MEAS<x> is 1 through 8 for the measurement slot using SOURCE<x>, 1
              or 2. To ensure accurate measurements, use this command to specify the input-signal
              type for the measurement source.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOUrce1:SIGType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:SOUrce1:SIGType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:SOUrce1:SIGType value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:SOUrce1:SIGType {PULse|EYE}
            - MEASUrement:MEAS<x>:SOUrce1:SIGType?
            ```

        Info:
            - ``PULSE`` is for generic signals that are not associated with synchronous
              communications standards.
            - ``EYE`` is for synchronous-communication signals with NRZ-like characteristics
              (nonreturn to zero).
        """
        return self._sigtype


class MeasurementMeasItemReflevelPercentMidItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x>`` command.

    Description:
        - This command sets or queries the percentage (where 100% is equal to HIGH) used to
          calculate the mid reference level for the second waveform specified when
          ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set to Percent. Mid1 specifies the 'from'
          waveform and Mid2 specifies the 'to' waveform for delay measurements. Measurements are
          specified by x, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x> value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x> <NR3>
        - MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x>?
        ```

    Info:
        - ``<NR3>`` is the mid reference level, ranging from 0 to 100%. The default mid reference
          level is 50%.
    """


class MeasurementMeasItemReflevelPercentLow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevel:PERCent:LOW`` command.

    Description:
        - This command sets or queries the percentage (where 100% is equal to HIGH) used to
          calculate the low reference level when ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set to
          Percent. This command is equivalent to selecting Reference Levels from the Measure menu,
          and then entering the Percentage Low Ref value. Measurements are specified by x, which
          ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevel:PERCent:LOW?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:PERCent:LOW?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:PERCent:LOW value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevel:PERCent:LOW <NR3>
        - MEASUrement:MEAS<x>:REFLevel:PERCent:LOW?
        ```

    Info:
        - ``<NR3>`` is the low reference level, ranging from 0 to 100%. The default low reference
          level is 10%.
    """


class MeasurementMeasItemReflevelPercentHigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH`` command.

    Description:
        - This command sets or queries the percentage (where 100% is equal to HIGH) used to
          calculate the high reference level when ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set to
          Percent. Measurements are specified by x, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH <NR3>
        - MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH?
        ```

    Info:
        - ``<NR3>`` is the high reference level, ranging from 0 to 100%. The default high reference
          level is 90%.
    """


class MeasurementMeasItemReflevelPercent(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevel:PERCent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevel:PERCent?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:PERCent?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.high``: The ``MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH`` command.
        - ``.low``: The ``MEASUrement:MEAS<x>:REFLevel:PERCent:LOW`` command.
        - ``.mid``: The ``MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = MeasurementMeasItemReflevelPercentHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = MeasurementMeasItemReflevelPercentLow(device, f"{self._cmd_syntax}:LOW")
        self._mid: Dict[int, MeasurementMeasItemReflevelPercentMidItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: MeasurementMeasItemReflevelPercentMidItem(
                    device, f"{self._cmd_syntax}:MID{x}"
                )
            )
        )

    @property
    def high(self) -> MeasurementMeasItemReflevelPercentHigh:
        """Return the ``MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH`` command.

        Description:
            - This command sets or queries the percentage (where 100% is equal to HIGH) used to
              calculate the high reference level when ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set
              to Percent. Measurements are specified by x, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH <NR3>
            - MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH?
            ```

        Info:
            - ``<NR3>`` is the high reference level, ranging from 0 to 100%. The default high
              reference level is 90%.
        """
        return self._high

    @property
    def low(self) -> MeasurementMeasItemReflevelPercentLow:
        """Return the ``MEASUrement:MEAS<x>:REFLevel:PERCent:LOW`` command.

        Description:
            - This command sets or queries the percentage (where 100% is equal to HIGH) used to
              calculate the low reference level when ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set to
              Percent. This command is equivalent to selecting Reference Levels from the Measure
              menu, and then entering the Percentage Low Ref value. Measurements are specified by x,
              which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent:LOW?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent:LOW?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent:LOW value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevel:PERCent:LOW <NR3>
            - MEASUrement:MEAS<x>:REFLevel:PERCent:LOW?
            ```

        Info:
            - ``<NR3>`` is the low reference level, ranging from 0 to 100%. The default low
              reference level is 10%.
        """
        return self._low

    @property
    def mid(self) -> Dict[int, MeasurementMeasItemReflevelPercentMidItem]:
        """Return the ``MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x>`` command.

        Description:
            - This command sets or queries the percentage (where 100% is equal to HIGH) used to
              calculate the mid reference level for the second waveform specified when
              ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set to Percent. Mid1 specifies the 'from'
              waveform and Mid2 specifies the 'to' waveform for delay measurements. Measurements are
              specified by x, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x> value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x> <NR3>
            - MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x>?
            ```

        Info:
            - ``<NR3>`` is the mid reference level, ranging from 0 to 100%. The default mid
              reference level is 50%.
        """
        return self._mid


class MeasurementMeasItemReflevelMethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevel:METHod`` command.

    Description:
        - This command specifies or queries the reference level units used for measurement
          calculations. This command is equivalent to selecting Reference Levels from the Measure
          menu and then choosing the desired reference level from the Units group box. Measurements
          are specified by x, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevel:METHod?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:REFLevel:METHod?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:METHod value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevel:METHod {ABSolute|PERCent}
        - MEASUrement:MEAS<x>:REFLevel:METHod?
        ```

    Info:
        - ``ABSolute`` specifies that the reference levels are set explicitly using the
          ``MEASUrement:MEAS<x>:REFLevel:ABSolute`` commands. This method is useful when precise
          values are required (for example, when designing to published interface specifications,
          such as RS-232-C.
        - ``PERCent`` specifies that the reference levels are calculated as a percent relative to
          HIGH and LOW. The percentages are defined using the
          ``MEASUrement:MEAS<x>:REFLevel:PERCent`` commands.
    """


class MeasurementMeasItemReflevelAbsoluteMidItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x>`` command.

    Description:
        - This command sets or queries the mid reference level for the 'to' waveform when taking a
          delay measurement, and is the 50% reference level when
          ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set to Absolute. Mid1 sets the 'from' waveform
          and Mid2 sets the 'to' waveform when taking a delay measurement. Measurements are
          specified by x, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x> value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x> <NR3>
        - MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x>?
        ```

    Info:
        - ``<NR3>`` is the mid reference level in volts. The default is 0.0 V.
    """


class MeasurementMeasItemReflevelAbsoluteLow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW`` command.

    Description:
        - This command sets or queries the low reference level, and is the lower reference level
          when ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set to Absolute. Measurements are specified
          by x, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW <NR3>
        - MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW?
        ```

    Info:
        - ``<NR3>`` is the low reference level in volts. The default is 0.0 V.
    """


class MeasurementMeasItemReflevelAbsoluteHigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH`` command.

    Description:
        - This command sets or queries the high reference level, and is the upper reference level
          when ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set to Absolute. Measurements are specified
          by x, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH <NR3>
        - MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH?
        ```

    Info:
        - ``<NR3>`` is the high reference level in volts. The default is 0.0 V.
    """


class MeasurementMeasItemReflevelAbsolute(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevel:ABSolute`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevel:ABSolute?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:MEAS<x>:REFLevel:ABSolute?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.high``: The ``MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH`` command.
        - ``.low``: The ``MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW`` command.
        - ``.mid``: The ``MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = MeasurementMeasItemReflevelAbsoluteHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = MeasurementMeasItemReflevelAbsoluteLow(device, f"{self._cmd_syntax}:LOW")
        self._mid: Dict[int, MeasurementMeasItemReflevelAbsoluteMidItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: MeasurementMeasItemReflevelAbsoluteMidItem(
                    device, f"{self._cmd_syntax}:MID{x}"
                )
            )
        )

    @property
    def high(self) -> MeasurementMeasItemReflevelAbsoluteHigh:
        """Return the ``MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH`` command.

        Description:
            - This command sets or queries the high reference level, and is the upper reference
              level when ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set to Absolute. Measurements are
              specified by x, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH <NR3>
            - MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH?
            ```

        Info:
            - ``<NR3>`` is the high reference level in volts. The default is 0.0 V.
        """
        return self._high

    @property
    def low(self) -> MeasurementMeasItemReflevelAbsoluteLow:
        """Return the ``MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW`` command.

        Description:
            - This command sets or queries the low reference level, and is the lower reference level
              when ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set to Absolute. Measurements are
              specified by x, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW <NR3>
            - MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW?
            ```

        Info:
            - ``<NR3>`` is the low reference level in volts. The default is 0.0 V.
        """
        return self._low

    @property
    def mid(self) -> Dict[int, MeasurementMeasItemReflevelAbsoluteMidItem]:
        """Return the ``MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x>`` command.

        Description:
            - This command sets or queries the mid reference level for the 'to' waveform when taking
              a delay measurement, and is the 50% reference level when
              ``MEASUREMENT:MEASX:REFLEVEL:METHOD`` is set to Absolute. Mid1 sets the 'from'
              waveform and Mid2 sets the 'to' waveform when taking a delay measurement. Measurements
              are specified by x, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x> value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x> <NR3>
            - MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x>?
            ```

        Info:
            - ``<NR3>`` is the mid reference level in volts. The default is 0.0 V.
        """
        return self._mid


class MeasurementMeasItemReflevel(SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:REFLevel`` command.

    Description:
        - This query-only command returns the current reference level parameters. It returns them in
          the following order: ABSOLUTE and then PERCENT for individual user measurements.
          Measurements are specified by x, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:REFLevel?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:REFLevel?
        ```

    Properties:
        - ``.absolute``: The ``MEASUrement:MEAS<x>:REFLevel:ABSolute`` command tree.
        - ``.method``: The ``MEASUrement:MEAS<x>:REFLevel:METHod`` command.
        - ``.percent``: The ``MEASUrement:MEAS<x>:REFLevel:PERCent`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = MeasurementMeasItemReflevelAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._method = MeasurementMeasItemReflevelMethod(device, f"{self._cmd_syntax}:METHod")
        self._percent = MeasurementMeasItemReflevelPercent(device, f"{self._cmd_syntax}:PERCent")

    @property
    def absolute(self) -> MeasurementMeasItemReflevelAbsolute:
        """Return the ``MEASUrement:MEAS<x>:REFLevel:ABSolute`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevel:ABSolute?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``MEASUrement:MEAS<x>:REFLevel:ABSolute:HIGH`` command.
            - ``.low``: The ``MEASUrement:MEAS<x>:REFLevel:ABSolute:LOW`` command.
            - ``.mid``: The ``MEASUrement:MEAS<x>:REFLevel:ABSolute:MID<x>`` command.
        """
        return self._absolute

    @property
    def method(self) -> MeasurementMeasItemReflevelMethod:
        """Return the ``MEASUrement:MEAS<x>:REFLevel:METHod`` command.

        Description:
            - This command specifies or queries the reference level units used for measurement
              calculations. This command is equivalent to selecting Reference Levels from the
              Measure menu and then choosing the desired reference level from the Units group box.
              Measurements are specified by x, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevel:METHod?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:METHod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:METHod value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevel:METHod {ABSolute|PERCent}
            - MEASUrement:MEAS<x>:REFLevel:METHod?
            ```

        Info:
            - ``ABSolute`` specifies that the reference levels are set explicitly using the
              ``MEASUrement:MEAS<x>:REFLevel:ABSolute`` commands. This method is useful when precise
              values are required (for example, when designing to published interface
              specifications, such as RS-232-C.
            - ``PERCent`` specifies that the reference levels are calculated as a percent relative
              to HIGH and LOW. The percentages are defined using the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent`` commands.
        """
        return self._method

    @property
    def percent(self) -> MeasurementMeasItemReflevelPercent:
        """Return the ``MEASUrement:MEAS<x>:REFLevel:PERCent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevel:PERCent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:REFLevel:PERCent?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``MEASUrement:MEAS<x>:REFLevel:PERCent:HIGH`` command.
            - ``.low``: The ``MEASUrement:MEAS<x>:REFLevel:PERCent:LOW`` command.
            - ``.mid``: The ``MEASUrement:MEAS<x>:REFLevel:PERCent:MID<x>`` command.
        """
        return self._percent


class MeasurementMeasItemNoise(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:NOISe`` command.

    Description:
        - This command sets or queries whether the noise measurement is made on the high or low
          level of the waveform. Sending this command is equivalent to selecting Ref Levs > Eye >
          Top Level or Base Level in the Comm tab of the Measurement Setup dialog box. The Eye
          section is displayed only if you have an eye-pattern or optical measurement defined.
          Measurements are specified by x, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:NOISe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:NOISe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:NOISe value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:NOISe {HIGH|LOW}
        - MEASUrement:MEAS<x>:NOISe?
        ```

    Info:
        - ``HIGH`` argument causes the measurement for noise to be taken at the high level of the
          waveform.
        - ``LOW`` argument causes the measurement for noise to be taken at the low level of the
          waveform.
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


class MeasurementMeasItemMethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:METHod`` command.

    Description:
        - This command specifies or queries the method used to calculate the 0% and 100% reference
          level.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:METHod?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:METHod?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:METHod value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:METHod {HIStogram|MINMax|MEAN}
        - MEASUrement:MEAS<x>:METHod?
        ```

    Info:
        - ``HIStogram`` sets the high and low waveform levels statistically using a histogram
          algorithm.
        - ``MINMax`` sets the high and low waveform levels to MAX and MIN, respectively.
        - ``MEAN`` sets the high and low waveform levels to their mean.
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
    """The ``MEASUrement:MEAS<x>:DELay:DIREction`` command.

    Description:
        - This command sets or queries the starting point and direction that determines the delay
          'to' edge when taking a delay measurement. Use the ``MEASUREMENT:MEASX:SOURCEX`` command
          to specify the waveform. This command is equivalent to selecting Time from the Measure
          menu, choosing Delay from the drop-down list and then clicking the desired Search
          Direction setting. Measurements are specified by x, which ranges from 1 through 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay:DIREction?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:DELay:DIREction?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:MEAS<x>:DELay:DIREction value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:DELay:DIREction {BACKWards|FORWards}
        - MEASUrement:MEAS<x>:DELay:DIREction?
        ```

    Info:
        - ``BACKWards`` means that the search starts at the end of the waveform and looks for the
          last rising or falling edge in the waveform. Use the ``MEASUREMENT:MEASX:DELAY:EDGEX``
          command to specify the slope of the edge.
        - ``FORWards`` means that the search starts at the beginning of the waveform and looks for
          the first rising or falling edge in the waveform. Use the
          ``MEASUREMENT:MEASX:DELAY:EDGEX`` command to specify the slope of the edge.
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
        - ``.direction``: The ``MEASUrement:MEAS<x>:DELay:DIREction`` command.
        - ``.edge``: The ``MEASUrement:MEAS<x>:DELay:EDGE<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = MeasurementMeasItemDelayDirection(device, f"{self._cmd_syntax}:DIREction")
        self._edge: Dict[int, MeasurementMeasItemDelayEdgeItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementMeasItemDelayEdgeItem(device, f"{self._cmd_syntax}:EDGE{x}")
        )

    @property
    def direction(self) -> MeasurementMeasItemDelayDirection:
        """Return the ``MEASUrement:MEAS<x>:DELay:DIREction`` command.

        Description:
            - This command sets or queries the starting point and direction that determines the
              delay 'to' edge when taking a delay measurement. Use the ``MEASUREMENT:MEASX:SOURCEX``
              command to specify the waveform. This command is equivalent to selecting Time from the
              Measure menu, choosing Delay from the drop-down list and then clicking the desired
              Search Direction setting. Measurements are specified by x, which ranges from 1 through
              8.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:DELay:DIREction?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:MEAS<x>:DELay:DIREction?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:MEAS<x>:DELay:DIREction value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:DELay:DIREction {BACKWards|FORWards}
            - MEASUrement:MEAS<x>:DELay:DIREction?
            ```

        Info:
            - ``BACKWards`` means that the search starts at the end of the waveform and looks for
              the last rising or falling edge in the waveform. Use the
              ``MEASUREMENT:MEASX:DELAY:EDGEX`` command to specify the slope of the edge.
            - ``FORWards`` means that the search starts at the beginning of the waveform and looks
              for the first rising or falling edge in the waveform. Use the
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
        - ``.method``: The ``MEASUrement:MEAS<x>:METHod`` command.
        - ``.minimum``: The ``MEASUrement:MEAS<x>:MINImum`` command.
        - ``.noise``: The ``MEASUrement:MEAS<x>:NOISe`` command.
        - ``.reflevel``: The ``MEASUrement:MEAS<x>:REFLevel`` command.
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
        self._method = MeasurementMeasItemMethod(device, f"{self._cmd_syntax}:METHod")
        self._minimum = MeasurementMeasItemMinimum(device, f"{self._cmd_syntax}:MINImum")
        self._noise = MeasurementMeasItemNoise(device, f"{self._cmd_syntax}:NOISe")
        self._reflevel = MeasurementMeasItemReflevel(device, f"{self._cmd_syntax}:REFLevel")
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
            - ``.direction``: The ``MEASUrement:MEAS<x>:DELay:DIREction`` command.
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
    def method(self) -> MeasurementMeasItemMethod:
        """Return the ``MEASUrement:MEAS<x>:METHod`` command.

        Description:
            - This command specifies or queries the method used to calculate the 0% and 100%
              reference level.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:METHod?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:METHod?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:METHod value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:METHod {HIStogram|MINMax|MEAN}
            - MEASUrement:MEAS<x>:METHod?
            ```

        Info:
            - ``HIStogram`` sets the high and low waveform levels statistically using a histogram
              algorithm.
            - ``MINMax`` sets the high and low waveform levels to MAX and MIN, respectively.
            - ``MEAN`` sets the high and low waveform levels to their mean.
        """
        return self._method

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
    def noise(self) -> MeasurementMeasItemNoise:
        """Return the ``MEASUrement:MEAS<x>:NOISe`` command.

        Description:
            - This command sets or queries whether the noise measurement is made on the high or low
              level of the waveform. Sending this command is equivalent to selecting Ref Levs > Eye
              > Top Level or Base Level in the Comm tab of the Measurement Setup dialog box. The Eye
              section is displayed only if you have an eye-pattern or optical measurement defined.
              Measurements are specified by x, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:NOISe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:NOISe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:NOISe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:NOISe {HIGH|LOW}
            - MEASUrement:MEAS<x>:NOISe?
            ```

        Info:
            - ``HIGH`` argument causes the measurement for noise to be taken at the high level of
              the waveform.
            - ``LOW`` argument causes the measurement for noise to be taken at the low level of the
              waveform.
        """
        return self._noise

    @property
    def reflevel(self) -> MeasurementMeasItemReflevel:
        """Return the ``MEASUrement:MEAS<x>:REFLevel`` command.

        Description:
            - This query-only command returns the current reference level parameters. It returns
              them in the following order: ABSOLUTE and then PERCENT for individual user
              measurements. Measurements are specified by x, which ranges from 1 through 8.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:REFLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:REFLevel?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:REFLevel?
            ```

        Sub-properties:
            - ``.absolute``: The ``MEASUrement:MEAS<x>:REFLevel:ABSolute`` command tree.
            - ``.method``: The ``MEASUrement:MEAS<x>:REFLevel:METHod`` command.
            - ``.percent``: The ``MEASUrement:MEAS<x>:REFLevel:PERCent`` command tree.
        """
        return self._reflevel

    @property
    def source1(self) -> MeasurementMeasItemSource1:
        """Return the ``MEASUrement:MEAS<x>:SOUrce1`` command.

        Description:
            - This command sets or queries the source for all single channel measurements and
              specifies the reference source to measure 'to' when taking a delay measurement or
              phase measurement. Measurements are specified by x, which ranges from 1 through 8.
              This command is equivalent to selecting Measurement Setup from the Measure menu,
              selecting a measurement type of either Phase or Delay, and then choosing the desired
              measurement source. Tip: Source2 measurements apply only to phase and delay
              measurement types, which require both a target (Source1) and reference (Source2)
              source.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|MATH<y>|REF<x>|HIStogram}
            - MEASUrement:MEAS<x>:SOUrce1?
            ```

        Info:
            - ``CH<x>`` is an input channel waveform. The x variable can be expressed as an integer
              ranging from 1 through 4.
            - ``MATH<y>`` is a math waveform. The y variable can be expressed as an integer ranging
              from 1 through 4.
            - ``REF<x>`` is a reference waveform. The x variable can be expressed as an integer
              ranging from 1 through 4.
            - ``HIStogram`` is a histogram. Histogram is valid only for source 1.

        Sub-properties:
            - ``.sigtype``: The ``MEASUrement:MEAS<x>:SOUrce1:SIGType`` command.
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
            - This command sets or queries the measurement type defined for the specified
              measurement slot. The measurement slot is specified by x, which ranges from 1 through
              8. This command is equivalent to selecting Measurement Setup from the Measure menu and
              then choosing the desired measurement type.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|DISTDUty|EXTINCTDB|EXTINCTPCT|EXTINCTRATIO|EYEHeight|EYEWIdth|FALL|FREQuency|HIGH|HITs|LOW|MAXimum|MEAN|MEDian|MINImum|NCROss|NDUty|NOVershoot|NWIdth|PBASe|PCROss|PCTCROss|PDUty|PEAKHits|PERIod|PHAse|PK2Pk|PKPKJitter|PKPKNoise|POVershoot|PTOP|PWIdth|QFACtor|RISe|RMS|RMSJitter|RMSNoise|SIGMA1|SIGMA2|SIGMA3|SIXSigmajit|SNRatio|STDdev|UNDEFINED|WAVEFORMS}
            - MEASUrement:MEAS<x>:TYPe?
            ```

        Info:
            - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it
              measures the high value less the low value measured over the entire waveform or gated
              region.
            - ``Amplitude = High - Low``
            - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
              region and is measured in volt-seconds. The area measured above the ground is
              positive, while the area below ground is negative.
            - ``BURst`` measures the duration of a burst. The measurement is made over the entire
              waveform or gated region.
            - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures in
              volt-seconds, the area over the first cycle in the waveform or the first cycle in the
              gated region. The area measured above the common reference point is positive, while
              the area below the common reference point is negative.
            - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the
              waveform or the first cycle in the gated region.
            - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle
              in the waveform or the first cycle in the gated region.
            - ``DELay`` measures the time between the middle reference (default = 50%) amplitude
              point of the source waveform and the destination waveform.
            - ``DISTDUty`` (duty cycle distortion) measures the time between the falling edge and
              the rising edge of the eye pattern at the mid reference level. It is the peak-to-peak
              time variation of the first eye crossing measured at the mid-reference as a percent of
              the eye period.
            - ``EXTINCTDB`` measures the extinction ratio of an optical waveform (eye diagram).
              Extinction Ratio (dB) measures the ratio of the average power levels for the logic
              High to the logic Low of an optical waveform and expresses the result in dB. This
              measurement only works for fast acquisition signals or a reference waveform saved in
              fast acquisition mode.
            - ``Extinction dB = 10 × (log 10 (High / Low)``
            - ``EXTINCTPCT`` measures the extinction ratio of the selected optical waveform.
              Extinction Ratio (%) measures the ratio of the average power levels for the logic Low
              (off) to the logic (High) (on) of an optical waveform and expresses the result in
              percent. This measurement only works for fast acquisition signals or a reference
              waveform saved in fast acquisition mode.
            - ``Extinction % = 100.0 × (Low / High)``
            - ``EXTINCTRATIO`` measures the extinction ratio of the selected optical waveform.
              Extinction Ratio measures the ratio of the average power levels for the logic High to
              the logic Low of an optical waveform and expresses the result without units. This
              measurement only works for fast acquisition signals or a reference waveform saved in
              fast acquisition mode. Extinction ratios greater than 100 or less than 1 generate
              errors; low must be greater than or equal to 1 µW.
            - ``Extinction Ratio = (High / Low)``
            - ``EYEHeight`` measures the vertical opening of an eye diagram in volts.
            - ``EYEWidth`` measures the width of an eye diagram in seconds.
            - ``FALL`` measures the time taken for the falling edge of the first pulse in the
              waveform or gated region to fall from a high reference value (default is 90%) to a low
              reference value (default is 10%).
            - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is
              the reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per
              second.
            - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a
              waveform.
            - ``HITs`` (histogram hits) measures the number of points in or on the histogram box.
            - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a
              waveform.
            - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
              found. It is measured over the entire waveform or gated region. When histogram is
              selected with the ``MEASUREMENT:METHOD`` command, the maximum measurement measures the
              voltage of the highest nonzero bin in vertical histograms or the time of the
              right-most bin in horizontal histograms.
            - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or
              gated region. When histogram is selected with the ``MEASUREMENT:METHOD`` command, the
              mean measurement measures the average of all acquired points within or on the
              histogram.
            - ``MEDian`` (histogram measurement) measures the middle point of the histogram box.
              Half of all acquired points within or on the histogram box are less than this value
              and half are greater than this value.
            - ``MINImum`` finds the minimum amplitude. This value is typically the most negative
              peak voltage. It is measured over the entire waveform or gated region. When histogram
              is selected with the ``MEASUREMENT:METHOD`` command, the minimum measurement measures
              the lowest nonzero bin in vertical histograms or the time of the left-most nonzero bin
              in the horizontal histograms.
            - ``NCROss`` (timing measurement) measures the time from the trigger point to the first
              falling edge of the waveform or gated region. The distance (time) is measured at the
              middle reference amplitude point of the signal.
            - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
              period, expressed as a percentage. The duty cycle is measured on the first cycle in
              the waveform or gated region.
            - ``Negative Duty Cycle = (Negative Width) / Period × 100%``
            - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
              waveform or gated region.
            - ``Negative Overshoot = (Low - Minimum) / Amplitude × 100%)``
            - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
              reference (default = 50%) amplitude points of a negative pulse. The measurement is
              made on the first pulse in the waveform or gated region.
            - ``PBASe`` measures the base value used in extinction ratio measurements.
            - ``PCROss`` (timing measurement) measures the time from the trigger point to the first
              positive edge of the waveform or gated region. The distance (time) is measured at the
              middle reference amplitude point of the signal.
            - ``PCTCROss`` measures the location of the eye crossing point expressed as a percentage
              of EYEHeight.
            - ``Crossing percent = 100 ×[(eye-crossing-point - PBASe)/(PTOP - PBASe)]``
            - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
              period, expressed as a percentage. It is measured on the first cycle in the waveform
              or gated region.
            - ``Positive Duty Cycle = (Positive Width)/Period × 100%``
            - ``PEAKHits`` measures the number of points in the largest bin of the histogram.
            - ``PERIod`` is the time required to complete the first cycle in a waveform or gated
              region. Period is the reciprocal of frequency and is measured in seconds.
            - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
              reference waveform) between two waveforms. The measurement is made between the middle
              reference points of the two waveforms and is expressed in degrees, where 360°
              represents one waveform cycle.
            - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
              amplitude in the entire waveform or gated region. When histogram is selected with the
              ``MEASUREMENT:METHOD`` command, the PK2Pk measurement measures the histogram peak to
              peak difference.
            - ``PKPKJitter`` measures the variance (minimum and maximum values) in the time
              locations of the cross point.
            - ``PKPKNoise`` measures the peak-to-peak noise on a waveform at the mid reference
              level.
            - ``POVershoot``
            - ``Positive Overshoot = (Maximum - High) / Amplitude ×100%``
            - ``PTOT`` measures the top value used in extinction ratio measurements.
            - ``PWIdth`` (positive width) is the distance (time) between the middle reference
              (default = 50%) amplitude points of a positive pulse. The measurement is made on the
              first pulse in the waveform or gated region.
            - ``QFACtor`` measures the quality factor. The Q factor is a figure of merit for an eye
              diagram, which indicates the vertical eye opening relative to the noise at the low and
              high logic levels. It is the ratio of the eye size to noise.
            - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the
              time it takes for the leading edge of the first pulse encountered to rise from a low
              reference value (default is 10%) to a high reference value (default is 90%).
            - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
              waveform or gated region.
            - ``RMSJitter`` measures the variance in the time locations of the cross point. The RMS
              jitter is defined as one standard deviation at the cross point.
            - ``RMSNoise`` measures the Root Mean Square noise amplitude on a waveform at the mid
              reference level.
            - ``SIGMA1`` (histogram measurement) measures the percentage of points in the histogram
              that are within one standard deviation of the histogram mean.
            - ``SIGMA2`` (histogram measurement) measures the percentage of points in the histogram
              that are within two standard deviations of the histogram mean.
            - ``SIGMA3`` (histogram measurement) measures the percentage of points in the histogram
              that are within three standard deviations of the histogram mean.
            - ``SIXSigmajit`` (histogram measurement) is six × RMSJitter.
            - ``SNRatio`` measures the signal-to-noise ratio. The signal-to-noise ratio is the
              amplitude of a noise rejection band centered on the mid level.
            - ``STDdev`` measures the standard deviation (Root Mean Square (RMS) deviation) of all
              acquired points within or on the histogram box.
            - ``UNDEFINED`` is the default measurement type, which indicates that no measurement
              type is specified. Once a measurement type is chosen, it can be cleared using this
              argument.
            - ``WAVEFORMS`` (waveform count) measures the number of waveforms used to calculate the
              histogram.
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
        - This command sets or queries the immediate measurement type. Immediate measurements and
          annotations are not displayed on the screen.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:TYPe value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|DISTDUty|EXTINCTDB|EXTINCTPCT|EXTINCTRATIO|EYEHeight|EYEWIdth|FALL|FREQuency|HIGH|HITs|LOW|MAXimum|MEAN|MEDian|MINImum|NCROss|NDUty|NOVershoot|NWIdth|PBASe|PCROss|PCTCROss|PDUty|PEAKHits|PERIod|PHAse|PK2Pk|PKPKJitter|PKPKNoise|POVershoot|PTOP|PWIdth|QFACtor|RISe|RMS|RMSJitter|RMSNoise|SIGMA1|SIGMA2|SIGMA3|SIXSigmajit|SNRatio|STDdev|UNDEFINED|WAVEFORMS}
        - MEASUrement:IMMed:TYPe?
        ```

    Info:
        - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it measures
          the high value less the low value measured over the entire waveform or gated region.
        - ``Amplitude = High - Low``
        - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
          region and is measured in volt-seconds. The area measured above the ground is positive,
          while the area below ground is negative.
        - ``BURst`` measures the duration of a burst. The measurement is made over the entire
          waveform or gated region.
        - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures in
          volt-seconds, the area over the first cycle in the waveform or the first cycle in the
          gated region. The area measured above the common reference point is positive, while the
          area below the common reference point is negative.
        - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the waveform
          or the first cycle in the gated region.
        - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle in
          the waveform or the first cycle in the gated region.
        - ``DELay`` measures the time between the middle reference (default = 50%) amplitude point
          of the source waveform and the destination waveform.
        - ``DISTDUty`` (duty cycle distortion) measures the time between the falling edge and the
          rising edge of the eye pattern at the mid reference level. It is the peak-to-peak time
          variation of the first eye crossing measured at the mid-reference as a percent of the eye
          period.
        - ``EXTINCTDB`` measures the extinction ratio of an optical waveform (eye diagram).
          Extinction Ratio (dB) measures the ratio of the average power levels for the logic High to
          the logic Low of an optical waveform and expresses the result in dB. This measurement only
          works for fast acquisition signals or a reference waveform saved in fast acquisition mode.
        - ``Extinction dB = 10 × (log 10 (High / Low)``
        - ``EXTINCTPCT`` measures the extinction ratio of the selected optical waveform. Extinction
          Ratio (%) measures the ratio of the average power levels for the logic Low (off) to the
          logic (High) (on) of an optical waveform and expresses the result in percent. This
          measurement only works for fast acquisition signals or a reference waveform saved in fast
          acquisition mode.
        - ``Extinction % = 100.0 × (Low / High)``
        - ``EXTINCTRATIO`` measures the extinction ratio of the selected optical waveform.
          Extinction Ratio measures the ratio of the average power levels for the logic High to the
          logic Low of an optical waveform and expresses the result without units. This measurement
          only works for fast acquisition signals or a reference waveform saved in fast acquisition
          mode. Extinction ratios greater than 100 or less than 1 generate errors; low must be
          greater than or equal to 1 µW.
        - ``Extinction Ratio = (High / Low)``
        - ``EYEHeight`` measures the vertical opening of an eye diagram in volts.
        - ``EYEWidth`` measures the width of an eye diagram in seconds.
        - ``FALL`` measures the time taken for the falling edge of the first pulse in the waveform
          or gated region to fall from a high reference value (default is 90%) to a low reference
          value (default is 10%).
        - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is the
          reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per second.
        - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a waveform.
        - ``HITs`` (histogram hits) measures the number of points in or on the histogram box.
        - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a waveform.
        - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
          found. It is measured over the entire waveform or gated region. When histogram is selected
          with the ``MEASUREMENT:METHOD`` command, the maximum measurement measures the voltage of
          the highest nonzero bin in vertical histograms or the time of the right-most bin in
          horizontal histograms.
        - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or gated
          region. When histogram is selected with the ``MEASUREMENT:METHOD`` command, the mean
          measurement measures the average of all acquired points within or on the histogram.
        - ``MEDian`` (histogram measurement) measures the middle point of the histogram box. Half of
          all acquired points within or on the histogram box are less than this value and half are
          greater than this value.
        - ``MINImum`` finds the minimum amplitude. This value is typically the most negative peak
          voltage. It is measured over the entire waveform or gated region. When histogram is
          selected with the ``MEASUREMENT:METHOD`` command, the minimum measurement measures the
          lowest nonzero bin in vertical histograms or the time of the left-most nonzero bin in the
          horizontal histograms.
        - ``NCROss`` (timing measurement) measures the time from the trigger point to the first
          falling edge of the waveform or gated region. The distance (time) is measured at the
          middle reference amplitude point of the signal.
        - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
          period, expressed as a percentage. The duty cycle is measured on the first cycle in the
          waveform or gated region.
        - ``Negative Duty Cycle = (Negative Width) / Period × 100%``
        - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
          waveform or gated region.
        - ``Negative Overshoot = (Low - Minimum) / Amplitude × 100%)``
        - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
          reference (default = 50%) amplitude points of a negative pulse. The measurement is made on
          the first pulse in the waveform or gated region.
        - ``PBASe`` measures the base value used in extinction ratio measurements.
        - ``PCROss`` (timing measurement) measures the time from the trigger point to the first
          positive edge of the waveform or gated region. The distance (time) is measured at the
          middle reference amplitude point of the signal.
        - ``PCTCROss`` measures the location of the eye crossing point expressed as a percentage of
          EYEHeight.
        - ``Crossing percent = 100 ×[(eye-crossing-point - PBASe)/(PTOP - PBASe)]``
        - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
          period, expressed as a percentage. It is measured on the first cycle in the waveform or
          gated region.
        - ``Positive Duty Cycle = (Positive Width)/Period × 100%``
        - ``PEAKHits`` measures the number of points in the largest bin of the histogram.
        - ``PERIod`` is the time required to complete the first cycle in a waveform or gated region.
          Period is the reciprocal of frequency and is measured in seconds.
        - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
          reference waveform) between two waveforms. The measurement is made between the middle
          reference points of the two waveforms and is expressed in degrees, where 360° represents
          one waveform cycle.
        - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
          amplitude in the entire waveform or gated region. When histogram is selected with the
          ``MEASUREMENT:METHOD`` command, the PK2Pk measurement measures the histogram peak to peak
          difference.
        - ``PKPKJitter`` measures the variance (minimum and maximum values) in the time locations of
          the cross point.
        - ``PKPKNoise`` measures the peak-to-peak noise on a waveform at the mid reference level.
        - ``POVershoot``
        - ``Positive Overshoot = (Maximum - High) / Amplitude ×100%``
        - ``PTOT`` measures the top value used in extinction ratio measurements.
        - ``PWIdth`` (positive width) is the distance (time) between the middle reference (default =
          50%) amplitude points of a positive pulse. The measurement is made on the first pulse in
          the waveform or gated region.
        - ``QFACtor`` measures the quality factor. The Q factor is a figure of merit for an eye
          diagram, which indicates the vertical eye opening relative to the noise at the low and
          high logic levels. It is the ratio of the eye size to noise.
        - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the time
          it takes for the leading edge of the first pulse encountered to rise from a low reference
          value (defaul t is 10%) to a high reference value (default is 90%).
        - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
          waveform or gated region.
        - ``RMSJitter`` measures the variance in the time locations of the cross point. The RMS
          jitter is defined as one standard deviation at the cross point.
        - ``RMSNoise`` measures the Root Mean Square noise amplitude on a waveform at the mid
          reference level.
        - ``SIGMA1`` (histogram measurement) measures the percentage of points in the histogram that
          are within one standard deviation of the histogram mean.
        - ``SIGMA2`` (histogram measurement) measures the percentage of points in the histogram that
          are within two standard deviations of the histogram mean.
        - ``SIGMA3`` (histogram measurement) measures the percentage of points in the histogram that
          are within three standard deviations of the histogram mean.
        - ``SIXSigmajit`` (histogram measurement) is six × RMSJitter.
        - ``SNRatio`` measures the signal-to-noise ratio. The signal-to-noise ratio is the amplitude
          of a noise rejection band centered on the mid level.
        - ``STDdev`` measures the standard deviation (Root Mean Square (RMS) deviation) of all
          acquired points within or on the histogram box.
        - ``UNDEFINED`` is the default measurement type, which indicates that no measurement type is
          specified. Once a measurement type is chosen, it can be cleared using this argument.
        - ``WAVEFORMS`` (waveform count) measures the number of waveforms used to calculate the
          histogram.
    """  # noqa: E501


class MeasurementImmedSource1Sigtype(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:SOUrce1:SIGType`` command.

    Description:
        - This command sets or queries the type of input signal used for measurement SOURCE<x>, 1 or
          2. To ensure accurate measurements, use this command to specify the input-signal type for
          the measurement source.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:SOUrce1:SIGType?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:SOUrce1:SIGType?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:IMMed:SOUrce1:SIGType value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:SOUrce1:SIGType {PULse|EYE}
        - MEASUrement:IMMed:SOUrce1:SIGType?
        ```

    Info:
        - ``PULSE`` is for generic signals that are not associated with synchronous communications
          standards.
        - ``EYE`` is for synchronous-communication signals with NRZ-like characteristics (nonreturn
          to zero).
    """


class MeasurementImmedSource1(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:SOUrce1`` command.

    Description:
        - This command sets or queries the source for phase or delay immediate measurements. This
          command is equivalent to selecting Measurement Setup from the Measure menu, choosing the
          Time tab, clicking the Delay button to display the delay settings and then clicking the
          desired Source1 (From) setting or Source2 (To) setting. Tip: Source2 measurements only
          apply to phase and delay measurement types, which require both a target (Source1) and
          reference (Source2) source.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:SOUrce1 value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:SOUrce1 {CH<x>|MATH<y>|REF<x>|HIStogram}
        - MEASUrement:IMMed:SOUrce1?
        ```

    Info:
        - ``CH<x>`` is an input channel waveform. The x variable can be expressed as an integer
          ranging from 1 through 4.
        - ``MATH<y>`` is a math waveform. The y variable can be expressed as an integer ranging from
          1 through 4.
        - ``REF<X>`` is a reference waveform. The x variable can be expressed as an integer ranging
          from 1 through 4.
        - ``HIStogram`` indicates histogram as the object to be measured. HIStogram not allowed on
          SOUrce2.

    Properties:
        - ``.sigtype``: The ``MEASUrement:IMMed:SOUrce1:SIGType`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sigtype = MeasurementImmedSource1Sigtype(device, f"{self._cmd_syntax}:SIGType")

    @property
    def sigtype(self) -> MeasurementImmedSource1Sigtype:
        """Return the ``MEASUrement:IMMed:SOUrce1:SIGType`` command.

        Description:
            - This command sets or queries the type of input signal used for measurement SOURCE<x>,
              1 or 2. To ensure accurate measurements, use this command to specify the input-signal
              type for the measurement source.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:SOUrce1:SIGType?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:SOUrce1:SIGType?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:SOUrce1:SIGType value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:SOUrce1:SIGType {PULse|EYE}
            - MEASUrement:IMMed:SOUrce1:SIGType?
            ```

        Info:
            - ``PULSE`` is for generic signals that are not associated with synchronous
              communications standards.
            - ``EYE`` is for synchronous-communication signals with NRZ-like characteristics
              (nonreturn to zero).
        """
        return self._sigtype


class MeasurementImmedReflevelPercentMidItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:REFLevel:PERCent:MID<x>`` command.

    Description:
        - This command sets or queries the percentage (where 100% is equal to HIGH) used to
          calculate the mid reference level when ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set to
          Percent. Mid1 is for the first waveform specified, and Mid2 is for the second waveform
          specified. Note that this command affects the results of delay measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel:PERCent:MID<x>?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:PERCent:MID<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:PERCent:MID<x> value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:REFLevel:PERCent:MID<x> <NR1>
        - MEASUrement:IMMed:REFLevel:PERCent:MID<x>?
        ```

    Info:
        - ``<NR1>`` is the mid reference level, ranging from 0 to 100%. The default mid reference
          level is 50%.
    """


class MeasurementImmedReflevelPercentLow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:REFLevel:PERCent:LOW`` command.

    Description:
        - This command sets or queries the percentage (where 100% is equal to HIGH) used to
          calculate the low reference level when ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set to
          Percent. Note that this command affects the results of rise and fall measurements. This
          command is equivalent to selecting Reference Levels from the Measure menu and then
          entering the Percentage Low Ref value.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel:PERCent:LOW?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:PERCent:LOW?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:PERCent:LOW value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:REFLevel:PERCent:LOW <NR1>
        - MEASUrement:IMMed:REFLevel:PERCent:LOW?
        ```

    Info:
        - ``<NR1>`` is the low reference level, ranging from 0 to 100%. The default low reference
          level is 10%.
    """


class MeasurementImmedReflevelPercentHigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:REFLevel:PERCent:HIGH`` command.

    Description:
        - This command sets or queries the percentage (where 100% is equal to HIGH) used to
          calculate the high reference level when ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set to
          Percent. Note that this command affects the results of rise and fall measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel:PERCent:HIGH?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:PERCent:HIGH?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:PERCent:HIGH value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:REFLevel:PERCent:HIGH <NR1>
        - MEASUrement:IMMed:REFLevel:PERCent:HIGH?
        ```

    Info:
        - ``<NR1>`` is the high reference level, ranging from 0 to 100%. The default high reference
          level is 90%.
    """


class MeasurementImmedReflevelPercent(SCPICmdRead):
    """The ``MEASUrement:IMMed:REFLevel:PERCent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel:PERCent?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:REFLevel:PERCent?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.high``: The ``MEASUrement:IMMed:REFLevel:PERCent:HIGH`` command.
        - ``.low``: The ``MEASUrement:IMMed:REFLevel:PERCent:LOW`` command.
        - ``.mid``: The ``MEASUrement:IMMed:REFLevel:PERCent:MID<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = MeasurementImmedReflevelPercentHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = MeasurementImmedReflevelPercentLow(device, f"{self._cmd_syntax}:LOW")
        self._mid: Dict[int, MeasurementImmedReflevelPercentMidItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementImmedReflevelPercentMidItem(device, f"{self._cmd_syntax}:MID{x}")
        )

    @property
    def high(self) -> MeasurementImmedReflevelPercentHigh:
        """Return the ``MEASUrement:IMMed:REFLevel:PERCent:HIGH`` command.

        Description:
            - This command sets or queries the percentage (where 100% is equal to HIGH) used to
              calculate the high reference level when ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set
              to Percent. Note that this command affects the results of rise and fall measurements.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:IMMed:REFLevel:PERCent:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:PERCent:HIGH?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:PERCent:HIGH value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:REFLevel:PERCent:HIGH <NR1>
            - MEASUrement:IMMed:REFLevel:PERCent:HIGH?
            ```

        Info:
            - ``<NR1>`` is the high reference level, ranging from 0 to 100%. The default high
              reference level is 90%.
        """
        return self._high

    @property
    def low(self) -> MeasurementImmedReflevelPercentLow:
        """Return the ``MEASUrement:IMMed:REFLevel:PERCent:LOW`` command.

        Description:
            - This command sets or queries the percentage (where 100% is equal to HIGH) used to
              calculate the low reference level when ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set to
              Percent. Note that this command affects the results of rise and fall measurements.
              This command is equivalent to selecting Reference Levels from the Measure menu and
              then entering the Percentage Low Ref value.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:IMMed:REFLevel:PERCent:LOW?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:PERCent:LOW?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:PERCent:LOW value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:REFLevel:PERCent:LOW <NR1>
            - MEASUrement:IMMed:REFLevel:PERCent:LOW?
            ```

        Info:
            - ``<NR1>`` is the low reference level, ranging from 0 to 100%. The default low
              reference level is 10%.
        """
        return self._low

    @property
    def mid(self) -> Dict[int, MeasurementImmedReflevelPercentMidItem]:
        """Return the ``MEASUrement:IMMed:REFLevel:PERCent:MID<x>`` command.

        Description:
            - This command sets or queries the percentage (where 100% is equal to HIGH) used to
              calculate the mid reference level when ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set to
              Percent. Mid1 is for the first waveform specified, and Mid2 is for the second waveform
              specified. Note that this command affects the results of delay measurements.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:IMMed:REFLevel:PERCent:MID<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:PERCent:MID<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:PERCent:MID<x> value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:REFLevel:PERCent:MID<x> <NR1>
            - MEASUrement:IMMed:REFLevel:PERCent:MID<x>?
            ```

        Info:
            - ``<NR1>`` is the mid reference level, ranging from 0 to 100%. The default mid
              reference level is 50%.
        """
        return self._mid


class MeasurementImmedReflevelMethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:REFLevel:METHod`` command.

    Description:
        - This command specifies or queries the reference level units used for measurement
          calculations. This command is equivalent to selecting Reference Levels from the Measure
          menu and then choosing the desired reference level from the Units group box.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel:METHod?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:REFLevel:METHod?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:METHod value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:REFLevel:METHod {ABSolute|PERCent}
        - MEASUrement:IMMed:REFLevel:METHod?
        ```

    Info:
        - ``ABSolute`` specifies that the reference levels are set explicitly using the
          ``MEASUrement:IMMed:REFLevel:ABSolute`` commands. This method is useful when precise
          values are required. For instance, when designing to published interface specifications,
          such as RS-232-C.
        - ``PERCent`` specifies that the reference levels are calculated as a percent relative to
          HIGH and LOW. The percentages are defined using the ``MEASUrement:IMMed:REFLevel:PERCent``
          commands.
    """


class MeasurementImmedReflevelAbsoluteMidItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:REFLevel:ABSolute:MID<x>`` command.

    Description:
        - This command sets or queries the mid reference level, and is the 50% reference level when
          ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set to Absolute. Note that this command affects
          the results of period, frequency, delay, and all cyclic measurements. Note that this
          command affects the results of delay measurements.

    Usage:
        - Using the ``.query()`` method will send the
          ``MEASUrement:IMMed:REFLevel:ABSolute:MID<x>?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:ABSolute:MID<x>?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:ABSolute:MID<x> value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:REFLevel:ABSolute:MID<x> <NR3>
        - MEASUrement:IMMed:REFLevel:ABSolute:MID<x>?
        ```

    Info:
        - ``<NR3>`` is the mid1 (the 'from' waveform when taking a delay measurement) or mid2 (the
          'to' waveform when taking a delay measurement) reference level in volts. The default is
          0.0 V.
    """


class MeasurementImmedReflevelAbsoluteLow(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:REFLevel:ABSolute:LOW`` command.

    Description:
        - This command sets or queries the low reference level, and is the zero percent level when
          ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set to Absolute. Note that this command affects
          the results of rise and fall measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel:ABSolute:LOW?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:ABSolute:LOW?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:ABSolute:LOW value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:REFLevel:ABSolute:LOW <NR3>
        - MEASUrement:IMMed:REFLevel:ABSolute:LOW?
        ```

    Info:
        - ``<NR3>`` is the low reference level in volts. The default is 0.0 V.
    """


class MeasurementImmedReflevelAbsoluteHigh(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:REFLevel:ABSolute:HIGH`` command.

    Description:
        - This command sets or queries the high reference level, and is the upper reference level
          when ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set to Absolute. Note that this command
          affects the results of rise and fall measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel:ABSolute:HIGH?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:ABSolute:HIGH?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:IMMed:REFLevel:ABSolute:HIGH value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:REFLevel:ABSolute:HIGH <NR3>
        - MEASUrement:IMMed:REFLevel:ABSolute:HIGH?
        ```

    Info:
        - ``<NR3>`` is the high reference level in volts. The default is 0.0 V.
    """


class MeasurementImmedReflevelAbsolute(SCPICmdRead):
    """The ``MEASUrement:IMMed:REFLevel:ABSolute`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel:ABSolute?``
          query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:REFLevel:ABSolute?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.high``: The ``MEASUrement:IMMed:REFLevel:ABSolute:HIGH`` command.
        - ``.low``: The ``MEASUrement:IMMed:REFLevel:ABSolute:LOW`` command.
        - ``.mid``: The ``MEASUrement:IMMed:REFLevel:ABSolute:MID<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = MeasurementImmedReflevelAbsoluteHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = MeasurementImmedReflevelAbsoluteLow(device, f"{self._cmd_syntax}:LOW")
        self._mid: Dict[int, MeasurementImmedReflevelAbsoluteMidItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementImmedReflevelAbsoluteMidItem(device, f"{self._cmd_syntax}:MID{x}")
        )

    @property
    def high(self) -> MeasurementImmedReflevelAbsoluteHigh:
        """Return the ``MEASUrement:IMMed:REFLevel:ABSolute:HIGH`` command.

        Description:
            - This command sets or queries the high reference level, and is the upper reference
              level when ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set to Absolute. Note that this
              command affects the results of rise and fall measurements.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:IMMed:REFLevel:ABSolute:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:ABSolute:HIGH?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:ABSolute:HIGH value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:REFLevel:ABSolute:HIGH <NR3>
            - MEASUrement:IMMed:REFLevel:ABSolute:HIGH?
            ```

        Info:
            - ``<NR3>`` is the high reference level in volts. The default is 0.0 V.
        """
        return self._high

    @property
    def low(self) -> MeasurementImmedReflevelAbsoluteLow:
        """Return the ``MEASUrement:IMMed:REFLevel:ABSolute:LOW`` command.

        Description:
            - This command sets or queries the low reference level, and is the zero percent level
              when ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set to Absolute. Note that this command
              affects the results of rise and fall measurements.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:IMMed:REFLevel:ABSolute:LOW?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:ABSolute:LOW?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:ABSolute:LOW value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:REFLevel:ABSolute:LOW <NR3>
            - MEASUrement:IMMed:REFLevel:ABSolute:LOW?
            ```

        Info:
            - ``<NR3>`` is the low reference level in volts. The default is 0.0 V.
        """
        return self._low

    @property
    def mid(self) -> Dict[int, MeasurementImmedReflevelAbsoluteMidItem]:
        """Return the ``MEASUrement:IMMed:REFLevel:ABSolute:MID<x>`` command.

        Description:
            - This command sets or queries the mid reference level, and is the 50% reference level
              when ``MEASUREMENT:IMMED:REFLEVEL:METHOD`` is set to Absolute. Note that this command
              affects the results of period, frequency, delay, and all cyclic measurements. Note
              that this command affects the results of delay measurements.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASUrement:IMMed:REFLevel:ABSolute:MID<x>?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:ABSolute:MID<x>?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:ABSolute:MID<x> value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:REFLevel:ABSolute:MID<x> <NR3>
            - MEASUrement:IMMed:REFLevel:ABSolute:MID<x>?
            ```

        Info:
            - ``<NR3>`` is the mid1 (the 'from' waveform when taking a delay measurement) or mid2
              (the 'to' waveform when taking a delay measurement) reference level in volts. The
              default is 0.0 V.
        """
        return self._mid


class MeasurementImmedReflevel(SCPICmdRead):
    """The ``MEASUrement:IMMed:REFLevel`` command.

    Description:
        - This query-only command returns the reference level settings for the immediate
          measurement. It returns them in the following order: ABSOLUTE and then PERCENT for
          individual user measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:REFLevel?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:REFLevel?
        ```

    Properties:
        - ``.absolute``: The ``MEASUrement:IMMed:REFLevel:ABSolute`` command tree.
        - ``.method``: The ``MEASUrement:IMMed:REFLevel:METHod`` command.
        - ``.percent``: The ``MEASUrement:IMMed:REFLevel:PERCent`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = MeasurementImmedReflevelAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._method = MeasurementImmedReflevelMethod(device, f"{self._cmd_syntax}:METHod")
        self._percent = MeasurementImmedReflevelPercent(device, f"{self._cmd_syntax}:PERCent")

    @property
    def absolute(self) -> MeasurementImmedReflevelAbsolute:
        """Return the ``MEASUrement:IMMed:REFLevel:ABSolute`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel:ABSolute?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:ABSolute?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``MEASUrement:IMMed:REFLevel:ABSolute:HIGH`` command.
            - ``.low``: The ``MEASUrement:IMMed:REFLevel:ABSolute:LOW`` command.
            - ``.mid``: The ``MEASUrement:IMMed:REFLevel:ABSolute:MID<x>`` command.
        """
        return self._absolute

    @property
    def method(self) -> MeasurementImmedReflevelMethod:
        """Return the ``MEASUrement:IMMed:REFLevel:METHod`` command.

        Description:
            - This command specifies or queries the reference level units used for measurement
              calculations. This command is equivalent to selecting Reference Levels from the
              Measure menu and then choosing the desired reference level from the Units group box.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel:METHod?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:METHod?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:METHod value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:REFLevel:METHod {ABSolute|PERCent}
            - MEASUrement:IMMed:REFLevel:METHod?
            ```

        Info:
            - ``ABSolute`` specifies that the reference levels are set explicitly using the
              ``MEASUrement:IMMed:REFLevel:ABSolute`` commands. This method is useful when precise
              values are required. For instance, when designing to published interface
              specifications, such as RS-232-C.
            - ``PERCent`` specifies that the reference levels are calculated as a percent relative
              to HIGH and LOW. The percentages are defined using the
              ``MEASUrement:IMMed:REFLevel:PERCent`` commands.
        """
        return self._method

    @property
    def percent(self) -> MeasurementImmedReflevelPercent:
        """Return the ``MEASUrement:IMMed:REFLevel:PERCent`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel:PERCent?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:REFLevel:PERCent?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.high``: The ``MEASUrement:IMMed:REFLevel:PERCent:HIGH`` command.
            - ``.low``: The ``MEASUrement:IMMed:REFLevel:PERCent:LOW`` command.
            - ``.mid``: The ``MEASUrement:IMMed:REFLevel:PERCent:MID<x>`` command.
        """
        return self._percent


class MeasurementImmedNoise(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:NOISe`` command.

    Description:
        - This command sets or queries whether the noise measurement is made on the high or low
          level of the waveform. Sending this command is equivalent to selecting Ref Levs > Eye >
          Top Level or Base Level in the Comm tab of the Measurement Setup dialog box. The Eye
          section is displayed only if you have an eye-pattern or optical measurement defined.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:NOISe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:NOISe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:NOISe value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:NOISe {HIGH|LOW}
        - MEASUrement:IMMed:NOISe?
        ```

    Info:
        - ``HIGH`` argument causes the measurement for noise to be taken at the high level of the
          waveform.
        - ``LOW`` argument causes the measurement for noise to be taken at the low level of the
          waveform.
    """


class MeasurementImmedMethod(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:METHod`` command.

    Description:
        - This command specifies or queries the method used to calculate the 0% and 100% reference
          level for immediate measurements.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:METHod?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:METHod?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:METHod value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:METHod {HIStogram|MINMax|MEAN}
        - MEASUrement:IMMed:METHod?
        ```

    Info:
        - ``HIStogram`` sets the high and low waveform levels statistically using a histogram
          algorithm.
        - ``MINMax`` sets the high and low waveform levels to MAX and MIN, respectively.
        - ``MEAN`` sets the high and low waveform levels to their mean.
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


class MeasurementImmedDelayEdge2(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:DELay:EDGE2`` command.

    Description:
        - This command sets or queries the slope of the edge that is used for the delay 'to'
          waveform when taking an immediate delay measurement. Use the ``MEASUREMENT:IMMED:SOURCEX``
          command to specify the waveform. This command is equivalent to selecting Measurement Setup
          from the Measure menu, choosing the Time tab, clicking the Delay button to display the
          delay settings and then clicking the desired Delay Edge2 setting.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:DELay:EDGE2?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:DELay:EDGE2?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:DELay:EDGE2 value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:DELay:EDGE2 {FALL|RISe}
        - MEASUrement:IMMed:DELay:EDGE2?
        ```

    Info:
        - ``FALL`` specifies the falling edge.
        - ``RISe`` specifies the rising edge.
    """


class MeasurementImmedDelayDirection(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:DELay:DIREction`` command.

    Description:
        - This command sets or returns the starting point and direction that determines the delay
          'to' edge when taking an immediate delay measurement. Use the
          ``MEASUREMENT:IMMED:SOURCEX`` command to specify the delay 'to' waveform. This command is
          equivalent to selecting Measurement Setup from the Measure menu, choosing the Time tab,
          clicking the Delay button to display the delay settings and then clicking the desired
          Search Direction setting.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:DELay:DIREction?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:DELay:DIREction?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:IMMed:DELay:DIREction value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:DELay:DIREction {BACKWards|FORWards}
        - MEASUrement:IMMed:DELay:DIREction?
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
        - ``.direction``: The ``MEASUrement:IMMed:DELay:DIREction`` command.
        - ``.edge2``: The ``MEASUrement:IMMed:DELay:EDGE2`` command.
        - ``.edge``: The ``MEASUrement:IMMed:DELay:EDGE<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._direction = MeasurementImmedDelayDirection(device, f"{self._cmd_syntax}:DIREction")
        self._edge2 = MeasurementImmedDelayEdge2(device, f"{self._cmd_syntax}:EDGE2")
        self._edge: Dict[int, MeasurementImmedDelayEdgeItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementImmedDelayEdgeItem(device, f"{self._cmd_syntax}:EDGE{x}")
        )

    @property
    def direction(self) -> MeasurementImmedDelayDirection:
        """Return the ``MEASUrement:IMMed:DELay:DIREction`` command.

        Description:
            - This command sets or returns the starting point and direction that determines the
              delay 'to' edge when taking an immediate delay measurement. Use the
              ``MEASUREMENT:IMMED:SOURCEX`` command to specify the delay 'to' waveform. This command
              is equivalent to selecting Measurement Setup from the Measure menu, choosing the Time
              tab, clicking the Delay button to display the delay settings and then clicking the
              desired Search Direction setting.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:DELay:DIREction?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:IMMed:DELay:DIREction?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:DELay:DIREction value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:DELay:DIREction {BACKWards|FORWards}
            - MEASUrement:IMMed:DELay:DIREction?
            ```

        Info:
            - ``BACKWards`` starts the search at the end of the waveform and looks for the last
              rising or falling edge in the waveform.
            - ``FORWards`` starts the search at the beginning of the waveform and looks for the
              first rising or falling edge in the waveform.
        """
        return self._direction

    @property
    def edge2(self) -> MeasurementImmedDelayEdge2:
        """Return the ``MEASUrement:IMMed:DELay:EDGE2`` command.

        Description:
            - This command sets or queries the slope of the edge that is used for the delay 'to'
              waveform when taking an immediate delay measurement. Use the
              ``MEASUREMENT:IMMED:SOURCEX`` command to specify the waveform. This command is
              equivalent to selecting Measurement Setup from the Measure menu, choosing the Time
              tab, clicking the Delay button to display the delay settings and then clicking the
              desired Delay Edge2 setting.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:DELay:EDGE2?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:DELay:EDGE2?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:IMMed:DELay:EDGE2 value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:DELay:EDGE2 {FALL|RISe}
            - MEASUrement:IMMed:DELay:EDGE2?
            ```

        Info:
            - ``FALL`` specifies the falling edge.
            - ``RISe`` specifies the rising edge.
        """
        return self._edge2

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


#  pylint: disable=too-many-instance-attributes
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
        - ``.method``: The ``MEASUrement:IMMed:METHod`` command.
        - ``.noise``: The ``MEASUrement:IMMed:NOISe`` command.
        - ``.reflevel``: The ``MEASUrement:IMMed:REFLevel`` command.
        - ``.source1``: The ``MEASUrement:IMMed:SOUrce1`` command.
        - ``.type``: The ``MEASUrement:IMMed:TYPe`` command.
        - ``.units``: The ``MEASUrement:IMMed:UNIts`` command.
        - ``.value``: The ``MEASUrement:IMMed:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delay = MeasurementImmedDelay(device, f"{self._cmd_syntax}:DELay")
        self._method = MeasurementImmedMethod(device, f"{self._cmd_syntax}:METHod")
        self._noise = MeasurementImmedNoise(device, f"{self._cmd_syntax}:NOISe")
        self._reflevel = MeasurementImmedReflevel(device, f"{self._cmd_syntax}:REFLevel")
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
            - ``.direction``: The ``MEASUrement:IMMed:DELay:DIREction`` command.
            - ``.edge2``: The ``MEASUrement:IMMed:DELay:EDGE2`` command.
            - ``.edge``: The ``MEASUrement:IMMed:DELay:EDGE<x>`` command.
        """
        return self._delay

    @property
    def method(self) -> MeasurementImmedMethod:
        """Return the ``MEASUrement:IMMed:METHod`` command.

        Description:
            - This command specifies or queries the method used to calculate the 0% and 100%
              reference level for immediate measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:METHod?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:METHod?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:METHod value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:METHod {HIStogram|MINMax|MEAN}
            - MEASUrement:IMMed:METHod?
            ```

        Info:
            - ``HIStogram`` sets the high and low waveform levels statistically using a histogram
              algorithm.
            - ``MINMax`` sets the high and low waveform levels to MAX and MIN, respectively.
            - ``MEAN`` sets the high and low waveform levels to their mean.
        """
        return self._method

    @property
    def noise(self) -> MeasurementImmedNoise:
        """Return the ``MEASUrement:IMMed:NOISe`` command.

        Description:
            - This command sets or queries whether the noise measurement is made on the high or low
              level of the waveform. Sending this command is equivalent to selecting Ref Levs > Eye
              > Top Level or Base Level in the Comm tab of the Measurement Setup dialog box. The Eye
              section is displayed only if you have an eye-pattern or optical measurement defined.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:NOISe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:NOISe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:NOISe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:NOISe {HIGH|LOW}
            - MEASUrement:IMMed:NOISe?
            ```

        Info:
            - ``HIGH`` argument causes the measurement for noise to be taken at the high level of
              the waveform.
            - ``LOW`` argument causes the measurement for noise to be taken at the low level of the
              waveform.
        """
        return self._noise

    @property
    def reflevel(self) -> MeasurementImmedReflevel:
        """Return the ``MEASUrement:IMMed:REFLevel`` command.

        Description:
            - This query-only command returns the reference level settings for the immediate
              measurement. It returns them in the following order: ABSOLUTE and then PERCENT for
              individual user measurements.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:REFLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:REFLevel?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:REFLevel?
            ```

        Sub-properties:
            - ``.absolute``: The ``MEASUrement:IMMed:REFLevel:ABSolute`` command tree.
            - ``.method``: The ``MEASUrement:IMMed:REFLevel:METHod`` command.
            - ``.percent``: The ``MEASUrement:IMMed:REFLevel:PERCent`` command tree.
        """
        return self._reflevel

    @property
    def source1(self) -> MeasurementImmedSource1:
        """Return the ``MEASUrement:IMMed:SOUrce1`` command.

        Description:
            - This command sets or queries the source for phase or delay immediate measurements.
              This command is equivalent to selecting Measurement Setup from the Measure menu,
              choosing the Time tab, clicking the Delay button to display the delay settings and
              then clicking the desired Source1 (From) setting or Source2 (To) setting. Tip: Source2
              measurements only apply to phase and delay measurement types, which require both a
              target (Source1) and reference (Source2) source.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:SOUrce1 {CH<x>|MATH<y>|REF<x>|HIStogram}
            - MEASUrement:IMMed:SOUrce1?
            ```

        Info:
            - ``CH<x>`` is an input channel waveform. The x variable can be expressed as an integer
              ranging from 1 through 4.
            - ``MATH<y>`` is a math waveform. The y variable can be expressed as an integer ranging
              from 1 through 4.
            - ``REF<X>`` is a reference waveform. The x variable can be expressed as an integer
              ranging from 1 through 4.
            - ``HIStogram`` indicates histogram as the object to be measured. HIStogram not allowed
              on SOUrce2.

        Sub-properties:
            - ``.sigtype``: The ``MEASUrement:IMMed:SOUrce1:SIGType`` command.
        """
        return self._source1

    @property
    def type(self) -> MeasurementImmedType:
        """Return the ``MEASUrement:IMMed:TYPe`` command.

        Description:
            - This command sets or queries the immediate measurement type. Immediate measurements
              and annotations are not displayed on the screen.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:TYPe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|DISTDUty|EXTINCTDB|EXTINCTPCT|EXTINCTRATIO|EYEHeight|EYEWIdth|FALL|FREQuency|HIGH|HITs|LOW|MAXimum|MEAN|MEDian|MINImum|NCROss|NDUty|NOVershoot|NWIdth|PBASe|PCROss|PCTCROss|PDUty|PEAKHits|PERIod|PHAse|PK2Pk|PKPKJitter|PKPKNoise|POVershoot|PTOP|PWIdth|QFACtor|RISe|RMS|RMSJitter|RMSNoise|SIGMA1|SIGMA2|SIGMA3|SIXSigmajit|SNRatio|STDdev|UNDEFINED|WAVEFORMS}
            - MEASUrement:IMMed:TYPe?
            ```

        Info:
            - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it
              measures the high value less the low value measured over the entire waveform or gated
              region.
            - ``Amplitude = High - Low``
            - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
              region and is measured in volt-seconds. The area measured above the ground is
              positive, while the area below ground is negative.
            - ``BURst`` measures the duration of a burst. The measurement is made over the entire
              waveform or gated region.
            - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures in
              volt-seconds, the area over the first cycle in the waveform or the first cycle in the
              gated region. The area measured above the common reference point is positive, while
              the area below the common reference point is negative.
            - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the
              waveform or the first cycle in the gated region.
            - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle
              in the waveform or the first cycle in the gated region.
            - ``DELay`` measures the time between the middle reference (default = 50%) amplitude
              point of the source waveform and the destination waveform.
            - ``DISTDUty`` (duty cycle distortion) measures the time between the falling edge and
              the rising edge of the eye pattern at the mid reference level. It is the peak-to-peak
              time variation of the first eye crossing measured at the mid-reference as a percent of
              the eye period.
            - ``EXTINCTDB`` measures the extinction ratio of an optical waveform (eye diagram).
              Extinction Ratio (dB) measures the ratio of the average power levels for the logic
              High to the logic Low of an optical waveform and expresses the result in dB. This
              measurement only works for fast acquisition signals or a reference waveform saved in
              fast acquisition mode.
            - ``Extinction dB = 10 × (log 10 (High / Low)``
            - ``EXTINCTPCT`` measures the extinction ratio of the selected optical waveform.
              Extinction Ratio (%) measures the ratio of the average power levels for the logic Low
              (off) to the logic (High) (on) of an optical waveform and expresses the result in
              percent. This measurement only works for fast acquisition signals or a reference
              waveform saved in fast acquisition mode.
            - ``Extinction % = 100.0 × (Low / High)``
            - ``EXTINCTRATIO`` measures the extinction ratio of the selected optical waveform.
              Extinction Ratio measures the ratio of the average power levels for the logic High to
              the logic Low of an optical waveform and expresses the result without units. This
              measurement only works for fast acquisition signals or a reference waveform saved in
              fast acquisition mode. Extinction ratios greater than 100 or less than 1 generate
              errors; low must be greater than or equal to 1 µW.
            - ``Extinction Ratio = (High / Low)``
            - ``EYEHeight`` measures the vertical opening of an eye diagram in volts.
            - ``EYEWidth`` measures the width of an eye diagram in seconds.
            - ``FALL`` measures the time taken for the falling edge of the first pulse in the
              waveform or gated region to fall from a high reference value (default is 90%) to a low
              reference value (default is 10%).
            - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is
              the reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per
              second.
            - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a
              waveform.
            - ``HITs`` (histogram hits) measures the number of points in or on the histogram box.
            - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a
              waveform.
            - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
              found. It is measured over the entire waveform or gated region. When histogram is
              selected with the ``MEASUREMENT:METHOD`` command, the maximum measurement measures the
              voltage of the highest nonzero bin in vertical histograms or the time of the
              right-most bin in horizontal histograms.
            - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or
              gated region. When histogram is selected with the ``MEASUREMENT:METHOD`` command, the
              mean measurement measures the average of all acquired points within or on the
              histogram.
            - ``MEDian`` (histogram measurement) measures the middle point of the histogram box.
              Half of all acquired points within or on the histogram box are less than this value
              and half are greater than this value.
            - ``MINImum`` finds the minimum amplitude. This value is typically the most negative
              peak voltage. It is measured over the entire waveform or gated region. When histogram
              is selected with the ``MEASUREMENT:METHOD`` command, the minimum measurement measures
              the lowest nonzero bin in vertical histograms or the time of the left-most nonzero bin
              in the horizontal histograms.
            - ``NCROss`` (timing measurement) measures the time from the trigger point to the first
              falling edge of the waveform or gated region. The distance (time) is measured at the
              middle reference amplitude point of the signal.
            - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
              period, expressed as a percentage. The duty cycle is measured on the first cycle in
              the waveform or gated region.
            - ``Negative Duty Cycle = (Negative Width) / Period × 100%``
            - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
              waveform or gated region.
            - ``Negative Overshoot = (Low - Minimum) / Amplitude × 100%)``
            - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
              reference (default = 50%) amplitude points of a negative pulse. The measurement is
              made on the first pulse in the waveform or gated region.
            - ``PBASe`` measures the base value used in extinction ratio measurements.
            - ``PCROss`` (timing measurement) measures the time from the trigger point to the first
              positive edge of the waveform or gated region. The distance (time) is measured at the
              middle reference amplitude point of the signal.
            - ``PCTCROss`` measures the location of the eye crossing point expressed as a percentage
              of EYEHeight.
            - ``Crossing percent = 100 ×[(eye-crossing-point - PBASe)/(PTOP - PBASe)]``
            - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
              period, expressed as a percentage. It is measured on the first cycle in the waveform
              or gated region.
            - ``Positive Duty Cycle = (Positive Width)/Period × 100%``
            - ``PEAKHits`` measures the number of points in the largest bin of the histogram.
            - ``PERIod`` is the time required to complete the first cycle in a waveform or gated
              region. Period is the reciprocal of frequency and is measured in seconds.
            - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
              reference waveform) between two waveforms. The measurement is made between the middle
              reference points of the two waveforms and is expressed in degrees, where 360°
              represents one waveform cycle.
            - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
              amplitude in the entire waveform or gated region. When histogram is selected with the
              ``MEASUREMENT:METHOD`` command, the PK2Pk measurement measures the histogram peak to
              peak difference.
            - ``PKPKJitter`` measures the variance (minimum and maximum values) in the time
              locations of the cross point.
            - ``PKPKNoise`` measures the peak-to-peak noise on a waveform at the mid reference
              level.
            - ``POVershoot``
            - ``Positive Overshoot = (Maximum - High) / Amplitude ×100%``
            - ``PTOT`` measures the top value used in extinction ratio measurements.
            - ``PWIdth`` (positive width) is the distance (time) between the middle reference
              (default = 50%) amplitude points of a positive pulse. The measurement is made on the
              first pulse in the waveform or gated region.
            - ``QFACtor`` measures the quality factor. The Q factor is a figure of merit for an eye
              diagram, which indicates the vertical eye opening relative to the noise at the low and
              high logic levels. It is the ratio of the eye size to noise.
            - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the
              time it takes for the leading edge of the first pulse encountered to rise from a low
              reference value (defaul t is 10%) to a high reference value (default is 90%).
            - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
              waveform or gated region.
            - ``RMSJitter`` measures the variance in the time locations of the cross point. The RMS
              jitter is defined as one standard deviation at the cross point.
            - ``RMSNoise`` measures the Root Mean Square noise amplitude on a waveform at the mid
              reference level.
            - ``SIGMA1`` (histogram measurement) measures the percentage of points in the histogram
              that are within one standard deviation of the histogram mean.
            - ``SIGMA2`` (histogram measurement) measures the percentage of points in the histogram
              that are within two standard deviations of the histogram mean.
            - ``SIGMA3`` (histogram measurement) measures the percentage of points in the histogram
              that are within three standard deviations of the histogram mean.
            - ``SIXSigmajit`` (histogram measurement) is six × RMSJitter.
            - ``SNRatio`` measures the signal-to-noise ratio. The signal-to-noise ratio is the
              amplitude of a noise rejection band centered on the mid level.
            - ``STDdev`` measures the standard deviation (Root Mean Square (RMS) deviation) of all
              acquired points within or on the histogram box.
            - ``UNDEFINED`` is the default measurement type, which indicates that no measurement
              type is specified. Once a measurement type is chosen, it can be cleared using this
              argument.
            - ``WAVEFORMS`` (waveform count) measures the number of waveforms used to calculate the
              histogram.
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
        - This command specifies or returns the measurement gating setting. This command is
          equivalent to selecting Gating from the Measure menu and then clicking the desired
          Measurement Gating setting.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:GATing?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:GATing value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:GATing {ON|OFF|<NR1>|ZOOM<x>|CURSor}
        - MEASUrement:GATing?
        ```

    Info:
        - ``ON`` turns on measurement gating.
        - ``OFF`` turns off measurement gating.
        - ``<NR1>`` = 0 turns off measurement gating; any other value turns on measurement gating.
        - ``ZOOM<x>`` turns on gating, using the left and right edges of the zoom box. <x> specifies
          the zoom window, which ranges from 1 through 4.
        - ``CURSOR`` limits measurements to the portion of the waveform between the vertical bar
          cursors, even if they are off screen.
    """


class MeasurementDpojetstatistics(SCPICmdRead):
    """The ``MEASUrement:DPOJETSTATistics`` command.

    Description:
        - This queries the DPOJET measurement statistics.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:DPOJETSTATistics?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:DPOJETSTATistics?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:DPOJETSTATistics?
        ```
    """


class MeasurementAnnotationYItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MEASUrement:ANNOTation:Y<x>`` command.

    Description:
        - This query-only command returns the value of the specified Y annotation. Y annotations are
          numbered, in general, from left to right on the display. The value of <x> can vary from 1
          to 6. Immediate measurements and annotations are not displayed on the screen.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:Y<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:Y<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:ANNOTation:Y<x>?
        ```
    """


class MeasurementAnnotationXItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MEASUrement:ANNOTation:X<x>`` command.

    Description:
        - This query-only command returns the value of the specified X annotation. X annotations are
          numbered, in general, from top to bottom on the display. The value of <x> can vary from 1
          to 6. Immediate measurements and annotations are not displayed on the screen.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:X<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:X<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:ANNOTation:X<x>?
        ```
    """


class MeasurementAnnotationType(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:ANNOTation:TYPe`` command.

    Description:
        - This command sets or queries the type of annotations being used. This command is similar
          to setting the annotation type in the Measure > Annotation menu.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:TYPe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:ANNOTation:TYPe value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:ANNOTation:TYPe {STANdard|DETAiled}
        - MEASUrement:ANNOTation:TYPe?
        ```

    Info:
        - ``STANdard`` sets the annotation type to STANDARD.
        - ``DETAiled`` sets the annotation type to DETAiled, so that more detailed annotations are
          displayed.
    """


class MeasurementAnnotationState(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:ANNOTation:STATE`` command.

    Description:
        - This command sets or returns the state of visible measurement annotations.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:ANNOTation:STATE value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:ANNOTation:STATE {OFF|MEAS<x>}
        - MEASUrement:ANNOTation:STATE?
        ```

    Info:
        - ``OFF`` turns off visible measurement annotations.
        - ``MEAS<x>`` turns on the display of visible measurement annotations for measurement <x>,
          where <x> can be 1, 2, 3, 4, 5, 6, 7, or 8. There must be an active measurement before you
          can activate an annotation for a specified measurement.
    """


class MeasurementAnnotationNumy(SCPICmdRead):
    """The ``MEASUrement:ANNOTation:NUMY`` command.

    Description:
        - This query-only command returns the number of vertical measurement annotations currently
          being displayed. Immediate measurements and annotations are not displayed on the screen.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:NUMY?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:NUMY?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:ANNOTation:NUMY?
        ```
    """


class MeasurementAnnotationNumx(SCPICmdRead):
    """The ``MEASUrement:ANNOTation:NUMX`` command.

    Description:
        - This query-only command returns the number of horizontal measurement annotations currently
          being displayed. Immediate measurements and annotations are not displayed on the screen.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:NUMX?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:NUMX?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:ANNOTation:NUMX?
        ```
    """


class MeasurementAnnotationImmedstate(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:ANNOTation:IMMEDSTAte`` command.

    Description:
        - This command sets or queries the state of immediate measurement annotation. Immediate
          measurements and annotations are not displayed on the screen.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:IMMEDSTAte?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:IMMEDSTAte?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MEASUrement:ANNOTation:IMMEDSTAte value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:ANNOTation:IMMEDSTAte {ON|OFF|<NR1>}
        - MEASUrement:ANNOTation:IMMEDSTAte?
        ```

    Info:
        - ``NR1`` = 0 disables immediate state measurement annotation, any other value enables
          immediate state measurements.
        - ``OFF`` disables annotation on immediate state measurements.
        - ``ON`` enables annotation on immediate state measurements.
    """


class MeasurementAnnotation(SCPICmdRead):
    """The ``MEASUrement:ANNOTation`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immedstate``: The ``MEASUrement:ANNOTation:IMMEDSTAte`` command.
        - ``.numx``: The ``MEASUrement:ANNOTation:NUMX`` command.
        - ``.numy``: The ``MEASUrement:ANNOTation:NUMY`` command.
        - ``.state``: The ``MEASUrement:ANNOTation:STATE`` command.
        - ``.type``: The ``MEASUrement:ANNOTation:TYPe`` command.
        - ``.x``: The ``MEASUrement:ANNOTation:X<x>`` command.
        - ``.y``: The ``MEASUrement:ANNOTation:Y<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immedstate = MeasurementAnnotationImmedstate(device, f"{self._cmd_syntax}:IMMEDSTAte")
        self._numx = MeasurementAnnotationNumx(device, f"{self._cmd_syntax}:NUMX")
        self._numy = MeasurementAnnotationNumy(device, f"{self._cmd_syntax}:NUMY")
        self._state = MeasurementAnnotationState(device, f"{self._cmd_syntax}:STATE")
        self._type = MeasurementAnnotationType(device, f"{self._cmd_syntax}:TYPe")
        self._x: Dict[int, MeasurementAnnotationXItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementAnnotationXItem(device, f"{self._cmd_syntax}:X{x}")
        )
        self._y: Dict[int, MeasurementAnnotationYItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementAnnotationYItem(device, f"{self._cmd_syntax}:Y{x}")
        )

    @property
    def immedstate(self) -> MeasurementAnnotationImmedstate:
        """Return the ``MEASUrement:ANNOTation:IMMEDSTAte`` command.

        Description:
            - This command sets or queries the state of immediate measurement annotation. Immediate
              measurements and annotations are not displayed on the screen.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:IMMEDSTAte?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:ANNOTation:IMMEDSTAte?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:ANNOTation:IMMEDSTAte value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:ANNOTation:IMMEDSTAte {ON|OFF|<NR1>}
            - MEASUrement:ANNOTation:IMMEDSTAte?
            ```

        Info:
            - ``NR1`` = 0 disables immediate state measurement annotation, any other value enables
              immediate state measurements.
            - ``OFF`` disables annotation on immediate state measurements.
            - ``ON`` enables annotation on immediate state measurements.
        """
        return self._immedstate

    @property
    def numx(self) -> MeasurementAnnotationNumx:
        """Return the ``MEASUrement:ANNOTation:NUMX`` command.

        Description:
            - This query-only command returns the number of horizontal measurement annotations
              currently being displayed. Immediate measurements and annotations are not displayed on
              the screen.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:NUMX?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:NUMX?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:ANNOTation:NUMX?
            ```
        """
        return self._numx

    @property
    def numy(self) -> MeasurementAnnotationNumy:
        """Return the ``MEASUrement:ANNOTation:NUMY`` command.

        Description:
            - This query-only command returns the number of vertical measurement annotations
              currently being displayed. Immediate measurements and annotations are not displayed on
              the screen.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:NUMY?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:NUMY?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:ANNOTation:NUMY?
            ```
        """
        return self._numy

    @property
    def state(self) -> MeasurementAnnotationState:
        """Return the ``MEASUrement:ANNOTation:STATE`` command.

        Description:
            - This command sets or returns the state of visible measurement annotations.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MEASUrement:ANNOTation:STATE value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:ANNOTation:STATE {OFF|MEAS<x>}
            - MEASUrement:ANNOTation:STATE?
            ```

        Info:
            - ``OFF`` turns off visible measurement annotations.
            - ``MEAS<x>`` turns on the display of visible measurement annotations for measurement
              <x>, where <x> can be 1, 2, 3, 4, 5, 6, 7, or 8. There must be an active measurement
              before you can activate an annotation for a specified measurement.
        """
        return self._state

    @property
    def type(self) -> MeasurementAnnotationType:
        """Return the ``MEASUrement:ANNOTation:TYPe`` command.

        Description:
            - This command sets or queries the type of annotations being used. This command is
              similar to setting the annotation type in the Measure > Annotation menu.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:TYPe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:ANNOTation:TYPe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:ANNOTation:TYPe {STANdard|DETAiled}
            - MEASUrement:ANNOTation:TYPe?
            ```

        Info:
            - ``STANdard`` sets the annotation type to STANDARD.
            - ``DETAiled`` sets the annotation type to DETAiled, so that more detailed annotations
              are displayed.
        """
        return self._type

    @property
    def x(self) -> Dict[int, MeasurementAnnotationXItem]:
        """Return the ``MEASUrement:ANNOTation:X<x>`` command.

        Description:
            - This query-only command returns the value of the specified X annotation. X annotations
              are numbered, in general, from top to bottom on the display. The value of <x> can vary
              from 1 to 6. Immediate measurements and annotations are not displayed on the screen.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:X<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:X<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:ANNOTation:X<x>?
            ```
        """
        return self._x

    @property
    def y(self) -> Dict[int, MeasurementAnnotationYItem]:
        """Return the ``MEASUrement:ANNOTation:Y<x>`` command.

        Description:
            - This query-only command returns the value of the specified Y annotation. Y annotations
              are numbered, in general, from left to right on the display. The value of <x> can vary
              from 1 to 6. Immediate measurements and annotations are not displayed on the screen.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation:Y<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation:Y<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:ANNOTation:Y<x>?
            ```
        """
        return self._y


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
        - ``.annotation``: The ``MEASUrement:ANNOTation`` command tree.
        - ``.dpojetstatistics``: The ``MEASUrement:DPOJETSTATistics`` command.
        - ``.gating``: The ``MEASUrement:GATing`` command.
        - ``.immed``: The ``MEASUrement:IMMed`` command.
        - ``.meas``: The ``MEASUrement:MEAS<x>`` command.
        - ``.method``: The ``MEASUrement:METHod`` command.
        - ``.noise``: The ``MEASUrement:NOISe`` command.
        - ``.reflevel``: The ``MEASUrement:REFLevel`` command.
        - ``.source1``: The ``MEASUrement:SOUrce1`` command tree.
        - ``.statistics``: The ``MEASUrement:STATIstics`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "MEASUrement"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._annotation = MeasurementAnnotation(device, f"{self._cmd_syntax}:ANNOTation")
        self._dpojetstatistics = MeasurementDpojetstatistics(
            device, f"{self._cmd_syntax}:DPOJETSTATistics"
        )
        self._gating = MeasurementGating(device, f"{self._cmd_syntax}:GATing")
        self._immed = MeasurementImmed(device, f"{self._cmd_syntax}:IMMed")
        self._meas: Dict[int, MeasurementMeasItem] = DefaultDictPassKeyToFactory(
            lambda x: MeasurementMeasItem(device, f"{self._cmd_syntax}:MEAS{x}")
        )
        self._method = MeasurementMethod(device, f"{self._cmd_syntax}:METHod")
        self._noise = MeasurementNoise(device, f"{self._cmd_syntax}:NOISe")
        self._reflevel = MeasurementReflevel(device, f"{self._cmd_syntax}:REFLevel")
        self._source1 = MeasurementSource1(device, f"{self._cmd_syntax}:SOUrce1")
        self._statistics = MeasurementStatistics(device, f"{self._cmd_syntax}:STATIstics")

    @property
    def annotation(self) -> MeasurementAnnotation:
        """Return the ``MEASUrement:ANNOTation`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:ANNOTation?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:ANNOTation?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immedstate``: The ``MEASUrement:ANNOTation:IMMEDSTAte`` command.
            - ``.numx``: The ``MEASUrement:ANNOTation:NUMX`` command.
            - ``.numy``: The ``MEASUrement:ANNOTation:NUMY`` command.
            - ``.state``: The ``MEASUrement:ANNOTation:STATE`` command.
            - ``.type``: The ``MEASUrement:ANNOTation:TYPe`` command.
            - ``.x``: The ``MEASUrement:ANNOTation:X<x>`` command.
            - ``.y``: The ``MEASUrement:ANNOTation:Y<x>`` command.
        """
        return self._annotation

    @property
    def dpojetstatistics(self) -> MeasurementDpojetstatistics:
        """Return the ``MEASUrement:DPOJETSTATistics`` command.

        Description:
            - This queries the DPOJET measurement statistics.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:DPOJETSTATistics?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:DPOJETSTATistics?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:DPOJETSTATistics?
            ```
        """
        return self._dpojetstatistics

    @property
    def gating(self) -> MeasurementGating:
        """Return the ``MEASUrement:GATing`` command.

        Description:
            - This command specifies or returns the measurement gating setting. This command is
              equivalent to selecting Gating from the Measure menu and then clicking the desired
              Measurement Gating setting.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:GATing?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:GATing?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:GATing value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:GATing {ON|OFF|<NR1>|ZOOM<x>|CURSor}
            - MEASUrement:GATing?
            ```

        Info:
            - ``ON`` turns on measurement gating.
            - ``OFF`` turns off measurement gating.
            - ``<NR1>`` = 0 turns off measurement gating; any other value turns on measurement
              gating.
            - ``ZOOM<x>`` turns on gating, using the left and right edges of the zoom box. <x>
              specifies the zoom window, which ranges from 1 through 4.
            - ``CURSOR`` limits measurements to the portion of the waveform between the vertical bar
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
            - ``.method``: The ``MEASUrement:IMMed:METHod`` command.
            - ``.noise``: The ``MEASUrement:IMMed:NOISe`` command.
            - ``.reflevel``: The ``MEASUrement:IMMed:REFLevel`` command.
            - ``.source1``: The ``MEASUrement:IMMed:SOUrce1`` command.
            - ``.type``: The ``MEASUrement:IMMed:TYPe`` command.
            - ``.units``: The ``MEASUrement:IMMed:UNIts`` command.
            - ``.value``: The ``MEASUrement:IMMed:VALue`` command.
        """
        return self._immed

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
            - ``.method``: The ``MEASUrement:MEAS<x>:METHod`` command.
            - ``.minimum``: The ``MEASUrement:MEAS<x>:MINImum`` command.
            - ``.noise``: The ``MEASUrement:MEAS<x>:NOISe`` command.
            - ``.reflevel``: The ``MEASUrement:MEAS<x>:REFLevel`` command.
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
            - This command sets or queries the method used to calculate the 0% and 100% reference
              level. This command is equivalent to selecting Reference Levels from the Measure menu
              and then choosing the desired Determine Base, Top From setting.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:METHod?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:METHod?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:METHod value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:METHod {HIStogram|MEAN|MINMax}
            - MEASUrement:METHod?
            ```

        Info:
            - ``HIStogram`` sets the high and low reference levels to the most common values either
              above or below the mid point, depending on whether the high reference point or the low
              reference point is being defined. Because the statistical approach ignores short-term
              aberrations, such as overshoot or ringing, the histogram method is the best setting
              for examining pulses.
            - ``MEAN`` sets the high and low reference levels to the mean values using all values
              either above or below the midpoint, depending on whether it is defining the high or
              low reference level. The selection is best used for examining eye patterns.
            - ``MINMax`` uses the highest and lowest values of the waveform record. This selection
              is best for examining waveforms with no large, flat portions of a common value, such
              as sine waves and triangle waves.
        """
        return self._method

    @property
    def noise(self) -> MeasurementNoise:
        """Return the ``MEASUrement:NOISe`` command.

        Description:
            - This command sets or queries whether the noise measurement is made on the high or low
              level of the waveform. Sending this command is equivalent to selecting Ref Levs > Eye
              > Top Level or Base Level in the Comm tab of the Measurement Setup dialog box. The Eye
              section is displayed only if you have an eye-pattern or optical measurement defined.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:NOISe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:NOISe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:NOISe value`` command.

        SCPI Syntax:
            ```
            - MEASUrement:NOISe {HIGH|LOW}
            - MEASUrement:NOISe?
            ```

        Info:
            - ``HIGH`` argument causes the measurement for noise to be taken at the high level of
              the waveform.
            - ``LOW`` argument causes the measurement for noise to be taken at the low level of the
              waveform.
        """
        return self._noise

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
    def source1(self) -> MeasurementSource1:
        """Return the ``MEASUrement:SOUrce1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SOUrce1?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.sigtype``: The ``MEASUrement:SOUrce1:SIGType`` command.
        """
        return self._source1

    @property
    def statistics(self) -> MeasurementStatistics:
        """Return the ``MEASUrement:STATIstics`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:STATIstics?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.count``: The ``MEASUrement:STATIstics:COUNt`` command.
            - ``.mode``: The ``MEASUrement:STATIstics:MODe`` command.
            - ``.weighting``: The ``MEASUrement:STATIstics:WEIghting`` command.
        """
        return self._statistics
