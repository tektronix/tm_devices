# pylint: disable=line-too-long
"""The afg commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AFG:AMPLitude <NR3>
    - AFG:AMPLitude?
    - AFG:ARBitrary:SOUrce <QString>
    - AFG:ARBitrary:SOUrce?
    - AFG:BURSt:CCOUnt <NR1>
    - AFG:BURSt:CCOUnt?
    - AFG:BURSt:TRIGger
    - AFG:FREQuency <NR3>
    - AFG:FREQuency?
    - AFG:FUNCtion {SINE|SQUare|PULSe|RAMP|NOISe|DC|SINC|GAUSsian|LORENtz|ERISe|EDECAy|HAVERSINe|CARDIac|ARBitrary}
    - AFG:FUNCtion?
    - AFG:HIGHLevel <NR3>
    - AFG:HIGHLevel?
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
    - AFG:OUTPut:MODe {OFF|CONTinuous|BURSt}
    - AFG:OUTPut:MODe?
    - AFG:OUTPut:STATE {0|1|OFF|ON}
    - AFG:OUTPut:STATE?
    - AFG:PERIod <NR3>
    - AFG:PERIod?
    - AFG:PULse:WIDth <NR3>
    - AFG:PULse:WIDth?
    - AFG:RAMP:SYMmetry <NR3>
    - AFG:RAMP:SYMmetry?
    - AFG:SQUare:DUty <NR3>
    - AFG:SQUare:DUty?
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

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


class AfgOutputMode(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:OUTPut:MODe`` command.

    Description:
        - This command sets or returns the AFG output mode.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:OUTPut:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:OUTPut:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:OUTPut:MODe value`` command.

    SCPI Syntax:
        ```
        - AFG:OUTPut:MODe {OFF|CONTinuous|BURSt}
        - AFG:OUTPut:MODe?
        ```

    Info:
        - ``OFF`` turns off the AFG output mode.
        - ``CONTinuous`` turns the AFG output mode to continuous.
        - ``BURSt`` turns the AFG output mode to burst.
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
        - ``.mode``: The ``AFG:OUTPut:MODe`` command.
        - ``.state``: The ``AFG:OUTPut:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._load = AfgOutputLoad(device, f"{self._cmd_syntax}:LOAd")
        self._mode = AfgOutputMode(device, f"{self._cmd_syntax}:MODe")
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
    def mode(self) -> AfgOutputMode:
        """Return the ``AFG:OUTPut:MODe`` command.

        Description:
            - This command sets or returns the AFG output mode.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:OUTPut:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:OUTPut:MODe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:OUTPut:MODe value`` command.

        SCPI Syntax:
            ```
            - AFG:OUTPut:MODe {OFF|CONTinuous|BURSt}
            - AFG:OUTPut:MODe?
            ```

        Info:
            - ``OFF`` turns off the AFG output mode.
            - ``CONTinuous`` turns the AFG output mode to continuous.
            - ``BURSt`` turns the AFG output mode to burst.
        """
        return self._mode

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


class AfgBurstTrigger(SCPICmdWriteNoArguments):
    """The ``AFG:BURSt:TRIGger`` command.

    Description:
        - This command triggers a burst on AFG output.

    Usage:
        - Using the ``.write()`` method will send the ``AFG:BURSt:TRIGger`` command.

    SCPI Syntax:
        ```
        - AFG:BURSt:TRIGger
        ```
    """


class AfgBurstCcount(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:BURSt:CCOUnt`` command.

    Description:
        - This command sets or returns the cycle count for AFG burst mode.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:BURSt:CCOUnt?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:BURSt:CCOUnt?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:BURSt:CCOUnt value`` command.

    SCPI Syntax:
        ```
        - AFG:BURSt:CCOUnt <NR1>
        - AFG:BURSt:CCOUnt?
        ```

    Info:
        - ``<NR1>`` is the cycle count.
    """


class AfgBurst(SCPICmdRead):
    """The ``AFG:BURSt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:BURSt?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:BURSt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ccount``: The ``AFG:BURSt:CCOUnt`` command.
        - ``.trigger``: The ``AFG:BURSt:TRIGger`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ccount = AfgBurstCcount(device, f"{self._cmd_syntax}:CCOUnt")
        self._trigger = AfgBurstTrigger(device, f"{self._cmd_syntax}:TRIGger")

    @property
    def ccount(self) -> AfgBurstCcount:
        """Return the ``AFG:BURSt:CCOUnt`` command.

        Description:
            - This command sets or returns the cycle count for AFG burst mode.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:BURSt:CCOUnt?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:BURSt:CCOUnt?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:BURSt:CCOUnt value`` command.

        SCPI Syntax:
            ```
            - AFG:BURSt:CCOUnt <NR1>
            - AFG:BURSt:CCOUnt?
            ```

        Info:
            - ``<NR1>`` is the cycle count.
        """
        return self._ccount

    @property
    def trigger(self) -> AfgBurstTrigger:
        """Return the ``AFG:BURSt:TRIGger`` command.

        Description:
            - This command triggers a burst on AFG output.

        Usage:
            - Using the ``.write()`` method will send the ``AFG:BURSt:TRIGger`` command.

        SCPI Syntax:
            ```
            - AFG:BURSt:TRIGger
            ```
        """
        return self._trigger


class AfgArbitrarySource(SCPICmdWrite, SCPICmdRead):
    """The ``AFG:ARBitrary:SOUrce`` command.

    Description:
        - This command sets or queries the source name for the Arbitrary Waveform. Currently
          supported sources are either waveform file (.wfm) or text file (.csv).

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:SOUrce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AFG:ARBitrary:SOUrce value`` command.

    SCPI Syntax:
        ```
        - AFG:ARBitrary:SOUrce <QString>
        - AFG:ARBitrary:SOUrce?
        ```

    Info:
        - ``<QString>`` is the source name.
    """

    _WRAP_ARG_WITH_QUOTES = True


class AfgArbitrary(SCPICmdRead):
    """The ``AFG:ARBitrary`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFG:ARBitrary?`` query.
        - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``AFG:ARBitrary:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = AfgArbitrarySource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> AfgArbitrarySource:
        """Return the ``AFG:ARBitrary:SOUrce`` command.

        Description:
            - This command sets or queries the source name for the Arbitrary Waveform. Currently
              supported sources are either waveform file (.wfm) or text file (.csv).

        Usage:
            - Using the ``.query()`` method will send the ``AFG:ARBitrary:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:ARBitrary:SOUrce?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AFG:ARBitrary:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - AFG:ARBitrary:SOUrce <QString>
            - AFG:ARBitrary:SOUrce?
            ```

        Info:
            - ``<QString>`` is the source name.
        """
        return self._source


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
        - ``.burst``: The ``AFG:BURSt`` command tree.
        - ``.frequency``: The ``AFG:FREQuency`` command.
        - ``.function``: The ``AFG:FUNCtion`` command.
        - ``.highlevel``: The ``AFG:HIGHLevel`` command.
        - ``.lowlevel``: The ``AFG:LOWLevel`` command.
        - ``.noiseadd``: The ``AFG:NOISEAdd`` command tree.
        - ``.offset``: The ``AFG:OFFSet`` command.
        - ``.output``: The ``AFG:OUTPut`` command tree.
        - ``.period``: The ``AFG:PERIod`` command.
        - ``.pulse``: The ``AFG:PULse`` command tree.
        - ``.ramp``: The ``AFG:RAMP`` command tree.
        - ``.square``: The ``AFG:SQUare`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "AFG") -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = AfgAmplitude(device, f"{self._cmd_syntax}:AMPLitude")
        self._arbitrary = AfgArbitrary(device, f"{self._cmd_syntax}:ARBitrary")
        self._burst = AfgBurst(device, f"{self._cmd_syntax}:BURSt")
        self._frequency = AfgFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._function = AfgFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._highlevel = AfgHighlevel(device, f"{self._cmd_syntax}:HIGHLevel")
        self._lowlevel = AfgLowlevel(device, f"{self._cmd_syntax}:LOWLevel")
        self._noiseadd = AfgNoiseadd(device, f"{self._cmd_syntax}:NOISEAdd")
        self._offset = AfgOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._output = AfgOutput(device, f"{self._cmd_syntax}:OUTPut")
        self._period = AfgPeriod(device, f"{self._cmd_syntax}:PERIod")
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
            - ``.source``: The ``AFG:ARBitrary:SOUrce`` command.
        """
        return self._arbitrary

    @property
    def burst(self) -> AfgBurst:
        """Return the ``AFG:BURSt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``AFG:BURSt?`` query.
            - Using the ``.verify(value)`` method will send the ``AFG:BURSt?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ccount``: The ``AFG:BURSt:CCOUnt`` command.
            - ``.trigger``: The ``AFG:BURSt:TRIGger`` command.
        """
        return self._burst

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
            - ``.mode``: The ``AFG:OUTPut:MODe`` command.
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
