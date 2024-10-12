"""The measu commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MAXimum? <Qstring>
    - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MEAN? <Qstring>
    - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MINimum? <Qstring>
    - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:PK2PK? <Qstring>
    - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:POPUlation? <Qstring>
    - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:STDDev? <Qstring>
    - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MAXimum? <Qstring>
    - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MEAN? <Qstring>
    - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MINimum? <Qstring>
    - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:PK2PK? <Qstring>
    - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:POPUlation? <Qstring>
    - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:STDDev? <Qstring>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MeasuMeas1SubgroupResultsCurrentacqStddev(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:STDDev`` command.

    Description:
        - This query returns the standard deviation value of the measurement specified by the
          string, for the current acquisition.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:STDDev? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:STDDev? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:STDDev? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\| OUTPUT6\|OUTPUT7\|
          RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK \|RAIL1RMS
          \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL \|RAIL3FREQUENCY
          \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK \|RAIL4RMS
          \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL \|RAIL6FREQUENCY
          \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT \|RAIL7DPMUNDERSHOOT
          \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
    """


class MeasuMeas1SubgroupResultsCurrentacqPopulation(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:POPUlation`` command.

    Description:
        - This query returns the population value of the measurement specified by the string, for
          the current acquisition.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:POPUlation? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:POPUlation? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:POPUlation? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\| OUTPUT6\|OUTPUT7\|
          RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK \|RAIL1RMS
          \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL \|RAIL3FREQUENCY
          \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK \|RAIL4RMS
          \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL \|RAIL6FREQUENCY
          \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT \|RAIL7DPMUNDERSHOOT
          \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
    """


class MeasuMeas1SubgroupResultsCurrentacqPk2pk(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:PK2PK`` command.

    Description:
        - This query returns the peak-to-peak value of the measurement specified by the string, for
          the current acquisition.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:PK2PK? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:PK2PK? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:PK2PK? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\| OUTPUT6\|OUTPUT7\|
          RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK \|RAIL1RMS
          \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL \|RAIL3FREQUENCY
          \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK \|RAIL4RMS
          \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL \|RAIL6FREQUENCY
          \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT \|RAIL7DPMUNDERSHOOT
          \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
    """


class MeasuMeas1SubgroupResultsCurrentacqMinimum(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MINimum`` command.

    Description:
        - This query returns the minimum value of the measurement specified by the string, for the
          current acquisition.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MINimum? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MINimum? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MINimum? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\| OUTPUT6\|OUTPUT7\|
          RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK \|RAIL1RMS
          \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL \|RAIL3FREQUENCY
          \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK \|RAIL4RMS
          \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL \|RAIL6FREQUENCY
          \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT \|RAIL7DPMUNDERSHOOT
          \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
    """


class MeasuMeas1SubgroupResultsCurrentacqMean(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MEAN`` command.

    Description:
        - This query returns the mean value of the measurement specified by the string, for the
          current acquisition.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MEAN? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MEAN? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MEAN? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT \|OUTPUT1 \|OUTPUT2 \|OUTPUT3 \|OUTPUT4 \|OUTPUT5 \|OUTPUT6
          \|OUTPUT7 \|RAIL1DPMOVERSHOOT \|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
          \|RAIL1RMS \|RAIL1RMSFULL \|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
          \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS \|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
          \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK \|RAIL5RMS \|RAIL5RMSFULL
          \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
          \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL \|L2LPH1VRMS
          \|L2LPH1VCFactor \|L2LPH1TruePwr \|L2LPH1RePwr \|L2LPH1AppPwr \|L2LPH1PwrFactor
          \|L2LPH1PhaseDiff \|L2LPH1VPhase \|L2LPH2VRMS \|L2LPH2VCFactor \|L2LPH2TruePwr
          \|L2LPH2RePwr \|L2LPH2AppPwr \|L2LPH2PwrFactor \|L2LPH2PhaseDiff \|L2LPH2VPhase
          \|L2LPH3VRMS \|L2LPH3VCFactor \|L2LPH3TruePwr \|L2LPH3RePwr \|L2LPH3AppPwr
          \|L2LPH3PwrFactor \|L2LPH3PhaseDiff \|L2LPH3VPhase \|L2NPH1VRMS \|L2NPH1VCFactor
          \|L2NPH1TruePwr \|L2NPH1RePwr \|L2NPH1AppPwr \|L2NPH1PwrFactor \|L2NPH1PhaseDiff
          \|L2NPH1VPhase \|L2NPH2VRMS \|L2NPH2VCFactor \|L2NPH2TruePwr \|L2NPH2RePwr \|L2NPH2AppPwr
          \|L2NPH2PwrFactor \|L2NPH2PhaseDiff \|L2NPH2VPhase \|L2NPH3VRMS \|L2NPH3VCFactor
          \|L2NPH3TruePwr \|L2NPH3RePwr \|L2NPH3AppPwr \|L2NPH3PwrFactor \|L2NPH3PhaseDiff
          \|L2NPH3VPhase \|PH1IRMS \|PH1IPhase \|PH1ICFactor \|PH2IRMS \|PH2IPhase \|PH2ICFactor
          \|PH3IRMS \|PH3IPhase \|PH3ICFactor \|Frequency \|L2LPH1F1Mag \|L2LPH1F3Mag \|L2LPH1THDF
          \|L2LPH1THDR \|L2LPH1RMS \|L2LPH1IRMS \|L2LPH1Status \|L2LPH1HarmonicsNumber
          \|L2LPH1Frequency \|L2LPH1MagnitudeAbs \|L2LPH1MagnitudePct \|L2LPH1Phase \|L2LPH1Limits
          \|L2LPH1PassFail \|L2LPH1Margin \|L2LPH2F1Mag \|L2LPH2F3Mag \|L2LPH2THDF \|L2LPH2THDR
          \|L2LPH2RMS \|L2LPH2IRMS \|L2LPH2Status \|L2LPH2HarmonicsNumber \|L2LPH2Frequency
          \|L2LPH2MagnitudeAbs \|L2LPH2MagnitudePct \|L2LPH2Phase \|L2LPH2Limits \|L2LPH2PassFail
          \|L2LPH2Margin \|L2LPH3F1Mag \|L2LPH3F3Mag \|L2LPH3THDF \|L2LPH3THDR \|L2LPH3RMS
          \|L2LPH3IRMS \|L2LPH3Status \|L2LPH3HarmonicsNumber \|L2LPH3Frequency \|L2LPH3MagnitudeAbs
          \|L2LPH3MagnitudePct \|L2LPH3Phase \|L2LPH3Limits \|L2LPH3PassFail \|L2LPH3Margin
          \|L2NPH1F1Mag \|L2NPH1F3Mag \|L2NPH1THDF \|L2NPH1THDR \|L2NPH1RMS \|L2NPH1IRMS
          \|L2NPH1Status \|L2NPH1HarmonicsNumber \|L2NPH1Frequency \|L2NPH1MagnitudeAbs
          \|L2NPH1MagnitudePct \|L2NPH1Phase\|L2NPH1Limits \|L2NPH1PassFail\|L2NPH1Margin
          \|L2NPH2F1Mag\|L2NPH2F3Mag \|L2NPH2THDF\|L2NPH2THDR \|L2NPH2RMS\|L2NPH2IRMS \|L2NPH2Status
          \|L2NPH2HarmonicsNumber \|L2NPH2Frequency \|L2NPH2MagnitudeAbs \|L2NPH2MagnitudePct
          \|L2NPH2Phase\|L2NPH2Limits \|L2NPH2PassFail\|L2NPH2Margin \|L2NPH3F1Mag \|L2NPH3F3Mag
          \|L2NPH3THDF \|L2NPH3THDR \|L2NPH3RMS \|L2NPH3IRMS \|L2NPH3Status \|L2NPH3HarmonicsNumber
          \|L2NPH3Frequency \|L2NPH3MagnitudeAbs \|L2NPH3MagnitudePct \|L2NPH3Phase \|L2NPH3Limits
          \|L2NPH3PassFail \|L2NPH3Margin \|ORDER\|PH1INPwr \|PH1OUTPwr \|PH1Efficiency \|PH2INPwr
          \|PH2OUTPwr \|PH2Efficiency \|TotalEfficiency \|PH1LRIPRMS \|PH1LRIPPK2PK \|PH2LRIPRMS
          \|PH2LRIPPK2PK \|PH3LRIPRMS \|PH3LRIPPK2PK \|PH1SWRIPRMS \|PH1SWRIPPK2PK \|PH2SWRIPRMS
          \|PH2SWRIPPK2PK \|PH3SWRIPRMS \|PH3SWRIPPK2PK \|TruePwrSum \|RePwrSum \|AppPwrSum
          \|InPwrSum \|OutPwrSum.
    """


class MeasuMeas1SubgroupResultsCurrentacqMaximum(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MAXimum`` command.

    Description:
        - This query returns the maximum value of the measurement specified by the string, for the
          current acquisition.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MAXimum? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MAXimum? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MAXimum? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\| OUTPUT6\|OUTPUT7\|
          RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK \|RAIL1RMS
          \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL \|RAIL3FREQUENCY
          \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK \|RAIL4RMS
          \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL \|RAIL6FREQUENCY
          \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT \|RAIL7DPMUNDERSHOOT
          \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
    """


class MeasuMeas1SubgroupResultsCurrentacq(SCPICmdRead):
    """The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.maximum``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MAXimum`` command.
        - ``.mean``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MEAN`` command.
        - ``.minimum``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MINimum`` command.
        - ``.pk2pk``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:PK2PK`` command.
        - ``.population``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:POPUlation`` command.
        - ``.stddev``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:STDDev`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._maximum = MeasuMeas1SubgroupResultsCurrentacqMaximum(
            device, f"{self._cmd_syntax}:MAXimum"
        )
        self._mean = MeasuMeas1SubgroupResultsCurrentacqMean(device, f"{self._cmd_syntax}:MEAN")
        self._minimum = MeasuMeas1SubgroupResultsCurrentacqMinimum(
            device, f"{self._cmd_syntax}:MINimum"
        )
        self._pk2pk = MeasuMeas1SubgroupResultsCurrentacqPk2pk(device, f"{self._cmd_syntax}:PK2PK")
        self._population = MeasuMeas1SubgroupResultsCurrentacqPopulation(
            device, f"{self._cmd_syntax}:POPUlation"
        )
        self._stddev = MeasuMeas1SubgroupResultsCurrentacqStddev(
            device, f"{self._cmd_syntax}:STDDev"
        )

    @property
    def maximum(self) -> MeasuMeas1SubgroupResultsCurrentacqMaximum:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MAXimum`` command.

        Description:
            - This query returns the maximum value of the measurement specified by the string, for
              the current acquisition.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MAXimum? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MAXimum? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MAXimum? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\|
              OUTPUT6\|OUTPUT7\| RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
        """
        return self._maximum

    @property
    def mean(self) -> MeasuMeas1SubgroupResultsCurrentacqMean:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MEAN`` command.

        Description:
            - This query returns the mean value of the measurement specified by the string, for the
              current acquisition.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MEAN? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MEAN? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MEAN? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT \|OUTPUT1 \|OUTPUT2 \|OUTPUT3 \|OUTPUT4 \|OUTPUT5 \|OUTPUT6
              \|OUTPUT7 \|RAIL1DPMOVERSHOOT \|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL \|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS \|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK \|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL
              \|L2LPH1VRMS \|L2LPH1VCFactor \|L2LPH1TruePwr \|L2LPH1RePwr \|L2LPH1AppPwr
              \|L2LPH1PwrFactor \|L2LPH1PhaseDiff \|L2LPH1VPhase \|L2LPH2VRMS \|L2LPH2VCFactor
              \|L2LPH2TruePwr \|L2LPH2RePwr \|L2LPH2AppPwr \|L2LPH2PwrFactor \|L2LPH2PhaseDiff
              \|L2LPH2VPhase \|L2LPH3VRMS \|L2LPH3VCFactor \|L2LPH3TruePwr \|L2LPH3RePwr
              \|L2LPH3AppPwr \|L2LPH3PwrFactor \|L2LPH3PhaseDiff \|L2LPH3VPhase \|L2NPH1VRMS
              \|L2NPH1VCFactor \|L2NPH1TruePwr \|L2NPH1RePwr \|L2NPH1AppPwr \|L2NPH1PwrFactor
              \|L2NPH1PhaseDiff \|L2NPH1VPhase \|L2NPH2VRMS \|L2NPH2VCFactor \|L2NPH2TruePwr
              \|L2NPH2RePwr \|L2NPH2AppPwr \|L2NPH2PwrFactor \|L2NPH2PhaseDiff \|L2NPH2VPhase
              \|L2NPH3VRMS \|L2NPH3VCFactor \|L2NPH3TruePwr \|L2NPH3RePwr \|L2NPH3AppPwr
              \|L2NPH3PwrFactor \|L2NPH3PhaseDiff \|L2NPH3VPhase \|PH1IRMS \|PH1IPhase \|PH1ICFactor
              \|PH2IRMS \|PH2IPhase \|PH2ICFactor \|PH3IRMS \|PH3IPhase \|PH3ICFactor \|Frequency
              \|L2LPH1F1Mag \|L2LPH1F3Mag \|L2LPH1THDF \|L2LPH1THDR \|L2LPH1RMS \|L2LPH1IRMS
              \|L2LPH1Status \|L2LPH1HarmonicsNumber \|L2LPH1Frequency \|L2LPH1MagnitudeAbs
              \|L2LPH1MagnitudePct \|L2LPH1Phase \|L2LPH1Limits \|L2LPH1PassFail \|L2LPH1Margin
              \|L2LPH2F1Mag \|L2LPH2F3Mag \|L2LPH2THDF \|L2LPH2THDR \|L2LPH2RMS \|L2LPH2IRMS
              \|L2LPH2Status \|L2LPH2HarmonicsNumber \|L2LPH2Frequency \|L2LPH2MagnitudeAbs
              \|L2LPH2MagnitudePct \|L2LPH2Phase \|L2LPH2Limits \|L2LPH2PassFail \|L2LPH2Margin
              \|L2LPH3F1Mag \|L2LPH3F3Mag \|L2LPH3THDF \|L2LPH3THDR \|L2LPH3RMS \|L2LPH3IRMS
              \|L2LPH3Status \|L2LPH3HarmonicsNumber \|L2LPH3Frequency \|L2LPH3MagnitudeAbs
              \|L2LPH3MagnitudePct \|L2LPH3Phase \|L2LPH3Limits \|L2LPH3PassFail \|L2LPH3Margin
              \|L2NPH1F1Mag \|L2NPH1F3Mag \|L2NPH1THDF \|L2NPH1THDR \|L2NPH1RMS \|L2NPH1IRMS
              \|L2NPH1Status \|L2NPH1HarmonicsNumber \|L2NPH1Frequency \|L2NPH1MagnitudeAbs
              \|L2NPH1MagnitudePct \|L2NPH1Phase\|L2NPH1Limits \|L2NPH1PassFail\|L2NPH1Margin
              \|L2NPH2F1Mag\|L2NPH2F3Mag \|L2NPH2THDF\|L2NPH2THDR \|L2NPH2RMS\|L2NPH2IRMS
              \|L2NPH2Status \|L2NPH2HarmonicsNumber \|L2NPH2Frequency \|L2NPH2MagnitudeAbs
              \|L2NPH2MagnitudePct \|L2NPH2Phase\|L2NPH2Limits \|L2NPH2PassFail\|L2NPH2Margin
              \|L2NPH3F1Mag \|L2NPH3F3Mag \|L2NPH3THDF \|L2NPH3THDR \|L2NPH3RMS \|L2NPH3IRMS
              \|L2NPH3Status \|L2NPH3HarmonicsNumber \|L2NPH3Frequency \|L2NPH3MagnitudeAbs
              \|L2NPH3MagnitudePct \|L2NPH3Phase \|L2NPH3Limits \|L2NPH3PassFail \|L2NPH3Margin
              \|ORDER\|PH1INPwr \|PH1OUTPwr \|PH1Efficiency \|PH2INPwr \|PH2OUTPwr \|PH2Efficiency
              \|TotalEfficiency \|PH1LRIPRMS \|PH1LRIPPK2PK \|PH2LRIPRMS \|PH2LRIPPK2PK \|PH3LRIPRMS
              \|PH3LRIPPK2PK \|PH1SWRIPRMS \|PH1SWRIPPK2PK \|PH2SWRIPRMS \|PH2SWRIPPK2PK
              \|PH3SWRIPRMS \|PH3SWRIPPK2PK \|TruePwrSum \|RePwrSum \|AppPwrSum \|InPwrSum
              \|OutPwrSum.
        """
        return self._mean

    @property
    def minimum(self) -> MeasuMeas1SubgroupResultsCurrentacqMinimum:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MINimum`` command.

        Description:
            - This query returns the minimum value of the measurement specified by the string, for
              the current acquisition.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MINimum? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MINimum? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MINimum? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\|
              OUTPUT6\|OUTPUT7\| RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
        """
        return self._minimum

    @property
    def pk2pk(self) -> MeasuMeas1SubgroupResultsCurrentacqPk2pk:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:PK2PK`` command.

        Description:
            - This query returns the peak-to-peak value of the measurement specified by the string,
              for the current acquisition.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:PK2PK? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:PK2PK? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:PK2PK? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\|
              OUTPUT6\|OUTPUT7\| RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
        """
        return self._pk2pk

    @property
    def population(self) -> MeasuMeas1SubgroupResultsCurrentacqPopulation:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:POPUlation`` command.

        Description:
            - This query returns the population value of the measurement specified by the string,
              for the current acquisition.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:POPUlation? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:POPUlation? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:POPUlation? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\|
              OUTPUT6\|OUTPUT7\| RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
        """
        return self._population

    @property
    def stddev(self) -> MeasuMeas1SubgroupResultsCurrentacqStddev:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:STDDev`` command.

        Description:
            - This query returns the standard deviation value of the measurement specified by the
              string, for the current acquisition.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:STDDev? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:STDDev? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:STDDev? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\|
              OUTPUT6\|OUTPUT7\| RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
        """
        return self._stddev


class MeasuMeas1SubgroupResultsAllacqsStddev(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:STDDev`` command.

    Description:
        - This query returns the standard deviation value of the measurement specified by the
          string, for all acquisitions.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:STDDev? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:STDDev? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:STDDev? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\| OUTPUT6\|OUTPUT7\|
          RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK \|RAIL1RMS
          \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL \|RAIL3FREQUENCY
          \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK \|RAIL4RMS
          \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL \|RAIL6FREQUENCY
          \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT \|RAIL7DPMUNDERSHOOT
          \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
    """


class MeasuMeas1SubgroupResultsAllacqsPopulation(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:POPUlation`` command.

    Description:
        - This query returns the population value of the measurement specified by the string, for
          all acquisitions.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:POPUlation? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:POPUlation? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:POPUlation? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\| OUTPUT6\|OUTPUT7\|
          RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK \|RAIL1RMS
          \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL \|RAIL3FREQUENCY
          \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK \|RAIL4RMS
          \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL \|RAIL6FREQUENCY
          \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT \|RAIL7DPMUNDERSHOOT
          \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
    """


class MeasuMeas1SubgroupResultsAllacqsPk2pk(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:PK2PK`` command.

    Description:
        - This query returns the peak-to-peak value of the measurement specified by the string, for
          all acquisitions.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:PK2PK? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:PK2PK? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:PK2PK? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\| OUTPUT6\|OUTPUT7\|
          RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK \|RAIL1RMS
          \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL \|RAIL3FREQUENCY
          \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK \|RAIL4RMS
          \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL \|RAIL6FREQUENCY
          \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT \|RAIL7DPMUNDERSHOOT
          \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
    """


class MeasuMeas1SubgroupResultsAllacqsMinimum(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MINimum`` command.

    Description:
        - This query returns the minimum value of the measurement specified by the string, for all
          acquisitions.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MINimum? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MINimum? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MINimum? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\| OUTPUT6\|OUTPUT7\|
          RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK \|RAIL1RMS
          \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL \|RAIL3FREQUENCY
          \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK \|RAIL4RMS
          \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL \|RAIL6FREQUENCY
          \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT \|RAIL7DPMUNDERSHOOT
          \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
    """


class MeasuMeas1SubgroupResultsAllacqsMean(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MEAN`` command.

    Description:
        - This query returns the mean value of the measurement specified by the string, for all
          acquisitions.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MEAN? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MEAN? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MEAN? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\| OUTPUT6\|OUTPUT7\|
          RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK \|RAIL1RMS
          \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL \|RAIL3FREQUENCY
          \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK \|RAIL4RMS
          \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL \|RAIL6FREQUENCY
          \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT \|RAIL7DPMUNDERSHOOT
          \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
    """


class MeasuMeas1SubgroupResultsAllacqsMaximum(SCPICmdReadWithArguments):
    r"""The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MAXimum`` command.

    Description:
        - This query returns the maximum value of the measurement specified by the string, for all
          acquisitions.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MAXimum? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MAXimum? argument`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MAXimum? <Qstring>
        ```

    Info:
        - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\| OUTPUT6\|OUTPUT7\|
          RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK \|RAIL1RMS
          \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL \|RAIL3FREQUENCY
          \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK \|RAIL4RMS
          \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL \|RAIL6FREQUENCY
          \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT \|RAIL7DPMUNDERSHOOT
          \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
    """


class MeasuMeas1SubgroupResultsAllacqs(SCPICmdRead):
    """The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.maximum``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MAXimum`` command.
        - ``.mean``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MEAN`` command.
        - ``.minimum``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MINimum`` command.
        - ``.pk2pk``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:PK2PK`` command.
        - ``.population``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:POPUlation`` command.
        - ``.stddev``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:STDDev`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._maximum = MeasuMeas1SubgroupResultsAllacqsMaximum(
            device, f"{self._cmd_syntax}:MAXimum"
        )
        self._mean = MeasuMeas1SubgroupResultsAllacqsMean(device, f"{self._cmd_syntax}:MEAN")
        self._minimum = MeasuMeas1SubgroupResultsAllacqsMinimum(
            device, f"{self._cmd_syntax}:MINimum"
        )
        self._pk2pk = MeasuMeas1SubgroupResultsAllacqsPk2pk(device, f"{self._cmd_syntax}:PK2PK")
        self._population = MeasuMeas1SubgroupResultsAllacqsPopulation(
            device, f"{self._cmd_syntax}:POPUlation"
        )
        self._stddev = MeasuMeas1SubgroupResultsAllacqsStddev(device, f"{self._cmd_syntax}:STDDev")

    @property
    def maximum(self) -> MeasuMeas1SubgroupResultsAllacqsMaximum:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MAXimum`` command.

        Description:
            - This query returns the maximum value of the measurement specified by the string, for
              all acquisitions.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MAXimum? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MAXimum? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MAXimum? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\|
              OUTPUT6\|OUTPUT7\| RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
        """
        return self._maximum

    @property
    def mean(self) -> MeasuMeas1SubgroupResultsAllacqsMean:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MEAN`` command.

        Description:
            - This query returns the mean value of the measurement specified by the string, for all
              acquisitions.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MEAN? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MEAN? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MEAN? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\|
              OUTPUT6\|OUTPUT7\| RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
        """
        return self._mean

    @property
    def minimum(self) -> MeasuMeas1SubgroupResultsAllacqsMinimum:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MINimum`` command.

        Description:
            - This query returns the minimum value of the measurement specified by the string, for
              all acquisitions.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MINimum? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MINimum? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MINimum? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\|
              OUTPUT6\|OUTPUT7\| RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
        """
        return self._minimum

    @property
    def pk2pk(self) -> MeasuMeas1SubgroupResultsAllacqsPk2pk:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:PK2PK`` command.

        Description:
            - This query returns the peak-to-peak value of the measurement specified by the string,
              for all acquisitions.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:PK2PK? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:PK2PK? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:PK2PK? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\|
              OUTPUT6\|OUTPUT7\| RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
        """
        return self._pk2pk

    @property
    def population(self) -> MeasuMeas1SubgroupResultsAllacqsPopulation:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:POPUlation`` command.

        Description:
            - This query returns the population value of the measurement specified by the string,
              for all acquisitions.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:POPUlation? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:POPUlation? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:POPUlation? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\|
              OUTPUT6\|OUTPUT7\| RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
        """
        return self._population

    @property
    def stddev(self) -> MeasuMeas1SubgroupResultsAllacqsStddev:
        r"""Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:STDDev`` command.

        Description:
            - This query returns the standard deviation value of the measurement specified by the
              string, for all acquisitions.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:STDDev? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:STDDev? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:STDDev? <Qstring>
            ```

        Info:
            - ``<Qstring>`` = INPUT\|OUTPUT1\|OUTPUT2\|OUTPUT3\|OUTPUT4\|OUTPUT5\|
              OUTPUT6\|OUTPUT7\| RAIL1DPMOVERSHOOT\|RAIL1DPMUNDERSHOOT \|RAIL1FREQUENCY \|RAIL1PK2PK
              \|RAIL1RMS \|RAIL1RMSFULL\|RAIL2FREQUENCY \|RAIL2PK2PK \|RAIL2RMS \|RAIL2RMSFULL
              \|RAIL3FREQUENCY \|RAIL3PK2PK \|RAIL3RMS\|RAIL3RMSFULL \|RAIL4FREQUENCY \|RAIL4PK2PK
              \|RAIL4RMS \|RAIL4RMSFULL \|RAIL5FREQUENCY \|RAIL5PK2PK\|RAIL5RMS \|RAIL5RMSFULL
              \|RAIL6FREQUENCY \|RAIL6PK2PK \|RAIL6RMS \|RAIL6RMSFULL \|RAIL7DPMOVERSHOOT
              \|RAIL7DPMUNDERSHOOT \|RAIL7FREQUENCY \|RAIL7PK2PK \|RAIL7RMS \|RAIL7RMSFULL.
        """
        return self._stddev


class MeasuMeas1SubgroupResults(SCPICmdRead):
    """The ``MEASU:MEAS1:SUBGROUP:RESUlts`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASU:MEAS1:SUBGROUP:RESUlts?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASU:MEAS1:SUBGROUP:RESUlts?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.allacqs``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs`` command tree.
        - ``.currentacq``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._allacqs = MeasuMeas1SubgroupResultsAllacqs(device, f"{self._cmd_syntax}:ALLAcqs")
        self._currentacq = MeasuMeas1SubgroupResultsCurrentacq(
            device, f"{self._cmd_syntax}:CURRentacq"
        )

    @property
    def allacqs(self) -> MeasuMeas1SubgroupResultsAllacqs:
        """Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.maximum``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MAXimum`` command.
            - ``.mean``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MEAN`` command.
            - ``.minimum``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:MINimum`` command.
            - ``.pk2pk``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:PK2PK`` command.
            - ``.population``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:POPUlation`` command.
            - ``.stddev``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs:STDDev`` command.
        """
        return self._allacqs

    @property
    def currentacq(self) -> MeasuMeas1SubgroupResultsCurrentacq:
        """Return the ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.maximum``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MAXimum`` command.
            - ``.mean``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MEAN`` command.
            - ``.minimum``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:MINimum`` command.
            - ``.pk2pk``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:PK2PK`` command.
            - ``.population``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:POPUlation`` command.
            - ``.stddev``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq:STDDev`` command.
        """
        return self._currentacq


class MeasuMeas1Subgroup(SCPICmdRead):
    """The ``MEASU:MEAS1:SUBGROUP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASU:MEAS1:SUBGROUP?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASU:MEAS1:SUBGROUP?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.results``: The ``MEASU:MEAS1:SUBGROUP:RESUlts`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._results = MeasuMeas1SubgroupResults(device, f"{self._cmd_syntax}:RESUlts")

    @property
    def results(self) -> MeasuMeas1SubgroupResults:
        """Return the ``MEASU:MEAS1:SUBGROUP:RESUlts`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASU:MEAS1:SUBGROUP:RESUlts?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASU:MEAS1:SUBGROUP:RESUlts?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.allacqs``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:ALLAcqs`` command tree.
            - ``.currentacq``: The ``MEASU:MEAS1:SUBGROUP:RESUlts:CURRentacq`` command tree.
        """
        return self._results


class MeasuMeas1(SCPICmdRead):
    """The ``MEASU:MEAS1`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASU:MEAS1?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASU:MEAS1?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.subgroup``: The ``MEASU:MEAS1:SUBGROUP`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._subgroup = MeasuMeas1Subgroup(device, f"{self._cmd_syntax}:SUBGROUP")

    @property
    def subgroup(self) -> MeasuMeas1Subgroup:
        """Return the ``MEASU:MEAS1:SUBGROUP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASU:MEAS1:SUBGROUP?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASU:MEAS1:SUBGROUP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.results``: The ``MEASU:MEAS1:SUBGROUP:RESUlts`` command tree.
        """
        return self._subgroup


class Measu(SCPICmdRead):
    """The ``MEASU`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEASU?`` query.
        - Using the ``.verify(value)`` method will send the ``MEASU?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.meas1``: The ``MEASU:MEAS1`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MEASU") -> None:
        super().__init__(device, cmd_syntax)
        self._meas1 = MeasuMeas1(device, f"{self._cmd_syntax}:MEAS1")

    @property
    def meas1(self) -> MeasuMeas1:
        """Return the ``MEASU:MEAS1`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEASU:MEAS1?`` query.
            - Using the ``.verify(value)`` method will send the ``MEASU:MEAS1?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.subgroup``: The ``MEASU:MEAS1:SUBGROUP`` command tree.
        """
        return self._meas1
