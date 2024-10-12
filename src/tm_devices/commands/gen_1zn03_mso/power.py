# pylint: disable=line-too-long
"""The power commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - POWer:ADDNew 'POWER<x>'
    - POWer:DELete 'POWER<x>'
    - POWer:POWer<x>:CLRESPONSE:AMP<x>Val <NR3>
    - POWer:POWer<x>:CLRESPONSE:AMP<x>Val?
    - POWer:POWer<x>:CLRESPONSE:AMPMode {CONSTant|PROFile}
    - POWer:POWer<x>:CLRESPONSE:AMPMode?
    - POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?
    - POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?
    - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude <NR3>
    - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?
    - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val <NR3>
    - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?
    - POWer:POWer<x>:CLRESPONSE:GENIPADDress <NR2>
    - POWer:POWer<x>:CLRESPONSE:GENIPADDress?
    - POWer:POWer<x>:CLRESPONSE:GENerator {INTernal|EXTernal}
    - POWer:POWer<x>:CLRESPONSE:GENerator?
    - POWer:POWer<x>:CLRESPONSE:IMPEDance {FIFTy|HIGHZ}
    - POWer:POWer<x>:CLRESPONSE:IMPEDance?
    - POWer:POWer<x>:CLRESPONSE:INPUTSOurce CH<x>
    - POWer:POWer<x>:CLRESPONSE:INPUTSOurce?
    - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce CH<x>
    - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?
    - POWer:POWer<x>:CLRESPONSE:PPD <NR3>
    - POWer:POWer<x>:CLRESPONSE:PPD?
    - POWer:POWer<x>:CLRESPONSE:STARTFREQuency <NR3>
    - POWer:POWer<x>:CLRESPONSE:STARTFREQuency?
    - POWer:POWer<x>:CLRESPONSE:STOPFREQuency <NR3>
    - POWer:POWer<x>:CLRESPONSE:STOPFREQuency?
    - POWer:POWer<x>:CLRESPONSE:TESTCONNection EXECute
    - POWer:POWer<x>:PRESET {EXECute}
    - POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? {PM| GAINCROSSOVERFREQ| GM| PHASECROSSOVERFREQ}
    - POWer:POWer<x>:RESUlts:CURRentacq:MEAN? {PM| GAINCROSSOVERFREQ| GM| PHASECROSSOVERFREQ}
    - POWer:POWer<x>:RESUlts:CURRentacq:MINimum? {PM| GAINCROSSOVERFREQ| GM| PHASECROSSOVERFREQ}
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdReadWithArguments,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class PowerPowerItemResultsCurrentacqMinimum(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum`` command.

    Description:
        - This command queries the minimum value of the current acquisition for the measurement
          parameter in the specified power measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:MINimum? {PM| GAINCROSSOVERFREQ| GM| PHASECROSSOVERFREQ}
        ```

    Info:
        - ``POWer<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge. This must be POWer1.
        - ``<QString>`` is the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
        - ``'PM'`` returns the Phase margin value.
        - ``'GAINCROSSOVERFREQ'`` returns the Gain crossover frequency value.
        - ``'GM'`` returns the Gain margin value.
        - ``'PHASECROSSOVERFREQ'`` returns the Phase cross over frequency value.
    """


class PowerPowerItemResultsCurrentacqMean(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN`` command.

    Description:
        - This command queries the mean value of the current acquisition for the measurement
          parameter in the specified power measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:MEAN? {PM| GAINCROSSOVERFREQ| GM| PHASECROSSOVERFREQ}
        ```

    Info:
        - ``POWer<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge. This must be POWer1.
        - ``<QString>`` is the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
        - ``'PM'`` returns the Phase margin value.
        - ``'GAINCROSSOVERFREQ'`` returns the Gain crossover frequency value.
        - ``'GM'`` returns the Gain margin value.
        - ``'PHASECROSSOVERFREQ'`` returns the Phase cross over frequency value.
    """


class PowerPowerItemResultsCurrentacqMaximum(SCPICmdReadWithArguments):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum`` command.

    Description:
        - This command queries the maximum value of the current acquisition for the measurement
          parameter in the specified power measurement number.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? {PM| GAINCROSSOVERFREQ| GM| PHASECROSSOVERFREQ}
        ```

    Info:
        - ``POWer<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge. This must be POWer1.
        - ``<QString>`` is the measurement result that you want to return from the specified power
          measurement number. Available results depend on the power measurement being taken in the
          specified measurement number. The valid <Qstring> arguments are.
        - ``'PM'`` returns the Phase margin value.
        - ``'GAINCROSSOVERFREQ'`` returns the Gain crossover frequency value.
        - ``'GM'`` returns the Gain margin value.
        - ``'PHASECROSSOVERFREQ'`` returns the Phase cross over frequency value.
    """


class PowerPowerItemResultsCurrentacq(SCPICmdRead):
    """The ``POWer:POWer<x>:RESUlts:CURRentacq`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:RESUlts:CURRentacq?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RESUlts:CURRentacq?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``POWer<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge. This must be POWer1.

    Properties:
        - ``.maximum``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum`` command.
        - ``.mean``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN`` command.
        - ``.minimum``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._maximum = PowerPowerItemResultsCurrentacqMaximum(
            device, f"{self._cmd_syntax}:MAXimum"
        )
        self._mean = PowerPowerItemResultsCurrentacqMean(device, f"{self._cmd_syntax}:MEAN")
        self._minimum = PowerPowerItemResultsCurrentacqMinimum(
            device, f"{self._cmd_syntax}:MINimum"
        )

    @property
    def maximum(self) -> PowerPowerItemResultsCurrentacqMaximum:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum`` command.

        Description:
            - This command queries the maximum value of the current acquisition for the measurement
              parameter in the specified power measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:MAXimum? {PM| GAINCROSSOVERFREQ| GM| PHASECROSSOVERFREQ}
            ```

        Info:
            - ``POWer<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge. This must be POWer1.
            - ``<QString>`` is the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
            - ``'PM'`` returns the Phase margin value.
            - ``'GAINCROSSOVERFREQ'`` returns the Gain crossover frequency value.
            - ``'GM'`` returns the Gain margin value.
            - ``'PHASECROSSOVERFREQ'`` returns the Phase cross over frequency value.
        """  # noqa: E501
        return self._maximum

    @property
    def mean(self) -> PowerPowerItemResultsCurrentacqMean:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN`` command.

        Description:
            - This command queries the mean value of the current acquisition for the measurement
              parameter in the specified power measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:MEAN? {PM| GAINCROSSOVERFREQ| GM| PHASECROSSOVERFREQ}
            ```

        Info:
            - ``POWer<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge. This must be POWer1.
            - ``<QString>`` is the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
            - ``'PM'`` returns the Phase margin value.
            - ``'GAINCROSSOVERFREQ'`` returns the Gain crossover frequency value.
            - ``'GM'`` returns the Gain margin value.
            - ``'PHASECROSSOVERFREQ'`` returns the Phase cross over frequency value.
        """  # noqa: E501
        return self._mean

    @property
    def minimum(self) -> PowerPowerItemResultsCurrentacqMinimum:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum`` command.

        Description:
            - This command queries the minimum value of the current acquisition for the measurement
              parameter in the specified power measurement number.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:RESUlts:CURRentacq:MINimum? {PM| GAINCROSSOVERFREQ| GM| PHASECROSSOVERFREQ}
            ```

        Info:
            - ``POWer<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge. This must be POWer1.
            - ``<QString>`` is the measurement result that you want to return from the specified
              power measurement number. Available results depend on the power measurement being
              taken in the specified measurement number. The valid <Qstring> arguments are.
            - ``'PM'`` returns the Phase margin value.
            - ``'GAINCROSSOVERFREQ'`` returns the Gain crossover frequency value.
            - ``'GM'`` returns the Gain margin value.
            - ``'PHASECROSSOVERFREQ'`` returns the Phase cross over frequency value.
        """  # noqa: E501
        return self._minimum


class PowerPowerItemResults(SCPICmdRead):
    """The ``POWer:POWer<x>:RESUlts`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:RESUlts?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RESUlts?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``POWer<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge. This must be POWer1.

    Properties:
        - ``.currentacq``: The ``POWer:POWer<x>:RESUlts:CURRentacq`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._currentacq = PowerPowerItemResultsCurrentacq(device, f"{self._cmd_syntax}:CURRentacq")

    @property
    def currentacq(self) -> PowerPowerItemResultsCurrentacq:
        """Return the ``POWer:POWer<x>:RESUlts:CURRentacq`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:RESUlts:CURRentacq?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:RESUlts:CURRentacq?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Info:
            - ``POWer<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge. This must be POWer1.

        Sub-properties:
            - ``.maximum``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MAXimum`` command.
            - ``.mean``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MEAN`` command.
            - ``.minimum``: The ``POWer:POWer<x>:RESUlts:CURRentacq:MINimum`` command.
        """
        return self._currentacq


class PowerPowerItemPreset(SCPICmdWrite):
    """The ``POWer:POWer<x>:PRESET`` command.

    Description:
        - This command runs a power preset action for the specified power measurement number.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PRESET value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:PRESET {EXECute}
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``EXECute`` runs the power preset action.
    """


class PowerPowerItemClresponseTestconnection(SCPICmdWrite):
    """The ``POWer:POWer<x>:CLRESPONSE:TESTCONNection`` command.

    Description:
        - This command tests the connection to the external generator used with the specified
          Control Loop Response power measurement.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:TESTCONNection value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:TESTCONNection EXECute
        ```

    Info:
        - ``POWer<x>`` is the number of the PSRR power measurement.
        - ``EXECute`` runs the test connection function.
    """


class PowerPowerItemClresponseStopfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency`` command.

    Description:
        - This command sets or queries the stop frequency value for the Control Loop Response power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:STOPFREQuency <NR3>
        - POWer:POWer<x>:CLRESPONSE:STOPFREQuency?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the stop frequency for the measurement, in the range of 10 Hz to 50 MHz.
    """


class PowerPowerItemClresponseStartfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency`` command.

    Description:
        - This command sets or queries the start frequency value for the Control Loop Response power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:STARTFREQuency <NR3>
        - POWer:POWer<x>:CLRESPONSE:STARTFREQuency?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the starting frequency for the measurement, in the range of 10 Hz to 50 MHz.
    """


class PowerPowerItemClresponsePpd(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:PPD`` command.

    Description:
        - This command sets or queries the points per decade (PPD) value for the Control Loop
          Response power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:PPD?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:PPD?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:PPD value``
          command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:PPD <NR3>
        - POWer:POWer<x>:CLRESPONSE:PPD?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the PPD value for the measurement, in the range of 10 to 100 points.
    """


class PowerPowerItemClresponseOutputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce`` command.

    Description:
        - This command sets or queries the output source for the Control Loop Response power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce CH<x>
        - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` sets the channel to use for the output signal source.
    """


class PowerPowerItemClresponseInputsource(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce`` command.

    Description:
        - This command sets or queries the input source for the Control Loop Response power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:INPUTSOurce CH<x>
        - POWer:POWer<x>:CLRESPONSE:INPUTSOurce?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CH<x>`` sets the channel to use for the output signal source.
    """


class PowerPowerItemClresponseImpedance(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:IMPEDance`` command.

    Description:
        - This command sets or queries the vertical termination impedance for the Control Loop
          Response power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:IMPEDance?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:IMPEDance?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:IMPEDance value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:IMPEDance {FIFTy|HIGHZ}
        - POWer:POWer<x>:CLRESPONSE:IMPEDance?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``FIFTy`` sets the impedance to be 50 Ω.
        - ``HIGHZ`` sets the impedance to be 1 MΩ.
    """


class PowerPowerItemClresponseGenerator(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:GENerator`` command.

    Description:
        - Sets or queries the generator source for the specified Control Loop Response power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:GENerator?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:GENerator?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:GENerator value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:GENerator {INTernal|EXTernal}
        - POWer:POWer<x>:CLRESPONSE:GENerator?
        ```

    Info:
        - ``POWer<x>`` is the number of the power measurement.INTernal sets the internal generator
          as the source for the Control Loop Response power measurement.
        - ``EXTernal`` sets the external generator as the source for the Control Loop Response power
          measurement.
    """


class PowerPowerItemClresponseGenipaddress(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:GENIPADDress`` command.

    Description:
        - Sets or queries the IP address of the external generator to be used with the specified
          Control Loop Response measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:GENIPADDress?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:GENIPADDress?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:GENIPADDress value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:GENIPADDress <NR2>
        - POWer:POWer<x>:CLRESPONSE:GENIPADDress?
        ```

    Info:
        - ``POWer<x>`` is the number of the power measurement.<NR2> is the IP address of the
          generator.
    """


class PowerPowerItemClresponseFreqvalItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val`` command.

    Description:
        - This command sets or queries the generator frequency value of the specified configuration
          step for the Control Loop Response power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val <NR3>
        - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?
        ```

    Info:
        - ``Power<x>`` sets the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``FREQ<x>`` sets the configuration step number, in the range of 1 to 11. Values outside
          this range will report an error.
        - ``<NR3>`` sets the frequency of the specified configuration step number, in the range of
          10 Hz to 50 MHz.
    """


class PowerPowerItemClresponseConstamplitude(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude`` command.

    Description:
        - This command sets or queries the constant amplitude voltage for the Control Loop Response
          power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude <NR3>
        - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``<NR3>`` is the constant amplitude voltage value for the measurement, in the range of
          -100 V to 100 V.
    """


class PowerPowerItemClresponseConnectstatus(SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus`` command.

    Description:
        - Queries connection status to the external generator used with the specified Control Loop
          Response power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?
        ```

    Info:
        - ``POWer<x>`` is the number of the power measurement.
    """


class PowerPowerItemClresponseAnalysismethod(SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod`` command.

    Description:
        - This command sets or queries the Analysis Method for Control Loop Response measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?
        ```

    Info:
        - ``POWer<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge. This must be POWer1.
    """


class PowerPowerItemClresponseAmpmode(SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:AMPMode`` command.

    Description:
        - This command sets or queries the amplitude mode for the Control Loop Response power
          measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMPMode?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMPMode?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:AMPMode value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:AMPMode {CONSTant|PROFile}
        - POWer:POWer<x>:CLRESPONSE:AMPMode?
        ```

    Info:
        - ``Power<x>`` is the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``CONSTant`` sets the amplitude mode to output a constant amplitude signal from the DUT
          stimulus generator for all frequency bands.
        - ``PROFile`` enables configuring the generator to set amplitude values for each frequency
          band.
    """


class PowerPowerItemClresponseAmpvalItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val`` command.

    Description:
        - This command sets or queries the generator amplitude value of the specified configuration
          step for the Control Loop Response power measurement.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val?``
          query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val value`` command.

    SCPI Syntax:
        ```
        - POWer:POWer<x>:CLRESPONSE:AMP<x>Val <NR3>
        - POWer:POWer<x>:CLRESPONSE:AMP<x>Val?
        ```

    Info:
        - ``Power<x>`` sets the power measurement number. This is the equivalent of the number shown
          in the UI for a power measurement badge.
        - ``AMP<x>`` sets the configuration step number, in the range of 1 to 10. Values outside
          this range will report an error.
        - ``<NR3>`` sets the generator amplitude for the specified configuration step, in the range
          of -100 V to 100 V.
    """


#  pylint: disable=too-many-instance-attributes
class PowerPowerItemClresponse(SCPICmdRead):
    """The ``POWer:POWer<x>:CLRESPONSE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ampval``: The ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val`` command.
        - ``.ampmode``: The ``POWer:POWer<x>:CLRESPONSE:AMPMode`` command.
        - ``.analysismethod``: The ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod`` command.
        - ``.connectstatus``: The ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus`` command.
        - ``.constamplitude``: The ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude`` command.
        - ``.freqval``: The ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val`` command.
        - ``.genipaddress``: The ``POWer:POWer<x>:CLRESPONSE:GENIPADDress`` command.
        - ``.generator``: The ``POWer:POWer<x>:CLRESPONSE:GENerator`` command.
        - ``.impedance``: The ``POWer:POWer<x>:CLRESPONSE:IMPEDance`` command.
        - ``.inputsource``: The ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce`` command.
        - ``.outputsource``: The ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce`` command.
        - ``.ppd``: The ``POWer:POWer<x>:CLRESPONSE:PPD`` command.
        - ``.startfrequency``: The ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency`` command.
        - ``.stopfrequency``: The ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency`` command.
        - ``.testconnection``: The ``POWer:POWer<x>:CLRESPONSE:TESTCONNection`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ampval: Dict[int, PowerPowerItemClresponseAmpvalItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerPowerItemClresponseAmpvalItem(device, f"{self._cmd_syntax}:AMP{x}Val")
        )
        self._ampmode = PowerPowerItemClresponseAmpmode(device, f"{self._cmd_syntax}:AMPMode")
        self._analysismethod = PowerPowerItemClresponseAnalysismethod(
            device, f"{self._cmd_syntax}:ANALYSISMethod"
        )
        self._connectstatus = PowerPowerItemClresponseConnectstatus(
            device, f"{self._cmd_syntax}:CONNECTSTATus"
        )
        self._constamplitude = PowerPowerItemClresponseConstamplitude(
            device, f"{self._cmd_syntax}:CONSTAMPlitude"
        )
        self._freqval: Dict[int, PowerPowerItemClresponseFreqvalItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerPowerItemClresponseFreqvalItem(device, f"{self._cmd_syntax}:FREQ{x}Val")
        )
        self._genipaddress = PowerPowerItemClresponseGenipaddress(
            device, f"{self._cmd_syntax}:GENIPADDress"
        )
        self._generator = PowerPowerItemClresponseGenerator(device, f"{self._cmd_syntax}:GENerator")
        self._impedance = PowerPowerItemClresponseImpedance(device, f"{self._cmd_syntax}:IMPEDance")
        self._inputsource = PowerPowerItemClresponseInputsource(
            device, f"{self._cmd_syntax}:INPUTSOurce"
        )
        self._outputsource = PowerPowerItemClresponseOutputsource(
            device, f"{self._cmd_syntax}:OUTPUTSOurce"
        )
        self._ppd = PowerPowerItemClresponsePpd(device, f"{self._cmd_syntax}:PPD")
        self._startfrequency = PowerPowerItemClresponseStartfrequency(
            device, f"{self._cmd_syntax}:STARTFREQuency"
        )
        self._stopfrequency = PowerPowerItemClresponseStopfrequency(
            device, f"{self._cmd_syntax}:STOPFREQuency"
        )
        self._testconnection = PowerPowerItemClresponseTestconnection(
            device, f"{self._cmd_syntax}:TESTCONNection"
        )

    @property
    def ampval(self) -> Dict[int, PowerPowerItemClresponseAmpvalItem]:
        """Return the ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val`` command.

        Description:
            - This command sets or queries the generator amplitude value of the specified
              configuration step for the Control Loop Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:AMP<x>Val <NR3>
            - POWer:POWer<x>:CLRESPONSE:AMP<x>Val?
            ```

        Info:
            - ``Power<x>`` sets the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``AMP<x>`` sets the configuration step number, in the range of 1 to 10. Values outside
              this range will report an error.
            - ``<NR3>`` sets the generator amplitude for the specified configuration step, in the
              range of -100 V to 100 V.
        """
        return self._ampval

    @property
    def ampmode(self) -> PowerPowerItemClresponseAmpmode:
        """Return the ``POWer:POWer<x>:CLRESPONSE:AMPMode`` command.

        Description:
            - This command sets or queries the amplitude mode for the Control Loop Response power
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:AMPMode?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:AMPMode?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:AMPMode value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:AMPMode {CONSTant|PROFile}
            - POWer:POWer<x>:CLRESPONSE:AMPMode?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CONSTant`` sets the amplitude mode to output a constant amplitude signal from the
              DUT stimulus generator for all frequency bands.
            - ``PROFile`` enables configuring the generator to set amplitude values for each
              frequency band.
        """
        return self._ampmode

    @property
    def analysismethod(self) -> PowerPowerItemClresponseAnalysismethod:
        """Return the ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod`` command.

        Description:
            - This command sets or queries the Analysis Method for Control Loop Response
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:ANALYSISMethod?
            ```

        Info:
            - ``POWer<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge. This must be POWer1.
        """
        return self._analysismethod

    @property
    def connectstatus(self) -> PowerPowerItemClresponseConnectstatus:
        """Return the ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus`` command.

        Description:
            - Queries connection status to the external generator used with the specified Control
              Loop Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:CONNECTSTATus?
            ```

        Info:
            - ``POWer<x>`` is the number of the power measurement.
        """
        return self._connectstatus

    @property
    def constamplitude(self) -> PowerPowerItemClresponseConstamplitude:
        """Return the ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude`` command.

        Description:
            - This command sets or queries the constant amplitude voltage for the Control Loop
              Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude <NR3>
            - POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the constant amplitude voltage value for the measurement, in the range of
              -100 V to 100 V.
        """
        return self._constamplitude

    @property
    def freqval(self) -> Dict[int, PowerPowerItemClresponseFreqvalItem]:
        """Return the ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val`` command.

        Description:
            - This command sets or queries the generator frequency value of the specified
              configuration step for the Control Loop Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val <NR3>
            - POWer:POWer<x>:CLRESPONSE:FREQ<x>Val?
            ```

        Info:
            - ``Power<x>`` sets the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``FREQ<x>`` sets the configuration step number, in the range of 1 to 11. Values
              outside this range will report an error.
            - ``<NR3>`` sets the frequency of the specified configuration step number, in the range
              of 10 Hz to 50 MHz.
        """
        return self._freqval

    @property
    def genipaddress(self) -> PowerPowerItemClresponseGenipaddress:
        """Return the ``POWer:POWer<x>:CLRESPONSE:GENIPADDress`` command.

        Description:
            - Sets or queries the IP address of the external generator to be used with the specified
              Control Loop Response measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:GENIPADDress?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:GENIPADDress?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:GENIPADDress value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:GENIPADDress <NR2>
            - POWer:POWer<x>:CLRESPONSE:GENIPADDress?
            ```

        Info:
            - ``POWer<x>`` is the number of the power measurement.<NR2> is the IP address of the
              generator.
        """
        return self._genipaddress

    @property
    def generator(self) -> PowerPowerItemClresponseGenerator:
        """Return the ``POWer:POWer<x>:CLRESPONSE:GENerator`` command.

        Description:
            - Sets or queries the generator source for the specified Control Loop Response power
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:GENerator?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:GENerator?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:GENerator value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:GENerator {INTernal|EXTernal}
            - POWer:POWer<x>:CLRESPONSE:GENerator?
            ```

        Info:
            - ``POWer<x>`` is the number of the power measurement.INTernal sets the internal
              generator as the source for the Control Loop Response power measurement.
            - ``EXTernal`` sets the external generator as the source for the Control Loop Response
              power measurement.
        """
        return self._generator

    @property
    def impedance(self) -> PowerPowerItemClresponseImpedance:
        """Return the ``POWer:POWer<x>:CLRESPONSE:IMPEDance`` command.

        Description:
            - This command sets or queries the vertical termination impedance for the Control Loop
              Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:IMPEDance?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:IMPEDance?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:IMPEDance value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:IMPEDance {FIFTy|HIGHZ}
            - POWer:POWer<x>:CLRESPONSE:IMPEDance?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``FIFTy`` sets the impedance to be 50 Ω.
            - ``HIGHZ`` sets the impedance to be 1 MΩ.
        """
        return self._impedance

    @property
    def inputsource(self) -> PowerPowerItemClresponseInputsource:
        """Return the ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce`` command.

        Description:
            - This command sets or queries the input source for the Control Loop Response power
              measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:INPUTSOurce CH<x>
            - POWer:POWer<x>:CLRESPONSE:INPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` sets the channel to use for the output signal source.
        """
        return self._inputsource

    @property
    def outputsource(self) -> PowerPowerItemClresponseOutputsource:
        """Return the ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce`` command.

        Description:
            - This command sets or queries the output source for the Control Loop Response power
              measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce CH<x>
            - POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``CH<x>`` sets the channel to use for the output signal source.
        """
        return self._outputsource

    @property
    def ppd(self) -> PowerPowerItemClresponsePpd:
        """Return the ``POWer:POWer<x>:CLRESPONSE:PPD`` command.

        Description:
            - This command sets or queries the points per decade (PPD) value for the Control Loop
              Response power measurement.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE:PPD?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE:PPD?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:PPD value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:PPD <NR3>
            - POWer:POWer<x>:CLRESPONSE:PPD?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the PPD value for the measurement, in the range of 10 to 100 points.
        """
        return self._ppd

    @property
    def startfrequency(self) -> PowerPowerItemClresponseStartfrequency:
        """Return the ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency`` command.

        Description:
            - This command sets or queries the start frequency value for the Control Loop Response
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:STARTFREQuency <NR3>
            - POWer:POWer<x>:CLRESPONSE:STARTFREQuency?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the starting frequency for the measurement, in the range of 10 Hz to 50
              MHz.
        """
        return self._startfrequency

    @property
    def stopfrequency(self) -> PowerPowerItemClresponseStopfrequency:
        """Return the ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency`` command.

        Description:
            - This command sets or queries the stop frequency value for the Control Loop Response
              power measurement.

        Usage:
            - Using the ``.query()`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:STOPFREQuency <NR3>
            - POWer:POWer<x>:CLRESPONSE:STOPFREQuency?
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``<NR3>`` is the stop frequency for the measurement, in the range of 10 Hz to 50 MHz.
        """
        return self._stopfrequency

    @property
    def testconnection(self) -> PowerPowerItemClresponseTestconnection:
        """Return the ``POWer:POWer<x>:CLRESPONSE:TESTCONNection`` command.

        Description:
            - This command tests the connection to the external generator used with the specified
              Control Loop Response power measurement.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``POWer:POWer<x>:CLRESPONSE:TESTCONNection value`` command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:CLRESPONSE:TESTCONNection EXECute
            ```

        Info:
            - ``POWer<x>`` is the number of the PSRR power measurement.
            - ``EXECute`` runs the test connection function.
        """
        return self._testconnection


class PowerPowerItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``POWer:POWer<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer:POWer<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.clresponse``: The ``POWer:POWer<x>:CLRESPONSE`` command tree.
        - ``.preset``: The ``POWer:POWer<x>:PRESET`` command.
        - ``.results``: The ``POWer:POWer<x>:RESUlts`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._clresponse = PowerPowerItemClresponse(device, f"{self._cmd_syntax}:CLRESPONSE")
        self._preset = PowerPowerItemPreset(device, f"{self._cmd_syntax}:PRESET")
        self._results = PowerPowerItemResults(device, f"{self._cmd_syntax}:RESUlts")

    @property
    def clresponse(self) -> PowerPowerItemClresponse:
        """Return the ``POWer:POWer<x>:CLRESPONSE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:CLRESPONSE?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:CLRESPONSE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ampval``: The ``POWer:POWer<x>:CLRESPONSE:AMP<x>Val`` command.
            - ``.ampmode``: The ``POWer:POWer<x>:CLRESPONSE:AMPMode`` command.
            - ``.analysismethod``: The ``POWer:POWer<x>:CLRESPONSE:ANALYSISMethod`` command.
            - ``.connectstatus``: The ``POWer:POWer<x>:CLRESPONSE:CONNECTSTATus`` command.
            - ``.constamplitude``: The ``POWer:POWer<x>:CLRESPONSE:CONSTAMPlitude`` command.
            - ``.freqval``: The ``POWer:POWer<x>:CLRESPONSE:FREQ<x>Val`` command.
            - ``.genipaddress``: The ``POWer:POWer<x>:CLRESPONSE:GENIPADDress`` command.
            - ``.generator``: The ``POWer:POWer<x>:CLRESPONSE:GENerator`` command.
            - ``.impedance``: The ``POWer:POWer<x>:CLRESPONSE:IMPEDance`` command.
            - ``.inputsource``: The ``POWer:POWer<x>:CLRESPONSE:INPUTSOurce`` command.
            - ``.outputsource``: The ``POWer:POWer<x>:CLRESPONSE:OUTPUTSOurce`` command.
            - ``.ppd``: The ``POWer:POWer<x>:CLRESPONSE:PPD`` command.
            - ``.startfrequency``: The ``POWer:POWer<x>:CLRESPONSE:STARTFREQuency`` command.
            - ``.stopfrequency``: The ``POWer:POWer<x>:CLRESPONSE:STOPFREQuency`` command.
            - ``.testconnection``: The ``POWer:POWer<x>:CLRESPONSE:TESTCONNection`` command.
        """
        return self._clresponse

    @property
    def preset(self) -> PowerPowerItemPreset:
        """Return the ``POWer:POWer<x>:PRESET`` command.

        Description:
            - This command runs a power preset action for the specified power measurement number.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:POWer<x>:PRESET value``
              command.

        SCPI Syntax:
            ```
            - POWer:POWer<x>:PRESET {EXECute}
            ```

        Info:
            - ``Power<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge.
            - ``EXECute`` runs the power preset action.
        """
        return self._preset

    @property
    def results(self) -> PowerPowerItemResults:
        """Return the ``POWer:POWer<x>:RESUlts`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>:RESUlts?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>:RESUlts?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``POWer<x>`` is the power measurement number. This is the equivalent of the number
              shown in the UI for a power measurement badge. This must be POWer1.

        Sub-properties:
            - ``.currentacq``: The ``POWer:POWer<x>:RESUlts:CURRentacq`` command tree.
        """
        return self._results


class PowerDelete(SCPICmdWrite):
    """The ``POWer:DELete`` command.

    Description:
        - This command deletes the specified power measurement number. The power measurement number
          is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:DELete value`` command.

    SCPI Syntax:
        ```
        - POWer:DELete 'POWER<x>'
        ```
    """


class PowerAddnew(SCPICmdWrite):
    """The ``POWer:ADDNew`` command.

    Description:
        - This command adds the specified power measurement number. The power measurement number is
          specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``POWer:ADDNew value`` command.

    SCPI Syntax:
        ```
        - POWer:ADDNew 'POWER<x>'
        ```
    """


class Power(SCPICmdRead):
    """The ``POWer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``POWer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``POWer:ADDNew`` command.
        - ``.delete``: The ``POWer:DELete`` command.
        - ``.power``: The ``POWer:POWer<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "POWer") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = PowerAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = PowerDelete(device, f"{self._cmd_syntax}:DELete")
        self._power: Dict[int, PowerPowerItem] = DefaultDictPassKeyToFactory(
            lambda x: PowerPowerItem(device, f"{self._cmd_syntax}:POWer{x}")
        )

    @property
    def addnew(self) -> PowerAddnew:
        """Return the ``POWer:ADDNew`` command.

        Description:
            - This command adds the specified power measurement number. The power measurement number
              is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:ADDNew value`` command.

        SCPI Syntax:
            ```
            - POWer:ADDNew 'POWER<x>'
            ```
        """
        return self._addnew

    @property
    def delete(self) -> PowerDelete:
        """Return the ``POWer:DELete`` command.

        Description:
            - This command deletes the specified power measurement number. The power measurement
              number is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``POWer:DELete value`` command.

        SCPI Syntax:
            ```
            - POWer:DELete 'POWER<x>'
            ```
        """
        return self._delete

    @property
    def power(self) -> Dict[int, PowerPowerItem]:
        """Return the ``POWer:POWer<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``POWer:POWer<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``POWer:POWer<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.clresponse``: The ``POWer:POWer<x>:CLRESPONSE`` command tree.
            - ``.preset``: The ``POWer:POWer<x>:PRESET`` command.
            - ``.results``: The ``POWer:POWer<x>:RESUlts`` command tree.
        """
        return self._power
