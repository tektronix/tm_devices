"""The actonevent commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ACTONEVent:ENable <NR1>
    - ACTONEVent:ENable?
    - ACTONEVent:NUMSAVEs?
    - ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
    - ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE?
    - ACTONEVent:TIMER:ACTION:SAVETable:STATE {ON|OFF|<NR1>}
    - ACTONEVent:TIMER:ACTION:SAVETable:STATE?
    - ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
    - ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE?
    - ACTONEVent:TIMERCount <NR1>
    - ACTONEVent:TIMERCount?
    - ACTONEVent:TIMERInterval <NR1>
    - ACTONEVent:TIMERInterval?
    - ACTONEVent:Type?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ActoneventType(SCPICmdRead):
    """The ``ACTONEVent:Type`` command.

    Description:
        - This command returns the act on event type.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:Type?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:Type?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ACTONEVent:Type?
        ```
    """


class ActoneventTimerinterval(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:TIMERInterval`` command.

    Description:
        - This command sets or queries the amount of time, in seconds, to wait for act on event
          timer event to trigger. The time can range from a minimum of 10 seconds to a maximum of
          100 seconds. The default is 30 seconds

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TIMERInterval?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TIMERInterval?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:TIMERInterval value``
          command.

    SCPI Syntax:
        ```
        - ACTONEVent:TIMERInterval <NR1>
        - ACTONEVent:TIMERInterval?
        ```

    Info:
        - ``<NR1>`` is the amount of time, in seconds, to wait for act on event timer event to
          trigger.
    """


class ActoneventTimercount(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:TIMERCount`` command.

    Description:
        - This command sets or queries the save on event timer count. The ``ACTONEVent:ENable`` must
          be enabled.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TIMERCount?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TIMERCount?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:TIMERCount value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:TIMERCount <NR1>
        - ACTONEVent:TIMERCount?
        ```

    Info:
        - ``<NR1>`` sets the number of allowed saves for the act on event feature. The number must
          be a positive integer.
    """


class ActoneventTimerActionSavewaveformState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE`` command.

    Description:
        - This command saves the user set source waveform(s) when ``:ACTONEVent:TIMERInterval``
          expires.

    Usage:
        - Using the ``.query()`` method will send the
          ``ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
        - ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE?
        ```

    Info:
        - ``ON`` enables the save source waveform(s) when ``:ACTONEVent:TIMERInterval`` expires.
        - ``OFF`` disables the save source waveform(s) when ``:ACTONEVent:TIMERInterval`` expires.
        - ``<NR1>`` is a number that enables or disables the user set source waveform(s) when
          ``:ACTONEVent:TIMERInterval`` expires. The number zero disables the feature, all other
          numbers enable the feature.
    """


class ActoneventTimerActionSavewaveform(SCPICmdRead):
    """The ``ACTONEVent:TIMER:ACTION:SAVEWAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TIMER:ACTION:SAVEWAVEform?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:TIMER:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventTimerActionSavewaveformState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventTimerActionSavewaveformState:
        """Return the ``ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE`` command.

        Description:
            - This command saves the user set source waveform(s) when ``:ACTONEVent:TIMERInterval``
              expires.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE {ON|OFF|<NR1>}
            - ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE?
            ```

        Info:
            - ``ON`` enables the save source waveform(s) when ``:ACTONEVent:TIMERInterval`` expires.
            - ``OFF`` disables the save source waveform(s) when ``:ACTONEVent:TIMERInterval``
              expires.
            - ``<NR1>`` is a number that enables or disables the user set source waveform(s) when
              ``:ACTONEVent:TIMERInterval`` expires. The number zero disables the feature, all other
              numbers enable the feature.
        """
        return self._state


class ActoneventTimerActionSavetableState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:TIMER:ACTION:SAVETable:STATE`` command.

    Description:
        - This command saves a measurement results when ``:ACTONEVent:TIMERInterval`` expires.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TIMER:ACTION:SAVETable:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:TIMER:ACTION:SAVETable:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:TIMER:ACTION:SAVETable:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:TIMER:ACTION:SAVETable:STATE {ON|OFF|<NR1>}
        - ACTONEVent:TIMER:ACTION:SAVETable:STATE?
        ```

    Info:
        - ``ON`` enables the save measurement results when ``:ACTONEVent:TIMERInterval`` expires.
        - ``OFF`` disables the save measurement results when ``:ACTONEVent:TIMERInterval`` expires.
        - ``<NR1>`` is a number that enables or disables the save measurement results
          ``:ACTONEVent:TIMERInterval`` expires. The number zero disables the feature, all other
          numbers enable the feature.
    """


class ActoneventTimerActionSavetable(SCPICmdRead):
    """The ``ACTONEVent:TIMER:ACTION:SAVETable`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TIMER:ACTION:SAVETable?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TIMER:ACTION:SAVETable?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:TIMER:ACTION:SAVETable:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventTimerActionSavetableState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventTimerActionSavetableState:
        """Return the ``ACTONEVent:TIMER:ACTION:SAVETable:STATE`` command.

        Description:
            - This command saves a measurement results when ``:ACTONEVent:TIMERInterval`` expires.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVETable:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVETable:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVETable:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:TIMER:ACTION:SAVETable:STATE {ON|OFF|<NR1>}
            - ACTONEVent:TIMER:ACTION:SAVETable:STATE?
            ```

        Info:
            - ``ON`` enables the save measurement results when ``:ACTONEVent:TIMERInterval``
              expires.
            - ``OFF`` disables the save measurement results when ``:ACTONEVent:TIMERInterval``
              expires.
            - ``<NR1>`` is a number that enables or disables the save measurement results
              ``:ACTONEVent:TIMERInterval`` expires. The number zero disables the feature, all other
              numbers enable the feature.
        """
        return self._state


class ActoneventTimerActionSaveimageState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE`` command.

    Description:
        - This command saves a screen capture when ``:ACTONEVent:TIMERInterval`` expires.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
        - ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE?
        ```

    Info:
        - ``ON`` enables the save screen capture when ``:ACTONEVent:TIMERInterval`` expires.
        - ``OFF`` disables the save screen capture when ``:ACTONEVent:TIMERInterval`` expires.
        - ``<NR1>`` is a number that enables or disables the save screen capture
          ``:ACTONEVent:TIMERInterval`` expires. The number zero disables the feature, all other
          numbers enable the feature.
    """


class ActoneventTimerActionSaveimage(SCPICmdRead):
    """The ``ACTONEVent:TIMER:ACTION:SAVEIMAGe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TIMER:ACTION:SAVEIMAGe?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TIMER:ACTION:SAVEIMAGe?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventTimerActionSaveimageState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventTimerActionSaveimageState:
        """Return the ``ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE`` command.

        Description:
            - This command saves a screen capture when ``:ACTONEVent:TIMERInterval`` expires.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE {ON|OFF|<NR1>}
            - ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE?
            ```

        Info:
            - ``ON`` enables the save screen capture when ``:ACTONEVent:TIMERInterval`` expires.
            - ``OFF`` disables the save screen capture when ``:ACTONEVent:TIMERInterval`` expires.
            - ``<NR1>`` is a number that enables or disables the save screen capture
              ``:ACTONEVent:TIMERInterval`` expires. The number zero disables the feature, all other
              numbers enable the feature.
        """
        return self._state


class ActoneventTimerAction(SCPICmdRead):
    """The ``ACTONEVent:TIMER:ACTION`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TIMER:ACTION?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TIMER:ACTION?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.saveimage``: The ``ACTONEVent:TIMER:ACTION:SAVEIMAGe`` command tree.
        - ``.savetable``: The ``ACTONEVent:TIMER:ACTION:SAVETable`` command tree.
        - ``.savewaveform``: The ``ACTONEVent:TIMER:ACTION:SAVEWAVEform`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._saveimage = ActoneventTimerActionSaveimage(device, f"{self._cmd_syntax}:SAVEIMAGe")
        self._savetable = ActoneventTimerActionSavetable(device, f"{self._cmd_syntax}:SAVETable")
        self._savewaveform = ActoneventTimerActionSavewaveform(
            device, f"{self._cmd_syntax}:SAVEWAVEform"
        )

    @property
    def saveimage(self) -> ActoneventTimerActionSaveimage:
        """Return the ``ACTONEVent:TIMER:ACTION:SAVEIMAGe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TIMER:ACTION:SAVEIMAGe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVEIMAGe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:TIMER:ACTION:SAVEIMAGe:STATE`` command.
        """
        return self._saveimage

    @property
    def savetable(self) -> ActoneventTimerActionSavetable:
        """Return the ``ACTONEVent:TIMER:ACTION:SAVETable`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TIMER:ACTION:SAVETable?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVETable?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:TIMER:ACTION:SAVETable:STATE`` command.
        """
        return self._savetable

    @property
    def savewaveform(self) -> ActoneventTimerActionSavewaveform:
        """Return the ``ACTONEVent:TIMER:ACTION:SAVEWAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TIMER:ACTION:SAVEWAVEform?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:TIMER:ACTION:SAVEWAVEform?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:TIMER:ACTION:SAVEWAVEform:STATE`` command.
        """
        return self._savewaveform


class ActoneventTimer(SCPICmdRead):
    """The ``ACTONEVent:TIMER`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:TIMER?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:TIMER?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.action``: The ``ACTONEVent:TIMER:ACTION`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._action = ActoneventTimerAction(device, f"{self._cmd_syntax}:ACTION")

    @property
    def action(self) -> ActoneventTimerAction:
        """Return the ``ACTONEVent:TIMER:ACTION`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TIMER:ACTION?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:TIMER:ACTION?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.saveimage``: The ``ACTONEVent:TIMER:ACTION:SAVEIMAGe`` command tree.
            - ``.savetable``: The ``ACTONEVent:TIMER:ACTION:SAVETable`` command tree.
            - ``.savewaveform``: The ``ACTONEVent:TIMER:ACTION:SAVEWAVEform`` command tree.
        """
        return self._action


class ActoneventNumsaves(SCPICmdRead):
    """The ``ACTONEVent:NUMSAVEs`` command.

    Description:
        - This command returns the number of saves completed for save on event timer type.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:NUMSAVEs?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:NUMSAVEs?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ACTONEVent:NUMSAVEs?
        ```
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


class Actonevent(SCPICmdRead):
    """The ``ACTONEVent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``ACTONEVent:ENable`` command.
        - ``.numsaves``: The ``ACTONEVent:NUMSAVEs`` command.
        - ``.timer``: The ``ACTONEVent:TIMER`` command tree.
        - ``.timercount``: The ``ACTONEVent:TIMERCount`` command.
        - ``.timerinterval``: The ``ACTONEVent:TIMERInterval`` command.
        - ``.type``: The ``ACTONEVent:Type`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "ACTONEVent"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = ActoneventEnable(device, f"{self._cmd_syntax}:ENable")
        self._numsaves = ActoneventNumsaves(device, f"{self._cmd_syntax}:NUMSAVEs")
        self._timer = ActoneventTimer(device, f"{self._cmd_syntax}:TIMER")
        self._timercount = ActoneventTimercount(device, f"{self._cmd_syntax}:TIMERCount")
        self._timerinterval = ActoneventTimerinterval(device, f"{self._cmd_syntax}:TIMERInterval")
        self._type = ActoneventType(device, f"{self._cmd_syntax}:Type")

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
    def numsaves(self) -> ActoneventNumsaves:
        """Return the ``ACTONEVent:NUMSAVEs`` command.

        Description:
            - This command returns the number of saves completed for save on event timer type.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:NUMSAVEs?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:NUMSAVEs?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ACTONEVent:NUMSAVEs?
            ```
        """
        return self._numsaves

    @property
    def timer(self) -> ActoneventTimer:
        """Return the ``ACTONEVent:TIMER`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TIMER?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:TIMER?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.action``: The ``ACTONEVent:TIMER:ACTION`` command tree.
        """
        return self._timer

    @property
    def timercount(self) -> ActoneventTimercount:
        """Return the ``ACTONEVent:TIMERCount`` command.

        Description:
            - This command sets or queries the save on event timer count. The ``ACTONEVent:ENable``
              must be enabled.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TIMERCount?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:TIMERCount?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACTONEVent:TIMERCount value``
              command.

        SCPI Syntax:
            ```
            - ACTONEVent:TIMERCount <NR1>
            - ACTONEVent:TIMERCount?
            ```

        Info:
            - ``<NR1>`` sets the number of allowed saves for the act on event feature. The number
              must be a positive integer.
        """
        return self._timercount

    @property
    def timerinterval(self) -> ActoneventTimerinterval:
        """Return the ``ACTONEVent:TIMERInterval`` command.

        Description:
            - This command sets or queries the amount of time, in seconds, to wait for act on event
              timer event to trigger. The time can range from a minimum of 10 seconds to a maximum
              of 100 seconds. The default is 30 seconds

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:TIMERInterval?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:TIMERInterval?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACTONEVent:TIMERInterval value``
              command.

        SCPI Syntax:
            ```
            - ACTONEVent:TIMERInterval <NR1>
            - ACTONEVent:TIMERInterval?
            ```

        Info:
            - ``<NR1>`` is the amount of time, in seconds, to wait for act on event timer event to
              trigger.
        """
        return self._timerinterval

    @property
    def type(self) -> ActoneventType:
        """Return the ``ACTONEVent:Type`` command.

        Description:
            - This command returns the act on event type.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:Type?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:Type?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ACTONEVent:Type?
            ```
        """
        return self._type
