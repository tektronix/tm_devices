# pylint: disable=line-too-long
"""The cplayback commands module.

These commands are used in the following models:
AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CPLayback:CAPTure:FILE <signal_name>,{SIQ|CIQ},<file_path>[,<file_path>]
    - CPLayback:CAPTure:INSTrument:OSCilloscope <signal_name>,<instrument_name>,<source_1>,<source_2>
    - CPLayback:CAPTure:INSTrument:RSA <signal_name>,<instrument_name>
    - CPLayback:CAPTure:WLISt <signal_name>,<waveform_name>
    - CPLayback:CLISt:NAME? <index>
    - CPLayback:CLISt:SIGNal:DELete {ALL|signal_name}
    - CPLayback:CLISt:SIGNal:SCOMpile <signal_name>,{OFF|ON|1|0}
    - CPLayback:CLISt:SIGNal:SCOMpile?
    - CPLayback:CLISt:SIGNal:WAVeform:FOFFset <signal_name>,<ALL|NR1>,<NRf>
    - CPLayback:CLISt:SIGNal:WAVeform:FOFFset? <signal_name>,<NR1>
    - CPLayback:CLISt:SIGNal:WAVeform:NAME? <signal_name>,<NR1>
    - CPLayback:CLISt:SIGNal:WAVeform:OTIMe <signal_name>,<ALL|<NR1>,<NRf>
    - CPLayback:CLISt:SIGNal:WAVeform:OTIMe? <signal_name>,<NR1>
    - CPLayback:CLISt:SIGNal:WAVeform:SRATe <signal_name>,<ALL|NR1>,<NRf>
    - CPLayback:CLISt:SIGNal:WAVeform:SRATe? <signal_name>,<NR1>
    - CPLayback:CLISt:SIGNal:WCOunt? <signal_name>
    - CPLayback:CLISt:SIZE?
    - CPLayback:COMPile
    - CPLayback:COMPile:CFRequency <carrier_frequency>
    - CPLayback:COMPile:CFRequency?
    - CPLayback:COMPile:LSEQuence {OFF|ON|0|1}
    - CPLayback:COMPile:LSEQuence?
    - CPLayback:COMPile:NORMalize {NONE|FSCale|ZREFerence}
    - CPLayback:COMPile:NORMalize?
    - CPLayback:COMPile:SRATe <NRf>
    - CPLayback:COMPile:SRATe:AUTO {0|1|OFF|ON}
    - CPLayback:COMPile:SRATe:AUTO?
    - CPLayback:COMPile:SRATe?
    ```
"""  # noqa: E501

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CplaybackCompileSrateAuto(SCPICmdWrite, SCPICmdRead):
    """The ``CPLayback:COMPile:SRATe:AUTO`` command.

    Description:
        - This command sets or returns if the system will calculate the output sampling rate
          automatically when compiling the selected signals.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:COMPile:SRATe:AUTO?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:COMPile:SRATe:AUTO?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CPLayback:COMPile:SRATe:AUTO value``
          command.

    SCPI Syntax:
        ```
        - CPLayback:COMPile:SRATe:AUTO {0|1|OFF|ON}
        - CPLayback:COMPile:SRATe:AUTO?
        ```
    """


class CplaybackCompileSrate(SCPICmdWrite, SCPICmdRead):
    """The ``CPLayback:COMPile:SRATe`` command.

    Description:
        - This command sets or returns the output sampling rate for the compiled signals.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:COMPile:SRATe?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:COMPile:SRATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CPLayback:COMPile:SRATe value``
          command.

    SCPI Syntax:
        ```
        - CPLayback:COMPile:SRATe <NRf>
        - CPLayback:COMPile:SRATe?
        ```

    Info:
        - ``*RST`` sets this to the maximum sample rate.

    Properties:
        - ``.auto``: The ``CPLayback:COMPile:SRATe:AUTO`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._auto = CplaybackCompileSrateAuto(device, f"{self._cmd_syntax}:AUTO")

    @property
    def auto(self) -> CplaybackCompileSrateAuto:
        """Return the ``CPLayback:COMPile:SRATe:AUTO`` command.

        Description:
            - This command sets or returns if the system will calculate the output sampling rate
              automatically when compiling the selected signals.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:COMPile:SRATe:AUTO?`` query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:COMPile:SRATe:AUTO?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CPLayback:COMPile:SRATe:AUTO value`` command.

        SCPI Syntax:
            ```
            - CPLayback:COMPile:SRATe:AUTO {0|1|OFF|ON}
            - CPLayback:COMPile:SRATe:AUTO?
            ```
        """
        return self._auto


class CplaybackCompileNormalize(SCPICmdWrite, SCPICmdRead):
    """The ``CPLayback:COMPile:NORMalize`` command.

    Description:
        - This command sets or returns if the IQ waveforms will be normalized during import.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:COMPile:NORMalize?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:COMPile:NORMalize?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CPLayback:COMPile:NORMalize value``
          command.

    SCPI Syntax:
        ```
        - CPLayback:COMPile:NORMalize {NONE|FSCale|ZREFerence}
        - CPLayback:COMPile:NORMalize?
        ```
    """


class CplaybackCompileLsequence(SCPICmdWrite, SCPICmdRead):
    """The ``CPLayback:COMPile:LSEQuence`` command.

    Description:
        - This command sets or returns if the compiled sequence should loop on itself, setting the
          GoTo of last sequence step to First.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:COMPile:LSEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:COMPile:LSEQuence?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CPLayback:COMPile:LSEQuence value``
          command.

    SCPI Syntax:
        ```
        - CPLayback:COMPile:LSEQuence {OFF|ON|0|1}
        - CPLayback:COMPile:LSEQuence?
        ```
    """


class CplaybackCompileCfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``CPLayback:COMPile:CFRequency`` command.

    Description:
        - This command sets or returns the Carrier Frequency for the compiled signals.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:COMPile:CFRequency?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:COMPile:CFRequency?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CPLayback:COMPile:CFRequency value``
          command.

    SCPI Syntax:
        ```
        - CPLayback:COMPile:CFRequency <carrier_frequency>
        - CPLayback:COMPile:CFRequency?
        ```

    Info:
        - ``*RST`` sets this to 1 GHz.
    """


class CplaybackCompile(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``CPLayback:COMPile`` command.

    Description:
        - The command resamples and upconverts the selected signal to the specified carrier
          frequency. With Option 03 (Sequencing) enabled: A sequence is generated containing all
          waveform segments in the signal (even if the signal contains only one waveform segment.
          Without Option 03 (Sequencing): A waveform is generated if there is only one waveform
          segment in the signal. If the signal contains multiple waveform segments, the compile
          fails and an error message is generated. You can select to compile more than one signal at
          a time. The compile process generates a sequence (or waveform) for each of the selected
          signals.

    Usage:
        - Using the ``.write()`` method will send the ``CPLayback:COMPile`` command.

    SCPI Syntax:
        ```
        - CPLayback:COMPile
        ```

    Properties:
        - ``.cfrequency``: The ``CPLayback:COMPile:CFRequency`` command.
        - ``.lsequence``: The ``CPLayback:COMPile:LSEQuence`` command.
        - ``.normalize``: The ``CPLayback:COMPile:NORMalize`` command.
        - ``.srate``: The ``CPLayback:COMPile:SRATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cfrequency = CplaybackCompileCfrequency(device, f"{self._cmd_syntax}:CFRequency")
        self._lsequence = CplaybackCompileLsequence(device, f"{self._cmd_syntax}:LSEQuence")
        self._normalize = CplaybackCompileNormalize(device, f"{self._cmd_syntax}:NORMalize")
        self._srate = CplaybackCompileSrate(device, f"{self._cmd_syntax}:SRATe")

    @property
    def cfrequency(self) -> CplaybackCompileCfrequency:
        """Return the ``CPLayback:COMPile:CFRequency`` command.

        Description:
            - This command sets or returns the Carrier Frequency for the compiled signals.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:COMPile:CFRequency?`` query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:COMPile:CFRequency?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CPLayback:COMPile:CFRequency value`` command.

        SCPI Syntax:
            ```
            - CPLayback:COMPile:CFRequency <carrier_frequency>
            - CPLayback:COMPile:CFRequency?
            ```

        Info:
            - ``*RST`` sets this to 1 GHz.
        """
        return self._cfrequency

    @property
    def lsequence(self) -> CplaybackCompileLsequence:
        """Return the ``CPLayback:COMPile:LSEQuence`` command.

        Description:
            - This command sets or returns if the compiled sequence should loop on itself, setting
              the GoTo of last sequence step to First.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:COMPile:LSEQuence?`` query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:COMPile:LSEQuence?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CPLayback:COMPile:LSEQuence value``
              command.

        SCPI Syntax:
            ```
            - CPLayback:COMPile:LSEQuence {OFF|ON|0|1}
            - CPLayback:COMPile:LSEQuence?
            ```
        """
        return self._lsequence

    @property
    def normalize(self) -> CplaybackCompileNormalize:
        """Return the ``CPLayback:COMPile:NORMalize`` command.

        Description:
            - This command sets or returns if the IQ waveforms will be normalized during import.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:COMPile:NORMalize?`` query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:COMPile:NORMalize?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CPLayback:COMPile:NORMalize value``
              command.

        SCPI Syntax:
            ```
            - CPLayback:COMPile:NORMalize {NONE|FSCale|ZREFerence}
            - CPLayback:COMPile:NORMalize?
            ```
        """
        return self._normalize

    @property
    def srate(self) -> CplaybackCompileSrate:
        """Return the ``CPLayback:COMPile:SRATe`` command.

        Description:
            - This command sets or returns the output sampling rate for the compiled signals.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:COMPile:SRATe?`` query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:COMPile:SRATe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CPLayback:COMPile:SRATe value``
              command.

        SCPI Syntax:
            ```
            - CPLayback:COMPile:SRATe <NRf>
            - CPLayback:COMPile:SRATe?
            ```

        Info:
            - ``*RST`` sets this to the maximum sample rate.

        Sub-properties:
            - ``.auto``: The ``CPLayback:COMPile:SRATe:AUTO`` command.
        """
        return self._srate


class CplaybackClistSize(SCPICmdRead):
    """The ``CPLayback:CLISt:SIZE`` command.

    Description:
        - This command returns the number of signals in the Captured Signal List.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:CLISt:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:CLISt:SIZE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CPLayback:CLISt:SIZE?
        ```
    """


class CplaybackClistSignalWcount(SCPICmdReadWithArguments):
    """The ``CPLayback:CLISt:SIGNal:WCOunt`` command.

    Description:
        - This command returns the number of waveform segments in the specified signal in the
          Captured Signal List.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``CPLayback:CLISt:SIGNal:WCOunt? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``CPLayback:CLISt:SIGNal:WCOunt? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CPLayback:CLISt:SIGNal:WCOunt? <signal_name>
        ```
    """


class CplaybackClistSignalWaveformSrate(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``CPLayback:CLISt:SIGNal:WAVeform:SRATe`` command.

    Description:
        - This command sets or returns the baseband sample rate of a waveform segment of a signal in
          the Captured Signal List.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``CPLayback:CLISt:SIGNal:WAVeform:SRATe? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``CPLayback:CLISt:SIGNal:WAVeform:SRATe? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CPLayback:CLISt:SIGNal:WAVeform:SRATe value`` command.

    SCPI Syntax:
        ```
        - CPLayback:CLISt:SIGNal:WAVeform:SRATe <signal_name>,<ALL|NR1>,<NRf>
        - CPLayback:CLISt:SIGNal:WAVeform:SRATe? <signal_name>,<NR1>
        ```
    """


class CplaybackClistSignalWaveformOtime(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``CPLayback:CLISt:SIGNal:WAVeform:OTIMe`` command.

    Description:
        - This command sets or returns the Off time between waveform segments of the specified
          signal in the Captured Signal List.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``CPLayback:CLISt:SIGNal:WAVeform:OTIMe? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``CPLayback:CLISt:SIGNal:WAVeform:OTIMe? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CPLayback:CLISt:SIGNal:WAVeform:OTIMe value`` command.

    SCPI Syntax:
        ```
        - CPLayback:CLISt:SIGNal:WAVeform:OTIMe <signal_name>,<ALL|<NR1>,<NRf>
        - CPLayback:CLISt:SIGNal:WAVeform:OTIMe? <signal_name>,<NR1>
        ```
    """


class CplaybackClistSignalWaveformName(SCPICmdReadWithArguments):
    """The ``CPLayback:CLISt:SIGNal:WAVeform:NAME`` command.

    Description:
        - This command returns the name of the specified waveform segment of the specified signal in
          the Captured Signal List.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``CPLayback:CLISt:SIGNal:WAVeform:NAME? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``CPLayback:CLISt:SIGNal:WAVeform:NAME? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CPLayback:CLISt:SIGNal:WAVeform:NAME? <signal_name>,<NR1>
        ```
    """


class CplaybackClistSignalWaveformFoffset(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``CPLayback:CLISt:SIGNal:WAVeform:FOFFset`` command.

    Description:
        - This command sets or returns the frequency offset of the specified waveform segment of the
          specified signal in the Captured Signal List.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``CPLayback:CLISt:SIGNal:WAVeform:FOFFset? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``CPLayback:CLISt:SIGNal:WAVeform:FOFFset? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CPLayback:CLISt:SIGNal:WAVeform:FOFFset value`` command.

    SCPI Syntax:
        ```
        - CPLayback:CLISt:SIGNal:WAVeform:FOFFset <signal_name>,<ALL|NR1>,<NRf>
        - CPLayback:CLISt:SIGNal:WAVeform:FOFFset? <signal_name>,<NR1>
        ```
    """


class CplaybackClistSignalWaveform(SCPICmdRead):
    """The ``CPLayback:CLISt:SIGNal:WAVeform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:CLISt:SIGNal:WAVeform?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:CLISt:SIGNal:WAVeform?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.foffset``: The ``CPLayback:CLISt:SIGNal:WAVeform:FOFFset`` command.
        - ``.name``: The ``CPLayback:CLISt:SIGNal:WAVeform:NAME`` command.
        - ``.otime``: The ``CPLayback:CLISt:SIGNal:WAVeform:OTIMe`` command.
        - ``.srate``: The ``CPLayback:CLISt:SIGNal:WAVeform:SRATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._foffset = CplaybackClistSignalWaveformFoffset(device, f"{self._cmd_syntax}:FOFFset")
        self._name = CplaybackClistSignalWaveformName(device, f"{self._cmd_syntax}:NAME")
        self._otime = CplaybackClistSignalWaveformOtime(device, f"{self._cmd_syntax}:OTIMe")
        self._srate = CplaybackClistSignalWaveformSrate(device, f"{self._cmd_syntax}:SRATe")

    @property
    def foffset(self) -> CplaybackClistSignalWaveformFoffset:
        """Return the ``CPLayback:CLISt:SIGNal:WAVeform:FOFFset`` command.

        Description:
            - This command sets or returns the frequency offset of the specified waveform segment of
              the specified signal in the Captured Signal List.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``CPLayback:CLISt:SIGNal:WAVeform:FOFFset? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CPLayback:CLISt:SIGNal:WAVeform:FOFFset? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CPLayback:CLISt:SIGNal:WAVeform:FOFFset value`` command.

        SCPI Syntax:
            ```
            - CPLayback:CLISt:SIGNal:WAVeform:FOFFset <signal_name>,<ALL|NR1>,<NRf>
            - CPLayback:CLISt:SIGNal:WAVeform:FOFFset? <signal_name>,<NR1>
            ```
        """
        return self._foffset

    @property
    def name(self) -> CplaybackClistSignalWaveformName:
        """Return the ``CPLayback:CLISt:SIGNal:WAVeform:NAME`` command.

        Description:
            - This command returns the name of the specified waveform segment of the specified
              signal in the Captured Signal List.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``CPLayback:CLISt:SIGNal:WAVeform:NAME? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CPLayback:CLISt:SIGNal:WAVeform:NAME? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CPLayback:CLISt:SIGNal:WAVeform:NAME? <signal_name>,<NR1>
            ```
        """
        return self._name

    @property
    def otime(self) -> CplaybackClistSignalWaveformOtime:
        """Return the ``CPLayback:CLISt:SIGNal:WAVeform:OTIMe`` command.

        Description:
            - This command sets or returns the Off time between waveform segments of the specified
              signal in the Captured Signal List.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``CPLayback:CLISt:SIGNal:WAVeform:OTIMe? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CPLayback:CLISt:SIGNal:WAVeform:OTIMe? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CPLayback:CLISt:SIGNal:WAVeform:OTIMe value`` command.

        SCPI Syntax:
            ```
            - CPLayback:CLISt:SIGNal:WAVeform:OTIMe <signal_name>,<ALL|<NR1>,<NRf>
            - CPLayback:CLISt:SIGNal:WAVeform:OTIMe? <signal_name>,<NR1>
            ```
        """
        return self._otime

    @property
    def srate(self) -> CplaybackClistSignalWaveformSrate:
        """Return the ``CPLayback:CLISt:SIGNal:WAVeform:SRATe`` command.

        Description:
            - This command sets or returns the baseband sample rate of a waveform segment of a
              signal in the Captured Signal List.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``CPLayback:CLISt:SIGNal:WAVeform:SRATe? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CPLayback:CLISt:SIGNal:WAVeform:SRATe? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CPLayback:CLISt:SIGNal:WAVeform:SRATe value`` command.

        SCPI Syntax:
            ```
            - CPLayback:CLISt:SIGNal:WAVeform:SRATe <signal_name>,<ALL|NR1>,<NRf>
            - CPLayback:CLISt:SIGNal:WAVeform:SRATe? <signal_name>,<NR1>
            ```
        """
        return self._srate


class CplaybackClistSignalScompile(SCPICmdWrite, SCPICmdRead):
    """The ``CPLayback:CLISt:SIGNal:SCOMpile`` command.

    Description:
        - This command selects or deselects a signal from the captured signal list to be compiled.
          Single signals are selected with the command but more than one signal can be selected for
          compilation by sending multiple commands. Signals remain selected until deselected with
          this command. The query form returns the list of selected signals.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:CLISt:SIGNal:SCOMpile?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:CLISt:SIGNal:SCOMpile?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CPLayback:CLISt:SIGNal:SCOMpile value``
          command.

    SCPI Syntax:
        ```
        - CPLayback:CLISt:SIGNal:SCOMpile <signal_name>,{OFF|ON|1|0}
        - CPLayback:CLISt:SIGNal:SCOMpile?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class CplaybackClistSignalDelete(SCPICmdWrite):
    """The ``CPLayback:CLISt:SIGNal:DELete`` command.

    Description:
        - This command removes the specified signal from the Captured Signal List.

    Usage:
        - Using the ``.write(value)`` method will send the ``CPLayback:CLISt:SIGNal:DELete value``
          command.

    SCPI Syntax:
        ```
        - CPLayback:CLISt:SIGNal:DELete {ALL|signal_name}
        ```
    """


class CplaybackClistSignal(SCPICmdRead):
    """The ``CPLayback:CLISt:SIGNal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:CLISt:SIGNal?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:CLISt:SIGNal?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delete``: The ``CPLayback:CLISt:SIGNal:DELete`` command.
        - ``.scompile``: The ``CPLayback:CLISt:SIGNal:SCOMpile`` command.
        - ``.waveform``: The ``CPLayback:CLISt:SIGNal:WAVeform`` command tree.
        - ``.wcount``: The ``CPLayback:CLISt:SIGNal:WCOunt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delete = CplaybackClistSignalDelete(device, f"{self._cmd_syntax}:DELete")
        self._scompile = CplaybackClistSignalScompile(device, f"{self._cmd_syntax}:SCOMpile")
        self._waveform = CplaybackClistSignalWaveform(device, f"{self._cmd_syntax}:WAVeform")
        self._wcount = CplaybackClistSignalWcount(device, f"{self._cmd_syntax}:WCOunt")

    @property
    def delete(self) -> CplaybackClistSignalDelete:
        """Return the ``CPLayback:CLISt:SIGNal:DELete`` command.

        Description:
            - This command removes the specified signal from the Captured Signal List.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``CPLayback:CLISt:SIGNal:DELete value`` command.

        SCPI Syntax:
            ```
            - CPLayback:CLISt:SIGNal:DELete {ALL|signal_name}
            ```
        """
        return self._delete

    @property
    def scompile(self) -> CplaybackClistSignalScompile:
        """Return the ``CPLayback:CLISt:SIGNal:SCOMpile`` command.

        Description:
            - This command selects or deselects a signal from the captured signal list to be
              compiled. Single signals are selected with the command but more than one signal can be
              selected for compilation by sending multiple commands. Signals remain selected until
              deselected with this command. The query form returns the list of selected signals.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:CLISt:SIGNal:SCOMpile?``
              query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:CLISt:SIGNal:SCOMpile?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CPLayback:CLISt:SIGNal:SCOMpile value`` command.

        SCPI Syntax:
            ```
            - CPLayback:CLISt:SIGNal:SCOMpile <signal_name>,{OFF|ON|1|0}
            - CPLayback:CLISt:SIGNal:SCOMpile?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._scompile

    @property
    def waveform(self) -> CplaybackClistSignalWaveform:
        """Return the ``CPLayback:CLISt:SIGNal:WAVeform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:CLISt:SIGNal:WAVeform?``
              query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:CLISt:SIGNal:WAVeform?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.foffset``: The ``CPLayback:CLISt:SIGNal:WAVeform:FOFFset`` command.
            - ``.name``: The ``CPLayback:CLISt:SIGNal:WAVeform:NAME`` command.
            - ``.otime``: The ``CPLayback:CLISt:SIGNal:WAVeform:OTIMe`` command.
            - ``.srate``: The ``CPLayback:CLISt:SIGNal:WAVeform:SRATe`` command.
        """
        return self._waveform

    @property
    def wcount(self) -> CplaybackClistSignalWcount:
        """Return the ``CPLayback:CLISt:SIGNal:WCOunt`` command.

        Description:
            - This command returns the number of waveform segments in the specified signal in the
              Captured Signal List.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``CPLayback:CLISt:SIGNal:WCOunt? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CPLayback:CLISt:SIGNal:WCOunt? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CPLayback:CLISt:SIGNal:WCOunt? <signal_name>
            ```
        """
        return self._wcount


class CplaybackClistName(SCPICmdReadWithArguments):
    """The ``CPLayback:CLISt:NAME`` command.

    Description:
        - This command returns the name of a signal from the Captured Signal List in the position
          specified by the index value.

    Usage:
        - Using the ``.query(argument)`` method will send the ``CPLayback:CLISt:NAME? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``CPLayback:CLISt:NAME? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - CPLayback:CLISt:NAME? <index>
        ```
    """


class CplaybackClist(SCPICmdRead):
    """The ``CPLayback:CLISt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:CLISt?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:CLISt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.name``: The ``CPLayback:CLISt:NAME`` command.
        - ``.signal``: The ``CPLayback:CLISt:SIGNal`` command tree.
        - ``.size``: The ``CPLayback:CLISt:SIZE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._name = CplaybackClistName(device, f"{self._cmd_syntax}:NAME")
        self._signal = CplaybackClistSignal(device, f"{self._cmd_syntax}:SIGNal")
        self._size = CplaybackClistSize(device, f"{self._cmd_syntax}:SIZE")

    @property
    def name(self) -> CplaybackClistName:
        """Return the ``CPLayback:CLISt:NAME`` command.

        Description:
            - This command returns the name of a signal from the Captured Signal List in the
              position specified by the index value.

        Usage:
            - Using the ``.query(argument)`` method will send the ``CPLayback:CLISt:NAME? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CPLayback:CLISt:NAME? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - CPLayback:CLISt:NAME? <index>
            ```
        """
        return self._name

    @property
    def signal(self) -> CplaybackClistSignal:
        """Return the ``CPLayback:CLISt:SIGNal`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:CLISt:SIGNal?`` query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:CLISt:SIGNal?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delete``: The ``CPLayback:CLISt:SIGNal:DELete`` command.
            - ``.scompile``: The ``CPLayback:CLISt:SIGNal:SCOMpile`` command.
            - ``.waveform``: The ``CPLayback:CLISt:SIGNal:WAVeform`` command tree.
            - ``.wcount``: The ``CPLayback:CLISt:SIGNal:WCOunt`` command.
        """
        return self._signal

    @property
    def size(self) -> CplaybackClistSize:
        """Return the ``CPLayback:CLISt:SIZE`` command.

        Description:
            - This command returns the number of signals in the Captured Signal List.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:CLISt:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:CLISt:SIZE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CPLayback:CLISt:SIZE?
            ```
        """
        return self._size


class CplaybackCaptureWlist(SCPICmdWrite):
    """The ``CPLayback:CAPTure:WLISt`` command.

    Description:
        - This command adds the specified IQ waveform from the Waveform List to the specified signal
          in the Captured Signal List. If the specified signal does not exist, a new signal is
          created and added to the captured signal list.

    Usage:
        - Using the ``.write(value)`` method will send the ``CPLayback:CAPTure:WLISt value``
          command.

    SCPI Syntax:
        ```
        - CPLayback:CAPTure:WLISt <signal_name>,<waveform_name>
        ```
    """


class CplaybackCaptureInstrumentRsa(SCPICmdWrite):
    """The ``CPLayback:CAPTure:INSTrument:RSA`` command.

    Description:
        - This command connects to the specified RSA (Realtime Spectrum Analyzer), transfers the
          existing acquisition to the AWG, and adds it to the specified signal. If the specified
          signal does not exist, it is created and added to the captured signal list.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``CPLayback:CAPTure:INSTrument:RSA value`` command.

    SCPI Syntax:
        ```
        - CPLayback:CAPTure:INSTrument:RSA <signal_name>,<instrument_name>
        ```
    """


class CplaybackCaptureInstrumentOscilloscope(SCPICmdWrite):
    """The ``CPLayback:CAPTure:INSTrument:OSCilloscope`` command.

    Description:
        - This command connects to the specified oscilloscope, transfers the existing acquisition
          from the oscilloscope to the AWG, and adds it to the specified signal. If the specified
          signal does not exist, it is created and added to the captured signal list.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``CPLayback:CAPTure:INSTrument:OSCilloscope value`` command.

    SCPI Syntax:
        ```
        - CPLayback:CAPTure:INSTrument:OSCilloscope <signal_name>,<instrument_name>,<source_1>,<source_2>
        ```
    """  # noqa: E501


class CplaybackCaptureInstrument(SCPICmdRead):
    """The ``CPLayback:CAPTure:INSTrument`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:CAPTure:INSTrument?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:CAPTure:INSTrument?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.oscilloscope``: The ``CPLayback:CAPTure:INSTrument:OSCilloscope`` command.
        - ``.rsa``: The ``CPLayback:CAPTure:INSTrument:RSA`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._oscilloscope = CplaybackCaptureInstrumentOscilloscope(
            device, f"{self._cmd_syntax}:OSCilloscope"
        )
        self._rsa = CplaybackCaptureInstrumentRsa(device, f"{self._cmd_syntax}:RSA")

    @property
    def oscilloscope(self) -> CplaybackCaptureInstrumentOscilloscope:
        """Return the ``CPLayback:CAPTure:INSTrument:OSCilloscope`` command.

        Description:
            - This command connects to the specified oscilloscope, transfers the existing
              acquisition from the oscilloscope to the AWG, and adds it to the specified signal. If
              the specified signal does not exist, it is created and added to the captured signal
              list.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``CPLayback:CAPTure:INSTrument:OSCilloscope value`` command.

        SCPI Syntax:
            ```
            - CPLayback:CAPTure:INSTrument:OSCilloscope <signal_name>,<instrument_name>,<source_1>,<source_2>
            ```
        """  # noqa: E501
        return self._oscilloscope

    @property
    def rsa(self) -> CplaybackCaptureInstrumentRsa:
        """Return the ``CPLayback:CAPTure:INSTrument:RSA`` command.

        Description:
            - This command connects to the specified RSA (Realtime Spectrum Analyzer), transfers the
              existing acquisition to the AWG, and adds it to the specified signal. If the specified
              signal does not exist, it is created and added to the captured signal list.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``CPLayback:CAPTure:INSTrument:RSA value`` command.

        SCPI Syntax:
            ```
            - CPLayback:CAPTure:INSTrument:RSA <signal_name>,<instrument_name>
            ```
        """
        return self._rsa


class CplaybackCaptureFile(SCPICmdWrite):
    """The ``CPLayback:CAPTure:FILE`` command.

    Description:
        - The command imports baseband IQ waveform data and adds the waveform to the specified
          Signal Name in the captured signal list. If the specified Signal Name does not exist, it
          is created and added to the captured signal list. You can import a single IQ waveform,
          containing both the I and Q data, or you can import separate I and Q data files. When
          importing a single IQ waveform, the following file types are supported: .IQT - RSA3000
          Series waveform file format.TIQ - RSA6000 Series waveform file format.MAT - MATLAB file
          format.TMP - Midas Blue file format.PRM - Midas Blue file format When importing individual
          I and Q data files, the following file types are supported: .WFMX - AWG70000 Series
          waveform file format.TXT - AWG400/AWG500/AWG600/AWG700/AWG5000/AWG7000 Series waveform.WFM
          - AWG400/AWG500/AWG600/AWG700/AWG5000/AWG7000 Series waveform.MAT - MATLAB file format.RFD
          - RFXpress waveform file format

    Usage:
        - Using the ``.write(value)`` method will send the ``CPLayback:CAPTure:FILE value`` command.

    SCPI Syntax:
        ```
        - CPLayback:CAPTure:FILE <signal_name>,{SIQ|CIQ},<file_path>[,<file_path>]
        ```
    """


class CplaybackCapture(SCPICmdRead):
    """The ``CPLayback:CAPTure`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback:CAPTure?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback:CAPTure?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.file``: The ``CPLayback:CAPTure:FILE`` command.
        - ``.instrument``: The ``CPLayback:CAPTure:INSTrument`` command tree.
        - ``.wlist``: The ``CPLayback:CAPTure:WLISt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._file = CplaybackCaptureFile(device, f"{self._cmd_syntax}:FILE")
        self._instrument = CplaybackCaptureInstrument(device, f"{self._cmd_syntax}:INSTrument")
        self._wlist = CplaybackCaptureWlist(device, f"{self._cmd_syntax}:WLISt")

    @property
    def file(self) -> CplaybackCaptureFile:
        """Return the ``CPLayback:CAPTure:FILE`` command.

        Description:
            - The command imports baseband IQ waveform data and adds the waveform to the specified
              Signal Name in the captured signal list. If the specified Signal Name does not exist,
              it is created and added to the captured signal list. You can import a single IQ
              waveform, containing both the I and Q data, or you can import separate I and Q data
              files. When importing a single IQ waveform, the following file types are supported:
              .IQT - RSA3000 Series waveform file format.TIQ - RSA6000 Series waveform file
              format.MAT - MATLAB file format.TMP - Midas Blue file format.PRM - Midas Blue file
              format When importing individual I and Q data files, the following file types are
              supported: .WFMX - AWG70000 Series waveform file format.TXT -
              AWG400/AWG500/AWG600/AWG700/AWG5000/AWG7000 Series waveform.WFM -
              AWG400/AWG500/AWG600/AWG700/AWG5000/AWG7000 Series waveform.MAT - MATLAB file
              format.RFD - RFXpress waveform file format

        Usage:
            - Using the ``.write(value)`` method will send the ``CPLayback:CAPTure:FILE value``
              command.

        SCPI Syntax:
            ```
            - CPLayback:CAPTure:FILE <signal_name>,{SIQ|CIQ},<file_path>[,<file_path>]
            ```
        """
        return self._file

    @property
    def instrument(self) -> CplaybackCaptureInstrument:
        """Return the ``CPLayback:CAPTure:INSTrument`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:CAPTure:INSTrument?`` query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:CAPTure:INSTrument?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.oscilloscope``: The ``CPLayback:CAPTure:INSTrument:OSCilloscope`` command.
            - ``.rsa``: The ``CPLayback:CAPTure:INSTrument:RSA`` command.
        """
        return self._instrument

    @property
    def wlist(self) -> CplaybackCaptureWlist:
        """Return the ``CPLayback:CAPTure:WLISt`` command.

        Description:
            - This command adds the specified IQ waveform from the Waveform List to the specified
              signal in the Captured Signal List. If the specified signal does not exist, a new
              signal is created and added to the captured signal list.

        Usage:
            - Using the ``.write(value)`` method will send the ``CPLayback:CAPTure:WLISt value``
              command.

        SCPI Syntax:
            ```
            - CPLayback:CAPTure:WLISt <signal_name>,<waveform_name>
            ```
        """
        return self._wlist


class Cplayback(SCPICmdRead):
    """The ``CPLayback`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CPLayback?`` query.
        - Using the ``.verify(value)`` method will send the ``CPLayback?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.capture``: The ``CPLayback:CAPTure`` command tree.
        - ``.clist``: The ``CPLayback:CLISt`` command tree.
        - ``.compile``: The ``CPLayback:COMPile`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CPLayback") -> None:
        super().__init__(device, cmd_syntax)
        self._capture = CplaybackCapture(device, f"{self._cmd_syntax}:CAPTure")
        self._clist = CplaybackClist(device, f"{self._cmd_syntax}:CLISt")
        self._compile = CplaybackCompile(device, f"{self._cmd_syntax}:COMPile")

    @property
    def capture(self) -> CplaybackCapture:
        """Return the ``CPLayback:CAPTure`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:CAPTure?`` query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:CAPTure?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.file``: The ``CPLayback:CAPTure:FILE`` command.
            - ``.instrument``: The ``CPLayback:CAPTure:INSTrument`` command tree.
            - ``.wlist``: The ``CPLayback:CAPTure:WLISt`` command.
        """
        return self._capture

    @property
    def clist(self) -> CplaybackClist:
        """Return the ``CPLayback:CLISt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CPLayback:CLISt?`` query.
            - Using the ``.verify(value)`` method will send the ``CPLayback:CLISt?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.name``: The ``CPLayback:CLISt:NAME`` command.
            - ``.signal``: The ``CPLayback:CLISt:SIGNal`` command tree.
            - ``.size``: The ``CPLayback:CLISt:SIZE`` command.
        """
        return self._clist

    @property
    def compile(self) -> CplaybackCompile:
        """Return the ``CPLayback:COMPile`` command.

        Description:
            - The command resamples and upconverts the selected signal to the specified carrier
              frequency. With Option 03 (Sequencing) enabled: A sequence is generated containing all
              waveform segments in the signal (even if the signal contains only one waveform
              segment. Without Option 03 (Sequencing): A waveform is generated if there is only one
              waveform segment in the signal. If the signal contains multiple waveform segments, the
              compile fails and an error message is generated. You can select to compile more than
              one signal at a time. The compile process generates a sequence (or waveform) for each
              of the selected signals.

        Usage:
            - Using the ``.write()`` method will send the ``CPLayback:COMPile`` command.

        SCPI Syntax:
            ```
            - CPLayback:COMPile
            ```

        Sub-properties:
            - ``.cfrequency``: The ``CPLayback:COMPile:CFRequency`` command.
            - ``.lsequence``: The ``CPLayback:COMPile:LSEQuence`` command.
            - ``.normalize``: The ``CPLayback:COMPile:NORMalize`` command.
            - ``.srate``: The ``CPLayback:COMPile:SRATe`` command.
        """
        return self._compile
