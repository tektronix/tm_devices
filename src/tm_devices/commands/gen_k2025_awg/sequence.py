"""The sequence commands module.

These commands are used in the following models:
AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SEQuence:ELEMent[n]:GOTO:INDex <target>
    - SEQuence:ELEMent[n]:GOTO:INDex?
    - SEQuence:ELEMent[n]:GOTO:STATe <goto_state>
    - SEQuence:ELEMent[n]:GOTO:STATe?
    - SEQuence:ELEMent[n]:JTARget:INDex <target>
    - SEQuence:ELEMent[n]:JTARget:INDex?
    - SEQuence:ELEMent[n]:JTARget:TYPE {INDex|NEXT|OFF}
    - SEQuence:ELEMent[n]:JTARget:TYPE?
    - SEQuence:ELEMent[n]:LOOP:COUNt <NR1>
    - SEQuence:ELEMent[n]:LOOP:COUNt?
    - SEQuence:ELEMent[n]:LOOP:INFinite <loop_state>
    - SEQuence:ELEMent[n]:LOOP:INFinite?
    - SEQuence:ELEMent[n]:SUBSequence <subseq_name>
    - SEQuence:ELEMent[n]:SUBSequence?
    - SEQuence:ELEMent[n]:TWAit <Boolean>
    - SEQuence:ELEMent[n]:TWAit?
    - SEQuence:ELEMent[n]:WAVeform[m] [1|2|3|4] <wfm_name>
    - SEQuence:ELEMent[n]:WAVeform[m]? [1|2|3|4]
    - SEQuence:JUMP:IMMediate <target>
    - SEQuence:LENGth <NR1>
    - SEQuence:LENGth?
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


class SequenceLength(SCPICmdWrite, SCPICmdRead):
    """The ``SEQuence:LENGth`` command.

    Description:
        - This command and query sets or returns the sequence length. Use this command to create an
          uninitialized sequence. You can also use the command to clear all sequence elements in a
          single action by passing 0 as the parameter. However, this action cannot be undone so
          exercise necessary caution. Also note that passing a value less than the sequence's
          current length will cause some sequence elements to be deleted at the end of the sequence.
          For example if ``SEQuence:LENGth?`` returns 200 and you subsequently send
          ``SEQuence:LENGth 21``, all sequence elements except the first 20 will be deleted.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:LENGth?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:LENGth?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEQuence:LENGth value`` command.

    SCPI Syntax:
        ```
        - SEQuence:LENGth <NR1>
        - SEQuence:LENGth?
        ```

    Info:
        - ``<NR1>``
    """


class SequenceJumpImmediate(SCPICmdWrite):
    """The ``SEQuence:JUMP:IMMediate`` command.

    Description:
        - This command forces the sequencer to jump to the specified element index. This is called a
          Force jump. This command does not require an event for executing the jump. Also, the Jump
          target specified for event jump is not used here.

    Usage:
        - Using the ``.write(value)`` method will send the ``SEQuence:JUMP:IMMediate value``
          command.

    SCPI Syntax:
        ```
        - SEQuence:JUMP:IMMediate <target>
        ```

    Info:
        - ``<target>`` ::=<NR1>.
    """


class SequenceJump(SCPICmdRead):
    """The ``SEQuence:JUMP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:JUMP?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:JUMP?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``SEQuence:JUMP:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = SequenceJumpImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> SequenceJumpImmediate:
        """Return the ``SEQuence:JUMP:IMMediate`` command.

        Description:
            - This command forces the sequencer to jump to the specified element index. This is
              called a Force jump. This command does not require an event for executing the jump.
              Also, the Jump target specified for event jump is not used here.

        Usage:
            - Using the ``.write(value)`` method will send the ``SEQuence:JUMP:IMMediate value``
              command.

        SCPI Syntax:
            ```
            - SEQuence:JUMP:IMMediate <target>
            ```

        Info:
            - ``<target>`` ::=<NR1>.
        """
        return self._immediate


class SequenceElementItemWaveformItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdReadWithArguments
):
    """The ``SEQuence:ELEMent[n]:WAVeform[m]`` command.

    Description:
        - This command and query sets or returns the waveform for a sequence element.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SEQuence:ELEMent[n]:WAVeform[m]? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SEQuence:ELEMent[n]:WAVeform[m]? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEQuence:ELEMent[n]:WAVeform[m] value``
          command.

    SCPI Syntax:
        ```
        - SEQuence:ELEMent[n]:WAVeform[m] [1|2|3|4] <wfm_name>
        - SEQuence:ELEMent[n]:WAVeform[m]? [1|2|3|4]
        ```

    Info:
        - ``<wfm_name`` >::=<string>.
    """


class SequenceElementItemTwait(SCPICmdWrite, SCPICmdRead):
    """The ``SEQuence:ELEMent[n]:TWAit`` command.

    Description:
        - This command and query sets or returns the wait trigger state for an element. Send a
          trigger signal in one of the following ways: By using an external trigger signal. By
          pressing the 'Force Trigger' button on the front panel. By sending the ``*TRG`` remote
          command.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:TWAit?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:TWAit?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEQuence:ELEMent[n]:TWAit value``
          command.

    SCPI Syntax:
        ```
        - SEQuence:ELEMent[n]:TWAit <Boolean>
        - SEQuence:ELEMent[n]:TWAit?
        ```

    Info:
        - ``<wait_trigger_state>`` ::=<Boolean>.
        - ``0`` indicates OFF.
        - ``1`` indicates ON.
    """


class SequenceElementItemSubsequence(SCPICmdWrite, SCPICmdRead):
    """The ``SEQuence:ELEMent[n]:SUBSequence`` command.

    Description:
        - This command and query sets or returns the subsequence for a sequence element. The
          AWG5012B, AWG5000C, and AWG7000C (option 09) series instruments support Subsequence. The
          subsequence name can be a null string (''). When a waveform is assigned to this sequence,
          the command returns ''.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:SUBSequence?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:SUBSequence?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEQuence:ELEMent[n]:SUBSequence value``
          command.

    SCPI Syntax:
        ```
        - SEQuence:ELEMent[n]:SUBSequence <subseq_name>
        - SEQuence:ELEMent[n]:SUBSequence?
        ```

    Info:
        - ``<subseq_name>`` ::=<string>.
    """


class SequenceElementItemLoopInfinite(SCPICmdWrite, SCPICmdRead):
    """The ``SEQuence:ELEMent[n]:LOOP:INFinite`` command.

    Description:
        - This command and query sets or returns the infinite looping state for a sequence element.
          When an infinite loop is set on an element, the sequencer continuously executes that
          element. To break the infinite loop, either issue the ``AWGCONTROL:STOP:IMMEDIATE``
          command or change the run mode to Continuous by using ``AWGCONTROL:RMODE`` command.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:LOOP:INFinite?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:LOOP:INFinite?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEQuence:ELEMent[n]:LOOP:INFinite value`` command.

    SCPI Syntax:
        ```
        - SEQuence:ELEMent[n]:LOOP:INFinite <loop_state>
        - SEQuence:ELEMent[n]:LOOP:INFinite?
        ```

    Info:
        - ``<loop_state>`` ::=<Boolean>.
        - ``0`` indicates OFF.
        - ``1`` indicates ON.
    """


class SequenceElementItemLoopCount(SCPICmdWrite, SCPICmdRead):
    """The ``SEQuence:ELEMent[n]:LOOP:COUNt`` command.

    Description:
        - This command and query sets or returns the loop count. Loop count setting for an element
          is ignored if ``SEQUENCE:ELEMENTN:LOOP:INFINITE`` is set to ON.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:LOOP:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:LOOP:COUNt?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEQuence:ELEMent[n]:LOOP:COUNt value``
          command.

    SCPI Syntax:
        ```
        - SEQuence:ELEMent[n]:LOOP:COUNt <NR1>
        - SEQuence:ELEMent[n]:LOOP:COUNt?
        ```

    Info:
        - ``<NR1>``
    """


class SequenceElementItemLoop(SCPICmdRead):
    """The ``SEQuence:ELEMent[n]:LOOP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:LOOP?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:LOOP?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.count``: The ``SEQuence:ELEMent[n]:LOOP:COUNt`` command.
        - ``.infinite``: The ``SEQuence:ELEMent[n]:LOOP:INFinite`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = SequenceElementItemLoopCount(device, f"{self._cmd_syntax}:COUNt")
        self._infinite = SequenceElementItemLoopInfinite(device, f"{self._cmd_syntax}:INFinite")

    @property
    def count(self) -> SequenceElementItemLoopCount:
        """Return the ``SEQuence:ELEMent[n]:LOOP:COUNt`` command.

        Description:
            - This command and query sets or returns the loop count. Loop count setting for an
              element is ignored if ``SEQUENCE:ELEMENTN:LOOP:INFINITE`` is set to ON.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:LOOP:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:LOOP:COUNt?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEQuence:ELEMent[n]:LOOP:COUNt value`` command.

        SCPI Syntax:
            ```
            - SEQuence:ELEMent[n]:LOOP:COUNt <NR1>
            - SEQuence:ELEMent[n]:LOOP:COUNt?
            ```

        Info:
            - ``<NR1>``
        """
        return self._count

    @property
    def infinite(self) -> SequenceElementItemLoopInfinite:
        """Return the ``SEQuence:ELEMent[n]:LOOP:INFinite`` command.

        Description:
            - This command and query sets or returns the infinite looping state for a sequence
              element. When an infinite loop is set on an element, the sequencer continuously
              executes that element. To break the infinite loop, either issue the
              ``AWGCONTROL:STOP:IMMEDIATE`` command or change the run mode to Continuous by using
              ``AWGCONTROL:RMODE`` command.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:LOOP:INFinite?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEQuence:ELEMent[n]:LOOP:INFinite?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEQuence:ELEMent[n]:LOOP:INFinite value`` command.

        SCPI Syntax:
            ```
            - SEQuence:ELEMent[n]:LOOP:INFinite <loop_state>
            - SEQuence:ELEMent[n]:LOOP:INFinite?
            ```

        Info:
            - ``<loop_state>`` ::=<Boolean>.
            - ``0`` indicates OFF.
            - ``1`` indicates ON.
        """
        return self._infinite


class SequenceElementItemJtargetType(SCPICmdWrite, SCPICmdRead):
    """The ``SEQuence:ELEMent[n]:JTARget:TYPE`` command.

    Description:
        - This command and query sets or returns the event jump target type for the jump. Generate
          an event in one of the following ways: By connecting an external cable to instrument rear
          panel for external event. By pressing the Force Event button on the front panel. By
          sending the ``EVENT:IMMEDIATE`` remote command.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:JTARget:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:JTARget:TYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEQuence:ELEMent[n]:JTARget:TYPE value`` command.

    SCPI Syntax:
        ```
        - SEQuence:ELEMent[n]:JTARget:TYPE {INDex|NEXT|OFF}
        - SEQuence:ELEMent[n]:JTARget:TYPE?
        ```

    Info:
        - ``INDex`` . This enables the sequencer to jump to an index set using
          ``SEQuence:ELEMent1:JTARget:INDexcommand``.
        - ``NEXT`` . This enables the sequencer to jump to the next sequence element.
          ``SEQuence:ELEMent1:JTARget:INDexsetting`` is ignored.
        - ``OFF`` . This enables the sequencer to turn off the event jump state. In this state, even
          if the event occurs, the sequencer ignores it.
    """


class SequenceElementItemJtargetIndex(SCPICmdWrite, SCPICmdRead):
    """The ``SEQuence:ELEMent[n]:JTARget:INDex`` command.

    Description:
        - This command and query sets or returns the target index for the sequencer's event jump
          operation. Note that this will take effect only when ``SEQUENCE:ELEMENTN:JTARGET:TYPE`` is
          set to INDex.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:JTARget:INDex?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:JTARget:INDex?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SEQuence:ELEMent[n]:JTARget:INDex value`` command.

    SCPI Syntax:
        ```
        - SEQuence:ELEMent[n]:JTARget:INDex <target>
        - SEQuence:ELEMent[n]:JTARget:INDex?
        ```

    Info:
        - ``<target>`` ::=<NR1>.
        - ``<n>`` is an index number of sequence.
    """


class SequenceElementItemJtarget(SCPICmdRead):
    """The ``SEQuence:ELEMent[n]:JTARget`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:JTARget?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:JTARget?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.index``: The ``SEQuence:ELEMent[n]:JTARget:INDex`` command.
        - ``.type``: The ``SEQuence:ELEMent[n]:JTARget:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._index = SequenceElementItemJtargetIndex(device, f"{self._cmd_syntax}:INDex")
        self._type = SequenceElementItemJtargetType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def index(self) -> SequenceElementItemJtargetIndex:
        """Return the ``SEQuence:ELEMent[n]:JTARget:INDex`` command.

        Description:
            - This command and query sets or returns the target index for the sequencer's event jump
              operation. Note that this will take effect only when
              ``SEQUENCE:ELEMENTN:JTARGET:TYPE`` is set to INDex.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:JTARget:INDex?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEQuence:ELEMent[n]:JTARget:INDex?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEQuence:ELEMent[n]:JTARget:INDex value`` command.

        SCPI Syntax:
            ```
            - SEQuence:ELEMent[n]:JTARget:INDex <target>
            - SEQuence:ELEMent[n]:JTARget:INDex?
            ```

        Info:
            - ``<target>`` ::=<NR1>.
            - ``<n>`` is an index number of sequence.
        """
        return self._index

    @property
    def type(self) -> SequenceElementItemJtargetType:
        """Return the ``SEQuence:ELEMent[n]:JTARget:TYPE`` command.

        Description:
            - This command and query sets or returns the event jump target type for the jump.
              Generate an event in one of the following ways: By connecting an external cable to
              instrument rear panel for external event. By pressing the Force Event button on the
              front panel. By sending the ``EVENT:IMMEDIATE`` remote command.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:JTARget:TYPE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``SEQuence:ELEMent[n]:JTARget:TYPE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEQuence:ELEMent[n]:JTARget:TYPE value`` command.

        SCPI Syntax:
            ```
            - SEQuence:ELEMent[n]:JTARget:TYPE {INDex|NEXT|OFF}
            - SEQuence:ELEMent[n]:JTARget:TYPE?
            ```

        Info:
            - ``INDex`` . This enables the sequencer to jump to an index set using
              ``SEQuence:ELEMent1:JTARget:INDexcommand``.
            - ``NEXT`` . This enables the sequencer to jump to the next sequence element.
              ``SEQuence:ELEMent1:JTARget:INDexsetting`` is ignored.
            - ``OFF`` . This enables the sequencer to turn off the event jump state. In this state,
              even if the event occurs, the sequencer ignores it.
        """
        return self._type


class SequenceElementItemGotoState(SCPICmdWrite, SCPICmdRead):
    """The ``SEQuence:ELEMent[n]:GOTO:STATe`` command.

    Description:
        - This command and query sets or returns the GOTO state of the sequencer. For the
          ``SEQUENCE:ELEMENTN:GOTO:INDEX`` command to take effect, the GOTO state must be set to ON.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:GOTO:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:GOTO:STATe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEQuence:ELEMent[n]:GOTO:STATe value``
          command.

    SCPI Syntax:
        ```
        - SEQuence:ELEMent[n]:GOTO:STATe <goto_state>
        - SEQuence:ELEMent[n]:GOTO:STATe?
        ```

    Info:
        - ``<goto_state>`` ::=<Boolean>.
        - ``0`` indicates OFF.
        - ``1`` indicates ON.
    """


class SequenceElementItemGotoIndex(SCPICmdWrite, SCPICmdRead):
    """The ``SEQuence:ELEMent[n]:GOTO:INDex`` command.

    Description:
        - This command and query sets or returns the target index for the GOTO command of the
          sequencer. After generating the waveform specified in a sequence element, the sequencer
          jumps to the element specified as GOTO target. This is an unconditional jump. If GOTO
          target is not specified, the sequencer simply moves on to the next element. If the Loop
          Count is Infinite, the GOTO target which is specified in the element is not used. For this
          command to work, the ``SEQUENCE:ELEMENTN:GOTO:STATE`` must be ON and the sequence element
          must exist. Note that the first element of a sequence is taken to be 1 not 0.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:GOTO:INDex?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:GOTO:INDex?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SEQuence:ELEMent[n]:GOTO:INDex value``
          command.

    SCPI Syntax:
        ```
        - SEQuence:ELEMent[n]:GOTO:INDex <target>
        - SEQuence:ELEMent[n]:GOTO:INDex?
        ```

    Info:
        - ``<target>`` ::=<NR1>.
    """


class SequenceElementItemGoto(SCPICmdRead):
    """The ``SEQuence:ELEMent[n]:GOTO`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:GOTO?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:GOTO?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.index``: The ``SEQuence:ELEMent[n]:GOTO:INDex`` command.
        - ``.state``: The ``SEQuence:ELEMent[n]:GOTO:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._index = SequenceElementItemGotoIndex(device, f"{self._cmd_syntax}:INDex")
        self._state = SequenceElementItemGotoState(device, f"{self._cmd_syntax}:STATe")

    @property
    def index(self) -> SequenceElementItemGotoIndex:
        """Return the ``SEQuence:ELEMent[n]:GOTO:INDex`` command.

        Description:
            - This command and query sets or returns the target index for the GOTO command of the
              sequencer. After generating the waveform specified in a sequence element, the
              sequencer jumps to the element specified as GOTO target. This is an unconditional
              jump. If GOTO target is not specified, the sequencer simply moves on to the next
              element. If the Loop Count is Infinite, the GOTO target which is specified in the
              element is not used. For this command to work, the ``SEQUENCE:ELEMENTN:GOTO:STATE``
              must be ON and the sequence element must exist. Note that the first element of a
              sequence is taken to be 1 not 0.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:GOTO:INDex?`` query.
            - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:GOTO:INDex?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEQuence:ELEMent[n]:GOTO:INDex value`` command.

        SCPI Syntax:
            ```
            - SEQuence:ELEMent[n]:GOTO:INDex <target>
            - SEQuence:ELEMent[n]:GOTO:INDex?
            ```

        Info:
            - ``<target>`` ::=<NR1>.
        """
        return self._index

    @property
    def state(self) -> SequenceElementItemGotoState:
        """Return the ``SEQuence:ELEMent[n]:GOTO:STATe`` command.

        Description:
            - This command and query sets or returns the GOTO state of the sequencer. For the
              ``SEQUENCE:ELEMENTN:GOTO:INDEX`` command to take effect, the GOTO state must be set to
              ON.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:GOTO:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:GOTO:STATe?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEQuence:ELEMent[n]:GOTO:STATe value`` command.

        SCPI Syntax:
            ```
            - SEQuence:ELEMent[n]:GOTO:STATe <goto_state>
            - SEQuence:ELEMent[n]:GOTO:STATe?
            ```

        Info:
            - ``<goto_state>`` ::=<Boolean>.
            - ``0`` indicates OFF.
            - ``1`` indicates ON.
        """
        return self._state


class SequenceElementItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SEQuence:ELEMent[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.goto``: The ``SEQuence:ELEMent[n]:GOTO`` command tree.
        - ``.jtarget``: The ``SEQuence:ELEMent[n]:JTARget`` command tree.
        - ``.loop``: The ``SEQuence:ELEMent[n]:LOOP`` command tree.
        - ``.subsequence``: The ``SEQuence:ELEMent[n]:SUBSequence`` command.
        - ``.twait``: The ``SEQuence:ELEMent[n]:TWAit`` command.
        - ``.waveform``: The ``SEQuence:ELEMent[n]:WAVeform[m]`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._goto = SequenceElementItemGoto(device, f"{self._cmd_syntax}:GOTO")
        self._jtarget = SequenceElementItemJtarget(device, f"{self._cmd_syntax}:JTARget")
        self._loop = SequenceElementItemLoop(device, f"{self._cmd_syntax}:LOOP")
        self._subsequence = SequenceElementItemSubsequence(
            device, f"{self._cmd_syntax}:SUBSequence"
        )
        self._twait = SequenceElementItemTwait(device, f"{self._cmd_syntax}:TWAit")
        self._waveform: Dict[int, SequenceElementItemWaveformItem] = DefaultDictPassKeyToFactory(
            lambda x: SequenceElementItemWaveformItem(device, f"{self._cmd_syntax}:WAVeform{x}")
        )

    @property
    def goto(self) -> SequenceElementItemGoto:
        """Return the ``SEQuence:ELEMent[n]:GOTO`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:GOTO?`` query.
            - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:GOTO?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.index``: The ``SEQuence:ELEMent[n]:GOTO:INDex`` command.
            - ``.state``: The ``SEQuence:ELEMent[n]:GOTO:STATe`` command.
        """
        return self._goto

    @property
    def jtarget(self) -> SequenceElementItemJtarget:
        """Return the ``SEQuence:ELEMent[n]:JTARget`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:JTARget?`` query.
            - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:JTARget?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.index``: The ``SEQuence:ELEMent[n]:JTARget:INDex`` command.
            - ``.type``: The ``SEQuence:ELEMent[n]:JTARget:TYPE`` command.
        """
        return self._jtarget

    @property
    def loop(self) -> SequenceElementItemLoop:
        """Return the ``SEQuence:ELEMent[n]:LOOP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:LOOP?`` query.
            - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:LOOP?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.count``: The ``SEQuence:ELEMent[n]:LOOP:COUNt`` command.
            - ``.infinite``: The ``SEQuence:ELEMent[n]:LOOP:INFinite`` command.
        """
        return self._loop

    @property
    def subsequence(self) -> SequenceElementItemSubsequence:
        """Return the ``SEQuence:ELEMent[n]:SUBSequence`` command.

        Description:
            - This command and query sets or returns the subsequence for a sequence element. The
              AWG5012B, AWG5000C, and AWG7000C (option 09) series instruments support Subsequence.
              The subsequence name can be a null string (''). When a waveform is assigned to this
              sequence, the command returns ''.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:SUBSequence?``
              query.
            - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:SUBSequence?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEQuence:ELEMent[n]:SUBSequence value`` command.

        SCPI Syntax:
            ```
            - SEQuence:ELEMent[n]:SUBSequence <subseq_name>
            - SEQuence:ELEMent[n]:SUBSequence?
            ```

        Info:
            - ``<subseq_name>`` ::=<string>.
        """
        return self._subsequence

    @property
    def twait(self) -> SequenceElementItemTwait:
        """Return the ``SEQuence:ELEMent[n]:TWAit`` command.

        Description:
            - This command and query sets or returns the wait trigger state for an element. Send a
              trigger signal in one of the following ways: By using an external trigger signal. By
              pressing the 'Force Trigger' button on the front panel. By sending the ``*TRG`` remote
              command.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]:TWAit?`` query.
            - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]:TWAit?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SEQuence:ELEMent[n]:TWAit value``
              command.

        SCPI Syntax:
            ```
            - SEQuence:ELEMent[n]:TWAit <Boolean>
            - SEQuence:ELEMent[n]:TWAit?
            ```

        Info:
            - ``<wait_trigger_state>`` ::=<Boolean>.
            - ``0`` indicates OFF.
            - ``1`` indicates ON.
        """
        return self._twait

    @property
    def waveform(self) -> Dict[int, SequenceElementItemWaveformItem]:
        """Return the ``SEQuence:ELEMent[n]:WAVeform[m]`` command.

        Description:
            - This command and query sets or returns the waveform for a sequence element.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SEQuence:ELEMent[n]:WAVeform[m]? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SEQuence:ELEMent[n]:WAVeform[m]? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SEQuence:ELEMent[n]:WAVeform[m] value`` command.

        SCPI Syntax:
            ```
            - SEQuence:ELEMent[n]:WAVeform[m] [1|2|3|4] <wfm_name>
            - SEQuence:ELEMent[n]:WAVeform[m]? [1|2|3|4]
            ```

        Info:
            - ``<wfm_name`` >::=<string>.
        """
        return self._waveform


class Sequence(SCPICmdRead):
    """The ``SEQuence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``SEQuence?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.element``: The ``SEQuence:ELEMent[n]`` command tree.
        - ``.jump``: The ``SEQuence:JUMP`` command tree.
        - ``.length``: The ``SEQuence:LENGth`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SEQuence") -> None:
        super().__init__(device, cmd_syntax)
        self._element: Dict[int, SequenceElementItem] = DefaultDictPassKeyToFactory(
            lambda x: SequenceElementItem(device, f"{self._cmd_syntax}:ELEMent{x}")
        )
        self._jump = SequenceJump(device, f"{self._cmd_syntax}:JUMP")
        self._length = SequenceLength(device, f"{self._cmd_syntax}:LENGth")

    @property
    def element(self) -> Dict[int, SequenceElementItem]:
        """Return the ``SEQuence:ELEMent[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:ELEMent[n]?`` query.
            - Using the ``.verify(value)`` method will send the ``SEQuence:ELEMent[n]?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.goto``: The ``SEQuence:ELEMent[n]:GOTO`` command tree.
            - ``.jtarget``: The ``SEQuence:ELEMent[n]:JTARget`` command tree.
            - ``.loop``: The ``SEQuence:ELEMent[n]:LOOP`` command tree.
            - ``.subsequence``: The ``SEQuence:ELEMent[n]:SUBSequence`` command.
            - ``.twait``: The ``SEQuence:ELEMent[n]:TWAit`` command.
            - ``.waveform``: The ``SEQuence:ELEMent[n]:WAVeform[m]`` command.
        """
        return self._element

    @property
    def jump(self) -> SequenceJump:
        """Return the ``SEQuence:JUMP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:JUMP?`` query.
            - Using the ``.verify(value)`` method will send the ``SEQuence:JUMP?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``SEQuence:JUMP:IMMediate`` command.
        """
        return self._jump

    @property
    def length(self) -> SequenceLength:
        """Return the ``SEQuence:LENGth`` command.

        Description:
            - This command and query sets or returns the sequence length. Use this command to create
              an uninitialized sequence. You can also use the command to clear all sequence elements
              in a single action by passing 0 as the parameter. However, this action cannot be
              undone so exercise necessary caution. Also note that passing a value less than the
              sequence's current length will cause some sequence elements to be deleted at the end
              of the sequence. For example if ``SEQuence:LENGth?`` returns 200 and you subsequently
              send ``SEQuence:LENGth 21``, all sequence elements except the first 20 will be
              deleted.

        Usage:
            - Using the ``.query()`` method will send the ``SEQuence:LENGth?`` query.
            - Using the ``.verify(value)`` method will send the ``SEQuence:LENGth?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SEQuence:LENGth value`` command.

        SCPI Syntax:
            ```
            - SEQuence:LENGth <NR1>
            - SEQuence:LENGth?
            ```

        Info:
            - ``<NR1>``
        """
        return self._length
