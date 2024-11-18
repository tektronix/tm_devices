# pylint: disable=line-too-long
"""The afg commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AFG:AMPLitude <NR3>
    - AFG:AMPLitude?
    - AFG:ARBitrary:ARB<x>:DATE?
    - AFG:ARBitrary:ARB<x>:LABel <QString>
    - AFG:ARBitrary:ARB<x>:LABel?
    - AFG:ARBitrary:ARB<x>:TIMe?
    - AFG:ARBitrary:EMEM:FUNCtion?
    - AFG:ARBitrary:EMEM:GENerate {SINE|SQUare|PULSe|RAMP|NOISe[,NR1]}
    - AFG:ARBitrary:EMEM:GENerate?
    - AFG:ARBitrary:EMEM:NUMPoints?
    - AFG:ARBitrary:EMEM:POINTS <BlockWfmInDTO> |<NrfWfmInDTO>
    - AFG:ARBitrary:EMEM:POINTS:BYTEORDer <LSB> |<MSB>
    - AFG:ARBitrary:EMEM:POINTS:BYTEORDer?
    - AFG:ARBitrary:EMEM:POINTS:ENCdg {ASCii|BINary}
    - AFG:ARBitrary:EMEM:POINTS:ENCdg?
    - AFG:ARBitrary:EMEM:POINTS?
    - AFG:FREQuency <NR3>
    - AFG:FREQuency?
    - AFG:FUNCtion {SINE|SQUare|PULSe|RAMP|NOISe|DC|SINC|GAUSsian|LORENtz|ERISe|EDECAy|HAVERSINe|CARDIac|ARBitrary}
    - AFG:FUNCtion?
    - AFG:HIGHLevel <NR3>
    - AFG:HIGHLevel?
    - AFG:LEVELPreset {CMOS_5_0V|CMOS_3_3V|CMOS_2_5V|ECL|TTL|USER}
    - AFG:LEVELPreset?
    - AFG:LOWLevel <NR3>
    - AFG:LOWLevel?
    - AFG:NOISEAdd:PERCent <NR3>
    - AFG:NOISEAdd:PERCent?
    - AFG:NOISEAdd:STATE {0|1|OFF|ON}
    - AFG:NOISEAdd:STATE?
    - AFG:OFFSet <NR3>
    - AFG:OFFSet?
    - AFG:OUTPut:LOAd:IMPEDance {FIFty|HIGHZ}
    - AFG:OUTPut:LOAd:IMPEDance?
    - AFG:OUTPut:STATE {0|1|OFF|ON}
    - AFG:OUTPut:STATE?
    - AFG:PERIod <NR3>
    - AFG:PERIod?
    - AFG:PHASe <NR3>
    - AFG:PHASe?
    - AFG:PULse:WIDth <NR3>
    - AFG:PULse:WIDth?
    - AFG:RAMP:SYMmetry <NR3>
    - AFG:RAMP:SYMmetry?
    - AFG:SQUare:DUty <NR3>
    - AFG:SQUare:DUty?
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


class AfgSquareDuty(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:SQUare:DUty`` command.

    Description:
        - Sets (or queries) the AFG duty cycle in percent. The minimum is 10.0%, maximum is 90.0%
          and increment is 0.10%.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:SQUare:DUty?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:SQUare:DUty?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:SQUare:DUty value`` command.

    SCPI Syntax:
        ```
        - AFG:SQUare:DUty <NR3>
        - AFG:SQUare:DUty?
        ```

    Info:
        - ``<NR3>`` is the floating point number that represents the AFG duty cycle, as a
          percentage.
    """


class AfgSquare(SCPICmdRead):
    """The ``AFG:SQUare`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:SQUare?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:SQUare?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.duty``: The ``AFG:SQUare:DUty`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._duty = AfgSquareDuty(device, f"{self._cmd_syntax}:DUty")

    @property
    def duty(self) -> AfgSquareDuty:
        """Return the ``AFG:SQUare:DUty`` command.

        Description:
            - Sets (or queries) the AFG duty cycle in percent. The minimum is 10.0%, maximum is
              90.0% and increment is 0.10%.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:SQUare:DUty?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:SQUare:DUty?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:SQUare:DUty value`` command.

        SCPI Syntax:
            ```
            - AFG:SQUare:DUty <NR3>
            - AFG:SQUare:DUty?
            ```

        Info:
            - ``<NR3>`` is the floating point number that represents the AFG duty cycle, as a
              percentage.
        """
        return self._duty


class AfgRampSymmetry(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:RAMP:SYMmetry`` command.

    Description:
        - Sets (or queries) the AFG ramp symmetry in percent. Minimum is 0.0%, maximum is 100.0% and
          increment is 0.10%.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:RAMP:SYMmetry?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:RAMP:SYMmetry?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:RAMP:SYMmetry value`` command.

    SCPI Syntax:
        ```
        - AFG:RAMP:SYMmetry <NR3>
        - AFG:RAMP:SYMmetry?
        ```

    Info:
        - ``<NR3>`` is the floating point number that represents the AFG ramp symmetry, as a
          percentage.
    """


class AfgRamp(SCPICmdRead):
    """The ``AFG:RAMP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:RAMP?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:RAMP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.symmetry``: The ``AFG:RAMP:SYMmetry`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._symmetry = AfgRampSymmetry(device, f"{self._cmd_syntax}:SYMmetry")

    @property
    def symmetry(self) -> AfgRampSymmetry:
        """Return the ``AFG:RAMP:SYMmetry`` command.

        Description:
            - Sets (or queries) the AFG ramp symmetry in percent. Minimum is 0.0%, maximum is 100.0%
              and increment is 0.10%.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:RAMP:SYMmetry?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:RAMP:SYMmetry?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:RAMP:SYMmetry value`` command.

        SCPI Syntax:
            ```
            - AFG:RAMP:SYMmetry <NR3>
            - AFG:RAMP:SYMmetry?
            ```

        Info:
            - ``<NR3>`` is the floating point number that represents the AFG ramp symmetry, as a
              percentage.
        """
        return self._symmetry


class AfgPulseWidth(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:PULse:WIDth`` command.

    Description:
        - Sets (or queries) the AFG pulse width, in seconds.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:PULse:WIDth?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:PULse:WIDth?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:PULse:WIDth value`` command.

    SCPI Syntax:
        ```
        - AFG:PULse:WIDth <NR3>
        - AFG:PULse:WIDth?
        ```

    Info:
        - ``<NR3>`` is the floating point number that represents the pulse width, in seconds.
    """


class AfgPulse(SCPICmdRead):
    """The ``AFG:PULse`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:PULse?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:PULse?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.width``: The ``AFG:PULse:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._width = AfgPulseWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def width(self) -> AfgPulseWidth:
        """Return the ``AFG:PULse:WIDth`` command.

        Description:
            - Sets (or queries) the AFG pulse width, in seconds.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:PULse:WIDth?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:PULse:WIDth?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:PULse:WIDth value`` command.

        SCPI Syntax:
            ```
            - AFG:PULse:WIDth <NR3>
            - AFG:PULse:WIDth?
            ```

        Info:
            - ``<NR3>`` is the floating point number that represents the pulse width, in seconds.
        """
        return self._width


class AfgPhase(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:PHASe`` command.

    Description:
        - Sets (or queries) the AFG phase. The AFG phase setting controls the phase difference
          between the trigger signal output and the AFG waveform output. Phase is expressed in
          degrees and ranges from -180.0 to 180.0 in increments of 0.1 degrees.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:PHASe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:PHASe value`` command.

    SCPI Syntax:
        ```
        - AFG:PHASe <NR3>
        - AFG:PHASe?
        ```
    """


class AfgPeriod(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:PERIod`` command.

    Description:
        - Sets (or queries) the period of the AFG waveform, in seconds.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:PERIod?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:PERIod?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:PERIod value`` command.

    SCPI Syntax:
        ```
        - AFG:PERIod <NR3>
        - AFG:PERIod?
        ```

    Info:
        - ``NR3`` is the floating point number that represents the AFG period value, in seconds.
    """


class AfgOutputState(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:OUTPut:STATE`` command.

    Description:
        - Sets (or queries) the AFG output state.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:OUTPut:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:OUTPut:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:OUTPut:STATE value`` command.

    SCPI Syntax:
        ```
        - AFG:OUTPut:STATE {0|1|OFF|ON}
        - AFG:OUTPut:STATE?
        ```

    Info:
        - ``1`` or ON turns on the AFG output state.
        - ``0`` or OFF turns it off.
    """


class AfgOutputLoadImpedance(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:OUTPut:LOAd:IMPEDance`` command.

    Description:
        - Sets (or queries) the AFG output load impedance.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:OUTPut:LOAd:IMPEDance?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:OUTPut:LOAd:IMPEDance?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:OUTPut:LOAd:IMPEDance value``
          command.

    SCPI Syntax:
        ```
        - AFG:OUTPut:LOAd:IMPEDance {FIFty|HIGHZ}
        - AFG:OUTPut:LOAd:IMPEDance?
        ```

    Info:
        - ``FIFty`` sets the output load impedance to 50 Ohms.
        - ``HIGHZ`` sets the output load impedance to the high-impedance state.
    """


class AfgOutputLoad(SCPICmdRead):
    """The ``AFG:OUTPut:LOAd`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:OUTPut:LOAd?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:OUTPut:LOAd?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.impedance``: The ``AFG:OUTPut:LOAd:IMPEDance`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._impedance = AfgOutputLoadImpedance(device, f"{self._cmd_syntax}:IMPEDance")

    @property
    def impedance(self) -> AfgOutputLoadImpedance:
        """Return the ``AFG:OUTPut:LOAd:IMPEDance`` command.

        Description:
            - Sets (or queries) the AFG output load impedance.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:OUTPut:LOAd:IMPEDance?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:OUTPut:LOAd:IMPEDance?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:OUTPut:LOAd:IMPEDance value``
              command.

        SCPI Syntax:
            ```
            - AFG:OUTPut:LOAd:IMPEDance {FIFty|HIGHZ}
            - AFG:OUTPut:LOAd:IMPEDance?
            ```

        Info:
            - ``FIFty`` sets the output load impedance to 50 Ohms.
            - ``HIGHZ`` sets the output load impedance to the high-impedance state.
        """
        return self._impedance


class AfgOutput(SCPICmdRead):
    """The ``AFG:OUTPut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:OUTPut?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:OUTPut?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.load``: The ``AFG:OUTPut:LOAd`` command tree.
        - ``.state``: The ``AFG:OUTPut:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._load = AfgOutputLoad(device, f"{self._cmd_syntax}:LOAd")
        self._state = AfgOutputState(device, f"{self._cmd_syntax}:STATE")

    @property
    def load(self) -> AfgOutputLoad:
        """Return the ``AFG:OUTPut:LOAd`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:OUTPut:LOAd?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:OUTPut:LOAd?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.impedance``: The ``AFG:OUTPut:LOAd:IMPEDance`` command.
        """
        return self._load

    @property
    def state(self) -> AfgOutputState:
        """Return the ``AFG:OUTPut:STATE`` command.

        Description:
            - Sets (or queries) the AFG output state.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:OUTPut:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:OUTPut:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:OUTPut:STATE value`` command.

        SCPI Syntax:
            ```
            - AFG:OUTPut:STATE {0|1|OFF|ON}
            - AFG:OUTPut:STATE?
            ```

        Info:
            - ``1`` or ON turns on the AFG output state.
            - ``0`` or OFF turns it off.
        """
        return self._state


class AfgOffset(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:OFFSet`` command.

    Description:
        - Sets (or queries) the AFG offset value, in volts.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:OFFSet?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:OFFSet value`` command.

    SCPI Syntax:
        ```
        - AFG:OFFSet <NR3>
        - AFG:OFFSet?
        ```

    Info:
        - ``<NR3>`` is a floating point number that represents the AFG offset, in volts.
    """


class AfgNoiseaddState(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:NOISEAdd:STATE`` command.

    Description:
        - Sets (or queries) the AFG additive noise state.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:NOISEAdd:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:NOISEAdd:STATE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:NOISEAdd:STATE value`` command.

    SCPI Syntax:
        ```
        - AFG:NOISEAdd:STATE {0|1|OFF|ON}
        - AFG:NOISEAdd:STATE?
        ```

    Info:
        - ``1`` or ON turns on the AFG additive noise state.
        - ``0`` or OFF turns it off.
    """


class AfgNoiseaddPercent(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:NOISEAdd:PERCent`` command.

    Description:
        - Sets (or queries) the AFG additive noise level as a percentage. Minimum is 0.0%, maximum
          is 100.0% and increment is 1.0%.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:NOISEAdd:PERCent?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:NOISEAdd:PERCent?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:NOISEAdd:PERCent value`` command.

    SCPI Syntax:
        ```
        - AFG:NOISEAdd:PERCent <NR3>
        - AFG:NOISEAdd:PERCent?
        ```

    Info:
        - ``<NR3>`` is the floating point number that represents the AFG additive noise level, as a
          percentage.
    """


class AfgNoiseadd(SCPICmdRead):
    """The ``AFG:NOISEAdd`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:NOISEAdd?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:NOISEAdd?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.percent``: The ``AFG:NOISEAdd:PERCent`` command.
        - ``.state``: The ``AFG:NOISEAdd:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._percent = AfgNoiseaddPercent(device, f"{self._cmd_syntax}:PERCent")
        self._state = AfgNoiseaddState(device, f"{self._cmd_syntax}:STATE")

    @property
    def percent(self) -> AfgNoiseaddPercent:
        """Return the ``AFG:NOISEAdd:PERCent`` command.

        Description:
            - Sets (or queries) the AFG additive noise level as a percentage. Minimum is 0.0%,
              maximum is 100.0% and increment is 1.0%.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:NOISEAdd:PERCent?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:NOISEAdd:PERCent?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:NOISEAdd:PERCent value``
              command.

        SCPI Syntax:
            ```
            - AFG:NOISEAdd:PERCent <NR3>
            - AFG:NOISEAdd:PERCent?
            ```

        Info:
            - ``<NR3>`` is the floating point number that represents the AFG additive noise level,
              as a percentage.
        """
        return self._percent

    @property
    def state(self) -> AfgNoiseaddState:
        """Return the ``AFG:NOISEAdd:STATE`` command.

        Description:
            - Sets (or queries) the AFG additive noise state.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:NOISEAdd:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:NOISEAdd:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:NOISEAdd:STATE value`` command.

        SCPI Syntax:
            ```
            - AFG:NOISEAdd:STATE {0|1|OFF|ON}
            - AFG:NOISEAdd:STATE?
            ```

        Info:
            - ``1`` or ON turns on the AFG additive noise state.
            - ``0`` or OFF turns it off.
        """
        return self._state


class AfgLowlevel(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:LOWLevel`` command.

    Description:
        - This command sets (or queries) the low level value of the output waveform, in volts, when
          using the arbitrary function generator feature.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:LOWLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:LOWLevel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:LOWLevel value`` command.

    SCPI Syntax:
        ```
        - AFG:LOWLevel <NR3>
        - AFG:LOWLevel?
        ```

    Info:
        - ``<NR3>`` is the floating point number that represents the AFG low level value, in volts.
    """


class AfgLevelpreset(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:LEVELPreset`` command.

    Description:
        - Sets (or queries) the AFG preset levels to values that correspond to the logic standard
          specified by the argument. The presets set the following vertical controls: AMPLitude
          OFFSet HIGHLevel LOWLevel Note that once any of these vertical settings are changed from
          the preset values, or the output load impedance is changed, the query form returns USER.
          The ``AFG:LEVELPreset`` command sets the high level and low level values as follows:
          ``AFG:HIGHLevel`` and ``AFG:LOWLevel Setting`` Values Load Impedance FIFTY Ohm Load
          Impedance HIGHZ LEVEL Preset High Low High Low TTL N/A 5.0V ``CMOS_5_0V N``/A 5.0V
          ``CMOS_3_3V 2``.5V 0V 3.3V 0V ``CMOS_2_5V 2``.5V 0V 2.5V 0V ECL -0.85V -1.65V -0.9V -1.7V

    Usage:
        - Using the ``.query()`` method will send the ``AFG:LEVELPreset?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:LEVELPreset?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:LEVELPreset value`` command.

    SCPI Syntax:
        ```
        - AFG:LEVELPreset {CMOS_5_0V|CMOS_3_3V|CMOS_2_5V|ECL|TTL|USER}
        - AFG:LEVELPreset?
        ```

    Info:
        - ``CMOS_5_0V`` - standard 5-volt CMOS levels. Not available when the load impedance is 50
          Ohm.
        - ``CMOS_3_3V`` - standard 3.3-volt CMOS levels.
        - ``CMOS_2_5V`` - standard 2.5-volt CMOS levels.
        - ``USER`` - user-defined.
        - ``ECL`` - -1.7 to -0.9 volts (note the full range is not available in 50 Ohm - actual is
          -1.65 to -0.85. See table below.
        - ``TTL`` - 5.0 volts. Not available when the load impedance is 50 Ohm.
    """


class AfgHighlevel(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:HIGHLevel`` command.

    Description:
        - This command sets (or queries) the high level value of the output waveform, in volts, when
          using the arbitrary function generator feature.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:HIGHLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:HIGHLevel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:HIGHLevel value`` command.

    SCPI Syntax:
        ```
        - AFG:HIGHLevel <NR3>
        - AFG:HIGHLevel?
        ```

    Info:
        - ``<NR3>`` is a floating point number that represents the AFG high level value, in volts.
    """


class AfgFunction(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:FUNCtion`` command.

    Description:
        - Sets (or queries) which AFG function to execute.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:FUNCtion?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - AFG:FUNCtion {SINE|SQUare|PULSe|RAMP|NOISe|DC|SINC|GAUSsian|LORENtz|ERISe|EDECAy|HAVERSINe|CARDIac|ARBitrary}
        - AFG:FUNCtion?
        ```

    Info:
        - ``SINE``
        - ``SQUare``
        - ``PULSe``
        - ``RAMP``
        - ``NOISe``
        - ``DC`` . The DC level is controlled by ``AFG:OFFSET``.
        - ``SINC`` (Sin(x)/x).
        - ``GAUSsian``
        - ``LORENtz``
        - ``ERISe``
        - ``EDECAy``
        - ``HAVERSINe``
        - ``CARDIac``
        - ``ARBitrary``
    """  # noqa: E501


class AfgFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:FREQuency`` command.

    Description:
        - Sets (or queries) the AFG frequency, in Hz.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:FREQuency?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:FREQuency value`` command.

    SCPI Syntax:
        ```
        - AFG:FREQuency <NR3>
        - AFG:FREQuency?
        ```

    Info:
        - ``<NR3>`` is the floating point number that represents the AFG frequency, in Hz.
    """


class AfgArbitraryEmemPointsEncdg(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:ARBitrary:EMEM:POINTS:ENCdg`` command.

    Description:
        - This command specifies the data encoding format for the ``AFG:ARBITRARY:EMEM:POINTS``
          query (either ASCII or binary). The default is ASCii. This setting is non-volatile and is
          reset by default setup or TekSecure. Refer to the ``AFG:ARBITRARY:EMEM:POINTS`` command
          description for more information.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:POINTS:ENCdg?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM:POINTS:ENCdg?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:ARBitrary:EMEM:POINTS:ENCdg value``
          command.

    SCPI Syntax:
        ```
        - AFG:ARBitrary:EMEM:POINTS:ENCdg {ASCii|BINary}
        - AFG:ARBitrary:EMEM:POINTS:ENCdg?
        ```

    Info:
        - ``ASCii`` - ASCII NR3 format.
        - ``BINary`` - IEEE488.2 binary block in 4-byte floating point format.
    """


class AfgArbitraryEmemPointsByteorder(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:ARBitrary:EMEM:POINTS:BYTEORDer`` command.

    Description:
        - ``:BYTEORDer This`` command specifies the byte order for the
          ``AFG:ARBITRARY:EMEM:POINTS?`` query when the ``AFG:ARBITRARY:EMEM:POINTS:ENCDG`` is set
          to BINary and when binary block data is sent for the ``AFG:ARBITRARY:EMEM:POINTS``
          command. LSB - Least significant byte first (little endian) MSB - Most significant byte
          first (big endian) The default is LSB. This setting is non-volatile and is reset by
          default setup or TekSecure. Refer to the ``AFG:ARBITRARY:EMEM:POINTS`` command description
          for more information.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:POINTS:BYTEORDer?``
          query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM:POINTS:BYTEORDer?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``AFG:ARBitrary:EMEM:POINTS:BYTEORDer value`` command.

    SCPI Syntax:
        ```
        - AFG:ARBitrary:EMEM:POINTS:BYTEORDer <LSB> |<MSB>
        - AFG:ARBitrary:EMEM:POINTS:BYTEORDer?
        ```

    Info:
        - ``LSB`` - Least significant byte first (little endian).
        - ``MSB`` - Most significant byte first (big endian).
    """


class AfgArbitraryEmemPoints(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:ARBitrary:EMEM:POINTS`` command.

    Description:
        - Specifies which points to load into the AFG arbitrary waveform edit memory. The point data
          to be loaded may be specified as an IEEE488.2 binary block with 4-byte floating point data
          values, or as a comma-separated list of NR2 or NR3 data values. The data values must be in
          the range of -1.0 to 1.0. The ``AFG:ARBITRARY:EMEM:POINTS:BYTEORDER`` command is used when
          the data is binary block format. The minimum number of points is 2 and maximum is 131072.
          Upon successful transfer of the data points, the ``AFG:ARBITRARY:EMEM:NUMPOINTS`` query
          will return the number of points loaded into arbitrary waveform edit memory and the
          ``AFG:ARBITRARY:EMEM:FUNCTION`` query will return USER. Note that the output, if turned
          on, will not change unless or until the AFG function is set to ARBitrary using the
          ``AFG:FUNCTION`` command. Point values may be coerced to the nearest valid step size. The
          query form returns the points stored in the AFG arbitrary waveform edit memory in the
          format specified by the ``AFG:ARBITRARY:EMEM:POINTS:ENCDG`` command and, for binary
          encoding, the byte order specified by the ``AFG:ARBITRARY:EMEM:POINTS:BYTEORDER`` command.
          Refer to the ``AFG:ARBITRARY:EMEM:POINTS:ENCDG`` command description for more information.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:POINTS?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM:POINTS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:ARBitrary:EMEM:POINTS value``
          command.

    SCPI Syntax:
        ```
        - AFG:ARBitrary:EMEM:POINTS <BlockWfmInDTO> |<NrfWfmInDTO>
        - AFG:ARBitrary:EMEM:POINTS?
        ```

    Info:
        - ``BlockWfmInDTO`` - an IEEE488.2 binary block with 4-byte floating point data values.
        - ``NrfWfmInDTO`` - a comma-separated list of NR2 or NR3 data values.

    Properties:
        - ``.byteorder``: The ``AFG:ARBitrary:EMEM:POINTS:BYTEORDer`` command.
        - ``.encdg``: The ``AFG:ARBitrary:EMEM:POINTS:ENCdg`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._byteorder = AfgArbitraryEmemPointsByteorder(device, f"{self._cmd_syntax}:BYTEORDer")
        self._encdg = AfgArbitraryEmemPointsEncdg(device, f"{self._cmd_syntax}:ENCdg")

    @property
    def byteorder(self) -> AfgArbitraryEmemPointsByteorder:
        """Return the ``AFG:ARBitrary:EMEM:POINTS:BYTEORDer`` command.

        Description:
            - ``:BYTEORDer This`` command specifies the byte order for the
              ``AFG:ARBITRARY:EMEM:POINTS?`` query when the ``AFG:ARBITRARY:EMEM:POINTS:ENCDG`` is
              set to BINary and when binary block data is sent for the ``AFG:ARBITRARY:EMEM:POINTS``
              command. LSB - Least significant byte first (little endian) MSB - Most significant
              byte first (big endian) The default is LSB. This setting is non-volatile and is reset
              by default setup or TekSecure. Refer to the ``AFG:ARBITRARY:EMEM:POINTS`` command
              description for more information.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:POINTS:BYTEORDer?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``AFG:ARBitrary:EMEM:POINTS:BYTEORDer?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AFG:ARBitrary:EMEM:POINTS:BYTEORDer value`` command.

        SCPI Syntax:
            ```
            - AFG:ARBitrary:EMEM:POINTS:BYTEORDer <LSB> |<MSB>
            - AFG:ARBitrary:EMEM:POINTS:BYTEORDer?
            ```

        Info:
            - ``LSB`` - Least significant byte first (little endian).
            - ``MSB`` - Most significant byte first (big endian).
        """
        return self._byteorder

    @property
    def encdg(self) -> AfgArbitraryEmemPointsEncdg:
        """Return the ``AFG:ARBitrary:EMEM:POINTS:ENCdg`` command.

        Description:
            - This command specifies the data encoding format for the ``AFG:ARBITRARY:EMEM:POINTS``
              query (either ASCII or binary). The default is ASCii. This setting is non-volatile and
              is reset by default setup or TekSecure. Refer to the ``AFG:ARBITRARY:EMEM:POINTS``
              command description for more information.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:POINTS:ENCdg?``
              query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM:POINTS:ENCdg?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``AFG:ARBitrary:EMEM:POINTS:ENCdg value`` command.

        SCPI Syntax:
            ```
            - AFG:ARBitrary:EMEM:POINTS:ENCdg {ASCii|BINary}
            - AFG:ARBitrary:EMEM:POINTS:ENCdg?
            ```

        Info:
            - ``ASCii`` - ASCII NR3 format.
            - ``BINary`` - IEEE488.2 binary block in 4-byte floating point format.
        """
        return self._encdg


class AfgArbitraryEmemNumpoints(SCPICmdRead):
    """The ``AFG:ARBitrary:EMEM:NUMPoints`` command.

    Description:
        - Returns the number of points in the AFB arbitrary waveform edit memory. This value will be
          used with the ``AFG:ARBITRARY:EMEM:GENERATE`` command in the event that the number of
          points is not specified. See the ``AFG:ARBITRARY:EMEM:GENERATE`` command description for
          more information.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:NUMPoints?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM:NUMPoints?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AFG:ARBitrary:EMEM:NUMPoints?
        ```
    """


class AfgArbitraryEmemGenerate(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:ARBitrary:EMEM:GENerate`` command.

    Description:
        - This command generates the arbitrary waveform function specified by the enumeration
          argument. The NR1 argument is optional; it can be used to specify the number of points; if
          it is used, it also sets the value that will be used by ``AFG:ARBITRARY:EMEM:NUMPOINTS``
          until the instrument is reset via TEKSECURE. In the absence of the NR1 argument, the
          number of points used with the function is that number returned by the
          ``AFG:ARBITRARY:EMEM:NUMPOINTS`` query. To query the arbitrary waveform function set by
          this command, use ``AFG:ARBITRARY:EMEM:FUNCTION`` (This value is not reset by default
          setup or by power cycle).

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:GENerate?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM:GENerate?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:ARBitrary:EMEM:GENerate value``
          command.

    SCPI Syntax:
        ```
        - AFG:ARBitrary:EMEM:GENerate {SINE|SQUare|PULSe|RAMP|NOISe[,NR1]}
        - AFG:ARBitrary:EMEM:GENerate?
        ```

    Info:
        - ``<NR1>`` (Optional) Specifies the number of points for the arbitrary waveform function.
          The number of points, if specified, must be >= 2 and <= 131072. The default number of
          points is 100.
        - ``SINE`` generates the Sine AFG function.
        - ``SQUare`` generates the Square AFG function.
        - ``PULSe`` generates the Pulse AFG function.
        - ``RAMP`` generates the Ramp AFG function.
        - ``NOISe`` generates the Noise AFG function.
    """


class AfgArbitraryEmemFunction(SCPICmdRead):
    """The ``AFG:ARBitrary:EMEM:FUNCtion`` command.

    Description:
        - Returns the currently selected arbitrary waveform pre-defined function. The pre-defined
          ARB function is selected using the command ``AFG:ARBITRARY:EMEM:GENERATE``. This query may
          also return USER, which indicates that the arbitrary waveform in edit memory has been
          altered from one of the predefined functions.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM:FUNCtion?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AFG:ARBitrary:EMEM:FUNCtion?
        ```
    """


class AfgArbitraryEmem(SCPICmdRead):
    """The ``AFG:ARBitrary:EMEM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.function``: The ``AFG:ARBitrary:EMEM:FUNCtion`` command.
        - ``.generate``: The ``AFG:ARBitrary:EMEM:GENerate`` command.
        - ``.numpoints``: The ``AFG:ARBitrary:EMEM:NUMPoints`` command.
        - ``.points``: The ``AFG:ARBitrary:EMEM:POINTS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._function = AfgArbitraryEmemFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._generate = AfgArbitraryEmemGenerate(device, f"{self._cmd_syntax}:GENerate")
        self._numpoints = AfgArbitraryEmemNumpoints(device, f"{self._cmd_syntax}:NUMPoints")
        self._points = AfgArbitraryEmemPoints(device, f"{self._cmd_syntax}:POINTS")

    @property
    def function(self) -> AfgArbitraryEmemFunction:
        """Return the ``AFG:ARBitrary:EMEM:FUNCtion`` command.

        Description:
            - Returns the currently selected arbitrary waveform pre-defined function. The
              pre-defined ARB function is selected using the command
              ``AFG:ARBITRARY:EMEM:GENERATE``. This query may also return USER, which indicates that
              the arbitrary waveform in edit memory has been altered from one of the predefined
              functions.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM:FUNCtion?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AFG:ARBitrary:EMEM:FUNCtion?
            ```
        """
        return self._function

    @property
    def generate(self) -> AfgArbitraryEmemGenerate:
        """Return the ``AFG:ARBitrary:EMEM:GENerate`` command.

        Description:
            - This command generates the arbitrary waveform function specified by the enumeration
              argument. The NR1 argument is optional; it can be used to specify the number of
              points; if it is used, it also sets the value that will be used by
              ``AFG:ARBITRARY:EMEM:NUMPOINTS`` until the instrument is reset via TEKSECURE. In the
              absence of the NR1 argument, the number of points used with the function is that
              number returned by the ``AFG:ARBITRARY:EMEM:NUMPOINTS`` query. To query the arbitrary
              waveform function set by this command, use ``AFG:ARBITRARY:EMEM:FUNCTION`` (This value
              is not reset by default setup or by power cycle).

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:GENerate?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM:GENerate?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:ARBitrary:EMEM:GENerate value``
              command.

        SCPI Syntax:
            ```
            - AFG:ARBitrary:EMEM:GENerate {SINE|SQUare|PULSe|RAMP|NOISe[,NR1]}
            - AFG:ARBitrary:EMEM:GENerate?
            ```

        Info:
            - ``<NR1>`` (Optional) Specifies the number of points for the arbitrary waveform
              function. The number of points, if specified, must be >= 2 and <= 131072. The default
              number of points is 100.
            - ``SINE`` generates the Sine AFG function.
            - ``SQUare`` generates the Square AFG function.
            - ``PULSe`` generates the Pulse AFG function.
            - ``RAMP`` generates the Ramp AFG function.
            - ``NOISe`` generates the Noise AFG function.
        """
        return self._generate

    @property
    def numpoints(self) -> AfgArbitraryEmemNumpoints:
        """Return the ``AFG:ARBitrary:EMEM:NUMPoints`` command.

        Description:
            - Returns the number of points in the AFB arbitrary waveform edit memory. This value
              will be used with the ``AFG:ARBITRARY:EMEM:GENERATE`` command in the event that the
              number of points is not specified. See the ``AFG:ARBITRARY:EMEM:GENERATE`` command
              description for more information.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:NUMPoints?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM:NUMPoints?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AFG:ARBitrary:EMEM:NUMPoints?
            ```
        """
        return self._numpoints

    @property
    def points(self) -> AfgArbitraryEmemPoints:
        """Return the ``AFG:ARBitrary:EMEM:POINTS`` command.

        Description:
            - Specifies which points to load into the AFG arbitrary waveform edit memory. The point
              data to be loaded may be specified as an IEEE488.2 binary block with 4-byte floating
              point data values, or as a comma-separated list of NR2 or NR3 data values. The data
              values must be in the range of -1.0 to 1.0. The
              ``AFG:ARBITRARY:EMEM:POINTS:BYTEORDER`` command is used when the data is binary block
              format. The minimum number of points is 2 and maximum is 131072. Upon successful
              transfer of the data points, the ``AFG:ARBITRARY:EMEM:NUMPOINTS`` query will return
              the number of points loaded into arbitrary waveform edit memory and the
              ``AFG:ARBITRARY:EMEM:FUNCTION`` query will return USER. Note that the output, if
              turned on, will not change unless or until the AFG function is set to ARBitrary using
              the ``AFG:FUNCTION`` command. Point values may be coerced to the nearest valid step
              size. The query form returns the points stored in the AFG arbitrary waveform edit
              memory in the format specified by the ``AFG:ARBITRARY:EMEM:POINTS:ENCDG`` command and,
              for binary encoding, the byte order specified by the
              ``AFG:ARBITRARY:EMEM:POINTS:BYTEORDER`` command. Refer to the
              ``AFG:ARBITRARY:EMEM:POINTS:ENCDG`` command description for more information.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM:POINTS?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM:POINTS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:ARBitrary:EMEM:POINTS value``
              command.

        SCPI Syntax:
            ```
            - AFG:ARBitrary:EMEM:POINTS <BlockWfmInDTO> |<NrfWfmInDTO>
            - AFG:ARBitrary:EMEM:POINTS?
            ```

        Info:
            - ``BlockWfmInDTO`` - an IEEE488.2 binary block with 4-byte floating point data values.
            - ``NrfWfmInDTO`` - a comma-separated list of NR2 or NR3 data values.

        Sub-properties:
            - ``.byteorder``: The ``AFG:ARBitrary:EMEM:POINTS:BYTEORDer`` command.
            - ``.encdg``: The ``AFG:ARBitrary:EMEM:POINTS:ENCdg`` command.
        """
        return self._points


class AfgArbitraryArbItemTime(SCPICmdRead):
    """The ``AFG:ARBitrary:ARB<x>:TIMe`` command.

    Description:
        - Returns the time that the data in the specified arbitrary waveform slot was saved.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:ARB<x>:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:ARB<x>:TIMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AFG:ARBitrary:ARB<x>:TIMe?
        ```
    """


class AfgArbitraryArbItemLabel(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:ARBitrary:ARB<x>:LABel`` command.

    Description:
        - Sets (or queries) the waveform label for arbitrary waveform slots 1- 4.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:ARB<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:ARB<x>:LABel?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:ARBitrary:ARB<x>:LABel value``
          command.

    SCPI Syntax:
        ```
        - AFG:ARBitrary:ARB<x>:LABel <QString>
        - AFG:ARBitrary:ARB<x>:LABel?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class AfgArbitraryArbItemDate(SCPICmdRead):
    """The ``AFG:ARBitrary:ARB<x>:DATE`` command.

    Description:
        - Returns the date that the data in the specified arbitrary waveform slot 1-4 was saved.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:ARB<x>:DATE?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:ARB<x>:DATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - AFG:ARBitrary:ARB<x>:DATE?
        ```
    """


class AfgArbitraryArbItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``AFG:ARBitrary:ARB<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:ARB<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:ARB<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.date``: The ``AFG:ARBitrary:ARB<x>:DATE`` command.
        - ``.label``: The ``AFG:ARBitrary:ARB<x>:LABel`` command.
        - ``.time``: The ``AFG:ARBitrary:ARB<x>:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._date = AfgArbitraryArbItemDate(device, f"{self._cmd_syntax}:DATE")
        self._label = AfgArbitraryArbItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._time = AfgArbitraryArbItemTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def date(self) -> AfgArbitraryArbItemDate:
        """Return the ``AFG:ARBitrary:ARB<x>:DATE`` command.

        Description:
            - Returns the date that the data in the specified arbitrary waveform slot 1-4 was saved.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:ARB<x>:DATE?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:ARB<x>:DATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AFG:ARBitrary:ARB<x>:DATE?
            ```
        """
        return self._date

    @property
    def label(self) -> AfgArbitraryArbItemLabel:
        """Return the ``AFG:ARBitrary:ARB<x>:LABel`` command.

        Description:
            - Sets (or queries) the waveform label for arbitrary waveform slots 1- 4.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:ARB<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:ARB<x>:LABel?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:ARBitrary:ARB<x>:LABel value``
              command.

        SCPI Syntax:
            ```
            - AFG:ARBitrary:ARB<x>:LABel <QString>
            - AFG:ARBitrary:ARB<x>:LABel?
            ```
        """
        return self._label

    @property
    def time(self) -> AfgArbitraryArbItemTime:
        """Return the ``AFG:ARBitrary:ARB<x>:TIMe`` command.

        Description:
            - Returns the time that the data in the specified arbitrary waveform slot was saved.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:ARB<x>:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:ARB<x>:TIMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - AFG:ARBitrary:ARB<x>:TIMe?
            ```
        """
        return self._time


class AfgArbitrary(SCPICmdRead):
    """The ``AFG:ARBitrary`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.arb``: The ``AFG:ARBitrary:ARB<x>`` command tree.
        - ``.emem``: The ``AFG:ARBitrary:EMEM`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._arb: Dict[int, AfgArbitraryArbItem] = DefaultDictPassKeyToFactory(
            lambda x: AfgArbitraryArbItem(device, f"{self._cmd_syntax}:ARB{x}")
        )
        self._emem = AfgArbitraryEmem(device, f"{self._cmd_syntax}:EMEM")

    @property
    def arb(self) -> Dict[int, AfgArbitraryArbItem]:
        """Return the ``AFG:ARBitrary:ARB<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:ARB<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:ARB<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.date``: The ``AFG:ARBitrary:ARB<x>:DATE`` command.
            - ``.label``: The ``AFG:ARBitrary:ARB<x>:LABel`` command.
            - ``.time``: The ``AFG:ARBitrary:ARB<x>:TIMe`` command.
        """
        return self._arb

    @property
    def emem(self) -> AfgArbitraryEmem:
        """Return the ``AFG:ARBitrary:EMEM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:EMEM?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:EMEM?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.function``: The ``AFG:ARBitrary:EMEM:FUNCtion`` command.
            - ``.generate``: The ``AFG:ARBitrary:EMEM:GENerate`` command.
            - ``.numpoints``: The ``AFG:ARBitrary:EMEM:NUMPoints`` command.
            - ``.points``: The ``AFG:ARBitrary:EMEM:POINTS`` command.
        """
        return self._emem


class AfgAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:AMPLitude`` command.

    Description:
        - Sets (or queries) the AFG amplitude in volts, peak to peak.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:AMPLitude?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - AFG:AMPLitude <NR3>
        - AFG:AMPLitude?
        ```

    Info:
        - ``<NR3>`` is a floating point number that represents the AFG amplitude, peak to peak, in
          volts.
    """


#  pylint: disable=too-many-instance-attributes
class Afg(SCPICmdRead):
    """The ``AFG`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``AFG:AMPLitude`` command.
        - ``.arbitrary``: The ``AFG:ARBitrary`` command tree.
        - ``.frequency``: The ``AFG:FREQuency`` command.
        - ``.function``: The ``AFG:FUNCtion`` command.
        - ``.highlevel``: The ``AFG:HIGHLevel`` command.
        - ``.levelpreset``: The ``AFG:LEVELPreset`` command.
        - ``.lowlevel``: The ``AFG:LOWLevel`` command.
        - ``.noiseadd``: The ``AFG:NOISEAdd`` command tree.
        - ``.offset``: The ``AFG:OFFSet`` command.
        - ``.output``: The ``AFG:OUTPut`` command tree.
        - ``.period``: The ``AFG:PERIod`` command.
        - ``.phase``: The ``AFG:PHASe`` command.
        - ``.pulse``: The ``AFG:PULse`` command tree.
        - ``.ramp``: The ``AFG:RAMP`` command tree.
        - ``.square``: The ``AFG:SQUare`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "AFG") -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = AfgAmplitude(device, f"{self._cmd_syntax}:AMPLitude")
        self._arbitrary = AfgArbitrary(device, f"{self._cmd_syntax}:ARBitrary")
        self._frequency = AfgFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._function = AfgFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._highlevel = AfgHighlevel(device, f"{self._cmd_syntax}:HIGHLevel")
        self._levelpreset = AfgLevelpreset(device, f"{self._cmd_syntax}:LEVELPreset")
        self._lowlevel = AfgLowlevel(device, f"{self._cmd_syntax}:LOWLevel")
        self._noiseadd = AfgNoiseadd(device, f"{self._cmd_syntax}:NOISEAdd")
        self._offset = AfgOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._output = AfgOutput(device, f"{self._cmd_syntax}:OUTPut")
        self._period = AfgPeriod(device, f"{self._cmd_syntax}:PERIod")
        self._phase = AfgPhase(device, f"{self._cmd_syntax}:PHASe")
        self._pulse = AfgPulse(device, f"{self._cmd_syntax}:PULse")
        self._ramp = AfgRamp(device, f"{self._cmd_syntax}:RAMP")
        self._square = AfgSquare(device, f"{self._cmd_syntax}:SQUare")

    @property
    def amplitude(self) -> AfgAmplitude:
        """Return the ``AFG:AMPLitude`` command.

        Description:
            - Sets (or queries) the AFG amplitude in volts, peak to peak.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:AMPLitude?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - AFG:AMPLitude <NR3>
            - AFG:AMPLitude?
            ```

        Info:
            - ``<NR3>`` is a floating point number that represents the AFG amplitude, peak to peak,
              in volts.
        """
        return self._amplitude

    @property
    def arbitrary(self) -> AfgArbitrary:
        """Return the ``AFG:ARBitrary`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.arb``: The ``AFG:ARBitrary:ARB<x>`` command tree.
            - ``.emem``: The ``AFG:ARBitrary:EMEM`` command tree.
        """
        return self._arbitrary

    @property
    def frequency(self) -> AfgFrequency:
        """Return the ``AFG:FREQuency`` command.

        Description:
            - Sets (or queries) the AFG frequency, in Hz.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:FREQuency?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:FREQuency value`` command.

        SCPI Syntax:
            ```
            - AFG:FREQuency <NR3>
            - AFG:FREQuency?
            ```

        Info:
            - ``<NR3>`` is the floating point number that represents the AFG frequency, in Hz.
        """
        return self._frequency

    @property
    def function(self) -> AfgFunction:
        """Return the ``AFG:FUNCtion`` command.

        Description:
            - Sets (or queries) which AFG function to execute.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:FUNCtion?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - AFG:FUNCtion {SINE|SQUare|PULSe|RAMP|NOISe|DC|SINC|GAUSsian|LORENtz|ERISe|EDECAy|HAVERSINe|CARDIac|ARBitrary}
            - AFG:FUNCtion?
            ```

        Info:
            - ``SINE``
            - ``SQUare``
            - ``PULSe``
            - ``RAMP``
            - ``NOISe``
            - ``DC`` . The DC level is controlled by ``AFG:OFFSET``.
            - ``SINC`` (Sin(x)/x).
            - ``GAUSsian``
            - ``LORENtz``
            - ``ERISe``
            - ``EDECAy``
            - ``HAVERSINe``
            - ``CARDIac``
            - ``ARBitrary``
        """  # noqa: E501
        return self._function

    @property
    def highlevel(self) -> AfgHighlevel:
        """Return the ``AFG:HIGHLevel`` command.

        Description:
            - This command sets (or queries) the high level value of the output waveform, in volts,
              when using the arbitrary function generator feature.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:HIGHLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:HIGHLevel?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:HIGHLevel value`` command.

        SCPI Syntax:
            ```
            - AFG:HIGHLevel <NR3>
            - AFG:HIGHLevel?
            ```

        Info:
            - ``<NR3>`` is a floating point number that represents the AFG high level value, in
              volts.
        """
        return self._highlevel

    @property
    def levelpreset(self) -> AfgLevelpreset:
        """Return the ``AFG:LEVELPreset`` command.

        Description:
            - Sets (or queries) the AFG preset levels to values that correspond to the logic
              standard specified by the argument. The presets set the following vertical controls:
              AMPLitude OFFSet HIGHLevel LOWLevel Note that once any of these vertical settings are
              changed from the preset values, or the output load impedance is changed, the query
              form returns USER. The ``AFG:LEVELPreset`` command sets the high level and low level
              values as follows: ``AFG:HIGHLevel`` and ``AFG:LOWLevel Setting`` Values Load
              Impedance FIFTY Ohm Load Impedance HIGHZ LEVEL Preset High Low High Low TTL N/A 5.0V
              ``CMOS_5_0V N``/A 5.0V ``CMOS_3_3V 2``.5V 0V 3.3V 0V ``CMOS_2_5V 2``.5V 0V 2.5V 0V ECL
              -0.85V -1.65V -0.9V -1.7V

        Usage:
            - Using the ``.query()`` method will send the ``AFG:LEVELPreset?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:LEVELPreset?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:LEVELPreset value`` command.

        SCPI Syntax:
            ```
            - AFG:LEVELPreset {CMOS_5_0V|CMOS_3_3V|CMOS_2_5V|ECL|TTL|USER}
            - AFG:LEVELPreset?
            ```

        Info:
            - ``CMOS_5_0V`` - standard 5-volt CMOS levels. Not available when the load impedance is
              50 Ohm.
            - ``CMOS_3_3V`` - standard 3.3-volt CMOS levels.
            - ``CMOS_2_5V`` - standard 2.5-volt CMOS levels.
            - ``USER`` - user-defined.
            - ``ECL`` - -1.7 to -0.9 volts (note the full range is not available in 50 Ohm - actual
              is -1.65 to -0.85. See table below.
            - ``TTL`` - 5.0 volts. Not available when the load impedance is 50 Ohm.
        """
        return self._levelpreset

    @property
    def lowlevel(self) -> AfgLowlevel:
        """Return the ``AFG:LOWLevel`` command.

        Description:
            - This command sets (or queries) the low level value of the output waveform, in volts,
              when using the arbitrary function generator feature.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:LOWLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:LOWLevel?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:LOWLevel value`` command.

        SCPI Syntax:
            ```
            - AFG:LOWLevel <NR3>
            - AFG:LOWLevel?
            ```

        Info:
            - ``<NR3>`` is the floating point number that represents the AFG low level value, in
              volts.
        """
        return self._lowlevel

    @property
    def noiseadd(self) -> AfgNoiseadd:
        """Return the ``AFG:NOISEAdd`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:NOISEAdd?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:NOISEAdd?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.percent``: The ``AFG:NOISEAdd:PERCent`` command.
            - ``.state``: The ``AFG:NOISEAdd:STATE`` command.
        """
        return self._noiseadd

    @property
    def offset(self) -> AfgOffset:
        """Return the ``AFG:OFFSet`` command.

        Description:
            - Sets (or queries) the AFG offset value, in volts.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:OFFSet value`` command.

        SCPI Syntax:
            ```
            - AFG:OFFSet <NR3>
            - AFG:OFFSet?
            ```

        Info:
            - ``<NR3>`` is a floating point number that represents the AFG offset, in volts.
        """
        return self._offset

    @property
    def output(self) -> AfgOutput:
        """Return the ``AFG:OUTPut`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:OUTPut?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:OUTPut?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.load``: The ``AFG:OUTPut:LOAd`` command tree.
            - ``.state``: The ``AFG:OUTPut:STATE`` command.
        """
        return self._output

    @property
    def period(self) -> AfgPeriod:
        """Return the ``AFG:PERIod`` command.

        Description:
            - Sets (or queries) the period of the AFG waveform, in seconds.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:PERIod?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:PERIod?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:PERIod value`` command.

        SCPI Syntax:
            ```
            - AFG:PERIod <NR3>
            - AFG:PERIod?
            ```

        Info:
            - ``NR3`` is the floating point number that represents the AFG period value, in seconds.
        """
        return self._period

    @property
    def phase(self) -> AfgPhase:
        """Return the ``AFG:PHASe`` command.

        Description:
            - Sets (or queries) the AFG phase. The AFG phase setting controls the phase difference
              between the trigger signal output and the AFG waveform output. Phase is expressed in
              degrees and ranges from -180.0 to 180.0 in increments of 0.1 degrees.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:PHASe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:PHASe value`` command.

        SCPI Syntax:
            ```
            - AFG:PHASe <NR3>
            - AFG:PHASe?
            ```
        """
        return self._phase

    @property
    def pulse(self) -> AfgPulse:
        """Return the ``AFG:PULse`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:PULse?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:PULse?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.width``: The ``AFG:PULse:WIDth`` command.
        """
        return self._pulse

    @property
    def ramp(self) -> AfgRamp:
        """Return the ``AFG:RAMP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:RAMP?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:RAMP?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.symmetry``: The ``AFG:RAMP:SYMmetry`` command.
        """
        return self._ramp

    @property
    def square(self) -> AfgSquare:
        """Return the ``AFG:SQUare`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:SQUare?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:SQUare?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.duty``: The ``AFG:SQUare:DUty`` command.
        """
        return self._square
