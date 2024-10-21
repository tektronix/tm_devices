"""The wlist commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - WLISt:NAME? <Index>
    - WLISt:SIZE?
    - WLISt:WAVeform:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
    - WLISt:WAVeform:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
    - WLISt:WAVeform:DELete {<wfm_name>|ALL}
    - WLISt:WAVeform:LENGth? <wfm_name>
    - WLISt:WAVeform:MARKer:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
    - WLISt:WAVeform:MARKer:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
    - WLISt:WAVeform:NEW <wfm_name>,<Size>,<Type>
    - WLISt:WAVeform:NORMalize <wfm_name>,<Type>
    - WLISt:WAVeform:PREDefined? <wfm_name>
    - WLISt:WAVeform:RESAmple <wfm_name>,<Size>
    - WLISt:WAVeform:TSTamp? <wfm_name>
    - WLISt:WAVeform:TYPE? <wfm_name>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class WlistWaveformType(SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:TYPE`` command.

    Description:
        - This command returns the type of the waveform.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:TYPE? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:TYPE? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:TYPE? <wfm_name>
        ```

    Info:
        - ``<wfm_name>`` ::= <string>.
    """


class WlistWaveformTstamp(SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:TSTamp`` command.

    Description:
        - This command returns the timestamp of the specified waveform in the waveform list.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:TSTamp? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:TSTamp? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:TSTamp? <wfm_name>
        ```
    """


class WlistWaveformResample(SCPICmdWrite):
    """The ``WLISt:WAVeform:RESAmple`` command.

    Description:
        - This command resamples a waveform that exists in the waveform list of the current setup.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:RESAmple value``
          command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:RESAmple <wfm_name>,<Size>
        ```
    """


class WlistWaveformPredefined(SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:PREDefined`` command.

    Description:
        - This query returns true or false based on whether the waveform is predefined.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``WLISt:WAVeform:PREDefined? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:PREDefined? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:PREDefined? <wfm_name>
        ```

    Info:
        - ``<wfm_name>`` ::=<string>.
    """


class WlistWaveformNormalize(SCPICmdWrite):
    r"""The ``WLISt:WAVeform:NORMalize`` command.

    Description:
        - This command normalizes a waveform that exists in the waveform list of the current setup.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:NORMalize value``
          command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:NORMalize <wfm_name>,<Type>
        ```

    Info:
        - ``<wfm_name>`` ::=<string>.
        - ``<Type>`` ::={FSCale\|ZREFerence}.
    """


class WlistWaveformNew(SCPICmdWrite):
    r"""The ``WLISt:WAVeform:NEW`` command.

    Description:
        - This command creates a new empty waveform in the waveform list of current setup.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:NEW value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:NEW <wfm_name>,<Size>,<Type>
        ```

    Info:
        - ``<wfm_name>`` ::=<string>.
        - ``<Size>`` ::=<NR1>.
        - ``<Type>`` ::={REAL\|INTeger}.
    """


class WlistWaveformMarkerData(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:MARKer:DATA`` command.

    Description:
        - This command sets or returns the waveform marker data. This command has a limit of
          999,999,999 bytes of data. If this limit is insufficient, consider the following
          alternatives: Send a more efficient file format using ``MMEM:DATA``. Use Ethernet (ftp,
          http, or file sharing) to transfer the file.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``WLISt:WAVeform:MARKer:DATA? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:MARKer:DATA? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:MARKer:DATA value``
          command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:MARKer:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
        - WLISt:WAVeform:MARKer:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
        ```
    """


class WlistWaveformMarker(SCPICmdRead):
    """The ``WLISt:WAVeform:MARKer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform:MARKer?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:MARKer?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.data``: The ``WLISt:WAVeform:MARKer:DATA`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = WlistWaveformMarkerData(device, f"{self._cmd_syntax}:DATA")

    @property
    def data(self) -> WlistWaveformMarkerData:
        """Return the ``WLISt:WAVeform:MARKer:DATA`` command.

        Description:
            - This command sets or returns the waveform marker data. This command has a limit of
              999,999,999 bytes of data. If this limit is insufficient, consider the following
              alternatives: Send a more efficient file format using ``MMEM:DATA``. Use Ethernet
              (ftp, http, or file sharing) to transfer the file.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:MARKer:DATA? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:MARKer:DATA? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:MARKer:DATA value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:MARKer:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
            - WLISt:WAVeform:MARKer:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
            ```
        """
        return self._data


class WlistWaveformLength(SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:LENGth`` command.

    Description:
        - This command returns the size of the specified waveform in the waveform list. The returned
          value represents data points (not bytes).

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:LENGth? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:LENGth? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:LENGth? <wfm_name>
        ```
    """


class WlistWaveformDelete(SCPICmdWrite):
    """The ``WLISt:WAVeform:DELete`` command.

    Description:
        - This command deletes a single waveform from the waveform list or all waveforms. If the
          deleted waveform is currently loaded into waveform memory, it is unloaded. If the RUN
          state of the AWG is ON, the state is turned OFF. If the channel is on, it will be switched
          off.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DELete value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:DELete {<wfm_name>|ALL}
        ```
    """


class WlistWaveformData(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:DATA`` command.

    Description:
        - This command transfers waveform data from the external controller into the waveform list
          or from the waveform list to the external control program. This command has a limit of
          650,000,000 bytes of data. If this limit is insufficient, consider the following
          alternatives: Use a more efficient file encoding (WFM or PAT) when sending data. Use
          instrument commands for direct control (``WLIST:WAVEFORM:DATA``, FREQ, VOLT, and so on).
          Use Ethernet (ftp, http, or file sharing) to transfer the file. Refer to the User Online
          Help, AWG Reference > Waveform General Information section for the detailed format
          specification.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:DATA? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:DATA? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DATA value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
        - WLISt:WAVeform:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
        ```

    Info:
        - ``StartIndex, Size,<block_data>``
        - ``<wfm_name>`` ::=<string>.
        - ``<StartIndex>`` ::=<NR1>.
        - ``<Size>`` ::=<NR1>.
        - ``<block_data>`` ::=<IEEE 488.2 block>.
    """


#  pylint: disable=too-many-instance-attributes
class WlistWaveform(SCPICmdRead):
    """The ``WLISt:WAVeform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.data``: The ``WLISt:WAVeform:DATA`` command.
        - ``.delete``: The ``WLISt:WAVeform:DELete`` command.
        - ``.length``: The ``WLISt:WAVeform:LENGth`` command.
        - ``.marker``: The ``WLISt:WAVeform:MARKer`` command tree.
        - ``.new``: The ``WLISt:WAVeform:NEW`` command.
        - ``.normalize``: The ``WLISt:WAVeform:NORMalize`` command.
        - ``.predefined``: The ``WLISt:WAVeform:PREDefined`` command.
        - ``.resample``: The ``WLISt:WAVeform:RESAmple`` command.
        - ``.tstamp``: The ``WLISt:WAVeform:TSTamp`` command.
        - ``.type``: The ``WLISt:WAVeform:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = WlistWaveformData(device, f"{self._cmd_syntax}:DATA")
        self._delete = WlistWaveformDelete(device, f"{self._cmd_syntax}:DELete")
        self._length = WlistWaveformLength(device, f"{self._cmd_syntax}:LENGth")
        self._marker = WlistWaveformMarker(device, f"{self._cmd_syntax}:MARKer")
        self._new = WlistWaveformNew(device, f"{self._cmd_syntax}:NEW")
        self._normalize = WlistWaveformNormalize(device, f"{self._cmd_syntax}:NORMalize")
        self._predefined = WlistWaveformPredefined(device, f"{self._cmd_syntax}:PREDefined")
        self._resample = WlistWaveformResample(device, f"{self._cmd_syntax}:RESAmple")
        self._tstamp = WlistWaveformTstamp(device, f"{self._cmd_syntax}:TSTamp")
        self._type = WlistWaveformType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def data(self) -> WlistWaveformData:
        """Return the ``WLISt:WAVeform:DATA`` command.

        Description:
            - This command transfers waveform data from the external controller into the waveform
              list or from the waveform list to the external control program. This command has a
              limit of 650,000,000 bytes of data. If this limit is insufficient, consider the
              following alternatives: Use a more efficient file encoding (WFM or PAT) when sending
              data. Use instrument commands for direct control (``WLIST:WAVEFORM:DATA``, FREQ, VOLT,
              and so on). Use Ethernet (ftp, http, or file sharing) to transfer the file. Refer to
              the User Online Help, AWG Reference > Waveform General Information section for the
              detailed format specification.

        Usage:
            - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:DATA? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:DATA? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DATA value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
            - WLISt:WAVeform:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
            ```

        Info:
            - ``StartIndex, Size,<block_data>``
            - ``<wfm_name>`` ::=<string>.
            - ``<StartIndex>`` ::=<NR1>.
            - ``<Size>`` ::=<NR1>.
            - ``<block_data>`` ::=<IEEE 488.2 block>.
        """
        return self._data

    @property
    def delete(self) -> WlistWaveformDelete:
        """Return the ``WLISt:WAVeform:DELete`` command.

        Description:
            - This command deletes a single waveform from the waveform list or all waveforms. If the
              deleted waveform is currently loaded into waveform memory, it is unloaded. If the RUN
              state of the AWG is ON, the state is turned OFF. If the channel is on, it will be
              switched off.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DELete value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:DELete {<wfm_name>|ALL}
            ```
        """
        return self._delete

    @property
    def length(self) -> WlistWaveformLength:
        """Return the ``WLISt:WAVeform:LENGth`` command.

        Description:
            - This command returns the size of the specified waveform in the waveform list. The
              returned value represents data points (not bytes).

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:LENGth? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:LENGth? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:LENGth? <wfm_name>
            ```
        """
        return self._length

    @property
    def marker(self) -> WlistWaveformMarker:
        """Return the ``WLISt:WAVeform:MARKer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:WAVeform:MARKer?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:MARKer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``WLISt:WAVeform:MARKer:DATA`` command.
        """
        return self._marker

    @property
    def new(self) -> WlistWaveformNew:
        r"""Return the ``WLISt:WAVeform:NEW`` command.

        Description:
            - This command creates a new empty waveform in the waveform list of current setup.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:NEW value`` command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:NEW <wfm_name>,<Size>,<Type>
            ```

        Info:
            - ``<wfm_name>`` ::=<string>.
            - ``<Size>`` ::=<NR1>.
            - ``<Type>`` ::={REAL\|INTeger}.
        """
        return self._new

    @property
    def normalize(self) -> WlistWaveformNormalize:
        r"""Return the ``WLISt:WAVeform:NORMalize`` command.

        Description:
            - This command normalizes a waveform that exists in the waveform list of the current
              setup.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:NORMalize value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:NORMalize <wfm_name>,<Type>
            ```

        Info:
            - ``<wfm_name>`` ::=<string>.
            - ``<Type>`` ::={FSCale\|ZREFerence}.
        """
        return self._normalize

    @property
    def predefined(self) -> WlistWaveformPredefined:
        """Return the ``WLISt:WAVeform:PREDefined`` command.

        Description:
            - This query returns true or false based on whether the waveform is predefined.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:PREDefined? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:PREDefined? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:PREDefined? <wfm_name>
            ```

        Info:
            - ``<wfm_name>`` ::=<string>.
        """
        return self._predefined

    @property
    def resample(self) -> WlistWaveformResample:
        """Return the ``WLISt:WAVeform:RESAmple`` command.

        Description:
            - This command resamples a waveform that exists in the waveform list of the current
              setup.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:RESAmple value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:RESAmple <wfm_name>,<Size>
            ```
        """
        return self._resample

    @property
    def tstamp(self) -> WlistWaveformTstamp:
        """Return the ``WLISt:WAVeform:TSTamp`` command.

        Description:
            - This command returns the timestamp of the specified waveform in the waveform list.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:TSTamp? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:TSTamp? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:TSTamp? <wfm_name>
            ```
        """
        return self._tstamp

    @property
    def type(self) -> WlistWaveformType:
        """Return the ``WLISt:WAVeform:TYPE`` command.

        Description:
            - This command returns the type of the waveform.

        Usage:
            - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:TYPE? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:TYPE? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:TYPE? <wfm_name>
            ```

        Info:
            - ``<wfm_name>`` ::= <string>.
        """
        return self._type


class WlistSize(SCPICmdRead):
    """The ``WLISt:SIZE`` command.

    Description:
        - This command returns the number of waveforms in the waveform list.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SIZE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:SIZE?
        ```
    """


class WlistName(SCPICmdReadWithArguments):
    """The ``WLISt:NAME`` command.

    Description:
        - This command returns the waveform name from the waveform list at the position specified by
          the index value.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:NAME? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``WLISt:NAME? argument`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:NAME? <Index>
        ```
    """


class Wlist(SCPICmdRead):
    """The ``WLISt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.name``: The ``WLISt:NAME`` command.
        - ``.size``: The ``WLISt:SIZE`` command.
        - ``.waveform``: The ``WLISt:WAVeform`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "WLISt") -> None:
        super().__init__(device, cmd_syntax)
        self._name = WlistName(device, f"{self._cmd_syntax}:NAME")
        self._size = WlistSize(device, f"{self._cmd_syntax}:SIZE")
        self._waveform = WlistWaveform(device, f"{self._cmd_syntax}:WAVeform")

    @property
    def name(self) -> WlistName:
        """Return the ``WLISt:NAME`` command.

        Description:
            - This command returns the waveform name from the waveform list at the position
              specified by the index value.

        Usage:
            - Using the ``.query(argument)`` method will send the ``WLISt:NAME? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``WLISt:NAME? argument``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:NAME? <Index>
            ```
        """
        return self._name

    @property
    def size(self) -> WlistSize:
        """Return the ``WLISt:SIZE`` command.

        Description:
            - This command returns the number of waveforms in the waveform list.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:SIZE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:SIZE?
            ```
        """
        return self._size

    @property
    def waveform(self) -> WlistWaveform:
        """Return the ``WLISt:WAVeform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:WAVeform?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``WLISt:WAVeform:DATA`` command.
            - ``.delete``: The ``WLISt:WAVeform:DELete`` command.
            - ``.length``: The ``WLISt:WAVeform:LENGth`` command.
            - ``.marker``: The ``WLISt:WAVeform:MARKer`` command tree.
            - ``.new``: The ``WLISt:WAVeform:NEW`` command.
            - ``.normalize``: The ``WLISt:WAVeform:NORMalize`` command.
            - ``.predefined``: The ``WLISt:WAVeform:PREDefined`` command.
            - ``.resample``: The ``WLISt:WAVeform:RESAmple`` command.
            - ``.tstamp``: The ``WLISt:WAVeform:TSTamp`` command.
            - ``.type``: The ``WLISt:WAVeform:TYPE`` command.
        """
        return self._waveform
