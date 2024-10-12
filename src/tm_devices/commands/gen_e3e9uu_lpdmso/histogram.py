# pylint: disable=line-too-long
"""The histogram commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HISTogram:ADDNew <QString>
    - HISTogram:DELETEALL
    - HISTogram:DELete <QString>
    - HISTogram:HISTogram<x>:BOX <NR3>,<NR3>,<NR3>,<NR3>
    - HISTogram:HISTogram<x>:BOX?
    - HISTogram:HISTogram<x>:BSTate {ON|OFF}
    - HISTogram:HISTogram<x>:BSTate?
    - HISTogram:HISTogram<x>:DATa?
    - HISTogram:HISTogram<x>:DISPlay {LINEAr|LOG}
    - HISTogram:HISTogram<x>:DISPlay?
    - HISTogram:HISTogram<x>:FUNCtion {HORizontal|VERTical}
    - HISTogram:HISTogram<x>:FUNCtion?
    - HISTogram:HISTogram<x>:MEASurement:COUNt {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:COUNt?
    - HISTogram:HISTogram<x>:MEASurement:HITS {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:HITS?
    - HISTogram:HISTogram<x>:MEASurement:MAX {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:MAX?
    - HISTogram:HISTogram<x>:MEASurement:MEAN {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:MEAN?
    - HISTogram:HISTogram<x>:MEASurement:MEDian {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:MEDian?
    - HISTogram:HISTogram<x>:MEASurement:MIN {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:MIN?
    - HISTogram:HISTogram<x>:MEASurement:MODE {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:MODE?
    - HISTogram:HISTogram<x>:MEASurement:ONESigma {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:ONESigma?
    - HISTogram:HISTogram<x>:MEASurement:PHITs {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:PHITs?
    - HISTogram:HISTogram<x>:MEASurement:PK2PK {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:PK2PK?
    - HISTogram:HISTogram<x>:MEASurement:RESUlts? {COUNt| HITS| MAX| MIN| PK2PK| MODE| MEAN| MEDian| PHITs| STDDev| ONESigma| TWOSigma| THRSigma},{ALLAcqs| CURRentacq| HISTory},{MAXimum| MEAN| MINimum| PK2PK| POPUlation| STDDev}
    - HISTogram:HISTogram<x>:MEASurement:STDDev {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:STDDev?
    - HISTogram:HISTogram<x>:MEASurement:THRSigma {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:THRSigma?
    - HISTogram:HISTogram<x>:MEASurement:TWOSigma {ON|OFF}
    - HISTogram:HISTogram<x>:MEASurement:TWOSigma?
    - HISTogram:HISTogram<x>:SAVe <QString>
    - HISTogram:HISTogram<x>:SIZe <NR3>
    - HISTogram:HISTogram<x>:SIZe?
    - HISTogram:HISTogram<x>:SOUrce {CH<x>|MATH<x>|REF<x>}
    - HISTogram:HISTogram<x>:SOUrce?
    - HISTogram:HISTogram<x>:STATE {ON|OFF}
    - HISTogram:HISTogram<x>:STATE?
    - HISTogram:HISTogram<x>:TRANsparency <NR3>
    - HISTogram:HISTogram<x>:TRANsparency?
    - HISTogram:LIST?
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdReadWithArguments,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class HistogramList(SCPICmdRead):
    """The ``HISTogram:LIST`` command.

    Description:
        - This query returns a comma separated list of all currently defined histograms.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HISTogram:LIST?
        ```
    """


class HistogramHistogramItemTransparency(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:TRANsparency`` command.

    Description:
        - This command sets or queries the transparency of the histogram bins.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:TRANsparency?``
          query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:TRANsparency?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:TRANsparency value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:TRANsparency <NR3>
        - HISTogram:HISTogram<x>:TRANsparency?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``<NR3>`` specifies the transparency as a percentage, with a minimum of 0 and a maximum of
          100.
    """


class HistogramHistogramItemState(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:STATE`` command.

    Description:
        - This command sets or queries whether histogram calculations are enabled for the specified
          histogram.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HISTogram:HISTogram<x>:STATE value``
          command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:STATE {ON|OFF}
        - HISTogram:HISTogram<x>:STATE?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the histogram calculations.
        - ``OFF`` disables the histogram calculations.
    """


class HistogramHistogramItemSource(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:SOUrce`` command.

    Description:
        - This command sets or queries which source waveform will be compared against the histogram
          box when the histogram testing is enabled.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:SOUrce?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HISTogram:HISTogram<x>:SOUrce value``
          command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:SOUrce {CH<x>|MATH<x>|REF<x>}
        - HISTogram:HISTogram<x>:SOUrce?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``CH<x>`` specifies an analog channel as source.
        - ``MATH<x>`` specifies a math channel as source.
        - ``REF<x>`` specifies a reference waveform as the source.
    """


class HistogramHistogramItemSize(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:SIZe`` command.

    Description:
        - This command sets or queries the height or width of the specified histogram bins in
          divisions. This size can be larger than the box, which allows you to view the histogram
          bins easily.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:SIZe?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:SIZe?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HISTogram:HISTogram<x>:SIZe value``
          command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:SIZe <NR3>
        - HISTogram:HISTogram<x>:SIZe?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``<NR3>`` specifies the number of divisions to set the height or width of the histogram
          bins to.
    """


class HistogramHistogramItemSave(SCPICmdWrite):
    """The ``HISTogram:HISTogram<x>:SAVe`` command.

    Description:
        - This command saves the specified histograms data as a comma separated list of values.

    Usage:
        - Using the ``.write(value)`` method will send the ``HISTogram:HISTogram<x>:SAVe value``
          command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:SAVe <QString>
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``<QString>`` is the file path to save the .csv file to.
    """

    _WRAP_ARG_WITH_QUOTES = True


class HistogramHistogramItemMeasurementTwosigma(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:TWOSigma`` command.

    Description:
        - This command sets or queries whether the µ±2(sigma) measurement is enabled on the
          histogram.

    Usage:
        - Using the ``.query()`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:TWOSigma?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:TWOSigma?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:TWOSigma value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:TWOSigma {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:TWOSigma?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the µ±2(sigma) measurement.
        - ``OFF`` disables the µ±2(sigma) measurement.
    """


class HistogramHistogramItemMeasurementThrsigma(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:THRSigma`` command.

    Description:
        - This command sets or queries whether the µ±3(sigma) measurement is enabled on the
          histogram.

    Usage:
        - Using the ``.query()`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:THRSigma?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:THRSigma?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:THRSigma value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:THRSigma {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:THRSigma?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the µ±3(sigma) measurement.
        - ``OFF`` disables the µ±3(sigma) measurement.
    """


class HistogramHistogramItemMeasurementStddev(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:STDDev`` command.

    Description:
        - This command sets or queries whether the Standard Deviation measurement is enabled on the
          histogram.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement:STDDev?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:STDDev?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:STDDev value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:STDDev {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:STDDev?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the Standard Deviation measurement.
        - ``OFF`` disables the Standard Deviation measurement.
    """


class HistogramHistogramItemMeasurementResults(SCPICmdReadWithArguments):
    """The ``HISTogram:HISTogram<x>:MEASurement:RESUlts`` command.

    Description:
        - This query only command returns the measurement results from the specified histogram. The
          argument must be in the form of {argument 1},{argument 2},{argument 3}. Argument 1
          specifies which histogram measurement to return results for. Argument 2 specifies which
          acquisitions to return measurement results for. Argument 3 specifies which statistic to
          return measurement results for.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:RESUlts? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:RESUlts? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:RESUlts? {COUNt| HITS| MAX| MIN| PK2PK| MODE| MEAN| MEDian| PHITs| STDDev| ONESigma| TWOSigma| THRSigma},{ALLAcqs| CURRentacq| HISTory},{MAXimum| MEAN| MINimum| PK2PK| POPUlation| STDDev}
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``COUNt`` specifies the Count as the histogram measurement to return results for.
        - ``HITS`` specifies the Hits as the histogram measurement to return results for.
        - ``MAX`` specifies the Max as the histogram measurement to return results for.
        - ``MIN`` specifies the Min as the histogram measurement to return results for.
        - ``PK2PK`` specifies the Peak-to-peak as the histogram measurement or statistic to return
          results for.
        - ``MODE`` specifies the Mode as the histogram measurement to return results for.
        - ``MEAN`` specifies the Mean as the histogram measurement or statistic to return results
          for.
        - ``MEDian`` specifies the Median as the histogram measurement to return results for.
        - ``PHITs`` specifies the Peak Hits as the histogram measurement to return results for.
        - ``STDDev`` specifies the Standard Deviation as the histogram measurement or statistic to
          return results for.
        - ``ONESigma`` specifies the µ±1(sigma) as the histogram measurement to return results for.
        - ``TWOSigma`` specifies the µ±2(sigma) as the histogram measurement to return results for.
        - ``THRSigma`` specifies the µ±3(sigma) as the histogram measurement to return results for.
        - ``ALLAcqs`` specifies the All Acquisitions as the acquisitions to return results for.
        - ``CURRentacq`` specifies the Current Acquisitions as the acquisitions to return results
          for.
        - ``HISTory`` specifies the History as the acquisitions to return results for.
        - ``MAXimum`` specifies the Maximum as the statistic to return results for.
        - ``MINimum`` specifies the Minimum as the statistic to return results for.
        - ``POPUlation`` specifies the Population as the statistic to return results for.
    """  # noqa: E501


class HistogramHistogramItemMeasurementPk2pk(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:PK2PK`` command.

    Description:
        - This command sets or queries whether the Peak-to-peak measurement is enabled on the
          histogram.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement:PK2PK?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:PK2PK?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:PK2PK value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:PK2PK {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:PK2PK?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the Peak-to-peak measurement.
        - ``OFF`` disables the Peak-to-peak measurement.
    """


class HistogramHistogramItemMeasurementPhits(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:PHITs`` command.

    Description:
        - This command sets or queries whether the Peak Hits measurement is enabled on the
          histogram.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement:PHITs?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:PHITs?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:PHITs value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:PHITs {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:PHITs?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the Peak Hits measurement.
        - ``OFF`` disables the Peak Hits measurement.
    """


class HistogramHistogramItemMeasurementOnesigma(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:ONESigma`` command.

    Description:
        - This command sets or queries whether the µ±1(sigma) measurement is enabled on the
          histogram.

    Usage:
        - Using the ``.query()`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:ONESigma?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:ONESigma?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:ONESigma value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:ONESigma {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:ONESigma?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the µ±1(sigma) measurement.
        - ``OFF`` disables the µ±1(sigma) measurement.
    """


class HistogramHistogramItemMeasurementMode(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:MODE`` command.

    Description:
        - This command sets or queries whether the Mode measurement is enabled on the histogram.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement:MODE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:MODE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:MODE value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:MODE {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:MODE?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the Mode measurement.
        - ``OFF`` disables the Mode measurement.
    """


class HistogramHistogramItemMeasurementMin(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:MIN`` command.

    Description:
        - This command sets or queries whether the Min measurement is enabled on the histogram.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement:MIN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:MIN?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:MIN value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:MIN {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:MIN?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the Min measurement.
        - ``OFF`` disables the Min measurement.
    """


class HistogramHistogramItemMeasurementMedian(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:MEDian`` command.

    Description:
        - This command sets or queries whether the Median measurement is enabled on the histogram.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement:MEDian?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:MEDian?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:MEDian value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:MEDian {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:MEDian?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the Median measurement.
        - ``OFF`` disables the Median measurement.
    """


class HistogramHistogramItemMeasurementMean(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:MEAN`` command.

    Description:
        - This command sets or queries whether the Mean measurement is enabled on the histogram.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement:MEAN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:MEAN?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:MEAN value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:MEAN {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:MEAN?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the Mean measurement.
        - ``OFF`` disables the Mean measurement.
    """


class HistogramHistogramItemMeasurementMax(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:MAX`` command.

    Description:
        - This command sets or queries whether the Max measurement is enabled on the histogram.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement:MAX?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:MAX?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:MAX value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:MAX {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:MAX?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the Max measurement.
        - ``OFF`` disables the Max measurement.
    """


class HistogramHistogramItemMeasurementHits(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:HITS`` command.

    Description:
        - This command sets or queries whether the Hits in Box measurement is enabled on the
          histogram.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement:HITS?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:HITS?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:HITS value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:HITS {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:HITS?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the Hits in Box measurement.
        - ``OFF`` disables the Hits in Box measurement.
    """


class HistogramHistogramItemMeasurementCount(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement:COUNt`` command.

    Description:
        - This command sets or queries whether the waveform count measurement is enabled on the
          histogram.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement:COUNt?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:COUNt?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HISTogram:HISTogram<x>:MEASurement:COUNt value`` command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:MEASurement:COUNt {ON|OFF}
        - HISTogram:HISTogram<x>:MEASurement:COUNt?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the waveform count measurement.
        - ``OFF`` disables the waveform count measurement.
    """


#  pylint: disable=too-many-instance-attributes
class HistogramHistogramItemMeasurement(SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:MEASurement`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:MEASurement?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``HISTogram<x>`` specifies the histogram number.

    Properties:
        - ``.count``: The ``HISTogram:HISTogram<x>:MEASurement:COUNt`` command.
        - ``.hits``: The ``HISTogram:HISTogram<x>:MEASurement:HITS`` command.
        - ``.max``: The ``HISTogram:HISTogram<x>:MEASurement:MAX`` command.
        - ``.mean``: The ``HISTogram:HISTogram<x>:MEASurement:MEAN`` command.
        - ``.median``: The ``HISTogram:HISTogram<x>:MEASurement:MEDian`` command.
        - ``.min``: The ``HISTogram:HISTogram<x>:MEASurement:MIN`` command.
        - ``.mode``: The ``HISTogram:HISTogram<x>:MEASurement:MODE`` command.
        - ``.onesigma``: The ``HISTogram:HISTogram<x>:MEASurement:ONESigma`` command.
        - ``.phits``: The ``HISTogram:HISTogram<x>:MEASurement:PHITs`` command.
        - ``.pk2pk``: The ``HISTogram:HISTogram<x>:MEASurement:PK2PK`` command.
        - ``.results``: The ``HISTogram:HISTogram<x>:MEASurement:RESUlts`` command.
        - ``.stddev``: The ``HISTogram:HISTogram<x>:MEASurement:STDDev`` command.
        - ``.thrsigma``: The ``HISTogram:HISTogram<x>:MEASurement:THRSigma`` command.
        - ``.twosigma``: The ``HISTogram:HISTogram<x>:MEASurement:TWOSigma`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = HistogramHistogramItemMeasurementCount(device, f"{self._cmd_syntax}:COUNt")
        self._hits = HistogramHistogramItemMeasurementHits(device, f"{self._cmd_syntax}:HITS")
        self._max = HistogramHistogramItemMeasurementMax(device, f"{self._cmd_syntax}:MAX")
        self._mean = HistogramHistogramItemMeasurementMean(device, f"{self._cmd_syntax}:MEAN")
        self._median = HistogramHistogramItemMeasurementMedian(device, f"{self._cmd_syntax}:MEDian")
        self._min = HistogramHistogramItemMeasurementMin(device, f"{self._cmd_syntax}:MIN")
        self._mode = HistogramHistogramItemMeasurementMode(device, f"{self._cmd_syntax}:MODE")
        self._onesigma = HistogramHistogramItemMeasurementOnesigma(
            device, f"{self._cmd_syntax}:ONESigma"
        )
        self._phits = HistogramHistogramItemMeasurementPhits(device, f"{self._cmd_syntax}:PHITs")
        self._pk2pk = HistogramHistogramItemMeasurementPk2pk(device, f"{self._cmd_syntax}:PK2PK")
        self._results = HistogramHistogramItemMeasurementResults(
            device, f"{self._cmd_syntax}:RESUlts"
        )
        self._stddev = HistogramHistogramItemMeasurementStddev(device, f"{self._cmd_syntax}:STDDev")
        self._thrsigma = HistogramHistogramItemMeasurementThrsigma(
            device, f"{self._cmd_syntax}:THRSigma"
        )
        self._twosigma = HistogramHistogramItemMeasurementTwosigma(
            device, f"{self._cmd_syntax}:TWOSigma"
        )

    @property
    def count(self) -> HistogramHistogramItemMeasurementCount:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:COUNt`` command.

        Description:
            - This command sets or queries whether the waveform count measurement is enabled on the
              histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:COUNt?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:COUNt value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:COUNt {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:COUNt?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the waveform count measurement.
            - ``OFF`` disables the waveform count measurement.
        """
        return self._count

    @property
    def hits(self) -> HistogramHistogramItemMeasurementHits:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:HITS`` command.

        Description:
            - This command sets or queries whether the Hits in Box measurement is enabled on the
              histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:HITS?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:HITS?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:HITS value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:HITS {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:HITS?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the Hits in Box measurement.
            - ``OFF`` disables the Hits in Box measurement.
        """
        return self._hits

    @property
    def max(self) -> HistogramHistogramItemMeasurementMax:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:MAX`` command.

        Description:
            - This command sets or queries whether the Max measurement is enabled on the histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MAX?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MAX?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MAX value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:MAX {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:MAX?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the Max measurement.
            - ``OFF`` disables the Max measurement.
        """
        return self._max

    @property
    def mean(self) -> HistogramHistogramItemMeasurementMean:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:MEAN`` command.

        Description:
            - This command sets or queries whether the Mean measurement is enabled on the histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MEAN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MEAN?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MEAN value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:MEAN {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:MEAN?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the Mean measurement.
            - ``OFF`` disables the Mean measurement.
        """
        return self._mean

    @property
    def median(self) -> HistogramHistogramItemMeasurementMedian:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:MEDian`` command.

        Description:
            - This command sets or queries whether the Median measurement is enabled on the
              histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MEDian?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MEDian?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MEDian value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:MEDian {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:MEDian?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the Median measurement.
            - ``OFF`` disables the Median measurement.
        """
        return self._median

    @property
    def min(self) -> HistogramHistogramItemMeasurementMin:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:MIN`` command.

        Description:
            - This command sets or queries whether the Min measurement is enabled on the histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MIN?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MIN?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MIN value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:MIN {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:MIN?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the Min measurement.
            - ``OFF`` disables the Min measurement.
        """
        return self._min

    @property
    def mode(self) -> HistogramHistogramItemMeasurementMode:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:MODE`` command.

        Description:
            - This command sets or queries whether the Mode measurement is enabled on the histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MODE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MODE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:MODE value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:MODE {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:MODE?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the Mode measurement.
            - ``OFF`` disables the Mode measurement.
        """
        return self._mode

    @property
    def onesigma(self) -> HistogramHistogramItemMeasurementOnesigma:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:ONESigma`` command.

        Description:
            - This command sets or queries whether the µ±1(sigma) measurement is enabled on the
              histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:ONESigma?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:ONESigma?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:ONESigma value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:ONESigma {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:ONESigma?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the µ±1(sigma) measurement.
            - ``OFF`` disables the µ±1(sigma) measurement.
        """
        return self._onesigma

    @property
    def phits(self) -> HistogramHistogramItemMeasurementPhits:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:PHITs`` command.

        Description:
            - This command sets or queries whether the Peak Hits measurement is enabled on the
              histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:PHITs?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:PHITs?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:PHITs value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:PHITs {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:PHITs?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the Peak Hits measurement.
            - ``OFF`` disables the Peak Hits measurement.
        """
        return self._phits

    @property
    def pk2pk(self) -> HistogramHistogramItemMeasurementPk2pk:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:PK2PK`` command.

        Description:
            - This command sets or queries whether the Peak-to-peak measurement is enabled on the
              histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:PK2PK?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:PK2PK?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:PK2PK value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:PK2PK {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:PK2PK?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the Peak-to-peak measurement.
            - ``OFF`` disables the Peak-to-peak measurement.
        """
        return self._pk2pk

    @property
    def results(self) -> HistogramHistogramItemMeasurementResults:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:RESUlts`` command.

        Description:
            - This query only command returns the measurement results from the specified histogram.
              The argument must be in the form of {argument 1},{argument 2},{argument 3}. Argument 1
              specifies which histogram measurement to return results for. Argument 2 specifies
              which acquisitions to return measurement results for. Argument 3 specifies which
              statistic to return measurement results for.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:RESUlts? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:RESUlts? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:RESUlts? {COUNt| HITS| MAX| MIN| PK2PK| MODE| MEAN| MEDian| PHITs| STDDev| ONESigma| TWOSigma| THRSigma},{ALLAcqs| CURRentacq| HISTory},{MAXimum| MEAN| MINimum| PK2PK| POPUlation| STDDev}
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``COUNt`` specifies the Count as the histogram measurement to return results for.
            - ``HITS`` specifies the Hits as the histogram measurement to return results for.
            - ``MAX`` specifies the Max as the histogram measurement to return results for.
            - ``MIN`` specifies the Min as the histogram measurement to return results for.
            - ``PK2PK`` specifies the Peak-to-peak as the histogram measurement or statistic to
              return results for.
            - ``MODE`` specifies the Mode as the histogram measurement to return results for.
            - ``MEAN`` specifies the Mean as the histogram measurement or statistic to return
              results for.
            - ``MEDian`` specifies the Median as the histogram measurement to return results for.
            - ``PHITs`` specifies the Peak Hits as the histogram measurement to return results for.
            - ``STDDev`` specifies the Standard Deviation as the histogram measurement or statistic
              to return results for.
            - ``ONESigma`` specifies the µ±1(sigma) as the histogram measurement to return results
              for.
            - ``TWOSigma`` specifies the µ±2(sigma) as the histogram measurement to return results
              for.
            - ``THRSigma`` specifies the µ±3(sigma) as the histogram measurement to return results
              for.
            - ``ALLAcqs`` specifies the All Acquisitions as the acquisitions to return results for.
            - ``CURRentacq`` specifies the Current Acquisitions as the acquisitions to return
              results for.
            - ``HISTory`` specifies the History as the acquisitions to return results for.
            - ``MAXimum`` specifies the Maximum as the statistic to return results for.
            - ``MINimum`` specifies the Minimum as the statistic to return results for.
            - ``POPUlation`` specifies the Population as the statistic to return results for.
        """  # noqa: E501
        return self._results

    @property
    def stddev(self) -> HistogramHistogramItemMeasurementStddev:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:STDDev`` command.

        Description:
            - This command sets or queries whether the Standard Deviation measurement is enabled on
              the histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:STDDev?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:STDDev?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:STDDev value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:STDDev {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:STDDev?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the Standard Deviation measurement.
            - ``OFF`` disables the Standard Deviation measurement.
        """
        return self._stddev

    @property
    def thrsigma(self) -> HistogramHistogramItemMeasurementThrsigma:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:THRSigma`` command.

        Description:
            - This command sets or queries whether the µ±3(sigma) measurement is enabled on the
              histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:THRSigma?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:THRSigma?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:THRSigma value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:THRSigma {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:THRSigma?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the µ±3(sigma) measurement.
            - ``OFF`` disables the µ±3(sigma) measurement.
        """
        return self._thrsigma

    @property
    def twosigma(self) -> HistogramHistogramItemMeasurementTwosigma:
        """Return the ``HISTogram:HISTogram<x>:MEASurement:TWOSigma`` command.

        Description:
            - This command sets or queries whether the µ±2(sigma) measurement is enabled on the
              histogram.

        Usage:
            - Using the ``.query()`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:TWOSigma?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:TWOSigma?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement:TWOSigma value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:MEASurement:TWOSigma {ON|OFF}
            - HISTogram:HISTogram<x>:MEASurement:TWOSigma?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the µ±2(sigma) measurement.
            - ``OFF`` disables the µ±2(sigma) measurement.
        """
        return self._twosigma


class HistogramHistogramItemFunction(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:FUNCtion`` command.

    Description:
        - This command sets or queries the histogram mode.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:FUNCtion?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HISTogram:HISTogram<x>:FUNCtion value``
          command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:FUNCtion {HORizontal|VERTical}
        - HISTogram:HISTogram<x>:FUNCtion?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``HORizontal`` sets the histogram mode to horizontal.
        - ``VERTical`` sets the histogram mode to vertical.
    """


class HistogramHistogramItemDisplay(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:DISPlay`` command.

    Description:
        - This command sets or queries the histogram scaling display setting.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:DISPlay?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:DISPlay?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HISTogram:HISTogram<x>:DISPlay value``
          command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:DISPlay {LINEAr|LOG}
        - HISTogram:HISTogram<x>:DISPlay?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``LINEAr`` sets the histogram scaling to linear mode.
        - ``LOG`` sets the histogram scaling to logarithmic mode.
    """


class HistogramHistogramItemData(SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:DATa`` command.

    Description:
        - This query only command returns a comma separated list of numbers representing the
          histogram bin data.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:DATa?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:DATa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:DATa?
        ```
    """


class HistogramHistogramItemBstate(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:BSTate`` command.

    Description:
        - This command sets or queries whether the histogram badge is displayed.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:BSTate?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:BSTate?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HISTogram:HISTogram<x>:BSTate value``
          command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:BSTate {ON|OFF}
        - HISTogram:HISTogram<x>:BSTate?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``ON`` enables the histogram badge display.
        - ``OFF`` disables the histogram badge display.
    """


class HistogramHistogramItemBox(SCPICmdWrite, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>:BOX`` command.

    Description:
        - This command sets or queries the top, left, bottom and right positions of the histogram
          box in source waveform coordinates. The argument is of the form
          <top>,<left>,<bottom>,<right>.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:BOX?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:BOX?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HISTogram:HISTogram<x>:BOX value``
          command.

    SCPI Syntax:
        ```
        - HISTogram:HISTogram<x>:BOX <NR3>,<NR3>,<NR3>,<NR3>
        - HISTogram:HISTogram<x>:BOX?
        ```

    Info:
        - ``HISTogram<x>`` specifies the histogram number.
        - ``<NR3>`` specifies four position values, separated by commas. The values are the top,
          left, bottom, and right coordinates in that order.
    """


#  pylint: disable=too-many-instance-attributes
class HistogramHistogramItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``HISTogram:HISTogram<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``HISTogram<x>`` specifies the histogram number.

    Properties:
        - ``.box``: The ``HISTogram:HISTogram<x>:BOX`` command.
        - ``.bstate``: The ``HISTogram:HISTogram<x>:BSTate`` command.
        - ``.data``: The ``HISTogram:HISTogram<x>:DATa`` command.
        - ``.display``: The ``HISTogram:HISTogram<x>:DISPlay`` command.
        - ``.function``: The ``HISTogram:HISTogram<x>:FUNCtion`` command.
        - ``.measurement``: The ``HISTogram:HISTogram<x>:MEASurement`` command tree.
        - ``.save``: The ``HISTogram:HISTogram<x>:SAVe`` command.
        - ``.size``: The ``HISTogram:HISTogram<x>:SIZe`` command.
        - ``.source``: The ``HISTogram:HISTogram<x>:SOUrce`` command.
        - ``.state``: The ``HISTogram:HISTogram<x>:STATE`` command.
        - ``.transparency``: The ``HISTogram:HISTogram<x>:TRANsparency`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._box = HistogramHistogramItemBox(device, f"{self._cmd_syntax}:BOX")
        self._bstate = HistogramHistogramItemBstate(device, f"{self._cmd_syntax}:BSTate")
        self._data = HistogramHistogramItemData(device, f"{self._cmd_syntax}:DATa")
        self._display = HistogramHistogramItemDisplay(device, f"{self._cmd_syntax}:DISPlay")
        self._function = HistogramHistogramItemFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._measurement = HistogramHistogramItemMeasurement(
            device, f"{self._cmd_syntax}:MEASurement"
        )
        self._save = HistogramHistogramItemSave(device, f"{self._cmd_syntax}:SAVe")
        self._size = HistogramHistogramItemSize(device, f"{self._cmd_syntax}:SIZe")
        self._source = HistogramHistogramItemSource(device, f"{self._cmd_syntax}:SOUrce")
        self._state = HistogramHistogramItemState(device, f"{self._cmd_syntax}:STATE")
        self._transparency = HistogramHistogramItemTransparency(
            device, f"{self._cmd_syntax}:TRANsparency"
        )

    @property
    def box(self) -> HistogramHistogramItemBox:
        """Return the ``HISTogram:HISTogram<x>:BOX`` command.

        Description:
            - This command sets or queries the top, left, bottom and right positions of the
              histogram box in source waveform coordinates. The argument is of the form
              <top>,<left>,<bottom>,<right>.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:BOX?`` query.
            - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:BOX?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HISTogram:HISTogram<x>:BOX value``
              command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:BOX <NR3>,<NR3>,<NR3>,<NR3>
            - HISTogram:HISTogram<x>:BOX?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``<NR3>`` specifies four position values, separated by commas. The values are the top,
              left, bottom, and right coordinates in that order.
        """
        return self._box

    @property
    def bstate(self) -> HistogramHistogramItemBstate:
        """Return the ``HISTogram:HISTogram<x>:BSTate`` command.

        Description:
            - This command sets or queries whether the histogram badge is displayed.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:BSTate?`` query.
            - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:BSTate?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:BSTate value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:BSTate {ON|OFF}
            - HISTogram:HISTogram<x>:BSTate?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the histogram badge display.
            - ``OFF`` disables the histogram badge display.
        """
        return self._bstate

    @property
    def data(self) -> HistogramHistogramItemData:
        """Return the ``HISTogram:HISTogram<x>:DATa`` command.

        Description:
            - This query only command returns a comma separated list of numbers representing the
              histogram bin data.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:DATa?`` query.
            - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:DATa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:DATa?
            ```
        """
        return self._data

    @property
    def display(self) -> HistogramHistogramItemDisplay:
        """Return the ``HISTogram:HISTogram<x>:DISPlay`` command.

        Description:
            - This command sets or queries the histogram scaling display setting.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:DISPlay?`` query.
            - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:DISPlay?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:DISPlay value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:DISPlay {LINEAr|LOG}
            - HISTogram:HISTogram<x>:DISPlay?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``LINEAr`` sets the histogram scaling to linear mode.
            - ``LOG`` sets the histogram scaling to logarithmic mode.
        """
        return self._display

    @property
    def function(self) -> HistogramHistogramItemFunction:
        """Return the ``HISTogram:HISTogram<x>:FUNCtion`` command.

        Description:
            - This command sets or queries the histogram mode.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:FUNCtion?``
              query.
            - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:FUNCtion?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:FUNCtion {HORizontal|VERTical}
            - HISTogram:HISTogram<x>:FUNCtion?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``HORizontal`` sets the histogram mode to horizontal.
            - ``VERTical`` sets the histogram mode to vertical.
        """
        return self._function

    @property
    def measurement(self) -> HistogramHistogramItemMeasurement:
        """Return the ``HISTogram:HISTogram<x>:MEASurement`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:MEASurement?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:MEASurement?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``HISTogram<x>`` specifies the histogram number.

        Sub-properties:
            - ``.count``: The ``HISTogram:HISTogram<x>:MEASurement:COUNt`` command.
            - ``.hits``: The ``HISTogram:HISTogram<x>:MEASurement:HITS`` command.
            - ``.max``: The ``HISTogram:HISTogram<x>:MEASurement:MAX`` command.
            - ``.mean``: The ``HISTogram:HISTogram<x>:MEASurement:MEAN`` command.
            - ``.median``: The ``HISTogram:HISTogram<x>:MEASurement:MEDian`` command.
            - ``.min``: The ``HISTogram:HISTogram<x>:MEASurement:MIN`` command.
            - ``.mode``: The ``HISTogram:HISTogram<x>:MEASurement:MODE`` command.
            - ``.onesigma``: The ``HISTogram:HISTogram<x>:MEASurement:ONESigma`` command.
            - ``.phits``: The ``HISTogram:HISTogram<x>:MEASurement:PHITs`` command.
            - ``.pk2pk``: The ``HISTogram:HISTogram<x>:MEASurement:PK2PK`` command.
            - ``.results``: The ``HISTogram:HISTogram<x>:MEASurement:RESUlts`` command.
            - ``.stddev``: The ``HISTogram:HISTogram<x>:MEASurement:STDDev`` command.
            - ``.thrsigma``: The ``HISTogram:HISTogram<x>:MEASurement:THRSigma`` command.
            - ``.twosigma``: The ``HISTogram:HISTogram<x>:MEASurement:TWOSigma`` command.
        """
        return self._measurement

    @property
    def save(self) -> HistogramHistogramItemSave:
        """Return the ``HISTogram:HISTogram<x>:SAVe`` command.

        Description:
            - This command saves the specified histograms data as a comma separated list of values.

        Usage:
            - Using the ``.write(value)`` method will send the ``HISTogram:HISTogram<x>:SAVe value``
              command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:SAVe <QString>
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``<QString>`` is the file path to save the .csv file to.
        """
        return self._save

    @property
    def size(self) -> HistogramHistogramItemSize:
        """Return the ``HISTogram:HISTogram<x>:SIZe`` command.

        Description:
            - This command sets or queries the height or width of the specified histogram bins in
              divisions. This size can be larger than the box, which allows you to view the
              histogram bins easily.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:SIZe?`` query.
            - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:SIZe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HISTogram:HISTogram<x>:SIZe value``
              command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:SIZe <NR3>
            - HISTogram:HISTogram<x>:SIZe?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``<NR3>`` specifies the number of divisions to set the height or width of the
              histogram bins to.
        """
        return self._size

    @property
    def source(self) -> HistogramHistogramItemSource:
        """Return the ``HISTogram:HISTogram<x>:SOUrce`` command.

        Description:
            - This command sets or queries which source waveform will be compared against the
              histogram box when the histogram testing is enabled.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:SOUrce?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:SOUrce value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:SOUrce {CH<x>|MATH<x>|REF<x>}
            - HISTogram:HISTogram<x>:SOUrce?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``CH<x>`` specifies an analog channel as source.
            - ``MATH<x>`` specifies a math channel as source.
            - ``REF<x>`` specifies a reference waveform as the source.
        """
        return self._source

    @property
    def state(self) -> HistogramHistogramItemState:
        """Return the ``HISTogram:HISTogram<x>:STATE`` command.

        Description:
            - This command sets or queries whether histogram calculations are enabled for the
              specified histogram.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:STATE value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:STATE {ON|OFF}
            - HISTogram:HISTogram<x>:STATE?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``ON`` enables the histogram calculations.
            - ``OFF`` disables the histogram calculations.
        """
        return self._state

    @property
    def transparency(self) -> HistogramHistogramItemTransparency:
        """Return the ``HISTogram:HISTogram<x>:TRANsparency`` command.

        Description:
            - This command sets or queries the transparency of the histogram bins.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>:TRANsparency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HISTogram:HISTogram<x>:TRANsparency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HISTogram:HISTogram<x>:TRANsparency value`` command.

        SCPI Syntax:
            ```
            - HISTogram:HISTogram<x>:TRANsparency <NR3>
            - HISTogram:HISTogram<x>:TRANsparency?
            ```

        Info:
            - ``HISTogram<x>`` specifies the histogram number.
            - ``<NR3>`` specifies the transparency as a percentage, with a minimum of 0 and a
              maximum of 100.
        """
        return self._transparency


class HistogramDelete(SCPICmdWrite):
    """The ``HISTogram:DELete`` command.

    Description:
        - This command deletes the specified histogram.

    Usage:
        - Using the ``.write(value)`` method will send the ``HISTogram:DELete value`` command.

    SCPI Syntax:
        ```
        - HISTogram:DELete <QString>
        ```

    Info:
        - ``<QString>`` specifies the waveform histogram to delete. The argument is of the form
          'HIST<NR1>', where NR1 is a number value ≥ 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class HistogramDeleteall(SCPICmdWriteNoArguments):
    """The ``HISTogram:DELETEALL`` command.

    Description:
        - This command deletes all the active instances of histograms defined in the scope
          application.

    Usage:
        - Using the ``.write()`` method will send the ``HISTogram:DELETEALL`` command.

    SCPI Syntax:
        ```
        - HISTogram:DELETEALL
        ```
    """


class HistogramAddnew(SCPICmdWrite):
    """The ``HISTogram:ADDNew`` command.

    Description:
        - This command adds the specified waveform histogram.

    Usage:
        - Using the ``.write(value)`` method will send the ``HISTogram:ADDNew value`` command.

    SCPI Syntax:
        ```
        - HISTogram:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` specifies the waveform histogram to add. The argument is of the form
          'HIST<NR1>', where NR1 is a number value ≥ 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Histogram(SCPICmdRead):
    """The ``HISTogram`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HISTogram?`` query.
        - Using the ``.verify(value)`` method will send the ``HISTogram?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``HISTogram:ADDNew`` command.
        - ``.deleteall``: The ``HISTogram:DELETEALL`` command.
        - ``.delete``: The ``HISTogram:DELete`` command.
        - ``.histogram``: The ``HISTogram:HISTogram<x>`` command tree.
        - ``.list``: The ``HISTogram:LIST`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "HISTogram") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = HistogramAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._deleteall = HistogramDeleteall(device, f"{self._cmd_syntax}:DELETEALL")
        self._delete = HistogramDelete(device, f"{self._cmd_syntax}:DELete")
        self._histogram: Dict[int, HistogramHistogramItem] = DefaultDictPassKeyToFactory(
            lambda x: HistogramHistogramItem(device, f"{self._cmd_syntax}:HISTogram{x}")
        )
        self._list = HistogramList(device, f"{self._cmd_syntax}:LIST")

    @property
    def addnew(self) -> HistogramAddnew:
        """Return the ``HISTogram:ADDNew`` command.

        Description:
            - This command adds the specified waveform histogram.

        Usage:
            - Using the ``.write(value)`` method will send the ``HISTogram:ADDNew value`` command.

        SCPI Syntax:
            ```
            - HISTogram:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` specifies the waveform histogram to add. The argument is of the form
              'HIST<NR1>', where NR1 is a number value ≥ 1.
        """
        return self._addnew

    @property
    def deleteall(self) -> HistogramDeleteall:
        """Return the ``HISTogram:DELETEALL`` command.

        Description:
            - This command deletes all the active instances of histograms defined in the scope
              application.

        Usage:
            - Using the ``.write()`` method will send the ``HISTogram:DELETEALL`` command.

        SCPI Syntax:
            ```
            - HISTogram:DELETEALL
            ```
        """
        return self._deleteall

    @property
    def delete(self) -> HistogramDelete:
        """Return the ``HISTogram:DELete`` command.

        Description:
            - This command deletes the specified histogram.

        Usage:
            - Using the ``.write(value)`` method will send the ``HISTogram:DELete value`` command.

        SCPI Syntax:
            ```
            - HISTogram:DELete <QString>
            ```

        Info:
            - ``<QString>`` specifies the waveform histogram to delete. The argument is of the form
              'HIST<NR1>', where NR1 is a number value ≥ 1.
        """
        return self._delete

    @property
    def histogram(self) -> Dict[int, HistogramHistogramItem]:
        """Return the ``HISTogram:HISTogram<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:HISTogram<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``HISTogram:HISTogram<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``HISTogram<x>`` specifies the histogram number.

        Sub-properties:
            - ``.box``: The ``HISTogram:HISTogram<x>:BOX`` command.
            - ``.bstate``: The ``HISTogram:HISTogram<x>:BSTate`` command.
            - ``.data``: The ``HISTogram:HISTogram<x>:DATa`` command.
            - ``.display``: The ``HISTogram:HISTogram<x>:DISPlay`` command.
            - ``.function``: The ``HISTogram:HISTogram<x>:FUNCtion`` command.
            - ``.measurement``: The ``HISTogram:HISTogram<x>:MEASurement`` command tree.
            - ``.save``: The ``HISTogram:HISTogram<x>:SAVe`` command.
            - ``.size``: The ``HISTogram:HISTogram<x>:SIZe`` command.
            - ``.source``: The ``HISTogram:HISTogram<x>:SOUrce`` command.
            - ``.state``: The ``HISTogram:HISTogram<x>:STATE`` command.
            - ``.transparency``: The ``HISTogram:HISTogram<x>:TRANsparency`` command.
        """
        return self._histogram

    @property
    def list(self) -> HistogramList:
        """Return the ``HISTogram:LIST`` command.

        Description:
            - This query returns a comma separated list of all currently defined histograms.

        Usage:
            - Using the ``.query()`` method will send the ``HISTogram:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``HISTogram:LIST?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HISTogram:LIST?
            ```
        """
        return self._list
