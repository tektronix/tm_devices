"""The mmemory commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MMEMory:CATalog? [<msus>]
    - MMEMory:CDIRectory [<directory_name>]
    - MMEMory:CDIRectory?
    - MMEMory:DATA <file_name>,<block_data>
    - MMEMory:DATA? <file_name>
    - MMEMory:DELete <file_name>[,<msus>]
    - MMEMory:EXPort <wfm_name>,<filename>,<type>
    - MMEMory:IMPort <wfm_name>,<filename>,<type>
    - MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe <state>
    - MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe?
    - MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel <NR1>
    - MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel?
    - MMEMory:IMPort:PARameter:LEVel:UPDate:STATe <state>
    - MMEMory:IMPort:PARameter:LEVel:UPDate:STATe?
    - MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE <Type>
    - MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE?
    - MMEMory:IMPort:PARameter:NORMalize {NONE|FSCale|ZREFerence}
    - MMEMory:IMPort:PARameter:NORMalize?
    - MMEMory:IMPort:PARameter:RESampling:FREQuency <NR3>
    - MMEMory:IMPort:PARameter:RESampling:FREQuency?
    - MMEMory:IMPort:PARameter:RESampling:STATe <state>
    - MMEMory:IMPort:PARameter:RESampling:STATe?
    - MMEMory:MDIRectory <directory_name>
    - MMEMory:MSIS [<msus>]
    - MMEMory:MSIS?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MmemoryMsis(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:MSIS`` command.

    Description:
        - This command selects or returns a mass storage device used by all MMEMory commands. <msus>
          specifies a drive using a drive letter. The drive letter can represent hard disk drives,
          network drives, external DVD/CD-RW drives, or USB memory.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:MSIS?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:MSIS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MMEMory:MSIS value`` command.

    SCPI Syntax:
        ```
        - MMEMory:MSIS [<msus>]
        - MMEMory:MSIS?
        ```
    """


class MmemoryMdirectory(SCPICmdWrite):
    """The ``MMEMory:MDIRectory`` command.

    Description:
        - This command creates a directory in the mass storage system. If the specified directory is
          locked in the mass storage system, this command causes an error.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:MDIRectory value`` command.

    SCPI Syntax:
        ```
        - MMEMory:MDIRectory <directory_name>
        ```
    """


class MmemoryImportParameterResamplingState(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:RESampling:STATe`` command.

    Description:
        - This command sets or queries the resampling state for waveform import. This command is
          effective only when the following conditions are met: Waveform data to be imported must
          have sampling rate information. ``MMEMORY:IMPORT:PARAMETER:FREQUENCY:UPDATE:STATE``
          command must be set to True. Use this command to set the resampling state on or off. If
          you set the resampling state on, resampling is automatically invoked when importing
          waveform data. The query form of this command returns the resampling state of the
          instrument.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:RESampling:STATe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MMEMory:IMPort:PARameter:RESampling:STATe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MMEMory:IMPort:PARameter:RESampling:STATe value`` command.

    SCPI Syntax:
        ```
        - MMEMory:IMPort:PARameter:RESampling:STATe <state>
        - MMEMory:IMPort:PARameter:RESampling:STATe?
        ```

    Info:
        - ``<state>`` ::=<Boolean>.
    """


class MmemoryImportParameterResamplingFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:RESampling:FREQuency`` command.

    Description:
        - This command sets or queries the sampling rate parameter for resampling. The specified
          sampling rate is applied to imported waveform.

    Usage:
        - Using the ``.query()`` method will send the
          ``MMEMory:IMPort:PARameter:RESampling:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MMEMory:IMPort:PARameter:RESampling:FREQuency?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MMEMory:IMPort:PARameter:RESampling:FREQuency value`` command.

    SCPI Syntax:
        ```
        - MMEMory:IMPort:PARameter:RESampling:FREQuency <NR3>
        - MMEMory:IMPort:PARameter:RESampling:FREQuency?
        ```

    Info:
        - ``<NR3>``
    """


class MmemoryImportParameterResampling(SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:RESampling`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:RESampling?``
          query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:IMPort:PARameter:RESampling?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``MMEMory:IMPort:PARameter:RESampling:FREQuency`` command.
        - ``.state``: The ``MMEMory:IMPort:PARameter:RESampling:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = MmemoryImportParameterResamplingFrequency(
            device, f"{self._cmd_syntax}:FREQuency"
        )
        self._state = MmemoryImportParameterResamplingState(device, f"{self._cmd_syntax}:STATe")

    @property
    def frequency(self) -> MmemoryImportParameterResamplingFrequency:
        """Return the ``MMEMory:IMPort:PARameter:RESampling:FREQuency`` command.

        Description:
            - This command sets or queries the sampling rate parameter for resampling. The specified
              sampling rate is applied to imported waveform.

        Usage:
            - Using the ``.query()`` method will send the
              ``MMEMory:IMPort:PARameter:RESampling:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:RESampling:FREQuency?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MMEMory:IMPort:PARameter:RESampling:FREQuency value`` command.

        SCPI Syntax:
            ```
            - MMEMory:IMPort:PARameter:RESampling:FREQuency <NR3>
            - MMEMory:IMPort:PARameter:RESampling:FREQuency?
            ```

        Info:
            - ``<NR3>``
        """
        return self._frequency

    @property
    def state(self) -> MmemoryImportParameterResamplingState:
        """Return the ``MMEMory:IMPort:PARameter:RESampling:STATe`` command.

        Description:
            - This command sets or queries the resampling state for waveform import. This command is
              effective only when the following conditions are met: Waveform data to be imported
              must have sampling rate information.
              ``MMEMORY:IMPORT:PARAMETER:FREQUENCY:UPDATE:STATE`` command must be set to True. Use
              this command to set the resampling state on or off. If you set the resampling state
              on, resampling is automatically invoked when importing waveform data. The query form
              of this command returns the resampling state of the instrument.

        Usage:
            - Using the ``.query()`` method will send the
              ``MMEMory:IMPort:PARameter:RESampling:STATe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:RESampling:STATe?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MMEMory:IMPort:PARameter:RESampling:STATe value`` command.

        SCPI Syntax:
            ```
            - MMEMory:IMPort:PARameter:RESampling:STATe <state>
            - MMEMory:IMPort:PARameter:RESampling:STATe?
            ```

        Info:
            - ``<state>`` ::=<Boolean>.
        """
        return self._state


class MmemoryImportParameterNormalize(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:NORMalize`` command.

    Description:
        - This command sets or queries if the imported data is normalized during text data import
          operation. The imported waveform data is normalized based on the option set in this
          command. When ZREFerence is selected, the offset is preserved during normalization
          operation. If FSCale is selected, offset is lost and full scale of the DAC is used for
          normalization. NONE will not normalize the data.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:NORMalize?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:IMPort:PARameter:NORMalize?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MMEMory:IMPort:PARameter:NORMalize value`` command.

    SCPI Syntax:
        ```
        - MMEMory:IMPort:PARameter:NORMalize {NONE|FSCale|ZREFerence}
        - MMEMory:IMPort:PARameter:NORMalize?
        ```

    Info:
        - ``<Normalization_type>``
        - ``NONE`` indicates that the imported data is not normalized.
        - ``FSCale`` indicates that the imported data is normalized with full DAC range.
        - ``ZREFerence`` indicates that the imported data is normalized with offset preserved.
    """


class MmemoryImportParameterLevelUpdateType(SCPICmdWrite, SCPICmdRead):
    r"""The ``MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE`` command.

    Description:
        - This commands sets or queries the data to be imported. It also sets or queries which
          data's amplitude and offset values are selected for update during RSA file import. This
          command is effective only when ``MMEMORY:IMPORT:PARAMETER:LEVEL:UPDATE:STATE`` is set to
          True and IQT or TIQ is selected as the <Type> for the ``MMEMORY:IMPORT`` command.

    Usage:
        - Using the ``.query()`` method will send the
          ``MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE value`` command.

    SCPI Syntax:
        ```
        - MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE <Type>
        - MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE?
        ```

    Info:
        - ``<Type>`` ::={IDATa\|QDATa}.
        - ``IDATa`` indicates that the instrument imports I data.
        - ``QDATa`` indicates that the instrument imports Q data.
    """


class MmemoryImportParameterLevelUpdateState(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:LEVel:UPDate:STATe`` command.

    Description:
        - This command sets or queries the LEVel parameter which determines whether amplitude and
          offsets are modified during waveform import. If this value is set, the instrument
          amplitude and offset are automatically updated during waveform import.

    Usage:
        - Using the ``.query()`` method will send the
          ``MMEMory:IMPort:PARameter:LEVel:UPDate:STATe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MMEMory:IMPort:PARameter:LEVel:UPDate:STATe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MMEMory:IMPort:PARameter:LEVel:UPDate:STATe value`` command.

    SCPI Syntax:
        ```
        - MMEMory:IMPort:PARameter:LEVel:UPDate:STATe <state>
        - MMEMory:IMPort:PARameter:LEVel:UPDate:STATe?
        ```

    Info:
        - ``<state>`` ::=<Boolean>.
        - ``0`` indicates OFF.
        - ``1`` indicates ON.
    """


class MmemoryImportParameterLevelUpdateChannel(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel`` command.

    Description:
        - This command sets or queries the channel for which the amplitude and offset values will be
          updated during import.

    Usage:
        - Using the ``.query()`` method will send the
          ``MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel value`` command.

    SCPI Syntax:
        ```
        - MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel <NR1>
        - MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel?
        ```

    Info:
        - ``<NR1>``
    """


class MmemoryImportParameterLevelUpdate(SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:LEVel:UPDate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:LEVel:UPDate?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MMEMory:IMPort:PARameter:LEVel:UPDate?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.channel``: The ``MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel`` command.
        - ``.type``: The ``MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE`` command.
        - ``.state``: The ``MMEMory:IMPort:PARameter:LEVel:UPDate:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._channel = MmemoryImportParameterLevelUpdateChannel(
            device, f"{self._cmd_syntax}:CHANnel"
        )
        self._type = MmemoryImportParameterLevelUpdateType(device, f"{self._cmd_syntax}:TYPE")
        self._state = MmemoryImportParameterLevelUpdateState(device, f"{self._cmd_syntax}:STATe")

    @property
    def channel(self) -> MmemoryImportParameterLevelUpdateChannel:
        """Return the ``MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel`` command.

        Description:
            - This command sets or queries the channel for which the amplitude and offset values
              will be updated during import.

        Usage:
            - Using the ``.query()`` method will send the
              ``MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel value`` command.

        SCPI Syntax:
            ```
            - MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel <NR1>
            - MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel?
            ```

        Info:
            - ``<NR1>``
        """
        return self._channel

    @property
    def type(self) -> MmemoryImportParameterLevelUpdateType:
        r"""Return the ``MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE`` command.

        Description:
            - This commands sets or queries the data to be imported. It also sets or queries which
              data's amplitude and offset values are selected for update during RSA file import.
              This command is effective only when ``MMEMORY:IMPORT:PARAMETER:LEVEL:UPDATE:STATE`` is
              set to True and IQT or TIQ is selected as the <Type> for the ``MMEMORY:IMPORT``
              command.

        Usage:
            - Using the ``.query()`` method will send the
              ``MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE value`` command.

        SCPI Syntax:
            ```
            - MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE <Type>
            - MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE?
            ```

        Info:
            - ``<Type>`` ::={IDATa\|QDATa}.
            - ``IDATa`` indicates that the instrument imports I data.
            - ``QDATa`` indicates that the instrument imports Q data.
        """
        return self._type

    @property
    def state(self) -> MmemoryImportParameterLevelUpdateState:
        """Return the ``MMEMory:IMPort:PARameter:LEVel:UPDate:STATe`` command.

        Description:
            - This command sets or queries the LEVel parameter which determines whether amplitude
              and offsets are modified during waveform import. If this value is set, the instrument
              amplitude and offset are automatically updated during waveform import.

        Usage:
            - Using the ``.query()`` method will send the
              ``MMEMory:IMPort:PARameter:LEVel:UPDate:STATe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:LEVel:UPDate:STATe?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MMEMory:IMPort:PARameter:LEVel:UPDate:STATe value`` command.

        SCPI Syntax:
            ```
            - MMEMory:IMPort:PARameter:LEVel:UPDate:STATe <state>
            - MMEMory:IMPort:PARameter:LEVel:UPDate:STATe?
            ```

        Info:
            - ``<state>`` ::=<Boolean>.
            - ``0`` indicates OFF.
            - ``1`` indicates ON.
        """
        return self._state


class MmemoryImportParameterLevel(SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:LEVel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:LEVel?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:IMPort:PARameter:LEVel?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.update``: The ``MMEMory:IMPort:PARameter:LEVel:UPDate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._update = MmemoryImportParameterLevelUpdate(device, f"{self._cmd_syntax}:UPDate")

    @property
    def update(self) -> MmemoryImportParameterLevelUpdate:
        """Return the ``MMEMory:IMPort:PARameter:LEVel:UPDate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:LEVel:UPDate?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:LEVel:UPDate?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.channel``: The ``MMEMory:IMPort:PARameter:LEVel:UPDate:CHANnel`` command.
            - ``.type``: The ``MMEMory:IMPort:PARameter:LEVel:UPDate:TYPE`` command.
            - ``.state``: The ``MMEMory:IMPort:PARameter:LEVel:UPDate:STATe`` command.
        """
        return self._update


class MmemoryImportParameterFrequencyUpdateState(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe`` command.

    Description:
        - This command sets or queries the FREQuency parameter which determines whether frequency is
          modified during waveform import. If this value is set, the sampling rate is automatically
          updated during waveform import.

    Usage:
        - Using the ``.query()`` method will send the
          ``MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe value`` command.

    SCPI Syntax:
        ```
        - MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe <state>
        - MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe?
        ```

    Info:
        - ``<state>`` ::=<Boolean>.
        - ``0`` indicates OFF.
        - ``1`` indicates ON.
    """


class MmemoryImportParameterFrequencyUpdate(SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:FREQuency:UPDate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:FREQuency:UPDate?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MMEMory:IMPort:PARameter:FREQuency:UPDate?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = MmemoryImportParameterFrequencyUpdateState(
            device, f"{self._cmd_syntax}:STATe"
        )

    @property
    def state(self) -> MmemoryImportParameterFrequencyUpdateState:
        """Return the ``MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe`` command.

        Description:
            - This command sets or queries the FREQuency parameter which determines whether
              frequency is modified during waveform import. If this value is set, the sampling rate
              is automatically updated during waveform import.

        Usage:
            - Using the ``.query()`` method will send the
              ``MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe value`` command.

        SCPI Syntax:
            ```
            - MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe <state>
            - MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe?
            ```

        Info:
            - ``<state>`` ::=<Boolean>.
            - ``0`` indicates OFF.
            - ``1`` indicates ON.
        """
        return self._state


class MmemoryImportParameterFrequency(SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter:FREQuency`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:IMPort:PARameter:FREQuency?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.update``: The ``MMEMory:IMPort:PARameter:FREQuency:UPDate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._update = MmemoryImportParameterFrequencyUpdate(device, f"{self._cmd_syntax}:UPDate")

    @property
    def update(self) -> MmemoryImportParameterFrequencyUpdate:
        """Return the ``MMEMory:IMPort:PARameter:FREQuency:UPDate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``MMEMory:IMPort:PARameter:FREQuency:UPDate?`` query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:FREQuency:UPDate?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``MMEMory:IMPort:PARameter:FREQuency:UPDate:STATe`` command.
        """
        return self._update


class MmemoryImportParameter(SCPICmdRead):
    """The ``MMEMory:IMPort:PARameter`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:IMPort:PARameter?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frequency``: The ``MMEMory:IMPort:PARameter:FREQuency`` command tree.
        - ``.level``: The ``MMEMory:IMPort:PARameter:LEVel`` command tree.
        - ``.normalize``: The ``MMEMory:IMPort:PARameter:NORMalize`` command.
        - ``.resampling``: The ``MMEMory:IMPort:PARameter:RESampling`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frequency = MmemoryImportParameterFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._level = MmemoryImportParameterLevel(device, f"{self._cmd_syntax}:LEVel")
        self._normalize = MmemoryImportParameterNormalize(device, f"{self._cmd_syntax}:NORMalize")
        self._resampling = MmemoryImportParameterResampling(
            device, f"{self._cmd_syntax}:RESampling"
        )

    @property
    def frequency(self) -> MmemoryImportParameterFrequency:
        """Return the ``MMEMory:IMPort:PARameter:FREQuency`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:FREQuency?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:FREQuency?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.update``: The ``MMEMory:IMPort:PARameter:FREQuency:UPDate`` command tree.
        """
        return self._frequency

    @property
    def level(self) -> MmemoryImportParameterLevel:
        """Return the ``MMEMory:IMPort:PARameter:LEVel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:LEVel?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:IMPort:PARameter:LEVel?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.update``: The ``MMEMory:IMPort:PARameter:LEVel:UPDate`` command tree.
        """
        return self._level

    @property
    def normalize(self) -> MmemoryImportParameterNormalize:
        """Return the ``MMEMory:IMPort:PARameter:NORMalize`` command.

        Description:
            - This command sets or queries if the imported data is normalized during text data
              import operation. The imported waveform data is normalized based on the option set in
              this command. When ZREFerence is selected, the offset is preserved during
              normalization operation. If FSCale is selected, offset is lost and full scale of the
              DAC is used for normalization. NONE will not normalize the data.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:NORMalize?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:NORMalize?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MMEMory:IMPort:PARameter:NORMalize value`` command.

        SCPI Syntax:
            ```
            - MMEMory:IMPort:PARameter:NORMalize {NONE|FSCale|ZREFerence}
            - MMEMory:IMPort:PARameter:NORMalize?
            ```

        Info:
            - ``<Normalization_type>``
            - ``NONE`` indicates that the imported data is not normalized.
            - ``FSCale`` indicates that the imported data is normalized with full DAC range.
            - ``ZREFerence`` indicates that the imported data is normalized with offset preserved.
        """
        return self._normalize

    @property
    def resampling(self) -> MmemoryImportParameterResampling:
        """Return the ``MMEMory:IMPort:PARameter:RESampling`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter:RESampling?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MMEMory:IMPort:PARameter:RESampling?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``MMEMory:IMPort:PARameter:RESampling:FREQuency`` command.
            - ``.state``: The ``MMEMory:IMPort:PARameter:RESampling:STATe`` command.
        """
        return self._resampling


class MmemoryImport(SCPICmdWrite, SCPICmdRead):
    r"""The ``MMEMory:IMPort`` command.

    Description:
        - This command imports a file into the arbitrary waveform generator's setup as a waveform.
          The supported file formats are: ISF - TDS3000 and DPO4000 waveform format TDS -
          TDS5000/TDS6000/TDS7000, DPO7000/DPO70000/DSA70000 Series waveform TXT - Text file with
          analog data TXT8 - Text file with 8-bit DAC resolution TXT10 - Text file with 10-bit DAC
          resolution TXT14 - Text file with 14-bit DAC resolution WFM - AWG400/AWG500/AWG600/AWG700
          Series waveform PAT - AWG400/AWG500/AWG600/AWG700 Series pattern file TFW - AFG3000 Series
          waveform file format IQT - RSA3000 Series waveform file format TIQ - RSA6000 Series
          waveform file format

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:IMPort value`` command.

    SCPI Syntax:
        ```
        - MMEMory:IMPort <wfm_name>,<filename>,<type>
        ```

    Info:
        - ``<wfm_name>,<filename>,<type>``
        - ``<wfm_name>`` ::=<string>.
        - ``<filename>`` ::=<string>.
        - ``<type>`` = {ISF\|TDS\|TXT\|TXT8\|TXT10\|TXT14\|WFM\|PAT\|TFW}.

    Properties:
        - ``.parameter``: The ``MMEMory:IMPort:PARameter`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._parameter = MmemoryImportParameter(device, f"{self._cmd_syntax}:PARameter")

    @property
    def parameter(self) -> MmemoryImportParameter:
        """Return the ``MMEMory:IMPort:PARameter`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:IMPort:PARameter?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:IMPort:PARameter?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frequency``: The ``MMEMory:IMPort:PARameter:FREQuency`` command tree.
            - ``.level``: The ``MMEMory:IMPort:PARameter:LEVel`` command tree.
            - ``.normalize``: The ``MMEMory:IMPort:PARameter:NORMalize`` command.
            - ``.resampling``: The ``MMEMory:IMPort:PARameter:RESampling`` command tree.
        """
        return self._parameter


class MmemoryExport(SCPICmdWrite):
    r"""The ``MMEMory:EXPort`` command.

    Description:
        - This command exports a waveform file from the arbitrary waveform generator setup. The
          supported file formats are: TXT - Text file with analog data TXT8 - Text file with 8-bit
          DAC resolution TXT10 - Text file with 10-bit DAC resolution TXT14 - Text file with 14-bit
          DAC resolution (AWG5000 Series only) WFM - AWG400/AWG500/AWG600/AWG700 Series waveform

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:EXPort value`` command.

    SCPI Syntax:
        ```
        - MMEMory:EXPort <wfm_name>,<filename>,<type>
        ```

    Info:
        - ``<wfm_name>,<filename>,<type>``
        - ``<wfm_name>`` ::=<string>.
        - ``<filename>`` ::=<string>.
        - ``<type>`` = {TXT\|TXT8\|TXT10\|TXT14\|WFM}.
    """


class MmemoryDelete(SCPICmdWrite):
    """The ``MMEMory:DELete`` command.

    Description:
        - This command deletes a file or directory from the AWG's hard disk. When used on a
          directory, this command succeeds only if the directory is empty.

    Usage:
        - Using the ``.write(value)`` method will send the ``MMEMory:DELete value`` command.

    SCPI Syntax:
        ```
        - MMEMory:DELete <file_name>[,<msus>]
        ```
    """


class MmemoryData(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``MMEMory:DATA`` command.

    Description:
        - This command and query sets or returns block data to/from the file in the current mass
          storage device. This command has a limit of 650,000,000 bytes of data. If this limit is
          insufficient, consider the following alternatives: Use a more efficient file encoding (WFM
          or PAT) when sending data. Use instrument commands for direct control
          (``WLIST:WAVEFORM:DATA``, FREQ, VOLT, and so on). Use Ethernet (ftp, http, or file
          sharing) to transfer the file.

    Usage:
        - Using the ``.query(argument)`` method will send the ``MMEMory:DATA? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``MMEMory:DATA? argument``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MMEMory:DATA value`` command.

    SCPI Syntax:
        ```
        - MMEMory:DATA <file_name>,<block_data>
        - MMEMory:DATA? <file_name>
        ```

    Info:
        - ``<file_name>`` , ``<block_data>``.
    """


class MmemoryCdirectory(SCPICmdWrite, SCPICmdRead):
    """The ``MMEMory:CDIRectory`` command.

    Description:
        - This command changes the current working directory in the mass storage system.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory:CDIRectory?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory:CDIRectory?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MMEMory:CDIRectory value`` command.

    SCPI Syntax:
        ```
        - MMEMory:CDIRectory [<directory_name>]
        - MMEMory:CDIRectory?
        ```
    """


class MmemoryCatalog(SCPICmdReadWithArguments):
    """The ``MMEMory:CATalog`` command.

    Description:
        - This command returns the current contents and state of the mass storage media.

    Usage:
        - Using the ``.query(argument)`` method will send the ``MMEMory:CATalog? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``MMEMory:CATalog? argument``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MMEMory:CATalog? [<msus>]
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Mmemory(SCPICmdRead):
    """The ``MMEMory`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MMEMory?`` query.
        - Using the ``.verify(value)`` method will send the ``MMEMory?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.catalog``: The ``MMEMory:CATalog`` command.
        - ``.cdirectory``: The ``MMEMory:CDIRectory`` command.
        - ``.data``: The ``MMEMory:DATA`` command.
        - ``.delete``: The ``MMEMory:DELete`` command.
        - ``.export``: The ``MMEMory:EXPort`` command.
        - ``.import``: The ``MMEMory:IMPort`` command.
        - ``.mdirectory``: The ``MMEMory:MDIRectory`` command.
        - ``.msis``: The ``MMEMory:MSIS`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MMEMory") -> None:
        super().__init__(device, cmd_syntax)
        self._catalog = MmemoryCatalog(device, f"{self._cmd_syntax}:CATalog")
        self._cdirectory = MmemoryCdirectory(device, f"{self._cmd_syntax}:CDIRectory")
        self._data = MmemoryData(device, f"{self._cmd_syntax}:DATA")
        self._delete = MmemoryDelete(device, f"{self._cmd_syntax}:DELete")
        self._export = MmemoryExport(device, f"{self._cmd_syntax}:EXPort")
        self._import = MmemoryImport(device, f"{self._cmd_syntax}:IMPort")
        self._mdirectory = MmemoryMdirectory(device, f"{self._cmd_syntax}:MDIRectory")
        self._msis = MmemoryMsis(device, f"{self._cmd_syntax}:MSIS")

    @property
    def catalog(self) -> MmemoryCatalog:
        """Return the ``MMEMory:CATalog`` command.

        Description:
            - This command returns the current contents and state of the mass storage media.

        Usage:
            - Using the ``.query(argument)`` method will send the ``MMEMory:CATalog? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MMEMory:CATalog? argument`` query and raise an AssertionError if the returned value
              does not match ``value``.

        SCPI Syntax:
            ```
            - MMEMory:CATalog? [<msus>]
            ```
        """
        return self._catalog

    @property
    def cdirectory(self) -> MmemoryCdirectory:
        """Return the ``MMEMory:CDIRectory`` command.

        Description:
            - This command changes the current working directory in the mass storage system.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:CDIRectory?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:CDIRectory?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MMEMory:CDIRectory value`` command.

        SCPI Syntax:
            ```
            - MMEMory:CDIRectory [<directory_name>]
            - MMEMory:CDIRectory?
            ```
        """
        return self._cdirectory

    @property
    def data(self) -> MmemoryData:
        """Return the ``MMEMory:DATA`` command.

        Description:
            - This command and query sets or returns block data to/from the file in the current mass
              storage device. This command has a limit of 650,000,000 bytes of data. If this limit
              is insufficient, consider the following alternatives: Use a more efficient file
              encoding (WFM or PAT) when sending data. Use instrument commands for direct control
              (``WLIST:WAVEFORM:DATA``, FREQ, VOLT, and so on). Use Ethernet (ftp, http, or file
              sharing) to transfer the file.

        Usage:
            - Using the ``.query(argument)`` method will send the ``MMEMory:DATA? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``MMEMory:DATA? argument``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MMEMory:DATA value`` command.

        SCPI Syntax:
            ```
            - MMEMory:DATA <file_name>,<block_data>
            - MMEMory:DATA? <file_name>
            ```

        Info:
            - ``<file_name>`` , ``<block_data>``.
        """
        return self._data

    @property
    def delete(self) -> MmemoryDelete:
        """Return the ``MMEMory:DELete`` command.

        Description:
            - This command deletes a file or directory from the AWG's hard disk. When used on a
              directory, this command succeeds only if the directory is empty.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:DELete value`` command.

        SCPI Syntax:
            ```
            - MMEMory:DELete <file_name>[,<msus>]
            ```
        """
        return self._delete

    @property
    def export(self) -> MmemoryExport:
        r"""Return the ``MMEMory:EXPort`` command.

        Description:
            - This command exports a waveform file from the arbitrary waveform generator setup. The
              supported file formats are: TXT - Text file with analog data TXT8 - Text file with
              8-bit DAC resolution TXT10 - Text file with 10-bit DAC resolution TXT14 - Text file
              with 14-bit DAC resolution (AWG5000 Series only) WFM - AWG400/AWG500/AWG600/AWG700
              Series waveform

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:EXPort value`` command.

        SCPI Syntax:
            ```
            - MMEMory:EXPort <wfm_name>,<filename>,<type>
            ```

        Info:
            - ``<wfm_name>,<filename>,<type>``
            - ``<wfm_name>`` ::=<string>.
            - ``<filename>`` ::=<string>.
            - ``<type>`` = {TXT\|TXT8\|TXT10\|TXT14\|WFM}.
        """
        return self._export

    @property
    def import_(self) -> MmemoryImport:
        r"""Return the ``MMEMory:IMPort`` command.

        Description:
            - This command imports a file into the arbitrary waveform generator's setup as a
              waveform. The supported file formats are: ISF - TDS3000 and DPO4000 waveform format
              TDS - TDS5000/TDS6000/TDS7000, DPO7000/DPO70000/DSA70000 Series waveform TXT - Text
              file with analog data TXT8 - Text file with 8-bit DAC resolution TXT10 - Text file
              with 10-bit DAC resolution TXT14 - Text file with 14-bit DAC resolution WFM -
              AWG400/AWG500/AWG600/AWG700 Series waveform PAT - AWG400/AWG500/AWG600/AWG700 Series
              pattern file TFW - AFG3000 Series waveform file format IQT - RSA3000 Series waveform
              file format TIQ - RSA6000 Series waveform file format

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:IMPort value`` command.

        SCPI Syntax:
            ```
            - MMEMory:IMPort <wfm_name>,<filename>,<type>
            ```

        Info:
            - ``<wfm_name>,<filename>,<type>``
            - ``<wfm_name>`` ::=<string>.
            - ``<filename>`` ::=<string>.
            - ``<type>`` = {ISF\|TDS\|TXT\|TXT8\|TXT10\|TXT14\|WFM\|PAT\|TFW}.

        Sub-properties:
            - ``.parameter``: The ``MMEMory:IMPort:PARameter`` command tree.
        """
        return self._import

    @property
    def mdirectory(self) -> MmemoryMdirectory:
        """Return the ``MMEMory:MDIRectory`` command.

        Description:
            - This command creates a directory in the mass storage system. If the specified
              directory is locked in the mass storage system, this command causes an error.

        Usage:
            - Using the ``.write(value)`` method will send the ``MMEMory:MDIRectory value`` command.

        SCPI Syntax:
            ```
            - MMEMory:MDIRectory <directory_name>
            ```
        """
        return self._mdirectory

    @property
    def msis(self) -> MmemoryMsis:
        """Return the ``MMEMory:MSIS`` command.

        Description:
            - This command selects or returns a mass storage device used by all MMEMory commands.
              <msus> specifies a drive using a drive letter. The drive letter can represent hard
              disk drives, network drives, external DVD/CD-RW drives, or USB memory.

        Usage:
            - Using the ``.query()`` method will send the ``MMEMory:MSIS?`` query.
            - Using the ``.verify(value)`` method will send the ``MMEMory:MSIS?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MMEMory:MSIS value`` command.

        SCPI Syntax:
            ```
            - MMEMory:MSIS [<msus>]
            - MMEMory:MSIS?
            ```
        """
        return self._msis
