"""The bwaveform commands module.

These commands are used in the following models:
AWG5200

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - BWAVeform:AMPLitude <amplitude>
    - BWAVeform:AUTO {LEN|CYCLE|DUR|FREQ|SR}
    - BWAVeform:AUTO?
    - BWAVeform:COMPile
    - BWAVeform:COMPile:CASSign {0|1|OFF|ON}
    - BWAVeform:COMPile:CASSign?
    - BWAVeform:COMPile:CHANnel {<channel_number>}
    - BWAVeform:COMPile:NAME <waveform_name>
    - BWAVeform:COMPile:NAME?
    - BWAVeform:COMPile:PLAY {0|1|OFF|ON}
    - BWAVeform:COMPile:PLAY?
    - BWAVeform:CYCLe <cycle>
    - BWAVeform:FDRange {0|1|OFF|ON}
    - BWAVeform:FREQuency <frequency>
    - BWAVeform:FUNCtion {sine|square|triangle|ramp|noise|DC}
    - BWAVeform:FUNCtion?
    - BWAVeform:HIGH <high>
    - BWAVeform:LENGth <length>
    - BWAVeform:LOW <low>
    - BWAVeform:OFFSet <offset>
    - BWAVeform:RESet
    - BWAVeform:SRATe <sample_rate>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class BwaveformSrate(SCPICmdWrite):
    """The ``BWAVeform:SRATe`` command.

    Description:
        - This command sets or returns the Sample Rate for the waveform created by the Basic
          Waveform editor plug-in.

    Usage:
        - Using the ``.write(value)`` method will send the ``BWAVeform:SRATe value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:SRATe <sample_rate>
        ```
    """


class BwaveformReset(SCPICmdWriteNoArguments):
    """The ``BWAVeform:RESet`` command.

    Description:
        - This command resets the Basic Waveform editor plug-in to its default values.

    Usage:
        - Using the ``.write()`` method will send the ``BWAVeform:RESet`` command.

    SCPI Syntax:
        ```
        - BWAVeform:RESet
        ```
    """


class BwaveformOffset(SCPICmdWrite):
    """The ``BWAVeform:OFFSet`` command.

    Description:
        - This command sets or returns the Offset voltage value for the waveform created by the
          Basic Waveform editor plug-in. This setting can be affected if the system is set to use
          the full DAC range. Using the full DAC range is the default setting. Refer to the command
          ``BWAVEFORM:FDRANGE`` for more information.

    Usage:
        - Using the ``.write(value)`` method will send the ``BWAVeform:OFFSet value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:OFFSet <offset>
        ```
    """


class BwaveformLow(SCPICmdWrite):
    """The ``BWAVeform:LOW`` command.

    Description:
        - This command sets or returns the Low voltage value for the waveform created by the Basic
          Waveform editor plug-in.

    Usage:
        - Using the ``.write(value)`` method will send the ``BWAVeform:LOW value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:LOW <low>
        ```
    """


class BwaveformLength(SCPICmdWrite):
    """The ``BWAVeform:LENGth`` command.

    Description:
        - This command sets or returns the Length for the waveform created by the Basic Waveform
          editor plug-in.

    Usage:
        - Using the ``.write(value)`` method will send the ``BWAVeform:LENGth value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:LENGth <length>
        ```
    """


class BwaveformHigh(SCPICmdWrite):
    """The ``BWAVeform:HIGH`` command.

    Description:
        - This command sets or returns the High voltage value for the waveform created by the Basic
          Waveform editor plug-in.

    Usage:
        - Using the ``.write(value)`` method will send the ``BWAVeform:HIGH value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:HIGH <high>
        ```
    """


class BwaveformFunction(SCPICmdWrite, SCPICmdRead):
    """The ``BWAVeform:FUNCtion`` command.

    Description:
        - This command sets or returns the Basic Waveform editor plug-in waveform type.

    Usage:
        - Using the ``.query()`` method will send the ``BWAVeform:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``BWAVeform:FUNCtion?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BWAVeform:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:FUNCtion {sine|square|triangle|ramp|noise|DC}
        - BWAVeform:FUNCtion?
        ```

    Info:
        - ``*RST`` sets this to SINE.
    """


class BwaveformFrequency(SCPICmdWrite):
    """The ``BWAVeform:FREQuency`` command.

    Description:
        - This command sets or returns the Frequency for the waveform created by the Basic Waveform
          editor plug-in.

    Usage:
        - Using the ``.write(value)`` method will send the ``BWAVeform:FREQuency value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:FREQuency <frequency>
        ```
    """


class BwaveformFdrange(SCPICmdWrite):
    """The ``BWAVeform:FDRange`` command.

    Description:
        - This command sets or returns the state (enabled or disabled) of the Basic Waveform editor
          plug-in to use or not use the full DAC range during compile. Using the full DAC range when
          compiling waveforms results in waveforms with the best resolution. When enabled, if the
          selected offset and amplitude are within the range of the instrument's hardware, then the
          compiled waveform is compiled using the full DAC range and the compiled waveform's
          recommended amplitude and offset properties are set to the requested amplitude and offset
          values. If the selected offset and amplitude will result in a compiled waveform that does
          not take advantage of the full DAC range, the instrument adjusts the compiled waveform's
          recommended amplitude and offset values to use the full DAC range. If the system cannot
          achieve the full DAC range, a warning message is displayed. When disabled, the waveform is
          compiled using the specified amplitude and offset values and the compiled waveform's
          recommended amplitude is set to the maximum value and the recommended offset is set to 0.
          The control is not available for a DC waveform.

    Usage:
        - Using the ``.write(value)`` method will send the ``BWAVeform:FDRange value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:FDRange {0|1|OFF|ON}
        ```
    """


class BwaveformCycle(SCPICmdWrite):
    """The ``BWAVeform:CYCLe`` command.

    Description:
        - This command sets or returns the Cycle value (number of times the waveform repeats) for
          the waveform created by the Basic Waveform editor plug-in.

    Usage:
        - Using the ``.write(value)`` method will send the ``BWAVeform:CYCLe value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:CYCLe <cycle>
        ```
    """


class BwaveformCompilePlay(SCPICmdWrite, SCPICmdRead):
    """The ``BWAVeform:COMPile:PLAY`` command.

    Description:
        - This command sets or returns the state (enabled or disabled) of the Basic Waveform editor
          to either immediately play the waveform after compile or just compile.

    Usage:
        - Using the ``.query()`` method will send the ``BWAVeform:COMPile:PLAY?`` query.
        - Using the ``.verify(value)`` method will send the ``BWAVeform:COMPile:PLAY?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BWAVeform:COMPile:PLAY value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:COMPile:PLAY {0|1|OFF|ON}
        - BWAVeform:COMPile:PLAY?
        ```
    """


class BwaveformCompileName(SCPICmdWrite, SCPICmdRead):
    """The ``BWAVeform:COMPile:NAME`` command.

    Description:
        - This command sets or returns the name of the Basic Waveform editor plug-in compiled
          waveform. If the name already exists in the Waveform List, the name is appended with an
          underscore suffix such as '``Waveform_1``'.

    Usage:
        - Using the ``.query()`` method will send the ``BWAVeform:COMPile:NAME?`` query.
        - Using the ``.verify(value)`` method will send the ``BWAVeform:COMPile:NAME?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BWAVeform:COMPile:NAME value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:COMPile:NAME <waveform_name>
        - BWAVeform:COMPile:NAME?
        ```
    """


class BwaveformCompileChannel(SCPICmdWrite):
    """The ``BWAVeform:COMPile:CHANnel`` command.

    Description:
        - This command sets or returns the playout channel intended for the compiled waveform of the
          Basic Waveform editor plug-in. The selected channel is also used to set the amplitude and
          offset range.

    Usage:
        - Using the ``.write(value)`` method will send the ``BWAVeform:COMPile:CHANnel value``
          command.

    SCPI Syntax:
        ```
        - BWAVeform:COMPile:CHANnel {<channel_number>}
        ```
    """


class BwaveformCompileCassign(SCPICmdWrite, SCPICmdRead):
    """The ``BWAVeform:COMPile:CASSign`` command.

    Description:
        - This command sets or returns the state (enabled or disabled) of the Basic Waveform editor
          to compile the waveform and immediately assign it to a specified channel (enabled) or just
          compile the waveform (disabled).

    Usage:
        - Using the ``.query()`` method will send the ``BWAVeform:COMPile:CASSign?`` query.
        - Using the ``.verify(value)`` method will send the ``BWAVeform:COMPile:CASSign?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BWAVeform:COMPile:CASSign value``
          command.

    SCPI Syntax:
        ```
        - BWAVeform:COMPile:CASSign {0|1|OFF|ON}
        - BWAVeform:COMPile:CASSign?
        ```
    """


class BwaveformCompile(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``BWAVeform:COMPile`` command.

    Description:
        - This command initiates the Basic Waveform editor plug-in compile process. The created
          waveform is placed in the Waveform List.

    Usage:
        - Using the ``.write()`` method will send the ``BWAVeform:COMPile`` command.

    SCPI Syntax:
        ```
        - BWAVeform:COMPile
        ```

    Properties:
        - ``.cassign``: The ``BWAVeform:COMPile:CASSign`` command.
        - ``.channel``: The ``BWAVeform:COMPile:CHANnel`` command.
        - ``.name``: The ``BWAVeform:COMPile:NAME`` command.
        - ``.play``: The ``BWAVeform:COMPile:PLAY`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cassign = BwaveformCompileCassign(device, f"{self._cmd_syntax}:CASSign")
        self._channel = BwaveformCompileChannel(device, f"{self._cmd_syntax}:CHANnel")
        self._name = BwaveformCompileName(device, f"{self._cmd_syntax}:NAME")
        self._play = BwaveformCompilePlay(device, f"{self._cmd_syntax}:PLAY")

    @property
    def cassign(self) -> BwaveformCompileCassign:
        """Return the ``BWAVeform:COMPile:CASSign`` command.

        Description:
            - This command sets or returns the state (enabled or disabled) of the Basic Waveform
              editor to compile the waveform and immediately assign it to a specified channel
              (enabled) or just compile the waveform (disabled).

        Usage:
            - Using the ``.query()`` method will send the ``BWAVeform:COMPile:CASSign?`` query.
            - Using the ``.verify(value)`` method will send the ``BWAVeform:COMPile:CASSign?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BWAVeform:COMPile:CASSign value``
              command.

        SCPI Syntax:
            ```
            - BWAVeform:COMPile:CASSign {0|1|OFF|ON}
            - BWAVeform:COMPile:CASSign?
            ```
        """
        return self._cassign

    @property
    def channel(self) -> BwaveformCompileChannel:
        """Return the ``BWAVeform:COMPile:CHANnel`` command.

        Description:
            - This command sets or returns the playout channel intended for the compiled waveform of
              the Basic Waveform editor plug-in. The selected channel is also used to set the
              amplitude and offset range.

        Usage:
            - Using the ``.write(value)`` method will send the ``BWAVeform:COMPile:CHANnel value``
              command.

        SCPI Syntax:
            ```
            - BWAVeform:COMPile:CHANnel {<channel_number>}
            ```
        """
        return self._channel

    @property
    def name(self) -> BwaveformCompileName:
        """Return the ``BWAVeform:COMPile:NAME`` command.

        Description:
            - This command sets or returns the name of the Basic Waveform editor plug-in compiled
              waveform. If the name already exists in the Waveform List, the name is appended with
              an underscore suffix such as '``Waveform_1``'.

        Usage:
            - Using the ``.query()`` method will send the ``BWAVeform:COMPile:NAME?`` query.
            - Using the ``.verify(value)`` method will send the ``BWAVeform:COMPile:NAME?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BWAVeform:COMPile:NAME value``
              command.

        SCPI Syntax:
            ```
            - BWAVeform:COMPile:NAME <waveform_name>
            - BWAVeform:COMPile:NAME?
            ```
        """
        return self._name

    @property
    def play(self) -> BwaveformCompilePlay:
        """Return the ``BWAVeform:COMPile:PLAY`` command.

        Description:
            - This command sets or returns the state (enabled or disabled) of the Basic Waveform
              editor to either immediately play the waveform after compile or just compile.

        Usage:
            - Using the ``.query()`` method will send the ``BWAVeform:COMPile:PLAY?`` query.
            - Using the ``.verify(value)`` method will send the ``BWAVeform:COMPile:PLAY?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BWAVeform:COMPile:PLAY value``
              command.

        SCPI Syntax:
            ```
            - BWAVeform:COMPile:PLAY {0|1|OFF|ON}
            - BWAVeform:COMPile:PLAY?
            ```
        """
        return self._play


class BwaveformAuto(SCPICmdWrite, SCPICmdRead):
    """The ``BWAVeform:AUTO`` command.

    Description:
        - This command sets or returns the Basic Waveform editor plug-in Auto Calculate setting,
          determining which value is automatically calculated.

    Usage:
        - Using the ``.query()`` method will send the ``BWAVeform:AUTO?`` query.
        - Using the ``.verify(value)`` method will send the ``BWAVeform:AUTO?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``BWAVeform:AUTO value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:AUTO {LEN|CYCLE|DUR|FREQ|SR}
        - BWAVeform:AUTO?
        ```

    Info:
        - ``*RST`` sets this to Cycle.
    """


class BwaveformAmplitude(SCPICmdWrite):
    """The ``BWAVeform:AMPLitude`` command.

    Description:
        - This command sets or returns the peak-to-peak Amplitude value for the waveform created by
          the Basic Waveform editor plug-in. This setting can be affected if the system is set to
          use the full DAC range. Using the full DAC range is the default setting. Refer to the
          command ``BWAVEFORM:FDRANGE`` for more information.

    Usage:
        - Using the ``.write(value)`` method will send the ``BWAVeform:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - BWAVeform:AMPLitude <amplitude>
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Bwaveform(SCPICmdRead):
    """The ``BWAVeform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``BWAVeform?`` query.
        - Using the ``.verify(value)`` method will send the ``BWAVeform?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``BWAVeform:AMPLitude`` command.
        - ``.auto``: The ``BWAVeform:AUTO`` command.
        - ``.compile``: The ``BWAVeform:COMPile`` command.
        - ``.cycle``: The ``BWAVeform:CYCLe`` command.
        - ``.fdrange``: The ``BWAVeform:FDRange`` command.
        - ``.frequency``: The ``BWAVeform:FREQuency`` command.
        - ``.function``: The ``BWAVeform:FUNCtion`` command.
        - ``.high``: The ``BWAVeform:HIGH`` command.
        - ``.length``: The ``BWAVeform:LENGth`` command.
        - ``.low``: The ``BWAVeform:LOW`` command.
        - ``.offset``: The ``BWAVeform:OFFSet`` command.
        - ``.reset``: The ``BWAVeform:RESet`` command.
        - ``.srate``: The ``BWAVeform:SRATe`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "BWAVeform") -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = BwaveformAmplitude(device, f"{self._cmd_syntax}:AMPLitude")
        self._auto = BwaveformAuto(device, f"{self._cmd_syntax}:AUTO")
        self._compile = BwaveformCompile(device, f"{self._cmd_syntax}:COMPile")
        self._cycle = BwaveformCycle(device, f"{self._cmd_syntax}:CYCLe")
        self._fdrange = BwaveformFdrange(device, f"{self._cmd_syntax}:FDRange")
        self._frequency = BwaveformFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._function = BwaveformFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._high = BwaveformHigh(device, f"{self._cmd_syntax}:HIGH")
        self._length = BwaveformLength(device, f"{self._cmd_syntax}:LENGth")
        self._low = BwaveformLow(device, f"{self._cmd_syntax}:LOW")
        self._offset = BwaveformOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._reset = BwaveformReset(device, f"{self._cmd_syntax}:RESet")
        self._srate = BwaveformSrate(device, f"{self._cmd_syntax}:SRATe")

    @property
    def amplitude(self) -> BwaveformAmplitude:
        """Return the ``BWAVeform:AMPLitude`` command.

        Description:
            - This command sets or returns the peak-to-peak Amplitude value for the waveform created
              by the Basic Waveform editor plug-in. This setting can be affected if the system is
              set to use the full DAC range. Using the full DAC range is the default setting. Refer
              to the command ``BWAVEFORM:FDRANGE`` for more information.

        Usage:
            - Using the ``.write(value)`` method will send the ``BWAVeform:AMPLitude value``
              command.

        SCPI Syntax:
            ```
            - BWAVeform:AMPLitude <amplitude>
            ```
        """
        return self._amplitude

    @property
    def auto(self) -> BwaveformAuto:
        """Return the ``BWAVeform:AUTO`` command.

        Description:
            - This command sets or returns the Basic Waveform editor plug-in Auto Calculate setting,
              determining which value is automatically calculated.

        Usage:
            - Using the ``.query()`` method will send the ``BWAVeform:AUTO?`` query.
            - Using the ``.verify(value)`` method will send the ``BWAVeform:AUTO?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BWAVeform:AUTO value`` command.

        SCPI Syntax:
            ```
            - BWAVeform:AUTO {LEN|CYCLE|DUR|FREQ|SR}
            - BWAVeform:AUTO?
            ```

        Info:
            - ``*RST`` sets this to Cycle.
        """
        return self._auto

    @property
    def compile(self) -> BwaveformCompile:
        """Return the ``BWAVeform:COMPile`` command.

        Description:
            - This command initiates the Basic Waveform editor plug-in compile process. The created
              waveform is placed in the Waveform List.

        Usage:
            - Using the ``.write()`` method will send the ``BWAVeform:COMPile`` command.

        SCPI Syntax:
            ```
            - BWAVeform:COMPile
            ```

        Sub-properties:
            - ``.cassign``: The ``BWAVeform:COMPile:CASSign`` command.
            - ``.channel``: The ``BWAVeform:COMPile:CHANnel`` command.
            - ``.name``: The ``BWAVeform:COMPile:NAME`` command.
            - ``.play``: The ``BWAVeform:COMPile:PLAY`` command.
        """
        return self._compile

    @property
    def cycle(self) -> BwaveformCycle:
        """Return the ``BWAVeform:CYCLe`` command.

        Description:
            - This command sets or returns the Cycle value (number of times the waveform repeats)
              for the waveform created by the Basic Waveform editor plug-in.

        Usage:
            - Using the ``.write(value)`` method will send the ``BWAVeform:CYCLe value`` command.

        SCPI Syntax:
            ```
            - BWAVeform:CYCLe <cycle>
            ```
        """
        return self._cycle

    @property
    def fdrange(self) -> BwaveformFdrange:
        """Return the ``BWAVeform:FDRange`` command.

        Description:
            - This command sets or returns the state (enabled or disabled) of the Basic Waveform
              editor plug-in to use or not use the full DAC range during compile. Using the full DAC
              range when compiling waveforms results in waveforms with the best resolution. When
              enabled, if the selected offset and amplitude are within the range of the instrument's
              hardware, then the compiled waveform is compiled using the full DAC range and the
              compiled waveform's recommended amplitude and offset properties are set to the
              requested amplitude and offset values. If the selected offset and amplitude will
              result in a compiled waveform that does not take advantage of the full DAC range, the
              instrument adjusts the compiled waveform's recommended amplitude and offset values to
              use the full DAC range. If the system cannot achieve the full DAC range, a warning
              message is displayed. When disabled, the waveform is compiled using the specified
              amplitude and offset values and the compiled waveform's recommended amplitude is set
              to the maximum value and the recommended offset is set to 0. The control is not
              available for a DC waveform.

        Usage:
            - Using the ``.write(value)`` method will send the ``BWAVeform:FDRange value`` command.

        SCPI Syntax:
            ```
            - BWAVeform:FDRange {0|1|OFF|ON}
            ```
        """
        return self._fdrange

    @property
    def frequency(self) -> BwaveformFrequency:
        """Return the ``BWAVeform:FREQuency`` command.

        Description:
            - This command sets or returns the Frequency for the waveform created by the Basic
              Waveform editor plug-in.

        Usage:
            - Using the ``.write(value)`` method will send the ``BWAVeform:FREQuency value``
              command.

        SCPI Syntax:
            ```
            - BWAVeform:FREQuency <frequency>
            ```
        """
        return self._frequency

    @property
    def function(self) -> BwaveformFunction:
        """Return the ``BWAVeform:FUNCtion`` command.

        Description:
            - This command sets or returns the Basic Waveform editor plug-in waveform type.

        Usage:
            - Using the ``.query()`` method will send the ``BWAVeform:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``BWAVeform:FUNCtion?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``BWAVeform:FUNCtion value`` command.

        SCPI Syntax:
            ```
            - BWAVeform:FUNCtion {sine|square|triangle|ramp|noise|DC}
            - BWAVeform:FUNCtion?
            ```

        Info:
            - ``*RST`` sets this to SINE.
        """
        return self._function

    @property
    def high(self) -> BwaveformHigh:
        """Return the ``BWAVeform:HIGH`` command.

        Description:
            - This command sets or returns the High voltage value for the waveform created by the
              Basic Waveform editor plug-in.

        Usage:
            - Using the ``.write(value)`` method will send the ``BWAVeform:HIGH value`` command.

        SCPI Syntax:
            ```
            - BWAVeform:HIGH <high>
            ```
        """
        return self._high

    @property
    def length(self) -> BwaveformLength:
        """Return the ``BWAVeform:LENGth`` command.

        Description:
            - This command sets or returns the Length for the waveform created by the Basic Waveform
              editor plug-in.

        Usage:
            - Using the ``.write(value)`` method will send the ``BWAVeform:LENGth value`` command.

        SCPI Syntax:
            ```
            - BWAVeform:LENGth <length>
            ```
        """
        return self._length

    @property
    def low(self) -> BwaveformLow:
        """Return the ``BWAVeform:LOW`` command.

        Description:
            - This command sets or returns the Low voltage value for the waveform created by the
              Basic Waveform editor plug-in.

        Usage:
            - Using the ``.write(value)`` method will send the ``BWAVeform:LOW value`` command.

        SCPI Syntax:
            ```
            - BWAVeform:LOW <low>
            ```
        """
        return self._low

    @property
    def offset(self) -> BwaveformOffset:
        """Return the ``BWAVeform:OFFSet`` command.

        Description:
            - This command sets or returns the Offset voltage value for the waveform created by the
              Basic Waveform editor plug-in. This setting can be affected if the system is set to
              use the full DAC range. Using the full DAC range is the default setting. Refer to the
              command ``BWAVEFORM:FDRANGE`` for more information.

        Usage:
            - Using the ``.write(value)`` method will send the ``BWAVeform:OFFSet value`` command.

        SCPI Syntax:
            ```
            - BWAVeform:OFFSet <offset>
            ```
        """
        return self._offset

    @property
    def reset(self) -> BwaveformReset:
        """Return the ``BWAVeform:RESet`` command.

        Description:
            - This command resets the Basic Waveform editor plug-in to its default values.

        Usage:
            - Using the ``.write()`` method will send the ``BWAVeform:RESet`` command.

        SCPI Syntax:
            ```
            - BWAVeform:RESet
            ```
        """
        return self._reset

    @property
    def srate(self) -> BwaveformSrate:
        """Return the ``BWAVeform:SRATe`` command.

        Description:
            - This command sets or returns the Sample Rate for the waveform created by the Basic
              Waveform editor plug-in.

        Usage:
            - Using the ``.write(value)`` method will send the ``BWAVeform:SRATe value`` command.

        SCPI Syntax:
            ```
            - BWAVeform:SRATe <sample_rate>
            ```
        """
        return self._srate
