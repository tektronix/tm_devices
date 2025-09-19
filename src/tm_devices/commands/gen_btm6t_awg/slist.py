"""The slist commands module.

These commands are used in the following models:
AWG5200, AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SLISt:NAME? <sequence_list_index>
    - SLISt:SEQuence:AMPLitude <sequence_name>,<amplitude>
    - SLISt:SEQuence:AMPLitude? <sequence_name>
    - SLISt:SEQuence:DELete {<sequence_name>|ALL}
    - SLISt:SEQuence:EVENt:JTIMing <sequence_name>, {END|IMMediate}
    - SLISt:SEQuence:EVENt:JTIMing? <sequence_name>
    - SLISt:SEQuence:EVENt:PJUMp:DEFine <sequence_name>, <pattern>, <jump_step>
    - SLISt:SEQuence:EVENt:PJUMp:DEFine? <sequence_name>, <pattern>
    - SLISt:SEQuence:EVENt:PJUMp:ENABle <sequence_name>, {0|1|OFF|ON}
    - SLISt:SEQuence:EVENt:PJUMp:ENABle? <sequence_name>
    - SLISt:SEQuence:EVENt:PJUMp:SIZE?
    - SLISt:SEQuence:FREQuency <seq_name>,<frequency>
    - SLISt:SEQuence:FREQuency? <seq_name>
    - SLISt:SEQuence:LENGth? <sequence_name>
    - SLISt:SEQuence:NEW <sequence_name>,<number_of_steps>[,<number_of_tracks>]
    - SLISt:SEQuence:OFFSet <sequence_name>,<offset>
    - SLISt:SEQuence:OFFSet? <sequence_name>
    - SLISt:SEQuence:RFLag <sequence_name>, {0|1|OFF|ON}
    - SLISt:SEQuence:RFLag? <sequence_name>
    - SLISt:SEQuence:SRATe <sequence_name>,<sample_rate>
    - SLISt:SEQuence:SRATe? <sequence_name>
    - SLISt:SEQuence:STEP:ADD <sequence_name>,<location>[,<steps to add>]
    - SLISt:SEQuence:STEP:MAX?
    - SLISt:SEQuence:STEP:RCOunt:MAX?
    - SLISt:SEQuence:STEP[n]:EJINput <sequence_name>,{ATRigger|BTRigger|OFF|ITRigger}
    - SLISt:SEQuence:STEP[n]:EJINput? <sequence_name>
    - SLISt:SEQuence:STEP[n]:EJUMp <sequence_name>, {<NR1>|NEXT|FIRSt|LAST|END}
    - SLISt:SEQuence:STEP[n]:EJUMp? <sequence_name>
    - SLISt:SEQuence:STEP[n]:GOTO <sequence_name>, {<NR1>|LAST|FIRSt|NEXT|END}
    - SLISt:SEQuence:STEP[n]:GOTO? <sequence_name>
    - SLISt:SEQuence:STEP[n]:RCOunt <sequence_name>, {ONCE|INFinite|<NR1>}
    - SLISt:SEQuence:STEP[n]:RCOunt? <sequence_name>
    - SLISt:SEQuence:STEP[n]:TASSet:SEQuence <sequence_name>, <subsequence_name>
    - SLISt:SEQuence:STEP[n]:TASSet[m]:TYPE? <sequence_name>
    - SLISt:SEQuence:STEP[n]:TASSet[m]:WAVeform <sequence_name>, <waveform_name>
    - SLISt:SEQuence:STEP[n]:TASSet[m]? <sequence_name>
    - SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
    - SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag? <sequence_name>
    - SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
    - SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag? <sequence_name>
    - SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
    - SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag? <sequence_name>
    - SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
    - SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag? <sequence_name>
    - SLISt:SEQuence:STEP[n]:WINPut <sequence_name>, {ATRigger|BTRigger|ITRigger|OFF}
    - SLISt:SEQuence:STEP[n]:WINPut? <sequence_name>
    - SLISt:SEQuence:TRACk:MAX?
    - SLISt:SEQuence:TRACk? <sequence_name>
    - SLISt:SEQuence:TSTamp? <sequence_name>
    - SLISt:SEQuence:WMUSage? <sequence_name>,<track_number>
    - SLISt:SIZE?
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


class SlistSequenceWmusage(SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:WMUSage`` command.

    Description:
        - This command returns the total waveform memory usage (in sample points) for the specified
          sequence track for the named sequence.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:WMUSage? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:WMUSage? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:WMUSage? <sequence_name>,<track_number>
        ```
    """


class SlistSequenceTstamp(SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:TSTamp`` command.

    Description:
        - This command returns the timestamp of the named sequence. Every sequence has a timestamp
          that indicates when the sequence was created or last modified.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:TSTamp? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:TSTamp? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:TSTamp? <sequence_name>
        ```
    """


class SlistSequenceTrackMax(SCPICmdRead):
    """The ``SLISt:SEQuence:TRACk:MAX`` command.

    Description:
        - This command returns the maximum number of tracks allowed in a sequence

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence:TRACk:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:TRACk:MAX?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:TRACk:MAX?
        ```
    """


class SlistSequenceTrack(SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:TRACk`` command.

    Description:
        - This command returns the number of tracks defined in the specified sequence.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:TRACk? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:TRACk? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:TRACk? <sequence_name>
        ```

    Properties:
        - ``.max``: The ``SLISt:SEQuence:TRACk:MAX`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = SlistSequenceTrackMax(device, f"{self._cmd_syntax}:MAX")

    @property
    def max(self) -> SlistSequenceTrackMax:
        """Return the ``SLISt:SEQuence:TRACk:MAX`` command.

        Description:
            - This command returns the maximum number of tracks allowed in a sequence

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence:TRACk:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:TRACk:MAX?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:TRACk:MAX?
            ```
        """
        return self._max


class SlistSequenceStepItemWinput(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:STEP[n]:WINPut`` command.

    Description:
        - This command sets or returns the trigger source for the wait input state for a step. Send
          a trigger signal in one of the following ways: Use an external trigger signal. Push the
          Force Trigger button on the front panel. Send the TRG or ``TRIGGER:IMMEDIATE`` remote
          commands. Use the Internal Trigger.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:STEP[n]:WINPut? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:WINPut? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:STEP[n]:WINPut value``
          command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:WINPut <sequence_name>, {ATRigger|BTRigger|ITRigger|OFF}
        - SLISt:SEQuence:STEP[n]:WINPut? <sequence_name>
        ```

    Info:
        - ``ATRigger`` - This enables the sequencer to move due to a trigger event from the A
          Trigger Input connector or the A Force Trigger front panel button.BTRigger - This enables
          the sequencer to move due to a trigger event from the B Trigger Input connector or the B
          Force Trigger front panel button.ITRigger - This enables the sequencer to move due to an
          Internal Trigger event.OFF - Disables the wait for trigger event, allowing the
          waveforms(s) of this step to be played immediately.
    """


class SlistSequenceStepItemTflagItemDflag(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag`` command.

    Description:
        - This command sets or returns the Flag D value of the track in a sequence step.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
        - SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag? <sequence_name>
        ```

    Info:
        - ``NCHange`` - The flag state continues to be in the state is defined in the previous step
          Default value.HIGH - The flag signal transitions to the high state.LOW - The flag signal
          transitions to the low state.TOGGle - The flag signal transitions to the high state if the
          previous step defined the flag to be in the low state and vice versa.PULSe - The flag
          signal outputs a pulse signal of a fixed width.
    """


class SlistSequenceStepItemTflagItemCflag(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag`` command.

    Description:
        - This command sets or returns the Flag C value of the track in a sequence step.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
        - SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag? <sequence_name>
        ```

    Info:
        - ``NCHange`` - The flag state continues to be in the state is defined in the previous step
          Default value.HIGH - The flag signal transitions to the high state.LOW - The flag signal
          transitions to the low state.TOGGle - The flag signal transitions to the high state if the
          previous step defined the flag to be in the low state and vice versa.PULSe - The flag
          signal outputs a pulse signal of a fixed width.
    """


class SlistSequenceStepItemTflagItemBflag(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag`` command.

    Description:
        - This command sets or returns the Flag B value of the track in a sequence step.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
        - SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag? <sequence_name>
        ```

    Info:
        - ``NCHange`` - The flag state continues to be in the state is defined in the previous step
          Default value.HIGH - The flag signal transitions to the high state.LOW - The flag signal
          transitions to the low state.TOGGle - The flag signal transitions to the high state if the
          previous step defined the flag to be in the low state and vice versa.PULSe - The flag
          signal outputs a pulse signal of a fixed width.
    """


class SlistSequenceStepItemTflagItemAflag(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag`` command.

    Description:
        - This command sets or returns the Flag A value of the track in a sequence step.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
        - SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag? <sequence_name>
        ```

    Info:
        - ``NCHange`` - The flag state continues to be in the state is defined in the previous step
          Default value.HIGH - The flag signal transitions to the high state.LOW - The flag signal
          transitions to the low state.TOGGle - The flag signal transitions to the high state if the
          previous step defined the flag to be in the low state and vice versa.PULSe - The flag
          signal outputs a pulse signal of a fixed width.
    """


class SlistSequenceStepItemTflagItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SLISt:SEQuence:STEP[n]:TFLag[m]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP[n]:TFLag[m]?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP[n]:TFLag[m]?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.aflag``: The ``SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag`` command.
        - ``.bflag``: The ``SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag`` command.
        - ``.cflag``: The ``SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag`` command.
        - ``.dflag``: The ``SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aflag = SlistSequenceStepItemTflagItemAflag(device, f"{self._cmd_syntax}:AFLag")
        self._bflag = SlistSequenceStepItemTflagItemBflag(device, f"{self._cmd_syntax}:BFLag")
        self._cflag = SlistSequenceStepItemTflagItemCflag(device, f"{self._cmd_syntax}:CFLag")
        self._dflag = SlistSequenceStepItemTflagItemDflag(device, f"{self._cmd_syntax}:DFLag")

    @property
    def aflag(self) -> SlistSequenceStepItemTflagItemAflag:
        """Return the ``SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag`` command.

        Description:
            - This command sets or returns the Flag A value of the track in a sequence step.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
            - SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag? <sequence_name>
            ```

        Info:
            - ``NCHange`` - The flag state continues to be in the state is defined in the previous
              step Default value.HIGH - The flag signal transitions to the high state.LOW - The flag
              signal transitions to the low state.TOGGle - The flag signal transitions to the high
              state if the previous step defined the flag to be in the low state and vice
              versa.PULSe - The flag signal outputs a pulse signal of a fixed width.
        """
        return self._aflag

    @property
    def bflag(self) -> SlistSequenceStepItemTflagItemBflag:
        """Return the ``SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag`` command.

        Description:
            - This command sets or returns the Flag B value of the track in a sequence step.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
            - SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag? <sequence_name>
            ```

        Info:
            - ``NCHange`` - The flag state continues to be in the state is defined in the previous
              step Default value.HIGH - The flag signal transitions to the high state.LOW - The flag
              signal transitions to the low state.TOGGle - The flag signal transitions to the high
              state if the previous step defined the flag to be in the low state and vice
              versa.PULSe - The flag signal outputs a pulse signal of a fixed width.
        """
        return self._bflag

    @property
    def cflag(self) -> SlistSequenceStepItemTflagItemCflag:
        """Return the ``SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag`` command.

        Description:
            - This command sets or returns the Flag C value of the track in a sequence step.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
            - SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag? <sequence_name>
            ```

        Info:
            - ``NCHange`` - The flag state continues to be in the state is defined in the previous
              step Default value.HIGH - The flag signal transitions to the high state.LOW - The flag
              signal transitions to the low state.TOGGle - The flag signal transitions to the high
              state if the previous step defined the flag to be in the low state and vice
              versa.PULSe - The flag signal outputs a pulse signal of a fixed width.
        """
        return self._cflag

    @property
    def dflag(self) -> SlistSequenceStepItemTflagItemDflag:
        """Return the ``SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag`` command.

        Description:
            - This command sets or returns the Flag D value of the track in a sequence step.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag <sequence_name>, {NCHange|HIGH|LOW|TOGGle|PULSe}
            - SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag? <sequence_name>
            ```

        Info:
            - ``NCHange`` - The flag state continues to be in the state is defined in the previous
              step Default value.HIGH - The flag signal transitions to the high state.LOW - The flag
              signal transitions to the low state.TOGGle - The flag signal transitions to the high
              state if the previous step defined the flag to be in the low state and vice
              versa.PULSe - The flag signal outputs a pulse signal of a fixed width.
        """
        return self._dflag


class SlistSequenceStepItemTassetItemWaveform(SCPICmdWrite):
    """The ``SLISt:SEQuence:STEP[n]:TASSet[m]:WAVeform`` command.

    Description:
        - This command assigns a waveform for a specific sequence's step and track. This waveform is
          played whenever the playing sequence reaches this step. A track in a sequence is assigned
          to a channel with the command [SOURce[n]]``:CASSET:SEQ``.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TASSet[m]:WAVeform value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:TASSet[m]:WAVeform <sequence_name>, <waveform_name>
        ```
    """


class SlistSequenceStepItemTassetItemType(SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:STEP[n]:TASSet[m]:TYPE`` command.

    Description:
        - This command returns the type of asset assigned at the step and track for a specified
          sequence. The types of assets are waveform and subsequence.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TASSet[m]:TYPE? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TASSet[m]:TYPE? argument`` query and raise an AssertionError if
          the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:TASSet[m]:TYPE? <sequence_name>
        ```
    """


class SlistSequenceStepItemTassetItem(ValidatedDynamicNumberCmd, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:STEP[n]:TASSet[m]`` command.

    Description:
        - This command returns the name of the waveform or subsequence at the specified sequence's
          step number and track asset value. Waveform or subsequence can be distinguished by the
          ``SLIST:SEQUENCE:STEPN:TASSETM:TYPE`` query.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TASSet[m]? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TASSet[m]? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:TASSet[m]? <sequence_name>
        ```

    Properties:
        - ``.type``: The ``SLISt:SEQuence:STEP[n]:TASSet[m]:TYPE`` command.
        - ``.waveform``: The ``SLISt:SEQuence:STEP[n]:TASSet[m]:WAVeform`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._type = SlistSequenceStepItemTassetItemType(device, f"{self._cmd_syntax}:TYPE")
        self._waveform = SlistSequenceStepItemTassetItemWaveform(
            device, f"{self._cmd_syntax}:WAVeform"
        )

    @property
    def type(self) -> SlistSequenceStepItemTassetItemType:
        """Return the ``SLISt:SEQuence:STEP[n]:TASSet[m]:TYPE`` command.

        Description:
            - This command returns the type of asset assigned at the step and track for a specified
              sequence. The types of assets are waveform and subsequence.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TASSet[m]:TYPE? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TASSet[m]:TYPE? argument`` query and raise an AssertionError
              if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:TASSet[m]:TYPE? <sequence_name>
            ```
        """
        return self._type

    @property
    def waveform(self) -> SlistSequenceStepItemTassetItemWaveform:
        """Return the ``SLISt:SEQuence:STEP[n]:TASSet[m]:WAVeform`` command.

        Description:
            - This command assigns a waveform for a specific sequence's step and track. This
              waveform is played whenever the playing sequence reaches this step. A track in a
              sequence is assigned to a channel with the command [SOURce[n]]``:CASSET:SEQ``.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TASSet[m]:WAVeform value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:TASSet[m]:WAVeform <sequence_name>, <waveform_name>
            ```
        """
        return self._waveform


class SlistSequenceStepItemTassetSequence(SCPICmdWrite):
    """The ``SLISt:SEQuence:STEP[n]:TASSet:SEQuence`` command.

    Description:
        - This command assigns a subsequence for a specific sequence's step and track.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:TASSet:SEQuence value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:TASSet:SEQuence <sequence_name>, <subsequence_name>
        ```
    """


class SlistSequenceStepItemTasset(SCPICmdRead):
    """The ``SLISt:SEQuence:STEP[n]:TASSet`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP[n]:TASSet?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP[n]:TASSet?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.sequence``: The ``SLISt:SEQuence:STEP[n]:TASSet:SEQuence`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sequence = SlistSequenceStepItemTassetSequence(device, f"{self._cmd_syntax}:SEQuence")

    @property
    def sequence(self) -> SlistSequenceStepItemTassetSequence:
        """Return the ``SLISt:SEQuence:STEP[n]:TASSet:SEQuence`` command.

        Description:
            - This command assigns a subsequence for a specific sequence's step and track.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TASSet:SEQuence value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:TASSet:SEQuence <sequence_name>, <subsequence_name>
            ```
        """
        return self._sequence


class SlistSequenceStepItemRcount(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:STEP[n]:RCOunt`` command.

    Description:
        - This command sets or returns the repeat count, which is the number of times the assigned
          waveform(s) play before proceeding to the next step in the sequence.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:STEP[n]:RCOunt? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:RCOunt? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:STEP[n]:RCOunt value``
          command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:RCOunt <sequence_name>, {ONCE|INFinite|<NR1>}
        - SLISt:SEQuence:STEP[n]:RCOunt? <sequence_name>
        ```

    Info:
        - ``ONCE`` - Plays the waveform one time during this sequence step.INFinte - Plays the
          waveform continuously during this sequence step.<NR1> - Plays this waveform the selected
          number of times during this sequence step. The allowed value is between 1 and 2^20.
    """


class SlistSequenceStepItemGoto(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:STEP[n]:GOTO`` command.

    Description:
        - This command sets or returns the target step for the GOTO command of the sequencer at the
          specified step. After generating the waveform(s) specified in a sequence step, the
          sequencer jumps to the step specified as the GOTO step. This is an unconditional jump. If
          the GOTO step is not specified, the sequencer moves to the next step. If the Repeat Count
          is Infinite, the specified GOTO step is not used.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:STEP[n]:GOTO? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:GOTO? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:STEP[n]:GOTO value``
          command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:GOTO <sequence_name>, {<NR1>|LAST|FIRSt|NEXT|END}
        - SLISt:SEQuence:STEP[n]:GOTO? <sequence_name>
        ```

    Info:
        - ``LAST`` - This enables the sequencer to go to the last step in the sequence.FIRSt - This
          enables the sequencer to go to first step in the sequence.NEXT - This enables the
          sequencer to go to the next sequence step. (The ``SLISt:SEQuence:STEP``[n]``:EJUMp:STEP``
          setting is ignored.)END - This enables the sequencer to go to the end and play 0 V until
          play is stopped.
    """


class SlistSequenceStepItemEjump(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:STEP[n]:EJUMp`` command.

    Description:
        - This command sets or returns the step that the specified sequence will jump to on a
          trigger event. This setting is only available if the event jump input has been selected as
          Trigger A or Trigger B for the specified step.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:STEP[n]:EJUMp? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:EJUMp? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:STEP[n]:EJUMp value``
          command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:EJUMp <sequence_name>, {<NR1>|NEXT|FIRSt|LAST|END}
        - SLISt:SEQuence:STEP[n]:EJUMp? <sequence_name>
        ```

    Info:
        - ``NEXT`` - This enables the sequencer to jump to the next sequence step.FIRSt - This
          enables the sequencer to jump to first step in the sequence.LAST - This enables the
          sequencer to jump to the last step in the sequence. END - This enables the sequencer to
          jump to the end and play 0 V until play is stopped.
    """


class SlistSequenceStepItemEjinput(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:STEP[n]:EJINput`` command.

    Description:
        - This command sets or returns wether the sequence will jump when it receives Trigger A,
          Trigger B, Internal Trigger, or no jump at all. This is settable for every step in a
          sequence.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:STEP[n]:EJINput? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:STEP[n]:EJINput? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:STEP[n]:EJINput value``
          command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP[n]:EJINput <sequence_name>,{ATRigger|BTRigger|OFF|ITRigger}
        - SLISt:SEQuence:STEP[n]:EJINput? <sequence_name>
        ```

    Info:
        - ``ATRigger`` - This enables the sequencer to jump to the event of a ATRIG.BTRigger - This
          enables the sequencer to jump to the event of a BTRIG.ITRigger - This enables the
          sequencer to jump to the event of an Internal Trigger.OFF - Ignores all events, even if an
          event occurs during that step.
        - ``*RST`` sets this to OFF.
    """


#  pylint: disable=too-many-instance-attributes
class SlistSequenceStepItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SLISt:SEQuence:STEP[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP[n]?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ejinput``: The ``SLISt:SEQuence:STEP[n]:EJINput`` command.
        - ``.ejump``: The ``SLISt:SEQuence:STEP[n]:EJUMp`` command.
        - ``.goto``: The ``SLISt:SEQuence:STEP[n]:GOTO`` command.
        - ``.rcount``: The ``SLISt:SEQuence:STEP[n]:RCOunt`` command.
        - ``.tasset``: The ``SLISt:SEQuence:STEP[n]:TASSet`` command tree.
        - ``.tassetx``: The ``SLISt:SEQuence:STEP[n]:TASSet[m]`` command.
        - ``.tflag``: The ``SLISt:SEQuence:STEP[n]:TFLag[m]`` command tree.
        - ``.winput``: The ``SLISt:SEQuence:STEP[n]:WINPut`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ejinput = SlistSequenceStepItemEjinput(device, f"{self._cmd_syntax}:EJINput")
        self._ejump = SlistSequenceStepItemEjump(device, f"{self._cmd_syntax}:EJUMp")
        self._goto = SlistSequenceStepItemGoto(device, f"{self._cmd_syntax}:GOTO")
        self._rcount = SlistSequenceStepItemRcount(device, f"{self._cmd_syntax}:RCOunt")
        self._tasset = SlistSequenceStepItemTasset(device, f"{self._cmd_syntax}:TASSet")
        self._tassetx: Dict[int, SlistSequenceStepItemTassetItem] = DefaultDictPassKeyToFactory(
            lambda x: SlistSequenceStepItemTassetItem(device, f"{self._cmd_syntax}:TASSet{x}")
        )
        self._tflag: Dict[int, SlistSequenceStepItemTflagItem] = DefaultDictPassKeyToFactory(
            lambda x: SlistSequenceStepItemTflagItem(device, f"{self._cmd_syntax}:TFLag{x}")
        )
        self._winput = SlistSequenceStepItemWinput(device, f"{self._cmd_syntax}:WINPut")

    @property
    def ejinput(self) -> SlistSequenceStepItemEjinput:
        """Return the ``SLISt:SEQuence:STEP[n]:EJINput`` command.

        Description:
            - This command sets or returns wether the sequence will jump when it receives Trigger A,
              Trigger B, Internal Trigger, or no jump at all. This is settable for every step in a
              sequence.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:STEP[n]:EJINput? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:EJINput? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:EJINput value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:EJINput <sequence_name>,{ATRigger|BTRigger|OFF|ITRigger}
            - SLISt:SEQuence:STEP[n]:EJINput? <sequence_name>
            ```

        Info:
            - ``ATRigger`` - This enables the sequencer to jump to the event of a ATRIG.BTRigger -
              This enables the sequencer to jump to the event of a BTRIG.ITRigger - This enables the
              sequencer to jump to the event of an Internal Trigger.OFF - Ignores all events, even
              if an event occurs during that step.
            - ``*RST`` sets this to OFF.
        """
        return self._ejinput

    @property
    def ejump(self) -> SlistSequenceStepItemEjump:
        """Return the ``SLISt:SEQuence:STEP[n]:EJUMp`` command.

        Description:
            - This command sets or returns the step that the specified sequence will jump to on a
              trigger event. This setting is only available if the event jump input has been
              selected as Trigger A or Trigger B for the specified step.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:STEP[n]:EJUMp? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:EJUMp? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:EJUMp value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:EJUMp <sequence_name>, {<NR1>|NEXT|FIRSt|LAST|END}
            - SLISt:SEQuence:STEP[n]:EJUMp? <sequence_name>
            ```

        Info:
            - ``NEXT`` - This enables the sequencer to jump to the next sequence step.FIRSt - This
              enables the sequencer to jump to first step in the sequence.LAST - This enables the
              sequencer to jump to the last step in the sequence. END - This enables the sequencer
              to jump to the end and play 0 V until play is stopped.
        """
        return self._ejump

    @property
    def goto(self) -> SlistSequenceStepItemGoto:
        """Return the ``SLISt:SEQuence:STEP[n]:GOTO`` command.

        Description:
            - This command sets or returns the target step for the GOTO command of the sequencer at
              the specified step. After generating the waveform(s) specified in a sequence step, the
              sequencer jumps to the step specified as the GOTO step. This is an unconditional jump.
              If the GOTO step is not specified, the sequencer moves to the next step. If the Repeat
              Count is Infinite, the specified GOTO step is not used.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:STEP[n]:GOTO? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:GOTO? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:STEP[n]:GOTO value``
              command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:GOTO <sequence_name>, {<NR1>|LAST|FIRSt|NEXT|END}
            - SLISt:SEQuence:STEP[n]:GOTO? <sequence_name>
            ```

        Info:
            - ``LAST`` - This enables the sequencer to go to the last step in the sequence.FIRSt -
              This enables the sequencer to go to first step in the sequence.NEXT - This enables the
              sequencer to go to the next sequence step. (The
              ``SLISt:SEQuence:STEP``[n]``:EJUMp:STEP`` setting is ignored.)END - This enables the
              sequencer to go to the end and play 0 V until play is stopped.
        """
        return self._goto

    @property
    def rcount(self) -> SlistSequenceStepItemRcount:
        """Return the ``SLISt:SEQuence:STEP[n]:RCOunt`` command.

        Description:
            - This command sets or returns the repeat count, which is the number of times the
              assigned waveform(s) play before proceeding to the next step in the sequence.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:STEP[n]:RCOunt? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:RCOunt? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:RCOunt value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:RCOunt <sequence_name>, {ONCE|INFinite|<NR1>}
            - SLISt:SEQuence:STEP[n]:RCOunt? <sequence_name>
            ```

        Info:
            - ``ONCE`` - Plays the waveform one time during this sequence step.INFinte - Plays the
              waveform continuously during this sequence step.<NR1> - Plays this waveform the
              selected number of times during this sequence step. The allowed value is between 1 and
              2^20.
        """
        return self._rcount

    @property
    def tasset(self) -> SlistSequenceStepItemTasset:
        """Return the ``SLISt:SEQuence:STEP[n]:TASSet`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP[n]:TASSet?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP[n]:TASSet?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.sequence``: The ``SLISt:SEQuence:STEP[n]:TASSet:SEQuence`` command.
        """
        return self._tasset

    @property
    def tassetx(self) -> Dict[int, SlistSequenceStepItemTassetItem]:
        """Return the ``SLISt:SEQuence:STEP[n]:TASSet[m]`` command.

        Description:
            - This command returns the name of the waveform or subsequence at the specified
              sequence's step number and track asset value. Waveform or subsequence can be
              distinguished by the ``SLIST:SEQUENCE:STEPN:TASSETM:TYPE`` query.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TASSet[m]? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:TASSet[m]? argument`` query and raise an AssertionError if
              the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:TASSet[m]? <sequence_name>
            ```

        Sub-properties:
            - ``.type``: The ``SLISt:SEQuence:STEP[n]:TASSet[m]:TYPE`` command.
            - ``.waveform``: The ``SLISt:SEQuence:STEP[n]:TASSet[m]:WAVeform`` command.
        """
        return self._tassetx

    @property
    def tflag(self) -> Dict[int, SlistSequenceStepItemTflagItem]:
        """Return the ``SLISt:SEQuence:STEP[n]:TFLag[m]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP[n]:TFLag[m]?``
              query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP[n]:TFLag[m]?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.aflag``: The ``SLISt:SEQuence:STEP[n]:TFLag[m]:AFLag`` command.
            - ``.bflag``: The ``SLISt:SEQuence:STEP[n]:TFLag[m]:BFLag`` command.
            - ``.cflag``: The ``SLISt:SEQuence:STEP[n]:TFLag[m]:CFLag`` command.
            - ``.dflag``: The ``SLISt:SEQuence:STEP[n]:TFLag[m]:DFLag`` command.
        """
        return self._tflag

    @property
    def winput(self) -> SlistSequenceStepItemWinput:
        """Return the ``SLISt:SEQuence:STEP[n]:WINPut`` command.

        Description:
            - This command sets or returns the trigger source for the wait input state for a step.
              Send a trigger signal in one of the following ways: Use an external trigger signal.
              Push the Force Trigger button on the front panel. Send the TRG or
              ``TRIGGER:IMMEDIATE`` remote commands. Use the Internal Trigger.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:STEP[n]:WINPut? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:WINPut? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:STEP[n]:WINPut value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP[n]:WINPut <sequence_name>, {ATRigger|BTRigger|ITRigger|OFF}
            - SLISt:SEQuence:STEP[n]:WINPut? <sequence_name>
            ```

        Info:
            - ``ATRigger`` - This enables the sequencer to move due to a trigger event from the A
              Trigger Input connector or the A Force Trigger front panel button.BTRigger - This
              enables the sequencer to move due to a trigger event from the B Trigger Input
              connector or the B Force Trigger front panel button.ITRigger - This enables the
              sequencer to move due to an Internal Trigger event.OFF - Disables the wait for trigger
              event, allowing the waveforms(s) of this step to be played immediately.
        """
        return self._winput


class SlistSequenceStepRcountMax(SCPICmdRead):
    """The ``SLISt:SEQuence:STEP:RCOunt:MAX`` command.

    Description:
        - This command returns the maximum number of repeats allowed for a step in a sequence.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP:RCOunt:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP:RCOunt:MAX?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP:RCOunt:MAX?
        ```
    """


class SlistSequenceStepRcount(SCPICmdRead):
    """The ``SLISt:SEQuence:STEP:RCOunt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP:RCOunt?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP:RCOunt?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.max``: The ``SLISt:SEQuence:STEP:RCOunt:MAX`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._max = SlistSequenceStepRcountMax(device, f"{self._cmd_syntax}:MAX")

    @property
    def max(self) -> SlistSequenceStepRcountMax:
        """Return the ``SLISt:SEQuence:STEP:RCOunt:MAX`` command.

        Description:
            - This command returns the maximum number of repeats allowed for a step in a sequence.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP:RCOunt:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP:RCOunt:MAX?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP:RCOunt:MAX?
            ```
        """
        return self._max


class SlistSequenceStepMax(SCPICmdRead):
    """The ``SLISt:SEQuence:STEP:MAX`` command.

    Description:
        - This command returns the maximum number of steps allowed in a sequence.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP:MAX?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP:MAX?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP:MAX?
        ```
    """


class SlistSequenceStepAdd(SCPICmdWrite):
    """The ``SLISt:SEQuence:STEP:ADD`` command.

    Description:
        - This command adds steps to the named sequence. If the specified location is occupied, the
          step(s) are inserted prior to the specified step. If the specified location is the first
          unoccupied step in the sequence, the step(s) are appended to the sequence. If the
          specified location would result in a gap within the sequence, steps are added to bridge
          the gap in addition to the number of steps specified to add. For example, if you have a
          sequence with 25 steps, and you specify to add 5 steps beginning at location 30, steps
          will be added to fill the gap between steps 25 and 30.

    Usage:
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:STEP:ADD value``
          command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:STEP:ADD <sequence_name>,<location>[,<steps to add>]
        ```
    """


class SlistSequenceStep(SCPICmdRead):
    """The ``SLISt:SEQuence:STEP`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.add``: The ``SLISt:SEQuence:STEP:ADD`` command.
        - ``.max``: The ``SLISt:SEQuence:STEP:MAX`` command.
        - ``.rcount``: The ``SLISt:SEQuence:STEP:RCOunt`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._add = SlistSequenceStepAdd(device, f"{self._cmd_syntax}:ADD")
        self._max = SlistSequenceStepMax(device, f"{self._cmd_syntax}:MAX")
        self._rcount = SlistSequenceStepRcount(device, f"{self._cmd_syntax}:RCOunt")

    @property
    def add(self) -> SlistSequenceStepAdd:
        """Return the ``SLISt:SEQuence:STEP:ADD`` command.

        Description:
            - This command adds steps to the named sequence. If the specified location is occupied,
              the step(s) are inserted prior to the specified step. If the specified location is the
              first unoccupied step in the sequence, the step(s) are appended to the sequence. If
              the specified location would result in a gap within the sequence, steps are added to
              bridge the gap in addition to the number of steps specified to add. For example, if
              you have a sequence with 25 steps, and you specify to add 5 steps beginning at
              location 30, steps will be added to fill the gap between steps 25 and 30.

        Usage:
            - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:STEP:ADD value``
              command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP:ADD <sequence_name>,<location>[,<steps to add>]
            ```
        """
        return self._add

    @property
    def max(self) -> SlistSequenceStepMax:
        """Return the ``SLISt:SEQuence:STEP:MAX`` command.

        Description:
            - This command returns the maximum number of steps allowed in a sequence.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP:MAX?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP:MAX?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:STEP:MAX?
            ```
        """
        return self._max

    @property
    def rcount(self) -> SlistSequenceStepRcount:
        """Return the ``SLISt:SEQuence:STEP:RCOunt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP:RCOunt?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP:RCOunt?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.max``: The ``SLISt:SEQuence:STEP:RCOunt:MAX`` command.
        """
        return self._rcount


class SlistSequenceSrate(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:SRATe`` command.

    Description:
        - The command sets or returns the Recommended Sampling Rate of the specified sequence.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:SRATe? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:SRATe? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:SRATe value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:SRATe <sequence_name>,<sample_rate>
        - SLISt:SEQuence:SRATe? <sequence_name>
        ```
    """


class SlistSequenceRflag(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:RFLag`` command.

    Description:
        - This command sets or returns the Enable Flag Repeat value for the sequence. If the value
          is ON, then the flags will change each time that the step plays out. For example if Wfm1
          is at a step in Sequence with repeat 2 and one of the flags is set to Toggle, then the
          flag state will toggle twice at this step if the Enable Flag Repeat value is ON.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:RFLag? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:RFLag? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:RFLag value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:RFLag <sequence_name>, {0|1|OFF|ON}
        - SLISt:SEQuence:RFLag? <sequence_name>
        ```
    """


class SlistSequenceOffset(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:OFFSet`` command.

    Description:
        - The command sets or returns the Recommended Offset of the specified sequence.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:OFFSet? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:OFFSet? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:OFFSet value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:OFFSet <sequence_name>,<offset>
        - SLISt:SEQuence:OFFSet? <sequence_name>
        ```
    """


class SlistSequenceNew(SCPICmdWrite):
    """The ``SLISt:SEQuence:NEW`` command.

    Description:
        - This command creates a new sequence with the selected name, number of steps, and number of
          tracks.

    Usage:
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:NEW value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:NEW <sequence_name>,<number_of_steps>[,<number_of_tracks>]
        ```
    """


class SlistSequenceLength(SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:LENGth`` command.

    Description:
        - This command returns the total number of steps in the named sequence.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:LENGth? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:LENGth? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:LENGth? <sequence_name>
        ```
    """


class SlistSequenceFrequency(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:FREQuency`` command.

    Description:
        - The command sets or returns the recommended frequency of the specified sequence when the
          sequence contains IQ waveforms.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:FREQuency? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:FREQuency? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:FREQuency value``
          command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:FREQuency <seq_name>,<frequency>
        - SLISt:SEQuence:FREQuency? <seq_name>
        ```
    """


class SlistSequenceEventPjumpSize(SCPICmdRead):
    """The ``SLISt:SEQuence:EVENt:PJUMp:SIZE`` command.

    Description:
        - This command returns the maximum number of entries in the pattern jump table.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence:EVENt:PJUMp:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:EVENt:PJUMp:SIZE?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:EVENt:PJUMp:SIZE?
        ```
    """


class SlistSequenceEventPjumpEnable(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:EVENt:PJUMp:ENABle`` command.

    Description:
        - This command sets or returns the Event Pattern Jump state (enabled or disabled) for the
          named sequence. When enabled, the data at the Pattern Jump In connector can be strobed in,
          causing a sequence to jump to a defined step. The sequence and step are defined with the
          command ``SLIST:SEQUENCE:EVENT:PJUMP:DEFINE``.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:EVENt:PJUMp:ENABle? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:EVENt:PJUMp:ENABle? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SLISt:SEQuence:EVENt:PJUMp:ENABle value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:EVENt:PJUMp:ENABle <sequence_name>, {0|1|OFF|ON}
        - SLISt:SEQuence:EVENt:PJUMp:ENABle? <sequence_name>
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class SlistSequenceEventPjumpDefine(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:EVENt:PJUMp:DEFine`` command.

    Description:
        - This command associates an event pattern with the jump-to-step for Pattern Jump. The query
          returns the jump step associated to the specified pattern. The event pattern is read from
          the Pattern Jump In connector on the rear panel. Eight bits of data and a strobe are
          required. When the strobed event pattern is received, an event pattern jump is created,
          moving the sequence to the step defined in this command.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:EVENt:PJUMp:DEFine? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:EVENt:PJUMp:DEFine? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``SLISt:SEQuence:EVENt:PJUMp:DEFine value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:EVENt:PJUMp:DEFine <sequence_name>, <pattern>, <jump_step>
        - SLISt:SEQuence:EVENt:PJUMp:DEFine? <sequence_name>, <pattern>
        ```
    """


class SlistSequenceEventPjump(SCPICmdRead):
    """The ``SLISt:SEQuence:EVENt:PJUMp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence:EVENt:PJUMp?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:EVENt:PJUMp?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.define``: The ``SLISt:SEQuence:EVENt:PJUMp:DEFine`` command.
        - ``.enable``: The ``SLISt:SEQuence:EVENt:PJUMp:ENABle`` command.
        - ``.size``: The ``SLISt:SEQuence:EVENt:PJUMp:SIZE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._define = SlistSequenceEventPjumpDefine(device, f"{self._cmd_syntax}:DEFine")
        self._enable = SlistSequenceEventPjumpEnable(device, f"{self._cmd_syntax}:ENABle")
        self._size = SlistSequenceEventPjumpSize(device, f"{self._cmd_syntax}:SIZE")

    @property
    def define(self) -> SlistSequenceEventPjumpDefine:
        """Return the ``SLISt:SEQuence:EVENt:PJUMp:DEFine`` command.

        Description:
            - This command associates an event pattern with the jump-to-step for Pattern Jump. The
              query returns the jump step associated to the specified pattern. The event pattern is
              read from the Pattern Jump In connector on the rear panel. Eight bits of data and a
              strobe are required. When the strobed event pattern is received, an event pattern jump
              is created, moving the sequence to the step defined in this command.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:EVENt:PJUMp:DEFine? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:EVENt:PJUMp:DEFine? argument`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:EVENt:PJUMp:DEFine value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:EVENt:PJUMp:DEFine <sequence_name>, <pattern>, <jump_step>
            - SLISt:SEQuence:EVENt:PJUMp:DEFine? <sequence_name>, <pattern>
            ```
        """
        return self._define

    @property
    def enable(self) -> SlistSequenceEventPjumpEnable:
        """Return the ``SLISt:SEQuence:EVENt:PJUMp:ENABle`` command.

        Description:
            - This command sets or returns the Event Pattern Jump state (enabled or disabled) for
              the named sequence. When enabled, the data at the Pattern Jump In connector can be
              strobed in, causing a sequence to jump to a defined step. The sequence and step are
              defined with the command ``SLIST:SEQUENCE:EVENT:PJUMP:DEFINE``.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:EVENt:PJUMp:ENABle? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:EVENt:PJUMp:ENABle? argument`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:EVENt:PJUMp:ENABle value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:EVENt:PJUMp:ENABle <sequence_name>, {0|1|OFF|ON}
            - SLISt:SEQuence:EVENt:PJUMp:ENABle? <sequence_name>
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._enable

    @property
    def size(self) -> SlistSequenceEventPjumpSize:
        """Return the ``SLISt:SEQuence:EVENt:PJUMp:SIZE`` command.

        Description:
            - This command returns the maximum number of entries in the pattern jump table.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence:EVENt:PJUMp:SIZE?``
              query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:EVENt:PJUMp:SIZE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:EVENt:PJUMp:SIZE?
            ```
        """
        return self._size


class SlistSequenceEventJtiming(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:EVENt:JTIMing`` command.

    Description:
        - This command sets or returns the condition of when the sequencer jumps upon a logic event,
          pattern jump, or software forced jump. The jump can occur immediately or at the end of the
          current sequence step.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``SLISt:SEQuence:EVENt:JTIMing? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:EVENt:JTIMing? argument`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:EVENt:JTIMing value``
          command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:EVENt:JTIMing <sequence_name>, {END|IMMediate}
        - SLISt:SEQuence:EVENt:JTIMing? <sequence_name>
        ```

    Info:
        - ``END`` - on receiving an event, wait until the end of current step before jumping to
          specified event jump step IMMediate - on receiving an event, immediately jump to specified
          event jump step.
    """


class SlistSequenceEvent(SCPICmdRead):
    """The ``SLISt:SEQuence:EVENt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence:EVENt?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:EVENt?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.jtiming``: The ``SLISt:SEQuence:EVENt:JTIMing`` command.
        - ``.pjump``: The ``SLISt:SEQuence:EVENt:PJUMp`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._jtiming = SlistSequenceEventJtiming(device, f"{self._cmd_syntax}:JTIMing")
        self._pjump = SlistSequenceEventPjump(device, f"{self._cmd_syntax}:PJUMp")

    @property
    def jtiming(self) -> SlistSequenceEventJtiming:
        """Return the ``SLISt:SEQuence:EVENt:JTIMing`` command.

        Description:
            - This command sets or returns the condition of when the sequencer jumps upon a logic
              event, pattern jump, or software forced jump. The jump can occur immediately or at the
              end of the current sequence step.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:EVENt:JTIMing? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:EVENt:JTIMing? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``SLISt:SEQuence:EVENt:JTIMing value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:EVENt:JTIMing <sequence_name>, {END|IMMediate}
            - SLISt:SEQuence:EVENt:JTIMing? <sequence_name>
            ```

        Info:
            - ``END`` - on receiving an event, wait until the end of current step before jumping to
              specified event jump step IMMediate - on receiving an event, immediately jump to
              specified event jump step.
        """
        return self._jtiming

    @property
    def pjump(self) -> SlistSequenceEventPjump:
        """Return the ``SLISt:SEQuence:EVENt:PJUMp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence:EVENt:PJUMp?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:EVENt:PJUMp?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.define``: The ``SLISt:SEQuence:EVENt:PJUMp:DEFine`` command.
            - ``.enable``: The ``SLISt:SEQuence:EVENt:PJUMp:ENABle`` command.
            - ``.size``: The ``SLISt:SEQuence:EVENt:PJUMp:SIZE`` command.
        """
        return self._pjump


class SlistSequenceDelete(SCPICmdWrite):
    """The ``SLISt:SEQuence:DELete`` command.

    Description:
        - This command deletes a specific sequence or all sequences from the sequence list.

    Usage:
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:DELete value`` command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:DELete {<sequence_name>|ALL}
        ```
    """


class SlistSequenceAmplitude(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``SLISt:SEQuence:AMPLitude`` command.

    Description:
        - The command sets or returns the Recommended Amplitude (peak-to-peak) of the specified
          sequence.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:AMPLitude? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``SLISt:SEQuence:AMPLitude? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:AMPLitude value``
          command.

    SCPI Syntax:
        ```
        - SLISt:SEQuence:AMPLitude <sequence_name>,<amplitude>
        - SLISt:SEQuence:AMPLitude? <sequence_name>
        ```
    """


#  pylint: disable=too-many-instance-attributes
class SlistSequence(SCPICmdRead):
    """The ``SLISt:SEQuence`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt:SEQuence?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``SLISt:SEQuence:AMPLitude`` command.
        - ``.delete``: The ``SLISt:SEQuence:DELete`` command.
        - ``.event``: The ``SLISt:SEQuence:EVENt`` command tree.
        - ``.frequency``: The ``SLISt:SEQuence:FREQuency`` command.
        - ``.length``: The ``SLISt:SEQuence:LENGth`` command.
        - ``.new``: The ``SLISt:SEQuence:NEW`` command.
        - ``.offset``: The ``SLISt:SEQuence:OFFSet`` command.
        - ``.rflag``: The ``SLISt:SEQuence:RFLag`` command.
        - ``.srate``: The ``SLISt:SEQuence:SRATe`` command.
        - ``.step``: The ``SLISt:SEQuence:STEP`` command tree.
        - ``.stepx``: The ``SLISt:SEQuence:STEP[n]`` command tree.
        - ``.track``: The ``SLISt:SEQuence:TRACk`` command.
        - ``.tstamp``: The ``SLISt:SEQuence:TSTamp`` command.
        - ``.wmusage``: The ``SLISt:SEQuence:WMUSage`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = SlistSequenceAmplitude(device, f"{self._cmd_syntax}:AMPLitude")
        self._delete = SlistSequenceDelete(device, f"{self._cmd_syntax}:DELete")
        self._event = SlistSequenceEvent(device, f"{self._cmd_syntax}:EVENt")
        self._frequency = SlistSequenceFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._length = SlistSequenceLength(device, f"{self._cmd_syntax}:LENGth")
        self._new = SlistSequenceNew(device, f"{self._cmd_syntax}:NEW")
        self._offset = SlistSequenceOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._rflag = SlistSequenceRflag(device, f"{self._cmd_syntax}:RFLag")
        self._srate = SlistSequenceSrate(device, f"{self._cmd_syntax}:SRATe")
        self._step = SlistSequenceStep(device, f"{self._cmd_syntax}:STEP")
        self._stepx: Dict[int, SlistSequenceStepItem] = DefaultDictPassKeyToFactory(
            lambda x: SlistSequenceStepItem(device, f"{self._cmd_syntax}:STEP{x}")
        )
        self._track = SlistSequenceTrack(device, f"{self._cmd_syntax}:TRACk")
        self._tstamp = SlistSequenceTstamp(device, f"{self._cmd_syntax}:TSTamp")
        self._wmusage = SlistSequenceWmusage(device, f"{self._cmd_syntax}:WMUSage")

    @property
    def amplitude(self) -> SlistSequenceAmplitude:
        """Return the ``SLISt:SEQuence:AMPLitude`` command.

        Description:
            - The command sets or returns the Recommended Amplitude (peak-to-peak) of the specified
              sequence.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:AMPLitude? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:AMPLitude? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:AMPLitude value``
              command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:AMPLitude <sequence_name>,<amplitude>
            - SLISt:SEQuence:AMPLitude? <sequence_name>
            ```
        """
        return self._amplitude

    @property
    def delete(self) -> SlistSequenceDelete:
        """Return the ``SLISt:SEQuence:DELete`` command.

        Description:
            - This command deletes a specific sequence or all sequences from the sequence list.

        Usage:
            - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:DELete value``
              command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:DELete {<sequence_name>|ALL}
            ```
        """
        return self._delete

    @property
    def event(self) -> SlistSequenceEvent:
        """Return the ``SLISt:SEQuence:EVENt`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence:EVENt?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:EVENt?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.jtiming``: The ``SLISt:SEQuence:EVENt:JTIMing`` command.
            - ``.pjump``: The ``SLISt:SEQuence:EVENt:PJUMp`` command tree.
        """
        return self._event

    @property
    def frequency(self) -> SlistSequenceFrequency:
        """Return the ``SLISt:SEQuence:FREQuency`` command.

        Description:
            - The command sets or returns the recommended frequency of the specified sequence when
              the sequence contains IQ waveforms.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:FREQuency? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:FREQuency? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:FREQuency value``
              command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:FREQuency <seq_name>,<frequency>
            - SLISt:SEQuence:FREQuency? <seq_name>
            ```
        """
        return self._frequency

    @property
    def length(self) -> SlistSequenceLength:
        """Return the ``SLISt:SEQuence:LENGth`` command.

        Description:
            - This command returns the total number of steps in the named sequence.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:LENGth? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:LENGth? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:LENGth? <sequence_name>
            ```
        """
        return self._length

    @property
    def new(self) -> SlistSequenceNew:
        """Return the ``SLISt:SEQuence:NEW`` command.

        Description:
            - This command creates a new sequence with the selected name, number of steps, and
              number of tracks.

        Usage:
            - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:NEW value`` command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:NEW <sequence_name>,<number_of_steps>[,<number_of_tracks>]
            ```
        """
        return self._new

    @property
    def offset(self) -> SlistSequenceOffset:
        """Return the ``SLISt:SEQuence:OFFSet`` command.

        Description:
            - The command sets or returns the Recommended Offset of the specified sequence.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:OFFSet? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:OFFSet? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:OFFSet value``
              command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:OFFSet <sequence_name>,<offset>
            - SLISt:SEQuence:OFFSet? <sequence_name>
            ```
        """
        return self._offset

    @property
    def rflag(self) -> SlistSequenceRflag:
        """Return the ``SLISt:SEQuence:RFLag`` command.

        Description:
            - This command sets or returns the Enable Flag Repeat value for the sequence. If the
              value is ON, then the flags will change each time that the step plays out. For example
              if Wfm1 is at a step in Sequence with repeat 2 and one of the flags is set to Toggle,
              then the flag state will toggle twice at this step if the Enable Flag Repeat value is
              ON.

        Usage:
            - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:RFLag? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:RFLag? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:RFLag value``
              command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:RFLag <sequence_name>, {0|1|OFF|ON}
            - SLISt:SEQuence:RFLag? <sequence_name>
            ```
        """
        return self._rflag

    @property
    def srate(self) -> SlistSequenceSrate:
        """Return the ``SLISt:SEQuence:SRATe`` command.

        Description:
            - The command sets or returns the Recommended Sampling Rate of the specified sequence.

        Usage:
            - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:SRATe? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:SRATe? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SLISt:SEQuence:SRATe value``
              command.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:SRATe <sequence_name>,<sample_rate>
            - SLISt:SEQuence:SRATe? <sequence_name>
            ```
        """
        return self._srate

    @property
    def step(self) -> SlistSequenceStep:
        """Return the ``SLISt:SEQuence:STEP`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.add``: The ``SLISt:SEQuence:STEP:ADD`` command.
            - ``.max``: The ``SLISt:SEQuence:STEP:MAX`` command.
            - ``.rcount``: The ``SLISt:SEQuence:STEP:RCOunt`` command tree.
        """
        return self._step

    @property
    def stepx(self) -> Dict[int, SlistSequenceStepItem]:
        """Return the ``SLISt:SEQuence:STEP[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence:STEP[n]?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence:STEP[n]?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ejinput``: The ``SLISt:SEQuence:STEP[n]:EJINput`` command.
            - ``.ejump``: The ``SLISt:SEQuence:STEP[n]:EJUMp`` command.
            - ``.goto``: The ``SLISt:SEQuence:STEP[n]:GOTO`` command.
            - ``.rcount``: The ``SLISt:SEQuence:STEP[n]:RCOunt`` command.
            - ``.tasset``: The ``SLISt:SEQuence:STEP[n]:TASSet`` command tree.
            - ``.tassetx``: The ``SLISt:SEQuence:STEP[n]:TASSet[m]`` command.
            - ``.tflag``: The ``SLISt:SEQuence:STEP[n]:TFLag[m]`` command tree.
            - ``.winput``: The ``SLISt:SEQuence:STEP[n]:WINPut`` command.
        """
        return self._stepx

    @property
    def track(self) -> SlistSequenceTrack:
        """Return the ``SLISt:SEQuence:TRACk`` command.

        Description:
            - This command returns the number of tracks defined in the specified sequence.

        Usage:
            - Using the ``.query(argument)`` method will send the ``SLISt:SEQuence:TRACk? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:TRACk? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:TRACk? <sequence_name>
            ```

        Sub-properties:
            - ``.max``: The ``SLISt:SEQuence:TRACk:MAX`` command.
        """
        return self._track

    @property
    def tstamp(self) -> SlistSequenceTstamp:
        """Return the ``SLISt:SEQuence:TSTamp`` command.

        Description:
            - This command returns the timestamp of the named sequence. Every sequence has a
              timestamp that indicates when the sequence was created or last modified.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:TSTamp? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:TSTamp? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:TSTamp? <sequence_name>
            ```
        """
        return self._tstamp

    @property
    def wmusage(self) -> SlistSequenceWmusage:
        """Return the ``SLISt:SEQuence:WMUSage`` command.

        Description:
            - This command returns the total waveform memory usage (in sample points) for the
              specified sequence track for the named sequence.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``SLISt:SEQuence:WMUSage? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``SLISt:SEQuence:WMUSage? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:SEQuence:WMUSage? <sequence_name>,<track_number>
            ```
        """
        return self._wmusage


class SlistName(SCPICmdReadWithArguments):
    """The ``SLISt:NAME`` command.

    Description:
        - This command returns the name of the sequence at the specified sequence list index.

    Usage:
        - Using the ``.query(argument)`` method will send the ``SLISt:NAME? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``SLISt:NAME? argument`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SLISt:NAME? <sequence_list_index>
        ```
    """


class Slist(SCPICmdRead):
    """The ``SLISt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SLISt?`` query.
        - Using the ``.verify(value)`` method will send the ``SLISt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.name``: The ``SLISt:NAME`` command.
        - ``.sequence``: The ``SLISt:SEQuence`` command tree.
        - ``.size``: The ``SLISt:SIZE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SLISt") -> None:
        super().__init__(device, cmd_syntax)
        self._name = SlistName(device, f"{self._cmd_syntax}:NAME")
        self._sequence = SlistSequence(device, f"{self._cmd_syntax}:SEQuence")
        self._size = SlistSize(device, f"{self._cmd_syntax}:SIZE")

    @property
    def name(self) -> SlistName:
        """Return the ``SLISt:NAME`` command.

        Description:
            - This command returns the name of the sequence at the specified sequence list index.

        Usage:
            - Using the ``.query(argument)`` method will send the ``SLISt:NAME? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``SLISt:NAME? argument``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SLISt:NAME? <sequence_list_index>
            ```
        """
        return self._name

    @property
    def sequence(self) -> SlistSequence:
        """Return the ``SLISt:SEQuence`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SLISt:SEQuence?`` query.
            - Using the ``.verify(value)`` method will send the ``SLISt:SEQuence?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``SLISt:SEQuence:AMPLitude`` command.
            - ``.delete``: The ``SLISt:SEQuence:DELete`` command.
            - ``.event``: The ``SLISt:SEQuence:EVENt`` command tree.
            - ``.frequency``: The ``SLISt:SEQuence:FREQuency`` command.
            - ``.length``: The ``SLISt:SEQuence:LENGth`` command.
            - ``.new``: The ``SLISt:SEQuence:NEW`` command.
            - ``.offset``: The ``SLISt:SEQuence:OFFSet`` command.
            - ``.rflag``: The ``SLISt:SEQuence:RFLag`` command.
            - ``.srate``: The ``SLISt:SEQuence:SRATe`` command.
            - ``.step``: The ``SLISt:SEQuence:STEP`` command tree.
            - ``.stepx``: The ``SLISt:SEQuence:STEP[n]`` command tree.
            - ``.track``: The ``SLISt:SEQuence:TRACk`` command.
            - ``.tstamp``: The ``SLISt:SEQuence:TSTamp`` command.
            - ``.wmusage``: The ``SLISt:SEQuence:WMUSage`` command.
        """
        return self._sequence

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
