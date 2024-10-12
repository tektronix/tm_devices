"""The slist commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SLISt:NAME? <Index>
    - SLISt:SIZE?
    - SLISt:SUBSequence:DELete {<subseq_name>|ALL}
    - SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt <subseq_name>,<NR1>
    - SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt? <subseq_name>
    - SLISt:SUBSequence:ELEMent[n]:WAVeform[n] <subseq_name>,<wfm_name>
    - SLISt:SUBSequence:ELEMent[n]:WAVeform[n]? <subseq_name>
    - SLISt:SUBSequence:LENGth <subseq_name>,<NR1>
    - SLISt:SUBSequence:LENGth? <subseq_name>
    - SLISt:SUBSequence:NEW <subseq_name>,<length>
    - SLISt:SUBSequence:TSTamp? <subseq_name>
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


class SlistSubsequenceTstamp(SCPICmdReadWithArguments):
    """The ``SLISt:SUBSequence:TSTamp`` command.

    Description:
        - This query returns the time stamp of the subsequence. Time stamp is updated whenever the
          subsequence is created or changed. It is not updated when it is renamed. It returns date
          as a string in the form 'yyyy/mm/dd ``hh:mm:ss``' (a white space between data and time).

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:SUBSequence:TSTamp? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SUBSequence:TSTamp? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SUBSequence:TSTamp? <subseq_name>
        ```

    Info:
        - ``<subseq_name>`` ::=<string>.
    """


class SlistSubsequenceNew(SCPICmdWrite):
    """The ``SLISt:SUBSequence:NEW`` command.

    Description:
        - This command creates a new subsequence.

    Usage:
        - Using the ``.write(value)`` method will send the ``SLISt:SUBSequence:NEW value`` command.

    SCPI Syntax:
        ```
        - SLISt:SUBSequence:NEW <subseq_name>,<length>
        ```

    Info:
        - ``<subseq_name>`` ::=<string>.
    """


class SlistSubsequenceLength(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SUBSequence:LENGth`` command.

    Description:
        - This command and query sets or returns the size of the subsequence.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:SUBSequence:LENGth? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SUBSequence:LENGth? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SUBSequence:LENGth value``
          command.

    SCPI Syntax:
        ```
        - SLISt:SUBSequence:LENGth <subseq_name>,<NR1>
        - SLISt:SUBSequence:LENGth? <subseq_name>
        ```

    Info:
        - ``<subseq_name>`` ::=<string>.
    """


class SlistSubsequenceElementItemWaveformItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdReadWithArguments
):
    """The ``SLISt:SUBSequence:ELEMent[n]:WAVeform[n]`` command.

    Description:
        - This command and query sets or returns the waveform for an element of the subsequence. The
          value of n = 1 | 2 | 3 | 4 based on the model. If suffix is not specified, the value of n
          is 1. The value of 'n' indicates which channel will output the waveform when the sequence
          is run.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SUBSequence:ELEMent[n]:WAVeform[n]? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SUBSequence:ELEMent[n]:WAVeform[n]? argument`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SLISt:SUBSequence:ELEMent[n]:WAVeform[n] value`` command.

    SCPI Syntax:
        ```
        - SLISt:SUBSequence:ELEMent[n]:WAVeform[n] <subseq_name>,<wfm_name>
        - SLISt:SUBSequence:ELEMent[n]:WAVeform[n]? <subseq_name>
        ```

    Info:
        - ``<subseq_name>`` ::=<string>.
        - ``<wfm_name>`` ::=<string>.
    """


class SlistSubsequenceElementItemLoopCount(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt`` command.

    Description:
        - This command and query sets or returns the loop count for the specified subsequence
          element. The loop count is an integer.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt value`` command.

    SCPI Syntax:
        ```
        - SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt <subseq_name>,<NR1>
        - SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt? <subseq_name>
        ```
    """


class SlistSubsequenceElementItemLoop(SCPICmdRead):
    """The ``SLISt:SUBSequence:ELEMent[n]:LOOP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SUBSequence:ELEMent[n]:LOOP?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SUBSequence:ELEMent[n]:LOOP?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.count``: The ``SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = SlistSubsequenceElementItemLoopCount(device, f"{self._cmd_syntax}:COUNt")

    @property
    def count(self) -> SlistSubsequenceElementItemLoopCount:
        """Return the ``SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt`` command.

        Description:
            - This command and query sets or returns the loop count for the specified subsequence
              element. The loop count is an integer.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt value`` command.

        SCPI Syntax:
            ```
            - SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt <subseq_name>,<NR1>
            - SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt? <subseq_name>
            ```
        """
        return self._count


class SlistSubsequenceElementItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SLISt:SUBSequence:ELEMent[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SUBSequence:ELEMent[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SUBSequence:ELEMent[n]?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.loop``: The ``SLISt:SUBSequence:ELEMent[n]:LOOP`` command tree.
        - ``.waveform``: The ``SLISt:SUBSequence:ELEMent[n]:WAVeform[n]`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._loop = SlistSubsequenceElementItemLoop(device, f"{self._cmd_syntax}:LOOP")
        self._waveform: Dict[int, SlistSubsequenceElementItemWaveformItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: SlistSubsequenceElementItemWaveformItem(
                    device, f"{self._cmd_syntax}:WAVeform{x}"
                )
            )
        )

    @property
    def loop(self) -> SlistSubsequenceElementItemLoop:
        """Return the ``SLISt:SUBSequence:ELEMent[n]:LOOP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SUBSequence:ELEMent[n]:LOOP?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SLISt:SUBSequence:ELEMent[n]:LOOP?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.count``: The ``SLISt:SUBSequence:ELEMent[n]:LOOP:COUNt`` command.
        """
        return self._loop

    @property
    def waveform(self) -> Dict[int, SlistSubsequenceElementItemWaveformItem]:
        """Return the ``SLISt:SUBSequence:ELEMent[n]:WAVeform[n]`` command.

        Description:
            - This command and query sets or returns the waveform for an element of the subsequence.
              The value of n = 1 | 2 | 3 | 4 based on the model. If suffix is not specified, the
              value of n is 1. The value of 'n' indicates which channel will output the waveform
              when the sequence is run.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SUBSequence:ELEMent[n]:WAVeform[n]? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SUBSequence:ELEMent[n]:WAVeform[n]? argument`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SUBSequence:ELEMent[n]:WAVeform[n] value`` command.

        SCPI Syntax:
            ```
            - SLISt:SUBSequence:ELEMent[n]:WAVeform[n] <subseq_name>,<wfm_name>
            - SLISt:SUBSequence:ELEMent[n]:WAVeform[n]? <subseq_name>
            ```

        Info:
            - ``<subseq_name>`` ::=<string>.
            - ``<wfm_name>`` ::=<string>.
        """
        return self._waveform


class SlistSubsequenceDelete(SCPICmdWrite):
    """The ``SLISt:SUBSequence:DELete`` command.

    Description:
        - This command deletes the subsequence from the currently loaded setup.

    Usage:
        - Using the ``.write(value)`` method will send the ``SLISt:SUBSequence:DELete value``
          command.

    SCPI Syntax:
        ```
        - SLISt:SUBSequence:DELete {<subseq_name>|ALL}
        ```

    Info:
        - ``<subseq_name>`` ::=<string>.
    """


class SlistSubsequence(SCPICmdRead):
    """The ``SLISt:SUBSequence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SUBSequence?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SUBSequence?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delete``: The ``SLISt:SUBSequence:DELete`` command.
        - ``.element``: The ``SLISt:SUBSequence:ELEMent[n]`` command tree.
        - ``.length``: The ``SLISt:SUBSequence:LENGth`` command.
        - ``.new``: The ``SLISt:SUBSequence:NEW`` command.
        - ``.tstamp``: The ``SLISt:SUBSequence:TSTamp`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delete = SlistSubsequenceDelete(device, f"{self._cmd_syntax}:DELete")
        self._element: Dict[int, SlistSubsequenceElementItem] = DefaultDictPassKeyToFactory(
            lambda x: SlistSubsequenceElementItem(device, f"{self._cmd_syntax}:ELEMent{x}")
        )
        self._length = SlistSubsequenceLength(device, f"{self._cmd_syntax}:LENGth")
        self._new = SlistSubsequenceNew(device, f"{self._cmd_syntax}:NEW")
        self._tstamp = SlistSubsequenceTstamp(device, f"{self._cmd_syntax}:TSTamp")

    @property
    def delete(self) -> SlistSubsequenceDelete:
        """Return the ``SLISt:SUBSequence:DELete`` command.

        Description:
            - This command deletes the subsequence from the currently loaded setup.

        Usage:
            - Using the ``.write(value)`` method will send the ``SLISt:SUBSequence:DELete value``
              command.

        SCPI Syntax:
            ```
            - SLISt:SUBSequence:DELete {<subseq_name>|ALL}
            ```

        Info:
            - ``<subseq_name>`` ::=<string>.
        """
        return self._delete

    @property
    def element(self) -> Dict[int, SlistSubsequenceElementItem]:
        """Return the ``SLISt:SUBSequence:ELEMent[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SUBSequence:ELEMent[n]?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SUBSequence:ELEMent[n]?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.loop``: The ``SLISt:SUBSequence:ELEMent[n]:LOOP`` command tree.
            - ``.waveform``: The ``SLISt:SUBSequence:ELEMent[n]:WAVeform[n]`` command.
        """
        return self._element

    @property
    def length(self) -> SlistSubsequenceLength:
        """Return the ``SLISt:SUBSequence:LENGth`` command.

        Description:
            - This command and query sets or returns the size of the subsequence.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SUBSequence:LENGth? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SUBSequence:LENGth? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SLISt:SUBSequence:LENGth value``
              command.

        SCPI Syntax:
            ```
            - SLISt:SUBSequence:LENGth <subseq_name>,<NR1>
            - SLISt:SUBSequence:LENGth? <subseq_name>
            ```

        Info:
            - ``<subseq_name>`` ::=<string>.
        """
        return self._length

    @property
    def new(self) -> SlistSubsequenceNew:
        """Return the ``SLISt:SUBSequence:NEW`` command.

        Description:
            - This command creates a new subsequence.

        Usage:
            - Using the ``.write(value)`` method will send the ``SLISt:SUBSequence:NEW value``
              command.

        SCPI Syntax:
            ```
            - SLISt:SUBSequence:NEW <subseq_name>,<length>
            ```

        Info:
            - ``<subseq_name>`` ::=<string>.
        """
        return self._new

    @property
    def tstamp(self) -> SlistSubsequenceTstamp:
        """Return the ``SLISt:SUBSequence:TSTamp`` command.

        Description:
            - This query returns the time stamp of the subsequence. Time stamp is updated whenever
              the subsequence is created or changed. It is not updated when it is renamed. It
              returns date as a string in the form 'yyyy/mm/dd ``hh:mm:ss``' (a white space between
              data and time).

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SUBSequence:TSTamp? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SUBSequence:TSTamp? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SUBSequence:TSTamp? <subseq_name>
            ```

        Info:
            - ``<subseq_name>`` ::=<string>.
        """
        return self._tstamp


class SlistSize(SCPICmdRead):
    """The ``SLISt:SIZE`` command.

    Description:
        - This command returns the number sequences in sequence list.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SIZE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SIZE?
        ```
    """


class SlistName(SCPICmdReadWithArguments):
    """The ``SLISt:NAME`` command.

    Description:
        - The query returns the name of the subsequence corresponding to the specified index in the
          subsequence list.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:NAME? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``SLISt:NAME? argument`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:NAME? <Index>
        ```

    Info:
        - ``<Index>`` ::=<NR1>.
    """


class Slist(SCPICmdRead):
    """The ``SLISt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.name``: The ``SLISt:NAME`` command.
        - ``.size``: The ``SLISt:SIZE`` command.
        - ``.subsequence``: The ``SLISt:SUBSequence`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SLISt") -> None:
        super().__init__(device, cmd_syntax)
        self._name = SlistName(device, f"{self._cmd_syntax}:NAME")
        self._size = SlistSize(device, f"{self._cmd_syntax}:SIZE")
        self._subsequence = SlistSubsequence(device, f"{self._cmd_syntax}:SUBSequence")

    @property
    def name(self) -> SlistName:
        """Return the ``SLISt:NAME`` command.

        Description:
            - The query returns the name of the subsequence corresponding to the specified index in
              the subsequence list.

        Usage:
            - Using the ``.query(argument)`` method will send the ``SLISt:NAME? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``SLISt:NAME? argument``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:NAME? <Index>
            ```

        Info:
            - ``<Index>`` ::=<NR1>.
        """
        return self._name

    @property
    def size(self) -> SlistSize:
        """Return the ``SLISt:SIZE`` command.

        Description:
            - This command returns the number sequences in sequence list.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SIZE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SIZE?
            ```
        """
        return self._size

    @property
    def subsequence(self) -> SlistSubsequence:
        """Return the ``SLISt:SUBSequence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SUBSequence?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SUBSequence?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delete``: The ``SLISt:SUBSequence:DELete`` command.
            - ``.element``: The ``SLISt:SUBSequence:ELEMent[n]`` command tree.
            - ``.length``: The ``SLISt:SUBSequence:LENGth`` command.
            - ``.new``: The ``SLISt:SUBSequence:NEW`` command.
            - ``.tstamp``: The ``SLISt:SUBSequence:TSTamp`` command.
        """
        return self._subsequence
