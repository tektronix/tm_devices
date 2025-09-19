# pylint: disable=line-too-long
"""The measurement commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

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
    - MEASUrement:IMMed:SOUrce1 {CH<x>|MATH|D<x>|HIStogram|RF_AMPlitude|RF_FREQuency|RF_PHASe}
    - MEASUrement:IMMed:SOUrce1?
    - MEASUrement:IMMed:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|HITS|LOW|MAXimum|MEAN|MEDian|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PEAKHits|PEDGECount|PDUty|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS|SIGMA<x>|STDdev|TOVershoot|WAVEFORMS}
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
    - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|MATH|R<x>|D<x>|HIStogram|RF_AMPlitude|RF_FREQuency|RF_PHASe}
    - MEASUrement:MEAS<x>:SOUrce1?
    - MEASUrement:MEAS<x>:STATE {ON|OFF|<NR1>}
    - MEASUrement:MEAS<x>:STATE?
    - MEASUrement:MEAS<x>:STDdev?
    - MEASUrement:MEAS<x>:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|HITS|LOW|MAXimum|MEAN|MEDian|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PEAKHits|PDUty|PEDGECount|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS|SIGMA<x>|STDdev|TOVershoot|WAVEFORMS}
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
    - MEASUrement:SNAPShot
    - MEASUrement:SNAPShot:AMPlitude?
    - MEASUrement:SNAPShot:AREa?
    - MEASUrement:SNAPShot:BURst?
    - MEASUrement:SNAPShot:CARea?
    - MEASUrement:SNAPShot:CMEan?
    - MEASUrement:SNAPShot:CRMs?
    - MEASUrement:SNAPShot:FALL?
    - MEASUrement:SNAPShot:FREQuency?
    - MEASUrement:SNAPShot:HIGH?
    - MEASUrement:SNAPShot:LOW?
    - MEASUrement:SNAPShot:MAXimum?
    - MEASUrement:SNAPShot:MEAN?
    - MEASUrement:SNAPShot:MINImum?
    - MEASUrement:SNAPShot:NDUty?
    - MEASUrement:SNAPShot:NEDGECount?
    - MEASUrement:SNAPShot:NOVershoot?
    - MEASUrement:SNAPShot:NPULSECount?
    - MEASUrement:SNAPShot:NWIdth?
    - MEASUrement:SNAPShot:PDUty?
    - MEASUrement:SNAPShot:PEDGECount?
    - MEASUrement:SNAPShot:PERIod?
    - MEASUrement:SNAPShot:PK2Pk?
    - MEASUrement:SNAPShot:POVershoot?
    - MEASUrement:SNAPShot:PPULSECount?
    - MEASUrement:SNAPShot:PWIdth?
    - MEASUrement:SNAPShot:RISe?
    - MEASUrement:SNAPShot:RMS?
    - MEASUrement:STATIstics RESET
    - MEASUrement:STATIstics:MODe {OFF|ALL}
    - MEASUrement:STATIstics:MODe?
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
    """The ``MEASUrement:STATIstics:MODe`` command.

    Description:
        - Controls the operation and display of management statistics.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:STATIstics:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics:MODe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:STATIstics:MODe value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:STATIstics:MODe {OFF|ALL}
        - MEASUrement:STATIstics:MODe?
        ```

    Info:
        - ``OFF`` turns all measurements off. This is the default value.
        - ``AL`` turns on statistics and displays all statistics for each measurement.
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
        - ``.mode``: The ``MEASUrement:STATIstics:MODe`` command.
        - ``.weighting``: The ``MEASUrement:STATIstics:WEIghting`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = MeasurementStatisticsMode(device, f"{self._cmd_syntax}:MODe")
        self._weighting = MeasurementStatisticsWeighting(device, f"{self._cmd_syntax}:WEIghting")

    @property
    def mode(self) -> MeasurementStatisticsMode:
        """Return the ``MEASUrement:STATIstics:MODe`` command.

        Description:
            - Controls the operation and display of management statistics.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:STATIstics:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:STATIstics:MODe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:STATIstics:MODe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:STATIstics:MODe {OFF|ALL}
            - MEASUrement:STATIstics:MODe?
            ```

        Info:
            - ``OFF`` turns all measurements off. This is the default value.
            - ``AL`` turns on statistics and displays all statistics for each measurement.
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


class MeasurementSnapshotRms(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:RMS`` command.

    Description:
        - This query returns the true root mean square (RMS) value, in Volts, from the last snapshot
          taken of all measurements. If a snapshot has not been executed, 0.0 is returned and no
          error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:RMS?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:RMS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:RMS?
        ```
    """


class MeasurementSnapshotRise(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:RISe`` command.

    Description:
        - This query returns the rise time value, in seconds, from the last snapshot taken of all
          measurements. The rise time is the time required for the first rising edge to rise from
          the low reference level to the high reference level. If a snapshot has not been executed,
          0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:RISe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:RISe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:RISe?
        ```
    """


class MeasurementSnapshotPwidth(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:PWIdth`` command.

    Description:
        - This query returns the positive pulse width value, in seconds, from the last snapshot
          taken of all measurements. The positive pulse width is the time between the mid reference
          crossings of the first positive pulse. If a snapshot has not been executed, 0.0 is
          returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PWIdth?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:PWIdth?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:PWIdth?
        ```
    """


class MeasurementSnapshotPpulsecount(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:PPULSECount`` command.

    Description:
        - This query returns the positive pulse count value from the last snapshot taken of all
          measurements. The positive pulse count is the number of positive pulses that rise above
          the mid reference level. If a snapshot has not been executed, 0.0 is returned and no error
          event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PPULSECount?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:PPULSECount?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:PPULSECount?
        ```
    """


class MeasurementSnapshotPovershoot(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:POVershoot`` command.

    Description:
        - This query returns the positive overshoot value from the last snapshot taken of all
          measurements. The positive overshoot is the difference between the max value and the high
          value, divided by Amplitude. You can query these values using
          ``MEASUREMENT:SNAPSHOT:MAXIMUM``, ``MEASUREMENT:SNAPSHOT:HIGH`` and
          ``MEASUREMENT:SNAPSHOT:AMPLITUDE``. If a snapshot has not been executed, 0.0 is returned
          and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:POVershoot?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:POVershoot?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:POVershoot?
        ```
    """


class MeasurementSnapshotPk2pk(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:PK2Pk`` command.

    Description:
        - This query returns the peak-to-peak value from the last snapshot taken of all
          measurements. Peak-to-peak is the difference between the max value and the min value. You
          can query the max and min values using ``MEASUREMENT:SNAPSHOT:MAXIMUM`` and
          ``MEASUREMENT:SNAPSHOT:MINIMUM``. If a snapshot has not been executed, 0.0 is returned and
          no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PK2Pk?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:PK2Pk?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:PK2Pk?
        ```
    """


class MeasurementSnapshotPeriod(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:PERIod`` command.

    Description:
        - This query returns the period value from the last snapshot taken of all measurements. The
          period is the time required to complete the first cycle. The first cycle is the time
          between the first two positive crossings, or the first two negative crossings, at the mid
          reference level. If a snapshot has not been executed, 0.0 is returned and no error event
          is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PERIod?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:PERIod?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:PERIod?
        ```
    """


class MeasurementSnapshotPedgecount(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:PEDGECount`` command.

    Description:
        - This query returns the rising edge count value from the last snapshot taken of all
          measurements. The rising edge count is the number of positive transitions from the low
          reference value to the high reference value. You can query the high and low reference
          values using ``MEASUREMENT:SNAPSHOT:HIGH`` and ``MEASUREMENT:SNAPSHOT:LOW``. If a snapshot
          has not been executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PEDGECount?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:PEDGECount?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:PEDGECount?
        ```
    """


class MeasurementSnapshotPduty(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:PDUty`` command.

    Description:
        - This query returns the positive duty cycle value from the last snapshot taken of all
          measurements. The positive duty cycle is the ratio of the positive pulse width to the
          period. The negative duty cycle is measured over the first cycle. If a snapshot has not
          been executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PDUty?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:PDUty?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:PDUty?
        ```
    """


class MeasurementSnapshotNwidth(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:NWIdth`` command.

    Description:
        - This query returns the negative pulse width value, in seconds, from the last snapshot
          taken of all measurements. The negative pulse width is the time between the mid reference
          crossings of the first negative pulse. If a snapshot has not been executed, 0.0 is
          returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:NWIdth?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:NWIdth?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:NWIdth?
        ```
    """


class MeasurementSnapshotNpulsecount(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:NPULSECount`` command.

    Description:
        - This query returns the negative pulse count value from the last snapshot taken of all
          measurements. The negative pulse count is the number of negative pulses that fall below
          the mid reference level. You can set or query the mid reference level using
          ``MEASUREMENT:REFLEVEL:ABSOLUTE:MIDX`` or ``MEASUREMENT:REFLEVEL:PERCENT:MIDX``. ??? If a
          snapshot has not been executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:NPULSECount?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:NPULSECount?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:NPULSECount?
        ```
    """


class MeasurementSnapshotNovershoot(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:NOVershoot`` command.

    Description:
        - This query returns the negative overshoot value from the last snapshot taken of all
          measurements. The negative overshoot is the difference between the minimum value and the
          low value, divided by the amplitude. You can query these values using
          ``MEASUREMENT:SNAPSHOT:MINIMUM``, ``MEASUREMENT:SNAPSHOT:LOW`` and
          ``MEASUREMENT:SNAPSHOT:AMPLITUDE``. If a snapshot has not been executed, 0.0 is returned
          and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:NOVershoot?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:NOVershoot?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:NOVershoot?
        ```
    """


class MeasurementSnapshotNedgecount(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:NEDGECount`` command.

    Description:
        - This query returns the falling edge count value from the last snapshot taken of all
          measurements. The falling edge count is the number of negative transitions from the high
          reference value to the low reference value. You can query the high and low reference
          values using ``MEASUREMENT:SNAPSHOT:HIGH`` and ``MEASUREMENT:SNAPSHOT:LOW``. If a snapshot
          has not been executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:NEDGECount?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:NEDGECount?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:NEDGECount?
        ```
    """


class MeasurementSnapshotNduty(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:NDUty`` command.

    Description:
        - This query returns the negative duty cycle value from the last snapshot taken of all
          measurements. The negative duty cycle is the ratio of the negative pulse width to the
          period. The negative duty cycle is measured over the first cycle. If a snapshot has not
          been executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:NDUty?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:NDUty?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:NDUty?
        ```
    """


class MeasurementSnapshotMinimum(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:MINImum`` command.

    Description:
        - This query returns the minimum value, in Volts, from the last snapshot taken of all
          measurements. If a snapshot has not been executed, 0.0 is returned and no error event is
          set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:MINImum?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:MINImum?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:MINImum?
        ```
    """


class MeasurementSnapshotMean(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:MEAN`` command.

    Description:
        - This query returns the mean value, in Volts, from the last snapshot taken of all
          measurements. If a snapshot has not been executed, 0.0 is returned and no error event is
          set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:MEAN?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:MEAN?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:MEAN?
        ```
    """


class MeasurementSnapshotMaximum(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:MAXimum`` command.

    Description:
        - This query returns the maximum value, in Volts, from the last snapshot taken of all
          measurements. If a snapshot has not been executed, 0.0 is returned and no error event is
          set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:MAXimum?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:MAXimum?
        ```
    """


class MeasurementSnapshotLow(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:LOW`` command.

    Description:
        - This query returns the low value, in Volts, from the last snapshot taken of all
          measurements. If the high-low method is Histogram, low is the lowest density of points
          below the midpoint of the waveform. If the high-low method is min-max, low is equal to
          min. You can set and query the high-low method using ``MEASUREMENT:METHOD``. If a snapshot
          has not been executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:LOW?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:LOW?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:LOW?
        ```
    """


class MeasurementSnapshotHigh(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:HIGH`` command.

    Description:
        - This query returns the high value, in Volts, from the last snapshot taken of all
          measurements. If the method used to calculate the 0% and 100% reference level (high and
          low) is Histogram, high is the highest density of points above the midpoint of the
          waveform. If the high-low method is min-max, high is equal to max. You can set and query
          the high-low method using ``MEASUREMENT:METHOD``. If a snapshot has not been executed, 0.0
          is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:HIGH?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:HIGH?
        ```
    """


class MeasurementSnapshotFrequency(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:FREQuency`` command.

    Description:
        - This query returns the frequency value, in hertz, from the last snapshot taken of all
          measurements. Frequency is the reciprocal of the period. If a snapshot has not been
          executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:FREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:FREQuency?
        ```
    """


class MeasurementSnapshotFall(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:FALL`` command.

    Description:
        - This query returns the fall time value, in seconds, from the last snapshot taken of all
          measurements. Fall time is the time required for the first falling edge to fall from the
          high reference level to the low reference level. If a snapshot has not been executed, 0.0
          is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:FALL?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:FALL?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:FALL?
        ```
    """


class MeasurementSnapshotCrms(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:CRMs`` command.

    Description:
        - This query returns the cycle root mean square (RMS) value, in Volts, from the last
          snapshot taken of all measurements. Cycle RMS is calculated over the first cycle. If a
          snapshot has not been executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:CRMs?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:CRMs?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:CRMs?
        ```
    """


class MeasurementSnapshotCmean(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:CMEan`` command.

    Description:
        - This query returns the cycle mean value, in Volts, from the last snapshot taken of all
          measurements. Cycle mean is the arithmetic mean value, which is calculated over the first
          cycle. If a snapshot has not been executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:CMEan?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:CMEan?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:CMEan?
        ```
    """


class MeasurementSnapshotCarea(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:CARea`` command.

    Description:
        - This query returns the cycle area value, in Volt-seconds, from the last snapshot taken of
          all measurements. Area is the area under the curve, calculated by integrating the samples.
          In other words, Area (Volt-seconds) = (S 0 + S 1 + .. + S n ) x (sample interval). The
          area measured above ground is positive; the area measured below ground is negative. If a
          snapshot has not been executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:CARea?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:CARea?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:CARea?
        ```
    """


class MeasurementSnapshotBurst(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:BURst`` command.

    Description:
        - This query returns the burst width value, in seconds, from the last snapshot taken of all
          measurements. Burst width is the time from the first mid-reference crossing to the last
          mid-reference crossing. If a snapshot has not been executed, 0.0 is returned and no error
          event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:BURst?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:BURst?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:BURst?
        ```
    """


class MeasurementSnapshotArea(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:AREa`` command.

    Description:
        - This query returns the area value, in Volt-seconds, from the last snapshot taken of all
          measurements. Area is the area under the curve, calculated by integrating the samples. In
          other words, Area (Volt-seconds) = (S 0 + S 1 + .. + S n ) x (sample interval) The area
          measured above ground is positive; the area measured below ground is negative. If a
          snapshot has not been executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:AREa?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:AREa?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:AREa?
        ```
    """


class MeasurementSnapshotAmplitude(SCPICmdRead):
    """The ``MEASUrement:SNAPShot:AMPlitude`` command.

    Description:
        - This query returns the amplitude value, in Volts, from the last snapshot taken of all
          measurements. Amplitude is the difference between the high value and the low value. The
          high and low values are queried using ``MEASUREMENT:SNAPSHOT:HIGH`` and
          ``MEASUREMENT:SNAPSHOT:LOW``. You can take a snapshot using ???? If a snapshot has not
          been executed, 0.0 is returned and no error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:AMPlitude?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:AMPlitude?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASUrement:SNAPShot:AMPlitude?
        ```
    """


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class MeasurementSnapshot(SCPICmdWriteNoArguments, SCPICmdRead):
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

    Properties:
        - ``.amplitude``: The ``MEASUrement:SNAPShot:AMPlitude`` command.
        - ``.area``: The ``MEASUrement:SNAPShot:AREa`` command.
        - ``.burst``: The ``MEASUrement:SNAPShot:BURst`` command.
        - ``.carea``: The ``MEASUrement:SNAPShot:CARea`` command.
        - ``.cmean``: The ``MEASUrement:SNAPShot:CMEan`` command.
        - ``.crms``: The ``MEASUrement:SNAPShot:CRMs`` command.
        - ``.fall``: The ``MEASUrement:SNAPShot:FALL`` command.
        - ``.frequency``: The ``MEASUrement:SNAPShot:FREQuency`` command.
        - ``.high``: The ``MEASUrement:SNAPShot:HIGH`` command.
        - ``.low``: The ``MEASUrement:SNAPShot:LOW`` command.
        - ``.maximum``: The ``MEASUrement:SNAPShot:MAXimum`` command.
        - ``.mean``: The ``MEASUrement:SNAPShot:MEAN`` command.
        - ``.minimum``: The ``MEASUrement:SNAPShot:MINImum`` command.
        - ``.nduty``: The ``MEASUrement:SNAPShot:NDUty`` command.
        - ``.nedgecount``: The ``MEASUrement:SNAPShot:NEDGECount`` command.
        - ``.novershoot``: The ``MEASUrement:SNAPShot:NOVershoot`` command.
        - ``.npulsecount``: The ``MEASUrement:SNAPShot:NPULSECount`` command.
        - ``.nwidth``: The ``MEASUrement:SNAPShot:NWIdth`` command.
        - ``.pduty``: The ``MEASUrement:SNAPShot:PDUty`` command.
        - ``.pedgecount``: The ``MEASUrement:SNAPShot:PEDGECount`` command.
        - ``.period``: The ``MEASUrement:SNAPShot:PERIod`` command.
        - ``.pk2pk``: The ``MEASUrement:SNAPShot:PK2Pk`` command.
        - ``.povershoot``: The ``MEASUrement:SNAPShot:POVershoot`` command.
        - ``.ppulsecount``: The ``MEASUrement:SNAPShot:PPULSECount`` command.
        - ``.pwidth``: The ``MEASUrement:SNAPShot:PWIdth`` command.
        - ``.rise``: The ``MEASUrement:SNAPShot:RISe`` command.
        - ``.rms``: The ``MEASUrement:SNAPShot:RMS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = MeasurementSnapshotAmplitude(device, f"{self._cmd_syntax}:AMPlitude")
        self._area = MeasurementSnapshotArea(device, f"{self._cmd_syntax}:AREa")
        self._burst = MeasurementSnapshotBurst(device, f"{self._cmd_syntax}:BURst")
        self._carea = MeasurementSnapshotCarea(device, f"{self._cmd_syntax}:CARea")
        self._cmean = MeasurementSnapshotCmean(device, f"{self._cmd_syntax}:CMEan")
        self._crms = MeasurementSnapshotCrms(device, f"{self._cmd_syntax}:CRMs")
        self._fall = MeasurementSnapshotFall(device, f"{self._cmd_syntax}:FALL")
        self._frequency = MeasurementSnapshotFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._high = MeasurementSnapshotHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = MeasurementSnapshotLow(device, f"{self._cmd_syntax}:LOW")
        self._maximum = MeasurementSnapshotMaximum(device, f"{self._cmd_syntax}:MAXimum")
        self._mean = MeasurementSnapshotMean(device, f"{self._cmd_syntax}:MEAN")
        self._minimum = MeasurementSnapshotMinimum(device, f"{self._cmd_syntax}:MINImum")
        self._nduty = MeasurementSnapshotNduty(device, f"{self._cmd_syntax}:NDUty")
        self._nedgecount = MeasurementSnapshotNedgecount(device, f"{self._cmd_syntax}:NEDGECount")
        self._novershoot = MeasurementSnapshotNovershoot(device, f"{self._cmd_syntax}:NOVershoot")
        self._npulsecount = MeasurementSnapshotNpulsecount(
            device, f"{self._cmd_syntax}:NPULSECount"
        )
        self._nwidth = MeasurementSnapshotNwidth(device, f"{self._cmd_syntax}:NWIdth")
        self._pduty = MeasurementSnapshotPduty(device, f"{self._cmd_syntax}:PDUty")
        self._pedgecount = MeasurementSnapshotPedgecount(device, f"{self._cmd_syntax}:PEDGECount")
        self._period = MeasurementSnapshotPeriod(device, f"{self._cmd_syntax}:PERIod")
        self._pk2pk = MeasurementSnapshotPk2pk(device, f"{self._cmd_syntax}:PK2Pk")
        self._povershoot = MeasurementSnapshotPovershoot(device, f"{self._cmd_syntax}:POVershoot")
        self._ppulsecount = MeasurementSnapshotPpulsecount(
            device, f"{self._cmd_syntax}:PPULSECount"
        )
        self._pwidth = MeasurementSnapshotPwidth(device, f"{self._cmd_syntax}:PWIdth")
        self._rise = MeasurementSnapshotRise(device, f"{self._cmd_syntax}:RISe")
        self._rms = MeasurementSnapshotRms(device, f"{self._cmd_syntax}:RMS")

    @property
    def amplitude(self) -> MeasurementSnapshotAmplitude:
        """Return the ``MEASUrement:SNAPShot:AMPlitude`` command.

        Description:
            - This query returns the amplitude value, in Volts, from the last snapshot taken of all
              measurements. Amplitude is the difference between the high value and the low value.
              The high and low values are queried using ``MEASUREMENT:SNAPSHOT:HIGH`` and
              ``MEASUREMENT:SNAPSHOT:LOW``. You can take a snapshot using ???? If a snapshot has not
              been executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:AMPlitude?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:AMPlitude?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:AMPlitude?
            ```
        """
        return self._amplitude

    @property
    def area(self) -> MeasurementSnapshotArea:
        """Return the ``MEASUrement:SNAPShot:AREa`` command.

        Description:
            - This query returns the area value, in Volt-seconds, from the last snapshot taken of
              all measurements. Area is the area under the curve, calculated by integrating the
              samples. In other words, Area (Volt-seconds) = (S 0 + S 1 + .. + S n ) x (sample
              interval) The area measured above ground is positive; the area measured below ground
              is negative. If a snapshot has not been executed, 0.0 is returned and no error event
              is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:AREa?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:AREa?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:AREa?
            ```
        """
        return self._area

    @property
    def burst(self) -> MeasurementSnapshotBurst:
        """Return the ``MEASUrement:SNAPShot:BURst`` command.

        Description:
            - This query returns the burst width value, in seconds, from the last snapshot taken of
              all measurements. Burst width is the time from the first mid-reference crossing to the
              last mid-reference crossing. If a snapshot has not been executed, 0.0 is returned and
              no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:BURst?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:BURst?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:BURst?
            ```
        """
        return self._burst

    @property
    def carea(self) -> MeasurementSnapshotCarea:
        """Return the ``MEASUrement:SNAPShot:CARea`` command.

        Description:
            - This query returns the cycle area value, in Volt-seconds, from the last snapshot taken
              of all measurements. Area is the area under the curve, calculated by integrating the
              samples. In other words, Area (Volt-seconds) = (S 0 + S 1 + .. + S n ) x (sample
              interval). The area measured above ground is positive; the area measured below ground
              is negative. If a snapshot has not been executed, 0.0 is returned and no error event
              is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:CARea?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:CARea?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:CARea?
            ```
        """
        return self._carea

    @property
    def cmean(self) -> MeasurementSnapshotCmean:
        """Return the ``MEASUrement:SNAPShot:CMEan`` command.

        Description:
            - This query returns the cycle mean value, in Volts, from the last snapshot taken of all
              measurements. Cycle mean is the arithmetic mean value, which is calculated over the
              first cycle. If a snapshot has not been executed, 0.0 is returned and no error event
              is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:CMEan?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:CMEan?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:CMEan?
            ```
        """
        return self._cmean

    @property
    def crms(self) -> MeasurementSnapshotCrms:
        """Return the ``MEASUrement:SNAPShot:CRMs`` command.

        Description:
            - This query returns the cycle root mean square (RMS) value, in Volts, from the last
              snapshot taken of all measurements. Cycle RMS is calculated over the first cycle. If a
              snapshot has not been executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:CRMs?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:CRMs?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:CRMs?
            ```
        """
        return self._crms

    @property
    def fall(self) -> MeasurementSnapshotFall:
        """Return the ``MEASUrement:SNAPShot:FALL`` command.

        Description:
            - This query returns the fall time value, in seconds, from the last snapshot taken of
              all measurements. Fall time is the time required for the first falling edge to fall
              from the high reference level to the low reference level. If a snapshot has not been
              executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:FALL?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:FALL?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:FALL?
            ```
        """
        return self._fall

    @property
    def frequency(self) -> MeasurementSnapshotFrequency:
        """Return the ``MEASUrement:SNAPShot:FREQuency`` command.

        Description:
            - This query returns the frequency value, in hertz, from the last snapshot taken of all
              measurements. Frequency is the reciprocal of the period. If a snapshot has not been
              executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:FREQuency?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:FREQuency?
            ```
        """
        return self._frequency

    @property
    def high(self) -> MeasurementSnapshotHigh:
        """Return the ``MEASUrement:SNAPShot:HIGH`` command.

        Description:
            - This query returns the high value, in Volts, from the last snapshot taken of all
              measurements. If the method used to calculate the 0% and 100% reference level (high
              and low) is Histogram, high is the highest density of points above the midpoint of the
              waveform. If the high-low method is min-max, high is equal to max. You can set and
              query the high-low method using ``MEASUREMENT:METHOD``. If a snapshot has not been
              executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:HIGH?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:HIGH?
            ```
        """
        return self._high

    @property
    def low(self) -> MeasurementSnapshotLow:
        """Return the ``MEASUrement:SNAPShot:LOW`` command.

        Description:
            - This query returns the low value, in Volts, from the last snapshot taken of all
              measurements. If the high-low method is Histogram, low is the lowest density of points
              below the midpoint of the waveform. If the high-low method is min-max, low is equal to
              min. You can set and query the high-low method using ``MEASUREMENT:METHOD``. If a
              snapshot has not been executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:LOW?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:LOW?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:LOW?
            ```
        """
        return self._low

    @property
    def maximum(self) -> MeasurementSnapshotMaximum:
        """Return the ``MEASUrement:SNAPShot:MAXimum`` command.

        Description:
            - This query returns the maximum value, in Volts, from the last snapshot taken of all
              measurements. If a snapshot has not been executed, 0.0 is returned and no error event
              is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:MAXimum?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:MAXimum?
            ```
        """
        return self._maximum

    @property
    def mean(self) -> MeasurementSnapshotMean:
        """Return the ``MEASUrement:SNAPShot:MEAN`` command.

        Description:
            - This query returns the mean value, in Volts, from the last snapshot taken of all
              measurements. If a snapshot has not been executed, 0.0 is returned and no error event
              is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:MEAN?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:MEAN?
            ```
        """
        return self._mean

    @property
    def minimum(self) -> MeasurementSnapshotMinimum:
        """Return the ``MEASUrement:SNAPShot:MINImum`` command.

        Description:
            - This query returns the minimum value, in Volts, from the last snapshot taken of all
              measurements. If a snapshot has not been executed, 0.0 is returned and no error event
              is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:MINImum?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:MINImum?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:MINImum?
            ```
        """
        return self._minimum

    @property
    def nduty(self) -> MeasurementSnapshotNduty:
        """Return the ``MEASUrement:SNAPShot:NDUty`` command.

        Description:
            - This query returns the negative duty cycle value from the last snapshot taken of all
              measurements. The negative duty cycle is the ratio of the negative pulse width to the
              period. The negative duty cycle is measured over the first cycle. If a snapshot has
              not been executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:NDUty?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:NDUty?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:NDUty?
            ```
        """
        return self._nduty

    @property
    def nedgecount(self) -> MeasurementSnapshotNedgecount:
        """Return the ``MEASUrement:SNAPShot:NEDGECount`` command.

        Description:
            - This query returns the falling edge count value from the last snapshot taken of all
              measurements. The falling edge count is the number of negative transitions from the
              high reference value to the low reference value. You can query the high and low
              reference values using ``MEASUREMENT:SNAPSHOT:HIGH`` and ``MEASUREMENT:SNAPSHOT:LOW``.
              If a snapshot has not been executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:NEDGECount?``
              query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:NEDGECount?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:NEDGECount?
            ```
        """
        return self._nedgecount

    @property
    def novershoot(self) -> MeasurementSnapshotNovershoot:
        """Return the ``MEASUrement:SNAPShot:NOVershoot`` command.

        Description:
            - This query returns the negative overshoot value from the last snapshot taken of all
              measurements. The negative overshoot is the difference between the minimum value and
              the low value, divided by the amplitude. You can query these values using
              ``MEASUREMENT:SNAPSHOT:MINIMUM``, ``MEASUREMENT:SNAPSHOT:LOW`` and
              ``MEASUREMENT:SNAPSHOT:AMPLITUDE``. If a snapshot has not been executed, 0.0 is
              returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:NOVershoot?``
              query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:NOVershoot?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:NOVershoot?
            ```
        """
        return self._novershoot

    @property
    def npulsecount(self) -> MeasurementSnapshotNpulsecount:
        """Return the ``MEASUrement:SNAPShot:NPULSECount`` command.

        Description:
            - This query returns the negative pulse count value from the last snapshot taken of all
              measurements. The negative pulse count is the number of negative pulses that fall
              below the mid reference level. You can set or query the mid reference level using
              ``MEASUREMENT:REFLEVEL:ABSOLUTE:MIDX`` or ``MEASUREMENT:REFLEVEL:PERCENT:MIDX``. ???
              If a snapshot has not been executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:NPULSECount?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:SNAPShot:NPULSECount?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:NPULSECount?
            ```
        """
        return self._npulsecount

    @property
    def nwidth(self) -> MeasurementSnapshotNwidth:
        """Return the ``MEASUrement:SNAPShot:NWIdth`` command.

        Description:
            - This query returns the negative pulse width value, in seconds, from the last snapshot
              taken of all measurements. The negative pulse width is the time between the mid
              reference crossings of the first negative pulse. If a snapshot has not been executed,
              0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:NWIdth?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:NWIdth?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:NWIdth?
            ```
        """
        return self._nwidth

    @property
    def pduty(self) -> MeasurementSnapshotPduty:
        """Return the ``MEASUrement:SNAPShot:PDUty`` command.

        Description:
            - This query returns the positive duty cycle value from the last snapshot taken of all
              measurements. The positive duty cycle is the ratio of the positive pulse width to the
              period. The negative duty cycle is measured over the first cycle. If a snapshot has
              not been executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PDUty?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:PDUty?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:PDUty?
            ```
        """
        return self._pduty

    @property
    def pedgecount(self) -> MeasurementSnapshotPedgecount:
        """Return the ``MEASUrement:SNAPShot:PEDGECount`` command.

        Description:
            - This query returns the rising edge count value from the last snapshot taken of all
              measurements. The rising edge count is the number of positive transitions from the low
              reference value to the high reference value. You can query the high and low reference
              values using ``MEASUREMENT:SNAPSHOT:HIGH`` and ``MEASUREMENT:SNAPSHOT:LOW``. If a
              snapshot has not been executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PEDGECount?``
              query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:PEDGECount?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:PEDGECount?
            ```
        """
        return self._pedgecount

    @property
    def period(self) -> MeasurementSnapshotPeriod:
        """Return the ``MEASUrement:SNAPShot:PERIod`` command.

        Description:
            - This query returns the period value from the last snapshot taken of all measurements.
              The period is the time required to complete the first cycle. The first cycle is the
              time between the first two positive crossings, or the first two negative crossings, at
              the mid reference level. If a snapshot has not been executed, 0.0 is returned and no
              error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PERIod?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:PERIod?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:PERIod?
            ```
        """
        return self._period

    @property
    def pk2pk(self) -> MeasurementSnapshotPk2pk:
        """Return the ``MEASUrement:SNAPShot:PK2Pk`` command.

        Description:
            - This query returns the peak-to-peak value from the last snapshot taken of all
              measurements. Peak-to-peak is the difference between the max value and the min value.
              You can query the max and min values using ``MEASUREMENT:SNAPSHOT:MAXIMUM`` and
              ``MEASUREMENT:SNAPSHOT:MINIMUM``. If a snapshot has not been executed, 0.0 is returned
              and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PK2Pk?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:PK2Pk?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:PK2Pk?
            ```
        """
        return self._pk2pk

    @property
    def povershoot(self) -> MeasurementSnapshotPovershoot:
        """Return the ``MEASUrement:SNAPShot:POVershoot`` command.

        Description:
            - This query returns the positive overshoot value from the last snapshot taken of all
              measurements. The positive overshoot is the difference between the max value and the
              high value, divided by Amplitude. You can query these values using
              ``MEASUREMENT:SNAPSHOT:MAXIMUM``, ``MEASUREMENT:SNAPSHOT:HIGH`` and
              ``MEASUREMENT:SNAPSHOT:AMPLITUDE``. If a snapshot has not been executed, 0.0 is
              returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:POVershoot?``
              query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:POVershoot?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:POVershoot?
            ```
        """
        return self._povershoot

    @property
    def ppulsecount(self) -> MeasurementSnapshotPpulsecount:
        """Return the ``MEASUrement:SNAPShot:PPULSECount`` command.

        Description:
            - This query returns the positive pulse count value from the last snapshot taken of all
              measurements. The positive pulse count is the number of positive pulses that rise
              above the mid reference level. If a snapshot has not been executed, 0.0 is returned
              and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PPULSECount?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASUrement:SNAPShot:PPULSECount?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:PPULSECount?
            ```
        """
        return self._ppulsecount

    @property
    def pwidth(self) -> MeasurementSnapshotPwidth:
        """Return the ``MEASUrement:SNAPShot:PWIdth`` command.

        Description:
            - This query returns the positive pulse width value, in seconds, from the last snapshot
              taken of all measurements. The positive pulse width is the time between the mid
              reference crossings of the first positive pulse. If a snapshot has not been executed,
              0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:PWIdth?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:PWIdth?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:PWIdth?
            ```
        """
        return self._pwidth

    @property
    def rise(self) -> MeasurementSnapshotRise:
        """Return the ``MEASUrement:SNAPShot:RISe`` command.

        Description:
            - This query returns the rise time value, in seconds, from the last snapshot taken of
              all measurements. The rise time is the time required for the first rising edge to rise
              from the low reference level to the high reference level. If a snapshot has not been
              executed, 0.0 is returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:RISe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:RISe?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:RISe?
            ```
        """
        return self._rise

    @property
    def rms(self) -> MeasurementSnapshotRms:
        """Return the ``MEASUrement:SNAPShot:RMS`` command.

        Description:
            - This query returns the true root mean square (RMS) value, in Volts, from the last
              snapshot taken of all measurements. If a snapshot has not been executed, 0.0 is
              returned and no error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:SNAPShot:RMS?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:SNAPShot:RMS?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASUrement:SNAPShot:RMS?
            ```
        """
        return self._rms


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
        - This command specifies the measurement type defined for the specified measurement slot.
          The measurement slot is specified by <x>, which ranges from 1 through 4. Digital channel
          measurements do not have a user-settable midRef threshold. If you specify a digital
          channel measurement that is not available, measurement error 2200: measurement system
          error occurs and 9.9e37 is returned.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|HITS|LOW|MAXimum|MEAN|MEDian|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PEAKHits|PDUty|PEDGECount|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS|SIGMA<x>|STDdev|TOVershoot|WAVEFORMS}
        - MEASUrement:MEAS<x>:TYPe?
        ```

    Info:
        - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it measures
          the high value less the low value measured over the entire waveform or gated region. This
          measurement is applicable only to the analog channels.
        - ``Amplitude = High - Low``
        - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
          region and is measured in volt-seconds. The area measured above the ground is positive,
          while the area below ground is negative. This measurement is applicable only to the analog
          channels.
        - ``BURst`` measures the duration of a burst. The measurement is made over the entire
          waveform or gated region.
        - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures, in
          volt-seconds, the area over the first cycle in the waveform or the first cycle in the
          gated region. The area measured above the common reference point is positive, while the
          area below the common reference point is negative. This measurement is applicable only to
          the analog channels.
        - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the waveform
          or the first cycle in the gated region. This measurement is applicable only to the analog
          channels.
        - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle in
          the waveform or the first cycle in the gated region. This measurement is applicable only
          to the analog channels.
        - ``DELay`` measures the time between the middle reference (default = 50%) amplitude point
          of the source waveform and the destination waveform. This measurement is applicable only
          to the analog channels.
        - ``FALL`` measures the time taken for the falling edge of the first pulse in the waveform
          or gated region to fall from a high reference value (default is 90%) to a low reference
          value (default is 10%). This measurement is applicable only to the analog channels.
        - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is the
          reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per second.
        - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a waveform.
          This measurement is applicable only to the analog channels.
        - ``HITS`` (histogram hits) measures the number of points in or on the histogram box.
        - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a waveform.
          This measurement is applicable only to the analog channels.
        - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
          found. It is measured over the entire waveform or gated region. This measurement is
          applicable only to the analog channels.
        - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or gated
          region. This measurement is applicable only to the analog channels.
        - ``MEDian`` (histogram measurement) measures the middle point of the histogram box. Half of
          all acquired points within or on the histogram box are less than this value and half are
          greater than this value.
        - ``MINImum`` finds the minimum amplitude. This value is typically the most negative peak
          voltage. It is measured over the entire waveform or gated region. This measurement is
          applicable only to the analog channels.
        - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
          period, expressed as a percentage. The duty cycle is measured on the first cycle in the
          waveform or gated region.
        - ``Negative Duty Cycle = ((Negative Width) / Period) × 100%``
        - ``NEDGECount`` is the count of negative edges.
        - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
          waveform or gated region. This measurement is applicable only to the analog channels.
        - ``Negative Overshoot = ((Low - Minimum) / Amplitude) × 100%)``
        - ``NPULSECount`` is the count of negative pulses.
        - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
          reference (default = 50%) amplitude points of a negative pulse. The measurement is made on
          the first pulse in the waveform or gated region.
        - ``PEAKHits`` measures the number of points in the largest bin of the histogram.
        - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
          period, expressed as a percentage. It is measured on the first cycle in the waveform or
          gated region.
        - ``Positive Duty Cycle = ((Positive Width)/Period) × 100%``
        - ``PEDGECount`` is the count of positive edges.
        - ``PERIod`` is the time required to complete the first cycle in a waveform or gated region.
          Period is the reciprocal of frequency and is measured in seconds.
        - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
          reference waveform) between two waveforms. The measurement is made between the middle
          reference points of the two waveforms and is expressed in degrees, where 360° represents
          one waveform cycle.
        - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
          amplitude in the entire waveform or gated region. This measurement is applicable only to
          the analog channels.
        - ``POVershoot`` is the positive overshoot value over the entire waveform or gated region.
          This measurement is applicable only to the analog channels.
        - ``Positive Overshoot = ((Maximum - High) / Amplitude) ×100%``
        - ``PPULSECount`` is the count of positive pulses.
        - ``PWIdth`` (positive width) is the distance (time) between the middle reference (default =
          50%) amplitude points of a positive pulse. The measurement is made on the first pulse in
          the waveform or gated region.
        - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the time
          it takes for the leading edge of the first pulse encountered to rise from a low reference
          value (default is 10%) to a high reference value (default is 90%). This measurement is
          applicable only to the analog channels.
        - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
          waveform or gated region. This measurement is applicable only to the analog channels.
        - ``SIGMA1`` (histogram measurement) measures the percentage of points in the histogram that
          are within one standard deviation of the histogram mean.
        - ``SIGMA2`` (histogram measurement) measures the percentage of points in the histogram that
          are within two standard deviations of the histogram mean.
        - ``SIGMA3`` (histogram measurement) measures the percentage of points in the histogram that
          are within three standard deviations of the histogram mean.
        - ``STDdev`` measures the standard deviation (Root Mean Square (RMS) deviation) of all
          acquired points within or on the histogram box.
        - ``TOVershoot`` (total overshoot) measures the sum of the positive and negative overshoot
          value over the entire waveform or gated region. This measurement is applicable only to the
          analog channels.
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


class MeasurementMeasItemSource1(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:MEAS<x>:SOUrce1`` command.

    Description:
        - For SOURce1: This command specifies the source for all single channel measurements. For
          delay or phase measurements, This command specifies the waveform to measure 'from'. This
          is equivalent to setting the 'From:' waveform in the 'Measure Delay' side menu or the
          'Measure Phase' side menu. SOUrce is equivalent to SOURCE1. For SOUrce2: This command
          specifies the waveform to measure 'to' when taking a delay measurement or phase
          measurement. This is equivalent to setting the 'To:' waveform in the 'Measure Delay' side
          menu or the 'Measure Phase' side menu. Measurements are specified by <x>, which ranges
          from 1 to 8.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1 value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|MATH|R<x>|D<x>|HIStogram|RF_AMPlitude|RF_FREQuency|RF_PHASe}
        - MEASUrement:MEAS<x>:SOUrce1?
        ```

    Info:
        - ``CH<x>`` is an analog channel to use as the source waveform. x has a minimum of 1 and a
          maximum of 4.
        - ``MATH`` is the math waveform.
        - ``REF<x>`` is a reference waveform to use as the source waveform. x has a minimum of 1 and
          a maximum of 4.
        - ``D<x>`` is a digital channel to use as the source waveform. (MSO/MDO4000/B models only as
          well as MDO3000 and MDO400C models with option MDO3MSO or MDO4MSO installed.) x has a
          minimum of 0 and a maximum of 15.
        - ``HIStogram`` indicates the histogram is the object to be measured. HIStogram only applies
          to SOUrce1; it is not allowed on SOUrce2.
        - ``RF_AMPlitude`` are the RF time domain traces. (MDO4000/B/C models only.).
        - ``RF_FREQuency`` are the RF time domain traces. (MDO4000/B/C models only.).
        - ``RF_PHASe`` are the RF time domain traces. (MDO4000/B/C models only.).
    """  # noqa: E501


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
    def source1(self) -> MeasurementMeasItemSource1:
        """Return the ``MEASUrement:MEAS<x>:SOUrce1`` command.

        Description:
            - For SOURce1: This command specifies the source for all single channel measurements.
              For delay or phase measurements, This command specifies the waveform to measure
              'from'. This is equivalent to setting the 'From:' waveform in the 'Measure Delay' side
              menu or the 'Measure Phase' side menu. SOUrce is equivalent to SOURCE1. For SOUrce2:
              This command specifies the waveform to measure 'to' when taking a delay measurement or
              phase measurement. This is equivalent to setting the 'To:' waveform in the 'Measure
              Delay' side menu or the 'Measure Phase' side menu. Measurements are specified by <x>,
              which ranges from 1 to 8.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:SOUrce1 {CH<x>|MATH|R<x>|D<x>|HIStogram|RF_AMPlitude|RF_FREQuency|RF_PHASe}
            - MEASUrement:MEAS<x>:SOUrce1?
            ```

        Info:
            - ``CH<x>`` is an analog channel to use as the source waveform. x has a minimum of 1 and
              a maximum of 4.
            - ``MATH`` is the math waveform.
            - ``REF<x>`` is a reference waveform to use as the source waveform. x has a minimum of 1
              and a maximum of 4.
            - ``D<x>`` is a digital channel to use as the source waveform. (MSO/MDO4000/B models
              only as well as MDO3000 and MDO400C models with option MDO3MSO or MDO4MSO installed.)
              x has a minimum of 0 and a maximum of 15.
            - ``HIStogram`` indicates the histogram is the object to be measured. HIStogram only
              applies to SOUrce1; it is not allowed on SOUrce2.
            - ``RF_AMPlitude`` are the RF time domain traces. (MDO4000/B/C models only.).
            - ``RF_FREQuency`` are the RF time domain traces. (MDO4000/B/C models only.).
            - ``RF_PHASe`` are the RF time domain traces. (MDO4000/B/C models only.).
        """  # noqa: E501
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
            - This command specifies the measurement type defined for the specified measurement
              slot. The measurement slot is specified by <x>, which ranges from 1 through 4. Digital
              channel measurements do not have a user-settable midRef threshold. If you specify a
              digital channel measurement that is not available, measurement error 2200: measurement
              system error occurs and 9.9e37 is returned.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:MEAS<x>:TYPe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:MEAS<x>:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|HITS|LOW|MAXimum|MEAN|MEDian|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PEAKHits|PDUty|PEDGECount|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS|SIGMA<x>|STDdev|TOVershoot|WAVEFORMS}
            - MEASUrement:MEAS<x>:TYPe?
            ```

        Info:
            - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it
              measures the high value less the low value measured over the entire waveform or gated
              region. This measurement is applicable only to the analog channels.
            - ``Amplitude = High - Low``
            - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
              region and is measured in volt-seconds. The area measured above the ground is
              positive, while the area below ground is negative. This measurement is applicable only
              to the analog channels.
            - ``BURst`` measures the duration of a burst. The measurement is made over the entire
              waveform or gated region.
            - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures, in
              volt-seconds, the area over the first cycle in the waveform or the first cycle in the
              gated region. The area measured above the common reference point is positive, while
              the area below the common reference point is negative. This measurement is applicable
              only to the analog channels.
            - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the
              waveform or the first cycle in the gated region. This measurement is applicable only
              to the analog channels.
            - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle
              in the waveform or the first cycle in the gated region. This measurement is applicable
              only to the analog channels.
            - ``DELay`` measures the time between the middle reference (default = 50%) amplitude
              point of the source waveform and the destination waveform. This measurement is
              applicable only to the analog channels.
            - ``FALL`` measures the time taken for the falling edge of the first pulse in the
              waveform or gated region to fall from a high reference value (default is 90%) to a low
              reference value (default is 10%). This measurement is applicable only to the analog
              channels.
            - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is
              the reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per
              second.
            - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a
              waveform. This measurement is applicable only to the analog channels.
            - ``HITS`` (histogram hits) measures the number of points in or on the histogram box.
            - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a
              waveform. This measurement is applicable only to the analog channels.
            - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
              found. It is measured over the entire waveform or gated region. This measurement is
              applicable only to the analog channels.
            - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or
              gated region. This measurement is applicable only to the analog channels.
            - ``MEDian`` (histogram measurement) measures the middle point of the histogram box.
              Half of all acquired points within or on the histogram box are less than this value
              and half are greater than this value.
            - ``MINImum`` finds the minimum amplitude. This value is typically the most negative
              peak voltage. It is measured over the entire waveform or gated region. This
              measurement is applicable only to the analog channels.
            - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
              period, expressed as a percentage. The duty cycle is measured on the first cycle in
              the waveform or gated region.
            - ``Negative Duty Cycle = ((Negative Width) / Period) × 100%``
            - ``NEDGECount`` is the count of negative edges.
            - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
              waveform or gated region. This measurement is applicable only to the analog channels.
            - ``Negative Overshoot = ((Low - Minimum) / Amplitude) × 100%)``
            - ``NPULSECount`` is the count of negative pulses.
            - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
              reference (default = 50%) amplitude points of a negative pulse. The measurement is
              made on the first pulse in the waveform or gated region.
            - ``PEAKHits`` measures the number of points in the largest bin of the histogram.
            - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
              period, expressed as a percentage. It is measured on the first cycle in the waveform
              or gated region.
            - ``Positive Duty Cycle = ((Positive Width)/Period) × 100%``
            - ``PEDGECount`` is the count of positive edges.
            - ``PERIod`` is the time required to complete the first cycle in a waveform or gated
              region. Period is the reciprocal of frequency and is measured in seconds.
            - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
              reference waveform) between two waveforms. The measurement is made between the middle
              reference points of the two waveforms and is expressed in degrees, where 360°
              represents one waveform cycle.
            - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
              amplitude in the entire waveform or gated region. This measurement is applicable only
              to the analog channels.
            - ``POVershoot`` is the positive overshoot value over the entire waveform or gated
              region. This measurement is applicable only to the analog channels.
            - ``Positive Overshoot = ((Maximum - High) / Amplitude) ×100%``
            - ``PPULSECount`` is the count of positive pulses.
            - ``PWIdth`` (positive width) is the distance (time) between the middle reference
              (default = 50%) amplitude points of a positive pulse. The measurement is made on the
              first pulse in the waveform or gated region.
            - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the
              time it takes for the leading edge of the first pulse encountered to rise from a low
              reference value (default is 10%) to a high reference value (default is 90%). This
              measurement is applicable only to the analog channels.
            - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
              waveform or gated region. This measurement is applicable only to the analog channels.
            - ``SIGMA1`` (histogram measurement) measures the percentage of points in the histogram
              that are within one standard deviation of the histogram mean.
            - ``SIGMA2`` (histogram measurement) measures the percentage of points in the histogram
              that are within two standard deviations of the histogram mean.
            - ``SIGMA3`` (histogram measurement) measures the percentage of points in the histogram
              that are within three standard deviations of the histogram mean.
            - ``STDdev`` measures the standard deviation (Root Mean Square (RMS) deviation) of all
              acquired points within or on the histogram box.
            - ``TOVershoot`` (total overshoot) measures the sum of the positive and negative
              overshoot value over the entire waveform or gated region. This measurement is
              applicable only to the analog channels.
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
        - This command specifies the immediate measurement type. Digital channel measurements do not
          have a user-settable midRef threshold. If you specify a digital channel measurement that
          is not available on models with 3-MSO option installed), measurement error 2200:
          measurement system error occurs and 9.91e37 (not a number) is returned.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:TYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:TYPe value`` command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|HITS|LOW|MAXimum|MEAN|MEDian|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PEAKHits|PEDGECount|PDUty|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS|SIGMA<x>|STDdev|TOVershoot|WAVEFORMS}
        - MEASUrement:IMMed:TYPe?
        ```

    Info:
        - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it measures
          the high value less the low value measured over the entire waveform or gated region. This
          measurement is applicable only to the analog channels.
        - ``Amplitude = High - Low``
        - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
          region and is measured in volt-seconds. The area measured above the ground is positive,
          while the area below ground is negative. This measurement is applicable only to the analog
          channels.
        - ``BURst`` measures the duration of a burst. The measurement is made over the entire
          waveform or gated region.
        - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures, in
          volt-seconds, the area over the first cycle in the waveform or the first cycle in the
          gated region. The area measured above the common reference point is positive, while the
          area below the common reference point is negative. This measurement is applicable only to
          the analog channels.
        - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the waveform
          or the first cycle in the gated region. This measurement is applicable only to the analog
          channels.
        - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle in
          the waveform or the first cycle in the gated region. This measurement is applicable only
          to the analog channels.
        - ``DELay`` measures the time between the middle reference (default = 50%) amplitude point
          of the source waveform and the destination waveform.
        - ``FALL`` measures the time taken for the falling edge of the first pulse in the waveform
          or gated region to fall from a high reference value (default is 90%) to a low reference
          value (default is 10%). This measurement is applicable only to the analog channels.
        - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is the
          reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per second.
        - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a waveform.
          This measurement is applicable only to the analog channels.
        - ``HITS`` (histogram hits) measures the number of points in or on the histogram box.
        - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a waveform.
          This measurement is applicable only to the analog channels.
        - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
          found. It is measured over the entire waveform or gated region. This measurement is
          applicable only to the analog channels.
        - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or gated
          region. This measurement is applicable only to the analog channels.
        - ``MEDian`` (histogram measurement) measures the middle point of the histogram box. Half of
          all acquired points within or on the histogram box are less than this value and half are
          greater than this value.
        - ``MINImum`` finds the minimum amplitude. This value is typically the most negative peak
          voltage. It is measured over the entire waveform or gated region. This measurement is
          applicable only to the analog channels.
        - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
          period, expressed as a percentage. The duty cycle is measured on the first cycle in the
          waveform or gated region.
        - ``Negative Duty Cycle = ((Negative Width) / Period) × 100%``
        - ``NEDGECount`` is the count of falling edges.
        - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
          waveform or gated region. This measurement is applicable only to the analog channels.
        - ``Negative Overshoot = ((Low - Minimum) / Amplitude) × 100%)``
        - ``NPULSECount`` is the count of negative pulses.
        - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
          reference (default = 50%) amplitude points of a negative pulse. The measurement is made on
          the first pulse in the waveform or gated region.
        - ``PEAKHits`` measures the number of points in the largest bin of the histogram.
        - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
          period, expressed as a percentage. It is measured on the first cycle in the waveform or
          gated region.
        - ``Positive Duty Cycle = ((Positive Width)/Period) × 100%``
        - ``PEDGECount`` is the count of rising edges.
        - ``PERIod`` is the time required to complete the first cycle in a waveform or gated region.
          Period is the reciprocal of frequency and is measured in seconds.
        - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
          reference waveform) between two waveforms. The measurement is made between the middle
          reference points of the two waveforms and is expressed in degrees, where 360° represents
          one waveform cycle.
        - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
          amplitude in the entire waveform or gated region. This measurement is applicable only to
          the analog channels.
        - ``POVershoot`` is the positive overshoot value over the entire waveform or gated region.
          This measurement is applicable only to the analog channels.
        - ``Positive Overshoot = ((Maximum - High) / Amplitude) ×100%``
        - ``PPULSECount`` is the count of positive pulses.
        - ``PWIdth`` (positive width) is the distance (time) between the middle reference (default =
          50%) amplitude points of a positive pulse. The measurement is made on the first pulse in
          the waveform or gated region.
        - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the time
          it takes for the leading edge of the first pulse encountered to rise from a low reference
          value (default is 10%) to a high reference value (default is 90%). This measurement is
          applicable only to the analog channels.
        - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
          waveform or gated region. This measurement is applicable only to the analog channels.
        - ``SIGMA1`` (histogram measurement) measures the percentage of points in the histogram that
          are within one standard deviation of the histogram mean.
        - ``SIGMA2`` (histogram measurement) measures the percentage of points in the histogram that
          are within two standard deviations of the histogram mean.
        - ``SIGMA3`` (histogram measurement) measures the percentage of points in the histogram that
          are within three standard deviations of the histogram mean.
        - ``STDdev`` measures the standard deviation (Root Mean Square (RMS) deviation) of all
          acquired points within or on the histogram box.
        - ``TOVershoot`` (total overshoot) (MDO models only) measures the sum of the positive and
          negative overshoot value over the entire waveform or gated region. This measurement is
          applicable only to the analog channels.
        - ``WAVEFORMS`` (waveform count) measures the number of waveforms used to calculate the
          histogram.
    """  # noqa: E501


class MeasurementImmedSource1(SCPICmdWrite, SCPICmdRead):
    """The ``MEASUrement:IMMed:SOUrce1`` command.

    Description:
        - For SOURce1: This command specifies the source for all single channel measurements. For
          delay or phase measurements, this command specifies the waveform to measure 'from'. This
          is equivalent to setting the 'From:' waveform in the 'Measure Delay' side menu or the
          'Measure Phase' side menu. SOUrce is equivalent to SOURCE1. For SOUrce2: This command
          specifies the waveform to measure 'to' when taking a delay measurement or phase
          measurement. This is equivalent to setting the 'To:' waveform in the 'Measure Delay' side
          menu or the 'Measure Phase' side menu.

    Usage:
        - Using the ``.query()`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:SOUrce1 value``
          command.

    SCPI Syntax:
        ```
        - MEASUrement:IMMed:SOUrce1 {CH<x>|MATH|D<x>|HIStogram|RF_AMPlitude|RF_FREQuency|RF_PHASe}
        - MEASUrement:IMMed:SOUrce1?
        ```

    Info:
        - ``CH<x>`` is the analog channel to use as the source waveform.
        - ``MATH`` is the math waveform.
        - ``D<x>`` is the digital waveform to use as the source waveform. (On models with option
          3-MSO installed.).
        - ``HIStogram`` indicates the histogram as the object to be measured. HIStogram only applies
          to SOUrce1; it is not available for SOUrce2.
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
        - ``.type``: The ``MEASUrement:IMMed:TYPe`` command.
        - ``.units``: The ``MEASUrement:IMMed:UNIts`` command.
        - ``.value``: The ``MEASUrement:IMMed:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delay = MeasurementImmedDelay(device, f"{self._cmd_syntax}:DELay")
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
    def source1(self) -> MeasurementImmedSource1:
        """Return the ``MEASUrement:IMMed:SOUrce1`` command.

        Description:
            - For SOURce1: This command specifies the source for all single channel measurements.
              For delay or phase measurements, this command specifies the waveform to measure
              'from'. This is equivalent to setting the 'From:' waveform in the 'Measure Delay' side
              menu or the 'Measure Phase' side menu. SOUrce is equivalent to SOURCE1. For SOUrce2:
              This command specifies the waveform to measure 'to' when taking a delay measurement or
              phase measurement. This is equivalent to setting the 'To:' waveform in the 'Measure
              Delay' side menu or the 'Measure Phase' side menu.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:SOUrce1?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:SOUrce1 {CH<x>|MATH|D<x>|HIStogram|RF_AMPlitude|RF_FREQuency|RF_PHASe}
            - MEASUrement:IMMed:SOUrce1?
            ```

        Info:
            - ``CH<x>`` is the analog channel to use as the source waveform.
            - ``MATH`` is the math waveform.
            - ``D<x>`` is the digital waveform to use as the source waveform. (On models with option
              3-MSO installed.).
            - ``HIStogram`` indicates the histogram as the object to be measured. HIStogram only
              applies to SOUrce1; it is not available for SOUrce2.
        """  # noqa: E501
        return self._source1

    @property
    def type(self) -> MeasurementImmedType:
        """Return the ``MEASUrement:IMMed:TYPe`` command.

        Description:
            - This command specifies the immediate measurement type. Digital channel measurements do
              not have a user-settable midRef threshold. If you specify a digital channel
              measurement that is not available on models with 3-MSO option installed), measurement
              error 2200: measurement system error occurs and 9.91e37 (not a number) is returned.

        Usage:
            - Using the ``.query()`` method will send the ``MEASUrement:IMMed:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASUrement:IMMed:TYPe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEASUrement:IMMed:TYPe value``
              command.

        SCPI Syntax:
            ```
            - MEASUrement:IMMed:TYPe {AMPlitude|AREa|BURst|CARea|CMEan|CRMs|DELay|FALL|FREQuency|HIGH|HITS|LOW|MAXimum|MEAN|MEDian|MINImum|NDUty|NEDGECount|NOVershoot|NPULSECount|NWIdth|PEAKHits|PEDGECount|PDUty|PERIod|PHAse|PK2Pk|POVershoot|PPULSECount|PWIdth|RISe|RMS|SIGMA<x>|STDdev|TOVershoot|WAVEFORMS}
            - MEASUrement:IMMed:TYPe?
            ```

        Info:
            - ``AMPlitude`` measures the amplitude of the selected waveform. In other words, it
              measures the high value less the low value measured over the entire waveform or gated
              region. This measurement is applicable only to the analog channels.
            - ``Amplitude = High - Low``
            - ``AREa`` measures the voltage over time. The area is over the entire waveform or gated
              region and is measured in volt-seconds. The area measured above the ground is
              positive, while the area below ground is negative. This measurement is applicable only
              to the analog channels.
            - ``BURst`` measures the duration of a burst. The measurement is made over the entire
              waveform or gated region.
            - ``CARea`` (cycle area) measures the voltage over time. In other words, it measures, in
              volt-seconds, the area over the first cycle in the waveform or the first cycle in the
              gated region. The area measured above the common reference point is positive, while
              the area below the common reference point is negative. This measurement is applicable
              only to the analog channels.
            - ``CMEan`` (cycle mean) measures the arithmetic mean over the first cycle in the
              waveform or the first cycle in the gated region. This measurement is applicable only
              to the analog channels.
            - ``CRMs`` (cycle rms) measures the true Root Mean Square voltage over the first cycle
              in the waveform or the first cycle in the gated region. This measurement is applicable
              only to the analog channels.
            - ``DELay`` measures the time between the middle reference (default = 50%) amplitude
              point of the source waveform and the destination waveform.
            - ``FALL`` measures the time taken for the falling edge of the first pulse in the
              waveform or gated region to fall from a high reference value (default is 90%) to a low
              reference value (default is 10%). This measurement is applicable only to the analog
              channels.
            - ``FREQuency`` measures the first cycle in the waveform or gated region. Frequency is
              the reciprocal of the period and is measured in hertz (Hz), where 1 Hz = 1 cycle per
              second.
            - ``HIGH`` measures the High reference (100% level, sometimes called Topline) of a
              waveform. This measurement is applicable only to the analog channels.
            - ``HITS`` (histogram hits) measures the number of points in or on the histogram box.
            - ``LOW`` measures the Low reference (0% level, sometimes called Baseline) of a
              waveform. This measurement is applicable only to the analog channels.
            - ``MAXimum`` finds the maximum amplitude. This value is the most positive peak voltage
              found. It is measured over the entire waveform or gated region. This measurement is
              applicable only to the analog channels.
            - ``MEAN`` amplitude measurement finds the arithmetic mean over the entire waveform or
              gated region. This measurement is applicable only to the analog channels.
            - ``MEDian`` (histogram measurement) measures the middle point of the histogram box.
              Half of all acquired points within or on the histogram box are less than this value
              and half are greater than this value.
            - ``MINImum`` finds the minimum amplitude. This value is typically the most negative
              peak voltage. It is measured over the entire waveform or gated region. This
              measurement is applicable only to the analog channels.
            - ``NDUty`` (negative duty cycle) is the ratio of the negative pulse width to the signal
              period, expressed as a percentage. The duty cycle is measured on the first cycle in
              the waveform or gated region.
            - ``Negative Duty Cycle = ((Negative Width) / Period) × 100%``
            - ``NEDGECount`` is the count of falling edges.
            - ``NOVershoot`` (negative overshoot) finds the negative overshoot value over the entire
              waveform or gated region. This measurement is applicable only to the analog channels.
            - ``Negative Overshoot = ((Low - Minimum) / Amplitude) × 100%)``
            - ``NPULSECount`` is the count of negative pulses.
            - ``NWIdth`` (negative width) measurement is the distance (time) between the middle
              reference (default = 50%) amplitude points of a negative pulse. The measurement is
              made on the first pulse in the waveform or gated region.
            - ``PEAKHits`` measures the number of points in the largest bin of the histogram.
            - ``PDUty`` (positive duty cycle) is the ratio of the positive pulse width to the signal
              period, expressed as a percentage. It is measured on the first cycle in the waveform
              or gated region.
            - ``Positive Duty Cycle = ((Positive Width)/Period) × 100%``
            - ``PEDGECount`` is the count of rising edges.
            - ``PERIod`` is the time required to complete the first cycle in a waveform or gated
              region. Period is the reciprocal of frequency and is measured in seconds.
            - ``PHAse`` measures the phase difference (amount of time a waveform leads or lags the
              reference waveform) between two waveforms. The measurement is made between the middle
              reference points of the two waveforms and is expressed in degrees, where 360°
              represents one waveform cycle.
            - ``PK2Pk`` (peak-to-peak) finds the absolute difference between the maximum and minimum
              amplitude in the entire waveform or gated region. This measurement is applicable only
              to the analog channels.
            - ``POVershoot`` is the positive overshoot value over the entire waveform or gated
              region. This measurement is applicable only to the analog channels.
            - ``Positive Overshoot = ((Maximum - High) / Amplitude) ×100%``
            - ``PPULSECount`` is the count of positive pulses.
            - ``PWIdth`` (positive width) is the distance (time) between the middle reference
              (default = 50%) amplitude points of a positive pulse. The measurement is made on the
              first pulse in the waveform or gated region.
            - ``RISe`` timing measurement finds the rise time of the waveform. The rise time is the
              time it takes for the leading edge of the first pulse encountered to rise from a low
              reference value (default is 10%) to a high reference value (default is 90%). This
              measurement is applicable only to the analog channels.
            - ``RMS`` amplitude measurement finds the true Root Mean Square voltage in the entire
              waveform or gated region. This measurement is applicable only to the analog channels.
            - ``SIGMA1`` (histogram measurement) measures the percentage of points in the histogram
              that are within one standard deviation of the histogram mean.
            - ``SIGMA2`` (histogram measurement) measures the percentage of points in the histogram
              that are within two standard deviations of the histogram mean.
            - ``SIGMA3`` (histogram measurement) measures the percentage of points in the histogram
              that are within three standard deviations of the histogram mean.
            - ``STDdev`` measures the standard deviation (Root Mean Square (RMS) deviation) of all
              acquired points within or on the histogram box.
            - ``TOVershoot`` (total overshoot) (MDO models only) measures the sum of the positive
              and negative overshoot value over the entire waveform or gated region. This
              measurement is applicable only to the analog channels.
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

        Sub-properties:
            - ``.amplitude``: The ``MEASUrement:SNAPShot:AMPlitude`` command.
            - ``.area``: The ``MEASUrement:SNAPShot:AREa`` command.
            - ``.burst``: The ``MEASUrement:SNAPShot:BURst`` command.
            - ``.carea``: The ``MEASUrement:SNAPShot:CARea`` command.
            - ``.cmean``: The ``MEASUrement:SNAPShot:CMEan`` command.
            - ``.crms``: The ``MEASUrement:SNAPShot:CRMs`` command.
            - ``.fall``: The ``MEASUrement:SNAPShot:FALL`` command.
            - ``.frequency``: The ``MEASUrement:SNAPShot:FREQuency`` command.
            - ``.high``: The ``MEASUrement:SNAPShot:HIGH`` command.
            - ``.low``: The ``MEASUrement:SNAPShot:LOW`` command.
            - ``.maximum``: The ``MEASUrement:SNAPShot:MAXimum`` command.
            - ``.mean``: The ``MEASUrement:SNAPShot:MEAN`` command.
            - ``.minimum``: The ``MEASUrement:SNAPShot:MINImum`` command.
            - ``.nduty``: The ``MEASUrement:SNAPShot:NDUty`` command.
            - ``.nedgecount``: The ``MEASUrement:SNAPShot:NEDGECount`` command.
            - ``.novershoot``: The ``MEASUrement:SNAPShot:NOVershoot`` command.
            - ``.npulsecount``: The ``MEASUrement:SNAPShot:NPULSECount`` command.
            - ``.nwidth``: The ``MEASUrement:SNAPShot:NWIdth`` command.
            - ``.pduty``: The ``MEASUrement:SNAPShot:PDUty`` command.
            - ``.pedgecount``: The ``MEASUrement:SNAPShot:PEDGECount`` command.
            - ``.period``: The ``MEASUrement:SNAPShot:PERIod`` command.
            - ``.pk2pk``: The ``MEASUrement:SNAPShot:PK2Pk`` command.
            - ``.povershoot``: The ``MEASUrement:SNAPShot:POVershoot`` command.
            - ``.ppulsecount``: The ``MEASUrement:SNAPShot:PPULSECount`` command.
            - ``.pwidth``: The ``MEASUrement:SNAPShot:PWIdth`` command.
            - ``.rise``: The ``MEASUrement:SNAPShot:RISe`` command.
            - ``.rms``: The ``MEASUrement:SNAPShot:RMS`` command.
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
            - ``.mode``: The ``MEASUrement:STATIstics:MODe`` command.
            - ``.weighting``: The ``MEASUrement:STATIstics:WEIghting`` command.
        """
        return self._statistics
