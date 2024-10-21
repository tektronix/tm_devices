"""The actonevent commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ACTONEVent:ENable <NR1>
    - ACTONEVent:ENable?
    - ACTONEVent:LIMITCount <NR1>
    - ACTONEVent:LIMITCount?
    - ACTONEVent:LIMit <NR1>
    - ACTONEVent:LIMit?
    - ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE?
    - ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE?
    - ACTONEVent:MASKFail:ACTION:SRQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKFail:ACTION:SRQ:STATE?
    - ACTONEVent:MASKFail:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKFail:ACTION:STOPACQ:STATE?
    - ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE?
    - ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE?
    - ACTONEVent:MASKHit:ACTION:SRQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKHit:ACTION:SRQ:STATE?
    - ACTONEVent:MASKHit:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKHit:ACTION:STOPACQ:STATE?
    - ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE?
    - ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE?
    - ACTONEVent:MASKPass:ACTION:SRQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKPass:ACTION:SRQ:STATE?
    - ACTONEVent:MASKPass:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MASKPass:ACTION:STOPACQ:STATE?
    - ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE?
    - ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE?
    - ACTONEVent:MEASUrement:ACTION:SRQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MEASUrement:ACTION:SRQ:STATE?
    - ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE?
    - ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
    - ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE?
    - ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
    - ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE?
    - ACTONEVent:SEARCH:ACTION:SRQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:SEARCH:ACTION:SRQ:STATE?
    - ACTONEVent:SEARCH:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:SEARCH:ACTION:STOPACQ:STATE?
    - ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
    - ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE?
    - ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
    - ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE?
    - ACTONEVent:TRIGger:ACTION:SRQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:TRIGger:ACTION:SRQ:STATE?
    - ACTONEVent:TRIGger:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
    - ACTONEVent:TRIGger:ACTION:STOPACQ:STATE?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ActoneventTriggerActionStopacqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:TRIGger:ACTION:STOPACQ:STATE`` command.

    Description:
        - This command stops acquisitions on a trigger event from a single sequence or sequence of N
          acquisition. Each acquisition in the sequence of N will perform a save operation.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION:STOPACQ:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:TRIGger:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:TRIGger:ACTION:STOPACQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:TRIGger:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:TRIGger:ACTION:STOPACQ:STATE?
        ```

    Info:
        - ``ON`` enables the stop acquisitions on a trigger event feature.
        - ``OFF`` disables the stop acquisitions on a trigger event feature.
        - ``<NR1>`` is a number that enables or disables the stop acquisitions on a trigger event
          feature. The number zero disables the feature, all other numbers enable the feature.
    """


class ActoneventTriggerActionStopacq(SCPICmdRead):
    """The ``ACTONEVent:TRIGger:ACTION:STOPACQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION:STOPACQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TRIGger:ACTION:STOPACQ?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:TRIGger:ACTION:STOPACQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventTriggerActionStopacqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventTriggerActionStopacqState:
        """Return the ``ACTONEVent:TRIGger:ACTION:STOPACQ:STATE`` command.

        Description:
            - This command stops acquisitions on a trigger event from a single sequence or sequence
              of N acquisition. Each acquisition in the sequence of N will perform a save operation.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:TRIGger:ACTION:STOPACQ:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TRIGger:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:TRIGger:ACTION:STOPACQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:TRIGger:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:TRIGger:ACTION:STOPACQ:STATE?
            ```

        Info:
            - ``ON`` enables the stop acquisitions on a trigger event feature.
            - ``OFF`` disables the stop acquisitions on a trigger event feature.
            - ``<NR1>`` is a number that enables or disables the stop acquisitions on a trigger
              event feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventTriggerActionSrqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:TRIGger:ACTION:SRQ:STATE`` command.

    Description:
        - This command generates an SRQ event when a trigger event occurs.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION:SRQ:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TRIGger:ACTION:SRQ:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:TRIGger:ACTION:SRQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:TRIGger:ACTION:SRQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:TRIGger:ACTION:SRQ:STATE?
        ```

    Info:
        - ``ON`` enables the generate an SRQ event when a trigger event occurs feature.
        - ``OFF`` disables the generate an SRQ event when a trigger event occurs feature.
        - ``<NR1>`` is a number that enables or disables the generate an SRQ event when a trigger
          event occurs feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventTriggerActionSrq(SCPICmdRead):
    """The ``ACTONEVent:TRIGger:ACTION:SRQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TRIGger:ACTION:SRQ?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:TRIGger:ACTION:SRQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventTriggerActionSrqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventTriggerActionSrqState:
        """Return the ``ACTONEVent:TRIGger:ACTION:SRQ:STATE`` command.

        Description:
            - This command generates an SRQ event when a trigger event occurs.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION:SRQ:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TRIGger:ACTION:SRQ:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:TRIGger:ACTION:SRQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:TRIGger:ACTION:SRQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:TRIGger:ACTION:SRQ:STATE?
            ```

        Info:
            - ``ON`` enables the generate an SRQ event when a trigger event occurs feature.
            - ``OFF`` disables the generate an SRQ event when a trigger event occurs feature.
            - ``<NR1>`` is a number that enables or disables the generate an SRQ event when a
              trigger event occurs feature. The number zero disables the feature, all other numbers
              enable the feature.
        """
        return self._state


class ActoneventTriggerActionSavewaveformState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE`` command.

    Description:
        - This command saves the user set source waveform(s) on a trigger event from a single
          sequence or sequence of N acquisition. Each acquisition in the sequence of N will perform
          a save operation. This command replaces ``SAVEON:WAVEFORM`` (still valid command, but only
          an alias for this new command).

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
        - ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE?
        ```

    Info:
        - ``ON`` enables the save source waveform(s) on a trigger event feature.
        - ``OFF`` disables the save source waveform(s) on a trigger event feature.
        - ``<NR1>`` is a number that enables or disables the save source waveform(s) on a trigger
          event feature. The number zero disables the feature, all other numbers enable the feature.
    """


class ActoneventTriggerActionSavewaveform(SCPICmdRead):
    """The ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventTriggerActionSavewaveformState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventTriggerActionSavewaveformState:
        """Return the ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE`` command.

        Description:
            - This command saves the user set source waveform(s) on a trigger event from a single
              sequence or sequence of N acquisition. Each acquisition in the sequence of N will
              perform a save operation. This command replaces ``SAVEON:WAVEFORM`` (still valid
              command, but only an alias for this new command).

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
            - ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE?
            ```

        Info:
            - ``ON`` enables the save source waveform(s) on a trigger event feature.
            - ``OFF`` disables the save source waveform(s) on a trigger event feature.
            - ``<NR1>`` is a number that enables or disables the save source waveform(s) on a
              trigger event feature. The number zero disables the feature, all other numbers enable
              the feature.
        """
        return self._state


class ActoneventTriggerActionSaveimageState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE`` command.

    Description:
        - This command saves a screen capture on a trigger event from a single sequence or sequence
          of N acquisition. Each acquisition in the sequence of N will perform a save operation.
          This command replaces ``SAVE:IMAGE`` (still valid command, but only an alias for this new
          command).

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
        - ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE?
        ```

    Info:
        - ``ON`` enables the save screen capture on a trigger event feature.
        - ``OFF`` disables the save screen capture on a trigger event feature.
        - ``<NR1>`` is a number that enables or disables the save screen capture on a trigger event
          feature. The number zero disables the feature, all other numbers enable the feature.
    """


class ActoneventTriggerActionSaveimage(SCPICmdRead):
    """The ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe?``
          query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventTriggerActionSaveimageState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventTriggerActionSaveimageState:
        """Return the ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE`` command.

        Description:
            - This command saves a screen capture on a trigger event from a single sequence or
              sequence of N acquisition. Each acquisition in the sequence of N will perform a save
              operation. This command replaces ``SAVE:IMAGE`` (still valid command, but only an
              alias for this new command).

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
            - ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE?
            ```

        Info:
            - ``ON`` enables the save screen capture on a trigger event feature.
            - ``OFF`` disables the save screen capture on a trigger event feature.
            - ``<NR1>`` is a number that enables or disables the save screen capture on a trigger
              event feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventTriggerAction(SCPICmdRead):
    """The ``ACTONEVent:TRIGger:ACTION`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TRIGger:ACTION?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.saveimage``: The ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe`` command tree.
        - ``.savewaveform``: The ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform`` command tree.
        - ``.srq``: The ``ACTONEVent:TRIGger:ACTION:SRQ`` command tree.
        - ``.stopacq``: The ``ACTONEVent:TRIGger:ACTION:STOPACQ`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._saveimage = ActoneventTriggerActionSaveimage(device, f"{self._cmd_syntax}:SAVEIMAGe")
        self._savewaveform = ActoneventTriggerActionSavewaveform(
            device, f"{self._cmd_syntax}:SAVEWAVEform"
        )
        self._srq = ActoneventTriggerActionSrq(device, f"{self._cmd_syntax}:SRQ")
        self._stopacq = ActoneventTriggerActionStopacq(device, f"{self._cmd_syntax}:STOPACQ")

    @property
    def saveimage(self) -> ActoneventTriggerActionSaveimage:
        """Return the ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe:STATE`` command.
        """
        return self._saveimage

    @property
    def savewaveform(self) -> ActoneventTriggerActionSavewaveform:
        """Return the ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform:STATE`` command.
        """
        return self._savewaveform

    @property
    def srq(self) -> ActoneventTriggerActionSrq:
        """Return the ``ACTONEVent:TRIGger:ACTION:SRQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION:SRQ?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:TRIGger:ACTION:SRQ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:TRIGger:ACTION:SRQ:STATE`` command.
        """
        return self._srq

    @property
    def stopacq(self) -> ActoneventTriggerActionStopacq:
        """Return the ``ACTONEVent:TRIGger:ACTION:STOPACQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION:STOPACQ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TRIGger:ACTION:STOPACQ?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:TRIGger:ACTION:STOPACQ:STATE`` command.
        """
        return self._stopacq


class ActoneventTrigger(SCPICmdRead):
    """The ``ACTONEVent:TRIGger`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TRIGger?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.action``: The ``ACTONEVent:TRIGger:ACTION`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._action = ActoneventTriggerAction(device, f"{self._cmd_syntax}:ACTION")

    @property
    def action(self) -> ActoneventTriggerAction:
        """Return the ``ACTONEVent:TRIGger:ACTION`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger:ACTION?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:TRIGger:ACTION?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.saveimage``: The ``ACTONEVent:TRIGger:ACTION:SAVEIMAGe`` command tree.
            - ``.savewaveform``: The ``ACTONEVent:TRIGger:ACTION:SAVEWAVEform`` command tree.
            - ``.srq``: The ``ACTONEVent:TRIGger:ACTION:SRQ`` command tree.
            - ``.stopacq``: The ``ACTONEVent:TRIGger:ACTION:STOPACQ`` command tree.
        """
        return self._action


class ActoneventSearchActionStopacqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:SEARCH:ACTION:STOPACQ:STATE`` command.

    Description:
        - This command stops acquisitions when a search event is found.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:STOPACQ:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:SEARCH:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:SEARCH:ACTION:STOPACQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:SEARCH:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:SEARCH:ACTION:STOPACQ:STATE?
        ```

    Info:
        - ``ON`` enables the stop acquisitions when a search event is found feature.
        - ``OFF`` disables the stop acquisitions when a search event is found feature.
        - ``<NR1>`` is a number that enables or disables the stop acquisitions when a search event
          is found feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventSearchActionStopacq(SCPICmdRead):
    """The ``ACTONEVent:SEARCH:ACTION:STOPACQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:STOPACQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:SEARCH:ACTION:STOPACQ?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:SEARCH:ACTION:STOPACQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventSearchActionStopacqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventSearchActionStopacqState:
        """Return the ``ACTONEVent:SEARCH:ACTION:STOPACQ:STATE`` command.

        Description:
            - This command stops acquisitions when a search event is found.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:SEARCH:ACTION:STOPACQ:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:SEARCH:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:SEARCH:ACTION:STOPACQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:SEARCH:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:SEARCH:ACTION:STOPACQ:STATE?
            ```

        Info:
            - ``ON`` enables the stop acquisitions when a search event is found feature.
            - ``OFF`` disables the stop acquisitions when a search event is found feature.
            - ``<NR1>`` is a number that enables or disables the stop acquisitions when a search
              event is found feature. The number zero disables the feature, all other numbers enable
              the feature.
        """
        return self._state


class ActoneventSearchActionSrqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:SEARCH:ACTION:SRQ:STATE`` command.

    Description:
        - This command generates an SRQ event when any search event is found.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:SRQ:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:SEARCH:ACTION:SRQ:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:SEARCH:ACTION:SRQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:SEARCH:ACTION:SRQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:SEARCH:ACTION:SRQ:STATE?
        ```

    Info:
        - ``ON`` enables the generate an SRQ event when any search event is found feature.
        - ``OFF`` disables the generate an SRQ event when any search event is found feature.
        - ``<NR1>`` is a number that enables or disables the generate an SRQ event when any search
          event is found feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventSearchActionSrq(SCPICmdRead):
    """The ``ACTONEVent:SEARCH:ACTION:SRQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:SEARCH:ACTION:SRQ?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:SEARCH:ACTION:SRQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventSearchActionSrqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventSearchActionSrqState:
        """Return the ``ACTONEVent:SEARCH:ACTION:SRQ:STATE`` command.

        Description:
            - This command generates an SRQ event when any search event is found.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:SRQ:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:SEARCH:ACTION:SRQ:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:SEARCH:ACTION:SRQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:SEARCH:ACTION:SRQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:SEARCH:ACTION:SRQ:STATE?
            ```

        Info:
            - ``ON`` enables the generate an SRQ event when any search event is found feature.
            - ``OFF`` disables the generate an SRQ event when any search event is found feature.
            - ``<NR1>`` is a number that enables or disables the generate an SRQ event when any
              search event is found feature. The number zero disables the feature, all other numbers
              enable the feature.
        """
        return self._state


class ActoneventSearchActionSavewaveformState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE`` command.

    Description:
        - This command saves the user set source waveform(s) when a search event is found.

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
        - ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE?
        ```

    Info:
        - ``ON`` enables the save source waveform(s) when a search event is found feature.
        - ``OFF`` disables the save source waveform(s) when a search event is found feature.
        - ``<NR1>`` is a number that enables or disables the save source waveform(s) when a search
          event is found feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventSearchActionSavewaveform(SCPICmdRead):
    """The ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventSearchActionSavewaveformState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventSearchActionSavewaveformState:
        """Return the ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE`` command.

        Description:
            - This command saves the user set source waveform(s) when a search event is found.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
            - ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE?
            ```

        Info:
            - ``ON`` enables the save source waveform(s) when a search event is found feature.
            - ``OFF`` disables the save source waveform(s) when a search event is found feature.
            - ``<NR1>`` is a number that enables or disables the save source waveform(s) when a
              search event is found feature. The number zero disables the feature, all other numbers
              enable the feature.
        """
        return self._state


class ActoneventSearchActionSaveimageState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE`` command.

    Description:
        - This command saves a screen capture when a search event is found.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
        - ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE?
        ```

    Info:
        - ``ON`` enables the save screen capture when a search event is found feature.
        - ``OFF`` disables the save screen capture when a search event is found feature.
        - ``<NR1>`` is a number that enables or disables the save screen capture when a search event
          is found feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventSearchActionSaveimage(SCPICmdRead):
    """The ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventSearchActionSaveimageState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventSearchActionSaveimageState:
        """Return the ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE`` command.

        Description:
            - This command saves a screen capture when a search event is found.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
            - ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE?
            ```

        Info:
            - ``ON`` enables the save screen capture when a search event is found feature.
            - ``OFF`` disables the save screen capture when a search event is found feature.
            - ``<NR1>`` is a number that enables or disables the save screen capture when a search
              event is found feature. The number zero disables the feature, all other numbers enable
              the feature.
        """
        return self._state


class ActoneventSearchAction(SCPICmdRead):
    """The ``ACTONEVent:SEARCH:ACTION`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:SEARCH:ACTION?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.saveimage``: The ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe`` command tree.
        - ``.savewaveform``: The ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform`` command tree.
        - ``.srq``: The ``ACTONEVent:SEARCH:ACTION:SRQ`` command tree.
        - ``.stopacq``: The ``ACTONEVent:SEARCH:ACTION:STOPACQ`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._saveimage = ActoneventSearchActionSaveimage(device, f"{self._cmd_syntax}:SAVEIMAGe")
        self._savewaveform = ActoneventSearchActionSavewaveform(
            device, f"{self._cmd_syntax}:SAVEWAVEform"
        )
        self._srq = ActoneventSearchActionSrq(device, f"{self._cmd_syntax}:SRQ")
        self._stopacq = ActoneventSearchActionStopacq(device, f"{self._cmd_syntax}:STOPACQ")

    @property
    def saveimage(self) -> ActoneventSearchActionSaveimage:
        """Return the ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe:STATE`` command.
        """
        return self._saveimage

    @property
    def savewaveform(self) -> ActoneventSearchActionSavewaveform:
        """Return the ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform:STATE`` command.
        """
        return self._savewaveform

    @property
    def srq(self) -> ActoneventSearchActionSrq:
        """Return the ``ACTONEVent:SEARCH:ACTION:SRQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:SRQ?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:SEARCH:ACTION:SRQ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:SEARCH:ACTION:SRQ:STATE`` command.
        """
        return self._srq

    @property
    def stopacq(self) -> ActoneventSearchActionStopacq:
        """Return the ``ACTONEVent:SEARCH:ACTION:STOPACQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION:STOPACQ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:SEARCH:ACTION:STOPACQ?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:SEARCH:ACTION:STOPACQ:STATE`` command.
        """
        return self._stopacq


class ActoneventSearch(SCPICmdRead):
    """The ``ACTONEVent:SEARCH`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:SEARCH?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.action``: The ``ACTONEVent:SEARCH:ACTION`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._action = ActoneventSearchAction(device, f"{self._cmd_syntax}:ACTION")

    @property
    def action(self) -> ActoneventSearchAction:
        """Return the ``ACTONEVent:SEARCH:ACTION`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH:ACTION?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:SEARCH:ACTION?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.saveimage``: The ``ACTONEVent:SEARCH:ACTION:SAVEIMAGe`` command tree.
            - ``.savewaveform``: The ``ACTONEVent:SEARCH:ACTION:SAVEWAVEform`` command tree.
            - ``.srq``: The ``ACTONEVent:SEARCH:ACTION:SRQ`` command tree.
            - ``.stopacq``: The ``ACTONEVent:SEARCH:ACTION:STOPACQ`` command tree.
        """
        return self._action


class ActoneventMeasurementActionStopacqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE`` command.

    Description:
        - This command stops acquisitions when the user-set measurement limit is exceeded.

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE?
        ```

    Info:
        - ``ON`` enables the stop acquisitions when the measurement limit is exceeded feature.
        - ``OFF`` disables the stop acquisitions when the measurement limit is exceeded feature.
        - ``<NR1>`` is a number that enables or disables the stop acquisitions when the measurement
          limit is exceeded feature. The number zero disables the feature, all other numbers enable
          the feature.
    """


class ActoneventMeasurementActionStopacq(SCPICmdRead):
    """The ``ACTONEVent:MEASUrement:ACTION:STOPACQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MEASUrement:ACTION:STOPACQ?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:STOPACQ?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMeasurementActionStopacqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMeasurementActionStopacqState:
        """Return the ``ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE`` command.

        Description:
            - This command stops acquisitions when the user-set measurement limit is exceeded.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE?
            ```

        Info:
            - ``ON`` enables the stop acquisitions when the measurement limit is exceeded feature.
            - ``OFF`` disables the stop acquisitions when the measurement limit is exceeded feature.
            - ``<NR1>`` is a number that enables or disables the stop acquisitions when the
              measurement limit is exceeded feature. The number zero disables the feature, all other
              numbers enable the feature.
        """
        return self._state


class ActoneventMeasurementActionSrqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MEASUrement:ACTION:SRQ:STATE`` command.

    Description:
        - This command generates an SRQ event when any measurement triggers the user-defined
          measurement limits.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MEASUrement:ACTION:SRQ:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:SRQ:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:SRQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MEASUrement:ACTION:SRQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MEASUrement:ACTION:SRQ:STATE?
        ```

    Info:
        - ``ON`` enables the generate an SRQ event when any measurement triggers the user-defined
          measurement limits feature.
        - ``OFF`` disables the generate an SRQ event when any measurement triggers the user-defined
          measurement limits feature.
        - ``<NR1>`` is a number that enables or disables the generate an SRQ event when any
          measurement triggers the user-defined measurement limits feature. The number zero disables
          the feature, all other numbers enable the feature.
    """


class ActoneventMeasurementActionSrq(SCPICmdRead):
    """The ``ACTONEVent:MEASUrement:ACTION:SRQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MEASUrement:ACTION:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MEASUrement:ACTION:SRQ?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MEASUrement:ACTION:SRQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMeasurementActionSrqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMeasurementActionSrqState:
        """Return the ``ACTONEVent:MEASUrement:ACTION:SRQ:STATE`` command.

        Description:
            - This command generates an SRQ event when any measurement triggers the user-defined
              measurement limits.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SRQ:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SRQ:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SRQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MEASUrement:ACTION:SRQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MEASUrement:ACTION:SRQ:STATE?
            ```

        Info:
            - ``ON`` enables the generate an SRQ event when any measurement triggers the
              user-defined measurement limits feature.
            - ``OFF`` disables the generate an SRQ event when any measurement triggers the
              user-defined measurement limits feature.
            - ``<NR1>`` is a number that enables or disables the generate an SRQ event when any
              measurement triggers the user-defined measurement limits feature. The number zero
              disables the feature, all other numbers enable the feature.
        """
        return self._state


class ActoneventMeasurementActionSavewaveformState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE`` command.

    Description:
        - This command saves the user set source waveform(s) when the user-set measurement limit is
          exceeded.

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE?
        ```

    Info:
        - ``ON`` enables the save source waveform(s) when the measurement limit is exceeded feature.
        - ``OFF`` disables the save source waveform(s) when the measurement limit is exceeded
          feature.
        - ``<NR1>`` is a number that enables or disables the save source waveform(s) when the
          measurement limit is exceeded feature. The number zero disables the feature, all other
          numbers enable the feature.
    """


class ActoneventMeasurementActionSavewaveform(SCPICmdRead):
    """The ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMeasurementActionSavewaveformState(
            device, f"{self._cmd_syntax}:STATE"
        )

    @property
    def state(self) -> ActoneventMeasurementActionSavewaveformState:
        """Return the ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE`` command.

        Description:
            - This command saves the user set source waveform(s) when the user-set measurement limit
              is exceeded.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE?
            ```

        Info:
            - ``ON`` enables the save source waveform(s) when the measurement limit is exceeded
              feature.
            - ``OFF`` disables the save source waveform(s) when the measurement limit is exceeded
              feature.
            - ``<NR1>`` is a number that enables or disables the save source waveform(s) when the
              measurement limit is exceeded feature. The number zero disables the feature, all other
              numbers enable the feature.
        """
        return self._state


class ActoneventMeasurementActionSaveimageState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE`` command.

    Description:
        - This command saves a screen capture when the user-set measurement limit is exceeded.

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE?
        ```

    Info:
        - ``ON`` enables the save screen capture when the measurement limit is exceeded feature.
        - ``OFF`` disables the save screen capture when the measurement limit is exceeded feature.
        - ``<NR1>`` is a number that enables or disables the save screen capture when the
          measurement limit is exceeded feature. The number zero disables the feature, all other
          numbers enable the feature.
    """


class ActoneventMeasurementActionSaveimage(SCPICmdRead):
    """The ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMeasurementActionSaveimageState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMeasurementActionSaveimageState:
        """Return the ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE`` command.

        Description:
            - This command saves a screen capture when the user-set measurement limit is exceeded.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE?
            ```

        Info:
            - ``ON`` enables the save screen capture when the measurement limit is exceeded feature.
            - ``OFF`` disables the save screen capture when the measurement limit is exceeded
              feature.
            - ``<NR1>`` is a number that enables or disables the save screen capture when the
              measurement limit is exceeded feature. The number zero disables the feature, all other
              numbers enable the feature.
        """
        return self._state


class ActoneventMeasurementAction(SCPICmdRead):
    """The ``ACTONEVent:MEASUrement:ACTION`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MEASUrement:ACTION?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MEASUrement:ACTION?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.saveimage``: The ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe`` command tree.
        - ``.savewaveform``: The ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform`` command tree.
        - ``.srq``: The ``ACTONEVent:MEASUrement:ACTION:SRQ`` command tree.
        - ``.stopacq``: The ``ACTONEVent:MEASUrement:ACTION:STOPACQ`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._saveimage = ActoneventMeasurementActionSaveimage(
            device, f"{self._cmd_syntax}:SAVEIMAGe"
        )
        self._savewaveform = ActoneventMeasurementActionSavewaveform(
            device, f"{self._cmd_syntax}:SAVEWAVEform"
        )
        self._srq = ActoneventMeasurementActionSrq(device, f"{self._cmd_syntax}:SRQ")
        self._stopacq = ActoneventMeasurementActionStopacq(device, f"{self._cmd_syntax}:STOPACQ")

    @property
    def saveimage(self) -> ActoneventMeasurementActionSaveimage:
        """Return the ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe:STATE`` command.
        """
        return self._saveimage

    @property
    def savewaveform(self) -> ActoneventMeasurementActionSavewaveform:
        """Return the ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform:STATE`` command.
        """
        return self._savewaveform

    @property
    def srq(self) -> ActoneventMeasurementActionSrq:
        """Return the ``ACTONEVent:MEASUrement:ACTION:SRQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MEASUrement:ACTION:SRQ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:SRQ?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MEASUrement:ACTION:SRQ:STATE`` command.
        """
        return self._srq

    @property
    def stopacq(self) -> ActoneventMeasurementActionStopacq:
        """Return the ``ACTONEVent:MEASUrement:ACTION:STOPACQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MEASUrement:ACTION:STOPACQ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MEASUrement:ACTION:STOPACQ?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MEASUrement:ACTION:STOPACQ:STATE`` command.
        """
        return self._stopacq


class ActoneventMeasurement(SCPICmdRead):
    """The ``ACTONEVent:MEASUrement`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MEASUrement?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MEASUrement?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.action``: The ``ACTONEVent:MEASUrement:ACTION`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._action = ActoneventMeasurementAction(device, f"{self._cmd_syntax}:ACTION")

    @property
    def action(self) -> ActoneventMeasurementAction:
        """Return the ``ACTONEVent:MEASUrement:ACTION`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MEASUrement:ACTION?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:MEASUrement:ACTION?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.saveimage``: The ``ACTONEVent:MEASUrement:ACTION:SAVEIMAGe`` command tree.
            - ``.savewaveform``: The ``ACTONEVent:MEASUrement:ACTION:SAVEWAVEform`` command tree.
            - ``.srq``: The ``ACTONEVent:MEASUrement:ACTION:SRQ`` command tree.
            - ``.stopacq``: The ``ACTONEVent:MEASUrement:ACTION:STOPACQ`` command tree.
        """
        return self._action


class ActoneventMaskpassActionStopacqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKPass:ACTION:STOPACQ:STATE`` command.

    Description:
        - This command stops acquisitions when a mask test passes.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION:STOPACQ:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKPass:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKPass:ACTION:STOPACQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKPass:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKPass:ACTION:STOPACQ:STATE?
        ```

    Info:
        - ``ON`` enables the stop acquisitions when a mask test passes feature.
        - ``OFF`` disables the stop acquisitions when a mask test passes feature.
        - ``<NR1>`` is a number that enables or disables the stop acquisitions when a mask test
          passes feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventMaskpassActionStopacq(SCPICmdRead):
    """The ``ACTONEVent:MASKPass:ACTION:STOPACQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION:STOPACQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKPass:ACTION:STOPACQ?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKPass:ACTION:STOPACQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskpassActionStopacqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskpassActionStopacqState:
        """Return the ``ACTONEVent:MASKPass:ACTION:STOPACQ:STATE`` command.

        Description:
            - This command stops acquisitions when a mask test passes.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKPass:ACTION:STOPACQ:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKPass:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKPass:ACTION:STOPACQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKPass:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKPass:ACTION:STOPACQ:STATE?
            ```

        Info:
            - ``ON`` enables the stop acquisitions when a mask test passes feature.
            - ``OFF`` disables the stop acquisitions when a mask test passes feature.
            - ``<NR1>`` is a number that enables or disables the stop acquisitions when a mask test
              passes feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventMaskpassActionSrqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKPass:ACTION:SRQ:STATE`` command.

    Description:
        - This command generates an SRQ event when a mask passes.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION:SRQ:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKPass:ACTION:SRQ:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKPass:ACTION:SRQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKPass:ACTION:SRQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKPass:ACTION:SRQ:STATE?
        ```

    Info:
        - ``ON`` enables the generate an SRQ event when a mask passes feature.
        - ``OFF`` disables the generate an SRQ event when a mask passes feature.
        - ``<NR1>`` is a number that enables or disables the generate an SRQ event when a mask
          passes feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventMaskpassActionSrq(SCPICmdRead):
    """The ``ACTONEVent:MASKPass:ACTION:SRQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKPass:ACTION:SRQ?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKPass:ACTION:SRQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskpassActionSrqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskpassActionSrqState:
        """Return the ``ACTONEVent:MASKPass:ACTION:SRQ:STATE`` command.

        Description:
            - This command generates an SRQ event when a mask passes.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION:SRQ:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKPass:ACTION:SRQ:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKPass:ACTION:SRQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKPass:ACTION:SRQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKPass:ACTION:SRQ:STATE?
            ```

        Info:
            - ``ON`` enables the generate an SRQ event when a mask passes feature.
            - ``OFF`` disables the generate an SRQ event when a mask passes feature.
            - ``<NR1>`` is a number that enables or disables the generate an SRQ event when a mask
              passes feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventMaskpassActionSavewaveformState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE`` command.

    Description:
        - This command saves the user set source waveform(s) when a mask test passes.

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE?
        ```

    Info:
        - ``ON`` enables the save source waveform(s) when a mask test passes feature.
        - ``OFF`` disables the save source waveform(s) when a mask test passes feature.
        - ``<NR1>`` is a number that enables or disables the save source waveform(s) when a mask
          test passes feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventMaskpassActionSavewaveform(SCPICmdRead):
    """The ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskpassActionSavewaveformState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskpassActionSavewaveformState:
        """Return the ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE`` command.

        Description:
            - This command saves the user set source waveform(s) when a mask test passes.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE?
            ```

        Info:
            - ``ON`` enables the save source waveform(s) when a mask test passes feature.
            - ``OFF`` disables the save source waveform(s) when a mask test passes feature.
            - ``<NR1>`` is a number that enables or disables the save source waveform(s) when a mask
              test passes feature. The number zero disables the feature, all other numbers enable
              the feature.
        """
        return self._state


class ActoneventMaskpassActionSaveimageState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE`` command.

    Description:
        - This command saves a screen capture when a mask test passes.

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE?
        ```

    Info:
        - ``ON`` enables the save screen capture when a mask test passes feature.
        - ``OFF`` disables the save screen capture when a mask test passes feature.
        - ``<NR1>`` is a number that enables or disables the save screen capture when a mask test
          passes feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventMaskpassActionSaveimage(SCPICmdRead):
    """The ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskpassActionSaveimageState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskpassActionSaveimageState:
        """Return the ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE`` command.

        Description:
            - This command saves a screen capture when a mask test passes.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE?
            ```

        Info:
            - ``ON`` enables the save screen capture when a mask test passes feature.
            - ``OFF`` disables the save screen capture when a mask test passes feature.
            - ``<NR1>`` is a number that enables or disables the save screen capture when a mask
              test passes feature. The number zero disables the feature, all other numbers enable
              the feature.
        """
        return self._state


class ActoneventMaskpassAction(SCPICmdRead):
    """The ``ACTONEVent:MASKPass:ACTION`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKPass:ACTION?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.saveimage``: The ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe`` command tree.
        - ``.savewaveform``: The ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform`` command tree.
        - ``.srq``: The ``ACTONEVent:MASKPass:ACTION:SRQ`` command tree.
        - ``.stopacq``: The ``ACTONEVent:MASKPass:ACTION:STOPACQ`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._saveimage = ActoneventMaskpassActionSaveimage(device, f"{self._cmd_syntax}:SAVEIMAGe")
        self._savewaveform = ActoneventMaskpassActionSavewaveform(
            device, f"{self._cmd_syntax}:SAVEWAVEform"
        )
        self._srq = ActoneventMaskpassActionSrq(device, f"{self._cmd_syntax}:SRQ")
        self._stopacq = ActoneventMaskpassActionStopacq(device, f"{self._cmd_syntax}:STOPACQ")

    @property
    def saveimage(self) -> ActoneventMaskpassActionSaveimage:
        """Return the ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe:STATE`` command.
        """
        return self._saveimage

    @property
    def savewaveform(self) -> ActoneventMaskpassActionSavewaveform:
        """Return the ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform:STATE`` command.
        """
        return self._savewaveform

    @property
    def srq(self) -> ActoneventMaskpassActionSrq:
        """Return the ``ACTONEVent:MASKPass:ACTION:SRQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION:SRQ?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKPass:ACTION:SRQ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKPass:ACTION:SRQ:STATE`` command.
        """
        return self._srq

    @property
    def stopacq(self) -> ActoneventMaskpassActionStopacq:
        """Return the ``ACTONEVent:MASKPass:ACTION:STOPACQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION:STOPACQ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKPass:ACTION:STOPACQ?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKPass:ACTION:STOPACQ:STATE`` command.
        """
        return self._stopacq


class ActoneventMaskpass(SCPICmdRead):
    """The ``ACTONEVent:MASKPass`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKPass?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.action``: The ``ACTONEVent:MASKPass:ACTION`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._action = ActoneventMaskpassAction(device, f"{self._cmd_syntax}:ACTION")

    @property
    def action(self) -> ActoneventMaskpassAction:
        """Return the ``ACTONEVent:MASKPass:ACTION`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass:ACTION?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKPass:ACTION?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.saveimage``: The ``ACTONEVent:MASKPass:ACTION:SAVEIMAGe`` command tree.
            - ``.savewaveform``: The ``ACTONEVent:MASKPass:ACTION:SAVEWAVEform`` command tree.
            - ``.srq``: The ``ACTONEVent:MASKPass:ACTION:SRQ`` command tree.
            - ``.stopacq``: The ``ACTONEVent:MASKPass:ACTION:STOPACQ`` command tree.
        """
        return self._action


class ActoneventMaskhitActionStopacqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKHit:ACTION:STOPACQ:STATE`` command.

    Description:
        - This command stops acquisitions when a mask hit occurs.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION:STOPACQ:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKHit:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKHit:ACTION:STOPACQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKHit:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKHit:ACTION:STOPACQ:STATE?
        ```

    Info:
        - ``ON`` enables the stop acquisitions when a mask hit occurs feature.
        - ``OFF`` disables the stop acquisitions when a mask hit occurs feature.
        - ``<NR1>`` is a number that enables or disables the stop acquisitions when a mask hit
          occurs feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventMaskhitActionStopacq(SCPICmdRead):
    """The ``ACTONEVent:MASKHit:ACTION:STOPACQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION:STOPACQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKHit:ACTION:STOPACQ?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKHit:ACTION:STOPACQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskhitActionStopacqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskhitActionStopacqState:
        """Return the ``ACTONEVent:MASKHit:ACTION:STOPACQ:STATE`` command.

        Description:
            - This command stops acquisitions when a mask hit occurs.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKHit:ACTION:STOPACQ:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKHit:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKHit:ACTION:STOPACQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKHit:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKHit:ACTION:STOPACQ:STATE?
            ```

        Info:
            - ``ON`` enables the stop acquisitions when a mask hit occurs feature.
            - ``OFF`` disables the stop acquisitions when a mask hit occurs feature.
            - ``<NR1>`` is a number that enables or disables the stop acquisitions when a mask hit
              occurs feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventMaskhitActionSrqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKHit:ACTION:SRQ:STATE`` command.

    Description:
        - This command generates an SRQ event when a mask hit occurs.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION:SRQ:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKHit:ACTION:SRQ:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKHit:ACTION:SRQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKHit:ACTION:SRQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKHit:ACTION:SRQ:STATE?
        ```

    Info:
        - ``ON`` enables the generate an SRQ event when a mask hit occurs feature.
        - ``OFF`` disables the generate an SRQ event when a mask hit occurs feature.
        - ``<NR1>`` is a number that enables or disables the generate an SRQ event when a mask hit
          occurs feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventMaskhitActionSrq(SCPICmdRead):
    """The ``ACTONEVent:MASKHit:ACTION:SRQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKHit:ACTION:SRQ?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKHit:ACTION:SRQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskhitActionSrqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskhitActionSrqState:
        """Return the ``ACTONEVent:MASKHit:ACTION:SRQ:STATE`` command.

        Description:
            - This command generates an SRQ event when a mask hit occurs.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION:SRQ:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKHit:ACTION:SRQ:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKHit:ACTION:SRQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKHit:ACTION:SRQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKHit:ACTION:SRQ:STATE?
            ```

        Info:
            - ``ON`` enables the generate an SRQ event when a mask hit occurs feature.
            - ``OFF`` disables the generate an SRQ event when a mask hit occurs feature.
            - ``<NR1>`` is a number that enables or disables the generate an SRQ event when a mask
              hit occurs feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventMaskhitActionSavewaveformState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE`` command.

    Description:
        - This command saves the user set source waveform(s) when a mask hit occurs.

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE?
        ```

    Info:
        - ``ON`` enables the save source waveform(s) when a mask hit occurs feature.
        - ``OFF`` disables the save source waveform(s) when a mask hit occurs feature.
        - ``<NR1>`` is a number that enables or disables the save source waveform(s) when a mask hit
          occurs feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventMaskhitActionSavewaveform(SCPICmdRead):
    """The ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskhitActionSavewaveformState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskhitActionSavewaveformState:
        """Return the ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE`` command.

        Description:
            - This command saves the user set source waveform(s) when a mask hit occurs.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE?
            ```

        Info:
            - ``ON`` enables the save source waveform(s) when a mask hit occurs feature.
            - ``OFF`` disables the save source waveform(s) when a mask hit occurs feature.
            - ``<NR1>`` is a number that enables or disables the save source waveform(s) when a mask
              hit occurs feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventMaskhitActionSaveimageState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE`` command.

    Description:
        - This command saves a screen capture when a mask hit occurs.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE?
        ```

    Info:
        - ``ON`` enables the save screen capture when a mask hit occurs feature.
        - ``OFF`` disables the save screen capture when a mask hit occurs feature.
        - ``<NR1>`` is a number that enables or disables the save screen capture when a mask hit
          occurs feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventMaskhitActionSaveimage(SCPICmdRead):
    """The ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe?``
          query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskhitActionSaveimageState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskhitActionSaveimageState:
        """Return the ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE`` command.

        Description:
            - This command saves a screen capture when a mask hit occurs.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE?
            ```

        Info:
            - ``ON`` enables the save screen capture when a mask hit occurs feature.
            - ``OFF`` disables the save screen capture when a mask hit occurs feature.
            - ``<NR1>`` is a number that enables or disables the save screen capture when a mask hit
              occurs feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventMaskhitAction(SCPICmdRead):
    """The ``ACTONEVent:MASKHit:ACTION`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKHit:ACTION?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.saveimage``: The ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe`` command tree.
        - ``.savewaveform``: The ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform`` command tree.
        - ``.srq``: The ``ACTONEVent:MASKHit:ACTION:SRQ`` command tree.
        - ``.stopacq``: The ``ACTONEVent:MASKHit:ACTION:STOPACQ`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._saveimage = ActoneventMaskhitActionSaveimage(device, f"{self._cmd_syntax}:SAVEIMAGe")
        self._savewaveform = ActoneventMaskhitActionSavewaveform(
            device, f"{self._cmd_syntax}:SAVEWAVEform"
        )
        self._srq = ActoneventMaskhitActionSrq(device, f"{self._cmd_syntax}:SRQ")
        self._stopacq = ActoneventMaskhitActionStopacq(device, f"{self._cmd_syntax}:STOPACQ")

    @property
    def saveimage(self) -> ActoneventMaskhitActionSaveimage:
        """Return the ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe:STATE`` command.
        """
        return self._saveimage

    @property
    def savewaveform(self) -> ActoneventMaskhitActionSavewaveform:
        """Return the ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform:STATE`` command.
        """
        return self._savewaveform

    @property
    def srq(self) -> ActoneventMaskhitActionSrq:
        """Return the ``ACTONEVent:MASKHit:ACTION:SRQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION:SRQ?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKHit:ACTION:SRQ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKHit:ACTION:SRQ:STATE`` command.
        """
        return self._srq

    @property
    def stopacq(self) -> ActoneventMaskhitActionStopacq:
        """Return the ``ACTONEVent:MASKHit:ACTION:STOPACQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION:STOPACQ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKHit:ACTION:STOPACQ?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKHit:ACTION:STOPACQ:STATE`` command.
        """
        return self._stopacq


class ActoneventMaskhit(SCPICmdRead):
    """The ``ACTONEVent:MASKHit`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKHit?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.action``: The ``ACTONEVent:MASKHit:ACTION`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._action = ActoneventMaskhitAction(device, f"{self._cmd_syntax}:ACTION")

    @property
    def action(self) -> ActoneventMaskhitAction:
        """Return the ``ACTONEVent:MASKHit:ACTION`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit:ACTION?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKHit:ACTION?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.saveimage``: The ``ACTONEVent:MASKHit:ACTION:SAVEIMAGe`` command tree.
            - ``.savewaveform``: The ``ACTONEVent:MASKHit:ACTION:SAVEWAVEform`` command tree.
            - ``.srq``: The ``ACTONEVent:MASKHit:ACTION:SRQ`` command tree.
            - ``.stopacq``: The ``ACTONEVent:MASKHit:ACTION:STOPACQ`` command tree.
        """
        return self._action


class ActoneventMaskfailActionStopacqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKFail:ACTION:STOPACQ:STATE`` command.

    Description:
        - This command stops acquisitions when a mask test fails.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION:STOPACQ:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKFail:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKFail:ACTION:STOPACQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKFail:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKFail:ACTION:STOPACQ:STATE?
        ```

    Info:
        - ``ON`` enables the stop acquisitions when a mask test fails feature.
        - ``OFF`` disables the stop acquisitions when a mask test fails feature.
        - ``<NR1>`` is a number that enables or disables the stop acquisitions when a mask test
          fails feature. The number zero disables the feature, all other numbers enable the feature.
    """


class ActoneventMaskfailActionStopacq(SCPICmdRead):
    """The ``ACTONEVent:MASKFail:ACTION:STOPACQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION:STOPACQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKFail:ACTION:STOPACQ?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKFail:ACTION:STOPACQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskfailActionStopacqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskfailActionStopacqState:
        """Return the ``ACTONEVent:MASKFail:ACTION:STOPACQ:STATE`` command.

        Description:
            - This command stops acquisitions when a mask test fails.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKFail:ACTION:STOPACQ:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKFail:ACTION:STOPACQ:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKFail:ACTION:STOPACQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKFail:ACTION:STOPACQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKFail:ACTION:STOPACQ:STATE?
            ```

        Info:
            - ``ON`` enables the stop acquisitions when a mask test fails feature.
            - ``OFF`` disables the stop acquisitions when a mask test fails feature.
            - ``<NR1>`` is a number that enables or disables the stop acquisitions when a mask test
              fails feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventMaskfailActionSrqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKFail:ACTION:SRQ:STATE`` command.

    Description:
        - This command generates an SRQ event when a mask fails.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION:SRQ:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKFail:ACTION:SRQ:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKFail:ACTION:SRQ:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKFail:ACTION:SRQ:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKFail:ACTION:SRQ:STATE?
        ```

    Info:
        - ``ON`` enables the generate an SRQ event when a mask fails feature.
        - ``OFF`` disables the generate an SRQ event when a mask fails feature.
        - ``<NR1>`` is a number that enables or disables the generate an SRQ event when a mask fails
          feature. The number zero disables the feature, all other numbers enable the feature.
    """


class ActoneventMaskfailActionSrq(SCPICmdRead):
    """The ``ACTONEVent:MASKFail:ACTION:SRQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKFail:ACTION:SRQ?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKFail:ACTION:SRQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskfailActionSrqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskfailActionSrqState:
        """Return the ``ACTONEVent:MASKFail:ACTION:SRQ:STATE`` command.

        Description:
            - This command generates an SRQ event when a mask fails.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION:SRQ:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKFail:ACTION:SRQ:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKFail:ACTION:SRQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKFail:ACTION:SRQ:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKFail:ACTION:SRQ:STATE?
            ```

        Info:
            - ``ON`` enables the generate an SRQ event when a mask fails feature.
            - ``OFF`` disables the generate an SRQ event when a mask fails feature.
            - ``<NR1>`` is a number that enables or disables the generate an SRQ event when a mask
              fails feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventMaskfailActionSavewaveformState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE`` command.

    Description:
        - This command saves the user set source waveform(s) when a mask test fails.

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE?
        ```

    Info:
        - ``ON`` enables the save source waveform(s) when a mask test fails feature.
        - ``OFF`` disables the save source waveform(s) when a mask test fails feature.
        - ``<NR1>`` is a number that enables or disables the save source waveform(s) when a mask
          test fails feature. The number zero disables the feature, all other numbers enable the
          feature.
    """


class ActoneventMaskfailActionSavewaveform(SCPICmdRead):
    """The ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskfailActionSavewaveformState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskfailActionSavewaveformState:
        """Return the ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE`` command.

        Description:
            - This command saves the user set source waveform(s) when a mask test fails.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE?
            ```

        Info:
            - ``ON`` enables the save source waveform(s) when a mask test fails feature.
            - ``OFF`` disables the save source waveform(s) when a mask test fails feature.
            - ``<NR1>`` is a number that enables or disables the save source waveform(s) when a mask
              test fails feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventMaskfailActionSaveimageState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE`` command.

    Description:
        - This command saves a screen capture when a mask test fails.

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
        - ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE?
        ```

    Info:
        - ``ON`` enables the save screen capture when a mask test fails feature.
        - ``OFF`` disables the save screen capture when a mask test fails feature.
        - ``<NR1>`` is a number that enables or disables the save screen capture when a mask test
          fails feature. The number zero disables the feature, all other numbers enable the feature.
    """


class ActoneventMaskfailActionSaveimage(SCPICmdRead):
    """The ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventMaskfailActionSaveimageState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventMaskfailActionSaveimageState:
        """Return the ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE`` command.

        Description:
            - This command saves a screen capture when a mask test fails.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
            - ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE?
            ```

        Info:
            - ``ON`` enables the save screen capture when a mask test fails feature.
            - ``OFF`` disables the save screen capture when a mask test fails feature.
            - ``<NR1>`` is a number that enables or disables the save screen capture when a mask
              test fails feature. The number zero disables the feature, all other numbers enable the
              feature.
        """
        return self._state


class ActoneventMaskfailAction(SCPICmdRead):
    """The ``ACTONEVent:MASKFail:ACTION`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKFail:ACTION?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.saveimage``: The ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe`` command tree.
        - ``.savewaveform``: The ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform`` command tree.
        - ``.srq``: The ``ACTONEVent:MASKFail:ACTION:SRQ`` command tree.
        - ``.stopacq``: The ``ACTONEVent:MASKFail:ACTION:STOPACQ`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._saveimage = ActoneventMaskfailActionSaveimage(device, f"{self._cmd_syntax}:SAVEIMAGe")
        self._savewaveform = ActoneventMaskfailActionSavewaveform(
            device, f"{self._cmd_syntax}:SAVEWAVEform"
        )
        self._srq = ActoneventMaskfailActionSrq(device, f"{self._cmd_syntax}:SRQ")
        self._stopacq = ActoneventMaskfailActionStopacq(device, f"{self._cmd_syntax}:STOPACQ")

    @property
    def saveimage(self) -> ActoneventMaskfailActionSaveimage:
        """Return the ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe:STATE`` command.
        """
        return self._saveimage

    @property
    def savewaveform(self) -> ActoneventMaskfailActionSavewaveform:
        """Return the ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform:STATE`` command.
        """
        return self._savewaveform

    @property
    def srq(self) -> ActoneventMaskfailActionSrq:
        """Return the ``ACTONEVent:MASKFail:ACTION:SRQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION:SRQ?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKFail:ACTION:SRQ?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKFail:ACTION:SRQ:STATE`` command.
        """
        return self._srq

    @property
    def stopacq(self) -> ActoneventMaskfailActionStopacq:
        """Return the ``ACTONEVent:MASKFail:ACTION:STOPACQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION:STOPACQ?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:MASKFail:ACTION:STOPACQ?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:MASKFail:ACTION:STOPACQ:STATE`` command.
        """
        return self._stopacq


class ActoneventMaskfail(SCPICmdRead):
    """The ``ACTONEVent:MASKFail`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKFail?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.action``: The ``ACTONEVent:MASKFail:ACTION`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._action = ActoneventMaskfailAction(device, f"{self._cmd_syntax}:ACTION")

    @property
    def action(self) -> ActoneventMaskfailAction:
        """Return the ``ACTONEVent:MASKFail:ACTION`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail:ACTION?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKFail:ACTION?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.saveimage``: The ``ACTONEVent:MASKFail:ACTION:SAVEIMAGe`` command tree.
            - ``.savewaveform``: The ``ACTONEVent:MASKFail:ACTION:SAVEWAVEform`` command tree.
            - ``.srq``: The ``ACTONEVent:MASKFail:ACTION:SRQ`` command tree.
            - ``.stopacq``: The ``ACTONEVent:MASKFail:ACTION:STOPACQ`` command tree.
        """
        return self._action


class ActoneventLimit(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:LIMit`` command.

    Description:
        - This command sets whether the act on event should limit the number of saves. This prevents
          the saves from filling the hard drive.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:LIMit?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:LIMit?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:LIMit value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:LIMit <NR1>
        - ACTONEVent:LIMit?
        ```

    Info:
        - ``<NR1>`` is a number that enables or disables whether the act on event should limit the
          number of saves. The number zero disables the feature and the number one enables the
          feature.
    """


class ActoneventLimitcount(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:LIMITCount`` command.

    Description:
        - This command sets the limit of act on even saves. The ``ACTONEVent:LIMit`` command must be
          enabled.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:LIMITCount?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:LIMITCount?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:LIMITCount value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:LIMITCount <NR1>
        - ACTONEVent:LIMITCount?
        ```

    Info:
        - ``<NR1>`` sets the number of allowed saves for the act on event feature. The number must
          be a positive integer.
    """


class ActoneventEnable(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:ENable`` command.

    Description:
        - This command enables or disables actions on event (AOE). If AOE saves are limited and the
          limit has been reached, this parameter will disable AOE.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ENable?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ENable?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:ENable value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:ENable <NR1>
        - ACTONEVent:ENable?
        ```

    Info:
        - ``<NR1>`` is a number that enables or disables actions on event. The number zero disables
          the feature and the number one enables the feature.
    """


#  pylint: disable=too-many-instance-attributes
class Actonevent(SCPICmdRead):
    """The ``ACTONEVent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``ACTONEVent:ENable`` command.
        - ``.limitcount``: The ``ACTONEVent:LIMITCount`` command.
        - ``.limit``: The ``ACTONEVent:LIMit`` command.
        - ``.maskfail``: The ``ACTONEVent:MASKFail`` command tree.
        - ``.maskhit``: The ``ACTONEVent:MASKHit`` command tree.
        - ``.maskpass``: The ``ACTONEVent:MASKPass`` command tree.
        - ``.measurement``: The ``ACTONEVent:MEASUrement`` command tree.
        - ``.search``: The ``ACTONEVent:SEARCH`` command tree.
        - ``.trigger``: The ``ACTONEVent:TRIGger`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "ACTONEVent"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = ActoneventEnable(device, f"{self._cmd_syntax}:ENable")
        self._limitcount = ActoneventLimitcount(device, f"{self._cmd_syntax}:LIMITCount")
        self._limit = ActoneventLimit(device, f"{self._cmd_syntax}:LIMit")
        self._maskfail = ActoneventMaskfail(device, f"{self._cmd_syntax}:MASKFail")
        self._maskhit = ActoneventMaskhit(device, f"{self._cmd_syntax}:MASKHit")
        self._maskpass = ActoneventMaskpass(device, f"{self._cmd_syntax}:MASKPass")
        self._measurement = ActoneventMeasurement(device, f"{self._cmd_syntax}:MEASUrement")
        self._search = ActoneventSearch(device, f"{self._cmd_syntax}:SEARCH")
        self._trigger = ActoneventTrigger(device, f"{self._cmd_syntax}:TRIGger")

    @property
    def enable(self) -> ActoneventEnable:
        """Return the ``ACTONEVent:ENable`` command.

        Description:
            - This command enables or disables actions on event (AOE). If AOE saves are limited and
              the limit has been reached, this parameter will disable AOE.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ENable?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ENable?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACTONEVent:ENable value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:ENable <NR1>
            - ACTONEVent:ENable?
            ```

        Info:
            - ``<NR1>`` is a number that enables or disables actions on event. The number zero
              disables the feature and the number one enables the feature.
        """
        return self._enable

    @property
    def limitcount(self) -> ActoneventLimitcount:
        """Return the ``ACTONEVent:LIMITCount`` command.

        Description:
            - This command sets the limit of act on even saves. The ``ACTONEVent:LIMit`` command
              must be enabled.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:LIMITCount?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:LIMITCount?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACTONEVent:LIMITCount value``
              command.

        SCPI Syntax:
            ```
            - ACTONEVent:LIMITCount <NR1>
            - ACTONEVent:LIMITCount?
            ```

        Info:
            - ``<NR1>`` sets the number of allowed saves for the act on event feature. The number
              must be a positive integer.
        """
        return self._limitcount

    @property
    def limit(self) -> ActoneventLimit:
        """Return the ``ACTONEVent:LIMit`` command.

        Description:
            - This command sets whether the act on event should limit the number of saves. This
              prevents the saves from filling the hard drive.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:LIMit?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:LIMit?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACTONEVent:LIMit value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:LIMit <NR1>
            - ACTONEVent:LIMit?
            ```

        Info:
            - ``<NR1>`` is a number that enables or disables whether the act on event should limit
              the number of saves. The number zero disables the feature and the number one enables
              the feature.
        """
        return self._limit

    @property
    def maskfail(self) -> ActoneventMaskfail:
        """Return the ``ACTONEVent:MASKFail`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKFail?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKFail?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.action``: The ``ACTONEVent:MASKFail:ACTION`` command tree.
        """
        return self._maskfail

    @property
    def maskhit(self) -> ActoneventMaskhit:
        """Return the ``ACTONEVent:MASKHit`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKHit?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKHit?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.action``: The ``ACTONEVent:MASKHit:ACTION`` command tree.
        """
        return self._maskhit

    @property
    def maskpass(self) -> ActoneventMaskpass:
        """Return the ``ACTONEVent:MASKPass`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MASKPass?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:MASKPass?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.action``: The ``ACTONEVent:MASKPass:ACTION`` command tree.
        """
        return self._maskpass

    @property
    def measurement(self) -> ActoneventMeasurement:
        """Return the ``ACTONEVent:MEASUrement`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:MEASUrement?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:MEASUrement?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.action``: The ``ACTONEVent:MEASUrement:ACTION`` command tree.
        """
        return self._measurement

    @property
    def search(self) -> ActoneventSearch:
        """Return the ``ACTONEVent:SEARCH`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:SEARCH?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:SEARCH?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.action``: The ``ACTONEVent:SEARCH:ACTION`` command tree.
        """
        return self._search

    @property
    def trigger(self) -> ActoneventTrigger:
        """Return the ``ACTONEVent:TRIGger`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TRIGger?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:TRIGger?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.action``: The ``ACTONEVent:TRIGger:ACTION`` command tree.
        """
        return self._trigger
