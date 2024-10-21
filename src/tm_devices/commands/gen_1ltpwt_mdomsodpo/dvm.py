"""The dvm commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DVM {RESET}
    - DVM:AUTORange {0|1|OFF|ON}
    - DVM:AUTORange?
    - DVM:DISPLAYSTYle {FULl|MINimum}
    - DVM:DISPLAYSTYle?
    - DVM:MEASUrement:FREQuency?
    - DVM:MEASUrement:HIStory:AVErage?
    - DVM:MEASUrement:HIStory:MAXimum?
    - DVM:MEASUrement:HIStory:MINImum?
    - DVM:MEASUrement:INFMAXimum?
    - DVM:MEASUrement:INFMINimum?
    - DVM:MEASUrement:VALue?
    - DVM:MODe {ACRMS|ACDCRMS|DC|FREQuency|OFF}
    - DVM:MODe?
    - DVM:SOUrce {CH<x>}
    - DVM:SOUrce?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DvmSource(SCPICmdWrite, SCPICmdRead):
    """The ``DVM:SOUrce`` command.

    Description:
        - This command sets (or queries) the source for the DVM.

    Usage:
        - Using the ``.query()`` method will send the ``DVM:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DVM:SOUrce value`` command.

    SCPI Syntax:
        ```
        - DVM:SOUrce {CH<x>}
        - DVM:SOUrce?
        ```

    Info:
        - ``CH<x>`` specify which channel to use as the source for the DVM.
    """


class DvmMode(SCPICmdWrite, SCPICmdRead):
    """The ``DVM:MODe`` command.

    Description:
        - Specifies (or queries) the mode to use for the Digital Voltmeter (ACRMS, ACDCRMS, DC,
          Frequency, or OFF).

    Usage:
        - Using the ``.query()`` method will send the ``DVM:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DVM:MODe value`` command.

    SCPI Syntax:
        ```
        - DVM:MODe {ACRMS|ACDCRMS|DC|FREQuency|OFF}
        - DVM:MODe?
        ```

    Info:
        - ``ACRMS`` - displays the root-mean-square value of the acquired data, with the DC
          component removed.
        - ``ACDCRMS`` - displays the RMS value of the acquired data.
        - ``DC`` - displays the DC value of the acquired data.
        - ``FREQuency`` - displays the frequency counter measurement.
        - ``OFF``
    """


class DvmMeasurementValue(SCPICmdRead):
    """The ``DVM:MEASUrement:VALue`` command.

    Description:
        - Returns the DVM readout value (the largest displayed value at the top of the DVM screen).

    Usage:
        - Using the ``.query()`` method will send the ``DVM:MEASUrement:VALue?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:VALue?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DVM:MEASUrement:VALue?
        ```
    """


class DvmMeasurementInfminimum(SCPICmdRead):
    """The ``DVM:MEASUrement:INFMINimum`` command.

    Description:
        - Returns the minimum readout value of the DVM over the entire time that the DVM has been on
          since the last change using the ``DVM:MODE`` or ``DVM:SOURCE`` commands or DVM RESET.

    Usage:
        - Using the ``.query()`` method will send the ``DVM:MEASUrement:INFMINimum?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:INFMINimum?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DVM:MEASUrement:INFMINimum?
        ```
    """


class DvmMeasurementInfmaximum(SCPICmdRead):
    """The ``DVM:MEASUrement:INFMAXimum`` command.

    Description:
        - Returns the maximum DVM readout value over the entire time that the DVM has been on since
          the last change using the ``DVM:MODE`` or ``DVM:SOURCE`` commands or DVM RESET.

    Usage:
        - Using the ``.query()`` method will send the ``DVM:MEASUrement:INFMAXimum?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:INFMAXimum?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DVM:MEASUrement:INFMAXimum?
        ```
    """


class DvmMeasurementHistoryMinimum(SCPICmdRead):
    """The ``DVM:MEASUrement:HIStory:MINImum`` command.

    Description:
        - Returns the minimum readout value for the DVM over the history period. The history period
          is a constant period of 5 seconds.

    Usage:
        - Using the ``.query()`` method will send the ``DVM:MEASUrement:HIStory:MINImum?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:HIStory:MINImum?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DVM:MEASUrement:HIStory:MINImum?
        ```
    """


class DvmMeasurementHistoryMaximum(SCPICmdRead):
    """The ``DVM:MEASUrement:HIStory:MAXimum`` command.

    Description:
        - Returns the maximum readout value for the DVM function over the history period. The
          history period is a constant period of 5 seconds.

    Usage:
        - Using the ``.query()`` method will send the ``DVM:MEASUrement:HIStory:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:HIStory:MAXimum?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DVM:MEASUrement:HIStory:MAXimum?
        ```
    """


class DvmMeasurementHistoryAverage(SCPICmdRead):
    """The ``DVM:MEASUrement:HIStory:AVErage`` command.

    Description:
        - Returns the average DVM readout value over the history period. The history period is a
          constant period of 5 seconds.

    Usage:
        - Using the ``.query()`` method will send the ``DVM:MEASUrement:HIStory:AVErage?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:HIStory:AVErage?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DVM:MEASUrement:HIStory:AVErage?
        ```
    """


class DvmMeasurementHistory(SCPICmdRead):
    """The ``DVM:MEASUrement:HIStory`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DVM:MEASUrement:HIStory?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:HIStory?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.average``: The ``DVM:MEASUrement:HIStory:AVErage`` command.
        - ``.maximum``: The ``DVM:MEASUrement:HIStory:MAXimum`` command.
        - ``.minimum``: The ``DVM:MEASUrement:HIStory:MINImum`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._average = DvmMeasurementHistoryAverage(device, f"{self._cmd_syntax}:AVErage")
        self._maximum = DvmMeasurementHistoryMaximum(device, f"{self._cmd_syntax}:MAXimum")
        self._minimum = DvmMeasurementHistoryMinimum(device, f"{self._cmd_syntax}:MINImum")

    @property
    def average(self) -> DvmMeasurementHistoryAverage:
        """Return the ``DVM:MEASUrement:HIStory:AVErage`` command.

        Description:
            - Returns the average DVM readout value over the history period. The history period is a
              constant period of 5 seconds.

        Usage:
            - Using the ``.query()`` method will send the ``DVM:MEASUrement:HIStory:AVErage?``
              query.
            - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:HIStory:AVErage?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DVM:MEASUrement:HIStory:AVErage?
            ```
        """
        return self._average

    @property
    def maximum(self) -> DvmMeasurementHistoryMaximum:
        """Return the ``DVM:MEASUrement:HIStory:MAXimum`` command.

        Description:
            - Returns the maximum readout value for the DVM function over the history period. The
              history period is a constant period of 5 seconds.

        Usage:
            - Using the ``.query()`` method will send the ``DVM:MEASUrement:HIStory:MAXimum?``
              query.
            - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:HIStory:MAXimum?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DVM:MEASUrement:HIStory:MAXimum?
            ```
        """
        return self._maximum

    @property
    def minimum(self) -> DvmMeasurementHistoryMinimum:
        """Return the ``DVM:MEASUrement:HIStory:MINImum`` command.

        Description:
            - Returns the minimum readout value for the DVM over the history period. The history
              period is a constant period of 5 seconds.

        Usage:
            - Using the ``.query()`` method will send the ``DVM:MEASUrement:HIStory:MINImum?``
              query.
            - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:HIStory:MINImum?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DVM:MEASUrement:HIStory:MINImum?
            ```
        """
        return self._minimum


class DvmMeasurementFrequency(SCPICmdRead):
    """The ``DVM:MEASUrement:FREQuency`` command.

    Description:
        - This command returns the current frequency value for the DVM.

    Usage:
        - Using the ``.query()`` method will send the ``DVM:MEASUrement:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:FREQuency?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DVM:MEASUrement:FREQuency?
        ```
    """


class DvmMeasurement(SCPICmdRead):
    """The ``DVM:MEASUrement`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DVM:MEASUrement?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``DVM:MEASUrement:FREQuency`` command.
        - ``.history``: The ``DVM:MEASUrement:HIStory`` command tree.
        - ``.infmaximum``: The ``DVM:MEASUrement:INFMAXimum`` command.
        - ``.infminimum``: The ``DVM:MEASUrement:INFMINimum`` command.
        - ``.value``: The ``DVM:MEASUrement:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = DvmMeasurementFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._history = DvmMeasurementHistory(device, f"{self._cmd_syntax}:HIStory")
        self._infmaximum = DvmMeasurementInfmaximum(device, f"{self._cmd_syntax}:INFMAXimum")
        self._infminimum = DvmMeasurementInfminimum(device, f"{self._cmd_syntax}:INFMINimum")
        self._value = DvmMeasurementValue(device, f"{self._cmd_syntax}:VALue")

    @property
    def frequency(self) -> DvmMeasurementFrequency:
        """Return the ``DVM:MEASUrement:FREQuency`` command.

        Description:
            - This command returns the current frequency value for the DVM.

        Usage:
            - Using the ``.query()`` method will send the ``DVM:MEASUrement:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:FREQuency?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DVM:MEASUrement:FREQuency?
            ```
        """
        return self._frequency

    @property
    def history(self) -> DvmMeasurementHistory:
        """Return the ``DVM:MEASUrement:HIStory`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DVM:MEASUrement:HIStory?`` query.
            - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:HIStory?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.average``: The ``DVM:MEASUrement:HIStory:AVErage`` command.
            - ``.maximum``: The ``DVM:MEASUrement:HIStory:MAXimum`` command.
            - ``.minimum``: The ``DVM:MEASUrement:HIStory:MINImum`` command.
        """
        return self._history

    @property
    def infmaximum(self) -> DvmMeasurementInfmaximum:
        """Return the ``DVM:MEASUrement:INFMAXimum`` command.

        Description:
            - Returns the maximum DVM readout value over the entire time that the DVM has been on
              since the last change using the ``DVM:MODE`` or ``DVM:SOURCE`` commands or DVM RESET.

        Usage:
            - Using the ``.query()`` method will send the ``DVM:MEASUrement:INFMAXimum?`` query.
            - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:INFMAXimum?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DVM:MEASUrement:INFMAXimum?
            ```
        """
        return self._infmaximum

    @property
    def infminimum(self) -> DvmMeasurementInfminimum:
        """Return the ``DVM:MEASUrement:INFMINimum`` command.

        Description:
            - Returns the minimum readout value of the DVM over the entire time that the DVM has
              been on since the last change using the ``DVM:MODE`` or ``DVM:SOURCE`` commands or DVM
              RESET.

        Usage:
            - Using the ``.query()`` method will send the ``DVM:MEASUrement:INFMINimum?`` query.
            - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:INFMINimum?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DVM:MEASUrement:INFMINimum?
            ```
        """
        return self._infminimum

    @property
    def value(self) -> DvmMeasurementValue:
        """Return the ``DVM:MEASUrement:VALue`` command.

        Description:
            - Returns the DVM readout value (the largest displayed value at the top of the DVM
              screen).

        Usage:
            - Using the ``.query()`` method will send the ``DVM:MEASUrement:VALue?`` query.
            - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement:VALue?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DVM:MEASUrement:VALue?
            ```
        """
        return self._value


class DvmDisplaystyle(SCPICmdWrite, SCPICmdRead):
    """The ``DVM:DISPLAYSTYle`` command.

    Description:
        - Sets (or queries) the display style for the Digital Voltmeter.

    Usage:
        - Using the ``.query()`` method will send the ``DVM:DISPLAYSTYle?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:DISPLAYSTYle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DVM:DISPLAYSTYle value`` command.

    SCPI Syntax:
        ```
        - DVM:DISPLAYSTYle {FULl|MINimum}
        - DVM:DISPLAYSTYle?
        ```

    Info:
        - ``FULl`` sets the display style for the DVM to Full.
        - ``MINimum`` sets the display style for the DVM to Minimum.
    """


class DvmAutorange(SCPICmdWrite, SCPICmdRead):
    """The ``DVM:AUTORange`` command.

    Description:
        - Sets (or queries) the autorange state for the Digital Voltmeter.

    Usage:
        - Using the ``.query()`` method will send the ``DVM:AUTORange?`` query.
        - Using the ``.verify(value)`` method will send the ``DVM:AUTORange?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DVM:AUTORange value`` command.

    SCPI Syntax:
        ```
        - DVM:AUTORange {0|1|OFF|ON}
        - DVM:AUTORange?
        ```

    Info:
        - ``1`` or ON turns on autorange for the Digital Voltmeter.
        - ``0`` or OFF turns autorange off.
    """


class Dvm(SCPICmdWrite, SCPICmdRead):
    """The ``DVM`` command.

    Description:
        - Resets the Digital Voltmeter measurements and history.

    Usage:
        - Using the ``.write(value)`` method will send the ``DVM value`` command.

    SCPI Syntax:
        ```
        - DVM {RESET}
        ```

    Properties:
        - ``.autorange``: The ``DVM:AUTORange`` command.
        - ``.displaystyle``: The ``DVM:DISPLAYSTYle`` command.
        - ``.measurement``: The ``DVM:MEASUrement`` command tree.
        - ``.mode``: The ``DVM:MODe`` command.
        - ``.source``: The ``DVM:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DVM") -> None:
        super().__init__(device, cmd_syntax)
        self._autorange = DvmAutorange(device, f"{self._cmd_syntax}:AUTORange")
        self._displaystyle = DvmDisplaystyle(device, f"{self._cmd_syntax}:DISPLAYSTYle")
        self._measurement = DvmMeasurement(device, f"{self._cmd_syntax}:MEASUrement")
        self._mode = DvmMode(device, f"{self._cmd_syntax}:MODe")
        self._source = DvmSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def autorange(self) -> DvmAutorange:
        """Return the ``DVM:AUTORange`` command.

        Description:
            - Sets (or queries) the autorange state for the Digital Voltmeter.

        Usage:
            - Using the ``.query()`` method will send the ``DVM:AUTORange?`` query.
            - Using the ``.verify(value)`` method will send the ``DVM:AUTORange?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DVM:AUTORange value`` command.

        SCPI Syntax:
            ```
            - DVM:AUTORange {0|1|OFF|ON}
            - DVM:AUTORange?
            ```

        Info:
            - ``1`` or ON turns on autorange for the Digital Voltmeter.
            - ``0`` or OFF turns autorange off.
        """
        return self._autorange

    @property
    def displaystyle(self) -> DvmDisplaystyle:
        """Return the ``DVM:DISPLAYSTYle`` command.

        Description:
            - Sets (or queries) the display style for the Digital Voltmeter.

        Usage:
            - Using the ``.query()`` method will send the ``DVM:DISPLAYSTYle?`` query.
            - Using the ``.verify(value)`` method will send the ``DVM:DISPLAYSTYle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DVM:DISPLAYSTYle value`` command.

        SCPI Syntax:
            ```
            - DVM:DISPLAYSTYle {FULl|MINimum}
            - DVM:DISPLAYSTYle?
            ```

        Info:
            - ``FULl`` sets the display style for the DVM to Full.
            - ``MINimum`` sets the display style for the DVM to Minimum.
        """
        return self._displaystyle

    @property
    def measurement(self) -> DvmMeasurement:
        """Return the ``DVM:MEASUrement`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DVM:MEASUrement?`` query.
            - Using the ``.verify(value)`` method will send the ``DVM:MEASUrement?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``DVM:MEASUrement:FREQuency`` command.
            - ``.history``: The ``DVM:MEASUrement:HIStory`` command tree.
            - ``.infmaximum``: The ``DVM:MEASUrement:INFMAXimum`` command.
            - ``.infminimum``: The ``DVM:MEASUrement:INFMINimum`` command.
            - ``.value``: The ``DVM:MEASUrement:VALue`` command.
        """
        return self._measurement

    @property
    def mode(self) -> DvmMode:
        """Return the ``DVM:MODe`` command.

        Description:
            - Specifies (or queries) the mode to use for the Digital Voltmeter (ACRMS, ACDCRMS, DC,
              Frequency, or OFF).

        Usage:
            - Using the ``.query()`` method will send the ``DVM:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``DVM:MODe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DVM:MODe value`` command.

        SCPI Syntax:
            ```
            - DVM:MODe {ACRMS|ACDCRMS|DC|FREQuency|OFF}
            - DVM:MODe?
            ```

        Info:
            - ``ACRMS`` - displays the root-mean-square value of the acquired data, with the DC
              component removed.
            - ``ACDCRMS`` - displays the RMS value of the acquired data.
            - ``DC`` - displays the DC value of the acquired data.
            - ``FREQuency`` - displays the frequency counter measurement.
            - ``OFF``
        """
        return self._mode

    @property
    def source(self) -> DvmSource:
        """Return the ``DVM:SOUrce`` command.

        Description:
            - This command sets (or queries) the source for the DVM.

        Usage:
            - Using the ``.query()`` method will send the ``DVM:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``DVM:SOUrce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DVM:SOUrce value`` command.

        SCPI Syntax:
            ```
            - DVM:SOUrce {CH<x>}
            - DVM:SOUrce?
            ```

        Info:
            - ``CH<x>`` specify which channel to use as the source for the DVM.
        """
        return self._source
